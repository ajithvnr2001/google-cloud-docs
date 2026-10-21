---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/
title: MCP Reference: saasservicemgmt \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:11.718034+00:00
---

# MCP Reference: saasservicemgmt  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  MCP Reference: saasservicemgmt Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The App Lifecycle Manager API MCP server has the following MCP endpoint:

  * https://saasservicemgmt.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The saasservicemgmt MCP server has the following tools:

MCP Tools  
---  
[list_saas](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_saas) |  Lists Saas resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_saas](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_saas) |  Gets a Saas resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/saas/my-saas).   
[create_saas](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_saas) |  Creates a Saas resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'saas_id', 'saas'. Optional parameters: 'validate_only', 'request_id'.   
[list_tenants](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_tenants) |  Lists Tenant resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_tenant](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_tenant) |  Gets a Tenant resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/tenants/my-tenant).   
[create_tenant](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_tenant) |  Creates a Tenant resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'tenant_id', 'tenant'. Optional parameters: 'validate_only', 'request_id'.   
[list_unit_kinds](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_kinds) |  Lists UnitKind resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_unit_kind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_unit_kind) |  Gets a UnitKind resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/unitKinds/my-unitkind).   
[create_unit_kind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_unit_kind) |  Creates a UnitKind resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'unit_kind_id', 'unit_kind'. Optional parameters: 'validate_only', 'request_id'.   
[list_units](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_units) |  Lists Unit resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_unit](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_unit) |  Gets a Unit resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/units/my-unit).   
[create_unit](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_unit) |  Creates a Unit resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'unit_id', 'unit'. Optional parameters: 'validate_only', 'request_id'.   
[list_unit_operations](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_unit_operations) |  Lists UnitOperation resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_unit_operation](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_unit_operation) |  Gets a UnitOperation resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/unitOperations/my-unitoperation).   
[list_releases](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_releases) |  Lists Release resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_release](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_release) |  Gets a Release resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/releases/my-release).   
[create_release](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_release) |  Creates a Release resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'release_id', 'release'. Optional parameters: 'validate_only', 'request_id'.   
[list_rollouts](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollouts) |  Lists Rollout resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_rollout](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_rollout) |  Gets a Rollout resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/rollouts/my-rollout).   
[list_rollout_kinds](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_rollout_kinds) |  Lists RolloutKind resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_rollout_kind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_rollout_kind) |  Gets a RolloutKind resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/rolloutKinds/my-rolloutkind).   
[create_rollout_kind](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_rollout_kind) |  Creates a RolloutKind resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'rollout_kind_id', 'rollout_kind'. Optional parameters: 'validate_only', 'request_id'.   
[list_maintenances](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_maintenances) |  Lists Maintenance resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_maintenance](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_maintenance) |  Gets a Maintenance resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/maintenances/my-maintenance).   
[create_maintenance](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_maintenance) |  Creates a Maintenance resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'maintenance_id', 'maintenance'. Optional parameters: 'validate_only', 'request_id'.   
[list_resource_maintenances](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_resource_maintenances) |  Lists ResourceMaintenance resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_resource_maintenance](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_resource_maintenance) |  Gets a ResourceMaintenance resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/resourceMaintenances/my-resourcemaintenance).   
[list_flags](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flags) |  Lists Flag resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_flag) |  Gets a Flag resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/flags/my-flag).   
[create_flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_flag) |  Creates a Flag resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'flag_id', 'flag'. Optional parameters: 'validate_only', 'request_id'.   
[list_flag_revisions](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_revisions) |  Lists FlagRevision resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_flag_revision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_flag_revision) |  Gets a FlagRevision resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/flagRevisions/my-flagrevision).   
[create_flag_revision](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_flag_revision) |  Creates a FlagRevision resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'flag_revision_id', 'flag_revision'. Optional parameters: 'validate_only', 'request_id'.   
[list_flag_releases](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_releases) |  Lists FlagRelease resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_flag_release](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_flag_release) |  Gets a FlagRelease resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/flagReleases/my-flagrelease).   
[create_flag_release](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_flag_release) |  Creates a FlagRelease resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'flag_release_id', 'flag_release'. Optional parameters: 'validate_only', 'request_id'.   
[list_flag_attributes](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/list_flag_attributes) |  Lists FlagAttribute resources. Required parameter: 'parent' (e.g. projects/my-project/locations/us-central1). Optional parameters: 'page_size', 'page_token', 'filter', 'order_by'.   
[get_flag_attribute](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/get_flag_attribute) |  Gets a FlagAttribute resource. Required parameter: 'name' (e.g. projects/my-project/locations/us-central1/flagAttributes/my-flagattribute).   
[create_flag_attribute](https://docs.cloud.google.com/app-lifecycle-manager/reference/mcp/alm/mcp/tools_list/create_flag_attribute) |  Creates a FlagAttribute resource. Required parameters: 'parent' (e.g. projects/my-project/locations/us-central1), 'flag_attribute_id', 'flag_attribute'. Optional parameters: 'validate_only', 'request_id'.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          
    curl --location 'https://saasservicemgmt.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
