---
url: https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/
title: MCP Reference: securesourcemanager.googleapis.com \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:44.842739+00:00
---

# MCP Reference: securesourcemanager.googleapis.com  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-source-manager/docs/authentication)



Send feedback 

#  MCP Reference: securesourcemanager.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

An MCP server for interacting with Secure Source Manager resources.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Secure Source Manager MCP server only supports regional service endpoints. For the following toolset endpoints, replace LOCATION with a [region with MCP support](https://docs.cloud.google.com/secure-source-manager/docs/locations). For example, `https://securesourcemanager.us-central1.rep.googleapis.com/mcp`.

  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/branch_rule
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/code_review
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/hook
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/ide
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/instance
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/management
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/pull_request
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/repository
  * https://securesourcemanager.LOCATION.rep.googleapis.com/mcp/iam



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world. Toolsets are a group of tools that are useful for a specific task. Using toolsets can help your agent perform better because it decreases the number of tools available to your agent.

### Toolsets

The securesourcemanager.googleapis.com MCP server has the following toolsets:

MCP Toolsets  
---  
Endpoint | Description | Tools  
/mcp/branch_rule | This toolsets provides tools for working with branch protection rules. | `

  * [create_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule)
  * [delete_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_branch_rule)
  * [get_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_branch_rule)
  * [list_branch_rules](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_branch_rules)
  * [update_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_branch_rule)

`  
/mcp/code_review | This toolset provides tools for performing code reviews on open pull requests. | `

  * [batch_create_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/batch_create_pull_request_comments)
  * [get_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_pull_request)
  * [list_pull_requests](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_requests)
  * [list_pull_request_file_diffs](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_request_file_diffs)

`  
/mcp | This toolset provides all available tools, and shouldn't be used outside testing and development. | `

  * [close_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/close_pull_request)
  * [create_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_pull_request)
  * [list_pull_request_file_diffs](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_request_file_diffs)
  * [list_pull_requests](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_requests)
  * [merge_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/merge_pull_request)
  * [open_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/open_pull_request)
  * [update_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_pull_request)
  * [create_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_pull_request_comment)
  * [delete_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_pull_request_comment)
  * [get_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_pull_request_comment)
  * [list_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_request_comments)
  * [resolve_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/resolve_pull_request_comments)
  * [unresolve_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/unresolve_pull_request_comments)
  * [update_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_pull_request_comment)
  * [get_instance](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_instance)
  * [list_instances](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_instances)
  * [create_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_repository)
  * [get_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_repository)
  * [list_repositories](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_repositories)
  * [update_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_repository)
  * [create_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule)
  * [delete_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_branch_rule)
  * [get_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_branch_rule)
  * [list_branch_rules](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_branch_rules)
  * [update_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_branch_rule)
  * [create_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_hook)
  * [delete_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_hook)
  * [get_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_hook)
  * [list_hooks](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_hooks)
  * [update_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_hook)
  * [get_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_pull_request)
  * [batch_create_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/batch_create_pull_request_comments)
  * [get_securesourcemanager_instance_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_securesourcemanager_instance_iam_policy)
  * [set_securesourcemanager_instance_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/set_securesourcemanager_instance_iam_policy)
  * [test_securesourcemanager_instance_iam_permissions](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/test_securesourcemanager_instance_iam_permissions)
  * [get_securesourcemanager_repository_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_securesourcemanager_repository_iam_policy)
  * [set_securesourcemanager_repository_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/set_securesourcemanager_repository_iam_policy)
  * [test_securesourcemanager_repository_iam_permissions](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/test_securesourcemanager_repository_iam_permissions)

`  
/mcp/hook | This toolset provides tools for working with hooks. | `

  * [create_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_hook)
  * [delete_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_hook)
  * [get_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_hook)
  * [list_hooks](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_hooks)
  * [update_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_hook)

`  
/mcp/ide | This toolset provides tools for common workflows in an integrated development environment. | `

  * [create_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_pull_request)
  * [get_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_pull_request)
  * [list_pull_requests](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_requests)
  * [merge_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/merge_pull_request)
  * [resolve_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/resolve_pull_request_comments)

`  
/mcp/instance | This toolset provides tools for fetching information about instances. | `

  * [get_instance](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_instance)
  * [list_instances](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_instances)

`  
/mcp/management | This toolset provides tools for managing instances and repositories. | `

  * [get_instance](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_instance)
  * [list_instances](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_instances)
  * [get_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_repository)
  * [list_repositories](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_repositories)
  * [update_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_repository)
  * [create_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_hook)
  * [delete_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_hook)
  * [get_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_hook)
  * [list_hooks](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_hooks)
  * [update_hook](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_hook)
  * [create_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule)
  * [delete_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_branch_rule)
  * [get_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_branch_rule)
  * [list_branch_rules](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_branch_rules)
  * [update_branch_rule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_branch_rule)

`  
/mcp/pull_request | This toolset provides tools for working with pull requests. | `

  * [close_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/close_pull_request)
  * [create_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_pull_request)
  * [get_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_pull_request)
  * [list_pull_requests](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_requests)
  * [list_pull_request_file_diffs](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_request_file_diffs)
  * [merge_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/merge_pull_request)
  * [open_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/open_pull_request)
  * [update_pull_request](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_pull_request)
  * [batch_create_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/batch_create_pull_request_comments)
  * [create_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_pull_request_comment)
  * [delete_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/delete_pull_request_comment)
  * [get_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_pull_request_comment)
  * [list_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_pull_request_comments)
  * [resolve_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/resolve_pull_request_comments)
  * [unresolve_pull_request_comments](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/unresolve_pull_request_comments)
  * [update_pull_request_comment](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_pull_request_comment)

`  
/mcp/repository | This toolset provides tools for working with repositories. | `

  * [create_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_repository)
  * [get_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_repository)
  * [list_repositories](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/list_repositories)
  * [update_repository](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_repository)

`  
/mcp/iam | IAM management APIs for v1 access control policies. | `

  * [get_securesourcemanager_instance_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_securesourcemanager_instance_iam_policy)
  * [set_securesourcemanager_instance_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/set_securesourcemanager_instance_iam_policy)
  * [test_securesourcemanager_instance_iam_permissions](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/test_securesourcemanager_instance_iam_permissions)
  * [get_securesourcemanager_repository_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/get_securesourcemanager_repository_iam_policy)
  * [set_securesourcemanager_repository_iam_policy](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/set_securesourcemanager_repository_iam_policy)
  * [test_securesourcemanager_repository_iam_permissions](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/test_securesourcemanager_repository_iam_permissions)

`  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications available within the MCP server in the `europe-west4` region. Replace `europe-west4` with a [region with MCP support](https://docs.cloud.google.com/secure-source-manager/docs/locations) where your instance is located. 

Curl Request  
---  
      
    
    curl --location 'https://securesourcemanager.europe-west4.rep.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
