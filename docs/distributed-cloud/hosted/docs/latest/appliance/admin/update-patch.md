---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/update-patch/
title: Update and patch device \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:58.396411+00:00
---

# Update and patch device  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/update-patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Update and patch device Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to update and patch your Google Distributed Cloud (GDC) air-gapped appliance device.

## Prepare for the upgrade

Make sure you meet the requirements listed in this section before the upgrade.

### Before you begin

Review the [Laptop prerequisites](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/install/device-prerequisites) to ensure that the laptop you use for the update and patch upgrades meets physical specifications and other requirements.

You must first complete the following actions regarding the `gdcloud` command-line interface (CLI) tools:

  1. [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) the `gdcloud` CLI tools.
  2. [Install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the `gdcloud` CLI tools.
  3. [Upgrade](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-upgrade) the `gdcloud` CLI tools as required.
  4. Ensure the [`docker-credential-gdcloud`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/push-container-image#before-you-begin) is present.
  5. Verify that the HPE Chassis Manager is running firmware version `2.10.12` or later. If updating from an earlier firmware version, see [Upgrade HPE Chassis Manager firmware](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/chassis-firmware-upgrade).



### Transfer the artifacts to the upgrade machine

You must have access to the Cloud Storage bucket.

Follow these steps to transfer the artifacts to the laptop you use for the update and patch upgrades:

  1. Download the package based on the selected patch version:
         
         VERSION=<x.x.x-gdch.yyy>
         RELEASE_SUFFIX="_te"
         DOWNLOADER=gdch-downloader-prod${RELEASE_SUFFIX}-$VERSION.sh
         gcloud storage cp "gs://$GCS_BUCKET/$VERSION/$DOWNLOADER" .
         gcloud storage cp "gs://$GCS_BUCKET/$VERSION/${DOWNLOADER}.sig" .
         
         PUBLIC_KEY=$(cat <<-PUBEND
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEn46iVSyFXsvuKLZ4dVOr2AqlXDnR
         5cKztkpraexHDxn/ozq03EvrdkRmZkSACFfcaEFyitpraidgAx8sPjvzXQ==
         -----END PUBLIC KEY-----
         PUBEND
         )
         echo "${PUBLIC_KEY}" > "key.pub"
         DOWNLOADER=gdch-downloader-${PRODUCT}-$VERSION.sh
         
         gcloud storage cp "gs://${GCS_BUCKET:-private-cloud-release}/$VERSION/$DOWNLOADER*" .
            openssl dgst -sha256 -verify "key.pub" -signature "${DOWNLOADER}.sig" ${DOWNLOADER} && chmod +x $DOWNLOADER && ./$DOWNLOADER --skip-unzip
         

This command fetches the update package and the downloader script to the current directory, for example, `/home/download`.

  2. Run `tree -L 3 /home/download`.

Example output:
         
         /home/download
         ├── gdch
         │   └── x.x.x-gdch.x
         │       ├── bootstrapper
         │       │   ├── bootstrapper.iso
         │       │   └── bootstrapper.iso.sig
         │       ├── gdch-prod_te-x.x.x-gdch.x-sbom.tar.gz
         │       ├── gdch-prod_te-x.x.x-gdch.x-sbom.tar.gz.sig
         │       ├── prod_te_gdch.tar.gz
         │       └── prod_te_gdch.tar.gz.sig
         ├── gdch-downloader-prod_te-x.x.x-gdch.x.sh
         ├── gdch-downloader-prod_te-x.x.x-gdch.x.sh.1.sig
         ├── gdch-downloader-prod_te-x.x.x-gdch.x.sh.sig
            └── key.pub
         

  3. Copy the update to the air-gapped environment, using your USB drive.

Copy both the downloader script and the `gdch` directory that you downloaded to your USB drive in step 1 to the upgrade machine in the air-gapped environment.

  4. In the upgrade machine, verify the contents and extract the files using the same information you used to download the package. For example, the following code copies the package to the `/root` directory.

Unpack the package:
         
         VERSION=x.x.x-gdch.x
         PRODUCT=prod_te
         DOWNLOADER=gdch-downloader-${PRODUCT}-$VERSION.sh
         openssl dgst -sha256 -verify "key.pub" -signature "${DOWNLOADER}.sig" ${DOWNLOADER} && chmod +x $DOWNLOADER && ./$DOWNLOADER --skip-download
         

The package is unpacked at the `/root/gdch/full-release-x.x.x-gdch.x` path.

  5. Confirm that the version matches the one that you set in VERSION:
         
         /root/gdch/full-release-x.x.x-gdch.x/gdcloud version
         

Sample output:
         
         gdcloud version: 1.14.4-gdch.0
         

**Note:** From here on, all CLI commands must use the gdcloud binary from the recently downloaded artifacts.



## Authenticate

To authenticate with your configured identity provider and request a kubeconfig file for your user identity and cluster, see [Authenticate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth).

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in) and generate the [kubeconfig files](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#generate-kubeconfig-file).

  2. Set the kubeconfig files as environment variables:
         
         export KUBECONFIG=ROOT_ADMIN_KUBECONFIG
           export MANAGEMENT_KUBECONFIG=MANAGEMENT_API_KUBECONFIG
         

  3. Request the following [roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings#gdcloud):

     * Upgrade Appliance Admin:
           
           kubectl --kubeconfig=$KUBECONFIG create clusterrolebinding upgrade-admin-te-initial-user --clusterrole=upgrade-admin-te --user=keycloak-oidc-initial-user@example.com
           kubectl --kubeconfig=$MANAGEMENT_KUBECONFIG create clusterrolebinding upgrade-admin-te-initial-user --clusterrole=upgrade-admin-te --user=keycloak-oidc-initial-user@example.com
           

     * System Artifact Management Admin:
           
           kubectl --kubeconfig=$KUBECONFIG create rolebinding system-artifact-management-admin-initial-user --role=system-artifact-management-admin --user=keycloak-oidc-initial-user@example.com -n gpc-system
            kubectl --kubeconfig=$MANAGEMENT_KUBECONFIG create rolebinding system-artifact-management-admin-initial-user --role=system-artifact-management-admin --user=keycloak-oidc-initial-user@example.com -n gpc-system
           

     * System Artifact Management Secrets Admin:
           
           kubectl --kubeconfig=$KUBECONFIG create rolebinding system-artifact-management-secrets-admin-initial-user --role=system-artifact-management-secrets-admin --user=keycloak-oidc-initial-user@example.com -n anthos-creds
           

     * DNS Suffix Viewer:
           
           kubectl --kubeconfig=$MANAGEMENT_KUBECONFIG create rolebinding dnssuffix-viewer-initial-user --role=dnssuffix-viewer --user=keycloak-oidc-initial-user@example.com -n gpc-system
           

     * System Artifact Registry Monitor:
           
           kubectl --kubeconfig=$KUBECONFIG create clusterrolebinding sar-monitor-initial-user --clusterrole=sar-monitor --user=keycloak-oidc-initial-user@example.com
            kubectl --kubeconfig=$MANAGEMENT_KUBECONFIG create clusterrolebinding sar-monitor-initial-user --clusterrole=sar-monitor --user=keycloak-oidc-initial-user@example.com
           

     * Upgrade Debugger:
           
           kubectl --kubeconfig=$KUBECONFIG create clusterrolebinding upgrade-debugger-initial-user --clusterrole=upgrade-debugger --user=keycloak-oidc-initial-user@example.com
           

     * System Artifact Registry Debugger:
           
           kubectl --kubeconfig=$KUBECONFIG create clusterrolebinding sar-debugger-initial-user --clusterrole=sar-debugger --user=keycloak-oidc-initial-user@example.com
           

  4. Configure Docker:
         
         gdcloud auth configure-docker --config-cert=true
         




## Start the upgrade

Go through the following steps to start the appliance upgrade:
    
    
    gdcloud appliance upgrade 
    

See [`gdcloud appliance upgrade`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-appliance-upgrade) for more information.

The command runs the following steps:

  1. Runs the preflight checks on the upgrade machine.
  2. Runs the preflight checks for OTS storage
  3. Pushes the artifacts to the artifact registry.
  4. Upgrades the appliance software and firmware, including: 
     1. GDC root-admin cluster.
     2. GDC services.
     3. The operating systems (OSes) of physical and virtual nodes.
     4. The switch.
     5. Storage



The command drives the updates in sequence, and waits for each step to complete. After completing the steps and if the upgrade is successful, you see a message similar to the following:
    
    
    The GDC appliance upgrade completed successfully
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
