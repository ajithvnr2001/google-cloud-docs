---
url: https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview/
title: API observations in API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:47.251703+00:00
---

# API observations in API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API observations in API hub Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

**Preview — API observations**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **API observations** feature in API hub helps you address the challenges of undocumented and unmanaged APIs, also known as _shadow APIs_ , which can introduce significant security and governance risks in your API infrastructure. Evolving from the [Shadow API Discovery](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery) feature in Apigee, API observations in API hub uses automated discovery processes to find and catalog all your APIs—both known and unknown—into a single, unified, and managed view. 

**Note:** API observations in API hub relies on the Apigee Shadow API Discovery feature, which is included as part of the paid Apigee [Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-security). This means you can incur charges related to your Apigee usage. See pricing and billing for more information. 

## How API observations works

API observations provides a comprehensive and continuously updated view of your API infrastructure. It works by automatically finding and cataloging undocumented or unmanaged APIs through the analysis of network traffic within your ingested data sources. This process of discovering and observing APIs is referred to as an _API observation_. 

The process of discovering and observing an API is referred to as an _observation_. An API observation is the result of combining API signals to represent a detected API endpoint and its operations. It's important to note that an API observation is not a complete API definition; it can represent one or more potential APIs depending on the scope of the observed endpoint. Once detected, these discovered API observations are automatically sent to and cataloged in API hub, creating a single, searchable catalog of all your APIs. 

## Enable API observations in API hub

To use API observations in API hub, you must first associate your desired API assets or data sources with API hub. You can do this while attaching Apigee runtime projects to API hub. For more information, see [Configure API observations in API hub](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-observation).

API observations in API hub relies on the Apigee Shadow API Discovery feature, which is included as part of the paid Apigee [Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-security). This means that in order to use API observations in API hub, you must also have the Advanced API Security add-on enabled for your Apigee organization. The Advanced API Security add-on is available for Google Cloud projects with or without Apigee provisioning: 

  * For subscription customers, the Advanced API Security add-on is available with the Apigee organization. See [Manage Advanced API Security for Subscription organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-subscription-organizations).
  * For pay-as-you-go customers, the add-on must be enabled for at least one Apigee environment. See [Manage Advanced API Security for Pay-as-you-go organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-pay-as-you-go-organizations).
  * For Google Cloud projects not provisioned for Apigee, you can enable the Advanced API Security add-on by contacting [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).
  * Shadow API Discovery is not available for Apigee evaluation environments.



### Supported data sources

API observations in API hub supports the following data source: 

Data source | How to enable | Description  
---|---|---  
**Apigee** | Attach Apigee runtime projects to API hub |  When you attach an Apigee runtime project to API hub, it automatically imports [Apigee API observation jobs](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery#create-observation-jobs) from that project. APIs discovered by these jobs are then analyzed and compared to documented APIs in API hub. If an API is a match, it is cataloged. If no match is found, the API is marked as **unknown**.   
  
## Discovered API observations

The **API observations** page in API hub displays a list of all detected APIs from all associated data sources, including both known and unknown APIs. For each discovered API observation, the following details are collected and displayed: 

  * **Hostname** : the hostname of the data source from which the API observation was collected.
  * **Observations** : the total number of API operations, categorized as known and unknown, for the observation.
  * **Server IPs** : a comma-separated list of all observed IP addresses.
  * **Source Type** : the primary data source from which the observation was collected.
  * **Project ID** : the Google Cloud project ID associated with the observation.
  * **Source Locations** : a comma-separated list of all the geographical locations where the observation was detected.
  * **Observed By** : the name and location of the Apigee API Observation job that initially detected the observation (this column is only available if the source is from Apigee). 
  * **Last Event Detected (UTC)** : the timestamp (in UTC) of the most recent detection of the discovered API observation

Discovered API observations in API hub

## IAM roles and permissions

To use API observations in API hub, you need the following IAM roles and permissions: 

IAM roles | Permissions  
---|---  
**API Management Admin (`roles/apim.admin`)** | 

  * apim.operations.delete
  * apim.operations.cancel
  * apim.observationSources.create
  * apim.observationSources.delete
  * apim.observationJobs.create
  * apim.observationJobs.enable
  * apim.observationJobs.disable
  * apim.observationJobs.delete
  * apim.apiObservations.batchEditTags

  
**API Management Viewer (`roles/apim.viewer`)** | 

  * resourcemanager.projects.get
  * resourcemanager.projects.list
  * apim.operations.list
  * apim.operations.get
  * apim.locations.list
  * apim.locations.get
  * apim.locations.listApiObservationTags
  * apim.observationSources.list
  * apim.observationSources.get
  * apim.observationJobs.list
  * apim.observationJobs.get
  * apim.apiObservations.list
  * apim.apiObservations.get
  * apim.apiOperations.list
  * apim.apiOperations.get
  * apim.entitlements.get

  
**Provisioning Admin Role (`roles/apihub.provisioningAdmin`)** | 

  * apihub.runtimeProjectAttachments.create
  * apihub.hostProjects.attach

  
**Viewer Role (`roles/apihub.viewer`)** | 

  * apihub.discoveredObservations.list
  * apihub.discoveredObservations.get
  * apihub.discoveredOperations.list
  * apihub.discoveredOperations.get

  
  
## Pricing and billing

The API observations feature in API hub is provided at no direct cost. However, since API observations in API hub leverages Shadow API discovery, which is part of the Apigee Advanced API Security add-on, you can incur charges related to your Apigee usage. While the feature itself doesn't have direct costs, the discovery and observation process can involve data processing from your existing Apigee runtime projects, which can incur charges or hit quota limits. 

For more information, see [Shadow API Discovery](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery). 

## What's next

  * [Configure API observations in API hub](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-observation).
  * [Manage API observations](https://docs.cloud.google.com/apigee/docs/apihub/manage-api-observations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
