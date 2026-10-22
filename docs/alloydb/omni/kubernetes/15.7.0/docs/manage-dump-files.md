---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/manage-dump-files/
title: Generate and diagnose AlloyDB Omni dump files \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:40.032619+00:00
---

# Generate and diagnose AlloyDB Omni dump files  |  AlloyDB Omni for Kubernetes: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/manage-dump-files/

This page documents AlloyDB Omni version **15.7.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/overview)



Send feedback 

#  Generate and diagnose AlloyDB Omni dump files Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/manage-dump-files)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/manage-dump-files)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/manage-dump-files)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/manage-dump-files)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/manage-dump-files)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/manage-dump-files)

This page describes how to generate AlloyDB Omni system dump files and analyze the causes of unexpected issues. 

## Before you begin

Extract the `alloydb-sysdump` utility that is included in the AlloyDB Omni Docker image you [installed](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/install):

###  Docker 
    
    
    docker run --rm --entrypoint /bin/bash $IMAGE -c
    "cat /usr/lib/postgresql/15/bin/alloydb-sysdump"
    > /tmp/alloydb-sysdump
    chmod +x /tmp/alloydb-sysdump

###  Podman 
    
    
    podman run --rm --entrypoint /bin/bash $IMAGE -c
    "cat /usr/lib/postgresql/15/bin/alloydb-sysdump"
    > /tmp/alloydb-sysdump
    chmod +x /tmp/alloydb-sysdump

## Generate an AlloyDB Omni dump file

You can manually generate an AlloyDB Omni dump file any time. Examining the dump file helps you or Google Cloud Customer Care analyze issues with your AlloyDB Omni installation, such as deadlocks that block new connections, slow queries, slow vacuum, high usage of memory, CPU, or storage.

To generate a dump file, run the following command:
    
    
       sudo /tmp/alloydb-sysdump -D=INSTALL_PATH -U=USERNAME -p=PORT -H=HOSTNAME -c=CONTAINER_NAME

Replace the following:

  * `INSTALL_PATH`: the path to your AlloyDB Omni installation directory accessible from the host file system.
  * `USERNAME`: the name of the user connecting to the database.
  * `PORT`: the TCP port where AlloyDB Omni accepts connections on. The default value is `5432`.
  * `HOSTNAME`: the hostname of the machine on which AlloyDB Omni runs. If the value begins with a slash, it is used as the directory for a Unix domain socket. The default value is `localhost`.
  * `CONTAINER_NAME`: the name of the container in which AlloyDB Omni runs.

The command output displays the location of the system dump file.

To learn more about the command arguments, run:
        
        /tmp/alloydb-sysdump --help




## Review an AlloyDB Omni dump file

An AlloyDB Omni dump file is an ordinary text file that summarizes various aspects of the system's state. To review it, open it in a text editor, the `less` program, or any other program for viewing text files.

AlloyDB Omni saves the file in your data directory, and it names the file as `alloydb_system_dump_` followed by a timestamp. For example, `alloydb_system_dump_20240614_062953PM`.

## Create a support case for assistance

If you need assistance in interpreting a system dump file to troubleshoot a problem with AlloyDB Omni, then [create a support case](https://docs.cloud.google.com/support/docs/manage-cases#creating_cases) and attach the file to it. You must have a Google Cloud account to create a support case.

The AlloyDB team responds to the case based on its priority and the respective support service at the time of creation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
