import heapq
import networkx as nx
import matplotlib.pyplot as plt


# ... (بقیه کدها مانند قبل بدون تغییر میمانند) ...

# تابع جدید برای رسم گراف
def plot_graph(graph, title="Graph Structure"):
    G = nx.DiGraph()

    # اضافه کردن گرهها و یالها به گراف شبکه‌ای
    for from_node in graph.nodes:
        G.add_node(from_node)
        for to_node, attrs in graph.nodes[from_node].items():
            G.add_edge(
                from_node,
                to_node,
                distance=attrs['distance'],
                speed_limit=attrs['speed_limit']
            )

    # تنظیمات بصری
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))

    # رسم گرهها
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

    # رسم یالها با پیکان
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', arrowstyle='->')

    # اضافه کردن لیبل‌ها
    edge_labels = {(u, v): f"Distance: {G[u][v]['distance']}km\nSpeed: {G[u][v]['speed_limit']}km/h"
                   for u, v in G.edges()}

    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred')

    plt.title(title)
    plt.axis('off')
    plt.show()


# به‌روزرسانی تابع main برای نمایش گراف
def main():
    base_graph = setup_base_graph()
    plot_graph(base_graph, "گراف اولیه (پیش‌فرض)")  # نمایش گراف

    # بقیه کدها مانند قبل...
    weather, max_speed, accidents, start, end = get_user_input()
    dynamic_graph = calculate_edge_weights(base_graph, weather, max_speed, accidents)
    path, total_weight = dijkstra(dynamic_graph, start, end)

    if path:
        print(f"مسیر بهینه: {' → '.join(path)}")
        print(f"وزن کلی: {total_weight:.2f} دقیقه")
    else:
        print("مسیری یافت نشد!")


if __name__ == "__main__":
    main()