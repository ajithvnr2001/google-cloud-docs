---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install/
title: Customize your AlloyDB Omni installation \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:41:11.400505+00:00
---

# Customize your AlloyDB Omni installation  |  AlloyDB Omni for Kubernetes: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install/

This page documents AlloyDB Omni version **15.7.1** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/overview)



Send feedback 

#  Customize your AlloyDB Omni installation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/install)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/install)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page describes how to customize your AlloyDB Omni installation, which is deployed through a container image that supports different forms of customization. This page shows some common customizations.

## Mount an external data directory

By default, the command in [Quickstart: Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/quickstart) stores the database data in an area managed by Docker or Podman. This is convenient for getting started but makes it difficult to find and use the data directory. Instead, you can set up a bind mount to map the data directory to a known location on your disk.

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name that you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `DATA_DIR`: Host directory path that your data is stored in.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `15.7.1` for the latest Debian image or `15.7.1-ubi` for the latest UBI image.



## Enable ulimits

The [ulimit](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/x4733.html) parameters specify process limits that the Docker or Podman container can use. For optimal performance, we recommend that you set the following ulimits:

  * `nice=-20:-20`: AlloyDB Omni adjusts process priorities to allow critical PostgreSQL processes to run with higher priority. The higher priority gives the processes a bigger allocation of available CPUs. To adjust process priorities, specify `--ulimit=nice=-20:-20`, which removes limitations for the AlloyDB Omni container.

  * `memlock=-1:-1`: AlloyDB Omni performs [automatic memory management](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/automatic-memory-management). Setting `--ulimit=memlock=-1:-1` allows the database to better control how memory pages are swapped in and out, which can result in better performance.




### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `AlloyDB Omni` for the latest Debian image or `AlloyDB Omni-ubi` for the latest UBI image.



## Specify a logging driver

By default, Docker and Podman don't perform log rotations. This can use up a lot of disk space, and eventually lead to disk space exhaustion. To use a different logging driver, you can specify the `--log-driver` field. For example, to log to `journald`:

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `15.7.1` for the latest Debian image or use `15.7.1-ubi` for the latest UBI image.



For more information about logging drivers, refer to Docker's [Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/) and Podman's [`podman-run`](https://docs.podman.io/en/v5.1.1/markdown/podman-run.1.html#log-driver-driver) documentation.

## Mount a shared memory volume

If you plan to use the AlloyDB [columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/configure) with AlloyDB Omni, we recommend making shared memory available to the AlloyDB Omni container. The method for doing this differs depending upon your host operating system, as shown in the following examples.

### Linux

To make shared memory available to the container, mount `/dev/shm`:

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `15.7.1` for the latest Debian image or use `15.7.1-ubi` for the latest UBI image.



### macOS

To make shared memory available to the container, include the `--shm-size` flag:

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `SHARED_MEMORY_SIZE`: Size to set for `/dev/shm` on the container, in the format described on [Running containers](https://docs.docker.com/engine/reference/run/). For example, to specify one gigabyte, use the value `1g`.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `15.7.1` for the latest Debian image or `15.7.1-ubi` for the latest UBI image.



We recommend that you set the shared memory size to a number of megabytes equal to at least your database's value of the [`google_job_scheduler.max_parallel_workers_per_job` flag](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/columnar-engine-flags#max-parallel-workers-per-job), times 250. For more information about the columnar engine, see [Configure the columnar engine in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/configure).

For example, if the `google_job_scheduler.max_parallel_workers_per_job` database flag is set to its default value of `2`, consider adding a flag of `--shm-size=500m` or greater when starting your database server.

For more information about the `--shm-size` flag, see [Running containers](https://docs.docker.com/engine/reference/run/).

## Enable extensions

The list of extensions available in AlloyDB Omni is available in [Supported database extensions](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/extensions). Although PostGIS and Orafce are not included with AlloyDB Omni, they can both be installed by following instructions:

  * [Install PostGIS for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install-postgis)
  * [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install-orafce)



Installed extensions are enabled using standard PostgreSQL `CREATE EXTENSION` statements as detailed in [Enable an extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/extensions#enable).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
