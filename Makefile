clean:
	rm -rf tests/*.log tests/*.nt
	rm -rf cache/
	rm -rf limespy/cache
limes-test-csv-csv:
	java -jar limes/LIMES.jar tests/cities-cities.xml
limes-test-csv-sparql:
	java -jar limes/LIMES.jar tests/cities-dbpedia.xml
