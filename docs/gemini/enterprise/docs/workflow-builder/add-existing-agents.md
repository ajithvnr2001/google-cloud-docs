---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/add-existing-agents/
title: Add an existing agent step \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:00.753714+00:00
---

# Add an existing agent step  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/add-existing-agents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Add an existing agent step Stay organized with collections  Save and categorize content based on your preferences. 

You can add existing AI agents as steps in your workflow to transfer tasks to specialized agents. This lets you compose multi-agent workflows that orchestrate among different agents, each handling a specific part of a larger process.

**At a glance:**

  * **Purpose:** Reuse specialized ADK and A2A agents as steps within Workflow Builder workflows.
  * **Clarifying questions:** Allows referenced agents to pause execution and ask the user for missing details instead of failing or guessing.
  * **Integration options:** Supported natively for custom A2A agents (`input-required`) and ADK agents (`RequestInput`).



## Before you begin

Before using this feature, complete the following steps:

  * Make sure a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Make sure the agents you want to add are available in your organization. This feature supports the addition of the following agents:

    * [ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
    * [A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent)



## Add an existing agent step

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing agent or [create a new agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent).
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **Existing agents** to expand the section.
  5. Browse the list of available agents.

**Note:** The agent picker displays published ADK and A2A agents that your organization has shared with you. Cross-project agents are not displayed.
  6. Click the agent you want to add.

The system adds the existing agent step to your workflow. The selected agent runs as part of your workflow, receiving input from earlier steps and passing output to later steps.

**Note:** If you add an A2A or ADK agent that requires user OAuth for authentication, you must first authenticate and then start a new run of the workflow.
  7. In the canvas, click the existing agent step to open its configuration panel, and configure the following:

     * **Prompt** : Enter the prompt or instructions used to trigger the agent. You can include static text or reference outputs from previous steps (for example, `${step_name.output}`).



The agent step is a dynamic reference to the selected agent. If the source agent is updated or a new version is made live, your workflow automatically uses the most recent version.

For more information on the limitations of this feature, see [Known issues and limitations](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#add_an_existing_agent_step).

## How clarifying questions work

When an existing agent runs in a workflow, it can pause execution to ask the user a clarifying question if it needs missing information to complete its task. Clarifying questions are supported natively when the referenced agent emits an `input-required` signal (A2A) or a `RequestInput` event (ADK).

When an existing agent step runs and requires additional information:

  1. **Execution pauses** : The workflow pauses execution at the existing agent step and initiates a human-in-the-loop (HITL) prompt.
  2. **User answers the prompt** : The Gemini Enterprise web app displays the agent's clarifying question to the user along with a text field to enter their response.
  3. **Execution resumes** : When the user submits their answer, the workflow resumes the existing agent, passing the user's answer back to the agent.
  4. **Multi-turn support** : The agent can ask multiple clarifying questions in succession across multiple turns until it gathers all required information and produces its final output.



### Context isolation

During a clarifying question exchange, the referenced agent only receives its own interaction history with the user and the initial prompt configured for the node. Outputs and variables from other steps in the workflow are not automatically passed to the referenced agent unless explicitly referenced in the step's prompt.

## Implement clarifying questions in your agent

To support clarifying questions, configure your custom agent to emit a protocol-level request-input signal when it needs additional information.

### A2A agents (native)

For agents that implement the Agent-to-Agent (A2A) protocol directly, return the task in the `input-required` state with `TaskUpdater`, providing the clarifying question in the message payload:
    
    
    from a2a.server.tasks import TaskUpdater
    from a2a.types import Message, Part, Role, TextPart
    
    # Inside your custom agent's task executor class:
    async def execute(self, context, event_queue):
        updater = TaskUpdater(event_queue, context.task_id, context.context_id)
        if context.current_task is None:
            await updater.submit()
        await updater.start_work()
    
        user_input = context.get_user_input()
        if "weather" in user_input and "tokyo" not in user_input.lower():
            await updater.requires_input(
                Message(
                    message_id=f"q-{context.task_id}",
                    role=Role.agent,
                    parts=[Part(root=TextPart(
                        text="Which city would you like the weather for?"))],
                    task_id=context.task_id,
                    context_id=context.context_id,
                )
            )
            return
    
        await updater.complete(
            Message(
                message_id=f"a-{context.task_id}",
                role=Role.agent,
                parts=[Part(root=TextPart(
                    text="It is sunny and 72°F in Tokyo."))],
                task_id=context.task_id,
                context_id=context.context_id,
            )
        )
    

The user's response is sent back to your agent as a `message/send` request with the same `taskId`.

### A2A agents (built with ADK)

If your agent is built with the Agent Development Kit (ADK) and exposed through A2A (using `to_a2a()`), wrap your question-asking function in `LongRunningFunctionTool`:
    
    
    from google.adk.agents import Agent
    from google.adk.tools.long_running_tool import LongRunningFunctionTool
    from google.adk.a2a.utils.agent_to_a2a import to_a2a
    
    def get_weather(city: str) -> str:
        """Returns weather information for a city."""
        return f"It is sunny and 72°F in {city}."
    
    def ask_clarifying_question(question: str) -> None:
        """Asks the user a question and waits for their reply."""
        return None
    
    root_agent = Agent(
        model="gemini-2.5-flash",
        name="weather_agent",
        instruction=(
            "If the user asks for weather without specifying a city, call "
            "`ask_clarifying_question` and wait. Do not guess."
        ),
        tools=[get_weather, LongRunningFunctionTool(ask_clarifying_question)],
    )
    
    a2a_app = to_a2a(root_agent, port=8000)
    

**Note:** The function passed to `LongRunningFunctionTool` must return `None`. If it returns a value, the step completes instead of pausing. 

### ADK agents on Agent Engine

For reasoning-engine-hosted ADK agents on Agent Engine, emit a `RequestInput` event within a generator tool or custom agent step:
    
    
    from google.adk.events import RequestInput
    
    # Inside a generator tool or custom agent step
    def ask_for_details():
        """Requests user input during tool or step execution."""
        yield RequestInput(
            interrupt_id="weather_city",
            message="Which city would you like the weather for?",
        )
    

## What's next

  * Learn how to [configure Agent node connectors and actions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions).
  * Learn how to [connect MCP servers](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/connect-mcp-servers).
  * Learn how to [use flow control steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
