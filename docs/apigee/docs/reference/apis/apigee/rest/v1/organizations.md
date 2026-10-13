---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/
title: REST Resource: organizations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:10.335168+00:00
---

# REST Resource: organizations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Organization
    * JSON representation
  * Type
  * RuntimeType
  * SubscriptionType
  * BillingType
  * AddonsConfig
    * JSON representation
  * AdvancedApiOpsConfig
    * JSON representation
  * IntegrationConfig
    * JSON representation
  * MonetizationConfig
    * JSON representation
  * ApiSecurityConfig
    * JSON representation
  * ConnectorsPlatformConfig
    * JSON representation
  * AnalyticsConfig
    * JSON representation
  * AddonState
  * SubscriptionPlan
  * Methods



## Resource: Organization

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "customerName": string,
      "attributes": [
        string
      ],
      "createdAt": string,
      "lastModifiedAt": string,
      "expiresAt": string,
      "environments": [
        string
      ],
      "properties": {
        object ([Properties](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Properties))
      },
      "type": enum ([Type](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#Type)),
      "analyticsRegion": string,
      "authorizedNetwork": string,
      "disableVpcPeering": boolean,
      "runtimeType": enum ([RuntimeType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#RuntimeType)),
      "subscriptionType": enum ([SubscriptionType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#SubscriptionType)),
      "billingType": enum ([BillingType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#BillingType)),
      "addonsConfig": {
        object ([AddonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AddonsConfig))
      },
      "caCertificate": string,
      "caCertificates": [
        string
      ],
      "runtimeDatabaseEncryptionKeyName": string,
      "projectId": string,
      "state": enum (State),
      "portalDisabled": boolean,
      "apiConsumerDataEncryptionKeyName": string,
      "controlPlaneEncryptionKeyName": string,
      "apiConsumerDataLocation": string,
      "apigeeProjectId": string,
      "subscriptionPlan": enum ([SubscriptionPlan](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#SubscriptionPlan)),
      "networkEgressRestricted": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the Apigee organization.  
`displayName` |  `string` Optional. Display name for the Apigee organization. Unused, but reserved for future use.  
`description` |  `string` Optional. Description of the Apigee organization.  
`customerName` |  `string` Not used by Apigee.  
`attributes[]` |  `string` Not used by Apigee.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time that the Apigee organization was created in milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time that the Apigee organization was last modified in milliseconds since epoch.  
`expiresAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time that the Apigee organization is scheduled for deletion.  
`environments[]` |  `string` Output only. List of environments in the Apigee organization.  
`properties` |  `object (`[Properties](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Properties)`)` Optional. Properties defined in the Apigee organization profile.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#Type)`)` Not used by Apigee.  
`analyticsRegion  
**(deprecated)**` |  `string` This item is deprecated!Required. DEPRECATED: This field will eventually be deprecated and replaced with a differently-named field. Primary Google Cloud region for analytics data storage. For valid values, see [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org).  
`authorizedNetwork` |  `string` Optional. Compute Engine network used for Service Networking to be peered with Apigee runtime instances. See [Getting started with the Service Networking API](https://cloud.google.com/service-infrastructure/docs/service-networking/getting-started). Valid only when RuntimeType is set to `CLOUD`. The value must be set before the creation of a runtime instance and can be updated only when there are no runtime instances. For example: `default`.When changing authorizedNetwork, you must reconfigure VPC peering. After VPC peering with previous network is deleted, [run the following command](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/delete): `gcloud services vpc-peerings delete --network=NETWORK`, where `NETWORK` is the name of the previous network. This will delete the previous Service Networking. Otherwise, you will get the following error: `The resource 'projects/...-tp' is already linked to another shared VPC host 'projects/...-tp`.Apigee also supports shared VPC (that is, the host network project is not the same as the one that is peering with Apigee). See [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc). To use a shared VPC network, use the following format: `projects/{host-project-id}/{region}/networks/{network-name}`. For example: `projects/my-sharedvpc-host/global/networks/mynetwork`**Note:** Not supported for Apigee hybrid.  
`disableVpcPeering` |  `boolean` Optional. Flag that specifies whether the VPC Peering through Private Google Access should be disabled between the consumer network and Apigee.Valid only when RuntimeType is set to CLOUD.Required if an authorizedNetwork on the consumer project is not provided, in which case the flag should be set to true. The value must be set before the creation of any Apigee runtime instance and can be updated only when there are no runtime instances.**Note:** Apigee will be deprecating the vpc peering model that requires you to provide 'authorizedNetwork', by making the non-peering model as the default way of provisioning Apigee organization in future. So, this will be a temporary flag to enable the transition. Not supported for Apigee hybrid.  
`runtimeType` |  `enum (`[RuntimeType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#RuntimeType)`)` Required. Runtime type of the Apigee organization based on the Apigee subscription purchased.  
`subscriptionType  
**(deprecated)**` |  `enum (`[SubscriptionType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#SubscriptionType)`)` This item is deprecated!Output only. DEPRECATED: This will eventually be replaced by BillingType. Subscription type of the Apigee organization. Valid values include trial (free, limited, and for evaluation purposes only) or paid (full subscription has been purchased). See [Apigee pricing](https://cloud.google.com/apigee/pricing/).  
`billingType` |  `enum (`[BillingType](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#BillingType)`)` Optional. Billing type of the Apigee organization. See [Apigee pricing](https://cloud.google.com/apigee/pricing).  
`addonsConfig` |  `object (`[AddonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AddonsConfig)`)` Optional. Addon configurations of the Apigee organization.  
`caCertificate  
**(deprecated)**` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Output only. Deprecated: Use `caCertificates` instead. Base64-encoded public certificate for the root CA of the Apigee organization. Valid only when RuntimeType is `CLOUD`.A base64-encoded string.  
`caCertificates[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Base64-encoded public certificates for the root CA of the Apigee organization. Valid only when RuntimeType is `CLOUD`. Multiple certificates are used to support certificate rotation.A base64-encoded string.  
`runtimeDatabaseEncryptionKeyName` |  `string` Optional. Cloud KMS key name used for encrypting the data that is stored and replicated across runtime instances. Update is not allowed after the organization is created.If not specified or RuntimeType is `TRIAL`, a Google-Managed encryption key will be used.For example: "projects/foo/locations/us/keyRings/bar/cryptoKeys/baz".**Note:** Not supported for Apigee hybrid.  
`projectId` |  `string` Output only. Project ID associated with the Apigee organization.  
`state` |  `enum (`State`)` Output only. State of the organization. Values other than ACTIVE means the resource is not ready to use.  
`portalDisabled` |  `boolean` Optional. Configuration for the Portals settings.  
`apiConsumerDataEncryptionKeyName` |  `string` Optional. Cloud KMS key name used for encrypting API consumer data.If not specified or BillingType is `EVALUATION`, a Google-Managed encryption key will be used.Format: `projects/*/locations/*/keyRings/*/cryptoKeys/*`  
`controlPlaneEncryptionKeyName` |  `string` Optional. Cloud KMS key name used for encrypting control plane data that is stored in a multi region. Only used for the data residency region "US" or "EU".If not specified or BillingType is `EVALUATION`, a Google-Managed encryption key will be used.Format: `projects/*/locations/*/keyRings/*/cryptoKeys/*`  
`apiConsumerDataLocation` |  `string` Optional. This field is needed only for customers using non-default data residency regions. Apigee stores some control plane data only in single region. This field determines which single region Apigee should use.For example: "us-west1" when control plane is in US or "europe-west2" when control plane is in EU.  
`apigeeProjectId` |  `string` Output only. Apigee Project ID associated with the organization. Use this project to allowlist Apigee in the Service Attachment when using private service connect with Apigee.  
`subscriptionPlan` |  `enum (`[SubscriptionPlan](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#SubscriptionPlan)`)` Output only. Subscription plan that the customer has purchased. Output only.  
`networkEgressRestricted` |  `boolean` Optional. Flag that specifies if internet egress is restricted for VPC Service Controls. Valid only when runtimeType is `CLOUD` and disableVpcPeering is `true`.  
  
## Type

Enums  
---  
`TYPE_UNSPECIFIED` | Subscription type not specified.  
`TYPE_TRIAL` | Subscription to Apigee is free, limited, and used for evaluation purposes only.  
`TYPE_PAID` | Full subscription to Apigee has been purchased. See [Apigee pricing](https://cloud.google.com/apigee/pricing/).  
`TYPE_INTERNAL` | For internal users only.  
  
## RuntimeType

Enums  
---  
`RUNTIME_TYPE_UNSPECIFIED` | Runtime type not specified.  
`CLOUD` | Google-managed Apigee runtime.  
`HYBRID` | User-managed Apigee hybrid runtime.  
  
## SubscriptionType

Enums  
---  
`SUBSCRIPTION_TYPE_UNSPECIFIED` | Subscription type not specified.  
`PAID` | Full subscription to Apigee has been purchased.  
`TRIAL` | Subscription to Apigee is free, limited, and used for evaluation purposes only.  
  
## BillingType

Billing type of the Apigee organization.

Enums  
---  
`BILLING_TYPE_UNSPECIFIED` | Billing type not specified.  
`SUBSCRIPTION` | A pre-paid subscription to Apigee.  
`EVALUATION` | Free and limited access to Apigee for evaluation purposes only.  
`PAYG` | Access to Apigee using a Pay-As-You-Go plan.  
  
## AddonsConfig

Add-on configurations for the Apigee organization.

JSON representation  
---  
      
    
    {
      "advancedApiOpsConfig": {
        object ([AdvancedApiOpsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AdvancedApiOpsConfig))
      },
      "integrationConfig": {
        object ([IntegrationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#IntegrationConfig))
      },
      "monetizationConfig": {
        object ([MonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#MonetizationConfig))
      },
      "apiSecurityConfig": {
        object ([ApiSecurityConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#ApiSecurityConfig))
      },
      "connectorsPlatformConfig": {
        object ([ConnectorsPlatformConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#ConnectorsPlatformConfig))
      },
      "analyticsConfig": {
        object ([AnalyticsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AnalyticsConfig))
      }
    }  
  
Fields  
---  
`advancedApiOpsConfig` |  `object (`[AdvancedApiOpsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AdvancedApiOpsConfig)`)` Configuration for the Advanced API Ops add-on.  
`integrationConfig` |  `object (`[IntegrationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#IntegrationConfig)`)` Configuration for the Integration add-on.  
`monetizationConfig` |  `object (`[MonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#MonetizationConfig)`)` Configuration for the Monetization add-on.  
`apiSecurityConfig` |  `object (`[ApiSecurityConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#ApiSecurityConfig)`)` Configuration for the API Security add-on.  
`connectorsPlatformConfig` |  `object (`[ConnectorsPlatformConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#ConnectorsPlatformConfig)`)` Configuration for the Connectors Platform add-on.  
`analyticsConfig` |  `object (`[AnalyticsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AnalyticsConfig)`)` Configuration for the Analytics add-on. Only used in organizations.environments.addonsConfig.  
  
## AdvancedApiOpsConfig

Configuration for the Advanced API Ops add-on.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Flag that specifies whether the Advanced API Ops add-on is enabled.  
  
## IntegrationConfig

Configuration for the Integration add-on.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Flag that specifies whether the Integration add-on is enabled.  
  
## MonetizationConfig

Configuration for the Monetization add-on.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Flag that specifies whether the Monetization add-on is enabled.  
  
## ApiSecurityConfig

Configurations of the API Security add-on.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "expiresAt": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Flag that specifies whether the API security add-on is enabled.  
`expiresAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time at which the API Security add-on expires in milliseconds since epoch. If unspecified, the add-on will never expire.  
  
## ConnectorsPlatformConfig

Configuration for the Connectors Platform add-on.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "expiresAt": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Flag that specifies whether the Connectors Platform add-on is enabled.  
`expiresAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time at which the Connectors Platform add-on expires in milliseconds since epoch. If unspecified, the add-on will never expire.  
  
## AnalyticsConfig

Configuration for the Analytics add-on.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "expireTimeMillis": string,
      "state": enum ([AddonState](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AddonState)),
      "updateTime": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether the Analytics add-on is enabled.  
`expireTimeMillis` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time at which the Analytics add-on expires in milliseconds since epoch. If unspecified, the add-on will never expire.  
`state` |  `enum (`[AddonState](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AddonState)`)` Output only. The state of the Analytics add-on.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The latest update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AddonState

The actual state of an addon.

Enums  
---  
`ADDON_STATE_UNSPECIFIED` | Default value.  
`ENABLING` | Add-on is in progress of enabling.  
`ENABLED` | Add-on is fully enabled and ready to use.  
`DISABLING` | Add-on is in progress of disabling.  
`DISABLED` | Add-on is fully disabled.  
  
## SubscriptionPlan

Subscription plan that the customer has purchased.

Enums  
---  
`SUBSCRIPTION_PLAN_UNSPECIFIED` | Subscription plan not specified.  
`SUBSCRIPTION_2021` | Traditional subscription plan.  
`SUBSCRIPTION_2024` | New subscription plan that provides standard proxy and scaled proxy implementation.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create)`

|  Creates an Apigee organization.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete)`

|  Delete an Apigee organization.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get)`

|  Gets the profile for an Apigee organization.  
  
### `[getControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getControlPlaneAccess)`

|  Lists the service accounts allowed to access Apigee control plane directly for limited functionality.  
  
### `[getProjectMapping](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getProjectMapping)`

|  Gets the project ID and region for an Apigee organization.  
  
### `[getSecuritySettings](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getSecuritySettings)`

|  GetSecuritySettings gets the security settings for API Security.  
  
### `[getSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getSyncAuthorization)`

|  Lists the service accounts with the permissions required to allow the Synchronizer to download environment data from the control plane.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/list)`

|  Lists the Apigee organizations and associated Google Cloud projects that you have permission to access.  
  
### `[setAddons](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons)`

|  Configures the add-ons for the Apigee organization.  
  
### `[setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization)`

|  Sets the permissions required to allow the Synchronizer to download environment data from the control plane.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/update)`

|  Updates the properties for an Apigee organization.  
  
### `[updateControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess)`

|  Updates the permissions required to allow Apigee runtime-plane components access to the control plane.  
  
### `[updateSecuritySettings](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateSecuritySettings)`

|  UpdateSecuritySettings updates the current security settings for API Security.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
