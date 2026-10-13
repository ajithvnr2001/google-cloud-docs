---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks
title: REST Resource: projects.locations.instances.soarNetworks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:15.881829+00:00
---

# REST Resource: projects.locations.instances.soarNetworks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.soarNetworks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SoarNetwork
    * JSON representation
  * Methods



## Resource: SoarNetwork

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Allows a customer to add, modify and delete networks in a CIDR format. The system supports identification of soarNetwork subnets.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "address": string,
      "environmentsJson": string,
      "priority": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the SoarNetwork. Format: projects/{project}/locations/{location}/instances/{instance}/soarNetworks/{soarNetwork}  
`displayName` |  `string` Required. SoarNetwork name, limited to 4096 characters.  
`address` |  `string` Required. Subnet in CIDR format.  
`environmentsJson` |  `string` Required. SoarNetwork associated logical environments.  
`priority` |  `integer` Optional. SoarNetwork priority.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/create)`

|  Creates a new `SoarNetwork`.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/delete)`

|  Deletes a single SoarNetwork.  
  
### `[deleteAll](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/deleteAll)`

|  Deletes all SoarNetworks within an instance.  
  
### `[export](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/export)`

|  Exports all `SoarNetworks` to a CSV file.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/get)`

|  Gets a single `SoarNetwork`.  
  
### `[import](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/import)`

|  Imports `SoarNetworks` from a CSV file.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/list)`

|  Lists SoarNetworks.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.soarNetworks/patch)`

|  Updates an existing SoarNetwork.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-20 UTC."],[],[]] 
