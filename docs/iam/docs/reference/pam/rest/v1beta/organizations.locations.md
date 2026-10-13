---
url: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations
title: REST Resource: organizations.locations \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:41.031564+00:00
---

# REST Resource: organizations.locations  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: organizations.locations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Location
    * JSON representation
  * Methods



## Resource: Location

A resource that represents a Google Cloud location.

JSON representation  
---  
      
    
    {
      "name": string,
      "locationId": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"`  
`locationId` |  `string` The canonical id for this location. For example: `"us-east1"`.  
`displayName` |  `string` The friendly name for this location, typically a nearby city name. For example, "Tokyo".  
`labels` |  `map (key: string, value: string)` Cross-service attributes for the location. For example
    
    
    {"cloud.googleapis.com/region": "us-east1"}
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`metadata` |  `object` Service-specific metadata. For example the available capacity at the given location.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Methods  
  
---  
  
### `[checkOnboardingStatus](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations/checkOnboardingStatus)`

|  `CheckOnboardingStatus` reports the onboarding status for a project, folder, or organization.  
  
### `[fetchEffectiveSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations/fetchEffectiveSettings)`

|  `FetchEffectiveSettings` returns the effective PAM Settings for the given project, folder, or organization.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations/get)`

|  Gets information about a location.  
  
### `[getSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations/getSettings)`

|  `GetSettings` returns the PAM Settings for the given project, folder, or organization.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations/list)`

|  Lists information about the supported locations for this service.  
  
### `[updateSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/organizations.locations/updateSettings)`

|  `UpdateSettings` updates the PAM Settings resource specified in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-26 UTC."],[],[]] 
