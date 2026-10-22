---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install-orafce/
title: Install orafce for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:36.996550+00:00
---

# Install orafce for AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install-orafce/

This page documents AlloyDB Omni version **16.3.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)



Send feedback 

#  Install orafce for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install-orafce)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install-orafce)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/install-orafce)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-orafce)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install-orafce)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/install-orafce)

Debian UBI

This page describes how to manually add the [orafce extension](https://github.com/orafce/orafce) to an existing AlloyDB Omni installation. The orafce extension provides functions and operators that emulate a subset of functions and packages from the Oracle database. This extension simplifies migration of applications from Oracle to PostgreSQL-compatible databases such as AlloyDB Omni.

## Before you begin

[Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install) on your system.

## Add orafce to your AlloyDB Omni installation

To add the orafce extension to your AlloyDB Omni installation, follow these steps:

  1. Find your installed AlloyDB Omni version labels:

### Docker
         
         docker run --rm -it  google/alloydbomni cat VERSION.txt
         

### Podman
         
         podman run --rm -it  google/alloydbomni cat VERSION.txt
         

The output is similar to the following:
         
         AlloyDB Omni version: 16.3.0
         

Take note of the AlloyDB Omni version number because you need it in the next step. 

  2. Create a new AlloyDB Omni container that includes orafce:

###  Linux 
         
         $ mkdir ~/alloydb-omni-orafce
         
         $ tee ~/alloydb-omni-orafce/Dockerfile << EOF
         ARG OMNI_VERSION
         FROM google/alloydbomni:${OMNI_VERSION}
         RUN apt-get update && \
               apt-get install -y --no-install-recommends postgresql-16-orafce && \
               apt-get purge -y --auto-remove && \
               rm -rf /var/lib/apt/lists/*
         EOF
         
         $ cd ~/alloydb-omni-orafce
         
         $ sudo docker build --build-arg OMNI_VERSION=OMNI_VERSION --tag google/alloydbomni-with-orafce:OMNI_VERSION .
         

###  MacOS 
         
         $ mkdir ~/alloydb-omni-orafce
         
         $ tee ~/alloydb-omni-orafce/Dockerfile << EOF
         ARG OMNI_VERSION
         FROM google/alloydbomni:OMNI_VERSION
         RUN apt-get update && \
               apt-get install -y --no-install-recommends postgresql-16-orafce && \
               apt-get purge -y --auto-remove && \
               rm -rf /var/lib/apt/lists/*
         EOF
         
         $ cd ~/alloydb-omni-orafce
         
         $ sudo docker build --build-arg OMNI_VERSION=OMNI_VERSION --tag google/alloydbomni-with-orafce:OMNI_VERSION .
         

  3. Create a new container with AlloyDB Omni named `my-omni-orafce`:
         
         docker build -t google/alloydbomni-with-orafce:latest
         docker run --name my-omni-orafce  -e POSTGRES_PASSWORD=NEW_PASSWORD  -d google/alloydbomni-with-orafce:OMNI_VERSION
         

  4. Connect to your database with the orafce extension:
         
         docker exec -it my-omni-orafce psql -h localhost -U postgres
         

  5. Enable orafce:
         
         CREATE EXTENSION IF NOT EXISTS ORAFCE;
         

  6. Confirm that orafce is installed and enabled:
         
         SELECT oracle.sysdate();
         

The output is similar to the following:
         
         postgres=# SELECT oracle.sysdate();
         sysdate
         ---------------------
         2024-06-10 16:36:30
         (1 row)
         

**Note:** Due to some known issues with the orafce extension on AlloyDB Omni, we don't recommend that you use the `dbms_utility.format_call_stack`, `dbms_output.get_line`, and `regexp_*` functions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
