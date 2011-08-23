__author__="Gregory McWhirter"
__date__ ="$Aug 22, 2011 4:36:18 PM$"

import random
import math

class RandomDynamics:

    # The system is:
    #
    # dx/dt = ax + by
    # dy/dt = cx + dy
    #
    #

    def __init__(self, min = -1, max = 1, **kwargs):
        self.a = kwargs.get('a', random.uniform(min, max))
        self.b = kwargs.get('b', random.uniform(min, max))
        self.c = kwargs.get('c', random.uniform(min, max))
        self.d = kwargs.get('d', random.uniform(min, max))

        if self.a < min or self.a > max:
            raise ValueError("Parameter a out of bounds.")
        if self.b < min or self.b > max:
            raise ValueError("Parameter b out of bounds.")
        if self.c < min or self.c > max:
            raise ValueError("Parameter c out of bounds.")
        if self.d < min or self.d > max:
            raise ValueError("Parameter d out of bounds.")

    def get_discriminant(self):
        return (self.a - self.d) ** 2 + (4 * self.b * self.c)

    def has_complex_eigenvalues(self):
        return self.get_discriminant() < 0.

    def has_distinct_eigenvalues(self):
        return self.get_discriminant() != 0.

    def get_node_type(self):
        if self.has_complex_eigenvalues():
            if (self.a + self.d) > 0.:
                return "source spiral"
            elif (self.a + self.d) < 0.:
                return "sink spiral"
            else:
                return "center"
        elif self.has_distinct_eigenvalues():
            sqr = math.sqrt(self.get_discriminant())
            rpt = (self.a + self.d)
            if abs(sqr) > abs(rpt):
                return "saddle"
            elif rpt < 0.:
                return "sink"
            else:
                return "source"
        else:
            return "degenerate"


if __name__ == "__main__":
    results = {"source spiral": 0, "sink spiral": 0, "center": 0, "saddle": 0, "sink": 0, "source": 0, "degenerate": 0}

    for i in range(int(1e6)):
        r = RandomDynamics()
        results[r.get_node_type()] += 1


    print "Results:"
    for key in results:
        val = results[key]
        print "{0:15}: {1:10} ({2:.3f})".format(key, val, val / float(1e6))