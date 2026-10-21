---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/patch/
title: Method: projects.locations.privateOffers.documents.patch \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:19:30.893284+00:00
---

# Method: projects.locations.privateOffers.documents.patch  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Method: projects.locations.privateOffers.documents.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Updates the target PrivateOfferDocument.

### HTTP request

`PATCH https://commerceproducer.googleapis.com/v1beta/{privateOfferDocument.name=projects/*/locations/*/privateOffers/*/documents/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`privateOfferDocument.name` |  `string` Identifier. Name of the resource.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement. If unspecified, all fields present in the request will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[PrivateOfferDocument](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents#PrivateOfferDocument)`.

### Response body

If successful, the response body contains an instance of `[PrivateOfferDocument](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents#PrivateOfferDocument)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `commerceproducer.privateOfferDocuments.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
