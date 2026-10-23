---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers/
title: Manage Cloud Routers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:27.435095+00:00
---

# Manage Cloud Routers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage Cloud Routers

This document describes how to list, update, get status of, and delete Cloud Router.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## List Cloud Routers

To list all the Cloud Routers in a project, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. On the **Cloud Routers** page, view a list of your Cloud Routers.




###  gcloud 

Run the `list` command. To restrict the list to only one region, specify `--filter="region:(<var>REGION</var>)`.
    
    
      gcloud compute routers list \
          --project=PROJECT_ID \
          [--filter="region:(REGION)]
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to list Cloud Routers
  * `REGION`: the region for which you want to list routers—for example, `asia-east1`



The output is similar to the following:
    
    
      NAME        REGION       NETWORK
      my-router   asia-east1   my-network
    

###  API 

Use the [`routers.aggregatedList`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/aggregatedList) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/routers
    

Replace `PROJECT_ID` with the ID of the project for which you want to list Cloud Routers.

To list only the Cloud Routers in a specific region, use the [`routers.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/list) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to list Cloud Routers
  * `REGION`: the region for which you want to list Cloud Routers



## Update Cloud Routers

If a Cloud Router is associated with an [NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview), keep the following in mind:

  * You can't update the `ncc_gateway` field.
  * The `patch` or `update` methods don't accept the `network` field as part of the request body.




###  gcloud 

Use the [`gcloud compute routers update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update):
    
    
    gcloud compute routers update ROUTER_NAME
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router that you want to update
  * `REGION`: the region where the Cloud Router resides



###  API 

Use the [`routers.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update) method:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to list Cloud Routers
  * `REGION`: the region where the Cloud Router resides
  * `ROUTER_NAME`: the name of the Cloud Router that you want to update



## Get Cloud Router status

###  gcloud 

Use the [`gcloud compute routers get-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status).
    
    
    gcloud compute routers get-status ROUTER_NAME \
        --project=PROJECT_ID \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router that you want to get the status of
  * `PROJECT_ID`: the project ID that the Cloud Router belongs to
  * `REGION`: the region where the Cloud Router resides



###  API 

Use the [`routers.getRouterStatus`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus) method with an empty request body:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/getRouterStatus
    

Replace the following:

  * `PROJECT_ID`: the project ID that the Cloud Router belongs to
  * `REGION`: the region where the Cloud Router resides
  * `ROUTER_NAME`: the name of the Cloud Router that you want to get the status of



## Delete Cloud Routers

Before you delete a Cloud Router, check that it isn't being used by another resource, such as a Cloud VPN tunnel or a VLAN attachment. You must delete the associated resource before you can delete the Cloud Router. However, you aren't required to remove BGP sessions before you delete the Cloud Router.

**Warning:** Deleting a Cloud Router deletes any Cloud NAT gateways that are associated with the Cloud Router.

To delete the Cloud Router, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the checkbox next to the Cloud Router that you want to delete.

  3. Click delete**Delete**.




###  gcloud 

Run the `delete` command. Specify the name and location of the Cloud Router that you want to delete.
    
    
    gcloud compute routers delete ROUTER_NAME \
        --project=PROJECT_ID \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router that you want to delete

  * `PROJECT_ID`: the ID of the project that contains the Cloud Router that you want to delete

  * `REGION`: the region in which the Cloud Router is located




The output is similar to the following:
    
    
    Deleted [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/asia-east1/routers/ROUTER_NAME].
    

###  API 

Use the [`routers.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the Cloud Router that you want to delete
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router



## What's next

  * To view the configuration of a Cloud Router, its BGP sessions, and the routes that Cloud Router is advertising, see [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).
  * To troubleshoot issues when using Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
