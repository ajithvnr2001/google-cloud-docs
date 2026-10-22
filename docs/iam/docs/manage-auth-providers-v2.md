---
url: https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2/
title: Manage Agent Identity auth providers \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:30.545528+00:00
---

# Manage Agent Identity auth providers  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Manage Agent Identity auth providers Stay organized with collections  Save and categorize content based on your preferences. 

In Agent Identity auth manager, you manage auth providers by editing their details, enabling or disabling them, or deleting and restoring them as needed.

**Important:** This document shows how to manage auth providers by using the Agent Identity API. We recommend using the Agent Identity API because the [IAM Connectors API](https://docs.cloud.google.com/iam/docs/manage-auth-providers) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) will not be [generally available](https://docs.cloud.google.com/products#product-launch-stages). If you are using the IAM Connectors API, then [migrate to the Agent Identity API](https://docs.cloud.google.com/iam/docs/migrate-to-agent-identity-api).

## Before you begin

  1. [Verify that you have chosen the correct authentication method](https://docs.cloud.google.com/iam/docs/agent-identity-overview#auth-models).
  2. Verify that you have the roles required to complete this task.



### Required roles

To get the permissions that you need to manage Agent Identity auth providers, ask your administrator to grant you the [Agent Identity Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage Agent Identity auth providers. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage Agent Identity auth providers:

  * `agentidentity.authProviders.update`
  * `agentidentity.authProviders.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Edit an auth provider

To update the description or authentication details of an auth provider, use the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Agent Registry** page.

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/agents)

  2. Click the name of the agent whose auth provider that you want to manage.
  3. Click **Identity**.
  4. In the **Auth Providers** section, find the auth provider that you want to manage.
  5. For your auth provider, click the **more_vert Actions** menu and select **Edit**.
  6. Update the description or authentication details as needed.
  7. Click **Save**.



### Google Cloud CLI

  1. To update an auth provider, run the following command:
         
         gcloud agent-identity auth-providers update AUTH_PROVIDER_NAME \
             --location="LOCATION" \
             --description="NEW_DESCRIPTION" \
             --three-legged-oauth-client-id="NEW_CLIENT_ID" \
             --three-legged-oauth-client-secret="NEW_CLIENT_SECRET" \
             --three-legged-oauth-authorization-url="NEW_ENDPOINT" \
             --three-legged-oauth-default-continue-uri="NEW_DEFAULT_CONTINUE_URI"

Replace the following:

     * `AUTH_PROVIDER_NAME`: The name of the auth provider.
     * `LOCATION`: The location of the auth provider.
     * `NEW_DESCRIPTION`: A new description for the auth provider.
     * `NEW_CLIENT_ID`: A new client ID from your third-party application.
     * `NEW_CLIENT_SECRET`: A new client secret from your third-party application.
     * `NEW_ENDPOINT`: A new URL of the third-party authorization server.
     * `NEW_DEFAULT_CONTINUE_URI`: Optional. A new default redirect URI where users are sent after granting consent.



## Enable or disable an auth provider

If you want to temporarily stop an agent from using an auth provider without deleting the auth provider, you can disable the auth provider. You can enable it again at any time.

### Console

  1. In the Google Cloud console, go to the **Agent Registry** page.

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/agents)

  2. Click the name of the agent whose auth provider that you want to manage.
  3. Click **Identity**.
  4. In the **Auth Providers** section, find the auth provider that you want to manage.
  5. For your auth provider, click **more_vert Actions** and select **Enable** or **Disable**.
  6. In the confirmation dialog, click **Enable** or **Disable**.



### Google Cloud CLI

  1. To enable an auth provider, run the following command:
         
         gcloud agent-identity auth-providers enable AUTH_PROVIDER_NAME \
             --location="LOCATION"

  2. To disable an auth provider, run the following command:
         
         gcloud agent-identity auth-providers disable AUTH_PROVIDER_NAME \
             --location="LOCATION"




Replace the following:

  * `AUTH_PROVIDER_NAME`: The name of the auth provider.
  * `LOCATION`: The location of the auth provider.



## Delete an auth provider

When you no longer need an auth provider, you can delete it. Deleting an auth provider disables it and places it in a soft-delete state for 30 days. During this period, you can restore the auth provider if you want to. After 30 days, it takes one additional day for its policy to be purged, at which point you can create an auth provider with the same name.

### Console

  1. In the Google Cloud console, go to the **Agent Registry** page.

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/agents)

  2. Click the name of the agent whose auth provider that you want to manage.
  3. Click **Identity**.
  4. In the **Auth Providers** section, find the auth provider that you want to manage.
  5. For your auth provider, click **more_vert Actions** and select **Delete**.
  6. In the confirmation dialog, click **Delete**.



### gcloud

  1. To delete an auth provider, run the following command:
         
         gcloud agent-identity auth-providers delete AUTH_PROVIDER_NAME \
             --location="LOCATION"




Replace the following:

  * `AUTH_PROVIDER_NAME`: The name of the auth provider.
  * `LOCATION`: The location of the auth provider.



## Restore a deleted auth provider

If you accidentally delete an auth provider, you can restore it from its soft-delete state within 30 days of deletion. During this period, you can restore the auth provider if you want to. After 30 days, it takes one additional day for its policy to be purged, at which point you can create an auth provider with the same name.

### Console

  1. In the Google Cloud console, go to the **Agent Registry** page.

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/agents)

  2. Click the name of the agent whose auth provider that you want to manage.
  3. Click **Identity**.
  4. In the **Auth Providers** section, find the auth provider that you want to manage.
  5. For your auth provider, click **more_vert Actions** and select **Restore**.
  6. In the confirmation dialog, click **Restore**.



### gcloud

  1. To restore an auth provider, run the following command:
         
         gcloud agent-identity auth-providers undelete AUTH_PROVIDER_NAME \
             --location="LOCATION"




Replace the following:

  * `AUTH_PROVIDER_NAME`: The name of the auth provider.
  * `LOCATION`: The location of the auth provider.



## What's next

  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2)
  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Agent Identity locations](https://docs.cloud.google.com/iam/docs/agent-identity-locations)
  * [Troubleshoot Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
