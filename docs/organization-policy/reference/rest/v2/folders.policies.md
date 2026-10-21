---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies
title: REST Resource: folders.policies \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:39.024806+00:00
---

# REST Resource: folders.policies  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  REST Resource: folders.policies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Policy
    * JSON representation
    * PolicySpec
      * JSON representation
    * PolicyRule
      * JSON representation
    * StringValues
      * JSON representation
    * Expr
      * JSON representation
    * AlternatePolicySpec
      * JSON representation
  * Methods



## Resource: Policy

Defines an organization policy that is used to specify constraints for configurations of Google Cloud resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "spec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec))
      },
      "alternate": {
        object ([AlternatePolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.AlternatePolicySpec))
      },
      "dryRunSpec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint that this policy configures:

  * `projects/{project_number}/policies/{constraint_name}`
  * `folders/{folder_number}/policies/{constraint_name}`
  * `organizations/{organization_number}/policies/{constraint_name}`

For example, `projects/123/policies/compute.disableSerialPortAccess`.Note: `projects/{projectId}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number.  
`spec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec)`)` Basic information about the organization policy.  
`alternate  
**(deprecated)**` |  `object (`[AlternatePolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.AlternatePolicySpec)`)` This item is deprecated!Deprecated.  
`dryRunSpec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec)`)` Dry-run policy. Audit-only policy, can be used to monitor how the policy would have impacted the existing and future resources if it's enforced.  
`etag` |  `string` Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This entity tag (ETag) is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
  
### PolicySpec

Defines a Google Cloud policy specification that is used to specify constraints for configurations of Google Cloud resources.

JSON representation  
---  
      
    
    {
      "etag": string,
      "updateTime": string,
      "rules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicyRule))
        }
      ],
      "inheritFromParent": boolean,
      "reset": boolean
    }  
  
Fields  
---  
`etag` |  `string` An opaque tag indicating the current version of the policySpec, used for concurrency control.This field is ignored if used in a `policies.create` request.When the policy is returned from either a `policies.get` or a `policies.list` request, this entity tag (ETag) indicates the version of the current policySpec to use when executing a read-modify-write loop.When the policy is returned from a `policies.getEffectivePolicy` request, the ETag will be unset.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time stamp this was previously updated. This represents the last time a call to `policies.create` or `policies.patch` was made for that policy.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicyRule)`)` In policies for boolean constraints, the following requirements apply:

  * There must be exactly one policy rule where a condition is unset.
  * Boolean policy rules with conditions must set `enforced` to the opposite of the policy rule without a condition.
  * During policy evaluation, policy rules with conditions that are true for a target resource take precedence.

  
`inheritFromParent` |  `boolean` Determines the inheritance behavior for this policy.If `inheritFromParent` is true, policy rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the new root for evaluation. This field can be set only for policies that configure list constraints.  
`reset` |  `boolean` Ignores policies set above this resource and restores the `constraintDefault` enforcement behavior of the specific constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inheritFromParent` must be set to false.  
  
### PolicyRule

A rule used to express this policy.

JSON representation  
---  
      
    
    {
      "condition": {
        object ([Expr](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.Expr))
      },
      "parameters": {
        object
      },
    
      // Union field kind can be only one of the following:
      "values": {
        object ([StringValues](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.StringValues))
      },
      "allowAll": boolean,
      "denyAll": boolean,
      "enforce": boolean
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.Expr)`)` A condition that determines whether this rule is used to evaluate the policy.When set, the `[google.type.Expr.expression](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.Expr.FIELDS.expression)` field must contain 1 to 10 subexpressions, joined by the `||` or `&&` operators. Each subexpression must use the `resource.matchTag()`, `resource.matchTagId()`, `resource.hasTagKey()`, or `resource.hasTagKeyId()` Common Expression Language (CEL) function.The `resource.matchTag()` function takes the following arguments:

  * `key_name`: the namespaced name of the tag key, with the organization ID and a slash (`/`) as a prefix; for example, `123456789012/environment`
  * `value_name`: the short name of the tag value

For example: `resource.matchTag('123456789012/environment, 'prod')`The `resource.matchTagId()` function takes the following arguments:

  * `key_id`: the permanent ID of the tag key; for example, `tagKeys/123456789012`
  * `value_id`: the permanent ID of the tag value; for example, `tagValues/567890123456`

For example: `resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456')`The `resource.hasTagKey()` function takes the following argument:

  * `key_name`: the namespaced name of the tag key, with the organization ID and a slash (`/`) as a prefix; for example, `123456789012/environment`

For example: `resource.hasTagKey('123456789012/environment')`The `resource.hasTagKeyId()` function takes the following arguments:

  * `key_id`: the permanent ID of the tag key; for example, `tagKeys/123456789012`

For example: `resource.hasTagKeyId('tagKeys/123456789012')`  
`parameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Required for managed constraints if parameters are defined. Passes parameter values when policy enforcement is enabled. Ensure that parameter value types match those defined in the constraint definition. For example:
    
    
    {
      "allowedLocations" : ["us-east1", "us-west1"],
      "allowAll" : true
    }
      
  
Union field `kind`.`kind` can be only one of the following:  
`values` |  `object (`[StringValues](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.StringValues)`)` List of values to be used for this policy rule. This field can be set only in policies for list constraints.  
`allowAll` |  `boolean` Setting this to true means that all values are allowed. This field can be set only in policies for list constraints.  
`denyAll` |  `boolean` Setting this to true means that all values are denied. This field can be set only in policies for list constraints.  
`enforce` |  `boolean` If `true`, then the policy is enforced. If `false`, then any configuration is acceptable. This field can be set in policies for boolean constraints, custom constraints and managed constraints.  
  
### StringValues

A message that holds specific allowed and denied values. This message can define specific values and subtrees of the Resource Manager resource hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or denied. This is achieved by using the `under:` and optional `is:` prefixes. The `under:` prefix is used to denote resource subtree values. The `is:` prefix is used to denote specific values, and is required only if the value contains a ":". Values prefixed with "is:" are treated the same as values with no prefix. Ancestry subtrees must be in one of the following formats:

  * `projects/<project-id>` (for example, `projects/tokyo-rain-123`)
  * `folders/<folder-id>` (for example, `folders/1234`)
  * `organizations/<organization-id>` (for example, `organizations/1234`)



The `supportsUnder` field of the associated `Constraint` defines whether ancestry prefixes can be used.

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
`allowedValues[]` |  `string` List of values allowed at this resource.  
`deniedValues[]` |  `string` List of values denied at this resource.  
  
### Expr

Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at <https://github.com/google/cel-spec>.

Example (Comparison):
    
    
    title: "Summary size limit"
    description: "Determines if a summary is less than 100 chars"
    expression: "document.summary.size() < 100"
    

Example (Equality):
    
    
    title: "Requestor is owner"
    description: "Determines if requestor is the document owner"
    expression: "document.owner == request.auth.claims.email"
    

Example (Logic):
    
    
    title: "Public documents"
    description: "Determine whether the document should be publicly visible"
    expression: "document.type != 'private' && document.type != 'internal'"
    

Example (Data Manipulation):
    
    
    title: "Notification string"
    description: "Create a notification string with a timestamp."
    expression: "'New message received at ' + string(document.create_time)"
    

The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

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
`expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
  
### AlternatePolicySpec

Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run.

JSON representation  
---  
      
    
    {
      "launch": string,
      "spec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec))
      }
    }  
  
Fields  
---  
`launch` |  `string` Reference to the launch that will be used while audit logging and to control the launch. Set only in the alternate policy.  
`spec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec)`)` Specify constraint for configurations of Google Cloud resources.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/create)`

|  Creates a policy.  
  
### `[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/delete)`

|  Deletes a policy.  
  
### `[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/get)`

|  Gets a policy on a resource.  
  
### `[getEffectivePolicy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/getEffectivePolicy)`

|  Gets the effective policy on a resource.  
  
### `[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/list)`

|  Retrieves all of the policies that exist on a particular resource.  
  
### `[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/patch)`

|  Updates a policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
