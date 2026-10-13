---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy/
title: Method: projects.serviceAccounts.setIamPolicy \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:07.362774+00:00
---

# Method: projects.serviceAccounts.setIamPolicy  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.setIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Sets the IAM policy that is attached to a `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`.

Use this method to grant or revoke access to the service account. For example, you could grant a principal the ability to impersonate the service account.

This method does not enable the service account to access other resources. To grant roles to a service account on a resource, follow these steps:

  1. Call the resource's `getIamPolicy` method to get its current IAM policy.
  2. Edit the policy so that it binds the service account to an IAM role for the resource.
  3. Call the resource's `setIamPolicy` method to update its IAM policy.



For detailed instructions, see [Manage access to project, folders, and organizations](https://cloud.google.com/iam/help/service-accounts/granting-access-to-service-accounts) or [Manage access to other resources](https://cloud.google.com/iam/help/access/manage-other-resources).

### HTTP request

`POST https://iam.googleapis.com/v1/{resource=projects/*/serviceAccounts/*}:setIamPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policy": {
        object ([Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy))
      },
      "updateMask": string
    }  
  
Fields  
---  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy)`)` REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:`paths: "bindings, etag"`This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
