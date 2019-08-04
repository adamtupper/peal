"""This module defines the genome encoding used by NEAT.

Genomes consist of a list connection genes, which themselves each consist of two node genes. Classes for a genome,
connection gene and node gene are defined in this module.

Example:

Attributes:

Todo:
    
Author: Adam Tupper
Since: 31/07/19
Updated: 31/07/19
"""


class ConnectionGene():
    """Defines a connection gene used in the genome encoding.

    Attributes:
        ...
    """

    def __init__(self, in_node, out_node, weight, expressed, innovation_number):
        """Creates a ConnectionGene object with the required properties.

        Args:
            in_node:
            out_node:
            weight:
            expressed:
            innovation_number:
        """


class NodeGene():
    """Defines a node gene used in the genome encoding.

    Attributes:
        ...
    """

    def __init__(self, inputs, hidden_nodes, outputs):
        """Creates a NodeGene object with the required properties.

        Args:
            inputs:
            hidden_nodes:
            outputs:
        """


class Genome():
    """Defines a genome used to encode a neural network.

    Attributes:
        ...
    """

    def __init__(self, input_nodes, output_nodes):
        """Creates a Genome objects with the required properties.

        Args:
            input_nodes:
            output_nodes:
        """
