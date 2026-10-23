---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install/
title: Customize your AlloyDB Omni installation \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:04.985126+00:00
---

# Customize your AlloyDB Omni installation  |  AlloyDB Omni for containers: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install/

This page documents AlloyDB Omni version **15.5.5** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)



Send feedback 

#  Customize your AlloyDB Omni installation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

AlloyDB Omni is deployed through a Docker image, which allows different forms of customization. This page shows some of the common customizations that are used.

To get started quickly with AlloyDB Omni using the default configuration, see [Quickstart: AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/quickstart).

## Before you begin

The following table lists recommended hardware and software configuration for AlloyDB Omni.

OS/Platform | Recommended hardware configuration | Recommended software configuration  
---|---|---  
Linux | 
* x86-64 or Arm (*) CPU with AVX2 support
* 8GB of RAM for every CPU allocated to AlloyDB Omni
* 20+ GB of disk space
| 
* Debian based OS (Ubuntu, etc.) or RHEL 9
* Linux kernel version 6.1 or higher or any Linux kernel version older than 5.3 that has support for the MADV_COLLAPSE and MADV_POPULATE_WRITE directives
* Cgroupsv2 enabled
* Docker Engine 25.0.0+ or Podman 5.0.0+  
macOS | 
* Intel CPU with AVX2 support or M-chip
* 8GB of RAM for every CPU allocated to AlloyDB Omni
* 20+ GB of disk space
| 
* Docker Desktop 4.30 or higher  
(*) Arm support is in [Preview](https://cloud.google.com/products?e=48754805&#product-launch-stages).  
  
AlloyDB Omni runs in a container. Install a container runtime like [Docker](https://docs.docker.com/engine/install/) or [Podman](https://podman.io/docs/installation) on your machine before installing AlloyDB Omni.

Podman commands are provided for a rootless container running on disabled Security-Enhanced Linux (SELinux).

###  Single-server 

## Mount an external data directory

By default, the command in the [Quickstart: Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/quickstart) stores the database data in an area managed by Docker. This is convenient for getting started but makes it difficult to find and use the data directory. Instead, you can set up a bind mount to map the data directory to a known location on your disk.

###  Docker 
    
    
    docker run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

Replace the following:

  * `CONTAINER_NAME`: the name to assign this new AlloyDB Omni container in your host machine's container registry—for example, `my-omni`.

  * `NEW_PASSWORD`: the password assigned the new container's `postgres` user after its creation.

  * `DATA_DIR`: the file system path that you want AlloyDB Omni to use for its data directory.

  * `HOST_PORT`: the TCP port on the host machine to which the container publishes port 5432. To use the PostgreSQL default port on the host machine as well, specify `5432`.




###  Podman 
    
    
    podman run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

Replace the following:

  * `CONTAINER_NAME`: the name to assign this new AlloyDB Omni container in your host machine's container registry—for example, `my-omni`.

  * `NEW_PASSWORD`: the password assigned the new container's `postgres` user after its creation.

  * `DATA_DIR`: the file system path that you want AlloyDB Omni to use for its data directory.

  * `HOST_PORT`: the TCP port on the host machine to which the container publishes port 5432. To use the PostgreSQL default port on the host machine as well, specify `5432`.




###  Podman 
    
    
    podman run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

Replace the following:

  * `CONTAINER_NAME`: the name to assign this new AlloyDB Omni container in your host machine's container registry—for example, `my-omni`.

  * `NEW_PASSWORD`: the password assigned the new container's `postgres` user after its creation.

  * `DATA_DIR`: the file system path that you want AlloyDB Omni to use for its data directory.

  * `HOST_PORT`: the TCP port on the host machine to which the container publishes port 5432. To use the PostgreSQL default port on the host machine as well, specify `5432`.




## Enable ulimits

The [ulimit](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/x4733.html) parameters specify process limits that the Docker container can use. For optimal performance, we recommend that you set the following ulimits:

  * `nice=-20:-20`: AlloyDB Omni adjusts process priorities to allow critical PostgreSQL processes to run with higher priority. The higher priority gives the processes a bigger allocation of available CPUs. To adjust process priorities, specify `--ulimit=nice=-20:-20`, which removes limitations for the AlloyDB Omni container.

  * `memlock=-1:-1`: AlloyDB Omni performs [automatic memory management](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/automatic-memory-management). Setting `--ulimit=memlock=-1:-1` allows the database to better control how memory pages are swapped in and out, which can result in better performance.




###  Docker 
    
    
    docker run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

###  Podman 
    
    
    podman run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

## Specify a logging driver

By default, Docker does not perform log rotations. This can use up a lot of disk space, and eventually lead to disk space exhaustion. You can configure Docker to use a different logging driver. For example, to log to journald:

###  Docker 
    
    
    docker run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

###  Podman 
    
    
    podman run --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 -d google/alloydbomni:15.5.5

For more information about Docker and logging drivers, refer to Docker's documentation [Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/).

You can also configure logging using PostgreSQL. For more information, refer to PostgreSQL documentation [Error reporting and logging](https://www.postgresql.org/docs/15/runtime-config-logging.html). **Warning:** In AlloyDB Omni only, setting the `alloydb.enable_pgaudit` flag to `true` and you set the PostgreSQL `logging_collector` parameter to `on`, you might experience a loss of audit logs. 

## Mount a shared memory volume

If you plan to use the AlloyDB [columnar engine](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure) with AlloyDB Omni, we recommend making shared memory available to the AlloyDB Omni container. The method for doing this differs depending upon your host operating system, as shown in the following examples.

###  Linux 

To make shared memory available to the container, mount `/dev/shm`:

###  Docker 
    
    
      docker run --name CONTAINER_NAME \
        -e POSTGRES_PASSWORD=NEW_PASSWORD \
        -p HOST_PORT:5432 \
        -v /dev/shm:/dev/shm \
        -d google/alloydbomni:15.5.5

###  Podman 
    
    
      podman run --name CONTAINER_NAME \
        -e POSTGRES_PASSWORD=NEW_PASSWORD \
        -p HOST_PORT:5432 \
        -v /dev/shm:/dev/shm \
        -d google/alloydbomni:15.5.5

###  macOS 

To make shared memory available to the container, include the `--shm-size` flag:

###  Docker 
    
    
      docker run --name CONTAINER_NAME \
        -e POSTGRES_PASSWORD=NEW_PASSWORD \
        -p HOST_PORT:5432 \
        --shm-size=SHARED_MEMORY_SIZE \
        -d google/alloydbomni:15.5.5

Replace `SHARED_MEMORY_SIZE` with the size to set for `/dev/shm` on the container, in the format described on [Running containers](https://docs.docker.com/engine/reference/run/). For example, to specify one gigabyte, use the value `1g`.

###  Podman 
    
    
      podman run --name CONTAINER_NAME \
        -e POSTGRES_PASSWORD=NEW_PASSWORD \
        -p HOST_PORT:5432 \
        --shm-size=SHARED_MEMORY_SIZE \
        -d google/alloydbomni:15.5.5

Replace `SHARED_MEMORY_SIZE` with the size to set for `/dev/shm` on the container, in the format described on [Running containers](https://docs.docker.com/engine/reference/run/). For example, to specify one gigabyte, use the value `1g`.

We recommend setting the shared memory size to a number of megabytes equal to at least your database's value of [the `google_job_scheduler.max_parallel_workers_per_job` flag](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#max-parallel-workers-per-job), times 250. For more information about the columnar engine, see [Configure the columnar engine in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure).

For example, if the `google_job_scheduler.max_parallel_workers_per_job` database flag is set to its default value of `2`, consider adding a flag of `--shm-size=500m` or greater when starting your database server.

For more information about the `--shm-size` flag, see [Running containers](https://docs.docker.com/engine/reference/run/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
