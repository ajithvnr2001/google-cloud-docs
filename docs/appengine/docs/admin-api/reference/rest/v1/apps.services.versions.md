---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions
title: REST Resource: apps.services.versions \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:57.605826+00:00
---

# REST Resource: apps.services.versions  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  REST Resource: apps.services.versions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Version
    * JSON representation
  * AutomaticScaling
    * JSON representation
  * CpuUtilization
    * JSON representation
  * RequestUtilization
    * JSON representation
  * DiskUtilization
    * JSON representation
  * NetworkUtilization
    * JSON representation
  * StandardSchedulerSettings
    * JSON representation
  * BasicScaling
    * JSON representation
  * ManualScaling
    * JSON representation
  * InboundServiceType
  * Network
    * JSON representation
  * Resources
    * JSON representation
  * Volume
    * JSON representation
  * FlexibleRuntimeSettings
    * JSON representation
  * ServingStatus
  * UrlMap
    * JSON representation
  * StaticFilesHandler
    * JSON representation
  * ScriptHandler
    * JSON representation
  * ApiEndpointHandler
    * JSON representation
  * SecurityLevel
  * LoginRequirement
  * AuthFailAction
  * RedirectHttpResponseCode
  * ErrorHandler
    * JSON representation
  * ErrorCode
  * Library
    * JSON representation
  * ApiConfigHandler
    * JSON representation
  * HealthCheck
    * JSON representation
  * ReadinessCheck
    * JSON representation
  * LivenessCheck
    * JSON representation
  * Deployment
    * JSON representation
  * FileInfo
    * JSON representation
  * ContainerInfo
    * JSON representation
  * ZipInfo
    * JSON representation
  * CloudBuildOptions
    * JSON representation
  * EndpointsApiService
    * JSON representation
  * RolloutStrategy
  * Entrypoint
    * JSON representation
  * VpcAccessConnector
    * JSON representation
  * EgressSetting
  * Methods



## Resource: Version

A Version resource is a specific set of source code and configuration files that are deployed into a service.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "inboundServices": [
        enum ([InboundServiceType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#InboundServiceType))
      ],
      "instanceClass": string,
      "network": {
        object ([Network](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Network))
      },
      "zones": [
        string
      ],
      "resources": {
        object ([Resources](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Resources))
      },
      "runtime": string,
      "runtimeChannel": string,
      "threadsafe": boolean,
      "vm": boolean,
      "flexibleRuntimeSettings": {
        object ([FlexibleRuntimeSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#FlexibleRuntimeSettings))
      },
      "appEngineApis": boolean,
      "betaSettings": {
        string: string,
        ...
      },
      "env": string,
      "servingStatus": enum ([ServingStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ServingStatus)),
      "createdBy": string,
      "createTime": string,
      "diskUsageBytes": string,
      "runtimeApiVersion": string,
      "runtimeMainExecutablePath": string,
      "serviceAccount": string,
      "handlers": [
        {
          object ([UrlMap](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#UrlMap))
        }
      ],
      "errorHandlers": [
        {
          object ([ErrorHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ErrorHandler))
        }
      ],
      "libraries": [
        {
          object ([Library](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Library))
        }
      ],
      "apiConfig": {
        object ([ApiConfigHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ApiConfigHandler))
      },
      "envVariables": {
        string: string,
        ...
      },
      "buildEnvVariables": {
        string: string,
        ...
      },
      "defaultExpiration": string,
      "healthCheck": {
        object ([HealthCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#HealthCheck))
      },
      "readinessCheck": {
        object ([ReadinessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ReadinessCheck))
      },
      "livenessCheck": {
        object ([LivenessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#LivenessCheck))
      },
      "nobuildFilesRegex": string,
      "deployment": {
        object ([Deployment](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Deployment))
      },
      "versionUrl": string,
      "endpointsApiService": {
        object ([EndpointsApiService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#EndpointsApiService))
      },
      "entrypoint": {
        object ([Entrypoint](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Entrypoint))
      },
      "vpcAccessConnector": {
        object ([VpcAccessConnector](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#VpcAccessConnector))
      },
    
      // Union field scaling can be only one of the following:
      "automaticScaling": {
        object ([AutomaticScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AutomaticScaling))
      },
      "basicScaling": {
        object ([BasicScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#BasicScaling))
      },
      "manualScaling": {
        object ([ManualScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ManualScaling))
      }
      // End of list of possible types for union field scaling.
    }  
  
Fields  
---  
`name` |  `string` Full path to the Version resource in the API. Example: `apps/myapp/services/default/versions/v1`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the version within the service. Example: `v1`. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names: "default", "latest", and any name with the prefix "ah-".  
`inboundServices[]` |  `enum (`[InboundServiceType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#InboundServiceType)`)` Before an application can receive email or XMPP messages, the application must be configured to enable the service.  
`instanceClass` |  `string` Instance class that is used to run this version. Valid values are:

  * AutomaticScaling: `F1`, `F2`, `F4`, `F4_1G`
  * ManualScaling or BasicScaling: `B1`, `B2`, `B4`, `B8`, `B4_1G`

Defaults to `F1` for AutomaticScaling and `B1` for ManualScaling or BasicScaling.  
`network` |  `object (`[Network](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Network)`)` Extra network settings. Only applicable in the App Engine flexible environment.  
`zones[]` |  `string` The Google Compute Engine zones that are supported by this version in the App Engine flexible environment. Deprecated.  
`resources` |  `object (`[Resources](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Resources)`)` Machine resources for this version. Only applicable in the App Engine flexible environment.  
`runtime` |  `string` Desired runtime. Example: `python27`.  
`runtimeChannel` |  `string` The channel of the runtime to use. Only available for some runtimes. Defaults to the `default` channel.  
`threadsafe` |  `boolean` Whether multiple requests can be dispatched to this version at once.  
`vm` |  `boolean` Whether to deploy this version in a container on a virtual machine.  
`flexibleRuntimeSettings` |  `object (`[FlexibleRuntimeSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#FlexibleRuntimeSettings)`)` Settings for App Engine flexible runtimes.  
`appEngineApis` |  `boolean` Allows App Engine second generation runtimes to access the legacy bundled services.  
`betaSettings` |  `map (key: string, value: string)` Metadata settings that are supplied to this version to enable beta runtime features.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`env` |  `string` App Engine execution environment for this version.Defaults to `standard`.  
`servingStatus` |  `enum (`[ServingStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ServingStatus)`)` Current serving status of this version. Only the versions with a `SERVING` status create instances and can be billed.`SERVING_STATUS_UNSPECIFIED` is an invalid value. Defaults to `SERVING`.  
`createdBy` |  `string` Email address of the user who created this version.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Time that this version was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`diskUsageBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total size in bytes of all the files that are included in this version and currently hosted on the App Engine disk.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`runtimeApiVersion` |  `string` The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at <https://cloud.google.com/appengine/docs/standard/>/config/appref  
`runtimeMainExecutablePath` |  `string` The path or name of the app's main executable.  
`serviceAccount` |  `string` The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag.  
`handlers[]` |  `object (`[UrlMap](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#UrlMap)`)` An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the request and other request handlers are not attempted.Only returned in `GET` requests if `view=FULL` is set.  
`errorHandlers[]` |  `object (`[ErrorHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ErrorHandler)`)` Custom static error pages. Limited to 10KB per page.Only returned in `GET` requests if `view=FULL` is set.  
`libraries[]` |  `object (`[Library](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Library)`)` Configuration for third-party Python runtime libraries that are required by the application.Only returned in `GET` requests if `view=FULL` is set.  
`apiConfig` |  `object (`[ApiConfigHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ApiConfigHandler)`)` Serving configuration for [Google Cloud Endpoints](https://cloud.google.com/endpoints).Only returned in `GET` requests if `view=FULL` is set.  
`envVariables` |  `map (key: string, value: string)` Environment variables available to the application.Only returned in `GET` requests if `view=FULL` is set.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`buildEnvVariables` |  `map (key: string, value: string)` Environment variables available to the build environment.Only returned in `GET` requests if `view=FULL` is set.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`defaultExpiration` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding [StaticFilesHandler](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler) does not specify its own expiration time.Only returned in `GET` requests if `view=FULL` is set.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`healthCheck` |  `object (`[HealthCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#HealthCheck)`)` Configures health checking for instances. Unhealthy instances are stopped and replaced with new instances. Only applicable in the App Engine flexible environment.Only returned in `GET` requests if `view=FULL` is set.  
`readinessCheck` |  `object (`[ReadinessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ReadinessCheck)`)` Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.Only returned in `GET` requests if `view=FULL` is set.  
`livenessCheck` |  `object (`[LivenessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#LivenessCheck)`)` Configures liveness health checking for instances. Unhealthy instances are stopped and replaced with new instancesOnly returned in `GET` requests if `view=FULL` is set.  
`nobuildFilesRegex` |  `string` Files that match this pattern will not be built into this version. Only applicable for Go runtimes.Only returned in `GET` requests if `view=FULL` is set.  
`deployment` |  `object (`[Deployment](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Deployment)`)` Code and application artifacts that make up this version.Only returned in `GET` requests if `view=FULL` is set.  
`versionUrl` |  `string` Serving URL for this version. Example: "https://myversion-dot-myservice-dot-myapp.appspot.com"Note: This field is used in responses only. Any value specified here in a request is ignored.  
`endpointsApiService` |  `object (`[EndpointsApiService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#EndpointsApiService)`)` Cloud Endpoints configuration.If endpointsApiService is set, the Cloud Endpoints Extensible Service Proxy will be provided to serve the API implemented by the app.  
`entrypoint` |  `object (`[Entrypoint](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Entrypoint)`)` The entrypoint for the application.  
`vpcAccessConnector` |  `object (`[VpcAccessConnector](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#VpcAccessConnector)`)` Enables VPC connectivity for standard apps.  
Union field `scaling`. Controls how instances are created, scaled, and reaped.Defaults to `AutomaticScaling`. `scaling` can be only one of the following:  
`automaticScaling` |  `object (`[AutomaticScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AutomaticScaling)`)` Automatic scaling is based on request rate, response latencies, and other application metrics. Instances are dynamically created and destroyed as needed in order to handle traffic.  
`basicScaling` |  `object (`[BasicScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#BasicScaling)`)` A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.  
`manualScaling` |  `object (`[ManualScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ManualScaling)`)` A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time. Manually scaled versions are sometimes referred to as "backends".  
  
## AutomaticScaling

Automatic scaling is based on request rate, response latencies, and other application metrics.

JSON representation  
---  
      
    
    {
      "coolDownPeriod": string,
      "cpuUtilization": {
        object ([CpuUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#CpuUtilization))
      },
      "maxConcurrentRequests": integer,
      "maxIdleInstances": integer,
      "maxTotalInstances": integer,
      "maxPendingLatency": string,
      "minIdleInstances": integer,
      "minTotalInstances": integer,
      "minPendingLatency": string,
      "requestUtilization": {
        object ([RequestUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#RequestUtilization))
      },
      "diskUtilization": {
        object ([DiskUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#DiskUtilization))
      },
      "networkUtilization": {
        object ([NetworkUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#NetworkUtilization))
      },
      "standardSchedulerSettings": {
        object ([StandardSchedulerSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings))
      }
    }  
  
Fields  
---  
`coolDownPeriod` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The time period that the [Autoscaler](https://cloud.google.com/compute/docs/autoscaler/) should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Only applicable in the App Engine flexible environment.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`cpuUtilization` |  `object (`[CpuUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#CpuUtilization)`)` Target scaling by CPU usage.  
`maxConcurrentRequests` |  `integer` Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.Defaults to a runtime-specific value.  
`maxIdleInstances` |  `integer` Maximum number of idle instances that should be maintained for this version.  
`maxTotalInstances` |  `integer` Maximum number of instances that should be started to handle requests for this version.  
`maxPendingLatency` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`minIdleInstances` |  `integer` Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.  
`minTotalInstances` |  `integer` Minimum number of running instances that should be maintained for this version.  
`minPendingLatency` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`requestUtilization` |  `object (`[RequestUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#RequestUtilization)`)` Target scaling by request utilization.  
`diskUtilization` |  `object (`[DiskUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#DiskUtilization)`)` Target scaling by disk usage.  
`networkUtilization` |  `object (`[NetworkUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#NetworkUtilization)`)` Target scaling by network usage.  
`standardSchedulerSettings` |  `object (`[StandardSchedulerSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)`)` Scheduler settings for standard environment.  
  
## CpuUtilization

Target scaling by CPU usage.

JSON representation  
---  
      
    
    {
      "aggregationWindowLength": string,
      "targetUtilization": number
    }  
  
Fields  
---  
`aggregationWindowLength` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Period of time over which CPU utilization is calculated.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`targetUtilization` |  `number` Target CPU utilization ratio to maintain when scaling. Must be between 0 and 1.  
  
## RequestUtilization

Target scaling by request utilization. Only applicable in the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "targetRequestCountPerSecond": integer,
      "targetConcurrentRequests": integer
    }  
  
Fields  
---  
`targetRequestCountPerSecond` |  `integer` Target requests per second.  
`targetConcurrentRequests` |  `integer` Target number of concurrent requests.  
  
## DiskUtilization

Target scaling by disk usage. Only applicable in the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "targetWriteBytesPerSecond": integer,
      "targetWriteOpsPerSecond": integer,
      "targetReadBytesPerSecond": integer,
      "targetReadOpsPerSecond": integer
    }  
  
Fields  
---  
`targetWriteBytesPerSecond` |  `integer` Target bytes written per second.  
`targetWriteOpsPerSecond` |  `integer` Target ops written per second.  
`targetReadBytesPerSecond` |  `integer` Target bytes read per second.  
`targetReadOpsPerSecond` |  `integer` Target ops read per seconds.  
  
## NetworkUtilization

Target scaling by network usage. Only applicable in the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "targetSentBytesPerSecond": integer,
      "targetSentPacketsPerSecond": integer,
      "targetReceivedBytesPerSecond": integer,
      "targetReceivedPacketsPerSecond": integer
    }  
  
Fields  
---  
`targetSentBytesPerSecond` |  `integer` Target bytes sent per second.  
`targetSentPacketsPerSecond` |  `integer` Target packets sent per second.  
`targetReceivedBytesPerSecond` |  `integer` Target bytes received per second.  
`targetReceivedPacketsPerSecond` |  `integer` Target packets received per second.  
  
## StandardSchedulerSettings

Scheduler settings for standard environment.

JSON representation  
---  
      
    
    {
      "targetCpuUtilization": number,
      "targetThroughputUtilization": number,
      "minInstances": integer,
      "maxInstances": integer
    }  
  
Fields  
---  
`targetCpuUtilization` |  `number` Target CPU utilization ratio to maintain when scaling.  
`targetThroughputUtilization` |  `number` Target throughput utilization ratio to maintain when scaling  
`minInstances` |  `integer` Minimum number of instances to run for this version. Set to zero to disable `minInstances` configuration.  
`maxInstances` |  `integer` Maximum number of instances to run for this version. Set to 2147483647 to disable `maxInstances` configuration.  
  
## BasicScaling

A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.

JSON representation  
---  
      
    
    {
      "idleTimeout": string,
      "maxInstances": integer
    }  
  
Fields  
---  
`idleTimeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Duration of time after the last request that an instance must wait before the instance is shut down.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`maxInstances` |  `integer` Maximum number of instances to create for this version.  
  
## ManualScaling

A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.

JSON representation  
---  
      
    
    {
      "instances": integer
    }  
  
Fields  
---  
`instances` |  `integer` Number of instances to assign to the service at the start. This number can later be altered by using the [Modules API](https://cloud.google.com/appengine/docs/python/modules/functions) `set_num_instances()` function.  
  
## InboundServiceType

Available inbound services.

Enums  
---  
`INBOUND_SERVICE_UNSPECIFIED` | Not specified.  
`INBOUND_SERVICE_MAIL` | Allows an application to receive mail.  
`INBOUND_SERVICE_MAIL_BOUNCE` | Allows an application to receive email-bound notifications.  
`INBOUND_SERVICE_XMPP_ERROR` | Allows an application to receive error stanzas.  
`INBOUND_SERVICE_XMPP_MESSAGE` | Allows an application to receive instant messages.  
`INBOUND_SERVICE_XMPP_SUBSCRIBE` | Allows an application to receive user subscription POSTs.  
`INBOUND_SERVICE_XMPP_PRESENCE` | Allows an application to receive a user's chat presence.  
`INBOUND_SERVICE_CHANNEL_PRESENCE` | Registers an application for notifications when a client connects or disconnects from a channel.  
`INBOUND_SERVICE_WARMUP` | Enables warmup requests.  
  
## Network

Extra network settings. Only applicable in the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "forwardedPorts": [
        string
      ],
      "instanceTag": string,
      "name": string,
      "subnetworkName": string,
      "sessionAffinity": boolean
    }  
  
Fields  
---  
`forwardedPorts[]` |  `string` List of ports, or port pairs, to forward from the virtual machine to the application container. Only applicable in the App Engine flexible environment.  
`instanceTag` |  `string` Tag to apply to the instance during creation. Only applicable in the App Engine flexible environment.  
`name` |  `string` Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path.Defaults to `default`.  
`subnetworkName` |  `string` Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path.If a subnetwork name is specified, a network name will also be required unless it is for the default network.

  * If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range.
  * If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetworkName) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network.
  * If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetworkName must be specified and the IP address is created from the IPCidrRange of the subnetwork.

If specified, the subnetwork must exist in the same region as the App Engine flexible environment application.  
`sessionAffinity` |  `boolean` Enable session affinity. Only applicable in the App Engine flexible environment.  
  
## Resources

Machine resources for a version.

JSON representation  
---  
      
    
    {
      "cpu": number,
      "diskGb": number,
      "memoryGb": number,
      "volumes": [
        {
          object ([Volume](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Volume))
        }
      ],
      "kmsKeyReference": string
    }  
  
Fields  
---  
`cpu` |  `number` Number of CPU cores needed.  
`diskGb` |  `number` Disk size (GB) needed.  
`memoryGb` |  `number` Memory (GB) needed.  
`volumes[]` |  `object (`[Volume](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Volume)`)` User specified volumes.  
  
## Volume

Volumes mounted within the app container. Only applicable in the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "name": string,
      "volumeType": string,
      "sizeGb": number
    }  
  
Fields  
---  
`name` |  `string` Unique name for the volume.  
`volumeType` |  `string` Underlying volume type, e.g. 'tmpfs'.  
`sizeGb` |  `number` Volume size in gigabytes.  
  
## FlexibleRuntimeSettings

Runtime settings for the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "operatingSystem": string,
      "runtimeVersion": string
    }  
  
Fields  
---  
`operatingSystem` |  `string` The operating system of the application runtime.  
`runtimeVersion` |  `string` The runtime version of an App Engine flexible application.  
  
## ServingStatus

Run states of a version.

Enums  
---  
`SERVING_STATUS_UNSPECIFIED` | Not specified.  
`SERVING` | Currently serving. Instances are created according to the scaling settings of the version.  
`STOPPED` | Disabled. No instances will be created and the scaling settings are ignored until the state of the version changes to `SERVING`.  
  
## UrlMap

URL pattern and description of how the URL should be handled. App Engine can handle URLs by executing application code or by serving static files uploaded with the version, such as images, CSS, or JavaScript.

JSON representation  
---  
      
    
    {
      "urlRegex": string,
      "securityLevel": enum ([SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#SecurityLevel)),
      "login": enum ([LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#LoginRequirement)),
      "authFailAction": enum ([AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AuthFailAction)),
      "redirectHttpResponseCode": enum ([RedirectHttpResponseCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#RedirectHttpResponseCode)),
    
      // Union field handler_type can be only one of the following:
      "staticFiles": {
        object ([StaticFilesHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler))
      },
      "script": {
        object ([ScriptHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ScriptHandler))
      },
      "apiEndpoint": {
        object ([ApiEndpointHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ApiEndpointHandler))
      }
      // End of list of possible types for union field handler_type.
    }  
  
Fields  
---  
`urlRegex` |  `string` URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings. All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.  
`securityLevel` |  `enum (`[SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#SecurityLevel)`)` Security (HTTPS) enforcement for this URL.  
`login` |  `enum (`[LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#LoginRequirement)`)` Level of login required to access this resource. Not supported for Node.js in the App Engine standard environment.  
`authFailAction` |  `enum (`[AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AuthFailAction)`)` Action to take when users access resources that require authentication. Defaults to `redirect`.  
`redirectHttpResponseCode` |  `enum (`[RedirectHttpResponseCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#RedirectHttpResponseCode)`)` `30x` code to use when performing redirects for the `secure` field. Defaults to `302`.  
Union field `handler_type`. Type of handler for this URL pattern. `handler_type` can be only one of the following:  
`staticFiles` |  `object (`[StaticFilesHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler)`)` Returns the contents of a file, such as an image, as the response.  
`script` |  `object (`[ScriptHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ScriptHandler)`)` Executes a script to handle the requests that match this URL pattern. Only the `auto` value is supported for Node.js in the App Engine standard environment, for example `"script": "auto"`.  
`apiEndpoint` |  `object (`[ApiEndpointHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ApiEndpointHandler)`)` Uses API Endpoints to handle requests.  
  
## StaticFilesHandler

Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.

JSON representation  
---  
      
    
    {
      "path": string,
      "uploadPathRegex": string,
      "httpHeaders": {
        string: string,
        ...
      },
      "mimeType": string,
      "expiration": string,
      "requireMatchingFile": boolean,
      "applicationReadable": boolean
    }  
  
Fields  
---  
`path` |  `string` Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern.  
`uploadPathRegex` |  `string` Regular expression that matches the file paths for all files that should be referenced by this handler.  
`httpHeaders` |  `map (key: string, value: string)` HTTP headers to use for all responses from these URLs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`mimeType` |  `string` MIME type used to serve all files served by this handler.Defaults to file-specific MIME types, which are derived from each file's filename extension.  
`expiration` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Time a static file served by this handler should be cached by web proxies and browsers.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`requireMatchingFile` |  `boolean` Whether this handler should match the request if the file referenced by the handler does not exist.  
`applicationReadable` |  `boolean` Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged against both your code and static data storage resource quotas.  
  
## ScriptHandler

Executes a script to handle the request that matches the URL pattern.

JSON representation  
---  
      
    
    {
      "scriptPath": string
    }  
  
Fields  
---  
`scriptPath` |  `string` Path to the script from the application root directory.  
  
## ApiEndpointHandler

Uses Google Cloud Endpoints to handle requests.

JSON representation  
---  
      
    
    {
      "scriptPath": string
    }  
  
Fields  
---  
`scriptPath` |  `string` Path to the script from the application root directory.  
  
## SecurityLevel

Methods to enforce security (HTTPS) on a URL.

Enums  
---  
`SECURE_UNSPECIFIED` | Not specified.  
`SECURE_DEFAULT` | Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used, and respond accordingly.  
`SECURE_NEVER` | Requests for a URL that match this handler that use HTTPS are automatically redirected to the HTTP equivalent URL.  
`SECURE_OPTIONAL` | Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used and respond accordingly.  
`SECURE_ALWAYS` | Requests for a URL that match this handler that do not use HTTPS are automatically redirected to the HTTPS URL with the same path. Query parameters are reserved for the redirect.  
  
## LoginRequirement

Methods to restrict access to a URL based on login status.

Enums  
---  
`LOGIN_UNSPECIFIED` | Not specified. `LOGIN_OPTIONAL` is assumed.  
`LOGIN_OPTIONAL` | Does not require that the user is signed in.  
`LOGIN_ADMIN` | If the user is not signed in, the `authFailAction` is taken. In addition, if the user is not an administrator for the application, they are given an error message regardless of `authFailAction`. If the user is an administrator, the handler proceeds.  
`LOGIN_REQUIRED` | If the user has signed in, the handler proceeds normally. Otherwise, the authFailAction is taken.  
  
## AuthFailAction

Actions to take when the user is not logged in.

Enums  
---  
`AUTH_FAIL_ACTION_UNSPECIFIED` | Not specified. `AUTH_FAIL_ACTION_REDIRECT` is assumed.  
`AUTH_FAIL_ACTION_REDIRECT` | Redirects user to "accounts.google.com". The user is redirected back to the application URL after signing in or creating an account.  
`AUTH_FAIL_ACTION_UNAUTHORIZED` | Rejects request with a `401` HTTP status code and an error message.  
  
## RedirectHttpResponseCode

Redirect codes.

Enums  
---  
`REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED` | Not specified. `302` is assumed.  
`REDIRECT_HTTP_RESPONSE_CODE_301` | `301 Moved Permanently` code.  
`REDIRECT_HTTP_RESPONSE_CODE_302` | `302 Moved Temporarily` code.  
`REDIRECT_HTTP_RESPONSE_CODE_303` | `303 See Other` code.  
`REDIRECT_HTTP_RESPONSE_CODE_307` | `307 Temporary Redirect` code.  
  
## ErrorHandler

Custom static error page to be served when an error occurs.

JSON representation  
---  
      
    
    {
      "errorCode": enum ([ErrorCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ErrorCode)),
      "staticFile": string,
      "mimeType": string
    }  
  
Fields  
---  
`errorCode` |  `enum (`[ErrorCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ErrorCode)`)` Error condition this handler applies to.  
`staticFile` |  `string` Static file content to be served for this error.  
`mimeType` |  `string` MIME type of file. Defaults to `text/html`.  
  
## ErrorCode

Error codes.

Enums  
---  
`ERROR_CODE_UNSPECIFIED` | Not specified. ERROR_CODE_DEFAULT is assumed.  
`ERROR_CODE_DEFAULT` | All other error types.  
`ERROR_CODE_OVER_QUOTA` | Application has exceeded a resource quota.  
`ERROR_CODE_DOS_API_DENIAL` | Client blocked by the application's Denial of Service protection configuration.  
`ERROR_CODE_TIMEOUT` | Deadline reached before the application responds.  
  
## Library

Third-party Python runtime library that is required by the application.

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string
    }  
  
Fields  
---  
`name` |  `string` Name of the library. Example: "django".  
`version` |  `string` Version of the library to select, or "latest".  
  
## ApiConfigHandler

[Google Cloud Endpoints](https://cloud.google.com/endpoints) configuration for API handlers.

JSON representation  
---  
      
    
    {
      "authFailAction": enum ([AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AuthFailAction)),
      "login": enum ([LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#LoginRequirement)),
      "script": string,
      "securityLevel": enum ([SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#SecurityLevel)),
      "url": string
    }  
  
Fields  
---  
`authFailAction` |  `enum (`[AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AuthFailAction)`)` Action to take when users access resources that require authentication. Defaults to `redirect`.  
`login` |  `enum (`[LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#LoginRequirement)`)` Level of login required to access this resource. Defaults to `optional`.  
`script` |  `string` Path to the script from the application root directory.  
`securityLevel` |  `enum (`[SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#SecurityLevel)`)` Security (HTTPS) enforcement for this URL.  
`url` |  `string` URL to serve the endpoint at.  
  
## HealthCheck

Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "disableHealthCheck": boolean,
      "host": string,
      "healthyThreshold": integer,
      "unhealthyThreshold": integer,
      "restartThreshold": integer,
      "checkInterval": string,
      "timeout": string
    }  
  
Fields  
---  
`disableHealthCheck` |  `boolean` Whether to explicitly disable health checks for this instance.  
`host` |  `string` Host header to send when performing an HTTP health check. Example: "myapp.appspot.com"  
`healthyThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive successful health checks required before receiving traffic.  
`unhealthyThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive failed health checks required before removing traffic.  
`restartThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive failed health checks required before an instance is restarted.  
`checkInterval` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Interval between health checks.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Time before the health check is considered failed.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ReadinessCheck

Readiness checking configuration for VM instances. Unhealthy instances are removed from traffic rotation.

JSON representation  
---  
      
    
    {
      "path": string,
      "host": string,
      "failureThreshold": integer,
      "successThreshold": integer,
      "checkInterval": string,
      "timeout": string,
      "appStartTimeout": string
    }  
  
Fields  
---  
`path` |  `string` The request path.  
`host` |  `string` Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com"  
`failureThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive failed checks required before removing traffic.  
`successThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive successful checks required before receiving traffic.  
`checkInterval` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Interval between health checks.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Time before the check is considered failed.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`appStartTimeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` A maximum time limit on application initialization, measured from moment the application successfully replies to a healthcheck until it is ready to serve traffic.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## LivenessCheck

Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.

JSON representation  
---  
      
    
    {
      "path": string,
      "host": string,
      "failureThreshold": integer,
      "successThreshold": integer,
      "checkInterval": string,
      "timeout": string,
      "initialDelay": string
    }  
  
Fields  
---  
`path` |  `string` The request path.  
`host` |  `string` Host header to send when performing a HTTP Liveness check. Example: "myapp.appspot.com"  
`failureThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive failed checks required before considering the VM unhealthy.  
`successThreshold` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Number of consecutive successful checks required before considering the VM healthy.  
`checkInterval` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Interval between health checks.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` Time before the check is considered failed.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`initialDelay` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The initial delay before starting to execute the checks.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Deployment

Code and application artifacts used to deploy a version to App Engine.

JSON representation  
---  
      
    
    {
      "files": {
        string: {
          object ([FileInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#FileInfo))
        },
        ...
      },
      "container": {
        object ([ContainerInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ContainerInfo))
      },
      "zip": {
        object ([ZipInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ZipInfo))
      },
      "cloudBuildOptions": {
        object ([CloudBuildOptions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#CloudBuildOptions))
      }
    }  
  
Fields  
---  
`files` |  `map (key: string, value: object (`[FileInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#FileInfo)`))` Manifest of the files stored in Google Cloud Storage that are included as part of this version. All files must be readable using the credentials supplied with this call.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`container` |  `object (`[ContainerInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ContainerInfo)`)` The Docker image for the container that runs the version. Only applicable for instances running in the App Engine flexible environment.  
`zip` |  `object (`[ZipInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#ZipInfo)`)` The zip file for this deployment, if this is a zip deployment.  
`cloudBuildOptions` |  `object (`[CloudBuildOptions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#CloudBuildOptions)`)` Options for any Google Cloud Build builds created as a part of this deployment.These options will only be used if a new build is created, such as when deploying to the App Engine flexible environment using files or zip.  
  
## FileInfo

Single source file that is part of the version to be deployed. Each source file that is deployed must be specified separately.

JSON representation  
---  
      
    
    {
      "sourceUrl": string,
      "sha1Sum": string,
      "mimeType": string
    }  
  
Fields  
---  
`sourceUrl` |  `string` URL source to use to fetch this file. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'.  
`sha1Sum` |  `string` The SHA1 hash of the file, in hex.  
`mimeType` |  `string` The MIME type of the file.Defaults to the value from Google Cloud Storage.  
  
## ContainerInfo

Docker image that is used to create a container and start a VM instance for the version that you deploy. Only applicable for instances running in the App Engine flexible environment.

JSON representation  
---  
      
    
    {
      "image": string
    }  
  
Fields  
---  
`image` |  `string` URI to the hosted container image in Google Container Registry. The URI must be fully qualified and include a tag or digest. Examples: "gcr.io/my-project/image:tag" or "gcr.io/my-project/image@digest"  
  
## ZipInfo

The zip file information for a zip deployment.

JSON representation  
---  
      
    
    {
      "sourceUrl": string,
      "filesCount": integer
    }  
  
Fields  
---  
`sourceUrl` |  `string` URL of the zip file to deploy from. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'.  
`filesCount` |  `integer` An estimate of the number of files in a zip for a zip deployment. If set, must be greater than or equal to the actual number of files. Used for optimizing performance; if not provided, deployment may be slow.  
  
## CloudBuildOptions

Options for the build operations performed as a part of the version deployment. Only applicable for App Engine flexible environment when creating a version using source code directly.

JSON representation  
---  
      
    
    {
      "appYamlPath": string,
      "cloudBuildTimeout": string
    }  
  
Fields  
---  
`appYamlPath` |  `string` Path to the yaml file used in deployment, used to determine runtime configuration details.Required for flexible environment builds.See <https://cloud.google.com/appengine/docs/standard/python/config/appref> for more details.  
`cloudBuildTimeout` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The Cloud Build timeout used as part of any dependent builds performed by version creation. Defaults to 10 minutes.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## EndpointsApiService

[Google Cloud Endpoints](https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.

The fields here refer to the name and configuration ID of a "service" resource in the [Service Management API](https://cloud.google.com/service-management/overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "configId": string,
      "rolloutStrategy": enum ([RolloutStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#RolloutStrategy)),
      "disableTraceSampling": boolean
    }  
  
Fields  
---  
`name` |  `string` Endpoints service name which is the name of the "service" resource in the Service Management API. For example "myapi.endpoints.myproject.cloud.goog"  
`configId` |  `string` Endpoints service configuration ID as specified by the Service Management API. For example "2016-09-19r1".By default, the rollout strategy for Endpoints is `RolloutStrategy.FIXED`. This means that Endpoints starts up with a particular configuration ID. When a new configuration is rolled out, Endpoints must be given the new configuration ID. The `configId` field is used to give the configuration ID and is required in this case.Endpoints also has a rollout strategy called `RolloutStrategy.MANAGED`. When using this, Endpoints fetches the latest configuration and does not need the configuration ID. In this case, `configId` must be omitted.  
`rolloutStrategy` |  `enum (`[RolloutStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#RolloutStrategy)`)` Endpoints rollout strategy. If `FIXED`, `configId` must be specified. If `MANAGED`, `configId` must be omitted.  
`disableTraceSampling` |  `boolean` Enable or disable trace sampling. By default, this is set to false for enabled.  
  
## RolloutStrategy

Available rollout strategies.

Enums  
---  
`UNSPECIFIED_ROLLOUT_STRATEGY` | Not specified. Defaults to `FIXED`.  
`FIXED` | Endpoints service configuration ID will be fixed to the configuration ID specified by `configId`.  
`MANAGED` | Endpoints service configuration ID will be updated with each rollout.  
  
## Entrypoint

The entrypoint for the application.

JSON representation  
---  
      
    
    {
      "shell": string
    }  
  
Fields  
---  
`shell` |  `string` The format should be a shell command that can be fed to `bash -c`.  
  
## VpcAccessConnector

VPC access connector specification.

JSON representation  
---  
      
    
    {
      "name": string,
      "egressSetting": enum ([EgressSetting](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#EgressSetting))
    }  
  
Fields  
---  
`name` |  `string` Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.  
`egressSetting` |  `enum (`[EgressSetting](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#EgressSetting)`)` The egress setting for the connector, controlling what traffic is diverted through it.  
  
## EgressSetting

Available egress settings.

This controls what traffic is diverted through the VPC Access Connector resource. By default PRIVATE_IP_RANGES will be used.

Enums  
---  
`EGRESS_SETTING_UNSPECIFIED` |   
`ALL_TRAFFIC` | Force the use of VPC Access for all egress traffic from the function.  
`PRIVATE_IP_RANGES` | Use the VPC Access Connector for private IP space from RFC1918.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/create)`

|  Deploys code and resource files to a new version.  
  
### `[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/delete)`

|  Deletes an existing Version resource.  
  
### `[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/get)`

|  Gets the specified Version resource.  
  
### `[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/list)`

|  Lists the versions of a service.  
  
### `[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch)`

|  Updates the specified Version resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
