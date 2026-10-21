---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/delete-storage-buckets/
title: Delete storage buckets for projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:08:50.228881+00:00
---

# Delete storage buckets for projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/delete-storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete storage buckets for projects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to delete Google Distributed Cloud (GDC) air-gapped storage buckets.

## Before you begin

Storage buckets are resources scoped to a specific [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management). The project acts as a container, grouping your buckets and enabling their management through the Management API server. Before you can perform the operations on this page, you must either create a new project or select an existing one where you have sufficient permissions.

### Required IAM roles

Contact your IAM Project Admin to request the following roles in your project namespace:

  * **Project Bucket Admin** (`project-bucket-admin`): create, update, and delete storage buckets.
  * **Project Bucket Object Viewer** (`project-bucket-object-viewer`): view and check details of storage buckets and objects.



For more information, see [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/grant-obtain-storage-access#grant_bucket_access).

### Prepare your environment

To run commands against the management API server or the global API server, do the following:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-resources-kubeconfig) the kubeconfig file for the zonal management API server if you don't have one.
  2. For dual-zone buckets, do the following: 
     * Verify with your Infrastructure Operator (IO) that the `BucketLocationConfig` custom resource has been created for your paired zones.
     * [Generate the kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#global-resources-kubeconfig) for the global API server.



## Delete storage buckets

**Warning:** Buckets with an [active retention policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/set-bucket-retention-periods) are blocked from deletion until the lock date expires. If you need to destroy the data before that date, you must [crypto-shred the bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-buckets#crypto_shred_bucket).

### Console

  1. In the navigation menu, click **Object Storage**.
  2. Click delete **Delete** at the end of the row of the bucket to be deleted.
  3. Wait a few minutes and refresh the page to check that the bucket is deleted.



### CLI

You can delete storage buckets by using the CLI. **Buckets must be empty before you can delete them.**

  1. Use the `GET` or `DESCRIBE` command from the [View bucket configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/list-view-storage-buckets#view_bucket_configurations) section to get the fully qualified bucket name.

  2. If the bucket is _not empty_ , delete files within the bucket:
         
         gdcloud storage rm --recursive --all-versions s3://FULLY_QUALIFIED_BUCKET_NAME/**
         

  3. Delete the empty bucket:

**Note:** Make sure the bucket is empty before using the following kubectl command to trigger the bucket deletion.
         
         kubectl delete buckets/FULLY_QUALIFIED_BUCKET_NAME --namespace PROJECT_NAMESPACE
         




## Crypto shred bucket

To crypto-shred a bucket is to permanently destroy access to its data by deleting the encryption keys, rendering the stored data unreadable. In comparison to deleting individual buckets when cleaning up storage, which can take minutes to days for very large buckets, crypto-shredding provides instant and irreversible data destruction at scale.

**Note:** Only `v1` encryption bucket can be crypto shred, for `v2` encryption bucket, use [Crypto shred objects in buckets with encryption v2](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-objects#crypto_shred_objects_in_buckets_with_encryption_v2)**Warning:** This step is not recoverable and you will lose all data encrypted in the bucket.

### Crypto shred buckets

Retrieve information about the `AEADKey` based on [Verify bucket resource creation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets#verify_bucket_and_related_resource_creation) and follow [Delete a key](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#delete) to delete the `AEADKey`, then the entire bucket would be crypto shredded.

After crypto shredding the bucket, proceed to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-buckets#verify_crypto_shred_success).

### Verify crypto shred success

You can run the following command to verify the bucket has been successfully crypto shredded. The `BucketReady` should be `False` and `Reason` to be `BucketCryptoShredded`.
    
    
    kubectl get buckets FULLY_QUALIFIED_BUCKET_NAME -n PROJECT_NAMESPACE
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
