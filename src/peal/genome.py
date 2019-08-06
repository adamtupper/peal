"""This module defines the genome encoding used by NEAT.

Genomes consist of a list connection genes, which themselves each consist of two
node genes. Classes for a genome, connection gene and node gene are defined in
this module.

Example:

Attributes:
    global_innov_num:

Todo:
    
Author: Adam Tupper
Since: 31/07/19
Updated: 04/08/19
"""

from enum import Enum
import random
from random import randrange

global_innov_num = 0


class NodeTypes(Enum):
    """Define the types for nodes in the network.
    """
    INPUT = 0
    HIDDEN = 1
    OUTPUT = 2


class ConnectionGene:
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


class NodeGene:
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


class Genome:
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
        global global_innov_num
        self.node_genes = []
        self.connection_genes = []

        # Create the required number of input and output nodes
        for _ in range(0, num_inputs):
            self.node_genes.append(NodeGene(type=NodeTypes.INPUT))

        for _ in range(0, num_outputs):
            self.node_genes.append(NodeGene(type=NodeTypes.OUTPUT))

        # Add initial connections
        for i in range(0, num_inputs):
            for j in range(num_inputs, num_inputs + num_outputs):
                new_connection_gene = ConnectionGene(
                    in_node=i,
                    out_node=j,
                    weight=1.0,
                    expressed=True,
                    innov_num=global_innov_num
                )
                self.connection_genes.append(new_connection_gene)
                global_innov_num += 1

    def add_connection(self):
        """Performs an 'add connection' structural mutation.
        
        A single connection with a random weight is added between two previously
        unconnected nodes.
        """
        global global_innov_num
        max_retries = 5
        num_retries = 0
        connection_added = False

        while num_retries < max_retries and not connection_added:
            in_node_idx = randrange(0, len(self.node_genes))
            out_node_idx = randrange(0, len(self.node_genes))

            existing_connection = False
            for connection_gene in self.connection_genes:
                if (connection_gene.in_node == in_node_idx and
                        connection_gene.out_node == out_node_idx):
                    existing_connection = True

            if not existing_connection:
                self.connection_genes.append(ConnectionGene(
                    in_node=in_node_idx,
                    out_node=out_node_idx,
                    weight=random.uniform(0, 1),
                    expressed=True,
                    innov_num=global_innov_num
                ))
                global_innov_num += 1
                connection_added = True

            num_retries += 1

    def add_node(self):
        """Performs an 'add node' structural mutation.
        
        An existing connection is split and the new node is placed where the old
        connection used to be. The old connection is disabled and two new
        connection genes are added. The new connection leading into the new node
        receives a weight of 1.0 and the connection leading out of the new node
        receives the old connection weight.
        """
        global global_innov_num
        self.node_genes.append(NodeGene(type=NodeTypes.HIDDEN))
        old_connection_gene_idx = randrange(0, len(self.node_genes))
        old_connection_gene = self.connection_genes[old_connection_gene_idx]
        self.connection_genes[old_connection_gene_idx].expressed = False
        new_in_connection_gene = ConnectionGene(in_node=old_connection_gene.in_node,
                                                out_node=len(self.node_genes) - 1,
                                                weight=1.0,
                                                expressed=True,
                                                innov_num=global_innov_num)
        global_innov_num += 1
        new_out_connection_gene = ConnectionGene(in_node=len(self.node_genes) - 1,
                                                 out_node=old_connection_gene.out_node,
                                                 weight=old_connection_gene.weight,
                                                 expressed=True,
                                                 innov_num=global_innov_num)
        global_innov_num += 1
        self.connection_genes.append(new_in_connection_gene)
        self.connection_genes.append(new_out_connection_gene)
