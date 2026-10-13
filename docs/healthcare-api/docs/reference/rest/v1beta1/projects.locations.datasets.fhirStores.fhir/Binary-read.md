---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Binary-read/
title: Method: fhir.Binary-read \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:24.168729+00:00
---

# Method: fhir.Binary-read  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Binary-read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: fhir.Binary-read Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.fhirStores.fhir.Binary-read

Gets the contents of a FHIR Binary resource.

This method can be used to retrieve a Binary resource either by using the FHIR JSON mimetype as the value for the Accept header, or as a raw data stream. If the FHIR Accept type is used this method will return a Binary resource with the data base64-encoded, regardless of how the resource was created. The resource data can be retrieved in base64-decoded form if the Accept type of the request matches the value of the resource's `contentType` field.

The definition of the Binary REST API can be found at <https://hl7.org/fhir/binary.html#rest>.

### HTTP request

`GET https://healthcare.googleapis.com/v1beta1/{name=projects/*/locations/*/datasets/*/fhirStores/*/fhir/Binary/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Binary resource to retrieve. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirResources.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
