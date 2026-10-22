---
url: https://docs.cloud.google.com/monitoring/api/enable-api/
title: Enable the Monitoring API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:31.592292+00:00
---

# Enable the Monitoring API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/enable-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Enable the Monitoring API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and authorize use of the Monitoring API v3. You must enable this API before you can use it.

## Enable the Monitoring API

To enable the Monitoring API, use either the Google Cloud console or the Google Cloud CLI.

###  Console 

Enable the Cloud Monitoring API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)

###  gcloud 

Enable the Cloud Monitoring API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable monitoring.googleapis.com

## Authorize use of the Monitoring API

Access to the Monitoring API is controlled by Identity and Access Management (IAM) roles and permissions. There is a permission associated with each method, and permissions for related methods are clustered into roles, which can then be granted to users. For more information, see [Control access with IAM](https://docs.cloud.google.com/monitoring/access-control).

After access to an API is authorized, the API can be used from anywhere. For example, you can call the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method from your local workstation. You can also use the API to send metrics against any entity that can be represented as a monitored resource. See [Monitored-resource types for user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics#which-resource) for the list of available types.

If you are writing an application that uses the recommended [client libraries](https://docs.cloud.google.com/monitoring/docs/reference/libraries), these libraries authorize your application by using [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/production).

You might also be able to use API keys in some situations, but service accounts are generally recommended. API keys are useful in clients like browsers and mobile applications that don't have a backend server. For more information, see [Using API Keys](https://docs.cloud.google.com/docs/authentication/api-keys).

You can find out more about authentication and authorization in our [Authentication guide](https://docs.cloud.google.com/docs/authentication/getting-started).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
