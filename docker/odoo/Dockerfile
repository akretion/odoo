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

# install local addons in docker entrypoint
COPY --chown=999:1000 /odoo/phs.cfg /odoo/phs.cfg
COPY --chown=999:1000 /odoo/setup.py /odoo/setup.py
RUN ln -s /odoo/local-src /odoo/addons
RUN ln -s /odoo /odoo/odoo

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

# copy local files
COPY --chown=999:1000 /odoo/local-src /odoo/local-src
COPY --chown=999:1000 /odoo/entrypoint/ /start-entrypoint.d/
COPY --chown=999:1000 /odoo/script/ /odoo/script/

FROM tests as preprod
COPY /make /odoo/make
COPY /Makefile /odoo/Makefile
FROM preprod as prod
