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

# odoo base requirement + some others from camp2camp
COPY /base_requirements.txt /odoo/
RUN pip install -r base_requirements.txt

# install odoo + custom addons 
COPY /odoo/src /odoo/src
COPY /odoo/entrypoint/ /start-entrypoint.d/
COPY /phs.cfg /odoo/
COPY /setup.py /odoo/
COPY /odoo/local-src /odoo/local-src
COPY /odoo/addons /odoo/odoo/addons
COPY /requirements.txt /odoo/
COPY /odoo/migration.yml /odoo/
RUN pip install -r requirements.txt

# install external addons from OCA
COPY /ext_requirements.txt /odoo/
RUN pip install -r ext_requirements.txt

RUN chown -R 999:1000 /odoo

FROM local as debug

RUN pip install -r dev_requirements.txt

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
