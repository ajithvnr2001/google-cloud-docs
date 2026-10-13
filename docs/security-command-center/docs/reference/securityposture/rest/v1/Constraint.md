---
url: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint/
title: Constraint \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:59.454423+00:00
---

# Constraint  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Constraint Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SecurityHealthAnalyticsModule
    * JSON representation
  * SecurityHealthAnalyticsCustomModule
    * JSON representation
  * CustomConfig
    * JSON representation
  * CustomOutputSpec
    * JSON representation
  * Property
    * JSON representation
  * ResourceSelector
    * JSON representation
  * OrgPolicyConstraint
    * JSON representation
  * PolicyRule
    * JSON representation
  * StringValues
    * JSON representation
  * OrgPolicyConstraintCustom
    * JSON representation
  * CustomConstraint
    * JSON representation



Metadata for a constraint in a `[Policy](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Policy)`.

JSON representation  
---  
      
    
    {
    
      // Union field implementation can be only one of the following:
      "securityHealthAnalyticsModule": {
        object ([SecurityHealthAnalyticsModule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#SecurityHealthAnalyticsModule))
      },
      "securityHealthAnalyticsCustomModule": {
        object ([SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#SecurityHealthAnalyticsCustomModule))
      },
      "orgPolicyConstraint": {
        object ([OrgPolicyConstraint](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#OrgPolicyConstraint))
      },
      "orgPolicyConstraintCustom": {
        object ([OrgPolicyConstraintCustom](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#OrgPolicyConstraintCustom))
      }
      // End of list of possible types for union field implementation.
    }  
  
Fields  
---  
Union field `implementation`. The implementation of the constraint. `implementation` can be only one of the following:  
`securityHealthAnalyticsModule` |  `object (`[SecurityHealthAnalyticsModule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#SecurityHealthAnalyticsModule)`)` Optional. A built-in detector for Security Health Analytics.  
`securityHealthAnalyticsCustomModule` |  `object (`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#SecurityHealthAnalyticsCustomModule)`)` Optional. A custom module for Security Health Analytics.  
`orgPolicyConstraint` |  `object (`[OrgPolicyConstraint](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#OrgPolicyConstraint)`)` Optional. A predefined organization policy constraint.  
`orgPolicyConstraintCustom` |  `object (`[OrgPolicyConstraintCustom](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#OrgPolicyConstraintCustom)`)` Optional. A custom organization policy constraint.  
  
## SecurityHealthAnalyticsModule

A built-in detector for Security Health Analytics.

JSON representation  
---  
      
    
    {
      "moduleName": string,
      "moduleEnablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/EnablementState))
    }  
  
Fields  
---  
`moduleName` |  `string` Required. The name of the detector. For example, `BIGQUERY_TABLE_CMEK_DISABLED`. This field is also used as the finding category for all the asset violation findings that the detector returns.  
`moduleEnablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/EnablementState)`)` Whether the detector is enabled at a specified level of the resource hierarchy.  
  
## SecurityHealthAnalyticsCustomModule

A custom module for Security Health Analytics.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "config": {
        object ([CustomConfig](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#CustomConfig))
      },
      "moduleEnablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/EnablementState))
    }  
  
Fields  
---  
`id` |  `string` Output only. Immutable. The unique identifier for the custom module. Contains 1 to 20 digits.  
`displayName` |  `string` Optional. The display name of the custom module. This value is used as the finding category for all the asset violation findings that the custom module returns. The display name must contain between 1 and 128 alphanumeric characters or underscores, and it must start with a lowercase letter.  
`config` |  `object (`[CustomConfig](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#CustomConfig)`)` Required. Configuration settings for the custom module.  
`moduleEnablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/EnablementState)`)` Whether the custom module is enabled at a specified level of the resource hierarchy.  
  
## CustomConfig

A custom module configuration for Security Health Analytics. Use `CustomConfig` to create custom detectors that generate custom findings for resources that you specify.

JSON representation  
---  
      
    
    {
      "predicate": {
        object ([Expr](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr))
      },
      "customOutput": {
        object ([CustomOutputSpec](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#CustomOutputSpec))
      },
      "resourceSelector": {
        object ([ResourceSelector](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#ResourceSelector))
      },
      "severity": enum ([Severity](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Severity)),
      "description": string,
      "recommendation": string
    }  
  
Fields  
---  
`predicate` |  `object (`[Expr](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr)`)` Required. The Common Expression Language (CEL) expression to evaluate. When the expression evaluates to `true` for a resource, a finding is generated.  
`customOutput` |  `object (`[CustomOutputSpec](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#CustomOutputSpec)`)` Optional. Definitions of custom source properties to include in findings.  
`resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#ResourceSelector)`)` Required. The resource types that the custom module operates on.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Severity)`)` Required. The severity of findings generated by the custom module.  
`description` |  `string` Optional. A description of the vulnerability or misconfiguration that the custom module detects.The description appears in each finding. Provide enough information to help an investigator understand the finding.The value must be enclosed in quotation marks.  
`recommendation` |  `string` Required. An explanation of the steps that security teams can take to resolve the detected issue. The explanation appears in each finding.  
  
## CustomOutputSpec

Definitions of custom source properties that can appear in findings.

JSON representation  
---  
      
    
    {
      "properties": [
        {
          object ([Property](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#Property))
        }
      ]
    }  
  
Fields  
---  
`properties[]` |  `object (`[Property](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#Property)`)` Optional. The custom source properties that can appear in findings.  
  
## Property

A name-value pair used as a custom source property.

JSON representation  
---  
      
    
    {
      "name": string,
      "valueExpression": {
        object ([Expr](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the custom source property.  
`valueExpression` |  `object (`[Expr](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr)`)` Optional. The CEL expression for the value of the custom source property. For resource properties, you can return the value of the property or a string enclosed in quotation marks.  
  
## ResourceSelector

A selector for the resource types to run the detector on.

JSON representation  
---  
      
    
    {
      "resourceTypes": [
        string
      ]
    }  
  
Fields  
---  
`resourceTypes[]` |  `string` Required. The resource types to run the detector on. Each custom module can specify up to 5 resource types.  
  
## OrgPolicyConstraint

A predefined organization policy constraint.

JSON representation  
---  
      
    
    {
      "cannedConstraintId": string,
      "policyRules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#PolicyRule))
        }
      ]
    }  
  
Fields  
---  
`cannedConstraintId` |  `string` Required. A unique identifier for the constraint.  
`policyRules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#PolicyRule)`)` Required. The rules enforced by the constraint.  
  
## PolicyRule

A rule that defines the allowed and denied values for an organization policy constraint.

JSON representation  
---  
      
    
    {
      "condition": {
        object ([Expr](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr))
      },
    
      // Union field kind can be only one of the following:
      "values": {
        object ([StringValues](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#StringValues))
      },
      "allowAll": boolean,
      "denyAll": boolean,
      "enforce": boolean
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr)`)` A condition that determines whether this rule is used to evaluate the policy.When set, the `[google.type.Expr.expression](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PolicySet#Expr.FIELDS.expression)` field must contain 1 to 10 subexpressions, joined by the `||` or `&&` operators. Each subexpression must use the `resource.matchTag()` or `resource.matchTagId()` Common Expression Language (CEL) function.The `resource.matchTag()` function takes the following arguments:

  * `key_name`: the namespaced name of the tag key, with the organization ID and a slash (`/`) as a prefix; for example, `123456789012/environment`
  * `value_name`: the short name of the tag value

For example: `resource.matchTag('123456789012/environment, 'prod')`The `resource.matchTagId()` function takes the following arguments:

  * `key_id`: the permanent ID of the tag key; for example, `tagKeys/123456789012`
  * `value_id`: the permanent ID of the tag value; for example, `tagValues/567890123456`

For example: `resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456')`  
Union field `kind`. The type of rule that the `PolicyRule` defines. `kind` can be only one of the following:  
`values` |  `object (`[StringValues](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#StringValues)`)` The allowed and denied values for a list constraint. Valid only for list constraints.  
`allowAll` |  `boolean` Whether to allow any value for a list constraint. Valid only for list constraints.  
`denyAll` |  `boolean` Whether to deny all values for a list constraint. Valid only for list constraints.  
`enforce` |  `boolean` Whether to enforce the constraint. Valid only for boolean constraints.  
  
## StringValues

The allowed and denied values for a list constraint.

For all constraints, these fields can contain literal values. Optionally, you can add the `is:` prefix to these values. If the value contains a colon (`:`), then the `is:` prefix is required.

Some constraints allow you to specify a portion of the resource hierarchy, known as a [_hierarchy subtree_](https://cloud.google.com/resource-manager/help/organization-policy/hierarchy-subtree), that the constraint applies to. To specify a hierarchy subtree, use the `under:` prefix, followed by a value with one of these formats:

  * `projects/{projectId}` (for example, `projects/tokyo-rain-123`)
  * `folders/{folder_id}` (for example, `folders/1234567890123`)
  * `organizations/{organization_id}` (for example, `organizations/123456789012`)



A constraint's `supportsUnder` field indicates whether you can specify a hierarchy subtree. To learn which predefined constraints let you specify a hierarchy subtree, see the [constraints reference](https://cloud.google.com/resource-manager/help/organization-policy/constraints/reference).

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ]
    }  
  
Fields  
---  
`allowedValues[]` |  `string` The allowed values for the constraint.  
`deniedValues[]` |  `string` The denied values for the constraint.  
  
## OrgPolicyConstraintCustom

A custom organization policy constraint.

JSON representation  
---  
      
    
    {
      "customConstraint": {
        object ([CustomConstraint](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#CustomConstraint))
      },
      "policyRules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#PolicyRule))
        }
      ]
    }  
  
Fields  
---  
`customConstraint` |  `object (`[CustomConstraint](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#CustomConstraint)`)` Required. Metadata for the constraint.  
`policyRules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Constraint#PolicyRule)`)` Required. The rules enforced by the constraint.  
  
## CustomConstraint

A custom, user-defined constraint. You can apply the constraint only to the resource types specified in the constraint, and only within the organization where the constraint is defined.

_When you create a custom constraint, it is not enforced automatically._ You must use an organization policy to [enforce the constraint](https://cloud.google.com/resource-manager/help/organization-policy/constraints/enforce).

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceTypes": [
        string
      ],
      "methodTypes": [
        enum ([MethodType](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/MethodType))
      ],
      "condition": string,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/ActionType)),
      "displayName": string,
      "description": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The name of the constraint, in the format `organizations/{organization_id}/customConstraints/custom.{custom_constraint_id}`. For example, `organizations/123456789012/customConstraints/custom.createOnlyE2TypeVms`.Must contain 1 to 62 characters, excluding the prefix `organizations/{organization_id}/customConstraints/custom.`.  
`resourceTypes[]` |  `string` Immutable. The resource type that the constraint applies to, in the format `{canonical_service_name}/{resource_type_name}`. For example, `compute.googleapis.com/Instance`.  
`methodTypes[]` |  `enum (`[MethodType](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/MethodType)`)` The types of operations that the constraint applies to.  
`condition` |  `string` A Common Expression Language (CEL) condition expression that must evaluate to `true` for the constraint to be enforced. The maximum length is 1000 characters.For example:

  * `resource.instanceName.matches('(production|test)_(.+_)?[\d]+')`: Evaluates to `true` if the resource's `instanceName` attribute contains the following: 
    * The prefix `production` or `test`
    * An underscore (`_`)
    * Optional: One or more characters, followed by an underscore (`_`)
    * One or more digits
  * `resource.management.auto_upgrade == true`: Evaluates to `true` if the resource's `management.auto_upgrade` attribute is `true`.

  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/ActionType)`)` Whether to allow or deny the action.  
`displayName` |  `string` A display name for the constraint. The maximum length is 200 characters.  
`description` |  `string` A description of the constraint. The maximum length is 2000 characters.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time at which the constraint was updated or created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
