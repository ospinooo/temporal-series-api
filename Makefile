


run:
	python -m app -vvvvvv

up:
	docker-compose up


build_docker:
	docker build -t tornado-temporal-series-app .

run_docker:	
	docker run -p ${PORT}:${PORT} \
		-e PORT="8887" \
		-e INFLUX_HOST="localhost" \
		-e INFLUX_PORT="8086"  \
		-e INFLUX_USER="admin" \
		-e INFLUX_PASS="1" \
		-e DEBUG="1" \
	 	tornado-temporal-series-app