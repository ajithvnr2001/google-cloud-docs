---
url: https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups/
title: Apply policies to user groups using access bindings \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:08.368630+00:00
---

# Apply policies to user groups using access bindings  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Apply policies to user groups using access bindings Stay organized with collections  Save and categorize content based on your preferences. 

You can use access bindings to control which applications and resources your user groups can access. An access binding specifies how to apply access levels and session controls to a user group. You can apply the same access level and session control to all applications, or you can define specific behaviors for individual applications.

**Preview — Session controls feature only**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To ensure that you configured everything correctly, test your policies before enforcing them.

When working with access bindings, keep in mind the following behavior:

  * A user group can have only one access binding.
  * If a user belongs to multiple groups, the user is granted access if any policy allows it (`OR` not `AND`).
  * For session controls, only the most recently created access binding applies.



## Use a single configuration for all applications

This method applies the same access level and session control to all of the applications accessed by a user group.

We recommend that you test your policy with a dry-run or apply it to a small test group before implementing it in production.

###  gcloud 

Create the access binding.
    
    
    gcloud access-context-manager cloud-bindings create \
         --group-key GROUP_ID
         --organization ORG_ID
         --level DEFAULT_ACCESS_LEVEL
      [  --session-length=DEFAULT_SESSION_LENGTH                ]
      [  --session-reauth-method=DEFAULT_SESSION_REAUTH_METHOD  ]

Replace the following:

  * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
  * ORG_ID: Your organization ID. 
  * DEFAULT_ACCESS_LEVEL: The optional access level name, which takes the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Replace `POLICY_ID` with the access policy ID, and `ACCESS_LEVEL_NAME` with the access level name. 
  * DEFAULT_SESSION_LENGTH: The optional session duration in the hour format, such as `15h` for 15 hours, or `2h` for two hours. 
  * DEFAULT_SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following: 
    * `LOGIN`: Apply the standard login, which can include MFA or other Workspace-defined factors.
    * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP is not live, users must sign in through the IdP.
    * `SECURITY_KEY`: Require a hardware security key.



###  API 

  1. Create a JSON body:
         
         {
           "groupKey": "GROUP_ID",
           "accessLevels": [
             "DEFAULT_ACCESS_LEVEL"
           ],
           // optional:
           "sessionSettings": {
             "sessionLength": "DEFAULT_SESSION_LENGTH",
             "sessionReauthMethod": "DEFAULT_SESSION_REAUTH_METHOD"
           }
         }
         

Replace the following:

     * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
     * DEFAULT_ACCESS_LEVEL: The optional access level name, which takes the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Replace `POLICY_ID` with the access policy ID, and `ACCESS_LEVEL_NAME` with the access level name. 
     * DEFAULT_SESSION_LENGTH: The optional session duration in the hour format, such as `15h` for 15 hours, or `2h` for two hours. 
     * DEFAULT_SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following: 
       * `LOGIN`: Apply the standard login, which can include MFA or other Workspace-defined factors.
       * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP is not live, users must sign in through the IdP.
       * `SECURITY_KEY`: Require a hardware security key.
  2. Send the POST request:
         
         POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
         

ORG_ID is the ID for the organization that you used to create the [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) role. If the `access-context-manager/organization` property hasn't been set, replace `ORG_ID` in the optional `--organization` flag with the ID for the organization that you used when you created the Cloud Access Binding Admin role.




If successful, you receive a representation of the JSON object. If a problem occurs, you receive an error message.

## Define configurations for specific applications

This method lets you apply different access levels and session controls to different applications. You can also set default rules for applications that don't have specific configurations.

You can specify applications in access bindings using their OAuth client ID. You can specify the following applications using their name:

  * [Cloud Console](https://console.cloud.google.com/)
  * [Google Cloud SDK](https://cloud.google.com/sdk/gcloud)

**Caution:** Access levels applied to the Google Cloud SDK application don't affect access to Cloud Shell. Cloud Shell operates in a separate environment that's not governed by Context-Aware Access policies set on the Google Cloud SDK. To control access to Cloud Shell, you must disable Cloud Shell at the organization level. For more information, see [Disable or reset Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell).

  * [Google Auth Library](https://googleapis.dev/nodejs/google-auth-library/5.6.1/) If you use the [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) generated by the [gcloud CLI](https://cloud.google.com/sdk/gcloud) and you want to use the name, you must use the default client ID built into the gcloud CLI. You cannot provide a client ID file to the gcloud CLI.
  * [Firebase Console](https://console.firebase.google.com)



This method is useful when you want to do the following:

  * Apply policies to only certain applications.
  * Create a general policy, but exclude some applications from it.




###  gcloud 

  1. Create a binding file in YAML format with a list of scope entries within the `scopedAccessSettings` list. For each application that you want to map to a specific access level, include a `clientScope` entry.
         
         scopedAccessSettings:
         - scope:
             clientScope:
               restrictedClientApplication:
                 clientId: CLIENT_ID
           activeSettings:
             accessLevels:
             - ACCESS_LEVEL_A
             sessionSettings:
               sessionLength: SESSION_LENGTH
               sessionReauthMethod: SESSION_REAUTH_METHOD
               sessionLengthEnabled: true
         - scope:
             clientScope:
               restrictedClientApplication:
                 name: CLIENT_NAME
           activeSettings:
             accessLevels:
             - ACCESS_LEVEL_B
         

Replace the following:

     * CLIENT_ID: The OAuth client ID. You can use either `clientId` or `name` when an application contains `sessionSettings`.
     * ACCESS_LEVEL_A: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * SESSION_LENGTH: The session duration in the hour format, such as `15h` for 15 hours, or `2h` for two hours.
     * SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following:

       * `LOGIN`: Apply the standard login, which can include multifactor authentication (MFA) or other Workspace-defined factors.
       * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP is not live, users must sign in through the IdP.
       * `SECURITY_KEY`: Require a hardware security key.
     * CLIENT_NAME: The client name. You can use either `name` or `clientId` when an application contains `sessionSettings`.

     * ACCESS_LEVEL_B: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.

To set a default access level for applications not defined in the YAML file, use the `--level` argument. The YAML file only supports application-specific settings (`scopedAccessSettings`).

  2. Create the access binding.
         
         gcloud access-context-manager cloud-bindings create
             --organization ORG_ID
             --group-key GROUP_ID
             --binding-file BINDING_FILE_PATH
           [  --level DEFAULT_ACCESS_LEVEL ]
           [  --session-length=DEFAULT_SESSION_LENGTH                ]
           [  --session-reauth-method=DEFAULT_SESSION_REAUTH_METHOD  ]
         

Replace the following:

     * ORG_ID: Your organization ID. 
     * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
     * BINDING_FILE_PATH: The path to the YAML file that contains the access binding scheme. The binding file supports only `scopedAccessSettings`. 
     * DEFAULT_ACCESS_LEVEL: The optional access level name, which takes the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Replace `POLICY_ID` with the access policy ID, and `ACCESS_LEVEL_NAME` with the access level name. 
     * DEFAULT_SESSION_LENGTH: The optional session duration in the hour format, such as `15h` for 15 hours, or `2h` for two hours. 
     * DEFAULT_SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following: 
       * `LOGIN`: Apply the standard login, which can include MFA or other Workspace-defined factors.
       * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP is not live, users must sign in through the IdP.
       * `SECURITY_KEY`: Require a hardware security key.



#### How the `--level` and `--binding-file` arguments work together

  * If you only use `--binding-file`, only the applications in the file have the policies applied.
  * If you only use `--level`, the access level applies to all applications.
  * If you use both, the rules are combined. The `--level` value applies to all applications, whereas the policies in the YAML file specified by `--binding-file` only apply to the applications as defined in the file.



#### Working with session controls

  * To set default session controls for all applications, use `--session-length` and `--session-reauth-method`.
  * If you also define session controls in the YAML file, those session controls override the default settings for those specific applications.
  * You must use both `--session-length` and `--session-reauth-method` together.



###  API 

Create a JSON body:
    
    
    {
      "groupKey": "GROUP_ID",
       //
       // Optional; if specified, all applications that aren't defined in
       // scopedAccessSettings have these access levels applied.
       //
       // If more than one access level is specified, the user is
       // granted access if any one resolves to TRUE (OR logic, not AND).
       //
       // If you omit this key entirely, then no policy enforcement is
       // applied by default.
       //
      "accessLevels": [
        "DEFAULT_ACCESS_LEVEL"
      ],
      "scopedAccessSettings": [
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "clientId": "CLIENT_ID"
              }
            }
          },
          "activeSettings": {
            "accessLevels": [
              "ACCESS_LEVEL_A"
            ],
            "sessionSettings": {
              "sessionLength": "SESSION_LENGTH",
              "sessionReauthMethod": "SESSION_REAUTH_METHOD",
              "sessionLengthEnabled": true
            }
          }
        },
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "CLIENT_NAME"
              }
            },
            "activeSettings": {
              "accessLevels": [
                "ACCESS_LEVEL_B"
              ]
            }
          }
        }
      ]
    }
    

Replace the following:

  * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
  * DEFAULT_ACCESS_LEVEL: The optional access level name, which takes the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Replace `POLICY_ID` with the access policy ID, and `ACCESS_LEVEL_NAME` with the access level name. 
  * CLIENT_ID: The OAuth client ID. You can use either `clientId` or `name` when an application contains `sessionSettings`.
  * ACCESS_LEVEL_A: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  * SESSION_LENGTH: The session duration in the hour format, such as `2h` for two hours.
  * SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following:

    * `LOGIN`: Apply the standard login, which can include MFA or other Workspace-defined factors.
    * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP isn't live, users must sign in through the IdP.
    * `SECURITY_KEY`: Require a hardware security key.
  * CLIENT_NAME: The client name. You can use either `name` or `clientId` when an application contains `sessionSettings`.

  * ACCESS_LEVEL_B: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.




Send the POST request:
    
    
    POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
    

ORG_ID is the ID for the organization that you used to create the [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) role. If the `access-context-manager/organization` property hasn't been set, replace `ORG_ID` in the optional `--organization` flag with the ID for the organization that you used when you created the Cloud Access Binding Admin role.

If successful, you should receive a representation of the JSON object, or an error message if there was a problem.

## Use dry-run access levels to simulate enforcement

Dry-run access levels let you test your access policies without actually enforcing them. This helps you understand the impact of a policy before it goes live. You can view the dry-run logs to see what would have happened if the policy were active.

Only access levels can be used in dry-run mode. Session controls are not available in dry-run mode.

### Create a blanket dry-run policy

This method applies the same dry-run access level to all of the applications accessed by a user group.

###  gcloud 

Create the access binding with the `--dry-run-level` flag.
    
    
    gcloud access-context-manager cloud-bindings create \
         --group-key=<var>GROUP_ID</var> \
         --organization=<var>ORG_ID</var> \
         --dry-run-level=<var>DEFAULT_DRY_RUN_ACCESS_LEVEL</var>
    

Replace the following:

  * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
  * ORG_ID: Your organization ID. 
  * DEFAULT_DRY_RUN_ACCESS_LEVEL: The dry-run access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.



###  API 

  1. Create a JSON body containing `dry_run_access_levels`.
         
         {
           "group_key": "GROUP_ID",
           "dry_run_access_levels": [
             "DEFAULT_DRY_RUN_ACCESS_LEVEL"
           ]
         }
         

Replace the following:

     * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
     * DEFAULT_DRY_RUN_ACCESS_LEVEL: The dry-run access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  2. Send the POST request:
         
         POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
         

ORG_ID is the ID for the organization that you used to create the [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) role. If the `access-context-manager/organization` property hasn't been set, replace `ORG_ID` in the optional `--organization` flag with the ID for the organization that you used when you created the Cloud Access Binding Admin role.




### Create a dry-run policy for specific applications

This method lets you apply different dry-run access levels to different applications. You can also set default rules for applications without a specific configuration.

###  gcloud 

  1. Configure the access settings in a YAML binding file using `dryRunSettings` field.
         
         scopedAccessSettings:
         - scope:
             clientScope:
               restrictedClientApplication:
                 name: CLIENT_NAME
           activeSettings:
             accessLevels:
             - ACCESS_LEVEL_A
           dryRunSettings:
             accessLevels:
             - DRY_RUN_ACCESS_LEVEL_1
         - scope:
             clientScope:
               restrictedClientApplication:
                 clientId: CLIENT_ID
           dryRunSettings:
             accessLevels:
             - DRY_RUN_ACCESS_LEVEL_2
         

Replace the following:

     * CLIENT_NAME: The client name. You can use either `name` or `clientId` when an application contains `sessionSettings`.
     * ACCESS_LEVEL_A: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * DRY_RUN_ACCESS_LEVEL_1: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * CLIENT_ID: The OAuth client ID. You can use either `clientId` or `name` when an application contains `sessionSettings`.
     * DRY_RUN_ACCESS_LEVEL_2: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  2. Create the access binding.
         
         gcloud access-context-manager cloud-bindings create \
           --organization ORG_ID \
           --group-key GROUP_ID \
           --binding-file BINDING_FILE_PATH
           --dry-run-level DEFAULT_DRY_RUN_ACCESS_LEVEL
         

Replace the following:

     * ORG_ID: Your organization ID. 
     * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
     * BINDING_FILE_PATH: The path to the YAML file that contains the access binding scheme. The binding file supports only `scopedAccessSettings`. 
     * DEFAULT_DRY_RUN_ACCESS_LEVEL: An optional dry-run access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.

Include this flag to apply the specified dry-run access level to all applications by default if they aren't specified in the YAML.




###  API 

  1. Create a JSON body:
         
         {
           "group_key": "GROUP_ID",
           //
           // Optional; if specified, all applications that aren't defined in scopedAccessSettings will have these dry-run access levels applied.
           //
           "dry_run_access_levels": [
             "DEFAULT_DRY_RUN_ACCESS_LEVEL"
           ],
           "scoped_access_settings": [
             {
               "scope": {
                 "client_scope": {
                   "restricted_client_application": {
                     "name": "CLIENT_NAME"
                   }
                 }
               },
               "active_settings": {
                 "access_levels": [
                   "ACCESS_LEVEL_A"
                 ]
               },
               "dry_run_settings": {
                 "access_levels": [
                   "DRY_RUN_ACCESS_LEVEL_1"
                 ]
               }
             },
             {
               "scope": {
                 "client_scope": {
                   "restricted_client_application": {
                     "client_id": "CLIENT_ID"
                   }
                 }
               },
               "dry_run_settings": {
                 "access_levels": [
                   "DRY_RUN_ACCESS_LEVEL_2"
                 ]
               }
             }
           ]
         }
         

Replace the following:

     * GROUP_ID: The group ID. If you don't have the group ID available, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. 
     * DEFAULT_DRY_RUN_ACCESS_LEVEL: An optional dry-run access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * CLIENT_NAME: The client name. You can use either `name` or `clientId` when an application contains `sessionSettings`.
     * ACCESS_LEVEL_A: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * DRY_RUN_ACCESS_LEVEL_1: An access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * CLIENT_ID: The OAuth client ID. You can use either `client_id` or `name` when an application contains `sessionSettings`.
     * DRY_RUN_ACCESS_LEVEL_2: An access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  2. Send the POST request:
         
         POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
         

ORG_ID is the ID for the organization that you used to create the [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) role. If the `access-context-manager/organization` property hasn't been set, replace `ORG_ID` in the optional `--organization` flag with the ID for the organization that you used when you created the Cloud Access Binding Admin role.

If successful, you receive a representation of the JSON object. If a problem occurs, you receive an error message.




### View the dry-run logs

After you set up a dry-run, you can check the logs to see which access attempts would have been denied.

The following table lists the log fields that you can use to create and run the query to get the logs:

Field name | Description  
---|---  
`protoPayload.authenticationInfo.principalEmail` | Email ID of the principal that the access is denied for.  
`protoPayload.metadata.deniedApplications` | Name of the application that the access is denied for.  
`protoPayload.metadata.evaluationResult` | The evaluation result of the active access policy. Possible values: `GRANTED` or `DENIED`. If no active access levels are applied in the binding, this field is set to `GRANTED`.  
`protoPayload.metadata.appliedAccessLevels` | The applied access levels required by the active access policy.  
`protoPayload.metadata.appliedDryRunAccessLevels` | The applied access levels required by the dry-run access policy.  
`protoPayload.metadata.dryRunEvaluationResult` | The evaluation result of the dry-run access policy, which indicates the intended action when the access policy is enforced. Possible values: `GRANTED` or `DENIED`. If no dry-run access levels are applied in the binding, this field is set to `GRANTED`, even when `evaluationResult` is `DENIED`.  
`protoPayload.metadata.unsatisfiedAccessLevels` | The access levels in the organization that the request failed to satisfy. This list can include access levels that aren't applied in the access binding. To identify which access levels caused an access denial, compare this field with `appliedAccessLevels` or `appliedDryRunAccessLevels`.  
  
For instructions on how to create a query for logs, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
