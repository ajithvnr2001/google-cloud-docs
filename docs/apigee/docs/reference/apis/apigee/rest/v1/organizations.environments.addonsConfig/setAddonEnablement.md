---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.addonsConfig/setAddonEnablement/
title: Method: organizations.environments.addonsConfig.setAddonEnablement \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:47.011736+00:00
---

# Method: organizations.environments.addonsConfig.setAddonEnablement  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.addonsConfig/setAddonEnablement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.addonsConfig.setAddonEnablement Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates an add-on enablement status of an environment.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/environments/*/addonsConfig}:setAddonEnablement`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the add-ons config. Must be in the format of `/organizations/{org}/environments/{env}/addonsConfig`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field addon_enablement can be only one of the following:
      "analyticsEnabled": boolean,
      "apiSecurityEnabled": boolean
      // End of list of possible types for union field addon_enablement.
    }  
  
Fields  
---  
Union field `addon_enablement`. Boolean flags manage add-ons enablement status. `addon_enablement` can be only one of the following:  
`analyticsEnabled` |  `boolean` If the Analytics should be enabled in the environment.  
`apiSecurityEnabled` |  `boolean` If the API Security should be enabled in the environment.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
