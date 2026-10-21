---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-etcd-kcp-encryption-keys/
title: Rotate etcd and control plane boot disk encryption keys \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:13.267796+00:00
---

# Rotate etcd and control plane boot disk encryption keys  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-etcd-kcp-encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Rotate etcd and control plane boot disk encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This document uses a [general availability](https://cloud.google.com/products#product-launch-stages) feature named _GKE control plane authority_ that's only available for eligible Google Cloud customers. To request access to this feature, contact your Google Cloud account team.

This page shows you how to rotate the etcd and control plane boot disk encryption keys that you configured for GKE control plane authority. This document is intended for cluster administrators and Security engineers.

Before you read this document, familiarize yourself with the following GKE control plane authority concepts:

  * [Key and credential management](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority#key-credential-management).
  * [Rotation of customer-managed credentials](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority#rotation-customer-managed-credentials).



## Plan key rotations

This document shows you how to rotate the following credential components in your control plane:

  * The encryption key for etcd and the control plane boot disks.
  * The encryption key for the etcd internal backup that Google Cloud uses for disaster recovery.

**Best practice** : 

Validate your key and credential rotation procedures _before_ an actual incident occurs.

You can also rotate the customer-managed certificate authorities (CAs) and service account signing keys that you configure with GKE control plane authority. For more information, see [Rotate customer-managed control plane CAs and signing keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-control-plane-cas-keys).

Keys in Cloud Key Management Service (Cloud KMS) don't expire. If your organization has a security requirement for key rotation, manually rotate the keys. To minimize disruptions to running workloads, don't configure automatic key rotation for these keys.

When you rotate the encryption keys for your control plane boot disks and etcd, GKE creates a new disk that's encrypted using the new key. For regional clusters, this operation has no downtime because of the replicated control plane. For zonal clusters, the control plane becomes unavailable until the new disk is available.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Have an existing cluster that uses [control plane boot disk and etcd encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks) and runs GKE version 1.35.2-gke.1842000 or later.

  * Identify the project IDs of the following Google Cloud projects:

    * **Key project** : the project that contains your Cloud KMS resources.
    * **Cluster project** : the project that contains your GKE cluster.
  * To do the validation tasks in this document, verify that the `DATA_READ` Data Access audit log is enabled for the Cloud Key Management Service (KMS) API. For more information, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).




### Required roles and permissions

To get the permissions that you need to rotate your customer-managed CAs and keys, ask your administrator to grant you the following IAM roles: 

  * Manage keys or key versions: [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) on your key project 
  * Configure clusters to use new keys: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) on your cluster project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Limitations

You can update your clusters to new _versions_ of existing keys, but you can't update your clusters to use entirely new keys for these encryption operations.

## Grant IAM roles to the GKE service agent

To rotate your encryption keys for boot disks and etcd, grant the [Kubernetes Engine KMS Crypto Key User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.cloudKmsKeyUser) (`roles/container.cloudKmsKeyUser`) role on the encryption keys in your key project to the GKE service agent in your cluster project:
    
    
    gcloud kms keys add-iam-policy-binding KCP_DISK_KEY_NAME \
        --keyring=KEYRING_NAME \
        --location=LOCATION \
        --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
        --role=roles/container.cloudKmsKeyUser \
        --project=KEY_PROJECT_ID
    

Replace the following:

  * `KCP_DISK_KEY_NAME`: the name of the encryption key for your control plane boot disks and etcd disks.
  * `KEYRING_NAME`: the name of the key ring that holds the key.
  * `LOCATION`: the Google Cloud location of the key ring. This must be the same as your cluster location. For a list of regions, filter for "Region" in the [Cloud KMS locations table](https://docs.cloud.google.com/kms/docs/locations).
  * `CLUSTER_PROJECT_NUMBER`: the numerical project number of the cluster project.
  * `KEY_PROJECT_ID`: the project ID of your _key project_.



## Rotate the key for etcd and control plane boot disks

  1. Create a new primary key version for the boot disk and etcd encryption key:
         
         gcloud kms keys versions create \
             --key=KCP_DISK_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=LOCATION \
             --project=KEY_PROJECT_ID \
             --primary
         

It might take up to 10 minutes for the changes to propagate in the project.

  2. Find the current patch version of the cluster control plane:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --format='value(currentMasterVersion)'
         

Replace the following:

     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `LOCATION`: the location of the GKE cluster control plane, such as `us-central1`.
  3. Upgrade the cluster control plane to the same version that it already uses.

**Caution:** In zonal clusters, the control plane becomes unavailable until the upgrade operation completes. In Autopilot clusters and regional Standard clusters, the control plane remains available.
         
         gcloud container clusters upgrade CLUSTER_NAME \
             --master \
             --location=LOCATION \
             --cluster-version=CONTROL_PLANE_VERSION \
             --project=CLUSTER_PROJECT_ID
         

Replace the following:

     * `CONTROL_PLANE_VERSION`: the version of the cluster control plane from the output of the previous step.
     * `CLUSTER_PROJECT_ID`: the project ID of your _cluster project_.



After the control plane upgrade operation completes, the cluster uses the new key version to encrypt your control plane boot disks and any etcd disks.

## Rotate the etcd internal backup encryption key

This section shows you how to rotate the encryption key for the etcd internal backup, which Google Cloud uses for disaster recovery purposes. You can configure automatic rotation for this key, but we recommend that you perform manual rotation instead. After you rotate the key, the cluster uses the new key version to encrypt new etcd internal backups.

etcd internal backups use the primary key version and occur at the following intervals:

  * Every 30 minutes for zonal clusters.
  * Every 10 minutes for Autopilot clusters and regional Standard clusters.



After you rotate the key, don't immediately disable or destroy the previous key version. Wait until enough time has passed for GKE to create new etcd internal backups that use the new key version.

  * Create a new primary key version for the etcd internal backup encryption key:
        
        gcloud kms keys versions create \
            --key=ETCD_BACKUP_KEY_NAME \
            --keyring=KEYRING_NAME \
            --location=LOCATION \
            --project=KEY_PROJECT_ID \
            --primary
        

Replace the following:

    * `ETCD_BACKUP_KEY_NAME`: the name of the etcd internal backup encryption key.
    * `KEYRING_NAME`: the name of the key ring that holds the key.
    * `LOCATION`: the Google Cloud location of the key ring. This must be the same as your cluster location. For a list of regions, filter for "Region" in the [Cloud KMS locations table](https://docs.cloud.google.com/kms/docs/locations).
    * `KEY_PROJECT_ID`: the project ID of your _key project_.



## What's next

  * [Rotate customer-managed control plane CAs and keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-control-plane-cas-keys)
  * [Verify identity issuance and usage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
