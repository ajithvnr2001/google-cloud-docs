---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/list-view-storage-buckets/
title: List and view storage bucket configurations \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:51.956290+00:00
---

# List and view storage bucket configurations  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/list-view-storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  List and view storage bucket configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to list storage buckets within a Google Distributed Cloud (GDC) air-gapped project and view the configuration details for each bucket. Learn about the prerequisites and the steps using both the GDC console and command line interface (CLI). This information lets you gain full visibility of your object storage resources and helps you verify their configuration.

This page is for audiences such as IT admins within the infrastructure operator group or developers within the application operator group who are responsible for managing object storage resources in GDC air-gapped environments. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

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



## List storage buckets

###  Console 

  1. In the navigation menu, click **Object Storage**. All buckets you have access to are listed in a table.



###  kubectl 

To list all the buckets that you have access to in a given object storage tenant, complete the following steps:

  * Run the following command to list all buckets:
        
        kubectl get buckets --all-namespaces
        

  * Run the following command to list all buckets in a namespace:
        
        kubectl get buckets --namespace NAMESPACE_NAME
        




## View bucket configurations

###  Console 

  1. In the navigation menu, click **Object Storage**.
  2. Click the name of the bucket of which you want to view the details.
  3. Wait to be redirected to a detailed view page.



###  kubectl 

Use either command to view the configuration details for a bucket:
    
    
    kubectl describe buckets/BUCKET_NAME --namespace NAMESPACE_NAME
    
    
    
    kubectl get buckets/BUCKET_NAME --namespace NAMESPACE_NAME -o yaml
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
