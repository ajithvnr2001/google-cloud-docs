---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/quickstart/
title: Example Store with Gemini quickstart \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:50.246473+00:00
---

# Example Store with Gemini quickstart  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Example Store with Gemini quickstart Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial demonstrates how you can iteratively create few-shot examples and dynamically retrieve them from Example Store to correct the behavior of an LLM. You'll do the following:

  * Create an Example Store instance (`ExampleStore`).

  * Author examples based on the response from Gemini and upload those examples to the Example Store instance.

  * Dynamically retrieve your examples from Example Store to guide the LLM towards the expected behavior.

  * Clean up.




## Before you begin

To complete the steps demonstrated in this tutorial, you must first set up your project and environment.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  8. If you selected a project, ensure that you have the [Agent Platform user](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on the project.



### Authenticate to Agent Platform

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Import libraries

  1. Run the following command to install the Agent Platform SDK for Example Store.
         
         pip install --upgrade google-cloud-aiplatform>=1.87.0

  2. Use the following code sample to import and initialize the SDK for Example Store.
         
         import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
         from vertexai.preview import example_stores
         
         [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
           project="PROJECT_ID",
           location="LOCATION"
         )
         

Replace the following:

     * PROJECT_ID: Your project ID.

     * LOCATION: Your region. Only `us-central1` is supported.




## Create an Example Store instance

Use the following code sample to create an Example Store instance that uses the `text-embedding-005` embedding model.
    
    
    example_store = example_stores.ExampleStore.create(
        example_store_config=example_stores.ExampleStoreConfig(
            vertex_embedding_model="text-embedding-005"
        )
    )
    

Note that creating an Example Store takes a few minutes.

For more information about creating or reusing Example Store instances, see [Create an Example Store instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/create-examplestore).

## Upload examples to the Example Store instance

Perform the following steps to author and upload examples to the Example Store instance. You can upload a maximum of five examples per request.

  1. Define the `get_current_weather` function tool. The examples you create in the subsequent steps will guide the model on when to invoke this function and what arguments to pass to it.

For more information about how examples can improve function calling performance and model responses, see [Use examples to improve function calling performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/upload-examples#improve-function-calling). For more information about how to create a function calling application, see [Introduction to function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling).
         
         from google.genai import types as genai_types
         
         get_current_weather_func = genai_types.FunctionDeclaration(
           name="get_current_weather",
           description="Get the current weather in a given location",
           parameters={
             "type": "object",
             "properties": {
               "location": {
                 "type": "string",
                 "description": "The city name of the location for which to get the weather."
               }
             },
           },
         )
         

  2. Send a request to Gemini to generate content using the `get_current_weather` function.

See [Create a client](https://googleapis.github.io/python-genai/#create-a-client) for the Gen AI SDK.
         
         from google import genai
         
         client = genai.Client(
             http_options=genai_types.HttpOptions(api_version="v1"),
             vertexai=True,
             project="PROJECT_ID",
             location="LOCATION")
         
         user_content = genai_types.Content(
           role="user",
           parts=[genai_types.Part(text="What is the weather like in Boston?")],
         )
         response = client.models.generate_content(
           model="gemini-3.5-flash",
           user_content,
           config=genai_types.GenerateContentConfig(
             tools=[
               genai_types.Tool(function_declarations=[get_current_weather_func])]
           )
         )
         

  3. Do any one of the following to create and upload an example.

     * If the response from the LLM shows the expected behavior, use the following code sample to author an example based on the response and upload it to Example Store.
           
           function_response = genai_types.Content(
             parts=[
               genai_types.Part(
                 function_response={
                   "name": "get_current_weather",
                   "response": {
                     "location": "New York, NY", "temperature": 38,
                     "description": "Partly Cloudy",
                     "icon": "partly-cloudy", "humidity": 65,
                     "wind": { "speed": 10, "direction": "NW" }
                   }
                 }
               )
             ]
           )
           final_model_response = genai_types.Content(
             role="model",
             parts=[genai_types.Part(text="The weather in NYC is 38 degrees and partly cloudy.")],
           )
           example = {
             "contents_example": {
               "contents": [user_content.to_json_dict()],
               "expected_contents": [
                 {"content": response.candidates[0].content.to_json_dict()},
                 {"content": function_response.to_json_dict()},
                 {"content": final_model_response.to_json_dict()},
               ],
             },
             "search_key": user_content.parts[0].text,
           }
           example_store.upsert_examples(examples=[example])
           

     * Alternatively, if the response doesn't cover all the functions or outcomes you expected or you see the model struggling with reasoning, use the following code sample to author a response to correct model behavior.
           
           expected_function_call = genai_types.Content(
             parts=[
               genai_types.Part(
                 function_call={
                   "name": "get_current_weather",
                   "args": {"location": "New York, NY"}
                 }
               )
             ]
           )
           function_response = genai_types.Content(
             parts=[
               genai_types.Part(
                 function_response={
                   "name": "get_current_weather",
                   "response": {
                     "location": "New York, NY", "temperature": 38,
                     "description": "Partly Cloudy",
                     "icon": "partly-cloudy", "humidity": 65,
                     "wind": { "speed": 10, "direction": "NW" }
                   }
                 }
               )
             ]
           )
           final_model_response = genai_types.Content(
             role="model",
             parts=[genai_types.Part(text="The weather in NYC is 38 degrees and partly cloudy.")],
           )
           example = {
             "contents_example": {
               "contents": [user_content.to_json_dict()],
               "expected_contents": [
                 {"content": expected_function_call.to_json_dict()},
                 {"content": function_response.to_json_dict()},
                 {"content": final_model_response.to_json_dict()},
               ],
             },
             "search_key": user_content.parts[0].text,
           }
           example_store.upsert_examples(examples=[example])
           

  4. Repeat steps 2 and 3 to author and upload multiple examples, as required. You can upload additional examples if the model shows unexpected behavior or the uploaded examples don't cover all the functions, outcomes, or reasoning that you expect. For more information about when you need to upload additional examples, see [Upload examples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/upload-examples).




## Retrieve and use examples with Gemini

Search for examples based on their similarity with your prompt. You can then include these examples in your prompt to guide the LLM towards the expected behavior.

### Define helper functions to format examples

Use the following code sample to define a `ExampleStorePrompt` class and helper functions that let you search and fetch examples.
    
    
    import abc
    import jinja2
    import json
    
    from google.protobuf import json_format
    # --BOILERPLATE CODE FOR FORMATTING--
    
    EXAMPLES_PREAMBLE = """<EXAMPLES>
    The following are examples of user queries and model responses using the available python libraries.
    
    Begin few-shot
    """
    
    EXAMPLES_POSTAMBLE = """
    End few-shot
    
    Now, try to follow these examples and complete the following conversation:
    </EXAMPLES>
    """
    
    EXAMPLE_PREAMBLE = "EXAMPLE"
    
    TEMPLATE = """
    """
    
    class ExampleStorePrompt:
    
        def __init__(
              self, template = TEMPLATE, example_preamble = EXAMPLE_PREAMBLE,
              examples_preamble = EXAMPLES_PREAMBLE,
              examples_postamble = EXAMPLES_POSTAMBLE):
    
            self.template = jinja2.Template(template)
            self.example_preamble = example_preamble
            self.examples_preamble = examples_preamble
            self.examples_postamble = examples_postamble
    
        @abc.abstractmethod
        def process_function_response(self, function_response):
            return json.dumps(function_response)
    
        @abc.abstractmethod
        def process_function_call(self, function_call):
            args_list = []
            for key, value in function_call.get("args", []).items():
                if isinstance(value, str):
                    # Wrap strings in quotes.
                    value = f'"{value}"'
                if isinstance(value, list):
                    value = ', '.join(
                        f'"{item}"' if isinstance(item, str)
                        else str(item) for item in value)
                    value = f"[{value}]"
                if isinstance(value, dict):
                    value = json.dumps(value)
                args_list.append(f'{key}={value}')
            args = ", ".join(args_list)
            return f"```\n{function_call.get('name')}({args})\n```"
    
        @abc.abstractmethod
        def process_part(self, part):
            if "function_call" in part:
                return self.process_function_call(part["function_call"])
            if "text" in part:
                return part.get("text")
            if "function_response" in part:
                return self.process_function_response(part["function_response"])
    
        @abc.abstractmethod
        def process_content(self, content):
            response = []
            for part in content.get("parts", []):
                response.append(self.process_part(part))
            return [content.get("role"), response]
    
        @abc.abstractmethod
        def example_formatter(self, example: dict):
            response = []
            for content in example.get("contents", []):
                response.append(self.process_content(content))
            for content in example.get("expected_contents", []):
                content = content.get("content", {})
                response.append(self.process_content(content))
            return response
    
        def get_prompt(self, examples: list):
            if not examples:
              return ""
            examples = [self.example_formatter(example) for example in examples]
            return self.template.render(
                examples=examples,
                example_preamble=self.example_preamble,
                examples_preamble=self.examples_preamble,
                examples_postamble=self.examples_postamble
            )
    

### Search for relevant examples

Use the following code sample to search for examples that are relevant to the ongoing conversation with the LLM. You can then use the helper functions to include these examples in your prompts.
    
    
    query = "what's the fastest way to get to disney from lax"
    
    # Search for relevant examples.
    examples = example_store.search_examples(
      {"stored_contents_example_key": query}, top_k=3)
    
    prompt = ExampleStorePrompt().get_prompt(examples.get("results", []))
    
    model_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="How do I get to LAX?",
        config=genai_types.GenerateContentConfig(
          system_instruction=prompt,
          tools=[
            genai_types.Tool(function_declarations=[get_current_weather_func])]
      )
    )
    

## Iteratively improve response quality

To improve the response patterns of Gemini using few-shot examples, repeat the steps in the following sections:

  1. Author and upload examples to the Example Store instance.

  2. Retrieve and use examples with Gemini




## Clean up

To clean up all resources used in this project, you can [delete the Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) you used for the quickstart.

Otherwise, you can delete the individual resources you created in this tutorial, as follows:

  1. Use the following code sample to delete the Example Store instance.
         
         example_store.delete()
         

  2. Delete any locally created files.




## What's next

  * Learn how to [create an Example Store instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/create-examplestore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
