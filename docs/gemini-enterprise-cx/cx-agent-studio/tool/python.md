---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/python/
title: Python code tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:06.738677+00:00
---

# Python code tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Python code tools Stay organized with collections  Save and categorize content based on your preferences. 

You can provide inline Python code as a tool for your agent, which provides flexibility to extend your agent's capabilities. This code can accept inputs provided by the agent, and return a result used by the agent in the conversation. You can implement any custom logic, connect to proprietary APIs or databases, and ensure deterministic outcomes for tasks that require precision.

## Name and description

When creating the tool, the name of the tool and the name of the main function to be called should be the same name in snake case.

Docstrings are a critical part of defining a Python tool. The function's docstring is used as the tool description, which is provided to agents that make use of the tool. You should think of docstrings as an extension of prompting. A clear, descriptive, and well-structured docstring directly influences how well the model understands what your tool does, when to use it, and what arguments to provide. This is the key to achieving reliable and accurate tool selection.

## Environment

In your Python tool code, you have access to certain classes and functions that help you write the code. For more information, see the [Python runtime reference](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python).

For example, the `context` object of type [ToolContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python#class-toolcontext) is a globally available variable that provides a snapshot of the current conversation state. You don't need to import it or define it as a parameter; you can access it directly. It contains valuable information for executing complex logic.

Here is a breakdown of the available keys in the context object:

  * `function_call_id`: A unique ID for the specific tool call being executed.
  * `user_content`: A dictionary containing the most recent message from the user, including the text and role. This is one of the most commonly used attributes.
  * `state`: A dictionary representing the session state. You can use this to store and retrieve variables that need to persist across multiple turns in a conversation (user profile, shopping cart contents, and so on).
  * `events`: A list of all events in the conversation history up to this point, allowing you to build tools with more complex contextual awareness.
  * `session_id`: The unique identifier for the entire conversation session.
  * `invocation_id`: A unique identifier for the current turn of the conversation.
  * `agent_name`: The name of the agent that is executing the tool.



## Channel and modality specific actions

When implementing Python tools or callbacks, it is often best to have the same behavior for all modalities and channels, but there are cases where channel-specific or modality-specific behavior is desired. You can check the channel or modality for a conversation by using the [_session global variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python#variable-_session).

### Deterministic tool masking using `before_model_callback`

When an agent supports both text and voice, the agent's toolset often contains a mix of:

  * **Chat/Visual tools** (interactive UI widgets like `custom_actions`, `card_builder`, `rich_carousel`)
  * **Telephony tools** (`send_sms_link`, `transfer_call`, `dtmf_input`)



Even though the prompt instructions for a given modality (like voice) may not refer to the chat tools, having those tools present in the model's schema consumes prompt tokens and could cause unintended tool invocations.

The following example uses `before_model_callback` alongside `llm_request.config.hide_tool()` (or `excluded_tools`), the callback checks `_session.get("modality")` and dynamically masks out tools not applicable to the active modality before the model generates its response:
    
    
    def before_model_callback(
        callback_context: CallbackContext, llm_request: LlmRequest
    ) -> None:
      _session = callback_context.variables.get("_session", {})
      modality = _session.get("modality", "TEXT").upper()
    
      if modality == "VOICE":
        # Hide visual UI widgets & chat-only tools from the model on voice calls
        for tool_name in ["custom_actions", "plan_builder", "rich_carousel"]:
          llm_request.config.hide_tool(tool_name)
      else:
        # Hide telephony-specific tools on text chat
        for tool_name in ["send_sms_link", "hang_up_call"]:
          llm_request.config.hide_tool(tool_name)
    

## Python tools calling other tools

When defining Python code tools, you can explicitly call other tools defined in the agent application. For example, if you have an OpenAPI tool called `crm_service_get_cart_information`, you can call that tool with the following code:
    
    
    # Deterministically call another tool from this tool.
    # This syntax for OpenAPI spec tool is:
    # tools.<tool_name>_<endpoint_name>({tool_args})
    res = tools.crm_service_get_cart_information({})
    

## Code samples

The following sections provide samples.

### Get last user input

This sample demonstrates a fundamental capability: accessing the user's most recent message. The tool inspects the `context.user_content` object and extracts the text from the last user turn. This pattern is essential for any tool that needs to perform an action based directly on what the user just said.
    
    
    from typing import Optional
    
    # Docstrings in tools are important because they are directly
    # sent to the model as the description for the tool. You should
    # think of docstrings as an extension of prompting. Clear and
    # descriptive docstrings will yield higher quality tool
    # selection from the model.
    def get_last_user_utterance() -> Optional[str]:
      """
      Retrieves the most recent message sent by the user from the conversation history.
    
      Returns:
        The text of the last user message, or None if no user messages are found.
      """
      # The 'context.user_content' contains the last input data
      # provided by the user.
      # We can filter it to find only the text input from the user.
      user_messages = [
        part.text for part in context.user_content.parts
        if context.user_content.role == "user"
      ]
    
      if user_messages:
        # The most recent message is the first one in the list.
        return user_messages[0]
    
      return None
    

### Get and update variables

Language models cannot directly modify session state. This is intentional, as it ensures that state changes are handled in a controlled and predictable way. State can only be modified through two mechanisms: Python Tools or Callbacks.

This sample shows how a Python tool can manage state. The tool first reads the current `customer_profile` from `context.state`. It then performs its business logic (adding points) and writes the updated profile back into context.state. This new state is then be available to the agent and other tools for the remainder of the session.
    
    
    from pydantic import BaseModel, Field
    from typing import Optional, Dict, Any
    
    # Using Pydantic defines the expected structure of your state variables. This makes your code more reliable and easier to
    # debug.
    class CustomerProfile(BaseModel):
      email: Optional[str] = None
      loyalty_points: int = Field(default=0, ge=0) # Must be >= 0
      plan: str = "Standard"
    
    # Docstrings in tools are important because they are directly
    # sent to the model as the description for the tool. You should
    # think of docstrings as an extension of prompting. Clear and
    # descriptive docstrings will yield higher quality tool
    # selection from the model.
    def update_customer_loyalty_points(points_to_add: int) -> Dict[str, Any]:
      """
      Adds loyalty points to the customer's profile and returns the updated profile.
    
      Args:
        points_to_add: The number of loyalty points to add to the existing total.
    
      Returns:
        A dictionary containing the customer's updated profile information.
      """
      # 1. Get the current profile data from the session state.
      # The .get() method safely returns an empty dict if
      # 'customer_profile' doesn't exist.
      current_profile_data = context.state.get("customer_profile", {})
    
      # 2. Load the data into a Pydantic model for validation and easy access.
      profile = CustomerProfile(**current_profile_data)
    
      # 3. Perform the business logic.
      # Print statements can be used for debugging and will show
      # up in the tracing details.
      profile.loyalty_points += points_to_add
      print(f"Updated loyalty points to: {profile.loyalty_points}")
    
      # 4. Save the updated data back into the session state.
      # .model_dump() converts the Pydantic model back to a
      # dictionary.
      context.state["customer_profile"] = profile.model_dump()
    
      return context.state["customer_profile"]
    

### External network requests

Python tools can make external network requests, which is useful for fetching real-time data or integrating with third-party services that don't have an OpenAPI specification. This provides a flexible alternative to using OpenAPI-based tools.

Key limitations for Python code tools:

  * **No Private network access (PNA)** : Python code tools cannot directly access private IP addresses or resolve private DNS domains, even if Service Directory is configured. If you need to access resources within a private network, you must use a tool type that supports Private network access (such as [OpenAPI](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api) or [MCP](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp) tools) instead.
  * **Public Internet Access** : Python code tools can only access endpoints that are publicly available on the internet.



The sample uses the standard requests library (available in the environment) to call a public API and retrieve a random fact.
    
    
    from typing import Optional
    
    # Docstrings in tools are important because they are directly sent to the model as the
    # description for the tool. You should think of docstrings as an extension of prompting.
    # Clear and descriptive docstrings will yield higher quality tool selection from the model.
    
    def get_random_fact() -> Optional[str]:
      """
      Fetches a random fact from a public API.
    
      Returns:
          A string containing the fact on success, or None if an error occurs.
      """
      # The 'ces_requests' library is inspired by 'requests', a  standard and powerful way in Python
      # to make HTTP network calls to any external API, just like you would with `curl` or a web browser.
      url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    
      try:
          # This example calls a public API that is completely open and requires no authentication
          # (like an API key). Many other APIs for services like weather or e-commerce require you
          # to send credentials, often as an API key in the request headers or parameters.
          res = ces_requests.get(url=url, json=request_body, headers=headers)
    
          # Example POST request
          #res = ces_requests.post(url=url, json=request_body, headers=headers)
    
          # This is a standard practice with 'ces_requests' to check if the call was successful. It will
          # raise an error for statuses like 404 or 500.
          res.raise_for_status()
    
          fact_data = res.json()
          return fact_data.get("text")
    
      except:
          return None
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
