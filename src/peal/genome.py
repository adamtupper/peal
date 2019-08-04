"""This module defines the genome encoding used by NEAT.

Genomes consist of a list connection genes, which themselves each consist of two node genes. Classes for a genome,
connection gene and node gene are defined in this module.

Example:

Attributes:
    global_innov_num:

Todo:
    
Author: Adam Tupper
Since: 31/07/19
Updated: 04/08/19
"""


global_innov_num = 0


class ConnectionGene():
    """Defines a connection gene used in the genome encoding.

    Attributes:
        ...
    """

    def __init__(self, in_node, out_node, weight, expressed, innov_num):
        """Creates a ConnectionGene object with the required properties.

        Args:
            in_node:
            out_node:
            weight:
            expressed:
            innov_num:
        """
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.expressed = expressed
        self.innov_num = innov_num


class NodeGene():
    """Defines a node gene used in the genome encoding.

    Attributes:
        ...
    """

    def __init__(self, type):
        """Creates a NodeGene object with the required properties.

        Args:
            type:
        """
        self.type = type


class Genome():
    """Defines a genome used to encode a neural network.

    Attributes:
        ...
    """

    def __init__(self, num_inputs, num_outputs):
        """Creates a Genome objects with the required properties.

        Args:
            num_inputs:
            num_outputs:
        """
        self.node_genes = []
        self.connection_genes = []

        # Create the required number of input and output nodes
        for _ in range(0, num_inputs):
            self.node_genes.append(NodeGene(type="input"))

        for _ in range(0, num_outputs):
            self.node_genes.append(NodeGene(type="output"))

        # Add initial connections
        for i in range(0, num_inputs):
            for j in range(num_inputs, num_inputs + num_outputs):
                new_connection_gene = ConnectionGene(in_node=self.node_genes[i],
                                                     out_node=self.node_genes[j],
                                                     weight=1.0,
                                                     expressed=True,
                                                     innov_num=global_innov_num)
                self.connection_genes.append(new_connection_gene)
                global_innov_num += 1
