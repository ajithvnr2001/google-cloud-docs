---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/issues-with-m2c-cli/
title: Issues with Migrate to Containers CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:18.011466+00:00
---

# Issues with Migrate to Containers CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/issues-with-m2c-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Issues with Migrate to Containers CLI

This document describes workarounds for some issues that you might encounter while working with the Migrate to Containers CLI.

## Copy operation fails due to permission errors

To gain read access on the entire file system, the `copy` command is run using a superuser on the source machine. However, sometimes the copy operation still fails due to permission errors. This issue occurs because in some cases even the superuser doesn't have read access to some directories on the source machine.

In such cases, you might see an error message similar to the following message:
    
    
    E   rsync   rsync: send_files failed to open "/var/lib/lxcfs/cgroup/blkio/blkio.reset_stats": Permission denied (13)
    ...
    E   rsync   rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1865) [generator=3.2.7]
    Error: failed to copy fs from GCP VM "petclinic-springboot": failed copying vm to "/tmp/copy-1411243774": exit status 23
    

As a workaround for this issue, create a custom filter to exclude such directories from the copy operation.

For example, to exclude the `/var/lib/lxcfs` directory from the copy operation, add the following custom filter in the filters file:
    
    
    - /var/lib/lxcfs
    

For more information, see [Reduce the size of the copied file system](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/copy-file-system#reduce_the_size_of_the_copied_file_system).

## Copy operation using `gcloud` fails to authenticate to the machine

If you use `gcloud` to run the `copy` command with `sudo`, then in some cases, the copy operation might fail to authenticate to the source machine. This issue occurs because `gcloud` is run with the same superuser that runs the Migrate to Containers CLI, and the superuser doesn't have the same credentials as the standard user.

In such cases, you might see an error message similar to the following message:
    
    
    E ssh init ERROR: (gcloud.compute.ssh) There was a problem refreshing your current auth tokens: ('Failed to retrieve TOKEN from the Google Compute Engine metadata service. Status: 404 Response:\nb\'"No service account scopes specified."\'', <google.auth.transport.requests._Response object at 0x7fecf5c75550>)
    E ssh init Please run:
    E ssh init
    E ssh init  $ gcloud auth login
    E ssh init
    E ssh init to obtain new credentials.
    E ssh init
    E ssh init If you have already logged in with a different account:
    E ssh init
    E ssh init    $ gcloud config set account ACCOUNT
    E ssh init
    E ssh init to select an already authenticated account to use.
    Error: failed to initiate a connection with GCP VM "tomcat-server": exit status 1
    

As a workaround for this issue, try running the `copy` command using `gcloud` without `sudo`.

## The `analyze` command fails when using the Snap version of Docker

If you're using the Snap version of Docker, then the `analyze` command fails.

In such cases, you might see an error message similar to the following message:
    
    
    I       Unpacking file system...
    I       Running analysis...
    Error: running analysis failed: failed to run container: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: PATH
    

As a workaround for this issue, install Docker again without using Snap. For more information, see [Install Docker Engine](https://docs.docker.com/engine/install/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
