---
url: https://docs.cloud.google.com/cloud-assist/reference/mcp/
title: MCP Reference: geminicloudassist.googleapis.com \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:49.807795+00:00
---

# MCP Reference: geminicloudassist.googleapis.com  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  MCP Reference: geminicloudassist.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : The Gemini Cloud Assist MCP server is in private preview. Use of this Preview offering is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805). To request access to the private preview, contact your Google Cloud account manager.

The Gemini Cloud Assist MCP Server provides automated assistance for Google Cloud Platform, enabling intelligent troubleshooting, cost optimization, infrastructure design and provisioning, and cloud operations. Prerequisites:

  * Required APIs: 
    * geminicloudassist.googleapis.com
    * designcenter.googleapis.com
    * apphub.googleapis.com
    * cloudasset.googleapis.com
    * appoptimize.googleapis.com
  * Recommended APIs (optional for full experience): 
    * logging.googleapis.com
    * monitoring.googleapis.com
    * apptopology.googleapis.com
    * recommender.googleapis.com
  * Required Roles: 
    * roles/geminicloudassist.viewer (for read-only tasks)
    * roles/geminicloudassist.user (for general usage)
    * roles/geminicloudassist.admin (for admin settings changes)



A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Gemini Cloud Assist API MCP server has the following global MCP endpoint:

  * https://geminicloudassist.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The geminicloudassist.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[ask_cloud_assist](https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/ask_cloud_assist)` |  The primary interface for Google Cloud Platform assistance. Use this tool to interact with the GCA Root Agent for general troubleshooting, log analysis, or broad cloud inquiries. It acts as the central orchestration agent that directs user requests to expert sub-agents or handles them directly using general-purpose tools.**Capabilities:**

  * **General Inquiries:** Answers broad questions about Google Cloud services, concepts, and documentation.
  * **Estate Queries:** Retrieves current resource state and inventory (e.g., "List my active VMs," "Show me the config for this pod").
  * **Directives:** Executes specific, low-complexity directives or status checks.
  * **Triage & Routing:** Handles complex or ambiguous intents (e.g., "Something is wrong with my app") to identify the problem scope before potentially handing off to specialized agents.
  * **Secure Execution:** Orchestrates mutative actions (e.g., "Restart this VM", "Scale this cluster") using a secure Human-in-the-Loop (HITL) workflow. It verifies user consent before executing `gcloud` commands.

**Usage Guidelines:**

  * **Default Choice:** Select this tool when the user's intent is broad, ambiguous, exploratory, purely informational, or involves planning.
  * **Triage:** Use this tool for initial issue reporting where the specific domain is not yet clear.
  * **Direct Execution:** Use this tool when the user requests a specific, intended change to their environment (e.g., "Restart instance X", "Scale this cluster", "Update the firewall rule").
  * **Exclusions:**
    * If the user explicitly asks to **design, architect, or deploy** infrastructure, use `design_infra`.
    * If the user explicitly asks for **deep root cause analysis, debugging, or remediation** of a known failure, use `investigate_issue`.
    * If the user explicitly asks about **costs, billing, or idle resources** , use `optimize_costs`.

**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId`.
  * Omit `contextId` to start a new, independent task.

  
`[investigate_issue](https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/investigate_issue)` |  The Investigation Orchestrator Agent is the **Principal Troubleshooting & Diagnostics Agent** for Google Cloud. It acts as a specialized "SRE in a box" capable of navigating complex infrastructure, application code, and observability data to resolve incidents.**Core Features & Architecture:**

  * **Advanced Reasoning & Interactive Investigations:** Uses sophisticated planning algorithms to execute **parallelized hypothesis evaluation** , allowing it to check multiple failure scenarios simultaneously rather than sequentially.
  * **Quick vs. Deep Investigation Strategy:**
    * **Express Mode:** For rapid insights, log/metric anomaly detection, and real-time status checks.
    * **Deep Research Mode:** For complex Root Cause Analysis (RCA). It leverages **domain expertise** by integrating with specialized Database & Analytics Agents via the Cloud Assist Planner Agent.
  * **Diagnostic Runbooks:** Can automatically select and execute pre-defined diagnostic playbooks for standardized troubleshooting.
  * **Trace-Based Topology:** Generates dynamic architecture maps derived from real traffic traces, not just static configuration.
  * **Source Code Insights:** Analyzes application logic to find root causes within the code itself (e.g., connection pools, queries).
  * **AI-Powered Explanation:** Provides plain-language explanations for obscure error logs and metric anomalies.

**When to route to this agent:**

  * User requests **Root Cause Analysis (RCA)** or help with an outage/crash.
  * User asks to analyze **logs, metrics, or traces** for anomalies.
  * User needs to **understand dependencies** or reason about topology graph.
  * User asks about **source code** issues causing infrastructure failures.
  * User wants to run specific **diagnostics** or health checks.

**Detailed Capabilities & Skills:**

  * **Deep Research & Root Cause Analysis (RCA):** Initiates a comprehensive, multi-step investigation using advanced reasoning and planning. It executes parallelized hypothesis evaluation, leveraging domain-specific agents (Database, Analytics) to find definitive root causes. Use this for complex, open-ended problems.
    * Examples: "My application latency has spiked to 5s, find the root cause.", "Investigate why the chatter-service is throwing 503 errors during the load test.", "Why are the pods on ClusterABC unschedulable?", "Analyze the bottlenecks in my checkout flow.", "Perform a deep analysis of the database lock contention."
  * **Diagnostic Runbooks & Playbooks:** Executes deterministic diagnostic runbooks and standard operating procedures (SOPs). This skill integrates with the Cloud Assist Planner Agent to run validated checks for known issues and common failure modes.
    * Examples: "Run the connectivity diagnostic for the frontend service.", "Execute the standard health check runbook.", "Check for known configuration issues using the diagnostic playbook.", "Is there a runbook to verify network reachability?"
  * **Express Diagnostics & Anomaly Detection:** Performs rapid 'Quick Checks' and automated anomaly detection on logs and metrics. Use this to instantly identify outliers, spikes, or error patterns without waiting for a full investigation.
    * Examples: "Detect any metric anomalies for the checkout-service.", "Show me the traffic level and latency for the chatter-frontend service.", "Are there any outliers in the CPU usage?", "What are the top errors for the store-processing service right now?", "Scan the logs for recent error spikes."
  * **AI-Powered Log & Error Reasoning:** Uses AI to **reason about** and interpret complex error logs, stack traces, and metric patterns. Beyond simple explanation, it deduces the technical meaning and potential impact of observability data.
    * Examples: "Analyze this stack trace and explain why the crash is happening.", "Reason about this 'Connection Reset' error in the context of high load.", "Interpret this obscure database error code.", "Why am I seeing this specific error log repeatedly?"
  * **Trace-Based Topology Graph:** Generates a dynamic topology graph derived from real application traces (OneGraph). It visualizes and reasons actual traffic paths and dependencies, overlaying latency and error signals on the graph nodes.
    * Examples: "Show me the trace-based topology for the payment service.", "Visualize the actual traffic flow between microservices.", "Map out the dependencies based on recent request traces.", "Generate a graph showing where the latency is introduced in the stack."
  * **Source Code Insights:** Deeply analyzes application source code and configuration files (via DevConnect). It connects infrastructure symptoms to specific lines of code, identifying issues like bad queries, aggressive timeouts, or logic bugs.
    * Examples: "Analyze the source code for inefficient database queries.", "Did a recent commit change the connection pool settings?", "Check the app logic for potential race conditions.", "Review the configuration files in the repo for errors."
  * **Root Cause Resolution & Remediation:** Synthesizes investigation findings to **identify the definitive root cause** and generates a corresponding actionable remediation plan (e.g., CLI commands, code patches) to resolve the issue.
    * Examples: "Find the root cause of the database timeout and generate a plan to fix it.", "Identify why the instance is crashing and create a gcloud command to resize it.", "Determine the cause of the connection errors and suggest code changes.", "What is the recommended fix for this error?"
  * **Multi-Turn Interactive Troubleshooting:** Supports stateful, multi-turn interactivity. Allows the user to guide the investigation, ask follow-up questions, refine the scope, and iterate on findings in a conversational manner.
    * Examples: "That didn't fix it, what should we check next?", "Can you look at the database logs instead?", "Let's focus on the frontend service now.", "Go deeper into that second hypothesis."

**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId`.
  * Omit `contextId` to start a new, independent task.

  
`[optimize_costs](https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/optimize_costs)` |  The Optimize Agent helps users analyze, track, and optimize their Google Cloud costs. It provides detailed breakdowns of spend and identifies opportunities for cost efficiency by finding idle or underutilized resources.**Core Features:**

  * **Cost Analysis:** Breaks down spend by project, application, product, resource, or location to answer "how much did I spend" questions.
  * **Top Cost Drivers:** Identifies the most expensive resources or services driving the bill.
  * **Cost Trends:** Analyzes how costs have changed over time (e.g., month-over-month increases).
  * **Efficiency & Rightsizing:** Identifies idle, overprovisioned, or underutilized resources _specifically_ to highlight cost-saving opportunities.

**Important Routing Constraints:**

  * **DO** route questions about "underutilized" or "idle" resources if the context is saving money (e.g., "Show me the cost of my most underutilized resources").
  * **DO NOT** route general utilization questions unrelated to cost (e.g., "How much vCPU did resource X use?").
  * This agent **does not** predict future costs.
  * This agent **does not** take any action to reduce costs (read-only analysis).

**When to route to this agent:**

  * User asks "How much did I spend on Compute Engine last month?"
  * User asks "What are my most expensive resources?"
  * User asks "Which resources are idle and costing me money?"
  * User asks "Why did my bill go up compared to last month?"

**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId`.
  * Omit `contextId` to start a new, independent task.

  
`[invoke_operation](https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/invoke_operation)` |  Invokes the Operations Agent for Cloud Operations tasks.The Operations Agent is capable of handling various cloud operations, investigations, and management tasks.The `user_query` is a stringified JSON object that defines the exact operation. The JSON MUST contain an `operation_type` key with one of two values: `GKE_APPLY`, `GKE_PATCH`. Based on the `operation_type`, provide exactly one of the corresponding objects:

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

  
`[design_infra](https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/design_infra)` |  Design Agent helps users manage the entire lifecycle of application infrastructure on Google Cloud Platform. It provides a set of specialized sub-agents to handle different aspects of infrastructure design and generation.**Supported Commands and Required Information:**

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

**Usage:** To use this tool, the caller must specify the `command` argument corresponding to the desired sub-agent and provide the `user_query` with the specific intent.  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          
    curl --location 'https://geminicloudassist.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
