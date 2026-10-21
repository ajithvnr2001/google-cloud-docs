---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/downloads/
title: Config Sync downloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:11:40.363348+00:00
---

# Config Sync downloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/resources)



Send feedback 

#  Config Sync downloads Stay organized with collections  Save and categorize content based on your preferences. 

This page contains links to download the Config Sync manifest and `nomos` binaries for each generally available (GA) release of Config Sync.

  * You must have access to the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud) commands provided by the [Google Cloud CLI](https://docs.cloud.google.com/sdk).
  * Before using the instructions on this page, you must authenticate to Google Cloud using the `gcloud auth login` command. Only [authenticated](https://docs.cloud.google.com/sdk/docs/authenticate) users are authorized to download artifacts. If you are not authenticated, you might see the `AccessDeniedException` error.



## Stable

Use these links to download the newest stable version of all Config Sync components. For a specific version, see the section for that version.

The latest stable product version is **1.25.1**.

### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/latest/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation using the instructions in [Manually installing Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features.

### `nomos` command

To download the `nomos` command-line tool, use **one** of the following commands:

#### Any supported platform
    
    
    gcloud components install nomos
    

We recommend that you use [`gcloud components install`](https://docs.cloud.google.com/sdk/gcloud/reference/components/install) to install the `nomos` command-line tool. Installing `nomos` with the Google Cloud CLI lets you use [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) to update `nomos` to the latest version.

#### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/latest/linux_amd64/nomos nomos
    

#### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/latest/linux_arm64/nomos nomos
    

#### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/latest/darwin_amd64/nomos nomos
    

#### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/latest/darwin_arm64/nomos nomos
    

#### Extra step for directly-installed Linux and macOS clients

**Note:** This step is not required if you installed `nomos` using the Google Cloud CLI.

After downloading the binary, configure it to be executable:
    
    
    chmod +x /path/to/nomos
    

You can move the command to a location your system searches for binaries, such as `/usr/local/bin`, or you can run the command by using its fully-qualified path.

## Supported version instructions

### v1.25.1

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.1-rc.2/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.1-rc.2/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.1-rc.2/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.1-rc.2/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.1-rc.2/darwin_arm64/nomos nomos
    

### v1.25.0

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.0-rc.1/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.0-rc.1/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.0-rc.1/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.0-rc.1/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.25.0-rc.1/darwin_arm64/nomos nomos
    

### v1.24.3

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.3-rc.2/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.3-rc.2/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.3-rc.2/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.3-rc.2/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.3-rc.2/darwin_arm64/nomos nomos
    

### v1.24.2

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.2-rc.2/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.2-rc.2/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.2-rc.2/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.2-rc.2/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.2-rc.2/darwin_arm64/nomos nomos
    

### v1.24.1

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.1-rc.1/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.1-rc.1/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.1-rc.1/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.1-rc.1/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.1-rc.1/darwin_arm64/nomos nomos
    

### v1.24.0

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.0-rc.4/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.0-rc.4/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.0-rc.4/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.0-rc.4/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/v1.24.0-rc.4/darwin_arm64/nomos nomos
    

### v1.23.3

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/1.23.3-rc.1/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.3-rc.1/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.3-rc.1/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.3-rc.1/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.3-rc.1/darwin_arm64/nomos nomos
    

### v1.23.2

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/1.23.2/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.2/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.2/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.2/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.2/darwin_arm64/nomos nomos
    

### v1.23.1

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/1.23.1/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.1/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.1/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.1/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.1/darwin_arm64/nomos nomos
    

### v1.23.0

#### Config Sync manifest

To download Config Sync, run the following command:
    
    
    gcloud storage cp gs://config-management-release/released/1.23.0/config-sync.tar.gz config-sync.tar.gz
    

After downloading the manifest, install or upgrade your installation by using the instructions in [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl).

#### `nomos`

**Note:** When you upgrade Config Sync, also upgrade the `nomos` command on all clients to ensure that it can validate configs that take advantage of new features. 

To download the `nomos` command, use **one** of the following commands:

##### Linux amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.0/linux_amd64/nomos nomos
    

##### Linux arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.0/linux_arm64/nomos nomos
    

##### macOS amd64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.0/darwin_amd64/nomos nomos
    

##### macOS arm64
    
    
    gcloud storage cp gs://config-management-release/released/1.23.0/darwin_arm64/nomos nomos
    

## What's next

  * [Read the release notes](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/release-notes)
  * [Read the Config Sync overview](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync)
  * [Use the `nomos` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
