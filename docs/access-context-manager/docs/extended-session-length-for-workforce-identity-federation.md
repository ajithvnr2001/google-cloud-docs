---
url: https://docs.cloud.google.com/access-context-manager/docs/extended-session-length-for-workforce-identity-federation/
title: Configure Extended Session Length for Workforce Identity Federation \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:51.009042+00:00
---

# Configure Extended Session Length for Workforce Identity Federation  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/extended-session-length-for-workforce-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configure Extended Session Length for Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Extended session length for Workforce Identity Federation is in [Preview](https://cloud.google.com/products#product-launch-stages) for Looker (Google Cloud core) and the Gemini Enterprise mobile app. Extended session length for the Gemini Enterprise mobile app is available by allowlist only. To request access to the allowlist during Preview, contact your Google Cloud Support point of contact (POC).

By default, Workforce Identity Federation sessions have a maximum duration of 12 hours. Extended session length lets organizations configure long-lasting sessions of up to 90 days for Looker (Google Cloud core) and the Gemini Enterprise mobile app:

  * **Looker (Google Cloud core)** : Configured using project scopes (`restricted_project`). Extended sessions allow workforce users to maintain an uninterrupted connection to Looker (Google Cloud core) without requiring daily reauthentication against your external identity provider (IdP). User interaction within Looker (Google Cloud core) remains governed by your Looker (Google Cloud core) session length configuration.

  * **The Gemini Enterprise mobile app** : Configured using application scopes (`restricted_client_application`). Extended sessions allow workforce users to maintain an uninterrupted connection to the Gemini Enterprise mobile app without requiring daily reauthentication against your external identity provider (IdP).




To maintain security throughout extended sessions, Google Cloud periodically synchronizes user attributes and group memberships directly from your external identity provider (IdP) in the background.

This document describes how to define extended session policies using the Access Context Manager API with project-scoped controls (for Looker (Google Cloud core)) and application-scoped controls (for the Gemini Enterprise mobile app), configure your workforce pool provider, and manage active bindings.

* * *

## Overview

Workforce Identity Federation uses Access Context Manager Google Cloud access bindings to configure extended session length:

  * **Google Cloud access binding** : Administrators define a session length policy using Access Context Manager that applies organization-wide across all workforce pools in your organization. Policies grant extended sessions of up to 90 days using either one of the following:

    * **Project scope (`restricted_project`)**: Applies extended sessions to Looker (Google Cloud core) instances in the designated project.

    * **Application scope (`restricted_client_application`)**: Applies extended sessions to the Gemini Enterprise mobile app.

  * **Background attribute synchronization** :

    * **OIDC** : Supported using either an OIDC Authorization Code flow with the `offline_access` scope (using refresh tokens to periodically refresh user attributes and group memberships from your external IdP in the background) or through SCIM provisioning.

    * **SAML** : For SAML providers, user attributes and group memberships are kept up-to-date using SCIM provisioning.

  * **Staleness protection** : If user attributes cannot be refreshed from the external IdP within 24 hours (for example, if the user is deprovisioned or credentials are revoked at the IdP), Google Cloud terminates the session.




* * *

## Before you begin

Before configuring extended session length, ensure you have the required Identity and Access Management permissions and APIs enabled:

### Required roles and permissions

To get the permissions that you need to configure extended session length, ask your administrator to grant you the following IAM roles:

  * **Configure workforce identity pool providers** : [Workforce Pool Admin (`roles/iam.workforcePoolAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) on the workforce pool or organization.
  * **Manage Access Context Manager cloud access bindings** : [Cloud Access Binding Admin (`roles/accesscontextmanager.gcpAccessAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) at the organization level. This role provides the permissions required to create, view, update, and delete Access Context Manager access bindings.



### Enable APIs

Enable the Access Context Manager and IAM APIs in your project:
    
    
    gcloud services enable \
        accesscontextmanager.googleapis.com \
        iam.googleapis.com
    

* * *

## Limitations and Requirements

Before configuring extended session length, review the following requirements and limitations:

  * **Supported applications** : Extended session length applies exclusively to the following: 
    * **Looker (Google Cloud core)** (configured using project scopes)
    * **The Gemini Enterprise mobile app** (configured using application scopes)
  * **Allowlist requirement for the Gemini Enterprise mobile app** : Extended session length for the Gemini Enterprise mobile app is available by allowlist only. To request access to the allowlist during Preview, contact your Google Cloud Support point of contact (POC).
  * **Scope types** : Session settings must be configured within `scopedAccessSettings` using one of the following client scopes: 
    * **Project scope (`restricted_project`)**: Specifies the Google Cloud project that owns the Looker (Google Cloud core) instance (`projects/{PROJECT_NUMBER}`). Only Looker (Google Cloud core) instances owned by the designated project are affected.
    * **Application scope (`restricted_client_application`)**: Specifies the application by its canonical display **`name`**.
    * To configure application scopes for the Gemini Enterprise mobile app, you must explicitly use one or both of the following exact application names: 
      * `"Gemini Enterprise mobile Android"`
      * `"Gemini Enterprise mobile IOS"`
    * Scoping by OAuth client ID (`clientId`) is **not supported** for Workforce Identity Federation bindings and will be rejected. You must identify the application using the `name` field.
  * **Session duration range** : Session duration must be between a minimum of **1 hour** (`3600s`) and a maximum of **90 days** (`7776000s`).
  * **Session settings parameter requirements** : 
    * `session_length_enabled`: Must be set to `true`.
    * `session_length`: Required duration between 1 hour (`3600s`) and 90 days (`7776000s`).
    * `session_reauth_method`: Must be unset or set to `LOGIN`.
    * `use_oidc_max_age`: Must be unset or set to `false`.
    * `max_inactivity`: Must be unset (or default `0s`). Idle session timeouts are not supported for `restricted_project` bindings and `restricted_client_application` bindings.
  * **Supported identity providers** : 
    * **OIDC** : Requires an OIDC provider configured with **Authorization Code Flow** and the **`offline_access`** scope to issue refresh tokens, or configured with **SCIM provisioning**.
    * **SAML 2.0** : Requires **SCIM provisioning** enabled on the workforce pool provider.
  * **Attribute staleness threshold** : A fixed **24-hour staleness threshold** is enforced. If Google Cloud cannot refresh user attributes from your IdP within 24 hours, the session is invalidated and the user must reauthenticate.
  * **Access Context Manager constraints** : 
    * **Single organizational binding** : Extended session length bindings for workforce pools must target the organization's "all workforce pools" principal (`principalSet://cloudresourcemanager.googleapis.com/organizations/{ORG_ID}/type/WorkforcePool`). Because this federated principal identifier applies organization-wide across all workforce pools in your organization, only one such binding can exist per organization. To configure extended sessions for multiple Looker (Google Cloud core) projects, the Gemini Enterprise mobile app, or a combination of both, include multiple `restricted_project` and `restricted_client_application` scope blocks within the single binding's `scopedAccessSettings` list.
    * **Access levels** (`access_levels`, `dry_run_access_levels`) are **not supported** on workforce pool bindings.
    * Top-level `sessionSettings` directly on the `GcpUserAccessBinding` are **not supported** for workforce pool bindings; settings must be defined within `scopedAccessSettings.activeSettings.sessionSettings`.



* * *

## Configure the workforce pool provider

To allow extended session length, your workforce pool provider must be configured to support background attribute refresh. You can configure the provider to use either the OIDC or SAML protocol.

### Configure an OIDC provider

Background attribute refresh for OIDC providers can be handled using either refresh tokens (`offline_access` scope) or SCIM provisioning. If using token-based attribute refresh:

  1. In your external IdP, configure an OIDC application with **Authorization Code Flow** and enable **Offline Access** so that a refresh token is returned.
  2. In Google Cloud, add `offline_access` to the additional scopes on your OIDC workforce pool provider.



Offline access must be configured on all workforce identity pools in your Google Cloud organization for the extended session length policy to have the intended effect.

**Warning:** If offline access is not configured for every workforce pool in the organization, federated users belonging to pools without offline access may be logged out earlier than the duration specified by the extended session length policy.

###  gcloud 

If your provider already has existing additional scopes, include them alongside `offline_access` so they are not overwritten:
    
    
    gcloud iam workforce-pools providers update-oidc PROVIDER_ID \
        --workforce-pool=WORKFORCE_POOL_NAME \
        --location=global \
        --web-sso-additional-scopes="offline_access[,EXISTING_ADDITIONAL_SCOPES]"
    

Replace the following:

  * `PROVIDER_ID`: The name of your workforce identity pool provider.
  * `WORKFORCE_POOL_NAME`: The name of your workforce identity pool.
  * `EXISTING_ADDITIONAL_SCOPES`: Any comma-separated additional scopes previously configured on the provider. If you have no existing additional scopes, omit this parameter.



###  REST API 

Send a `PATCH` request to update the provider. Include any existing additional scopes alongside `offline_access`:
    
    
    PATCH https://iam.googleapis.com/v1/locations/global/workforcePools/WORKFORCE_POOL_NAME/providers/PROVIDER_ID?updateMask=oidc.webSsoConfig.additionalScopes
    

Request body:
    
    
    {
      "oidc": {
        "webSsoConfig": {
          "additionalScopes": [
            "offline_access"
          ]
        }
      }
    }
    

Replace the following:

  * `WORKFORCE_POOL_NAME`: The name of your workforce identity pool.
  * `PROVIDER_ID`: The ID of your workforce identity pool provider.



### Configure a SAML provider

For SAML providers, background attribute refresh requires SCIM provisioning:

  1. Set up a SCIM tenant for your workforce pool provider.
  2. Configure user and group provisioning from your SAML identity provider to the SCIM endpoint.



For step-by-step instructions, see [SCIM provisioning for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim).

* * *

## Example policy configuration for Looker (Google Cloud core)

Create a `GcpUserAccessBinding` resource that assigns the extended session length policy to your organization's workforce pool, scoping the policy to the project hosting your Looker (Google Cloud core) instance.

**Note:** Because the federated principal `principalSet://cloudresourcemanager.googleapis.com/organizations/ORG_ID/type/WorkforcePool` applies to all workforce pools in an organization, only one binding of this type is allowed per organization. If an access binding already exists for your organization, update that binding to add new `restricted_project` scopes as needed.

###  gcloud 

Define the policy in a YAML file named `esl-binding.yaml`:
    
    
    scopedAccessSettings:
    - scope:
        clientScope:
          restrictedProject:
            name: projects/PROJECT_NUMBER
      activeSettings:
        sessionSettings:
          sessionLength: 7776000s
          sessionLengthEnabled: true
          sessionReauthMethod: LOGIN
    

Create the access binding:
    
    
    gcloud access-context-manager cloud-bindings create \
        --organization=ORG_ID \
        --federated-principal="principalSet://cloudresourcemanager.googleapis.com/organizations/ORG_ID/type/WorkforcePool" \
        --binding-file="esl-binding.yaml"
    

Replace the following:

  * `ORG_ID`: Your Google Cloud organization ID (for example, `123456789012`).
  * `PROJECT_NUMBER`: The project number that owns the target Looker (Google Cloud core) instance (for example, `987654321098`). Only Looker (Google Cloud core) applications owned by this project receive the extended session length.
  * `sessionLength`: The session duration in seconds followed by `s`. For example, `7776000s` specifies a 90-day session.
  * `sessionLengthEnabled`: Set to `true`.
  * `sessionReauthMethod`: Set to `LOGIN` (or leave unset).



###  REST API 

Send a `POST` request to the Access Context Manager API:
    
    
    POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
    

JSON request body:
    
    
    {
      "principal": {
        "federatedPrincipal": "principalSet://cloudresourcemanager.googleapis.com/organizations/ORG_ID/type/WorkforcePool"
      },
      "scopedAccessSettings": [
        {
          "scope": {
            "clientScope": {
              "restrictedProject": {
                "name": "projects/PROJECT_NUMBER"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
              "sessionLength": "7776000s",
              "sessionLengthEnabled": true,
              "sessionReauthMethod": "LOGIN"
            }
          }
        }
      ]
    }
    

Replace the following:

  * `ORG_ID`: Your Google Cloud organization ID (for example, `123456789012`).
  * `PROJECT_NUMBER`: The project number that owns the target Looker (Google Cloud core) instance (for example, `987654321098`). Only Looker (Google Cloud core) applications owned by this project receive the extended session length.
  * `sessionLength`: The session duration in seconds followed by `s`. For example, `7776000s` specifies a 90-day session.
  * `sessionLengthEnabled`: Set to `true`.
  * `sessionReauthMethod`: Set to `LOGIN` (or leave unset).



## Example policy configuration for the Gemini Enterprise mobile app

Create a `GcpUserAccessBinding` resource that assigns the extended session length policy to your organization's workforce pool, scoping the policy to the Gemini Enterprise mobile app using the `restricted_client_application` scope. You must identify the applications using their exact canonical display names: `"Gemini Enterprise mobile Android"` and `"Gemini Enterprise mobile IOS"`.

**Note:** Because the federated principal `principalSet://cloudresourcemanager.googleapis.com/organizations/ORG_ID/type/WorkforcePool` applies to all workforce pools in an organization, only one binding of this type is allowed per organization. If an access binding already exists for your organization (for example, for Looker (Google Cloud core)), update that binding to add the `restricted_client_application` scopes instead of creating a new one.

###  gcloud 

Define the policy in a YAML file named `esl-app-binding.yaml`:
    
    
    scopedAccessSettings:
    - scope:
        clientScope:
          restrictedClientApplication:
            name: "Gemini Enterprise mobile Android"
      activeSettings:
        sessionSettings:
          sessionLength: 7776000s
          sessionLengthEnabled: true
          sessionReauthMethod: LOGIN
    - scope:
        clientScope:
          restrictedClientApplication:
            name: "Gemini Enterprise mobile IOS"
      activeSettings:
        sessionSettings:
          sessionLength: 7776000s
          sessionLengthEnabled: true
          sessionReauthMethod: LOGIN
    

Create the access binding:
    
    
    gcloud access-context-manager cloud-bindings create \
        --organization=ORG_ID \
        --federated-principal="principalSet://cloudresourcemanager.googleapis.com/organizations/ORG_ID/type/WorkforcePool" \
        --binding-file="esl-app-binding.yaml"
    

Replace the following:

  * `ORG_ID`: Your Google Cloud organization ID (for example, `123456789012`).
  * `name`: Must be `"Gemini Enterprise mobile Android"` or `"Gemini Enterprise mobile IOS"`. Identifying applications by OAuth client ID (`clientId`) is not supported for workforce pools.
  * `sessionLength`: The session duration in seconds followed by `s` (between `3600s` and `7776000s`).
  * `sessionLengthEnabled`: Set to `true`.
  * `sessionReauthMethod`: Set to `LOGIN` (or leave unset).



###  REST API 

Send a `POST` request to the Access Context Manager API:
    
    
    POST https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings
    

JSON request body:
    
    
    {
      "principal": {
        "federatedPrincipal": "principalSet://cloudresourcemanager.googleapis.com/organizations/ORG_ID/type/WorkforcePool"
      },
      "scopedAccessSettings": [
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "Gemini Enterprise mobile Android"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
              "sessionLength": "7776000s",
              "sessionLengthEnabled": true,
              "sessionReauthMethod": "LOGIN"
            }
          }
        },
        {
          "scope": {
            "clientScope": {
              "restrictedClientApplication": {
                "name": "Gemini Enterprise mobile IOS"
              }
            }
          },
          "activeSettings": {
            "sessionSettings": {
              "sessionLength": "7776000s",
              "sessionLengthEnabled": true,
              "sessionReauthMethod": "LOGIN"
            }
          }
        }
      ]
    }
    

Replace the following:

  * `ORG_ID`: Your Google Cloud organization ID (for example, `123456789012`).
  * `name`: Must be `"Gemini Enterprise mobile Android"` or `"Gemini Enterprise mobile IOS"`. Identifying applications by OAuth client ID (`clientId`) is not supported for workforce pools.
  * `sessionLength`: The session duration in seconds followed by `s`. For example, `7776000s` specifies a 90-day session.
  * `sessionLengthEnabled`: Set to `true`.
  * `sessionReauthMethod`: Set to `LOGIN` (or leave unset).



* * *

## Viewing and listing bindings

Because the binding applies across all workforce pools in the organization, there is at most one access binding per organization.

### List active bindings

To list the workforce pool access binding in your organization, use the `principal:federatedPrincipal` filter:

###  gcloud 
    
    
    gcloud access-context-manager cloud-bindings list \
        --organization=ORG_ID \
        --filter="principal:federatedPrincipal"
    

###  REST API 
    
    
    GET https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings?filter=principal:federated_principal
    

### Get binding details

To view the details of a specific workforce pool access binding:

###  gcloud 
    
    
    gcloud access-context-manager cloud-bindings describe \
        --binding=BINDING_NAME
    

Replace `BINDING_NAME` with the full resource name of the binding (for example, `organizations/123456789012/gcpUserAccessBindings/b1234567890`).

###  REST API 
    
    
    GET https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings/BINDING_ID
    

Replace the following:

  * `ORG_ID`: Your Google Cloud organization ID (for example, `123456789012`).
  * `BINDING_ID`: The ID of your access binding (for example, `b1234567890`).



* * *

## Update an access binding

You can update an existing workforce pool access binding to modify session lengths, add new project or application scopes, or remove existing scopes.

###  gcloud 

  1. Define the updated policy in a YAML file named `updated-esl-binding.yaml`:
         
         scopedAccessSettings:
         - scope:
             clientScope:
               restrictedProject:
                 name: projects/PROJECT_NUMBER
           activeSettings:
             sessionSettings:
               sessionLength: 2592000s
               sessionLengthEnabled: true
               sessionReauthMethod: LOGIN
         

  2. Apply the updated policy:

     * **Replace scoped access settings** : To overwrite the existing scopes with the configuration defined in `updated-esl-binding.yaml`:
    
    gcloud access-context-manager cloud-bindings update \
        --binding=BINDING_NAME \
        --binding-file="updated-esl-binding.yaml"
    

     * **Append to existing settings** : To append the scopes defined in `updated-esl-binding.yaml` to the binding's existing scopes without overwriting them, pass the `--append` flag:
    
    gcloud access-context-manager cloud-bindings update \
        --binding=BINDING_NAME \
        --binding-file="updated-esl-binding.yaml" \
        --append
    




Replace the following: * `BINDING_NAME`: The full resource name of the binding (for example, `organizations/123456789012/gcpUserAccessBindings/b1234567890`). * `PROJECT_NUMBER`: The project number that owns the target Looker (Google Cloud core) instance. * `sessionLength`: The updated session duration (for example, `2592000s` for 30 days).

###  REST API 

Send a `PATCH` request to update the binding.

  * **Replace scoped access settings** : To overwrite existing scopes:


    
    
    PATCH https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings/BINDING_ID?updateMask=scopedAccessSettings
    

  * **Append to existing settings** : To append new scopes without overwriting existing ones, set the `append=true` query parameter:


    
    
    PATCH https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings/BINDING_ID?updateMask=scopedAccessSettings&append=true
    

JSON request body:
    
    
    {
    "scopedAccessSettings": [
      {
        "scope": {
          "clientScope": {
            "restrictedProject": {
              "name": "projects/PROJECT_NUMBER"
            }
          }
        },
        "activeSettings": {
          "sessionSettings": {
            "sessionLength": "2592000s",
            "sessionLengthEnabled": true,
            "sessionReauthMethod": "LOGIN"
          }
        }
      }
    ]
    }
    

Replace the following: * `ORG_ID`: Your Google Cloud organization ID (for example, `123456789012`). * `BINDING_ID`: The ID of your access binding (for example, `b1234567890`). * `PROJECT_NUMBER`: The project number that owns the target Looker (Google Cloud core) instance. * `sessionLength`: The updated session duration (for example, `2592000s` for 30 days).

* * *

## Delete an access binding

If you delete the workforce pool access binding, extended session length is disabled for all workforce pools in your organization.

###  gcloud 
    
    
    gcloud access-context-manager cloud-bindings delete \
        --binding=BINDING_NAME
    

Replace `BINDING_NAME` with the full resource name of the binding.

###  REST API 

Send a `DELETE` request to remove the binding:
    
    
    DELETE https://accesscontextmanager.googleapis.com/v1/organizations/ORG_ID/gcpUserAccessBindings/BINDING_ID
    

Replace the following:

  * `ORG_ID`: Your Google Cloud organization ID.
  * `BINDING_ID`: The ID of the access binding to delete.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
