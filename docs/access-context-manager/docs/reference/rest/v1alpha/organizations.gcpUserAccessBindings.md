---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings
title: REST Resource: organizations.gcpUserAccessBindings \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:25.265648+00:00
---

# REST Resource: organizations.gcpUserAccessBindings  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  REST Resource: organizations.gcpUserAccessBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GcpUserAccessBinding
    * JSON representation
  * Principal
    * JSON representation
  * SessionSettings
    * JSON representation
  * SessionReauthMethod
  * ScopedAccessSettings
    * JSON representation
  * AccessScope
    * JSON representation
  * ClientScope
    * JSON representation
  * Application
    * JSON representation
  * Project
    * JSON representation
  * AccessSettings
    * JSON representation
  * Methods



## Resource: GcpUserAccessBinding

Restricts access to Cloud Console and Google Cloud APIs for a set of users using Context-Aware Access.

JSON representation  
---  
      
    
    {
      "name": string,
      "groupKey": string,
      "principal": {
        object ([Principal](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#Principal))
      },
      "accessLevels": [
        string
      ],
      "dryRunAccessLevels": [
        string
      ],
      "sessionSettings": {
        object ([SessionSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#SessionSettings))
      },
      "scopedAccessSettings": [
        {
          object ([ScopedAccessSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#ScopedAccessSettings))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by [RFC 3986 Section 2.3](https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"  
`groupKey` |  `string` Optional. Immutable. Google Group id whose users are subject to this binding's restrictions. See "id" in the [Google Workspace Directory API's Group Resource](https://developers.google.com/admin-sdk/directory/v1/reference/groups#resource). If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"  
`principal` |  `object (`[Principal](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#Principal)`)` Optional. Immutable. The principal that is subject to the access policies in this policy binding.  
`accessLevels[]` |  `string` Optional. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"  
`dryRunAccessLevels[]` |  `string` Optional. Dry run access level that will be evaluated but will not be enforced. The access denial based on dry run policy will be logged. Only one access level is supported, not multiple. This list must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"  
`sessionSettings` |  `object (`[SessionSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#SessionSettings)`)` Optional. The Google Cloud session length (GCSL) policy for the group key.  
`scopedAccessSettings[]` |  `object (`[ScopedAccessSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#ScopedAccessSettings)`)` Optional. A list of scoped access settings that set this binding's restrictions on a subset of applications.  
  
## Principal

The comprehensive identity container supporting all 1p and 3p identities. Only one of them can be set to create an access binding. Next ID: 5

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "federatedPrincipal": string,
      "serviceAccountProjectNumber": string,
      "serviceAccount": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`federatedPrincipal` |  `string` Immutable. The IAM principal identifier of the federated workforce or workload to assign the policy to. Examples include the following:

  * Single principal: `principal://iam.googleapis.com/projects/{projectNumber}/locations/global/workloadIdentityPools/{pool_id}/subject/{subject_attribute_value}`
  * All workloads in a workload identity pool: `principalSet://iam.googleapis.com/projects/{projectNumber}/locations/global/workloadIdentityPools/{pool_id}/*`
  * All Workforce Pools in a Google Cloud organization: `principalSet://cloudresourcemanager.googleapis.com/organizations/{organizationId}/type/WorkforcePool`

Bindings created for all Workforce Pools in a Google Cloud organization support only `scopedAccessSettings` with the `restrictedProject` client scope and active `sessionSettings`. No other configurations are allowed.  
`serviceAccountProjectNumber` |  `string` Immutable. Project number used to assign policies to all service accounts in a Google Cloud project.  
`serviceAccount` |  `string` Immutable. Service account email used to assign policies to a single service account.  
End of mutually exclusive fields.  
  
## SessionSettings

Stores settings related to Google Cloud Session Length including session duration, the type of challenge (i.e. method) they should face when their session expires, and other related settings.

JSON representation  
---  
      
    
    {
      "sessionReauthMethod": enum ([SessionReauthMethod](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#SessionReauthMethod)),
      "sessionLength": string,
      "maxInactivity": string,
      "useOidcMaxAge": boolean,
      "sessionLengthEnabled": boolean
    }  
  
Fields  
---  
`sessionReauthMethod` |  `enum (`[SessionReauthMethod](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#SessionReauthMethod)`)` Optional. Session method when user's Google Cloud session is up.  
`sessionLength` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The session length. Setting this field to zero allows for sessions that are active indefinitely. Also, setting `sessionLengthEnabled` to `false` disregards session limits, which means that sessions never expire. If `useOidcMaxAge` is `true`, for OIDC apps, the session length will be the minimum of this field and the OIDC `max_age` param. If this field is set to zero, `sessionLengthEnabled` must be set to `false` or left unset.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`maxInactivity` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long a user is allowed to take between actions before a new access token must be issued. Only set for Google Cloud apps.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`useOidcMaxAge` |  `boolean` Optional. Only useful for OIDC apps. When false, the OIDC max_age param, if passed in the authentication request will be ignored. When true, the re-auth period will be the minimum of the sessionLength field and the max_age OIDC param.  
`sessionLengthEnabled` |  `boolean` Optional. This field enables or disables Google Cloud session length. When false, all fields set above will be disregarded and the session length is basically infinite. If `sessionLength` is set to zero, this field must be set to false.  
  
## SessionReauthMethod

The session challenges proposed to users when the Google Cloud session length is up.

Enums  
---  
`SESSION_REAUTH_METHOD_UNSPECIFIED` | If method is undefined in the API, LOGIN will be used by default.  
`LOGIN` | The user will be prompted to perform regular login. Users who are enrolled for two-step verification and haven't chosen "Remember this computer" will be prompted for their second factor.  
`SECURITY_KEY` | The user will be prompted to authenticate using their security key. If no security key has been configured, then authentication will fallback to LOGIN.  
`PASSWORD` | The user will be prompted for their password.  
  
## ScopedAccessSettings

A relationship between access settings and its scope.

JSON representation  
---  
      
    
    {
      "scope": {
        object ([AccessScope](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#AccessScope))
      },
      "activeSettings": {
        object ([AccessSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#AccessSettings))
      },
      "dryRunSettings": {
        object ([AccessSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#AccessSettings))
      }
    }  
  
Fields  
---  
`scope` |  `object (`[AccessScope](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#AccessScope)`)` Optional. Application, etc. to which the access settings will be applied to. Implicitly, this is the scoped access settings key; as such, it must be unique and non-empty.  
`activeSettings` |  `object (`[AccessSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#AccessSettings)`)` Optional. Access settings for this scoped access settings. This field may be empty if dryRunSettings is set.  
`dryRunSettings` |  `object (`[AccessSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#AccessSettings)`)` Optional. Dry-run access settings for this scoped access settings. This field may be empty if activeSettings is set.  
  
## AccessScope

Access scope represents the client scope, etc. to which the settings will be applied to.

JSON representation  
---  
      
    
    {
      "clientScope": {
        object ([ClientScope](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#ClientScope))
      }
    }  
  
Fields  
---  
`clientScope` |  `object (`[ClientScope](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#ClientScope)`)` Optional. Client scope for this access scope.  
  
## ClientScope

Client scope represents the application, project, etc. subject to this binding's restrictions.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "restrictedClientApplication": {
        object ([Application](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#Application))
      },
      "restrictedProject": {
        object ([Project](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#Project))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Client Scope Identifier The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`restrictedClientApplication` |  `object (`[Application](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#Application)`)` Optional. The application that is subject to this binding's scope.  
`restrictedProject` |  `object (`[Project](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#Project)`)` Optional. The Google Cloud project that is subject to this binding's scope.  
End of mutually exclusive fields.  
  
## Application

An application that accesses Google Cloud APIs.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "clientId": string,
      "name": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
An identifier of the application. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`clientId` |  `string` The OAuth client ID of the application.  
`name` |  `string` The name of the application. Example: "Cloud Console"  
End of mutually exclusive fields.  
  
## Project

A Google Cloud project which contains applications and resources that users can access.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` The Google Cloud project resource name. Format: `projects/{projectNumber}`. Only the project number is supported. Example: `projects/1234567890`  
  
## AccessSettings

Access settings represent the set of conditions that must be met for access to be granted. At least one of the fields must be set.

JSON representation  
---  
      
    
    {
      "accessLevels": [
        string
      ],
      "sessionSettings": {
        object ([SessionSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#SessionSettings))
      }
    }  
  
Fields  
---  
`accessLevels[]` |  `string` Optional. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"  
`sessionSettings` |  `object (`[SessionSettings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#SessionSettings)`)` Optional. Session settings applied to user access on a given AccessScope.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings/create)`

|  Creates a `[GcpUserAccessBinding](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#GcpUserAccessBinding)`.  
  
### `[delete](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings/delete)`

|  Deletes a `[GcpUserAccessBinding](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#GcpUserAccessBinding)`.  
  
### `[get](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings/get)`

|  Gets the `[GcpUserAccessBinding](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#GcpUserAccessBinding)` with the given name.  
  
### `[list](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings/list)`

|  Lists all `[GcpUserAccessBindings](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#GcpUserAccessBinding)` for a Google Cloud organization.  
  
### `[patch](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings/patch)`

|  Updates a `[GcpUserAccessBinding](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/organizations.gcpUserAccessBindings#GcpUserAccessBinding)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
