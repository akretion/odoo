make down
psql -U odoo -d template1 -h localhost -c "DROP DATABASE odoo12;"
psql -U odoo -d template1 -h localhost -c "CREATE DATABASE odoo12;"
make run 'odoo -d odoo12 -i web-environment-ribbon,phs_base --stop-after-init'
make up logs