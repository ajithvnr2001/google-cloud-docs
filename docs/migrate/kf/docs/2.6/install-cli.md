---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/install-cli/
title: Install the Kf CLI \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:22.495637+00:00
---

# Install the Kf CLI  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/install-cli/

Version 2.6

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.6/getting-started)



Send feedback 

#  Install the Kf CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install the Kf CLI. You typically install the Kf CLI when you already have access to a GKE cluster running Kf. That means that you can get started using Kf commands without having to first create your own GKE cluster.

After installing the Kf CLI and connecting to the Kf cluster, you can run any of the Kf commands. For a complete list of the available Kf commands, see the [Kf command reference](https://docs.cloud.google.com/migrate/kf/docs/2.6/cli).

## Before you begin

Before you can use the Kf CLI, you must have access to a GKE cluster running a full Kf installation. That means that you have run the following command to connect to the cluster:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --project=CLUSTER_PROJECT_ID \
        --zone=CLUSTER_LOCATION

## Install the CLI

  1. Install the Kf CLI:

### Linux

This command installs the Kf CLI for all users on the system. Follow the instructions in the Cloud Shell tab to install it just for yourself.
         
         gcloud storage cp gs://kf-releases/v2.6.1/kf-linux /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Mac

This command installs `kf` for all users on the system.
         
         gcloud storage cp gs://kf-releases/v2.6.1/kf-darwin /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Cloud Shell

This command installs `kf` on your Cloud Shell instance if you use `bash`, the instructions may need to be modified for other shells.
         
         mkdir -p ~/bin
         gcloud storage cp gs://kf-releases/v2.6.1/kf-linux ~/bin/kf
         chmod a+x ~/bin/kf
         echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc
         source ~/.bashrc

### Windows

This command downloads `kf` to current directory. Add it to the path if you want to call if from anywhere other than the current directory.
         
         gcloud storage cp gs://kf-releases/v2.6.1/kf-windows.exe kf.exe




## Upgrade the CLI

If you have an existing installation of the Kf CLI, then you can use the following procedure to upgrade it to the current version.

  1. Install the CLI:

### Linux

This command installs the Kf CLI for all users on the system. Follow the instructions in the Cloud Shell tab to install it just for yourself.
         
         gcloud storage cp gs://kf-releases/v2.6.1/kf-linux /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Mac

This command installs `kf` for all users on the system.
         
         gcloud storage cp gs://kf-releases/v2.6.1/kf-darwin /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Cloud Shell

This command installs `kf` on your Cloud Shell instance if you use `bash`, the instructions may need to be modified for other shells.
         
         mkdir -p ~/bin
         gcloud storage cp gs://kf-releases/v2.6.1/kf-linux ~/bin/kf
         chmod a+x ~/bin/kf
         echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc
         source ~/.bashrc

### Windows

This downloads `kf` to current directory. Add it to the path if you want to call if from anywhere other than the current directory.
         
         gcloud storage cp gs://kf-releases/v2.6.1/kf-windows.exe kf.exe

  2. Validate the Kf CLI and Kf server versions match:

     * The CLI version is listed under `Kf Client`.
     * The Kf server version is listed under `kf["app.kubernetes.io/version"]`.
    
    $ kf debug
    ...
    Version:
      **Kf Client:                        v2.6.1**
      Server version:                   v1.21.3-gke.2001
      **kf["app.kubernetes.io/version"]:  v2.6.1**
    ...
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
