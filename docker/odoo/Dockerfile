FROM camptocamp/odoo-project:12.0-latest as dist
MAINTAINER 1001Pharmacies <technique+docker@1001pharmacies.com>
ARG DOCKER_BUILD_DIR

# RUN apt-get update \
#  && apt-get -fy upgrade \
#  && apt-get -fy remove libpq5 \
#  && apt-get -fy install --no-install-recommends -t jessie \
#             libpq-dev \
#             make \
#             postgresql-client \
#  && apt-get -fy install --no-install-recommends $BUILD_PACKAGE \
#  && pip install -r /odoo/requirements.txt \
#  && apt-get -fy remove $BUILD_PACKAGE \
#  && apt-get -fy purge --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $PURGE_PACKAGE \
#  && apt-get -fy install --no-install-recommends \
#             libmagickwand-dev \
#  && rm -rf /var/lib/apt/lists/* /root/.cache/pip/*

WORKDIR /odoo

FROM dist as local

COPY /odoo/addons /odoo/odoo/addons
COPY /odoo/entrypoint/ /start-entrypoint.d/
COPY /odoo/local-src /odoo/local-src
COPY /odoo/migration.yml /odoo/
COPY /odoo/src /odoo/src
COPY /phs.cfg /odoo/
COPY /requirements.txt /odoo/
COPY /ext_requirements.txt /odoo/
COPY /setup.py /odoo/

RUN chown -R 999:1000 /odoo
# RUN pip install -r ext_requirements.txt

FROM local as debug

RUN pip install ptvsd

EXPOSE 9999

CMD ["gosu", "odoo", "python3", "-m", "ptvsd", "--host", "0.0.0.0", "--port", "9999", "--multiprocess", "/odoo/src/odoo-bin", "-c", "/etc/odoo.cfg"],

FROM local as tests
ARG BRANCH
ARG TARGET
ARG VERSION
LABEL com.1001pharmacies.branch=${BRANCH}
LABEL com.1001pharmacies.target=${TARGET}
LABEL com.1001pharmacies.version=${VERSION}

FROM tests as preprod
FROM preprod as prod
