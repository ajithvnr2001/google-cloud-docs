---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/omni-cli/
title: Install and manage the AlloyDB Omni CLI \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:01.054518+00:00
---

# Install and manage the AlloyDB Omni CLI  |  AlloyDB Omni for Kubernetes: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/omni-cli/

This page documents AlloyDB Omni version **15.5.2** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/overview)



Send feedback 

#  Install and manage the AlloyDB Omni CLI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/omni-cli)

The AlloyDB Omni CLI is a command-line tool that lets you install, run, and manage AlloyDB Omni. You can download and install it at no cost by using various Linux package-management tools. 

## Install the AlloyDB Omni CLI

The specific commands needed to install the AlloyDB Omni CLI depend on your Linux distribution.

### Install on Debian or Ubuntu

To install the AlloyDB Omni CLI on Debian or on Debian-based Linux distributions such as Ubuntu, run the following commands:
    
    
    curl https://REGION-apt.pkg.dev/doc/repo-signing-key.gpg | sudo apt-key add -
    sudo apt update
    echo "deb https://REGION-apt.pkg.dev/projects/alloydb-omni alloydb-omni-apt main" \
      | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
    sudo apt update
    sudo apt-get install alloydb-cli

Replace `REGION` with one of the following:

  * `asia`
  * `europe`
  * `us`



### Install on RHEL

To install the AlloyDB Omni CLI on Red Hat Enterprise Linux (RHEL), run the following commands:
    
    
    sudo tee -a /etc/yum.repos.d/artifact-registry.repo << EOF
    [alloydb-omni-yum]
    name=alloydb-omni-yum
    baseurl=https://REGION-yum.pkg.dev/projects/alloydb-omni/alloydb-omni-yum
    enabled=1
    repo_gpgcheck=0
    gpgcheck=0
    EOF
    sudo yum makecache
    sudo yum --enablerepo=alloydb-omni-yum install -y alloydb-cli

Replace `REGION` with one of the following:

  * `asia`
  * `europe`
  * `us`



## Update the AlloyDB Omni CLI

The specific commands needed to update the AlloyDB Omni CLI depend on your Linux distribution.

### Update on Debian or Ubuntu
    
    
    sudo apt-get update
    sudo apt-get install alloydb-cli

### Update on RHEL
    
    
    sudo yum makecache
    sudo yum install alloydb-cli -y

## Uninstall the AlloyDB Omni CLI

The specific commands needed to uninstall the AlloyDB Omni CLI depend on your Linux distribution.

### Uninstall from Debian or Ubuntu
    
    
    sudo apt-get remove alloydb-cli

### Uninstall from RHEL
    
    
    sudo yum remove alloydb-cli

## What's next

  * [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/install)

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/run-connect)

  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/manage)

  * [Create a read-only replica](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/set-up-read-replica)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
