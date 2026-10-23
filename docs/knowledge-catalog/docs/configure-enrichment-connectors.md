---
url: https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-connectors/
title: Configure external connectors for enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:59.926106+00:00
---

# Configure external connectors for enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-connectors/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Configure external connectors for enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Third-party auth providers let you securely connect Knowledge Studio enrichment tasks to external platforms like GitHub, Microsoft SharePoint, and Atlassian Confluence. Complete the credential generation and auth provider configuration steps in this document as part of your prerequisite setup.

## Before you begin

Before configuring external connectors, ensure that you have completed the following prerequisites:

  * Review the overall enrichment configuration workflow in [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites).
  * Ensure you have the necessary administrator or developer permissions in your target third-party platforms (GitHub, Microsoft SharePoint, or Atlassian Confluence) to generate access tokens or register applications.
  * To securely store credentials and attach them to tasks, ensure you have properly configured the Agent Identity service. For more information, see [Set up IAM permissions for auth providers](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#setup-iam-permissions).



When connecting the enrichment agent to third-party knowledge sources, you must use the Google Cloud Agent Identity service. Agent Identity acts as an auth manager that securely stores your third-party credentials and provisions short-lived access tokens to the enrichment agent so that human operators never have to directly manage raw client secrets during task execution.

## Configure GitHub

To connect Knowledge Studio to GitHub repositories, you must create a fine-grained Personal Access Token (PAT) in GitHub and store it in an API key auth provider.

  1. Sign in to [GitHub](https://github.com/), click your profile photo, and click **Settings**.
  2. Go to **Developer settings** > **Personal access tokens** > **Fine-grained tokens**.
  3. Click **Generate new token**.
  4. Configure the token properties: 
     * **Token name** : Enter a descriptive name (for example, `enrichment-agent`).
     * **Expiration** : Set an appropriate expiration date.
     * **Resource owner** : Select the organization or user account that owns the target repositories.
     * **Repository access** : Select **Only select repositories** and choose the repositories you want to enrich.
     * **Permissions** : Grant specific **Read** or **Read and Write** access for the required scopes (such as **Issues** , **Pull Requests** , and **Contents**).
  5. Click **Generate token** and copy the token safely.
  6. Register an API key auth provider in Google Cloud and supply the PAT as the API key. See [Authenticate using an API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2#create-connector).



For more information about creating a PAT, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in the GitHub documentation.

## Configure Microsoft SharePoint

If you are connecting to Microsoft SharePoint, obtain OAuth credentials from Microsoft Entra ID (formerly Azure Active Directory) using a 2-Legged OAuth flow.

  1. Register a new application in the [Microsoft Entra admin center](https://entra.microsoft.com/).
  2. Grant Microsoft Graph API permissions: 
     1. Go to **API permissions** > **Add a permission** > **Microsoft Graph** > **Application permissions** (do not select Delegated permissions).
     2. Add the `Sites.Read.All` and `Files.Read.All` scopes.
     3. Click **Grant admin consent** for your tenant so both Application permissions show as "Granted".
  3. Create a new client secret. Record its value immediately, as it is only shown once. For more information, see [Create a new client secret](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret).

  4. Copy your application configuration values. After registration, collect the following values for your auth provider configuration:

     * **Client ID** : The Application (client) ID from your app overview.
     * **Token URL** : While on the **Overview** page, click the **Endpoints** tab. Copy the URL labeled **OAuth 2.0 token endpoint (v2)**.
  5. Register a 2-legged OAuth auth provider in Google Cloud using these secrets. When creating the provider, supply the default scope to the `--allowed-scopes` parameter:
         
         --allowed-scopes="https://graph.microsoft.com/.default"
         

For more information, see [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft Entra documentation.




## Configure Atlassian Confluence

Because Confluence does not support 2-Legged OAuth for server-to-server agents, you must create a dedicated service account (or dummy user account) in Atlassian, grant it the required permissions, and generate a PAT.

  1. Sign in to the specific service account in [Confluence](https://confluence.atlassian.com/).
  2. Click your **Profile picture** in the top-right corner of the screen.
  3. Select **Settings** (or **Account settings**) from the menu.
  4. In the Security tab, navigate to the API tokens section.
  5. Click the **Create API token with scopes** button. Don't use an unscoped token because it won't fetch all the required tools.
  6. Provide a descriptive name (for example, `enrichment-agent`), configure the expiration date, and click **Next**.
  7. In the **Select the app** list, select the **Atlassian MCP** option and click **Next**.
  8. Select all of the following Confluence read and search scopes: 
     * `read:page:confluence`
     * `read:space:confluence`
     * `search:confluence`
     * `read:confluence-content.all`
     * `read:confluence-content.summary`
     * `read:confluence-space.summary`
     * `search:rovo:mcp`
     * `read:jira-work`
  9. Click **Next** , and then click **Create**.
  10. Copy the generated token.
  11. Format the credential string for the Google Cloud auth provider as `<ATLASSIAN_EMAIL>:<API_TOKEN>`. Atlassian requires HTTP basic authentication encoding (`email:api_token`) to use the personal API tokens programmatically.
  12. Register an API key auth provider in Google Cloud and supply the `<ATLASSIAN_EMAIL>:<API_TOKEN>` string as the API key. See [Authenticate using an API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2#create-connector).



For more information about creating a PAT, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) in the Atlassian documentation.

## What's next

  * Learn how to [create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
