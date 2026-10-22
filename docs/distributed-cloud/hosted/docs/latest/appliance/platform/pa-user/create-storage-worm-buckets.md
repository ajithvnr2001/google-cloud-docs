---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-storage-worm-buckets/
title: Create storage WORM buckets \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:54.726537+00:00
---

# Create storage WORM buckets  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-storage-worm-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create storage WORM buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to create Write Once Read Many (WORM) storage buckets in Google Distributed Cloud (GDC) air-gapped appliance environments. This covers the prerequisites and steps for creating a WORM bucket with a defined retention period, and for granting access permissions using role bindings. This information lets you enforce strict data retention practices and immutability, providing robust and compliant data storage for records and use cases like audit logging.

This page is for audiences such as IT administrators within the infrastructure operator group or developers within the application operator group who manage data retention and compliance settings for storage buckets in GDC air-gapped environments.

## Before you begin

A project namespace manages bucket resources in the management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

You must also have the appropriate bucket permissions to perform the following operation. See [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

To run commands against the management API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) the kubeconfig file for the management API server if you don't have one.

## Create a WORM bucket

A WORM bucket ensures that nothing else overwrites objects and it retains them for a minimum period of time. Audit logging is an example use case for a WORM bucket.

Take the following steps to create a WORM bucket:

  1. Set a retention period when creating the bucket. For example, the following example bucket has a retention period of 365 days.
         
         apiVersion: object.gdc.goog/v1
         kind: Bucket
         metadata:
           name: foo logging-bucket
           namespace: foo-service
         spec:
           description: "Audit logs for foo"
           storageClass: Standard
           bucketPolicy :
             lockingPolicy :
               defaultObjectRetentionDays: 365
         

  2. Grant the `project-bucket-object-viewer` role to all users who need read-only access:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           namespace: foo-service
           name: object-readonly-access
         roleRef:
           kind: Role
           name: project-bucket-object-viewer
           apiGroup: rbac.authorization.k8s.io
         subjects:
         - kind: ServiceAccount
           namespace: foo-service
           name: foo-log-processor
         - kind: User
           name: bob@example.com
           apiGroup: rbac.authorization.k8s.io
         

  3. Grant the `project-bucket-object-admin` role to users who need to write content to the bucket:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           namespace: foo-service
           name: object-write-access
         roleRef:
           kind: Role
           name: project-bucket-object-viewer
           apiGroup: rbac.authorization.k8s.io
         subjects:
         - kind: ServiceAccount
           namespace: foo-service
           name: foo-service-account
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
