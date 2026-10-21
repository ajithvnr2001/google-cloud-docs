---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-worm-buckets/
title: Create storage WORM buckets \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:01.661821+00:00
---

# Create storage WORM buckets  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-worm-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create storage WORM buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to create Write Once Read Many (WORM) storage buckets in Google Distributed Cloud (GDC) air-gapped environments. This covers the prerequisites and steps for creating a WORM bucket with a defined retention period, and for granting access permissions using role bindings. This information lets you enforce strict data retention practices and immutability, providing robust and compliant data storage for records and use cases like audit logging.

This page is for audiences such as IT administrators within the infrastructure operator group or developers within the application operator group who manage data retention and compliance settings for storage buckets in GDC air-gapped environments. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

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



## Create a WORM bucket

A WORM bucket ensures that nothing else overwrites objects and it retains them for a minimum period of time. Audit logging is an example use case for a WORM bucket.

**Note:** If you attempt to overwrite an object in a WORM bucket, you will add a new version of the object. Only after a WORM object's retention period, as dictated by the bucket locking policy, is over can you proceed with object, bucket, and project deletion.

Take the following steps to create a WORM bucket:

  1. Set a retention period when creating the bucket. The retention period defines how many days each object version is locked against deletion or modification. This retention period is distinct from the storage class minimum storage duration (such as the 30-day minimum for the `Standard` storage class). For example, the following bucket sets a retention period of 365 days. Contact your Infrastructure Operator (IO) if you need to exceed retention policy limits.
         
         apiVersion: object.gdc.goog/v1
         kind: Bucket
         metadata:
           name: foo-logging-bucket
           namespace: foo-service
         spec:
           description: "Audit logs for foo"
           storageClass: Standard
           bucketPolicy:
             lockingPolicy:
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
           name: project-bucket-object-admin
           apiGroup: rbac.authorization.k8s.io
         subjects:
         - kind: ServiceAccount
           namespace: foo-service
           name: foo-service-account
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
