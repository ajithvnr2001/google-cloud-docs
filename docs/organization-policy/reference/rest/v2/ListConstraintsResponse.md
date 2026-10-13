---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse/
title: ListConstraintsResponse \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:43.181814+00:00
---

# ListConstraintsResponse  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  ListConstraintsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Constraint
    * JSON representation
  * ConstraintDefault
  * ListConstraint
    * JSON representation
  * BooleanConstraint
    * JSON representation
  * CustomConstraintDefinition
    * JSON representation
  * MethodType
  * ActionType
  * Parameter
    * JSON representation
  * Type
  * Metadata
    * JSON representation



The response returned from the `[constraints.list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.constraints/list#google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints)` method.

JSON representation  
---  
      
    
    {
      "constraints": [
        {
          object ([Constraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Constraint))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`constraints[]` |  `object (`[Constraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Constraint)`)` The collection of constraints that are available on the targeted resource.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is not used.  
  
## Constraint

A constraint describes a way to restrict a resource's configuration. For example, you could enforce a constraint that controls which Google Cloud services can be activated across an organization, or whether a Compute Engine instance can have serial port connections established. Constraints can be configured by the organization policy administrator to fit the needs of the organization by setting a policy that includes constraints at different locations in the organization's resource hierarchy. Policies are inherited down the resource hierarchy from higher levels, but can also be overridden. For details about the inheritance rules, see `[`Policy`](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy)`.

Constraints have a default behavior determined by the `constraintDefault` field, which is the enforcement behavior that is used in the absence of a policy being defined or inherited for the resource in question.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "constraintDefault": enum ([ConstraintDefault](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#ConstraintDefault)),
      "supportsDryRun": boolean,
      "equivalentConstraint": string,
      "supportsSimulation": boolean,
    
      // Union field constraint_type can be only one of the following:
      "listConstraint": {
        object ([ListConstraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#ListConstraint))
      },
      "booleanConstraint": {
        object ([BooleanConstraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#BooleanConstraint))
      }
      // End of list of possible types for union field constraint_type.
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the constraint. Must be in one of the following forms:

  * `projects/{project_number}/constraints/{constraint_name}`
  * `folders/{folder_number}/constraints/{constraint_name}`
  * `organizations/{organization_number}/constraints/{constraint_name}`

For example, "/projects/123/constraints/compute.disableSerialPortAccess".  
`displayName` |  `string` The human readable name.Mutable.  
`description` |  `string` Detailed description of what this constraint controls as well as how and where it is enforced.Mutable.  
`constraintDefault` |  `enum (`[ConstraintDefault](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#ConstraintDefault)`)` The evaluation behavior of this constraint in the absence of a policy.  
`supportsDryRun` |  `boolean` Shows if dry run is supported for this constraint or not.  
`equivalentConstraint` |  `string` Defines the equivalent constraint name, if it exists. Managed constraints can have an equivalent legacy managed constraint, and legacy managed constraints can have an equivalent managed constraint. For example, "constraints/iam.disableServiceAccountKeyUpload" is equivalent to "constraints/iam.managed.disableServiceAccountKeyUpload".  
`supportsSimulation` |  `boolean` Shows if simulation is supported for this constraint or not.  
Union field `constraint_type`. The type of restrictions for this `Constraint`.Immutable after creation. `constraint_type` can be only one of the following:  
`listConstraint` |  `object (`[ListConstraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#ListConstraint)`)` Defines this constraint as being a list constraint.  
`booleanConstraint` |  `object (`[BooleanConstraint](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#BooleanConstraint)`)` Defines this constraint as being a boolean constraint.  
  
## ConstraintDefault

Specifies the default behavior in the absence of any policy for the constraint. This must not be `CONSTRAINT_DEFAULT_UNSPECIFIED`.

Immutable after creation.

Enums  
---  
`CONSTRAINT_DEFAULT_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if set.  
`ALLOW` | Indicate that all values are allowed for list constraints. Indicate that enforcement is off for boolean constraints.  
`DENY` | Indicate that all values are denied for list constraints. Indicate that enforcement is on for boolean constraints.  
  
## ListConstraint

A constraint type that allows or disallows a list of string values, which are configured in the `[`PolicyRule`](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicyRule)`.

JSON representation  
---  
      
    
    {
      "supportsIn": boolean,
      "supportsUnder": boolean
    }  
  
Fields  
---  
`supportsIn` |  `boolean` Indicates whether values grouped into categories can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"in:Python"` would match any value in the 'Python' group.  
`supportsUnder` |  `boolean` Indicates whether subtrees of the Resource Manager resource hierarchy can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"under:folders/123"` would match any resource under the 'folders/123' folder.  
  
## BooleanConstraint

A constraint type is enforced or not enforced, which is configured in the `[`PolicyRule`](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicyRule)`.

If `customConstraintDefinition` is defined, this constraint is a managed constraint.

JSON representation  
---  
      
    
    {
      "customConstraintDefinition": {
        object ([CustomConstraintDefinition](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#CustomConstraintDefinition))
      }
    }  
  
Fields  
---  
`customConstraintDefinition` |  `object (`[CustomConstraintDefinition](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#CustomConstraintDefinition)`)` Custom constraint definition. Defines this as a managed constraint.  
  
## CustomConstraintDefinition

Custom constraint definition. Defines this as a managed constraint.

JSON representation  
---  
      
    
    {
      "resourceTypes": [
        string
      ],
      "methodTypes": [
        enum ([MethodType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#MethodType))
      ],
      "condition": string,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#ActionType)),
      "parameters": {
        string: {
          object ([Parameter](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Parameter))
        },
        ...
      }
    }  
  
Fields  
---  
`resourceTypes[]` |  `string` The resource instance type that this policy applies to, in the format `<service name>/<type>`. Example:

  * `compute.googleapis.com/Instance`.

  
`methodTypes[]` |  `enum (`[MethodType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#MethodType)`)` All the operations being applied for this constraint.  
`condition` |  `string` Org policy condition/expression. For example: `resource.instanceName.matches("(production|test)_(.+_)?[\d]+")` or, `resource.management.auto_upgrade == true`The max length of the condition is 1000 characters.  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#ActionType)`)` Allow or deny type.  
`parameters` |  `map (key: string, value: object (`[Parameter](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Parameter)`))` Stores the structure of `[`Parameters`](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Parameter)` used by the constraint condition. The key of `map` represents the name of the parameter.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## MethodType

The operation for which this constraint will be applied. To apply this constraint only when creating new resources, set `methodTypes` to `CREATE` only. To apply this constraint when creating or updating resources, set `methodTypes` to `CREATE` and `UPDATE`.

`UPDATE`-only custom constraints are not supported. Use `CREATE` or `CREATE, UPDATE`.

Enums  
---  
`METHOD_TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`CREATE` | Constraint applied when creating the resource.  
`UPDATE` | Constraint applied when updating the resource.  
`DELETE` | Constraint applied when deleting the resource. Not supported.  
`REMOVE_GRANT` | Constraint applied when removing an IAM grant.  
`GOVERN_TAGS` | Constraint applied when enforcing forced tagging.  
  
## ActionType

Allow or deny type.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`ALLOW` | Allowed action type.  
`DENY` | Deny action type.  
  
## Parameter

Defines a parameter structure.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Type)),
      "defaultValue": value,
      "validValuesExpr": string,
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Metadata))
      },
      "item": enum ([Type](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Type)`)` Type of the parameter.  
`defaultValue` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Sets the value of the parameter in an assignment if no value is given.  
`validValuesExpr` |  `string` Provides a CEL expression to specify the acceptable parameter values during assignment. For example, parameterName in ("parameterValue1", "parameterValue2").  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Metadata)`)` Defines subproperties primarily used by the UI to display user-friendly information.  
`item` |  `enum (`[Type](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse#Type)`)` Determines the parameter's value structure. For example, `LIST<STRING>` can be specified by defining `type: LIST`, and `item: STRING`.  
  
## Type

All valid types of parameter.

Enums  
---  
`TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`LIST` | List parameter type.  
`STRING` | String parameter type.  
`BOOLEAN` | Boolean parameter type.  
  
## Metadata

Defines Metadata structure.

JSON representation  
---  
      
    
    {
      "description": string
    }  
  
Fields  
---  
`description` |  `string` Detailed description of what this `parameter` is and its use. Mutable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
