---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact/
title: Method: projects.locations.image.redact \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:37.220875+00:00
---

# Method: projects.locations.image.redact  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Method: projects.locations.image.redact Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Redacts potentially sensitive info from an image. This method has limits on input size, processing time, and output size. See <https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images> to learn more.

When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4useuin

  
`POST https://dlp.googleapis.com/v2/{parent=projects/*/locations/*}/image:redact`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

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
      "locationId": string,
      "inspectConfig": {
        object ([InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig))
      },
      "imageRedactionConfigs": [
        {
          object ([ImageRedactionConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ImageRedactionConfig))
        }
      ],
      "includeFindings": boolean,
      "byteItem": {
        object ([ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem))
      },
      "inspectTemplate": string,
      "deidentifyTemplate": string
    }  
  
Fields  
---  
`locationId` |  `string` Deprecated. This field has no effect.  
`inspectConfig` |  `object (`[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`)` Configuration for the inspector.  
`imageRedactionConfigs[]` |  `object (`[ImageRedactionConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ImageRedactionConfig)`)` The configuration for specifying what content to redact from images.  
`includeFindings` |  `boolean` Whether the response should include findings along with the redacted image.  
`byteItem` |  `object (`[ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem)`)` The content must be PNG, JPEG, SVG or BMP.  
`inspectTemplate` |  `string` The full resource name of the inspection template to use. Settings in the main `inspectConfig` field override the corresponding settings in this inspection template.The merge behavior is as follows:

  * Singular field: The main field's value replaces the value of the corresponding field in the template.
  * Repeated fields: The field values are appended to the list defined in the template.
  * Sub-messages and groups: The fields are recursively merged.

  
`deidentifyTemplate` |  `string` The full resource name of the de-identification template to use. Settings in the main `imageRedactionConfigs` field override the corresponding settings in this de-identification template. The request fails if the type of the template's deidentifyConfig is not imageTransformations.  
  
### Response body

If successful, the response body contains an instance of `[RedactImageResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RedactImageResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
