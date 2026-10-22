---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/configure-omni/
title: Set up AlloyDB Omni for production \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:09.170272+00:00
---

# Set up AlloyDB Omni for production  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/configure-omni/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Set up AlloyDB Omni for production Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/configure-omni)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/configure-omni)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/configure-omni)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/configure-omni)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/configure-omni)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/configure-omni)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/configure-omni)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/configure-omni)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/configure-omni)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/configure-omni)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/configure-omni)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/configure-omni)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/configure-omni)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/configure-omni)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/configure-omni)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/configure-omni)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/configure-omni)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/configure-omni)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/configure-omni)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/configure-omni)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/configure-omni)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/configure-omni)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/configure-omni)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/configure-omni)

This page shows common settings when using AlloyDB Omni for production workloads. 

## Enable huge pages

AlloyDB Omni, just like PostgreSQL, supports the use of huge pages. This requires your machine to have huge pages enabled, and you also need to enable a database setting `huge_pages`.

Run the provided script to enable huge pages on your machine:

### Docker
    
    
          docker run --rm --privileged google/alloydbomni setup-host
          

### Docker
    
    
          docker run --rm --privileged google/alloydbomni setup-host
          

### Podman
    
    
          podman run --rm --privileged google/alloydbomni setup-host
          

### Podman
    
    
          podman run --rm --privileged google/alloydbomni setup-host
          

Add the following line to your `postgresql.conf` to enable huge pages: 
    
    
       huge_pages=on

## Enable swapping

Swapping in the operating system lets you extend available physical memory by moving inactive memory pages between random access memory (RAM) and the hard disk to free up RAM space for active processes. AlloyDB Omni uses swapping when it is under high load and requires extra memory.

To check how much swapping space is enabled on your system, run the following:
    
    
       cat /proc/meminfo | grep SwapTotal

The output looks similar to the following:
    
    
       SwapTotal:      165748732 kB
    

To enable swapping on your operating system if the output value is `0`, see the following:

  * [Debian](https://wiki.debian.org/Swap)
  * [Ubuntu](https://help.ubuntu.com/community/SwapFaq)




## Enable core dumps

If AlloyDB Omni encounters an unrecoverable error and crashes, it is helpful to have a core dump for analysis. A core dump is a snapshot of the memory of the AlloyDB Omni process at the point of its crash.

To set up core dumps, set up `kernel.core_pattern` as follows:

  1. Use the `sysctl` command to configure run time kernel parameters.
  2. To set the `kernel.core_pattern` immediately, use:
         
         sysctl -w kernel.core_pattern="CORE_PATTERN"

Replace `CORE_PATTERN` with a core filename pattern such as "%e-%t.core".

For more information on core filename patterns, see [How to set process core file names](https://access.redhat.com/solutions/901293#:%7E:text=an%20unknown%20key-,Resolution,-In%20current%20linux%22) for details.

The [systemd-coredump handler](https://systemd.io/COREDUMP/) allows further configuration of your coredump settings. The tool is installed by default in RHEL. On Debian and Ubuntu systems, run `sudo apt install coredumpctl` to install the tool.




When you start AlloyDB Omni, ensure that you pass the `--ulimit=core:-1:-1` argument in the `docker run` command:

### Docker
    
    
       docker run --name CONTAINER_NAME   
    
       -e POSTGRES_PASSWORD=NEW_PASSWORD   
    
       --ulimit=core:-1:-1   
    
       -p HOST_PORT:5432 -d google/alloydbomni
       

### Docker
    
    
       docker run --name CONTAINER_NAME   
    
       -e POSTGRES_PASSWORD=NEW_PASSWORD   
    
       --ulimit=core:-1:-1   
    
       -p HOST_PORT:5432 -d google/alloydbomni
       

### Podman
    
    
       podman run --name CONTAINER_NAME   
    
       -e POSTGRES_PASSWORD=NEW_PASSWORD   
    
       --ulimit=core:-1:-1   
    
       -p HOST_PORT:5432 -d google/alloydbomni
       

### Podman
    
    
       podman run --name CONTAINER_NAME   
    
       -e POSTGRES_PASSWORD=NEW_PASSWORD   
    
       --ulimit=core:-1:-1   
    
       -p HOST_PORT:5432 -d google/alloydbomni
       

Replace the following:
    
    
      - `CONTAINER_NAME`: the name of a new
        AlloyDB Omni container&mdash;for example, `my-omni-1`.
      - `NEW_PASSWORD`: the password assigned to the new
        container's `postgres` user after the password creation.
    

## Enable internal logging

AlloyDB Omni provides more messages in addition to regular [PostgreSQL logs](https://www.postgresql.org/docs/current/runtime-config-logging.html). These messages are intended for AlloyDB for PostgreSQL support because of their technical nature. However, additional information can assist in the debugging of database issues.

To enable internal logging, complete these steps:

  1. Set the database parameter `enable_alloydb_internal_log` to `on`:
         
         ALTER SYSTEM SET enable_alloydb_internal_log=on;
         

For more information about modifying AlloyDB Omni settings, see [Configure AlloyDB Omni database parameters](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/configure-database-flags).

  2. Restart the AlloyDB Omni service:




### Docker
    
    
       docker restart CONTAINER_NAME
       

### Docker
    
    
       docker restart CONTAINER_NAME
       

### Podman
    
    
       podman restart CONTAINER_NAME
       

### Podman
    
    
       podman restart CONTAINER_NAME
       

To customize internal logging such as configuring log file names and rotation policies further, use [PostgreSQL parameters](https://www.postgresql.org/docs/current/runtime-config-logging.html).

For example, the `log_directory` parameter specifies the directory where to save a log file and the `log_filename` parameter defines the name of the individual log file.

AlloyDB Omni combines the `log_directory` and `log_filename` parameters and saves internal logs as follows:
    
    
    LOG_DIRECTORY/LOG_FILENAME.internal
    

## Set up systemd units to run operations automatically

If you run AlloyDB Omni on a dedicated server, then you may want to configure certain operations to start automatically when the server boots up. One way to do this is through `systemd` units.

For example, the following steps configure `systemd` so that huge pages are enabled automatically whenever the server boots up.

Create a file in `/etc/systemd/system/alloydb-setup-env.service`:
    
    
       [Unit]
       Description=Setup huge pages for AlloyDB Omni
    
       [Service]
       Type=oneshot
    
       ExecStart=/usr/bin/docker run --rm --privileged google/alloydbomni setup-host
    
       [Install]
       WantedBy=multi-user.target
    

Enable the service as follows:
    
    
       sudo systemctl enable alloydb-setup-env.service

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/run-connect).

  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage).

  * [Create a read-only replica](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/set-up-read-replica).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
