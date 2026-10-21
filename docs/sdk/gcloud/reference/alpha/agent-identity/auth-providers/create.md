---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/create/
title: gcloud alpha agent-identity auth-providers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:26:58.550061+00:00
---

# gcloud alpha agent-identity auth-providers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha agent-identity auth-providers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha agent-identity auth-providers create - create an auth provider 
SYNOPSIS
    

`gcloud alpha agent-identity auth-providers create` (`AUTH_PROVIDER` : `--location`=`LOCATION`) (`--api-key`=`API_KEY` | `--three-legged-oauth-authorization-url`=`THREE_LEGGED_OAUTH_AUTHORIZATION_URL` `--three-legged-oauth-client-id`=`THREE_LEGGED_OAUTH_CLIENT_ID` `--three-legged-oauth-client-secret`=`THREE_LEGGED_OAUTH_CLIENT_SECRET` `--three-legged-oauth-default-continue-uri`=`THREE_LEGGED_OAUTH_DEFAULT_CONTINUE_URI` `--three-legged-oauth-enable-pkce` `--three-legged-oauth-token-url`=`THREE_LEGGED_OAUTH_TOKEN_URL` | `--two-legged-oauth-client-id`=`TWO_LEGGED_OAUTH_CLIENT_ID` `--two-legged-oauth-client-secret`=`TWO_LEGGED_OAUTH_CLIENT_SECRET` `--two-legged-oauth-token-url`=`TWO_LEGGED_OAUTH_TOKEN_URL`) [`--allowed-scopes`=[`ALLOWED_SCOPES`,…]] [`--blocked-scopes`=[`BLOCKED_SCOPES`,…]] [`--description`=`DESCRIPTION`] [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [`--workload-ids`=[`WORKLOAD_IDS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new auth provider in a given project and location. 
EXAMPLES
     To create an API key auth provider 'my-auth-provider' in location 'us-central1' and project 'my-project', run: 
    
    
    gcloud alpha agent-identity auth-providers create my-auth-provider --location=us-central1 --project=my-project --api-key=my-api-key

POSITIONAL ARGUMENTS
    

AuthProvider resource - Identifier. The full resource name of the auth_provider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `auth_provider` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTH_PROVIDER`
     ID of the authProvider or fully qualified identifier for the authProvider. 

To set the `auth_provider` attribute: 

  * provide the argument `auth_provider` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the authProvider resource. 

To set the `location` attribute: 

  * provide the argument `auth_provider` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

AuthProvider type specific parameters. Required when creating an auth_provider. 

This must be specified. 

Arguments for the type. 

At most one of these can be specified: 

Message describing ApiKeyParams object. 
`--api-key`=`API_KEY`
     The API key for this auth_provider. 
Message describing ThreeLeggedOAuth object. 
`--three-legged-oauth-authorization-url`=`THREE_LEGGED_OAUTH_AUTHORIZATION_URL`
     The authorization endpoint to send users to for consenting to delegate to the agent. eg. "https://auth.atlassian.com/authorize" 
`--three-legged-oauth-client-id`=`THREE_LEGGED_OAUTH_CLIENT_ID`
     The client ID of the OAuth client. 
`--three-legged-oauth-client-secret`=`THREE_LEGGED_OAUTH_CLIENT_SECRET`
     The client secret of the OAuth client. 
`--three-legged-oauth-default-continue-uri`=`THREE_LEGGED_OAUTH_DEFAULT_CONTINUE_URI`
     The default continue URI for 3LO flow to redirect end users after consent. 
`--three-legged-oauth-enable-pkce`
     Enables Proof Key for Code Exchange (PKCE) for the OAuth flow to prevent authorization code interception attacks. 
`--three-legged-oauth-token-url`=`THREE_LEGGED_OAUTH_TOKEN_URL`
     The token endpoint for requesting tokens on behalf of an end user. eg. "https://auth.atlassian.com/oauth/token" 
Message describing TwoLeggedOAuth object. 
`--two-legged-oauth-client-id`=`TWO_LEGGED_OAUTH_CLIENT_ID`
     The client ID of the OAuth client. 
`--two-legged-oauth-client-secret`=`TWO_LEGGED_OAUTH_CLIENT_SECRET`
     The client secret of the OAuth client. 
`--two-legged-oauth-token-url`=`TWO_LEGGED_OAUTH_TOKEN_URL`
     The token endpoint of the OAuth client. 
OPTIONAL FLAGS
    

`--allowed-scopes`=[`ALLOWED_SCOPES`,…]
     List of scopes that are allowed to be requested for this auth_provider. If this list is non-empty, only scopes within this list may be requested. If this list is empty, all scopes may be requested. Scopes appearing in `blocked_scopes` are disallowed even if they appear in `allowed_scopes`. The number of allowed scopes is limited to 200. 
`--blocked-scopes`=[`BLOCKED_SCOPES`,…]
     List of scopes that are blocked from being requested for this auth_provider. If a scope appears in this list, it will not be requested, even if it also appears in `allowed_scopes`. `blocked_scopes` takes precedence over `allowed_scopes`. The number of blocked scopes is limited to 200\. 
`--description`=`DESCRIPTION`
     Description of the resource. Must be less than 256 characters. 
`--labels`=[`LABELS`,…]
     Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--workload-ids`=[`WORKLOAD_IDS`,…]
     Represents the workload identity in IAM `principal://` format of the agent(s) that will use this AuthProvider. Example: `principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentidentity/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud agent-identity auth-providers create](https://docs.cloud.google.com/sdk/gcloud/reference/agent-identity/auth-providers/create)
    
    
    [gcloud beta agent-identity auth-providers create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity/auth-providers/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
