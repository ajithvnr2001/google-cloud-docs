---
url: https://docs.cloud.google.com/apigee/docs/apihub/gcloud-cli-apihub/
title: gcloud CLI for API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:27.131883+00:00
---

# gcloud CLI for API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/gcloud-cli-apihub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  gcloud CLI for API hub Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to install, authorize, and use the gcloud CLI for API hub. 

The `**gcloud CLI apihub**` component lets you to manage your API resources within API hub directly from the command line. This includes registering APIs, creating versions and specifications, managing deployments, and configuring attributes or plugins. 

## Before you begin

Install [Google Cloud SDK](https://docs.cloud.google.com/sdk/install). Alternatively, you can use the [Google Cloud Shell](https://console.cloud.google.com/?cloudshell=true), which comes with the SDK pre-installed.

##  Authenticate for the gcloud CLI 

See [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts) for instructions on how to authenticate. 

For example, to authorize access using your user account and perform other common Cloud SDK setup steps, use the following command: 
    
    
    gcloud CLI init

Follow the prompts to authenticate the account, grant access permissions, and initialize your Cloud SDK installation, as described in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize). 

Alternatively, to authorize access without performing any additional set up, use the following command: 
    
    
    gcloud CLI auth login

Follow the browser-based authorization flow to authenticate the account and grant access permissions. For more information about authorizing and revoking access to the gcloud CLI, see [Credentials](https://docs.cloud.google.com/sdk/docs/cheatsheet#credentials).

## Set up environment variables for gcloud CLI commands

Using environment variables can simplify your CLI commands. The following variables are commonly used in API hub operations: 

Environment variable | Description  
---|---  
`$PROJECT` | Your Google Cloud project ID.  
`$LOCATION` | The location of your API hub resources (for example, `us-central1`).  
`$API` | The ID of your API resource.  
`$VERSION` | The ID of a specific API version.  
`$SPEC` | The ID of an API specification.  
`$DEPLOYMENT` | The ID of an API deployment.  
  
## Use the gcloud CLI 

The basic structure for API hub commands is as follows: 
    
    
    gcloud CLI apihub [GROUP](https://docs.cloud.google.com/sdk/gcloud%20CLI/reference/apihub#GROUP) [[gcloud CLI_WIDE_FLAG](https://docs.cloud.google.com/sdk/gcloud%20CLI/reference/apihub#gcloud%20CLI-WIDE-FLAGS) …]

### Common command groups

The following table lists some common command groups for the `gcloud CLI apihub` CLI. 

Command group | Description  
---|---  
`apis` | Manage top-level API resources.  
`apis versions` | Manage versions associated with an API.  
`apis versions specs` | Manage API specifications.  
`deployments` | Manage API deployments.  
`attributes` | Manage user-defined and system attributes.  
`runtime-project-attachments` | Manage attachments for runtime projects.  
  
For more information about the available command groups and flags, see [gcloud CLI apihub](https://docs.cloud.google.com/sdk/gcloud/reference/apihub). 

### API management commands

The following examples show how to use common `gcloud CLI apihub` commands:

  * **Registering an API**
        
        gcloud CLI apihub apis create --api="my-api" --display-name="My New API" --project=$PROJECT --location=$LOCATION

**Note:** To create a new API, you must specify a display name and an ID using the `--api` flag. 
  * **Listing APIs**
        
        gcloud CLI apihub apis list --project=$PROJECT --location=$LOCATION

  * **Adding a version to an API**
        
        gcloud CLI apihub apis versions create "v1" --api="my-api" --display-name="Version 1.0" --project=$PROJECT --location=$LOCATION

You can specify the version as a positional argument or using the `--version` flag. 

  * **Uploading a specification**
        
        gcloud CLI apihub apis versions specs create "openapi-spec" --api="my-api" --version="v1" --display-name="OpenAPI 3.0 Spec" --contents='{"openapi": "3.0.0", ...}' --contents-mime-type="application/json" --project=$PROJECT --location=$LOCATION




## Configure and deploy an API hub MCP server

Use the following command to configure and deploy an API hub MCP server on an attached Apigee runtime:
    
    
    gcloud CLI apihub locations configure-and-deploy-server

**Note:** If a proxy with the specified `--apigee-x-proxy` name already exists in the target Apigee environment, this command creates a new revision of that proxy and completely replaces the previous revision's tool set. To avoid losing tools, ensure that your command includes the complete set of tools intended for the server. 

The following examples demonstrate how to configure and deploy an API hub MCP server on Apigee runtime.

### Deploy an MCP server with a single tool

Use this command to reference a single tool inline by its full operation resource name:
    
    
    gcloud CLI apihub locations configure-and-deploy-server LOCATION \
        --project=PROJECT_ID \
        --mcp-tools='tool-id=TOOL_ID,description=TOOL_DESCRIPTION,operation=OPERATION_RESOURCE_NAME' \
        --apigee-x-environment=APIGEE_ENVIRONMENT \
        --apigee-x-proxy=PROXY_NAME \
        --apigee-x-target-project=TARGET_PROJECT_ID

Replace `LOCATION` with the location of your API hub resources. For example, `us-central1`.

### Deploy an MCP server from a tools specification file

This method is required for tools that reference an HTTP operation by specification resource name, path, and HTTP method, as the inline `--mcp-tools` form cannot express this structure:
    
    
    gcloud CLI apihub locations configure-and-deploy-server LOCATION \
        --project=PROJECT_ID \
        --mcp-tools-from-file=FILE_PATH \
        --apigee-x-environment=APIGEE_ENVIRONMENT \
        --apigee-x-proxy=PROXY_NAME \
        --apigee-x-target-project=TARGET_PROJECT_ID

Replace `LOCATION` with the location of your API hub resources. For example, `us-central1`.

In the `tools.yaml` file, use one of the following tool types:

  * `operation`: Specify the full API hub operation resource name.
  * `http_operation`: Specify the specification resource name, path, and HTTP method.



For example:
    
    
    - tool_id: TOOL_ID_1
      description: TOOL_DESCRIPTION_1
      operation: OPERATION_RESOURCE_NAME_1
    
    
    - tool_id: TOOL_ID_2
      description: TOOL_DESCRIPTION_2
      http_operation:
        spec: SPEC_RESOURCE_NAME
        path: API_PATH
        method: HTTP_METHOD

### Use comma-containing values (alternate delimiter)

When any flag value contains a comma (such as a tool description), use the `^DELIM^` alternate-delimiter syntax:
    
    
    gcloud CLI apihub locations configure-and-deploy-server LOCATION \
        --project=PROJECT_ID \
        --mcp-tools='^|^tool-id=TOOL_ID|description=TOOL_DESCRIPTION_WITH_COMMAS|operation=OPERATION_RESOURCE_NAME' \
        --apigee-x-environment=APIGEE_ENVIRONMENT \
        --apigee-x-proxy=PROXY_NAME \
        --apigee-x-target-project=TARGET_PROJECT_ID

Replace `LOCATION` with the location of your API hub resources. For example, `us-central1`. 

### Deploy an MCP server asynchronously

For longer-running deployments, deploy the server asynchronously by using the `--async` flag:
    
    
    gcloud CLI apihub locations configure-and-deploy-server LOCATION \
        --project=PROJECT_ID \
        --mcp-tools='tool-id=TOOL_ID,description=TOOL_DESCRIPTION,operation=OPERATION_RESOURCE_NAME' \
        --apigee-x-environment=APIGEE_ENVIRONMENT \
        --apigee-x-proxy=PROXY_NAME \
        --apigee-x-target-project=TARGET_PROJECT_ID \
        --async
    

Replace `LOCATION` with the location of your API hub resources. For example, `us-central1`.

Poll the returned OPERATION_ID by using the following command:
    
    
    gcloud CLI apihub operations describe OPERATION_ID \
        --location=LOCATION --project=PROJECT_ID

### Add a display name and description

Use this command to add a display name and description to the proxy:
    
    
    gcloud CLI apihub locations configure-and-deploy-server LOCATION \
        --project=PROJECT_ID \
        --mcp-tools-from-file=FILE_PATH \
        --apigee-x-environment=APIGEE_ENVIRONMENT \
        --apigee-x-proxy=PROXY_NAME \
        --apigee-x-target-project=TARGET_PROJECT_ID \
        --apigee-x-proxy-display-name='PROXY_DISPLAY_NAME' \
        --apigee-x-proxy-description='PROXY_DESCRIPTION'

Replace `LOCATION` with the location of your API hub resources. For example, `us-central1`.

## Considerations

  * Creating resources without specifying an ID is not supported in the CLI.
  * The `--filter` flag performs client-side filtering. gcloud CLI fetches all resources from the backend and then filters them locally, which may impact performance for large collections.
  * For the `apis create` and `update` commands, you must use the `--api` flag to specify the resource ID. Positional arguments for IDs are not supported for the top-level API resource.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
