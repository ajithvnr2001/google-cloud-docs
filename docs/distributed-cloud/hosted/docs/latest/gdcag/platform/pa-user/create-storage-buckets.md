---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets/
title: Create storage buckets \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:59.653188+00:00
---

# Create storage buckets  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to create a storage bucket for your Google Distributed Cloud (GDC) air-gapped projects. It covers prerequisites, creation and verification steps, and naming guidelines. This helps you establish compliant and well-configured object storage that meets the needs of your isolated deployments.

This page is for audiences such as IT admins within the infrastructure operator group or developers within the application operator group who are looking to provision and manage object storage buckets for projects within GDC air-gapped environments. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

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



## Storage bucket naming guidelines

Bucket names must adhere to the following naming conventions:

  * Be unique within the project. The management API server prepends a unique prefix to the bucket's fully qualified name, ensuring there aren't clashes within the organization. In the unlikely event of a prefix and bucket name clash across organizations, the bucket creation fails with a "bucket name in use" error.
  * Refrain from including any personally identifiable information (PII).
  * Be DNS-compliant.
  * Have at least 1 and no more than 55 characters.
  * Start with a letter and use only letters, numbers, and hyphens.



## Create a bucket

**Note:** The bucket that is created will be automatically encrypted with either version `v1` or `v2`. `v2` will be the default if the `encryption-version` label is not specified since `v2` bucket is strongly recommended as it has better encryption and security. `v1` is only recommended if you need higher performance for many small objects.

By default, buckets use the `Standard` storage class. If Nearline storage has been enabled by your Infrastructure Operator (IO), you can also select the `Nearline` storage class for data that is accessed less frequently. Nearline storage is supported for both single-zone and dual-zone buckets.

### Console

  1. In the navigation menu, click **Object Storage**.
  2. In the project selector, select the project where you want to create the bucket.
  3. Click **Create Bucket**.
  4. In the bucket creation flow, assign a name unique across all buckets within the project.
  5. Enter a description.
  6. Under **Storage class** , select **Standard** or **Nearline**. The **Nearline** option is visible only if Nearline storage is enabled.
  7. Optional: Click the toggle_off toggle to set a retention policy and enter your preferred number of days. Contact your IO if you need to exceed retention policy limits.
  8. Click **Create**. A success message appears and you are directed back to the **Buckets** page.



To verify that you have successfully created a new bucket, refresh the **Buckets** page after a few minutes and check that the bucket state updates from `Not ready` to `Ready`.

### API

To create a zonal bucket, apply a bucket specification to your project namespace:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f bucket.yaml
    

The following is an example of a bucket specification using the `Standard` storage class:
    
    
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
    

The following is an example of a bucket specification using the `Nearline` storage class:
    
    
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
    spec:
      description: DESCRIPTION
      storageClass: Nearline
      bucketPolicy:
        lockingPolicy:
          defaultObjectRetentionDays: RETENTION_DAY_COUNT
    

The following is an example of a bucket specification with encryption version as `v1`:
    
    
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: NAMESPACE_NAME
      labels:
        object.gdc.goog/encryption-version: v1
    spec:
      description: DESCRIPTION
      storageClass: Standard
      bucketPolicy:
        lockingPolicy:
          defaultObjectRetentionDays: RETENTION_DAY_COUNT
    

For more details, see the [Bucket API reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/storage-api-overview).

The following is an example of a dual-zone bucket specification for the global API server:
    
    
    apiVersion: object.global.gdc.goog/v1
    kind: Bucket
    metadata:
      name: BUCKET_NAME
      namespace: PROJECT_NAME
    spec:
      location: LOCATION_NAME
      description: Sample DZ Bucket
      storageClass: Standard
    

To create a dual-zone bucket using Nearline storage, set `storageClass: Nearline`.

Note that only V2 encryption is supported for dual-zone buckets and all operations for creating, updating, or deleting a dual-zone bucket resource must be performed against the global API server.

To create a dual-zone bucket, apply the specification against the global API server:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f bucket.yaml
    

### gdcloud

To create a single-zone bucket with `gdcloud` using the `Nearline` storage class:
    
    
    gdcloud storage buckets create BUCKET_NAME \
        --location=ZONE_NAME \
        --location-type=SingleZone \
        --storage-class=Nearline
    

To create a dual-zone bucket with `gdcloud` using the global location:
    
    
    gdcloud storage buckets create BUCKET_NAME \
        --location=ZONE_1,ZONE_2 \
        --location-type=AsyncDualZone \
        --storage-class=Nearline
    

If `--storage-class` is omitted, `Standard` is used by default.

For more details, see [gdcloud storage buckets create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-create).

## Verify bucket and related resource creation

After creating the bucket, run the following command to confirm and check the details of the bucket:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG describe buckets BUCKET_NAME -n PROJECT_NAMESPACE
    

The **Status** section has two important fields: **Encryption** (for encryption details) and **Fully Qualified Name** (which contains the FULLY_QUALIFIED_BUCKET_NAME).

### Encryption v1

The information is about the AEADKey named as `obj-FULLY_QUALIFIED_BUCKET_NAME`, which serves as a reference to the encryption key employed for encrypting objects stored within the bucket. Here is an example:
    
    
    Status:
      Encryption:
        Key Ref:
          Kind: AEADKey
          Name: obj-FULLY_QUALIFIED_BUCKET_NAME
          Namespace: PROJECT_NAMESPACE
        Type: CMEK
    

### Encryption v2

The information pertains to the Secret named as `kek-ref-FULLY_QUALIFIED_BUCKET_NAME`, which acts as a reference for active default AEADKeys. Active default AEADKeys are randomly selected from to encrypt objects uploaded to the bucket when specific AEADKey is not specified.

**Note:** Inactive default AEADKeys are those that are no longer referenced in the Secret. See the Manage Encryption Resources section for more info.

Here is an example:
    
    
    Status:
      Encryption:
        Key Ref:
          Kind: Secret
          Name: kek-ref-FULLY_QUALIFIED_BUCKET_NAME
          Namespace: PROJECT_NAMESPACE
        Type: CMEK
    

You can also run the following command to verify needed AEADKeys are created:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG get aeadkeys -n PROJECT_NAMESPACE -l  cmek.security.gdc.goog/resource-name=FULLY_QUALIFIED_BUCKET_NAME
    

After creating a bucket, you can manage it on behalf of Application Operators (AOs) by creating a policy file when granting bucket access and assign the policy to a bucket.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
