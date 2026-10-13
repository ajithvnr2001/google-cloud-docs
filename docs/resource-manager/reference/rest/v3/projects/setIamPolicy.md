---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/setIamPolicy/
title: Method: projects.setIamPolicy \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:42.746973+00:00
---

# Method: projects.setIamPolicy  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/setIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.setIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Sets the IAM access control policy for the specified project, in the format `projects/{ProjectIdOrNumber}` e.g. projects/123.

CAUTION: This method will replace the existing policy, and cannot be used to append additional IAM settings.

Note: Removing service accounts from policies or changing their roles can render services completely inoperable. It is important to understand how the service account is being used before removing or updating its roles.

The following constraints apply when using `setIamPolicy()`:

  * Project does not support `allUsers` and `allAuthenticatedUsers` as `members` in a `Binding` of a `Policy`.

  * The owner role can be granted to a `user`, `serviceAccount`, or a group that is part of an organization. For example, [group@myownpersonaldomain.com](mailto:group@myownpersonaldomain.com) could be added as an owner to a project in the myownpersonaldomain.com organization, but not the examplepetstore.com organization.

  * Service accounts can be made owners of a project directly without any restrictions. However, to be added as an owner, a user must be invited using the Cloud Platform console and must accept the invitation.

  * A user cannot be granted the owner role using `setIamPolicy()`. The user must be granted the owner role using the Cloud Platform Console and must explicitly accept the invitation.

  * Invitations to grant the owner role cannot be sent using `setIamPolicy()`; they must be sent only using the Cloud Platform Console.

  * If the project is not part of an organization, there must be at least one owner who has accepted the Terms of Service (ToS) agreement in the policy. Calling `setIamPolicy()` to remove the last ToS-accepted owner from the policy will fail. This restriction also applies to legacy projects that no longer have owners who have accepted the ToS. Edits to IAM policies will be rejected until the lack of a ToS-accepting owner is rectified. If the project is part of an organization, you can remove all owners, potentially making the organization inaccessible.




### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v3/{resource=projects/*}:setIamPolicy`

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
        object ([Policy](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Policy))
      },
      "updateMask": string
    }  
  
Fields  
---  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Policy)`)` REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:`paths: "bindings, etag"`This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Policy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformprojects`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
