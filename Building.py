class Building:
    def __init__(self, minf, maxf, numelev):
        self.minf = minf
        self.maxf = maxf
        self.numelv = numelev

    def minfloor(self):
        return self.minf

    def maxfloor(self):
        return self.maxf

    def numelevator(self):
        return self.numelv


