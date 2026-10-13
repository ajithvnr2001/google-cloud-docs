---
url: https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/deployments/setIamPolicy/
title: Deployments: setIamPolicy \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:39.622581+00:00
---

# Deployments: setIamPolicy  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/deployments/setIamPolicy/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Deployments: setIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Requires authorization.

Sets the access control policy on the specified resource. Replaces any existing policy. Try it now. 

## Request

### HTTP request
    
    
    POST https://www.googleapis.com/deploymentmanager/v2beta/projects/project/global/deployments/resource/setIamPolicy

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`project` | `string` |  Project ID for this request.   
`resource` | `string` |  Name or id of the resource for this request.   
  
### Authorization

This request requires authorization with at least one of the following scopes:

Scope  
---  
`https://www.googleapis.com/auth/cloud-platform`  
`https://www.googleapis.com/auth/ndev.cloudman`  
  
### Request body

In the request body, supply data with the following structure:
    
    
    {
      "policy": {
        "version": integer,
        "bindings": [
          {
            "role": string,
            "members": [
              string
            ],
            "condition": {
              "expression": string,
              "title": string,
              "description": string,
              "location": string
            }
          }
        ],
        "auditConfigs": [
          {
            "service": string,
            "exemptedMembers": [
              string
            ],
            "auditLogConfigs": [
              {
                "logType": string,
                "exemptedMembers": [
                  string
                ],
                "ignoreChildExemptions": boolean
              }
            ]
          }
        ],
        "rules": [
          {
            "description": string,
            "permissions": [
              string
            ],
            "action": string,
            "ins": [
              string
            ],
            "notIns": [
              string
            ],
            "conditions": [
              {
                "iam": string,
                "sys": string,
                "svc": string,
                "op": string,
                "values": [
                  string
                ]
              }
            ],
            "logConfigs": [
              {
                "counter": {
                  "metric": string,
                  "field": string,
                  "customFields": [
                    {
                      "name": string,
                      "value": string
                    }
                  ]
                },
                "dataAccess": {
                  "logMode": string
                },
                "cloudAudit": {
                  "logName": string,
                  "authorizationLoggingOptions": {
                    "permissionType": string
                  }
                }
              }
            ]
          }
        ],
        "etag": bytes,
        "iamOwned": boolean
      },
      "bindings": [
        {
          "role": string,
          "members": [
            string
          ],
          "condition": {
            "expression": string,
            "title": string,
            "description": string,
            "location": string
          }
        }
      ],
      "etag": bytes
    }

Property name | Value | Description | Notes  
---|---|---|---  
`policy` | `nested object` | REQUIRED: The complete policy to be applied to the 'resource'. The size of the policy is limited to a few 10s of KB. An empty policy is in general a valid policy but certain services (like Projects) might reject them. |   
`policy.version` | `integer` | Specifies the format of the policy.   
  
Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.   
  
Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:   
  
* Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions   
  
**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.   
  
If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.   
  
To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).   
  
|   
`policy.bindings[]` | `list` | Associates a list of `members` to a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one member. |   
`policy.bindings[].role` | `string` | Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. |   
`policy.bindings[].members[]` | `list` | Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values:   
  
* `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.   
  
* `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.   
  
* `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .   
  
  
  
* `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.   
  
* `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.   
  
* `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.   
  
* `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.   
  
* `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.   
  
  
  
* `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.   
  
  
  
  
  
  
  
|   
`policy.bindings[].condition` | `nested object` | The condition that is associated with this binding.   
  
If the condition evaluates to `true`, then this binding applies to the current request.   
  
If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the members in this binding.   
  
To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). |   
`policy.bindings[].condition.expression` | `string` | Textual representation of an expression in Common Expression Language syntax. |   
`policy.bindings[].condition.title` | `string` | Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. |   
`policy.bindings[].condition.description` | `string` | Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. |   
`policy.bindings[].condition.location` | `string` | Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. |   
`policy.auditConfigs[]` | `list` | Specifies cloud audit logging configuration for this policy.   
  
|   
`policy.auditConfigs[].service` | `string` | Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. |   
`policy.auditConfigs[].exemptedMembers[]` | `list` |   
  
|   
`policy.auditConfigs[].auditLogConfigs[]` | `list` | The configuration for logging of each type of permission. |   
`policy.auditConfigs[].auditLogConfigs[].logType` | `string` | The log type that this config enables. |   
`policy.auditConfigs[].auditLogConfigs[].exemptedMembers[]` | `list` | Specifies the identities that do not cause logging for this type of permission. Follows the same format of [Binding.members][]. |   
`policy.auditConfigs[].auditLogConfigs[].ignoreChildExemptions` | `boolean` |   
  
|   
`policy.rules[]` | `list` | If more than one rule is specified, the rules are applied in the following manner: - All matching LOG rules are always applied. - If any DENY/DENY_WITH_LOG rule matches, permission is denied. Logging will be applied if one or more matching rule requires logging. - Otherwise, if any ALLOW/ALLOW_WITH_LOG rule matches, permission is granted. Logging will be applied if one or more matching rule requires logging. - Otherwise, if no rule applies, permission is denied. |   
`policy.rules[].description` | `string` | Human-readable description of the rule. |   
`policy.rules[].permissions[]` | `list` | A permission is a string of form '..' (e.g., 'storage.buckets.list'). A value of '*' matches all permissions, and a verb part of '*' (e.g., 'storage.buckets.*') matches all verbs.   
  
|   
`policy.rules[].action` | `string` | Required |   
`policy.rules[].ins[]` | `list` | If one or more 'in' clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in at least one of these entries. |   
`policy.rules[].notIns[]` | `list` | If one or more 'not_in' clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in none of the entries. |   
`policy.rules[].conditions[]` | `list` | Additional restrictions that must be met. All conditions must pass for the rule to match. |   
`policy.rules[].conditions[].iam` | `string` | Trusted attributes supplied by the IAM system. |   
`policy.rules[].conditions[].sys` | `string` | Trusted attributes supplied by any service that owns resources and uses the IAM system for access control. |   
`policy.rules[].conditions[].svc` | `string` | Trusted attributes discharged by the service. |   
`policy.rules[].conditions[].op` | `string` | An operator to apply the subject with. |   
`policy.rules[].conditions[].values[]` | `list` | The objects of the condition. |   
`policy.rules[].logConfigs[]` | `list` | The config returned to callers of tech.iam.IAM.CheckPolicy for any entries that match the LOG action. |   
`policy.rules[].logConfigs[].counter` | `nested object` | Counter options. |   
`policy.rules[].logConfigs[].counter.metric` | `string` | The metric to update. |   
`policy.rules[].logConfigs[].counter.field` | `string` | The field value to attribute. |   
`policy.rules[].logConfigs[].counter.customFields[]` | `list` | Custom fields. |   
`policy.rules[].logConfigs[].counter.customFields[].name` | `string` | Name is the field name. |   
`policy.rules[].logConfigs[].counter.customFields[].value` | `string` | Value is the field value. It is important that in contrast to the CounterOptions.field, the value here is a constant that is not derived from the IAMContext. |   
`policy.rules[].logConfigs[].dataAccess` | `nested object` | Data access options. |   
`policy.rules[].logConfigs[].dataAccess.logMode` | `string` |   
  
|   
`policy.rules[].logConfigs[].cloudAudit` | `nested object` | Cloud audit options. |   
`policy.rules[].logConfigs[].cloudAudit.logName` | `string` | The log_name to populate in the Cloud Audit Record.   
  
|   
`policy.rules[].logConfigs[].cloudAudit.authorizationLoggingOptions` | `nested object` | Information used by the Cloud Audit Logging pipeline. |   
`policy.rules[].logConfigs[].cloudAudit.authorizationLoggingOptions.permissionType` | `string` | The type of the permission that was checked. |   
`policy.etag` | `bytes` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.   
  
**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. |   
`policy.iamOwned` | `boolean` |   
  
|   
`bindings[]` | `list` | Flatten Policy to create a backward compatible wire-format. Deprecated. Use 'policy' to specify bindings. |   
`bindings[].role` | `string` | Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. |   
`bindings[].members[]` | `list` | Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values:   
  
* `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.   
  
* `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.   
  
* `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .   
  
  
  
* `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.   
  
* `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.   
  
* `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.   
  
* `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.   
  
* `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.   
  
  
  
* `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.   
  
  
  
  
  
  
  
|   
`bindings[].condition` | `nested object` | The condition that is associated with this binding.   
  
If the condition evaluates to `true`, then this binding applies to the current request.   
  
If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the members in this binding.   
  
To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). |   
`bindings[].condition.expression` | `string` | Textual representation of an expression in Common Expression Language syntax. |   
`bindings[].condition.title` | `string` | Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. |   
`bindings[].condition.description` | `string` | Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. |   
`bindings[].condition.location` | `string` | Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. |   
`etag` | `bytes` | Flatten Policy to create a backward compatible wire-format. Deprecated. Use 'policy' to specify the etag. |   
  
## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "version": integer,
      "bindings": [
        {
          "role": string,
          "members": [
            string
          ],
          "condition": {
            "expression": string,
            "title": string,
            "description": string,
            "location": string
          }
        }
      ],
      "auditConfigs": [
        {
          "service": string,
          "exemptedMembers": [
            string
          ],
          "auditLogConfigs": [
            {
              "logType": string,
              "exemptedMembers": [
                string
              ],
              "ignoreChildExemptions": boolean
            }
          ]
        }
      ],
      "rules": [
        {
          "description": string,
          "permissions": [
            string
          ],
          "action": string,
          "ins": [
            string
          ],
          "notIns": [
            string
          ],
          "conditions": [
            {
              "iam": string,
              "sys": string,
              "svc": string,
              "op": string,
              "values": [
                string
              ]
            }
          ],
          "logConfigs": [
            {
              "counter": {
                "metric": string,
                "field": string,
                "customFields": [
                  {
                    "name": string,
                    "value": string
                  }
                ]
              },
              "dataAccess": {
                "logMode": string
              },
              "cloudAudit": {
                "logName": string,
                "authorizationLoggingOptions": {
                  "permissionType": string
                }
              }
            }
          ]
        }
      ],
      "etag": bytes,
      "iamOwned": boolean
    }

Property name | Value | Description | Notes  
---|---|---|---  
`version` | `integer` | Specifies the format of the policy.   
  
Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.   
  
Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:   
  
* Getting a policy that includes a conditional role binding * Adding a conditional role binding to a policy * Changing a conditional role binding in a policy * Removing any role binding, with or without a condition, from a policy that includes conditions   
  
**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.   
  
If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.   
  
To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).   
  
|   
`bindings[]` | `list` | Associates a list of `members` to a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one member. |   
`bindings[].role` | `string` | Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. |   
`bindings[].members[]` | `list` | Specifies the identities requesting access for a Cloud Platform resource. `members` can have the following values:   
  
* `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.   
  
* `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.   
  
* `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .   
  
  
  
* `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.   
  
* `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.   
  
* `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.   
  
* `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.   
  
* `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.   
  
  
  
* `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.   
  
  
  
  
  
  
  
|   
`bindings[].condition` | `nested object` | The condition that is associated with this binding.   
  
If the condition evaluates to `true`, then this binding applies to the current request.   
  
If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the members in this binding.   
  
To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). |   
`bindings[].condition.expression` | `string` | Textual representation of an expression in Common Expression Language syntax. |   
`bindings[].condition.title` | `string` | Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. |   
`bindings[].condition.description` | `string` | Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. |   
`bindings[].condition.location` | `string` | Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. |   
`auditConfigs[]` | `list` | Specifies cloud audit logging configuration for this policy.   
  
|   
`auditConfigs[].service` | `string` | Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. |   
`auditConfigs[].exemptedMembers[]` | `list` |   
  
|   
`auditConfigs[].auditLogConfigs[]` | `list` | The configuration for logging of each type of permission. |   
`auditConfigs[].auditLogConfigs[].logType` | `string` | The log type that this config enables. |   
`auditConfigs[].auditLogConfigs[].exemptedMembers[]` | `list` | Specifies the identities that do not cause logging for this type of permission. Follows the same format of [Binding.members][]. |   
`auditConfigs[].auditLogConfigs[].ignoreChildExemptions` | `boolean` |   
  
|   
`rules[]` | `list` | If more than one rule is specified, the rules are applied in the following manner: - All matching LOG rules are always applied. - If any DENY/DENY_WITH_LOG rule matches, permission is denied. Logging will be applied if one or more matching rule requires logging. - Otherwise, if any ALLOW/ALLOW_WITH_LOG rule matches, permission is granted. Logging will be applied if one or more matching rule requires logging. - Otherwise, if no rule applies, permission is denied. |   
`rules[].description` | `string` | Human-readable description of the rule. |   
`rules[].permissions[]` | `list` | A permission is a string of form '..' (e.g., 'storage.buckets.list'). A value of '*' matches all permissions, and a verb part of '*' (e.g., 'storage.buckets.*') matches all verbs.   
  
|   
`rules[].action` | `string` | Required |   
`rules[].ins[]` | `list` | If one or more 'in' clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in at least one of these entries. |   
`rules[].notIns[]` | `list` | If one or more 'not_in' clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in none of the entries. |   
`rules[].conditions[]` | `list` | Additional restrictions that must be met. All conditions must pass for the rule to match. |   
`rules[].conditions[].iam` | `string` | Trusted attributes supplied by the IAM system. |   
`rules[].conditions[].sys` | `string` | Trusted attributes supplied by any service that owns resources and uses the IAM system for access control. |   
`rules[].conditions[].svc` | `string` | Trusted attributes discharged by the service. |   
`rules[].conditions[].op` | `string` | An operator to apply the subject with. |   
`rules[].conditions[].values[]` | `list` | The objects of the condition. |   
`rules[].logConfigs[]` | `list` | The config returned to callers of tech.iam.IAM.CheckPolicy for any entries that match the LOG action. |   
`rules[].logConfigs[].counter` | `nested object` | Counter options. |   
`rules[].logConfigs[].counter.metric` | `string` | The metric to update. |   
`rules[].logConfigs[].counter.field` | `string` | The field value to attribute. |   
`rules[].logConfigs[].counter.customFields[]` | `list` | Custom fields. |   
`rules[].logConfigs[].counter.customFields[].name` | `string` | Name is the field name. |   
`rules[].logConfigs[].counter.customFields[].value` | `string` | Value is the field value. It is important that in contrast to the CounterOptions.field, the value here is a constant that is not derived from the IAMContext. |   
`rules[].logConfigs[].dataAccess` | `nested object` | Data access options. |   
`rules[].logConfigs[].dataAccess.logMode` | `string` |   
  
|   
`rules[].logConfigs[].cloudAudit` | `nested object` | Cloud audit options. |   
`rules[].logConfigs[].cloudAudit.logName` | `string` | The log_name to populate in the Cloud Audit Record.   
  
|   
`rules[].logConfigs[].cloudAudit.authorizationLoggingOptions` | `nested object` | Information used by the Cloud Audit Logging pipeline. |   
`rules[].logConfigs[].cloudAudit.authorizationLoggingOptions.permissionType` | `string` | The type of the permission that was checked. |   
`etag` | `bytes` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.   
  
**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. |   
`iamOwned` | `boolean` |   
  
|   
  
## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
