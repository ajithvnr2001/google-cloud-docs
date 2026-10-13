---
url: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets
title: REST Resource: projects.locations.ruleSets \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:14.909597+00:00
---

# REST Resource: projects.locations.ruleSets  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/document-warehouse/docs/reference/rest)



Send feedback 

#  REST Resource: projects.locations.ruleSets Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: RuleSet

Represents a set of rules from a single customer.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "source": string,
      "rules": [
        {
          object ([Rule](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Rule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the rule set. Managed internally. Format: projects/{projectNumber}/locations/{location}/ruleSet/{rule_set_id}.The name is ignored when creating a rule set.  
`description` |  `string` Short description of the rule-set.  
`source` |  `string` source of the rules i.e., customer name.  
`rules[]` |  `object (`[Rule](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Rule)`)` List of rules given by the customer.  
  
## Rule

Represents the rule for a content warehouse trigger.

JSON representation  
---  
      
    
    {
      "description": string,
      "ruleId": string,
      "triggerType": enum ([TriggerType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#TriggerType)),
      "condition": string,
      "actions": [
        {
          object ([Action](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Action))
        }
      ]
    }  
  
Fields  
---  
`description` |  `string` Short description of the rule and its context.  
`ruleId` |  `string` id of the rule. It has to be unique across all the examples. This is managed internally.  
`triggerType` |  `enum (`[TriggerType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#TriggerType)`)` Identifies the trigger type for running the policy.  
`condition` |  `string` Represents the conditional expression to be evaluated. Expression should evaluate to a boolean result. When the condition is true actions are executed. Example: user_role = "hsbc_role_1" AND doc.salary > 20000  
`actions[]` |  `object (`[Action](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Action)`)` List of actions that are executed when the rule is satisfied.  
  
## TriggerType

The trigger types for actions.

Enums  
---  
`UNKNOWN` | Trigger for unknown action.  
`ON_CREATE` | Trigger for create document action.  
`ON_UPDATE` | Trigger for update document action.  
`ON_CREATE_LINK` | Trigger for create link action.  
`ON_DELETE_LINK` | Trigger for delete link action.  
  
## Action

Represents the action triggered by Rule Engine when the rule is true.

JSON representation  
---  
      
    
    {
      "actionId": string,
    
      // Union field action can be only one of the following:
      "accessControl": {
        object ([AccessControlAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AccessControlAction))
      },
      "dataValidation": {
        object ([DataValidationAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#DataValidationAction))
      },
      "dataUpdate": {
        object ([DataUpdateAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#DataUpdateAction))
      },
      "addToFolder": {
        object ([AddToFolderAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AddToFolderAction))
      },
      "publishToPubSub": {
        object ([PublishAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#PublishAction))
      },
      "removeFromFolderAction": {
        object ([RemoveFromFolderAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#RemoveFromFolderAction))
      },
      "deleteDocumentAction": {
        object ([DeleteDocumentAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#DeleteDocumentAction))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
`actionId` |  `string` id of the action. Managed internally.  
Union field `action`.`action` can be only one of the following:  
`accessControl` |  `object (`[AccessControlAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AccessControlAction)`)` Action triggering access control operations.  
`dataValidation` |  `object (`[DataValidationAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#DataValidationAction)`)` Action triggering data validation operations.  
`dataUpdate` |  `object (`[DataUpdateAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#DataUpdateAction)`)` Action triggering data update operations.  
`addToFolder` |  `object (`[AddToFolderAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AddToFolderAction)`)` Action triggering create document link operation.  
`publishToPubSub` |  `object (`[PublishAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#PublishAction)`)` Action publish to Pub/Sub operation.  
`removeFromFolderAction` |  `object (`[RemoveFromFolderAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#RemoveFromFolderAction)`)` Action removing a document from a folder.  
`deleteDocumentAction` |  `object (`[DeleteDocumentAction](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#DeleteDocumentAction)`)` Action deleting the document.  
  
## AccessControlAction

Represents the action responsible for access control list management operations.

JSON representation  
---  
      
    
    {
      "operationType": enum ([OperationType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#OperationType)),
      "policy": {
        object ([Policy](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Policy))
      }
    }  
  
Fields  
---  
`operationType` |  `enum (`[OperationType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#OperationType)`)` Identifies the type of operation.  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Policy)`)` Represents the new policy from which bindings are added, removed or replaced based on the type of the operation. the policy is limited to a few 10s of KB.  
  
## OperationType

type of ACL modification operation.

Enums  
---  
`UNKNOWN` | The unknown operation type.  
`ADD_POLICY_BINDING` | Adds newly given policy bindings in the existing bindings list.  
`REMOVE_POLICY_BINDING` | Removes newly given policy bindings from the existing bindings list.  
`REPLACE_POLICY_BINDING` | Replaces existing policy bindings with the given policy binding list  
  
## Policy

An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources.

A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role.

For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

**JSON example:**
    
    
        {
          "bindings": [
            {
              "role": "roles/resourcemanager.organizationAdmin",
              "members": [
                "user:mike@example.com",
                "group:admins@example.com",
                "domain:google.com",
                "serviceAccount:my-project-id@appspot.gserviceaccount.com"
              ]
            },
            {
              "role": "roles/resourcemanager.organizationViewer",
              "members": [
                "user:eve@example.com"
              ],
              "condition": {
                "title": "expirable access",
                "description": "Does not grant access after Sep 2020",
                "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')",
              }
            }
          ],
          "etag": "BwWWja0YfJA=",
          "version": 3
        }
    

**YAML example:**
    
    
        bindings:
        - members:
          - user:mike@example.com
          - group:admins@example.com
          - domain:google.com
          - serviceAccount:my-project-id@appspot.gserviceaccount.com
          role: roles/resourcemanager.organizationAdmin
        - members:
          - user:eve@example.com
          role: roles/resourcemanager.organizationViewer
          condition:
            title: expirable access
            description: Does not grant access after Sep 2020
            expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
        etag: BwWWja0YfJA=
        version: 3
    

For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).

JSON representation  
---  
      
    
    {
      "version": integer,
      "bindings": [
        {
          object ([Binding](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Binding))
        }
      ],
      "auditConfigs": [
        {
          object ([AuditConfig](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AuditConfig))
        }
      ],
      "etag": string
    }  
  
Fields  
---  
`version` |  `integer` Specifies the format of the policy.Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:

  * Getting a policy that includes a conditional role binding
  * Adding a conditional role binding to a policy
  * Changing a conditional role binding in a policy
  * Removing any role binding, with or without a condition, from a policy that includes conditions

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).  
`bindings[]` |  `object (`[Binding](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Binding)`)` Associates a list of `members`, or principals, with a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one principal.The `bindings` in a `Policy` can refer to up to 1,500 principals; up to 250 of these principals can be Google groups. Each occurrence of a principal counts towards these limits. For example, if the `bindings` grant 50 different roles to `user:alice@example.com`, and not to any other principal, then you can add another 1,450 principals to the `bindings` in the `Policy`.  
`auditConfigs[]` |  `object (`[AuditConfig](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AuditConfig)`)` Specifies cloud audit logging configuration for this policy.  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.A base64-encoded string.  
  
## Binding

Associates `members`, or principals, with a `role`.

JSON representation  
---  
      
    
    {
      "role": string,
      "members": [
        string
      ],
      "condition": {
        object ([Expr](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Expr))
      }
    }  
  
Fields  
---  
`role` |  `string` role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`.  
`members[]` |  `string` Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values:

  * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.
  * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account. Does not include identities that come from external identity providers (IdPs) through identity federation.
  * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .


  * `serviceAccount:{emailid}`: An email address that represents a Google service account. For example, `my-other-app@appspot.gserviceaccount.com`.
  * `serviceAccount:{projectid}.svc.id.goog[{namespace}/{kubernetes-sa}]`: An identifier for a [Kubernetes service account](https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts). For example, `my-project.svc.id.goog[my-namespace/my-kubernetes-sa]`.
  * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.


  * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.


  * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.
  * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.
  * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.

  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Expr)`)` The condition that is associated with this binding.If the condition evaluates to `true`, then this binding applies to the current request.If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the principals in this binding.To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).  
  
## Expr

Represents a textual expression in the Common Expression language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at <https://github.com/google/cel-spec>.

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
    

Example (data Manipulation):
    
    
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
`expression` |  `string` Textual representation of an expression in Common Expression language syntax.  
`title` |  `string` Optional. title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`description` |  `string` Optional. description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
  
## AuditConfig

Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs.

If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exemptedMembers in each AuditLogConfig are exempted.

Example Policy with multiple AuditConfigs:
    
    
    {
      "auditConfigs": [
        {
          "service": "allServices",
          "auditLogConfigs": [
            {
              "logType": "DATA_READ",
              "exemptedMembers": [
                "user:jose@example.com"
              ]
            },
            {
              "logType": "DATA_WRITE"
            },
            {
              "logType": "ADMIN_READ"
            }
          ]
        },
        {
          "service": "sampleservice.googleapis.com",
          "auditLogConfigs": [
            {
              "logType": "DATA_READ"
            },
            {
              "logType": "DATA_WRITE",
              "exemptedMembers": [
                "user:aliya@example.com"
              ]
            }
          ]
        }
      ]
    }
    

For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

JSON representation  
---  
      
    
    {
      "service": string,
      "auditLogConfigs": [
        {
          object ([AuditLogConfig](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AuditLogConfig))
        }
      ]
    }  
  
Fields  
---  
`service` |  `string` Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.  
`auditLogConfigs[]` |  `object (`[AuditLogConfig](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#AuditLogConfig)`)` The configuration for logging of each type of permission.  
  
## AuditLogConfig

Provides the configuration for logging a type of permissions. Example:
    
    
    {
      "auditLogConfigs": [
        {
          "logType": "DATA_READ",
          "exemptedMembers": [
            "user:jose@example.com"
          ]
        },
        {
          "logType": "DATA_WRITE"
        }
      ]
    }
    

This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting [jose@example.com](mailto:jose@example.com) from DATA_READ logging.

JSON representation  
---  
      
    
    {
      "logType": enum ([LogType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#LogType)),
      "exemptedMembers": [
        string
      ]
    }  
  
Fields  
---  
`logType` |  `enum (`[LogType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#LogType)`)` The log type that this config enables.  
`exemptedMembers[]` |  `string` Specifies the identities that do not cause logging for this type of permission. Follows the same format of `[Binding.members](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets#Binding.FIELDS.members)`.  
  
## LogType

The list of valid permission types for which logging can be configured. Admin writes are always logged, and are not configurable.

Enums  
---  
`LOG_TYPE_UNSPECIFIED` | Default case. Should never be this.  
`ADMIN_READ` | Admin reads. Example: CloudIAM getIamPolicy  
`DATA_WRITE` | data writes. Example: CloudSQL Users create  
`DATA_READ` | data reads. Example: CloudSQL Users list  
  
## DataValidationAction

Represents the action responsible for data validation operations.

JSON representation  
---  
      
    
    {
      "conditions": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`conditions` |  `map (key: string, value: string)` Map of (K, V) -> (field, string condition to be evaluated on the field) E.g., ("age", "age > 18 && age < 60") entry triggers validation of field age with the given condition. Map entries will be ANDed during validation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## DataUpdateAction

Represents the action responsible for properties update operations.

JSON representation  
---  
      
    
    {
      "entries": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`entries` |  `map (key: string, value: string)` Map of (K, V) -> (valid name of the field, new value of the field) E.g., ("age", "60") entry triggers update of field age with a value of 60. If the field is not present then new entry is added. During update action execution, value strings will be casted to appropriate types.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## AddToFolderAction

Represents the action responsible for adding document under a folder.

JSON representation  
---  
      
    
    {
      "folders": [
        string
      ]
    }  
  
Fields  
---  
`folders[]` |  `string` Names of the folder under which new document is to be added. Format: projects/{projectNumber}/locations/{location}/documents/{documentId}.  
  
## PublishAction

Represents the action responsible for publishing messages to a Pub/Sub topic.

JSON representation  
---  
      
    
    {
      "topicId": string,
      "messages": [
        string
      ]
    }  
  
Fields  
---  
`topicId` |  `string` The topic id in the Pub/Sub service for which messages will be published to.  
`messages[]` |  `string` Messages to be published.  
  
## RemoveFromFolderAction

Represents the action responsible for remove a document from a specific folder.

JSON representation  
---  
      
    
    {
      "condition": string,
      "folder": string
    }  
  
Fields  
---  
`condition` |  `string` Condition of the action to be executed.  
`folder` |  `string` name of the folder under which new document is to be added. Format: projects/{projectNumber}/locations/{location}/documents/{documentId}.  
  
## DeleteDocumentAction

Represents the action responsible for deleting the document.

JSON representation  
---  
      
    
    {
      "enableHardDelete": boolean
    }  
  
Fields  
---  
`enableHardDelete` |  `boolean` Boolean field to select between hard vs soft delete options. Set 'true' for 'hard delete' and 'false' for 'soft delete'.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets/create)`

|  Creates a ruleset.  
  
### `[delete](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets/delete)`

|  Deletes a ruleset.  
  
### `[get](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets/get)`

|  Gets a ruleset.  
  
### `[list](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets/list)`

|  Lists rulesets.  
  
### `[patch](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets/patch)`

|  Updates a ruleset.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
