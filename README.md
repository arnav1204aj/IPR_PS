# Dependencies
Check requirements.txt

# Parameters
1. albedo - 'sv' for spatially varying (SRT3), 'unif' for uniform (SRT2)
2. mode - 'norm' for normal, 'rob' for robust
3. num_lights - 4 to 24 for 'norm', 17 to 24 for 'rob', 4 or 12 in real world
4. object - 'relief' or 'budrelief'

# Running Results

1. Error Maps, Normal Estimates, MAE, Rendered Images, Albedos
Run err_maps.py (set params albedo, mode, num_lights), err_maps_part2.py (set params albedo, num_lights), realworld.py (params num_lights, object)

2. Graphs
In testplot.py and testplot_part2.py, uncomment appropriate block for the required graph.

3. Lights
Run generateLight.py, set num_lights to required number.




