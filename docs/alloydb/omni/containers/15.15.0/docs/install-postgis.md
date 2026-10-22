---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-postgis/
title: Install PostGIS for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:50.651804+00:00
---

# Install PostGIS for AlloyDB Omni  |  AlloyDB Omni using containers: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-postgis/

This page documents AlloyDB Omni version **15.15.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/overview)



Send feedback 

#  Install PostGIS for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-postgis)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-postgis)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install-postgis)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install-postgis)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install-postgis)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install-postgis)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-postgis)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-postgis)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install-postgis)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install-postgis)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install-postgis)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-postgis)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install-postgis)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install-postgis)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-postgis)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install-postgis)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-postgis)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install-postgis)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install-postgis)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-postgis)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install-postgis)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-postgis)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-postgis)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-postgis)

AlloyDB Omni does not include [the PostGIS extension](http://www.postgis.net/), but you can manually add it to an existing AlloyDB Omni installation by following the instructions on this page to add support for storing, indexing, and querying geospatial data. 

## Before you begin

Ensure that you've [installed AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install) on your system.

## Add PostGIS to your AlloyDB Omni installation

To add the PostGIS extension to your AlloyDB Omni installation, follow these steps:

  1. Find your installed AlloyDB Omni version labels: 

### Docker
         
         docker run --rm -it  google/alloydbomni cat VERSION.txt

### Podman
         
         podman run --rm -it  google/alloydbomni cat VERSION.txt

The output is similar to the following:
         
         AlloyDB Omni version: 15.15.0
         

Take note of the AlloyDB Omni version number; you need it in the next step.

  2. Set the `OMNI_VERSION` environment variable: 
         
         OMNI_VERSION=VERSION

Replace VERSION with the complete database server version from the previous step—for example, `15.15.0`.

  3. Create a new AlloyDB Omni container that includes PostGIS: 

### Linux
         
         mkdir ~/alloydb-omni-postgis
                tee ~/alloydb-omni-postgis/Dockerfile << EOF
                ARG OMNI_VERSION
                FROM google/alloydbomni:${OMNI_VERSION}
                RUN apt-get update &&   
                      apt-get install -y --no-install-recommends   
                      postgresql-15-postgis-3 &&   
                      apt-get purge -y --auto-remove &&   
                      rm -rf /var/lib/apt/lists/*
                EOF
                cd ~/alloydb-omni-postgis
                sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:$OMNI_VERSION .

### macOS
         
         mkdir ~/alloydb-omni-postgis
                tee ~/alloydb-omni-postgis/Dockerfile << EOF
                ARG OMNI_VERSION
                FROM google/alloydbomni:${OMNI_VERSION}
                RUN apt-get update &&   
                      apt-get install -y --no-install-recommends   
                      postgresql-15-postgis-3 &&   
                      apt-get purge -y --auto-remove &&   
                      rm -rf /var/lib/apt/lists/*
                EOF
                cd ~/alloydb-omni-postgis
                sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:$OMNI_VERSION .

  4. Create a new container with AlloyDB Omni named `my-omni-postgis`: 

### Docker
         
         docker run --name my-omni-postgis  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-postgis:OMNI_VERSION

### Podman
         
         podman run --name my-omni-postgis  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-postgis:OMNI_VERSION

  5. Connect to your database with the PostGIS extension:
         
         docker exec -it my-omni-postgis psql -h localhost -U postgres

  6. Enable PostGIS:
         
         CREATE EXTENSION IF NOT EXISTS POSTGIS;
            SELECT postgis_full_version();

The output looks similar to the following:
         
         postgres=# SELECT postgis_full_version();
            postgis_full_version
            --------------------------------------------------------------------------------------------------------------------------------
            POSTGIS="3.3.2 4975da8" [EXTENSION] PGSQL="150" GEOS="3.11.1-CAPI-1.17.1" PROJ="9.1.1" LIBXML="2.9.14" LIBJSON="0.16" LIBPROTOBUF="1.4.1" WAGYU="0.5.0 (Internal)"
            (1 row)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
