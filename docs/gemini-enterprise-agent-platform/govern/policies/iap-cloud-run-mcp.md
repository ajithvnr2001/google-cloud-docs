---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp/
title: Authenticate your Cloud Run MCP server with IAP \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:52.272368+00:00
---

# Authenticate your Cloud Run MCP server with IAP  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Authenticate your Cloud Run MCP server with IAP Stay organized with collections  Save and categorize content based on your preferences. 

Identity-Aware Proxy (IAP) lets you secure Model Context Protocol (MCP) servers deployed on Cloud Run with centralized identity verification. You can then configure clients such as the Gemini CLI or AI agents to authenticate through IAP and securely run tools on your remote server.

## Before you begin

  1. Verify that you have the required roles.

  2. Enable Cloud Run in your project.

  3. Enable IAP in your project.

  4. [Deploy an MCP server on Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server).




### Required roles

To get the permissions that you need to configure IAP authentication for Cloud Run MCP servers, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the project
  * [IAP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`) on the project
  * Deploy a new service or deploy a new revision of an existing service: 
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the runtime service account
    * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the container image repository
  * Create and configure an OAuth client: [OAuth Config Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`) on the project 
  * Connect to or call the IAP-secured MCP server: [IAP-secured Web App User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.httpsResourceAccessor) (`roles/iap.httpsResourceAccessor`) on the project or Cloud Run service 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure IAP on a Cloud Run service

To configure IAP on your Cloud Run MCP server, do the following:

  1. Grant the Cloud Run Invoker role (`roles/run.invoker`) to the IAP service agent:
         
         gcloud beta run services add-iam-policy-binding SERVICE_NAME \
             --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-iap.iam.gserviceaccount.com' \
             --role='roles/run.invoker'
         

Replace the following:

     * `SERVICE_NAME`: the service name
     * `PROJECT_NUMBER`: your Google Cloud project number
  2. Enable IAP when you deploy a new service or deploy a new revision of an existing service:

### New service

To deploy a new service with IAP enabled, run the [`gcloud beta run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy) command:
         
         gcloud beta run deploy SERVICE_NAME \
           --image=CONTAINER_IMAGE \
           --region=REGION \
           --project=PROJECT_ID \
           --allow-unauthenticated \
           --iap \
           --functional-type=mcp-server
         

Replace the following:

     * `SERVICE_NAME`: the service name
     * `CONTAINER_IMAGE`: your container image
     * `REGION`: the region where you deploy your service
     * `PROJECT_ID`: the ID of the project where Cloud Run is enabled

### Existing service

To deploy a new revision of an existing service with IAP enabled, run the [`gcloud beta run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/services/update) command:
    
    gcloud beta run services update SERVICE_NAME \
      --region=REGION \
      --iap \
      --functional-type=mcp-server
    

Replace the following:

     * `SERVICE_NAME`: the service name
     * `REGION`: the region where you deploy your service

  3. Create and configure an OAuth client:

To register your OAuth client's universal client ID for use with IAP, see [Sharing OAuth clients for programmatic access](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients).

Record the following values:

     * OAuth client ID
     * OAuth client secret
     * Redirect URI
  4. To connect a client such as the Gemini CLI or your agent to your deployed MCP server, edit the `~/.gemini/settings.json` file.

Add the following configuration to your `settings.json` file:
         
         {
           "mcpServers": {
             "my_mcp_server": {
               "httpUrl": "https://SERVICE_URL",
               "oauth": {
                 "enabled": "true",
                 "clientId": "OAUTH_CLIENT_ID",
                 "clientSecret": "OAUTH_CLIENT_SECRET",
                 "scopes": [ "email", "openid" ],
                 "redirectUri": "REDIRECT_URI"
               }
             }
           }
         }
         

Replace the following:

     * `SERVICE_URL`: your Cloud Run service URL
     * `OAUTH_CLIENT_ID`: the client ID from the OAuth client configuration
     * `OAUTH_CLIENT_SECRET`: the client secret from the OAuth client configuration
     * `REDIRECT_URI`: the redirect URI from the OAuth client configuration



## Verify the connection

To verify that your client can authenticate through IAP and connect to the MCP server, do the following:

  1. In your terminal, start the Gemini CLI:
         
         gemini
         

  2. When prompted in your browser, complete the IAP authentication flow.

  3. Verify that the Gemini CLI successfully discovers and lists the tools provided by your MCP server.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
