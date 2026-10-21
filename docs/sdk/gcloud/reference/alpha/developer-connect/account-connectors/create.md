---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/account-connectors/create/
title: gcloud alpha developer-connect account-connectors create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:44:36.230033+00:00
---

# gcloud alpha developer-connect account-connectors create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/account-connectors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha developer-connect account-connectors create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha developer-connect account-connectors create - create accountConnectors 
SYNOPSIS
    

`gcloud alpha developer-connect account-connectors create` `ACCOUNT_CONNECTOR` [`--annotations`=[`ANNOTATIONS`,…]] [`--async`] [`--etag`=`ETAG`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--proxy-config-enabled`] [`--request-id`=`REQUEST_ID`] [`--validate-only`] [[`--custom-oauth-config-auth-uri`=`CUSTOM_OAUTH_CONFIG_AUTH_URI` `--custom-oauth-config-client-id`=`CUSTOM_OAUTH_CONFIG_CLIENT_ID` `--custom-oauth-config-client-secret`=`CUSTOM_OAUTH_CONFIG_CLIENT_SECRET` `--custom-oauth-config-host-uri`=`CUSTOM_OAUTH_CONFIG_HOST_URI` `--custom-oauth-config-scm-provider`=`CUSTOM_OAUTH_CONFIG_SCM_PROVIDER` `--custom-oauth-config-scopes`=[`CUSTOM_OAUTH_CONFIG_SCOPES`,…] `--custom-oauth-config-token-uri`=`CUSTOM_OAUTH_CONFIG_TOKEN_URI` : `--custom-oauth-config-pkce-disabled` `--custom-oauth-config-ssl-ca-certificate`=`CUSTOM_OAUTH_CONFIG_SSL_CA_CERTIFICATE` [`--custom-oauth-config-service-directory`=`CUSTOM_OAUTH_CONFIG_SERVICE_DIRECTORY` : `--namespace`=`NAMESPACE`]] | [`--provider-oauth-config-scopes`=[`PROVIDER_OAUTH_CONFIG_SCOPES`,…] : `--provider-oauth-config-system-id`=`PROVIDER_OAUTH_CONFIG_SYSTEM_ID`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an accountConnector 
EXAMPLES
     To create the accountConnector, run: 
    
    
    gcloud alpha developer-connect account-connectors create

POSITIONAL ARGUMENTS
    

AccountConnector resource - Identifier. The resource name of the accountConnector, in the format `projects/{project}/locations/{location}/accountConnectors/{account_connector_id}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `account_connector` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `account_connector` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`ACCOUNT_CONNECTOR`
     ID of the accountConnector or fully qualified identifier for the accountConnector. 

To set the `account_connector` attribute: 

  * provide the argument `account_connector` on the command line. 


FLAGS
    

`--annotations`=[`ANNOTATIONS`,…]
     Allows users to store small amounts of arbitrary data. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--etag`=`ETAG`
     This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 
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

`--location`=`LOCATION`
     For resources [account_connector, custom-oauth-config-service-directory], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Proxy configuration. 
`--proxy-config-enabled`
     Setting this to true allows the git and http proxies to perform actions on behalf of the user configured under the account connector. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--validate-only`
     If set, validate the request, but do not actually post it. 
Arguments for the account connector config. 

At most one of these can be specified: 

Message for a customized OAuth config. 
`--custom-oauth-config-auth-uri`=`CUSTOM_OAUTH_CONFIG_AUTH_URI`
     OAuth2 authorization server URL. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-oauth-config-client-id`=`CUSTOM_OAUTH_CONFIG_CLIENT_ID`
     Client ID of the OAuth application. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-oauth-config-client-secret`=`CUSTOM_OAUTH_CONFIG_CLIENT_SECRET`
     Client secret of the OAuth application. It will be provided as plain text, but encrypted and stored in developer connect. As INPUT_ONLY field, it will not be included in the output. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-oauth-config-host-uri`=`CUSTOM_OAUTH_CONFIG_HOST_URI`
     Host URI of the OAuth application. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-oauth-config-scm-provider`=`CUSTOM_OAUTH_CONFIG_SCM_PROVIDER`
     Type of the SCM provider. `CUSTOM_OAUTH_CONFIG_SCM_PROVIDER` must be one of: 

`bitbucket-data-center`
     BYO Account Connector is an instance of Bitbucket Data Center. 
`github-enterprise`
     BYO Account Connector is an instance of GitHub Enterprise. 
`gitlab-enterprise`
     BYO Account Connector is an instance of GitLab Enterprise. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--custom-oauth-config-scopes`=[`CUSTOM_OAUTH_CONFIG_SCOPES`,…]
     Scopes to be requested during OAuth. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-oauth-config-token-uri`=`CUSTOM_OAUTH_CONFIG_TOKEN_URI`
     OAuth2 token request URL. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-oauth-config-pkce-disabled`
     Disable PKCE for this OAuth config. PKCE is enabled by default. 
`--custom-oauth-config-ssl-ca-certificate`=`CUSTOM_OAUTH_CONFIG_SSL_CA_CERTIFICATE`
     SSL certificate to use for requests to a private service. 
ServiceDirectoryConfig represents Service Directory configuration for a connection. 
Service resource - Service Directory service name. Format: projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--custom-oauth-config-service-directory` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--custom-oauth-config-service-directory` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--custom-oauth-config-service-directory`=`CUSTOM_OAUTH_CONFIG_SERVICE_DIRECTORY`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `--custom-oauth-config-service-directory` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--namespace`=`NAMESPACE`
     The namespace id of the service resource. 

To set the `namespace` attribute: 

  * provide the argument `--custom-oauth-config-service-directory` on the command line with a fully specified name; 
  * provide the argument `--namespace` on the command line. 


ProviderOAuthConfig is the OAuth config for a provider. 
`--provider-oauth-config-scopes`=[`PROVIDER_OAUTH_CONFIG_SCOPES`,…]
     User selected scopes to apply to the Oauth config In the event of changing scopes, user records under AccountConnector will be deleted and users will re-auth again. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Arguments for the oauth provider id. 
`--provider-oauth-config-system-id`=`PROVIDER_OAUTH_CONFIG_SYSTEM_ID`
     Developer Connect provided OAuth. `PROVIDER_OAUTH_CONFIG_SYSTEM_ID` must be one of: 

`bitbucket-cloud`
     Bitbucket Cloud provider. 
`datastax`
     Datastax provider. No scopes are allowed. 
`dynatrace`
     Dynatrace provider. 
`github`
     GitHub provider. Scopes can be found at <https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes>
`gitlab`
     GitLab provider. Scopes can be found at <https://docs.gitlab.com/user/profile/personal_access_tokens/#personal-access-token-scopes>
`google`
     Google provider. Recommended scopes: "https://www.googleapis.com/auth/drive.readonly", "https://www.googleapis.com/auth/documents.readonly" 
`new-relic`
     New Relic provider. No scopes are allowed. 
`rovo`
     Rovo provider. Must select the "rovo" scope. 
`sentry`
     Sentry provider. Scopes can be found at <https://docs.sentry.io/api/permissions/>
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `developerconnect/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/developer-connect/docs/overview>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud developer-connect account-connectors create](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/account-connectors/create)
    
    
    [gcloud beta developer-connect account-connectors create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/account-connectors/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
