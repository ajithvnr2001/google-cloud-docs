---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/quickstart/
title: Install AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:54.517609+00:00
---

# Install AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/quickstart/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Install AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

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

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This quickstart shows you how to install AlloyDB Omni on your own environment in a few steps.

  * To install a production-ready AlloyDB Omni cluster in a Linux environment, see Install AlloyDB Omni on Debian or Ubuntu.



## Install AlloyDB Omni on Debian or Ubuntu

This section shows you how to install AlloyDB Omni using the AlloyDB Omni CLI in your Debian or Ubuntu environment.

#### System requirements

Ensure that you have a Linux machine that meets the following system requirements:

  * A virtual or physical machine running a Debian-based OS, such as Debian or Ubuntu.
  * A minimum of 2 CPUs, with x86/AMD64 architecture.
  * A minimum of 2 GB of RAM. For optimal performance, we recommend allocating 8 GB of RAM for each CPU.
  * At least 20 GB of available storage.
  * Unrestricted root access within the OS.
  * Linux kernel version 4.18 or higher. We recommend kernel version 5.3 or higher for best performance.
  * Linux cgroup v2 enabled. 

By default, cgroup v2 is enabled on most modern Linux systems. To check whether cgroup v2 is enabled, run `stat -fc %T /sys/fs/cgroup/` in a shell. If cgroup v2 is enabled, the command output shows `cgroup2fs`.

  * TCP port `5432` not in use by any other service.
  * If you are installing AlloyDB Omni on a cloud platform, then we recommend using the following instance types:
    * On Google Cloud, we recommend `n2-highmem` instances.
    * On Amazon Web Services, we recommend `R6i` instances.
    * On Microsoft Azure, we recommend `Ebsv5` instances.



  1. Install the AlloyDB Omni CLI and Docker on your Debian or Ubuntu machine:
         
         curl https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo apt-key add -
           sudo apt update
           echo "deb https://us-apt.pkg.dev/projects/alloydb-omni alloydb-omni-apt main" \
           | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
           sudo apt update
           sudo apt-get -y install alloydb-cli docker.io

  2. Use the command-line program to install and launch the AlloyDB Omni server software:
         
         sudo alloydb database-server install

  3. Connect to AlloyDB Omni using `psql`:
         
         sudo docker exec -it pg-service psql -h localhost -U postgres

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.




## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect)

  * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
