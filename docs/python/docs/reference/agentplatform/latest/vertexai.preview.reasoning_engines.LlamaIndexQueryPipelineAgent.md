---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent
title: Class LlamaIndexQueryPipelineAgent (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:30.382686+00:00
---

# Class LlamaIndexQueryPipelineAgent (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LlamaIndexQueryPipelineAgent (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    LlamaIndexQueryPipelineAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[QueryComponent] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], FunctionCallingLLM]] = None,
        retriever_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        retriever_builder: typing.Optional[typing.Callable[[...], QueryComponent]] = None,
        response_synthesizer_kwargs: typing.Optional[
            typing.Mapping[str, typing.Any]
        ] = None,
        response_synthesizer_builder: typing.Optional[
            typing.Callable[[...], QueryComponent]
        ] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], QueryPipeline]] = None,
        enable_tracing: bool = False
    )

A LlamaIndex Query Pipeline Agent.

This agent uses a query pipeline for LLAIndex, including prompt, model, retrieval and summarization steps. More details can be found in <https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/>.

## Methods 

### LlamaIndexQueryPipelineAgent
    
    
    LlamaIndexQueryPipelineAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[QueryComponent] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], FunctionCallingLLM]] = None,
        retriever_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        retriever_builder: typing.Optional[typing.Callable[[...], QueryComponent]] = None,
        response_synthesizer_kwargs: typing.Optional[
            typing.Mapping[str, typing.Any]
        ] = None,
        response_synthesizer_builder: typing.Optional[
            typing.Callable[[...], QueryComponent]
        ] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], QueryPipeline]] = None,
        enable_tracing: bool = False
    )

Initializes the LlamaIndexQueryPipelineAgent.

Under-the-hood, assuming .set_up() is called, this will correspond to
    
    
    # model_builder
    model = model_builder(model_name, project, location, model_kwargs)
    
    # runnable_builder
    runnable = runnable_builder(
        prompt=prompt,
        model=model,
        retriever=retriever_builder(model, retriever_kwargs),
        response_synthesizer=response_synthesizer_builder(
            model, response_synthesizer_kwargs
        ),
        runnable_kwargs=runnable_kwargs,
    )
    

When everything is based on their default values, this corresponds to a query pipeline `Prompt - Model`:
    
    
    # Default Model Builder
    model = google_genai.GoogleGenAI(
        model=model_name,
        vertexai_config={
            "project": initializer.global_config.project,
            "location": initializer.global_config.location,
        },
    )
    
    # Default Prompt Builder
    prompt = prompts.ChatPromptTemplate(
        message_templates=[
            types.ChatMessage(
                role=types.MessageRole.USER,
                content="{input}",
            ),
        ],
    )
    
    # Default Runnable Builder
    runnable = QueryPipeline(
        modules = {
            "prompt": prompt,
            "model": model,
        },
    )
    pipeline.add_link("prompt", "model")
    

When `system_instruction` is specified, the prompt will be updated to include the system instruction.
    
    
    # Updated Prompt Builder
    prompt = prompts.ChatPromptTemplate(
        message_templates=[
            types.ChatMessage(
                role=types.MessageRole.SYSTEM,
                content=system_instruction,
            ),
            types.ChatMessage(
                role=types.MessageRole.USER,
                content="{input}",
            ),
        ],
    )
    

When all inputs are specified, this corresponds to a query pipeline `Prompt - Model - Retriever - Summarizer`:
    
    
    runnable = QueryPipeline(
        modules = {
            "prompt": prompt,
            "model": model,
            "retriever": retriever_builder(retriever_kwargs),
            "response_synthesizer": response_synthesizer_builder(
                response_synthesizer_kwargs
            ),
        },
    )
    pipeline.add_link("prompt", "model")
    pipeline.add_link("model", "retriever")
    pipeline.add_link("model", "response_synthesizer", dest_key="query_str")
    pipeline.add_link("retriever", "response_synthesizer", dest_key="nodes")
    

**Parameters**  
---  
**Name** | **Description**  
`model` |  `str`   
The name of the model (e.g. "gemini-1.0-pro").  
`system_instruction` |  `str`   
Optional. The system instruction to use for the agent.  
`prompt` |  `llama_index.core.base.query_pipeline.query.QUERY_COMPONENT_TYPE`   
Optional. The prompt template for the model.  
`model_kwargs` |  `Mapping[str, Any]`   
Optional. Keyword arguments for the model constructor of the google_genai.GoogleGenAI. An example of a model_kwargs is: 
    
    
    python { # api_key (string): The API key for the GoogleGenAI model. # The API can also be fetched from the GOOGLE_API_KEY # environment variable. If vertexai_config is provided, # the API key is ignored. "api_key": "your_api_key", # temperature (float): Sampling temperature, it controls the # degree of randomness in token selection. If not provided, # the default temperature is 0.1. "temperature": 0.1, # context_window (int): The context window of the model. # If not provided, the default context window is 200000. "context_window": 200000, # max_tokens (int): Token limit determines the maximum # amount of text output from one prompt. If not provided, # the default max_tokens is 256. "max_tokens": 256, # is_function_calling_model (bool): Whether the model is a # function calling model. If not provided, the default # is_function_calling_model is True. "is_function_calling_model": True, }   
  
`model_builder` |  `Callable`   
Optional. Callable that returns a language model.  
`retriever_kwargs` |  `Mapping[str, Any]`   
Optional. Keyword arguments for the retriever constructor.  
`retriever_builder` |  `Callable`   
Optional. Callable that returns a retriever object.  
`response_synthesizer_kwargs` |  `Mapping[str, Any]`   
Optional. Keyword arguments for the response synthesizer constructor.  
`response_synthesizer_builder` |  `Callable`   
Optional. Callable that returns a response_synthesizer object.  
`runnable_kwargs` |  `Mapping[str, Any]`   
Optional. Keyword arguments for the runnable constructor.  
`runnable_builder` |  `Callable`   
Optional. Callable that returns a runnable (query pipeline).  
`enable_tracing` |  `bool`   
Optional. Whether to enable tracing. Defaults to False.  
  
### clone
    
    
    clone() -> (
        vertexai.preview.reasoning_engines.templates.llama_index.LlamaIndexQueryPipelineAgent
    )

Returns a clone of the LlamaIndexQueryPipelineAgent.

### query
    
    
    query(
        input: typing.Union[str, typing.Mapping[str, typing.Any]], **kwargs: typing.Any
    ) -> typing.Union[
        str,
        typing.Dict[str, typing.Any],
        typing.Sequence[typing.Union[str, typing.Dict[str, typing.Any]]],
    ]

Queries the Agent with the given input and config.

**Parameter**  
---  
**Name** | **Description**  
`input` |  `Union[str, Mapping[str, Any]]`   
Required. The input to be passed to the Agent.  
  
### set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

It initializes the model, connects it with the prompt template, retriever and response_synthesizer.

This method should not be called for an object that being passed to the ReasoningEngine service for deployment, as it initializes clients that can not be serialized.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
