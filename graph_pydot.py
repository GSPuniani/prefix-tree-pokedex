import json
import pydot


def struct():
    """Return a dictionary structure with a Boolean flag for terminal nodes"""
    struct = {
        'is_terminal': 'False'
    }
    return struct

# Retrieve list of words from the input file
file_ = open('./input.txt', 'r')
file_text = file_.read()
file_len = len(file_text)
file_.close()

# Iterate through nested dictionaries to produce trie
node_dict = struct()
root = node_dict
for char in file_text:
    if char != '\n':
        if char not in node_dict:
            node_dict[char] = struct()
        node_dict = node_dict[char]
    elif char == '\n':
        node_dict['is_terminal'] = 'True'
        node_dict = root

# Save the trie into JSON format
with open('output.json', 'w') as json_file:
    json.dump(root, json_file, indent=4)

# Convert and save the trie to decision tree graph using PyDot
# Code inspiration: https://stackoverflow.com/questions/13688410/dictionary-object-to-decision-tree-in-pydot
root_dict = {'root': root}
counter = 0
def draw(parent_name, child_name):
    global counter
    counter += 1
    # Strip the underscore and counter from each label for display purposes
    graph.add_node(pydot.Node(parent_name, label=parent_name.split('_')[0]))
    graph.add_node(pydot.Node(child_name, label=child_name.split('_')[0]))
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(node, parent=None):
    global counter
    for k,v in node.items():
        if isinstance(v, dict):
            # We start with the root node whose parent is None
            # print("k before", k)
            k = k + '_' + str(counter)
            # print("k after", k)
            if parent:
                # print("draw parent k", parent, k)
                draw(parent, k)
            print("visit v k", v, k)
            visit(v, k)
        else:
            # Draw the label using a distinct name by appending the counter
            v = v + '_' + str(counter)
            # print("draw parent v", parent, v)
            # Draw only if the child is not a False label
            if "False" not in v:
                draw(parent, v)

# Create instance of PyDot digraph for tree structure
graph = pydot.Dot(graph_type='digraph')
# Run recursive visit function beginning at root node
visit(root_dict)
# Produce output in a png file
graph.write_png('output.png')