---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apihub/locations/configure-and-deploy-server/
title: gcloud apihub locations configure-and-deploy-server \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:49:30.166617+00:00
---

# gcloud apihub locations configure-and-deploy-server  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apihub/locations/configure-and-deploy-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apihub locations configure-and-deploy-server Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apihub locations configure-and-deploy-server - configure and deploy an API Hub server 
SYNOPSIS
    

`gcloud apihub locations configure-and-deploy-server` `LOCATION` ([`--apigee-x-environment`=`APIGEE_X_ENVIRONMENT` `--apigee-x-proxy`=`APIGEE_X_PROXY` `--apigee-x-target-project`=`APIGEE_X_TARGET_PROJECT` : `--apigee-x-proxy-description`=`APIGEE_X_PROXY_DESCRIPTION` `--apigee-x-proxy-display-name`=`APIGEE_X_PROXY_DISPLAY_NAME`]) ((`--mcp-tools`=[`description`=`DESCRIPTION`],[`operation`=`OPERATION`],[`tool-id`=`TOOL-ID`] | `--mcp-tools-from-file`=`MCP_TOOLS_FROM_FILE`)) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Configures and deploys an API Hub server in the specified location. If a server with the same target identity already exists, this command overwrites it by creating a new revision; all existing tools are replaced. 

Currently only MCP (Model Context Protocol) servers on Apigee X are supported. 

EXAMPLES
     To deploy an MCP server with a single tool on Apigee X: 
    
    
    gcloud apihub locations configure-and-deploy-server us-central1 --project=my-project --mcp-tools='tool-id=greet,description=Greet the
     user,operation=projects/my-project/locations/us-central1/apis/hello\
    /versions/v1/operations/greet' --apigee-x-environment=eval \
        --apigee-x-proxy=mcp-discovery-server \
        --apigee-x-target-project=my-apigee-project

To deploy with a tools spec file (required for tools that reference an HTTP operation by spec + path + method): 
    
    
    gcloud apihub locations configure-and-deploy-server us-central1 --project=my-project --mcp-tools-from-file=tools.yaml --apigee-x-environment=eval --apigee-x-proxy=mcp-discovery-server --apigee-x-target-project=my-apigee-project

If any flag value contains a comma, use the alternate delimiter syntax `^DELIM^value` (see `[gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping)`). For example: 
    
    
    gcloud apihub locations configure-and-deploy-server us-central1 --project=my-project --mcp-tools='^|^tool-id=lookup|description=Lookup by id, name,
     or
     email|operation=projects/my-project/locations/us-central1/apis/user\
    s/versions/v1/operations/lookup' --apigee-x-environment=eval \
        --apigee-x-proxy=mcp-discovery-server \
        --apigee-x-target-project=my-apigee-project

POSITIONAL ARGUMENTS
    

Location resource - The location in which to configure and deploy the server. Format: `projects/{project}/locations/{location}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `location` on the command line. 


REQUIRED FLAGS
    

Deployment target runtime. Exactly one target must be specified. 

This must be specified. 

Apigee X runtime target. 
`--apigee-x-environment`=`APIGEE_X_ENVIRONMENT`
     The specific Apigee X environment where the server will be deployed. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--apigee-x-proxy`=`APIGEE_X_PROXY`
     Name identifying the proxy resource in Apigee X. Standard alphanumeric format (e.g. "mcp-discovery-server"). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--apigee-x-target-project`=`APIGEE_X_TARGET_PROJECT`
     The runtime project that hosts the Apigee X organization. This must be one of the runtime projects attached to the API Hub host project. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--apigee-x-proxy-description`=`APIGEE_X_PROXY_DESCRIPTION`
     Description for the deployed proxy revision in Apigee X. 
`--apigee-x-proxy-display-name`=`APIGEE_X_PROXY_DISPLAY_NAME`
     Display name for the deployed proxy revision in Apigee X. 
Server protocol configuration. Exactly one server type must be specified. 

This must be specified. 

MCP (Model Context Protocol) server configuration. Provide either --mcp-tools (one or more) or --mcp-tools-from-file. 

Exactly one of these must be specified: 

`--mcp-tools`=[`description`=`DESCRIPTION`],[`operation`=`OPERATION`],[`tool-id`=`TOOL-ID`]
     A tool to expose on the MCP server. Repeatable. Each value is a comma-separated dict with keys: 

  * tool-id (required) Unique identifier for the tool. 
  * description (required) What the tool does. 
  * operation (required) Full API Hub operation resource name, e.g. `projects/{project}/locations/ {location}/apis/{api}/versions/{version}/ operations/{operation}`. 



For tools that reference an operation by spec + path + method, use \--mcp-tools-from-file instead (this flag cannot express the http_operation oneof arm). 

`--mcp-tools-from-file`=`MCP_TOOLS_FROM_FILE`
     Path to a YAML or JSON file containing a list of MCP tools. Each list item maps 1:1 to a tool, with keys: 

  * tool_id (required) 
  * description (required) 
  * Exactly one of: 
    * operation: full API Hub operation resource name 
    * http_operation: { spec, path, method } 

where `method` is one of GET, PUT, POST, DELETE, OPTIONS, HEAD, PATCH, TRACE. 



OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `apihub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha apihub locations configure-and-deploy-server](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/locations/configure-and-deploy-server)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
