---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-hub-route-table/
title: View the hub route table and routes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:02.013530+00:00
---

# View the hub route table and routes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-hub-route-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  View the hub route table and routes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use hub route tables and routes.

When you create a hub and configure it to use mesh topology, a single default hub route table is generated. With star topology, one hub route table _per group_ is generated.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubRouteTables.list` to list hub route tables
  * `networkconnectivity.hubRouteTables.get` to view hub route tables



**Roles**

  * `roles/networkconnectivity.hubAdmin`
  * `roles/networkconnectivity.hubViewer`



### List hub route tables

To get a list of hub route tables, follow these steps.

###  gcloud 

Run the [`gcloud network-connectivity hubs route-tables list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/list).
    
    
    gcloud network-connectivity hubs route-tables list \
        --hub=HUB_NAME
    

Replace `HUB_NAME`with the name of the hub in your project that you want to list the route table for.

###  API 

Use the [`networkconnectivity.hubs.routeTables.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables/list) with an empty request body.
    
    
      GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME/routeTables
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the hub
  * `HUB_NAME`: the name of the hub for which you want to list the hub route table



### View hub route tables

To view details, such as name and description of a Network Connectivity Center (NCC) route table, follow these steps.

###  Console 

  1. In the Google Cloud console, go to **Network Connectivity Center**.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project in which you want to view the hub details.

  3. Click the name of the hub that you want to view the hub route table for.

  4. Click the **Routes** tab.

  5. In the **Region** section, select the region for which you want to view routes.

  6. Follow these steps depending on the topology that your hub is configured for.

     * If you're using mesh topology connectivity, the routes and route details are displayed in the **Routes** section.
     * If you're using star topology connectivity, in the **Routes** section, change the **Spoke group** to **Center** or **Edge** to see the appropriate route table.



###  gcloud 

Run the [`gcloud network-connectivity hubs route-tables describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/describe).
    
    
    gcloud network-connectivity hubs route-tables describe GROUP_NAME \
        --hub=HUB_NAME
    
    

Replace the following:

  * `GROUP_NAME`: the name of the group for which you want to view the hub route table. For mesh topology connectivity, there is a single default group; for star topology connectivity, there is a _center_ or _edge_ group.
  * `HUB_NAME`: the name of the hub for which you want to view the hub route table



###  API 

Use the [`networkconnectivity.hubs.routeTables.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables/get) with an empty request body.
    
    
      GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME/routeTables/NAME
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new hub
  * `HUB_NAME`: the name of the hub for which you want to view the hub route table
  * `NAME`: the name of the hub route table resource



## Manage hub routes

A route resource nested under the hub route table corresponds to a subnet in a VPC spoke that has been exported from the VPC network to the hub.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubRoutes.get` to view hub routes
  * `networkconnectivity.hubRoutes.list` to list hub routes



**Roles**(one of the following):

  * `roles/networkconnectivity.hubAdmin`
  * `roles/networkconnectivity.hubViewer`



### List hub routes

To see a list of hub routes for a specific region, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project in which you want to view the hub route details.

  3. Click the name of the hub that you want to view the route details for.

  4. Click the **Routes** tab.

  5. In the **Region** section, select the region for which you want to view routes. The route table lists both subnet routes and dynamic routes.




###  gcloud 

Run the [`gcloud network-connectivity hubs route-tables routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list).
    
    
    gcloud network-connectivity hubs route-tables routes list \
        --hub=HUB_NAME \
        --route_table=NAME \
        --effective-location=EFFECTIVE_LOCATION
    

Replace the following:

  * `HUB_NAME`: the name of the hub, such as `my-hub`
  * `NAME`: the name of the hub route table, such as `edge-route-table` or `center-route-table`
  * `EFFECTIVE_LOCATION`: the location of the hub for which you want to view routes, such as `us-central1`



###  API 

Use the [`networkconnectivity.hubs.routeTables.routes.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes/list) with an empty request body.
    
    
      GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME/routeTables/NAME/routes
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the hub
  * `HUB_NAME`: the name of the hub
  * `NAME`: the name of the hub route table resource



### View hub route details

To view the details of a specific hub route, such as route type, destination IP address range, and next hop, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project in which you want to view the hub route details.

  3. Click the name of the hub that you want to view the route details for.

  4. Click the **Routes** tab.

  5. Use the **Filter** field to sort routes by type, IP version, destination IP address range, priority, spoke, or next hop.




###  gcloud 

Run the [`gcloud network-connectivity hubs route-tables routes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/describe).
    
    
    gcloud network-connectivity hubs route-tables routes describe NAME \
        --hub=HUB_NAME \
        --route_table=ROUTE_TABLE
    

Replace the following:

  * `NAME`: the name or ID of the route that you want to describe. Query the API to get the exact route name by using the [`gcloud network-connectivity hubs route-tables routes list` command](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-hub-route-table#list_hub_routes).
  * `HUB_NAME`: the name of the hub, such as `my-hub`.
  * `ROUTE_TABLE`: the name of the hub route table, such as `edge-route-table` or `center-route-table` for star topology connectivity and `default-route-table` for full mesh topology.



###  API 

Use the [`networkconnectivity.hubs.routeTables.routes.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes/get).
    
    
      GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME/routeTables/NAME/routes/ROUTE_NAME
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new hub
  * `HUB_NAME`: the name of the hub for which you want to view the hub route table
  * `NAME`: the name of the hub route table resource
  * `ROUTE_NAME`: the name of the route



## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
