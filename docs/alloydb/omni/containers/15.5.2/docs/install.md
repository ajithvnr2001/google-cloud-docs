---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install/
title: Customize your AlloyDB Omni installation \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:38:22.581618+00:00
---

# Customize your AlloyDB Omni installation  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Customize your AlloyDB Omni installation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

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

This page shows you how to download, install, and connect to [AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs). To get started quickly with AlloyDB Omni using the default configuration, see [Install AlloyDB Omni on Debian or Ubuntu](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/quickstart).

In this document, you also learn how to do the following:

  * Create a new disk partition to optimize data storage.
  * Configure your server.
  * Ensure compatibility with Debian, Ubuntu, and RHEL.



## Before you begin

#### System requirements

### Debian

  * A virtual or physical machine running a Debian-based OS, such as Debian or Ubuntu.
  * A minimum of 2 CPUs, with x86/AMD64 architecture.
  * A minimum of 2 GB of RAM. For optimal performance, we recommend allocating 8 GB of RAM for each CPU.
  * At least 20 GB of available storage.
  * Unrestricted root access within the OS.
  * Docker version 20.10 or higher.
  * Linux kernel version 4.18 or higher. We recommend kernel version 5.3 or higher for best performance.
  * Linux cgroup v2 enabled. 

By default, cgroup v2 is enabled on most modern Linux systems. To check whether cgroup v2 is enabled, run `stat -fc %T /sys/fs/cgroup/` in a shell. If cgroup v2 is enabled, the command output shows `cgroup2fs`.

  * If you want to integrate with Vertex AI, then you need the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) available in your environment.

  * To install AlloyDB Omni on a cloud platform, we recommend using the following instance types: 
    * On Google Cloud, we recommend `n2-highmem` instances.
    * On Amazon Web Services, we recommend `R6i` instances.
    * On Microsoft Azure, we recommend `Ebsv5` instances.
  * We recommend that you use a dedicated SSD storage device for storing your data. If you use a physical device for this purpose, we recommend attaching it directly to the host machine.



### RHEL

  * A virtual or physical machine running a Red Hat Enterprise Linux (RHEL) version 8 or later. To let the automatic memory management features of AlloyDB Omni work, use RHEL version 9 or later.
  * A minimum of 2 CPUs, with x86/AMD64 architecture.
  * A minimum of 2 GB of RAM. For optimal performance, we recommend allocating 8 GB of RAM for each CPU.
  * At least 20 GB of available storage.
  * Unrestricted root access within the OS.
  * Docker version 20.10 or higher.
  * Linux kernel version 4.18 or higher. We recommend kernel version 5.3 or higher for best performance.
  * Linux cgroup v2 enabled. 

By default, cgroup v2 is enabled on most modern Linux systems. To check whether cgroup v2 is enabled, run `stat -fc %T /sys/fs/cgroup/` in a shell. If cgroup v2 is enabled, the command output shows `cgroup2fs`.

  * If you want to integrate with Vertex AI, then you need the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) available in your environment.

  * To install AlloyDB Omni on a cloud platform, we recommend using the following instance types: 
    * On Google Cloud, we recommend `n2-highmem` instances.
    * On Amazon Web Services, we recommend `R6i` instances.
    * On Microsoft Azure, we recommend `Ebsv5` instances.
  * We recommend that you use a dedicated SSD storage device for storing your data. If you use a physical device for this purpose, we recommend attaching it directly to the host machine.



## Download and install AlloyDB Omni

**Note:** To install the latest version of AlloyDB Omni, see [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/docs/omni/install).

  1. [Install the AlloyDB Omni CLI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/omni-cli#install-debian).

  2. Use the AlloyDB Omni CLI to confirm that your Linux machine is ready to install AlloyDB Omni:
         
         sudo alloydb system-check

If needed, modify your system until the output of the `system-check` command returns a successful check.

  3. Optional: To create a new disk partition for AlloyDB Omni to use for data storage, we recommend that you use an `ext4` file system for optimal performance.

     1. To create an `ext4` file system, use the following command:
            
            mkfs.ext4 -m 1 -F "$disk_path"

     2. To mount your disk, use the following command:
            
            mount --make-shared -o noatime,discard,errors=panic "$disk_path" "$disk_mountpoint"

  4. Install the server software using one of the following options:

**Note:** To install AlloyDB Omni with machine learning (ML) functions enabled, including the ability to query large language models (LLMs), see [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-with-alloydb-ai).
     * To configure the server as a primary instance, run the following command:
           
           sudo alloydb database-server install --data-dir=$(realpath DATA_DIR)

Replace `DATA_DIR` with the directory on your local file system where you want AlloyDB Omni to store its data, metadata, and configuration files. AlloyDB Omni tries to create this directory if it doesn't already exist. If you don't specify this value, then AlloyDB Omni defaults to `/var/alloydb/main/`.

To have AlloyDB Omni listen for connections on a TCP port other than the default `5432`, include the `--pg-port` flag:
           
           sudo alloydb database-server install \
               --data-dir=$(realpath DATA_DIR) \
               --pg-port=PORT

Replace `PORT` with the TCP port that you want AlloyDB Omni to accept connections on.

     * To configure the server as a read replica, include the `--replica-source-ip` and `--replica-source-port` flags:
           
           sudo alloydb database-server install \
               --data-dir=$(realpath DATA_DIR) \
               --replica-source-ip=SOURCE_IP \
               --replica-source-port=SOURCE_PORT

Replace the following:

       * `DATA_DIR`: the directory on your local file system where you want AlloyDB Omni to store its data, metadata, and configuration files. AlloyDB Omni tries to create this directory if it doesn't already exist. If you don't specify this value, then AlloyDB Omni defaults to `/var/alloydb/main/`.

       * `SOURCE_IP`: the IP address of the primary AlloyDB Omni instance to replicate from.

       * `SOURCE_PORT`: the TCP port of the primary AlloyDB Omni instance to replicate from. If you don't provide this value, then AlloyDB Omni applies a default value of `5432`.

For more information on AlloyDB Omni read replicas, see [Create a read-only replica](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-read-replica).

  5. If your system runs Red Hat Enterprise Linux, then update the `/usr/lib/tuned/virtual-guest/tuned.conf` file with the following:
         
         vm.swappiness=1
         




## Connect to and use the database server

Connect to AlloyDB Omni using `psql`:
    
    
    sudo docker exec -it pg-service psql -h localhost -U postgres

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
