---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySystem/legacyGetLicenseStatus/
title: Method: legacySystem.legacyGetLicenseStatus \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:19.399028+00:00
---

# Method: legacySystem.legacyGetLicenseStatus  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySystem/legacyGetLicenseStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySystem.legacyGetLicenseStatus Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * LicenceModuleStatus
    * JSON representation
  * LicenseType



**Full name** : projects.locations.instances.legacySystem.legacyGetLicenseStatus

Returns the current status of the SecOps license. This includes detailed information about environment limits, enabled modules, and expiration dates.

### HTTP request

`GET https://{endpoint}/v1alpha/{instance}/legacySystem:legacyGetLicenseStatus`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to get the license status for. Format: projects/{project}/locations/{location}/instances/{instance}/legacySystem:legacyGetLicenseStatus  
  
### Request body

The request body must be empty.

### Response body

Response message for legacySystem.legacyGetLicenseStatus.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "licenceRemainingDays": integer,
      "usersAmountLimit": integer,
      "collaboratorUsersAmountLimit": integer,
      "viewOnlyUsersAmountLimit": integer,
      "managedUserUsersAmountLimit": integer,
      "managedUserPlusUsersAmountLimit": integer,
      "environmentsAmountLimit": integer,
      "environmentsThatIncludesAgentsLimit": integer,
      "usersInUsage": integer,
      "collaboratorUsersInUsage": integer,
      "viewOnlyUsersInUsage": integer,
      "managedUserUsersInUsage": integer,
      "managedUserPlusUsersInUsage": integer,
      "environmentsThatIncludesAgentsUsage": integer,
      "environmentsInUsage": integer,
      "remainingUsers": integer,
      "alertsPerDayLimit": integer,
      "alertsPerDayInUsage": integer,
      "remainingViewOnlyUsers": integer,
      "remainingCollaboratorUsers": integer,
      "remainingManagedUserUsers": integer,
      "remainingManagedUserPlusUsers": integer,
      "playbooksInUsage": integer,
      "playbooksAmountLimit": integer,
      "connectorsInUsage": integer,
      "connectorsAmountLimit": integer,
      "webhooksInUsage": integer,
      "webhooksAmountLimit": integer,
      "remainingEnvironments": integer,
      "remainingEnvironmentsThatIncludesAgents": integer,
      "serverVersion": string,
      "systemModules": [
        {
          object ([LicenceModuleStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySystem/legacyGetLicenseStatus#LicenceModuleStatus))
        }
      ],
      "isEvaluation": boolean,
      "maxDataRetentionDuration": integer,
      "licenseType": enum ([LicenseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySystem/legacyGetLicenseStatus#LicenseType)),
      "customerId": string,
      "expirationDateUnixTimeInMs": string,
      "warRoomEnvironmentLimit": integer,
      "warRoomEnvironmentUsage": integer,
      "advancedReportsUserLimit": string,
      "advancedReportsUserUsage": integer,
      "versionMetadata": string
    }  
  
Fields  
---  
`licenceRemainingDays` |  `integer` The remaining license days.  
`usersAmountLimit` |  `integer` The number of users allowed.  
`collaboratorUsersAmountLimit` |  `integer` The number of collaborator users allowed.  
`viewOnlyUsersAmountLimit` |  `integer` The number of view only users allowed.  
`managedUserUsersAmountLimit` |  `integer` The number of managed user users allowed.  
`managedUserPlusUsersAmountLimit` |  `integer` The number of managed user plus users allowed.  
`environmentsAmountLimit` |  `integer` The number of environments allowed.  
`environmentsThatIncludesAgentsLimit` |  `integer` The number of environments that includes agents allowed.  
`usersInUsage` |  `integer` The number of users in usage.  
`collaboratorUsersInUsage` |  `integer` The number of collaborator users in usage.  
`viewOnlyUsersInUsage` |  `integer` The number of view only users in usage.  
`managedUserUsersInUsage` |  `integer` The number of managed user users in usage.  
`managedUserPlusUsersInUsage` |  `integer` The number of managed user plus users in usage.  
`environmentsThatIncludesAgentsUsage` |  `integer` The number of environments that includes agents in usage.  
`environmentsInUsage` |  `integer` The number of environments in usage.  
`remainingUsers` |  `integer` The number of remaining users.  
`alertsPerDayLimit` |  `integer` The number of alerts per day limit.  
`alertsPerDayInUsage` |  `integer` The number of alerts per day in usage.  
`remainingViewOnlyUsers` |  `integer` The number of remaining view only users.  
`remainingCollaboratorUsers` |  `integer` The number of remaining collaborator users.  
`remainingManagedUserUsers` |  `integer` The number of remaining managed user users.  
`remainingManagedUserPlusUsers` |  `integer` The number of remaining managed user plus users.  
`playbooksInUsage` |  `integer` The number of playbooks in usage.  
`playbooksAmountLimit` |  `integer` The number of playbooks allowed.  
`connectorsInUsage` |  `integer` The number of connectors in usage.  
`connectorsAmountLimit` |  `integer` The number of connectors allowed.  
`webhooksInUsage` |  `integer` The number of webhooks in usage.  
`webhooksAmountLimit` |  `integer` The number of webhooks allowed.  
`remainingEnvironments` |  `integer` The number of remaining environments.  
`remainingEnvironmentsThatIncludesAgents` |  `integer` The number of remaining environments that includes agents.  
`serverVersion` |  `string` The server version.  
`systemModules[]` |  `object (`[LicenceModuleStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySystem/legacyGetLicenseStatus#LicenceModuleStatus)`)` The list of system modules.  
`isEvaluation` |  `boolean` Whether the instance is an evaluation instance.  
`maxDataRetentionDuration` |  `integer` The maximum data retention value time in months.  
`licenseType` |  `enum (`[LicenseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySystem/legacyGetLicenseStatus#LicenseType)`)` The license type.  
`customerId` |  `string` The customer id.  
`expirationDateUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The expiration date in unix time in milliseconds.  
`warRoomEnvironmentLimit` |  `integer` The number of war room environments allowed.  
`warRoomEnvironmentUsage` |  `integer` The number of war room environments in usage.  
`advancedReportsUserLimit` |  `string` The number of advanced reports users allowed.  
`advancedReportsUserUsage` |  `integer` The number of advanced reports users in usage.  
`versionMetadata` |  `string` Output only. Additional metadata to display next to the version (e.g. "Google.com").  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacySystem.getLicenseStatus`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## LicenceModuleStatus

The license module status.

JSON representation  
---  
      
    
    {
      "name": string,
      "identifier": string,
      "isActive": boolean
    }  
  
Fields  
---  
`name` |  `string` The name of the license module.  
`identifier` |  `string` The identifier of the license module.  
`isActive` |  `boolean` Whether the license module is active.  
  
## LicenseType

The license type.

Enums  
---  
`LICENSE_TYPE_UNSPECIFIED` | Unspecified license type.  
`ENTERPRISE` | Enterprise license type.  
`COMMUNITY` | Community license type.  
`EVALUATION` | Evaluation license type.  
`CLOUD` | Cloud license type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
