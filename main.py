import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager
import matplotlib.animation as animation
import numpy as np

COLOR_NODE_DEFAULT = '#00BFFF' 
COLOR_NODE_START = '#FFD700'    
COLOR_NODE_OBJECTIVE = '#32CD32' 
COLOR_NODE_CRITICAL = '#FF4500'  
COLOR_NODE_WAYPOINT = '#9370DB'  
COLOR_NODE_RISK = '#FFBF00'      

COLOR_EDGE_DEFAULT = '#A9A9A9'  
COLOR_EDGE_GLOW = '#87CEFA'     
COLOR_EDGE_LABEL = '#B0C4DE'    


COLOR_ROUTE_HIGHLIGHT = '#800080' 
COLOR_ROUTE_GLOW = '#9400D3'      

COLOR_BACKGROUND_FIG = '#050510' 
COLOR_TEXT_DARK = '#F0F8FF'    
COLOR_TEXT_LIGHT_ON_NODE = '#FFFFFF' 
COLOR_TEXT_DARK_ON_NODE = '#000000' 

def criar_sistema_interestelar_cenario():
    G = nx.Graph()
    locais = [
        ("Terra", {"tipo": "planeta_partida", "cor_mapa": COLOR_NODE_START, "info": "Ponto de partida da Missão Garrido.", "fator_dilatacao_terra_por_nave": 1.0}),
        ("Saturno (BM)", {"tipo": "ponto_chave", "cor_mapa": COLOR_NODE_WAYPOINT, "info": "Buraco de Minhoca para sistema Gargantua.", "fator_dilatacao_terra_por_nave": 1.0}),
        ("Sist. Gargantua", {"tipo": "ponto_navegacao", "cor_mapa": COLOR_NODE_WAYPOINT, "info": "Entrada do sistema de Gargantua.", "fator_dilatacao_terra_por_nave": 10.0}),
        ("Miller (Órbita)", {"tipo": "orbita_planeta_risco", "cor_mapa": COLOR_NODE_RISK, "info": "Planeta Miller: possível ponto de passagem.", "fator_dilatacao_terra_por_nave": 3000.0}),
        ("Mann (Órbita)", {"tipo": "orbita_planeta_risco", "cor_mapa": COLOR_NODE_RISK, "info": "Planeta Mann: possível ponto de passagem.", "fator_dilatacao_terra_por_nave": 5.0}),
        ("Planeta Edmunds", {"tipo": "planeta_habitavel_objetivo", "cor_mapa": COLOR_NODE_OBJECTIVE, "info": "Planeta Edmunds: destino principal da Missão Garrido.", "fator_dilatacao_terra_por_nave": 1.5}),
        ("Gargantua (Manobra)", {"tipo": "ponto_critico", "cor_mapa": COLOR_NODE_CRITICAL, "info": "Manobra de slingshot em Gargantua.", "fator_dilatacao_terra_por_nave": 75000.0})
    ]
    for nome, atributos in locais:
        G.add_node(nome, **atributos)

    rotas = [
        ("Terra", "Saturno (BM)", {"tempo_nave_anos": 2.0, "info_rota": "2.0a"}),
        ("Saturno (BM)", "Sist. Gargantua", {"tempo_nave_anos": 0.01, "info_rota": "0.01a"}),
        ("Sist. Gargantua", "Miller (Órbita)", {"tempo_nave_anos": 0.1, "info_rota": "0.1a"}),
        ("Sist. Gargantua", "Mann (Órbita)", {"tempo_nave_anos": 0.3, "info_rota": "0.3a"}),
        ("Miller (Órbita)", "Mann (Órbita)", {"tempo_nave_anos": 0.4, "info_rota": "0.4a"}),
        ("Mann (Órbita)", "Miller (Órbita)", {"tempo_nave_anos": 0.4, "info_rota": "0.4a"}),
        ("Mann (Órbita)", "Gargantua (Manobra)", {"tempo_nave_anos": 0.05, "info_rota": "0.05a"}),
        ("Gargantua (Manobra)", "Planeta Edmunds", {"tempo_nave_anos": 0.5, "info_rota": "0.5a"}),
        ("Mann (Órbita)", "Planeta Edmunds", {"tempo_nave_anos": 2.5, "info_rota": "2.5a (D)"}),
        ("Miller (Órbita)", "Planeta Edmunds", {"tempo_nave_anos": 2.8, "info_rota": "2.8a (D)"}),
        ("Sist. Gargantua", "Planeta Edmunds", {"tempo_nave_anos": 3.5, "info_rota": "3.5a (SG->E)"})
    ]
    for u, v, atributos in rotas:
        G.add_edge(u, v, **atributos)

    for u, v, data in G.edges(data=True):
        tempo_nave_trecho = data.get('tempo_nave_anos', float('inf'))
        if tempo_nave_trecho == float('inf'):
            data['tempo_terra_aresta'] = float('inf')
            continue

        fator_u_aresta = G.nodes[u].get('fator_dilatacao_terra_por_nave', 1.0)
        fator_v_aresta = G.nodes[v].get('fator_dilatacao_terra_por_nave', 1.0)

        fator_dil_aresta = fator_v_aresta
        if 'Gargantua (Manobra)' in v or 'Gargantua (Manobra)' in u:
            fator_dil_aresta = G.nodes["Gargantua (Manobra)"].get('fator_dilatacao_terra_por_nave', 1.0)
        elif 'Miller (Órbita)' in v or 'Miller (Órbita)' in u:
            fator_dil_aresta = G.nodes["Miller (Órbita)"].get('fator_dilatacao_terra_por_nave', 1.0)

        data['tempo_terra_aresta'] = tempo_nave_trecho * fator_dil_aresta

    return G

def calcular_tempos_caminho_final(grafo, caminho):
    tempo_total_nave_caminho = 0
    tempo_total_terra_caminho = 0
    if not caminho :
        return float('inf'), float('inf')
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i+1]
        if not grafo.has_edge(u,v):
            return float('inf'), float('inf')

        dados_aresta = grafo.edges[u,v]
        tempo_nave_trecho = dados_aresta.get('tempo_nave_anos', float('inf'))
        tempo_terra_trecho_precalculado = dados_aresta.get('tempo_terra_aresta', float('inf'))

        if tempo_nave_trecho == float('inf') or tempo_terra_trecho_precalculado == float('inf'):
            return float('inf'), float('inf')

        tempo_total_nave_caminho += tempo_nave_trecho
        tempo_total_terra_caminho += tempo_terra_trecho_precalculado

    return tempo_total_nave_caminho, tempo_total_terra_caminho


def encontrar_rota_dijkstra_otimizando_terra(grafo, origem, destino, max_tempo_terra, peso_dijkstra='tempo_terra_aresta'):
    try:
        caminho_otimo_terra = nx.dijkstra_path(grafo, source=origem, target=destino, weight=peso_dijkstra)
        tempo_nave_final, tempo_terra_final = calcular_tempos_caminho_final(grafo, caminho_otimo_terra)
        
        if tempo_terra_final == float('inf'): 
            return None, float('inf'), float('inf'), False 
        
        restricao_atendida = tempo_terra_final <= max_tempo_terra
        
        return caminho_otimo_terra, tempo_nave_final, tempo_terra_final, restricao_atendida

    except nx.NetworkXNoPath:
        return None, float('inf'), float('inf'), False
    except nx.NodeNotFound:
        print(f"Erro: Nó de origem '{origem}' ou destino '{destino}' não encontrado no grafo.")
        return None, float('inf'), float('inf'), False

def visualizar_cenario_interestelar(grafo, caminho_otimizado=None):
    plt.style.use('default')

    fig, ax = plt.subplots(figsize=(22, 17))
    fig.patch.set_facecolor(COLOR_BACKGROUND_FIG)
    ax.set_facecolor(COLOR_BACKGROUND_FIG)

    plt.subplots_adjust(top=0.86, bottom=0.05, left=0.05, right=0.95)

    num_stars = 2500
    star_x = np.random.uniform(-1.2, 1.2, num_stars)
    star_y = np.random.uniform(-1.2, 1.2, num_stars)
    star_sizes = np.random.uniform(0.1, 2.0, num_stars)
    star_colors = np.random.choice(['#FFFFFF', '#F0F0FF', '#FFE0E0', '#D0E0FF', '#ADD8E6'], num_stars)

    ax.scatter(star_x, star_y, s=star_sizes, c=star_colors, alpha=0.8, zorder=-2)

    pos = {
        "Terra": (-0.8, 0.8),
        "Saturno (BM)": (-0.4, 0.6),
        "Sist. Gargantua": (0.0, 0.0),
        "Miller (Órbita)": (-0.6, -0.5),
        "Mann (Órbita)": (0.6, -0.4),
        "Planeta Edmunds": (0.8, 0.8),
        "Gargantua (Manobra)": (0.2, -0.8)
    }

    node_colors = [grafo.nodes[node]['cor_mapa'] for node in grafo.nodes()]
    all_node_sizes_base = {}
    for node in grafo.nodes():
        if grafo.nodes[node]['tipo'] == 'ponto_critico':
            all_node_sizes_base[node] = 5000
        elif grafo.nodes[node]['tipo'] == 'planeta_habitavel_objetivo':
            all_node_sizes_base[node] = 4500
        else:
            all_node_sizes_base[node] = 4000
    node_size_list_for_drawing = [all_node_sizes_base[node] for node in grafo.nodes()]

    nx.draw_networkx_nodes(ax=ax, G=grafo, pos=pos,
                           node_color=node_colors,
                           node_size=node_size_list_for_drawing,
                           alpha=0.9,
                           edgecolors='#FFFFFF',
                           linewidths=1.5)

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
                fontsize=8, fontweight='bold', color=text_color)


    nx.draw_networkx_edges(ax=ax, G=grafo, pos=pos,
                           width=3.5,
                           alpha=0.3,
                           edge_color=COLOR_EDGE_GLOW,
                           arrows=False) 

    nx.draw_networkx_edges(ax=ax, G=grafo, pos=pos,
                           width=1.8,
                           alpha=0.8,
                           edge_color=COLOR_EDGE_DEFAULT,
                           arrows=False)

    edge_labels = {}
    for u, v, data in grafo.edges(data=True):
        tempo_nave_aresta = data.get('tempo_nave_anos', 0)
        tempo_terra_aresta_precalc = data.get('tempo_terra_aresta', 0)
        
        label_nave = data.get('info_rota', f"{tempo_nave_aresta:.2f}a")
        edge_labels[(u,v)] = f"{label_nave} Nave\n({tempo_terra_aresta_precalc:.1f}a Terra)"
        
    nx.draw_networkx_edge_labels(ax=ax, G=grafo, pos=pos, edge_labels=edge_labels,
                                 font_size=11.0,
                                 font_color=COLOR_EDGE_LABEL,
                                 font_weight='normal',
                                 bbox=dict(facecolor=COLOR_BACKGROUND_FIG, alpha=0.6, edgecolor='none', pad=0.1),
                                 label_pos=0.5,
                                 rotate=False)

    path_edge_artists_animated = []

    if caminho_otimizado and len(caminho_otimizado) > 1:
        path_edges_segments = list(zip(caminho_otimizado[:-1], caminho_otimizado[1:]))

        def update_animation(frame_num):
            nonlocal path_edge_artists_animated
            for artist_collection in path_edge_artists_animated:
                if isinstance(artist_collection, list):
                    for artist in artist_collection:
                        try: artist.remove()
                        except ValueError: pass
                else:
                    try: artist_collection.remove()
                    except ValueError: pass
            path_edge_artists_animated.clear()

            edges_to_draw_this_frame = path_edges_segments[:frame_num + 1]

            if edges_to_draw_this_frame:

                drawn_glow_collection = nx.draw_networkx_edges(
                    ax=ax, G=grafo, pos=pos,
                    edgelist=edges_to_draw_this_frame,
                    width=7.0,
                    edge_color=COLOR_ROUTE_GLOW,
                    style='-', alpha=0.5, arrows=False
                )
                if drawn_glow_collection:
                    if not isinstance(drawn_glow_collection, list):
                        drawn_glow_collection = [drawn_glow_collection]
                    path_edge_artists_animated.extend(drawn_glow_collection)

                drawn_main_collection = nx.draw_networkx_edges(
                    ax=ax, G=grafo, pos=pos,
                    edgelist=edges_to_draw_this_frame,
                    width=4.0,
                    edge_color=COLOR_ROUTE_HIGHLIGHT,
                    style='-', alpha=1.0, arrows=True,
                    arrowsize=20
                )
                if drawn_main_collection:
                    if not isinstance(drawn_main_collection, list):
                        drawn_main_collection = [drawn_main_collection]
                    path_edge_artists_animated.extend(drawn_main_collection)
            return path_edge_artists_animated

        num_frames = len(path_edges_segments)
        if num_frames > 0:
            ani = animation.FuncAnimation(fig, update_animation, frames=num_frames,
                                          interval=700, # VALOR RESTAURADO PARA 700ms
                                          blit=False, repeat=False)
            fig.ani = ani

    if caminho_otimizado and len(caminho_otimizado) > 1:
        path_node_sizes_calculated = []
        for node_in_path in caminho_otimizado:
            base_size = all_node_sizes_base[node_in_path]
            path_node_sizes_calculated.append(base_size * 1.25)

        nx.draw_networkx_nodes(ax=ax, G=grafo, pos=pos, nodelist=caminho_otimizado,
                               node_color=[grafo.nodes[node]['cor_mapa'] for node in caminho_otimizado],
                               node_size=path_node_sizes_calculated,
                               edgecolors=COLOR_ROUTE_HIGHLIGHT,
                               linewidths=2.5)

        for node in caminho_otimizado:
            label_text = node_labels_internal[node]
            text_color = get_text_color_for_node(grafo.nodes[node]['cor_mapa'])
            ax.text(pos[node][0], pos[node][1], label_text,
                    ha='center', va='center',
                    fontsize=8, fontweight='bold', color=text_color)

    fig.suptitle("Missão Garrido: Rota Interestelar Direta para Edmunds",
                 fontsize=16,
                 fontweight='bold',
                 color=COLOR_TEXT_DARK,
                 y=0.98)

    ax.axis('off')
    plt.show()


if __name__ == "__main__":
    grafo_missao = criar_sistema_interestelar_cenario()

    origem_missao = "Terra"
    destino_final_missao = "Planeta Edmunds"
    max_tempo_terra_permitido = 200.0

    print(f"🚀 Iniciando simulação da Missão Garrido (cenário Interestelar)...")
    print(f"   Objetivo: Encontrar a rota MAIS RÁPIDA EM TEMPO TERRESTRE de '{origem_missao}' para '{destino_final_missao}',")
    print(f"             e verificar se respeita o limite de {max_tempo_terra_permitido} anos terrestres.")
    print(f"             Tripulação: Matheus, Yago, Caio, João.")
    print("-" * 70)

    caminho, tempo_nave, tempo_terra, restricao_ok = encontrar_rota_dijkstra_otimizando_terra(
        grafo_missao,
        origem_missao,
        destino_final_missao,
        max_tempo_terra_permitido,
        peso_dijkstra='tempo_terra_aresta'
    )

    if caminho:
        print("\n✨ ROTA MAIS RÁPIDA EM TEMPO TERRESTRE (via Dijkstra) ENCONTRADA! ✨\n")
        print(f"  ➡️ Sequência de Locais Sugerida:")
        print(f"     {' -> '.join(caminho)}\n")
        print(f"  ⏳ Tempo Total Estimado de Nave (Tripulação) para esta rota: {tempo_nave:.3f} anos.")
        print(f"  🌍 Tempo Total Estimado Decorrido na Terra para esta rota: {tempo_terra:.2f} anos.")

        if restricao_ok:
            print(f"  ✅ RESTRIÇÃO DE TEMPO TERRESTRE ATENDIDA (<= {max_tempo_terra_permitido} anos).")
        else:
            print(f"  ❌ ATENÇÃO: MESMO A ROTA MAIS RÁPIDA EM TEMPO TERRESTRE ({tempo_terra:.2f} anos) NÃO ATENDE À RESTRIÇÃO de {max_tempo_terra_permitido} anos.")
        print("-" * 70)

        print("\nℹ️ INFORMAÇÕES SOBRE OS LOCAIS NA ROTA (Cenário Interestelar):\n")
        for local_nome in caminho:
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
            info_rota_trecho = dados_aresta.get('info_rota', 'N/A')
            tempo_terra_trecho_aresta = dados_aresta.get('tempo_terra_aresta', 0)
            
            print(f"  ➡️ Trecho: De '{u}' para '{v}':")
            print(f"     ⏳ Tempo de Nave: {tempo_nave_trecho_atual:.4f} anos ({info_rota_trecho})")
            print(f"     🌍 Tempo na Terra (para este trecho): {tempo_terra_trecho_aresta:.2f} anos")
            print("-" * 40)
        print("=" * 70)

    else:
        print(f"\n❌ NENHUMA ROTA DIRETA ENCONTRADA de '{origem_missao}' para '{destino_final_missao}' usando Dijkstra com peso 'tempo_terra_aresta'.")
        print("   Verifique a conectividade do grafo e os pesos das arestas.")
        print("=" * 70)

    if caminho:
        print("\n🌌 Gerando visualização do mapa estelar...")
        visualizar_cenario_interestelar(grafo_missao, caminho_otimizado=caminho)
    else:
        print("\n🌌 Visualização não gerada pois não há caminho.")
    print("\n✅ Simulação Concluída.")
