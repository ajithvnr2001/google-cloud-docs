---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-cluster/
title: Update your Azure cluster parameters \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:55.032225+00:00
---

# Update your Azure cluster parameters  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-cluster/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update your Azure cluster parameters

This page describes how to update your GKE on Azure cluster's settings. You can use these instructions to update any updatable setting in your cluster, including the Kubernetes version. Because upgrading the version is one of the most common cluster update operations, a separate [upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/upgrade-cluster) page covers how to upgrade a cluster version.

## Reasons to update a cluster

You might update a cluster for any of the following reasons:

  * To update your cluster's description.
  * To update your cluster's annotations.
  * To update your cluster's list of administrative users.
  * To update your cluster's logging configuration. 
  * To update your cluster's VM size.
  * To update your cluster's AzureClient.
  * To update your cluster's Authentication from AzureClient to workload identity federation. 



You can also update other fields in your clusters not listed here. For a complete list of fields you can update, see the [`gcloud container azure clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update) and the [`projects.locations.azureClusters.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/patch) documentation.

## Prerequisites

  * To update any of your cluster's fields, you must have the `gkemulticloud.googleapis.com/azureClusters.update` Identity and Access Management permission. 




## The update process

The process by which GKE on Azure updates a cluster differs depending on the type of update. For some changes, GKE on Azure can update a cluster without restarting or recreating any resources—for example, updating a cluster's description. GKE on Azure makes these changes immediately.

Other changes require restarting the control plane nodes—for example, updating the VM size or Kubernetes version. For such updates, GKE on Azure performs a "rolling update" consisting of the following steps:

  1. Choose one control plane instance to update. GKE on Azure updates unhealthy instances, if any, before healthy ones.
  2. Delete the instance. GKE on Azure recreates the instance and the instance boots with the new configuration.
  3. Perform health checks on the new instance.
  4. If the health checks succeed, select another instance and perform the same steps on it. Repeat this cycle until all instances are restarted or recreated. If the health check fails, GKE on Azure places the cluster into a `DEGRADED` state and stops the update. For more information, see the following section.



### When an update fails

After an update, GKE on Azure performs a health check on the cluster. If the health check fails, the cluster is marked as `DEGRADED`. You can display the status of your cluster with the following Google Cloud CLI command:
    
    
    gcloud container azure clusters describe CLUSTER_NAME \
      --location=GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster



## Update your cluster

You can use either the Google Cloud console, the Google Cloud CLI, or the GKE Multi-Cloud API to update multiple cluster fields at once.

### Choose an update method

You can update most fields through either the console, the gcloud CLI, or the GKE Multi-Cloud API. Some fields can only be updated through one mechanism or the other. If you want to use the console to update a cluster, you must first choose and configure an authentication method for logging in to the cluster. For more information, see [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster).

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. In the cluster list, select the name of the cluster, and then select **View details** in the side panel.

  4. On the **Details** tab, select edit  **Edit** on the field that you want to change.

For example, to grant cluster administrative privileges to other users select edit **Edit** next to **Admin users** and enter the email address of the user.

  5. When you are finished making changes, select **Done**.




### gcloud

When you update a cluster using the gcloud CLI, you must always include the`CLUSTER_NAME` and `GOOGLE_CLOUD_LOCATION` fields, which tell GKE on Azure what cluster to update. In the following command, only include the fields that you want to update; remove the other fields before running the command.
    
    
    gcloud container azure clusters update CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --cluster-version=CLUSTER_VERSION \
        --admin-users=USERNAME_LIST \
        --client=CLIENT_NAME \
        --vm-size=VM_SIZE 
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION` (required): the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  * `CLUSTER_VERSION`: the new [supported cluster version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions)
  * `USERNAME_LIST`: a comma-separated list of usernames, for example, "kai@example.com,hao@example.com,kalani@example.com". These are the email addresses of the users you're granting administrative privileges on this cluster to. The names in this setting will replace any previous list of admin-users on the cluster. 
  * `CLIENT_NAME`: your AzureClient
  * `VM_SIZE`: the new supported [VM size](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-vms)



To update the cluster's Authentication from AzureClient to [workload identity federation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster#workload-identity-federation), run the following command:
    
    
    gcloud container azure clusters update CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --azure-tenant-id="${TENANT_ID}" \
        --azure-application-id="${APPLICATION_ID}" \
        --clear-client
    

### API

When you update a cluster using the GKE Multi-Cloud API, you must always include the`CLUSTER_NAME` and `GOOGLE_CLOUD_LOCATION` fields in the HTTP request. These fields tell GKE on Azure what cluster to update. You must also include the API endpoint in the request. You create a JSON file with the fields that you want to update. Only include the fields that you want to update in the JSON file and in the `UPDATE_MASK`.

The following example shows how to update your cluster through the API. For more information, including the list of fields that you can update, see the [`projects.locations.azureClusters.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/patch) method documentation.

  1. Create a JSON file named `cluster_update.json` with the fields that you want to update.

     * When using [workload identity federation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster#workload-identity-federation), the JSON file should look like this: 
           
           {
             "description": "CLUSTER_DESCRIPTION",
             "controlPlane": {
               "version": "CLUSTER_VERSION",
               "vm_size": "VM_SIZE
             },
             "azureServicesAuthentication": {
               "tenantId": "TENANT_ID",
               "applicationId": "APPLICATION_ID"
             },
             "authorization": {
                 "adminUsers": [
                     {
                     "username": USERNAME1,
                     "username": USERNAME2,
                     "username": USERNAME3
                     }
                 ]
             }
           }
           

     * When using [Azure client](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster#create-client), the JSON file should look like this: 
           
           {
             "description": "CLUSTER_DESCRIPTION",
             "controlPlane": {
               "version": "CLUSTER_VERSION",
               "vm_size": "VM_SIZE
             },
             "azureClient": "CLIENT_NAME",
             "authorization": {
                 "adminUsers": [
                     {
                     "username": USERNAME1,
                     "username": USERNAME2,
                     "username": USERNAME3
                     }
                 ]
             }
           }
           

Replace the following:

     * `CLUSTER_VERSION`: the new [supported cluster version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions). Note that you must upgrade through all minor versions when upgrading your cluster
     * `CLUSTER_DESCRIPTION`: the new cluster description
     * `USERNAME1`,`USERNAME2`,`USERNAME3`: the email addresses of the users you're granting administrative privileges on this cluster to. The names in these fields will replace any previous list of admin-users on the cluster. 
     * `CLIENT_NAME`: your [AzureClient](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client) name
     * `TENANT_ID`: the Azure tenant ID
     * `APPLICATION_ID`: the Azure application ID that was created in [Create an Azure Active Directory Application](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application)
     * `VM_SIZE`: the new [VM size](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-vms)
  2. Update these settings through the GKE Multi-Cloud API with following command.
         
         curl -d @cluster_update.json -X PATCH \
            ENDPOINT/projects/PROJECT_ID/locations/GOOGLE_CLOUD_LOCATION/azureClusters/CLUSTER_NAME?update_mask=UPDATE_MASK
         




Replace the following:

  * `ENDPOINT` (required): Your Google Cloud [service endpoint](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest#rest_endpoints)
  * `PROJECT_ID` (required): Your Google Cloud project
  * `GOOGLE_CLOUD_LOCATION` (required): the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  * `CLUSTER_NAME` (required): Your cluster name
  * `UPDATE_MASK` (required): a comma-separated list of one or more of the following flags, indicating which fields you want to update. In this example, specify the following. 
    * controlPlane.version
    * description
    * authorization.admin_users 
    * control_plane.vm_size
    * azure_client
    * azure_services_authentication.tenant_id
    * azure_services_authentication.application_id 



To update the cluster's Authentication from AzureClient to [workload identity federation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster#workload-identity-federation), add `azure_client`, `azure_services_authentication.tenant_id` and `azure_services_authentication.application_id` in the field `update_mask`. 

## Update Logging Config

You can update your cluster's [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/cloud-logging) configuration settings with the Google Cloud CLI. To update the logging configuration, run the following command:
    
    
    gcloud container azure clusters update CLUSTER_NAME \
        --location=GOOGLE_CLOUD_LOCATION \
        --logging=LOGGING_CONFIG \
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  * `LOGGING_CONFIG`: [SYSTEM] or [SYSTEM,WORKLOAD]



## What's next

  * To update volume KMS keys, see [Key rotation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/key-rotation#control_plane_root_volume)
  * For more information on updatable fields, see the [`gcloud container azure clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update) reference documentation.
  * See the [`projects.locations.azureClusters.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/patch) REST API documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
