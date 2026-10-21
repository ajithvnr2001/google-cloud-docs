---
url: https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/update/
title: gcloud agent-registry services update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:07.519145+00:00
---

# gcloud agent-registry services update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud agent-registry services update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud agent-registry services update - modify service parameters 
SYNOPSIS
    

`gcloud agent-registry services update` (`SERVICE` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--request-id`=`REQUEST_ID`] [`--agent-spec-content`=`AGENT_SPEC_CONTENT` | `--endpoint-spec-content`=`ENDPOINT_SPEC_CONTENT` | `--mcp-server-spec-content`=`MCP_SERVER_SPEC_CONTENT`] [`--interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`] | `--add-interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`] `--clear-interfaces` | `--remove-interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update properties on a writable Service resource representing a manually registered agentic component (agent, MCP server, or endpoint). 
EXAMPLES
     To update the display name of service 'my-service' in location 'us-central1', run: 
    
    
    gcloud agent-registry services update my-service --location=us-central1 --display-name="New Display Name"

POSITIONAL ARGUMENTS
    

Service resource - Identifier. The resource name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the service resource. 

To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-defined description of an Service. Can have a maximum length of `2048` characters. 
`--display-name`=`DISPLAY_NAME`
     User-defined display name for the Service. Can have a maximum length of `63` characters. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Arguments for the spec. 

At most one of these can be specified: 

The spec of the agent. 
`--agent-spec-content`=`AGENT_SPEC_CONTENT`
     The content of the Agent spec in the JSON format. This payload is validated against the schema for the specified type. The content size is limited to `10KB`. 
The spec of the endpoint. 
`--endpoint-spec-content`=`ENDPOINT_SPEC_CONTENT`
     The content of the endpoint spec. Reserved for future use. 
The spec of the MCP Server. 
`--mcp-server-spec-content`=`MCP_SERVER_SPEC_CONTENT`
     The content of the MCP Server spec. This payload is validated against the schema for the specified type. The content size is limited to `10KB`. 
Update interfaces. 

At most one of these can be specified: 

`--interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`]
     Set interfaces to new value. The connection details for the Service. 

`protocolBinding`
     The protocol binding of the interface. 
`url`
     The destination URL. 
`Shorthand Example:`
    
    
    --interfaces=protocolBinding=string,url=string --interfaces=protocolBinding=string,url=string

`JSON Example:`
    
    
    --interfaces='[{"protocolBinding": "string", "url": "string"}]'

`File Example:`
    
    
    --interfaces=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`]
     Add new value to interfaces list. The connection details for the Service. 

`protocolBinding`
     The protocol binding of the interface. 
`url`
     The destination URL. 
`Shorthand Example:`
    
    
    --add-interfaces=protocolBinding=string,url=string --add-interfaces=protocolBinding=string,url=string

`JSON Example:`
    
    
    --add-interfaces='[{"protocolBinding": "string", "url": "string"}]'

`File Example:`
    
    
    --add-interfaces=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-interfaces`
     Clear interfaces value and set to empty list. 
`--remove-interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`]
     Remove existing value from interfaces list. The connection details for the Service. 

`protocolBinding`
     The protocol binding of the interface. 
`url`
     The destination URL. 
`Shorthand Example:`
    
    
    --remove-interfaces=protocolBinding=string,url=string --remove-interfaces=protocolBinding=string,url=string

`JSON Example:`
    
    
    --remove-interfaces='[{"protocolBinding": "string", "url": "string"}]'

`File Example:`
    
    
    --remove-interfaces=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentregistry/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/agent-registry/overview>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha agent-registry services update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/services/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
