---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-storage-buckets/
title: Create storage buckets \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:00.534197+00:00
---

# Create storage buckets  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to create a storage bucket for your Google Distributed Cloud (GDC) air-gapped appliance projects. It covers prerequisites, creation and verification steps, and naming guidelines. This helps you establish compliant and well-configured object storage that meets the needs of your isolated deployments.

This page is for audiences such as IT admins within the infrastructure operator group or developers within the application operator group who are looking to provision and manage object storage buckets for projects within GDC air-gapped environments.

## Before you begin

A project namespace manages bucket resources in the management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

You must also have the appropriate bucket permissions to perform the following operation. See [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

To run commands against the management API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) the kubeconfig file for the management API server if you don't have one.

## Storage bucket naming guidelines

Bucket names must adhere to the following naming conventions:

  * Be unique within the project. A project appends a unique prefix to the bucket name, ensuring there aren't clashes within the organization. In the unlikely event of a prefix and bucket name clash across organizations, the bucket creation fails with a `bucket name in use` error.
  * Have at least one and no more than 57 characters.
  * Refrain from including any personally identifiable information (PII).
  * Be DNS-compliant.
  * Start with a letter and contain only letters, numbers, and hyphens.



## Create a bucket

To create a bucket, apply a bucket specification to your project namespace:
    
    
      kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f bucket.yaml
    

The following is an example of a bucket specification:
    
    
        apiVersion: object.gdc.goog/v1
        kind: Bucket
        metadata:
          name: BUCKET_NAME
          namespace: NAMESPACE_NAME
        spec:
          description: DESCRIPTION
          storageClass: Standard
          bucketPolicy:
            lockingPolicy:
              defaultObjectRetentionDays: RETENTION_DAY_COUNT
    

For more details, see the [Bucket API reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-krm-api).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
