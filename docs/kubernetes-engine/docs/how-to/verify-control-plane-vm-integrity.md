---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-control-plane-vm-integrity/
title: Verify GKE control plane VM integrity \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:13.361987+00:00
---

# Verify GKE control plane VM integrity  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-control-plane-vm-integrity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Verify GKE control plane VM integrity Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can verify the integrity of the Compute Engine virtual machine (VM) image that Google Kubernetes Engine (GKE) uses for control plane VMs. This page provides instructions for a security team that monitors the control plane logs to verify the following:

  * The control plane VM booted with authentic firmware and other boot software that was cryptographically verified by secure boot and integrity monitoring.
  * The control plane VM booted from an authentic GKE OS image.



You can also perform this verification for the OS images and boot integrity of your nodes.

This page describes one part of a set of optional control plane features in GKE that lets you perform tasks like verifying your control plane security posture or configuring encryption and credential signing in the control plane using keys that you manage. For details, see [About GKE control plane authority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority).

By default, Google Cloud applies various security measures to the managed control plane. This page describes _optional_ capabilities that give you more visibility or control over the GKE control plane.

## About VM integrity verification

By default, all GKE control plane instances are [Shielded VMs](https://docs.cloud.google.com/security/products/shielded-vm), which are hardened VMs that use security capabilities like secure and measured boot, a virtual trusted platform module (vTPM), and UEFI firmware. All GKE nodes also enable [_integrity monitoring_](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring), which validates the boot sequence of each Shielded VM against a baseline "good" boot sequence. This validation returns pass or fail results for each boot sequence phase and adds those results to Cloud Logging. Integrity monitoring is enabled by default in all GKE clusters and validates the following phases:

  * **Early boot sequence** : from when the UEFI firmware starts until the bootloader takes control. Added to the VM logs as `earlyBootReportEvent`.
  * **Late boot sequence** : from when the bootloader takes control until the operating system kernel takes control. Added to the VM logs as `lateBootReportEvent`.



GKE also adds control plane VM creation logs to Logging. These logs contain metadata that identifies the machine and includes details about the VM image and the boot sequence. Google Cloud publishes a [_verification summary attestation (VSA)_](https://slsa.dev/spec/v1.0/verification_summary) for each GKE control plane VM image in the [gke-vsa repository on GitHub](http://github.com/GoogleCloudPlatform/gke-vsa). The VSA uses the [in-toto framework](https://in-toto.io/) for attestations. You can validate the control plane VM logs for your clusters against the corresponding VSAs to verify that your control plane nodes booted as expected.

Performing these validations can help you to achieve the following goals:

  * Ensure that the software on the control plane is protected by secure boot and integrity monitoring, matches the intended source code, and is exactly the same as the image that other Google Cloud customers use.
  * Improve your confidence in how GKE secures the control plane.



## Pricing

This feature is offered at no extra cost in GKE.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  * Ensure that you already have a GKE Autopilot mode or Standard mode cluster running version 1.29 or later.



### Required roles

To get the permissions that you need to verify control plane VM integrity, ask your administrator to grant you the following IAM roles on your project: 

  * Create and interact with clusters: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) 
  * Access and process logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Check for failed boot sequence phases

Integrity monitoring adds a log to Logging if a control plane VM fails or successfully completes a phase of the boot sequence. To view failed boot events, run the following commands:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, specify the following query:
         
         jsonPayload.@type="type.googleapis.com/cloud_integrity.IntegrityEvent"
         jsonPayload.earlyBootReportEvent.policyEvaluationPassed="false" OR jsonPayload.lateBootReportEvent.policyEvaluationPassed="false"
         jsonPayload.metadata.isKubernetesControlPlaneVM="true"
         

You can also check for successful boot events by replacing `false` with `true` in this query.

  3. Click **Run query**. If you don't see results, your control plane VMs passed all integrity monitoring checks. If you see an output, proceed to the next step to identify the corresponding cluster.

  4. In the failed boot integrity log, copy the value in the `resource.labels.instance_id` field.

  5. In the **Query** field, specify the following query:
         
         protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
         protoPayload.metadata.isKubernetesControlPlaneVM="true"
         resource.labels.instance_id="INSTANCE_ID"
         protoPayload.methodName="v1.compute.instances.insert"
         

Replace `INSTANCE_ID` with the value of the `instance_id` field from the previous step.

  6. Click **Run query**. The value in the `protoPayload.metadata.parentResource.parentResourceId` field is the GKE cluster ID.

  7. Find the name of the GKE cluster:
         
         gcloud asset query \
             --organization=ORGANIZATION_ID \
             --statement="SELECT name FROM container_googleapis_com_Cluster WHERE resource.data.id='CLUSTER_ID';"
         

Replace the following:

     * `ORGANIZATION_ID`: the numerical ID of your Google Cloud organization.
     * `CLUSTER_ID`: the value of the `protoPayload.metadata.parentResource.parentResourceId` field from the previous step.

The output is similar to the following:
    
    # lines omitted for clarity
    //container.googleapis.com/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME
    

This output has the following fields:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `LOCATION`: the location of the cluster.
     * `CLUSTER_NAME`: the name of the cluster.



## Find and inspect the control plane VM logs

The Compute Engine VM creation logs that correspond to GKE clusters are stored in the [`_Default` log bucket](https://docs.cloud.google.com/logging/docs/routing/overview#default-bucket). To find the creation logs for your cluster control plane VMs and retrieve this metadata, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, specify the following query:
         
         resource.type="gce_instance"
         protoPayload.methodName="v1.compute.instances.insert"
         protoPayload.metadata.isKubernetesControlPlaneVM="true"
         

  3. Click **Run query**. If you don't see results, check that you meet all of the requirements in the Before you begin section.

  4. In the query results, check the `metadata` field. The output is similar to the following:
         
         # fields omitted for clarity
         "metadata": {
           "usedResources": {
             "attachedDisks": [
               {
                 "sourceImageId": "9046093115864736653",
                 "sourceImage": "https://www.googleapis.com/compute/v1/projects/1234567890/global/images/gke-1302-gke1627000-cos-113-18244-85-49-c-pre",
                 "isBootDisk": true
               }
         # fields omitted for clarity
         

The `metadata` field includes the following information:

     * `usedResources`: the list of resources used to create the VM.
     * `attachedDisks`: the boot disk for the VM.
     * `sourceImageId`: the unique ID of the VM image.
     * `sourceImage`: the URL of the source VM image. The syntax of the value in this field is `https://www.googleapis.com/compute/v1/projects/PROJECT_NUMBER/global/images/IMAGE_NAME`, where `PROJECT_NUMBER` is the number of the Google Cloud-owned project that hosts the control plane VMs and `IMAGE_NAME` is the name of the image that was used to boot the VM.
     * `isBootDisk`: a boolean identifier for whether this disk was used as the boot disk for the VM.



## Find and verify the VSA for control plane VM images

**Note** : This tutorial provides instructions for working with this app: slsa-verifier. The instructions might not represent newer versions of the app. For more information, see the documentation: [slsa-verifier](https://github.com/slsa-framework/slsa-verifier). 

In this section, you find the VSA that corresponds to your control plane VM image in the gke-vsa repository on GitHub. You then use a tool named `slsa-verifier` provided by the [Supply chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/) to verify the VSA. You need the following data from the control plane VM creation log:

  * The VM image ID
  * The project number of the Google Cloud-owned project that hosts the VMs
  * The OS image name that was used to boot the VM



The file that corresponds to your control plane VM has the following filename format:
    
    
    IMAGE_NAME:IMAGE_ID.intoto.jsonl
    

Replace the following:

  * `IMAGE_NAME`: the VM image name, which is the string after `/images/` in the `attachedDisks.sourceImage` field in the VM audit log from the previous section. For example, `gke-1302-gke1627000-cos-113-18244-85-49-c-pre`.
  * `IMAGE_ID`: the VM image ID, which is the value of the `attachedDisks.sourceImageId` field in the VM audit log from the previous section. For example, `9046093115864736653`.



To find and verify the VSA when you know the filename of your VSA file, perform the following steps:

  1. Open the [`gke-vsa` GitHub repository](http://github.com/GoogleCloudPlatform/gke-vsa).
  2. In the "gke-master-images" directory, find the file that corresponds to your VM image. For example, `https://github.com/GoogleCloudPlatform/gke-vsa/blob/main/gke-master-images:78064567238/IMAGE_NAME:IMAGE_ID.intoto.jsonl`
  3. Download the VSA file.
  4. [Install the `slsa-verifier` tool](https://github.com/slsa-framework/slsa-verifier#installation).
  5. Save the public key for verifying the VSA to a file named `vsa_signing_public_key`:
         
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEeGa6ZCZn0q6WpaUwJrSk+PPYEsca
         3Xkk3UrxvbQtoZzTmq0zIYq+4QQl0YBedSyy+XcwAMaUWTouTrB05WhYtg==
         -----END PUBLIC KEY-----
         

  6. Verify the VSA:
         
         slsa-verifier verify-vsa \
             --attestation-path=PATH_TO_VSA_FILE \
             --resource-uri=gce_image://gke-master-images:IMAGE_NAME \
             --subject-digest=gce_image_id:IMAGE_ID\
             --verifier-id=https://bcid.corp.google.com/verifier/bcid_package_enforcer/v0.1 \
             --verified-level=BCID_L1 \
             --verified-level=SLSA_BUILD_LEVEL_2 \
             --public-key-path=PATH_TO_PUBLIC_KEY_FILE \
             --public-key-id=keystore://76574:prod:vsa_signing_public_key
         

Replace the following:

     * `PATH_TO_VSA_FILE`: the path to the VSA file that you downloaded.
     * `IMAGE_NAME`: the name of the VM image, like `gke-1302-gke1627000-cos-113-18244-85-49-c-pre`.
     * `IMAGE_ID`: the VM image ID, like `9046093115864736653`.

If the VSA passes the verification checks, the output is the following:
    
    Verifying VSA: PASSED
    PASSED: SLSA verification passed
    




## What's next

  * [Learn about what else you can view in the control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
