---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent
title: Class LangchainAgent (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:30.220211+00:00
---

# Class LangchainAgent (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LangchainAgent (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
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
        enable_tracing: bool = False
    )

A Langchain Agent.

See <https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/develop/langchain> for details.

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
        enable_tracing: bool = False
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
Optional. Callable that returns a new language model. Defaults to a a callable that returns ChatVertexAI based on `model`, `model_kwargs` and the parameters in `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai)`.  
`runnable_builder` |  `Callable`   
Optional. Callable that returns a new runnable. This can be used for customizing the orchestration logic of the Agent based on the model returned by `model_builder` and the rest of the input arguments.  
`enable_tracing` |  `bool`   
Optional. Whether to enable tracing in Cloud Trace. Defaults to False.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If both `prompt` and `system_instruction` are specified.  
`TypeError` | If there is an invalid tool (e.g. function with an input  
`tha` | did not specify its type).:  
  
### clone
    
    
    clone() -> vertexai.preview.reasoning_engines.templates.langchain.LangchainAgent

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

This method should not be called for an object that being passed to the ReasoningEngine service for deployment, as it initializes clients that can not be serialized.

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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
