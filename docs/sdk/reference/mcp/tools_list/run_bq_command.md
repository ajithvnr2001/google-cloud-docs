---
url: https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_bq_command/
title: MCP Tools Reference: cloudcli.googleapis.com \u00a0|\u00a0 Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:19:18.967130+00:00
---

# MCP Tools Reference: cloudcli.googleapis.com  |  Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_bq_command/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud SDK ](https://docs.cloud.google.com/sdk)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  MCP Tools Reference: cloudcli.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `run_bq_command`

Runs a single [BigQuery CLI (bq) command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference). This tool allows you to run any bq command in the user's project, including commands that create, update, or delete GCP resources (i.e., mutations).

**CRITICAL SAFETY WARNING (POTENTIALLY DESTRUCTIVE)** : This tool can create, update, or delete BigQuery resources (e.g., `bq rm`, `bq cancel`, `bq query`). It is NOT restricted to read-only commands. Use extreme caution.

**FORBIDDEN COMMANDS** : An agent MUST NOT execute the following bq commands: `bq init`, `bq pyshell`, `bq shell`.

**STRICT EXECUTION RULES** :

  1. At least one of `--project_id` or `--quota_project_id` MUST be specified in the command string.
  2. Project ID vs Quota Project: The --project_id flag specifies the resource project the command operates on (mirrors gcloud's --project flag). The --quota_project_id flag specifies the project charged for billing/quota of the downstream BigQuery API call (mirrors gcloud's `--billing-project` flag). If `--project_id` is specified in the command, it will be used as the billing/quota project. If `--project_id` is not specified OR `--quota_project_id` is additionally specified, the billing/quota project will be the project set in the `--quota_project_id` flag.
  3. Flag Formatting: You MUST always use an '=' sign to separate flag keys from their values for all long options. Correct: `'--project_id=my-project'` or `'--location=us'`. Incorrect: `'--project_id my-project'` or `'--location us'`. Do not use spaces between flags and their values.
  4. No Configuration Defaults: The bq command is executed in a stateless manner; it does not load local configuration files like .bigqueryrc. Therefore, for all regional operations (e.g., creating a dataset or querying a regional dataset), you MUST explicitly specify the `--location` flag (e.g., `--location=us` or `--location=EU`).
  5. Asynchronous Operations: Some commands initiate synchronous long-running operations (e.g., running query jobs). You SHOULD ALWAYS pass the `--nosync` flag for these commands to prevent agent timeouts.
  6. Command Restrictions: You MUST NOT use the following bq commands: `bq init`, `bq pyshell`, `bq shell`. Command piping or chaining is NOT supported.
  7. Self-Correction: If a command returns an error, analyze the stderr, correct the syntax or flags, and retry in the next iteration.



Examples of mutating bq commands include: `bq mk`, `bq rm`, `bq update`, `bq insert`, `bq query` (without `--dry_run`), etc. Usage: `RunBq(command="bq query --project_id=PROJECT_ID 'SELECT 1'", project="projects/PROJECT_ID", input_files=[{"path": "PATH", "contents": "CONTENTS"}])` You MUST provide the full bq command as a single string in the 'command' parameter. You MUST provide the 'project' parameter (format: projects/PROJECT_ID) as the API execution project for billing, API enablement, and quota consumption checks.

Example bq commands/patterns:

  1. Run a query: `bq query --use_legacy_sql=false --project_id=PROJECT_ID 'SELECT * FROM`project.dataset.table`LIMIT 10'`
  2. Create a dataset: `bq mk --dataset --location=us --project_id=PROJECT_ID myDataset`
  3. Create a table: `bq mk --table --project_id=PROJECT_ID myDataset.myTable name:string,value:integer`
  4. Remove a dataset: `bq rm -f --dataset --project_id=PROJECT_ID myDataset`
  5. Remove a table: `bq rm -f -t --project_id=PROJECT_ID myDataset.myTable`
  6. Update table description: `bq update --description="New description" --project_id=PROJECT_ID myDataset.myTable`
  7. List datasets in a project: `bq ls --datasets=true --project_id=PROJECT_ID`



The following code sample shows how to use `curl` to call the `run_bq_command` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudcli.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "run_bq_command",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for RunBq.

### RunBqRequest

JSON representation  
---  
      
    
    {
      "project": string,
      "command": string,
      "inputFiles": [
        {
          object ([File](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Input.Schema.File))
        }
      ]
    }  
  
Fields  
---  
`project` |  `string` Required. Project for api enablement and quota consumption for the CloudCli API.Format must be projects/ or projects/  
`command` |  `string` Required. The full bq command line to run as a single string. Example: "bq ls my-dataset --location=us"LLMs are instructed to use the `--nosync` flag for long-running operations to avoid timeouts.  
`inputFiles[]` |  `object (`[File](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Input.Schema.File)`)` Optional. Files to be made available to the bq command for its execution.  
  
### File

JSON representation  
---  
      
    
    {
      "path": string,
      "contents": string
    }  
  
Fields  
---  
`path` |  `string` Required. Filepath relative to the home directory. Must not contain parent directory traversal (..) or shell expansions.  
`contents` |  `string` Required. Contents of the file.  
  
## Output Schema

Response message for RunBq.

### RunBqResponse

JSON representation  
---  
      
    
    {
      "response": {
        object ([CliExecutionResponse](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Output.Schema.CliExecutionResponse))
      },
      "outputFiles": [
        {
          object ([File](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Input.Schema.File))
        }
      ]
    }  
  
Fields  
---  
`response` |  `object (`[CliExecutionResponse](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Output.Schema.CliExecutionResponse)`)` The response from the CLI tool execution, containing independent stdout, stderr stream and an exit code.  
`outputFiles[]` |  `object (`[File](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Input.Schema.File)`)` Files generated by the bq command from its execution.  
  
### CliExecutionResponse

JSON representation  
---  
      
    
    {
      "stdout": string,
      "stderr": string,
      "exitCode": string
    }  
  
Fields  
---  
`stdout` |  `string` The stdout stream from the CLI tool execution.  
`stderr` |  `string` The stderr stream from the CLI tool execution.  
`exitCode` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The exit code of the CLI tool execution.  
  
### File

JSON representation  
---  
      
    
    {
      "path": string,
      "contents": string
    }  
  
Fields  
---  
`path` |  `string` Required. Filepath relative to the home directory. Must not contain parent directory traversal (..) or shell expansions.  
`contents` |  `string` Required. Contents of the file.  
  
### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
