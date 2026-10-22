---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/quickstart/
title: Install AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:22.326553+00:00
---

# Install AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/quickstart/

This page documents AlloyDB Omni version **15.5.4** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)



Send feedback 

#  Install AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/quickstart)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/quickstart)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/quickstart)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/quickstart)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/quickstart)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/quickstart)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This quickstart shows you how to install AlloyDB Omni that can run in any UNIX-based environment which supports container runtimes.

For an overview of AlloyDB Omni, see [AlloyDB Omni overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs).

## Before you begin

The following table lists minimum hardware and software requirements for AlloyDB Omni.

OS/Platform | Minimum hardware | Minimum software  
---|---|---  
Linux | 
* x86-64 or Arm (*) CPU with AVX2 support
* 2 GB of RAM
* 10 GB of disk space
| 
* Debian based OS (Ubuntu, etc) or RHEL 9
* Linux kernel version 5.3 or higher
* Cgroupsv2 enabled
* Docker Engine 20.10+ or Podman 4.2.0+  
macOS | 
* Intel CPU with AVX2 support or M-chip
* 2GB of RAM
* 10 GB of disk space
| 
* Docker Desktop 4.20 or higher  
(*) Arm support is in [Preview](https://cloud.google.com/products?e=48754805&#product-launch-stages).  
  
AlloyDB Omni runs in a container. Install a container runtime like [Docker](https://docs.docker.com/engine/install/) or [Podman](https://podman.io/docs/installation) on your machine before installing AlloyDB Omni.

## Install AlloyDB Omni using Docker

**Note:** [Root access](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) is not required for installing AlloyDB Omni.

  1. Use the `docker run` command to create a new container with AlloyDB Omni named `my-omni`:
         
         docker run --name my-omni \
           -e POSTGRES_PASSWORD=NEW_PASSWORD \
           -d google/alloydbomni:15.5.4

Replace `NEW_PASSWORD` with a password to assign the new container's `postgres` user after its creation.


**Note:** By default, AlloyDB Omni stores your data on the container itself, and not on your host file system. The data directory is deleted once you delete your AlloyDB Omni container. To mount a data directory stored on your host file system, see instructions in [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install).

  1. Connect to containerized AlloyDB Omni using `psql`:
         
         docker exec -it my-omni psql -h localhost -U postgres

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.




## Clean up

To clean up the AlloyDB Omni container you created during this quickstart, use these steps:

  1. Stop your AlloyDB Omni container named `my-omni`:
         
         docker container stop my-omni

  2. Delete your AlloyDB Omni container named `my-omni`:
         
         docker container rm my-omni




For instructions how to install AlloyDB Omni in a new container for production usage, go to the [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install) page.

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/run-connect)

  * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install)

  * [Set up your AlloyDB Omni for production](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/configure-omni)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
