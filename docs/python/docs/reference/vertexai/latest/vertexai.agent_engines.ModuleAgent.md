---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.agent_engines.ModuleAgent
title: Class ModuleAgent (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:22.390145+00:00
---

# Class ModuleAgent (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.agent_engines.ModuleAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModuleAgent (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
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

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
