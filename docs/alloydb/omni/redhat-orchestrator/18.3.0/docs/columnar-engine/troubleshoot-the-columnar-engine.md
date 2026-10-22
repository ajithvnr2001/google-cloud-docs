---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/troubleshoot-the-columnar-engine/
title: Troubleshoot the columnar engine \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:42:40.131983+00:00
---

# Troubleshoot the columnar engine  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/troubleshoot-the-columnar-engine/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Troubleshoot the columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/troubleshoot-the-columnar-engine)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/columnar-engine/troubleshoot-the-columnar-engine)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/troubleshoot-the-columnar-engine)

This page describes how to troubleshoot issues that you might encounter when you use the AlloyDB Omni columnar engine. For more information about the columnar engine, see [Columnar engine overview](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/overview). 

## Fix the "insufficient shared memory" error

If you run AlloyDB Omni without enough shared memory for the columnar engine, then you might see the following error:
    
    
    Insufficient shared memory for generating the columnar formats.
    

To address this issue, specify the amount of shared memory that's available to the AlloyDB Omni container.

###  Linux 

  1. Make sure that you already installed AlloyDB Omni with your `/dev/shm` directory mounted on the container. For more information, see [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-psql#one-omni).

  2. Increase the size of your host machine's `/dev/shm` partition by using a technique such as editing your `/etc/fstab` file.




## Find the tables that are populated in the columnar engine

In the `g_columnar_relations` view, create queries to find the tables that are present in the columnar engine.
    
    
    SELECT * FROM g_columnar_relations;
    

## Find the overall memory that the columnar engine uses

Use the `google_columnar_engine_memory_available()` SQL function to determine the amount of memory that the columnar engine uses.
    
    
    SELECT google_columnar_engine_memory_available();
    

## Determine if specific columns aren't populated in the columnar engine

Try the following possible solutions:

  * Check whether the columnar engine supports the column's data type.
  * If you recently added or dropped columns to the base table, verify that you performed the same operation in the columnar engine.



## Verify if a query uses the columnar engine

In the query plan, verify if there's a "Custom Scan (columnar scan)" planner node.

## Find the maintenance jobs in progress

Query in the `g_columnar_jobs` view to find the jobs in progress.
    
    
    SELECT * FROM g_columnar_jobs;
    

## Set the amount of resources that maintenance activities use in the columnar engine

By default, the columnar engine uses up to 20% of the database resources. To increase or decrease this usage, adjust the `google_columnar_engine.maintenance_cpu_percentage` (GUC) setting. For more information, see [Adjust the CPU resources for maintenance tasks](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/tune-columnar-engine#adjust-cpu-resources).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
