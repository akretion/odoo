##
# APP

APP_TYPE := app python
include make/include.mk

DOCKER_SERVICE := odoo12

.PHONY: install
install: install-infra install-pgsql-database-odoo12 bootstrap ## Install application

.PHONY: debug
debug: DOCKER_BUILD_TARGET := debug
debug: MOUNT_DEBUG := true
debug: build up;## Launch application in debug mode

.PHONY: reset
reset: down
	psql -U odoo -d template1 -h localhost -c "DROP DATABASE IF EXISTS odoo12;"
	psql -U odoo -d template1 -h localhost -c "CREATE DATABASE odoo12;"
reset: ARGS=odoo -c /etc/odoo.cfg -i web_environment_ribbon,phs_base --stop-after-init 
reset: run

.PHONY: upgrade
upgrade: MODULES ?= all
upgrade: ARGS=odoo --stop-after-init -u $(MODULES)
upgrade: run ## Upgrade application $(MODULES) and exit

.PHONY: test
test: DOCKER_BUILD_TARGET := test
test: MOUNT_DEBUG := true
test: MODULES ?= all
test: ARGS=odoo -c /etc/odoo.cfg --stop-after-init --test-enable -u $(MODULES)
test: run
