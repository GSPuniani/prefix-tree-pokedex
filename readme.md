# Prefix Tree Pokédex

## About

This project visually showcases the genealogy of Pokemon using Prefix Trees (a.k.a. Tries). 

The accompanying Medium blog post for this project is available [here](). This blog post explains the concept of prefix trees and explains the purpose of this project. Essentially, we use the PyDot graph visualization library to display prefix trees consisting of Pokémon names. Since many Pokémon that are evolutionary variants of each other usually begin with the same few letters, we display these names as prefix trees to show related evolutionary states of some Pokémon. 

To run this project on your local machine, follow the instructions below.

## Download, Install, and Run

Download or clone the repo. Install `PyDot`; a virtual environment is recommended. If `pip3 install pydot` doesn't work, consider using `conda install pydot`. 

There are four files for implementing the prefix tree data structure: `prefixtreenode.py`, `prefixtreenode_test.py`, `prefixtree.py`, and `prefixtree_test.py`. The file that produces the visualizations is `graph_pydot.py`. When run, it produces a JSON file called `output.json` as well as a PNG file in the `output_images` folder called `output.png`. Other files were for experimentation.

The Pokémon names used for the visualization come from `input.txt`. Feel free to add as many names as you want here (note that each name is on its own line). In order for the `terminal_word` flag to work properly, make sure there is a new line after the final name on the list (for more information about the `terminal_word` flag, read the blog post). Again, the output visualization will appear in `output.png` in the `output_images` folder. The file name can be changed from the last line of `graph_pydot.py`. 

Here is the output after adding one Pokémon:

<img alt="Charmander Prefix Tree" src="https://github.com/GSPuniani/prefix-tree-pokedex/blob/main/output_images/charmander_output.png?raw=true">


After adding multiple Pokémon with the same "Char" prefix:

<img alt="Char Family Prefix Tree" src="https://github.com/GSPuniani/prefix-tree-pokedex/blob/main/output_images/char_output.png?raw=true">


And after adding several other unrelated Pokémon:

<img alt="Pokémon Prefix Tree" src="https://github.com/GSPuniani/prefix-tree-pokedex/blob/main/output_images/final_output.png?raw=true">
