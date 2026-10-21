---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/upgrade/
title: Upgrade Kf \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T10:41:56.511702+00:00
---

# Upgrade Kf  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/upgrade/

Version 2.3

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
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.3/getting-started)



Send feedback 

#  Upgrade Kf Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to upgrade an existing Kf installation and its dependencies. 

## Before you begin

You will need:

  * An existing cluster with Kf installed.
  * Access to a machine with `gcloud`, `kf`, and `kubectl` installed.



## Validate the existing Kf installation

  1. Get authentication credentials to interact with the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
           --zone CLUSTER_ZONE \
           --project CLUSTER_PROJECT_ID

  2. Run `kf debug` and validate the Kf CLI and Kf server versions match.

     * The CLI version is listed under `Kf Client`.
     * The Kf server version is listed under `kf["app.kubernetes.io/version"]`.
    
    $ kf debug
    ...
    Version:
      **Kf Client:                        v2.0.0**
      Server version:                   v1.17.13-gke.1401
      **kf["app.kubernetes.io/version"]:  v2.0.0**
    ...
    

If the Kf client and Kf server values **do not** match, [download](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads) and install the version of the Kf CLI that matches the server version then repeat the check with the new CLI. The CLI version **must** match the server version before you continue.

  3. Run `kf doctor` to check the state of your cluster. Ensure all tests pass before you continue.
         
         $ kf doctor
         ...
         === RUN doctor/user
         === RUN doctor/user/ContainerRegistry
         --- PASS: doctor/user
            --- PASS: doctor/user/ContainerRegistry
         ...
         

If you see the message `Error: environment failed checks`, follow the guidance in the `doctor` output to resolve the issue and retry the command until it is successful.




## Upgrade

To upgrade Kf perform the following steps:

  * Prepare the local environment and the upgrade.
  * Upgrade Kf's dependencies.
  * Upgrade Kf and verify that the upgrade was a success.



### Prepare the upgrade

  1. Run `kf version` to get the current version of Kf.
         
         $ kf version
         kf version **v2.0.0** linux
         

  2. Find the next newest version of Kf from the [downloads page](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads).

**Warning:** Kf currently only supports upgrading one minor version at a time. For example v2.0.0 to v2.1.0.
     1. Download the Kf release YAML file and save it as `kf-release.yaml`.

     2. Download the version of Kf for your OS and name it `kf-next`.

     3. Run `chmod` to make `kf-next` executable:
            
            chmod +x kf-next

     4. Run `kf-next version` to ensure the downloaded version matches the version of Kf you want to install:
            
            $ kf-next version
            kf version v2.1.0 linux
            

  3. Make a backup of the `config-defaults` configmap by running:
         
         kubectl get configmap config-defaults -o yaml -n kf > config-defaults-backup.yaml

**Note:** This backup is for reference only and should not be directly applied.
  4. Run `kubectl diff -f kf-release.yaml` and inspect the changes the upgrade would make to your cluster.

**Note:** Pay close attention to the `config-defaults` configmap. Kf uses that configmap to store cluster wide customizations like domains, feature flags, and container registries.
  5. Edit `kf-release.yaml` and modify it to keep any changes you want to maintain.

For example, if you set the `config-defaults` configmap property `spaceDefaultToV3Stack` to false in `v2.0.0` of Kf, the `v2.1.0` release would have the default value of `true`.

  6. Run `kubectl diff -f kf-release.yaml` again to ensure any changes you made produce the expected output.




### Upgrade Kf dependencies

  1. Open the [downloads page](https://docs.cloud.google.com/migrate/kf/docs/2.3/downloads) and find the dependency matrix for the version of Kf you're upgrading to.

  2. Upgrade Tekton:

     1. Open the [Tekton Release page](https://github.com/tektoncd/pipeline/releases).

     2. Find the version of Tekton listed in the Kf dependency matrix.

     3. Run the command under the "Installation one-liner" heading to upgrade Tekton.

  3. Upgrade Cloud Service Mesh:

     1. Open the [Cloud Service Mesh upgrade guide](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-upgrading).

     2. In the version dropdown, pick the version of Cloud Service Mesh listed in the Kf dependency matrix.

     3. Follow the guide to upgrade ASM.




### Upgrade and verify Kf

  1. Install the upgraded Kf components using the modified release configuration:
         
         kubectl apply -f kf-release.yaml

  2. Run `doctor` to ensure the newly installed version is healthy:
         
         kf-next doctor --retries=12 --delay=5s

The command will run cluster checks several times. It's normal for a few of the attempts to fail while the new controllers are starting.

If the command fails with the message `Error: environment failed checks`, follow the guidance in the `doctor` output to resolve the issue and retry the command until it is successful.

  3. Replace the existing `kf` CLI on your system with the `kf-next` CLI.
         
         chmod +x kf-next
         mv kf-next $(which kf)

**Note:** You might have to run this command as a super user using `sudo` if Kf is installed globally.
  4. Compare the `config-defaults-backup.yaml` file with `kubectl diff -f config-defaults-backup.yaml` to ensure your cluster is still configured correctly.

For example, if you kept all changes from your old Kf version, and approved use of a new buildpack bundled with the next version of Kf:
         
         $ kubectl diff -f config-defaults-backup.yaml
         diff -u -N /tmp/LIVE/v1.ConfigMap.kf.config-defaults /tmp/MERGED/v1.ConfigMap.kf.config-defaults
         --- /tmp/LIVE/v1.ConfigMap.kf.config-defaults
         +++ /tmp/MERGED/v1.ConfigMap.kf.config-defaults
         @@ -131,6 +131,8 @@
              enable_route_services: false
            spaceBuildpacksV2: |
         -    - name: new_buildpack
         -      url: https://github.com/cloudfoundry/new-buildpack
              - name: staticfile_buildpack
                url: https://github.com/cloudfoundry/staticfile-buildpack
              - name: java_buildpack
         exit status 1
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
