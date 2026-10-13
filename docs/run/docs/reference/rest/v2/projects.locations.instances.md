---
url: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:33.657782+00:00
---

# REST Resource: projects.locations.instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Reference ](https://docs.cloud.google.com/run/docs/apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * RestartPolicy
  * ContainerStatus
    * JSON representation
  * Methods



## Resource: Instance

A Cloud Run Instance represents a single group of containers running in a region.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "uid": string,
      "generation": string,
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "expireTime": string,
      "creator": string,
      "lastModifier": string,
      "client": string,
      "clientVersion": string,
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/run/docs/reference/rest/v2/LaunchStage)),
      "binaryAuthorization": {
        object ([BinaryAuthorization](https://docs.cloud.google.com/run/docs/reference/rest/v2/BinaryAuthorization))
      },
      "vpcAccess": {
        object ([VpcAccess](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess))
      },
      "serviceAccount": string,
      "containers": [
        {
          object ([Container](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container))
        }
      ],
      "volumes": [
        {
          object ([Volume](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume))
        }
      ],
      "encryptionKey": string,
      "encryptionKeyRevocationAction": enum ([EncryptionKeyRevocationAction](https://docs.cloud.google.com/run/docs/reference/rest/v2/EncryptionKeyRevocationAction)),
      "encryptionKeyShutdownDuration": string,
      "nodeSelector": {
        object ([NodeSelector](https://docs.cloud.google.com/run/docs/reference/rest/v2/NodeSelector))
      },
      "ingress": enum ([IngressTraffic](https://docs.cloud.google.com/run/docs/reference/rest/v2/IngressTraffic)),
      "invokerIamDisabled": boolean,
      "defaultUriDisabled": boolean,
      "iapEnabled": boolean,
      "restartPolicy": enum ([RestartPolicy](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances#RestartPolicy)),
      "observedGeneration": string,
      "logUri": string,
      "terminalCondition": {
        object ([Condition](https://docs.cloud.google.com/run/docs/reference/rest/v2/Condition))
      },
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/run/docs/reference/rest/v2/Condition))
        }
      ],
      "containerStatuses": [
        {
          object ([ContainerStatus](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances#ContainerStatus))
        }
      ],
      "satisfiesPzs": boolean,
      "urls": [
        string
      ],
      "reconciling": boolean,
      "etag": string,
      "gpuZonalRedundancyDisabled": boolean
    }  
  
Fields  
---  
`name` |  `string` The fully qualified name of this Instance. In `CreateInstanceRequest`, this field is ignored, and instead composed from `CreateInstanceRequest.parent` and `CreateInstanceRequest.instance_id`.  
`description` |  `string` User-provided description of the Instance. This field currently has a 512-character limit.  
`uid` |  `string` Output only. Server assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A number that monotonically increases every time the user modifies the desired state. Please note that unlike v1, this is an `int64` value. As with most Google APIs, its JSON representation will be a `string` instead of an `integer`.  
`labels` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last-modified time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The deletion time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. For a deleted resource, the time after which it will be permamently deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creator` |  `string` Output only. Email address of the authenticated creator.  
`lastModifier` |  `string` Output only. Email address of the last authenticated modifier.  
`client` |  `string` Arbitrary identifier for the API client.  
`clientVersion` |  `string` Arbitrary version identifier for the API client.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/run/docs/reference/rest/v2/LaunchStage)`)` The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, `GA` is assumed. Set the launch stage to a preview stage on input to allow use of preview features in that stage. On read (or output), describes whether the resource uses preview features.For example, if `ALPHA` is provided as input, but only `BETA` and `GA`-level features are used, this field will be `BETA` on output.  
`binaryAuthorization` |  `object (`[BinaryAuthorization](https://docs.cloud.google.com/run/docs/reference/rest/v2/BinaryAuthorization)`)` Settings for the Binary Authorization feature.  
`vpcAccess` |  `object (`[VpcAccess](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess)`)` Optional. VPC Access configuration to use for this Revision. For more information, visit <https://cloud.google.com/run/docs/configuring/connecting-vpc>.  
`serviceAccount` |  `string`  
`containers[]` |  `object (`[Container](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container)`)` Required. Holds the single container that defines the unit of execution for this Instance.  
`volumes[]` |  `object (`[Volume](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume)`)` A list of Volumes to make available to containers.  
`encryptionKey` |  `string` A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to <https://cloud.google.com/run/docs/securing/using-cmek>  
`encryptionKeyRevocationAction` |  `enum (`[EncryptionKeyRevocationAction](https://docs.cloud.google.com/run/docs/reference/rest/v2/EncryptionKeyRevocationAction)`)` The action to take if the encryption key is revoked.  
`encryptionKeyShutdownDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` If `encryptionKeyRevocationAction` is `SHUTDOWN`, the duration before shutting down all instances. The minimum increment is 1 hour.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`nodeSelector` |  `object (`[NodeSelector](https://docs.cloud.google.com/run/docs/reference/rest/v2/NodeSelector)`)` Optional. The node selector for the instance.  
`ingress` |  `enum (`[IngressTraffic](https://docs.cloud.google.com/run/docs/reference/rest/v2/IngressTraffic)`)` Optional. Provides the ingress settings for this Instance. On output, returns the currently observed ingress settings, or `INGRESS_TRAFFIC_UNSPECIFIED` if no revision is active.  
`invokerIamDisabled` |  `boolean` Optional. Disables IAM permission check for `run.routes.invoke` for callers of this Instance. For more information, visit <https://cloud.google.com/run/docs/securing/managing-access#invoker_check>.  
`defaultUriDisabled` |  `boolean` Optional. Disables public resolution of the default URI of this Instance.  
`iapEnabled` |  `boolean` Optional. IAP settings on the Instance.  
`restartPolicy` |  `enum (`[RestartPolicy](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances#RestartPolicy)`)` Optional. Restart policy for the Instance.  
`observedGeneration` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The generation of this Instance currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. Please note that unlike v1, this is an `int64` value. As with most Google APIs, its JSON representation will be a `string` instead of an `integer`.  
`logUri` |  `string` Output only. The Google Console URI to obtain logs for the Instance.  
`terminalCondition` |  `object (`[Condition](https://docs.cloud.google.com/run/docs/reference/rest/v2/Condition)`)` Output only. The Condition of this Instance, containing its readiness status, and detailed error information in case it did not reach a serving state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/run/docs/reference/rest/v2/Condition)`)` Output only. The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Instance does not reach its Serving state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.  
`containerStatuses[]` |  `object (`[ContainerStatus](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances#ContainerStatus)`)` Output only. Status information for each of the specified containers. The status includes the resolved digest for specified images.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`urls[]` |  `string` Output only. All URLs serving traffic for this Instance.  
`reconciling` |  `boolean` Output only. Returns `true` if the Instance is currently being acted upon by the system to bring it into the desired state.When a new Instance is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Instance to the desired serving state. This process is called reconciliation. While reconciliation is in process, `observedGeneration` will have a transient value that might mismatch the intended state. Once reconciliation is over (and this field is `false`), there are two possible outcomes: reconciliation succeeded and the serving state matches the Instance, or there was an error, and reconciliation failed. This state can be found in `terminalCondition.state`.  
`etag` |  `string` Optional. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.  
`gpuZonalRedundancyDisabled` |  `boolean` Optional. True if GPU zonal redundancy is disabled on this instance.  
  
## RestartPolicy

Restart policy options for the instance. If not provided, the default is `ON_FAILURE`.

Enums  
---  
`RESTART_POLICY_UNSPECIFIED` | Unspecified restart policy.  
`ALWAYS` | Always restart the instance.  
`ON_FAILURE` | Restart if the instance terminates with non-zero exit code.  
`NEVER` | Never restart the instance.  
  
## ContainerStatus

ContainerStatus holds the information of container name and image digest value.

JSON representation  
---  
      
    
    {
      "name": string,
      "imageDigest": string
    }  
  
Fields  
---  
`name` |  `string` The name of the container, if specified.  
`imageDigest` |  `string` ImageDigest holds the resolved digest for the image specified and resolved during the creation of Revision. This field holds the digest value regardless of whether a tag or digest was originally specified in the Container object.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/create)`

|  Creates an Instance.  
  
### `[delete](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/delete)`

|  Deletes an Instance  
  
### `[get](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/get)`

|  Gets an Instance  
  
### `[getIamPolicy](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/getIamPolicy)`

|  Gets the IAM Access Control policy currently in effect for the given Instance.  
  
### `[list](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/list)`

|  Lists Instances.  
  
### `[patch](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/patch)`

|  Updates an Instance.  
  
### `[setIamPolicy](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/setIamPolicy)`

|  Sets the IAM Access control policy for the specified Instance.  
  
### `[start](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/start)`

|  Starts an Instance.  
  
### `[stop](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/stop)`

|  Stops an Instance.  
  
### `[testIamPermissions](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.instances/testIamPermissions)`

|  Returns permissions that a caller has on the specified Project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
