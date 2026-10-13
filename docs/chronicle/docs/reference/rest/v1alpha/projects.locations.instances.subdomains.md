---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.subdomains
title: REST Resource: projects.locations.instances.subdomains \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:26.145248+00:00
---

# REST Resource: projects.locations.instances.subdomains  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.subdomains

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.subdomains Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Subdomain
    * JSON representation
  * Methods



## Resource: Subdomain

A Subdomain represents a frontend path configured for a Chronicle instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "workforcePoolProvider": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of this subdomain. Format: `projects/{project}/locations/{location}/instances/{instance}/subdomains/{subdomain}`  
`workforcePoolProvider` |  `string` Required. The workforce pool provider connected to the subdomain. Format: `locations/{location}/workforcePools/{workforcePoolId}/providers/{providerId}`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.subdomains/create)`

|  Creates a Subdomain.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.subdomains/delete)`

|  Deletes a Subdomain.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.subdomains/get)`

|  Gets a Subdomain.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.subdomains/list)`

|  Lists Subdomains for a given instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
