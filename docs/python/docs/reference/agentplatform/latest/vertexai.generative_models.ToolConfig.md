---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.generative_models.ToolConfig
title: Class ToolConfig (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:16.009244+00:00
---

# Class ToolConfig (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.generative_models.ToolConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ToolConfig (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ToolConfig(
        function_calling_config: vertexai.generative_models._generative_models.ToolConfig.FunctionCallingConfig,
    )

Config shared for all tools provided in the request.

Usage: Create ToolConfig
    
    
    ```
    tool_config = ToolConfig(
        function_calling_config=ToolConfig.FunctionCallingConfig(
            mode=ToolConfig.FunctionCallingConfig.Mode.ANY,
            allowed_function_names=["get_current_weather_func"],
    ))
    ```
    
    Use ToolConfig in `GenerativeModel.generate_content`:
    
    ```
    model = GenerativeModel("gemini-pro")
    print(model.generate_content(
        "What is the weather like in Boston?",
        # You can specify tools when creating a model to avoid having to send them with every request.
        tools=[weather_tool],
        tool_config=tool_config,
    ))
    ```
    
    Use ToolConfig in chat:
    
    ```
    model = GenerativeModel(
        "gemini-pro",
        # You can specify tools when creating a model to avoid having to send them with every request.
        tools=[weather_tool],
        tool_config=tool_config,
    )
    chat = model.start_chat()
    print(chat.send_message("What is the weather like in Boston?"))
    print(chat.send_message(
        Part.from_function_response(
            name="get_current_weather",
            response={
                "content": {"weather_there": "super nice"},
            }
        ),
    ))
    ```
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
