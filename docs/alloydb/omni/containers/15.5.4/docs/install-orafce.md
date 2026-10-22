---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-orafce/
title: Install Orafce for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:10.145084+00:00
---

# Install Orafce for AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-orafce/

This page documents AlloyDB Omni version **15.5.4** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)



Send feedback 

#  Install Orafce for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-orafce)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-orafce)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install-orafce)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install-orafce)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install-orafce)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install-orafce)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-orafce)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-orafce)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install-orafce)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install-orafce)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install-orafce)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-orafce)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install-orafce)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install-orafce)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-orafce)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install-orafce)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-orafce)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install-orafce)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install-orafce)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-orafce)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install-orafce)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-orafce)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-orafce)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-orafce)

AlloyDB Omni does not include [the Orafce extension](https://github.com/orafce/orafce), but you can manually add it to an existing AlloyDB Omni installation by following the instructions on this page to provide additional functions and operators from the Oracle database. 

## Before you begin

Ensure that you've [installed AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install) on your system.

###  Single-server 

## Add Orafce to your AlloyDB Omni installation

To add the Orafce extension to your AlloyDB Omni installation, follow these steps:

  1. Find your installed AlloyDB Omni version labels: 
         
         docker run --rm -it  google/alloydbomni cat VERSION.txt

The output is similar to the following:
         
         AlloyDB Omni version: 15.5.4
         

Take note of the AlloyDB Omni version number; you need it in the next step.

  2. Set the `OMNI_VERSION` environment variable: 
         
         OMNI_VERSION=VERSION

Replace VERSION with the complete database server version from the previous step—for example, `15.5.4`.

  3. Create a new AlloyDB Omni container that includes Orafce: 

### Docker
         
         mkdir ~/alloydb-omni-orafce
           tee -a ~/alloydb-omni-orafce/Dockerfile << EOF
           ARG OMNI_VERSION
         
           FROM postgres:15-bookworm AS postgres
         
           RUN apt-get update && \
           apt-get install -y --no-install-recommends \
           postgresql-15-orafce && \
           apt-get purge -y --auto-remove && \
           rm -rf /var/lib/apt/lists/*
         
           FROM google/alloydbomni:${OMNI_VERSION}
         
           COPY --from=postgres /usr/lib/postgresql/15/lib/orafce.so /usr/lib/postgresql/15/lib/orafce.so
           COPY --from=postgres /usr/share/postgresql/15/extension/orafce* /usr/lib/postgresql/15/share/extension/
         
           COPY --from=postgres /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
           COPY --from=postgres /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
           EOF
           cd ~/alloydb-omni-orafce
           sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-orafce:$OMNI_VERSION .
           

### Podman
         
         mkdir ~/alloydb-omni-orafce
           tee -a ~/alloydb-omni-orafce/Dockerfile << EOF
           ARG OMNI_VERSION
         
           FROM postgres:15-bookworm AS postgres
         
           RUN apt-get update && \
           apt-get install -y --no-install-recommends \
           postgresql-15-orafce && \
           apt-get purge -y --auto-remove && \
           rm -rf /var/lib/apt/lists/*
         
           FROM google/alloydbomni:${OMNI_VERSION}
         
           COPY --from=postgres /usr/lib/postgresql/15/lib/orafce.so /usr/lib/postgresql/15/lib/orafce.so
           COPY --from=postgres /usr/share/postgresql/15/extension/orafce* /usr/lib/postgresql/15/share/extension/
         
           COPY --from=postgres /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
           COPY --from=postgres /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
           EOF
           cd ~/alloydb-omni-orafce
           sudo podman build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-orafce:$OMNI_VERSION .
           

### Docker
         
         mkdir ~/alloydb-omni-orafce
           tee -a ~/alloydb-omni-orafce/Dockerfile << EOF
           ARG OMNI_VERSION
         
           FROM postgres:15-bookworm AS postgres
         
           RUN apt-get update && \
           apt-get install -y --no-install-recommends \
           postgresql-15-orafce && \
           apt-get purge -y --auto-remove && \
           rm -rf /var/lib/apt/lists/*
         
           FROM google/alloydbomni:${OMNI_VERSION}
         
           COPY --from=postgres /usr/lib/postgresql/15/lib/orafce.so /usr/lib/postgresql/15/lib/orafce.so
           COPY --from=postgres /usr/share/postgresql/15/extension/orafce* /usr/lib/postgresql/15/share/extension/
         
           COPY --from=postgres /usr/lib/aarch64-linux-gnu/ /usr/lib/aarch64-linux-gnu/
           COPY --from=postgres /lib/aarch64-linux-gnu/ /lib/aarch64-linux-gnu/
           EOF
           cd ~/alloydb-omni-orafce
           sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-orafce:$OMNI_VERSION .
           

### Podman
         
         mkdir ~/alloydb-omni-orafce
           tee -a ~/alloydb-omni-orafce/Dockerfile << EOF
           ARG OMNI_VERSION
         
           FROM postgres:15-bookworm AS postgres
         
           RUN apt-get update && \
           apt-get install -y --no-install-recommends \
           postgresql-15-orafce && \
           apt-get purge -y --auto-remove && \
           rm -rf /var/lib/apt/lists/*
         
           FROM google/alloydbomni:${OMNI_VERSION}
         
           COPY --from=postgres /usr/lib/postgresql/15/lib/orafce.so /usr/lib/postgresql/15/lib/orafce.so
           COPY --from=postgres /usr/share/postgresql/15/extension/orafce* /usr/lib/postgresql/15/share/extension/
         
           COPY --from=postgres /usr/lib/aarch64-linux-gnu/ /usr/lib/aarch64-linux-gnu/
           COPY --from=postgres /lib/aarch64-linux-gnu/ /lib/aarch64-linux-gnu/
           EOF
           cd ~/alloydb-omni-orafce
           sudo podman build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-orafce:$OMNI_VERSION .

  4. Create a new container with AlloyDB Omni named `my-omni-orafce`: 

### Docker
         
         docker run --name my-omni-orafce  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-orafce:OMNI_VERSION

### Podman
         
         podman run --name my-omni-orafce  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-orafce:OMNI_VERSION

  5. Connect to your database with the Orafce extension: 

### Docker
         
         docker exec -it my-omni-orafce psql -h localhost -U postgres

### Podman
         
         podman exec -it my-omni-orafce psql -h localhost -U postgres

  6. Enable Orafce: 
         
         CREATE EXTENSION IF NOT EXISTS ORAFCE;

  7. Confirm that Orafce is installed and enabled: 
         
         SELECT oracle.sysdate();

The output looks similar to the following: 
         
         postgres=# SELECT oracle.sysdate();
              sysdate
         ---------------------
         2024-06-10 16:36:30
         (1 row)


**Note:** Due to some known issues with the Orafce extension on AlloyDB Omni, we don't recommend using the `dbms_utility.format_call_stack` and `dbms_output.get_line` functions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
