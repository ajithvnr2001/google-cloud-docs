---
url: https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers/
title: Set up authentication to Google and Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:02.072337+00:00
---

# Set up authentication to Google and Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Set up authentication to Google and Google Cloud MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

Google and Google Cloud Model Context Protocol (MCP) servers let you authenticate AI applications using either your own credentials or dedicated application credentials. You can configure the credential method that best matches your client's supported authentication flows and operational requirements. 

For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Limitations

Google and Google Cloud remote MCP servers don't support [Dynamic Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#dynamic-client-registration) or [OAuth Client ID Metadata Documents](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#client-id-metadata-documents).

## Before you begin

  1. [Enable the products](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) that you want to use through MCP in your Google Cloud project.

  2. Ensure that you, or the agent you're using to authenticate to the MCP server, have the required roles and permissions to make MCP calls and access the Google or Google Cloud resources.




### Required roles

[Non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers) don't require the MCP Tool User (`roles/mcp.toolUser`) role. You also can't use Identity and Access Management (IAM) policies or permissions to control access to non-Google Cloud MCP servers.

To get the permission that you need to make tool calls to Google Cloud MCP servers, ask your administrator to grant you the [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) IAM role on the Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `mcp.tools.call` permission, which is required to make tool calls to Google Cloud MCP servers. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To access Google Cloud products through MCP, your administrator must also grant you or your agent the required IAM roles for the accessed resources. See the documentation for the MCP server for the required roles or access for specific actions.

## Authentication methods

Most applications that can connect to MCP servers offer a way to add authentication, but not all Google authentication methods are supported by all applications. The following table lists some common authentication methods and when you might want to use them. Read the documentation for the application that you're using to determine which of these authentication methods are supported.

**Authentication type** | **Use cases**  
---|---  
Application Default Credentials (ADC) | Connecting from a Google-owned application like [Antigravity](https://antigravity.google/), or a third-party application that supports ADC like [Visual Studio Code](https://code.visualstudio.com/), or from an application running on Google infrastructure.  
OAuth 2.0 Client ID and secret | Connecting from a Google-owned or third-party application.  
Authorization header and OAuth 2.0 token | Connecting from a Google-owned or third-party application using an OAuth 2.0 bearer token or an API key. This method has better security than using a client ID and secret, but OAuth tokens must be refreshed regularly.  
  
## Authentication identities

You can use the following identities to authenticate to Google and Google Cloud MCP servers:

  * A [user identity](https://docs.cloud.google.com/iam/docs/user-identities).
  * An application or [workload identity](https://docs.cloud.google.com/iam/docs/workload-identities).
  * An [Agent identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview).



If the principal you're using doesn't have the permissions that you need to accomplish your task, or if you want to use a service account in a development environment, then you can use [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).

## Authenticate with Application Default Credentials

Some Google MCP clients use ADC automatically and might not require all the instructions in this section. For example, [Antigravity authentication](https://antigravity.google/docs/mcp#google-credentials) doesn't require using the authorization header. Read your application's authentication instructions to determine if it supports ADC, and how to configure it.

How you set up Application Default Credentials (ADC) depends on the environment where your code is running. The following instructions show you how to set up ADC using the Google Cloud CLI and your user identity for a local development environment. For more information about ADC for different environments, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

  1. [Set up ADC for your local environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#google-account).

  2. Generate an application default token by running the following command:
         
         gcloud auth application-default print-access-token
         

  3. In your application's configuration file, add the following to your MCP server entry:
         
         "headers": {
           "Authorization": "Bearer TOKEN",
           "x-goog-user-project": "PROJECT_ID"
         }
         

Replace the following:

     * TOKEN: the application default token.
     * PROJECT_ID: your project ID.

The following example shows an MCP server entry that uses ADC for authentication to the Cloud Run MCP server:
    
    {
      "servers": [
        {
          "name": "My Cloud Run MCP Server",
          "uri": "https://run.googleapis.com/mcp",
          "headers": {
            "Authorization": "Bearer abCdeFghIj1234567890abCDEFghIJ0987654321az",
            "x-goog-user-project": "my-project"
          }
        }
      ]
    }
    




## Authenticate with an OAuth 2.0 client ID and secret

You can create an [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) client ID and client secret to permit your AI application to authenticate to Google and Google Cloud remote MCP servers. When configured, the AI application can access resources that the authenticated user has access to, within the scopes that the user has authorized. This is achieved through OAuth tokens, so the actual user credentials are never shared with or stored in the AI application.

Depending on what kind of application you're using to send MCP requests, you'll need to select a **Desktop** or **Web** application client ID. Generally, if your application runs on your machine, then select **Desktop**. If you access your application through the internet, then select **Web**.

### Create an OAuth 2.0 client ID and secret

To create a client ID and secret, complete the following steps for the type of client ID you want to create:

### Web

Before creating a client ID for your web application, you need the following information:

  * `REDIRECT_URL`: The application redirect URL. The OAuth 2.0 server sends responses to this URL, and the user is redirected to it after they have authenticated with Google. Your application's documentation should provide the redirect URL. [Custom redirect URLs](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_custom-scheme) aren't supported.
  * `AUTHORIZED_JS_ORIGINS`: The authorized JavaScript origins. Applications that use client-side JavaScript to access Google's APIs must specify the authorized JavaScript Origins. The origins identify the domains from which the application sends API requests. For more information, see [Web applications](https://support.google.com/cloud/answer/15549257#web-applications).



#### Create a client ID for a web application

  1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

  2. In the **Application type** list, select **Web application**.

  3. In the **Name** field, enter a name for your application.

  4. In the **Authorized JavaScript origins** section, click **\+ Add URI** , and then enter `AUTHORIZED_JS_ORIGINS` in the **URIs** field.

  5. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `REDIRECT_URL` in the **URIs** field.

  6. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

  7. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.



### Desktop

  1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

  2. In the **Application type** list, select **Desktop app**.

  3. In the **Name** field, enter a name for your application.

  4. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

  5. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.



For more information about OAuth 2.0 credentials, read [Obtain OAuth 2.0 credentials from the Google API Console](https://developers.google.com/identity/protocols/oauth2#1.-obtain-oauth-2.0-credentials-from-the-google-api-console).

### Add the client ID to your MCP server configuration

In your application's configuration file, add the following to your MCP server entry:
    
    
    "oauth": {
      "clientId": "OAUTH_CLIENT_ID",
      "clientSecret": "OAUTH_CLIENT_SECRET",
      "scopes": ["SCOPE_1", "SCOPE_2"],
      "callbackPort": CALLBACK_PORT
      }
    

Replace the following:

  * `OAUTH_CLIENT_ID`: the OAuth 2.0 client ID.
  * `OAUTH_CLIENT_SECRET`: the OAuth 2.0 client secret.
  * `SCOPE_1`, `SCOPE_2`: the scopes needed to use the MCP server. To see what scopes are required, read the documentation for the MCP server you're configuring.
  * `CALLBACK_PORT`: the redirect URI or port that the user is sent to after authentication. Check the documentation for your application to determine the correct redirect URI.



The following example configures the Cloud Run MCP server with a read-only scope in Antigravity using a client ID and secret, and Antigravity's callback URI, `https://antigravity.google/oauth-callback`:
    
    
    {
      "mcpServers": {
        "oauth-server": {
          "serverUrl": "https://run.googleapis.com/mcp",
          "oauth": {
            "clientId": "1234567890abcdefgh.apps.googleusercontent.com",
            "clientSecret": "${MY_OAUTH_CLIENT_SECRET}",
            "scopes": ["https://www.googleapis.com/auth/run.readonly"],
            "callbackPort": "https://antigravity.google/oauth-callback"
          }
        }
      }
    }
    

## Authenticate with an Authorization header

You can use an [OAuth 2.0 Authorization header](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1) to authenticate with an OAuth 2.0 bearer token or an API key.

### Authenticate with a bearer token

By default, bearer tokens expire after 1 hour. You can extend the lifetime of a token up to 12 hours by passing the `--lifetime` flag when you create the token. For more information about bearer tokens, see [gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token).

  1. Create a bearer token with the Google Cloud CLI:
         
         gcloud auth print-access-token
         

  2. In your application's configuration file, add the following to your MCP server entry:
         
         "headers": {
           "Authorization": "Bearer TOKEN",
           "x-goog-user-project": "PROJECT_ID"
         }
         

Replace the following:

     * TOKEN: your bearer token.
     * PROJECT_ID: your project ID.

The following example shows an MCP server entry that uses an OAuth 2.0 bearer token for authentication to the Cloud Run MCP server:
    
    {
      "servers": [
        {
          "name": "My Cloud Run MCP Server",
          "uri": "https://run.googleapis.com/mcp",
          "headers": {
            "Authorization": "Bearer nYkwroEYjN4Fw1TTNhe69F4rR6o9bvrR1P4U1l0DVq9p81sN0",
            "x-goog-user-project": "my-project"
          }
        }
      ]
    }
    




### Authenticate with an API Key

[Standard API keys](https://docs.cloud.google.com/docs/authentication/api-keys#standard-api-keys) can only be used to authenticate to services that don't require a principal.

Services that don't require a principal can use API keys for authentication.

To create an API key for an AI application, do the following:

  1. In the Google Cloud console, go to the **APIs & Services > Credentials** page.

[Go Credentials](https://console.cloud.google.com/projectselector2/apis/credentials?supportedpurview=project)

  2. Click **Create credentials** and then select **API key**.

  3. In the **API key created** dialog, click **Edit API key**.

     1. Edit the API key **Application restrictions**. Application restrictions limit an API key's usage to specific websites, IP addresses, Android applications, or iOS applications. You can set one application restriction per key.
     2. Edit the API key **API restrictions**. API restrictions specify the enabled APIs that the key can call.
  4. Click **Save**.

  5. In your application's configuration file, add the following to your MCP server entry:
         
         "headers": {
           "X-Goog-Api-Key": GOOGLE_API_KEY
         }
         

Replace `GOOGLE_API_KEY` with the API key that has the required application and API restrictions.

The following example configures the Maps Grounding Lite MCP server with an API key in [Antigravity](https://antigravity.google/):
         
         {
           "mcpServers": {
             "my-remote-server": {
               "serverUrl": "https://mapstools.googleapis.com/mcp",
               "headers": {
                 "X-Goog-Api-Key": "EXAMPLE_API_KEY_VALUE"
               }
             }
           }
         }
         




To keep your API key secure, follow the [best practices for securely using API keys](https://support.google.com/googleapi/answer/6310037).

## What's next

  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).
  * Learn more about [authentication for Google Cloud APIs and services](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
