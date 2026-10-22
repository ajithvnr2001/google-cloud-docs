---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server/
title: Configure the Mainframe Assessment Tool MCP server and agent skills \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:26.795184+00:00
---

# Configure the Mainframe Assessment Tool MCP server and agent skills  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Configure the Mainframe Assessment Tool MCP server and agent skills Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set up and interact with the Mainframe Assessment Tool MCP server and install the `mat-backend-query` agent skill. By using the MCP server and the `mat-backend-query` skill, you can explore business domains, search for assets, and retrieve complexity and dependency metrics from your mainframe assessments by using natural language prompts. To interact with the MCP server, connect through AI agents or Model Context Protocol (MCP) clients, such as [Antigravity](https://antigravity.google/).

By using the Mainframe Assessment Tool MCP server, you can do the following:

  * List and view existing assessments.
  * Explore business domains discovered in your assessments.
  * Search and filter assets based on different criteria.
  * Retrieve asset specifications, including dependencies and complexity metrics.
  * Query call trees, DB2 and database table usage, and dataset I/O metrics from PostgreSQL materialized views by using the `mat-backend-query` skill.



For more information on MCP, see [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro).

## Before you begin

Before you enable and connect to the MCP server, complete the following tasks:

  * **Create an assessment.** You can enable the MCP server and install the `mat-backend-query` skill at any time, but querying assessment data requires at least one completed assessment in Mainframe Assessment Tool. For more information, see [Create an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment).
  * **Grant necessary permissions.** The permissions you need depend on your Mainframe Assessment Tool deployment environment: 
    * On a Compute Engine VM instance, you need permission to set custom metadata on the instance. For details on the required roles, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).
    * On a GKE cluster, you need permission to update deployments in the cluster, and you must configure the `kubectl` command-line tool to connect to the cluster. For more information, see [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).
  * **Set up Google Cloud CLI.** Install and configure the latest version of the Google Cloud CLI. For more information, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).



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
    

Replace VERSION with the Mainframe Assessment Tool version deployed on the cluster. This version is also the deployment's namespace (for example, mainframe-assessment-2-8-0).

Updating the environment variable restarts the Mainframe Assessment Tool pod with the MCP server enabled. Since Mainframe Assessment Tool runs as a single pod, it is briefly unavailable while the new pod starts. To disable the MCP server, set the `MAT_ENABLE_MCP` environment variable to `false`.

## Connect to the MCP server

You can connect to the MCP server using standard AI agents that support MCP connections over streamable HTTP.

To open these configuration instructions directly from Mainframe Assessment Tool, follow these steps:

  1. In Mainframe Assessment Tool, go to the **Assessments** page.
  2. In the toolbar, click **Use with Antigravity** , and then select **Configure MCP**.



The MCP server is located under the `/mcp/` route on the same port used to access the Mainframe Assessment Tool UI. For more information, see [Access Mainframe Assessment Tool VM from your computer](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance#set-up-access-vm) or [Access GKE-deployed Mainframe Assessment Tool from your computer](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-instance#set-up-access-gke).

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

## Install and use the Mainframe Assessment Tool agent skill

Mainframe Assessment Tool provides the `mat-backend-query` agent skill for [Antigravity](https://antigravity.google/docs/skills/) that lets you analyze program call trees, inter-module dependencies, database table access patterns, and dataset I/O usage in your assessment by using natural language prompts instead of writing SQL queries. To query data with this skill, you must first [create an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment) in Mainframe Assessment Tool.

### Download and extract the skill

To download and extract the `mat-backend-query` agent skill, follow these steps:

  1. In Mainframe Assessment Tool, go to the **Assessments** page.
  2. In the toolbar, click **Use with Antigravity** , and then select **Download Skill**. Your browser downloads a ZIP file named `skill.zip`.
  3. On your computer, open a terminal and go to your local Antigravity project directory. If the `.agents/skills` directory doesn't exist, create it, and then extract `skill.zip`:
         
         cd PROJECT_ROOT
         mkdir -p .agents/skills
         unzip PATH_TO_ZIP/skill.zip -d .agents/
         

Replace the following:

     * `PROJECT_ROOT`: the path to the local project directory on your computer where you run Antigravity.
     * `PATH_TO_ZIP`: the path to the directory where you downloaded the `skill.zip` file.
  4. Confirm that the extracted files in `PROJECT_ROOT` match the following directory structure:
         
         PROJECT_ROOT/
         └── .agents/
             └── skills/
                 ├── README.md
                 └── mat-backend-query/
                     ├── SKILL.md
                     └── references/
                         └── schemas.md
         




### Verify the skill in Antigravity

To verify that Antigravity detects the MCP server and the `mat-backend-query` skill, follow these steps:

  1. Launch Antigravity from your `PROJECT_ROOT` directory so that it discovers the `.agents/skills/` directory.
  2. In Antigravity chat, run the `/mcp` command to verify that the `mainframe-assessment-tool` MCP server is connected and exposes the `db_query_tool` tool.
  3. Run the `/skills` command to confirm that the `mat-backend-query` skill is loaded.
  4. If you have already completed an assessment in Mainframe Assessment Tool, test the skill by entering the following prompt:
         
         Using the mat-backend-query skill, query 5 rows from mat_views.called_dependency for assessment 'ASSESSMENT_ID'.
         

Replace `ASSESSMENT_ID` with the ID of your assessment.




## MCP server tools

The Mainframe Assessment Tool MCP server provides tools that enable AI agents to retrieve data from your assessments.

### `ListAssessments`

Lists all assessments on the Mainframe Assessment Tool instance. Each assessment includes its name, ID, description, and timestamps.

### `ListDomains`

Lists the domains for a given Mainframe Assessment Tool assessment ID. Each domain includes its name, description, and ID.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
  
### `ListAssets`

Lists the assets for a given Mainframe Assessment Tool assessment ID. Each asset includes its ID, name, path, type, and assigned domain IDs.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
  
### `FetchDomain`

Fetches the domain details for a given domain ID and Mainframe Assessment Tool assessment ID. Domain details include ID, name, description, and summary.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`DomainId` | string | Yes | The ID of the Mainframe Assessment Tool domain.  
  
### `FetchAsset`

Fetches the specification summary for an asset for a given Mainframe Assessment Tool assessment ID. The asset specification includes its ID, name, usage, description, ETL graph, and BMS maps.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`AssetId` | string | Yes | The ID of the Mainframe Assessment Tool asset.  
`DetailedSpec` | boolean | No (default: `false`) | If set to true, the response also includes method specifications with their test cases.  
  
### `FetchAssetsCyclomaticComplexity`

Fetches the cyclomatic complexity scores for a list of assets for a given Mainframe Assessment Tool assessment ID.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`AssetIds` | string[] | Yes | List of Mainframe Assessment Tool assets IDs.  
  
### `SearchContent`

Searches across source code, AI-generated specifications, and business rules within a specific mainframe assessment. It supports keyword-based (`bm25`), semantic (`embedding`), and hybrid (`hybrid`) search modes, allowing users to locate relevant assets and documentation.

The tool can filter results by document type (`source`, `spec`, or `bre`), limit the number of returned matches, and optionally retrieve the full content of matching documents.

#### Arguments

The following table describes the arguments for this tool:

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

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`Query` | string | Yes | The question or query for data exploration.  
  
### `ListBusinessRulesExtractionJobs`

Lists the Business Rules Jobs for a given Mainframe Assessment Tool assessment ID. The returned list includes each job's ID, name, status, focus prompt, and more.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
  
### `ListBusinessRules`

Lists the business rules extracted by a specific business rules extraction job ID and Mainframe Assessment Tool assessment ID. To handle large numbers of rules, this action supports pagination.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`JobId` | string | Yes | The ID of the business rules extraction job.  
`PageSize` | string | No | The size of the page to fetch. Maximum supported value is `25`.  
`PageToken` | string | No | The token of the page to fetch. This value was returned by a previous call to this action.  
`OrderList` | object | No | The order in which to return the results. See the per-field descriptions.  
`OrderList.OrderBy` | string | No | The name of the field to order the results based on. Examples: `business_rule_id`, `business_rule_name`, `status`.  
`OrderList.Order` | string | No | The direction of the order. Supported values are: `ASCENDING`, `DESCENDING`.  
`Filter` | object | No | Filter the returned results. See the per-field descriptions.  
`Filter.Status` | string | No | The business rules status to filter by. Supported values are: `PENDING`, `VALIDATED`, `OBSOLETE`.  
`Filter.Tags` | string[] | No | List of tags associated with the business rules.  
`Filter.AssetIDs` | string[] | No | List of Mainframe Assessment Tool asset IDs associated with the business rules.  
  
### `FetchJobSpec`

Fetches the business rules extraction (BRE) job specification for a Mainframe Assessment Tool assessment ID.

#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`AssessmentId` | string | Yes | The ID of the Mainframe Assessment Tool assessment.  
`JobId` | string | Yes | The ID of the business rules extraction (BRE) job.  
  
### `db_query_tool`

Runs direct, read-only PostgreSQL `SELECT` queries against the Mainframe Assessment Tool `mat_views` schema and returns up to 10,000 rows as a JSON array.

Use the `mat-backend-query` skill with this tool so that the agent follows required rules:

  * Every query must filter by a specific assessment ID (`WHERE assessment_id = 'ASSESSMENT_ID'`).
  * Only `SELECT` statements against views in the `mat_views` schema are allowed.
  * Queries must include an explicit `LIMIT` clause.



#### Arguments

The following table describes the arguments for this tool:

Name | Type | Required | Description  
---|---|---|---  
`query` | string | Yes | The read-only PostgreSQL `SELECT` query to run against the `mat_views` schema (maximum 10,000 rows returned).  
  
#### Available materialized views

The following table describes the PostgreSQL materialized views in the `mat_views` schema that you can query with `db_query_tool`:

View | Description | Key columns  
---|---|---  
`mat_views.called_dependency` | Program call trees and inter-module dependencies across mainframe applications, system utilities, and unresolved external programs. | `assessment_id`, `calling_module`, `calling_module_type`, `called_module`, `called_module_type`, `call_count`  
`mat_views.databases` | Database usage metrics and table access operations performed by mainframe programs, including DB2 tables and unparsed tables. | `assessment_id`, `database_name`, `table_name`, `program_name`, `access_type`, `sql_statements_count`, `is_db2`  
`mat_views.datasets` | Mainframe Dataset Name (DSN) file I/O usage and JCL job-to-step mappings, including shared datasets bridging multiple jobs. | `assessment_id`, `dataset_name`, `job_name`, `step_name`, `dd_name`, `program_name`, `io_operation`, `is_shared_bridge`  
  
## Usage examples

The following are examples of natural language prompts that an AI agent can answer by using the MCP server tools and the `mat-backend-query` skill to retrieve and process assessment data:

  * **Scenario** : find complex programs in an assessment. 
    * **User prompt** : _"List the 10 most complex COBOL programs in the assessment called`AssessmentName`."_
  * **Scenario** : find and filter assets that belong to a business domain. 
    * **User prompt** : _"List all the JCL jobs related to the`DomainName` domain under the assessment called `AssessmentName`."_
  * **Scenario** : get asset dependencies from an assessment. 
    * **User prompt** : _"What are the dependencies of the JCL job`JCLJobName` in the assessment called `AssessmentName`?"_
  * **Scenario** : find the extracted business rules from a specific job. 
    * **User prompt** : _"List all business rules extracted by`BusinessRuleJobName` in the assessment called `AssessmentName`."_
  * **Scenario** : explore assessment data using natural language. 
    * **User prompt** : _"Explain how the data processing flow works for the billing system in the assessment called`AssessmentName`."_
  * **Scenario** : query program call trees using the `mat-backend-query` skill. 
    * **User prompt** : _"Using the mat-backend-query skill, find the top 10 most frequently called modules and their caller types for assessment ' ASSESSMENT_ID'."_
  * **Scenario** : analyze database table access and dataset usage using the `mat-backend-query` skill. 
    * **User prompt** : _"Using the mat-backend-query skill, list all DB2 tables accessed with write or update operations in assessment ' ASSESSMENT_ID'."_



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
