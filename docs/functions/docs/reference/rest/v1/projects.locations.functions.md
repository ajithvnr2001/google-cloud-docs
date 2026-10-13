---
url: https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions
title: REST Resource: projects.locations.functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:14.375201+00:00
---

# REST Resource: projects.locations.functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback 

#  REST Resource: projects.locations.functions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CloudFunction
    * JSON representation
  * SourceRepository
    * JSON representation
  * HttpsTrigger
    * JSON representation
  * SecurityLevel
  * EventTrigger
    * JSON representation
  * FailurePolicy
    * JSON representation
  * Retry
  * CloudFunctionStatus
  * VpcConnectorEgressSettings
  * IngressSettings
  * SecretEnvVar
    * JSON representation
  * SecretVolume
    * JSON representation
  * SecretVersion
    * JSON representation
  * DockerRegistry
  * AutomaticUpdatePolicy
  * OnDeployUpdatePolicy
    * JSON representation
  * Methods



## Resource: CloudFunction

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulate function and triggers configurations.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "status": enum ([CloudFunctionStatus](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#CloudFunctionStatus)),
      "entryPoint": string,
      "runtime": string,
      "timeout": string,
      "availableMemoryMb": integer,
      "serviceAccountEmail": string,
      "updateTime": string,
      "versionId": string,
      "labels": {
        string: string,
        ...
      },
      "environmentVariables": {
        string: string,
        ...
      },
      "buildEnvironmentVariables": {
        string: string,
        ...
      },
      "network": string,
      "maxInstances": integer,
      "minInstances": integer,
      "vpcConnector": string,
      "vpcConnectorEgressSettings": enum ([VpcConnectorEgressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#VpcConnectorEgressSettings)),
      "ingressSettings": enum ([IngressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#IngressSettings)),
      "kmsKeyName": string,
      "buildWorkerPool": string,
      "buildId": string,
      "buildName": string,
      "secretEnvironmentVariables": [
        {
          object ([SecretEnvVar](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecretEnvVar))
        }
      ],
      "secretVolumes": [
        {
          object ([SecretVolume](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecretVolume))
        }
      ],
      "sourceToken": string,
      "dockerRepository": string,
      "dockerRegistry": enum ([DockerRegistry](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#DockerRegistry)),
      "buildServiceAccount": string,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
    
      // Union field source_code can be only one of the following:
      "sourceArchiveUrl": string,
      "sourceRepository": {
        object ([SourceRepository](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SourceRepository))
      },
      "sourceUploadUrl": string
      // End of list of possible types for union field source_code.
    
      // Union field trigger can be only one of the following:
      "httpsTrigger": {
        object ([HttpsTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#HttpsTrigger))
      },
      "eventTrigger": {
        object ([EventTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#EventTrigger))
      }
      // End of list of possible types for union field trigger.
    
      // Union field runtime_update_policy can be only one of the following:
      "automaticUpdatePolicy": {
        object ([AutomaticUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#AutomaticUpdatePolicy))
      },
      "onDeployUpdatePolicy": {
        object ([OnDeployUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#OnDeployUpdatePolicy))
      }
      // End of list of possible types for union field runtime_update_policy.
    }  
  
Fields  
---  
`name` |  `string` A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*`  
`description` |  `string` User-provided description of a function.  
`status` |  `enum (`[CloudFunctionStatus](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#CloudFunctionStatus)`)` Output only. Status of the function deployment.  
`entryPoint` |  `string` The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix (ID of the function), if not specified.  
`runtime` |  `string` The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`availableMemoryMb` |  `integer` The amount of memory in MB available for a function. Defaults to 256MB.  
`serviceAccountEmail` |  `string` The email of the function's service account. If empty, defaults to `{projectId}@appspot.gserviceaccount.com`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of a Cloud Function.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`versionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The version identifier of the Cloud Function. Each deployment attempt results in a new version of a function being created.  
`labels` |  `map (key: string, value: string)` Labels associated with this Cloud Function.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`environmentVariables` |  `map (key: string, value: string)` Environment variables that shall be available during function execution.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`buildEnvironmentVariables` |  `map (key: string, value: string)` Build environment variables that shall be available during build time.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`network  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use vpcConnector  
`maxInstances` |  `integer` The limit on the maximum number of function instances that may coexist at a given time.In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate.See the [Max Instances](https://cloud.google.com/functions/docs/max-instances) Guide for more details.  
`minInstances` |  `integer` A lower bound for the number function instances that may coexist at a given time.  
`vpcConnector` |  `string` The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`This field is mutually exclusive with `network` field and will eventually replace it.See [the VPC documentation](https://cloud.google.com/compute/docs/vpc) for more information on connecting Cloud projects.  
`vpcConnectorEgressSettings` |  `enum (`[VpcConnectorEgressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#VpcConnectorEgressSettings)`)` The egress settings for the connector, controlling what traffic is diverted through it.  
`ingressSettings` |  `enum (`[IngressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#IngressSettings)`)` The ingress settings for the function, controlling what traffic can reach it.  
`kmsKeyName` |  `string` Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources.It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.If specified, you must also provide an artifact registry repository using the `dockerRepository` field that was created with the same KMS crypto key.The following service accounts need to be granted the role 'Cloud KMS CryptoKey Encrypter/Decrypter (roles/cloudkms.cryptoKeyEncrypterDecrypter)' on the Key/KeyRing/Project/Organization (least access preferred).

  1. Google Cloud Functions service account (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com) - Required to protect the function's image.
  2. Google Storage service account (service-{project_number}@gs-project-accounts.iam.gserviceaccount.com) - Required to protect the function's source code. If this service account does not exist, deploying a function without a KMS key or retrieving the service agent name provisions it. For more information, see <https://cloud.google.com/storage/docs/projects#service-agents> and <https://cloud.google.com/storage/docs/getting-service-agent#gsutil>.

Google Cloud Functions delegates access to service agents to protect function resources in internal projects that are not accessible by the end user.  
`buildWorkerPool` |  `string` Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where `{project}` and `{region}` are the project id and region respectively where the worker pool is defined and `{workerPool}` is the short name of the worker pool.If the project id is not the same as the function, then the Cloud Functions Service Agent (`service-<project_number>@gcf-admin-robot.iam.gserviceaccount.com`) must be granted the role Cloud Build Custom Workers Builder (`roles/cloudbuild.customworkers.builder`) in the project.  
`buildId` |  `string` Output only. The Cloud Build ID of the latest successful deployment of the function.  
`buildName` |  `string` Output only. The Cloud Build Name of the function deployment. `projects/<project-number>/locations/<region>/builds/<build-id>`.  
`secretEnvironmentVariables[]` |  `object (`[SecretEnvVar](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecretEnvVar)`)` Secret environment variables configuration.  
`secretVolumes[]` |  `object (`[SecretVolume](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecretVolume)`)` Secret volumes configuration.  
`sourceToken` |  `string` Input only. An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.  
`dockerRepository` |  `string` User-managed repository created in Artifact Registry to which the function's Docker image will be pushed after it is built by Cloud Build. May optionally be encrypted with a customer-managed encryption key (CMEK). If unspecified and `dockerRegistry` is not explicitly set to `CONTAINER_REGISTRY`, GCF will create and use a default Artifact Registry repository named 'gcf-artifacts' in the region.It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`.Cross-project repositories are not supported. Cross-location repositories are not supported. Repository format must be 'DOCKER'.  
`dockerRegistry  
**(deprecated)**` |  `enum (`[DockerRegistry](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#DockerRegistry)`)` This item is deprecated!Docker Registry to use for this deployment. Deprecated: as of March 2025, `CONTAINER_REGISTRY` option is no longer available in response to Container Registry's deprecation: <https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr> Please use Artifact Registry instead, which is the default choice.If unspecified, it defaults to `ARTIFACT_REGISTRY`. If `dockerRepository` field is specified, this field should either be left unspecified or set to `ARTIFACT_REGISTRY`.  
`buildServiceAccount` |  `string` A service account the user provides for use with Cloud Build. The format of this field is `projects/{projectId}/serviceAccounts/{serviceAccountEmail}`.  
`satisfiesPzs` |  `boolean` Output only.  
`satisfiesPzi` |  `boolean` Output only.  
Union field `source_code`. The location of the function source code. `source_code` can be only one of the following:  
`sourceArchiveUrl` |  `string` The Google Cloud Storage URL, starting with `gs://`, pointing to the zip archive which contains the function.  
`sourceRepository` |  `object (`[SourceRepository](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SourceRepository)`)` **Beta Feature** The source repository where a function is hosted.  
`sourceUploadUrl` |  `string` The Google Cloud Storage signed URL used for source uploading, generated by calling [google.cloud.functions.v1.GenerateUploadUrl].The signature is validated on write methods (Create, Update) The signature is stripped from the Function object on read methods (Get, List)  
Union field `trigger`. An event that triggers the function. `trigger` can be only one of the following:  
`httpsTrigger` |  `object (`[HttpsTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#HttpsTrigger)`)` An HTTPS endpoint type of source that can be triggered via URL.  
`eventTrigger` |  `object (`[EventTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#EventTrigger)`)` A source that fires events in response to a condition in another service.  
Union field `runtime_update_policy`. This controls when security patches are applied to the runtime environment. `runtime_update_policy` can be only one of the following:  
`automaticUpdatePolicy` |  `object (`[AutomaticUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#AutomaticUpdatePolicy)`)`  
`onDeployUpdatePolicy` |  `object (`[OnDeployUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#OnDeployUpdatePolicy)`)`  
  
## SourceRepository

Describes SourceRepository, used to represent parameters related to source repository where a function is hosted.

JSON representation  
---  
      
    
    {
      "url": string,
      "deployedUrl": string
    }  
  
Fields  
---  
`url` |  `string` The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:To refer to a specific commit: `https://source.developers.google.com/projects/*/repos/*/revisions/*/paths/*` To refer to a moveable alias (branch): `https://source.developers.google.com/projects/*/repos/*/moveable-aliases/*/paths/*` In particular, to refer to HEAD use `master` moveable alias. To refer to a specific fixed alias (tag): `https://source.developers.google.com/projects/*/repos/*/fixed-aliases/*/paths/*`You may omit `paths/*` if you want to use the main directory. The function response may add an empty `/paths/` to the URL.  
`deployedUrl` |  `string` Output only. The URL pointing to the hosted repository where the function were defined at the time of deployment. It always points to a specific commit in the format described above.  
  
## HttpsTrigger

Describes HttpsTrigger, could be used to connect web hooks to function.

JSON representation  
---  
      
    
    {
      "url": string,
      "securityLevel": enum ([SecurityLevel](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecurityLevel))
    }  
  
Fields  
---  
`url` |  `string` Output only. The deployed url for the function.  
`securityLevel` |  `enum (`[SecurityLevel](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecurityLevel)`)` The security level for the function.  
  
## SecurityLevel

Available security level settings.

This controls the methods to enforce security (HTTPS) on a URL.

If unspecified, SECURE_OPTIONAL will be used.

Enums  
---  
`SECURITY_LEVEL_UNSPECIFIED` | Unspecified.  
`SECURE_ALWAYS` | Requests for a URL that match this handler that do not use HTTPS are automatically redirected to the HTTPS URL with the same path. Query parameters are reserved for the redirect.  
`SECURE_OPTIONAL` | Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used and respond accordingly.  
  
## EventTrigger

Describes EventTrigger, used to request events be sent from another service.

JSON representation  
---  
      
    
    {
      "eventType": string,
      "resource": string,
      "service": string,
      "failurePolicy": {
        object ([FailurePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#FailurePolicy))
      }
    }  
  
Fields  
---  
`eventType` |  `string` Required. The type of event to observe. For example: `providers/cloud.storage/eventTypes/object.change` and `providers/cloud.pubsub/eventTypes/topic.publish`.Event types match pattern `providers/*/eventTypes/*.*`. The pattern contains:

  1. namespace: For example, `cloud.storage` and `google.firebase.analytics`.
  2. resource type: The type of resource on which event occurs. For example, the Google Cloud Storage API includes the type `object`.
  3. action: The action that generates the event. For example, action for a Google Cloud Storage Object is 'change'. These parts are lower case.

  
`resource` |  `string` Required. The resource(s) from which to observe events, for example, `projects/_/buckets/myBucket`.Not all syntactically correct values are accepted by all services. For example:

  1. The authorization model must support it. Google Cloud Functions only allows EventTriggers to be deployed that observe resources in the same project as the `CloudFunction`.
  2. The resource type must match the pattern expected for an `eventType`. For example, an `EventTrigger` that has an `eventType` of "google.pubsub.topic.publish" should have a resource that matches Google Cloud Pub/Sub topics.

Additionally, some services may support short names when creating an `EventTrigger`. These will always be returned in the normalized "long" format.See each _service's_ documentation for supported formats.  
`service` |  `string` The hostname of the service that should be observed.If no string is provided, the default service implementing the API will be used. For example, `storage.googleapis.com` is the default for all event types in the `google.storage` namespace.  
`failurePolicy` |  `object (`[FailurePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#FailurePolicy)`)` Specifies policy for failed executions.  
  
## FailurePolicy

Describes the policy in case of function's execution failure. If empty, then defaults to ignoring failures (i.e. not retrying them).

JSON representation  
---  
      
    
    {
    
      // Union field action can be only one of the following:
      "retry": {
        object ([Retry](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#Retry))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
Union field `action`. Defines the action taken in case of a function execution failure. `action` can be only one of the following:  
`retry` |  `object (`[Retry](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#Retry)`)` If specified, then the function will be retried in case of a failure.  
  
## Retry

This type has no fields.

Describes the retry policy in case of function's execution failure. A function execution will be retried on any failure. A failed execution will be retried up to 7 days with an exponential backoff (capped at 10 seconds). Retried execution is charged as any other execution.

## CloudFunctionStatus

Describes the current stage of a deployment.

Enums  
---  
`CLOUD_FUNCTION_STATUS_UNSPECIFIED` | Not specified. Invalid state.  
`ACTIVE` | Function has been successfully deployed and is serving.  
`OFFLINE` | Function deployment failed and the function isn’t serving.  
`DEPLOY_IN_PROGRESS` | Function is being created or updated.  
`DELETE_IN_PROGRESS` | Function is being deleted.  
`UNKNOWN` | Function deployment failed and the function serving state is undefined. The function should be updated or deleted to move it out of this state.  
  
## VpcConnectorEgressSettings

Available egress settings.

This controls what traffic is diverted through the VPC Access Connector resource. By default PRIVATE_RANGES_ONLY will be used.

Enums  
---  
`VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED` | Unspecified.  
`PRIVATE_RANGES_ONLY` | Use the VPC Access Connector only for private IP space from RFC1918.  
`ALL_TRAFFIC` | Force the use of VPC Access Connector for all egress traffic from the function.  
  
## IngressSettings

Available ingress settings.

This controls what traffic can reach the function.

If unspecified, ALLOW_ALL will be used.

Enums  
---  
`INGRESS_SETTINGS_UNSPECIFIED` | Unspecified.  
`ALLOW_ALL` | Allow HTTP traffic from public and private sources.  
`ALLOW_INTERNAL_ONLY` | Allow HTTP traffic from only private VPC sources.  
`ALLOW_INTERNAL_AND_GCLB` | Allow HTTP traffic from private VPC sources and through GCLB.  
  
## SecretEnvVar

Configuration for a secret environment variable. It has the information necessary to fetch the secret value from secret manager and expose it as an environment variable.

JSON representation  
---  
      
    
    {
      "key": string,
      "projectId": string,
      "secret": string,
      "version": string
    }  
  
Fields  
---  
`key` |  `string` Name of the environment variable.  
`projectId` |  `string` Project identifier (preferably project number but can also be the project ID) of the project that contains the secret. If not set, it will be populated with the function's project assuming that the secret exists in the same project as of the function.  
`secret` |  `string` Name of the secret in secret manager (not the full resource name).  
`version` |  `string` Version of the secret (version number or the string 'latest'). It is recommended to use a numeric version for secret environment variables as any updates to the secret value is not reflected until new instances start.  
  
## SecretVolume

Configuration for a secret volume. It has the information necessary to fetch the secret value from secret manager and make it available as files mounted at the requested paths within the application container. Secret value is not a part of the configuration. Every filesystem read operation performs a lookup in secret manager to retrieve the secret value.

JSON representation  
---  
      
    
    {
      "mountPath": string,
      "projectId": string,
      "secret": string,
      "versions": [
        {
          object ([SecretVersion](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecretVersion))
        }
      ]
    }  
  
Fields  
---  
`mountPath` |  `string` The path within the container to mount the secret volume. For example, setting the mountPath as `/etc/secrets` would mount the secret value files under the `/etc/secrets` directory. This directory will also be completely shadowed and unavailable to mount any other secrets.Recommended mount paths: /etc/secrets Restricted mount paths: /cloudsql, /dev/log, /pod, /proc, /var/log  
`projectId` |  `string` Project identifier (preferrably project number but can also be the project ID) of the project that contains the secret. If not set, it will be populated with the function's project assuming that the secret exists in the same project as of the function.  
`secret` |  `string` Name of the secret in secret manager (not the full resource name).  
`versions[]` |  `object (`[SecretVersion](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#SecretVersion)`)` List of secret versions to mount for this secret. If empty, the `latest` version of the secret will be made available in a file named after the secret under the mount point.  
  
## SecretVersion

Configuration for a single version.

JSON representation  
---  
      
    
    {
      "version": string,
      "path": string
    }  
  
Fields  
---  
`version` |  `string` Version of the secret (version number or the string 'latest'). It is preferable to use `latest` version with secret volumes as secret value changes are reflected immediately.  
`path` |  `string` Relative path of the file under the mount path where the secret value for this version will be fetched and made available. For example, setting the mountPath as '/etc/secrets' and path as `/secret_foo` would mount the secret value file at `/etc/secrets/secret_foo`.  
  
## DockerRegistry

Docker Registry to use for storing function Docker images.

Enums  
---  
`DOCKER_REGISTRY_UNSPECIFIED` | Unspecified.  
`CONTAINER_REGISTRY` | Docker images will be stored in multi-regional Container Registry repositories named `gcf`.  
`ARTIFACT_REGISTRY` | Docker images will be stored in regional Artifact Registry repositories. By default, GCF will create and use repositories named `gcf-artifacts` in every region in which a function is deployed. But the repository to use can also be specified by the user using the `dockerRepository` field.  
  
## AutomaticUpdatePolicy

This type has no fields.

Security patches are applied automatically to the runtime without requiring the function to be redeployed.

## OnDeployUpdatePolicy

Security patches are only applied when a function is redeployed.

JSON representation  
---  
      
    
    {
      "runtimeVersion": string
    }  
  
Fields  
---  
`runtimeVersion` |  `string` Output only. Contains the runtime version which was used during latest function deployment.  
  
## Methods  
  
---  
  
### `[call](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/call)`

|  Synchronously invokes a deployed Cloud Function.  
  
### `[create](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/create)`

|  Creates a new function.  
  
### `[delete](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/delete)`

|  Deletes a function with the given name from the specified project.  
  
### `[generateDownloadUrl](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/generateDownloadUrl)`

|  Returns a signed URL for downloading deployed function source code.  
  
### `[generateUploadUrl](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/generateUploadUrl)`

|  Returns a signed URL for uploading a function source code.  
  
### `[get](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/get)`

|  Returns a function with the given name from the requested project.  
  
### `[getIamPolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/getIamPolicy)`

|  Gets the IAM access control policy for a function.  
  
### `[list](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/list)`

|  Returns a list of functions that belong to the requested project.  
  
### `[patch](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/patch)`

|  Updates existing function.  
  
### `[setIamPolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/setIamPolicy)`

|  Sets the IAM access control policy on the specified function.  
  
### `[testIamPermissions](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/testIamPermissions)`

|  Tests the specified permissions against the IAM access control policy for a function.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
