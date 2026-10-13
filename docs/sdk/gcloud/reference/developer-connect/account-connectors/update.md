---
url: https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/account-connectors/update/
title: gcloud developer-connect account-connectors update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:32.578915+00:00
---

# gcloud developer-connect account-connectors update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/account-connectors/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud developer-connect account-connectors update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud developer-connect account-connectors update - update accountConnectors 
SYNOPSIS
    

`gcloud developer-connect account-connectors update` `ACCOUNT_CONNECTOR` [`--[no-]allow-missing`] [`--async`] [`--etag`=`ETAG`] [`--location`=`LOCATION`] [`--request-id`=`REQUEST_ID`] [`--[no-]validate-only`] [`--annotations`=[`ANNOTATIONS`,…] | `--update-annotations`=[`UPDATE_ANNOTATIONS`,…] `--clear-annotations` | `--remove-annotations`=`REMOVE_ANNOTATIONS`] [`--clear-custom-oauth-config` `--custom-oauth-config-client-id`=`CUSTOM_OAUTH_CONFIG_CLIENT_ID` `--custom-oauth-config-client-secret`=`CUSTOM_OAUTH_CONFIG_CLIENT_SECRET` `--custom-oauth-config-host-uri`=`CUSTOM_OAUTH_CONFIG_HOST_URI` `--[no-]custom-oauth-config-pkce-disabled` `--custom-oauth-config-scm-provider`=`CUSTOM_OAUTH_CONFIG_SCM_PROVIDER` `--custom-oauth-config-scopes`=[`CUSTOM_OAUTH_CONFIG_SCOPES`,…] `--custom-oauth-config-ssl-ca-certificate`=`CUSTOM_OAUTH_CONFIG_SSL_CA_CERTIFICATE` [`--custom-oauth-config-service-directory`=`CUSTOM_OAUTH_CONFIG_SERVICE_DIRECTORY` : `--namespace`=`NAMESPACE`] | `--clear-provider-oauth-config` `--provider-oauth-config-scopes`=[`PROVIDER_OAUTH_CONFIG_SCOPES`,…]] [`--clear-proxy-config` `--[no-]proxy-config-enabled`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an accountConnector 
EXAMPLES
     To update the accountConnector, run: 
    
    
    gcloud developer-connect account-connectors update

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
    

`--[no-]allow-missing`
     If set to true, and the accountConnector is not found a new accountConnector will be created. In this situation `update_mask` is ignored. The creation will succeed only if the input accountConnector has all the necessary. Use `--allow-missing` to enable and `--no-allow-missing` to disable. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--etag`=`ETAG`
     This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 
`--location`=`LOCATION`
     For resources [account_connector, custom-oauth-config-service-directory], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--[no-]validate-only`
     If set, validate the request, but do not actually post it. Use `--validate-only` to enable and `--no-validate-only` to disable. 
Update annotations. 

At most one of these can be specified: 

`--annotations`=[`ANNOTATIONS`,…]
     Set annotations to new value. Allows users to store small amounts of arbitrary data. 

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

Or at least one of these can be specified: 

`--update-annotations`=[`UPDATE_ANNOTATIONS`,…]
     Update annotations value or add key value pair. Allows users to store small amounts of arbitrary data. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-annotations=string=string

`JSON Example:`
    
    
    --update-annotations='{"string": "string"}'

`File Example:`
    
    
    --update-annotations=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-annotations`
     Clear annotations value and set to empty map. 
`--remove-annotations`=`REMOVE_ANNOTATIONS`
     Remove existing value from map annotations. Sets `remove_annotations` value. `Shorthand Example:`
    
    
    --remove-annotations=string,string

`JSON Example:`
    
    
    --remove-annotations=["string"]

`File Example:`
    
    
    --remove-annotations=path_to_file.(yaml|json)

Arguments for the account connector config. 

At most one of these can be specified: 

Message for a customized OAuth config. 
`--clear-custom-oauth-config`
     Set accountConnector.customOauthConfig back to default value. 
`--custom-oauth-config-client-id`=`CUSTOM_OAUTH_CONFIG_CLIENT_ID`
     Client ID of the OAuth application. 
`--custom-oauth-config-client-secret`=`CUSTOM_OAUTH_CONFIG_CLIENT_SECRET`
     Client secret of the OAuth application. It will be provided as plain text, but encrypted and stored in developer connect. As INPUT_ONLY field, it will not be included in the output. 
`--custom-oauth-config-host-uri`=`CUSTOM_OAUTH_CONFIG_HOST_URI`
     Host URI of the OAuth application. 
`--[no-]custom-oauth-config-pkce-disabled`
     Disable PKCE for this OAuth config. PKCE is enabled by default. Use `--custom-oauth-config-pkce-disabled` to enable and `--no-custom-oauth-config-pkce-disabled` to disable. 
`--custom-oauth-config-scm-provider`=`CUSTOM_OAUTH_CONFIG_SCM_PROVIDER`
     Type of the SCM provider. `CUSTOM_OAUTH_CONFIG_SCM_PROVIDER` must be one of: 

`bitbucket-data-center`
     BYO Account Connector is an instance of Bitbucket Data Center. 
`github-enterprise`
     BYO Account Connector is an instance of GitHub Enterprise. 
`gitlab-enterprise`
     BYO Account Connector is an instance of GitLab Enterprise. 
`--custom-oauth-config-scopes`=[`CUSTOM_OAUTH_CONFIG_SCOPES`,…]
     Scopes to be requested during OAuth. 
`--custom-oauth-config-ssl-ca-certificate`=`CUSTOM_OAUTH_CONFIG_SSL_CA_CERTIFICATE`
     SSL certificate to use for requests to a private service. 
ServiceDirectoryConfig represents Service Directory configuration for a connection. 
Service resource - The Service Directory service name. Format: projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
`--clear-provider-oauth-config`
     Set accountConnector.providerOauthConfig back to default value. 
`--provider-oauth-config-scopes`=[`PROVIDER_OAUTH_CONFIG_SCOPES`,…]
     User selected scopes to apply to the Oauth config In the event of changing scopes, user records under AccountConnector will be deleted and users will re-auth again. 
Proxy configuration. 
`--clear-proxy-config`
     Set accountConnector.proxyConfig back to default value. 
`--[no-]proxy-config-enabled`
     Setting this to true allows the git and http proxies to perform actions on behalf of the user configured under the account connector. Use `--proxy-config-enabled` to enable and `--no-proxy-config-enabled` to disable. 
Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Labels as key value pairs. 

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

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `developerconnect/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/developer-connect/docs/overview>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha developer-connect account-connectors update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/account-connectors/update)
    
    
    [gcloud beta developer-connect account-connectors update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/account-connectors/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
