---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/activate/
title: Method: consents.activate \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:06.252728+00:00
---

# Method: consents.activate  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/activate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: consents.activate Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.consentStores.consents.activate

Activates the latest revision of the specified `[Consent](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents#Consent)` by committing a new revision with `state` updated to `ACTIVE`. If the latest revision of the specified Consent is in the `ACTIVE` state, no new revision is committed. A `[FAILED_PRECONDITION](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Code#ENUM_VALUES.FAILED_PRECONDITION)` error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state.

### HTTP request

`POST https://healthcare.googleapis.com/v1/{name=projects/*/locations/*/datasets/*/consentStores/*/consents/*}:activate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Consent to activate, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/consentStores/{consentStoreId}/consents/{consent_id}`. An `[INVALID_ARGUMENT](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Code#ENUM_VALUES.INVALID_ARGUMENT)` error occurs if `revisionId` is specified in the name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.consents.activate`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consentArtifact": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "expireTime": string,
      "ttl": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`consentArtifact` |  `string` Required. The resource name of the Consent artifact that contains documentation of the user's consent, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/consentStores/{consentStoreId}/consentArtifacts/{consent_artifact_id}`. If the draft Consent had a Consent artifact, this Consent artifact overwrites it. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `consentArtifact`:

  * `healthcare.consentArtifacts.get`

  
Optional. Allows setting expiration time for Consents. Expired consents are ignored in access determination methods such as [CheckDataAccess]. This value overrides the expiration duration configured for the consent store. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`expireTime` |  `string(`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp in UTC of when this Consent is considered expired.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ttl` |  `string(`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The time to live for this Consent from when it is marked as active.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Consent](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents#Consent)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
