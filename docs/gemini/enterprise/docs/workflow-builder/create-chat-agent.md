---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent/
title: Create a chat agent \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:15:22.811192+00:00
---

# Create a chat agent  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Create a chat agent Stay organized with collections  Save and categorize content based on your preferences. 

You can create a new chat agent using the following methods:

  * Using a prompt: This is the quickest way to create a chat agent. You describe the agent's purpose, and Workflow Builder generates the initial version for you within your app. This is ideal for basic agents or as a starting point for more complex ones.
  * Using the flow builder: This method gives you direct, granular control over the agent's design from the beginning. It's ideal for designing complex, multi-step agents that require specific subagent configurations and logic flows.



These methods are flexible, and you can combine them to suit your requirements. For example, you can start with a prompt to generate the initial chat agent and then switch to the flow builder to visually refine its logic and add complexity.

## Before you begin

  * Ensure you have a web app with the necessary data sources connected. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).
  * Ensure that you have enabled the Workflow Builder feature toggle for your web app. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).



## Best practices for creating agents

To ensure your agents perform effectively and efficiently, consider the following best practices:

  * **Define clear objectives:** clearly state what you want your agent to achieve. A well-defined objective helps in designing the agent's logic and evaluating its performance.
  * **Start small, then expand:** begin with a basic agent that handles core functionalities. Once it's stable, gradually add more features and complexity.
  * **Break down complex tasks:** for multi-step agents, divide large tasks into smaller, manageable sub-tasks. Each subagent should have a specific role.
  * **Test iteratively:** regularly test your agent at each stage of development. This helps identify and fix issues early.
  * **Provide clear instructions:** when using prompts, be specific and concise. Avoid ambiguity to ensure the agent understands its purpose. See Best practices for writing prompts to create an agent.
  * **Use connected data stores for large document libraries:** Gemini Enterprise loads files that you upload to an agent's **Knowledge** section (or attach in a chat session) directly into the model's context window on every turn, up to a combined limit of 800,000 tokens. For large static reference libraries, policy manuals, or dense PDFs (such as documents over 100 pages), ingest the documents into a connected data store and enable it under **Manage your data** rather than uploading the files directly. Reserve direct file uploads for smaller, session-specific documents or multi-sheet spreadsheets. See [Knowledge base and file upload limits](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits#knowledge-upload-limits).



## Create a chat agent using prompts

Use this method to quickly build a chat agent using conversational input.

### App

To create a chat agent using a natural language prompt, do the following:

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click **\+ Create agent > Chat agent**.

The agent canvas opens in chat mode.

  3. Enter a prompt that describes your agent's purpose and intended behavior.

**Note:** You can't use conversational prompts to enable or connect to data stores from the _Cloud sources_ category (for example, BigQuery, Cloud Storage, Cloud SQL). Create your agent using the designer mode for such tasks.**Tip:** See Best practices for writing prompts to create an agent.
  4. Optional: Click ![Agents icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/database_spark_icon.png)**Manage your data** and enable or disable the data sources you want your agent to use.

  5. Optional: Click add_circle **Add files** to upload any additional reference materials for your agent to use.

  6. Click send **Submit**.

The chat agent canvas appears, displaying a live preview of your agent.

  7. In the **Preview** tab, interact with your agent to test and evaluate its responses.

  8. Optional: Refine your agent's function and behaviour by providing additional instructions in the left chat pane.

  9. To view the overall details of your agent, go to the **Flow** tab and click the main agent node.

     * Optional: In the **Knowledge** section, click add_circle **Add files** to upload any additional reference materials for your agent.
     * Optional: In the **Personalization** section, add starter prompts that guide users on how to interact with the agent. You can add as many starter prompts as you like, but the system shows you a random selection of up to three prompts at a time.
  10. Optional: Click the **Schedule** tab to configure execution schedules for your agent. For more information about agent schedules, see [Schedule agent executions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent).

  11. Click **Create** to launch and start using your agent.

**Note:** Exiting the agent canvas without clicking **Create** puts your agent in a _Draft_ state.



### Best practices for writing prompts to create a chat agent

The prompt you provide helps Gemini understand your goals and generate the best possible agent. To get clear and relevant responses, follow these guidelines and best practices:

  * **Provide enough context to eliminate ambiguity**

Be specific about what you want the agent to do. For example, specify the level of detail, the types of examples to use, or the required output. This helps Gemini Enterprise to generate an agent plan that is more relevant and specific to your needs.

Not recommended: `Create an agent for sales emails.`

Recommended: `Create an agent that drafts follow-up emails for new sales leads from my CRM. It should search for the contact's company, summarize their business, and suggest how our product can help them.`

  * **Set boundaries or limitations on the agent's output**

Define what the agent should and shouldn't do. You can set limits on the length of its responses, the format, the tone, or specific elements to include or exclude. This helps the agent stay focused and produce more predictable results.

Not recommended: `Create a sales email agent.`

Recommended: `Create an agent that drafts follow-up emails for sales leads. The drafts should always use a professional tone, be no more than three paragraphs, and never include personal information about the client.`

  * **Prompt Gemini to ask you questions**

Instruct Gemini to ask you questions, if needed. This allows Gemini to gather details that it might have missed, and ensures that the resulting agent plan meets your expectations.

Not recommended: `Create an agent to handle sales emails.`

Recommended: `I need an agent that can help me draft sales emails. First, ask me what information you need to effectively qualify a lead and draft a personalized message.`




**Examples of effective prompts**

  * **Simple example:** `Create a sales email agent that drafts concise follow-up emails to new leads. The tone should be professional, and the email should be no more than three paragraphs.`

  * **Advanced example:** `Create an agent that automatically drafts sales emails to leads. Use my Gmail and access emails with the 'leads' label. First, ask me to confirm which leads you should prioritize and what the main selling points are for each. Once you have this information, your drafts should be no more than three paragraphs and use a professional tone. Don't include any technical jargon or slang and never include any personal information about the client.`




## Create a chat agent using the flow builder

Use this method for granular control over agent design, model selection, and multi-step orchestration.

### App

To create a chat agent using the flow builder, do the following:

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click **\+ Create agent > Chat agent**.

The agent canvas opens in chat mode.

  3. Click **Proceed to builder** to switch to designer mode.

A default agent name, **My Agent** , is created in the canvas.

  4. To view and configure the node details, click the **My Agent** node and do the following:

     1. **Name:** enter a name for your agent.
     2. **Description:** enter a summary of the agent's purpose.
     3. **Instructions:** provide a detailed set of instructions that define the agent's objectives, tasks, and behaviors.
     4. **Model:** select the Gemini LLM model for the agent to use. Use a **Flash** model for low-latency lookups and everyday conversational tasks, and reserve **Pro** models for complex multi-step reasoning or multi-document synthesis.
     5. **Data and tools:** click add_circle **Add data sources & tools** to add the data sources connected to your app.
     6. Optional: In the **Knowledge** section, click add_circle**Add files** to upload any additional reference materials for your agent.
     7. Optional: In the **Personalization** section, add starter prompts that guide users on how to interact with the agent. You can add as many starter prompts as you like, but the system shows you a random selection of up to three prompts at a time.
  5. Build your subagent flow:

     1. In the **Flow** tab, hold the pointer over the main agent node, and then click add_circle **Add subagent**.
     2. Configure the subagent details.
  6. Repeat _step 5_ as needed to complete your subagent flow logic.

  7. Optional: Click the **Schedule** tab to configure execution schedules for your agent.

  8. Click the **Preview** tab to interact with your agent to test and evaluate if your agent flow logic is performing as expected.

  9. Click **Create** to publish and start using your chat agent.

**Note:** Exiting the Workflow Builder canvas without clicking **Create** puts your agent in a _Draft_ state.



## What's next

  * Learn how to [use a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-chat-agent).
  * Learn how to [schedule chat agent runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent).
  * Learn how to [edit a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent).
  * Learn how to [share a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent).
  * Learn how to [delete a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-chat-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
