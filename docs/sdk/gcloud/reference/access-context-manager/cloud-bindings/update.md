---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update/
title: gcloud access-context-manager cloud-bindings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:52:57.662271+00:00
---

# gcloud access-context-manager cloud-bindings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager cloud-bindings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager cloud-bindings update - update an existing cloud access binding under an organization 
SYNOPSIS
    

`gcloud access-context-manager cloud-bindings update` (`--binding`=`BINDING` : `--organization`=`ORGANIZATION`) [`--append`] [`--binding-file`=`YAML_FILE`] [`--dry-run-level`=[`DRY_RUN_LEVEL`,…]] [`--level`=[`LEVEL`,…]] [`--session-length`=`SESSION_LENGTH`] [`--session-reauth-method`=`SESSION_REAUTH_METHOD`; default="login"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an existing cloud access binding. You can update the level, dry run level, session settings, and scoped access settings. They cannot all be empty. 

For Google Group bindings (`--group-key`), you can update any combination of the access level, dry run level, top-level session settings (1 hour to 24 hours, or 0 to disable), and scoped access settings for specific applications (`restrictedClientApplication`). 

For bindings tied to all workforce pools in an organization (`principalSet://cloudresourcemanager.googleapis.com/organizations/{organization_id}/type/WorkforcePool`), you can update or append scoped access settings with `restrictedProject` and active `sessionSettings` using `--binding-file`. Top-level session settings, top-level access levels, dry run levels, and application scopes (`restrictedClientApplication`) are not supported for this principal type. 

Session settings are supported only for Google Groups and bindings tied to all workforce pools in an organization. No other bindings allow session settings, and requests containing session settings for other principal types are rejected. 

EXAMPLES
     To update an existing cloud access binding, run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --level=accessPolicies/123/accessLevels/new-abc

To remove level and add dry run level, run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --level= --dry-run-level=accessPolicies/123/accessLevels/new-def

To replace scoped access settings (such as for specific applications on a group binding or restricted projects on a workforce pool binding) with a new list, run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml'

To append scoped access settings to the existing list, run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml' --append

Note this is only possible for scoped access settings that exclusively hold session settings (that is, no access levels). 

To update or append project-scoped session settings on a binding tied to all workforce pools in an organization: 
    
    
    Create a binding.yaml file containing the desired scopedAccessSettings with restrictedProject:
    
    
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
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml' --append

To update top-level session settings on a Google Group binding, run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --session-length=2h

To update the session reauth method on a Google Group binding, you must also specify `--session-length` (this can be the existing value if you only want to modify the reauth method), run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --session-length=2h --session-reauth-method=login

To disable session settings on a Google Group binding, set `--session-length=0` and run the following command: 
    
    
    gcloud access-context-manager cloud-bindings update --binding=my-binding-id --session-length=0

REQUIRED FLAGS
    

Cloud access binding resource - The cloud access binding you want to update. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--binding`=`BINDING`
     ID of the cloud-access-binding or fully qualified identifier for the cloud-access-binding. 

To set the `binding` attribute: 

  * provide the argument `--binding` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     The ID of the organization. To set the `organization` attribute: 

  * provide the argument `--binding` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property `access_context_manager/organization`. 


OPTIONAL FLAGS
    

`--append`
     When true, append the `ScopedAccessSettings` in `--binding-file` to the existing `ScopedAccessSettings` on the binding. When false, the existing binding's `ScopedAccessSettings` will be overwritten. Defaults to false. You may only append `ScopedAccessSettings` that exclusively hold session settings (that is, no access levels). 
`--binding-file`=`YAML_FILE`
     Path to the file that contains a Google Cloud user access binding. 

This file contains a YAML-compliant object representing a GcpUserAccessBinding that contains `scopedAccessSettings` only. No other binding fields are allowed. 

For details about the object, see the API reference: <https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications>

For Google Group bindings, `scopedAccessSettings` can specify `restrictedClientApplication` (using `clientId` or `name`) with `accessLevels`, `dryRunAccessLevels`, and `sessionSettings` (session length up to 24 hours). The `restrictedProject` scope is not supported for Google Group bindings. 

For bindings tied to all workforce pools in an organization (`principalSet://cloudresourcemanager.googleapis.com/organizations/{organization_id}/type/WorkforcePool`), `scopedAccessSettings` must only contain `restrictedProject` (format: `name: projects/{project_number}`) within `scope.clientScope` and `sessionSettings` within `activeSettings`. For this configuration, the following requirements apply: 

  * `sessionLength` must be set and must be between 1 hour and 90 days (for example, `7776000s`). 
  * `sessionReauthMethod` must be `LOGIN` or omitted (defaults to `LOGIN`). 
  * `sessionLengthEnabled` must be set to `true`. 
  * `maxInactivity` must be set to 0 or omitted. 
  * `useOidcMaxAge` must be set to `false` or omitted. 
  * No application scopes (`restrictedClientApplication`), access levels, or dry run settings are allowed. 



The `restrictedProject` scope is usable only with bindings tied to all workforce pools in an organization. 

The file content replaces the corresponding fields in the existing binding, unless `--append` is specified. See `--append` help text for more details. 

`--dry-run-level`=[`DRY_RUN_LEVEL`,…]
     The dry run access level that replaces the existing dry run level for the given binding. The input must be the full identifier of an access level, such as `accessPolicies/123/accessLevels/new-def`. This parameter is not supported for bindings tied to all workforce pools in an organization. 
`--level`=[`LEVEL`,…]
     The access level that replaces the existing level for the given binding. The input must be the full identifier of an access level, such as `accessPolicies/123/accessLevels/new-abc`. This parameter is not supported for bindings tied to all workforce pools in an organization. 
`--session-length`=`SESSION_LENGTH`
     The maximum lifetime of a user session provided as an ISO 8601 duration string. Must be at least one hour or zero seconds, and no more than twenty-four hours. Granularity is limited to seconds. 

When `--session-length=0`, users in the group attached to this binding have infinite session length, which effectively disables session settings. 

A session begins after a user signs in successfully. If a user signs out before the end of the session lifetime, a new login creates a new session with a fresh lifetime. When a session expires, the user is asked to re-authenticate in accordance with `--session-reauth-method`. 

Setting `--session-reauth-method` when `--session-length` is empty raises an error. 

The session length is supported only for Google Group bindings. It isn't supported for bindings tied to all workforce pools in an organization, or for any other principal type. For bindings tied to all workforce pools in an organization, update or append session settings through `--binding-file`. 

`--session-reauth-method`=`SESSION_REAUTH_METHOD`; default="login"
     Specifies the security check a user must undergo when their session expires. Defaults to `--session-reauth-method=LOGIN` if unspecified and `--session-length` is set. Cannot be used when `--session-length` is empty or 0. This parameter is supported only for Google Group bindings. It isn't supported for bindings tied to all workforce pools in an organization; for those bindings, configure session settings through `--binding-file`. `SESSION_REAUTH_METHOD` must be one of: 

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
     This command uses the `accesscontextmanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha access-context-manager cloud-bindings update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
