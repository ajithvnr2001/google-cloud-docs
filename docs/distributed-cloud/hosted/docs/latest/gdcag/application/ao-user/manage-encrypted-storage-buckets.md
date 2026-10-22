---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/manage-encrypted-storage-buckets/
title: Manage Encryption Resources \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:12.418222+00:00
---

# Manage Encryption Resources  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/manage-encrypted-storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage Encryption Resources Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to manage encrypted Google Distributed Cloud (GDC) air-gapped storage buckets.

## Before you begin

Storage buckets are resources scoped to a specific [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management). The project acts as a container, grouping your buckets and enabling their management through the Management API server. Before you can perform the operations on this page, you must either create a new project or select an existing one where you have sufficient permissions.

### Required IAM roles

Contact your IAM Project Admin to request the following roles in your project namespace:

  * **Project Bucket Admin** (`project-bucket-admin`): create, update, and delete storage buckets.
  * **Project Bucket Object Viewer** (`project-bucket-object-viewer`): view and check details of storage buckets and objects.



For more information, see [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

### Prepare your environment

To run commands against the management API server or the global API server, do the following:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) the kubeconfig file for the zonal management API server if you don't have one.
  2. For dual-zone buckets, do the following: 
     * Verify with your Infrastructure Operator (IO) that the `BucketLocationConfig` custom resource has been created for your paired zones.
     * [Generate the kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig) for the global API server.



## Manage encryption resources

Buckets with `v2` encryption would have a secret `kekRef` and several AEADKeys created, in which `kekRef` is used to reference active default AEADKeys being used and AEADKeys include active and archive ones belong to the bucket.

**Note:** Archive AEADKey means it has been deactivated due to the deletion of old secret.

## Refresh active default AEADKeys for a bucket

As a best practice, refresh your bucket's default AEADKeys after approximately 42 billion object writes. This proactive step enhances security and prevents key exhaustion. The refresh process will create a new kekRef and deactivates the previous AEADKeys. To start the refresh process, delete the kekRef secret associated with the bucket.

**Note:** Mark AEADKey to be inactive wouldn't cause objects encrypted using that key to be crypto shredded.

The previous kekRef can be retrieved by running the following command to retrieve:
    
    
    kubectl get secrets -n NAMESPACE_NAME -l  object.gdc.goog/bucket-name=BUCKET_NAME
    

Then you can run the following to delete the existing kekRef:
    
    
    kubectl delete secrets OLD_KEKREF_NAME -n  NAMESPACE_NAME
    

After the successful deletion, you can run the following to confirm a new kekRef has been created based on `AGE`:
    
    
    kubectl get secrets -n NAMESPACE_NAME -l  object.gdc.goog/bucket-name=BUCKET_NAME
    

Verify new default AEADKeys have been created based on `AGE`:
    
    
    kubectl get aeadkeys -n NAMESPACE_NAME -l  cmek.security.gdc.goog/resource-name=BUCKET_NAME
    

## Rotate default AEADKeys for a bucket

If an AEADKey for your bucket becomes compromised, you must manually rotate the key encryption keys associated with the bucket.

To start the process, you must first refresh the active default keys. This creates new active default AEADKeys, and marks the previous key encryption keys as deactivated. After the default keys refresh, the subsequent object uploads use the new AEADKeys as the key encryption keys. The previous AEADKeys are not destroyed, so you can still decrypt existing objects that were previously encrypted using those keys.

Next, follow the steps to [download and re-upload](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/upload-download-storage-objects) the objects in your bucket and [delete the old objects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-objects).

After you re-upload all the objects in your bucket, you can clean up the inactive AEADKeys and old objects. Identify the deactivated AEADKeys based on `AGE`:
    
    
    kubectl get aeadkeys -n NAMESPACE_NAME -l  cmek.security.gdc.goog/resource-name=BUCKET_NAME
    

Lastly, follow the steps to [delete the AEADKeys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#delete).

**Note:** You can also [create a new bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets) and [delete and crypto-shred the compromised bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-buckets).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
