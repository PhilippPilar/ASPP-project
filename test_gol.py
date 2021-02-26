import GameOfLife.patterns as pt
import GameOfLife.gameoflife as gol
import numpy as np

def test_random():
    s0 = np.loadtxt('state0_test.txt')
    s1 = np.loadtxt('state1_test.txt')
    Gtest = gol.GameOfLife(s0)
    Gtest.evolve(1000,plot='off')
    assert np.array_equal(Gtest.state,s1)
    