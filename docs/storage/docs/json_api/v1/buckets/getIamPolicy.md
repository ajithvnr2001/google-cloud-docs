---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy/
title: Buckets: getIamPolicy \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:44.170338+00:00
---

# Buckets: getIamPolicy  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: getIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

Returns an Identity and Access Management (IAM) policy for the specified bucket.

## Required permissions

The authenticated user must have the `storage.buckets.getIamPolicy` IAM permission to use this method. 

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/iam

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
`optionsRequestedPolicyVersion` | `int` |  The [IAM policy version](https://docs.cloud.google.com/iam/docs/policies#versions) to be returned. If the optionsRequestedPolicyVersion is for an older version that doesn't support part of the requested IAM policy, the request fails. Required to be 3 or greater for buckets with [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "version": int,
      "kind": "storage#policy",
      "resourceId": string,
      "bindings": [
        {
          "role": string,
          "members": [
            string
          ],
          "condition": {
            "title": string,
            "description": string,
            "expression": RFC 3339 format string
          }
        }
      ],
      "etag": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`version` | `int` | The [IAM policy version](https://docs.cloud.google.com/iam/docs/policies#versions). |   
`kind` | `string` | The kind of item this is. For policies, this field is ignored in a request and is `"storage#policy"` in a response. |   
`resourceId` | `string` | The ID of the resource to which this policy belongs. The response for this field is of the form `"projects/_/buckets/bucket"`. This field is ignored in a request. |   
`bindings[]` | `list` | An association between a role, which comes with a set of permissions, and principals that have that role. |   
`bindings[].role` | `string` | The role that principals have. Two types of roles are supported: standard IAM roles, which grant permissions that do not map directly to those provided by ACLs, and legacy IAM roles, which do map directly to ACL permissions. All roles are of the format `"roles/storage.specificRole"`.   
See [Cloud Storage IAM Roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) for a list of available roles. |   
`bindings[].members[]` | `list` | A collection of principals that have the specified role. For a list of recognized values, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) and [Convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values).  |   
`bindings[].condition` | `object` | A condition object associated with this binding. Each role binding can only contain one condition. | optional  
`bindings[].condition.title` | `string` |  Title of the condition. For example, `"expires_end_of_2018"`.  |   
`bindings[].condition.description` | `string` |  Optional description of the condition. For example, `"Expires at midnight on 2018-12-31"`.  | optional  
`bindings[].condition.expression` | `string` |  [Attribute-based](https://docs.cloud.google.com/iam/docs/conditions-overview#attributes) logic expression using a subset of the Common Expression Language (CEL). For example, `"request.time < timestamp('2019-01-01T00:00:00Z')"`.  |   
`etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the policy. |  writable   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
