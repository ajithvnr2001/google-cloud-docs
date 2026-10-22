---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/set-bucket-lifecycle-policy/
title: Set object lifecycle policy for storage buckets \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:49.366144+00:00
---

# Set object lifecycle policy for storage buckets  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/set-bucket-lifecycle-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Set object lifecycle policy for storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set object lifecycle policy for Google Distributed Cloud (GDC) air-gapped storage buckets.

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



## Set object lifecycle policy on bucket

You can use object lifecycle policy to automatically manage objects in your buckets. This helps you store data more efficiently throughout its lifespan. A lifecycle configuration is a list of rules to expire a group of objects based on certain matching criteria.

You can create a bucket with or without object lifecycle policy. And you can apply new, update existing or remove existing lifecycle policy after the bucket is created.

For unversioned buckets, expiration means permanently removing the object asynchronously.

For versioned buckets, if the current object version is not a deletion marker, expiration makes the current version noncurrent and then adds a delete marker to the current version.

To set and modify the object lifecycle policy, update the `Bucket.spec.bucketPolicy.lifecyclePolicy` field.

### CLI

The following are few examples of bucket resources with different object lifecycle policy configured:
    
    
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire all objects after 365 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              days: 365
            id: expire-all-after-365-days
            status: Enabled
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire objects in the logs/ directory after 30 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              days: 30
            id: expire-logs-dir-after-30-days
            status: Enabled
            filter:
              prefixFilter: "logs/"
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire objects having specific tag after 30 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              days: 30
            id: expire-tagged-objects-after-30-days
            status: Enabled
            filter:
              tagFilters:
              - key: environment
                value: dev
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire noncurrent versions after 90 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - noncurrentExpiration:
              noncurrentDays: 90
            id: expire-noncurrent-after-90-days
            status: Enabled
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire objects on a specific date"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              date: "2027-01-01T00:00:00Z"
            id: expire-on-specific-date
            status: Enabled
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with multiple lifecycle rules and advanced filters"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          # Rule 1: Expire objects in 'tmp/' directory AND tagged with 'status=ready' after 7 days
          - expiration:
              days: 7
            id: expire-ready-tmp-objects
            status: Enabled
            filter:
              prefixFilter: "tmp/"
              tagFilters:
              - key: status
                value: ready
          # Rule 2: Expire all objects in 'logs/' directory after 90 days
          - expiration:
              days: 90
            id: expire-logs-after-90-days
            status: Enabled
            filter:
              prefixFilter: "logs/"
    

**Note:** To expire noncurrent versions in a versioned bucket, use the `noncurrentExpiration` field as shown in the examples. You can combine both `expiration` and `noncurrentExpiration` in a single rule. If multiple filters (e.g. prefix and tags) are specified in a single rule, they are evaluated using AND logic (all conditions must match).

Any updates to the lifecycle policy applies to the existing objects and objects uploaded after the update.

When the bucket also has object locking configured, objects are being protected from expiration before the retention days end.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
