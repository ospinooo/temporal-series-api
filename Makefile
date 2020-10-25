


run:
	python -m app


influx_up:
	docker run -p 8086:8086 \
      -v ${PWD}/docker/influxdb:/var/lib/influxdb \
      influxdb

