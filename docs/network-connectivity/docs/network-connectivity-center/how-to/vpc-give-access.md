---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access/
title: Give access \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.551303+00:00
---

# Give access  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Give access Stay organized with collections  Save and categorize content based on your preferences. 

As a hub administrator, you can grant specific users the ability to create spokes in other projects associated with the hub, and retain full control over which spokes are accepted into the hub. Spokes do not become active until you explicitly accept them. You can also reject spokes at any time, if necessary.

To grant another user the ability to create spokes in other projects associated with the hub, you can grant the `roles/networkconnectivity.groupUser` role to that user. A user with the `groupUser` role on a hub automatically has the role on all groups in the hub through the Identity and Access Management (IAM) resource hierarchy. As the hub administrator, you can also revoke a user's access.

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

To enable the Network Connectivity API:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. Click **Enable**.




Alternatively, you can enable the API by using the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), as described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.getIamPolicy`
  * `networkconnectivity.hubs.setIamPolicy`



**Roles**

  * `roles/networkconnectivity.hubAdmin`



## Manage access to create spokes in hubs across projects

The following sections describe how to grant, revoke, or view permissions to create spokes in different projects than a hub.

### Grant the `groupUser` role on a hub to another user

To grant the `networkconnectivity.groupUser` role on a hub to another user, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click the **Hubs** tab.

  4. In the hubs list, select the hub to which you to add access.

  5. Click **Permissions**.

  6. In the **Permissions** dialog, click **Add principal**.

  7. Enter the username of the administrator that you want to add.

  8. In the **Manage roles** dialog, from the **Network Connectivity** roles list, select the role that you want to assign, such as **Spoke Admin**.

  9. Click **Save**.




###  gcloud 

Run the [`gcloud network-connectivity hubs add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/add-iam-policy-binding).
    
    
    gcloud network-connectivity hubs add-iam-policy-binding HUB_NAME \
        --member=MEMBER_DETAILS \
        --role='roles/networkconnectivity.groupUser'
    
    

Replace the following:

  * `HUB_NAME`: the hub for the spoke, such as `my-hub`.
  * `MEMBER_DETAILS`: details about the user to whom you want to grant access. For detailed information about identifiers and format, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1).



### Revoke the `groupUser` role on a hub from a user

To revoke the `roles/networkconnectivity.groupUser` role on a hub from a user, follow these steps.

###  gcloud 

Run the [`gcloud network-connectivity hubs remove-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/remove-iam-policy-binding).
    
    
    gcloud network-connectivity hubs remove-iam-policy-binding HUB_NAME \
        --member=MEMBER_DETAILS \
        --role='roles/networkconnectivity.groupUser'
    
    

Replace the following:

  * `HUB_NAME`: the hub for the spoke, such as `my-hub`.
  * `MEMBER_DETAILS`: details about the user that you want to remove access from. For detailed information about identifiers and format, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1).



### View permissions for a user

To view permissions that have been granted to a user on a hub, follow these steps.

###  gcloud 

Run the [`gcloud network-connectivity hubs get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/get-iam-policy).
    
    
    gcloud network-connectivity hubs get-iam-policy HUB_NAME
    

Replace `HUB_NAME` with the name of the hub for which you want to view permissions, such as `my-hub`.

## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
