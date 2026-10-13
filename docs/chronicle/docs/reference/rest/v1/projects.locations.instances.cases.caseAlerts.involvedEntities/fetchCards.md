---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards/
title: Method: involvedEntities.fetchCards \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:21.280915+00:00
---

# Method: involvedEntities.fetchCards  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: involvedEntities.fetchCards Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * InvolvedEntityCard
    * JSON representation
  * SecurityEntityDirection



**Full name** : projects.locations.instances.cases.caseAlerts.involvedEntities.fetchCards

Returns metadate of each involved entity in a specific alert, including their connectivity and high-level status. Use this method to populate visual graphs or high-level summaries of an investigation scope.

### HTTP request

`GET https://{endpoint}/v1/{parent}/involvedEntities:fetchCards`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{caseAlert}/involvedEntities:fetchCards  
  
### Request body

The request body must be empty.

### Response body

Response message for FetchCards.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "cards": [
        {
          object ([InvolvedEntityCard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards#InvolvedEntityCard))
        }
      ]
    }  
  
Fields  
---  
`cards[]` |  `object (`[InvolvedEntityCard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards#InvolvedEntityCard)`)` Required. The list of cards.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.involvedEntities.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## InvolvedEntityCard

Involved entity card.

JSON representation  
---  
      
    
    {
      "identifier": string,
      "type": string,
      "linkedEntities": [
        {
          object ([InvolvedEntityCard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards#InvolvedEntityCard))
        }
      ],
      "suspicious": boolean,
      "direction": enum ([SecurityEntityDirection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards#SecurityEntityDirection))
    }  
  
Fields  
---  
`identifier` |  `string` Required. The identifier of the entity.  
`type` |  `string` Required. The type of the entity.  
`linkedEntities[]` |  `object (`[InvolvedEntityCard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards#InvolvedEntityCard)`)` Required. Involved entity card.  
`suspicious` |  `boolean` Required. Is the entity suspicious.  
`direction` |  `enum (`[SecurityEntityDirection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards#SecurityEntityDirection)`)` Required. Security entity direction.  
  
## SecurityEntityDirection

Security entity direction.

Enums  
---  
`NONE` | Unspecified security entity direction.  
`INBOUND` | Inbound security entity direction.  
`OUTBOUND` | Outbound security entity direction.  
`BOTH` | Both inbound and outbound security entity direction.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
