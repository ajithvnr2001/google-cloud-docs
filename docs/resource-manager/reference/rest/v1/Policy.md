---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy/
title: Policy \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:22.122459+00:00
---

# Policy  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Policy Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ListPolicy
    * JSON representation
  * AllValues
  * BooleanPolicy
    * JSON representation
  * RestoreDefault



Defines a Cloud Organization `Policy` which is used to specify `Constraints` for configurations of Cloud Platform resources.

JSON representation  
---  
      
    
    {
      "version": integer,
      "constraint": string,
      "etag": string,
      "updateTime": string,
    
      // Union field policy_type can be only one of the following:
      "listPolicy": {
        object ([ListPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#ListPolicy))
      },
      "booleanPolicy": {
        object ([BooleanPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#BooleanPolicy))
      },
      "restoreDefault": {
        object ([RestoreDefault](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#RestoreDefault))
      }
      // End of list of possible types for union field policy_type.
    }  
  
Fields  
---  
`version` |  `integer` Version of the `Policy`. Default version is 0;  
`constraint` |  `string` The name of the `Constraint` the `Policy` is configuring, for example, `constraints/serviceuser.services`.A [list of available constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) is available.Immutable after creation.  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` An opaque tag indicating the current version of the `Policy`, used for concurrency control.When the `Policy` is returned from either a `GetPolicy` or a `ListOrgPolicy` request, this `etag` indicates the version of the current `Policy` to use when executing a read-modify-write loop.When the `Policy` is returned from a `GetEffectivePolicy` request, the `etag` will be unset.When the `Policy` is used in a `projects.setOrgPolicy` method, use the `etag` value that was returned from a `projects.getOrgPolicy` request as part of a read-modify-write loop for concurrency control. Not setting the `etag`in a `projects.setOrgPolicy` request will result in an unconditional write of the `Policy`.A base64-encoded string.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time stamp the `Policy` was previously updated. This is set by the server, not specified by the caller, and represents the last time a call to `projects.setOrgPolicy` was made for that `Policy`. Any value set by the client will be ignored.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `policy_type`. The field to populate is based on the `constraint_type` value in the `Constraint`. `list_constraint` => `list_policy` `boolean_constraint` => `boolean_policy`A `restore_default` message may be used with any `Constraint` type.Providing a *_policy that is incompatible with the `constraint_type` will result in an `invalid_argument` error.Attempting to set a `Policy` with a `policy_type` not set will result in an `invalid_argument` error. `policy_type` can be only one of the following:  
`listPolicy` |  `object (`[ListPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#ListPolicy)`)` List of values either allowed or disallowed.  
`booleanPolicy` |  `object (`[BooleanPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#BooleanPolicy)`)` For boolean `Constraints`, whether to enforce the `Constraint` or not.  
`restoreDefault` |  `object (`[RestoreDefault](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#RestoreDefault)`)` Restores the default behavior of the constraint; independent of `Constraint` type.  
  
## ListPolicy

Used in `policyType` to specify how `listPolicy` behaves at this resource.

`ListPolicy` can define specific values and subtrees of Cloud Resource Manager resource hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or denied by setting the `allowedValues` and `deniedValues` fields. This is achieved by using the `under:` and optional `is:` prefixes. The `under:` prefix is used to denote resource subtree values. The `is:` prefix is used to denote specific values, and is required only if the value contains a ":". Values prefixed with "is:" are treated the same as values with no prefix. Ancestry subtrees must be in one of the following formats:

  * "projects/", e.g. "projects/tokyo-rain-123"
  * "folders/", e.g. "folders/1234"
  * "organizations/", e.g. "organizations/1234"



The `supportsUnder` field of the associated `Constraint` defines whether ancestry prefixes can be used. You can set `allowedValues` and `deniedValues` in the same `Policy` if `allValues` is `ALL_VALUES_UNSPECIFIED`. `ALLOW` or `DENY` are used to allow or deny all values. If `allValues` is set to either `ALLOW` or `DENY`, `allowedValues` and `deniedValues` must be unset.

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ],
      "allValues": enum ([AllValues](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#AllValues)),
      "suggestedValue": string,
      "inheritFromParent": boolean
    }  
  
Fields  
---  
`allowedValues[]` |  `string` List of values allowed at this resource. Can only be set if `allValues` is set to `ALL_VALUES_UNSPECIFIED`.  
`deniedValues[]` |  `string` List of values denied at this resource. Can only be set if `allValues` is set to `ALL_VALUES_UNSPECIFIED`.  
`allValues` |  `enum (`[AllValues](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#AllValues)`)` The policy allValues state.  
`suggestedValue` |  `string` Optional. The Google Cloud Console will try to default to a configuration that matches the value specified in this `Policy`. If `suggestedValue` is not set, it will inherit the value specified higher in the hierarchy, unless `inheritFromParent` is `false`.  
`inheritFromParent` |  `boolean` Determines the inheritance behavior for this `Policy`.By default, a `ListPolicy` set at a resource supersedes any `Policy` set anywhere up the resource hierarchy. However, if `inheritFromParent` is set to `true`, then the values from the effective `Policy` of the parent resource are inherited, meaning the values set in this `Policy` are added to the values inherited up the hierarchy.Setting `Policy` hierarchies that inherit both allowed values and denied values isn't recommended in most circumstances to keep the configuration simple and understandable. However, it is possible to set a `Policy` with `allowedValues` set that inherits a `Policy` with `deniedValues` set. In this case, the values that are allowed must be in `allowedValues` and not present in `deniedValues`.For example, suppose you have a `Constraint` `constraints/serviceuser.services`, which has a `constraint_type` of `listConstraint`, and with `constraintDefault` set to `ALLOW`. Suppose that at the Organization level, a `Policy` is applied that restricts the allowed API activations to {`E1`, `E2`}. Then, if a `Policy` is applied to a project below the Organization that has `inheritFromParent` set to `false` and field allValues set to DENY, then an attempt to activate any API will be denied.The following examples demonstrate different possible layerings for `projects/bar` parented by `organizations/foo`:Example 1 (no inherited values): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues:"E2"} `projects/bar` has `inheritFromParent` `false` and values: {allowedValues: "E3" allowedValues: "E4"} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are `E3`, and `E4`.Example 2 (inherited values): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues:"E2"} `projects/bar` has a `Policy` with values: {value: "E3" value: "E4" inheritFromParent: true} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are `E1`, `E2`, `E3`, and `E4`.Example 3 (inheriting both allowed and denied values): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues: "E2"} `projects/bar` has a `Policy` with: {deniedValues: "E1"} The accepted values at `organizations/foo` are `E1`, `E2`. The value accepted at `projects/bar` is `E2`.Example 4 (RestoreDefault): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues:"E2"} `projects/bar` has a `Policy` with values: {RestoreDefault: {}} The accepted values at `organizations/foo` are `E1`, `E2`. The accepted values at `projects/bar` are either all or none depending on the value of `constraintDefault` (if `ALLOW`, all; if `DENY`, none).Example 5 (no policy inherits parent policy): `organizations/foo` has no `Policy` set. `projects/bar` has no `Policy` set. The accepted values at both levels are either all or none depending on the value of `constraintDefault` (if `ALLOW`, all; if `DENY`, none).Example 6 (ListConstraint allowing all): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues: "E2"} `projects/bar` has a `Policy` with: {all: ALLOW} The accepted values at `organizations/foo` are `E1`, E2`. Any value is accepted at`projects/bar`.Example 7 (ListConstraint allowing none): `organizations/foo` has a `Policy` with values: {allowedValues: "E1" allowedValues: "E2"} `projects/bar` has a `Policy` with: {all: DENY} The accepted values at `organizations/foo` are `E1`, E2`. No value is accepted at`projects/bar`.Example 10 (allowed and denied subtrees of Resource Manager hierarchy): Given the following resource hierarchy O1->{F1, F2}; F1->{P1}; F2->{P2, P3}, `organizations/foo` has a `Policy` with values: {allowedValues: "under:organizations/O1"} `projects/bar` has a `Policy` with: {allowedValues: "under:projects/P3"} {deniedValues: "under:folders/F2"} The accepted values at `organizations/foo` are `organizations/O1`, `folders/F1`, `folders/F2`, `projects/P1`, `projects/P2`, `projects/P3`. The accepted values at `projects/bar` are `organizations/O1`, `folders/F1`, `projects/P1`.  
  
## AllValues

This enum can be used to set `Policies` that apply to all possible configuration values rather than specific values in `allowedValues` or `deniedValues`.

Setting this to `ALLOW` will mean this `Policy` allows all values. Similarly, setting it to `DENY` will mean no values are allowed. If set to either `ALLOW` or `DENY,`allowedValues`and`deniedValues` must be unset. Setting this to`ALL_VALUES_UNSPECIFIED`allows for setting`allowedValues`and`deniedValues`.

Enums  
---  
`ALL_VALUES_UNSPECIFIED` | Indicates that allowedValues or deniedValues must be set.  
`ALLOW` | A policy with this set allows all values.  
`DENY` | A policy with this set denies all values.  
  
## BooleanPolicy

Used in `policyType` to specify how `booleanPolicy` will behave at this resource.

JSON representation  
---  
      
    
    {
      "enforced": boolean
    }  
  
Fields  
---  
`enforced` |  `boolean` If `true`, then the `Policy` is enforced. If `false`, then any configuration is acceptable.Suppose you have a `Constraint` `constraints/compute.disableSerialPortAccess` with `constraintDefault` set to `ALLOW`. A `Policy` for that `Constraint` exhibits the following behavior: - If the `Policy` at this resource has enforced set to `false`, serial port connection attempts will be allowed. - If the `Policy` at this resource has enforced set to `true`, serial port connection attempts will be refused. - If the `Policy` at this resource is `RestoreDefault`, serial port connection attempts will be allowed. - If no `Policy` is set at this resource or anywhere higher in the resource hierarchy, serial port connection attempts will be allowed. - If no `Policy` is set at this resource, but one exists higher in the resource hierarchy, the behavior is as if the`Policy` were set at this resource.The following examples demonstrate the different possible layerings:Example 1 (nearest `Constraint` wins): `organizations/foo` has a `Policy` with: {enforced: false} `projects/bar` has no `Policy` set. The constraint at `projects/bar` and `organizations/foo` will not be enforced.Example 2 (enforcement gets replaced): `organizations/foo` has a `Policy` with: {enforced: false} `projects/bar` has a `Policy` with: {enforced: true} The constraint at `organizations/foo` is not enforced. The constraint at `projects/bar` is enforced.Example 3 (RestoreDefault): `organizations/foo` has a `Policy` with: {enforced: true} `projects/bar` has a `Policy` with: {RestoreDefault: {}} The constraint at `organizations/foo` is enforced. The constraint at `projects/bar` is not enforced, because `constraintDefault` for the `Constraint` is `ALLOW`.  
  
## RestoreDefault

This type has no fields.

Ignores policies set above this resource and restores the `constraintDefault` enforcement behavior of the specific `Constraint` at this resource.

Suppose that `constraintDefault` is set to `ALLOW` for the `Constraint` `constraints/serviceuser.services`. Suppose that organization foo.com sets a `Policy` at their Organization resource node that restricts the allowed service activations to deny all service activations. They could then set a `Policy` with the `policyType` `restoreDefault` on several experimental projects, restoring the `constraintDefault` enforcement of the `Constraint` for only those projects, allowing those projects to have all services activated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
