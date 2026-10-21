---
url: https://docs.cloud.google.com/iam/docs/create-and-deploy-agent/
title: Create and deploy an agent with Agent CLI and Agent Identity \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:06.370037+00:00
---

# Create and deploy an agent with Agent CLI and Agent Identity  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-and-deploy-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create and deploy an agent with Agent CLI and Agent Identity Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to create and deploy an agent in Agent Runtime on Gemini Enterprise Agent Platform with Agent Identity enabled.

Agent Identity assigns a secure SPIFFE identity to your deployed agent. The agent uses this identity to authenticate to Google Cloud services and retrieve credentials from the Agent Identity auth manager.

## Before you begin

  1. Enable the Agent Identity API, Agent Platform API, Agent Registry API, and App Hub API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=agentidentity.googleapis.com,agentregistry.googleapis.com,aiplatform.googleapis.com,apphub.googleapis.com)

  2. Ensure you have the **Agent Platform User** (`roles/aiplatform.user`) role on your project.




## Create and deploy the agent

Create a sample agent using `google-agents-cli` and deploy it with Agent Identity:

  1. Install `uv`, and then run the `google-agents-cli` setup:
         
         pip install uv
         uvx google-agents-cli setup

  2. Create an agent project using the prototype template:
         
         uvx google-agents-cli create AGENT_PROJECT --prototype --yes

Replace `AGENT_PROJECT` with the name for your new agent project directory (for example, `maps-agent`).

This command generates the following project directory structure:
         
         AGENT_PROJECT/
         ├── app/                       # Core agent code
         │   ├── agent.py               # Main agent logic
         │   ├── fast_api_app.py        # Client application logic
         │   └── app_utils/             # App utilities and helpers
         ├── tests/                     # Unit and integration tests
         ├── GEMINI.md                  # Development guide
         └── pyproject.toml             # Project dependencies

**Note:** The previous tree highlights the relevant configuration files and might not represent all files in your directory.
  3. Rename the default application folder (`app`) to match your agent name (`AGENT_NAME`, for example, `maps_agent`). Agent names must be a valid Python identifier: they must start with a letter, and contain only letters, numbers, and underscores.
         
         cd AGENT_PROJECT
         mv app AGENT_NAME

  4. Update your `agent.py` configuration file to reflect the new name:
         
         # In AGENT_PROJECT/AGENT_NAME/agent.py
         app = App(
             root_agent=root_agent,
             name="AGENT_NAME",
         )

  5. Choose a model to use, based on its [regional availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#google-models). Update the value for `MODEL` in `agent.py` to match your chosen model.

####  Workaround for models that are only available in the `global` region 

To use a model that's only available in the `global` region, you must modify `agent.py` so that your agent can access it. 

     1. Add the following imports:
            
            from functools import cached_property
            from google.genai import Client

     2. Add the following subclass after the imports:
            
            class GlobalGemini(Gemini):
                @cached_property
                def api_client(self) -> Client:
                    return Client(enterprise=True, location="global")

     3. Find the following code:
            
            root_agent = Agent(
                name="root_agent",
                model=Gemini(

Change it to reference the new subclass:
            
            root_agent = Agent(
                name="root_agent",
                model=GlobalGemini(

  6. Enable Agent Identity by creating a config file:
         
         echo '{ "identity_type": "AGENT_IDENTITY" }' > AGENT_NAME/.agent_engine_config.json

  7. Create a `requirements.txt` file for the deployment dependencies:
         
         uv export \
             --no-emit-workspace \
             --no-hashes \
             --format requirements.txt \
             --output-file AGENT_NAME/requirements.txt

  8. Verify the project directory structure:
         
         AGENT_PROJECT/
         ├── AGENT_NAME/                 # Agent application folder
         │   ├── .agent_engine_config.json # Agent Identity configuration
         │   ├── agent.py                  # Main agent logic
         │   ├── fast_api_app.py           # Client application logic
         │   ├── requirements.txt          # Deployment dependencies
         │   └── app_utils/                # App helpers
         ├── tests/                        # Tests
         ├── GEMINI.md                     # Development guide
         └── pyproject.toml                # Project dependencies

  9. Test your agent locally:
         
         uv run adk web . --port 8501 --reload_agents

**Note:** If you're testing on Cloud Shell, you must add the `--allow_origins="*"` flag to bypass CORS issues.

To validate your agent, do the following:

     1. Go to `http://localhost:8501`. Alternatively, if you're using Cloud Shell, click the link provided by the web server output.

     2. In the chat interface, send a test prompt to verify the response.

  10. Terminate the server with `CTRL`+`C`.

  11. Deploy your agent to Google Cloud:
         
         uv run adk deploy agent_engine AGENT_NAME \
             --project="PROJECT_ID" \
             --region="LOCATION"

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID.

     * `LOCATION`: The [supported region](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations) where you want to deploy the agent (for example, `us-west1`).

The deployment can take a few minutes to complete. After it finishes, the CLI outputs a confirmation message and a link to your agent's playground in the Google Cloud console.

  12. Retrieve your agent's SPIFFE ID (Agent Identity):

     1. In the Google Cloud console, go to the **Deployments** page.

[Go to Deployments](https://console.cloud.google.com/agent-platform/runtimes)

     2. To copy your agent's SPIFFE ID to the clipboard, find the row that your deployed agent is in, and in the **Identity** column of that row click content_copy **Copy to clipboard**. The identity looks similar to the following: `principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/ENGINE_ID`.




## What's next

  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Agent Identity auth manager overview](https://docs.cloud.google.com/iam/docs/auth-manager-overview)
  * [Authenticate using 3-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-3lo-v2)
  * [Authenticate using 2-legged OAuth with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-2lo-v2)
  * [Authenticate using API key with auth manager](https://docs.cloud.google.com/iam/docs/auth-with-api-key-v2)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
