---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/machines/
title: Manage machines \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:19.237538+00:00
---

# Manage machines  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/machines/

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
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Manage machines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Google Distributed Cloud machine resources in a Distributed Cloud connected zone.

For more information about Distributed Cloud connected machines, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

## List machines in a zone

To list the Distributed Cloud connected machines in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the **Edge Zones** page. 

[Go to Edge Zones](https://console.cloud.google.com/distributed-cloud/edgezones/list)

  2. Click the desired zone.

The Google Cloud console displays detailed information about the selected zone, including a list of machines present in that zone.




###  gcloud 

Use the `gcloud edge-cloud container machines list` command:
    
    
    gcloud edge-cloud container machines list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.



###  API 

Make a `GET` request to the `projects.locations.machines.list` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a machine

To get information about a Distributed Cloud connected machine in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  Console 

  1. In the Google Cloud console, go to the **Edge Zones** page. 

[Go to Edge Zones](https://console.cloud.google.com/distributed-cloud/edgezones/list)

  2. Click the desired zone.

The Google Cloud console displays detailed information about the selected zone, including a list of machines present in that zone.

  3. In the list of machines, click the desired machine.

The Google Cloud console displays detailed information about the selected machine.




###  gcloud 

Use the `gcloud edge-cloud container machines describe` command:
    
    
    gcloud edge-cloud container machines describe MACHINE_ID \
        --location=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `MACHINE_ID`: the ID of the target machine resource.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud zone has been created.
  * `PROJECT_ID`: the ID of the target Google Cloud project.



###  API 

Make a `GET` request to the `projects.locations.machines.get` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION/machines/MACHINE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
  * `MACHINE_NAME`: the name of the target machine resource.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/zones)
  * [Manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/clusters)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/nodepools)
  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/virtual-machines)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/gpu)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
