---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/manage-dump-files/
title: Generate and diagnose AlloyDB Omni using RPM dump files \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:39:40.209032+00:00
---

# Generate and diagnose AlloyDB Omni using RPM dump files  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/manage-dump-files/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)



Send feedback 

#  Generate and diagnose AlloyDB Omni using RPM dump files Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/manage-dump-files)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/manage-dump-files)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/manage-dump-files)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/manage-dump-files)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage-dump-files)

This page describes how to generate AlloyDB Omni system dump files and analyze the causes of unexpected issues. 

## Before you begin

The `alloydb-sysdump` utility is included in the AlloyDB Omni package. The utility is available at `/usr/lib/postgresql/PG_VERSION/bin/alloydb-sysdump`, where `PG_VERSION` is the PostgreSQL major version, for example, `18`.

## Generate an AlloyDB Omni dump file

You can manually generate an AlloyDB Omni dump file any time. Examining the dump file helps you or Google Cloud Customer Care analyze issues with your AlloyDB Omni installation, such as deadlocks that block new connections, slow queries, slow vacuum, high usage of memory, CPU, or storage.

To generate a dump file, run the following command:
    
    
        sudo /usr/lib/postgresql/PG_VERSION/bin/alloydb-sysdump -r -D=DATA_DIR -s=SERVICE_NAME -U=USERNAME -p=PORT -H=HOSTNAME
       

Replace the following:

  * `PG_VERSION`: the PostgreSQL major version of your AlloyDB Omni installation, for example, `18`.
  * `DATA_DIR`: the path to your AlloyDB Omni data directory, for example, `/var/alloydb/main/data`.
  * `SERVICE_NAME`: the name of the AlloyDB Omni systemd service. The default value is `alloydbomni18`.
  * `USERNAME`: the name of the user connecting to the database. The default value is `alloydbadmin`.
  * `PORT`: the TCP port where AlloyDB Omni accepts connections on. The default value is `5432`.
  * `HOSTNAME`: the hostname of the machine on which AlloyDB Omni runs. If the value begins with a slash, it is used as the directory for a Unix domain socket. The default value is `localhost`.

The following example command generates a dump file for an AlloyDB Omni version 18 installation using default values:
        
        sudo /usr/lib/postgresql/18/bin/alloydb-sysdump -r -D=/var/alloydb/main/data -s=alloydbomni18 -U=alloydbadmin -p=5432 -H=localhost

The command output displays the location of the system dump file.

To learn more about the command arguments, run:
        
        /usr/lib/postgresql/PG_VERSION/bin/alloydb-sysdump --help




## Review an AlloyDB Omni dump file

An AlloyDB Omni dump file is an ordinary text file that summarizes various aspects of the system's state. To review it, open it in a text editor, the `less` program, or any other program for viewing text files.

AlloyDB Omni saves the file in your data directory, and it names the file as `alloydb_system_dump_` followed by a timestamp. For example, `alloydb_system_dump_20240614_062953PM`.

## Create a support case for assistance

If you need assistance in interpreting a system dump file to troubleshoot a problem with AlloyDB Omni, then [create a support case](https://docs.cloud.google.com/support/docs/manage-cases#creating_cases) and attach the file to it. You must have a Google Cloud account to create a support case.

The AlloyDB team responds to the case based on its priority and the respective support service at the time of creation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
