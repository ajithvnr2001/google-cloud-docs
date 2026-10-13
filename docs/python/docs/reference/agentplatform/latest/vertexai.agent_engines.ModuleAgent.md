---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.ModuleAgent
title: Class ModuleAgent (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:05.299488+00:00
---

# Class ModuleAgent (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.ModuleAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModuleAgent (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ModuleAgent(
        *,
        module_name: str,
        agent_name: str,
        register_operations: typing.Dict[str, typing.Sequence[str]],
        sys_paths: typing.Optional[typing.Sequence[str]] = None,
        agent_framework: typing.Optional[str] = None
    )

Agent that is defined by a module and an agent name.

This agent is instantiated by importing a module and instantiating an agent from that module. It also allows to register operations that are defined in the agent.

## Methods 

### ModuleAgent
    
    
    ModuleAgent(
        *,
        module_name: str,
        agent_name: str,
        register_operations: typing.Dict[str, typing.Sequence[str]],
        sys_paths: typing.Optional[typing.Sequence[str]] = None,
        agent_framework: typing.Optional[str] = None
    )

Initializes a module-based agent.

**Parameters**  
---  
**Name** | **Description**  
`module_name` |  `str`   
Required. The name of the module to import.  
`agent_name` |  `str`   
Required. The name of the agent in the module to instantiate.  
`register_operations` |  `Dict[str, Sequence[str]]`   
Required. A dictionary of API modes to a list of method names.  
`sys_paths` |  `Sequence[str]`   
Optional. The system paths to search for the module. It should be relative to the directory where the code will be running. I.e. it should correspond to the directory being passed to `extra_packages=...` in the create method. It will be appended to the system path in the sequence being specified here, and only be appended if it is not already in the system path.  
  
### clone
    
    
    clone()

Return a clone of the agent.

### register_operations
    
    
    register_operations(**kwargs) -> typing.Dict[str, typing.Sequence[str]]

Register the user provided operations (modes and methods).

### set_up
    
    
    set_up() -> None

Sets up the agent for execution of queries at runtime.

It runs the code to import the agent from the module, and registers the operations of the agent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
