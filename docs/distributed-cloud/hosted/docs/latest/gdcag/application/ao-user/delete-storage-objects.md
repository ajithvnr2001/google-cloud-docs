---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/delete-storage-objects/
title: Delete storage objects in projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:51.082684+00:00
---

# Delete storage objects in projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/delete-storage-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete storage objects in projects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to delete objects from Google Distributed Cloud (GDC) air-gapped storage buckets.

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



## Delete objects in buckets

###  Console 

  1. In the navigation menu, click **Object Storage**.
  2. Click the name of the bucket containing the objects.
  3. Wait to be redirected to the **Bucket details** page with objects listed in a table.
  4. Navigate to the object's detail page and click **Permanently delete**. Alternatively, in the bucket object list view, select the checkbox next to the object and then click **Permanently delete**.
  5. Wait a few minutes and refresh the page to check that the object is deleted.



Note that all objects in dual-zone buckets are versioned, so deleting an object won't remove that object from storage. Instead, the object will be marked for deletion and will no longer be visible in LIST calls. The object can still be retrieved by specifying its version ID. An object is permanently deleted only if you specify the `versionID` when performing the deletion.

###  gdcloud 

Delete a file from a bucket:
    
    
    gdcloud storage rm s3://FULLY_QUALIFIED_BUCKET_NAME/OBJECT
    

## Crypto shred objects in buckets with encryption v2

**Warning:** Deleting an AEADKey leads to irreversible data loss. Objects encrypted with the deleted key cannot be recovered.

  1. Retrieve all AEADKeys that belong to a bucket:
         
         kubectl get aeadkeys -n PROJECT_NAMESPACE -l  cmek.security.gdc.goog/resource-name=FULLY_QUALIFIED_BUCKET_NAME
         

  2. Follow [Delete a key](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#delete) to delete the intended AEADKey to crypto shred objects.




### Crypto shred dual-zone buckets

**Warning:** Deleting an MZAEADKey leads to irreversible data loss. Objects encrypted with the deleted key cannot be recovered.

  1. Retrieve all `MZAEADKeys` that belong to a bucket:


    
    
    kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG \
      get mzaeadkey -n PROJECT_NAMESPACE -l cmek.security.gdc.goog/resource-name=FULLY_QUALIFIED_BUCKET_NAME
    

  1. For each `MZAEADKey`, use the following command to delete the key and its zonal `AEADKey` replicas:


    
    
    kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG \
      delete mzaeadkey KEY_NAME --namespace=PROJECT_NAMESPACE
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
