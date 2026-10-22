---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-orafce/
title: Install Orafce for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:17.302988+00:00
---

# Install Orafce for AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-orafce/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Install Orafce for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

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

AlloyDB Omni does not include the Orafce extension, but you can manually add it to an existing AlloyDB Omni installation by following the instructions on this page. 

## Before you begin

Ensure that you meet the following system requirements:

  * You've [installed AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install) on your system.

  * You've [installed the AlloyDB Omni CLI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/omni-cli) on your system.




## Add Orafce to your AlloyDB Omni installation

To add the Orafce extension to your AlloyDB Omni installation, follow these steps:

  1. Find your installed AlloyDB Omni version labels: 
         
         sudo alloydb version

The output is similar to the following:
         
         AlloyDB Omni CLI version: 1.0
         AlloyDB Omni database server version: 15.5.2
         

Take note of the database server version number; you need it in the next step.

  2. Set the `OMNI_VERSION` environment variable: 
         
         OMNI_VERSION=VERSION

Replace VERSION with the complete database server version from the previous step—for example, `15.5.2`.

  3. Create a new AlloyDB Omni container that includes Orafce: 
         
         mkdir ~/alloydb-omni-orafce
         tee -a ~/alloydb-omni-orafce/Dockerfile << EOF
         ARG OMNI_VERSION
         
         FROM postgres:15-bookworm as postgres
         
         RUN apt-get update && \
                 apt-get install -y --no-install-recommends \
                 postgresql-15-orafce && \
                 apt-get purge -y --auto-remove && \
                 rm -rf /var/lib/apt/lists/*
         
         FROM gcr.io/alloydb-omni/pg-service:${OMNI_VERSION}
         
         COPY --from=postgres /usr/lib/postgresql/15/lib/orafce.so /lib/orafce.so
         COPY --from=postgres /usr/share/postgresql/15/extension/orafce* /share/extension/
         
         COPY --from=postgres /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
         COPY --from=postgres /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
         EOF
         
         cd ~/alloydb-omni-orafce
         
         sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag gcr.io/alloydb-omni/pg-service-with-orafce:$OMNI_VERSION .

  4. Stop the database server: 
         
         sudo alloydb database-server stop
         

  5. Open `/var/alloydb/config/dataplane.conf` in a text editor.
  6. Modify the line that defines the `PG_IMAGE` variable so that it refers to the container that you built in a previous step: 
         
         PG_IMAGE=gcr.io/alloydb-omni/pg-service-with-orafce
         

  7. Start AlloyDB Omni: 
         
         sudo alloydb database-server start
         

  8. Connect to your database: 
         
         sudo docker exec -it pg-service psql -h localhost -U postgres
         

  9. Enable Orafce: 
         
         CREATE EXTENSION IF NOT EXISTS ORAFCE;

  10. Confirm that Orafce is installed and enabled: 
         
         SELECT oracle.sysdate();


**Note:** Due to some known issues with the Orafce extension on AlloyDB Omni, we do not recommend using `dbms_utility.format_call_stack` and `dbms_output.get_line` functions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
