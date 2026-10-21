---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/create/
title: gcloud alpha access-context-manager cloud-bindings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:04.138850+00:00
---

# gcloud alpha access-context-manager cloud-bindings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha access-context-manager cloud-bindings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha access-context-manager cloud-bindings create - create cloud access bindings for a specific group 
SYNOPSIS
    

`gcloud alpha access-context-manager cloud-bindings create` [`--binding-file`=`YAML_FILE`] [`--dry-run-level`=[`DRY_RUN_LEVEL`,…]] [`--federated-principal`=`FEDERATED_PRINCIPAL`] [`--group-key`=`GROUP_KEY`] [`--level`=[`LEVEL`,…]] [`--organization`=`ORGANIZATION`] [`--service-account`=`SERVICE_ACCOUNT`] [`--service-account-project-number`=`SERVICE_ACCOUNT_PROJECT_NUMBER`] [`--session-length`=`SESSION_LENGTH`] [`--session-reauth-method`=`SESSION_REAUTH_METHOD`; default="login"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new cloud access binding. 

For Google Group bindings (`--group-key`), the access level, the session settings, or both can apply globally across the group or be scoped to specific applications using `--binding-file`. To apply an access level or session settings to a specific application, specify `restrictedClientApplication` in the `--binding-file`. In this case, the settings specified in the binding file apply to the group for those restricted applications. 

The access level can also be bound to a specific service account or all service accounts in a specified project. 

To apply session settings to all workforce pools in an organization, specify the `restrictedProject` scope in the `--binding-file` with `--federated-principal` set to `principalSet://cloudresourcemanager.googleapis.com/organizations/{organization_id}/type/WorkforcePool`. Bindings created for all workforce pools in an organization support only `scopedAccessSettings` with the `restrictedProject` client scope and active `sessionSettings`. Application scopes (`restrictedClientApplication`), top-level session settings, access levels, and dry run levels are not allowed for this principal type. 

Binding session settings to other principal types isn't supported, and those requests are rejected. You can bind session settings only to the following principal types: 

  * Google Groups: specify the group by using the `--group-key` flag. 
  * All workforce pools in an organization: specify the organization's workforce pools by using the `--federated-principal` flag. Binding session settings to other federated principals isn't supported. 


EXAMPLES
     To create a new cloud access binding, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --level=accessPolicies/123/accessLevels/abc

To create a new cloud access binding for particular applications (with access levels, session settings, or both) using a YAML file, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --organization='1234567890' --binding-file='binding.yaml'

To create a new cloud access binding with a global access level, and settings for particular applications using a YAML file, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --level=accessPolicies/123/accessLevels/abc --organization='1234567890' --binding-file='binding.yaml'

To create a new cloud access binding for the dry run access level, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --level=accessPolicies/123/accessLevels/abc --dry-run-level=accessPolicies/123/accessLevels/def

To create a new cloud access binding with global session settings, specify your session length using an ISO duration string and the `session-length` flag. For example, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --organization='1234567890' --session-length=2h

To set a particular session reauth method for these session settings, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --organization='1234567890' --session-length=2h --session-reauth-method=LOGIN

Global and per-app session settings can be set on the same group, along with access levels. For example, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --group-key=my-group-key --organization='1234567890' --session-length=2h --session-reauth-method=LOGIN --level=accessPolicies/123/accessLevels/abc --dry-run-level=accessPolicies/123/accessLevels/def --binding-file='binding.yaml'

To create a new cloud access binding for a particular service account, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --service-account=service-account@project.iam.gserviceaccount.com --level=accessPolicies/123/accessLevels/abc --organization='1234567890'

To create a new cloud access binding for all service accounts in a particular project, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --service-account-project-number='987654321' --level=accessPolicies/123/accessLevels/abc --organization='1234567890'

To create a new cloud access binding for a specific federated principal, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings create --federated-principal='principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/my-subject' --level=accessPolicies/123/accessLevels/abc --organization='1234567890'

To create a new cloud access binding for all workforce pools in a given organization with project-scoped session settings: 
    
    
    Create a binding.yaml file containing scopedAccessSettings with restrictedProject and
    activeSettings (session length between 1 hour and 90 days, sessionReauthMethod: LOGIN,
    and sessionLengthEnabled: true):
    
    
    scopedAccessSettings:
    - scope:
        clientScope:
          restrictedProject:
            name: projects/1234567890
      activeSettings:
        sessionSettings:
          sessionLength: 7776000s
          sessionLengthEnabled: true
          sessionReauthMethod: LOGIN
    
    
    Then run the following command:
    
    
    gcloud alpha access-context-manager cloud-bindings create --federated-principal='principalSet://cloudresourcemanager.googleapis.com/organizations/1234567890/type/WorkforcePool' --organization='1234567890' --binding-file='binding.yaml'

FLAGS
    

`--binding-file`=`YAML_FILE`
     Path to the file that contains a Google Cloud user access binding. 

This file contains a YAML-compliant object representing a GcpUserAccessBinding that contains `scopedAccessSettings` only. No other binding fields are allowed. 

For details about the object, see the API reference: <https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications>

For Google Group bindings (`--group-key`), `scopedAccessSettings` can specify `restrictedClientApplication` (using `clientId` or `name`) with `accessLevels`, `dryRunAccessLevels`, and `sessionSettings` (session length up to 24 hours). The `restrictedProject` scope is not supported for Google Group bindings. 

For bindings tied to all workforce pools in an organization (`principalSet://cloudresourcemanager.googleapis.com/organizations/{organization_id}/type/WorkforcePool`), `scopedAccessSettings` must only contain `restrictedProject` (format: `name: projects/{project_number}`) within the `scope.clientScope` and `sessionSettings` within `activeSettings`. For this configuration, the following requirements apply: 

  * `sessionLength` must be set and must be between 1 hour and 90 days (for example, `7776000s`). 
  * `sessionReauthMethod` must be `LOGIN` or omitted (defaults to `LOGIN`). 
  * `sessionLengthEnabled` must be set to `true`. 
  * `maxInactivity` must be set to 0 or omitted. 
  * `useOidcMaxAge` must be set to `false` or omitted. 
  * No application scopes (`restrictedClientApplication`), access levels, or dry run settings are allowed. 



The `restrictedProject` scope is usable only with bindings tied to all workforce pools in an organization. 

`--dry-run-level`=[`DRY_RUN_LEVEL`,…]
     The dry run access level that binds to the given group. The dry run access level will be evaluated but won't be enforced. Denial on dry run access level will be logged. The input must be the full identifier of an access level, such as `accessPolicies/123/accessLevels/new-def`. 
`--federated-principal`=`FEDERATED_PRINCIPAL`
     The IAM principal identifier of the federated workforce or workload to assign the policy to. Examples include the following: 

  * Single principal: `principal://iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/subject/{subject_attribute_value}`
  * All workloads in a workload identity pool: `principalSet://iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/*`
  * All Workforce Pools in a Google Cloud organization: `principalSet://cloudresourcemanager.googleapis.com/organizations/{organization_id}/type/WorkforcePool`



Bindings created for all Workforce Pools in an organization support only `scopedAccessSettings` with the `restrictedProject` client scope and active `sessionSettings`. No other configurations (such as application scopes, access levels, or dry run settings) are allowed. 

Session settings cannot be configured for individual federated principals or workload identity pools. At most one of `--group-key`, `--federated-principal`, `--service-account`, or `--service-account-project-number` can be specified. 

`--group-key`=`GROUP_KEY`
     Google Group ID whose members are subject to the restrictions of this binding. At most one of `--group-key`, `--federated-principal`, `--service-account`, or `--service-account-project-number` can be specified. 
`--level`=[`LEVEL`,…]
     The access level that binds to the given group. The input must be the full identifier of an access level, such as `accessPolicies/123/accessLevels/abc`. 
`--organization`=`ORGANIZATION`
     Parent organization for this binding. 
`--service-account`=`SERVICE_ACCOUNT`
     Service account email that this binding applies to. Used to assign policies to a single first-party service account. At most one of `--group-key`, `--federated-principal`, `--service-account`, or `--service-account-project-number` can be specified. 
`--service-account-project-number`=`SERVICE_ACCOUNT_PROJECT_NUMBER`
     Project number of the project that contains the service accounts that are subject to the restrictions of this binding. Used to assign policies to all service accounts in a Google Cloud project. At most one of `--group-key`, `--federated-principal`, `--service-account`, or `--service-account-project-number` can be specified. 
`--session-length`=`SESSION_LENGTH`
     The maximum lifetime of a user session provided as an ISO 8601 duration string. Must be at least one hour or zero seconds, and no more than twenty-four hours. Granularity is limited to seconds. 

When `--session-length=0`, users in the group attached to this binding have infinite session length, which effectively disables session settings. 

A session begins when a user signs in successfully. If a user signs out before the end of the session lifetime, a new login creates a new session with a fresh lifetime. When a session expires, the user is asked to re-authenticate in accordance with `--session-reauth-method`. 

Setting `--session-reauth-method` when `--session-length` is empty raises an error. 

The session length applies only to Google Group bindings (`--group-key`). It isn't supported for bindings tied to all workforce pools in an organization, or for any other principal type. For bindings tied to all workforce pools in an organization, configure session settings through `--binding-file`, under `scopedAccessSettings` on the `restrictedProject` scope. 

`--session-reauth-method`=`SESSION_REAUTH_METHOD`; default="login"
     Specifies the type of re-authentication challenge given to the user when their session expires. Defaults to `--session-reauth-method=login` if unspecified and `--session-length` is set. Cannot be used when `--session-length` is empty or 0. This parameter is supported only for Google Group bindings. It isn't supported for bindings tied to all workforce pools in an organization; for those bindings, configure session settings through `--binding-file`. `SESSION_REAUTH_METHOD` must be one of: 

`login`
     The user will be prompted to perform regular login. Users who are enrolled for two-step verification and haven't chosen to "Remember this computer" will be prompted for their second factor. 
`password`
     The user will only be required to enter their password. 
`security-key`
     The user will be prompted to authenticate using their security key. If no security key has been configured, authentication will fall back to LOGIN. For help configuring your security key, see <https://support.google.com/a/answer/2537800?hl=en#zippy=%2Cview-add-or-remove-security-keys>
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud access-context-manager cloud-bindings create](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
