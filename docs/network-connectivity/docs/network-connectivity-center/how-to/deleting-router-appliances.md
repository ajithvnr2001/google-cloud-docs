---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/deleting-router-appliances/
title: Delete router appliance instances \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:50.336090+00:00
---

# Delete router appliance instances  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/deleting-router-appliances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Delete router appliance instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a router appliance instance and its underlying Google Cloud resources. To illustrate the process, this page uses the scenario described in [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).

**Caution:** When following the steps on this page, make sure that you're not deleting any Google Cloud resources that carry production traffic.

For more information about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

For more information about Network Connectivity Center (NCC), see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

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




### Get access

To work with NCC, you need the permissions described in [Access control](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

## Delete the BGP peers on Cloud Router

**Note:** You can delete multiple BGP peers or multiple interfaces in one command by separating them with a comma.

###  gcloud 

To delete two redundant BGP peers on the Cloud Router for the router appliance instance, enter the following command:
    
    
     gcloud compute routers remove-bgp-peer NAME \
         --peer-name PEER_NAME,PEER_NAME \
         --region=REGION \
         --project=PROJECT_ID
    

Replace the following:

  * `NAME`: the name of the Cloud Router to update—for example, `router-a`
  * `PEER_NAME`: the name of the BGP peer to delete—for example, `router-appliance-bgp-peer-0`, `router-appliance-bgp-peer-1`
  * `REGION`: the region where the VM acting as the router appliance instance is located—for example, `us-west1`
  * `PROJECT_ID`: the ID for the project for the Cloud Router—for example, `my-project`



###  API 

To delete two BGP peers on the Cloud Router for a router appliance instance, use the [`compute.routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch). In your request, pass information about the BGP peers _that you want to keep_. You must include all configured fields for each peer.

The following example removes all BGP peers from the Cloud Router:
    
    
    PATCH
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/region/REGION/routers/NAME
     {
      "bgpPeers": []
     }
    

Replace the following:

  * `PROJECT_ID`: the ID for the project for the Cloud Router—for example, `my-project`
  * `REGION`: the region where the VM acting as the router appliance instance is located—for example, `us-west1`
  * `NAME`: the name of the Cloud Router to update—for example, `router-a`



## Delete Cloud Router interfaces for the router appliance instance

When deleting Cloud Router interfaces for router appliance instances, use the following guidelines:

  * Delete both interfaces at the same time.
  * Only delete Cloud Router interfaces if other Google Cloud resources aren't using them.

**Note:** You must delete the primary interface and the redundant interface at the same time.

###  gcloud 

To delete two redundant Cloud Router interfaces for a router appliance instance, enter the following command:
    
    
     gcloud compute routers remove-interface NAME \
         --interface-names=INTERFACE_NAME,INTERFACE_NAME \
         --region=REGION \
         --project=PROJECT_ID
    

Replace the following:

  * `NAME`: the name of the Cloud Router to update—for example, `router-a`
  * `INTERFACE_NAME`: the name of the interface—for example, `router-appliance-interface-0`, `router-appliance-interface-1`
  * `REGION`: the Google Cloud region where the Cloud Router is located—for example, `us-west1`
  * `PROJECT_ID`: the ID for the project for the Cloud Router—for example, `my-project`



###  API 

To delete two redundant interfaces on the Cloud Router for a router appliance instance, use the [`compute.routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch). In your request, pass information about the BGP peers _that you want to keep_. You must include all configured fields for each peer.

The following example removes all interfaces from the Cloud Router:
    
    
    "PATCH   https"://www.googleapis.com/compute/v1/projects/PROJECT_ID/region/REGION/routers/NAME{
      "region":"REGION",
      "interfaces":[]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID for the project for the Cloud Router—for example, `my-project`
  * `REGION`: the Google Cloud region where the Cloud Router is located—for example, `us-west1`
  * `NAME`: the name of the Cloud Router to update—for example, `router-a`
  * `NETWORK`: the name of the VPC network—for example, `network-a`
  * `INTERFACE_NAME`: the name of the interface—for example, `router-appliance-interface-0`, `router-appliance-interface-1`



## Delete the Cloud Router

**Caution:** Make sure not to delete a Cloud Router that carries production traffic.

For steps, see [Deleting routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers#deleting_routers).

## Delete the Network Connectivity Center spoke

For steps, see [Deleting a spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-spoke).

## Delete router appliance software on the VM

For steps, refer to the documentation from your router appliance vendor.

## Delete the router appliance VM

###  gcloud 

To delete a router appliance VM instance, enter the following command:
    
    
    gcloud compute instances delete INSTANCE_NAME \
        --project=PROJECT_ID \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the router appliance instance—for example, `router-app-a`
  * `PROJECT_ID`: the ID for the project for the Cloud Router—for example, `my-project`
  * `ZONE`: the zone where the VM acting as the router appliance instance is located—for example, `us-west1-a`



###  API 

To delete a VM instance, use the [`compute.instances.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/delete):
    
    
    DELETE https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID for the project for the Cloud Router—for example, `my-project`
  * `ZONE`: the zone where the VM acting as the router appliance instance is located—for example, `us-west1-a`
  * `INSTANCE_NAME`: the name of the router appliance instance—for example, `router-app-a`



## Delete the firewall rule that allows BGP

If applicable, delete the firewall rule that allows BGP traffic on TCP port `179` to the network that contains router appliance instances.

For steps, see [Delete firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#deleting_firewall_rules).

## What's next

  * To view Router appliance monitoring and logging information, see [Viewing logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/viewing-logs-metrics).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
