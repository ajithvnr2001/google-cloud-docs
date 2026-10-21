---
url: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/design_infra/
title: MCP Tools Reference: geminicloudassist.googleapis.com \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:55.495112+00:00
---

# MCP Tools Reference: geminicloudassist.googleapis.com  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/design_infra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  MCP Tools Reference: geminicloudassist.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : The Gemini Cloud Assist MCP server is in private preview. Use of this Preview offering is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805). To request access to the private preview, contact your Google Cloud account manager.

## Tool: `design_infra`

Design Agent helps users manage the entire lifecycle of application infrastructure on Google Cloud Platform. It provides a set of specialized sub-agents to handle different aspects of infrastructure design and generation.

**Supported Commands and Required Information:**

  * `manage_app_design`: Design and architect infrastructure on Google Cloud Platform required for application infrastructure design intents.

    * **Description** : 
      * This command can generate the Google Cloud architecture, then render the Mermaid diagram as well as generate the Terraform code.
      * This command **may** also accept Infrastructure as Code (IaC) when iterating on a design (e.g. import Terraform code into existing application template).
      * This command can also be used to retrieve the Terraform code for an existing application template or app design.
    * **Design Session** : 
      * Each design session is associated with an Application Design Center (ADC) application template (identified by `applicationTemplateURI`).
      * The agent will maintain the state of application designs and its Terraform artifacts.
      * To iterate on a design, you MUST provide the application template ID in the form of `projects/{projectid}/locations/{region}/spaces/{spaceid}/applicationTemplates/{templateid}`.
      * To create a new design, do not supply the application template ID.
    * **User Query:** Should describe the high-level application architecture, requirements, and constraints. You may specify environment variables, port, etc. Or specific request for IaC import or Terraform code retrieval. 
      * _Example:_ "Design a 3-tier web app with a load balancer, frontend, backend, and a database."
      * _Example:_ "Import application design from IaC, here are my terraform files: - main.tf `terraform\n<main.tf file content>\n`, - variables.tf `terraform\n<variables file content>\n` ..."
      * _Example:_ "Show me the Terraform code for application template `projects/.../applicationTemplates/test-app`"
    * **Important Guidelines**
      * **Design Iteration:** : If the user wants to _modify_ or _update_ an existing design, they **MUST** provide the `application_template_id` in the query. 
        * _Example:_ "Update design `projects/{projectid}/locations/{region}/spaces/{spaceid}/applicationTemplates/{templateid}`: add a Cloud SQL instance."
      * `project` input **must** be formatted as `projects/{projectid}`.
    * **Goal:** Generates a comprehensive design using Application Design Center (ADC) concepts or imports an application design from IaC.
    * **Returns:** An XML-formatted string containing one or more of: `Message`, `serializedDesign`, `applicationTemplateURI`, `terraformCode`, `mermaidCode`, and `Instructions`.
  * `generate_terraform`: Generate Terraform configs a single resource.

    * **User Query:** specific request for Terraform code. 
      * _Example:_ "Generate Terraform for a GKE cluster with a spot node pool."
    * **Hint** : If user wants to generate Terraform for an ADC application template, they **MUST** use `manage_app_design` instead. 
      * _Example:_ "Generate Terraform for application template `tmpl_12345`" should be routed to `manage_app_design`.
    * **Goal:** Produces valid, deployable Terraform HCL code.
  * `generate_gcloud`: Generate gcloud commands.

    * **User Query:** A request to perform an action using the Google Cloud CLI. 
      * _Example:_ "Give me the gcloud command to create a Pub/Sub topic."
    * **Goal:** Generates a sequence of executable `gcloud` commands.
  * `generate_bigquery`: Generate BigQuery commands.

    * **User Query:** A request for BigQuery commands. 
      * _Example:_ "Give me the bq command to create a dataset."
    * **Goal:** Generates a sequence of executable `bq` commands.
  * `generate_kubernetes_yaml`: Generate Kubernetes YAML.

    * **User Query:** A request for Kubernetes manifests. 
      * _Example:_ "Create a Kubernetes Deployment for Nginx with 3 replicas."
    * **Goal:** Produces valid Kubernetes YAML manifests.
  * `debug_deployment`: Debug deployment failure in ADC application.

    * **User Query:** A request to debug a deployment failure in ADC application. It needs to contain a helper phrase like 'Help me debug this application' and only the application_uri and no other information. 
      * _Example:_ "Help me debug this application - projects/test-project/locations/us-central1/spaces/test-space/applicationTemplates/test-app"
    * **Goal:** Diagnoses deployment issues and returns instructions to fix the problem.
    * **Follow-up Actions:**
      * If the output contains `gcloud` commands, follow the instructions and run the gcloud command to fix the issue.
      * If the output describes an infrastructure design change, call the `manage_app_design` tool to apply recommended changes in the infrastructure.



**Usage:**

To use this tool, the caller must specify the `command` argument corresponding to the desired sub-agent and provide the `user_query` with the specific intent.

The following sample demonstrate how to use `curl` to invoke the `design_infra` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://geminicloudassist.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "design_infra",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for DesignInfra

### DesignInfraRequest

JSON representation  
---  
      
    
    {
      "project": string,
      "userQuery": string,
      "contextId": string,
      "command": string
    }  
  
Fields  
---  
`project` |  `string` Required. The project resource name in the format `projects/{project}`.  
`userQuery` |  `string` Required. The natural language prompt provided by the user.  
`contextId` |  `string` Optional. This is an optional session ID to continue a conversation.  
`command` |  `string` Required. The command being invoked. Valid values are: - "manage_app_design" - "generate_terraform" - "generate_gcloud" - "generate_yaml" - "debug_deployment"  
  
## Output Schema

Represents the response for DesignInfra. This message is only used as an output_schema_override.

### DesignInfraResponse

JSON representation  
---  
      
    
    {
      "content": string,
      "contextId": string,
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`content` |  `string` Contains the textual response received from the agent.  
`contextId` |  `string` Represents the session ID; clients must persist this.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Contains the metadata returned from the agent.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a Value with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
