##
# APP

APP_TYPE := app python
include make/include.mk

DOCKER_SERVICE := odoo12

.PHONY: install
install: install-infra install-pgsql-database-odoo bootstrap ## Install application

.PHONY: debug
debug: DOCKER_BUILD_TARGET := debug
debug: MOUNT_DEBUG := true
debug: build up ## Launch application in debug mode

.PHONY: upgrade
upgrade: MODULES ?= all
upgrade: ARGS=odoo --stop-after-init -u $(MODULES)
upgrade: run ## Upgrade application $(MODULES) and exit

.PHONY: test
test: DOCKER_BUILD_TARGET := test
test: MOUNT_DEBUG := true
test: MODULES ?= all
test: ARGS=odoo --stop-after-init --test-enable -u $(MODULES)
test: run
