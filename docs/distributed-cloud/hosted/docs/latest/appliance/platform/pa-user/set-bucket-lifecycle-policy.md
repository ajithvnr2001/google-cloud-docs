---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/set-bucket-lifecycle-policy/
title: Set object lifecycle policy for storage buckets \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:44.144170+00:00
---

# Set object lifecycle policy for storage buckets  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/set-bucket-lifecycle-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Set object lifecycle policy for storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set object lifecycle policy for Google Distributed Cloud (GDC) air-gapped appliance storage buckets.

## Before you begin

A project namespace manages bucket resources in the management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

You must also have the appropriate bucket permissions to perform the following operation. See [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

To run commands against the management API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) the kubeconfig file for the management API server if you don't have one.

## Set object lifecycle policy on bucket

You can use object lifecycle policy to automatically manage objects in your buckets. This helps you store data more efficiently throughout its lifespan. A lifecycle configuration is a list of rules to expire a group of objects based on certain matching criteria.

You can create a bucket with or without object lifecycle policy. And you can apply new, update existing or remove existing lifecycle policy after the bucket is created.

For unversioned buckets, expiration means permantently removing the object asynchronously.

For versioned buckets, if the current object version is not a deletion marker, expiration makes the current version noncurrent and then adds a delete marker the current version.

To set and modify the object lifecycle policy, update the `Bucket.spec.bucketPolicy.lifecyclePolicy` field.

The following are few examples of bucket resources with different object lifecycle policy configured:
    
    
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire all objects after 2000 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              days: 2000
            id: expire-all-after-2000-days
            status: Enabled
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire objects having name start with abc after 500 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              days: 500
            id: expire-all-start-with-abc-after-500-days
            status: Enabled
            filter:
              prefixFilter: "abc"
    ----------
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: "Bucket with lifecycle rule to expire objects having specific tag after 300 days"
      storageClass: Standard
      bucketPolicy:
        lifecyclePolicy:
          enable: true
          lifecycleRules:
          - expiration:
              days: 300
            id: expire-all-objects-with-specific-tag-after-300-days
            status: Enabled
            filter:
              tagFilters:
              - key: testKey
                value: testValue
    

**Note:** If you also want to expire the noncurrent version, you need to set the `noncurrentExpiration` field in the lifecycle rule.

Any updates to the lifecycle policy applies to the existing objects and objects uploaded after the update.

When the bucket also has object locking configured, objects are being protected from expiration before the retention days end.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
