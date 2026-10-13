---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status/
title: Check the status of a VPC spoke \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:57.967927+00:00
---

# Check the status of a VPC spoke  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Check the status of a VPC spoke Stay organized with collections  Save and categorize content based on your preferences. 

When you [propose a Virtual Private Cloud (VPC) spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke) connection to a hub, the spoke is not fully operational until the hub administrator accepts the spoke. Similarly, when you propose updates to the properties of an existing spoke, the updates aren't effective until the hub administrator accepts the updates. This page describes how you can check the status of a spoke after you have proposed a new spoke or updates to an existing spoke.

## Before you begin

Before you get started, review the following sections.

### Create or select a project

To make it easier to configure NCC, start by identifying a valid project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. If you are using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your unique project ID.

The gcloud CLI instructions on this page assume that you have set your project ID. 

  13. To confirm that you set the project ID correctly, use the [`gcloud config list` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/list).
         
         gcloud config list --format='text(core.project)'




### Enable the Network Connectivity API

Before you can perform _any_ tasks using Network Connectivity Center (NCC), you must enable the Network Connectivity API.

###  Console

To enable the Network Connectivity API, do the following:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. Click **Enable**.




Alternatively, you can enable the API by using the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), as described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.get`



**Roles** (one of the following)

  * `roles/networkconnectivity.hubAdmin`
  * `roles/networkconnectivity.spokeAdmin`
  * `roles/networkconnectivity.hubViewer`



## Spoke states

The following table describes the different states that a spoke might be in after it is proposed to the hub administrator.

Spoke state | State reason | Description  
---|---|---  
`ACTIVE` | The `reasons` field is empty. |  For new spoke proposals, this means that the hub administrator has accepted the spoke and the spoke is fully operational.  For updates to existing spokes, this means that the hub administrator has accepted the updates and the updates have been applied.   
`ACTIVE` | `UPDATE_PENDING_REVIEW` |  This means that the spoke is operational, but a proposed update to the spoke's properties hasn't yet been accepted or rejected. If a spoke update is rejected by the hub administrator, but the rejection fails, the spoke might still show an `UPDATE_PENDING_REVIEW` state.   
`ACTIVE` | `UPDATE_FAILED` |  This means that the spoke is operational, and a proposed update to the spoke's properties was accepted, but the update failed.   
`ACTIVE` | `UPDATE_REJECTED` |  This means that the spoke is operational, but a proposed update to the spoke's properties was rejected.   
`INACTIVE` | `PENDING_REVIEW` |  This means that the spoke is not operational, and that the hub administrator hasn't yet accepted or rejected the spoke.   
`INACTIVE` | `REJECTED` |  This means that the spoke is not operational because the hub administrator has rejected the spoke.   
`OBSOLETE` | The `reasons` field is empty. |  This means that the hub has been deleted. Once in this state, the state never changes, and the spoke can only be deleted.   
  
## Get the status of a spoke proposal

To get the status of a spoke that you have proposed in a different project from the hub, including updates to existing spokes, follow these steps.

###  gcloud 

Run the [`gcloud network-connectivity spokes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/describe).
    
    
    gcloud network-connectivity spokes describe SPOKE_NAME \
        --global
    

Replace `SPOKE_NAME` with the name of the spoke for which you want to check the status, such as `my-spoke`.

###  API 

To describe a spoke, use the [`networkconnectivity.spokes.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/get).
    
    
     GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the spoke
  * `SPOKE_NAME`: the name of the spoke for which you want to get status



## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
