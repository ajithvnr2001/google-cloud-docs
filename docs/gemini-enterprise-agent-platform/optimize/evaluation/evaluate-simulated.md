---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-simulated/
title: Simulate agent behavior \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:28.445766+00:00
---

# Simulate agent behavior  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-simulated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Simulate agent behavior Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

To simulate and evaluate agent behavior, ensure you have completed the following:

  * **Create an agent version** : Simulation requires an immutable snapshot of your agent's configuration, including system instructions, tools, and model, etc. Ensure you have created at least one version of your agent in the [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry).
  * **Initialize the SDK** : If you plan to run simulation programmatically, install the **Agent Platform SDK** and initialize the client as described in [Evaluate your agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-agents).



Simulation allows you to build a comprehensive evaluation suite from scratch, even without existing production data. This process uses LLMs to automatically generate test cases and then roleplay as a user to stress-test your agent's multi-turn conversational logic.

## The 2-step simulation workflow

Testing a new agent typically follows a two-stage process:

  1. **Generate Scenarios:** Create a dataset of "test specs" based on your agent's instructions and tool definitions.

  2. **Simulate Sessions:** Execute those specs by having a simulated user interact with your agent to produce behavior **traces**. A **trace** is a factual, immutable record of the agent's behavior, including model inputs, responses, and tool calls.




In the first step, the system creates **eval cases**. An **eval case** is a specification that defines an agent's task. Each case consists of two elements:

  * **Starting Prompt:** The first message a user sends to the agent.
  * **Conversation Plan:** A hidden "instruction" for the simulated user, describing their goals and how they should react if the agent asks certain questions.



In the second step, the system generates list of agent behaviors in canonical agent data format.

### Generate scenarios in the console

  1. In the Google Cloud console, navigate to the **Agent Platform > Agents > Evaluation** page. 

[Go to Evaluation](https://console.cloud.google.com/agent-platform/agent-evaluation)

  2. Click **New evaluation** and select **Simulate sessions**.

  3. Enter a **Generation instruction** to guide the scenarios (for example, "Generate scenarios where the user tries to book a flight but then changes their mind").

  4. Review the generated table. You can edit the prompts or manually add your own test cases.




## Run user simulation

Once your scenarios are generated, the **User Simulator** acts as the user to drive the conversation forward.

### User simulation settings

When running the simulation, you can configure the following attributes:

  * **Max Turn:** Maximum number of invocations allowed by the multi-turn agent run. This property allows us to stop a run-off conversation where the agent and the user simulator get into a never ending loop. (The default value is 5).
  * **Model Name:** The model name to simulate next user message for multi-turn agent run.
  * **Model Configuration:** The configuration of the model to simulate user message.



### SDK Example: Programmatic Simulation

You can also bootstrap your evaluation suite using the **Agent Platform SDK** :
    
    
    # 1. Define agent
    travel_agent = Agent(
        model="gemini-3-flash-preview",
        name='travel_agent',
        instruction='You are a travel expert, help users to find flights, book flights with flight ID',
        tools=[find_flights, book_flight],
    )
    
    # 2. Generate scenarios from agent info
    travel_agent_info = types.evals.AgentInfo.load_from_agent(agent=travel_agent)
    
    eval_dataset = client.evals.generate_conversation_scenarios(
        agent_info=travel_agent_info,
        config={
            "count": 5,
            "generation_instruction": "Generate scenarios where the user tries to book a flight.",
            "environment_context": "Today is Monday. I am located in San Francisco. Flights to Paris, New York, Tokyo, Chicago, Sydney, etc are available.",
        },
    )
    
    # 3. Simulate multi-turn interactions
    eval_dataset_with_traces = client.evals.run_inference(
        agent=travel_agent,
        src=eval_dataset,
        config={
            "user_simulator_config": {
                "max_turn": 5
            }
        }
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
