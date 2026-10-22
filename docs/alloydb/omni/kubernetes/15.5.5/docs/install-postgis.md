---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-postgis/
title: Install PostGIS for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:11:35.385370+00:00
---

# Install PostGIS for AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-postgis/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Install PostGIS for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-postgis)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/install-postgis)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/install-postgis)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-postgis)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/install-postgis)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/install-postgis)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-postgis)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/install-postgis)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/install-postgis)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/install-postgis)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/install-postgis)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/install-postgis)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/install-postgis)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install-postgis)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install-postgis)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/install-postgis)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-postgis)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install-postgis)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/install-postgis)

AlloyDB Omni does not include [the PostGIS extension](http://www.postgis.net/), but you can manually add it to an existing AlloyDB Omni installation by following the instructions on this page to add support for storing, indexing, and querying geospatial data. 

## Before you begin

Ensure that you've [installed AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install) on your system.

###  Single-server 

## Add PostGIS to your AlloyDB Omni installation

To add the PostGIS extension to your AlloyDB Omni installation, follow these steps:

  1. Find your installed AlloyDB Omni version labels: 

### Docker
         
         docker run --rm -it  google/alloydbomni cat VERSION.txt

### Podman
         
         podman run --rm -it  google/alloydbomni cat VERSION.txt

The output is similar to the following:
         
         AlloyDB Omni version: 15.5.5
         

Take note of the AlloyDB Omni version number; you need it in the next step.

  2. Set the `OMNI_VERSION` environment variable: 
         
         OMNI_VERSION=VERSION

Replace VERSION with the complete database server version from the previous step—for example, `15.5.5`.

  3. Create a new AlloyDB Omni container that includes PostGIS: 

### Docker
         
         mkdir ~/alloydb-omni-postgis
            tee -a ~/alloydb-omni-postgis/Dockerfile << EOF
            ARG OMNI_VERSION
            FROM postgres:15-bookworm AS postgres
         
            RUN apt-get update && \
            apt-get install -y --no-install-recommends \
            postgresql-15-postgis-3 && \
            apt-get purge -y --auto-remove && \
            rm -rf /var/lib/apt/lists/*
         
            FROM google/alloydbomni:${OMNI_VERSION}
         
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis-3.so /usr/lib/postgresql/15/lib/postgis-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_raster-3.so /usr/lib/postgresql/15/lib/postgis_raster-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_topology-3.so /usr/lib/postgresql/15/lib/postgis_topology-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/address_standardizer-3.so /usr/lib/postgresql/15/lib/address_standardizer-3.so
            COPY --from=postgres /usr/share/postgresql/15/extension/address_standardizer* /usr/lib/postgresql/15/share/extension/
            COPY --from=postgres /usr/share/postgresql/15/extension/postgis* /usr/lib/postgresql/15/share/extension/
         
            COPY --from=postgres /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
            COPY --from=postgres /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
         
            COPY --from=postgres /usr/lib/x86_64-linux-gnu/liblapack.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/x86_64-linux-gnu/libblas.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/libarmadillo.so.11 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libogdi.so.4.1 /usr/lib/
            COPY --from=postgres /usr/share/proj/proj.db /usr/share/proj/proj.db
         
            EOF
         cd ~/alloydb-omni-postgis
         sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:$OMNI_VERSION .

### Podman
         
         mkdir ~/alloydb-omni-postgis
            tee -a ~/alloydb-omni-postgis/Dockerfile << EOF
            ARG OMNI_VERSION
            FROM postgres:15-bookworm AS postgres
         
            RUN apt-get update && \
            apt-get install -y --no-install-recommends \
            postgresql-15-postgis-3 && \
            apt-get purge -y --auto-remove && \
            rm -rf /var/lib/apt/lists/*
         
            FROM google/alloydbomni:${OMNI_VERSION}
         
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis-3.so /usr/lib/postgresql/15/lib/postgis-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_raster-3.so /usr/lib/postgresql/15/lib/postgis_raster-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_topology-3.so /usr/lib/postgresql/15/lib/postgis_topology-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/address_standardizer-3.so /usr/lib/postgresql/15/lib/address_standardizer-3.so
            COPY --from=postgres /usr/share/postgresql/15/extension/address_standardizer* /usr/lib/postgresql/15/share/extension/
            COPY --from=postgres /usr/share/postgresql/15/extension/postgis* /usr/lib/postgresql/15/share/extension/
         
            COPY --from=postgres /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
            COPY --from=postgres /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
         
            COPY --from=postgres /usr/lib/x86_64-linux-gnu/liblapack.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/x86_64-linux-gnu/libblas.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/libarmadillo.so.11 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libogdi.so.4.1 /usr/lib/
            COPY --from=postgres /usr/share/proj/proj.db /usr/share/proj/proj.db
         
            EOF
         cd ~/alloydb-omni-postgis
         sudo podman build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:$OMNI_VERSION .

### Docker
         
         mkdir ~/alloydb-omni-postgis
            tee -a ~/alloydb-omni-postgis/Dockerfile << EOF
            ARG OMNI_VERSION
            FROM postgres:15-bookworm AS postgres
         
            RUN apt-get update && \
            apt-get install -y --no-install-recommends \
            postgresql-15-postgis-3 && \
            apt-get purge -y --auto-remove && \
            rm -rf /var/lib/apt/lists/*
         
            FROM google/alloydbomni:${OMNI_VERSION}
         
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis-3.so /usr/lib/postgresql/15/lib/postgis-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_raster-3.so /usr/lib/postgresql/15/lib/postgis_raster-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_topology-3.so /usr/lib/postgresql/15/lib/postgis_topology-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/address_standardizer-3.so /usr/lib/postgresql/15/lib/address_standardizer-3.so
            COPY --from=postgres /usr/share/postgresql/15/extension/address_standardizer* /usr/lib/postgresql/15/share/extension/
            COPY --from=postgres /usr/share/postgresql/15/extension/postgis* /usr/lib/postgresql/15/share/extension/
         
            COPY --from=postgres /usr/lib/aarch64-linux-gnu/ /usr/lib/aarch64-linux-gnu/
            COPY --from=postgres /lib/aarch64-linux-gnu/ /lib/aarch64-linux-gnu/
         
            COPY --from=postgres /usr/lib/aarch64-linux-gnu/liblapack.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/aarch64-linux-gnu/libblas.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/libarmadillo.so.11 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libogdi.so.4.1 /usr/lib/
            COPY --from=postgres /usr/share/proj/proj.db /usr/share/proj/proj.db
         
            EOF
         cd ~/alloydb-omni-postgis
         sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:$OMNI_VERSION .

### Podman
         
         mkdir ~/alloydb-omni-postgis
            tee -a ~/alloydb-omni-postgis/Dockerfile << EOF
            ARG OMNI_VERSION
            FROM postgres:15-bookworm AS postgres
         
            RUN apt-get update && \
            apt-get install -y --no-install-recommends \
            postgresql-15-postgis-3 && \
            apt-get purge -y --auto-remove && \
            rm -rf /var/lib/apt/lists/*
         
            FROM google/alloydbomni:${OMNI_VERSION}
         
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis-3.so /usr/lib/postgresql/15/lib/postgis-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so /usr/lib/postgresql/15/lib/postgis_sfcgal-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_raster-3.so /usr/lib/postgresql/15/lib/postgis_raster-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/postgis_topology-3.so /usr/lib/postgresql/15/lib/postgis_topology-3.so
            COPY --from=postgres /usr/lib/postgresql/15/lib/address_standardizer-3.so /usr/lib/postgresql/15/lib/address_standardizer-3.so
            COPY --from=postgres /usr/share/postgresql/15/extension/address_standardizer* /usr/lib/postgresql/15/share/extension/
            COPY --from=postgres /usr/share/postgresql/15/extension/postgis* /usr/lib/postgresql/15/share/extension/
         
            COPY --from=postgres /usr/lib/aarch64-linux-gnu/ /usr/lib/aarch64-linux-gnu/
            COPY --from=postgres /lib/aarch64-linux-gnu/ /lib/aarch64-linux-gnu/
         
            COPY --from=postgres /usr/lib/aarch64-linux-gnu/liblapack.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/aarch64-linux-gnu/libblas.so.3 /usr/lib/
            COPY --from=postgres /usr/lib/libarmadillo.so.11 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libmfhdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libdfalt.so.0 /usr/lib/
            COPY --from=postgres /usr/lib/libogdi.so.4.1 /usr/lib/
            COPY --from=postgres /usr/share/proj/proj.db /usr/share/proj/proj.db
         
            EOF
         cd ~/alloydb-omni-postgis
         sudo podman build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:$OMNI_VERSION .

  4. Create a new container with AlloyDB Omni named `my-omni-postgis`: 

### Docker
         
         docker run --name my-omni-postgis  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-postgis:OMNI_VERSION

### Podman
         
         podman run --name my-omni-postgis  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-postgis:OMNI_VERSION

  5. Connect to your database with the PostGIS extension: 

### Docker
         
         docker exec -it my-omni-postgis psql -h localhost -U postgres

### Podman
         
         podman exec -it my-omni-postgis psql -h localhost -U postgres

  6. Enable PostGIS: 
         
         CREATE EXTENSION IF NOT EXISTS POSTGIS;
         
         SELECT postgis_full_version();

The output looks similar to the following: 
         
         postgis_full_version
         ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         POSTGIS="3.4.2 c19ce56" [EXTENSION] PGSQL="150" GEOS="3.11.1-CAPI-1.17.1" PROJ="9.1.1 NETWORK_ENABLED=OFF URL_ENDPOINT= USER_WRITABLE_DIRECTORY=/var/lib/postgresql/.local/share/proj DATABASE_PATH=/usr/share/proj/proj.db" LIBXML="2.9.14" LIBJSON="0.16" LIBPROTOBUF="1.4.1" WAGYU="0.5.0 (Internal)"
         (1 row)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
