---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/set-bucket-retention-periods/
title: Set storage bucket retention periods for projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:19.374126+00:00
---

# Set storage bucket retention periods for projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/set-bucket-retention-periods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Set storage bucket retention periods for projects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set retention periods for Google Distributed Cloud (GDC) air-gapped storage buckets.

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



## Set a bucket retention period

###  Console 

  1. In the navigation menu, click **Object Storage**.
  2. Click the name of the bucket that you want to update.
  3. Click the **Configuration** tab.
  4. In the Security section, next to the **Retention policy** field, click edit **Edit**.
  5. Edit the number of days with a value higher than the existing number of days and click **Save**.



###  API 

By default, you can delete objects at any time. You can enable object locking with a retention period to prevent all objects in the bucket from deletion for the specified number of days. You cannot delete a bucket until you delete all objects after the retention period.

You must enable object locking when creating the bucket. You cannot enable or disable object locking after you create a bucket. However, you can modify the default object retention period.

You can create a bucket with or without enabling object locking. If you've enabled object locking, specifying a default retention period is optional.

To modify the retention period, update the `Bucket.spec.bucketPolicy.lockingPolicy.defaultObjectRetentionDays` field in the [Bucket resource](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/storage-krm-api.md).

The following is an example of updating the field in the Bucket resource:
    
    
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "This bucket has a default retention period specified."
      storageClass: Standard
      bucketPolicy:
        lockingPolicy:
          defaultObjectRetentionDays: RETENTION_DAY_COUNT
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "This would enable object locking but not specify a default retention period."
      storageClass: Standard
      bucketPolicy:
        lockingPolicy:
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "This bucket does not have locking or retention enabled."
      storageClass: Standard
    

Any updates to the retention period apply to objects created in the bucket after the update. For pre-existing objects, the retention period does not change.

When you've enabled object locking, if you attempt to overwrite an object, you add a new version of the object. You can retrieve both object versions. To retrieve object versions, see [List storage objects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/list-storage-objects).

To create a write-once, read-many (WORM) bucket, refer to the [WORM Bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-worm-buckets) section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
