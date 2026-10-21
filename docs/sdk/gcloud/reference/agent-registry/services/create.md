---
url: https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/create/
title: gcloud agent-registry services create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:06.843169+00:00
---

# gcloud agent-registry services create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud agent-registry services create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud agent-registry services create - register a new service 
SYNOPSIS
    

`gcloud agent-registry services create` (`SERVICE` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`]] [`--request-id`=`REQUEST_ID`] [[`--agent-spec-type`=`AGENT_SPEC_TYPE` : `--agent-spec-content`=`AGENT_SPEC_CONTENT`] | [`--endpoint-spec-type`=`ENDPOINT_SPEC_TYPE` : `--endpoint-spec-content`=`ENDPOINT_SPEC_CONTENT`] | [`--mcp-server-spec-type`=`MCP_SERVER_SPEC_TYPE` : `--mcp-server-spec-content`=`MCP_SERVER_SPEC_CONTENT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a writable Service resource to manually register custom or external agentic components into the registry. A Service represents an agent, an MCP server, or an endpoint that is manually added to your registry. Depending on the specification provided, Agent Registry automatically projects this Service onto the consumer side as a read-only Agent, McpServer, or Endpoint resource for discovery. 
EXAMPLES
     To create an agent service with an interface URL and HTTP+JSON binding, run: 
    
    
    gcloud agent-registry services create my-service --location=us-central1 --display-name="My Agent Service" --agent-spec-type=no-spec --interfaces="url=https://example.com/api,protocolBinding=http-json"

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
`--interfaces`=[`protocolBinding`=`PROTOCOLBINDING`],[`url`=`URL`]
     The connection details for the Service. 

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

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Arguments for the spec. 

At most one of these can be specified: 

The spec of the agent. 
`--agent-spec-type`=`AGENT_SPEC_TYPE`
     The type of the agent spec content. `AGENT_SPEC_TYPE` must be one of: 

`a2a-agent-card`
     The content is an A2A Agent Card following the A2A specification. The `interfaces` field must be empty. 
`no-spec`
     There is no spec for the Agent. The `content` field must be empty. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--agent-spec-content`=`AGENT_SPEC_CONTENT`
     The content of the Agent spec in the JSON format. This payload is validated against the schema for the specified type. The content size is limited to `10KB`. 
The spec of the endpoint. 
`--endpoint-spec-type`=`ENDPOINT_SPEC_TYPE`
     The type of the endpoint spec content. `ENDPOINT_SPEC_TYPE` must be (only one value is supported): 

`no-spec`
     There is no spec for the Endpoint. The `content` field must be empty. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--endpoint-spec-content`=`ENDPOINT_SPEC_CONTENT`
     The content of the endpoint spec. Reserved for future use. 
The spec of the MCP Server. 
`--mcp-server-spec-type`=`MCP_SERVER_SPEC_TYPE`
     The type of the MCP Server spec content. `MCP_SERVER_SPEC_TYPE` must be one of: 

`no-spec`
     There is no spec for the MCP Server. The `content` field must be empty. 
`tool-spec`
     The content is a MCP Tool Spec following the One MCP specification. The payload is the same as the `tools/list` response. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--mcp-server-spec-content`=`MCP_SERVER_SPEC_CONTENT`
     The content of the MCP Server spec. This payload is validated against the schema for the specified type. The content size is limited to `10KB`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentregistry/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/agent-registry/overview>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha agent-registry services create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/services/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
