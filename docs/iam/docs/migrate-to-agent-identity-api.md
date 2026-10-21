---
url: https://docs.cloud.google.com/iam/docs/migrate-to-agent-identity-api/
title: Migrate to Agent Identity API \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:06.555440+00:00
---

# Migrate to Agent Identity API  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/migrate-to-agent-identity-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Migrate to Agent Identity API Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to migrate your deployed agents and auth providers from the legacy IAM Connectors API (`iamconnectors.googleapis.com`) to the new Agent Identity API (`agentidentity.googleapis.com`).

Both APIs operate side-by-side during the preview migration period, allowing you to migrate your workloads without interrupting existing agent conversations.

The migration workflow includes the following tasks:

  1. Enable the Agent Identity API
  2. Update IAM allow policies
  3. Update your agent code and SDKs
  4. Disable the legacy API



## Enable the Agent Identity API

To start the migration, enable the new Agent Identity API in your project.

Enable the Agent Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=agentidentity.googleapis.com)

When you enable the Agent Identity API, the Agent Registry page in the Google Cloud console switches to the new API to read and write resources:

  * **You don't need to recreate your auth providers.** The new API mirrors each legacy auth provider (for example, `projects/PROJECT_ID/locations/LOCATION/**connectors** /AUTH_PROVIDER_NAME`) as an `**authProviders**` resource (`projects/PROJECT_ID/locations/LOCATION/**authProviders** /AUTH_PROVIDER_NAME`).

  * A newly created auth provider using the Google Cloud console or the gcloud CLI appears as an `authProviders/` resource and isn't visible in the legacy API.

  * The active agents using legacy `connectors/` strings continue to work during the migration window.




## Update IAM allow policies

Grant the new IAM roles on mirrored auth provider resources so that your agents can retrieve credentials from the new API endpoints.

For example, if you granted the **Connector User** (`roles/iamconnectors.user`) role to your agent's SPIFFE ID on the legacy `**connectors** /AUTH_PROVIDER_NAME` resource, grant the **Agent Identity User** (`roles/agentidentity.user`) role on the new `**authProviders** /AUTH_PROVIDER_NAME` resource:
    
    
    gcloud agent-identity auth-providers add-iam-policy-binding \
        AUTH_PROVIDER_NAME \
        --project="PROJECT_ID" \
        --location="LOCATION" \
        --role="roles/agentidentity.user" \
        --member="principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/ENGINE_ID"

If you test your agent locally using `adk web`, grant `roles/agentidentity.user` to your personal user account (`user:USER_EMAIL`).

## Update your agent code and SDKs

Update your agent code to reference the new `authProviders/` resource hierarchy and endpoints:

  1. Update your ADK version in your agent code to **2.3.0** or higher.

  2. In your agent code (for example, `agent.py`), replace `connectors/` with `authProviders/` in the `GcpAuthProviderScheme` resource string.

**Legacy configuration** : 
         
         auth_scheme = GcpAuthProviderScheme(
             name="projects/PROJECT_ID/locations/LOCATION/**connectors** /AUTH_PROVIDER_NAME"
         )

**New configuration** : 
         
         auth_scheme = GcpAuthProviderScheme(
             name="projects/PROJECT_ID/locations/LOCATION/**authProviders** /AUTH_PROVIDER_NAME"
         )

  3. 3-legged OAuth only: If your agent calls the REST API directly, update the endpoint hostname from `iamconnectorcredentials.googleapis.com` to `agentidentitycredentials.googleapis.com`, and replace `connectors/` with `authProviders/` in the request path.

  4. 3-legged OAuth only: In your frontend validation server (for example, `main.py`), update the `FinalizeCredentials` endpoint URL to `https://agentidentitycredentials.googleapis.com/v1`. Also, read the `auth_provider_name` from the incoming request and set it as the `auth_provider` field in the `FinalizeCredentials` request body.




## Disable the legacy API

After you update your IAM allow policies and deploy your agent code, verify that your agent authenticates and retrieves credentials using the new API.

After you migrate all active workflows, disable the legacy service in your project:
    
    
    gcloud services disable iamconnectors.googleapis.com \
        --project="PROJECT_ID"

## What's next

  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2)
  * [Agent Identity locations](https://docs.cloud.google.com/iam/docs/agent-identity-locations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
