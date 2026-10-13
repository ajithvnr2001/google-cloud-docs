---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads
title: REST Resource: organizations.locations.workloads \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:27.794680+00:00
---

# REST Resource: organizations.locations.workloads  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.workloads Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Workload
    * JSON representation
  * ResourceInfo
    * JSON representation
  * ResourceType
  * KMSSettings
    * JSON representation
  * ResourceSettings
    * JSON representation
  * KajEnrollmentState
  * SaaEnrollmentResponse
    * JSON representation
  * SetupState
  * SetupError
  * ComplianceStatus
    * JSON representation
  * Partner
  * PartnerPermissions
    * JSON representation
  * EkmProvisioningResponse
    * JSON representation
  * EkmProvisioningState
  * EkmProvisioningErrorDomain
  * EkmProvisioningErrorMapping
  * WorkloadOptions
    * JSON representation
  * KajEnrollmentType
  * Methods



## Resource: Workload

A Workload object for managing highly regulated workloads of cloud customers.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "resources": [
        {
          object ([ResourceInfo](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceInfo))
        }
      ],
      "complianceRegime": enum (ComplianceRegime),
      "createTime": string,
      "billingAccount": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "provisionedResourcesParent": string,
      "kmsSettings": {
        object ([KMSSettings](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#KMSSettings))
      },
      "resourceSettings": [
        {
          object ([ResourceSettings](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceSettings))
        }
      ],
      "kajEnrollmentState": enum ([KajEnrollmentState](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#KajEnrollmentState)),
      "enableSovereignControls": boolean,
      "saaEnrollmentResponse": {
        object ([SaaEnrollmentResponse](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#SaaEnrollmentResponse))
      },
      "complianceStatus": {
        object ([ComplianceStatus](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ComplianceStatus))
      },
      "compliantButDisallowedServices": [
        string
      ],
      "partner": enum ([Partner](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#Partner)),
      "partnerPermissions": {
        object ([PartnerPermissions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#PartnerPermissions))
      },
      "partnerServicesBillingAccount": string,
      "ekmProvisioningResponse": {
        object ([EkmProvisioningResponse](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningResponse))
      },
      "resourceMonitoringEnabled": boolean,
      "workloadOptions": {
        object ([WorkloadOptions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#WorkloadOptions))
      },
      "violationNotificationsEnabled": boolean
    }  
  
Fields  
---  
`name` |  `string` Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload}Read-only.  
`displayName` |  `string` Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces.Example: My Workload  
`resources[]` |  `object (`[ResourceInfo](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceInfo)`)` Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.  
`complianceRegime` |  `enum (`ComplianceRegime`)` Required. Immutable. Compliance Regime associated with this workload.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Immutable. The Workload creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`billingAccount` |  `string` Optional. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.  
`etag` |  `string` Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.  
`labels` |  `map (key: string, value: string)` Optional. Labels applied to the workload.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`provisionedResourcesParent` |  `string` Input only. The parent resource for the resources managed by this Assured Workload. May be either empty or a folder resource which is a child of the Workload parent. If not specified all resources are created under the parent organization. Format: folders/{folderId}  
`kmsSettings  
**(deprecated)**` |  `object (`[KMSSettings](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#KMSSettings)`)` This item is deprecated!Input only. Settings used to create a CMEK crypto key. When set, a project with a KMS CMEK key is provisioned. This field is deprecated as of Feb 28, 2022. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.  
`resourceSettings[]` |  `object (`[ResourceSettings](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceSettings)`)` Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.  
`kajEnrollmentState` |  `enum (`[KajEnrollmentState](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#KajEnrollmentState)`)` Output only. Represents the KAJ enrollment state of the given workload.  
`enableSovereignControls` |  `boolean` Optional. Indicates the sovereignty status of the given workload. Currently meant to be used by Europe/Canada customers.  
`saaEnrollmentResponse` |  `object (`[SaaEnrollmentResponse](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#SaaEnrollmentResponse)`)` Output only. Represents the SAA enrollment response of the given workload. SAA enrollment response is queried during workloads.get call. In failure cases, user friendly error message is shown in SAA details page.  
`complianceStatus` |  `object (`[ComplianceStatus](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ComplianceStatus)`)` Output only. Count of active Violations in the Workload.  
`compliantButDisallowedServices[]` |  `string` Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke workloads.restrictAllowedResources endpoint to allow your project developers to use these services in their environment.  
`partner` |  `enum (`[Partner](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#Partner)`)` Optional. Partner regime associated with this workload.  
`partnerPermissions` |  `object (`[PartnerPermissions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#PartnerPermissions)`)` Optional. Permissions granted to the AW Partner SA account for the customer workload  
`partnerServicesBillingAccount` |  `string` Optional. Billing account necessary for purchasing services from Sovereign Partners. This field is required for creating SIA/PSN/CNTXT partner workloads. The caller should have 'billing.resourceAssociations.create' IAM permission on this billing-account. The format of this string is billingAccounts/AAAAAA-BBBBBB-CCCCCC  
`ekmProvisioningResponse` |  `object (`[EkmProvisioningResponse](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningResponse)`)` Output only. Represents the Ekm Provisioning State of the given workload.  
`resourceMonitoringEnabled` |  `boolean` Output only. Indicates whether resource monitoring is enabled for workload or not. It is true when Resource feed is subscribed to AWM topic and AWM Service Agent Role is binded to AW Service Account for resource Assured workload.  
`workloadOptions` |  `object (`[WorkloadOptions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#WorkloadOptions)`)` Optional. Options to be set for the given created workload.  
`violationNotificationsEnabled` |  `boolean` Optional. Indicates whether the e-mail notification for a violation is enabled for a workload. This value will be by default True, and if not present will be considered as true. This should only be updated via updateWorkload call. Any Changes to this field during the createWorkload call will not be honored. This will always be true while creating the workload.  
  
## ResourceInfo

Represent the resources that are children of this Workload.

JSON representation  
---  
      
    
    {
      "resourceId": string,
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceType))
    }  
  
Fields  
---  
`resourceId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Resource identifier. For a project this represents project_number.  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceType)`)` Indicates the type of resource.  
  
## ResourceType

The type of resource.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Unknown resource type.  
`CONSUMER_PROJECT` | Deprecated. Existing workloads will continue to support this, but new CreateWorkloadRequests should not specify this as an input value.This item is deprecated!  
`CONSUMER_FOLDER` | Consumer Folder.  
`ENCRYPTION_KEYS_PROJECT` | Consumer project containing encryption keys.  
`KEYRING` | Keyring resource that hosts encryption keys.  
  
## KMSSettings

This item is deprecated!

Settings specific to the Key Management Service.

JSON representation  
---  
      
    
    {
      "nextRotationTime": string,
      "rotationPeriod": string
    }  
  
Fields  
---  
`nextRotationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rotationPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. Input only. Immutable. [nextRotationTime] will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ResourceSettings

Represent the custom settings for the resources to be created.

JSON representation  
---  
      
    
    {
      "resourceId": string,
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceType)),
      "displayName": string
    }  
  
Fields  
---  
`resourceId` |  `string` Resource identifier. For a project this represents projectId. If the project is already taken, the workload creation will fail. For KeyRing, this represents the keyring_id. For a folder, don't set this value as folderId is assigned by Google.  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#ResourceType)`)` Indicates the type of resource. This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT)  
`displayName` |  `string` User-assigned resource display name. If not empty it will be used to create a resource with the specified name.  
  
## KajEnrollmentState

Key Access Justifications(KAJ) Enrollment State.

Enums  
---  
`KAJ_ENROLLMENT_STATE_UNSPECIFIED` | Default State for KAJ Enrollment.  
`KAJ_ENROLLMENT_STATE_PENDING` | Pending State for KAJ Enrollment.  
`KAJ_ENROLLMENT_STATE_COMPLETE` | Complete State for KAJ Enrollment.  
  
## SaaEnrollmentResponse

Signed Access Approvals (SAA) enrollment response.

JSON representation  
---  
      
    
    {
      "setupErrors": [
        enum ([SetupError](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#SetupError))
      ],
      "setupStatus": enum ([SetupState](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#SetupState))
    }  
  
Fields  
---  
`setupErrors[]` |  `enum (`[SetupError](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#SetupError)`)` Indicates SAA enrollment setup error if any.  
`setupStatus` |  `enum (`[SetupState](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#SetupState)`)` Output only. Indicates SAA enrollment status of a given workload.  
  
## SetupState

Setup state of SAA enrollment.

Enums  
---  
`SETUP_STATE_UNSPECIFIED` | Unspecified.  
`STATUS_PENDING` | SAA enrollment pending.  
`STATUS_COMPLETE` | SAA enrollment comopleted.  
  
## SetupError

Setup error of SAA enrollment.

Enums  
---  
`SETUP_ERROR_UNSPECIFIED` | Unspecified.  
`ERROR_INVALID_BASE_SETUP` | Invalid states for all customers, to be redirected to AA UI for additional details.  
`ERROR_MISSING_EXTERNAL_SIGNING_KEY` | Returned when there is not an EKM key configured.  
`ERROR_NOT_ALL_SERVICES_ENROLLED` | Returned when there are no enrolled services or the customer is enrolled in CAA only for a subset of services.  
`ERROR_SETUP_CHECK_FAILED` | Returned when exception was encountered during evaluation of other criteria.  
  
## ComplianceStatus

Represents the Compliance Status of this workload

JSON representation  
---  
      
    
    {
      "activeViolationCount": integer,
      "acknowledgedViolationCount": integer,
      "activeResourceViolationCount": integer,
      "acknowledgedResourceViolationCount": integer
    }  
  
Fields  
---  
`activeViolationCount` |  `integer` Number of current orgPolicy violations which are not acknowledged.  
`acknowledgedViolationCount` |  `integer` Number of current orgPolicy violations which are acknowledged.  
`activeResourceViolationCount` |  `integer` Number of current resource violations which are acknowledged.  
`acknowledgedResourceViolationCount` |  `integer` Number of current resource violations which are not acknowledged.  
  
## Partner

Supported Assured Workloads Partners.

Enums  
---  
`PARTNER_UNSPECIFIED` |   
`LOCAL_CONTROLS_BY_S3NS` | Enum representing S3NS (Thales) partner.  
`SOVEREIGN_CONTROLS_BY_T_SYSTEMS` | Enum representing T_SYSTEM (TSI) partner.  
`SOVEREIGN_CONTROLS_BY_SIA_MINSAIT` | Enum representing SIA_MINSAIT (Indra) partner.  
`SOVEREIGN_CONTROLS_BY_PSN` | Enum representing PSN (TIM) partner.  
`SOVEREIGN_CONTROLS_BY_CNTXT` | Enum representing CNTXT (Kingdom of Saudi Arabia) partner.  
`SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM` | Enum representing CNTXT (Kingdom of Saudi Arabia) partner offering without EKM.  
  
## PartnerPermissions

Permissions granted to the AW Partner SA account for the customer workload

JSON representation  
---  
      
    
    {
      "dataLogsViewer": boolean,
      "serviceAccessApprover": boolean,
      "assuredWorkloadsMonitoring": boolean,
      "accessTransparencyLogsSupportCaseViewer": boolean
    }  
  
Fields  
---  
`dataLogsViewer` |  `boolean` Optional. Allow the partner to view inspectability logs and monitoring violations.  
`serviceAccessApprover` |  `boolean` Optional. Allow partner to view access approval logs.  
`assuredWorkloadsMonitoring` |  `boolean` Optional. Allow partner to view violation alerts.  
`accessTransparencyLogsSupportCaseViewer` |  `boolean` Optional. Allow partner to view support case details for an AXT log  
  
## EkmProvisioningResponse

External key management systems(EKM) Provisioning response

JSON representation  
---  
      
    
    {
      "ekmProvisioningState": enum ([EkmProvisioningState](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningState)),
      "ekmProvisioningErrorDomain": enum ([EkmProvisioningErrorDomain](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningErrorDomain)),
      "ekmProvisioningErrorMapping": enum ([EkmProvisioningErrorMapping](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningErrorMapping))
    }  
  
Fields  
---  
`ekmProvisioningState` |  `enum (`[EkmProvisioningState](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningState)`)` Output only. Indicates Ekm enrollment Provisioning of a given workload.  
`ekmProvisioningErrorDomain` |  `enum (`[EkmProvisioningErrorDomain](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningErrorDomain)`)` Indicates Ekm provisioning error if any.  
`ekmProvisioningErrorMapping` |  `enum (`[EkmProvisioningErrorMapping](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#EkmProvisioningErrorMapping)`)` Detailed error message if Ekm provisioning fails  
  
## EkmProvisioningState

External key management systems(EKM) Provisioning State

Enums  
---  
`EKM_PROVISIONING_STATE_UNSPECIFIED` | Default State for Ekm Provisioning  
`EKM_PROVISIONING_STATE_PENDING` | Pending State for Ekm Provisioning  
`EKM_PROVISIONING_STATE_FAILED` | Failed State for Ekm Provisioning  
`EKM_PROVISIONING_STATE_COMPLETED` | Completed State for Ekm Provisioning  
  
## EkmProvisioningErrorDomain

Provisioning error of EKM resources

Enums  
---  
`EKM_PROVISIONING_ERROR_DOMAIN_UNSPECIFIED` | No error domain  
`UNSPECIFIED_ERROR` | Error but domain is unspecified.  
`GOOGLE_SERVER_ERROR` | Internal logic breaks within provisioning code.  
`EXTERNAL_USER_ERROR` | Error occurred with the customer not granting permission/creating resource.  
`EXTERNAL_PARTNER_ERROR` | Error occurred within the partner's provisioning cluster.  
`TIMEOUT_ERROR` | Resource wasn't provisioned in the required 7 day time period  
  
## EkmProvisioningErrorMapping

Error Mapping if Ekm provisioning fails

Enums  
---  
`EKM_PROVISIONING_ERROR_MAPPING_UNSPECIFIED` | Error is unspecified.  
`INVALID_SERVICE_ACCOUNT` | Service account is used is invalid.  
`MISSING_METRICS_SCOPE_ADMIN_PERMISSION` | Iam permission monitoring.MetricsScopeAdmin wasn't applied.  
`MISSING_EKM_CONNECTION_ADMIN_PERMISSION` | Iam permission cloudkms.ekmConnectionsAdmin wasn't applied.  
  
## WorkloadOptions

Options to be set for the given created workload.

JSON representation  
---  
      
    
    {
      "kajEnrollmentType": enum ([KajEnrollmentType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#KajEnrollmentType))
    }  
  
Fields  
---  
`kajEnrollmentType` |  `enum (`[KajEnrollmentType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads#KajEnrollmentType)`)` Optional. Specifies type of KAJ Enrollment if provided.  
  
## KajEnrollmentType

Types of KAJ Enrollment

Enums  
---  
`KAJ_ENROLLMENT_TYPE_UNSPECIFIED` | KAJ Enrollment type is unspecified  
`KEY_ACCESS_TRANSPARENCY_OFF` | KAT sets External, Hardware, and Software key feature logging only to TRUE.  
  
## Methods  
  
---  
  
### `[analyzeWorkloadMove](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/analyzeWorkloadMove)`

|  Analyzes a hypothetical move of a source resource to a target workload to surface compliance risks.  
  
### `[create](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/create)`

|  Creates Assured Workload.  
  
### `[delete](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/delete)`

|  Deletes the workload.  
  
### `[enableComplianceUpdates](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/enableComplianceUpdates)`

|  This endpoint enables Assured Workloads service to offer compliance updates for the folder based assured workload.  
  
### `[enableResourceMonitoring](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/enableResourceMonitoring)`

|  Enable resource violation monitoring for a workload.  
  
### `[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/get)`

|  Gets Assured Workload associated with a CRM Node  
  
### `[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/list)`

|  Lists Assured Workloads under a CRM Node.  
  
### `[mutatePartnerPermissions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/mutatePartnerPermissions)`

|  Update the permissions settings for an existing partner workload.  
  
### `[patch](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/patch)`

|  Updates an existing workload.  
  
### `[restrictAllowedResources](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/restrictAllowedResources)`

|  Restrict the list of resources allowed in the Workload environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
