---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/mcp-transcoders/create/
title: gcloud alpha network-services mcp-transcoders create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:45.051982+00:00
---

# gcloud alpha network-services mcp-transcoders create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/mcp-transcoders/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-services mcp-transcoders create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-services mcp-transcoders create - create an MCP Transcoder 
SYNOPSIS
    

`gcloud alpha network-services mcp-transcoders create` `MCP_TRANSCODER` `--agent-gateway`=`AGENT_GATEWAY` `--endpoints`=[`ENDPOINTS`,…] `--mcp-server-url`=`MCP_SERVER_URL` [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a new McpTranscoder in a given project and location. 
EXAMPLES
     To create a global MCP transcoder `my-mcp-transcoder` associated with agent gateway `my-agent-gateway`, run: 
    
    
    gcloud alpha network-services mcp-transcoders create my-mcp-transcoder --location=global --agent-gateway=projects/my-project/locations/global/agentGateways/my-agent-gateway --mcp-server-url="https://api.example.com/v1/mcp" --endpoints="//agentregistry.googleapis.com/projects/my-project/locations/global/services/my-service"

POSITIONAL ARGUMENTS
    

McpTranscoder resource - Identifier. Resource name of the McpTranscoder. It must be in the format `projects/*/locations/*/mcpTranscoders/{mcp_transcoder}`. `{mcp_transcoder}` must be 1-63 characters long and match the regex `[a-z]([-a-z0-9]*[a-z0-9])?`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `mcp_transcoder` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `mcp_transcoder` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`MCP_TRANSCODER`
     ID of the mcpTranscoder or fully qualified identifier for the mcpTranscoder. 

To set the `mcp_transcoder` attribute: 

  * provide the argument `mcp_transcoder` on the command line. 


REQUIRED FLAGS
    

AgentGateway resource - The resource name of the AgentGateway this McpTranscoder is associated with. Must be in the format `projects/*/locations/*/agentGateways/{agent_gateway_id}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--agent-gateway` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--agent-gateway` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--agent-gateway`=`AGENT_GATEWAY`
     ID of the agentGateway or fully qualified identifier for the agentGateway. 

To set the `agent-gateway` attribute: 

  * provide the argument `--agent-gateway` on the command line. 


`--endpoints`=[`ENDPOINTS`,…]
     A list of resource URIs of Service resources (from Agent Registry) that contain the OpenAPI specifications. Must be in the format `//agentregistry.googleapis.com/projects/*/locations/*/services/{service}`. Note: For the MVP, each McpTranscoder is limited to a single tool set. 
`--mcp-server-url`=`MCP_SERVER_URL`
     Specifies the MCP server URL used for the MCP request calls. Must be a valid URL starting with `http://` or `https://` (e.g., "https://api.example.com/v1/mcp"). 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     An optional description of the McpTranscoder resource. Max length 1024 characters. 
`--etag`=`ETAG`
     Etag of the resource. If this is provided, it must match the server's etag. If the provided etag does not match the server's etag, the request will fail with a 409 ABORTED error. 
`--labels`=[`LABELS`,…]
     Set of labels associated with the McpTranscoder resource. 

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
     For resources [agent-gateway, mcp_transcoder], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
