---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint/
title: AnalyzerOrgPolicyConstraint \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:06.265876+00:00
---

# AnalyzerOrgPolicyConstraint  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  AnalyzerOrgPolicyConstraint Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Constraint
    * JSON representation
  * ConstraintDefault
  * ListConstraint
    * JSON representation
  * BooleanConstraint
  * CustomConstraint
    * JSON representation
  * MethodType
  * ActionType



The organization policy constraint definition.

JSON representation  
---  
      
    
    {
    
      // Union field constraint_definition can be only one of the following:
      "googleDefinedConstraint": {
        object ([Constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#Constraint))
      },
      "customConstraint": {
        object ([CustomConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#CustomConstraint))
      }
      // End of list of possible types for union field constraint_definition.
    }  
  
Fields  
---  
Union field `constraint_definition`.`constraint_definition` can be only one of the following:  
`googleDefinedConstraint` |  `object (`[Constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#Constraint)`)` The definition of the canned constraint defined by Google.  
`customConstraint` |  `object (`[CustomConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#CustomConstraint)`)` The definition of the custom constraint.  
  
## Constraint

The definition of a constraint.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "constraintDefault": enum ([ConstraintDefault](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#ConstraintDefault)),
    
      // Union field constraint_type can be only one of the following:
      "listConstraint": {
        object ([ListConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#ListConstraint))
      },
      "booleanConstraint": {
        object ([BooleanConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#BooleanConstraint))
      }
      // End of list of possible types for union field constraint_type.
    }  
  
Fields  
---  
`name` |  `string` The unique name of the constraint. Format of the name should be * `constraints/{constraint_name}`For example, `constraints/compute.disableSerialPortAccess`.  
`displayName` |  `string` The human readable name of the constraint.  
`description` |  `string` Detailed description of what this `Constraint` controls as well as how and where it is enforced.  
`constraintDefault` |  `enum (`[ConstraintDefault](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#ConstraintDefault)`)` The evaluation behavior of this constraint in the absence of 'Policy'.  
Union field `constraint_type`. The type of restrictions for this `Constraint`.Immutable after creation. `constraint_type` can be only one of the following:  
`listConstraint` |  `object (`[ListConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#ListConstraint)`)` Defines this constraint as being a ListConstraint.  
`booleanConstraint` |  `object (`[BooleanConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#BooleanConstraint)`)` Defines this constraint as being a BooleanConstraint.  
  
## ConstraintDefault

Specifies the default behavior in the absence of any `Policy` for the `Constraint`. This must not be `CONSTRAINT_DEFAULT_UNSPECIFIED`.

Enums  
---  
`CONSTRAINT_DEFAULT_UNSPECIFIED` | This is only used for distinguishing unset values and should never be used.  
`ALLOW` | Indicates that all values are allowed for list constraints. Indicates that enforcement is off for boolean constraints.  
`DENY` | Indicates that all values are denied for list constraints. Indicates that enforcement is on for boolean constraints.  
  
## ListConstraint

A `Constraint` that allows or disallows a list of string values, which are configured by an organization's policy administrator with a `Policy`.

JSON representation  
---  
      
    
    {
      "supportsIn": boolean,
      "supportsUnder": boolean
    }  
  
Fields  
---  
`supportsIn` |  `boolean` Indicates whether values grouped into categories can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"in:Python"` would match any value in the 'Python' group.  
`supportsUnder` |  `boolean` Indicates whether subtrees of Cloud Resource Manager resource hierarchy can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"under:folders/123"` would match any resource under the 'folders/123' folder.  
  
## BooleanConstraint

This type has no fields.

A `Constraint` that is either enforced or not.

For example a constraint `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM instance, serial port connections will not be opened to that instance.

## CustomConstraint

The definition of a custom constraint.

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceTypes": [
        string
      ],
      "methodTypes": [
        enum ([MethodType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#MethodType))
      ],
      "condition": string,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#ActionType)),
      "displayName": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Name of the constraint. This is unique within the organization. Format of the name should be * `organizations/{organizationId}/customConstraints/{custom_constraint_id}`Example : "organizations/123/customConstraints/custom.createOnlyE2TypeVms"  
`resourceTypes[]` |  `string` The Resource Instance type on which this policy applies to. Format will be of the form : "/" Example: * `compute.googleapis.com/Instance`.  
`methodTypes[]` |  `enum (`[MethodType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#MethodType)`)` All the operations being applied for this constraint.  
`condition` |  `string` Organization Policy condition/expression. For example: `resource.instanceName.matches("(production|test)_(.+_)?[\d]+")'` or, `resource.management.auto_upgrade == true`  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint#ActionType)`)` Allow or deny type.  
`displayName` |  `string` One line display name for the UI.  
`description` |  `string` Detailed information about this custom policy constraint.  
  
## MethodType

The operation in which this constraint will be applied. For example: If the constraint applies only when create VMs, the methodTypes will be "CREATE" only. If the constraint applied when create or delete VMs, the methodTypes will be "CREATE" and "DELETE".

Enums  
---  
`METHOD_TYPE_UNSPECIFIED` | Unspecified. Will results in user error.  
`CREATE` | Constraint applied when creating the resource.  
`UPDATE` | Constraint applied when updating the resource.  
`DELETE` | Constraint applied when deleting the resource.  
`REMOVE_GRANT` | Constraint applied when removing an IAM grant.  
`GOVERN_TAGS` | Constraint applied when enforcing forced tagging.  
  
## ActionType

Allow or deny type.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | Unspecified. Will results in user error.  
`ALLOW` | Allowed action type.  
`DENY` | Deny action type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
