---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget/
title: Method: projects.locations.privateOffers.resolveAmendmentTarget \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:23:36.669493+00:00
---

# Method: projects.locations.privateOffers.resolveAmendmentTarget  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Method: projects.locations.privateOffers.resolveAmendmentTarget Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * OptionalOffers
    * JSON representation



Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

### HTTP request

`GET https://commerceproducer.googleapis.com/v1beta/{parent=projects/*/locations/*}/privateOffers:resolveAmendmentTarget`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ResolveAmendmentTargetRequest  
  
### Query parameters

Parameters  
---  
`targetBillingAccount` |  `string` Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billingAccount}.  
`baseStandardOffer` |  `string` Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
  
### Request body

The request body must be empty.

### Response body

Message in response to privateOffers.resolveAmendmentTarget.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field amendment_requirement can be only one of the following:
      "requiredPrivateOffer": string,
      "requiredStandardOffer": string,
      "optionalOffers": {
        object ([OptionalOffers](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget#OptionalOffers))
      }
      // End of list of possible types for union field amendment_requirement.
    }  
  
Fields  
---  
Union field `amendment_requirement`. The amendment requirements for the new private offer.If this oneof is empty, the client should create a brand new offer. `amendment_requirement` can be only one of the following:  
`requiredPrivateOffer` |  `string` The resource name of an existing private offer that MUST be amended.If this is set, the new private offer the client creates must populate the `singleProductOffer.amended_private_offer` field with this value.  
`requiredStandardOffer` |  `string` The resource name of an existing standard offer that MUST be amended.If this is set, the new private offer the client creates must populate the `singleProductOffer.amended_standard_offer` field with this value.  
`optionalOffers` |  `object (`[OptionalOffers](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget#OptionalOffers)`)` A list of existing offers that may optionally be amended.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `commerceproducer.privateOffers.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## OptionalOffers

A wrapper message containing offers that can optionally be amended.

JSON representation  
---  
      
    
    {
      "privateOffers": [
        string
      ]
    }  
  
Fields  
---  
`privateOffers[]` |  `string` A list of existing private offers that are eligible to be amended.When creating a new private offer, the client may choose to populate the `singleProductOffer.amended_private_offer` field with one of these resource names. Alternatively, the client may leave the field unset to create a brand new offer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-15 UTC."],[],[]] 
