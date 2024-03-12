from typing import List
import pytest


class Solution:
    def trav(self, fr, to, gp, v, vis):
        if fr not in gp or to not in gp:
            return -1.0

        if fr == to:
            return v

        if to in gp[fr]:
            return v*gp[fr][to]

        vis[fr] = 1
        for nto, val in gp[fr].items():
            if nto not in vis:
                nv = v * val
                res = self.trav(nto, to, gp, nv, vis)
                if res > 0.0:
                    return res

        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a --> b : 2
        b --> c : 3
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

        - build graph
        - traverse graph to find the element.
        {a: {b: 2}, b: {a: 0.5, c: 3}, c: {b: 1/3}}

        trav: a-c

        """
        gr = {}
        for i, e in enumerate(equations):
            fr = e[0]
            to = e[1]
            val = values[i]

            if fr not in gr:
                gr[fr] = {}
            gr[fr][to] = val

        for i, e in enumerate(equations):
            fr = e[0]
            to = e[1]
            val = values[i]

            if to not in gr:
                gr[to] = {}
            gr[to][fr] = 1/val

        res = []
        for q in queries:
            fr = q[0]
            to = q[1]
            a = round(self.trav(fr, to, gr, 1.0, {}), 5)
            res.append(a)

        return res



@pytest.mark.parametrize("eqs,vals,qs,exp", [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]),
    ([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]],[3.75000,0.40000,5.00000,0.20000]),
    ([["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]],[0.50000,2.00000,-1.00000,-1.00000]),
    ([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]],[360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000])
])
def test_calc(eqs, vals, qs, exp):
    assert Solution().calcEquation(eqs, vals, qs) == exp
