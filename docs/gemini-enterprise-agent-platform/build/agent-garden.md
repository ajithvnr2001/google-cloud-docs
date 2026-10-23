---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden/
title: Agent Garden \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:26.990489+00:00
---

# Agent Garden  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Agent Garden Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [Agent Garden](https://console.cloud.google.com/agent-platform/agent-garden) is a curated library within Google Cloud's Gemini Enterprise Agent Platform that provides prebuilt agent samples. These samples are designed to help developers quickly jumpstart the creation of AI agents by providing high-quality, functional templates for common AI patterns.

Agent Garden simplifies the process of building sophisticated AI applications by offering:

  * **Ready-to-use samples** : Templates like [Retrieval-Augmented Generation (RAG)](https://console.cloud.google.com/agent-platform/agent-garden/samples/retrieval-augmented-generation) that come with pre-configured logic.
  * **Customizable logic** : While the samples work out of the box, they provide [access to GitHub](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents) source code for deep customization.
  * **Integrated infrastructure** : Agents are built to work seamlessly with other Agent Platform components like **RAG Engine** , **Vector Search** , and **Gemini models**.
  * **Use case focused** : Each agent is tailored for specific tasks, such as documentation-grounded customer support or industry-specific research synthesis.



## Deployment steps

To deploy an agent sample from Agent Garden, follow these steps:

  1. Navigate to the [Agent Platform console](https://console.cloud.google.com/agent-platform/) and select **Agent Garden** from the **Agent Builder** section in the left-hand menu to access Agent Garden.
  2. Choose a sample that fits your needs. For example, the [Retrieval-Augmented Generation (RAG)](https://console.cloud.google.com/agent-platform/agent-garden/samples/retrieval-augmented-generation) sample is ideal for building factually grounded Q&A systems.
  3. Configure the following environment settings: 
     * **Project** : Ensure you are in the correct Google Cloud project.
     * **Region** : Select a supported region for your deployment.
     * **Model selection** : Choose the model (for example, Gemini 3 Flash) that your agent will use.
  4. Click **Deploy** , and then select one of the deployment options described in the following section.
  5. Click **Create** or **Confirm** to initialize the agent. The system will provision the necessary resources. You can track the progress in the notification bar or the "Agent Runtime" section.



### Deployment options

When you deploy an agent, you can choose one of three options:

#### Deploy with Agents CLI

This method is the standard and most direct path for deploying agents from the Agent Garden by using the [Agents CLI](https://google.github.io/agents-cli/guide/getting-started/). It is good for learners, prototyping, and rapid testing because it offers a deployment solution with foundational resources for monitoring.

  * **Tool and method** : Pressing the **Deploy** button opens a command-line interface (CLI) with a filled command. Enter the region when asked.
  * **Target environment** : Deploys the agent into an Agent Runtime instance.



#### Deploy E2E implementation with Application Design Center

This option is for full-scale, enterprise-grade deployment. It uses App Design Center, which provides a low-code visual 'ClickOps' configuration experience. You can copy and customize Google-provided templates, such as [Simple Agent Platform](https://docs.cloud.google.com/application-design-center/docs/simple-agent-platform) or [Agent Platform with governance](https://docs.cloud.google.com/application-design-center/docs/agent-platform-with-governance). Then use your customized template to standardize the architecture for every agent that you deploy.

  * **Target environment** : Deploys the agent in an application, which is a complex grouping of production-ready infrastructure and configurations.
  * **Use case** : This option provides the entire enterprise deployment stack, offering significant benefits over simpler deployment methods, including the following: 
    * Managed post-deployment experience across Day 0, 1, and 2.
    * Operational dashboards, FinOps cost optimization, and version control.
    * Security, Compliance, and CI/CD/GitOps integrations.



#### Deploy and register to Gemini Enterprise with Agents CLI

This option focuses on making a production-ready agent discoverable and governed within the corporate ecosystem.

  * **Process** : The agent is first deployed to a managed runtime (like Agent Runtime) using a tool like [Agents CLI](https://google.github.io/agents-cli/guide/getting-started/). The critical second step is registration with Gemini Enterprise.

  * **Target environment** : A Gemini Enterprise Application, using the Agent Platform Agent Runtime as the runtime.

  * **Use case** : Registration is the critical bridge that connects your agent's backend logic to the Gemini Enterprise orchestration layer.




## Post-deployment and testing

Once deployed, you have several options to interact with your new agent:

  * **Preview** : Use the **Open Agent** button to test the agent's performance in a chat interface immediately.
  * **Debug** : Toggle the **Show debug panel** to see the underlying reasoning, tool calls, and retrieval steps the agent is taking.
  * **Expand** : Use the **Tools** menu to connect your agent to external APIs or private data stores.

**Tip:** If you want to modify the core behavior, use the [Open GitHub](https://www.google.com/search?q=https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents) link on the sample page to clone the repository and deploy your custom version using the Agent Platform SDK.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
