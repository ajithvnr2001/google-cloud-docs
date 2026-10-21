---
url: https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command/
title: MCP Tools Reference: cloudcli.googleapis.com \u00a0|\u00a0 Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:06:34.658941+00:00
---

# MCP Tools Reference: cloudcli.googleapis.com  |  Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud SDK ](https://docs.cloud.google.com/sdk)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  MCP Tools Reference: cloudcli.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `run_gcloud_command`

Executes a single gcloud CLI command within the user's Google Cloud project.

**CRITICAL SAFETY WARNING (POTENTIALLY DESTRUCTIVE)** : This tool can create, update, or delete GCP resources (e.g., gcloud compute instances delete). It is NOT restricted to read-only commands. Use extreme caution.

**FORBIDDEN COMMANDS** : An agent MUST NOT execute the following gcloud commands (including their alpha/beta variants): `app deploy`, `app instances ssh`, `auth`, `billing`, `components`, `config`, `docker`, `feedback`, `info`, `init`, `meta`, `survey`.

**STRICT EXECUTION RULES** :

  1. You MUST provide the 'project' parameter (i.e. project="projects/PROJECT_ID") when using this tool (it is used for Cloud CLI Execution API enablement check, billing, quota, etc.). This is NOT the same as the --project flag in gcloud commands used to specify the project gcloud operates on.
  2. Flag Formatting: You MUST always use an '=' sign to separate flag keys from their values for all long options. Correct: `--zone=us-central1-a` or `--project=my-project`. Incorrect: `--zone us-central1-a` or `--project my-project`.
  3. Billing Project: You cannot assume any pre-configured project or billing settings in the execution environment. For non-project scoped commands (e.g., folder or organization level) or specific scenarios like Cloud Storage Requester Pays, you MUST pass the `--billing-project=PROJECT` flag. For project-scoped commands, you MAY additionally specify `--billing-project=PROJECT` to override the quota project, which will take effect for GCP APIs that do not support resource-project-override.
  4. Project Scope: You SHOULD ALWAYS pass the `--project=PROJECT_ID` flag for project-scoped commands. Do not use it for organization or folder-level commands. If you do not provide a `--project flag` for a project-scoped command, the resource project will default to the project set in the `--billing-project` flag.
  5. If specifying `--billing-project` flag in the gcloud command, ensure that the value is a project ID or a project number. The value MUST NOT be a special value (ie LEGACY, CURRENT_PROJECT, CURRENT_PROJECT_WITH_FALLBACK).
  6. At least one of `--project` or `--billing-project` MUST be specified in the command string.
  7. Asynchronous Operations: For long-running synchronous operations (e.g., creating a VM or a database), you SHOULD ALWAYS pass the `--async` flag to prevent agent timeouts.
  8. Log Rate Limiting: When using `gcloud logging read`, you MUST ALWAYS include a `--limit` flag (e.g., `--limit=100`) to prevent credential and connection timeouts.
  9. Self-Correction: If a command returns an error, analyze the stderr, correct the syntax or flags, and retry in the next iteration.
  10. input_files: (Optional) A list of files to be created in the environment before running the command. Each file must have a 'path' (relative to the current directory) and 'contents'. The 'contents' must be plain text representing the file's content. This is useful for commands that read from files (e.g. `gcloud builds submit --config=cloudbuild.yaml --async --project=PROJECT_ID`).



Example gcloud commands/patterns:

  1. Read GCE instance logs with severity>=ERROR: `gcloud logging read "severity>=ERROR AND resource.type='gce_instance'" --limit=10 --order=DESC --project=PROJECT_ID`
     * Note the use of quotes for the filter expression.
  2. List all PSC endpoints: `gcloud compute forwarding-rules list --project=PROJECT_ID`
  3. Describe a PSC endpoint: `gcloud compute forwarding-rules describe FORWARDING_RULE_NAME --region=REGION --project=PROJECT_ID`
     * Note the use of '=' for the --region flag.
  4. List all clusters: `gcloud container clusters list --project=PROJECT_ID`
  5. Describe a cluster: `gcloud container clusters describe CLUSTER_NAME --region=REGION --project=PROJECT_ID`
  6. List compute instances: `gcloud compute instances list --project=PROJECT_ID`
  7. Get IAM policy for a project: `gcloud projects get-iam-policy PROJECT_ID --project=PROJECT_ID`



Response strings are formatted for terminal output by default (stdout or stderr). Use --format flag to change the format.

The following code sample shows how to use `curl` to call the `run_gcloud_command` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudcli.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "run_gcloud_command",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for RunGcloud.

### RunGcloudRequest

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
`project` |  `string` Required. Project for api enablement and quota consumption for the Cloud CLI Execution API.Format must be projects/ or projects/  
`command` |  `string` Required. The full gcloud command line to run as a single string. Example: "gcloud compute instances create my-vm --zone=us-central1-a"LLMs are instructed to use the `--async` flag for long-running operations to avoid timeouts.  
`inputFiles[]` |  `object (`[File](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Input.Schema.File)`)` Optional. Files to be made available to the gcloud command for its execution.  
  
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

Response message for RunGcloud.

### RunGcloudResponse

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
`outputFiles[]` |  `object (`[File](https://docs.cloud.google.com/sdk/reference/mcp/tools_list/run_gcloud_command#Input.Schema.File)`)` Files generated by the gcloud command from its execution.  
  
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
