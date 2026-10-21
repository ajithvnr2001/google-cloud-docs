---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect/
title: Run and connect to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:33:05.944800+00:00
---

# Run and connect to AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Run and connect to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

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



This page describes how to run and connect to AlloyDB Omni after you [install it on your own machine](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install).

## Before you begin

Most of the commands on this page use the AlloyDB Omni CLI.

To install this command-line tool on your machine, see [Install the AlloyDB Omni CLI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/omni-cli).

## Run AlloyDB Omni

The procedures you use to run AlloyDB Omni depend on whether you're running AlloyDB Omni in a container on a single server.

Installing AlloyDB Omni sets up a system service called `alloydb-dataplane` that's configured to launch every time that your machine boots.

For basic control and monitoring of AlloyDB Omni, use the `sudo alloydb` command, as demonstrated in the following sections.

### Start AlloyDB Omni

**Caution:** Make sure that the storage device containing [the data directory](https://docs.cloud.google.com/alloydb/omni/15.5.2/docs/configure-omni#configure_your_data_directory_location) has at least 20 GB of free space. If it doesn't, then attempting to start AlloyDB Omni might cause it to fill up all available space on the device, causing it to fail to launch.
    
    
    sudo alloydb database-server start

**Note:** By default, AlloyDB Omni also starts when your machine boots.

To perform a test connection, see Connect using the containerized `psql`.

### Check the status of AlloyDB Omni
    
    
    sudo alloydb database-server status

### Stop AlloyDB Omni
    
    
    sudo alloydb database-server stop

### Disable startup launch

Running the following command prevents AlloyDB Omni from automatically starting when your machine boots.
    
    
    sudo systemctl disable alloydb-dataplane

### Re-enable startup launch
    
    
      sudo systemctl enable alloydb-dataplane

## Connect to AlloyDB Omni running on a single server

The AlloyDB Omni container includes its own copy of `psql` that lets you open an interactive SQL shell session with its database server.

You can also connect to AlloyDB Omni from outside the container, using the PostgreSQL-compatible software of your choice.

### Connect using the containerized `psql`

To connect to the AlloyDB Omni database server using its own containerized copy of `psql`, run the following command:

###  Single-server 
    
    
    docker exec -it pg-service psql -h localhost -U postgres

This command connects you to the server as the `postgres` user role, and displays a `postgres=#` command prompt. You can now [run `psql` commands](https://www.postgresql.org/docs/current/app-psql.html) and SQL queries.

To exit `psql`, run the `\q` command.

### Connect using your own applications

Any application that works with PostgreSQL can also work with AlloyDB Omni, with no modification needed.

To connect to the AlloyDB Omni database server, use any PostgreSQL-compatible client or code library to connect to port `5432`—the default PostgreSQL database server port—of the machine running AlloyDB Omni.

This works because the AlloyDB Omni container exposes its own port `5432` to the same port of the machine that it runs on.

After connecting to the database server, you can define, query, and modify your databases using DML and SQL queries by using standard PostgreSQL communication protocols.

Because AlloyDB Omni runs within your own environment, you can control how you connect to AlloyDB Omni. This includes allowing or restricting network access to this service according to the needs of your application, just as you would with an ordinary PostgreSQL server.

## What's next

  * [Manage and monitor AlloyDB Omni.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
