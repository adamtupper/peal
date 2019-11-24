"""
Tests for the genome encoding module.
"""

import pytest
from peal.genome import NodeTypes, NodeGene, ConnectionGene

__author__ = "Adam Tupper"
__copyright__ = "Adam Tupper"
__license__ = "mit"


def test_create_node_gene():
    """
    Test the creation of node genes.
    """
    node_gene = NodeGene(type=NodeTypes.INPUT)
    assert node_gene.type == NodeTypes.INPUT

def test_create_connection_gene():
    """
    Test the creation of connection genes.
    """
    in_node = NodeGene(NodeTypes.INPUT)
    out_node = NodeGene(NodeTypes.HIDDEN)
    connection_gene = ConnectionGene(
        in_node=in_node,
        out_node=out_node,
        weight=1.0,
        expressed=True,
        innov_num=0
    )

    assert connection_gene.in_node == in_node
    assert connection_gene.out_node == out_node
    assert connection_gene.weight == pytest.approx(1.0)
    assert connection_gene.expressed == True
    assert connection_gene.innov_num == 0
