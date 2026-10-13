---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/organizationSecurityPolicies/listAssociations/
title: Method: organizationSecurityPolicies.listAssociations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:14.595958+00:00
---

# Method: organizationSecurityPolicies.listAssociations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/organizationSecurityPolicies/listAssociations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: organizationSecurityPolicies.listAssociations Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists associations of a specified target, i.e., organization or folder.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.listAssociations instead.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/locations/global/securityPolicies/listAssociations`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`targetResource` |  `string` The target resource to list associations. It is an organization, or a folder.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "associations": [
        {
          "name": string,
          "attachmentId": string,
          "excludedProjects": [
            string
          ],
          "excludedFolders": [
            string
          ],
          "securityPolicyId": string,
          "shortName": string,
          "displayName": string
        }
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of securityPolicy associations. Always `compute#organizationSecurityPoliciesListAssociations` for lists of securityPolicy associations.  
`associations[]` |  `object` A list of associations.  
`associations[].name` |  `string` The name for an association.  
`associations[].attachmentId` |  `string` The resource that the security policy is attached to.  
`associations[].excludedProjects[]` |  `string` A list of projects to exclude from the security policy.  
`associations[].excludedFolders[]` |  `string` A list of folders to exclude from the security policy.  
`associations[].securityPolicyId` |  `string` Output only. The security policy ID of the association.  
`associations[].shortName` |  `string` Output only. The short name of the security policy of the association.  
`associations[].displayName  
**(deprecated)**` |  `string` Output only. The display name of the security policy of the association.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.organizations.listAssociations`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
