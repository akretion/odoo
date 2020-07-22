FROM camptocamp/odoo-project:12.0-latest as dist
MAINTAINER 1001Pharmacies <technique+docker@1001pharmacies.com>
ARG DOCKER_BUILD_DIR

WORKDIR /odoo

FROM dist as local

# install requirements
COPY --chown=999:1000 /odoo/requirements.txt /odoo/
RUN pip install -r /odoo/requirements.txt

# install odoo
COPY --chown=999:1000 /odoo/src /odoo/src
RUN pip install -e /odoo/src

# install external addons
COPY --chown=999:1000 /odoo/external-src /odoo/external-src
RUN pip install -r /odoo/external-src/requirements.txt

COPY --chown=999:1000 /odoo/migration.yml /odoo/

FROM local as debug

COPY /odoo/debug_requirements.txt /odoo/
RUN pip install -r debug_requirements.txt

EXPOSE 9999

CMD ["gosu", "odoo", "python3", "-m", "ptvsd", "--host", "0.0.0.0", "--port", "9999", "--multiprocess", "/odoo/src/odoo-bin", "-c", "/etc/odoo.cfg"],

FROM local as tests
ARG BRANCH
ARG TARGET
ARG VERSION
LABEL com.1001pharmacies.branch=${BRANCH}
LABEL com.1001pharmacies.target=${TARGET}
LABEL com.1001pharmacies.version=${VERSION}

# install local addons
COPY --chown=999:1000 /odoo/local-src /odoo/local-src
COPY --chown=999:1000 /phs.cfg /
COPY --chown=999:1000 /setup.py /
RUN ln -s /odoo/local-src /odoo/addons
RUN pip install -e /

COPY --chown=999:1000 /odoo/entrypoint/ /start-entrypoint.d/

FROM tests as preprod
COPY /make /odoo/make
COPY /Makefile /odoo/Makefile
FROM preprod as prod
