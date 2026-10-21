---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python/
title: Python runtime reference \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:58:59.965892+00:00
---

# Python runtime reference  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Python runtime reference Stay organized with collections  Save and categorize content based on your preferences. 

You can use Python code in Python [tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool) and in [callbacks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback). This reference describes the Python runtime, import options and classes, global variables, and functions you can use in your code.

## Python environment

Python tools and callbacks run in a secure sandbox environment. This environment is running Python 3.12.

## Imports

Your ability to import modules is limited to the following:

  * [Standard Python 3.12 modules](https://docs.python.org/3.12/py-modindex.html)
  * [Pydantic 2.11.6](https://pypi.org/project/pydantic/)
  * [numpy 2.3.1](https://pypi.org/project/numpy/)
  * [protobuf 5.29.1](https://pypi.org/project/protobuf/)



## Classes

### `AsyncTools`

Alias class for calling tools asynchronously. See `async_tools` global variable for more information.

### `Blob`

Inlined bytes data.

Attributes:

Attribute | Description  
---|---  
`display_name: Optional[str]` | Display name of the `Blob`. Used to provide a label or filename to distinguish blobs.  
`data: Optional[bytes]` | Base64 encoded bytes.  
`raw_data: Optional[bytes]` | Raw decoded bytes.  
`mime_type: Optional[str]` | The IANA standard MIME type of the source data.  
  
Methods:

Method | Description  
---|---  
`transcript() -> Optional[str]` | Returns a cached transcript for the `Blob` data if available. This is only applicable to audio blobs.  
`from_json(data: str) -> Blob` | A class method to create a `Blob` instance from a JSON string, with `mime_type` set to 'application/json'.  
  
Samples:
    
    
    # Create a blob from raw bytes
    blob = Blob(mime_type='text/plain')
    blob.raw_data = b'hello world'
    
    # Create a blob from a JSON string
    Blob.from_json(data='{"key": "value"}')
    

### `CallbackContext`

The session information available during a callback.

Attributes:

Attribute | Description  
---|---  
`user_content: Optional[Content]` | Most recent inputs from the user.  
`invocation_id: str` | Unique identifier for the specific callback invocation, useful for debugging.  
`agent_name: str` | Display name of the agent associated with the current callback.  
`session_id: str` | Unique session identifier of the current session in progress.  
`variables: dict[str, Any]` | Dictionary containing key-value pairs of variables defined either at design-time or injected during runtime. This is the current state of variables at the moment of callback execution.  
`state: dict[str, Any]` | Same as `variables` property.  
`events: list[Event]` | Session events.  
  
Methods:

Method | Description  
---|---  
`get_variable(key: str, default: Any) -> Any` | Gets a variable from the state. If the variable doesn't exist, return default.  
`set_variable(key: str, value: Any) -> None` | Sets a variable in the state.  
`remove_variable(key: str) -> None` | Removes a variable from the state.  
`get_last_user_input() -> list[Part]` | Gets a list of all the parts in the last chunk of user events.  
`get_last_agent_output() -> list[Part]` | Gets a list of all the parts in the last chunk of agent events.  
`parts() -> list[Part]` | A list of all parts recorded in the session history.  
  
### `Content`

Message content from user or agent.

Attributes:

Attribute | Description  
---|---  
`parts: Optional[list[Part]]` | List of parts that constitute a single message. Each part may have a different IANA MIME type.  
`role: Optional[str]` | The role of the author of the content. Either `'user'` or `'agent'`.  
  
Methods:

Method | Description  
---|---  
`is_user() -> bool` | Returns `True` if the role is `'user'`.  
`is_model() -> bool` | Returns `True` if the role is `'model'`.  
  
### `Event`

Representation of an event in the session.

Attributes:

Attribute | Description  
---|---  
`id: str` | Event identifier.  
`invocation_id: str` | Event invocation identifier.  
`author: str` | 'user' or the name of the agent, indicating who attended the event to the session.  
`timestamp: int` | Event timestamp.  
`content: Content` | The content associated with this event.  
`actions: EventActions` | The actions taken by the agent.  
`long_running_tool_ids: set[str]` | Set of identifiers of the long running function calls.  
`partial: bool` | `True` for incomplete chunks from the LLM streaming response.  
`turn_complete: bool` | `True` if the current turn is complete.  
`error_code: str` | Error code.  
`error_message: str` | Error message.  
`interrupted: bool` | `True` if the turn was interrupted.  
`branch: str` | The branch of the event.  
  
The format is like `agent_1.agent_2.agent_3`, where `agent_1` is the parent of `agent_2`, and `agent_2` is the parent of `agent_3`.  
  
Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.  
`grounding_metadata: Any` | The grounding metadata of the event.  
  
Methods:

Method | Description  
---|---  
`is_user() -> bool` | `True` if the event's author is 'user'.  
`is_agent(agent_name: Optional[str] = None) -> bool` | `True` if the event's author is an agent. If `agent_name` is provided, it checks if the author matches that specific agent.  
`has_error() -> bool` | `True` if the event has an associated error code.  
`parts() -> list[Part]` | A convenience method to get the list of `Part` objects from the event's `content`. Returns an empty list if there is no content or parts.  
  
### `EventActions`

Actions that occur for events.

Attributes:

Attribute | Description  
---|---  
`skip_summarization: bool` | If `True`, the model is not called to summarize function response. Only used for `function_response` event.  
`state_delta: dict[str,Any]` | The changes to variables caused by this event.  
`artifact_delta: dict[str,Any]` | The changes to artifacts by this event. The key is the filename, value is the version.  
`transfer_to_agent: str` | If set, the event transfers to the specified agent.  
`escalate: bool` | The agent is escalating to a higher level agent.  
`requested_auth_configs: dict[str,dict[str,Any]]` | Authentication configurations requested by tool responses.  
  
This field is only be set by a tool response event indicating tool request auth credential.  
  
Keys: The function call identifier. Since one function response event could contain multiple function responses that correspond to multiple function calls. Each function call could request different auth configs. This identifier is used to identify the function call.  
  
Values: The requested auth config.  
`end_invocation: bool` | The agent loop is interrupted.  
  
### `ExternalResponse`

Represents a response from outside the Python environment, such as a tool call or HTTP request.

Attributes:

Attribute | Description  
---|---  
`text: str` | The response body as a string.  
`status_code: int` | The HTTP status code.  
`reason: str` | The reason the error is being thrown. Empty if no error.  
`ok: bool` | `True` if `status_code` is less than 400, otherwise `False`.  
  
Methods:

Method | Description  
---|---  
`json() -> Any` | Parses the text attribute JSON and returns the result. If parsing fails, this will throw an error.  
`raise_for_status()` | Raises a `StatusError` if response is not ok (`ok` == `False`).  
  
### `FunctionCall`

Represents a function call.

Attributes:

Attribute | Description  
---|---  
`id: Optional[str]` | The unique identifier of the function call.  
`args: Optional[dict[str,Any]]` | The function parameters and values in JSON object format.  
`name: Optional[str]` | Function name.  
  
### `FunctionDeclaration`

A predicted `FunctionCall` returned from the model that contains a string representing the `FunctionDeclaration` `name` attribute with the parameters and their values.

Attributes:

Attribute | Description  
---|---  
`name: Optional[str]` | Function name.  
  
### `FunctionResponse`

The result of a `FunctionCall` that contains a string representing the `FunctionDeclaration` `name` attribute and a structured JSON object containing any output from the function call. It is used as context to the model.

Attributes:

Attribute | Description  
---|---  
`id: Optional[str]` | Identifier of the corresponding function call.  
`name: Optional[str]` | Function name.  
`response: Optional[dict[str,Any]]` | The function response in JSON object format. Use "output" key to specify function output and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as function output.  
  
### `GenerateContentConfig`

Optional model configuration parameters.

Attributes:

Attribute | Description  
---|---  
`system_instruction: Optional[Content]` | Instructions for the model to steer it towards better performance. For example, "Answer as concisely as possible" or "Don't use technical terms in your response".  
`tools: Optional[list[ToolDeclaration]]` | A list of available tools that the model can execute.  
`excluded_tools: Optional[list[str]]` | A list of tool names that will be ignored by the model. This overrides `tools`.  
  
Methods:

Method | Description  
---|---  
`hide_tool(tool_name: str)` | Adds `tool_name` to the `excluded_tools` list.  
  
### `HttpMethod`

A string enum to represent an HTTP method. The possible values are:

  * `GET`
  * `POST`
  * `PUT`
  * `DELETE`
  * `PATCH`
  * `HEAD`
  * `OPTIONS`



### `LlmRequest`

Data models for representing requests to the LLM.

Attributes:

Attribute | Description  
---|---  
`model: Optional[str]` | Model name  
`contents: List[Content]` | A list of contents sent to the model.  
`config: Optional[GeneralContentConfig]` | Model configuration parameters.  
  
### `LlmResponse`

Data models for representing responses from the LLM.

Attributes:

Attribute | Description  
---|---  
`content: Content` | The first `Content` that the model responds with.  
`partial: Optional[bool]` | Indicates whether the content represents an incomplete model response. Agent will continue the processing after emitting the partial response.  
  
Methods:

Method | Description  
---|---  
`from_parts(parts: list[Part]) -> LlmResponse` | Class method that returns an `LlmResponse` from the model.  
  
Samples:
    
    
    response = LlmResponse.from_parts(
      parts=[
        Part.from_text(text="hello world")
      ]
    )
    

### `Part`

A datatype containing media content. Exactly one field within a `Part` should be set, representing the specific type of content being conveyed. Using multiple fields within the same `Part` instance is considered invalid.

Attributes:

Attribute | Description  
---|---  
`function_call: Optional[FunctionCall]` | A predicted `FunctionCall` returned from the model that contains a string representing the function name and a structured JSON object containing the parameters and their values.  
`function_response: Optional[FunctionResponse]` | The result output of `FunctionCall` that contains a string representing the function name and structured JSON object containing any output from the function call. It is used as context to the model.  
`text: Optional[str]` | Message text.  
`inline_data: Optional[Blob]` | Inlined bytes data.  
  
Methods:

Method | Description  
---|---  
`text_or_transcript() -> Optional[str]` | Returns the text if available, otherwise returns the transcript of the inline data.  
`has_function_call(name) -> bool` | Returns `True` if the part holds a specific function call.  
`has_function_response(name) -> bool` | Returns `True` if the part holds a specific function response.  
`from_text(text: str) -> Part` | Class method that creates a text `Part`.  
`from_function_call(name: str, args: dict[str, Any]) -> Part` | Class method that creates a function call `Part`.  
`from_function_response(name: str, response: dict[str, Any]) -> Part` | Class method that creates a function response `Part`.  
`from_inline_data(data: bytes, mime_type: str) -> Part` | Class method that creates an inline data `Part`.  
`from_json(data: str) -> Part` | Class method that creates a JSON inline data `Part`.  
`from_agent_transfer(agent: str) -> Part` | Class method that creates a `Part` for transferring to another agent.  
`from_end_session(*, reason: str, escalated: bool = False) -> Part` | Class method that creates a `Part` for terminating the session.  
`from_customized_response(*, content: str, disable_barge_in: bool = False, enable_dtmf: bool = False, dtmf_finish_digit = str: '#', dtmf_endpointing_timeout: int = 3) -> Part` | Class method that creates a `Part` for response with customized behavior (for example, disable barege-in, enable DTMF input, etc).  
  
Samples:
    
    
    text_part = ces_public.Part.from_text(text="Hello from the user!")
    
    tool_part = ces_public.Part.from_function_call(
      name="get_weather",
      args={"location": "Mountain View"}
    )
    

### `Requests`

Alias class for making HTTP requests. See ces_requests global variable for more information.

Methods:

  * `get(url, params=None, **kwargs)`
  * `post(url, data=None, json=None, **kwargs)`
  * `put(url, data=None, json=None, **kwargs)`
  * `delete(url, **kwargs)`
  * `patch(url, data=None, json=None, **kwargs)`
  * `head(url, **kwargs)`
  * `options(url, **kwargs)`



### `StatusError`

Used for errors raised with a status code.

Attributes:

Attribute | Description  
---|---  
`status_code: int` | The HTTP status code associated with this error.  
`reason: str` | The reason the error is being thrown.  
  
### `Tool`

Represents a tool with a name and description.

Attributes:

Attribute | Description  
---|---  
`name: str` | The name of the tool.  
`description: str` | A description of what the tool does.  
  
### `ToolContext`

Derived from `CallbackContext`. The session information available when executing a tool.

Attributes:

Attribute | Description  
---|---  
`function_call_id: str` | The function call identifier of the current tool call being executed.  
  
### `Tools`

Alias class for calling tools synchronously. See tools global variable for more information.

### `ToolDeclaration`

A tool schema that can be shown to the model.

Attributes:

Attribute | Description  
---|---  
`function_declarations: Optional[list[FunctionDeclaration]]` | List of function declarations that the tool supports.  
  
## Functions

### `get_variable`

This function retrieves a value from the session state using the provided key. It serves as a shortcut for `context.state.get(key)` or `context.variables.get(key)`.

Sample code:
    
    
    def get_a_value() -> int:
      # Retrieve the value of 'my_key' from the state
      my_value = get_variable('my_key')
      return my_value + 5
    

### `remove_variable`

This function removes a key-value pair from the session state. This is a shortcut for `del context.state[key]`.

Sample code:
    
    
    def remove_a_value() -> None:
      # Delete 'my_key' from the state
      remove_variable('my_key')
    

### `set_variable`

This function sets a value for a given key in the session state. If the key already exists, its value will be updated. It's a shortcut for `context.state[key] = value`.

Sample code:
    
    
    def set_a_value() -> None:
      # Set the value of 'my_key' to 10
      set_variable('my_key', 10)
    

## Global variables

### `_session`

You can access the current channel and modality for a conversation, similar to how it is done in [modular components](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components). Access these values using the predefined variable called `_session`.

Python tool sample (using the global `context` variable):
    
    
    def check_order_status(order_id: str) -> str:
      # Resolve modality and channel from the session state
      session_vars = context.variables.get('_session', {})
      modality = session_vars.get('modality', 'TEXT')
      channel = session_vars.get('channel', 'API')
    
      status = get_raw_order_status(order_id)  # Internal API lookup
    
      if modality == 'VOICE':
        # Keep response concise and remove markdown/links for natural TTS playback
        return "Your order has shipped and is estimated to arrive tomorrow."
      else:
        # Rich text with markdown links for Chat/Web interfaces
        return f"Your order shipped [Track it](https://shipper.com/{order_id})."
    

Callback sample (using `CallbackContext`):
    
    
    def before_agent_callback(callback_context: CallbackContext) -> None:
      session_vars = callback_context.get_variable('_session', {})
      modality = session_vars.get('modality', 'TEXT')
      channel = session_vars.get('channel', 'API')
      callback_context.set_variable('active_modality', modality)
    

### `async_tools`

An instance of `AsyncTools`, which lets you to make asynchronous calls to tools.

Samples:
    
    
    response_future = async_tools.<TOOL_DISPLAY_NAME>(<ARGS_AS_DICT>)
    # ... misc work
    response = response_future() # poll for response
    
    # Check if the tool call was successful
    try:
      response.raise_for_status()
    except StatusError:
      print(f"Request failed with status {response.status_code}")
    
    # Convert the response to json
    data = response.json()
    

### `ces_requests`

An instance of `Requests`. `Requests` allow you to make HTTP calls with similar syntax to the popular Python requests module.

Samples:
    
    
    # Make a GET request
    response = ces_requests.get('https://api.example.com/data')
    
    # Check if the request was successful
    try:
      response.raise_for_status()
    except StatusError:
      print(f"Request failed with status {response.status_code}")
    
    # Convert the response to json
    data = response.json()
    

### `tools`

An instance of `Tools`, which lets you to make synchronous calls to tools.

Samples:
    
    
    response = tools.<TOOL_DISPLAY_NAME>(<ARGS_AS_DICT>)
    
    # Check if the tool call was successful
    try:
      response.raise_for_status()
    except StatusError:
      print(f"Request failed with status {response.status_code}")
    
    # Convert the response to json
    data = response.json()
    

### `context`

In your code, you can access the [ADK context](https://google.github.io/adk-docs/context), which can be used to read and write many types of ADK context data. A global variable called `context` is available to use in your code.

The `context.state` and `context.variables` objects are interchangeable. The `state` object is supported for compatibility with ADK code, but new code should use the `variables` object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
