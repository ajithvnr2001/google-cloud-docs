---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure/
title: Data store search configuration \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:22.296213+00:00
---

# Data store search configuration  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data store search configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can influence search results retrieved from Dialogflow CX data store tools by configuring boost and filter specifications. This lets you have more personalized and context-aware interactions when your agent uses a data store to find information.

Optionally, you can include **dynamic expressions** to fine-tune your results based on conversation context. For example, your agent has captured information indicating that the end-user owns a "mobile phone". You can configure the data store tool to boost documents related to mobile phones when answering a general query later in the conversation like "How do I check my voicemail?".

You can configure data store search results using the [console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#console_configuration), [API](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#search-configuration-api), or [Dialogflow CX Messenger integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#search-configuration-messenger).

## Search condition inputs

You configure search results by using the [**boost specification (`BoostSpec`)**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#boost-specifications-boost-specs) and [**filter specification (`FilterSpec`)**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#filter-specifications-filter-specs) fields in a [`SearchConfig`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#searchconfig) object. These configurations apply per data store within the tool, letting you control how each connected data store behaves.

You can configure search conditions in one of two ways: by using the [console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#console_configuration) or by sending a [direct API call](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#search-configuration-api).

There are important distinctions between the two:

  * **API call:** You send `BoostSpec` and `FilterSpec` in a `SearchConfig` using a `DetectIntent` API call. You must provide a full [`SearchConfig`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#searchconfig) object in the request. A `SearchConfig` sent by direct API call always overrides a `SearchConfig` sent using the console. Dynamic expressions and parameter references aren't supported.

  * **Console:** The console uses your `BoostSpec` and `FilterSpec` configurations to construct a `SearchConfig` object that it sends with the search request. Optionally, you can include parameter references and [dynamic expressions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure#using-cx-expressions) to tailor results to context data recorded from the conversation. You're only required to provide `ConditionBoostSpec` objects and a list of filter strings to construct `FilterSpecs` rather than a full `SearchConfig` object.




End-user information is provided as JSON in [detectIntentRequest](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#detectintentrequest). There's no expected schema, so you can define the object properties. 

### Boost specifications (Boost specs)

[Boost specs](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#BoostSpec) lets you change search result ranking by applying a boost value to specific documents. You can add multiple boost specifications to a single data store.

You enter each **Boost Spec** as a JSON string that represents a single `ConditionBoostSpec` object.

Key fields:

  * `condition`: (String) An expression that specifies when the boost should apply. This uses the standard [filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax). You can use Dialogflow CX expressions to make the results dynamic, such as `$session.params.YOUR_PARAM_NAME` or `$request.end-user-metadata.YOUR_KEY`.
  * `boost`: (Number) A value between -1.0 and 1.0 that determines the strength of the boost. 
    * A positive value promotes matching documents. A value of `1.0` gives a strong promotion.
    * A negative value demotes matching documents. A value of `-1.0` gives a strong demotion.
    * A value of `0.0` applies no boost and isn't allowed.
  * `boostControlSpec`: Provides more controls for a customized ranking than the basic combination of condition and boost. For more information about configuring this field, see the [reference documentation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#BoostControlSpec).



**Example console input:**

If you configure your agent in the console, provide a list of [`ConditionBoostSpecs`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#conditionboostspec) in the following format:
    
    
    {
      "condition": "uri: ANY(\"http://www.example.com/docs/$session.params.doc_id\")",
      "boost": 0.5
    }
    

**Note:** In this example, documents with a URI matching the value of the `$session.params.doc_id` session parameter are boosted with a strength of `0.5`.

**Example API input:**

If you call the API directly, you must provide `ConditionBoostSpecs` in a full [`SearchConfig`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#searchconfig) object. The following search configuration describes a boost spec:
    
    
    "searchConfig": {
      "boostSpecs": [
        {
          "dataStores": [ "DATASTORE_ID" ],
          "spec": [
            {
              "conditionBoostSpecs": {
                "condition": "CONDITION",
                "boost": "1.0"
              }
            }
          ]
        }
      ]
    }
    

**Note:** `DATASTORE_ID` is the full name of the data store: _projects/your_project_id/locations/your_location/collections/your_collection_name/dataStores/your_datastore_name_ ,   
`CONDITION` must follow the Agent Search's [filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax),   
and the [boost value](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls#boost) must be between `-1.0` and `1.0`.

### Filter Specifications (Filter specs)

Filter specifications restrict search results only to include documents that match the defined criteria. You can add multiple filter specifications to a single data store.

Each **Filter Spec** must be entered as a string expression. The string must conform to the [standard filter expression syntax](https://google.aip.dev/160). You can use Dialogflow CX expressions within this string to make the results dynamic, such as `$session.params.YOUR_PARAM_NAME` or `$request.end-user-metadata.YOUR_KEY`.

**Example Console Filter Spec string:**

If you configure your agent using the console, you must provide a list of `filter` strings to form a [`FilterSpec`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#FilterSpecs.FIELDS.filter) object.

In this example, the filter only returns documents with `numeric_field` greater than or equal to the value of `$session.params.min_value` and where `stock_availability` is `"IN_STOCK"`:
    
    
    "numeric_field >= $session.params.min_value AND stock_availability: ANY(\"IN_STOCK\")"
    

**Example API filter configuration:**

If you call the API directly, you must provide `filter` strings in a full `SearchConfig` object:
    
    
    "searchConfig": {
      "filterSpecs": [
        {
          "dataStores": [ "DATASTORE_ID" ],
          "filter": "CONDITION"
        }
      ]
    }
    

**Note:** `DATASTORE_ID` is the full name of the data store: _projects/your_project_id/locations/your_location/collections/your_collection_name/dataStores/your_datastore_name_ ,   
and `CONDITION` must follow the Agent Search's [filter expression syntax](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax).

## Dialogflow CX dynamic expressions

**Note:** Dynamic expressions are available for [data store tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#data-store-console) only. They aren't available for [data store handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#data-store-handler).

Both `BoostSpec` conditions and `FilterSpec` strings can incorporate Dialogflow CX expressions to make them dynamic. This lets you tailor search behavior based on context data retrieved from an ongoing conversation. **Dynamic expressions aren't supported in direct API calls and can only be used if you're configuring using the console**.

You can access conversation context data in two ways:

  * **Session parameters:** The values collected during the conversation by using `$session.params.YOUR_PARAMETER_ID`.
  * **End-user metadata:** The metadata about the end-user passed in the `DetectIntentRequest` by using `$request.end-user-metadata.YOUR_KEY`. To make this option available, verify that `end_user_metadata` is included in the `QueryParameters` of your `DetectIntent` calls. For more information, see [endUserMetadata](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#FIELDS.end_user_metadata).



For more information about available system functions and expression syntax, see the [conditions and system functions reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions).

## Search conditions applied at runtime

When your data store tool executes a search:

  1. Evaluate the JSON strings that you provided for boost specifications. Each valid JSON string is converted into a `ConditionBoostSpec` object. These are then grouped into a `BoostSpecs` object for the specific data store connection, which is added to the overall `SearchConfig`.
  2. Evaluate the strings that you provided for filter specifications as Dialogflow CX expressions. Each resulting filter string is used to create a `FilterSpecs` object for the data store, which is also added to the `SearchConfig`.
  3. Include this dynamically constructed `SearchConfig` in the `QueryParameters` of the search request sent to the data store.



## Configure search conditions

To configure search conditions, make sure that you've completed the following prerequisites:

  * An existing Dialogflow CX agent.
  * A [data store tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler) configured for your agent with one or more data stores enabled.



### Console configuration

  1. Open the [Conversational Agents console](https://conversational-agents.cloud.google.com) and choose a Google Cloud project.
  2. Select an agent from the drop-down menu.
  3. Navigate to the left-hand menu and click **Tools**. Select the data store tool that you want to configure.
  4. In the tool editing page, navigate to the **Data stores** section. Click the **Settings** icon (⚙️) next to the data store you want to modify.
  5. The **Configure Data Store** menu appears. Here you can add Boost Specs and Filter Specs to modify your search results. 
     * For a **Boost Spec** , provide a JSON object that defines a `ConditionBoostSpec`. See Boost Specifications for details.
     * For a **Filter Spec** , provide a string that defines the filter criteria. See Filter Specifications for details.
  6. After adding and configuring your specifications, click **Confirm** at the bottom of the side panel.
  7. Click **Save** on the data store tool edit page to save the changes.



### API configuration

You can provide search configuration data to Dialogflow CX when sending detect intent requests. You must provide this information in every detect intent request because it isn't persisted in the session.

Provide this information in the `queryParams.searchConfig` field in the `Sessions.detectIntent` method.

Go to the Session API reference

**Select a protocol and version for the Session reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions) |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions)  
RPC |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions) |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Sessions)  
C++ |  [SessionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionsClient.html) |  Not available   
C# |  [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) |  Not available   
Go |  [SessionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient) |  Not available   
Java |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionsClient)  
Node.js |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionsClient.html) |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.sessions.SessionsClient)  
Ruby |  Not available  |  Not available   
  
Close

### Dialogflow CX Messenger configuration

You can provide search configuration data to the Dialogflow CX Messenger integration. For more information, see the [setContext](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#setcontext) method.

To apply a search spec or search config, you must add the following snippet to the Dialogflow CX Messenger code when embedding it into a website:
    
    
    <script>
      document.addEventListener('df-messenger-loaded', () => {
        const dfMessenger = document.querySelector('df-messenger');
        const searchConfig = { ... }
        dfMessenger.setQueryParameters(searchConfig);
      });
    </script>
    

For more information, see the [setQueryParameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#setqueryparameters) method.

## Troubleshooting

The following solutions address some common issues encountered during configuration. Test your configurations thoroughly by simulating conversations that trigger different session parameters and end-user metadata values.

### Invalid expressions

If a Boost Spec condition or a Filter Spec string contains an invalid Dialogflow CX expression (for example, incorrect syntax or reference to a nonexistent parameter), the expression compilation will fail. Errors related to expression compilation are typically returned in the `DetectIntentResponse` within the [diagnostic_info](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult#FIELDS.diagnostic_info) field as `SystemFunctionResults`.

### Invalid `ConditionBoostSpec` JSON

The Conversational Agents console performs some validation on the `ConditionBoostSpec` JSON string when saving it to check whether it's valid JSON and its structure can be mapped to a `ConditionBoostSpec` object. If the JSON is valid but it results in an invalid `SearchConfig` according to the underlying search service (for example, an invalid condition string after parameter substitution), the search service will return an error.

### Runtime substitution errors

If a `ConditionBoostSpec` JSON string is valid and parsable but an error occurs during the runtime substitution of Dialogflow CX expressions within its fields (such as the condition string), these errors will be reported in [diagnostic_info](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult#FIELDS.diagnostic_info) as `SystemFunctionResults`.

### Review the compiled `SearchConfig`

The `SearchConfig` applied when the query is run is available in [search_signals](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult#DataStoreConnectionSignals.FIELDS.search_signals) in the response. Reviewing the `SearchConfig` can provide insight into additional issues not outlined here.

## What's next

  * For more information about the structure of the `SearchConfig` and its components, see the [`search_config` documentation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#searchconfig).
  * For more information about expression syntax, see the [Dialogflow CX conditions and system functions reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions).
  * For more information about filter expression syntax for search, see [Filter and order results](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata).



[ Previous arrow_back  Data store hybrid agents  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/hybrid)

[ Next Flow-based agent basics  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/basics)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
