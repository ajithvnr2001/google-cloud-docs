---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/migrate/
title: Migrate from Vertex AI Extensions to Agent Platform \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:57.446399+00:00
---

# Migrate from Vertex AI Extensions to Agent Platform  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/migrate/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)



Send feedback 

#  Migrate from Vertex AI Extensions to Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

With the deprecation of Vertex AI Extensions, existing workflows must be migrated to Gemini Enterprise Agent Platform (Agent Platform). This guide explains the migration paths for the three core extension categories:

  * Code Interpreter extension
  * Google Search extension
  * Custom extensions



## Code Interpreter extension

**Migrate to:** Agent Platform Code Execution Sandbox **Alternative:** Gemini API `CodeExecution` tool

The Code Interpreter extension should be migrated to **Agent Platform Code Execution Sandbox**. This managed service provides a secure, isolated, and stateful sandbox environment that is specifically designed to run untrusted AI-generated code. It is ideal for programmatic execution, financial calculations, and data science workflows.

Alternatively, if you prefer letting the Gemini models automatically write and execute code natively during a generation pass, you can use the built-in `code_execution` tool in the `google-genai` SDK.

### Migration examples

**Vertex AI Extensions:**
    
    
    from vertexai.preview import extensions
    
    extension = extensions.Extension.from_hub("code_interpreter")
    response = extension.execute(
        operation_id="generate_and_execute_code",
        operation_params={"code": "import math\nprint(math.sqrt(15376))"}
    )
    

**Agent Platform Code Execution Sandbox:**

Option 1: Using the Agent Development Kit (ADK)
    
    
    from google.adk.code_executors.agent_engine_sandbox_code_executor import (
        AgentEngineSandboxCodeExecutor,
    )
    from vertexai.preview.reasoning_engines import Agent
    
    root_agent = Agent(
        model="gemini-2.0-flash-001",
        name="agent_engine_code_execution_agent",
        instruction=base_system_instruction()
        + """
    You need to assist the user with their queries by looking at the data and the
    context in the conversation. Your final answer should summarize the code and
    code execution relevant to the user query.
    
    Include all pieces of data required to answer the question, such as a table
    from code execution results. If the query can be answered directly without
    writing code, generate the textual response directly. Take care not to manually
    run commands like `pip install`. When plotting trends, sort data by the x-axis.
    """,
        code_executor=AgentEngineSandboxCodeExecutor(
            sandbox_resource_name=None,
            agent_engine_resource_name=None,
        ),
    )
    

Option 2: Using the GenAI Client SDK
    
    
    from google import genai
    
    # Initialize Gemini model
    model = genai.Client().models
    
    # Ask Gemini to generate code for a calculation
    prompt = """
    Write Python code to calculate the mean and standard deviation of these numbers:
    [23, 45, 67, 89, 12, 34, 56]
    
    Return only the Python code, no explanations.
    """
    
    response = model.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    generated_code = response.text.replace("```python", "").replace("```", "").strip()
    
    
    # Execute the generated code in Agent Engine Sandbox using new pattern
    exec_response = client.agent_engines.sandboxes.execute_code(
        name=sandbox_resource_name,
        input_data={"code": generated_code},
    )
    
    # Parse response with new file handling logic
    for output in exec_response.outputs:
        if output.mime_type == "application/json" and output.metadata is None:
            result = json.loads(output.data.decode("utf-8"))
            if result.get("msg_out"):
                print(result.get("msg_out"))
            if result.get("msg_err"):
                print(f"Error occurred: {result.get('msg_err')}")
    

Option 3: Defining as a dynamic manual Tool
    
    
    import json
    import re
    from google.genai.types import FunctionDeclaration, Tool
    
    
    def execute_python_code(code: str) -> str:
        """Execute Python code in a secure sandbox.
    
        Args:
            code: Python code to execute
        Returns:
            The output from code execution
        """
        # Extract code block if wrapped in markdown
        code_match = re.search(r"```python\n(.*?)\n```", code, re.DOTALL)
        code_to_execute = code_match.group(1) if code_match else code
    
        # Execute in sandbox
        response = client.agent_engines.sandboxes.execute_code(
            name=sandbox_resource_name, input_data={"code": code_to_execute}
        )
    
        # Parse response using new pattern
        for output in response.outputs:
            if output.mime_type == "application/json" and output.metadata is None:
                result = json.loads(output.data.decode("utf-8"))
    
                if result.get("msg_err"):
                    return f"Error: {result.get('msg_err')}"
                return result.get("msg_out", "Code executed successfully")
    
        return "Code executed (no output)"
    
    
    # Create a tool from the function
    code_tool = Tool(
        function_declarations=[FunctionDeclaration.from_func(execute_python_code)]
    )
    

## Google Search Extension

**Migrate to:** Grounding with Google Search

Migrate to **Grounding with Google Search**. This capability anchors model responses in trusted search indexes and up-to-date public information, yielding higher factuality rates.

### Migration examples

**Vertex AI Extensions:**
    
    
    from vertexai.preview import extensions
    
    extension = extensions.Extension.from_hub("google_search")
    response = extension.execute(
        operation_id="search",
        operation_params={"query": "What is the next total solar eclipse in the US?"}
    )
    

**Grounding with Google Search by using the Google GenAI SDK:**
    
    
    from google import genai
    from google.genai.types import GenerateContentConfig, GoogleSearch, Tool
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.1-flash",
        contents="When is the next total solar eclipse in the United States?",
        config=GenerateContentConfig(
            tools=[Tool(google_search=GoogleSearch())],
            temperature=0.0,
        ),
    )
    print(response.text)
    

## Custom extensions

**Migrate to:** Function Calling (Tool Use)

Migrate custom extensions that you configured with OpenAPI specifications to **Function Calling**. Function calling lets you to define external platform APIs within your source files and forward their interface abstractions to models.

### Migration examples

**Vertex AI Extensions:**
    
    
    from vertexai.preview import extensions
    
    extension = extensions.Extension.create(
        manifest={
            "name": "my_custom_api",
            "apiSpec": {"openApiYaml": "..."}
        }
    )
    

**Tool Use by using the Google GenAI SDK:**
    
    
    from google import genai
    from google.genai.types import GenerateContentConfig
    
    
    def get_order_status(order_id: str) -> str:
        """Returns the current status of a customer order.
    
        Args:
            order_id: The unique identifier of the order.
        """
        statuses = {"123": "Shipped", "456": "Processing"}
        return statuses.get(order_id, "Order not found")
    
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.0-pro",
        contents="Can you check the status of my order 123?",
        config=GenerateContentConfig(
            tools=[get_order_status],
        ),
    )
    
    print(response.text)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
