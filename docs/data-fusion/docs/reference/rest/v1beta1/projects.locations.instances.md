---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:10.047233+00:00
---

# REST Resource: projects.locations.instances  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * Type
  * NetworkConfig
    * JSON representation
  * ConnectionType
  * PrivateServiceConnectConfig
    * JSON representation
  * State
  * Version
    * JSON representation
  * Type
  * Accelerator
    * JSON representation
  * AcceleratorType
  * State
  * CryptoKeyConfig
    * JSON representation
  * DisabledReason
  * EventPublishConfig
    * JSON representation
  * MaintenancePolicy
    * JSON representation
  * MaintenanceWindow
    * JSON representation
  * RecurringTimeWindow
    * JSON representation
  * TimeWindow
    * JSON representation
  * MaintenanceEvent
    * JSON representation
  * State
  * LoggingConfig
    * JSON representation
  * MonitoringConfig
    * JSON representation
  * Methods



## Resource: Instance

Represents a Data Fusion instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([Type](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Type)),
      "enableStackdriverLogging": boolean,
      "enableStackdriverMonitoring": boolean,
      "privateInstance": boolean,
      "networkConfig": {
        object ([NetworkConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#NetworkConfig))
      },
      "labels": {
        string: string,
        ...
      },
      "options": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#State)),
      "stateMessage": string,
      "serviceEndpoint": string,
      "zone": string,
      "version": string,
      "serviceAccount": string,
      "displayName": string,
      "availableVersion": [
        {
          object ([Version](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Version))
        }
      ],
      "apiEndpoint": string,
      "gcsBucket": string,
      "accelerators": [
        {
          object ([Accelerator](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Accelerator))
        }
      ],
      "p4ServiceAccount": string,
      "tenantProjectId": string,
      "dataprocServiceAccount": string,
      "enableRbac": boolean,
      "cryptoKeyConfig": {
        object ([CryptoKeyConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#CryptoKeyConfig))
      },
      "disabledReason": [
        enum ([DisabledReason](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#DisabledReason))
      ],
      "eventPublishConfig": {
        object ([EventPublishConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#EventPublishConfig))
      },
      "enableZoneSeparation": boolean,
      "satisfiesPzs": boolean,
      "workforceIdentityServiceEndpoint": string,
      "patchRevision": string,
      "dataplexDataLineageIntegrationEnabled": boolean,
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MaintenancePolicy))
      },
      "tags": {
        string: string,
        ...
      },
      "maintenanceEvents": [
        {
          object ([MaintenanceEvent](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MaintenanceEvent))
        }
      ],
      "loggingConfig": {
        object ([LoggingConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#LoggingConfig))
      },
      "satisfiesPzi": boolean,
      "monitoringConfig": {
        object ([MonitoringConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MonitoringConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}.  
`description` |  `string` Optional. A description of this instance.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Type)`)` Required. Instance type.  
`enableStackdriverLogging` |  `boolean` Optional. Option to enable Dataproc Stackdriver Logging.  
`enableStackdriverMonitoring` |  `boolean` Optional. Option to enable Stackdriver Monitoring.  
`privateInstance` |  `boolean` Optional. Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet.  
`networkConfig` |  `object (`[NetworkConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#NetworkConfig)`)` Optional. Network configuration options. These are required when a private Data Fusion instance is to be created.  
`labels` |  `map (key: string, value: string)` The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`options` |  `map (key: string, value: string)` Optional. Map of additional options used to configure the behavior of Data Fusion instance.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the instance was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#State)`)` Output only. The current state of this Data Fusion instance.  
`stateMessage` |  `string` Output only. Additional information about the current state of this Data Fusion instance if available.  
`serviceEndpoint` |  `string` Output only. Endpoint on which the Data Fusion UI is accessible.  
`zone` |  `string` Optional. Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field.  
`version` |  `string` Optional. Current version of Data Fusion.  
`serviceAccount  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated. Use tenantProjectId instead to extract the tenant project ID.  
`displayName` |  `string` Optional. Display name for an instance.  
`availableVersion[]` |  `object (`[Version](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Version)`)` Output only. Available versions that the instance can be upgraded to using UpdateInstanceRequest.  
`apiEndpoint` |  `string` Output only. Endpoint on which the REST APIs is accessible.  
`gcsBucket` |  `string` Output only. Cloud Storage bucket generated by Data Fusion in the customer project.  
`accelerators[]` |  `object (`[Accelerator](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Accelerator)`)` Output only. List of accelerators enabled for this CDF instance.  
`p4ServiceAccount` |  `string` Output only. Service agent for the customer project.  
`tenantProjectId` |  `string` Output only. The name of the tenant project.  
`dataprocServiceAccount` |  `string` Optional. User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines.This allows users to have fine-grained access control on Dataproc's accesses to cloud resources.  
`enableRbac` |  `boolean` Optional. Option to enable granular role-based access control.  
`cryptoKeyConfig` |  `object (`[CryptoKeyConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#CryptoKeyConfig)`)` Optional. The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.  
`disabledReason[]` |  `enum (`[DisabledReason](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#DisabledReason)`)` Output only. If the instance state is DISABLED, the reason for disabling the instance.  
`eventPublishConfig` |  `object (`[EventPublishConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#EventPublishConfig)`)` Optional. Option to enable and pass metadata for event publishing.  
`enableZoneSeparation` |  `boolean` Output only. Option to enable zone separation.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`workforceIdentityServiceEndpoint` |  `string` Output only. Endpoint on which the Data Fusion UI is accessible to third-party users.  
`patchRevision` |  `string` Optional. Current patch revision of the Data Fusion.  
`dataplexDataLineageIntegrationEnabled` |  `boolean` Optional. Option to enable the Dataplex Lineage Integration feature.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MaintenancePolicy)`)` Optional. Configure the maintenance policy for this instance.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`maintenanceEvents[]` |  `object (`[MaintenanceEvent](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MaintenanceEvent)`)` Output only. The maintenance events for this instance.  
`loggingConfig` |  `object (`[LoggingConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#LoggingConfig)`)` Optional. The logging configuration for this instance. This field is supported only in CDF versions 6.11.0 and above.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
`monitoringConfig` |  `object (`[MonitoringConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MonitoringConfig)`)` Optional. The monitoring configuration for this instance.  
  
## Type

Represents the type of Data Fusion instance. Each type is configured with the default settings for processing and memory.

Enums  
---  
`TYPE_UNSPECIFIED` | No type specified. The instance creation will fail.  
`BASIC` | Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines using point and click UI. However, there are certain limitations, such as fewer number of concurrent pipelines, no support for streaming pipelines, etc.  
`ENTERPRISE` | Enterprise Data Fusion instance. In Enterprise type, the user will have all features available, such as support for streaming pipelines, unlimited number of concurrent pipelines, etc.  
`DEVELOPER` | Developer Data Fusion instance. In Developer type, the user will have all features available but with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration pipelines at low cost.  
  
## NetworkConfig

Network configuration for a Data Fusion instance. These configurations are used for peering with the customer network. Configurations are optional when a public Data Fusion instance is to be created. However, providing these configurations allows several benefits, such as reduced network latency while accessing the customer resources from managed Data Fusion instance nodes, as well as access to the customer on-prem resources.

JSON representation  
---  
      
    
    {
      "network": string,
      "ipAllocation": string,
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#ConnectionType)),
      "privateServiceConnectConfig": {
        object ([PrivateServiceConnectConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#PrivateServiceConnectConfig))
      }
    }  
  
Fields  
---  
`network` |  `string` Optional. Name of the network in the customer project with which the Tenant Project will be peered for executing pipelines. In case of shared VPC where the network resides in another host project the network should specified in the form of projects/{host-project-id}/global/networks/{network}. This is only required for connectivity type VPC_PEERING.  
`ipAllocation` |  `string` Optional. The IP range in CIDR notation to use for the managed Data Fusion instance nodes. This range must not overlap with any other ranges used in the Data Fusion instance network. This is required only when using connection type VPC_PEERING. Format: a.b.c.d/22Example: 192.168.0.0/22  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#ConnectionType)`)` Optional. Type of connection for establishing private IP connectivity between the Data Fusion customer project VPC and the corresponding tenant project from a predefined list of available connection modes. If this field is unspecified for a private instance, VPC peering is used.  
`privateServiceConnectConfig` |  `object (`[PrivateServiceConnectConfig](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#PrivateServiceConnectConfig)`)` Optional. Configuration for Private Service Connect. This is required only when using connection type PRIVATE_SERVICE_CONNECT_INTERFACES.  
  
## ConnectionType

Represents connection type between the consumer project VPC and the corresponding Data Fusion tenant project, from a predefined list of available connection modes.

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | No specific connection type was requested, the default value of VPC_PEERING is chosen.  
`VPC_PEERING` | Requests the use of VPC peerings for connecting the consumer and tenant projects.  
`PRIVATE_SERVICE_CONNECT_INTERFACES` | Requests the use of Private Service Connect Interfaces for connecting the consumer and tenant projects.  
  
## PrivateServiceConnectConfig

Configuration for using Private Service Connect to establish connectivity between the Data Fusion consumer project and the corresponding tenant project.

JSON representation  
---  
      
    
    {
      "networkAttachment": string,
      "unreachableCidrBlock": string,
      "effectiveUnreachableCidrBlock": string
    }  
  
Fields  
---  
`networkAttachment` |  `string` Required. The reference to the network attachment used to establish private connectivity. It will be of the form projects/{project-id}/regions/{region}/networkAttachments/{network-attachment-id}.  
`unreachableCidrBlock` |  `string` Optional. Input only. The CIDR block to which the CDF instance can't route traffic to in the consumer project VPC. The size of this block should be at least /25. This range should not overlap with the primary address range of any subnetwork used by the network attachment. This range can be used for other purposes in the consumer VPC as long as there is no requirement for CDF to reach destinations using these addresses. If this value is not provided, the server chooses a non RFC 1918 address range. The format of this field is governed by RFC 4632.Example: 192.168.0.0/25  
`effectiveUnreachableCidrBlock` |  `string` Output only. The CIDR block to which the CDF instance can't route traffic to in the consumer project VPC. The size of this block is /25. The format of this field is governed by RFC 4632.Example: 240.0.0.0/25  
  
## State

Represents the state of a Data Fusion instance

Enums  
---  
`STATE_UNSPECIFIED` | Instance does not have a state yet  
`CREATING` | Instance is being created  
`RUNNING` | Instance is running and ready for requests  
`FAILED` | Instance creation failed  
`DELETING` | Instance is being deleted  
`UPGRADING` | Instance is being upgraded  
`RESTARTING` | Instance is being restarted  
`UPDATING` | Instance is being updated on customer request  
`AUTO_UPDATING` | Instance is being auto-updated  
`AUTO_UPGRADING` | Instance is being auto-upgraded  
`DISABLED` | Instance is disabled  
`ENABLING` | Instance is being enabled.  
  
## Version

The Data Fusion version.

JSON representation  
---  
      
    
    {
      "versionNumber": string,
      "defaultVersion": boolean,
      "availableFeatures": [
        string
      ],
      "type": enum ([Type](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Type_1))
    }  
  
Fields  
---  
`versionNumber` |  `string` The version number of the Data Fusion instance, such as '6.0.1.0'.  
`defaultVersion` |  `boolean` Whether this is currently the default version for Cloud Data Fusion  
`availableFeatures[]` |  `string` Represents a list of available feature names for a given version.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#Type_1)`)` Type represents the release availability of the version  
  
## Type

Each type represents the release availability of a CDF version

Enums  
---  
`TYPE_UNSPECIFIED` | Version does not have availability yet  
`TYPE_PREVIEW` | Version is under development and not considered stable  
`TYPE_GENERAL_AVAILABILITY` | Version is available for public use  
`TYPE_DEPRECATED` | Version is no longer supported.  
  
## Accelerator

Identifies Cloud Data Fusion accelerators for an instance.

JSON representation  
---  
      
    
    {
      "acceleratorType": enum ([AcceleratorType](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#AcceleratorType)),
      "state": enum ([State](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#State_1))
    }  
  
Fields  
---  
`acceleratorType` |  `enum (`[AcceleratorType](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#AcceleratorType)`)` Optional. The type of an accelator for a Cloud Data Fusion instance.  
`state` |  `enum (`[State](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#State_1)`)` Output only. The state of the accelerator.  
  
## AcceleratorType

Each type represents an Accelerator (Add-On) supported by Cloud Data Fusion service.

Enums  
---  
`ACCELERATOR_TYPE_UNSPECIFIED` | Default value, if unspecified.  
`CDC` | Change Data Capture accelerator for Cloud Data Fusion.  
`HEALTHCARE` | Reserved for internal use.  
`CCAI_INSIGHTS` | Contact Center AI Insights This accelerator is used to enable import and export pipelines custom built to streamline CCAI Insights processing.  
`CLOUDSEARCH` | Reserved for internal use.  
  
## State

Different values possible for the state of an accelerator.

Enums  
---  
`STATE_UNSPECIFIED` | Default value, do not use.  
`ENABLED` | Indicates that the accelerator is enabled and available to use.  
`DISABLED` | Indicates that the accelerator is disabled and not available to use.  
`UNKNOWN` | Indicates that accelerator state is currently unknown. Requests for enable, disable could be retried while in this state.  
  
## CryptoKeyConfig

The crypto key configuration. This field is used by the Customer-managed encryption keys (CMEK) feature.

JSON representation  
---  
      
    
    {
      "keyReference": string
    }  
  
Fields  
---  
`keyReference` |  `string` Optional. The name of the key which is used to encrypt/decrypt customer data. For key in Cloud KMS, the key should be in the format of `projects/*/locations/*/keyRings/*/cryptoKeys/*`.  
  
## DisabledReason

The reason for disabling the instance if the state is DISABLED.

Enums  
---  
`DISABLED_REASON_UNSPECIFIED` | This is an unknown reason for disabling.  
`KMS_KEY_ISSUE` | The KMS key used by the instance is either revoked or denied access to  
`PROJECT_STATE_OFF` | The consumer project is in a non-ACTIVE state.  
  
## EventPublishConfig

Confirguration of PubSubEventWriter.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "topic": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Required. Option to enable Event Publishing.  
`topic` |  `string` Required. The resource name of the Pub/Sub topic. Format: projects/{projectId}/topics/{topic_id}  
  
## MaintenancePolicy

Maintenance policy of the instance.

JSON representation  
---  
      
    
    {
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MaintenanceWindow))
      },
      "maintenanceExclusionWindow": {
        object ([TimeWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#TimeWindow))
      }
    }  
  
Fields  
---  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#MaintenanceWindow)`)` Optional. The maintenance window of the instance.  
`maintenanceExclusionWindow` |  `object (`[TimeWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#TimeWindow)`)` Optional. The maintenance exclusion window of the instance.  
  
## MaintenanceWindow

Maintenance window of the instance.

JSON representation  
---  
      
    
    {
      "recurringTimeWindow": {
        object ([RecurringTimeWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#RecurringTimeWindow))
      }
    }  
  
Fields  
---  
`recurringTimeWindow` |  `object (`[RecurringTimeWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#RecurringTimeWindow)`)` Required. The recurring time window of the maintenance window.  
  
## RecurringTimeWindow

Represents an arbitrary window of time that recurs.

JSON representation  
---  
      
    
    {
      "window": {
        object ([TimeWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#TimeWindow))
      },
      "recurrence": string
    }  
  
Fields  
---  
`window` |  `object (`[TimeWindow](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#TimeWindow)`)` Required. The window representing the start and end time of recurrences. This field ignores the date components of the provided timestamps. Only the time of day and duration between start and end time are relevant.  
`recurrence` |  `string` Required. An RRULE with format [RFC-5545](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for how this window reccurs. They go on for the span of time between the start and end time. The only supported FREQ value is "WEEKLY". To have something repeat every weekday, use: "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR". This specifies how frequently the window starts. To have a 9 am - 5 pm UTC-4 window every weekday, use something like:
    
    
    start time = 2019-01-01T09:00:00-0400
    end time = 2019-01-01T17:00:00-0400
    recurrence = FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR
      
  
## TimeWindow

Represents an arbitrary window of time.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The start time of the time window provided in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Example: "2024-01-01T12:04:06-04:00"Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The end time of the time window provided in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. The end time should take place after the start time. Example: "2024-01-02T12:04:06-06:00"Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## MaintenanceEvent

Represents a maintenance event.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#State_2))
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the maintenance event provided in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Example: "2024-01-01T12:04:06-04:00"Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the maintenance event provided in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Example: "2024-01-02T12:04:06-06:00" This field will be empty if the maintenance event is not yet complete.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances#State_2)`)` Output only. The state of the maintenance event.  
  
## State

The state of the maintenance event.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the maintenance event is unspecified.  
`SCHEDULED` | The maintenance is scheduled but has not started.  
`STARTED` | The maintenance has been started.  
`COMPLETED` | The maintenance has been completed.  
  
## LoggingConfig

Logging configuration for a Data Fusion instance.

JSON representation  
---  
      
    
    {
      "instanceCloudLoggingDisabled": boolean,
      "enableInstanceV2Logs": boolean
    }  
  
Fields  
---  
`instanceCloudLoggingDisabled` |  `boolean` Optional. Option to determine whether instance logs should be written to Cloud Logging. By default, instance logs are written to Cloud Logging.  
`enableInstanceV2Logs` |  `boolean` Optional. Option to enable the InstanceV2 logging for this instance. This field is supported only in CDF patch revision versions 6.11.1.1 and above.  
  
## MonitoringConfig

Monitoring configuration for a Data Fusion instance.

JSON representation  
---  
      
    
    {
      "enableInstanceV2Metrics": boolean
    }  
  
Fields  
---  
`enableInstanceV2Metrics` |  `boolean` Optional. Option to enable the instance v2 metrics for this instance. This field is supported only in CDF versions 6.11.1.1 and above.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/create)`

|  Creates a new Data Fusion instance in the specified project and location.  
  
### `[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/delete)`

|  Deletes a single Data Fusion instance.  
  
### `[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/get)`

|  Gets details of a single Data Fusion instance.  
  
### `[getIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/list)`

|  Lists Data Fusion instances in the specified project and location.  
  
### `[patch](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/patch)`

|  Updates a single Data Fusion instance.  
  
### `[restart](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/restart)`

|  Restart a single Data Fusion instance.  
  
### `[setIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[upgrade](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/upgrade)`

|  Upgrade a single Data Fusion instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
