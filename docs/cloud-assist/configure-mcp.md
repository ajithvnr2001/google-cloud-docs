---
url: https://docs.cloud.google.com/cloud-assist/configure-mcp/
title: Integrate Gemini Cloud Assist with third-party tools using MCP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:27.752927+00:00
---

# Integrate Gemini Cloud Assist with third-party tools using MCP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/configure-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Integrate Gemini Cloud Assist with third-party tools using MCP Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Integrating Gemini Cloud Assist with third-party tools using MCP is in private preview. To request access, contact your Google Cloud account team.   
  
Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

Model Context Protocol (MCP) lets you integrate Gemini Cloud Assist and Application Design Center agentic capabilities directly into third-party tools, such as Antigravity, Gemini CLI, and Cursor. This integration brings cloud operations expertise and architecture assistance into your existing development workflows. For more information, see [Configure MCP for your AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).

## Gemini Cloud Assist MCP tools

Gemini Cloud Assist is an agent that is accessible through a set of MCP tools using the agents-as-tools pattern. Unlike tools that fetch data or do procedural processing, the Gemini Cloud Assist tools expose agentic functionality of all of Gemini Cloud Assist or of specific workflows. The agent invoked by MCP tool calls makes its own tool calls internally to Google Cloud. The following MCP tools are published for agents to consume:

  * `ask_cloud_assist`: This is the primary interface for Google Cloud assistance and for the Gemini Cloud Assist agent. All functionality of Gemini Cloud Assist is accessible through this tool and it encompasses the functionality of the other MCP tools.
  * `design_infra`: This supports workflows for designing and architecting infrastructure on Google Cloud. It works with App Design Center MCP server tools to manage your infrastructure design lifecycle—for example, run and remediate security findings, or deploy and remediate issues.
  * `investigate_issue`: This supports workflows for troubleshooting in Google Cloud. It can do quick troubleshooting or deeper troubleshooting through an Investigation resource.
  * `invoke_operation`: This supports workflows for creating, updating, and deleting resources in Google Cloud. This tool is only functional when Agent Actions are enabled. Write operations in Gemini Cloud Assist can only be executed through the invocation of this tool.
  * `optimize_costs`: This supports workflows for analyzing, tracking, and optimizing Google Cloud costs. It provides detailed breakdowns of spending and identifies opportunities for cost efficiency by finding idle or underutilized resources.



### App Design Center MCP tools

These tools, often orchestrated by Gemini Cloud Assist's `design_infra` tool, manages infrastructure application lifecycles using App Design Center, including template management, security compliance and remediation, and deployment. The tools are:

  * `setup_adc`: Initializes the App Design Center environment. This is a one-time setup step that must be performed before other App Design Center tools can be used.
  * `manage_application`: Manages the deployment lifecycle of an application. Use this tool to deploy a verified design using the App Design Center or retrieve the status and details of an existing deployment. This is the final step that turns your design into a deployed infrastructure on Google Cloud.
  * `manage_application_template`: Manages the Infrastructure as Code (IaC) content of your infrastructure design. Use this to save the design as an App Design Center template, export the design as Terraform files, or update the design. For example, you can use this tool to update the design by modifying component settings and parameter configurations.
  * `assess_best_practices`: Performs a comprehensive security and configuration audit on your application design before deployment. It validates the design against Security Command Center frameworks and relevant controls, returning a report with actionable findings for remediation.
  * `list_application_templates`: Lists all available application designs.



These MCP tools shouldn't be treated as stable APIs or configured through procedural API clients. Tools from this list or their parameters might be renamed, re-defined, removed, or added over time to account for the evolving capabilities of Gemini Cloud Assist. The capabilities of Gemini Cloud Assist will remain stable so that client agents are able to consistently execute the same tasks, but the way in which agents interact with and invoke Gemini Cloud Assist through these tools will change over time.

## Before you begin

  1. Grant access: To use MCP, you need to be granted an Identity and Access Management role that contains the `mcp.googleapis.com/tools.call` permission, such as one of the following Gemini Cloud Assist roles:

     * `roles/geminicloudassist.user`
     * `roles/geminicloudassist.editor`
     * `roles/geminicloudassist.admin`
  2. If you haven't already done so, install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) and its [beta components](https://docs.cloud.google.com/sdk/docs/components#alpha_beta_and_preview_components).

  3. Enable the MCP service in your project with the following command:
         
         gcloud beta services mcp enable geminicloudassist.googleapis.com \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  4. Authenticate using [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) by running the following command:
         
         gcloud auth application-default login
         




## Configure MCP for your client

The client-agent configuration depends on which agent you are using. The following sections provide instructions to configure MCP for different clients.

To enable the full design-to-deploy workflow, you must configure your client to connect to both the Gemini Cloud Assist and App Design Center MCP servers and include the relevant `SKILL.md` file. The following snippets show the combined configuration.

**Tip:** Creating an OAuth 2.0 client in Google Auth Platform requires elevated permissions (`oauthconfig.clients.create`) that standard users with the `roles/geminicloudassist.user` role don't typically have. For third-party clients that require OAuth 2.0 credentials—such as Claude, ChatGPT, or Cursor—we recommend that an administrator create a single shared OAuth 2.0 client ID and client secret for each client tool and share those credentials with your team.

### Antigravity

To add the Gemini Cloud Assist and App Design Center remote MCP servers to Antigravity, follow the instructions in [Antigravity Editor: MCP Integration](https://antigravity.google/docs/mcp) or complete the following steps:

  1. **Install the extension.**

In Antigravity, open the **Extensions** marketplace. Search for the Gemini Cloud Assist extension, click **Install** , and then click **Refresh**.

  2. **Configure the MCP servers manually.**

Open the **Manage MCP Servers** pane and click **View raw config** to edit the `mcp_config.json` file. Add or merge the following configuration block. This setup uses your Application Default Credentials for authentication.
         
         {
           "mcpServers": {
             "gemini_cloud_assist": {
               "serverUrl": "https://geminicloudassist.googleapis.com/mcp",
               "headers": {},
               "authProviderType": "google_credentials"
             },
             "application_design_center": {
               "serverUrl": "https://designcenter.googleapis.com/mcp",
               "headers": {},
               "authProviderType": "google_credentials"
             }
           }
         }
                 

  3. **Verify your setup.**

After you modify your `mcp_config.json` and `SKILL.md` files, restart Antigravity. In the **Agent pane** , run the following slash commands to verify the connection:

     * `/skills list`: verifies that your local skills have been discovered.
     * `/mcp list`: verifies that the Gemini Cloud Assist and App Design Center MCP servers are connected.



### ChatGPT

You must have a [ChatGPT Business subscription](https://chatgpt.com/business/) to use Google and Google Cloud MCP servers with ChatGPT.

To add the Gemini Cloud Assist and App Design Center remote MCP servers to ChatGPT, create an OAuth 2.0 client ID and client secret, and then add the MCP servers as plugins in ChatGPT:

  1. Create an OAuth 2.0 client ID and client secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized JavaScript origins** section, click **\+ Add URI** , and then enter `https://chatgpt.com` in the **URIs** field.

     5. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://chatgpt.com/connector_platform_oauth_redirect` in the **URIs** field.

     6. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     7. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  2. Sign in to ChatGPT with developer mode turned on.

  3. Follow the instructions in [Build a plugin](https://developers.openai.com/plugins/build/plugins) to add a custom connector for each MCP server:

     * For Gemini Cloud Assist, set the server URL to `https://geminicloudassist.googleapis.com/mcp`.
     * For App Design Center, set the server URL to `https://designcenter.googleapis.com/mcp`.
  4. Under OAuth or **Advanced settings** , enter your OAuth client ID and client secret.

  5. Complete the sign-in prompt to enable the MCP servers in chat.




### Claude.ai

To add the Gemini Cloud Assist and App Design Center remote MCP servers to Claude.ai, configure custom connectors with an OAuth 2.0 client ID and client secret:

  1. Create an OAuth 2.0 client ID and client secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized JavaScript origins** section, click **\+ Add URI** , and then enter `https://claude.ai` in the **URIs** field.

     5. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

     6. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     7. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  2. Follow the instructions to [create a custom connector](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for each MCP server:

     * For Gemini Cloud Assist, set the server URL to `https://geminicloudassist.googleapis.com/mcp`.
     * For App Design Center, set the server URL to `https://designcenter.googleapis.com/mcp`.
  3. In the **Advanced settings** menu, enter your OAuth client ID and client secret.

  4. Complete the sign-in prompt to enable the MCP servers in chat.




### Claude Code

To add the Gemini Cloud Assist and App Design Center remote MCP servers to Claude Code, configure custom connectors with an OAuth 2.0 client ID and client secret:

  1. [Install Claude Code](https://code.claude.com/docs/en/quickstart).

  2. Create an OAuth 2.0 client ID and client secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  3. Follow the instructions to [create a custom connector](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for each MCP server:

     * For Gemini Cloud Assist, set the server URL to `https://geminicloudassist.googleapis.com/mcp`.
     * For App Design Center, set the server URL to `https://designcenter.googleapis.com/mcp`.
  4. In the **Advanced settings** menu, enter your OAuth client ID and client secret.

  5. Complete the sign-in prompt to enable the MCP servers in chat.




### Claude Desktop

To add the Gemini Cloud Assist and App Design Center remote MCP servers to Claude Desktop, configure custom connectors with an OAuth 2.0 client ID and client secret:

  1. [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop).

  2. Create an OAuth 2.0 client ID and client secret:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  3. Follow the instructions to [create a custom connector](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) for each MCP server:

     * For Gemini Cloud Assist, set the server URL to `https://geminicloudassist.googleapis.com/mcp`.
     * For App Design Center, set the server URL to `https://designcenter.googleapis.com/mcp`.
  4. In the **Advanced settings** menu, enter your OAuth client ID and client secret.

  5. Complete the sign-in prompt to enable the MCP servers in chat.




### Codex

To add the Gemini Cloud Assist and App Design Center remote MCP servers to Codex Enterprise, complete the following steps:

  1. In the Codex Enterprise UI, open **Settings** , select **MCP Servers** , and then click **View raw config** to open the `mcp_config.json` editor.

  2. Add or merge the following configuration block into the `mcp_config.json` file. This setup uses your Application Default Credentials for authentication.
         
         {
           "mcpServers": {
             "gemini_cloud_assist": {
               "serverUrl": "https://geminicloudassist.googleapis.com/mcp",
               "headers": {},
               "authProviderType": "google_credentials"
             },
             "application_design_center": {
               "serverUrl": "https://designcenter.googleapis.com/mcp",
               "headers": {},
               "authProviderType": "google_credentials"
             }
           }
         }
                 




### Cursor

To add the Gemini Cloud Assist and App Design Center remote MCP servers to Cursor, create an OAuth 2.0 client ID and client secret, and then configure the MCP servers with static OAuth. Cursor uses different redirect URIs depending on whether you access Cursor through the web or a desktop app:

  1. Create an OAuth 2.0 client ID and client secret:

### Web or Cursor agents

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://www.cursor.com/agents/mcp/oauth/callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.

### Desktop

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `http://localhost:8787/callback` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.

  2. Follow the instructions to [configure the MCP server with static OAuth](https://cursor.com/docs/mcp#static-oauth-for-remote-servers), and add or merge the following configuration block into your Cursor MCP configuration:
         
         {
           "mcpServers": {
             "gemini_cloud_assist": {
               "url": "https://geminicloudassist.googleapis.com/mcp",
               "auth": {
                 "CLIENT_ID": "${env:OAUTH_CLIENT_ID}",
                 "CLIENT_SECRET": "${env:OAUTH_CLIENT_SECRET}",
                 "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
               }
             },
             "application_design_center": {
               "url": "https://designcenter.googleapis.com/mcp",
               "auth": {
                 "CLIENT_ID": "${env:OAUTH_CLIENT_ID}",
                 "CLIENT_SECRET": "${env:OAUTH_CLIENT_SECRET}",
                 "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
               }
             }
           }
         }
                 

  3. Set the `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` environment variables in your environment.

  4. [Use the MCP server in Chat](https://cursor.com/docs/mcp#using-mcp-in-chat).




### Gemini CLI

### Configure using an extension

Install the MCP server as a Gemini CLI extension using the following command:
    
    
    gemini extensions install https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp
              

### Configure manually

  1. **Configure the MCP server settings.**

Open your Gemini CLI user-scope settings file at `~/.gemini/settings.json` or your workspace-scope settings at `.gemini/settings.json`. If the file doesn't exist, create it. Add or merge the following configuration block under the `mcpServers` key. Ensure that the file uses valid JSON format. This configuration automatically uses your Application Default Credentials. 
         
         {
           "mcpServers": {
             "gemini_cloud_assist": {
               "httpUrl": "https://geminicloudassist.googleapis.com/mcp",
               "authProviderType": "google_credentials",
               "oauth": {
                 "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
               },
               "timeout": 600000
             },
             "application_design_center": {
               "httpUrl": "https://designcenter.googleapis.com/mcp",
               "authProviderType": "google_credentials",
               "oauth": {
                 "scopes": ["https://www.googleapis.com/auth/cloud-platform"]
               },
               "timeout": 600000
             }
           }
         }
                       

  2. **Create and populate your skill files.**

Create a `SKILL.md` file in one of the following directories. Copy and paste the Markdown content for your chosen skill from the skill reference section of this document into the file.

     * Workspace scope: `.gemini/skills/SKILL_NAME/`
     * User scope: `~/.gemini/skills/SKILL_NAME/`

Replace `SKILL_NAME` with the directory name for your skill.

The following is an example directory structure:
    
    .gemini/
    └── skills/
        ├── design-and-deploy/
        │   └── SKILL.md
        └── google-gemini-cloud-assist/
            └── SKILL.md
                  

  3. **Verify your skills.**

After you modify your `settings.json` and `SKILL.md` files, restart Gemini CLI, and then run the following commands to verify your setup:

     * `/skills list`: verifies that your local skills have been discovered.
     * `/mcp list`: verifies that the Gemini Cloud Assist and App Design Center MCP servers are connected.



### Gemini Enterprise

**Important:** Gemini Enterprise is an organization-wide configuration, not a per-user setup. An administrator registers the MCP servers once as custom MCP server data stores, and the tools become available to agents across the organization. 

To register the Gemini Cloud Assist and App Design Center remote MCP servers in Gemini Enterprise, an administrator must complete the following steps:

  1. Create an OAuth 2.0 client ID and client secret with the Gemini Enterprise redirect URI:

     1. In the Google Cloud console, go to **Google Auth Platform > Clients > Create client**.

[Go to Create client](https://console.cloud.google.com/auth/clients/create)

You are prompted to create a project if you don't have one selected.

     2. In the **Application type** list, select **Web application**.

     3. In the **Name** field, enter a name for your application.

     4. In the **Authorized redirect URIs** section, click **\+ Add URI** , and then enter `https://vertexaisearch.cloud.google.com/oauth-redirect` in the **URIs** field.

     5. Click **Create**. The client is created.

The **OAuth 2.0 client created** dialog opens.

     6. In the **Client secrets** section, copy the **Client secret** and save it in a secure place. You can only copy it once. If you lose it, delete the secret and create a new one.

**Caution:** Treat client secrets like passwords and store them in a secure place.
  2. In the Google Cloud console, go to **Gemini Enterprise > Data stores**, and then click **Create data store**. For more information, see [Set up your custom MCP server datastore](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).

  3. Select **Custom MCP Server** as the data source.

  4. Configure a custom MCP server datastore for each endpoint:

     * For Gemini Cloud Assist, enter `https://geminicloudassist.googleapis.com/mcp`.
     * For App Design Center, enter `https://designcenter.googleapis.com/mcp`.
  5. Enter the OAuth **Client ID** and **Client secret** , and then save the datastore. The tools become available to Gemini Enterprise agents.




## Gemini Cloud Assist skills

The Gemini Cloud Assist and App Design Center MCP tools use agent skills to instruct your agent. The skill guides your agent to perform the following tasks:

  * Chain together multiple tools into a workstream.
  * Process relevant local information, such as Terraform deployment code, to reason about your local context.
  * Respond to explicit invocations when you reference the skill directly.



When using interactive agents like Antigravity or Gemini CLI, you can integrate Gemini Cloud Assist MCP tools with other agents and workflows. Because these tools provide broad capabilities that might overlap with your existing specialized tools, use the following strategies to optimize for your specific environment and use case:

  1. **Customize the skill definition** : Update the `SKILL.md` file to specify the intents and use cases for which you want to invoke Gemini Cloud Assist. This ensures the agent is only triggered for tasks where its broad cloud expertise is required.
  2. **Invoke skills explicitly** : Many interactive agents allow you to control when a skill is triggered. If your agent supports it, you can configure the skill to require manual invocation using **slash commands** (`/`) or **at-mentions** (`@`). This approach lets you precisely choose when to use Gemini Cloud Assist versus another specialized tool.



## Gemini Cloud Assist skill reference

We recommend the following `SKILL.md` file on any agents that are configured with Gemini Cloud Assist MCP tools. This file guides your agent on how to use the tools appropriately.

#### Design and deploy infrastructure
    
    
    ---
    name: designing-and-deploying-infrastructure
    description: This skill is used to design, assess, deploy, and troubleshoot cloud infrastructure using the Application Design Center (ADC).
    ---
    
    # Designing and Deploying Infrastructure
    
    ## Index
    1. [Overview](#overview)
    2. [Best Practices & Constraints](#best-practices--constraints)
    3. [Phase 1: Infrastructure Design & Refinement](#phase-1-infrastructure-design--refinement)
    4. [Phase 2: Best Practices Assessment & Design Iteration](#phase-2-best-practices-assessment--design-iteration)
    5. [Phase 3: Application Deployment](#phase-3-application-deployment)
    6. [Phase 4: Get Deployed Resources](#phase-4-get-deployed-resources)
    7. [Phase 5: Troubleshoot Deployment Failures](#phase-5-troubleshoot-deployment-failures)
    8. [Phase 6: Verification & E2E Testing](#phase-6-verification--e2e-testing)
    
    ## Overview
    This skill provides a prescriptive, multi-loop workflow for the entire infrastructure lifecycle on Google Cloud Platform (GCP). It leverages the Gemini Application Designer (GAD) and Application Design Center (ADC) tools (like `gemini_cloud_assist:design_infra` and `application_design_center:assess_best_practices`) to intelligently design architectures, assess best practices, and automate deployment and troubleshooting.
    Always maintain the persona of a Principal Cloud Architect. Delegate all research and design to the specialized tools provided.
    **Note:** These tools are part of the `gemini_cloud_assist` and `application_design_center` MCP Servers. Tool names are qualified with their respective server names (e.g., `gemini_cloud_assist:tool_name`).
    
    ## Best Practices & Constraints
    -   **Delegation & No Manual Design**: Delegate all architecture decisions and product selections to the `gemini_cloud_assist:design_infra` tool. **Do not** design manually or edit generated Terraform code. Request changes via the tool.
    -   **Inputs**: Always ask the user for required context like project ID, service accounts, etc. if necessary -- do not make assumptions or use placeholders.
    -   **Visualization Power**: Always render the Mermaid diagram from `gemini_cloud_assist:design_infra` in every implementation plan. Refresh the diagram after every design change. Do not create your own diagrams.
    -   **Loop Discipline**: Follow the workflow loops and exit criteria strictly. If you cannot follow the Infrastructure Lifecycle Workflow, you must exit and inform the user (for example, if the user cancels the process, or if you hit the maximum troubleshooting loop threshold in Phase 5).
    -   **Application Template as the main resource**: The application template is the main resource when generating and iterating on a design. **Always** look for the application template URI in the `gemini_cloud_assist:design_infra` response (`serializedApplicationTemplateURI`), and use that for the rest of the Infrastructure Lifecycle Workflow.
        -   **Application Template vs Application**: Application template is a template that is used to create an application. Application is an instance of an application template. Do not confuse these two.
        -   **Never** attempt to create an application template URI yourself; always use the URI returned from `gemini_cloud_assist:design_infra`.
    
    ## Infrastructure Lifecycle Workflow
    ### Phase 1: Infrastructure Design & Refinement
    **Goal**: Transform vague user requirements into a concrete, approved architectural design.
    1.  **Requirement Gathering**: Capture user intent if it's vague (e.g., "3-tier web app with high availability").
    Guidelines for initial design that **you must follow**:
        - Gather project ID (required) and ADC space ID (optional) from the user.
    2.  **Codebase Analysis**: Critically, **before** calling `gemini_cloud_assist:design_infra`, you **must** perform a thorough exhaustive analysis of the user's application codebase (if available). **Do not** stop at high-level documentation or configuration files at the surface level; you **must** inspect the full depth of the codebase, including business logic, to find hidden API clients, dependencies, environment variables, and other application code context required to design cloud infrastructure. The list below outlines critical checks you **must** perform. **Do not** limit your investigation to only these items:
        - If you scan the application code to provide additional context, summarize *only* the application's characteristics (e.g., languages, frameworks, statefulness) and **do not** assume or suggest specific infrastructure components or services (e.g., **do not** choose the product type (e.g. GKE, Cloud Run, etc) or network information unless the user explicitly requested them or they are specified in codebase).
        - **NEVER** rely solely on `grep_search`, `os.environ`, or summary documentation (like READMEs) to determine infrastructure needs. **DO NOT** make premature assumptions or over-optimize for speed. Accuracy is critical; you **must** inspect the entire codebase.
        - Identify required environment variables, secrets, ports exposed in application, and database connection patterns. Environment Variables may also be present in nginx config files. Environment variables are critical for architecture so double check you have identified all of them.
        - Identify all the dependencies on existing GCP services (e.g., Vertex AI API, pre-existing GCS buckets). Along with the rest of the codebase, you **must** read dependency files (e.g., `requirements.txt`, `package.json`, `go.mod`) to identify GCP SDKs used and scan source code for explicit GCP client initializations.
        - Scan the codebase (e.g., `cloudbuild.yaml`, `Dockerfile`, CI/CD configs) to extract container image URLs. If no image is found or if the identified image does not exist in the Artifact Registry, you must build and upload the image. Provide only the resulting URL to `gemini_cloud_assist:design_infra`.
    3.  **Initial Design**: Call `gemini_cloud_assist:design_infra` tool with `command="manage_app_design"` and the user's query. Ensure that `project` is `projects/{project_id}`
        - **MANDATORY - PRODUCT AGNOSTICISM**: Do NOT architect the infrastructure prematurely (e.g. "frontend should be a Cloud Run service"), instead delegate this responsibilty entirely to `gemini_cloud_assist:design_infra` tool. The codebase analysis results __may suggest__ certain product types (e.g. database uses the PostgreSQL client library, therefore database may be PostgreSQL), but otherwise make **zero** assumptions about the architecture. Since environment variables are critical to the architecture, you **must** pass the full set discovered during codebase analysis phase in all the design_infra manage_app_design requests.
        - **Prevent Naming Collisions**: Generate a unique, non-sequential five-character alphanumeric suffix, strictly avoiding common patterns like `12345`, `abcde` or `a1b2c`. Instruct `gemini_cloud_assist:design_infra` in the prompt to append this suffix to all newly created components.
    4.  **Visualization, Terraform Code and Verification**: The `gemini_cloud_assist:design_infra` will respond with a Mermaid diagram, Terraform code, and the `serializedApplicationTemplateURI`.
        - Retrieve the Terraform code corresponding to each `.tf` file referenced and save them into a dedicated directory called `infra`.
        - You **must** present an Implementation Plan that contains the Mermaid diagram rendered within the Implementation Plan, as well as the location of the Terraform configs.
        - **Verification Step**: This is a critical step. You **must** meticulously verify the generated Terraform code to ensure it includes all the environment variables, secrets, dependencies, and correct container image URLs required by application, identified during the Codebase Analysis step. If *any* required configurations are missing or incorrect, you **must** iterate on the design using `gemini_cloud_assist:design_infra command="manage_app_design"` to correct them. **Do not proceed to deployment with an unverified or incomplete design.**
    5.  **Iteration**: Refine the design by feeding user feedback back into `gemini_cloud_assist:design_infra`.
        -   **Design Iteration Constraints**: When iterating on the design, **do not** make manual edits to the Terraform code. **Always** use `gemini_cloud_assist:design_infra` tool exclusively to update the Terraform code.  **Always** keep the local Terraform code in sync with Terraform code returned from `gemini_cloud_assist:design_infra`.
        -   **Visualization Update**: Update the Implementation Plan by re-rendering the Mermaid diagram and updating the Terraform configs.
        -   **Retries**: After encountering transient errors and you need to retry `gemini_cloud_assist:design_infra` calls, you **must make exactly the same call** with **same** arguments.
    6.  **Exit Criteria**:
        -   Design fulfills all critical requirements and has resources needed by the application, especially the environment variables for each service.
        -   User confirms the design is satisfactory.
        -   `gemini_cloud_assist:design_infra` reaches a stable state with no further architectural changes.
    
    ### Phase 2: Best Practices Assessment & Design Iteration
    **Goal**: Validate design alignment with security, cost, and reliability benchmarks prior to deployment.
    1. **Execution**: Invoke `assess_best_practices` using the application template metadata (project, location, space and application template identifiers).
    2. **Analysis**: You **MUST** present all findings to the user in a pretty tabular fashion per framework, detailing specific violations, and their associated severity levels - before proceeding to remediation.
    3. **Remediation Loop**:
        - Pass identified findings as context to `gemini_cloud_assist:design_infra(command="manage_app_design")`.
        - **Strict Constraint**: All modifications must be executed via the `gemini_cloud_assist:design_infra` tool; manual Terraform manipulation is prohibited.
        - Perform a diff-based comparison between current and updated Terraform code for user approval.
        - Re-assess post-update to verify the resolution of findings.
    4. **Exit Criteria**:
        - **Optimization**: Zero findings remaining.
        - **Convergence**: `gemini_cloud_assist:design_infra` provides no further suggestions.
        - **Threshold**: Maximum of three (3) iterative attempts reached.
    5. **Transition**: Proceed to Phase 3 deployment only upon loop termination.
    
    ### Phase 3: Application Deployment
    **Goal**: Deploy the application template to the GCP environment.
    1.  **Deploy Application**: Use the `application_design_center:manage_application` tool with the `APPLICATION_OPERATION_DEPLOY` operation to deploy the application.
        *   **Required Arguments**: `project`, `location`, `spaceId`, `applicationTemplateUri`, `applicationId`, `serviceAccount`.
        *   **Note**: This returns a Long-Running Operation (LRO). Inform the user that the deployment has started.
        *   **Example**:
            ```json
            {
              "project": "my-project",
              "location": "us-central1",
              "spaceId": "my-space",
              "applicationId": "my-app",
              "operation": "APPLICATION_OPERATION_DEPLOY",
              "applicationTemplateUri": "projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-template",
              "serviceAccount": "projects/my-project/serviceAccounts/deployer@my-project.iam.gserviceaccount.com"
            }
            ```
    2.  **Monitor Deployment**: Repeatedly poll the LRO (e.g., every 30-60 seconds) until `done: true`.
    3.  **Handle Results**:
        -   **Success**: If `done` is `true` and there is no `error` field, proceed to Phase 4.
        -   **Failure**: If an `error` field is present, proceed to Phase 5.
    
    ### Phase 4: Get Deployed Resources
    1.  **Retrieve Information**: Call the `application_design_center:manage_application` tool with the `APPLICATION_OPERATION_GET` operation, providing `project`, `location`, `spaceId` and `applicationId`, to fetch the outputs and status of the deployed resources.
        *   **Example**:
            ```json
            {
              "project": "my-project",
              "location": "us-central1",
              "spaceId": "my-space",
              "applicationId": "my-app",
              "operation": "APPLICATION_OPERATION_GET"
            }
            ```
    2.  **User Confirmation**: Present the deployed resource information to the user and conclude the task.
    
    ### Phase 5: Troubleshoot Deployment Failures
    **Goal**: Diagnose and remediate deployment failures iteratively.
    When troubleshooting a failed application, follow these steps.
    **Process:**
    1.  **Initiate Troubleshooting:**
        - **Action:** Call `gemini_cloud_assist:design_infra` with `applicationUri` (format: projects/{project}/locations/{location}/spaces/{spaceId}/applications/{applicationId}) to get suggested fixes.
        - Convert the returned response to JSON. The value of a parameter may be a JSON string that needs to be parsed.
        - **Expected Output Structure from Troubleshooting:**
          ```json
          {
            "summary": "...",
            "troubleshootingSteps": [
              {
                "description": "...",
                "gcloud_commands": ["gcloud ..."],
                "componentParameters": null
              },
              {
                "description": "...",
                "gcloud_commands": null,
                "componentParameters": [
                  {
                    "componentUri": "projects/.../components/comp-a",
                    "parameters": [
                      { "key": "param1", "value": "new_value" },
                      { "key": "param3", "value": "another" }
                    ]
                  }
                ]
              }
            ]
          }
          ```
    2.  **Analyze Troubleshooting Steps**: Iterate through each `step` in `troubleshootingSteps`. Identify if `gcloud_commands` or `component_parameters` are provided.
    3.  **Update Application Template**:
        - **If `component_parameters` updates are suggested**:
          1. Get the `application_template_id` from the Application object obtained in Step 2. The value is present at `serialized_application_template.uri`. Get the `application_template_id` from the uri.
          2. **Update Application Template**: Call `application_design_center:manage_application_template` with `APPLICATION_TEMPLATE_OPERATION_UPDATE_COMPONENT_PARAMETERS`.
             - **Tool**: `application_design_center:manage_application_template`
             - **Arguments**: `parent`, `applicationTemplateId`, `componentParameters`, `operation` - `APPLICATION_TEMPLATE_OPERATION_UPDATE_COMPONENT_PARAMETERS`
          3. **Example**:
             ```json
             {
               "applicationTemplateId": "my-template",
               "componentParameters": [
                 {
                   "component": "projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-template/components/cloud-run-1",
                   "parameters": [
                     {
                       "key": "containers",
                       "value": [
                         {
                           "container_image": "us-docker.pkg.dev/cloudrun/container/hello",
                           "container_name": "service-container",
                           "ports": {
                             "container_port": 8080,
                             "name": "http1"
                           },
                           "resources": {
                             "cpu_idle": false,
                             "limits": {
                               "cpu": "4",
                               "memory": "16Gi"
                             },
                             "startup_cpu_boost": false
                           }
                         }
                       ]
                     }
                   ]
                 }
               ],
               "operation": "APPLICATION_TEMPLATE_OPERATION_UPDATE_COMPONENT_PARAMETERS",
               "parent": "projects/my-project/locations/us-central1/spaces/my-space"
             }
             ```
    4.  **Retry Deployment**:
        - **Action**: Attempt to deploy the application again.
        - **Tool**: `application_design_center:manage_application`
        - **Arguments**: `project`, `location`, `spaceId`, `applicationTemplateUri`, `applicationId`, `serviceAccount`. `operation` - `APPLICATION_OPERATION_DEPLOY`
    5.  **Iterate if Necessary**: If deployment fails again, repeat troubleshooting steps up to 5 times. Report the history to the user if the limit is reached.
    **Operational Notes:**
    * Mutating tool calls often return an LRO.
    * Always poll LROs on behalf of the user; do not ask the user to run the polling command.
    * Do not sleep during deployment status polling. Poll actively every 30-60 seconds until the LRO is done.
    * Apply `debug_deployment` responses exactly as provided.
    * For retries, disregard previous attempts and start from Step 2 again.
    * Handle bad-gateway errors during commit with jittered retries and verify the template revision.
    * Exclude `PORT` from being explicitly set as a Cloud Run environment variables as it is a reserved name.
    
    ### Phase 6: Verification & E2E Testing
    Following a successful deployment:
    - Verify that services are using correct container image URLs and that each component is healthy.
    - Conduct a simple demo test to ensure E2E functionality and validate the hosted services are working as expected.
    

#### Operate on Google Cloud
    
    
    ---
    name: operating-google-cloud
    description: Comprehensive management of GCP resources and Kubernetes. Supports direct tool delegation for assistance, infrastructure design, troubleshooting, cost optimization, and resource mutations.
    ---
    
    # Managing GCP and Kubernetes
    
    ## Index
    1. [Overview](#overview)
    2. [Tool Usage & Routing](#tool-usage--routing)
    3. [Instructions and Constraints](#instructions-and-constraints)
    
    ## Overview
    GCP and Kubernetes resources and mutations should use MCP tools. These tools are specialized backend agents. As the client agent, your role is to identify the intent and delegate the entire task verbatim to the appropriate intelligent tool.
    
    **Note:** These tools are part of the `gemini_cloud_assist` and `application_design_center` MCP Servers. Tool names are qualified with their respective server names (e.g., `gemini_cloud_assist:tool_name`).
    
    ## Tool Usage & Routing
    
    1.  **General Assistance & Orchestration**: Use `gemini_cloud_assist:ask_cloud_assist` for general inquiries, estate queries (e.g., "List my active VMs"), low-complexity directives, and triage of ambiguous issues.
        *   *Triggers*: Broad questions, status checks, exploratory queries, mutative directives (e.g., "Restart VM", "Scale cluster").
        *   *Routing*: This is the **default choice** for intents that are purely informational or involve general cloud concepts.
    
    2.  **Infrastructure Design & Architecture**: Use `gemini_cloud_assist:design_infra` for designing, architecting, or deploying infrastructure.
        *   *Commands*: 
            - `manage_app_design`: Use for comprehensive ADC application designs and IaC imports.
            - `generate_terraform`: Use for single-resource Terraform generation.
            - `generate_gcloud` / `generate_bigquery`: Use for generating CLI commands.
            - `generate_kubernetes_yaml`: Use for Kubernetes manifests.
            - `debug_deployment`: Use for debugging ADC deployment failures.
    
    3.  **Troubleshooting & Deep Diagnostics**: Use `gemini_cloud_assist:investigate_issue` for specialized "SRE in a box" diagnostics and Root Cause Analysis (RCA).
        *   *Triggers*: Outages, crashes, latency spikes, deep debugging, error log reasoning, and understanding application dependencies (topology).
        *   *Routing*: Use when the user asks "Why" a failure occurred or needs remediation for a known incident.
    
    4.  **Cost Optimization**: Use `gemini_cloud_assist:optimize_costs` for analyzing spend and identifying savings.
        *   *Triggers*: Spending analysis, top cost drivers, identifying idle or underutilized resources for the purpose of saving money.
        *   *Constraints*: This tool is **read-only**; it provides analysis but does not execute changes. Do not use for general utilization queries unrelated to cost.
    
    5.  **GKE Resource Mutations**: Use `gemini_cloud_assist:invoke_operation` specifically for GKE operations.
        *   *Operation Types*: `GKE_APPLY` (for raw YAML manifests) and `GKE_PATCH` (for specific JSON patches).
        *   *Input Requirement*: The `userQuery` must be a stringified JSON object containing `operation_type` and the corresponding `gke_apply` or `gke_patch` details.
    
    ## Instructions and Constraints
    When answering any queries about Google Cloud Platform (GCP), YOU MUST follow these rules:
    
    - **Context ID Persistence:** All Gemini Cloud Assist (GCA) tools return a `contextId` in their response. Ensure that any subsequent turns to a GCA tool pass this `contextId` as a parameter to maintain multi-turn conversation state.
    - **Direct Tool Mapping:** Upon receiving a request about GCP resources, immediately invoke the relevant tool identified in the Routing section.
    - **Context Integrity:** Pass the user's entire prompt exactly as provided; maintain the original query without summarization, rephrasing, or truncation.
    - **Atomic Delegation:** Execute the request as a single turn; delegate the entire problem to the tool rather than breaking it down into intermediate queries.
    - **Identifier Precision:** Include all identifiers (Project IDs, Cluster names, or Instance paths) discovered in the prompt.
    - **Local Context Enrichment:** Forward the user's query to the tools along with any additional relevant local context identified in the working directory.
    - **Persistence to Local Workspace:** Save any configuration, manifest, or YAML generated or updated by the tools to the local workspace.
    - **Tool Exclusivity:** Rely exclusively on the provided MCP tools for cloud interactions; refrain from executing local commands such as `gcloud` or `kubectl`.
    - **Remote Source of Truth:** Rely solely on MCP tools to discover and validate the existence of cloud resources; bypass local validation against configuration files like `.gcloud/config` or `kubeconfig`.
    - **Execution Workflow:** Always ask the user if they want to apply the YAML using `gemini_cloud_assist:invoke_operation` after generation. Explicitly ask: "Would you like to proceed with applying this configuration?". If the user confirms, invoke the tool to apply the manifests.
    

## What's next

  * [View other Gemini for Google Cloud administrator settings](https://docs.cloud.google.com/gemini/docs/admin-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
