---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes/
title: Create and manage NCC Gateway advertised routes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:51:44.197483+00:00
---

# Create and manage NCC Gateway advertised routes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Create and manage NCC Gateway advertised routes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure _NCC Gateway advertised routes_. Each NCC Gateway advertised route is installed in each region of the NCC hub route table with a next hop being the NCC Gateway spoke. The [standard best path selection mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#standard-best-path-mode) determines the priority of each NCC Gateway advertised route. NCC Gateway advertised routes provide paths that resources in other spokes of the hub use to send packets to the corresponding NCC Gateway.

When you configure a gateway advertised route in the gateway spoke, this route is not propagated to the NCC hub route table until there is an active SSE gateway.

**Note:** NCC Gateway advertised routes are different from Cloud Router advertised routes, including any Cloud Router advertised routes on Cloud Routers that are associated with the NCC Gateway spoke. Cloud Router advertised routes provide paths that on-premises resources use to send packets to the NCC Gateway. For information about Cloud Router advertised routes, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) in the Cloud Router documentation.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.gatewayAdvertisedRoutes.create` to create a hub
  * `networkconnectivity.gatewayAdvertisedRoutes.create` to create an advertised route
  * `networkconnectivity.gatewayAdvertisedRoutes.update` to update advertised routes
  * `networkconnectivity.gatewayAdvertisedRoutes.delete` to delete advertised routes
  * `networkconnectivity.gatewayAdvertisedRoutes.get` to get advertised routes
  * `networkconnectivity.gatewayAdvertisedRoutes.list` to list advertised routes
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`)
  * [Hub & Spoke Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubViewer`)



## Create NCC Gateway advertised routes

To create routes for traffic from the VPC networks to the NCC Gateway, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. On the **Spokes** page, click the spoke for which you want to add NCC Gateway advertised routes.

  5. On the **Spoke details** page, in the **Routes advertised from NCC Gateway to hub** section, click **Add routes**.

  6. In the **Add routes** dialog, do the following:

     * In the **Route name** field, enter a name for the route.
     * In the **IP range** field, enter the destination IP address range of the NCC Gateway advertised route.
     * In the **Priority** field, enter the priority for the advertised route. The default value is 0.
  7. To add more routes, click **Add route** and enter the information in the previous step.

  8. Click **Create**.




###  gcloud 

Use the [`gcloud network-connectivity spokes gateways advertised-routes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/gateways/advertised-routes/create):
    
    
    gcloud network-connectivity spokes gateways advertised-routes create ROUTE_NAME \
        --region=REGION \
        --project=PROJECT \
        --spoke=SPOKE_NAME \
        --ip-range=IP_RANGE \
        --priority=PRIORITY \
        --advertise-to-hub
    

Replace the following:

  * `ROUTE_NAME`: the name for the NCC Gateway advertised route that you want to create
  * `REGION`: the region that contains the NCC Gateway
  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke
  * `IP_RANGE`: the destination IP address range of the NCC Gateway advertised route
  * `PRIORITY`: the priority for the advertised route. The default value is 0



###  API 

Use the [`projects.locations.spokes.gatewayAdvertisedRoutes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/create) with the IP address range and priority specified:
    
    
    POST https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT/locations/REGION/spokes/SPOKE_NAME/gatewayAdvertisedRoutes
    {
    "ip_range": "IP_RANGE",
    "priority": "PRIORITY",
    "recipient": "ADVERTISE_TO_HUB",
    }
    

Replace the following:

  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `REGION`: the region that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke
  * `IP_RANGE`: the destination IP address range of the NCC Gateway advertised route.
  * `PRIORITY`: the priority for the advertised route. The default value is 0



## Update gateway advertised routes

The only attribute that you can change on an existing NCC Gateway advertised route is its priority. To change the priority of an advertised route, follow these steps.

###  API 

Use the [`projects.locations.spokes.gatewayAdvertisedRoutes.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/patch):
    
    
    POST https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT/locations/REGION/spokes/SPOKE_NAME/gatewayAdvertisedRoutes/ROUTE_NAME
    {
    "priority": PRIORITY
    }
    

Replace the following:

  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `REGION`: the region that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke
  * `ROUTE_NAME`: the name of the NCC Gateway advertised route
  * `PRIORITY`: the new priority for the advertised route



## Get details of a gateway advertised route

You can get details of an NCC Gateway advertised route by following these steps:

###  gcloud 

Use the [`gcloud beta network-connectivity spokes gateways advertised-routes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/gateways/advertised-routes/describe):
    
    
    gcloud beta network-connectivity spokes gateways advertised-routes describe ROUTE_NAME \
        --region=REGION \
        --project=PROJECT \
        --spoke=SPOKE_NAME
    

Replace the following:

  * `ROUTE_NAME`: the name of the NCC Gateway advertised route
  * `REGION`: the region that contains the NCC Gateway
  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke



###  API 

Use the [`projects.locations.spokes.gatewayAdvertisedRoutes.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/get) with an empty request body:
    
    
    GET https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT/regions/REGION/spokes/SPOKE_NAME/gatewayAdvertisedRoutes/ROUTE_NAME
    

Replace the following:

  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `REGION`: the region that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke
  * `ROUTE_NAME`: the name of the NCC Gateway advertised route



## View a list of gateway advertised routes

You can view a list of NCC Gateway advertised routes by following these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project the spoke resides in.

  3. In the **Spoke name** column, click the NCC Gateway spoke for which you want to view the gateway advertised route.

  4. The **Spoke details** page lists **Routes advertised from NCC Gateway to hub**.




###  gcloud 

Use the [`gcloud beta network-connectivity spokes gateways advertised-routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/gateways/advertised-routes/list):
    
    
    gcloud beta network-connectivity spokes gateways advertised-routes list \
        --region=REGION \
        --project=PROJECT \
        --spoke=SPOKE_NAME
    

Replace the following:

  * `REGION`: the region that contains the NCC Gateway
  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke



###  API 

Use the [`projects.locations.spokes.gatewayAdvertisedRoutes.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/list) with an empty request body:
    
    
    LIST https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT/regions/REGION/spokes/SPOKE_NAME/gatewayAdvertisedRoutes
    

Replace the following:

  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `REGION`: the region that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke



## Delete a gateway advertised route

You can delete an NCC Gateway advertised route by following these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. On the **Spokes** page, click the spoke for which you want to add NCC Gateway advertised routes.

  5. On the **Spoke details** page, in the **Routes advertised from NCC Gateway to hub** section, click the routes that you want to delete.

  6. Click **Delete routes**.




###  gcloud 

Use the [`gcloud beta network-connectivity spokes gateways advertised-routes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/gateways/advertised-routes/delete):
    
    
    gcloud beta network-connectivity spokes gateways advertised-routes delete ROUTE_NAME \
      --region=REGION \
      --project=PROJECT \
      --spoke=SPOKE_NAME
    

Replace the following:

  * `ROUTE_NAME`: the name of the NCC Gateway advertised route that you want to delete
  * `REGION`: the region that contains the NCC Gateway
  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke



###  API 

Use the [`projects.locations.spokes.gatewayAdvertisedRoutes.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/delete) with an empty request body:
    
    
    DELETE https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT/regions/REGION/spokes/SPOKE_NAME/gatewayAdvertisedRoutes/ROUTE_NAME
    

Replace the following:

  * `PROJECT`: the ID of the project that contains the NCC Gateway
  * `REGION`: the region that contains the NCC Gateway
  * `SPOKE_NAME`: the name of the gateway spoke
  * `ROUTE_NAME`: the name of the NCC Gateway advertised route that you want to delete



## What's next

  * To learn about NCC Gateway, see [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview).
  * To learn how to configure NCC Gateway, see [NCC Gateway setup overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/setup-overview).
  * To find solutions for common issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and Google Cloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



[ Previous arrow_back  Add VLAN attachments  ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
