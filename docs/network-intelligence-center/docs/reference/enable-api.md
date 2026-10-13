---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/enable-api/
title: Enable the Network Management API \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:22.687455+00:00
---

# Enable the Network Management API  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/enable-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Enable the Network Management API Stay organized with collections  Save and categorize content based on your preferences. 

Before you can run Connectivity Tests or configure VPC Flow Logs, you must enable the Network Management API.

Enabling the API is required in order to use the API itself, the Google Cloud CLI, or the Google Cloud console.

You can check API status or enable the API by using a `gcloud` command or by using the Google Cloud console. You can also authorize users to access the API.

## Enable the API

Use one of the following methods to enable the API.

### Console

When you load Connectivity Tests or VPC Flow Logs in the Google Cloud console for the first time for a specific project. To enable the API click **Enable Network Management API**.

###  gcloud 

  1. If you have not already installed the Google Cloud CLI on your workstation, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/docs) to do so.

  2. To check if the Network Management API is enabled, run the following command on your workstation:
         
         gcloud services list
         

If `networkmanagement.googleapis.com` appears in the command output, the API is enabled.

  3. If the API is not enabled, run the following command to enable it. For more information, see [`gcloud services`](https://docs.cloud.google.com/sdk/gcloud/reference/services).
         
         gcloud services enable networkmanagement.googleapis.com
         




## Authorize use of the API

Access to the Network Management API is controlled by Identity and Access Management roles and permissions. Permissions for related methods are clustered into roles, which you can then grant to users.

For more information, see the following documents:

  * [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control)
  * [Managing access control for Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-access-control)



## Use the API Explorer

You can test Network Management API commands by using the API Explorer. In the Network Management API reference document, use the `Try this API` column to explore API fields and [run a test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
