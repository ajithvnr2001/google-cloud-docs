---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview/
title: NCC Gateway setup overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:05.464249+00:00
---

# NCC Gateway setup overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  NCC Gateway setup overview Stay organized with collections  Save and categorize content based on your preferences. 

This page gives you an overview of the steps required to set up NCC Gateway.

Before you begin the setup process for NCC Gateway, familiarize yourself with the following resources:

  * [Network Connectivity Center (NCC) overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)

  * [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview)




As part of the NCC Gateway setup process, you must complete several tasks. Depending on your configuration, the way that you complete these tasks can vary significantly. The following set up instructions use a four [spoke group](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#hybrid-inspection-spoke-groups) hybrid inspection topology.

## Set up NCC Gateway for new users

If you want to set up NCC Gateway no pre-existing connectivity, do the following:

  1. [Create a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-hub#ncc-gateway-create-ncc-hub).

You first create an NCC hub to which you can attach NCC Gateway spokes. The hub can use any of the preset [connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).

  2. [Create an NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke).

You must create an [NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#gateway-spokes) and attach it to the hub that you created.

  3. [Connect the Secure Access Connect attachment to NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/connect-sac).

The Secure Access Connect attachment lets you connect NCC Gateway with third-party Security Service Edge (SSE) products.

NCC Gateway supports connections to the following SSE products:

     * [Palo Alto Networks Prisma Access](https://docs.paloaltonetworks.com/prisma-access/integration/ncc-gateway-integration-in-prisma-access)
     * [Symantec Cloud Secure Web Gateway (Cloud SWG)](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/conn-matrix/adm_addlocation_st/express-connect.html) ([Preview](https://cloud.google.com/products#product-launch-stages))

To complete this step, you must already have an account with the provider.

  4. [Add VLAN attachments to the NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments).

Your Google Cloud and on-premises environment or other cloud environments must be connected through [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) by using Cloud Interconnect VLAN attachments with Cloud Router.

  5. [Create and manage NCC Gateway advertised routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes).

Each NCC Gateway advertised route that you create is installed in the route tables of the NCC hub to which the NCC Gateway spoke is connected. The gateway itself is the next hop for each route that it advertises.

**Note:** When you configure a gateway advertised route in the gateway spoke, this route is not propagated to the NCC hub route table until there is an active SSE gateway.



### Add regions

If you want to add NCC Gateway spokes and VLAN attachments in other regions, repeat steps 2-5 in the NCC Gateway setup. Adding more connections is optional.

## Manage NCC Gateway

After you have configured NCC Gateway, you can manage the gateway. See the following resources for instructions.

### Hubs

  * [Update the hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update_a_hub)
  * [Delete the hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-hub)



### Spokes

  * [Update the NCC Gateway spoke's capacity](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update-gateway-spoke-capacity)



### Advertised routes

  * [Create and manage NCC Gateway advertised routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes)



### Cloud Routers

  * [Manage Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers)
  * [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details)



You can't change the NCC Gateway linked with the Cloud Router. However, you can change the custom route advertisements. For detailed information about Cloud Router advertised routes, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).

## View gateway spoke routes

To verify the routing path in the gateway, you can view gateway spoke route tables to see how traffic enters and leaves a gateway and where a packet is routed.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. On the **Hub** tab, select the hub. All the spokes attached to that hub are listed.

  4. To view details for a specific NCC Gateway spoke, select a spoke to view the **Spoke details** page.

  5. To view the gateway route table, on the **Spoke details** page, click the **Gateway spoke routes** tab.

  6. Specify the following two filters:

     * **Gateway interface** : Choose from one of the following gateway interface options:

       * **Hybrid attachments**
       * **Other gateway spokes**
       * **Secure Access Connect attachment`sac-name`**, where `sac-name` is the name of the Secure Access Connect attachment used by the NCC Gateway
       * **Hub`hub-name`**, where `hub-name` is the name of the NCC Gateway spoke's hub
     * **Direction** : You can choose one of the following options:

       * For learned routes, choose **Ingress**
       * For advertised routes, choose **Egress**
  7. Click **View**.




## Monitoring

  * [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/viewing-logs-metrics)



## What's next?

  * To learn about NCC Gateway, see [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview).
  * To learn how to configure NCC Gateway, see [NCC Gateway setup overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview).
  * To learn how to configure Secure Access Connect, see [Create a realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms)
  * To find solutions for common issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and gcloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
