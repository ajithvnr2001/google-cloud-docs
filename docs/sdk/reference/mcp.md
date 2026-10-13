---
url: https://docs.cloud.google.com/sdk/reference/mcp/
title: MCP Reference: cloudcli.googleapis.com \u00a0|\u00a0 Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:52.254048+00:00
---

# MCP Reference: cloudcli.googleapis.com  |  Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud SDK ](https://docs.cloud.google.com/sdk)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  MCP Reference: cloudcli.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud CLI MCP Server provides tools to run Google Cloud CLI commands in a remote sandbox environment.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud CLI Execution API MCP server has the following global MCP endpoint:

  * https://cloudcli.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The cloudcli.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[run_gcloud_command](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command)` |  Executes a single gcloud CLI command within the user's Google Cloud project.**CRITICAL SAFETY WARNING (POTENTIALLY DESTRUCTIVE)** : This tool can create, update, or delete Google Cloud resources (e.g., gcloud compute instances delete). It is NOT restricted to read-only commands. Use extreme caution.**FORBIDDEN COMMANDS** : An agent MUST NOT execute the following gcloud commands (including their alpha/beta variants): `app deploy`, `app instances ssh`, `auth`, `billing`, `components`, `config`, `docker`, `feedback`, `info`, `init`, `meta`, `survey`.**STRICT EXECUTION RULES** :

  1. You MUST provide the 'project' parameter (i.e. project="projects/PROJECT_ID") when using this tool (it is used for Cloud CLI Execution API enablement check, billing, quota, etc.). This is NOT the same as the --project flag in gcloud commands used to specify the project gcloud operates on.
  2. Flag Formatting: You MUST always use an '=' sign to separate flag keys from their values for all long options. Correct: `--zone=us-central1-a` or `--project=my-project`. Incorrect: `--zone us-central1-a` or `--project my-project`.
  3. Billing Project: You cannot assume any pre-configured project or billing settings in the execution environment. For non-project scoped commands (e.g., folder or organization level) or specific scenarios like Cloud Storage Requester Pays, you MUST pass the `--billing-project=PROJECT` flag. For project-scoped commands, you MAY additionally specify `--billing-project=PROJECT` to override the quota project, which will take effect for Google Cloud APIs that do not support resource-project-override.
  4. Project Scope: You SHOULD ALWAYS pass the `--project=PROJECT_ID` flag for project-scoped commands. Do not use it for organization or folder-level commands. If you do not provide a `--project flag` for a project-scoped command, the resource project will default to the project set in the `--billing-project` flag.
  5. If specifying `--billing-project` flag in the gcloud command, ensure that the value is a project ID or a project number. The value MUST NOT be a special value (ie LEGACY, CURRENT_PROJECT, CURRENT_PROJECT_WITH_FALLBACK).
  6. At least one of `--project` or `--billing-project` MUST be specified in the command string.
  7. Asynchronous Operations: For long-running synchronous operations (e.g., creating a VM or a database), you SHOULD ALWAYS pass the `--async` flag to prevent agent timeouts.
  8. Log Rate Limiting: When using `gcloud logging read`, you MUST ALWAYS include a `--limit` flag (e.g., `--limit=100`) to prevent credential and connection timeouts.
  9. Self-Correction: If a command returns an error, analyze the stderr, correct the syntax or flags, and retry in the next iteration.
  10. input_files: (Optional) A list of files to be created in the environment before running the command. Each file must have a 'path' (relative to the current directory) and 'contents'. The 'contents' must be plain text representing the file's content. This is useful for commands that read from files (e.g. `gcloud builds submit --config=cloudbuild.yaml --async --project=PROJECT_ID`).

Example gcloud commands/patterns:

  1. Read Compute Engine instance logs with severity>=ERROR: `gcloud logging read "severity>=ERROR AND resource.type='gce_instance'" --limit=10 --order=DESC --project=PROJECT_ID`
     * Note the use of quotes for the filter expression.
  2. List all PSC endpoints: `gcloud compute forwarding-rules list --project=PROJECT_ID`
  3. Describe a PSC endpoint: `gcloud compute forwarding-rules describe FORWARDING_RULE_NAME --region=REGION --project=PROJECT_ID`
     * Note the use of '=' for the --region flag.
  4. List all clusters: `gcloud container clusters list --project=PROJECT_ID`
  5. Describe a cluster: `gcloud container clusters describe CLUSTER_NAME --region=REGION --project=PROJECT_ID`
  6. List compute instances: `gcloud compute instances list --project=PROJECT_ID`
  7. Get IAM policy for a project: `gcloud projects get-iam-policy PROJECT_ID --project=PROJECT_ID`

Response strings are formatted for terminal output by default (stdout or stderr). Use --format flag to change the format.  
`[run_bq_command](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_bq_command)` |  Runs a single [BigQuery CLI (bq) command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference). This tool allows you to run any bq command in the user's project, including commands that create, update, or delete Google Cloud resources (i.e., mutations).**CRITICAL SAFETY WARNING (POTENTIALLY DESTRUCTIVE)** : This tool can create, update, or delete BigQuery resources (e.g., `bq rm`, `bq cancel`, `bq query`). It is NOT restricted to read-only commands. Use extreme caution.**FORBIDDEN COMMANDS** : An agent MUST NOT execute the following bq commands: `bq init`, `bq pyshell`, `bq shell`.**STRICT EXECUTION RULES** :

  1. At least one of `--project_id` or `--quota_project_id` MUST be specified in the command string.
  2. Project ID vs Quota Project: The --project_id flag specifies the resource project the command operates on (mirrors gcloud's --project flag). The --quota_project_id flag specifies the project charged for billing/quota of the downstream BigQuery API call (mirrors gcloud's `--billing-project` flag). If `--project_id` is specified in the command, it will be used as the billing/quota project. If `--project_id` is not specified OR `--quota_project_id` is additionally specified, the billing/quota project will be the project set in the `--quota_project_id` flag.
  3. Flag Formatting: You MUST always use an '=' sign to separate flag keys from their values for all long options. Correct: `'--project_id=my-project'` or `'--location=us'`. Incorrect: `'--project_id my-project'` or `'--location us'`. Do not use spaces between flags and their values.
  4. No Configuration Defaults: The bq command is executed in a stateless manner; it does not load local configuration files like .bigqueryrc. Therefore, for all regional operations (e.g., creating a dataset or querying a regional dataset), you MUST explicitly specify the `--location` flag (e.g., `--location=us` or `--location=EU`).
  5. Asynchronous Operations: Some commands initiate synchronous long-running operations (e.g., running query jobs). You SHOULD ALWAYS pass the `--nosync` flag for these commands to prevent agent timeouts.
  6. Command Restrictions: You MUST NOT use the following bq commands: `bq init`, `bq pyshell`, `bq shell`. Command piping or chaining is NOT supported.
  7. Self-Correction: If a command returns an error, analyze the stderr, correct the syntax or flags, and retry in the next iteration.

Examples of mutating bq commands include: `bq mk`, `bq rm`, `bq update`, `bq insert`, `bq query` (without `--dry_run`), etc. Usage: `RunBq(command="bq query --project_id=PROJECT_ID 'SELECT 1'", project="projects/PROJECT_ID", input_files=[{"path": "PATH", "contents": "CONTENTS"}])` You MUST provide the full bq command as a single string in the 'command' parameter. You MUST provide the 'project' parameter (format: projects/PROJECT_ID) as the API execution project for billing, API enablement, and quota consumption checks.Example bq commands/patterns:

  1. Run a query: `bq query --use_legacy_sql=false --project_id=PROJECT_ID 'SELECT * FROM`project.dataset.table`LIMIT 10'`
  2. Create a dataset: `bq mk --dataset --location=us --project_id=PROJECT_ID myDataset`
  3. Create a table: `bq mk --table --project_id=PROJECT_ID myDataset.myTable name:string,value:integer`
  4. Remove a dataset: `bq rm -f --dataset --project_id=PROJECT_ID myDataset`
  5. Remove a table: `bq rm -f -t --project_id=PROJECT_ID myDataset.myTable`
  6. Update table description: `bq update --description="New description" --project_id=PROJECT_ID myDataset.myTable`
  7. List datasets in a project: `bq ls --datasets=true --project_id=PROJECT_ID`

  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://cloudcli.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
