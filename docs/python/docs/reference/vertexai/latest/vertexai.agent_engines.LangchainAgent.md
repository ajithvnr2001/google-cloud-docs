---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.agent_engines.LangchainAgent
title: Class LangchainAgent (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:21.149123+00:00
---

# Class LangchainAgent (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.agent_engines.LangchainAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LangchainAgent (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
    LangchainAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[RunnableSerializable] = None,
        tools: typing.Optional[_ToolsType] = None,
        output_parser: typing.Optional[RunnableSerializable] = None,
        chat_history: typing.Optional[GetSessionHistoryCallable] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable] = None,
        runnable_builder: typing.Optional[typing.Callable] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

A Langchain Agent.

See <https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/develop> for details.

## Methods 

### LangchainAgent
    
    
    LangchainAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[RunnableSerializable] = None,
        tools: typing.Optional[_ToolsType] = None,
        output_parser: typing.Optional[RunnableSerializable] = None,
        chat_history: typing.Optional[GetSessionHistoryCallable] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable] = None,
        runnable_builder: typing.Optional[typing.Callable] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

Initializes the LangchainAgent.

Under-the-hood, assuming .set_up() is called, this will correspond to
    
    
    model = model_builder(model_name=model, model_kwargs=model_kwargs)
    runnable = runnable_builder(
        prompt=prompt,
        model=model,
        tools=tools,
        output_parser=output_parser,
        chat_history=chat_history,
        agent_executor_kwargs=agent_executor_kwargs,
        runnable_kwargs=runnable_kwargs,
    )
    

When everything is based on their default values, this corresponds to
    
    
    # model_builder
    from langchain_google_vertexai import ChatVertexAI
    llm = ChatVertexAI(model_name=model, **model_kwargs)
    
    # runnable_builder
    from langchain import agents
    from langchain_core.runnables.history import RunnableWithMessageHistory
    llm_with_tools = llm.bind_tools(tools=tools, **model_tool_kwargs)
    agent_executor = agents.AgentExecutor(
        agent=prompt | llm_with_tools | output_parser,
        tools=tools,
        **agent_executor_kwargs,
    )
    runnable = RunnableWithMessageHistory(
        runnable=agent_executor,
        get_session_history=chat_history,
        **runnable_kwargs,
    )
    

**Parameters**  
---  
**Name** | **Description**  
`model` |  `str`   
Optional. The name of the model (e.g. "gemini-1.0-pro").  
`system_instruction` |  `str`   
Optional. The system instruction to use for the agent. This argument should not be specified if `prompt` is specified.  
`prompt` |  `langchain_core.runnables.RunnableSerializable`   
Optional. The prompt template for the model. Defaults to a ChatPromptTemplate.  
`tools` |  `Sequence[langchain_core.tools.BaseTool, Callable]`   
Optional. The tools for the agent to be able to use. All input callables (e.g. function or class method) will be converted to a langchain.tools.base.StructuredTool. Defaults to None.  
`output_parser` |  `langchain_core.runnables.RunnableSerializable`   
Optional. The output parser for the model. Defaults to an output parser that works with Gemini function-calling.  
`chat_history` |  `langchain_core.runnables.history.GetSessionHistoryCallable`   
Optional. Callable that returns a new BaseChatMessageHistory. Defaults to None, i.e. chat_history is not preserved.  
`model_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of chat_models.ChatVertexAI. An example would be 
    
    
     { # temperature (float): Sampling temperature, it controls the # degree of randomness in token selection. "temperature": 0.28, # max_output_tokens (int): Token limit determines the # maximum amount of text output from one prompt. "max_output_tokens": 1000, # top_p (float): Tokens are selected from most probable to # least, until the sum of their probabilities equals the # top_p value. "top_p": 0.95, # top_k (int): How the model selects tokens for output, the # next token is selected from among the top_k most probable # tokens. "top_k": 40, }   
  
`model_tool_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments when binding tools to the model using `model.bind_tools()`.  
`agent_executor_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of langchain.agents.AgentExecutor. An example would be 
    
    
     { # Whether to return the agent's trajectory of intermediate # steps at the end in addition to the final output. "return_intermediate_steps": False, # The maximum number of steps to take before ending the # execution loop. "max_iterations": 15, # The method to use for early stopping if the agent never # returns AgentFinish. Either 'force' or 'generate'. "early_stopping_method": "force", # How to handle errors raised by the agent's output parser. # Defaults to False, which raises the error. "handle_parsing_errors": False, }   
  
`runnable_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of langchain.runnables.history.RunnableWithMessageHistory if chat_history is specified. If chat_history is None, this will be ignored.  
`model_builder` |  `Callable`   
Optional. Callable that returns a new language model. Defaults to a a callable that returns ChatVertexAI based on `model`, `model_kwargs` and the parameters in `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai)`.  
`runnable_builder` |  `Callable`   
Optional. Callable that returns a new runnable. This can be used for customizing the orchestration logic of the Agent based on the model returned by `model_builder` and the rest of the input arguments.  
`enable_tracing` |  `bool`   
Optional. Whether to enable tracing in Cloud Trace. Defaults to False.  
`instrumentor_builder` |  `Callable[..., Any]`   
Optional. Callable that returns a new instrumentor. This can be used for customizing the instrumentation logic of the Agent. If not provided, a default instrumentor builder will be used. This parameter is ignored if `enable_tracing` is False.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If both `prompt` and `system_instruction` are specified.  
`TypeError` | If there is an invalid tool (e.g. function with an input  
`tha` | did not specify its type).:  
  
### clone
    
    
    clone() -> vertexai.agent_engines.templates.langchain.LangchainAgent

Returns a clone of the LangchainAgent.

### query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
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
  
### set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

It initializes the model, binds the model with tools, and connects it with the prompt template and output parser.

This method should not be called for an object being passed to the service for deployment, as it might initialize clients that can not be serialized.

### stream_query
    
    
    stream_query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
