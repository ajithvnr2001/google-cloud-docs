---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage/
title: Manage and monitor AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:03.251428+00:00
---

# Manage and monitor AlloyDB Omni  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Manage and monitor AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/manage)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/manage)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/manage)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/manage)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/manage)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/manage)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/manage)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/manage)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/manage)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/manage)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/manage)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/manage)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/manage)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/manage)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/manage)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/manage)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/manage)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/manage)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/manage)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/manage)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage)

This page describes how to manage AlloyDB Omni user roles, monitor the activity of your AlloyDB Omni server, and update or remove your AlloyDB Omni installation. 

## Manage user roles

AlloyDB Omni uses the following roles:

  * AlloyDB Omni includes a superuser role named `alloydbadmin`, and a non-superuser role named `alloydbmetadata`.

  * The default `postgres` user has a superuser role.

  * All other predefined user roles have no privileges. They are reserved for potential uses in the future.




### Set up an AlloyDB Omni database

We recommend following these steps when setting up an AlloyDB Omni database:

  1. Define or import your databases using the `postgres` user role. In a new installation, this role has superuser privileges.

  2. Create new user roles that have the correct level of access to your application's tables, again using the `postgres` user role.

  3. Configure your application to connect to the database using these new, limited-access roles.




You can create and define as many new user roles as you need. Don't modify or delete any of the user roles that comes with AlloyDB Omni.

For more information, see [Manage AlloyDB Omni users and roles](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/database-users/manage-users).

## Monitor AlloyDB Omni

Monitoring your AlloyDB Omni installation includes fetching and analyzing AlloyDB Omni metrics.

###  Single-server 

By default, to retrieve AlloyDB Omni logs, run:

###  Docker 
    
    
      docker logs CONTAINER_NAME

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container.

To configure the logging behavior of AlloyDB Omni, see [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install).

###  Podman 
    
    
      podman logs CONTAINER_NAME

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container.

To configure the logging behavior of AlloyDB Omni, see [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install).

## Uninstall AlloyDB Omni

###  Single-server 

To uninstall AlloyDB Omni, stop and delete the AlloyDB Omni container using the following command:

###  Docker 
    
    
     docker container stop CONTAINER_NAME
       docker container rm CONTAINER_NAME

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container.

**Caution:** You must [mount](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install#mount-external-data-directory) an external data directory, so that your database data is not deleted when you delete the container.

###  Podman 
    
    
     podman container stop CONTAINER_NAME
       podman container rm CONTAINER_NAME

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container.

**Caution:** You must [mount](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install#mount-external-data-directory) an external data directory, so that your database data is not deleted when you delete the container.

###  Podman 
    
    
     podman container stop CONTAINER_NAME
       podman container rm CONTAINER_NAME

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container.

**Caution:** You must [mount](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install#mount-external-data-directory) an external data directory, so that your database data is not deleted when you delete the container.

You can move, archive, or delete an external data directory depending on whether and how you want to preserve your data after uninstalling AlloyDB Omni.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
