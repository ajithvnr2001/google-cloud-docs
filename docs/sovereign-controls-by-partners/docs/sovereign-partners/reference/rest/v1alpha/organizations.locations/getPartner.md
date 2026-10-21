---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner/
title: Method: organizations.locations.getPartner \u00a0|\u00a0 Sovereign Controls by Partners guides for partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:30:03.568992+00:00
---

# Method: organizations.locations.getPartner  |  Sovereign Controls by Partners guides for partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners)
  * [ Sovereign Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/guides)
  * [ Reference ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest)



Send feedback 

#  Method: organizations.locations.getPartner Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Sku
    * JSON representation
  * EkmMetadata
    * JSON representation
  * EkmSolution



Get details of a Partner.

### HTTP request

`GET https://cloudcontrolspartner.googleapis.com/v1alpha/{name=organizations/*/locations/*/partner}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Format: organizations/{organization}/locations/{location}/partner  
  
### Request body

The request body must be empty.

### Response body

Message describing Partner resource

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "skus": [
        {
          object ([Sku](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner#Sku))
        }
      ],
      "ekmSolutions": [
        {
          object ([EkmMetadata](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner#EkmMetadata))
        }
      ],
      "operatedCloudRegions": [
        string
      ],
      "partnerProjectId": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the partner. Format: organizations/{organization}/locations/{location}/partner Example: "organizations/123456/locations/us-central1/partner"  
`skus[]` |  `object (`[Sku](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner#Sku)`)` List of SKUs the partner is offering  
`ekmSolutions[]` |  `object (`[EkmMetadata](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner#EkmMetadata)`)` List of Google Cloud supported EKM partners supported by the partner  
`operatedCloudRegions[]` |  `string` List of Google Cloud regions that the partner sells services to customers. Valid Google Cloud regions found here: <https://cloud.google.com/compute/docs/regions-zones>  
`partnerProjectId` |  `string` Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time the resource was createdA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The last time the resource was updatedA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudcontrolspartner.partners.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Sku

Represents the SKU a partner owns inside Google Cloud to sell to customers.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string
    }  
  
Fields  
---  
`id` |  `string` Argentum product SKU, that is associated with the partner offerings to customers used by Syntro for billing purposes. SKUs can represent resold Google products or support services.  
`displayName` |  `string` Display name of the product identified by the SKU. A partner may want to show partner branded names for their offerings such as local sovereign cloud solutions.  
  
## EkmMetadata

Holds information needed by Mudbray to use partner EKMs for workloads.

JSON representation  
---  
      
    
    {
      "ekmSolution": enum ([EkmSolution](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner#EkmSolution)),
      "ekmEndpointUri": string
    }  
  
Fields  
---  
`ekmSolution` |  `enum (`[EkmSolution](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner#EkmSolution)`)` The Cloud EKM partner.  
`ekmEndpointUri` |  `string` Endpoint for sending requests to the EKM for key provisioning during Assured Workload creation.  
  
## EkmSolution

Represents Google Cloud supported external key management partners [Google Cloud EKM partners docs](https://cloud.google.com/kms/docs/ekm#supported_partners).

Enums  
---  
`EKM_SOLUTION_UNSPECIFIED` | Unspecified EKM solution  
`FORTANIX` | EKM Partner Fortanix  
`FUTUREX` | EKM Partner FutureX  
`THALES` | EKM Partner Thales  
`VIRTRU` | EKM Partner Virtu  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
