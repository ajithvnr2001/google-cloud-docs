---
url: https://docs.cloud.google.com/access-context-manager/docs/session-controls-for-reauthentication/
title: Configure session controls for reauthentication \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:29.654948+00:00
---

# Configure session controls for reauthentication  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/session-controls-for-reauthentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configure session controls for reauthentication Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Before 2023, Google Cloud sessions had the default setting "Never Expire." Starting in 2023, Google Cloud started to enforce a default session length of 16 hours for Google Cloud console and Google Cloud SDK customers, which overrode the previous default setting. If the change was enforced on your organization after June 2026, your Google Admin console won't show this default policy. To override the default policy, use the Access Context Manager API. For an example, see Override the default 16-hour session length.

Session controls let you configure how often users must reauthenticate after being granted access and whether a full login, password only, or hardware security key is required.

You can apply session controls to do the following:

  * **Enforce frequent reauthentication for privileged users** : Require users with elevated privileges, such as project owners and billing administrators, to reauthenticate more frequently.
  * **Configure longer sessions for certain applications** : Allow supported applications, such as the Google Cloud console, Google Cloud SDK, or specific OAuth apps, to have longer session durations to preserve the large context window required for optimal performance.

**Warning:** If you previously created session controls for Google Workspace Organizational Units (OUs) using the Google Admin console and create session controls using Access Context Manager targeted to a Google Group, then the session controls defined in Access Context Manager bindings supersede OU session controls for the members of that Google Group and aren't visible in the Google Admin console.

## Define session length and reauthentication methods

You can define session controls when creating an Access Context Manager binding. For more information about the session controls, see [Apply policies to user groups using access bindings](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups).

###  gcloud 

  * [**Set default session controls for all applications**](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#use_a_single_configuration_for_all_applications)

Use the `--session-length` flag to set the session duration. The value must be `0s`, or between 1 hour and 24 hours. Specify the duration in hours. For example, use "12h" to set a session that is 12 hours long. Use the `--session-reauth-method` flag to specify the reauthentication method. For example, you can set a session duration time of 3 hours (3h) and a `LOGIN`, `PASSWORD`, or `SECURITY_KEY` reauthentication method.

This will be applied to all applications unless overridden by application-specific settings.

  * [**Set application-specific session controls**](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#define_configurations_for_specific_applications)

Define `scopedAccessSettings` in a YAML file to specify session controls for specific applications using `clientId`. This lets you override the default session controls for those applications. You can then pass the YAML file using the `--binding-file flag`.




###  REST API 

Define the `sessionLength` and `sessionReauthMethod` fields within the `sessionSettings` object in the JSON body of your POST request to create or update a `GcpUserAccessBinding` binding.

  * `sessionLength` is the session duration in seconds, formatted as the number of seconds followed by `s` (for example, `3600s`). The value must be `0s` or from `3600s` (1 hour) to `86400s` (24 hours). If set to `0s`, then `sessionLengthEnabled` must be set to `false` or left unset. You cannot set `sessionLength` to `0s` and `sessionLengthEnabled` to `true`.
  * `sessionReauthMethod` can be `LOGIN`, `PASSWORD`, or `SECURITY_KEY`.
  * Use `scopedAccessSettings` to define application-specific session controls. See [Define configurations for specific applications](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#api) for details.



###  Terraform 

Within the [Terraform Google Cloud User Access Binding resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/access_context_manager_gcp_user_access_binding), set the `session_settings` argument to configure general session length controls that apply to all user traffic:

  * `session_length`: The duration of the session in seconds. For example, `3600s` sets the session length to 1 hour. The `s` at the end is required.
  * `session_length_enabled`: Set to false to disable the specified session settings.
  * `session_reauth_method`: The type of authentication challenge that's used to refresh credentials. The options are `LOGIN`, `PASSWORD`, or `SECURITY_KEY`.
  * `use_oidc_max_age`: An advanced field that's used to configure whether the session honors an optional OIDC maximum age parameter, which is specified if the authenticating credential is an OAuth token.



When defining session controls only the most recently created access binding that matches the request is used when resolving session control settings.

## Example policy configuration

**Note:** To configure session controls for Workforce Identity Federation, see [Configure Extended Session Length for Workforce Identity Federation](https://docs.cloud.google.com/access-context-manager/docs/extended-session-length-for-workforce-identity-federation).

The following example shows how to create a session control that requires reauthentication every 18 hours with `LOGIN` and every two hours for a specific application (`SENSITIVE_APP_ID`) with `SECURITY_KEY`.

**Default settings**

The `--level`, `--session-length`, and `--session-reauth-method` flags in the Google Cloud CLI command (or the corresponding fields in the JSON body for the API call) set the default behavior for all applications not explicitly defined in `scopedAccessSettings`.

**Application-specific settings**

The `scopedAccessSettings` section in the YAML file (or JSON body) lets you override the default settings for specific applications. In the example, we set a two hour reauthentication requirement with `SECURITY_KEY` for the application with the client ID `SENSITIVE_APP_ID`.

Application-specific settings in `scopedAccessSettings` completely override the default (global) session controls. If a scoped setting is defined for an application, the default session controls do not apply to that application.

To exempt certain applications from session control when global controls are active, you must explicitly add them to `scopedAccessSettings` and set the `sessionLength` field to `0s` and `sessionLengthEnabled` to `false`.

###  gcloud 

The following example shows the session settings configuration:
    
    
    scopedAccessSettings:
    - scope:
        clientScope:
          restrictedClientApplication:
            clientId: SENSITIVE_APP_ID
      activeSettings:
        sessionSettings:
          sessionLength: 7200s
          sessionReauthMethod: SECURITY_KEY
          sessionLengthEnabled: true
    

Create the access binding:
    
    
    gcloud access-context-manager cloud-bindings create \
        --organization=ORG_ID \
        --group-key=GROUP_ID \
        --binding-file=BINDING_FILE_PATH \
        --session-length=SESSION_LENGTH \
        --session-reauth-method LOGIN
    

Replace the following:

  * `ORG_ID`: the ID of the Google Cloud organization

  * `GROUP_ID`: the unique Cloud Identity group ID

  * `BINDING_FILE_PATH`: the path of the binding file

  * `SESSION_LENGTH`: the session length—for example, `18h`




To obtain the unique group ID, run the following command:
    
    
    gcloud identity groups describe GROUP_EMAIL
    

Replace `GROUP_EMAIL` with your group's email address. The unique group ID is the value returned after `groups/` in the `name` field in the output. For example, the unique group ID in `groups/01gf8i8311xalqg` is `01gf8i8311xalqg`.

###  REST API 

An example JSON body of the API request:
    
    
    {
      "groupKey": "GROUP_ID",
      "sessionSettings": {
        "sessionLength": "64800s",
        "sessionReauthMethod": "LOGIN",
        "sessionLengthEnabled": true
      },
      "scopedAccessSettings": [
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "clientId": "SENSITIVE_APP_ID"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
              "sessionLength": "7200s",
              "sessionReauthMethod": "SECURITY_KEY",
              "sessionLengthEnabled": true
            }
          }
        }
      ]
    }
    
    

Construct the POST request in the following format:
    
    
    POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
    

Replace `ORG_ID` with the ID of the Google Cloud organization.

###  Terraform 

To specify session controls that apply globally and to specific applications, set the `session_settings` and `scoped_access_settings` arguments:
    
    
        resource "google_access_context_manager_gcp_user_access_binding" "gcp_user_access_binding" {
          organization_id = "ORG_ID"
          group_key = "GROUP_ID"
          session_settings {
            session_length = "64800s"
            session_length_enabled = true
            session_reauth_method = "LOGIN"
            use_oidc_max_age = false
          }
          scoped_access_settings {
            scope {
              client_scope {
                restricted_client_application {
                  client_id = "CLIENT_ID"
                }
              }
            }
            active_settings {
              session_settings {
                session_length = "7200s"
                session_length_enabled = true
                session_reauth_method = "SECURITY_KEY"
                use_oidc_max_age = false
              }
            }
          }
        }
    

Replace the following:

  * `ORG_ID`: the numeric ID of the Google Cloud organization.

  * `GROUP_ID`: the raw Cloud Identity or Google Workspace Directory API group ID. Don't use a group email address or a `"groups/..."` resource name. Instead, pass the raw ID or use `trimprefix(google_cloud_identity_group.example.id, "groups/")`.

  * `CLIENT_ID`: the OAuth 2.0 client ID of the application.




## Example policy configuration for Google Cloud applications

You can configure application-specific reauthentication controls for Google Cloud applications, for example requiring `SECURITY_KEY` for Google Cloud SDK and `LOGIN` for the Google Cloud console. The following example shows how to create a session control that requires reauthentication every hour for Google Cloud SDK with `SECURITY_KEY`, and every 4 hours for the Google Cloud console with `LOGIN`.

The `scopedAccessSettings` section in the YAML file (or JSON body) lets you override the default settings for specific applications. In this example, we set a one hour reauthentication requirement with `SECURITY_KEY` for Google Cloud SDK, and a four hour reauthentication requirement with `LOGIN` for the Google Cloud console using the `name` field to identify these applications.

To exempt certain applications from session control, set the `sessionLength` field to `0s` or `sessionLengthEnabled` to `false`. The `sessionReauthMethod` method will then be ignored.

###  gcloud 

The following example shows the session settings configuration:
    
    
    scopedAccessSettings:
    - scope:
        clientScope:
          restrictedClientApplication:
            name: Google Cloud SDK
      activeSettings:
        sessionSettings:
          sessionLength: 3600s
          sessionReauthMethod: SECURITY_KEY
          sessionLengthEnabled: true
    - scope:
        clientScope:
          restrictedClientApplication:
            name: Cloud Console
      activeSettings:
        sessionSettings:
          sessionLength: 14400s
          sessionReauthMethod: LOGIN
          sessionLengthEnabled: true
    

Create the access binding:
    
    
    gcloud access-context-manager cloud-bindings create \
        --organization=ORG_ID \
        --group-key=GROUP_ID \
        --binding-file=BINDING_FILE_PATH
    

Replace the following:

  * `ORG_ID`: the ID of the Google Cloud organization

  * `GROUP_ID`: the unique Cloud Identity group ID

  * `BINDING_FILE_PATH`: the path of the binding file




###  REST API 

An example JSON body of the API request:
    
    
    {
      "groupKey": "GROUP_ID",
      "scopedAccessSettings": [
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "Google Cloud SDK"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
                "sessionLength": "3600s",
                "sessionReauthMethod": "SECURITY_KEY",
                "sessionLengthEnabled": true
              }
          }
        },
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "Cloud Console"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
                "sessionLength": "14400s",
                "sessionReauthMethod": "LOGIN",
                "sessionLengthEnabled": true
              }
          }
        }
      ]
    }
    

Construct the POST request in the following format:
    
    
    POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
    

Replace `ORG_ID` with the ID of the Google Cloud organization.

###  Terraform 

To specify session length settings for Google Cloud SDK and the Google Cloud console, set the appropriate `scoped_access_settings` argument:
    
    
        resource "google_access_context_manager_gcp_user_access_binding" "gcp_user_access_binding" {
          organization_id = "ORG_ID"
          group_key = "GROUP_ID"
          scoped_access_settings {
            scope {
              client_scope {
                restricted_client_application {
                  name = "Google Cloud SDK"
                }
              }
            }
            active_settings {
              session_settings {
                session_length = "3600s"
                session_length_enabled = true
                session_reauth_method = "SECURITY_KEY"
                use_oidc_max_age = false
              }
            }
          }
          scoped_access_settings {
            scope {
              client_scope {
                restricted_client_application {
                  name = "Cloud Console"
                }
              }
            }
            active_settings {
              session_settings {
                session_length = "14400s"
                session_length_enabled = true
                session_reauth_method = "LOGIN"
                use_oidc_max_age = false
              }
            }
          }
        }
    

Replace the following:

  * `ORG_ID`: the numeric ID of the Google Cloud organization.

  * `GROUP_ID`: the raw Cloud Identity or Google Workspace Directory API group ID. Don't use a group email address or a `"groups/..."` resource name. Instead, pass the raw ID or use `trimprefix(google_cloud_identity_group.example.id, "groups/")`.




## Override the default 16-hour session length for Google Cloud applications

Starting in June 2026, a default session length of 16 hours was introduced for a subset of Google Cloud organizations. This default policy isn't visible in the Google Admin console and affected Google Cloud organizations must use the Access Context Manager API to override it for their users.

To override this default policy and exempt these applications from session control (making the session length effectively infinite), you can create a cloud binding with `scopedAccessSettings` where `sessionLengthEnabled` is set to `false` for both the Google Cloud SDK and Google Cloud console ("Cloud Console") applications.

**Note:** The following example shows how to configure an override to disable reauthentication (revert to pre existing behavior) for Google Cloud SDK and Google Cloud console users. However, any `sessionSettings` configuration within `scopedAccessSettings.activeSettings` for the Google Cloud SDK and Google Cloud console applications will override the default value for the users within the specified Google Group:

###  gcloud 

The following example shows the YAML configuration to disable session controls for these applications:
    
    
    scopedAccessSettings:
    - scope:
        clientScope:
          restrictedClientApplication:
            name: Google Cloud SDK
      activeSettings:
        sessionSettings:
          sessionLength: 0s
          sessionReauthMethod: LOGIN
          sessionLengthEnabled: false
    - scope:
        clientScope:
          restrictedClientApplication:
            name: Cloud Console
      activeSettings:
        sessionSettings:
          sessionLength: 0s
          sessionReauthMethod: LOGIN
          sessionLengthEnabled: false
    

Create or update the access binding using this file:
    
    
    gcloud access-context-manager cloud-bindings create \
        --organization=ORG_ID \
        --group-key=GROUP_ID \
        --binding-file=BINDING_FILE_PATH
    

Replace the following:

  * `ORG_ID`: the ID of the Google Cloud organization

  * `GROUP_ID`: the unique Cloud Identity group ID (for example, the ID of a group that contains all the users that you want this override to apply to)

  * `BINDING_FILE_PATH`: the path of the binding file




###  REST API 

An example JSON body of the API request:
    
    
    {
      "groupKey": "GROUP_ID",
      "scopedAccessSettings": [
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "Google Cloud SDK"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
              "sessionLength": "0s",
              "sessionReauthMethod": "LOGIN",
              "sessionLengthEnabled": false
            }
          }
        },
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "Cloud Console"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
              "sessionLength": "0s",
              "sessionReauthMethod": "LOGIN",
              "sessionLengthEnabled": false
            }
          }
        }
      ]
    }
    

Construct the POST request in the following format:
    
    
    POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
    

Replace `ORG_ID` with the ID of the Google Cloud organization.

###  Terraform 

To specify that session controls are disabled for Google Cloud SDK and the Google Cloud console, set the appropriate `scoped_access_settings` argument with `session_length_enabled = false`:
    
    
        resource "google_access_context_manager_gcp_user_access_binding" "gcp_user_access_binding" {
          organization_id = "ORG_ID"
          group_key = "GROUP_ID"
          scoped_access_settings {
            scope {
              client_scope {
                restricted_client_application {
                  name = "Google Cloud SDK"
                }
              }
            }
            active_settings {
              session_settings {
                session_length = "0s"
                session_length_enabled = false
                session_reauth_method = "LOGIN"
                use_oidc_max_age = false
              }
            }
          }
          scoped_access_settings {
            scope {
              client_scope {
                restricted_client_application {
                  name = "Cloud Console"
                }
              }
            }
            active_settings {
              session_settings {
                session_length = "0s"
                session_length_enabled = false
                session_reauth_method = "LOGIN"
                use_oidc_max_age = false
              }
            }
          }
        }
    

Replace the following:

  * `ORG_ID`: the numeric ID of the Google Cloud organization.

  * `GROUP_ID`: the raw Cloud Identity or Google Workspace Directory API group ID. Don't use a group email address or a `"groups/..."` resource name. Instead, pass the raw ID or use `trimprefix(google_cloud_identity_group.example.id, "groups/")`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
