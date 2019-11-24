"""
Tests for the genome encoding module.
"""

import pytest
from peal.genome import NodeTypes, NodeGene

__author__ = "Adam Tupper"
__copyright__ = "Adam Tupper"
__license__ = "mit"


def test_create_node_gene():
    """
    Test the creation of node genes.
    """
    node_gene = NodeGene(type=NodeTypes.INPUT)
    assert node_gene.type == NodeTypes.INPUT
