include .env

onDB:
	@docker-compose up

removeDB:
	sudo rm -rf ./db/psql/pgdata
	@docker-compose down --rmi local

run:
	@cd src; uvicorn --host ${APP_HOST} --port ${APP_PORT} --reload --reload-dir . --workers ${WORKERS} --loop ${LOOP} main:app