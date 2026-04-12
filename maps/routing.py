import osmnx as ox

def get_route(start_lat, start_lon, end_lat, end_lon):

    G = ox.graph_from_place("Vijayawada, India", network_type='drive')

    orig = ox.distance.nearest_nodes(G, start_lon, start_lat)
    dest = ox.distance.nearest_nodes(G, end_lon, end_lat)

    route = ox.shortest_path(G, orig, dest, weight='length')

    return G, route