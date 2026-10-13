---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/
title: REST Resource: allowlistedDomains \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:44.949139+00:00
---

# REST Resource: allowlistedDomains  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: allowlistedDomains Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: AllowlistedDomain

This resource object defines a domain that has been designated as allowlisted.

JSON representation  
---  
      
    
    {
      "name": string,
      "domain": string,
      "customer": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Resource name of the domain in the allowlist e.g. "allowlistedDomains/0184mhaj1smlusv"  
`domain` |  `string` Required. Immutable. Name of the domain that is in the allowlist. e.g. "google.com"  
`customer` |  `string` Immutable. Customer to which domain allowlist belongs to. The value is in the format 'customers/{customerId}'. The customerId must begin with "C". To find your customer ID in Admin Console see <https://support.google.com/a/answer/10070793>.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/create)`

|  Adds a domain to the allowlist.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/delete)`

|  Removes a domain from the allowlist.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/get)`

|  Retrieves a specific domain from the allowlist.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/list)`

|  Lists the domains in the allowlist.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
