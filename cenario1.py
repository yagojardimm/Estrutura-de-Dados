import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager # Para verificar fontes
import matplotlib.animation as animation # Importar o módulo de animação

# --- DEFINIÇÕES DE CORES INSPIRADAS NA IMAGEM DE REFERÊNCIA E NO TEMA ---
COLOR_NODE_DEFAULT = '#67E8F9' 
COLOR_NODE_START = '#3B82F6'    
COLOR_NODE_OBJECTIVE = '#34D399' # Edmunds
COLOR_NODE_CRITICAL = '#F87171'  # Gargantua
COLOR_NODE_WAYPOINT = '#A78BFA'  # Saturno, Sist. Gargantua
COLOR_NODE_RISK = '#FBBF24'      # Miller, Mann (planetas de exploração antes do objetivo)


COLOR_EDGE_DEFAULT = '#CFD8DC' 
COLOR_EDGE_LABEL = '#455A64'   # Um cinza um pouco mais escuro para contraste

COLOR_ROUTE_HIGHLIGHT = '#8B5CF6' 
COLOR_BACKGROUND_FIG = '#FFFFFF' 
COLOR_TEXT_DARK = '#263238'    
COLOR_TEXT_LIGHT_ON_NODE = '#FFFFFF' 
COLOR_TEXT_DARK_ON_NODE = '#000000' 

# Função para criar o sistema planetário (NOMES DE INTERESTELAR - VALORES AJUSTADOS)
def criar_sistema_interestelar_cenario(): 
    G = nx.Graph()
    locais = [
        ("Terra", {"tipo": "planeta_partida", "cor_mapa": COLOR_NODE_START, "info": "Ponto de partida da Missão Garrido.", "fator_dilatacao_terra_por_nave": 1.0}), 
        ("Saturno (BM)", {"tipo": "ponto_chave", "cor_mapa": COLOR_NODE_WAYPOINT, "info": "Buraco de Minhoca para sistema Gargantua.", "fator_dilatacao_terra_por_nave": 1.0}), 
        ("Sist. Gargantua", {"tipo": "ponto_navegacao", "cor_mapa": COLOR_NODE_WAYPOINT, "info": "Entrada do sistema de Gargantua.", "fator_dilatacao_terra_por_nave": 10.0}), 
        ("Miller (Órbita)", {"tipo": "orbita_planeta_risco", "cor_mapa": COLOR_NODE_RISK, "info": "Planeta Miller: candidato a exploração.", "fator_dilatacao_terra_por_nave": 3000.0}), 
        ("Mann (Órbita)", {"tipo": "orbita_planeta_risco", "cor_mapa": COLOR_NODE_RISK, "info": "Planeta Mann: candidato a exploração.", "fator_dilatacao_terra_por_nave": 5.0}), 
        ("Planeta Edmunds", {"tipo": "planeta_habitavel_objetivo", "cor_mapa": COLOR_NODE_OBJECTIVE, "info": "Planeta Edmunds: destino final da sequência de exploração.", "fator_dilatacao_terra_por_nave": 1.5}),
        ("Gargantua (Manobra)", {"tipo": "ponto_critico", "cor_mapa": COLOR_NODE_CRITICAL, "info": "Manobra de slingshot em Gargantua.", "fator_dilatacao_terra_por_nave": 75000.0}) 
    ]
    for nome, atributos in locais:
        G.add_node(nome, **atributos)

    rotas = [
        ("Terra", "Saturno (BM)", {"tempo_nave_anos": 2.0, "info_rota_curta": "2.0a"}), 
        ("Saturno (BM)", "Sist. Gargantua", {"tempo_nave_anos": 0.01, "info_rota_curta": "0.01a"}), 
        ("Sist. Gargantua", "Miller (Órbita)", {"tempo_nave_anos": 0.1, "info_rota_curta": "0.1a"}),
        ("Sist. Gargantua", "Mann (Órbita)", {"tempo_nave_anos": 0.3, "info_rota_curta": "0.3a"}),
        ("Miller (Órbita)", "Mann (Órbita)", {"tempo_nave_anos": 0.4, "info_rota_curta": "0.4a"}),
        ("Mann (Órbita)", "Miller (Órbita)", {"tempo_nave_anos": 0.4, "info_rota_curta": "0.4a"}), 
        ("Mann (Órbita)", "Gargantua (Manobra)", {"tempo_nave_anos": 0.05, "info_rota_curta": "0.05a"}), 
        ("Gargantua (Manobra)", "Planeta Edmunds", {"tempo_nave_anos": 0.5, "info_rota_curta": "0.5a"}), 
        ("Mann (Órbita)", "Planeta Edmunds", {"tempo_nave_anos": 2.5, "info_rota_curta": "2.5a (D)"}), 
        ("Miller (Órbita)", "Planeta Edmunds", {"tempo_nave_anos": 2.8, "info_rota_curta": "2.8a (D)"}), 
    ]
    for u, v, atributos in rotas:
        G.add_edge(u, v, **atributos)
    return G

# Função para calcular tempos de um caminho específico
def calcular_tempos_caminho(grafo, caminho):
    tempo_total_nave_caminho = 0
    tempo_total_terra_caminho = 0
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i+1]
        if not grafo.has_edge(u,v): 
            print(f"Atenção: Aresta ausente entre {u} e {v} no caminho fornecido: {caminho}")
            return float('inf'), float('inf')

        dados_aresta = grafo.edges[u,v]
        tempo_nave_trecho = dados_aresta.get('tempo_nave_anos', float('inf'))
        if tempo_nave_trecho == float('inf'):
            print(f"Atenção: Aresta {u}-{v} não tem 'tempo_nave_anos'.")
            return float('inf'), float('inf')
        tempo_total_nave_caminho += tempo_nave_trecho
        
        fator_u = grafo.nodes[u].get('fator_dilatacao_terra_por_nave', 1.0)
        fator_v = grafo.nodes[v].get('fator_dilatacao_terra_por_nave', 1.0)
        
        fator_dilatacao_trecho = fator_v 
        if 'Gargantua (Manobra)' in v or 'Gargantua (Manobra)' in u:
            fator_dilatacao_trecho = grafo.nodes["Gargantua (Manobra)"].get('fator_dilatacao_terra_por_nave', 1.0)
        elif 'Miller (Órbita)' in v or 'Miller (Órbita)' in u: 
             fator_dilatacao_trecho = grafo.nodes["Miller (Órbita)"].get('fator_dilatacao_terra_por_nave', 1.0)
        
        tempo_total_terra_caminho += tempo_nave_trecho * fator_dilatacao_trecho
    return tempo_total_nave_caminho, tempo_total_terra_caminho

# Função atualizada para encontrar a melhor rota de exploração (otimizando tempo de nave)
def encontrar_melhor_rota_exploracao(grafo, origem, destinos_exploracao, destino_final):
    todas_as_rotas_exploracao_completas = []
    
    for p_expl in destinos_exploracao:
        if p_expl not in grafo:
            print(f"Erro: Planeta de exploração '{p_expl}' não encontrado no grafo.")
            return None, float('inf'), float('inf')
    if destino_final not in grafo:
        print(f"Erro: Destino final '{destino_final}' não encontrado no grafo.")
        return None, float('inf'), float('inf')

    from itertools import permutations
    ordens_exploracao = list(permutations(destinos_exploracao))

    for ordem_visita in ordens_exploracao:
        sequencia_waypoints = [origem] + list(ordem_visita) + [destino_final]
        
        caminho_completo_segmentado = []
        tempo_nave_total_para_sequencia = 0
        tempo_terra_total_para_sequencia = 0
        sequencia_valida = True

        for i in range(len(sequencia_waypoints) - 1):
            wp_origem = sequencia_waypoints[i]
            wp_destino = sequencia_waypoints[i+1]
            
            try: 
                melhor_segmento = nx.dijkstra_path(grafo, source=wp_origem, target=wp_destino, weight='tempo_nave_anos')
            except nx.NetworkXNoPath:
                sequencia_valida = False
                break 
            
            tempo_nave_segmento, tempo_terra_segmento = calcular_tempos_caminho(grafo, melhor_segmento)

            if tempo_nave_segmento == float('inf'): 
                sequencia_valida = False
                break
            
            tempo_nave_total_para_sequencia += tempo_nave_segmento
            tempo_terra_total_para_sequencia += tempo_terra_segmento
            
            if not caminho_completo_segmentado:
                caminho_completo_segmentado.extend(melhor_segmento)
            else:
                caminho_completo_segmentado.extend(melhor_segmento[1:]) 
        
        if sequencia_valida: 
            todas_as_rotas_exploracao_completas.append({
                "caminho": caminho_completo_segmentado,
                "tempo_nave": tempo_nave_total_para_sequencia,
                "tempo_terra": tempo_terra_total_para_sequencia
            })

    if not todas_as_rotas_exploracao_completas:
        return None, float('inf'), float('inf')
        
    todas_as_rotas_exploracao_completas.sort(key=lambda x: x['tempo_nave'])
    
    melhor_rota_obj = todas_as_rotas_exploracao_completas[0]
    return melhor_rota_obj['caminho'], melhor_rota_obj['tempo_nave'], melhor_rota_obj['tempo_terra']

# Função de visualização (COM ANIMAÇÃO DA ROTA E LABELS DE ARESTA ATUALIZADOS)
def visualizar_cenario_interestelar(grafo, caminho_otimizado=None):
    plt.style.use('default') 

    fig, ax = plt.subplots(figsize=(22, 17)) # Aumentei um pouco o figsize para os labels
    fig.patch.set_facecolor(COLOR_BACKGROUND_FIG) 
    ax.set_facecolor(COLOR_BACKGROUND_FIG) 

    pos = nx.spring_layout(grafo, k=1.3, iterations=180, seed=42, weight=None) # Ajustei k e iterations

    node_colors = [grafo.nodes[node]['cor_mapa'] for node in grafo.nodes()]
    all_node_sizes_base = {}
    for node in grafo.nodes():
        if grafo.nodes[node]['tipo'] == 'ponto_critico':
            all_node_sizes_base[node] = 6500 # Um pouco maior para destaque
        elif grafo.nodes[node]['tipo'] == 'planeta_habitavel_objetivo':
            all_node_sizes_base[node] = 6000
        else:
            all_node_sizes_base[node] = 5000
    node_size_list_for_drawing = [all_node_sizes_base[node] for node in grafo.nodes()]

    nx.draw_networkx_nodes(ax=ax, G=grafo, pos=pos, 
                           node_color=node_colors, 
                           node_size=node_size_list_for_drawing, 
                           alpha=1.0, 
                           edgecolors='#78909C', 
                           linewidths=1)
    
    node_labels_internal = {}
    for node in grafo.nodes():
        parts = node.split("(")
        label = parts[0].strip() 
        if len(label.split()) > 1 and len(label) > 7:
             label = "".join(word[0] for word in label.split())
        elif len(label) > 7:
             label = label[:6] + "."
        node_labels_internal[node] = label.upper()

    def get_text_color_for_node(node_color_hex):
        h = node_color_hex.lstrip('#')
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255
        return COLOR_TEXT_LIGHT_ON_NODE if luminance < 0.5 else COLOR_TEXT_DARK_ON_NODE

    for node, label_text in node_labels_internal.items():
        text_color = get_text_color_for_node(grafo.nodes[node]['cor_mapa'])
        ax.text(pos[node][0], pos[node][1], label_text, 
                ha='center', va='center', 
                fontsize=8.5, fontweight='bold', color=text_color) 

    nx.draw_networkx_edges(ax=ax, G=grafo, pos=pos, 
                           width=0.8, 
                           alpha=0.4, 
                           edge_color=COLOR_EDGE_DEFAULT, 
                           arrows=False) 

    # --- LABELS DAS ARESTAS ATUALIZADOS PARA MOSTRAR TEMPO NAVE E TEMPO TERRA ---
    edge_labels = {}
    for u, v, data in grafo.edges(data=True):
        tempo_nave_aresta = data.get('tempo_nave_anos', 0)
        
        # Calcular tempo terra para este trecho específico
        fator_u_aresta = grafo.nodes[u].get('fator_dilatacao_terra_por_nave', 1.0)
        fator_v_aresta = grafo.nodes[v].get('fator_dilatacao_terra_por_nave', 1.0)
        fator_dil_aresta = fator_v_aresta # Default para o nó de destino
        if 'Gargantua (Manobra)' in v or 'Gargantua (Manobra)' in u:
            fator_dil_aresta = grafo.nodes["Gargantua (Manobra)"].get('fator_dilatacao_terra_por_nave', 1.0)
        elif 'Miller (Órbita)' in v or 'Miller (Órbita)' in u:
            fator_dil_aresta = grafo.nodes["Miller (Órbita)"].get('fator_dilatacao_terra_por_nave', 1.0)
        
        tempo_terra_aresta = tempo_nave_aresta * fator_dil_aresta
        
        # Formatar o label com quebra de linha
        # Usar info_rota_curta se existir, senão o tempo de nave
        label_nave = data.get('info_rota_curta', f"{tempo_nave_aresta:.2f}a")
        edge_labels[(u,v)] = f"{label_nave} Nave\n({tempo_terra_aresta:.1f}a Terra)"
        
    nx.draw_networkx_edge_labels(ax=ax, G=grafo, pos=pos, edge_labels=edge_labels, 
                                 font_size=7.0, # Ajuste o tamanho da fonte se necessário
                                 font_color=COLOR_EDGE_LABEL,
                                 font_weight='normal',
                                 bbox=dict(facecolor=COLOR_BACKGROUND_FIG, alpha=0.0, edgecolor='none', pad=0.1), 
                                 label_pos=0.5, 
                                 rotate=False) 
    # --- FIM DA ATUALIZAÇÃO DOS LABELS DAS ARESTAS ---

    path_edge_artists_animated = [] 

    if caminho_otimizado and len(caminho_otimizado) > 1:
        path_edges_segments = list(zip(caminho_otimizado[:-1], caminho_otimizado[1:])) 
        
        def update_animation(frame_num):
            nonlocal path_edge_artists_animated 
            for artist_collection in path_edge_artists_animated:
                if isinstance(artist_collection, list):
                    for artist in artist_collection:
                        artist.remove()
                elif artist_collection: 
                    artist_collection.remove()
            path_edge_artists_animated.clear()

            edges_to_draw_this_frame = path_edges_segments[:frame_num + 1] 
            
            if edges_to_draw_this_frame:
                drawn_collection = nx.draw_networkx_edges(
                    ax=ax, G=grafo, pos=pos,
                    edgelist=edges_to_draw_this_frame,
                    width=2.5, edge_color=COLOR_ROUTE_HIGHLIGHT,
                    style='-', alpha=0.9, arrows=False
                )
                if drawn_collection:
                    if isinstance(drawn_collection, list):
                        path_edge_artists_animated.extend(drawn_collection)
                    else:
                        path_edge_artists_animated.append(drawn_collection)
            return path_edge_artists_animated 

        num_frames = len(path_edges_segments)
        if num_frames > 0:
            ani = animation.FuncAnimation(fig, update_animation, frames=num_frames, 
                                          interval=700, blit=False, repeat=False)
            fig.ani = ani 
    
    if caminho_otimizado and len(caminho_otimizado) > 1: 
        path_node_sizes_calculated = []
        for node_in_path in caminho_otimizado:
            base_size = all_node_sizes_base[node_in_path] 
            path_node_sizes_calculated.append(base_size * 1.15) 

        nx.draw_networkx_nodes(ax=ax, G=grafo, pos=pos, nodelist=caminho_otimizado, 
                               node_color=[grafo.nodes[node]['cor_mapa'] for node in caminho_otimizado],
                               node_size=path_node_sizes_calculated, 
                               edgecolors=COLOR_ROUTE_HIGHLIGHT, 
                               linewidths=2.0) 
                               
        for node in caminho_otimizado: 
            label_text = node_labels_internal[node]
            text_color = get_text_color_for_node(grafo.nodes[node]['cor_mapa'])
            ax.text(pos[node][0], pos[node][1], label_text, 
                    ha='center', va='center', 
                    fontsize=8.5, fontweight='bold', color=text_color) 

    ax.set_title("Missão Garrido: Rota Interestelar", 
                 fontsize=18, fontweight='bold', color=COLOR_TEXT_DARK, pad=20)

    ax.axis('off')
    plt.tight_layout()
    plt.show()

# --- Execução Principal (EXPLORAÇÃO SEQUENCIAL, OTIMIZANDO TEMPO DE NAVE) ---
if __name__ == "__main__":
    grafo_missao = criar_sistema_interestelar_cenario() 

    origem_missao = "Terra"
    planetas_exploracao_obrigatoria = ["Miller (Órbita)", "Mann (Órbita)"] 
    destino_final_missao = "Planeta Edmunds" 
    # max_tempo_terra_permitido = 200.0 # REMOVIDA A RESTRIÇÃO DE TEMPO TERRESTRE

    print(f"🚀 Iniciando simulação da Missão Garrido (cenário Interestelar)...")
    print(f"   Objetivo: Encontrar a rota para '{destino_final_missao}', visitando {', '.join(planetas_exploracao_obrigatoria)} antes,")
    print(f"             minimizando o tempo TOTAL DE NAVE da tripulação (Matheus, Yago, Caio, João).")
    print("-" * 70)

    caminho, tempo_nave, tempo_terra = encontrar_melhor_rota_exploracao(
        grafo_missao, 
        origem_missao, 
        planetas_exploracao_obrigatoria,
        destino_final_missao
    )

    if caminho:
        print("\n✨ MELHOR ROTA DE EXPLORAÇÃO (MENOR TEMPO DE NAVE) ENCONTRADA! ✨\n")
        print(f"  ➡️ Sequência de Locais Sugerida:")
        print(f"     {' -> '.join(caminho)}\n")
        print(f"  ⏳ Tempo Total Estimado de Nave (Tripulação): {tempo_nave:.3f} anos.")
        print(f"  🌍 Tempo Total Estimado Decorrido na Terra (Informativo): {tempo_terra:.2f} anos.")
        print("-" * 70)

        print("\nℹ️ INFORMAÇÕES SOBRE OS LOCAIS NA ROTA (Cenário Interestelar):\n")
        nos_unicos_no_caminho = []
        [nos_unicos_no_caminho.append(x) for x in caminho if x not in nos_unicos_no_caminho]

        for local_nome in nos_unicos_no_caminho:
            info_local = grafo_missao.nodes[local_nome].get('info', 'N/A') 
            fator_dil = grafo_missao.nodes[local_nome].get('fator_dilatacao_terra_por_nave', 1.0) 
            print(f"  📍 Local: {local_nome}")
            print(f"     Info: {info_local}")
            print(f"     Fator de Dilatação da Região (aprox.): {fator_dil:.0f}x")
            print("-" * 40) 
        
        print("\n🛤️ DETALHES DOS TRECHOS DA ROTA OTIMIZADA (Cenário Interestelar):\n")
        for i in range(len(caminho) - 1):
            u, v = caminho[i], caminho[i+1]
            if u == v: continue

            dados_aresta = grafo_missao.get_edge_data(u, v) 
            if dados_aresta is None: 
                print(f"    Atenção: Não há aresta direta entre {u} e {v} no caminho final.")
                continue
            tempo_nave_trecho_atual = dados_aresta.get('tempo_nave_anos', 0) 
            # Usaremos 'info_rota_curta' se existir para o label de nave, ou o tempo.
            info_nave_label = dados_aresta.get('info_rota_curta', f"{tempo_nave_trecho_atual:.2f}a")
            
            fator_u_calc = grafo_missao.nodes[u].get('fator_dilatacao_terra_por_nave', 1.0) 
            fator_v_calc = grafo_missao.nodes[v].get('fator_dilatacao_terra_por_nave', 1.0) 
            
            fator_dil_trecho_calc = fator_v_calc 
            if 'Gargantua (Manobra)' in v or 'Gargantua (Manobra)' in u: 
                fator_dil_trecho_calc = grafo_missao.nodes["Gargantua (Manobra)"].get('fator_dilatacao_terra_por_nave', 1.0)
            elif 'Miller (Órbita)' in v or 'Miller (Órbita)' in u: 
                 fator_dil_trecho_calc = grafo_missao.nodes["Miller (Órbita)"].get('fator_dilatacao_terra_por_nave', 1.0)

            tempo_terra_trecho_calc = tempo_nave_trecho_atual * fator_dil_trecho_calc 
            print(f"  ➡️ Trecho: De '{u}' para '{v}':")
            print(f"     ⏳ Tempo de Nave: {tempo_nave_trecho_atual:.4f} anos ({info_nave_label})") # Mostra o label curto aqui também
            print(f"     🌍 Tempo na Terra (para este trecho): {tempo_terra_trecho_calc:.2f} anos (dilatação de '{v}' com ajuste: {fator_dil_trecho_calc:.0f}x)")
            print("-" * 40) 
        print("=" * 70)

    else:
        print(f"\n❌ NENHUMA ROTA DE EXPLORAÇÃO ENCONTRADA que visite {', '.join(planetas_exploracao_obrigatoria)} antes de '{destino_final_missao}'.")
        print("   Verifique a conectividade do grafo e a definição dos waypoints.")
        print("=" * 70)

    if caminho: 
        print("\n🌌 Gerando visualização do mapa estelar...")
        visualizar_cenario_interestelar(grafo_missao, caminho_otimizado=caminho) 
    else:
        print("\n🌌 Visualização não gerada pois não há caminho viável.")
    print("\n✅ Simulação Concluída.")
