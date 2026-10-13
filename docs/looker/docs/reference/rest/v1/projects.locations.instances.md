---
url: https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:23.859546+00:00
---

# REST Resource: projects.locations.instances  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * State
  * PlatformEdition
  * PscConfig
    * JSON representation
  * ServiceAttachment
    * JSON representation
  * ConnectionStatus
  * MaintenanceWindow
    * JSON representation
  * DayOfWeek
  * TimeOfDay
    * JSON representation
  * DenyMaintenancePeriod
    * JSON representation
  * Date
    * JSON representation
  * MaintenanceSchedule
    * JSON representation
  * UserMetadata
    * JSON representation
  * CustomDomain
    * JSON representation
  * CustomDomainState
  * AdminSettings
    * JSON representation
  * OAuthConfig
    * JSON representation
  * ControlledEgressConfig
    * JSON representation
  * PeriodicExportConfig
    * JSON representation
  * IngressIpAllowlistConfig
    * JSON representation
  * IngressIpAllowlistRule
    * JSON representation
  * ReleaseChannel
  * SoftDeleteReason
  * Methods



## Resource: Instance

A Looker instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#State)),
      "platformEdition": enum ([PlatformEdition](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#PlatformEdition)),
      "publicIpEnabled": boolean,
      "privateIpEnabled": boolean,
      "lookerVersion": string,
      "egressPublicIp": string,
      "ingressPrivateIp": string,
      "ingressPublicIp": string,
      "lookerUri": string,
      "pscEnabled": boolean,
      "pscConfig": {
        object ([PscConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#PscConfig))
      },
      "consumerNetwork": string,
      "reservedRange": string,
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#MaintenanceWindow))
      },
      "denyMaintenancePeriod": {
        object ([DenyMaintenancePeriod](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#DenyMaintenancePeriod))
      },
      "lastDenyMaintenancePeriod": {
        object ([DenyMaintenancePeriod](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#DenyMaintenancePeriod))
      },
      "maintenanceSchedule": {
        object ([MaintenanceSchedule](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#MaintenanceSchedule))
      },
      "userMetadata": {
        object ([UserMetadata](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#UserMetadata))
      },
      "customDomain": {
        object ([CustomDomain](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#CustomDomain))
      },
      "encryptionConfig": {
        object ([EncryptionConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/EncryptionConfig))
      },
      "adminSettings": {
        object ([AdminSettings](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#AdminSettings))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#OAuthConfig))
      },
      "linkedLspProjectNumber": string,
      "fipsEnabled": boolean,
      "geminiEnabled": boolean,
      "controlledEgressConfig": {
        object ([ControlledEgressConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ControlledEgressConfig))
      },
      "controlledEgressEnabled": boolean,
      "periodicExportConfig": {
        object ([PeriodicExportConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#PeriodicExportConfig))
      },
      "ingressIpAllowlistConfig": {
        object ([IngressIpAllowlistConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#IngressIpAllowlistConfig))
      },
      "releaseChannel": enum ([ReleaseChannel](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ReleaseChannel)),
      "softDeleteReason": enum ([SoftDeleteReason](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#SoftDeleteReason)),
      "suspendedTime": string,
      "catalogIntegrationOptOut": boolean,
      "acceleratedSecurityPatchEnabled": boolean,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. Format: `projects/{project}/locations/{location}/instances/{instance}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the Looker instance provisioning was first requested.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the Looker instance was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#State)`)` Output only. The state of the instance.  
`platformEdition` |  `enum (`[PlatformEdition](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#PlatformEdition)`)` Platform edition.  
`publicIpEnabled` |  `boolean` Whether public IP is enabled on the Looker instance.  
`privateIpEnabled` |  `boolean` Whether private IP is enabled on the Looker instance.  
`lookerVersion` |  `string` Output only. The Looker version that the instance is using.  
`egressPublicIp` |  `string` Output only. Public Egress IP (IPv4).  
`ingressPrivateIp` |  `string` Output only. Private Ingress IP (IPv4).  
`ingressPublicIp` |  `string` Output only. Public Ingress IP (IPv4).  
`lookerUri` |  `string` Output only. Looker instance URI which can be used to access the Looker Instance UI.  
`pscEnabled` |  `boolean` Optional. Whether to use Private Service Connect (PSC) for private IP connectivity. If true, neither `publicIpEnabled` nor `privateIpEnabled` can be true.  
`pscConfig` |  `object (`[PscConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#PscConfig)`)` Optional. PSC configuration. Used when `pscEnabled` is true.  
`consumerNetwork` |  `string` Network name in the consumer project. Format: `projects/{project}/global/networks/{network}`. Note that the consumer network may be in a different GCP project than the consumer project that is hosting the Looker Instance.  
`reservedRange` |  `string` Name of a reserved IP address range within the `[Instance.consumer_network](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#Instance.FIELDS.consumer_network)`, to be used for private services access connection. May or may not be specified in a create request.  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#MaintenanceWindow)`)` Maintenance window for this instance.  
`denyMaintenancePeriod` |  `object (`[DenyMaintenancePeriod](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#DenyMaintenancePeriod)`)` Maintenance denial period for this instance.  
`lastDenyMaintenancePeriod` |  `object (`[DenyMaintenancePeriod](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#DenyMaintenancePeriod)`)` Output only. Last computed maintenance denial period for this instance.  
`maintenanceSchedule` |  `object (`[MaintenanceSchedule](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#MaintenanceSchedule)`)` Maintenance schedule for this instance.  
`userMetadata` |  `object (`[UserMetadata](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#UserMetadata)`)` Optional. User metadata.  
`customDomain` |  `object (`[CustomDomain](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#CustomDomain)`)` Custom domain configuration for the instance.  
`encryptionConfig` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/EncryptionConfig)`)` Encryption configuration (CMEK). Only set if CMEK has been enabled on the instance.  
`adminSettings` |  `object (`[AdminSettings](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#AdminSettings)`)` Looker Instance Admin settings.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#OAuthConfig)`)` Looker instance OAuth login settings.  
`linkedLspProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Linked Google Cloud Project Number for Looker Studio Pro.  
`fipsEnabled` |  `boolean` Optional. Whether FIPS is enabled on the Looker instance.  
`geminiEnabled` |  `boolean` Optional. Whether Gemini feature is enabled on the Looker instance or not.  
`controlledEgressConfig` |  `object (`[ControlledEgressConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ControlledEgressConfig)`)` Optional. Controlled egress configuration.  
`controlledEgressEnabled` |  `boolean` Optional. Whether controlled egress is enabled on the Looker instance.  
`periodicExportConfig` |  `object (`[PeriodicExportConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#PeriodicExportConfig)`)` Optional. Configuration for periodic export.  
`ingressIpAllowlistConfig` |  `object (`[IngressIpAllowlistConfig](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#IngressIpAllowlistConfig)`)` Optional. Ingress IP allowlist configuration for the Looker instance.  
`releaseChannel` |  `enum (`[ReleaseChannel](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ReleaseChannel)`)` Optional. The selected release channel for the instance.  
`softDeleteReason` |  `enum (`[SoftDeleteReason](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#SoftDeleteReason)`)` Output only. The reason for the instance being in a soft-deleted state.  
`suspendedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the Looker instance was suspended (soft deleted).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`catalogIntegrationOptOut` |  `boolean` Optional. Indicates whether catalog integration is disabled for the Looker instance.  
`acceleratedSecurityPatchEnabled` |  `boolean` Optional. Accelerated security patch enabled for the instance.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
## State

Possible states for a Looker instance.

Enums  
---  
`STATE_UNSPECIFIED` | State is unspecified.  
`ACTIVE` | Instance is active and ready for use.  
`CREATING` | Instance provisioning is in progress.  
`FAILED` | Instance is in a failed state.  
`SUSPENDED` | Instance was suspended.  
`UPDATING` | Instance update is in progress.  
`DELETING` | Instance delete is in progress.  
`EXPORTING` | Instance is being exported.  
`IMPORTING` | Instance is importing data.  
  
## PlatformEdition

Platform editions for a Looker instance. Each edition maps to a set of instance features.

Enums  
---  
`PLATFORM_EDITION_UNSPECIFIED` | Represents an unspecified platform edition.  
`LOOKER_CORE_TRIAL` | Represents the Looker Core Trial edition.  
`LOOKER_CORE_STANDARD` | Represents the Looker Core Standard edition.  
`LOOKER_CORE_STANDARD_ANNUAL` | Represents the Looker Core Standard Annual edition.  
`LOOKER_CORE_ENTERPRISE_ANNUAL` | Represents the Looker Core Enterprise Annual edition.  
`LOOKER_CORE_EMBED_ANNUAL` | Represents the Looker Core Embed Annual edition.  
`LOOKER_CORE_NONPROD_STANDARD_ANNUAL` | Represents the Looker Core Nonprod Standard Annual edition.  
`LOOKER_CORE_NONPROD_ENTERPRISE_ANNUAL` | Represents the Looker Core Nonprod Enterprise Annual edition.  
`LOOKER_CORE_NONPROD_EMBED_ANNUAL` | Represents the Looker Core Nonprod Embed Annual edition.  
`LOOKER_CORE_TRIAL_STANDARD` | Represents the Looker Core Trial Standard edition.  
`LOOKER_CORE_TRIAL_ENTERPRISE` | Represents the Looker Core Trial Enterprise edition.  
`LOOKER_CORE_TRIAL_EMBED` | Represents the Looker Core Trial Embed edition.  
  
## PscConfig

Information for Private Service Connect (PSC) setup for a Looker instance.

JSON representation  
---  
      
    
    {
      "allowedVpcs": [
        string
      ],
      "serviceAttachments": [
        {
          object ([ServiceAttachment](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ServiceAttachment))
        }
      ],
      "lookerServiceAttachmentUri": string
    }  
  
Fields  
---  
`allowedVpcs[]` |  `string` Optional. List of VPCs that are allowed ingress into looker. Format: projects/{project}/global/networks/{network}  
`serviceAttachments[]` |  `object (`[ServiceAttachment](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ServiceAttachment)`)` Optional. List of egress service attachment configurations.  
`lookerServiceAttachmentUri` |  `string` Output only. URI of the Looker service attachment.  
  
## ServiceAttachment

Service attachment configuration.

JSON representation  
---  
      
    
    {
      "localFqdn": string,
      "targetServiceAttachmentUri": string,
      "connectionStatus": enum ([ConnectionStatus](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ConnectionStatus)),
      "localFqdns": [
        string
      ],
      "failureReason": string
    }  
  
Fields  
---  
`localFqdn` |  `string` Optional. Fully qualified domain name that will be used in the private DNS record created for the service attachment.  
`targetServiceAttachmentUri` |  `string` Required. URI of the service attachment to connect to. Format: projects/{project}/regions/{region}/serviceAttachments/{service_attachment}  
`connectionStatus` |  `enum (`[ConnectionStatus](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#ConnectionStatus)`)` Output only. Connection status.  
`localFqdns[]` |  `string` Optional. List of fully qualified domain names that will be used in the private DNS record created for the service attachment.  
`failureReason` |  `string` Output only. Reason the service attachment creation failed. This value will only be populated if the service attachment encounters an issue during provisioning.  
  
## ConnectionStatus

Status of the service attachment connection. Referencing <https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses>

Enums  
---  
`UNKNOWN` | Connection status is unspecified.  
`ACCEPTED` | Connection is established and functioning normally.  
`PENDING` | Connection is not established (Looker tenant project hasn't been allowlisted).  
`REJECTED` | Connection is not established (Looker tenant project is explicitly in reject list).  
`NEEDS_ATTENTION` | Issue with target service attachment, e.g. NAT subnet is exhausted.  
`CLOSED` | Target service attachment does not exist. This status is a terminal state.  
  
## MaintenanceWindow

Specifies the recurring maintenance window.

JSON representation  
---  
      
    
    {
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay))
      }
    }  
  
Fields  
---  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#DayOfWeek)`)` Required. Day of the week for this MaintenanceWindow (in UTC).  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay)`)` Required. Time in UTC when the period starts. Maintenance will be scheduled within 60 minutes.  
  
## DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `[google.type.Date](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#Date)` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
## DenyMaintenancePeriod

Specifies the maintenance denial period.

JSON representation  
---  
      
    
    {
      "startDate": {
        object ([Date](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#Date))
      },
      "time": {
        object ([TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay))
      }
    }  
  
Fields  
---  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#Date)`)` Required. Start date of the deny maintenance period.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#Date)`)` Required. End date of the deny maintenance period.  
`time` |  `object (`[TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay)`)` Required. Time in UTC when the period starts and ends.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `[google.type.TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay)`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
## MaintenanceSchedule

Published upcoming future maintenance schedule.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The scheduled start time for the maintenance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The scheduled end time for the maintenance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## UserMetadata

Metadata about users for a Looker instance.

JSON representation  
---  
      
    
    {
      "additionalViewerUserCount": integer,
      "additionalStandardUserCount": integer,
      "additionalDeveloperUserCount": integer
    }  
  
Fields  
---  
`additionalViewerUserCount` |  `integer` Optional. The number of additional viewer users the instance owner has purchased.  
`additionalStandardUserCount` |  `integer` Optional. The number of additional standard users the instance owner has purchased.  
`additionalDeveloperUserCount` |  `integer` Optional. The number of additional developer users the instance owner has purchased.  
  
## CustomDomain

Custom domain information.

JSON representation  
---  
      
    
    {
      "domain": string,
      "state": enum ([CustomDomainState](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#CustomDomainState))
    }  
  
Fields  
---  
`domain` |  `string` Domain name.  
`state` |  `enum (`[CustomDomainState](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#CustomDomainState)`)` Domain state.  
  
## CustomDomainState

Enum for Custom Domain State.

Enums  
---  
`CUSTOM_DOMAIN_STATE_UNSPECIFIED` | Unspecified state.  
`UNVERIFIED` | DNS record is not created.  
`VERIFIED` | DNS record is created.  
`MODIFYING` | Calling SLM to update.  
`AVAILABLE` | ManagedCertificate is ready.  
`UNAVAILABLE` | ManagedCertificate is not ready.  
`UNKNOWN` | Status is not known.  
  
## AdminSettings

Looker instance Admin settings fields.

JSON representation  
---  
      
    
    {
      "allowedEmailDomains": [
        string
      ]
    }  
  
Fields  
---  
`allowedEmailDomains[]` |  `string` Email domain allowlist for the instance.  
  
## OAuthConfig

Looker instance OAuth login settings.

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string,
      "sharedOauthClientEnabled": boolean
    }  
  
Fields  
---  
`clientId` |  `string` Input only. Client ID from an external OAuth application. This is an input-only field, and thus will not be set in any responses.  
`clientSecret` |  `string` Input only. Client secret from an external OAuth application. This is an input-only field, and thus will not be set in any responses.  
`sharedOauthClientEnabled` |  `boolean` Optional. Whether to use the shared OAuth client. Instances specifying this field do not need to provide clientId and clientSecret.  
  
## ControlledEgressConfig

Controlled egress configuration.

JSON representation  
---  
      
    
    {
      "marketplaceEnabled": boolean,
      "egressFqdns": [
        string
      ],
      "webProxyIps": [
        string
      ]
    }  
  
Fields  
---  
`marketplaceEnabled` |  `boolean` Optional. Whether marketplace is enabled.  
`egressFqdns[]` |  `string` Optional. List of fully qualified domain names to be added to the allowlist for outbound traffic.  
`webProxyIps[]` |  `string` Output only. The list of IP addresses used by Secure Web Proxy for outbound traffic.  
  
## PeriodicExportConfig

Configuration for periodic export.

JSON representation  
---  
      
    
    {
      "kmsKey": string,
      "gcsUri": string,
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay))
      }
    }  
  
Fields  
---  
`kmsKey` |  `string` Required. Name of the CMEK key in KMS. Format: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}  
`gcsUri` |  `string` Required. Cloud Storage bucket URI for periodic export. Format: gs://{bucket_name}  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#TimeOfDay)`)` Required. Time in UTC to start the periodic export job.  
  
## IngressIpAllowlistConfig

Ingress IP allowlist configuration.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "allowlistRules": [
        {
          object ([IngressIpAllowlistRule](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#IngressIpAllowlistRule))
        }
      ],
      "googleServicesEnabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Whether ingress IP allowlist functionality is enabled on the Looker instance.  
`allowlistRules[]` |  `object (`[IngressIpAllowlistRule](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances#IngressIpAllowlistRule)`)` Optional. List of IP range rules to allow ingress traffic.  
`googleServicesEnabled` |  `boolean` Optional. Whether google service connections are enabled for the instance.  
  
## IngressIpAllowlistRule

Ingress IP allowlist rule.

JSON representation  
---  
      
    
    {
      "description": string,
      "ipRange": string
    }  
  
Fields  
---  
`description` |  `string` Optional. Description for the IP range.  
`ipRange` |  `string` Optional. The IP range to allow ingress traffic from.  
  
## ReleaseChannel

Release channel specified for the instance.

Enums  
---  
`RELEASE_CHANNEL_UNSPECIFIED` | Unspecified release channel.  
`RAPID` | Rapid: Most frequent updates.  
`REGULAR` | Regular: Balanced, default for production.  
`STABLE` | Stable: Least frequent, for maximum stability.  
  
## SoftDeleteReason

Reason for an instance's soft-deleted state. Used to distinguish between system and customer initiated soft-deletes.

Enums  
---  
`SOFT_DELETE_REASON_UNSPECIFIED` | Soft delete reason is unspecified. This is the default value.  
`BILLING_ACCOUNT_ISSUE` | Instance is soft deleted due to billing account issues.  
`TRIAL_EXPIRED` | Instance is soft deleted due to trial expiration.  
`CUSTOMER_REQUEST` | Instance is soft deleted by the customer.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/create)`

|  Creates a new Instance in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/delete)`

|  Delete instance.  
  
### `[export](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/export)`

|  Export instance.  
  
### `[get](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/get)`

|  Gets details of a single Instance.  
  
### `[import](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/import)`

|  Import instance.  
  
### `[list](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/list)`

|  Lists Instances in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/patch)`

|  Update Instance.  
  
### `[restart](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/restart)`

|  Restart instance.  
  
### `[restore](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/restore)`

|  Restore Looker instance.  
  
### `[undelete](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances/undelete)`

|  Undeletes Looker instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
