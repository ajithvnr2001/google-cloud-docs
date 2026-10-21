---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/create-agent/
title: Create an agent application \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:20.452454+00:00
---

# Create an agent application  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/create-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Create an agent application Stay organized with collections  Save and categorize content based on your preferences. 

This guide takes you through the steps to create a basic agent application that can answer user queries about the weather.

## Before you begin

Be sure to complete [setup instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/setup) before following this guide.

## Create an agent application

Create an agent application and root agent:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Select your project.
  3. Click **Create agent** or **New agent**.
  4. Provide "weather app" as the agent name.
  5. Click **Create**. If this is the first agent application you have created for the project, creation may take 1-2 minutes. The _agent builder_ is shown and, a root agent is created for you.



## Create the agent hierarchy

This agent application will use three [agents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent):

  * Root agent to greet the user and delegate to other sub-agents.
  * Weather agent to answer weather related questions.
  * Farewell agent to complete the conversation.



The root agent is already created, but you should update the settings for this agent:

  1. Click the title bar of the root agent.
  2. You can optionally change the name of the agent.
  3. Enter the description: "Handles simple greetings and delegates to other agents".
  4. Click **Save** , then close the settings panel.



Create the weather agent:

  1. Click the **+** button at the bottom of the root agent.
  2. Click **Add new sub-agent**.
  3. Click the title bar of the new agent.
  4. Change the name to "Weather agent".
  5. Enter the description: "Handles any weather related questions from the user".
  6. Click **Save** , then close the settings panel.



In a similar manner, create another sub-agent of the root agent called "Farewell agent" with a description of "Handles user farewells and goodbyes".

![screenshot of agent hierarchy](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/get-started-agent-hierarchy.png)

## Create a weather tool

[Tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool) are used to connect your agent to external systems or inline code supplied to the agent. This allows your agent to interact with other systems to fetch, update, format, or analyze information.

In this step, you create a weather tool, which is used to fetch weather information. For the sake of this guide, this tool has a mocked response for the user. In a real weather application, this tool would access an external server to get information.

Create the weather tool:

  1. Click the tools button on the right side of the agent builder.
  2. Click **+** to create a new tool for the agent application.
  3. Click **Python code**.
  4. Paste the following code:
         
         def get_weather(city: str) -> dict:
           """Retrieves the current weather report for a specified city.
         
           Args:
             city (str): The name of the city.
         
           Returns:
             dict: A dictionary containing the weather information.
                   Includes a 'status' key ('success' or 'error').
                   If 'success', includes a 'report' key with weather details.
                   If 'error', includes an 'error_message' key.
           """
           city_normalized = city.lower().replace(" ", "")
         
           mock_weather_db = {
             "newyork": {"status": "success",
               "report": "The weather in New York is sunny and 25°C."},
             "london": {"status": "success",
               "report": "It's cloudy in London and  15°C."},
             "tokyo": {"status": "success",
               "report": "Tokyo is experiencing light rain and 18°C."},
           }
           if city_normalized in mock_weather_db:
             return mock_weather_db[city_normalized]
           else:
             return {"status": "error",
               "error_message": f"No weather information for '{city}'."}
         

  5. Click **Create**.




Now, you need to add this tool to the weather agent:

  1. Click the **+** button in the title bar of the weather agent.
  2. Click **Add tool**.
  3. Select the weather tool.



## Create agent instructions

Each agent has a set of [instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction) which define what the agent should do.

When providing instructions that reference an agent, use the syntax `{@AGENT: Agent name}`. For referencing tools, use `{@TOOL: tool_name}`.

Create instructions for each agent:

  1. Click the **+** button in the title bar of the root agent.
  2. Click **Add instructions**.
  3. Enter the following instructions:
         
         You are a helpful weather application.
         Your job is to greet the user and delegate to other sub-agents as needed.
         When greeting the user, describe how you can help them.
         When the user asks for the weather, delegate to {@AGENT: Weather agent}.
         When the user is ending the conversation,
         delegate to {@AGENT: Farewell agent}.
         Handle only weather requests, greetings, and farewells.
         

  4. Click **Create**.

  5. In a similar manner, add the following instructions for the weather agent:
         
         You are a helpful weather agent.
         When the user asks for the weather in a specific city,
         use {@TOOL: get_weather} to find the information.
         If the tool returns an error, inform the user politely.
         If the tool is successful, present the weather report clearly.
         

  6. In a similar manner, add the following instructions for the farewell agent:
         
         You are the Farewell Agent.
         Your ONLY task is to provide a polite goodbye message.
         




## Test the agent

Your agent application is now ready for interactions using the [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator):

  1. In the bottom left corner of the console screen, click the **Preview agent** bar to expand the window if it is not already expanded.
  2. Type "hello", then press enter. The agent responds with a generic greeting.
  3. Type "what is the weather in new york?", then press enter. The agent responds with weather information.
  4. Type "goodbye", then press enter. The agent concludes the conversation.



## Use variables

[Variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable) are used to store and retrieve runtime conversation data. This enables agents to remember information across conversational turns, leading to more contextual interactions. For this agent, you will create a variable that captures the user's name.

To create the variable:

  1. Click the variables button on the right side of the agent builder.
  2. Click **Create a variable** or **+**.
  3. Type "username" as the variable name.
  4. Leave the type as **Text**.
  5. Click **Create**.



Now that you have defined the variable, you need to define a tool that lets the agent update the variable:

  1. Click the tools button on the right side of the agent builder.
  2. Click **+** to create a new tool for the agent application.
  3. Click **Python code**.
  4. Paste the following code:
         
         from typing import Optional
         
         def update_username(username: str) -> Optional[str]:
           """Updates the current user's name"""
           set_variable("username", username)
         

  5. Click **Create**.




Add this tool to the root agent:

  1. Click the **+** button in the title bar of the root agent.
  2. Click **Add tool**.
  3. Select the update_username tool.



Add the following sentence to the root agent instructions, which references the variable using the `{variable_name}` syntax:
    
    
    If provided, the current user is {username},
    and you should address them with this name.
    You can use {@TOOL: update_username} to update the user's name if they provide
    it.
    

You can test the agent again to verify variable usage:

  1. Click **Start new conversation** in the simulator title bar.
  2. Input "Hello, my name is Frank".
  3. Input "How accurate is your information?".



Note that the agent now responds using your name for each response. You can also expand the **Steps** sections of the simulator conversation, where you can verify tool execution among other things.

## Control how to end the session

By default, each of your agents are configured to use the `end_session` [system tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/system), however, you can improve the reliability and control of how to end the session by creating explicit instructions.

Remove the `end_session` tools from the root and weather agents by clicking the **x** next to the tool in each agent. This ensures that only your farewell agent will end the session.

Add the following to your farewell agent's instructions:
    
    
    After providing the goodbye message and confirming the user has no more
    questions, execute the tool {@TOOL: end_session}(reason="success").
    

## Use a callback to enforce a static message at session end

[Callbacks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback) provide a mechanism to hook into a specific agent's execution process using Python code. They allow you to observe, customize, and even control the agent's behavior at specific, predefined points.

There are a variety of callback types you can utilize, where each type of callback is executed at a specific point in the conversational turn.

For this tutorial, append a static message to the model response when ending the session:

  1. Click the title bar of the farewell agent.
  2. Click **Add callback**.
  3. Select **After LLM**.
  4. Enter the following code:
         
         SURVEY_MESSAGE = "Click here to take our post call survey."
         
         def after_model_callback(
             callback_context: CallbackContext,
             llm_response: LlmResponse
         ) -> Optional[LlmResponse]:
           for index, part in enumerate(llm_response.content.parts):
             if part.has_function_call('end_session'):
               return LlmResponse.from_parts(parts=[
                 *llm_response.content.parts,
                 Part.from_text(SURVEY_MESSAGE)
         
             ])
           return None
         

  5. Click **Done**.

  6. Click **Save**.




You can test the agent again to verify session ending behavior:

  1. Click **Start new conversation** in the simulator title bar.
  2. Input "Hello".
  3. Input "Goodbye".



Note that the agent now responds using your appended message.

## Structure instructions

To improve agent behavior, you can structure all of the agent instructions in a free-form XML format that is optimal for model processing. Perform the following for each of your agents:

  1. Open the instructions panel for an agent.
  2. Click the **Structure** button at the top right.
  3. Click **Save**.



## Deploy

Once you have a working agent, you have multiple [deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy) options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
