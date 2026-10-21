---
url: https://docs.cloud.google.com/mcp/authenticate-mcp/
title: Authenticate to Google and Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:36.838400+00:00
---

# Authenticate to Google and Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/authenticate-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Reference ](https://docs.cloud.google.com/mcp/authenticate-mcp)



Send feedback 

#  Authenticate to Google and Google Cloud MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

Model Context Protocol (MCP) authentication lets your AI applications and agents securely access Google and Google Cloud MCP servers. These remote MCP servers implement the [MCP authorization specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) for HTTP-based transports. Depending on service requirements, your [MCP client](https://modelcontextprotocol.io/docs/learn/client-concepts) can authenticate by using credentials that represent an Identity and Access Management (IAM) principal or by supplying [standard API keys](https://docs.cloud.google.com/docs/authentication/api-keys#standard-api-keys). Consult the MCP server's documentation to understand which methods are supported.

The terms _AI application_ and _agent_ are used interchangeably throughout this document, and refer to any program that can instantiate an [MCP client](https://modelcontextprotocol.io/docs/learn/client-concepts).

## How MCP requests and authentication work

When your AI application sends an MCP request, the MCP client must authenticate to the MCP server using the authentication method and identity that you supply. If you use your own identity, actions taken by the AI application through MCP requests are attributed to you. Additionally, the MCP client has the same permissions as you do on all resources. If you don't want to use your own credentials, then you can create a separate identity for the application to use to authenticate to the MCP server.

## Authentication identities

You can use the following identities to authenticate to Google and Google Cloud MCP servers:

  * A [user identity](https://docs.cloud.google.com/iam/docs/user-identities).
  * An application or [workload identity](https://docs.cloud.google.com/iam/docs/workload-identities).
  * An [Agent identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview).



If the principal you're using doesn't have the permissions that you need to accomplish your task, or if you want to use a service account in a development environment, then you can use [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).

### User, workload, and agent identities

You can use your own user identity to authenticate to MCP servers, but when you do so, the MCP client has the same permissions as you do on Google and Google Cloud resources, and actions taken by the MCP client are attributed to you.

For production workloads, we recommend that you create a separate agent or workload identity, instead of using your identity. Using a separate identity to access MCP servers means you can limit the permissions and actions taken by the MCP client and view actions taken through MCP requests in your logs.

Only grant your agent identity the minimum permissions necessary, and consider using Identity and Access Management attributes to [prevent read-write MCP tool use](https://docs.cloud.google.com/mcp/prevent-read-write-tool-use) on important resources.

The following sections describe how to set up a separate identity, or principal, for your agent. The agent principal can be granted separate roles to control the AI application's access to resources.

Your authentication setup depends on your environment. The most common options are described in the following sections.

### Agents on Google Cloud

To authenticate an agent running on Google Cloud, you can use the credentials of a service account attached to a compute resource where your code is running, such as a [Compute Engine virtual machine (VM) instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) or an [agent identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

#### Use a service account for authentication

Use the gcloud CLI to create a service account and attach it to your resource:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. To provide access to your project and your resources, grant a role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     4. To grant another role to the service account, run the command as you did in the previous step. 
     5. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account
  3. Create the resource that will run your code, and attach the service account to that resource. For example, if you use Compute Engine: Create a Compute Engine instance. Configure the instance as follows: 
     * Replace `INSTANCE_NAME` with your preferred instance name. 
     * Set the `--zone` flag to the [zone](https://docs.cloud.google.com/compute/docs/zones#available) in which you want to create your instance. 
     * Set the `--service-account` flag to the email address for the service account that you created. 
    
    gcloud compute instances create INSTANCE_NAME --zone=ZONE --service-account=SERVICE_ACCOUNT_EMAIL




For more information about authenticating to Google APIs, see [Authentication methods](https://docs.cloud.google.com/docs/authentication).

#### Use an agent identity for authentication

Agent Identity provides a strongly attested, cryptographic identity for each agent that is based on the [SPIFFE standard](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity). With Agent Identity, your agent can securely authenticate to MCP servers, cloud resources, endpoints, and other agents, acting either on its own behalf or on behalf of an end user. Agent Identity uses the [agent's own credential](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-credentials) and [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager). You can use the auth manager to create and manage _auth providers_ , which are the specific configurations used to acquire, manage, and secure API keys, OAuth client IDs, OAuth client secrets, and delegated end-user OAuth tokens.

Unlike service accounts, agent identities are not shared by multiple workloads by default, can't be impersonated, and don't allow developers to generate long-lived service account keys. Access tokens generated for Google Cloud are cryptographically bound to the agent's unique X.509 certificates to prevent token theft.

For more information, see [Agent identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

### Agents on-premises or on a different cloud provider

The preferred method to set up identities to use for authentication from outside of Google Cloud is to use workload identity federation. For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises) in the authentication documentation.

### API keys for services that don't require a principal

Services that don't require a principal can use API keys for authentication. For information about how to create and use an API key for authentication to MCP servers, see [Set up authentication for MCP servers](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers).

## Authentication methods

Most applications that can connect to MCP servers offer a way to add authentication, but not all Google authentication methods are supported by all applications. The following table lists some common authentication methods and when you might want to use them. Read the documentation for the application that you're using to determine which of these authentication methods are supported.

**Authentication type** | **Use cases**  
---|---  
Application Default Credentials (ADC) | Connecting from a Google-owned application like [Antigravity](https://antigravity.google/) or from an application running on Google infrastructure.  
OAuth 2.0 Client ID and secret | Connecting from a Google-owned or third-party application.  
Authorization header | Connecting from a Google-owned or third-party application using an OAuth 2.0 bearer token or an API key. This method has better security than using a client ID and secret, but OAuth tokens must be refreshed regularly.  
  
### ADC for MCP servers

Authentication libraries use the [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) strategy to automatically find credentials based on the application environment. The authentication libraries make those credentials available to [Cloud Client Libraries and Google API Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained). When you use ADC, your code can run in either a development or production environment without changing how your application authenticates to Google Cloud services and APIs.

If you're connecting to our MCP servers from a Google-owned application or an agent running on Google Cloud, then you can [set up ADC for your environment](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#adc) to authenticate. You can use ADC with user, workload, or agent identities.

**Note** : If you use an ADC generated bearer token for authentication, then you need to re-authenticate every hour to refresh your access token with Google Cloud CLI. If you are using ADC for authentication to Antigravity or Gemini CLI, then your token is automatically refreshed.

If you use this method, you might encounter an authentication error when you try to authenticate to MCP servers. For more information about this error and how to address it, see [User credentials not working](https://docs.cloud.google.com/docs/authentication/troubleshoot-adc#user-creds-client-based).

### OAuth client ID

You can create an OAuth 2.0 client ID and client secret for your MCP client to use to authenticate to Google and Google Cloud remote MCP servers. When configured, the MCP client can access Google and Google Cloud resources that the authenticated user has access to, within the scopes that the user has authorized. This is achieved through OAuth tokens, so the actual user credentials are never shared with or stored in the AI application.

To create an OAuth 2.0 client ID and secret, follow the instructions in [Authenticate with an OAuth 2.0 client ID and secret](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers#client-id-secret).

### Authorization header

You can use an [OAuth 2.0 Authorization header](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1) to authenticate with an OAuth 2.0 bearer token or an API key. For more information, see [Set up authentication for MCP servers](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers).

## Limitations

Google and Google Cloud remote MCP servers don't support [Dynamic Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#dynamic-client-registration) or [OAuth Client ID Metadata Documents](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#client-id-metadata-documents).

## What's next

  * [Set up authentication to Google and Google Cloud MCP servers](https://docs.cloud.google.com/mcp/set-up-authentication-mcp-servers)
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
