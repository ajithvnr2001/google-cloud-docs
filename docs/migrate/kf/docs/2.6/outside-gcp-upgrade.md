---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/outside-gcp-upgrade/
title: Upgrade Kf outside Google Cloud \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:27:15.033712+00:00
---

# Upgrade Kf outside Google Cloud  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/outside-gcp-upgrade/

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

#  Upgrade Kf outside Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to upgrade an existing Kf installation and its dependencies. 

As part of the upgrade procedure, ensure that your Kf installation uses the latest version of the Kf operator:

  * Confirm your current Kf version can upgrade to Kf v2.6.1.
  * Upgrade to Kf v2.6.1.
  * Upgrade dependencies (if needed).



## Before you begin

**Warning:** Kf currently only supports upgrading one minor version at a time. The steps on this page are for upgrading Kf v2.5.x to Kf v2.6.1. If your current version is not Kf v2.5.x, you must first upgrade incrementally until your current version is v2.5.x.

You will need:

  * An existing cluster with Kf installed.
  * Access to a machine with `gcloud`, `kf`, and `kubectl` installed.



## Prepare for the upgrade

### Connect to your target cluster
    
    
    gcloud container hub memberships get-credentials CLUSTER_NAME \
     --zone CLUSTER_ZONE \
     --project CLUSTER_PROJECT_ID

### Confirm that your current Kf CLI and server versions match

Run `kf debug` and validate the Kf CLI and Kf server versions match.

  * The CLI version is listed under `Kf Client`.
  * The Kf server version is listed under `kf["app.kubernetes.io/version"]`.


    
    
    $ kf debug
    ...
    Version:
      **Kf Client:                        v2.5.4**
      Server version:                   v1.21.3-gke.2001
      **kf["app.kubernetes.io/version"]:  v2.5.4**
    ...
    

If the Kf client and Kf server values **do not** match, but the server version is v2.5.x, install the Kf v2.6.1 CLI before you continue.

If the Kf server value is older than v2.5.x, you must first incrementally upgrade to Kf v2.5.x to continue.

### Confirm that Kf is healthy before upgrading

Run `kf doctor` to check the state of your cluster. Ensure all tests pass before you continue.
    
    
    $ kf doctor
    ...
    === RUN doctor/user
    === RUN doctor/user/ContainerRegistry
    --- PASS: doctor/user
       --- PASS: doctor/user/ContainerRegistry
    ...
    

If you see any `FAIL` or `Error: environment failed checks` messages, follow the guidance in the `kf doctor` output, or view the [troubleshooting guide](https://docs.cloud.google.com/migrate/kf/docs/2.6/support/troubleshooting) to resolve the issue and retry the command until it is successful.

## Upgrade the operator

The Kf operator performs upgrades for you.

  1. Apply the operator yaml:

**Note:** This operation starts immediately, and is not reversible.
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.6.1/operator.yaml"




## Upgrade Kf dependencies

  1. Upgrade Tekton:
         
         kubectl apply -f "https://storage.googleapis.com/tekton-releases/pipeline/previous/v0.26.0/release.yaml"

  2. Upgrade to the latest Cloud Service Mesh:

     1. Follow the steps in the [Cloud Service Mesh upgrade guide](https://docs.cloud.google.com/service-mesh/docs/unified-install/upgrade).



## Upgrade to the Kf v2.6.1 CLI

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
    




## Verify that Kf upgraded successfully

  1. Run `doctor` to ensure the newly installed version is healthy:
         
         kf doctor --retries=20

The command runs cluster checks several times. It's normal for a few of the attempts to fail while the new controllers are starting.

If the command fails with the message `Error: environment failed checks`, follow the guidance in the `doctor` output to resolve the issue and retry the command until it is successful.




If the verification steps pass, your cluster has successfully been upgraded! If you have any issues, please review the [support](https://docs.cloud.google.com/migrate/kf/docs/2.6/support) page for guidance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
