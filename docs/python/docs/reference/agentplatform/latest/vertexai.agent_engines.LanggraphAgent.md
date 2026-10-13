---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.LanggraphAgent
title: Class LanggraphAgent (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:04.875271+00:00
---

# Class LanggraphAgent (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.LanggraphAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LanggraphAgent (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    LanggraphAgent(
        model: str,
        *,
        tools: typing.Optional[typing.Sequence[_ToolLike]] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], BaseLanguageModel]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None,
        checkpointer_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        checkpointer_builder: typing.Optional[
            typing.Callable[[...], BaseCheckpointSaver]
        ] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

A LangGraph Agent.

## Methods 

### LanggraphAgent
    
    
    LanggraphAgent(
        model: str,
        *,
        tools: typing.Optional[typing.Sequence[_ToolLike]] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], BaseLanguageModel]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None,
        checkpointer_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        checkpointer_builder: typing.Optional[
            typing.Callable[[...], BaseCheckpointSaver]
        ] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

Initializes the LangGraph Agent.

Under-the-hood, assuming .set_up() is called, this will correspond to
    
    
    model = model_builder(model_name=model, model_kwargs=model_kwargs)
    runnable = runnable_builder(
        model=model,
        tools=tools,
        model_tool_kwargs=model_tool_kwargs,
        runnable_kwargs=runnable_kwargs,
    )
    

When everything is based on their default values, this corresponds to
    
    
    # model_builder
    from langchain_google_vertexai import ChatVertexAI
    llm = ChatVertexAI(model_name=model, **model_kwargs)
    
    # runnable_builder
    from langgraph.prebuilt import create_react_agent
    llm_with_tools = llm.bind_tools(tools=tools, **model_tool_kwargs)
    runnable = create_react_agent(
        llm_with_tools,
        tools=tools,
        **runnable_kwargs,
    )
    

By default, no checkpointer is used (i.e. there is no state history). To enable checkpointing, provide a `checkpointer_builder` function that returns a checkpointer instance.

**Example using Spanner:**
    
    
    def checkpointer_builder(instance_id, database_id, project_id, **kwargs):
        from langchain_google_spanner import SpannerCheckpointSaver
    
        checkpointer = SpannerCheckpointSaver(instance_id, database_id, project_id)
        with checkpointer.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS checkpoints")
            cur.execute("DROP TABLE IF EXISTS checkpoint_writes")
        checkpointer.setup()
    
        return checkpointer
    

**Example using an in-memory checkpointer:**
    
    
    def checkpointer_builder(**kwargs):
        from langgraph.checkpoint.memory import MemorySaver
    
        return MemorySaver()
    

The `checkpointer_builder` function will be called with any keyword arguments passed to the agent's constructor. Ensure your `checkpointer_builder` function accepts `**kwargs` to handle these arguments, even if unused.

**Parameters**  
---  
**Name** | **Description**  
`model` |  `str`   
Optional. The name of the model (e.g. "gemini-1.0-pro").  
`tools` |  `Sequence[langchain_core.tools.BaseTool, Callable]`   
Optional. The tools for the agent to be able to use. All input callables (e.g. function or class method) will be converted to a langchain.tools.base.StructuredTool. Defaults to None.  
`model_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of chat_models.ChatVertexAI. An example would be 
    
    
     { # temperature (float): Sampling temperature, it controls the # degree of randomness in token selection. "temperature": 0.28, # max_output_tokens (int): Token limit determines the # maximum amount of text output from one prompt. "max_output_tokens": 1000, # top_p (float): Tokens are selected from most probable to # least, until the sum of their probabilities equals the # top_p value. "top_p": 0.95, # top_k (int): How the model selects tokens for output, the # next token is selected from among the top_k most probable # tokens. "top_k": 40, }   
  
`model_tool_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments when binding tools to the model using `model.bind_tools()`.  
`model_builder` |  `Callable[..., BaseLanguageModel]`   
Optional. Callable that returns a new language model. Defaults to a a callable that returns ChatVertexAI based on `model`, `model_kwargs` and the parameters in `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai)`.  
`runnable_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of langchain.runnables.history.RunnableWithMessageHistory if chat_history is specified. If chat_history is None, this will be ignored.  
`runnable_builder` |  `Callable[..., RunnableSerializable]`   
Optional. Callable that returns a new runnable. This can be used for customizing the orchestration logic of the Agent based on the model returned by `model_builder` and the rest of the input arguments.  
`checkpointer_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of the checkpointer returned by `checkpointer_builder`.  
`checkpointer_builder` |  `Callable[..., "BaseCheckpointSaver"]`   
Optional. Callable that returns a checkpointer. This can be used for defining the checkpointer of the Agent. Defaults to None.  
`enable_tracing` |  `bool`   
Optional. Whether to enable tracing in Cloud Trace. Defaults to False.  
`instrumentor_builder` |  `Callable[..., Any]`   
Optional. Callable that returns a new instrumentor. This can be used for customizing the instrumentation logic of the Agent. If not provided, a default instrumentor builder will be used. This parameter is ignored if `enable_tracing` is False.  
**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If there is an invalid tool (e.g. function with an input  
`tha` | did not specify its type).:  
  
### clone
    
    
    clone() -> vertexai.agent_engines.templates.langgraph.LanggraphAgent

Returns a clone of the LanggraphAgent.

### get_state
    
    
    get_state(
        config: typing.Optional[dict[str, typing.Any]] = None, **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Gets the current state of the Agent.

**Parameter**  
---  
**Name** | **Description**  
`config` |  `Optional[RunnableConfig]`   
Optional. The config for invoking the Agent.  
**Returns**  
---  
**Type** | **Description**  
`Dict[str, Any]` | The current state of the Agent.  
  
### get_state_history
    
    
    get_state_history(
        config: typing.Optional[dict[str, typing.Any]] = None, **kwargs: typing.Any
    ) -> typing.Iterable[typing.Any]

Gets the state history of the Agent.

**Parameter**  
---  
**Name** | **Description**  
`config` |  `Optional[RunnableConfig]`   
Optional. The config for invoking the Agent.  
  
### query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[dict[str, typing.Any]] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input and config.

**Parameters**  
---  
**Name** | **Description**  
`input` |  `Union[str, Mapping[str, Any]]`   
Required. The input to be passed to the Agent.  
`config` |  `langchain_core.runnables.RunnableConfig`   
Optional. The config (if any) to be used for invoking the Agent.  
  
### register_operations
    
    
    register_operations() -> typing.Mapping[str, typing.Sequence[str]]

Registers the operations of the Agent.

This mapping defines how different operation modes (e.g., "", "stream") are implemented by specific methods of the Agent. The "default" mode, represented by the empty string `, is associated with the`query`API, while the "stream" mode is associated with the`stream_query` API.

**Returns**  
---  
**Type** | **Description**  
`Mapping[str, Sequence[str]]` | A mapping of operation modes to a list of method names that implement those operation modes.  
  
### set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

It initializes the model, binds the model with tools, and connects it with the prompt template and output parser.

This method should not be called for an object that being passed to the ReasoningEngine service for deployment, as it initializes clients that can not be serialized.

### stream_query
    
    
    stream_query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[dict[str, typing.Any]] = None,
        **kwargs
    ) -> typing.Iterable[typing.Any]

Stream queries the Agent with the given input and config.

**Parameters**  
---  
**Name** | **Description**  
`input` |  `Union[str, Mapping[str, Any]]`   
Required. The input to be passed to the Agent.  
`config` |  `langchain_core.runnables.RunnableConfig`   
Optional. The config (if any) to be used for invoking the Agent.  
  
### update_state
    
    
    update_state(
        config: typing.Optional[dict[str, typing.Any]] = None, **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Updates the state of the Agent.

**Parameter**  
---  
**Name** | **Description**  
`config` |  `Optional[RunnableConfig]`   
Optional. The config for invoking the Agent.  
**Returns**  
---  
**Type** | **Description**  
`Dict[str, Any]` | The updated state of the Agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
