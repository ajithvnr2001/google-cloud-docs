---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.A2aAgent
title: Class A2aAgent (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:29.256054+00:00
---

# Class A2aAgent (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.A2aAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class A2aAgent (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    A2aAgent(
        *,
        agent_card: AgentCard,
        task_store_builder: typing.Callable[[...], TaskStore] = None,
        task_store_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_builder: typing.Optional[
            typing.Callable[[...], AgentExecutor]
        ] = None,
        request_handler_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        request_handler_builder: typing.Optional[
            typing.Callable[[...], RequestHandler]
        ] = None,
        extended_agent_card: AgentCard = None
    )

A class to initialize and set up an Agent-to-Agent application.

## Methods 

### A2aAgent
    
    
    A2aAgent(
        *,
        agent_card: AgentCard,
        task_store_builder: typing.Callable[[...], TaskStore] = None,
        task_store_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_builder: typing.Optional[
            typing.Callable[[...], AgentExecutor]
        ] = None,
        request_handler_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        request_handler_builder: typing.Optional[
            typing.Callable[[...], RequestHandler]
        ] = None,
        extended_agent_card: AgentCard = None
    )

Initializes the A2A agent.

### clone
    
    
    clone() -> vertexai.preview.reasoning_engines.templates.a2a.A2aAgent

Clones the A2A agent.

### on_message_send_stream
    
    
    on_message_send_stream(
        request: Request, context: ServerCallContext
    ) -> collections.abc.AsyncIterator[str]

Handles A2A streaming requests via SSE.

### on_resubscribe_to_task
    
    
    on_resubscribe_to_task(
        request: Request, context: ServerCallContext
    ) -> collections.abc.AsyncIterator[str]

Handles A2A task resubscription requests via SSE.

### register_operations
    
    
    register_operations() -> typing.Dict[str, typing.List[str]]

Registers the operations of the A2A Agent.

### set_up
    
    
    set_up()

Sets up the A2A application.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
