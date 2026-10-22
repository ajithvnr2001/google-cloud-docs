---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/automatic-memory-management/
title: About automatic memory management \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:19.655731+00:00
---

# About automatic memory management  |  AlloyDB Omni for containers: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/automatic-memory-management/

This page documents AlloyDB Omni version **15.5.5** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)



Send feedback 

#  About automatic memory management Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/automatic-memory-management)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/automatic-memory-management)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/automatic-memory-management)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/automatic-memory-management)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/automatic-memory-management)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/automatic-memory-management)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/automatic-memory-management)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/automatic-memory-management)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/automatic-memory-management)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/automatic-memory-management)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/automatic-memory-management)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/automatic-memory-management)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/automatic-memory-management)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/automatic-memory-management)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/automatic-memory-management)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/automatic-memory-management)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/automatic-memory-management)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/automatic-memory-management)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/automatic-memory-management)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/automatic-memory-management)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/automatic-memory-management)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/automatic-memory-management)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/automatic-memory-management)

AlloyDB Omni uses adaptive algorithms for memory management. 

You can decide the upper limit of the shared buffer on starting AlloyDB Omni. If you don't set the upper limit, AlloyDB Omni automatically sets the shared buffer backing up size to 80% of system memory. The initial backing up size of the shared buffer can be different from the upper limit.

AlloyDB Omni consists of an intelligent memory worker which constantly monitors the memory status, and tunes shared buffer backing up size for best performance when caching data.

![Automatic memory](https://docs.cloud.google.com/static/alloydb/omni/containers/15.5.5/docs/images/automatic-memory-management.png)

By default the `shared_buffers` parameter is set to `0` which is a special value that sets the upper limit of the size of the `shared buffers` cache to 80% of system memory. AlloyDB Omni starts at 10% of the `shared_buffers` upper limit. If `shared_buffers` is overridden by a custom value, then AlloyDB Omni respects the value as the upper limit of the `shared_buffers` size, and starts with that specified custom size.

**Note:** Memory worker can still decide to shrink, and later grow shared buffer backing up size at runtime.

To specify a custom size, edit the `postgresql.conf` configuration file. For example, you can set `shared_buffers` to `1GB` using either of the following:

  * `docker run --name CONTAINER_NAME -e INITDB_ARGS="-c shared_buffers=1GB" $image`

  * `docker run --name CONTAINER_NAME $image -c shared_buffers=1GB`

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.




## Optimize query performance

The default value of the `shared_buffers` parameter works for common scenarios.

However, you can tune the value for best performance. If you choose to rely on the default value of `shared_buffers` to deduce the shared buffer upper limit, then use the cgroup `memory.max` value to influence the computation.

## Columnar engine memory

The dynamic `shared_buffers` is independent of the [columnar engine memory](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure). When the columnar engine is enabled, the dynamic `shared_buffers` size can be derived by subtracting the amount of memory used by the columnar engine from 80% of the total memory available to the system or cgroup.

## Huge pages

Huge pages improve database performance. AlloyDB Omni manages huge pages explicitly if possible, otherwise it relies on the transparent huge pages (THP) feature of the operating system. If neither huge page type is supported, AlloyDB Omni falls back to 4k page, and prints a warning in docker container logs `docker logs $container_name` with specific instructions to set up huge pages. See [Start AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#start) for instructions how to start a container.

The warning looks similar to the following:
    
    
    HINT:  Please either execute the all-in-one setup script:
              docker run --rm --privileged $image setup-host
            OR manually execute:
              echo within_size | sudo tee /sys/kernel/mm/transparent_hugepage/shmem_enabled
              sudo sysctl -w vm.nr_overcommit_hugepages=1048576
    

## Automatic memory management at runtime

AlloyDB Omni constantly monitors the system load, and adjusts its memory consumptions for better performance. Specifically, you might observe the following:

**Dynamic`shared_buffers` size change**
    AlloyDB Omni increases the dynamic `shared_buffers` size when the system memory consumption is low, and decreases the size when the system memory consumption is high. To monitor the dynamic `shared_buffers` size, use: 
    
    
    CREATE EXTENSION IF NOT EXISTS g_memory;
    SELECT g_dynamic_shared_size();

**Termination of a PostgreSQL connection when the system is extremely low on memory**
    When AlloyDB Omni detects that the system is extremely low on memory, it attempts to delete the most memory-consuming PostgreSQL connections until the load falls back to a reasonable level. When such an event happens, AlloyDB Omni logs the following in docker container logs: 
    
    
    WARNING: Sending SIGTERM to pid=xxx NSpid=xxx (VA size = xxxMB) (RSS size = xxxMB)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
