---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/set-bucket-retention-periods/
title: Set bucket retention periods \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:58.644552+00:00
---

# Set bucket retention periods  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/set-bucket-retention-periods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Set bucket retention periods Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to set retention periods for storage buckets within Google Distributed Cloud (GDC) air-gapped appliance environments. It covers the prerequisites and the steps for defining the length of time that data must be retained within a storage bucket. This information helps you meet your regulatory and data management requirements.

This page is for audiences such as IT administrators within the infrastructure operator group or developers within the application operator group who are responsible for configuring and managing storage bucket settings in GDC air-gapped environments.

By default, you can delete objects at any time. Enable object locking with a retention period to prevent all objects in the bucket from deletion for the specified number of days. You cannot delete a bucket until you delete all objects after the retention period.

You must enable object locking when creating the bucket. You cannot enable or disable object locking after you create a bucket. However, you can modify the default object retention period.

You can create a bucket with or without enabling object locking. If you've enabled object locking, specifying a default retention period is optional.

To modify the retention period, update the `Bucket.spec.bucketPolicy.lockingPolicy.defaultObjectRetentionDays` field in the [Bucket resource](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-krm-api).

The following is an example of updating the field in the Bucket resource:
    
    
    apiVersion: object.gdc.goog/v1alpha1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "This bucket has a default retention period specified."
      storageClass: Standard
      bucketPolicy :
        lockingPolicy :
          defaultObjectRetentionDays: RETENTION_DAY_COUNT
    ---
    apiVersion: object.gdc.goog/v1alpha1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "This would enable object locking but not specify a default retention period."
      storageClass: Standard
      bucketPolicy :
        lockingPolicy :
    ---
    apiVersion: object.gdc.goog/v1alpha1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "This bucket does not have locking or retention enabled."
      storageClass: Standard
    

Any updates to the retention period apply to objects created in the bucket after the update. For pre-existing objects, the retention period does not change.

When you've enabled object locking, if you attempt to overwrite an object, you add a new version of the object. You can retrieve both object versions. For details on how to list object versions, see `ListObjectVersions` from the Amazon Web Services documentation: <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html>

To create a write-once, read-many (WORM) bucket, refer to the WORM Bucket section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
