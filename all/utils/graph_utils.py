import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

def create_graph(schema):
    G = nx.Graph()
    for table, details in schema.items():
        G.add_node(table, label=table, color="blue")
        for column in details["columns"]:
            col_node = f"{table}.{column}"
            G.add_node(col_node, label=column, color="gray")
            G.add_edge(table, col_node)
        for fk_col, ref_table in details["foreign_keys"].items():
            fk_node = f"{table}.{fk_col}"
            ref_node = f"{ref_table}.{fk_col}"
            G.add_edge(fk_node, ref_node, color="red")
    return G

def visualize_graph(G):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    node_colors = [G.nodes[n].get("color", "gray") for n in G.nodes]
    labels = {n: G.nodes[n].get("label", n) for n in G.nodes} # Use get for safety
    edge_colors = [G.edges[e].get("color", "black") for e in G.edges]
    edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True) if 'label' in d}

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=8)
    st.pyplot(plt)