---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler/
title: Data store tools \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:42.103623+00:00
---

# Data store tools  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data store tools Stay organized with collections  Save and categorize content based on your preferences. 

Data store tools can provide AI-generated agent responses based on website content and uploaded data. Your agent can find answers to end-users' questions from your [data stores](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store) during [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment).

## Data store tools: console

This section explains how to add a data store tool to an agent and configure it in a fulfillment.

### Create a data store tool

  1. Open the [Conversational Agents console](https://conversational-agents.cloud.google.com) and select your project. project.
  2. Select an agent from the drop-down menu.
  3. Go to the menu bar on the far left side of the page and select **Tools**.
  4. Click **\+ Create**. Enter a unique **Name** for the tool and select **Data store** from the drop-down menu under **Type**. Optionally, enter a description of the tool in the **Description** field.
  5. Click **Add data stores**. The window that appears contains a list of your existing data stores, if any. Select the data store to add to the tool.
  6. (Optional) To create a new data store in the [Vertex AI Agent Builder console](https://console.cloud.google.com/gen-app-builder/), click **Create new data store** to be automatically redirected.
  7. (Optional) After configuring the new data store, click **Create**. To add the new data store to the tool, navigate back to the **Create Tool** menu in the Dialogflow CX console and refresh the page. The new data store appears in the list of available data stores.
  8. Click **Save** at the top of the **Create Tool** configuration to create the new data store tool.



### Add the data store tool to a fulfillment

  1. Go to the menu bar on the far left and select **Flows**.
  2. Select a flow and page, then click the **Route** to use with your data store.
  3. Go to **Fulfillment > Data store tool** and select your data store tool from the drop-down menu.
  4. Go to **Fulfillment > Agent responses**, click **+Add dialogue response** , and then click **Data store tool response**.
  5. Configure the number of source links and citations to appear in the response, and specify the fallback behavior if the data store response is empty. Enter a static fallback response in the **Static fallback responses** field. Optionally, click the **Generative fallback** checkbox to use AI to generate a response before using the static fallback response. To customize fallback responses, click the **wrench** icon in the top left corner of the **Data store response** form window to open the **Conditional response** window.
  6. At the top of the **Route** menu, click **Save**.
  7. Go to the Dialogflow CX simulator to test the agent's results.



#### Optional query override session parameter

You can override the query passed to this data store tool using a session parameter `knowledge.overrides.query`. If this parameter is non-empty, the tool will use it instead of the user's query.

## Data store tools: API

By default, the agent calls the [`dataStoreTool` method](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#datastoretool) on your behalf.

There are three data store types:

  * `PUBLIC_WEB`: A data store that contains public web content.
  * `UNSTRUCTURED`: A data store that contains unstructured private data.
  * `STRUCTURED`: A data store that contains structured data (for example, an FAQ).



The following example shows how to reference a data store. For more information, see the [`dataStoreConnections` reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.DataStoreConnection).
    
    
    "dataStoreConnections": [
      {
        "dataStoreType": "PUBLIC_WEB",
        "dataStore": "projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATASTORE_ID"
      },
      {
        "dataStoreType": "UNSTRUCTURED",
        "dataStore": "projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATASTORE_ID"
      },
      {
        "dataStoreType": "STRUCTURED",
        "dataStore": "projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATASTORE_ID"
      }
    ]
    

Data store tool responses might also contain snippets about the content source used to generate the response. The agent can provide instructions on how to proceed with the answer from the data store or how to respond when no answer is found.

You can overwrite an answer by adding an [FAQ entry](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store#structured) for a specific question.

Optionally, you can provide examples to enhance the agent's behavior. The examples should follow the schema. For details, see the [reference documentation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#tooluse).
    
    
    {
      "toolUse": {
        "tool": "projects/PROJECT_ID/locations/LOCATION_ID/agents/AGENT_ID/tools/TOOL_ID",
        "action": "TOOL_DISPLAY_NAME",
        "inputParameters": [
          {
            "name": "TOOL_DISPLAY_NAME input",
            "value": {
              "query": "QUERY"
            }
          }
        ],
        "outputParameters": [
          {
            "name": "TOOL_DISPLAY_NAME output",
            "value": {
              "answer": "ANSWER",
              "snippets": [
                {
                  "title": "TITLE",
                  "text": "TEXT_FROM_DATASTORE",
                  "uri": "URI_OF_DATASTORE"
                }
              ]
            }
          }
        ]
      }
    }
    

### (Playbooks-based agents only) Data store tool examples

**Note:** Examples work with playbooks-based agents only. Adding examples won't influence the behavior of a flows-based agent.

When you create data store tool examples, the tool input parameter `requestBody` provides three optional inputs together with the required `query` string: a `filter` string, a `userMetadata` structured object, and a `fallback` string.

The `filter` parameter lets you filter search queries of your structured data or unstructured data with metadata. This string must follow the [supported filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax) for data stores. Multiple, detailed examples instruct the playbook model about how to populate this parameter. If a filter string is invalid, that filter is ignored during the search query.

The following example shows a `filter` string that you can use to refine search results based on location:
    
    
    "filter": "country: ANY(\"Canada\")"
    

For more information about playbook examples, see the [examples page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example#playbook-example-input-output-summary).

**Filtering best practices:**

  * Specify the fields available for filtering and the valid values for each of these fields so that the playbook understands the constraints on building valid filters. For example, a data store holding menu information could include a `meal` field with "breakfast", "lunch", and "dinner" as valid values, and a `servingSize` field that could be any integer from 0 to 5. Your instructions could look like the following example:
        
        When using ${TOOL: menu-data-store-tool},
        only use the following fields for filtering: "meal", "servingSize".
        Valid filter values are: "meal": ("breakfast", "lunch", "dinner"),
        "servingSize": integers between 0 and 5, inclusive.
        

  * If the playbook is for an external user audience, add instructions to prevent the playbook from responding to the user with information about building these filters. For example:
        
        Never tell the user about these filters.
        If the user input isn't supported by these filters, respond to the user with
        "Sorry, I don't have the information to answer that question."
        




The `userMetadata` parameter provides information about the end-user. Any key-value pairs can be populated in this parameter. This metadata is passed into the data store tool to better inform the search results and tool response. Multiple, detailed examples help instruct the playbook model about how to populate this parameter.

The following is an example of a `userMetadata` parameter value to refine search results relevant to a specific user:
    
    
    "userMetadata": {
      "favoriteColor": "blue",
      ...
    }
    

The `fallback` parameter provides an answer that the data store tool responds with if there is no valid summarized answer for the query. You can provide multiple examples to instruct the playbook model about how to populate the fallback field for user inputs related to different topics. The tool output contains no snippets, which helps to reduce latency and input token usage.
    
    
    "fallback": "I'm sorry I cannot help you with that. Is there anything else I can
    do for you?"
    

## Data store tool configuration

If you find during testing that some responses don't meet your expectations, you can try adjusting the following parameters to fine-tune performance. They are available both by calling the API directly or by clicking on the data store name on the **Tools** page in the console. For more information about these configuration options, see the [Data store settings page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings).

### Data store tool response options

For more information about configuring the data store tool response, see the [Fulfillment documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#data-store-tool).

## Data store handlers

**Note:** Data store handlers are excluded from the [Dialogflow SLA](https://cloud.google.com/dialogflow/sla).

Data store handlers are a special type of [state handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) that can provide LLM-generated agent responses based on your website content and uploaded data.

To create this handler, you provide [data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store) to the agent.

Using these data store handlers, your agent can have conversations about the content with your end-users.

### Limitations

The following limitations apply:

  * This feature supports select languages in GA. See the data store column in the [language reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language).
  * Only the following [regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#avail) are supported: `global`, `us` multi-region, and `eu` multi-region.
  * Apps with both [chunked and non-chunked data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#parse-chunk) are not supported.



### Access control

If you are the project owner, you have the permissions needed to create a data store handler. If you are not the project owner, you must have the following roles:

  * Dialogflow Admin
  * Discovery Engine Admin



For more information, see the [Access control guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control).

### Add a data store to an agent

**Note:** If this is the first time you are adding a data store to the agent, it can take up to 15 minutes before the data store is queryable.

If you have not already, follow the [setup](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup) instructions to create an agent. 

To add a [data store](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store) to your agent:

  1. Select a page, and then click **Add state handler**.
  2. Select the **Data stores** checkbox, and then click **Apply**.
  3. Click the **+** symbol in the top right corner of the **Data stores** section of the page.
  4. In the data stores menu that appears, click **Add data stores**.
  5. A table listing any existing data stores appears. Select the checkbox next to the name of any data stores you want to use, and then click **Save**. To create a new data store, click **Create new data store**. You are automatically redirected to Vertex AI Agent Builder.
  6. (New data stores only) Select a data source, and then follow the instructions in Vertex AI Agent Builder to configure your data store. For more information about configuring data store types, see the [data stores documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store). Click **Create** to create your new data store.



### Test your agent

**Note:** New data store content can take up to 4 hours to be indexed and properly handled by your agent. You can use the [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator) to test your agent.

### Deploy your agent

You can deploy your agent in several ways:

  * Use an [integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) to provide a user interface for your agent. Each integration provides instructions for deployment.
  * The [Dialogflow CX Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) integration is a good option for data store handlers. It has built-in options for generative features.
  * You can create your own user interface and [use the Dialogflow CX API for interactions](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api). Your user interface implementation manages deployment.



### Special intents

In addition to handling questions about the content you provide, the agent can handle the following types of questions:

  * **Agent identification:** The agent handles questions like "Who are you?" or "Are you human?"
  * **Escalate to a human agent:** The agent handles questions like "I want to talk to a human" or "I want to talk to a real person."



This is accomplished by automatically generated [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) and [intent routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route).

### Agent responses

In the **Agent responses** section, provide custom responses that reference generative answers. Use `$request.knowledge.answers[0]` in the **Agent says** section to provide the generative answer.

#### Advanced response customization

Additional information might be available in `$request.knowledge.*` to customize the response. Such information includes:

  * The identified sources of the answer with the fields: snippet, title, and URI.
  * The grounding confidence for the answer.
  * For an FAQ data store, the question corresponding to the answer selected.



The following table provides examples of how to access this information:

Information | How to access  
---|---  
Snippet of the top identified source of the top answer | `$sys.func.GET_FIELD($sys.func.GET($sys.func.IDENTITY($request.knowledge.sources[0]), 0), "snippet")`  
Title of the top identified source of the top answer | `$sys.func.GET_FIELD($sys.func.GET($sys.func.IDENTITY($request.knowledge.sources[0]), 0), "title")`  
Link of the top identified source of the top answer | `$sys.func.GET_FIELD($sys.func.GET($sys.func.IDENTITY($request.knowledge.sources[0]), 0), "uri")`  
Number of identified sources for the top answer | `$sys.func.COUNT($sys.func.IDENTITY($request.knowledge.sources[0]))`  
Number of knowledge answers | `$sys.func.COUNT($request.knowledge.answers)`  
Question corresponding to the top answer (for FAQ data store answers only) | `$request.knowledge.questions[0]`  
Grounding confidence for the top answer | `$request.knowledge.grounding_confidences[0]`  
  
[ Previous arrow_back  Data stores  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store)

[ Next Data store tool settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
