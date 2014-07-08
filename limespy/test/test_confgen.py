from limespy.confgen import LimesConfigGenerator

class TestLimesConfigGenerator(object):
    def __init__(self):
        self.confgen = LimesConfigGenerator()
        pass

    def testConfigCsvSparql(self):
        sourceUri = "/home/ivan/Soft/Installed/LIMES-test/cities.csv"
        sourceProperty = "City AS lowercase"
        sourceType = "csv"
        targetUri = "http://dbpedia.org/sparql"
        targetProperty = "rdfs:label AS nolang->lowercase"
        targetType = "sparql"
        metricString = "levenshtein(x.City, y.rdfs:label)"
        acceptanceThreshold = "0.95"
        acceptanceOutfile = "foo.nt"
        reviewThreshold = "0.9"
        reviewOutfile = "foo2.nt"

    def testConfigCsvCsv(self):
        sourceUri = "/home/ivan/Soft/Installed/LIMES-test/cities.csv"
        sourceProperty = "City"
        sourceType = "csv"
        sourceVar = "?x"
        sourceRestriction = ""
        targetUri = "/home/ivan/Soft/Installed/LIMES-test/cities.csv"
        targetProperty = "City"
        targetType = "csv"
        targetVar = "?y"
        targetRestriction = ""
        metricString = "levenshtein(x.City, y.City)"
        acceptanceThreshold = "0.95"
        acceptanceOutfile = "foo.nt"
        acceptanceRelation = "owl:sameAs"
        reviewThreshold = "0.9"
        reviewOutfile = "foo2.nt"
        reviewRelation = "owl:sameAs"

        config = self.confgen.generateMinimalConfig(sourceUri, sourceProperty, sourceType, sourceVar, sourceRestriction,
                                             targetUri, targetProperty, targetType, targetVar, targetRestriction,
                                             metricString, 
                                             acceptanceThreshold, acceptanceOutfile, acceptanceRelation,
                                             reviewThreshold, reviewOutfile, reviewRelation)

        f = open('/tmp/limestestcsvcsv.xml', 'wb+')
        f.write(config)
        f.close()
        from limespy.limes import LimesRunner 
        limesRunner = LimesRunner()
        print limesRunner.run('/tmp/limestestcsvcsv.xml')

if __name__ == "__main__":
    test = TestLimesConfigGenerator()
    test.testConfigCsvCsv()
            


