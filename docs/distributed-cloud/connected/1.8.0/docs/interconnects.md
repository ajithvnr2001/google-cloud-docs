---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/interconnects/
title: Manage interconnects \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:39.658472+00:00
---

# Manage interconnects  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/interconnects/

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
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/overview)



Send feedback 

#  Manage interconnects Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Google Distributed Cloud interconnect resources in a Distributed Cloud connected zone.

This functionality is only available on Distributed Cloud connected racks. Distributed Cloud connected servers don't support interconnect resources.

For more information about Distributed Cloud interconnects, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/how-it-works#networking).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

## List interconnects

To list the Distributed Cloud interconnects in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects list` command:
    
    
    gcloud edge-cloud networking interconnects list \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



###  API 

Make a `GET` request to the `projects.locations.zones.interconnects.list` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/interconnects?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about an interconnect

To get information about a Distributed Cloud interconnect in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects describe` command:
    
    
    gcloud edge-cloud networking interconnects describe INTERCONNECT_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `INTERCONNECT_NAME`: the name of the target interconnect.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



###  API 

Make a `GET` request to the `projects.locations.zones.interconnects.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/interconnects/INTERCONNECT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `INTERCONNECT_ID`: the ID of the target interconnect.



## Get the operational status of an interconnect

To get the operational status of a Distributed Cloud interconnect in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects get-diagnostics` command:
    
    
    gcloud edge-cloud networking interconnects get-diagnostics INTERCONNECT_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `INTERCONNECT_NAME`: the name of the target interconnect.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



###  API 

Make a `GET` request to the `projects.locations.zones.interconnects.diagnose` method:
    
    
     GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/interconnects/INTERCONNECT_ID:diagnose
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `INTERCONNECT_ID`: the ID of the target interconnect.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/deploy)
  * [Manage interconnect attachments](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/attachments)
  * [Manage networks](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/networks)
  * [Manage routers](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/routers)
  * [Manage subnetworks](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/subnetworks)
  * [Manage VPN connections](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/vpn-connections)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/zones)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
