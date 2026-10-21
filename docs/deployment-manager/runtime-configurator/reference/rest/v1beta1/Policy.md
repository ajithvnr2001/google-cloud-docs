---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/Policy/
title: Policy \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:35.649891+00:00
---

# Policy  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/Policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Policy Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Binding
    * JSON representation
  * Expr
    * JSON representation



Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources.

A `Policy` consists of a list of `bindings`. A `binding` binds a list of `members` to a `role`, where the members can be user accounts, Google groups, Google domains, and service accounts. A `role` is a named list of permissions defined by IAM.

**JSON Example**
    
    
    {
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:mike@example.com",
            "group:admins@example.com",
            "domain:google.com",
            "serviceAccount:my-other-app@appspot.gserviceaccount.com"
          ]
        },
        {
          "role": "roles/viewer",
          "members": ["user:sean@example.com"]
        }
      ]
    }
    

**YAML Example**
    
    
    bindings:
    - members:
      - user:mike@example.com
      - group:admins@example.com
      - domain:google.com
      - serviceAccount:my-other-app@appspot.gserviceaccount.com
      role: roles/owner
    - members:
      - user:sean@example.com
      role: roles/viewer
    

For a description of IAM and its features, see the [IAM developer's guide](https://cloud.google.com/iam/docs).

JSON representation  
---  
      
    
    {
      "version": number,
      "bindings": [
        {
          object([Binding](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/Policy#Binding))
        }
      ],
      "etag": string
    }  
  
Fields  
---  
`version  
**(deprecated)**` |  `number` This item is deprecated!Deprecated.  
`bindings[]` |  `object(`[Binding](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/Policy#Binding)`)` Associates a list of `members` to a `role`. `bindings` with no members will result in an error.   
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.If no `etag` is provided in the call to `setIamPolicy`, then the existing policy is overwritten blindly.A base64-encoded string.  
  
## Binding

Associates `members` with a `role`.

JSON representation  
---  
      
    
    {
      "role": string,
      "members": [
        string
      ],
      "condition": {
        object([Expr](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/Policy#Expr))
      }
    }  
  
Fields  
---  
`role` |  `string` Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`.   
`members[]` |  `string` Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values:

  * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.
  * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.
  * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@gmail.com` .


  * `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.
  * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.


  * `domain:{domain}`: A Google Apps domain name that represents all the users of that domain. For example, `google.com` or `example.com`.

  
`condition` |  `object(`[Expr](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/Policy#Expr)`)` Unimplemented. The condition that is associated with this binding. NOTE: an unsatisfied condition will not allow user access via current binding. Different bindings, including their conditions, are examined independently.   
  
## Expr

Represents an expression text. Example:
    
    
    title: "User account presence"
    description: "Determines whether the request has a user account"
    expression: "size(request.user) > 0"
    

JSON representation  
---  
      
    
    {
      "expression": string,
      "title": string,
      "description": string,
      "location": string
    }  
  
Fields  
---  
`expression` |  `string` Textual representation of an expression in Common Expression Language syntax.The application context of the containing message determines which well-known feature set of CEL is supported.  
`title` |  `string` An optional title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.   
`description` |  `string` An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.   
`location` |  `string` An optional string indicating the location of the expression for error reporting, e.g. a file name and a position in the file.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
