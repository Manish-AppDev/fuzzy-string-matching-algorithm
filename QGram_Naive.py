import unittest
import re
import csv

_SPACE_PATTERN = re.compile("\\s+")

class ShingleBased:

    def __init__(self, k=3):
        self.k = k

    def get_k(self):
        return self.k

    def get_profile(self, string):
        shingles = dict()
        no_space_str = _SPACE_PATTERN.sub(" ", string)
        for i in range(len(no_space_str) - self.k + 1):
            shingle = no_space_str[i:i + self.k]
            old = shingles.get(shingle)
            if old:
                shingles[str(shingle)] = int(old + 1)
            else:
                shingles[str(shingle)] = 1
        return shingles

class StringDistance:

    def distance(self, s0, s1):
        raise NotImplementedError()


class NormalizedStringDistance(StringDistance):

    def distance(self, s0, s1):
        raise NotImplementedError()


class MetricStringDistance(StringDistance):

    def distance(self, s0, s1):
        raise NotImplementedError()

class QGram(ShingleBased, StringDistance):

    def __init__(self, k=3):
        super().__init__(k)

    def distance(self, s0, s1):
        if s0 is None:
            raise TypeError("Argument s0 is NoneType.")
        if s1 is None:
            raise TypeError("Argument s1 is NoneType.")
        if s0 == s1:
            return 0.0

        profile0 = self.get_profile(s0)
        profile1 = self.get_profile(s1)
        return self.distance_profile(profile0, profile1)

    @staticmethod
    def distance_profile(profile0, profile1):
        union = set()
        for k in profile0.keys():
            union.add(k)
        for k in profile1.keys():
            union.add(k)
        agg = 0
        for k in union:
            v0, v1 = 0, 0
            if profile0.get(k) is not None:
                v0 = int(profile0.get(k))
            if profile1.get(k) is not None:
                v1 = int(profile1.get(k))
            agg += abs(v0 - v1)
        return agg

class TestQGram(unittest.TestCase):

    def readMyFile(filename):
        data = []
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                data.append(row[0])            
        return data

    def test_qgram(self):
        data = TestQGram.readMyFile('Movie.csv')
        Str2 = input("Enter String To Be Searched:")
        Movie=[[0 for col in range(2)] for row in range(len(data))]
        a = QGram(2)
        for i in range(len(data)):
            Str1 = data[i]
            Movie[i][0] = Str1 
            Movie[i][1] = a.distance(Str1, Str2)
    
        Res = sorted(Movie, key = lambda x: x[1], reverse = False)[:6]
        print(Res)

if __name__ == "__main__":
    unittest.main()
