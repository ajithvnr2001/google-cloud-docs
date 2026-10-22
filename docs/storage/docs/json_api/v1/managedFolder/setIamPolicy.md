---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy/
title: ManagedFolder: setIamPolicy \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:50.894227+00:00
---

# ManagedFolder: setIamPolicy  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ManagedFolder: setIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

Updates an Identity and Access Management (IAM) policy for a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders). 

## Required permissions

The authenticated user must have the `storage.managedfolders.setIamPolicy` IAM permission to use this method.

## Request

### HTTP request
    
    
    PUT https://storage.googleapis.com/storage/v1/b/bucket/managedFolders/managedFolder/iam

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the managed folder.   
`managedFolder` | `string` |  The name of the managed folder, expressed as a path. For example, `example-dir`. If the managed folder is nested (for example, `example-dir1/example-dir2`), the `/` character in the managed folder path must be escaped. For example, `example-dir1%2Fexample-dir2`.   
  
### Request body

In the request body, supply data with the following structure:
    
    
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
        }],
      "etag": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`version` | `int` | The [IAM policy version](https://docs.cloud.google.com/iam/docs/policies#versions). Required to be 3 or greater for buckets with [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). |   
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
          ]
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
`bindings[].members[]` | `list` | A collection of identifiers for principals that have the specified role. Recognized identifiers are as follows: 

  * `"allUsers"` — A special identifier that represents any entity on the internet; with or without a user account.
  * `"allAuthenticatedUsers"` — A special identifier that represents most authenticated users, including all service accounts. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers).
  * `"user:emailid"` — An email address that represents a specific account. For example, `"user:joe@example.com"`.
  * `"serviceAccount:emailid"` — An email address that represents a service account. For example, `"serviceAccount:my-other-app@appspot.gserviceaccount.com"`. 
  * `"group:emailid"` — An email address that represents a Google group. For example, `"group:admins@example.com"`.
  * `"domain:domain"` — A domain name that represents all the users of that domain. For example, `"domain:example.com"`.
  * `"projectOwner:projectid"` — Owners of the given project. For example, `"projectOwner:my-example-project`"
  * `"projectEditor:projectid"` — Editors of the given project. For example, `"projectEditor:my-example-project`"
  * `"projectViewer:projectid"` — Viewers of the given project. For example, `"projectViewer:my-example-project"`

|   
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
