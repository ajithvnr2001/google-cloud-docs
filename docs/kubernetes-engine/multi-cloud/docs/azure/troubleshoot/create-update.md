---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/create-update/
title: Troubleshoot cluster creation or update issues \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:57.437686+00:00
---

# Troubleshoot cluster creation or update issues  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/create-update/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot cluster creation or update issues

This page shows you how to resolve issues related to installing or upgrading GKE on Azure.

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 

## Cluster creation failures

When you make a request to create a cluster, GKE on Azure first runs a set of _pre-flight tests_ to verify the request. If the cluster creation fails, it can be either because one of these pre-flight tests failed or because a step in the cluster creation process itself didn't complete.

If a pre-flight test fails, your cluster doesn't create any resources, and returns information on the error to you directly. For example, if you try to create a cluster with the name `invalid%%%name`, the pre-flight test for a valid cluster name fails and the request returns the following error:
    
    
    ERROR: (gcloud.container.azure.clusters.create) INVALID_ARGUMENT: must be
    between 1-63 characters, valid characters are /[a-z][0-9]-/, should start with a
    letter, and end with a letter or a number: "invalid%%%name",
    field: azure_cluster_id
    

Cluster creation can also fail after the pre-flight tests have passed. This can happen several minutes after cluster creation has begun, after GKE on Azure has created resources in Google Cloud and Azure. In this case, an Azure resource will exist in your Google Cloud project with its state set to `ERROR`.

To get details about the failure, run the following command:
    
    
    gcloud container azure clusters describe CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --format "value(state, errors)"
    

Replace the following:

  * CLUSTER_NAME with the name of the cluster whose state you're querying
  * GOOGLE_CLOUD_LOCATION with the name of the Google Cloud region that manages this Azure cluster



Alternatively, you can get details about the creation failure by describing the `Operation` resource associated with the create cluster API call.
    
    
    gcloud container azure operations describe OPERATION_ID
    

Replace OPERATION_ID with the ID of the operation that created the cluster. If you don't have the operation ID of your cluster creation request, you can fetch it with the following command:
    
    
    gcloud container azure operations list \
        --location GOOGLE_CLOUD_LOCATION
    

Use the timestamp or related information to identify the cluster creation operation of interest.

**Note:** After you resolve the failure, you must delete the cluster to release any resources that GKE on Azure created for it. You can then recreate the cluster.

## Cluster update failures

When you update a cluster, just as when you create a new cluster, GKE on Azure first runs a set of _pre-flight tests_ to verify the request. If the cluster update fails, it can be either because one of these pre-flight tests failed or because a step in the cluster update process itself didn't complete.

If a pre-flight test fails, your cluster doesn't update any resources, and returns information on the error to you directly. For example, if you try to update a cluster to use an SSH key pair with name `test_ec2_keypair`, the pre-flight test tries to fetch the EC2 key pair and fails and the request returns the following error:
    
    
    ERROR: (gcloud.container.azure.clusters.update) INVALID_ARGUMENT: key pair
    "test_ec2_keypair" not found,
    field: azure_cluster.control_plane.ssh_config.ec2_key_pair
    

Cluster updates can also fail after the pre-flight tests have passed. This can happen several minutes after cluster update has begun, and your Azure resource in your Google Cloud project has its state set to `DEGRADED`.

To get details about the failure and the related operation, follow the steps described in cluster creation failures.

## What's next

  * If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
