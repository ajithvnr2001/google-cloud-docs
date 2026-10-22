---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/object-storage-key-rotation/
title: Rotate object storage credentials \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:40.719133+00:00
---

# Rotate object storage credentials  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/object-storage-key-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Rotate object storage credentials Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance object storage is provided by OTS (ONTAP Select). OTS has its own object storage user management system. Each `OTS` object storage user credentials is stored as a secret in clusters.

This document describes the steps to rotate `OTS` object storage user credentials. Rotate object storage user credentials in the following situations:

  * regularly scheduled key rotation to rotate all user keys.
  * mitigating key exposure. You should rotate the exposed user key as soon as possible.



## Before you begin

Complete the following steps:

  1. Verify that you meet the [laptop prerequisites](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/laptop).
  2. Ensure that you can login to the OTS cluster and run `vserver object-store-server` CLI commands.
  3. Ensure that you can log as administrator into the infra cluster and management cluster using `kubectl`.



## Translate UID

Each object storage user has an access key and secret key that are stored as a Kubernetes secret and used by Kubernetes workloads to access the backend object storage. Rotating the user keys includes updating all the secrets.

You can get a list of object storage users by signing into one of the three nodes using:
    
    
    vserver object-store-server user show
    

The output is a list of UIDs and should be similar to:
    
    
    [
        "root",
        "k8ssa_gpc-system_inventory-export-images",
        "k8ssa_gpc-system_inventory-export-hardware",
        "k8su_test-user@example.com"
    ]
    

There are three types of users:

Object storage users **UID** | **User type** | **Secret name** | **Secret namespace**  
---|---|---|---  
root | System administrator | objectstorage-tenant-bucket-controller-standard-system-s3-sa | gpc-system  
objectstorage-tenant-bucket-controller-standard-user-s3-sa  
objectstorage-tenant-bucket-controller-nearline-user-s3-sa  
k8ssa_<namespace>_<sa> | Kubernetes service account | object-storage-key-std-sa-<encoded-sa> | <namespace>  
k8su_<username> | Kubernetes user | object-storage-key-std-user-<encoded-username> | object-storage-access-keys  
  
The `root` user has three identical secrets, mirroring the structure of the Data Center, which encompasses multiple storage classes and tenant categories. In contrast, Appliance only has a single tier of object storage. _All three secrets_ associated with the root user must be rotated simultaneously.

User identification (UID), excluding the `root` user, should adhere to either the `k8ssa_<namespace>_<sa>` or `k8su_<username>` format. Obtain either the `<encoded-sa>` or `<encoded-username>`:
    
    
    echo -n 'UID_SUFFIX' | shasum -a 256 | cut -d " " -f 1 | xxd -r -p | base32 | awk '{print tolower($0)}' | sed 's/=*$//g'
    

Replace `UID_SUFFIX` with `<sa>` in the UID, and you will get `<encoded-sa>`.

Replace `UID_SUFFIX` with `<username>` in the UID, and you will get `<encoded-username>`.

## Rotate user key

  1. Login to the OTS cluster.

  2. Get a list of object storage user UIDs.
         
         vserver object-store-server user show
         

The result is a list of UIDs. Examples can be found in Translate UID. Repeat the following steps for each UID in the list.

  3. Get the old access key and secret key for the target user.
         
         set -privilege advanced
         vserver object-store-server user show -user UID
         

Replace `UID` with the target user UID.

  4. Generate a new access key and secret key for the target user in object storage. The old and new keys co-exist after this step, and both can be use for access.
         
         vserver object-store-server user regenerate-keys -vserver root-admin -user UID
         

  5. Update the Kubernetes secret with the new access key and secret key. You only need to update the secret in the root infra cluster or management cluster, and the secret is propagated to other clusters if needed.
         
         kubectl --kubeconfig KUBECONFIG patch secret -n SECRET_NAMESPACE SECRET_NAME --type='json' -p='[{"op": "replace", "path": "/data/access-key-id", "value": "'"$(echo -n "ACCESS_KEY" | base64)"'"}, {"op": "replace", "path": "/data/secret-access-key", "value": "'"$(echo -n "ACCESS_KEY" | base64)"'"}]'
         

Replace the following:

     * `KUBECONFIG`: the path to the kubeconfig. The API server must be the control plane API server for the `root` user; if not, it must be the management API server.
     * `SECRET_NAME`: the secret name for the user, which can be derived from the Translate UID section. If the user has multiple Kubernetes secrets (i.e., `root` user), replace with each secret name and run the command.
     * `SECRET_NAMESPACE`: the secret namespace for user, which can be derived from the Translate UID section.
     * `ACCESS_KEY`: the new access key generated in the previous step.
     * `SECRET_KEY`: the new secret key generated in the previous step.
  6. The workload that consumes the secret must be implemented to refresh automatically. If not, you must restart the workload to reflect the change in the secret.

For example, for `root` user, you need to restart the following workloads in the infra cluster:
         
         kubectl --kubeconfig KUBECONFIG rollout restart deployment obj-bucket-cm-backend-controller -n obj-system
         




## Validation

Follow the Object Storage [create bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-storage-buckets) and [upload and download object](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/upload-download-storage-objects) to create a new bucket and grant access using RBAC. The object storage key rotation is complete if the bucket is successfully created and the subject has the necessary permissions to access it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
