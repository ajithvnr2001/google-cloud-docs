---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify/
title: Method: projects.content.reidentify \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:26.665678+00:00
---

# Method: projects.content.reidentify  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Method: projects.content.reidentify Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Re-identifies content that has been de-identified. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#re-identification_in_free_text_code_example> to learn more.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4useuin

  
`POST https://dlp.googleapis.com/v2/{parent=projects/*}/content:reidentify`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{projectId}/locations/{locationId}`
  * Projects scope, no location specified (defaults to global): `projects/{projectId}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `serviceusage.services.use`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "reidentifyConfig": {
        object ([DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig))
      },
      "inspectConfig": {
        object ([InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig))
      },
      "item": {
        object ([ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem))
      },
      "inspectTemplateName": string,
      "reidentifyTemplateName": string,
      "locationId": string
    }  
  
Fields  
---  
`reidentifyConfig` |  `object (`[DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig)`)` Configuration for the re-identification of the content item. This field shares the same proto message type that is used for de-identification, however its usage here is for the reversal of the previous de-identification. Re-identification is performed by examining the transformations used to de-identify the items and executing the reverse. This requires that only reversible transformations be provided here. The reversible transformations are:

  * `CryptoDeterministicConfig`
  * `CryptoReplaceFfxFpeConfig`

  
`inspectConfig` |  `object (`[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`)` Configuration for the inspector.  
`item` |  `object (`[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem)`)` The item to re-identify. Will be treated as text.  
`inspectTemplateName` |  `string` Template to use. Any configuration directly specified in `inspectConfig` will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`reidentifyTemplateName` |  `string` Template to use. References an instance of `DeidentifyTemplate`. Any configuration directly specified in `reidentifyConfig` or `inspectConfig` will override those set in the template. The `DeidentifyTemplate` used must include only reversible transformations. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`locationId` |  `string` Deprecated. This field has no effect.  
  
### Response body

If successful, the response body contains an instance of `[ReidentifyContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ReidentifyContentResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
