---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/zones/
title: Manage zones \u00a0|\u00a0 Google Distributed Cloud connected, version 1.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:06.478223+00:00
---

# Manage zones  |  Google Distributed Cloud connected, version 1.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/zones/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/overview)



Send feedback 

#  Manage zones Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Google Distributed Cloud connected zone resources in a Distributed Cloud connected deployment. Due to the structuring of Google Cloud APIs, Distributed Cloud connected zone resources are referred to as _locations_ in the Distributed Cloud Edge Container API.

For more information about Distributed Cloud connected zones, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

## List zones

To list the Distributed Cloud connected zone in your Google Cloud project, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the **Edge Zones** page.

[Go to Edge Zones](https://console.cloud.google.com/distributed-cloud/edgezones/list)

  2. Examine the list of zones and their details.




###  gcloud 

Use the `gcloud edge-cloud container zones list` command:
    
    
    gcloud edge-cloud container zones list \
        --project=PROJECT_ID
     

Replace `PROJECT_ID` with the ID of the target Google Cloud project.

###  API 

Make a `GET` request to the `projects.locations.list` method:
    
    
    GET /v1/PROJECT_ID/locations?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Initialize the network configuration of a zone

To initialize the network configuration of a Distributed Cloud connected zone, complete the steps in this section.

Before you can initialize the network configuration of a zone, you must first [enable the Distributed Cloud Edge Network API](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/networking#network-api-enable).

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

You must initialize the network configuration of each of your Distributed Cloud connected zones in the following cases:

  * Immediately after your Distributed Cloud connected hardware is installed on your premises.
  * You upgraded to Distributed Cloud connected version 1.3.0 on an existing Distributed Cloud connected deployment but did not participate in the private preview of the Distributed Cloud Edge Network API.



Initializing the network configuration of a zone creates a default router named `default`. The `default` router is then configured to peer with all of the interconnects that you requested when you ordered the Distributed Cloud connected hardware by creating corresponding interconnect attachments. This provides your Distributed Cloud connected deployment with basic uplink connectivity to your local network.

This is a run-once procedure. Subsequent runs do not alter your existing Distributed Cloud networking settings.

###  gcloud 

Use the `gcloud edge-cloud networking zones init` command:
    
    
    gcloud edge-cloud networking zones init ZONE_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.



###  API 

Make a `POST` request to the `projects.locations.zones.initialize` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME:init
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



## Get information about a zone

To get information about a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the **Edge Zones** page.

[Go to Edge Zones](https://console.cloud.google.com/distributed-cloud/edgezones/list)

  2. Click the desired zone.

The Google Cloud console displays detailed information about the selected zone.




###  gcloud 

Use the `gcloud edge-cloud container zones describe` command:
    
    
    gcloud edge-cloud container zones describe ZONE_NAME \
        --project=PROJECT_ID
    

Replace the following:

  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `PROJECT_ID`: the ID of the target Google Cloud project.



###  API 

Make a `GET` request to the `projects.locations.get` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.



## What's next

  * [Deploy workloads on Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/deploy)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/machines)
  * [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/clusters)
  * [Create and manage networks](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/networks)
  * [Create and manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/nodepools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
