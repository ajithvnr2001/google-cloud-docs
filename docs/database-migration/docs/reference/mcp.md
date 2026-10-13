---
url: https://docs.cloud.google.com/database-migration/docs/reference/mcp/
title: MCP Reference: datamigration \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:25.210645+00:00
---

# MCP Reference: datamigration  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  MCP Reference: datamigration Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration MCP service

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Database Migration API MCP server has the following global MCP endpoint:

  * https://datamigration.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The datamigration MCP server has the following tools:

MCP Tools  
---  
`[list_static_ips](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_static_ips)` |  When you migrate a database into Google Cloud using DMS, Google needs a way to securely connect to your source database to read the data. If you choose the Static-IP connectivity method to connect to your source database, you will need to allow incoming traffic from DMS's specific, trusted IPs. This tool lists the IP addresses (matching the provided resource name) that should be allowlisted by the customer.

  * The resource `name` parameter is in the form `projects/{project name}/locations/{location}`, for example: `projects/my-project/locations/us-central1`.

  
`[list_migration_jobs](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs)` |  Lists the migration jobs of the provided parent with optional filters.

  * Parent parameter is in the form `projects/{project name}/locations/{location}`, for example: `projects/my-project/locations/us-central1`.
  * You can use any, some or all of the additional parameters to filter the results.
  * You can specify in the 'pageSize' parameter the maximum number of migration jobs to return. The tool may return fewer than this value. If more jobs are available, a 'nextPageToken' value is returned and you can use it in the next call to retrieve the next page of results. If unspecified, at most 50 migration jobs will be returned. The maximum value is 100; values above 100 are coerced to 100.
  * If no 'nextPageToken' is returned, there are no more migration jobs to retrieve.
  * Not all the details of the migration jobs are returned.
  * To get the full details of a specific job use the 'get_migration_job' tool.

For example: `{ create_time_after: 2025-10-02T10:15:33Z create_time_before: 2025-10-03T00:00:00Z display_name: hr running: true page_size: 80 } ` will return up to 80 migration jobs that were created on or after 2025-10-02T10:15:33 UTC and before 2025-10-03T00:00:00 UTC and have `hr` in their display name and are currently running. If there are more than 80 such jobs, a `nextPageToken` value (like `CgtteS1qb2IxM`) will be returned and you can use it in the next call to retrieve the next page of results.  
`[get_operation](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/get_operation)` |  Gets the status of a long-running operation.**Usage** Some tools (for example, `start_migration_job`) return a long-running operation. You can use this tool to get the status of the operation. It can be called repeatedly until the operation is complete.**Parameters**

  * `name`: The name of the operation to get. 
    * `name` should be the name returned by the tool that initiated the operation.
    * `name` should be in the format of: `projects/{project}/locations/{location}/operations/{operation}`.

**Returns**

  * An `Operation` object that contains the status of the operation.
  * If the operation is not complete, the response will be empty. Use a command line tool to pause for 10 seconds before rechecking the status.
  * If the operation is complete, the response will contain either: 
    * A `response` field that contains the result of the operation and indicates that it was successful.
    * A `error` field that indicates any errors that occurred during the operation.

  
`[get_migration_job](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/get_migration_job)` |  Get details of the migration job specified by the provided resource `name` parameter.

  * The resource `name` parameter is in the form: `projects/{project name}/locations/{location}/migrationJobs/{migration job name}`, for example: `projects/my-project/locations/us-central1/migrationJobs/my-migration-job`.

  
`[start_migration_job](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/start_migration_job)` |  Starts an already created migration job, specified by the provided resource `name` parameter.

  * The resource `name` parameter is in the form: `projects/{project name}/locations/{location}/migrationJobs/{migration job name}`, for example: `projects/my-project/locations/us-central1/migrationJobs/my-migration-job`.
  * Use the optional 'skipValidation' parameter to specify whether to start the migration job without running prior configuration verification. The default is 'false'.
  * This tool returns a long-running operation. Use the 'get_operation' tool with the returned operation name to poll its status until it completes. Operation may take several minutes; use a command line tool to pause for 10 seconds before rechecking the status as needed.

  
`[stop_migration_job](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/stop_migration_job)` |  Stops an already started migration job, specified by the provided resource `name` parameter.

  * The resource `name` parameter is in the form: `projects/{project name}/locations/{location}/migrationJobs/{migration job name}`, for example: `projects/my-project/locations/us-central1/migrationJobs/my-migration-job`.
  * This tool returns a long-running operation. Use the 'get_operation' tool with the returned operation name to poll its status until it completes. Operation may take several minutes; use a command line tool to pause for 10 seconds before rechecking the status as needed.

  
`[resume_migration_job](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/resume_migration_job)` |  Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). Migration job is specified by the provided resource `name` parameter.

  * The resource `name` parameter is in the form: `projects/{project name}/locations/{location}/migrationJobs/{migration job name}`, for example: `projects/my-project/locations/us-central1/migrationJobs/my-migration-job`.
  * Use the optional 'skipValidation' parameter to specify whether to resume the migration job without running prior configuration verification. The default is 'false'.
  * This tool returns a long-running operation. Use the 'get_operation' tool with the returned operation name to poll its status until it completes. Operation may take several minutes; use a command line tool to pause for 10 seconds before rechecking the status as needed.

  
`[delete_migration_job](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/delete_migration_job)` |  Deletes a migration job, specified by the provided resource `name` parameter.

  * The resource `name` parameter is in the form: `projects/{project name}/locations/{location}/migrationJobs/{migration job name}`, for example: `projects/my-project/locations/us-central1/migrationJobs/my-migration-job`.
  * This tool returns a long-running operation. Use the 'get_operation' tool with the returned operation name to poll its status until it completes. Operation may take several minutes; use a command line tool to pause for 10 seconds before rechecking the status as needed.

  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          
    curl --location 'https://datamigration.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
