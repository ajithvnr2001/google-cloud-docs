---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess/
title: Method: consentStores.checkDataAccess \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:02.203719+00:00
---

# Method: consentStores.checkDataAccess  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: consentStores.checkDataAccess Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.consentStores.checkDataAccess

Checks if a particular dataId of a `[User data mapping](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.userDataMappings#UserDataMapping)` in the specified `[consent store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore)` is consented for the specified use.

### HTTP request

`POST https://healthcare.googleapis.com/v1/{consentStore=projects/*/locations/*/datasets/*/consentStores/*}:checkDataAccess`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`consentStore` |  `string` Required. Name of the consent store where the requested dataId is stored, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/consentStores/{consentStoreId}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `consentStore`:

  * `healthcare.consentStores.checkDataAccess`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataId": string,
      "requestAttributes": {
        string: string,
        ...
      },
      "responseView": enum([ResponseView](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess#ResponseView)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "consentList": {
        object([ConsentList](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/ConsentList))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`dataId` |  `string` Required. The unique identifier of the resource to check access for. This identifier must correspond to a User data mapping in the given consent store.  
`requestAttributes` |  `map (key: string, value: string)` The values of request attributes associated with this access request.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`responseView` |  `enum(`[ResponseView](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess#ResponseView)`)` Optional. The view for `[CheckDataAccessResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess#body.CheckDataAccessResponse)`. If unspecified, defaults to `BASIC` and returns `consented` as `TRUE` or `FALSE`.  
The selection of `[Consents](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents#Consent)` to evaluate the access request against. If no selection is specified, the access request is evaluated against all `ACTIVE` unexpired Consents with the same `user_id` as the data to check access for. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`consentList` |  `object(`[ConsentList](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/ConsentList)`)` Optional. Specific `[Consents](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents#Consent)` to evaluate the access request against. These Consents must have the same `userId` as the evaluated User data mapping, must exist in the current `consentStore`, and have a `state` of either `ACTIVE` or `DRAFT`. A maximum of 100 Consents can be provided here. If no selection is specified, the access request is evaluated against all `ACTIVE` unexpired Consents with the same `userId` as the evaluated User data mapping.  
End of mutually exclusive fields.  
  
### Response body

Checks if a particular dataId of a `[User data mapping](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.userDataMappings#UserDataMapping)` in the given `[consent store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore)` is consented for a given use.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consented": boolean,
      "consentDetails": {
        string: {
          object([ConsentEvaluation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/ConsentEvaluation))
        },
        ...
      }
    }  
  
Fields  
---  
`consented` |  `boolean` Whether the requested resource is consented for the given use.  
`consentDetails` |  `map (key: string, value: object(`[ConsentEvaluation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/ConsentEvaluation)`))` The resource names of all evaluated `[Consents](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents#Consent)` mapped to their evaluation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ResponseView

The supported views for `[CheckDataAccessResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess#body.CheckDataAccessResponse)`.

Enums  
---  
`RESPONSE_VIEW_UNSPECIFIED` | No response view specified. The API will default to the BASIC view.  
`BASIC` | Only the `consented` field is populated in `[CheckDataAccessResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess#body.CheckDataAccessResponse)`.  
`FULL` | All fields within `[CheckDataAccessResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess#body.CheckDataAccessResponse)` are populated. When set to `FULL`, all `ACTIVE` Consents are evaluated even if a matching policy is found during evaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
