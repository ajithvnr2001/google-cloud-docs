---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/configure-omni/
title: Configure AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:33.792915+00:00
---

# Configure AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/configure-omni/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Configure AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

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

This page shows how to configure AlloyDB Omni after you have [installed it](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install). 

#### Change your data directory location

AlloyDB Omni has a default configuration file named `dataplane.conf` that's present in the `/var/alloydb/config` directory. To change your server's data directory location, update the `DATADIR_PATH` variable in the `dataplane.conf` file.

To update the `DATADIR_PATH` variable in `dataplane.conf`, run the following command:
    
    
    sudo sed -i "s|^\(DATADIR_PATH=\).*|\1DATA_DIRECTORY|" /var/alloydb/config/dataplane.conf

Replace `DATA_DIRECTORY` with the full file system path to the existing directory that you want to contain your AlloyDB Omni installation.

Alternately, use a text editor to open `dataplane.conf` and update the value of the `DATADIR_PATH` directive.

**Note:** Set the value of `DATADIR_PATH` to the directory that contains the `data` subdirectory—for example, `$HOME/alloydb` and not `$HOME/alloydb/data`.

#### Configure other server options

The `/var/alloydb/config` directory also contains the following two standard PostgreSQL configuration files:

  * [`postgresql.conf`](https://www.postgresql.org/docs/current/config-setting.html)
  * [`pg_hba.conf`](https://www.postgresql.org/docs/15/auth-pg-hba-conf.html)



The AlloyDB Omni installer populates both of these files with default values to get you started. You can update both files in whatever way is appropriate for your own needs.

**Caution:** AlloyDB Omni copies these files into your data directory for its own runtime use. Edit only the files in `/var/alloydb/config`, and not the copies in your data directory. Otherwise, any changes you make to those files risk being overwritten. 

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect).

  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage).

  * [Create a read-only replica](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-read-replica).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
