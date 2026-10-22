---
url: https://docs.cloud.google.com/iam/docs/auth-manager-overview/
title: Agent Identity auth manager overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:23.413509+00:00
---

# Agent Identity auth manager overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/auth-manager-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Agent Identity auth manager overview Stay organized with collections  Save and categorize content based on your preferences. 

When generative AI agents interact with external tools, APIs, or services (such as BigQuery, Jira, GitHub, or Google Maps), they need a secure mechanism to authenticate outbound requests. The Agent Identity auth manager (auth manager) provides this by acting as a centralized credentials vault and authentication broker that simplifies outbound tool authentication.

## Benefits of using the auth manager

The auth manager provides the following benefits for agent development:

  * **Centralized credential vault** : Stores API keys, OAuth client secrets, and user tokens in a Google-managed vault, helping to avoid hardcoded secrets and custom database storage.
  * **Automated OAuth 2.0** : Handles multi-step OAuth 2.0 flows, such as user consent, authorization code exchange, and token refreshes, without custom backend code.
  * **Seamless ADK integration** : Integrates natively with the Agent Development Kit (ADK) to retrieve and inject outbound authentication headers, such as `Authorization` or `X-Goog-Api-Key`, into tool and Model Context Protocol (MCP) server invocations.
  * **Granular SPIFFE ID access control** : Uses SPIFFE-based agent identities to define precise Identity and Access Management (IAM) policies, helping to ensure only authorized agent principals and developers can access specific auth providers.



## How the auth manager works

The auth manager acts as a credentials vault between your Agent Runtime on Gemini Enterprise Agent Platform environment and external service endpoints.

When an agent calls an external tool, the ADK intercepts the tool execution, requests the appropriate credential from the auth manager vault, and attaches the required authentication headers before dispatching the request to the target API.

The following flow diagram illustrates the high-level architecture and credential retrieval lifecycle: ![Outbound credentials retrieval architecture diagram.](https://docs.cloud.google.com/static/iam/img/auth-manager-arch.svg)

  1. The end user triggers an event or prompt that requires outbound tool authentication.
  2. The deployed agent (using the ADK) transparently intercepts the tool request and queries the secure auth manager vault.
  3. The auth manager returns the secure credential (API key or OAuth token) to the agent.
  4. The agent invokes the external API or tool with the attached credential.
  5. The third-party service validates the credential and returns the requested data to the agent.
  6. The agent uses the returned data to generate and deliver the final response to the user.



## Sample third-party integrations

The auth manager supports standard OAuth 2.0 and API key patterns, making it compatible with many third-party services.

The following table lists some verified third-party services, their supported authentication methods, and setup documentation.

**Note:** This list is not exhaustive.Service | Supported authentication methods | Credential setup documentation  
---|---|---  
Atlassian Jira | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2), [API key](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2) | [Jira OAuth 2.0 guide](https://developer.atlassian.com/cloud/jira/software/oauth-2-3lo-apps/)  
Dropbox | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2) | [Dropbox OAuth guide](https://developers.dropbox.com/oauth-guide)  
GitHub | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)* | [GitHub OAuth Apps](https://docs.github.com/en/apps/oauth-apps)  
GitLab | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2) | [GitLab OAuth provider](https://docs.gitlab.com/integration/oauth_provider/)  
Microsoft | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)* | [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/)  
Salesforce | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2), [2-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2) | [Salesforce Connected Apps](https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm)  
ServiceNow | [3-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)*, [2-legged OAuth](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2) | [ServiceNow OAuth setup](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/security/concept/c_OAuthApplications.html)  
  
* For details on service limitations and requirements, see Service-specific considerations.

### Service-specific considerations

  * **GitHub and Microsoft** : The auth manager supports single-scope integrations for GitHub and Microsoft. The auth manager doesn't support requesting multiple scopes. For more information, see [GitHub or Microsoft multiple scopes error](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager#multiple-scopes-error).
  * **ServiceNow** : In ServiceNow, administrators configure allowed scopes at the application level. Regardless of what an agent requests, ServiceNow grants only these configured scopes. If an agent requires a scope that isn't configured, authentication might fail or enter a request loop. Ensure that the ServiceNow application configuration includes all of the scopes that your agent requires. For more information, see [ServiceNow authentication loop or unexpected scopes](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager#servicenow-scopes).



## Locations

The Agent Identity auth manager is available in regions across the Americas, Europe, and Asia Pacific. For a list of supported regions, see [Agent Identity locations](https://docs.cloud.google.com/iam/docs/agent-identity-locations).

## What's next

  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2)
  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2)
  * [Agent Identity locations](https://docs.cloud.google.com/iam/docs/agent-identity-locations)
  * [Troubleshoot Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/troubleshoot-auth-manager)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
