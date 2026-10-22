---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/run-connect/
title: Run and connect to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:41.172286+00:00
---

# Run and connect to AlloyDB Omni  |  AlloyDB Omni for containers: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/run-connect/

This page documents AlloyDB Omni version **15.13.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/overview)



Send feedback 

#  Run and connect to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/run-connect)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/run-connect)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/run-connect)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/run-connect)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/run-connect)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/run-connect)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/run-connect)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/run-connect)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/run-connect)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/run-connect)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/run-connect)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/run-connect)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/run-connect)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/run-connect)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/run-connect)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/run-connect)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/run-connect)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/run-connect)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/run-connect)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/run-connect)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/run-connect)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/run-connect)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect)



This page describes how to run and connect to AlloyDB Omni after you [install it on your own machine](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install).

## Run AlloyDB Omni

The procedures you use to run AlloyDB Omni depend on whether you're running AlloyDB Omni in a container on a single server.

### Start AlloyDB Omni

To start a stopped AlloyDB Omni container, run either [the `docker container start` command](https://docs.docker.com/reference/cli/docker/container/start/) or [the `podman container start` command](https://docs.podman.io/en/v1.6.4/markdown/podman-start.1.html):

###  Docker 
    
    
    docker container start CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
    
    
    podman container start CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

### Check the status of AlloyDB Omni

To check the status of all of the containers you have running, run either [the `docker container ls` command](https://docs.docker.com/reference/cli/docker/container/ls/) or [the `podman container ls` command](https://docs.podman.io/en/latest/markdown/podman-ps.1.html):

###  Docker 
    
    
    docker container ls

###  Podman 
    
    
    podman container ls

If your AlloyDB Omni container is running, then its name will appear in the `NAMES` column of the output table. The corresponding row summarizes the container's state.

If the name of your container doesn't appear in the `NAMES` column, then your AlloyDB Omni is not running.

### Stop AlloyDB Omni

To stop a AlloyDB Omni container, run either [the `docker container stop` command](https://docs.docker.com/reference/cli/docker/container/stop/) or [the `podman container stop` command](https://docs.podman.io/en/latest/markdown/podman-stop.1.html):

###  Docker 
    
    
      docker container stop CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
    
    
      podman container stop CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

## Connect to AlloyDB Omni running on a single server

The AlloyDB Omni container includes its own copy of `psql` that lets you open an interactive SQL shell session with its database server.

You can also connect to AlloyDB Omni from outside the container, using the PostgreSQL-compatible software of your choice.

For information about connecting to an AlloyDB Omni database cluster running on a Kubernetes cluster, see Connect to AlloyDB Omni running on Kubernetes.

### Connect using the containerized `psql`

To connect to the AlloyDB Omni database server using its own containerized copy of `psql`, run the following command:

###  Docker 
    
    
      docker exec -it CONTAINER_NAME psql -U postgres

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
    
    
      podman exec -it CONTAINER_NAME psql -U postgres

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

This command connects you to the server as the `postgres` user role, and displays a `postgres=#` command prompt. You can now [run `psql` commands](https://www.postgresql.org/docs/current/app-psql.html) and SQL queries.

To exit `psql`, run the `\q` command.

### Connect using your own applications

Any application that works with PostgreSQL can also work with AlloyDB Omni, with no modification needed.

To connect to the AlloyDB Omni database server, expose networking from the AlloyDB Omni docker container to your host machine by adding `--network=host` or `-p 5432:5432` to your `docker run` or `podman run` command when you start AlloyDB Omni.

To select a custom port number, use `-p [HOST_PORT]:5432` when you start AlloyDB Omni. Then, use any PostgreSQL-compatible client or code library to connect to port `5432` or the custom port number that you specified.

After connecting to the database server, you can define, query, and modify your databases using DML and SQL queries by using standard PostgreSQL communication protocols.

Because AlloyDB Omni runs within your own environment, you can control how you connect to AlloyDB Omni. This includes allowing or restricting network access to this service according to the needs of your application, just as you would with an ordinary PostgreSQL server.

## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
