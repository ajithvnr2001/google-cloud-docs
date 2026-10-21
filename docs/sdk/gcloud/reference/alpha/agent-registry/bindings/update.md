---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/bindings/update/
title: gcloud alpha agent-registry bindings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:52:36.955568+00:00
---

# gcloud alpha agent-registry bindings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/bindings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha agent-registry bindings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha agent-registry bindings update - modify binding parameters 
SYNOPSIS
    

`gcloud alpha agent-registry bindings update` (`BINDING` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--request-id`=`REQUEST_ID`] [`--auth-provider-binding`=`AUTH_PROVIDER_BINDING` `--auth-provider-binding-continue-uri`=`AUTH_PROVIDER_BINDING_CONTINUE_URI` `--clear-auth-provider-binding` `--auth-provider-binding-scopes`=[`AUTH_PROVIDER_BINDING_SCOPES`,…] | `--add-auth-provider-binding-scopes`=[`ADD_AUTH_PROVIDER_BINDING_SCOPES`,…] `--clear-auth-provider-binding-scopes` | `--remove-auth-provider-binding-scopes`=[`REMOVE_AUTH_PROVIDER_BINDING_SCOPES`,…]] [`--clear-source` `--source-identifier`=`SOURCE_IDENTIFIER`] [`--clear-target` `--target-identifier`=`TARGET_IDENTIFIER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update properties on a binding connecting a source agent to a target resource or auth provider. 
EXAMPLES
     To update display name of binding 'my-binding' in location 'us-central1', run: 
    
    
    gcloud alpha agent-registry bindings update my-binding --location=us-central1 --display-name="Updated Binding Name"

POSITIONAL ARGUMENTS
    

Binding resource - Identifier. The resource name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `binding` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BINDING`
     ID of the binding or fully qualified identifier for the binding. 

To set the `binding` attribute: 

  * provide the argument `binding` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the binding resource. 

To set the `location` attribute: 

  * provide the argument `binding` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-defined description of a Binding. Can have a maximum length of `2048` characters. 
`--display-name`=`DISPLAY_NAME`
     User-defined display name for the Binding. Can have a maximum length of `63` characters. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Arguments for the binding. 
The AuthProvider of the Binding. 
`--auth-provider-binding`=`AUTH_PROVIDER_BINDING`
     The resource name of the target AuthProvider. Format: 

  * `projects/{project}/locations/{location}/authProviders/{auth_provider}`


`--auth-provider-binding-continue-uri`=`AUTH_PROVIDER_BINDING_CONTINUE_URI`
     The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow. 
`--clear-auth-provider-binding`
     Set binding.authProviderBinding back to default value. 
Update auth_provider_binding_scopes. 

At most one of these can be specified: 

`--auth-provider-binding-scopes`=[`AUTH_PROVIDER_BINDING_SCOPES`,…]
     Set auth_provider_binding_scopes to new value. 
Or at least one of these can be specified: 

`--add-auth-provider-binding-scopes`=[`ADD_AUTH_PROVIDER_BINDING_SCOPES`,…]
     Add new value to auth_provider_binding_scopes list. 
At most one of these can be specified: 

`--clear-auth-provider-binding-scopes`
     Clear auth_provider_binding_scopes value and set to empty list. 
`--remove-auth-provider-binding-scopes`=[`REMOVE_AUTH_PROVIDER_BINDING_SCOPES`,…]
     Remove existing value from auth_provider_binding_scopes list. 
The source of the Binding. 
`--clear-source`
     Set binding.source back to default value. 
Arguments for the source type. 
`--source-identifier`=`SOURCE_IDENTIFIER`
     The identifier of the source Agent. Format: 

  * `urn:agent:{publisher}:{namespace}:{name}`


The target of the Binding. 
`--clear-target`
     Set binding.target back to default value. 
Arguments for the target type. 
`--target-identifier`=`TARGET_IDENTIFIER`
     The identifier of the target Agent, MCP Server, or Endpoint. Format: 

  * `urn:agent:{publisher}:{namespace}:{name}`
  * `urn:mcp:{publisher}:{namespace}:{name}`
  * `urn:endpoint:{publisher}:{namespace}:{name}`


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentregistry/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/agent-registry/overview>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud agent-registry bindings update](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/bindings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
