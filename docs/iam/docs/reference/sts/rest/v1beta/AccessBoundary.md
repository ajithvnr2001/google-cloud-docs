---
url: https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1beta/AccessBoundary/
title: AccessBoundary \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:56.076722+00:00
---

# AccessBoundary  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1beta/AccessBoundary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  AccessBoundary Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AccessBoundaryRule
    * JSON representation



An access boundary defines the upper bound of what a principal may access. It includes a list of access boundary rules that each defines the resource that may be allowed as well as permissions that may be used on those resources.

JSON representation  
---  
      
    
    {
      "accessBoundaryRules": [
        {
          object ([AccessBoundaryRule](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1beta/AccessBoundary#AccessBoundaryRule))
        }
      ]
    }  
  
Fields  
---  
`accessBoundaryRules[]` |  `object (`[AccessBoundaryRule](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1beta/AccessBoundary#AccessBoundaryRule)`)` A list of access boundary rules which defines the upper bound of the permission a principal may carry. If multiple rules are specified, the effective access boundary is the union of all the access boundary rules attached.One access boundary can contain at most 10 rules.  
  
## AccessBoundaryRule

An access boundary rule defines an upper bound of IAM permissions on a single resource.

JSON representation  
---  
      
    
    {
      "availableResource": string,
      "availablePermissions": [
        string
      ],
      "availabilityCondition": {
        object ([Expr](https://docs.cloud.google.com/iam/docs/reference/sts/rest/Shared.Types/Expr))
      }
    }  
  
Fields  
---  
`availableResource` |  `string` The full resource name of a Google Cloud resource entity. The format definition is at <https://cloud.google.com/apis/design/resource_names>.Example value: `//cloudresourcemanager.googleapis.com/projects/my-project`.  
`availablePermissions[]` |  `string` A list of permissions that may be allowed for use on the specified resource.The only supported values in the list are IAM roles, following the format of `[google.iam.v1.Binding.role](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/Binding#FIELDS.role)`.Example value: `inRole:roles/logging.viewer` for predefined roles and `inRole:organizations/{ORGANIZATION_ID}/roles/logging.viewer` for custom roles.  
`availabilityCondition` |  `object (`[Expr](https://docs.cloud.google.com/iam/docs/reference/sts/rest/Shared.Types/Expr)`)` The availability condition further constrains the access allowed by the access boundary rule.If the condition evaluates to `true`, then this access boundary rule will provide access to the specified resource, assuming the principal has the required permissions for the resource.If the condition does not evaluate to `true`, then access to the specified resource will not be available. Note that all access boundary rules in an access boundary are evaluated together as a union. As such, another access boundary rule may allow access to the resource, even if this access boundary rule does not allow access.To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).The maximum length of the `expression` field is 2048 characters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
