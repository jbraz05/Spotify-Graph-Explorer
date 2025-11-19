import csv
import os
from .graph import Graph

def load_spotify_graph(filepath):
    print(f"... Lendo arquivo: {filepath}")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo {filepath} não encontrado.")

    g = Graph(directed=False)
    
    try:
        f = open(filepath, 'r', encoding='utf-8')
    except UnicodeDecodeError:
        f = open(filepath, 'r', encoding='latin-1')

    with f:
        reader = csv.DictReader(f)
        for row in reader:
            track_name = row.get('track_name', 'Unknown Track')
            artists_raw = row.get('artist(s)_name', '')
            if not artists_raw: continue
            artists = [a.strip() for a in artists_raw.split(',')]
            
            if len(artists) == 1:
                g.nodes.add(artists[0])
                if artists[0] not in g.adj_list: g.adj_list[artists[0]] = {}
                continue

            streams_str = row.get('streams', '0').replace(',', '')
            try:
                streams = float(streams_str)
            except ValueError:
                streams = 0.0
            
            weight = 1_000_000_000/ streams + 1
            
            
            for i in range(len(artists)):
                for j in range(i + 1, len(artists)):
                    g.add_edge(artists[i], artists[j], weight, track_name=track_name)

    return g