FROM camptocamp/odoo-project:12.0-latest as dist
MAINTAINER 1001Pharmacies <technique+docker@1001pharmacies.com>
ARG DOCKER_BUILD_DIR

COPY /odoo/src /odoo/src
COPY /odoo/addons /odoo/odoo/addons

COPY /requirements.txt /odoo/
COPY /setup.py /odoo/
COPY /phs.cfg /odoo/

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

RUN pip install -r requirements.txt


FROM dist as local

COPY /odoo/src /odoo/src
COPY /odoo/setup.py /odoo/
COPY /odoo/VERSION /odoo/
COPY /odoo/bin/odoo /odoo-bin-compat/odoo

RUN pip install -e /odoo
RUN pip install -e /odoo/src

COPY /odoo/migration.yml /odoo/

FROM local as debug

RUN pip install ptvsd

EXPOSE 8888

CMD ["gosu", "odoo", "python", "-m", "ptvsd", "--host", "0.0.0.0", "--port", "8888", "--multiprocess", "/odoo/src/odoo.py", "-c", "/etc/odoo.cfg"],

FROM local as tests
ARG BRANCH
ARG TARGET
ARG VERSION
LABEL com.1001pharmacies.branch=${BRANCH}
LABEL com.1001pharmacies.target=${TARGET}
LABEL com.1001pharmacies.version=${VERSION}

COPY /odoo/entrypoint/ /start-entrypoint.d/
COPY /odoo/external-src/ /odoo/external-src/
COPY /odoo/local-src/ /odoo/local-src/
COPY /odoo/script/ /odoo/script/
RUN chown -R 999:1000 /odoo

FROM tests as preprod
FROM preprod as prod
