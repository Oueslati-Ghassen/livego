dockerize:
	docker build -t livego/testing:latest .
	docker run -p 1935:1935 -p 7001:7001 -p 7002:7002 -p 8090:8090 -d livego/testing:latest
