---
url: https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers/
title: Authenticate MCP servers \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:29.881328+00:00
---

# Authenticate MCP servers  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Authenticate MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Configure Agent Platform features for Cloud Run**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When your agent needs to connect to an MCP server or tool hosted on Cloud Run, you can secure the connection using built-in Identity and Access Management and Identity-Aware Proxy (IAP).

If you're connecting an agent running on Cloud Run to an MCP server on Cloud Run, see [Authenticate your AI agents](https://docs.cloud.google.com/run/docs/ai/authenticate-agents#authenticate-mcp-servers) for instructions on `run.invoker` policies.

## Developer CLI tools and clients to MCP server

To securely connect developer tools, local SDKs, and generic MCP clients to a private MCP server hosted on Cloud Run, we strongly recommend configuring Identity-Aware Proxy.

### Enable IAP

Enable IAP for your deployed Cloud Run MCP service:
    
    
    gcloud run services update MCP_SERVICE_NAME \
        --iap \
        --region=REGION

Replace the following:

  * `MCP_SERVICE_NAME`: the name of your MCP server service.
  * `REGION`: the region where your service is deployed.



### Grant access to the MCP server

Bind the calling agent's identity or a developer's user identity to the IAP invoker role on the backend service:
    
    
    gcloud iap web add-iam-policy-binding \
        --resource-type=cloud-run \
        --service=MCP_SERVICE_NAME \
        --member="PRINCIPAL" \
        --role="roles/iap.httpsResourceAccessor" \
        --region=REGION

Replace the following:

  * `MCP_SERVICE_NAME`: the name of your MCP server service.
  * `PRINCIPAL`: An identifier for the principals, or members, which usually has the following form: `PRINCIPAL`:`ID`. For example, `user:my-user@example.com`. For a full list of the values that `PRINCIPAL` can have, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).
  * `REGION`: the region where your service is deployed.



### Configure access with IAP

By default, IAP uses a Google-managed OAuth client that only supports browser-based user logins. To allow CLI tools and agents to access the MCP server programmatically, you must configure a Custom OAuth Client ID.

  1. Create an OAuth client in the Google Cloud console under **APIs and Services > Credentials**. Note the **Client ID** and **Client Secret**. 
     * If configuring for local developer tools like the [Antigravity CLI](https://antigravity.google/docs/cli/overview/), add `http://localhost:7777/oauth/callback` to your allowlisted redirection URLs.
  2. Add the OAuth client to the allowlist for programmatic access in your IAP settings by following the guide to [Share OAuth clients](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients#programmatic_access).



### Update client settings to connect

After setting up programmatic access, update your client configuration to supply the connection details and Custom OAuth Client ID credentials.

For example, to configure a tool like the Antigravity CLI to connect to your protected MCP server, update the `mcpServers` block in your settings:
    
    
    {
      "mcpServers": {
        "my-mcp-server": {
          "httpUrl": "https://my-mcp-server-<PROJECT_NUMBER>.<REGION>.run.app",
          "oauth": {
            "enabled": "true",
            "clientId": "YOUR_CUSTOM_OAUTH_CLIENT_ID",
            "clientSecret": "YOUR_CLIENT_SECRET",
            "scopes": [
              "email",
              "openid"
            ],
            "redirectUri": "http://localhost:7777/oauth/callback"
          }
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
