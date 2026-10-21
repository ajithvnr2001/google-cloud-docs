---
url: https://docs.cloud.google.com/migrate/kf/docs/2.4/upgrade/
title: Upgrade Kf \u00a0|\u00a0 Kf 2.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:16:23.276476+00:00
---

# Upgrade Kf  |  Kf 2.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.4/upgrade/

Version 2.4

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
  * [ 2.4 ](https://docs.cloud.google.com/migrate/kf/docs/2.4)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.4/getting-started)



Send feedback 

#  Upgrade Kf Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to upgrade an existing Kf installation and its dependencies. 

As part of the upgrade procedure, you ensure that your Kf installation uses the latest version of the Kf operator:

  * Confirm your current Kf version can upgrade to Kf v2.4.1.
  * Upgrade to Kf v2.4.1.
  * Upgrade dependencies (if needed).



## Before you begin

**Warning:** Kf currently only supports upgrading one minor version at a time. The steps on this page are for upgrading Kf v2.3.x or 2.4.x to Kf v2.4.1. 

You will need:

  * An existing cluster with Kf installed.
  * Access to a machine with `gcloud`, `kf`, and `kubectl` installed.



## Preparing for the upgrade

### Connect to your target cluster
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
     --zone CLUSTER_ZONE \
     --project CLUSTER_PROJECT_ID

### Confirm your current Kf CLI and server versions match

Run `kf debug` and validate the Kf CLI and Kf server versions match.

  * The CLI version is listed under `Kf Client`.
  * The Kf server version is listed under `kf["app.kubernetes.io/version"]`.


    
    
    $ kf debug
    ...
    Version:
      **Kf Client:                        v2.3.2**
      Server version:                   v1.20.6-gke.1000
      **kf["app.kubernetes.io/version"]:  v2.3.2**
    ...
    

If the Kf client and Kf server values **do not** match, but the server version is v2.3.x, install the Kf v2.4.1 CLI before you continue.

If the Kf server value is older than v2.3.x, you must first incrementally upgrade to Kf v2.3.x to continue.

### Confirm Kf is healthy before upgrading

Run `kf doctor` to check the state of your cluster. Ensure all tests pass before you continue.
    
    
    $ kf doctor
    ...
    === RUN doctor/user
    === RUN doctor/user/ContainerRegistry
    --- PASS: doctor/user
       --- PASS: doctor/user/ContainerRegistry
    ...
    

If you see any `FAIL` or `Error: environment failed checks` messages, follow the guidance in the `kf doctor` output, or view the [troubleshooting guide](https://docs.cloud.google.com/migrate/kf/docs/2.4/support/troubleshooting) to resolve the issue and retry the command until it is successful.

### Optionally backup Kf configmaps if you have made customizations

**Note:** These backups will be used later in the verification steps to confirm your customizations were preserved.

  1. Make a backup of the `config-defaults` configmap by running:
         
         kubectl get configmap config-defaults -o yaml -n kf > config-defaults-backup.yaml

  2. Make a backup of the `config-secrets` configmap by running:
         
         kubectl get configmap config-secrets -o yaml -n kf > config-secrets-backup.yaml

**Note:** This backup is for reference only and should not be directly applied.



## Upgrade the Kf operator

The Kf operator was first released as part of versions 2.4.0:

  * **If you have already installed the Kf operator as part of installing 2.4.0** , then you only have to upgrade it as part of upgrading to 2.4.1.

See Upgrade the Kf operator.

  * **If you are upgrading from 2.3.2** , you must install the 2.4.1 version of the Kf operator to upgrade to operator managed Kf.

See Install the Kf operator.




### Upgrade the current Kf operator

The Kf operator performs upgrades for you.

  1. Apply the operator yaml:

**Note:** This operation starts immediately, and is not reversible.
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.4.1/operator.yaml"




### Install the Kf operator for the first time

Perform these steps to upgrade to operator managed Kf.

  1. Apply the operator yaml:

**Note:** This operation starts immediately, and is not reversible.
         
         kubectl apply -f "https://storage.googleapis.com/kf-releases/v2.4.1/operator.yaml"

  2. Choose between using defaults or retaining customizations:

**Note:** Choose one or the other. Do not complete both.
     1. Prepare `kfsystem.yaml` for the upgrade **using defaults** :

**Note:** Follow these steps if you have **not** made any customizations to `config-defaults` or `config-secrets`.

[Download](https://docs.cloud.google.com/migrate/kf/docs/2.4/downloads) the `kfsystem.yaml` file, fill in the variables below, then run the commands in the same directory as the file to automatically prepare `kfsystem.yaml` for the upgrade.
            
            export CLUSTER_PROJECT_ID=YOUR_PROJECT_ID
            export CLUSTER_NAME=YOUR_CLUSTER_NAME
            export CONTAINER_REGISTRY=YOUR_CLUSTER_COMPUTE_REGION-docker.pkg.dev/${CLUSTER_PROJECT_ID}/${CLUSTER_NAME}
            
            kubectl apply -f kfsystem.yaml
            
            kubectl patch \
            kfsystem kfsystem \
            --type='json' \
            -p="[{'op': 'replace', 'path': '/spec/kf', 'value': {'enabled': true, 'config': {'spaceContainerRegistry': '${CONTAINER_REGISTRY}', 'secrets':{'workloadidentity':{'googleserviceaccount':'${CLUSTER_NAME}-sa', 'googleprojectid':'${CLUSTER_PROJECT_ID}'}}}}}]"
            

     2. Prepare `kfsystem.yaml` for the upgrade **while preserving customizations** :

**Note:** Follow these steps if you have made customizations to `config-defaults` or `config-secrets`, you'll need to manually copy them to the corresponding fields in `kfsystem.yaml`.
        1. [Download](https://docs.cloud.google.com/migrate/kf/docs/2.4/downloads) the `kfsystem.yaml` file.

        2. Make a backup of the `config-defaults` configmap by running:
               
               kubectl get configmap config-defaults -o yaml -n kf > config-defaults-backup.yaml

        3. Make a backup of the `config-secrets` configmap by running:
               
               kubectl get configmap config-secrets -o yaml -n kf > config-secrets-backup.yaml

        4. Inspect the current config-defaults and config-secrets configmaps, and find the corresponding settings in `kfsystem.yaml`.

        5. Copy over the existing settings from `config-secrets` and `config-defaults`. All the settings in `config-secrets` and `config-defaults` can be found in `kfsystem.yaml`. The `googleProjectId` field is now required.

        6. The `wi.googleServiceAccount` field is the full Service Account in `config-secrets`, but for `kfsystem` the suffix must be removed. For example, `${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com` would become `${CLUSTER_NAME}-sa` in `kfsystem.yaml`.

        7. After the settings are copied over, change the field `enabled` in `kfsystem` to `true`.

        8. Save your changes to `kfsystem.yaml`.

        9. Configure the operator for Kf:
               
               kubectl apply -f kfsystem.yaml




## Upgrade Kf dependencies

  1. Upgrade Tekton:
         
         kubectl apply -f "https://storage.googleapis.com/tekton-releases/pipeline/previous/v0.23.0/release.yaml"

  2. Upgrade Cloud Service Mesh:

**Note:** If you are running a version of Cloud Service Mesh older than 1.9, complete this step.
     1. Follow the steps in the [Cloud Service Mesh 1.9 upgrade guide](https://docs.cloud.google.com/service-mesh/v1.9/docs/scripted-install/gke-upgrade).
  3. Upgrade Config Connector.

**Note:** Config Connector is required starting with Kf v2.4.0.**Warning:** Do not use the GKE add-on method to install Config Connector as it is not supported by Kf. Please use these custom installation steps.
     1. [Download](https://storage.googleapis.com/configconnector-operator/1.46.0/release-bundle.tar.gz) the required Config Connector Operator tar file.

**Note:** Keep a copy of the installation bundle as you need this bundle to uninstall Config Connector.
     2. Extract the tar file.
            
            tar zxvf release-bundle.tar.gz

     3. Install the Config Connector operator on your cluster.
            
            kubectl apply -f operator-system/configconnector-operator.yaml

     4. Configure the Config Connector operator if installing Config Connector for the first time.

        1. Copy the following YAML into a file named `configconnector.yaml`:

**Warning:** Replace the `KF_SERVICE_ACCOUNT_NAME` variable in the YAML below with the full service account resolved from `${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com`
               
               # configconnector.yaml
               apiVersion: core.cnrm.cloud.google.com/v1beta1
               kind: ConfigConnector
               metadata:
               # the name is restricted to ensure that there is only one
               # ConfigConnector resource installed in your cluster
               name: configconnector.core.cnrm.cloud.google.com
               spec:
               mode: cluster
               googleServiceAccount: "KF_SERVICE_ACCOUNT_NAME" # Replace with the full service account resolved from ${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com

        2. Apply the configuration to your cluster.
               
               kubectl apply -f configconnector.yaml

     5. Verify Config Connector is fully installed before continuing.

        * Config Connector runs all of its components in a namespace named `cnrm-system`. Verify the Pods are ready by running the following command:
              
              kubectl wait -n cnrm-system --for=condition=Ready pod --all

        * If Config Connector is installed correctly, the output is similar to the following:
              
              pod/cnrm-controller-manager-0 condition met

**Note:** The controller Pod can take several minutes to start.
     6. Setup Workload Identity if installing Config Connector for the first time.
            
            kubectl annotate serviceaccount \
            --namespace cnrm-system \
            --overwrite \
            cnrm-controller-manager \
            iam.gke.io/gcp-service-account=${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com




## Upgrade to the Kf v2.4.1 CLI

  1. Install the CLI:

### Linux

This command installs the Kf CLI for all users on the system. Follow the instructions in the Cloud Shell tab to install it just for yourself.
         
         gcloud storage cp gs://kf-releases/v2.4.1/kf-linux /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Mac

This command installs `kf` for all users on the system.
         
         gcloud storage cp gs://kf-releases/v2.4.1/kf-darwin /tmp/kf
         chmod a+x /tmp/kf
         sudo mv /tmp/kf /usr/local/bin/kf

### Cloud Shell

This command installs `kf` on your Cloud Shell instance if you use `bash`, the instructions may need to be modified for other shells.
         
         mkdir -p ~/bin
         gcloud storage cp gs://kf-releases/v2.4.1/kf-linux ~/bin/kf
         chmod a+x ~/bin/kf
         echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc
         source ~/.bashrc

### Windows

This downloads `kf` to current directory. Add it to the path if you want to call if from anywhere other than the current directory.
         
         gcloud storage cp gs://kf-releases/v2.4.1/kf-windows.exe kf.exe

  2. Validate the Kf CLI and Kf server versions match:

     * The CLI version is listed under `Kf Client`.
     * The Kf server version is listed under `kf["app.kubernetes.io/version"]`.
    
    $ kf debug
    ...
    Version:
      **Kf Client:                        v2.4.1**
      Server version:                   v1.20.6-gke.1000
      **kf["app.kubernetes.io/version"]:  v2.4.1**
    ...
    




## Verify Kf upgraded successfully

  1. If installing the Kf operator for the first time, confirm the operator installed:
         
         kubectl get deployment -n appdevexperience appdevexperience-operator

If you do not see the operator like in the example output below, review the Install the Kf operator for the first time steps.
         
         NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
         appdevexperience-operator   1/1     1            1           1h
         

  2. Run `doctor` to ensure the newly installed version is healthy:
         
         kf doctor --retries=20

The command will run cluster checks several times. It's normal for a few of the attempts to fail while the new controllers are starting.

If the command fails with the message `Error: environment failed checks`, follow the guidance in the `doctor` output to resolve the issue and retry the command until it is successful.

  3. If you have made customizations to `config-defaults` or `config-secrets`, verify they carried over:

Compare the `config-defaults-backup.yaml` file with `kubectl diff -f config-defaults-backup.yaml` to ensure your cluster is still configured correctly.

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
         




If the verification steps pass, your cluster has successfully been upgraded! If you have any issues, please review the [support](https://docs.cloud.google.com/migrate/kf/docs/2.4/support) page for guidance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
