---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/quickstart/
title: Install AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:21.647545+00:00
---

# Install AlloyDB Omni  |  AlloyDB Omni using containers: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/quickstart/

This page documents AlloyDB Omni version **15.17.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/overview)



Send feedback 

#  Install AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.17.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/quickstart)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/quickstart)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/quickstart)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/quickstart)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/quickstart)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/quickstart)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/quickstart)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/quickstart)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/quickstart)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/quickstart)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/quickstart)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/quickstart)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/quickstart)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/quickstart)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/quickstart)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/quickstart)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/quickstart)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/quickstart)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/quickstart)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/quickstart)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/quickstart)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/quickstart)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/quickstart)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/quickstart)

This quickstart shows you how to install AlloyDB Omni that can run in any UNIX-based environment which supports container runtimes. 

For an overview of AlloyDB Omni, see [AlloyDB Omni overview](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs).

## Before you begin

**Note:** You can run AlloyDB Omni on macOS. However, AlloyDB Omni in a Docker container on macOS uses Docker's compatibility layer, which can result in reduced performance compared to running it directly on Linux.

### Choose a download or installation option

**Media** | **Download locations and installation guides** | **Deployment to**  
---|---|---  
**Debian image** | [DockerHub](https://hub.docker.com/r/google/alloydbomni/tags) (tags) | 

  * [Docker](https://www.docker.com/), [Podman](https://podman.io/). You can run these containerization tools as a container in any virtual machine (VM).


  * [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/click-to-deploy-images/alloydb-omni)


  * [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-sne7ttiby7nxi)


  * [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/google-cloud-alloydb-omni.alloydbomni?tab=overview)

  
**UBI Image (Red Hat)** | [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/container-stacks/detail/67d88bd7ce4ca47642c2a072) | 

  * Red Hat environment. Run this as a container.


  * [Red Hat Marketplace](https://catalog.redhat.com/software/containers/google/alloydbomni/681daa13362cef4fe8a0115f) (UBI)

  
  
### Fulfill hardware and software requirements

Make sure that you meet the following minimum hardware and software requirements:

OS/Platform | Minimum hardware | Minimum software  
---|---|---  
Linux | 
* x86-64 or Arm (*) CPU with AVX2 support
* 2 GB of RAM
* 10 GB of disk space
| 
* Debian based OS (Ubuntu, etc.), RHEL 8 or 9
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
  
#### Verify that cgroupsv2 is enabled

To determine whether cgroupsv2 is enabled on your machine, run the following command:
    
    
    grep cgroup /proc/filesystems
    

If your machine supports cgroupsv2, you see the following output:
    
    
    nodev cgroup
    nodev cgroupsv2
    

If your machine doesn't support cgroupsv2, you see the following output:
    
    
    nodev cgroup
    

### Install a container runtime

Install a container runtime like [Docker](https://docs.docker.com/engine/install/) or [Podman](https://podman.io/docs/installation). AlloyDB Omni runs in a container.

**Note:** AlloyDB Omni is compiled to run directly on Linux systems. Running AlloyDB Omni in a Docker container on macOS utilizes Docker's compatibility layer, which results in reduced performance compared to running directly on Linux.

## Install AlloyDB Omni using Docker

**Note:** If you want to deploy AlloyDB Omni in your production environment, see [Run AlloyDB Omni in production](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/run-alloydb-omni-production).

[Root access](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) is not required for installing AlloyDB Omni.

###  Docker 

  1. Use the `docker run` command to create a new container with AlloyDB Omni named `my-omni`:
         
         docker run --name my-omni \
             -e POSTGRES_PASSWORD=NEW_PASSWORD \
             -d google/alloydbomni:15

Replace `NEW_PASSWORD` with a password to assign the new container's `postgres` user after its creation.

**Note:** By default, AlloyDB Omni stores your data on the container itself, and not on your host file system. The data directory is deleted once you delete your AlloyDB Omni container. To mount a data directory stored on your host file system, see instructions in [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install).
  2. Connect to containerized AlloyDB Omni using `psql`:
         
         docker exec -it my-omni psql -h localhost -U postgres

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.




###  Podman 

  1. Use the `docker run` command to create a new container with AlloyDB Omni named `my-omni`:
         
         podman run --name my-omni \
             -e POSTGRES_PASSWORD=NEW_PASSWORD \
             -d google/alloydbomni:15

Replace `NEW_PASSWORD` with a password to assign the new container's `postgres` user after its creation.

**Note:** By default, AlloyDB Omni stores your data on the container itself, and not on your host file system. The data directory is deleted once you delete your AlloyDB Omni container. To mount a data directory stored on your host file system, see instructions in [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install).
  2. Connect to containerized AlloyDB Omni using `psql`:
         
         podman exec -it my-omni psql -h localhost -U postgres

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.




## Clean up

To clean up the AlloyDB Omni container you created during this quickstart, use these steps:

###  Docker 

  1. Stop your AlloyDB Omni container named `my-omni`:
         
         docker container stop my-omni

  2. Delete your AlloyDB Omni container named `my-omni`:
         
         docker container rm my-omni




###  Podman 

  1. Stop your AlloyDB Omni container named `my-omni`:
         
         podman container stop my-omni

  2. Delete your AlloyDB Omni container named `my-omni`:
         
         podman container rm my-omni




For instructions how to install AlloyDB Omni in a new container for production usage, go to the [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install) page.

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/run-connect)

  * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install)

  * [Set up your AlloyDB Omni for production](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/configure-omni)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
