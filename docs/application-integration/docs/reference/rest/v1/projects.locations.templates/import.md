---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.templates/import/
title: Method: projects.locations.templates.import \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:28.964630+00:00
---

# Method: projects.locations.templates.import  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.templates/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  Method: projects.locations.templates.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Import the template to an existing integration. This api would keep track of usageCount and lastUsedTime. PERMISSION_DENIED would be thrown if template is not accessible by client.

### HTTP request

`POST https://integrations.googleapis.com/v1/{name=projects/*/locations/*/templates/*}:import`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name that is associated with the Template.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "integration": string,
      "subIntegrations": {
        string: {
          object ([IntegrationDetails](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationDetails))
        },
        ...
      }
    }  
  
Fields  
---  
`integration` |  `string` Required. Resource name of the integration where template needs to be imported/inserted.  
`subIntegrations` |  `map (key: string, value: object (`[IntegrationDetails](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationDetails)`))` Optional. Sub Integration which would be created via templates.  
  
### Response body

Response for import template

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "integrationVersion": {
        object ([IntegrationVersion](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions#IntegrationVersion))
      },
      "subIntegrationVersions": [
        {
          object ([IntegrationVersion](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions#IntegrationVersion))
        }
      ]
    }  
  
Fields  
---  
`integrationVersion` |  `object (`[IntegrationVersion](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions#IntegrationVersion)`)` IntegrationVersion after the import.  
`subIntegrationVersions[]` |  `object (`[IntegrationVersion](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions#IntegrationVersion)`)` Sub integration versions which are imported.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `integrations.templates.use`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
