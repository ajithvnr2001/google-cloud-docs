---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AG2Agent
title: Class AG2Agent (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:01.928679+00:00
---

# Class AG2Agent (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AG2Agent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AG2Agent (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AG2Agent(
        model: str,
        runnable_name: str,
        *,
        api_type: typing.Optional[str] = None,
        llm_config: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        system_instruction: typing.Optional[str] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], ConversableAgent]] = None,
        tools: typing.Optional[typing.Sequence[typing.Callable[[...], typing.Any]]] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

An AG2 Agent.

## Methods 

### AG2Agent
    
    
    AG2Agent(
        model: str,
        runnable_name: str,
        *,
        api_type: typing.Optional[str] = None,
        llm_config: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        system_instruction: typing.Optional[str] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], ConversableAgent]] = None,
        tools: typing.Optional[typing.Sequence[typing.Callable[[...], typing.Any]]] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

Initializes the AG2 Agent.

Under-the-hood, assuming .set_up() is called, this will correspond to
    
    
    # runnable_builder
    runnable = runnable_builder(
        llm_config=llm_config,
        system_message=system_instruction,
        **runnable_kwargs,
    )
    

When everything is based on their default values, this corresponds to
    
    
    # llm_config
    llm_config = {
        "config_list": [{
            "project_id":       initializer.global_config.project,
            "location":         initializer.global_config.location,
            "model":            "gemini-1.0-pro-001",
            "api_type":         "google",
        }]
    }
    
    # runnable_builder
    runnable = ConversableAgent(
        llm_config=llm_config,
        name="Default AG2 Agent"
        system_message="You are a helpful AI Assistant.",
        human_input_mode="NEVER",
    )
    

By default, if `llm_config` is not specified, a default configuration will be created using the provided `model` and `api_type`.

If `runnable_builder` is not specified, a default runnable builder will be used, configured with the `system_instruction`, `runnable_name` and `runnable_kwargs`.

**Parameters**  
---  
**Name** | **Description**  
`model` |  `str`   
Required. The name of the model (e.g. "gemini-1.0-pro"). Used to create a default `llm_config` if one is not provided. This parameter is ignored if `llm_config` is provided.  
`runnable_name` |  `str`   
Required. The name of the runnable. This name is used as the default `runnable_kwargs["name"]` unless `runnable_kwargs` already contains a "name", in which case the provided `runnable_kwargs["name"]` will be used.  
`api_type` |  `str`   
Optional. The API type to use for the language model. Used to create a default `llm_config` if one is not provided. This parameter is ignored if `llm_config` is provided.  
`llm_config` |  `Mapping[str, Any]`   
Optional. Configuration dictionary for the language model. If provided, this configuration will be used directly. Otherwise, a default `llm_config` will be created using `model` and `api_type`. This `llm_config` is used as the default `runnable_kwargs["llm_config"]` unless `runnable_kwargs` already contains a "llm_config", in which case the provided `runnable_kwargs["llm_config"]` will be used.  
`system_instruction` |  `str`   
Optional. The system instruction for the agent. This instruction is used as the default `runnable_kwargs["system_message"]` unless `runnable_kwargs` already contains a "system_message", in which case the provided `runnable_kwargs["system_message"]` will be used.  
`runnable_kwargs` |  `Mapping[str, Any]`   
Optional. Additional keyword arguments for the constructor of the runnable. Details of the kwargs can be found in <https://docs.ag2.ai/docs/api-reference/autogen/ConversableAgent>. `runnable_kwargs` only supports `human_input_mode="NEVER"`. Other `human_input_mode` values will trigger a warning.  
`runnable_builder` |  `Callable[..., "ConversableAgent"]`   
Optional. Callable that returns a new runnable. This can be used for customizing the orchestration logic of the Agent. If not provided, a default runnable builder will be used.  
`tools` |  `Sequence[Callable[..., Any]]`   
Optional. The tools for the agent to be able to use. All input callables (e.g. function or class method) will be converted to a AG2 tool . Defaults to None.  
`enable_tracing` |  `bool`   
Optional. Whether to enable tracing in Cloud Trace. Defaults to False.  
`instrumentor_builder` |  `Callable[..., Any]`   
Optional. Callable that returns a new instrumentor. This can be used for customizing the instrumentation logic of the Agent. If not provided, a default instrumentor builder will be used. This parameter is ignored if `enable_tracing` is False.  
  
### clone
    
    
    clone() -> vertexai.agent_engines.templates.ag2.AG2Agent

Returns a clone of the AG2Agent.

### query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        max_turns: typing.Optional[int] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input.

**Parameters**  
---  
**Name** | **Description**  
`input` |  `Union[str, Mapping[str, Any]]`   
Required. The input to be passed to the Agent.  
`max_turns` |  `int`   
Optional. The maximum number of turns to run the agent for. If not provided, the agent will run indefinitely. If `max_turns` is a `float`, it will be converted to `int` through rounding.  
  
### set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

It initializes the runnable, binds the runnable with tools.

This method should not be called for an object that being passed to the ReasoningEngine service for deployment, as it initializes clients that can not be serialized.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
