---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-route-table/
title: View the VPC route table \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:53.540285+00:00
---

# View the VPC route table  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-view-route-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  View the VPC route table Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view VPC route tables. This page assumes that you are familiar with how to [list routes for a VPC network](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.routes.list`



**Roles**

To find predefined roles that contain those permissions, see [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam). 


## List and describe routes in a VPC spoke

You can use the Google Cloud CLI or the API to list and view details about the following types of routes:

  * [System-generated default routes](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet)
  * [Subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes)
  * [Peering subnet routes](https://docs.cloud.google.com/vpc/docs/routes#peering-subnet-routes)
  * [NCC subnet routes](https://docs.cloud.google.com/vpc/docs/routes#ncc-subnet-routes)
  * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes)



Neither the gcloud CLI commands nor the API methods show the following types of routes:

  * [Policy-based routes](https://docs.cloud.google.com/vpc/docs/routes#policy-based_routes)
  * [Dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes)
  * [Peering static and dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#peering-custom-routes)



To see the complete route view, use the Google Cloud console. To list and describe policy-based routes, see [Use policy-based routes](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes).

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. On the **Effective routes** tab, do the following:

     * Choose a VPC network.
     * Choose a region.
  3. Click **View**.

  4. You can filter on properties including [route type](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes), destination IP range, and [next hop type](https://docs.cloud.google.com/vpc/docs/routes#static-route-next-hops).

  5. Optional: Click the **Show suppressed routes** toggle to the on position to view routes that are suppressed. To view the reason why a route is suppressed, point to the icon in the **Status** column.




###  gcloud 

To list and view details for [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) and [static routes](https://docs.cloud.google.com/vpc/docs/static-routes), use the [`gcloud compute routes` commands](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes). These commands don't show other types of routes. To see all routes, use the Google Cloud console.

To list routes, do the following:
    
    
    gcloud compute routes list \
        --filter="network=NETWORK_NAME" \
        --project=PROJECT_ID
    

To get details for a route, do the following:
    
    
    gcloud compute routes describe ROUTE_NAME \
        --format="flattened()" \
        --project=PROJECT_ID
    

Replace the following:

  * `NETWORK_NAME`: the name of the VPC network
  * `PROJECT_ID`: the project ID that contains your VPC network
  * `ROUTE_NAME`: the name of the route



###  API 

To list and view details for [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) and [static routes](https://docs.cloud.google.com/vpc/docs/static-routes), use the [routes.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/list) and [routes.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/get) methods. These methods don't show other types of routes. To see all routes, use the Google Cloud console.

To list routes, do the following:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes?filter=network="NETWORK_URL
    

To get details for a route, do the following:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes/ROUTE_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID that contains your VPC network
  * `NETWORK_URL`: the URL of the VPC network
  * `ROUTE_NAME`: the name of the route



## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with Network Connectivity Center (NCC), see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
