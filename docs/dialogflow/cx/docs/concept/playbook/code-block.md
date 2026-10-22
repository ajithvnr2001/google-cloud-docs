---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block/
title: Code blocks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:10.874699+00:00
---

# Code blocks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Code blocks Stay organized with collections  Save and categorize content based on your preferences. 

When defining a playbook, you can optionally provide _code blocks_ , which are inline Python code that can be used to better control agent behavior. This code is made up of functions with special decorators and whatever utility functions you require.

When writing your code, you can use the [code block system library](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library) to control agent behavior.

## Limitations

The following limitations apply:

  * Code blocks cannot contain any objects that persist data. However, you can use tools to persist data and maintain state.
  * Code blocks cannot make remote calls directly. For example, you cannot use the Python requests library. However, you can utilize tools to make remote calls indirectly.
  * Resource names that are converted to Python names [must be legal Python names](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#naming).
  * Code blocks cannot write session parameters, unless a flow transition takes place.



## Inline Actions

Inline actions behave similar to [tool actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example#tool-use). They have a defined input and output schema, which is determined by the Python function signature, including type annotations and docstring. Similar to tool calls, the LLM is unaware of the code that implements the action.

Sample:
    
    
    @Action
    def is_prime(n: int) -> bool:
      """Returns true if n is prime."""
      if not isinstance(n, int) or n < 2:
        return False
    
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
          return False
    
      return True
    

For this function, the LLM will be provided with information about the action, its input, and its output.

To reference an inline action in your playbook instructions, just reference the action name in backticks and describe how it should be used.

Sample for a `place_order` inline action:
    
    
    Take the customer's order, then call the `place_order` action when the order is ready.
    

To create examples that use inline actions, use the **inline-action** tool type in the **Input & Output** section.

For more information, see the [@Action](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-action) reference documentation.

## Trigger functions

Trigger functions are used to define [conditional actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions) in code.

Trigger functions are declared using decorators. You can use the following trigger function decorators:

Decorator | Decorator parameters | Description  
---|---|---  
[@EventTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-eventtrigger) | `event: str, condition: str`, where condition is optional | Triggered by an event  
[@BeforeModelTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-beforemodeltrigger) | `condition: str`, where condition is optional | Triggered every time before the LLM predicts the next action.  
[@BeforeActionTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-beforeactiontrigger) | `condition: str`, where condition is optional | Triggered every time before the LLM executes an action.  
[@BeforePlaybookTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-beforeplaybooktrigger) | `condition: str`, where condition is optional | Triggered the first time a playbook is started.  
  
For instance, these functions show how to use these decorators and decorator parameters, and also how to use the [respond](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-respond) code block system library function.
    
    
    # No decorator parameter
    @PlaybookStartTrigger
    def my_playbook_conditional_action():
      respond("How can I help?")
    
    # With a condition decorator parameter
    @BeforeActionTrigger('$next-action.name = "search"')
    def my_before_action_conditional_action():
      respond("One moment please")
    
    # Event
    @EventTrigger(event="welcome")
    def my_welcome_event():
      respond("hi")
    
    # Event with a condition:
    @EventTrigger(event="welcome",
                  condition="$sys.func.NOW().hours < 10")
    def my_good_morning_event():
      respond("Good morning ☕")
    

## Referencing flows, playbooks, and tools

In your code block, you can reference specific flows, playbooks, and tools using the [flows](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#variable-flows), [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#variable-playbooks), and [tools](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#variable-tools) global variables.

Each of these objects have members that match the names of the corresponding resources. These names need to be [legal Python names](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#naming).

Sample:
    
    
      add_override(playbooks.troubleshooting, {})
      add_override(flows.billing)
      add_override(tools.weather_api.get_weather, {"location": "San Francisco"})
    

When referencing flows and playbooks in a code block, you must also reference them in the playbook instructions with the following syntax:
    
    
    ${RESOURCE_TYPE: my_resource_name}
    

For example, if your code block contains `flows.myflow` and `playbooks.myplaybook`, your playbook instructions should include:
    
    
    ${FLOW: myflow}
    ${PLAYBOOK: myplaybook}
    

## Action overrides

You can use code blocks to create a queue of actions that will take place before any further actions determined by the LLM, and potentially override them. You create action overrides by using the [add_override](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-add_override) global function.

All queued override actions will execute sequentially, and the action output will be available to the LLM. Once the queue is empty, operation returns to the LLM for action and input selection, unless an override finishes the turn with [respond](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-respond) or another function that completes the turn.

Function arguments:

  * action: The action to take place. For an inline action, use `my_function_name`. For a tool action, use `tools.my_tool_name.my_tool_action`. For a flow action, use `flows.my_flow_name`.
  * inputs: Optional inputs for the action. For example: `{"location": "Omaha"}`.



Samples:
    
    
    # Assuming remote tool named "dmv" with operationId "search_offices"
    # remote tool with only requestBody
    add_override(tools.dmv.search_offices,{"address": "95030"})
    
    # remote tool with only parameters
    add_override(tools.pets.get_pet, {"id": "123"})
    
    # remote tool with requestBody + parameters:
    add_override(tools.pets.create_pet, {"requestBody": {"arg1":"foo"}, "param1": "bar"})
    
    # datastore. Assumes existing datastore tool named "Menu".
    add_override(tools.menu.Menu, {"query": "what is the menu"})
    
    # code block action. Assumes another code block @Action my_action.
    add_override(my_action)
    

## Response overrides

Similar to action overrides, but specifically for agent responses, you can use the [respond](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-respond) global function to force the agent to respond to the user with specific content.

Sample:
    
    
    respond("Hello")
    

## Calling tools

In your code block functions, you can call the tools that are defined for your agent. Unlike when you override a tool action, when you call a tool directly, the results of the tool execution are not available to the LLM.

Samples:
    
    
    # Assumes existing tool named "DMV" with operationId "search_offices"
    # remote tool with only request body.
    offices = tools.dmv.search_offices({"address": "95030"})
    
    # remote tool with parameters and request body
    offices = tools.dmv.search_offices({"requestBody": {"address":"95030"}, "param1":"foo"})
    
    # datastore actions. Assumes existing datastore tool named "Menu".
    data = tools.menu.Menu({"query": "get the menu"})["snippets"]
    

## Match intent

Code blocks can programmatically match an intent for a given flow using the [Flow.match_intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#class-flow-match_intent) function.

Sample:
    
    
    matches = flows.flow1.match_intent(history.last_user_utterance).matches
    if matches and matches[0].intent == "some_intent":
      to_country = matches[0].parameters.get("to_country")
      if to_country:
        respond(f"To confirm, you're going to {to_country}, right?")
    

## Read session parameters

Code blocks can read [parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) that are available at the time of execution.

Sample:
    
    
    state["$session.params.my-param"]
    state["$request.session-id"]
    

## Debugging

You can use the simulator to debug your code block functions. These functions will be shown as actions in the simulator, and they will provide our details as needed.

## Additional control

This guide covers some common uses of the [code block system library](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library). For additional types of control, see the library documentation.

[ Previous arrow_back  Playbook instructions  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction)

[ Next Playbook conditional actions  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
