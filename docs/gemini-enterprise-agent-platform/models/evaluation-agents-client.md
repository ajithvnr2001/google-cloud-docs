---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents-client/
title: Evaluate generative AI agents using the GenAI Client in Agent Platform SDK \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:39.241615+00:00
---

# Evaluate generative AI agents using the GenAI Client in Agent Platform SDK  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Evaluate generative AI agents using the GenAI Client in Agent Platform SDK Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you build and evaluate your generative AI model, you might use the model to build an agent such as a chatbot. The Gen AI evals lets you measure your agent's ability to complete tasks and goals for your use case.

This page shows you how to create and deploy a basic agent and use the Gen AI evals to evaluate the agent:

  * Develop an agent: Define an agent with basic tool functions.

  * Deploy an agent: Deploy the agent to Agent Platform Runtime.

  * Run agent inference: Define an evaluation dataset and run agent inference to generate responses.

  * Create evaluation run: Create an evaluation run to perform evaluation.

  * View evaluation results: View the evaluation results through the evaluation run.




To see an example of Create a Gen AI Agent Evaluation for a Deployed Agent, run the "Create & Deploy Agent and Run Gen AI Agent Evaluation" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/create_agent_and_run_evaluation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fcreate_agent_and_run_evaluation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fcreate_agent_and_run_evaluation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/create_agent_and_run_evaluation.ipynb)

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Install the Agent Platform SDK for Python:
         
         %pip install google-cloud-aiplatform[adk,agent_engines]
         %pip install --upgrade --force-reinstall -q google-cloud-aiplatform[evaluation]
         

  3. Set up your credentials. If you are running this tutorial in Colaboratory, run the following:
         
         from google.colab import auth
         auth.authenticate_user()
         

For other environments, refer to [Authenticate to Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/authentication#client-libraries).

  4. Initialize the GenAI Client in Agent Platform SDK:
         
         import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
         from vertexai import Client
         from google.genai import [types](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.html) as genai_types
         
         GCS_DEST = "gs://BUCKET_NAME/output-path"
         [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
             project=PROJECT_ID,
             location=LOCATION,
         )
         
         client = Client(
             project=PROJECT_ID,
             location=LOCATION,
             http_options=genai_types.HttpOptions(api_version="v1beta1"),
           )
         

Replace the following:

     * BUCKET_NAME: Cloud Storage bucket name. See [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to learn more about creating buckets.

     * PROJECT_ID: Your project ID.

     * LOCATION: Your selected region.




## Develop an agent

Develop an Agent Development Kit (ADK) agent by defining the model, instruction, and set of tools. For more information on developing an agent, see [Develop an Agent Development Kit agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-adk-agent).
    
    
    from google.adk import Agent
    
    # Define Agent Tools
    def search_products(query: str):
        """Searches for products based on a query."""
        # Mock response for demonstration
        if "headphones" in query.lower():
            return {"products": [{"name": "Wireless Headphones", "id": "B08H8H8H8H"}]}
        else:
            return {"products": []}
    
    def get_product_details(product_id: str):
        """Gets the details for a given product ID."""
        if product_id == "B08H8H8H8H":
            return {"details": "Noise-cancelling, 20-hour battery life."}
        else:
            return {"error": "Product not found."}
    
    def add_to_cart(product_id: str, quantity: int):
        """Adds a specified quantity of a product to the cart."""
        return {"status": f"Added {quantity} of {product_id} to cart."}
    
    # Define Agent
    my_agent = Agent(
        model="gemini-2.5-flash",
        name='ecommerce_agent',
        instruction='You are an ecommerce expert',
        tools=[search_products, get_product_details, add_to_cart],
    )
    

## Deploy agent

[Deploy your agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) to Agent Platform Runtime. This can take up to 10 minutes. Retrieve the resource name from the deployed agent.
    
    
    def deploy_adk_agent(root_agent):
      """Deploy agent to agent engine.
      Args:
        root_agent: The ADK agent to deploy.
      """
      app = vertexai.agent_engines.AdkApp(
          agent=root_agent,
      )
      remote_app = client.agent_engines.create(
          agent=app,
          config = {
              "staging_bucket": gs://BUCKET_NAME,
              "requirements": ['google-cloud-aiplatform[adk,agent_engines]'],
              "env_vars": {"GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY": "true"}
          }
      )
      return remote_app
    
    agent_engine = deploy_adk_agent(my_agent)
    agent_engine_resource_name = agent_engine.api_resource.name
    

To get the list of agents that are deployed to Agent Platform, see [Manage deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents).

## Generate responses

  1. Generate model responses for your dataset using `run_inference()`:

[Prepare your dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-dataset) as a Pandas DataFrame. The prompts should be specific to your agent. Session inputs are required for traces. For more information, see [Session: Tracking Individual Conversations](https://google.github.io/adk-docs/sessions/session/).
         
         import pandas as pd
         from vertexai import types
         
         session_inputs = types.evals.SessionInput(
             user_id="user_123",
             state={},
         )
         agent_prompts = [
             "Search for 'noise-cancelling headphones'.",
             "Show me the details for product 'B08H8H8H8H'.",
             "Add one pair of 'B08H8H8H8H' to my shopping cart.",
             "Find 'wireless earbuds' and then add the first result to my cart.",
             "I need a new laptop for work, can you find one with at least 16GB of RAM?",
         ]
         agent_dataset = pd.DataFrame({
             "prompt": agent_prompts,
             "session_inputs": [session_inputs] * len(agent_prompts),
         })
         

  2. Generate model responses using `run_inference()`:
         
         agent_dataset_with_inference = client.evals.run_inference(
             agent=agent_engine_resource_name,
             src=agent_dataset,
         )
         

  3. [Visualize your inference results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/view-evaluation#visualizing-inference-results) by calling `.show()` on the `EvaluationDataset` object to inspect the model's outputs alongside your original prompts and references:
         
         agent_dataset_with_inference.show()
         




## Run the agent evaluation

[Run `create_evaluation_run()`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/run-evaluation#run-evaluation) to evaluate the agent responses.

  1. Retrieve the `agent_info` using the built-in helper function:
         
         agent_info = types.evals.AgentInfo.load_from_agent(
             my_agent,
             agent_engine_resource_name
         )
         

  2. Evaluate the model responses using agent-specific [adaptive rubric-based metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/determine-eval) (`FINAL_RESPONSE_QUALITY`, `TOOL_USE_QUALITY`, and `HALLUCINATION`):
         
         evaluation_run = client.evals.create_evaluation_run(
             dataset=agent_dataset_with_inference,
             agent_info=agent_info,
             metrics=[
                 types.RubricMetric.FINAL_RESPONSE_QUALITY,
                 types.RubricMetric.TOOL_USE_QUALITY,
                 types.RubricMetric.HALLUCINATION,
                 types.RubricMetric.SAFETY,
             ],
             dest=GCS_DEST,
         )
         




## View the agent evaluation results

You can view the evaluation results using the Agent Platform SDK.

Retrieve the evaluation run and [visualize your evaluation results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/view-evaluation) by calling `.show()` to display summary metrics and detailed results:
    
    
    evaluation_run = client.evals.get_evaluation_run(
        name=evaluation_run.name,
        include_evaluation_items=True
    )
    
    evaluation_run.show()
    

The detailed results also include traces showing the agent interactions. For more information on traces see [Trace an agent](https://docs.cloud.google.com/agent-builder/agent-engine/manage/tracing).

## What's next

Try the following agent evaluation notebooks:

  * [Evaluate a Langchain agent with Agent Engine](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/evaluating_langchain_agent_engine_prebuilt_template.ipynb)

  * [Evaluate a LangGraph agent with Agent Engine](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/evaluating_langgraph_agent_engine_customized_template.ipynb)

  * [Evaluate a CrewAI agent with Agent Engine](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/evaluating_crewai_agent_engine_customized_template.ipynb)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
