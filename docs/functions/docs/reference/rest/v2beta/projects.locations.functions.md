---
url: https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions
title: REST Resource: projects.locations.functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:36.612559+00:00
---

# REST Resource: projects.locations.functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback 

#  REST Resource: projects.locations.functions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Function
    * JSON representation
  * BuildConfig
    * JSON representation
  * AutomaticUpdatePolicy
  * OnDeployUpdatePolicy
    * JSON representation
  * Source
    * JSON representation
  * StorageSource
    * JSON representation
  * RepoSource
    * JSON representation
  * SourceProvenance
    * JSON representation
  * DockerRegistry
  * ServiceConfig
    * JSON representation
  * VpcConnectorEgressSettings
  * IngressSettings
  * SecretEnvVar
    * JSON representation
  * SecretVolume
    * JSON representation
  * SecretVersion
    * JSON representation
  * SecurityLevel
  * DirectVpcNetworkInterface
    * JSON representation
  * DirectVpcEgress
  * EventTrigger
    * JSON representation
  * EventFilter
    * JSON representation
  * RetryPolicy
  * State
  * StateMessage
    * JSON representation
  * Severity
  * Environment
  * UpgradeInfo
    * JSON representation
  * UpgradeState
  * Methods



## Resource: Function

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulates function and trigger configurations.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "buildConfig": {
        object ([BuildConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#BuildConfig))
      },
      "serviceConfig": {
        object ([ServiceConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#ServiceConfig))
      },
      "eventTrigger": {
        object ([EventTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#EventTrigger))
      },
      "state": enum ([State](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#State)),
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "stateMessages": [
        {
          object ([StateMessage](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#StateMessage))
        }
      ],
      "environment": enum ([Environment](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#Environment)),
      "upgradeInfo": {
        object ([UpgradeInfo](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#UpgradeInfo))
      },
      "url": string,
      "kmsKeyName": string,
      "satisfiesPzs": boolean,
      "createTime": string,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*`  
`description` |  `string` User-provided description of a function.  
`buildConfig` |  `object (`[BuildConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#BuildConfig)`)` Describes the Build step of the function that builds a container from the given source.  
`serviceConfig` |  `object (`[ServiceConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#ServiceConfig)`)` Describes the Service being deployed. Currently deploys services to Cloud Run (fully managed).  
`eventTrigger` |  `object (`[EventTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#EventTrigger)`)` An Eventarc trigger managed by Google Cloud Functions that fires events in response to a condition in another service.  
`state` |  `enum (`[State](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#State)`)` Output only. State of the function.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of a Cloud Function.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this Cloud Function.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`stateMessages[]` |  `object (`[StateMessage](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#StateMessage)`)` Output only. State Messages for this Cloud Function.  
`environment` |  `enum (`[Environment](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#Environment)`)` Describe whether the function is 1st Gen or 2nd Gen.  
`upgradeInfo` |  `object (`[UpgradeInfo](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#UpgradeInfo)`)` Output only. UpgradeInfo for this Cloud Function  
`url` |  `string` Output only. The deployed url for the function.  
`kmsKeyName` |  `string` Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources.It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create timestamp of a Cloud Function. This is only applicable to 2nd Gen functions.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
## BuildConfig

Describes the Build step of the function that builds a container from the given source.

JSON representation  
---  
      
    
    {
      "build": string,
      "runtime": string,
      "entryPoint": string,
      "source": {
        object ([Source](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#Source))
      },
      "sourceProvenance": {
        object ([SourceProvenance](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SourceProvenance))
      },
      "workerPool": string,
      "environmentVariables": {
        string: string,
        ...
      },
      "dockerRegistry": enum ([DockerRegistry](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#DockerRegistry)),
      "dockerRepository": string,
      "serviceAccount": string,
      "sourceToken": string,
    
      // Union field runtime_update_policy can be only one of the following:
      "automaticUpdatePolicy": {
        object ([AutomaticUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#AutomaticUpdatePolicy))
      },
      "onDeployUpdatePolicy": {
        object ([OnDeployUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#OnDeployUpdatePolicy))
      }
      // End of list of possible types for union field runtime_update_policy.
    }  
  
Fields  
---  
`build` |  `string` Output only. The Cloud Build name of the latest successful deployment of the function.  
`runtime` |  `string` The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).  
`entryPoint` |  `string` The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.  
`source` |  `object (`[Source](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#Source)`)` The location of the function source code.  
`sourceProvenance` |  `object (`[SourceProvenance](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SourceProvenance)`)` Output only. A permanent fixed identifier for source.  
`workerPool` |  `string` Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool.If the project id is not the same as the function, then the Cloud Functions Service Agent (service-@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role Cloud Build Custom Workers Builder (roles/cloudbuild.customworkers.builder) in the project.  
`environmentVariables` |  `map (key: string, value: string)` User-provided build-time environment variables for the functionAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`dockerRegistry  
**(deprecated)**` |  `enum (`[DockerRegistry](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#DockerRegistry)`)` This item is deprecated!Docker Registry to use for this deployment. This configuration is only applicable to 1st Gen functions, 2nd Gen functions can only use Artifact Registry. Deprecated: as of March 2025, `CONTAINER_REGISTRY` option is no longer available in response to Container Registry's deprecation: <https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr> Please use Artifact Registry instead, which is the default choice.If unspecified, it defaults to `ARTIFACT_REGISTRY`. If `dockerRepository` field is specified, this field should either be left unspecified or set to `ARTIFACT_REGISTRY`.  
`dockerRepository` |  `string` Repository in Artifact Registry to which the function docker image will be pushed after it is built by Cloud Build. If specified by user, it is created and managed by user with a customer managed encryption key. Otherwise, GCF will create and use a repository named 'gcf-artifacts' for every deployed region.It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`. Repository format must be 'DOCKER'.  
`serviceAccount` |  `string` Service account to be used for building the container. The format of this field is `projects/{projectId}/serviceAccounts/{serviceAccountEmail}`.  
`sourceToken` |  `string` An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.  
Union field `runtime_update_policy`. This controls when security patches are applied to the runtime environment. `runtime_update_policy` can be only one of the following:  
`automaticUpdatePolicy` |  `object (`[AutomaticUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#AutomaticUpdatePolicy)`)`  
`onDeployUpdatePolicy` |  `object (`[OnDeployUpdatePolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#OnDeployUpdatePolicy)`)`  
  
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
`runtimeVersion` |  `string` Output only. contains the runtime version which was used during latest function deployment.  
  
## Source

The location of the function source code.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "storageSource": {
        object ([StorageSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#StorageSource))
      },
      "repoSource": {
        object ([RepoSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#RepoSource))
      },
      "gitUri": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Location of the source. At least one source needs to be provided for the deployment to succeed. `source` can be only one of the following:  
`storageSource` |  `object (`[StorageSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#StorageSource)`)` If provided, get the source from this location in Google Cloud Storage.  
`repoSource` |  `object (`[RepoSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#RepoSource)`)` If provided, get the source from this location in a Cloud Source Repository.  
`gitUri` |  `string` If provided, get the source from GitHub repository. This option is valid only for GCF 1st Gen function. Example: <https://github.com/>//blob//  
  
## StorageSource

Location of the source in an archive file in Google Cloud Storage.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "object": string,
      "generation": string,
      "sourceUploadUrl": string
    }  
  
Fields  
---  
`bucket` |  `string` Google Cloud Storage bucket containing the source (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)).  
`object` |  `string` Google Cloud Storage object containing the source.This object must be a gzipped archive file (`.tar.gz`) containing source to build.  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Google Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used.  
`sourceUploadUrl` |  `string` When the specified storage bucket is a 1st gen function uploard url bucket, this field should be set as the generated upload url for 1st gen deployment.  
  
## RepoSource

Location of the source in a Google Cloud Source Repository.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "repoName": string,
      "dir": string,
    
      // Union field revision can be only one of the following:
      "branchName": string,
      "tagName": string,
      "commitSha": string
      // End of list of possible types for union field revision.
    }  
  
Fields  
---  
`projectId` |  `string` ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed.  
`repoName` |  `string` Name of the Cloud Source Repository.  
`dir` |  `string` Directory, relative to the source root, in which to run the build.This must be a relative path. If a step's `dir` is specified and is an absolute path, this value is ignored for that step's execution. eg. helloworld (no leading slash allowed)  
Union field `revision`. A revision within the Cloud Source Repository must be specified in one of these ways. `revision` can be only one of the following:  
`branchName` |  `string` Regex matching branches to build.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
`tagName` |  `string` Regex matching tags to build.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
`commitSha` |  `string` Explicit commit SHA to build.  
  
## SourceProvenance

Provenance of the source. Ways to find the original source, or verify that some source was used for this build.

JSON representation  
---  
      
    
    {
      "resolvedStorageSource": {
        object ([StorageSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#StorageSource))
      },
      "resolvedRepoSource": {
        object ([RepoSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#RepoSource))
      },
      "gitUri": string
    }  
  
Fields  
---  
`resolvedStorageSource` |  `object (`[StorageSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#StorageSource)`)` A copy of the build's `source.storage_source`, if exists, with any generations resolved.  
`resolvedRepoSource` |  `object (`[RepoSource](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#RepoSource)`)` A copy of the build's `source.repo_source`, if exists, with any revisions resolved.  
`gitUri` |  `string` A copy of the build's `source.git_uri`, if exists, with any commits resolved.  
  
## DockerRegistry

Docker Registry to use for storing function Docker images.

Enums  
---  
`DOCKER_REGISTRY_UNSPECIFIED` | Unspecified.  
`CONTAINER_REGISTRY` | Docker images will be stored in multi-regional Container Registry repositories named `gcf`.  
`ARTIFACT_REGISTRY` | Docker images will be stored in regional Artifact Registry repositories. By default, GCF will create and use repositories named `gcf-artifacts` in every region in which a function is deployed. But the repository to use can also be specified by the user using the `dockerRepository` field.  
  
## ServiceConfig

Describes the Service being deployed. Currently Supported : Cloud Run (fully managed).

JSON representation  
---  
      
    
    {
      "service": string,
      "timeoutSeconds": integer,
      "availableMemory": string,
      "availableCpu": string,
      "environmentVariables": {
        string: string,
        ...
      },
      "maxInstanceCount": integer,
      "minInstanceCount": integer,
      "vpcConnector": string,
      "vpcConnectorEgressSettings": enum ([VpcConnectorEgressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#VpcConnectorEgressSettings)),
      "ingressSettings": enum ([IngressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#IngressSettings)),
      "uri": string,
      "serviceAccountEmail": string,
      "allTrafficOnLatestRevision": boolean,
      "secretEnvironmentVariables": [
        {
          object ([SecretEnvVar](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecretEnvVar))
        }
      ],
      "secretVolumes": [
        {
          object ([SecretVolume](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecretVolume))
        }
      ],
      "revision": string,
      "maxInstanceRequestConcurrency": integer,
      "securityLevel": enum ([SecurityLevel](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecurityLevel)),
      "binaryAuthorizationPolicy": string,
      "directVpcNetworkInterface": [
        {
          object ([DirectVpcNetworkInterface](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#DirectVpcNetworkInterface))
        }
      ],
      "directVpcEgress": enum ([DirectVpcEgress](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#DirectVpcEgress))
    }  
  
Fields  
---  
`service` |  `string` Output only. Name of the service associated with a Function. The format of this field is `projects/{project}/locations/{region}/services/{service}`  
`timeoutSeconds` |  `integer` The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds.  
`availableMemory` |  `string` The amount of memory available for a function. Defaults to 256M. Supported units are k, M, G, Mi, Gi. If no unit is supplied the value is interpreted as bytes. See <https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go> a full description.  
`availableCpu` |  `string` The number of CPUs used in a single container instance. Default value is calculated from available memory. Supports the same values as Cloud Run, see <https://cloud.google.com/run/docs/reference/rest/v1/Container#resourcerequirements> Example: "1" indicates 1 vCPU  
`environmentVariables` |  `map (key: string, value: string)` Environment variables that shall be available during function execution.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`maxInstanceCount` |  `integer` The limit on the maximum number of function instances that may coexist at a given time.In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate.See the [Max Instances](https://cloud.google.com/functions/docs/max-instances) Guide for more details.  
`minInstanceCount` |  `integer` The limit on the minimum number of function instances that may coexist at a given time.Function instances are kept in idle state for a short period after they finished executing the request to reduce cold start time for subsequent requests. Setting a minimum instance count will ensure that the given number of instances are kept running in idle state always. This can help with cold start times when jump in incoming request count occurs after the idle instance would have been stopped in the default case.  
`vpcConnector` |  `string` The Serverless VPC Access connector that this cloud function can connect to. The format of this field is `projects/*/locations/*/connectors/*`.  
`vpcConnectorEgressSettings` |  `enum (`[VpcConnectorEgressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#VpcConnectorEgressSettings)`)` The egress settings for the connector, controlling what traffic is diverted through it.  
`ingressSettings` |  `enum (`[IngressSettings](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#IngressSettings)`)` The ingress settings for the function, controlling what traffic can reach it.  
`uri` |  `string` Output only. URI of the Service deployed.  
`serviceAccountEmail` |  `string` The email of the service's service account. If empty, defaults to `{project_number}-compute@developer.gserviceaccount.com`.  
`allTrafficOnLatestRevision` |  `boolean` Whether 100% of traffic is routed to the latest revision. On functions.create and functions.patch, when set to true, the revision being deployed will serve 100% of traffic, ignoring any traffic split settings, if any. On functions.get, true will be returned if the latest revision is serving 100% of traffic.  
`secretEnvironmentVariables[]` |  `object (`[SecretEnvVar](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecretEnvVar)`)` Secret environment variables configuration.  
`secretVolumes[]` |  `object (`[SecretVolume](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecretVolume)`)` Secret volumes configuration.  
`revision` |  `string` Output only. The name of service revision.  
`maxInstanceRequestConcurrency` |  `integer` Sets the maximum number of concurrent requests that each instance can receive. Defaults to 1.  
`securityLevel` |  `enum (`[SecurityLevel](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecurityLevel)`)` Security level configure whether the function only accepts https. This configuration is only applicable to 1st Gen functions with Http trigger. By default https is optional for 1st Gen functions; 2nd Gen functions are https ONLY.  
`binaryAuthorizationPolicy` |  `string` Optional. The binary authorization policy to be checked when deploying the Cloud Run service.  
`directVpcNetworkInterface[]` |  `object (`[DirectVpcNetworkInterface](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#DirectVpcNetworkInterface)`)` Optional. The Direct VPC network interface for the Cloud Function. Currently only a single Direct VPC is supported.  
`directVpcEgress` |  `enum (`[DirectVpcEgress](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#DirectVpcEgress)`)` Optional. Egress settings for direct VPC. If not provided, it defaults to VPC_EGRESS_PRIVATE_RANGES_ONLY.  
  
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
`projectId` |  `string` Project identifier (preferably project number but can also be the project ID) of the project that contains the secret. If not set, it is assumed that the secret is in the same project as the function.  
`secret` |  `string` Name of the secret in secret manager (not the full resource name).  
`version` |  `string` Version of the secret (version number or the string 'latest'). It is recommended to use a numeric version for secret environment variables as any updates to the secret value is not reflected until new instances start.  
  
## SecretVolume

Configuration for a secret volume. It has the information necessary to fetch the secret value from secret manager and make it available as files mounted at the requested paths within the application container.

JSON representation  
---  
      
    
    {
      "mountPath": string,
      "projectId": string,
      "secret": string,
      "versions": [
        {
          object ([SecretVersion](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecretVersion))
        }
      ]
    }  
  
Fields  
---  
`mountPath` |  `string` The path within the container to mount the secret volume. For example, setting the mountPath as `/etc/secrets` would mount the secret value files under the `/etc/secrets` directory. This directory will also be completely shadowed and unavailable to mount any other secrets. Recommended mount path: /etc/secrets  
`projectId` |  `string` Project identifier (preferably project number but can also be the project ID) of the project that contains the secret. If not set, it is assumed that the secret is in the same project as the function.  
`secret` |  `string` Name of the secret in secret manager (not the full resource name).  
`versions[]` |  `object (`[SecretVersion](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#SecretVersion)`)` List of secret versions to mount for this secret. If empty, the `latest` version of the secret will be made available in a file named after the secret under the mount point.  
  
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
`path` |  `string` Relative path of the file under the mount path where the secret value for this version will be fetched and made available. For example, setting the mountPath as '/etc/secrets' and path as `secret_foo` would mount the secret value file at `/etc/secrets/secret_foo`.  
  
## SecurityLevel

Available security level settings.

This enforces security protocol on function URL.

Security level is only configurable for 1st Gen functions, If unspecified, SECURE_OPTIONAL will be used. 2nd Gen functions are SECURE_ALWAYS ONLY.

Enums  
---  
`SECURITY_LEVEL_UNSPECIFIED` | Unspecified.  
`SECURE_ALWAYS` | Requests for a URL that match this handler that do not use HTTPS are automatically redirected to the HTTPS URL with the same path. Query parameters are reserved for the redirect.  
`SECURE_OPTIONAL` | Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used and respond accordingly.  
  
## DirectVpcNetworkInterface

The Direct VPC network interface. This is mutually exclusive with VPC Connector.

JSON representation  
---  
      
    
    {
      "network": string,
      "subnetwork": string,
      "tags": [
        string
      ]
    }  
  
Fields  
---  
`network` |  `string` Optional. The name of the VPC network to which the function will be connected. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.  
`subnetwork` |  `string` Optional. The name of the VPC subnetwork that the Cloud Function resource will get IPs from. Specify either a VPC network or a subnet, or both. If both network and subnetwork are specified, the given VPC subnetwork must belong to the given VPC network. If subnetwork is not specified, the subnetwork with the same name with the network will be used.  
`tags[]` |  `string` Optional. Network tags applied to this Cloud Function resource.  
  
## DirectVpcEgress

Available egress settings for Direct VPC.

Enums  
---  
`DIRECT_VPC_EGRESS_UNSPECIFIED` | Unspecified.  
`VPC_EGRESS_PRIVATE_RANGES_ONLY` | Sends only traffic to internal addresses through the VPC network.  
`VPC_EGRESS_ALL_TRAFFIC` | Sends all outbound traffic through the VPC network.  
  
## EventTrigger

Describes EventTrigger, used to request events to be sent from another service.

JSON representation  
---  
      
    
    {
      "trigger": string,
      "triggerRegion": string,
      "eventType": string,
      "eventFilters": [
        {
          object ([EventFilter](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#EventFilter))
        }
      ],
      "pubsubTopic": string,
      "serviceAccountEmail": string,
      "retryPolicy": enum ([RetryPolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#RetryPolicy)),
      "channel": string,
      "service": string
    }  
  
Fields  
---  
`trigger` |  `string` Output only. The resource name of the Eventarc trigger. The format of this field is `projects/{project}/locations/{region}/triggers/{trigger}`.  
`triggerRegion` |  `string` The region that the trigger will be in. The trigger will only receive events originating in this region. It can be the same region as the function, a different region or multi-region, or the global region. If not provided, defaults to the same region as the function.  
`eventType` |  `string` Required. The type of event to observe. For example: `google.cloud.audit.log.v1.written` or `google.cloud.pubsub.topic.v1.messagePublished`.  
`eventFilters[]` |  `object (`[EventFilter](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#EventFilter)`)` Criteria used to filter events.  
`pubsubTopic` |  `string` Optional. The name of a Pub/Sub topic in the same project that will be used as the transport topic for the event delivery. Format: `projects/{project}/topics/{topic}`.This is only valid for events of type `google.cloud.pubsub.topic.v1.messagePublished`. The topic provided here will not be deleted at function deletion.  
`serviceAccountEmail` |  `string` Optional. The email of the trigger's service account. The service account must have permission to invoke Cloud Run services, the permission is `run.routes.invoke`. If empty, defaults to the Compute Engine default service account: `{project_number}-compute@developer.gserviceaccount.com`.  
`retryPolicy` |  `enum (`[RetryPolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#RetryPolicy)`)` Optional. If unset, then defaults to ignoring failures (i.e. not retrying them).  
`channel` |  `string` Optional. The name of the channel associated with the trigger in `projects/{project}/locations/{location}/channels/{channel}` format. You must provide a channel to receive events from Eventarc SaaS partners.  
`service` |  `string` Optional. The hostname of the service that 1st Gen function should be observed.If no string is provided, the default service implementing the API will be used. For example, `storage.googleapis.com` is the default for all event types in the `google.storage` namespace.The field is only applicable to 1st Gen functions.  
  
## EventFilter

Filters events based on exact matches on the CloudEvents attributes.

JSON representation  
---  
      
    
    {
      "attribute": string,
      "value": string,
      "operator": string
    }  
  
Fields  
---  
`attribute` |  `string` Required. The name of a CloudEvents attribute.  
`value` |  `string` Required. The value for the attribute.  
`operator` |  `string` Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is `match-path-pattern`.  
  
## RetryPolicy

Describes the retry policy in case of function's execution failure. Retried execution is charged as any other execution.

Enums  
---  
`RETRY_POLICY_UNSPECIFIED` | Not specified.  
`RETRY_POLICY_DO_NOT_RETRY` | Do not retry.  
`RETRY_POLICY_RETRY` | Retry on any failure, retry up to 7 days with an exponential backoff (capped at 10 seconds).  
  
## State

Describes the current state of the function.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified. Invalid state.  
`ACTIVE` | Function has been successfully deployed and is serving.  
`FAILED` | Function deployment failed and the function is not serving.  
`DEPLOYING` | Function is being created or updated.  
`DELETING` | Function is being deleted.  
`UNKNOWN` | Function deployment failed and the function serving state is undefined. The function should be updated or deleted to move it out of this state.  
`DETACHING` | Function is being detached.  
`DETACH_FAILED` | Function detach failed and the function is still serving.  
  
## StateMessage

Informational messages about the state of the Cloud Function or Operation.

JSON representation  
---  
      
    
    {
      "severity": enum ([Severity](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#Severity)),
      "type": string,
      "message": string
    }  
  
Fields  
---  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#Severity)`)` Severity of the state message.  
`type` |  `string` One-word CamelCase type of the state message.  
`message` |  `string` The message.  
  
## Severity

Severity of the state message.

Enums  
---  
`SEVERITY_UNSPECIFIED` | Not specified. Invalid severity.  
`ERROR` | ERROR-level severity.  
`WARNING` | WARNING-level severity.  
`INFO` | INFO-level severity.  
  
## Environment

The environment the function is hosted on.

Enums  
---  
`ENVIRONMENT_UNSPECIFIED` | Unspecified  
`GEN_1` | Gen 1  
`GEN_2` | Gen 2  
  
## UpgradeInfo

Information related to: * A function's eligibility for 1st Gen to 2nd Gen migration. * Current state of migration for function undergoing migration.

JSON representation  
---  
      
    
    {
      "upgradeState": enum ([UpgradeState](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#UpgradeState)),
      "serviceConfig": {
        object ([ServiceConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#ServiceConfig))
      },
      "eventTrigger": {
        object ([EventTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#EventTrigger))
      },
      "buildConfig": {
        object ([BuildConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#BuildConfig))
      }
    }  
  
Fields  
---  
`upgradeState` |  `enum (`[UpgradeState](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#UpgradeState)`)` UpgradeState of the function  
`serviceConfig` |  `object (`[ServiceConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#ServiceConfig)`)` Describes the Cloud Run service which has been setup to prepare for 2nd gen upgrade.  
`eventTrigger` |  `object (`[EventTrigger](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#EventTrigger)`)` Describes the Event trigger which has been setup to prepare for 2nd gen upgrade.  
`buildConfig` |  `object (`[BuildConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions#BuildConfig)`)` Describes the Build step of the function that builds a container to prepare for 2nd gen upgrade.  
  
## UpgradeState

Enum representing the various upgrade state a function can have.

Enums  
---  
`UPGRADE_STATE_UNSPECIFIED` | Unspecified state. Most functions are in this upgrade state.  
`ELIGIBLE_FOR_2ND_GEN_UPGRADE` | Functions in this state are eligible for 1st Gen upgrade.  
`INELIGIBLE_FOR_UPGRADE_UNTIL_REDEPLOYMENT` | Functions in this state are ineligible for 1st Gen upgrade until redeployment with newer runtime.  
`UPGRADE_OPERATION_IN_PROGRESS` | An upgrade related operation is in progress.  
`SETUP_FUNCTION_UPGRADE_CONFIG_SUCCESSFUL` | functions.setupFunctionUpgradeConfig API was successful and a 2nd Gen function has been created based on 1st Gen function instance.  
`SETUP_FUNCTION_UPGRADE_CONFIG_ERROR` | functions.setupFunctionUpgradeConfig API was un-successful.  
`ABORT_FUNCTION_UPGRADE_ERROR` | functions.abortFunctionUpgrade API was un-successful.  
`REDIRECT_FUNCTION_UPGRADE_TRAFFIC_SUCCESSFUL` | functions.redirectFunctionUpgradeTraffic API was successful and traffic is served by 2nd Gen function stack.  
`REDIRECT_FUNCTION_UPGRADE_TRAFFIC_ERROR` | functions.redirectFunctionUpgradeTraffic API was un-successful.  
`ROLLBACK_FUNCTION_UPGRADE_TRAFFIC_ERROR` | functions.rollbackFunctionUpgradeTraffic API was un-successful.  
`COMMIT_FUNCTION_UPGRADE_ERROR` | functions.commitFunctionUpgrade API was un-successful and 1st gen function might have broken.  
`COMMIT_FUNCTION_UPGRADE_ERROR_ROLLBACK_SAFE` | functions.commitFunctionUpgrade API was un-successful but safe to rollback traffic or abort.  
`COMMIT_FUNCTION_UPGRADE_AS_GEN2_SUCCESSFUL` | Deprecated: This state is no longer returned by the backend. Clients should not rely on polling for this specific state. A successful upgrade is now indicated by the long-running operation completing successfully with a Function resource in the response.This item is deprecated!  
`COMMIT_FUNCTION_UPGRADE_AS_GEN2_ERROR` | functions.commitFunctionUpgradeAsGen2 API was un-successful and 1st gen function might have broken.  
  
## Methods  
  
---  
  
### `[abortFunctionUpgrade](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/abortFunctionUpgrade)`

|  Aborts generation upgrade process for a function with the given name from the specified project.  
  
### `[commitFunctionUpgrade](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/commitFunctionUpgrade)`

|  Finalizes the upgrade after which function upgrade can not be rolled back.  
  
### `[commitFunctionUpgradeAsGen2](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/commitFunctionUpgradeAsGen2)`

|  Commits a function upgrade from GCF Gen1 to GCF Gen2.  
  
### `[create](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/create)`

|  Creates a new function.  
  
### `[delete](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/delete)`

|  Deletes a function with the given name from the specified project.  
  
### `[detachFunction](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/detachFunction)`

|  Detaches 2nd Gen function to Cloud Run function.  
  
### `[generateDownloadUrl](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/generateDownloadUrl)`

|  Returns a signed URL for downloading deployed function source code.  
  
### `[generateUploadUrl](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/generateUploadUrl)`

|  Returns a signed URL for uploading a function source code.  
  
### `[get](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/get)`

|  Returns a function with the given name from the requested project.  
  
### `[getIamPolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/list)`

|  Returns a list of functions that belong to the requested project.  
  
### `[patch](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/patch)`

|  Updates existing function.  
  
### `[redirectFunctionUpgradeTraffic](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/redirectFunctionUpgradeTraffic)`

|  Changes the traffic target of a function from the original 1st Gen function to the 2nd Gen copy.  
  
### `[rollbackFunctionUpgradeTraffic](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/rollbackFunctionUpgradeTraffic)`

|  Reverts the traffic target of a function from the 2nd Gen copy to the original 1st Gen function.  
  
### `[setIamPolicy](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[setupFunctionUpgradeConfig](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/setupFunctionUpgradeConfig)`

|  Creates a 2nd Gen copy of the function configuration based on the 1st Gen function with the given name.  
  
### `[testIamPermissions](https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
