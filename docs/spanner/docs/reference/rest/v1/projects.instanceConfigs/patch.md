---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/patch/
title: Method: projects.instanceConfigs.patch \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:00.022136+00:00
---

# Method: projects.instanceConfigs.patch  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instanceConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates an instance configuration. The returned long-running operation can be used to track the progress of updating the instance. If the named instance configuration does not exist, returns `NOT_FOUND`.

Only user-managed configurations can be updated.

Immediately after the request returns:

  * The instance configuration's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig.FIELDS.reconciling)` field is set to true.



While the operation is pending:

  * Cancelling the operation sets its metadata's `[cancelTime](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateInstanceConfigMetadata#FIELDS.cancel_time)`. The operation is guaranteed to succeed at undoing all changes, after which point it terminates with a `CANCELLED` status.
  * All other attempts to modify the instance configuration are rejected.
  * Reading the instance configuration via the API continues to give the pre-request values.



Upon completion of the returned operation:

  * Creating instances using the instance configuration uses the new values.
  * The new values of the instance configuration are readable via the API.
  * The instance configuration's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig.FIELDS.reconciling)` field becomes false.



The returned long-running operation will have a name of the format `<instance_config_name>/operations/<operationId>` and can be used to track the instance configuration modification. The metadata field type is `[UpdateInstanceConfigMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateInstanceConfigMetadata)`. The response field type is `[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)`, if successful.

Authorization requires `spanner.instanceConfigs.update` permission on the resource `[name](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig.FIELDS.name)`.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`PATCH https://spanner.googleapis.com/v1/{instanceConfig.name=projects/*/instanceConfigs/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`instanceConfig.name` |  `string` A unique identifier for the instance configuration. Values are of the form `projects/<project>/instanceConfigs/[a-z][-a-z0-9]*`.User instance configuration must start with `custom-`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instanceConfig": {
        "name": string,
        "displayName": string,
        "configType": enum ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#Type)),
        "replicas": [
          {
            "location": string,
            "type": enum ([ReplicaType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#ReplicaType)),
            "defaultLeaderLocation": boolean
          }
        ],
        "optionalReplicas": [
          {
            "location": string,
            "type": enum ([ReplicaType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#ReplicaType)),
            "defaultLeaderLocation": boolean
          }
        ],
        "baseConfig": string,
        "labels": {
          string: string,
          ...
        },
        "etag": string,
        "leaderOptions": [
          string
        ],
        "reconciling": boolean,
        "state": enum ([State](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#State)),
        "freeInstanceAvailability": enum ([FreeInstanceAvailability](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#FreeInstanceAvailability)),
        "quorumType": enum ([QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#QuorumType)),
        "storageLimitPerProcessingUnit": string
      },
      "updateMask": string,
      "validateOnly": boolean
    }  
  
Fields  
---  
`instanceConfig.displayName` |  `string` The name of this instance configuration as it appears in UIs.  
`instanceConfig.configType` |  `enum (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#Type)`)` Output only. Whether this instance configuration is a Google-managed or user-managed configuration.  
`instanceConfig.replicas[]` |  `object (`[ReplicaInfo](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#ReplicaInfo)`)` The geographic placement of nodes in this instance configuration and their replication properties.To create user-managed configurations, input `replicas` must include all replicas in `replicas` of the `baseConfig` and include one or more replicas in the `optionalReplicas` of the `baseConfig`.  
`instanceConfig.optionalReplicas[]` |  `object (`[ReplicaInfo](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#ReplicaInfo)`)` Output only. The available optional replicas to choose from for user-managed configurations. Populated for Google-managed configurations.  
`instanceConfig.baseConfig` |  `string` Base configuration name, e.g. projects//instanceConfigs/nam3, based on which this configuration is created. Only set for user-managed configurations. `baseConfig` must refer to a configuration of type `GOOGLE_MANAGED` in the same project as this configuration.  
`instanceConfig.labels` |  `map (key: string, value: string)` Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. Cloud Labels can be used to filter collections of resources. They can be used to control how resource metrics are aggregated. And they can be used as arguments to policy management rules (e.g. route, firewall, load balancing, etc.).

  * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z][a-z0-9_-]{0,62}`.
  * Label values must be between 0 and 63 characters long and must conform to the regular expression `[a-z0-9_-]{0,63}`.
  * No more than 64 labels can be associated with a given resource.

See <https://goo.gl/xmQnxf> for more information on and examples of labels.If you plan to use labels in your own code, please note that additional characters may be allowed in the future. Therefore, you are advised to use an internal label representation, such as JSON, which doesn't rely upon specific characters being disallowed. For example, representing labels as the string: name + "_" + value would prove problematic if we were to allow "_" in a future release.  
`instanceConfig.etag` |  `string` etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance configuration from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance configuration updates in order to avoid race conditions: An etag is returned in the response which contains instance configurations, and systems are expected to put that etag in the request to update instance configuration to ensure that their change is applied to the same version of the instance configuration. If no etag is provided in the call to update the instance configuration, then the existing instance configuration is overwritten blindly.  
`instanceConfig.leaderOptions[]` |  `string` Allowed values of the "defaultLeader" schema option for databases in instances that use this instance configuration.  
`instanceConfig.reconciling` |  `boolean` Output only. If true, the instance configuration is being created or updated. If false, there are no ongoing operations for the instance configuration.  
`instanceConfig.state` |  `enum (`[State](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#State)`)` Output only. The current instance configuration state. Applicable only for `USER_MANAGED` configurations.  
`instanceConfig.freeInstanceAvailability` |  `enum (`[FreeInstanceAvailability](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#FreeInstanceAvailability)`)` Output only. Describes whether free instances are available to be created in this instance configuration.  
`instanceConfig.quorumType` |  `enum (`[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#QuorumType)`)` Output only. The `QuorumType` of the instance configuration.  
`instanceConfig.storageLimitPerProcessingUnit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The storage limit in bytes per processing unit.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. A mask specifying which fields in `[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)` should be updated. The field mask must always be specified; this prevents any future fields in `[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)` from being erased accidentally by clients that do not know about them. Only displayName and labels can be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`validateOnly` |  `boolean` An option to validate, but not actually execute, a request, and provide the same response.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
