---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/configure-citations-for-custom-mcp-data-stores/
title: Configure citations for custom MCP data stores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:20.238102+00:00
---

# Configure citations for custom MCP data stores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/configure-citations-for-custom-mcp-data-stores/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure citations for custom MCP data stores Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.**Key Term:** In the Model Context Protocol (MCP) specification, capabilities are called _tools_. In Gemini Enterprise data stores, these tools are referred to as _actions_. The two terms can be used interchangeably.

Citation mappings for custom Model Context Protocol (MCP) data stores let you display source citation chips when Gemini Enterprise answers a question using tools on your custom MCP server. Because each MCP server returns results in its own JSON structure, you can configure the `citation_mappings` action parameter using the Discovery Engine REST API to specify where each tool's response stores the link, title, snippet, and ID for each result.

You can configure `citation_mappings` only by using the `v1` REST API. This parameter isn't available in the Google Cloud console.

## Before you begin

Before you configure citation mappings for a custom MCP data store, make sure you've completed the following prerequisites:

  * Create a custom MCP server data store and enable its actions. For more information, see [Set up your custom MCP server data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).
  * Ensure that you have the [Discovery Engine Editor](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.editor) or [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.
  * Obtain the collection ID (`COLLECTION_ID`) for your custom MCP data store. A custom MCP data store's ID is `COLLECTION_ID_mcp_data`, so you can take the data store ID from the Google Cloud console and remove the `_mcp_data` suffix instead of calling the `collections` API. For more information on how to find the collection ID of your data store, see [Get data store and entity details](https://docs.cloud.google.com/gemini/enterprise/docs/get-datastore-details).



## How citation mappings work

When Gemini Enterprise calls a tool on your custom MCP server to answer a user's question, the answer can display citation chips (small cards that link claims in the answer to their source documents). Citation chips are separate from inline Markdown links that a model might generate in the answer text based on its instructions.

To build a citation chip, Gemini Enterprise extracts up to four fields from each result returned by the tool: a link (`uri`), a title (`title`), a short text excerpt (`snippet`), and a source identifier (`id`). You define where these fields live in each tool's response using the following concepts:

  * **Tool** : a single function exposed by your MCP server, identified by its bare name, such as `search_docs`.
  * **Tool response** : the JSON payload the tool returns for a single call.
  * **Item** : a single result object inside the tool response. Each item becomes one citation.
  * **Role** : the citation field that a JSON Pointer populates: `items`, `uri`, `title`, `snippet`, or `id`.
  * **JSON Pointer** : a path string standardized in [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901) that selects a value from a JSON document. For example, `/results` selects the `results` field, and `/author/name` selects `name` inside `author`.



### Structure of the `citation_mappings` parameter

The `citation_mappings` parameter is a JSON object. Each key is a tool name, and each value is an object that maps citation roles to JSON Pointers.

The `items` pointer locates the list of results from the root of the tool response. The remaining four pointers (`uri`, `title`, `snippet`, and `id`) are evaluated relative to each individual item, not from the root of the tool response. In practice, `uri` and `title` have the greatest effect on what users see, and `uri` is required.

The following table describes each role supported in the mapping object of a tool:

Role | Points to | Read from | Behavior if omitted  
---|---|---|---  
`items` | List of results | Tool response |  List is found automatically using common field names, for example, `results`, `items`, `documents`, or `content`.   
`uri` | Link that the citation chip opens | Each item |  Required. Every covered tool must provide a `uri`, either directly or through the default entry (`""`).   
`title` | Title displayed on the citation chip | Each item | Citation chip displays `Untitled`.  
`snippet` | Short text displayed on the citation chip | Each item |  A snippet is selected automatically from common fields on the item, for example, `snippet`, `text`, `description`, or `summary`.   
`id` | A stable ID for the source | Each item | The `uri` value is used as the ID.  
  
### Example citation mappings

Suppose a tool named `search_docs` returns the following JSON payload:
    
    
    {
      "results": [
        {
          "doc_id": "kb-1042",
          "name": "Expense policy 2026",
          "link": "https://intranet.cymbal.com/kb/1234",
          "summary": "Meals are reimbursed up to 60 USD per day."
        }
      ]
    }
    

The following `citation_mappings` configuration maps the fields from `search_docs` to citation chips:
    
    
    {
      "search_docs": {
        "items": "/results",
        "uri": "/link",
        "title": "/name",
        "snippet": "/summary",
        "id": "/doc_id"
      }
    }
    

In this example, `/results` locates the list of items, and `/link`, `/name`, `/summary`, and `/doc_id` are read from each item in that list. The resulting citation chip displays `Expense policy 2026`, links to `https://intranet.cymbal.com/kb/1234`, and shows the summary as its snippet.

If several tools return results in the same shape, you can define a default entry (`""`) and override specific roles only where needed:
    
    
    {
      "": {
        "items": "/results",
        "uri": "/link",
        "title": "/name"
      },
      "get_doc": {
        "items": ""
      }
    }
    

In this configuration, `get_doc` inherits `uri` (`/link`) and `title` (`/name`) from the default entry, and overrides `items` with `""` because `get_doc` returns a single document object rather than a list under `/results`.

### Tool key rules

The following rules apply to tool keys in `citation_mappings`:

  * **Use bare tool names** : specify the tool name exactly as the MCP server declares it, without a server or connector prefix.
  * **Default entry (`""`)**: the empty key `""` defines a default mapping that applies to every tool on the connector. A named tool entry overrides the default entry one role at a time. For example, a tool entry that sets only `uri` inherits `items`, `title`, `snippet`, and `id` from the default entry.
  * **Unmapped tools** : when no default entry (`""`) is present, any tool without a named entry isn't covered by the mapping.
  * **Maximum entries** : `citation_mappings` supports up to 101 entries (up to 100 named tools plus the `""` default entry).



### JSON Pointer evaluation rules

JSON Pointers in `citation_mappings` follow [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901). Keep the following rules in mind when writing pointers:

  * **Empty pointer (`""`)**: an empty string `""` refers to the entire JSON document or item. For `items`, use `""` when the tool response itself is a list of items or a single result object.
  * **Leading slash (`/`)**: every nonempty pointer must start with `/` and can be up to 512 characters long. For example, `/results` is valid, whereas `results` is invalid.
  * **Array indices** : non-negative integers select zero-based list positions. For example, `/links/0/href` selects the `href` field of the first element in `links`.
  * **Escaped characters** : two characters must be escaped inside field names: write `~1` for `/` and `~0` for `~`. For example, a field literally named `a/b` is written as `/a~1b`.
  * **Exact, case-sensitive matching** : pointer matching is exact and case-sensitive. Except for `snippet`, if a pointer doesn't match a field, Gemini Enterprise doesn't guess another field: 
    * A missed `title` pointer displays `Untitled` on the citation chip.
    * A missed `uri` pointer on an individual item means the item is still used to generate the answer, but no citation link is displayed for that item.
    * A missed `snippet` pointer falls back to selecting a snippet automatically from common fields on the item.
  * **Single-object`items`**: if `items` resolves to a JSON object instead of a list, Gemini Enterprise treats that object as a single result item.
  * **Automatic fallback** : if the mapping finds nothing usable for a call—for example, if the `items` pointer matches nothing or no result item has a `uri`—the mapping steps aside and Gemini Enterprise falls back to its automatic response handling for that response.



#### How MCP response wrappers are handled

How you write the `items` pointer depends on how your MCP server formats its tool responses:

  * **JSON serialized inside a text block** : many MCP servers return JSON as a string inside a text content block (`{"content": [{"type": "text", "text": "..."}]}`). The `text` field must contain a valid serialized JSON string. Gemini Enterprise decodes that JSON string first, so you write pointers against the decoded JSON that the tool returns, not against the outer `content` wrapper. If a tool returns unstructured plain text, such as raw Markdown or free-form strings, JSON Pointers can't evaluate it, and `citation_mappings` doesn't extract citation chips.
  * **Structured content** : if your MCP tool returns structured content, pointers address the top-level MCP result object. To reach a list inside `structuredContent`, include `/structuredContent` in your pointer, such as `/structuredContent/results`. When `items` is `""` and `structuredContent.result` is an object, the item pointers (`uri`, `title`, `snippet`, and `id`) resolve against `structuredContent.result` itself. For example, a single-object tool can use `/url` instead of `/structuredContent/result/url`.



## Set or update citation mappings

To configure `citation_mappings` on a custom MCP data store, call the [`updateDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/reference/rest/v1/projects.locations.collections/updateDataConnector) method in the `v1` API with the `updateMask` query parameter set to `action_config.action_params`.

Before running the update request, keep the following behaviors in mind:

  * **The entire mapping is replaced** : sending `citation_mappings` overwrites every existing tool entry in the mapping. To add or modify a single tool, send the complete `citation_mappings` object with your changes included. If you already have existing tools mapped, follow these steps: 
    1. Run `getDataConnector` (`GET`) and copy only the `citation_mappings` JSON block from `actionParams`.
    2. Add or modify your tool's entry in that copied block.
    3. Send the updated `citation_mappings` block in your `PATCH` request.
  * **Other connector parameters are preserved** : action parameters that you omit from the request, such as OAuth settings, keep their existing values. Include only `citation_mappings` in `actionParams`. Don't copy all `actionParams` fields from a `GET` response into your `PATCH` request: on OAuth connectors, `GET` doesn't return `client_id`, so sending the `GET` output back fails with `Connector params must contain client_id`.
  * **Use the narrow update mask** : specify `updateMask=action_config.action_params`. Although `updateMask=action_config` is also accepted, it rewrites other `actionConfig` fields that aren't included in your request.
  * **Changes apply to new chats** : chats that are already open keep the connector settings that they started with. Start a new chat session to test updated citation mappings.
  * **Mappings belong to a single connector** : if you delete a custom MCP data store and create it again, the recreated data store has no citation mapping, and you must configure `citation_mappings` again.



To set or update `citation_mappings`, run the following command:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=action_config.action_params" \
      -d '{
        "actionConfig": {
          "actionParams": {
            "citation_mappings": {
              "search_docs": {
                "items": "/results",
                "uri": "/link",
                "title": "/name"
              }
            }
          }
        }
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT`: the API endpoint for the location of your data store: 
    * `discoveryengine.googleapis.com` for the `global` location
    * `us-discoveryengine.googleapis.com` for the `us` multi-region
    * `eu-discoveryengine.googleapis.com` for the `eu` multi-region
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the location of your data store (`global`, `us`, or `eu`).
  * `COLLECTION_ID`: the ID of the collection that contains your custom MCP data store.



To confirm that the update worked, see Verify citation mappings.

## View citation mappings

To read the current citation mappings for a custom MCP data store, call the [`getDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections/getDataConnector) method on the data connector resource:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/COLLECTION_ID/dataConnector"
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT`: the API endpoint for the location of your data store: 
    * `discoveryengine.googleapis.com` for the `global` location
    * `us-discoveryengine.googleapis.com` for the `us` multi-region
    * `eu-discoveryengine.googleapis.com` for the `eu` multi-region
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the location of your data store (`global`, `us`, or `eu`).
  * `COLLECTION_ID`: the ID of the collection that contains your custom MCP data store.



In the response, the configured mapping appears under `actionConfig.actionParams.citation_mappings`. When no mappings are configured, including right after sending `"citation_mappings": {}`, the response omits `citation_mappings` from `actionConfig.actionParams` entirely rather than returning `{}`.

## Verify citation mappings

After you set or update citation mappings, check that they work:

  1. Call `getDataConnector` as described in View citation mappings and confirm that your mapping appears under `actionConfig.actionParams.citation_mappings`.
  2. In Gemini Enterprise, start a new chat. Chats that were already open keep the connector settings that they started with.
  3. Ask a question that makes the agent call one of the mapped tools.
  4. In the chat response, check for the tool execution indicator or card, such as under **Show thinking** , to confirm that the agent invoked the mapped tool. If the model answers from its own knowledge without calling the tool, citation chips don't appear.
  5. Confirm that the answer displays citation chips with the expected title, description or snippet and link.



If citation chips don't appear, see Troubleshoot citation mappings.

## Remove citation mappings

To remove all citation mappings from a custom MCP data store, send an empty object (`"citation_mappings": {}`) in `actionConfig.actionParams`:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=action_config.action_params" \
      -d '{
        "actionConfig": {
          "actionParams": {
            "citation_mappings": {}
          }
        }
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT`: the API endpoint for the location of your data store: 
    * `discoveryengine.googleapis.com` for the `global` location
    * `us-discoveryengine.googleapis.com` for the `us` multi-region
    * `eu-discoveryengine.googleapis.com` for the `eu` multi-region
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the location of your data store (`global`, `us`, or `eu`).
  * `COLLECTION_ID`: the ID of the collection that contains your custom MCP data store.



## Troubleshoot citation mappings

If citation mappings are rejected by the API or citation chips don't appear as expected, check the following validation errors and common issues.

### Validation errors

Malformed mappings are rejected with a `400 INVALID_ARGUMENT` error. The error message identifies the tool and role at fault:

Error message (abbreviated) | Cause and resolution  
---|---  
`must be an object mapping each tool name to its citation field pointers` |  `citation_mappings` isn't a JSON object. Ensure that the value of `citation_mappings` is a JSON object (`{...}`).   
`declares N tools, more than the supported maximum of 101` |  The mapping contains too many entries. Reduce the number of entries to at most 100 named tools plus the default entry (`""`).   
`entry for tool "TOOL_NAME" must be an object mapping citation role to JSON Pointer` |  A tool's value isn't a JSON object. Map each tool name to an object containing role-to-pointer key-value pairs.   
`entry for tool "TOOL_NAME" has unknown citation role "ROLE"` |  A role name is misspelled, such as `titel` instead of `title`. Valid roles are `items`, `uri`, `title`, `snippet`, and `id`.   
`role "ROLE" on tool "TOOL_NAME" must be a string JSON Pointer` |  A pointer value isn't a string. Format every JSON Pointer value as a JSON string.   
`exceeds the maximum pointer length of 512 characters` |  A JSON Pointer is too long. Shorten the pointer to 512 characters or fewer.   
`is not a valid RFC 6901 JSON Pointer` |  A nonempty pointer is missing a leading `/`, or contains an invalid `~` escape sequence. Use `~0` for `~` and `~1` for `/`.   
`entry for tool "TOOL_NAME" declares no "uri" role` |  Neither the named tool entry nor the default entry (`""`) specifies a `uri` pointer. Add a `uri` role to the tool entry or the default entry.   
`Data Connector parameters must be one of: ... but got: citation_mapping` |  The parameter name in `actionParams` is misspelled. Use `citation_mappings`.   
**Note:** A default entry (`""`) is exempt from the `uri` requirement when named tool entries are also present, because each named tool entry can supply its own `uri`.

### Common issues

If your mapping saves without errors but citation chips don't appear or show unexpected values, check for the following common mistakes:

  * **Writing item pointers from the root of the response** : after `items` selects the list of results, role pointers (`uri`, `title`, `snippet`, and `id`) are read relative to a single item. Specify `/link`, not `/results/0/link`.
  * **Prefixing the tool name** : don't prefix the tool name with the MCP server name or connector name. Use the bare tool name declared by the MCP server.
  * **Sending only the changed tool in an update** : updating `citation_mappings` replaces the entire mapping object. When modifying one tool's mapping, include all other tool entries that you want to keep.
  * **Testing in an existing chat** : updated mappings apply only to new chats. Start a new chat session after updating `citation_mappings`.
  * **Confusing citation chips with inline links** : Markdown links written into the answer text by the model's instructions are separate from the source citation chips controlled by `citation_mappings`.



## What's next

  * [Set up your custom MCP server data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server)
  * [Override the organization policy for Custom MCP data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores)
  * [Import MCP servers from Agent Registry](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
