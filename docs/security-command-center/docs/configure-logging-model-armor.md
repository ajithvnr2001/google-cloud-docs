---
url: https://docs.cloud.google.com/security-command-center/docs/configure-logging-model-armor/
title: Configure logging \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:11:39.104133+00:00
---

# Configure logging  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/configure-logging-model-armor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Configure logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Model Armor to log the following operations:

  * Operations that create, update, or delete a template
  * Operations that sanitize a user prompt or model response



Model Armor uses audit logs to record administrative and resource management activities. For more information, see [Model Armor audit logging](https://docs.cloud.google.com/model-armor/audit-logging-model-armor).

For information about log pricing, see the [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing). Model Armor usage charges might also apply based on the volume of data processed; see [Model Armor Pricing](https://cloud.google.com/security-command-center/pricing#model-armor-pricing) for details.

## Before you begin

Before you begin, complete the following tasks.

### Obtain the required permissions

To get the permissions that you need to configure logging for Model Armor, ask your administrator to grant you the [Model Armor Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`) IAM role on the Model Armor template. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

You must enable the Model Armor API before you can use Model Armor.

###  Console 

  1. Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

  2. Select the project where you want to activate Model Armor.




###  gcloud 

Before you begin, follow these steps using the Google Cloud CLI with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the Model Armor API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable modelarmor.googleapis.com

  3. Set the API endpoint override using the gcloud CLI.




### Set the API endpoint override using the gcloud CLI

This step is only required if you use the gcloud CLI with Model Armor and want to use a region or multi-region other than the default `us` multi-region. You must manually set the API endpoint override to ensure the gcloud CLI correctly routes requests to the Model Armor service.

Run the following command to set the API endpoint for the Model Armor service.
    
    
    gcloud config set api_endpoint_overrides/modelarmor "https://modelarmor.LOCATION.rep.googleapis.com/"

Replace `LOCATION` with the [region or multi-region where you want to use Model Armor](https://docs.cloud.google.com/model-armor/data-residency#data-residency-enforced).

### Set up traffic sanitization

For Google and Google Cloud MCP servers, set up traffic sanitization through floor settings. For more information, see [Configure protection for Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration#configure-protection-mcp).

## Configure logging in templates

Templates define the filters and thresholds for different safety and security categories. When you create or update a [Model Armor template](https://docs.cloud.google.com/model-armor/manage-templates), you can specify whether Model Armor logs certain operations. Use the following flags in the template metadata:

  * `log_template_operations`: A boolean value that lets you log the create, update, read, and delete template operations.
  * `log_sanitize_operations`: A boolean value that lets you log the full content of user prompts and model responses during sanitize operations.



###  Console 

  1. In the Google Cloud console, go to the **Model Armor** page.

[Go to Model Armor](https://console.cloud.google.com/security/modelarmor)

  2. Verify that you are viewing the project for which you activated Model Armor.

  3. On the **Model Armor** page, click **Create Template**. For more information about creating templates, see [Create a Model Armor template](https://docs.cloud.google.com/model-armor/manage-templates#create-ma-template).

  4. In the **Configure logging** section, select the operations for which you want to configure logging.

  5. Click **Create**.




###  REST 
    
    
      curl -X POST \
          -d '{ "filterConfig": {}, "templateMetadata": { "logTemplateOperations": true, "logSanitizeOperations": true } }' \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates?template_id=TEMPLATE_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that the template belongs to.
  * `LOCATION`: the [location](https://docs.cloud.google.com/model-armor/locations) of the template.
  * `TEMPLATE_ID`: the ID of the template.



###  Python 

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Model Armor Python SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).
    
    
       request = modelarmor_v1.CreateTemplateRequest(
         parent="projects/PROJECT_ID/locations/LOCATION",
         template_id="TEMPLATE_ID",
         template={
            "name": "projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID",
            "filter_config": {},
            "template_metadata": {
               "log_template_operations": True,
               "log_sanitize_operations": True
            }
         }
       )
       response = client.create_template(request=request)
       

Replace the following:

  * `PROJECT_ID`: the ID of the project that the template belongs to.
  * `LOCATION`: the [location](https://docs.cloud.google.com/model-armor/locations) of the template.
  * `TEMPLATE_ID`: the ID of the template.



## Configure logging in floor settings

When you enforce floor settings on traffic from Gemini models in Gemini Enterprise Agent Platform and Google and Google Cloud MCP servers within your project, floor settings define the safety and security filters for sanitization operations. When you are updating [Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings), you can specify whether Model Armor logs sanitize operations.

You can enable logging of sanitize operations for Agent Platform and Google and Google Cloud MCP servers individually. When enabled, logs include the prompt and response (for Agent Platform) or tool calls and tool responses (for MCP servers), Model Armor's evaluation results, and additional metadata fields.

**Note:** In the Google Cloud console, floor settings logging for sanitize operations is enabled by default for Agent Platform, but disabled by default for MCP servers.

If you have data residency requirements, you must configure a log sink to route logs to a compliant storage location before you enable Cloud Logging in the next procedure. Configuring a log sink helps ensure that Model Armor stores logs in the appropriate regional buckets. For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).

The following examples show how to enable sanitize operations logging for both Agent Platform and Google and Google Cloud MCP servers.

###  Console 

  1. In the Google Cloud console, go to the **Model Armor** page.

[Go to Model Armor](https://console.cloud.google.com/security/modelarmor)

  2. Verify that you are viewing the project for which you activated Model Armor.

  3. Navigate to the **Floor Settings** tab.

  4. In the **Logs** section, select the **Vertex AI** and **Google managed MCP** checkboxes to enable logging for each service.

  5. Click **Save**.




###  gcloud 

Use the `--enable-vertex-ai-cloud-logging` flag to enable logging for Agent Platform, and the `--enable-google-mcp-server-cloud-logging` flag to enable logging for Google and Google Cloud MCP servers. To disable logging, use the `--no-enable-vertex-ai-cloud-logging` and `--no-enable-google-mcp-server-cloud-logging` flags.

The following example command enables sanitize operations logging for both Agent Platform and Google and Google Cloud MCP servers:
    
    
    gcloud model-armor floorsettings update \
    --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
    --enable-vertex-ai-cloud-logging \
    --enable-google-mcp-server-cloud-logging
    

Replace `PROJECT_ID` with the ID of your project.

###  REST 

To enable logging, set `aiPlatformFloorSetting.enableCloudLogging` to `true` for Agent Platform and `googleMcpServerFloorSetting.enableCloudLogging` to `true` for Google and Google Cloud MCP servers in the `UpdateFloorSetting` method.

The following example command enables sanitize operations logging for both Agent Platform and Google and Google Cloud MCP servers:
    
    
    curl -X PATCH \
     -d '{ "aiPlatformFloorSetting":{ "enableCloudLogging": true}, "googleMcpServerFloorSetting":{ "enableCloudLogging": true}}' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://modelarmor.googleapis.com/v1/projects/PROJECT_ID/locations/global/floorSetting?updateMask=aiPlatformFloorSetting.enableCloudLogging,googleMcpServerFloorSetting.enableCloudLogging"
    

Replace `PROJECT_ID` with the ID of your project.

###  Python 

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Model Armor Python SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).
    
    
    from google.cloud.modelarmor import v1 as modelarmor_v1
    from google.protobuf import field_mask_pb2
    
    # TODO: Initialize the ModelArmorClient, "client"
    # client = modelarmor_v1.ModelArmorClient()
    
    project_id = "PROJECT_ID"
    location = "global"
    
    floor_setting_name = f"projects/{project_id}/locations/{location}/floorSetting"
    
    request = modelarmor_v1.UpdateFloorSettingRequest(
        floor_setting=modelarmor_v1.FloorSetting(
            name=floor_setting_name,
            ai_platform_floor_setting=modelarmor_v1.FloorSetting.AiPlatformFloorSetting(
                enable_cloud_logging=True
            ),
            google_mcp_server_floor_setting=modelarmor_v1.FloorSetting.GoogleMcpServerFloorSetting(
                enable_cloud_logging=True
            ),
        ),
        update_mask=field_mask_pb2.FieldMask(
            paths=["ai_platform_floor_setting.enable_cloud_logging", "google_mcp_server_floor_setting.enable_cloud_logging"]
        )
    )
    
    try:
        response = client.update_floor_setting(request=request)
        print("Successfully updated floor settings logging.")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    

Replace `PROJECT_ID` with the ID of your project.

## View and filter Model Armor logs

To view and filter Model Armor logs, use the Logs Explorer in Logging:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

For more information, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  2. In the query pane, enter one of the following queries to filter Model Armor logs:

     * To view all Model Armor logs, including audit logs and sanitization operation logs:
           
           protoPayload.serviceName="modelarmor.googleapis.com" OR jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
           

     * To view only Model Armor audit logs:
           
           protoPayload.serviceName="modelarmor.googleapis.com"
           

For a list of all the service names and monitored resource types, see [Monitored resources and services](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

     * To view only Model Armor logs for sanitization operations:
           
           jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
           

To further refine the sanitization operation logs, you can specify a client name, correlation ID, or [exclusion rule](https://docs.cloud.google.com/model-armor/configure-exclusion-rules) ([Preview](https://cloud.google.com/products#product-launch-stages)) evaluation label in the query:

       * Using a client name: When Model Armor integrates with services like Gemini Enterprise Agent Platform or Gemini Enterprise, you can use the client name to filter logs for a specific integration.
             
             jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
             labels."modelarmor.googleapis.com/client_name"="CLIENT_NAME"
             

       * Using a correlation ID:
             
             jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
             labels."modelarmor.googleapis.com/client_correlation_id"="CORRELATION_ID"
             

Replace the following:

         * `CLIENT_NAME`: the name of your client. Use one of the following values:

           * `CLIENT_NAME_UNSPECIFIED`: Default value, used when the client name isn't specified.
           * `VERTEX_AI`: For integration with Gemini Enterprise Agent Platform.
           * `LOAD_BALANCER`: For integration using load balancer as a service extension.
           * `LANGCHAIN`: For integration with LangChain.
           * `GEMINI_ENTERPRISE_BUSINESS`: For integration with Gemini Enterprise - Business edition.
           * `GOOGLE_MCP_SERVER`: For integration with Google and Google-managed MCP servers.
           * `AGENT_GATEWAY`: For integration with Agent Gateway.
           * `GEMINI_ENTERPRISE_NON_BUSINESS`: For integration with Gemini Enterprise editions other than Business (Standard, Plus, and Frontline).
           * `SECURE_WEB_PROXY`: For integration with Secure Web Proxy.
         * `CORRELATION_ID`: the unique identifier that you generate for a specific request.

       * Using [exclusion rule](https://docs.cloud.google.com/model-armor/configure-exclusion-rules) ([Preview](https://cloud.google.com/products#product-launch-stages)) labels: When an exclusion rule overrides a filter result or when Model Armor skips exclusion rule evaluation, Model Armor populates the following optional top-level `labels` fields on `modelarmor.googleapis.com/SanitizeOperation` log entries:

         * `modelarmor.googleapis.com/exclusion_rule_overridden_filters`: a comma-separated list of filters whose `MATCH_FOUND` or `EXECUTION_SKIPPED` results were overridden to `NO_MATCH_FOUND` because an exclusion rule matched.
         * `modelarmor.googleapis.com/exclusion_rule_skipped_filters`: a comma-separated list of filters whose exclusion rule evaluation was skipped (for example, when an input exceeds the 130,000 tokens (0.5 MB) [exclusion payload limit](https://docs.cloud.google.com/model-armor/quotas#exclusion-rules-limits)).

Use the following sample queries to filter sanitization logs by exclusion rule labels:

         * To find requests where a filter result was overridden by an exclusion rule:
    
    jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
    labels."modelarmor.googleapis.com/exclusion_rule_overridden_filters":"FILTER_NAME"
    

         * To find requests where a prompt injection and jailbreak detection was overridden by an exclusion rule:
    
    jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
    labels."modelarmor.googleapis.com/exclusion_rule_overridden_filters"="PROMPT_INJECTION_AND_JAILBREAK"
    

         * To find requests where exclusion rule evaluation was skipped:
    
    jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
    labels."modelarmor.googleapis.com/exclusion_rule_skipped_filters"="FILTER_NAME"
    

Replace `FILTER_NAME` with the name of the filter (`PROMPT_INJECTION_AND_JAILBREAK` or `RESPONSIBLE_AI`).




## Correlate logs and related events

To correlate logs and events for a specific interaction, you can use a Model Armor client correlation ID. This ID is a unique identifier that you generate (for example, a UUID) that tracks a specific request across your system. To set a client correlation ID in a curl header, use the `-H` option to include a `MA-Client-Correlation-Id` custom header in your request.

Here's the sample format:
    
    
    uuid=$(uuidgen) \
    curl -X POST -d  '{"userPromptData": { "text": "USER_PROMPT" } }' \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "MA-Client-Correlation-Id:${uuid}" \
        "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeUserPrompt"
    
    curl -X POST \
        -d  '{"modelResponseData": { "text": "MODEL_RESPONSE" }, "userPrompt": "USER_PROMPT" }' \
        -H "Content-Type: application/json" \
        -H "MA-Client-Correlation-Id:${uuid}" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeModelResponse"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that the template belongs to.
  * `LOCATION`: the [location](https://docs.cloud.google.com/model-armor/locations) of the template.
  * `TEMPLATE_ID`: the ID of the template.
  * `USER_PROMPT`: the prompt provided to the model.
  * `MODEL_RESPONSE`: the response received from the model.



## Platform logs versus Cloud Audit Logs

It's important to distinguish between the logs that you can enable within a Model Armor template or floor settings and Cloud Audit Logs.

Feature | Cloud Audit Logs | Platform logs  
---|---|---  
Primary purpose | Security auditing of API calls (who did what, when) and compliance monitoring. | Operational monitoring, debugging, and detailed analysis of sanitization events.  
API operations captured | Create, read, update, delete, and list operations on templates and floor settings. Sanitize operations (`SanitizeUserPrompt`, `SanitizeModelResponse`) are logged as metadata. | Captures all requests such as `SanitizeUserPrompt` and `SanitizeModelResponse`.  
Payload content | Does not include the actual user prompt or model response text for sanitize operations. Contains metadata like the caller, method, resource, timestamp, and status. | Includes the full payload, such as the prompt or response text, filter results, and other details of the sanitization.  
Enabling mechanism | Standard Google Cloud IAM audit logs settings for the Model Armor API. Data access logs often require explicit enablement. Audit logs for template operations are generated automatically. | Enabled by setting the boolean flag `log_sanitize_operations` in the template metadata or floor settings.  
Logging conditions | Logs create, read, update, delete, and list operations on templates and floor settings automatically. | Logs data (user prompts and model responses) for any dataplane requests, regardless of whether Sensitive Data Protection is enabled or if any filter setting was matched.  
Log volume and cost | Generally smaller and more predictable, incurring standard Cloud Logging pricing. | Can be very large and voluminous, potentially leading to significant Cloud Logging costs due to large payloads and frequent use. Large payloads might be split into multiple log entries.  
Security considerations | Relatively safe as payload data is not logged. Requires special IAM permissions to access (for example, specific IAM roles to view audit logs). | Contains potentially sensitive user data (PII, confidential information). Accessible to anyone with log viewing permissions (for example, `roles/logging.privateLogViewer`).  
Recommendation | Enable for general security and compliance monitoring. | Not recommended for production or sensitive data unless securely routed to an access-controlled sink (for example, BigQuery with strict IAM).  
  
Enabling logging in a template writes raw prompts and responses to Logging. This data might include sensitive user data, personally identifiable information (PII), or confidential information. High traffic and large payloads can lead to substantial logging costs and potential for large log volumes exceeding limits and requiring careful management.

## Caller identity in audit logs

When you view audit logs, Cloud Audit Logs captures the identity of the caller in the `protoPayload.authenticationInfo.principalEmail` field. The identity recorded depends on how the Model Armor API is called:

  * **Direct API invocation** : If a user or service account calls the Model Armor API directly (for example, by using `gcloud`, client libraries, or REST APIs), then `principalEmail` contains the email address of that user or service account.
  * **Invocation through an integrated Google Cloud service** : If Model Armor integrates with another Google Cloud service such as Gemini Enterprise Agent Platform, then `principalEmail` contains that service's identity, which is typically a Google-managed service account. The format for service agents is `service-PROJECT_NUMBER@SERVICE_NAME.iam.gserviceaccount.com`. For example, a call that originates from a Gemini Enterprise Agent Platform feature uses a Gemini Enterprise Agent Platform service agent.



To distinguish between callers, examine the `principalEmail` field in the audit log entry. Calls from end-users or user-managed service accounts show their email addresses, while calls through other Google Cloud services show Google-managed service account email addresses.

## What's next

  * [Correlate Model Armor logs with Gemini Enterprise logs](https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
