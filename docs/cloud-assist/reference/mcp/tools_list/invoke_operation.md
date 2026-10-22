---
url: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/invoke_operation/
title: MCP Tools Reference: geminicloudassist.googleapis.com \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:14.119528+00:00
---

# MCP Tools Reference: geminicloudassist.googleapis.com  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/invoke_operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  MCP Tools Reference: geminicloudassist.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : The Gemini Cloud Assist MCP server is in private preview. Use of this Preview offering is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805). To request access to the private preview, contact your Google Cloud account manager.

## Tool: `invoke_operation`

Invokes the Operations Agent for Cloud Operations tasks.

The Operations Agent is capable of handling various cloud operations, investigations, and management tasks.

The `user_query` is a stringified JSON object that defines the exact operation. The JSON MUST contain an `operation_type` key with one of two values: `GKE_APPLY`, `GKE_PATCH`. Based on the `operation_type`, provide exactly one of the corresponding objects:

  * **If`GKE_APPLY`:** Provide a `gke_apply` object containing:

    * `target_cluster` (string, required): Full resource name, e.g., `projects/{p}/locations/{l}/clusters/{c}`.
    * `yaml_manifest` (string, required): The raw YAML string. Ensure newlines are escaped.
    * `namespace` (string, optional): Overrides the namespace.
    * `force_conflicts` (boolean, optional): If true, force conflicts resolution when applying. This corresponds to kubectl apply --server-side --force-conflicts. Use this to ensure the intended state is applied even if another field manager currently owns the targeted fields.
  * **If`GKE_PATCH`:** Provide a `gke_patch` object containing:

    * `target_cluster` (string, required): Full resource name.
    * `resource_type` (string, required): e.g., `deployments`.
    * `resource_name` (string, required): Name of the k8s resource.
    * `patch_json` (string, required): The JSON patch string. Escaped properly.
    * `namespace` (string, optional): The namespace of the resource.



**Examples:**

  * Example 1 (`GKE_APPLY`):
        
        {
                  "operation_type": "GKE_APPLY",
                  "gke_apply": {
                    "target_cluster": "projects/my-company/locations/us-central1/clusters/my-cluster",
                    "yaml_manifest": "apiVersion: v1 | kind: ConfigMap | metadata: name: my-config | data: key: value",
                    "namespace": "default"
                  }
                }
                

  * Example 2 (`GKE_PATCH`):
        
        {
                  "operation_type": "GKE_PATCH",
                  "gke_patch": {
                    "target_cluster": "projects/my-company/locations/us-central1/clusters/my-cluster",
                    "resource_type": "deployments",
                    "resource_name": "my-app",
                    "patch_json": "{'spec': {'replicas': 5}}",
                    "namespace": "default"
                  }
                }
                

  * Example 3 (`GKE_APPLY` with force_conflicts to override existing field managers):
        
        {
                  "operation_type": "GKE_APPLY",
                  "gke_apply": {
                    "target_cluster": "projects/my-company/locations/us-central1/clusters/my-cluster",
                    "yaml_manifest": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: web-backend\nspec:\n  replicas: 5\n  template:\n    spec:\n      containers:\n      - name: app\n        image: my-repo/web-backend:v2.0.1",
                    "namespace": "default",
                    "force_conflicts": true
                  }
                }
                




**Args:**

  * `project`: The Google Cloud project with format `projects/{project_id}`.
  * `userQuery`: A stringified JSON object that defines the exact operation.
  * `contextId`: Context ID from the previous agent response.



**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId` in the next request.
  * Omit `contextId` to start a new, independent task.



The following sample demonstrate how to use `curl` to invoke the `invoke_operation` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://geminicloudassist.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "invoke_operation",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for InvokeOperation

### InvokeOperationRequest

JSON representation  
---  
      
    
    {
      "project": string,
      "userQuery": string,
      "contextId": string
    }  
  
Fields  
---  
`project` |  `string` Required. The project resource name in the format `projects/{project}`.  
`userQuery` |  `string` Required. The natural language prompt provided by the user.  
`contextId` |  `string` Optional. This is an optional session ID to continue a conversation.  
  
## Output Schema

Represents the response for InvokeOperation. This message is only used as an output_schema_override.

### InvokeOperationResponse

JSON representation  
---  
      
    
    {
      "content": string,
      "contextId": string
    }  
  
Fields  
---  
`content` |  `string` Contains the textual response received from the agent.  
`contextId` |  `string` Represents the session ID; clients must persist this.  
  
### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
