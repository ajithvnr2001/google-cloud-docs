---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server/
title: Enable the Mainframe Assessment Tool MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:08.737657+00:00
---

# Enable the Mainframe Assessment Tool MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Enable the Mainframe Assessment Tool MCP server Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set up and interact with the Mainframe Assessment Tool MCP server. You can explore business domains, search for assets, and retrieve complexity metrics from your mainframe assessments by using natural language prompts. To interact with the MCP server, connect through AI agents or Model Context Protocol (MCP) clients, such as [Antigravity](https://antigravity.google/).

For example, you can do the following:

  * List and view existing assessments.
  * Explore business domains discovered in your assessments.
  * Search and filter assets based on different criteria.
  * Retrieve asset specifications, including dependencies and complexity metrics.



For more information on MCP, see [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro).

## Before you begin

To prepare for enabling and connecting to the MCP server, complete the following tasks:

  * **Familiarize yourself with Mainframe Assessment Tool.** make sure that you have already used Mainframe Assessment Tool to run an assessment.
  * **Grant necessary permissions.** The permissions you need depend on how you deployed Mainframe Assessment Tool: 
    * On a Compute Engine VM instance, you need permission to set custom metadata on the instance. For details on the required roles, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).
    * On a GKE cluster, you need permission to update deployments in the cluster, and you must configure the `kubectl` command-line tool to connect to the cluster. For more information, see [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).
  * **Set up Google Cloud CLI.** install and configure the latest version of the Google Cloud CLI. For more information, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).



## Enable the MCP server

The MCP server is disabled by default. To enable the MCP server, follow the instructions for your deployment environment.

### On a Compute Engine instance

To enable the MCP server on your Mainframe Assessment Tool Compute Engine instance, add the `MAT_ENABLE_MCP` metadata key and set its value to `true` by running the following `gcloud` command:
    
    
        gcloud compute instances add-metadata INSTANCE_NAME \
        --metadata=MAT_ENABLE_MCP=true \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of your VM instance.
  * `ZONE`: the zone where your VM instance is located.



If you set the metadata key on a running VM, you must restart the VM for the changes to take effect.

### On a GKE cluster

To enable the MCP server on a GKE deployment, set the `MAT_ENABLE_MCP` environment variable on the `mcp-server` container to `true`:
    
    
    kubectl set env deployment/mat-apps --containers=mcp-server \
        MAT_ENABLE_MCP=true --namespace=VERSION
    

Replace VERSION with the Mainframe Assessment Tool version deployed on the cluster. This version is also the deployment's namespace (for example, mainframe-assessment-2-8-0). Updating the environment variable restarts the Mainframe Assessment Tool pod with the MCP server enabled. Because Mainframe Assessment Tool runs as a single pod, it is briefly unavailable while the new pod starts. To disable the MCP server, set the `MAT_ENABLE_MCP` environment variable to `false`.

## Connect to the MCP server

You can connect to the MCP server using standard AI agents that support MCP connections over Streamable HTTP.

The MCP server is located under the /mcp/ route on the same port used to access the Mainframe Assessment Tool UI. For more information, see [Access Mainframe Assessment Tool VM from your computer](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance#set-up-access-vm) or [Access GKE-deployed Mainframe Assessment Tool from your computer](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance#set-up-access-gke).

#### Configuration examples

The following sections provide examples of how to configure different AI agents to connect to the MCP server.

Replace LOCAL_PORT with the local port used for accessing the Mainframe Assessment Tool UI.

##### Antigravity

To use [Antigravity](https://antigravity.google/), configure the MCP server in the `mcp_config.json` file as follows:
    
    
    {
      "mcpServers": {
        "mainframe-assessment-tool": {
          "serverUrl": "http://localhost:LOCAL_PORT/mcp/"
        }
      }
    }
    

For more information, see [Model Context Protocol (MCP)](https://antigravity.google/docs/mcp).

## MCP server tools

The Mainframe Assessment Tool MCP server provides tools that enable AI agents to retrieve data from your assessments.

### `ListAssessments`

Lists all assessments on the Mainframe Assessment Tool instance. Each assessment includes its name, ID, description, and timestamps.

### `ListDomains`

Lists the domains for a given Mainframe Assessment Tool assessment ID. Each domain includes its name, description, and ID.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
  
### `ListAssets`

Lists the assets for a given Mainframe Assessment Tool assessment ID. Each asset includes its ID, name, path, type, and assigned domain IDs.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
  
### `FetchDomain`

Fetches the domain details for a given domain ID and Mainframe Assessment Tool assessment ID. Domain details include ID, name, description, and summary.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`DomainId` | string | Yes | The ID of the Mainframe Assessment Tool domain.  
  
### `FetchAsset`

Fetches the specification summary for an asset for a given Mainframe Assessment Tool assessment ID. The asset specification includes its ID, name, usage, description, ETL graph, and BMS maps.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`AssetId` | string | Yes | The ID of the Mainframe Assessment Tool asset.  
`DetailedSpec` | boolean | No (default: `false`) | If is set to true, the response also includes method specifications with their test cases.  
  
### `FetchAssetsCyclomaticComplexity`

Fetches the cyclomatic complexity scores for a list of assets for a given Mainframe Assessment Tool assessment ID.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`AssetIds` | string[] | Yes | List of Mainframe Assessment Tool assets IDs.  
  
### `SearchContent`

Searches across source code, AI-generated specifications, and business rules within a specific mainframe assessment. It supports keyword-based (`bm25`), semantic (`embedding`), and hybrid (`hybrid`) search modes, allowing users to locate relevant assets and documentation.

The tool can filter results by document type (`source`, `spec`, or `bre`), limit the number of returned matches, and optionally retrieve the full content of matching documents.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`Query` | string | Yes | The search query.  
`DocTypes` | string[] | No | Filter results by document type. Supported values are: `source`, `spec`, or `bre`.  
`Limit` | integer | No | Limit the number of returned matches.  
`IncludeContent` | boolean | No | If set to true, the response also includes the full content of matching documents. Default value is `false`.  
`SearchMode` | string | No | The search mode to use. Supported values are: `bm25` (keyword-based), `embedding` (semantic), or `hybrid`. Default value is `hybrid`.  
  
### `ExploreData`

Runs an interactive AI agent (Data Explorer) that acts as a data analyst for your assessment. The agent can query the underlying structured database of a specific assessment to answer complex questions.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`Query` | string | Yes | The question or query for data exploration.  
  
### `ListBusinessRulesExtractionJobs`

Lists the Business Rules Jobs for a given Mainframe Assessment Tool assessment ID. The returned list includes each job's ID, name, status, focus prompt and more.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
  
### `ListBusinessRules`

Lists the business rules extracted by a specific business rules extraction job ID and Mainframe Assessment Tool assessment ID. To handle the large number of rules, this action supports pagination.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`JobId` | string | Yes | The ID of the business rules extraction job.  
`PageSize` | string | No | The size of the page to fetch. Maximum supported value is `25`.  
`PageToken` | string | No | The token of the page to fetch. This value was returned by a previous call to this action.  
`OrderList` | object | No | The order in which to return the results. See the per-field descriptions.  
`OrderList.OrderBy` | string | No | The name of the field to order the results based on. Examples: business_rule_id, business_rule_name, status.  
`OrderList.Order` | string | No | The direction of the order. Supported values are: ASCENDING, DESCENDING.  
`Filter` | object | No | Filter the returned results. See the per-field descriptions.  
`Filter.Status` | string | No | The business rules status to filter by. Supported values are: PENDING, VALIDATED, OBSOLETE.  
`Filter.Tags` | string[] | No | List of tags associated with the business rules.  
`Filter.AssetIDs` | string[] | No | List of Mainframe Assessment Tool asset IDs associated with the business rules.  
  
### `FetchJobSpec`

Fetches the business rules extraction (BRE) job specification for a Mainframe Assessment Tool assessment ID.

#### Arguments

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`JobId` | string | Yes | The ID of the business rules extraction (BRE) job.  
  
## Usage Examples

The following are examples of natural language prompts that an AI agent can answer by using the MCP server tools to retrieve and process assessment data:

  * Scenario: Find complex programs in an assessment.
  * User prompt: _"List the 10 most complex COBOL programs in the assessment called`AssessmentName`."_   
  

  * Scenario: Find and filter assets that belong to a business domain.
  * User prompt: _"List all the JCL jobs related to the`DomainName` domain under the assessment called `AssessmentName`."_   
  

  * Scenario: Get asset dependencies from an assessment.
  * User prompt: _"What are the dependencies of the JCL job`JCLJobName` in the assessment called `AssessmentName`?"_   
  

  * Scenario: Find the extracted business rules from the certain job.
  * User prompt: _"List all business rules extracted by`BusinessRuleJobName` in the assessment called `AssessmentName`."_   
  

  * Scenario: Explore assessment data using natural language.
  * User prompt: _"Explain how the data processing flow works for the billing system in the assessment called`AssessmentName`."_



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
