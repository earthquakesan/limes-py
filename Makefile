clean:
	rm -rf tests/*.log tests/*.nt
	rm -rf cache/
	rm -rf limespy/cache
limes-test:
	java -jar limes/LIMES.jar tests/cities.xml
