---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/fetch-memories/
title: Fetch memories \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:07.546675+00:00
---

# Fetch memories  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/fetch-memories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Fetch memories Stay organized with collections  Save and categorize content based on your preferences. 

Memory Bank lets you retrieve stored memories using different operations depending on your needs. You can fetch a single memory, list all memories, or perform scope-based retrieval with similarity search. 

This document explains how to use these fetch operations using the Agent Platform SDK.

If you use the Agent Development Kit (ADK), your agent can automatically orchestrate these calls for you. See [Quickstart with ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/adk-quickstart).

## Before you begin

To complete the steps in this page, you must first complete the steps in [Set up for Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup).

## Fetch operations

You have the following options to fetch generated memories:

  * Get memory: Get the full content of a single memory using the Agent Platform SDK.

  * Retrieve memories: Using the Agent Platform SDK, retrieve memories using scope-based memory retrieval. Retrieve memories using similarity search or all memories within the scope.

  * List memories: List memories using the Agent Platform SDK.




### Get memory

Use `GetMemories` to get the full content of a single memory:
    
    
    memory = client.memory_banks.memories.get(
        name="MEMORY_NAME")
    

Replace the following:

  * `MEMORY_NAME`: A fully-qualified memory name in the format "projects/.../locations/.../reasoningEngines/.../memories...".



### Fetch memories using scope-based retrieval

You can use `RetrieveMemories` to retrieve memories for a particular scope. Only memories that have the exact same scope (independent of order) as the retrieval request are returned. For example, you can retrieve all memories that are scoped to a particular user by using `{"user_id": "123"}`. If no memories are returned, Memory Bank doesn't have any memories for the provided scope.

A memory's scope is defined when the memory is generated or created and is immutable.

You can use `RetrieveMemories` to perform the following operations for a particular scope:

  * Retrieve memories using similarity search
  * Retrieve all memories



#### Retrieve memories using similarity search

For cases where you have many memories for a particular scope, you can use similarity search to retrieve only the most similar memories by providing similarity search parameters. Memory Bank only considers memories that have exactly the same scope as the request when performing similarity search. Similarity search compares the embedding vectors between memories' facts and the request's search query.

Returned memories are sorted from most similar (shortest Euclidean distance) to least similar (greatest Euclidean distance):
    
    
    results = client.memory_banks.memories.retrieve(
        name=memory_bank.name,
        scope=SCOPE,
        similarity_search_params={
            "search_query": "QUERY",
            # Optional. Defaults to 3.
            "top_k": 3
        }
    )
    # RetrieveMemories returns a pager. You can use `page` to retrieve memories.
    
    results.page
    
    """
    Returns:
    
    [
        RetrieveMemoriesResponseRetrievedMemory(
          memory=Memory(
            name="projects/.../locations/.../reasoningEngines/.../memories/...",
            ...
            fact="This is a fact."
          },
          distance=0.5
        ),
        RetrieveMemoriesResponseRetrievedMemory(
          memory=Memory(
            name="projects/.../locations/.../reasoningEngines/.../memories/...",
            ...
            fact="This is another fact."
          },
          distance=0.7
        ),
    ]
    """
    

Replace the following:

  * `QUERY`: The query for which to perform similarity search. For example, you can use the last user turn of the conversation as the query.

  * `SCOPE`: A dictionary, representing the scope for the similarity search. For example, `{"user_id": "123"}`. Only memories with the same scope as the request are considered.




#### Retrieve all memories

If no similarity search parameters are provided, `RetrieveMemories` returns all memories that have the provided scope, regardless of their similarity with the current conversation.

**Warning:** Retrieving all memories without similarity search can return multiple pages. Calling `list()` on a `RetrieveMemories` response triggers automatic pagination across all pages. For large collections, use `response.page` directly to fetch items one page at a time and prevent unexpected calls.
    
    
    results = client.memory_banks.memories.retrieve(
        name=memory_bank.name,
        scope=SCOPE
    )
    # RetrieveMemories returns a pager. You can use `page` to retrieve up to 100 memories per page.
    
    results.page
    
    """
    Returns:
    
    [
        RetrieveMemoriesResponseRetrievedMemory(
          memory=Memory(
            name="projects/.../locations/.../reasoningEngines/.../memories/...",
            ...
            fact="This is a fact."
          }
        ),
        RetrieveMemoriesResponseRetrievedMemory(
          memory=Memory(
            name="projects/.../locations/.../reasoningEngines/.../memories/...",
            ...
            fact="This is another fact."
          }
        ),
    ]
    """
    

Replace the following:

  * `SCOPE`: A dictionary representing the scope for retrieval. For example, `{"user_id": "123"}`. Only memories with the same scope as the request are returned.



### List memories

**Warning:** Calling `list()` on a `ListMemories` response triggers automatic pagination across all pages. For large collections, use `response.page` directly to fetch items one page at a time and prevent unexpected calls.

Use `ListMemories` to memories from your Memory Bank without scope-based filtering. For scope-based retrieval, use `RetrieveMemories` instead. `ListMemories` is not recommended for low-latency retrieval.
    
    
    pager = client.memory_banks.memories.list(name=memory_bank.name)
    for page in pager:
      print(page)
    

## Filter memories

This section describes how to use filters to restrict which memories are fetched. You can filter on:

  * Metadata using the `filter_groups` attribute for scope-based retrieval.

  * System fields using `filter`. System fields include memories' `topics`, `create_time`, `update_time`, and `fact`.




Both metadata and system field filtering can be used in the same request.

### Filter by metadata

**Note:** Filtering by metadata is only supported for scope-based retrieval and [purging memories](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/api-quickstart#purge-memories).

When creating, updating, or generating memories, you can apply structured metadata to the stored memories:
    
    
    import datetime
    
    from agentplatform import types
    
    metadata = {
        "my_string_key": types.MemoryMetadataValue(string_value="my_string_value"),
        "my_double_key": types.MemoryMetadataValue(double_value=123.456),
        "my_boolean_key": types.MemoryMetadataValue(bool_value=True),
        "my_timestamp_key": types.MemoryMetadataValue(
            timestamp_value=datetime.datetime(
                2027, 1, 1, 12, 30, 00, tzinfo=datetime.timezone.utc
            )
        ),
    }
    
    client.memory_banks.memories.create(
      ...,
      config={"metadata": metadata}
    )
    
    client.memory_banks.memories.update(
      ...,
      config={"metadata": metadata}
    )
    
    client.memory_banks.memories.generate(
      ...,
      config={"metadata": metadata}
    )
    

You can filter on this metadata when retrieving memories using the `filter_groups` attribute. Metadata filters are defined in [disjunctive normal form (DNF)](https://en.wikipedia.org/wiki/Disjunctive_normal_form), which is a logical expression of ORs of ANDs.

For example, the following request will retrieve memories that include the metadata (`{"my_string_key": {"string_value": "my_value"}}` AND `{"my_double_key": {"double": 1.23}}`) OR `{"my_string_key": {"string_value": "other"}}`.

### Dictionary
    
    
    results = client.memory_banks.memories.retrieve(
      ...,
      config={
        # Each element of `filter_groups` is combined using OR logic.
        "filter_groups": [
          {
            # Each element of `filters` is combined using AND logic.
            "filters": [
              {
                "key": "my_string_key",
                "value": {"string_value": "my_value"}
              },
              {
                "key": "my_double_key",
                "value": {"double_value": 1.23}
              }
            ]
          },
          {
            "filters": [
              {
                "key": "my_string_key",
                "value": {"string_value": "other"}
              }
            ]
          }
        ]
      }
    )
    

### Class-based
    
    
    from agentplatform import types
    
    results = client.memory_banks.memories.retrieve(
      ...,
      config=types.RetrieveMemoriesConfig(
        # Each element of `filter_groups` is combined using OR logic.
        filter_groups=[
          types.MemoryConjunctionFilter(
            # Each element of `filters` is combined using AND logic.
            filters=[
              types.MemoryFilter(
                key="my_string_key",
                value=types.MemoryMetadataValue(string_value="my_value")
              ),
              types.MemoryFilter(
                key="my_double_key",
                value=types.MemoryMetadataValue(double_value=1.23)
              )
            ]
          ),
          types.MemoryConjunctionFilter(
            filters=[
              types.MemoryFilter(
                key="my_string_key",
                value=types.MemoryMetadataValue(string_value="other")
              )
            ]
          )
        ]
      )
    )
    
    

### Filter by system fields

You can filter on system fields using the `filter` attribute, which expects a string value using [EBNF](https://google.aip.dev/assets/misc/ebnf-filtering.txt) syntax. System fields include `create_time`, `update_time`, `fact`, and `topics`.

EBNF syntax has the following requirements when constructing a filter string:

  * To combine filters, use `AND` and `OR`.
  * String should use double quotes `"`.
  * Datetime fields (like `create_time`) uses either a double quoted string representing ISO 8601 datetime or a numerical field representing microseconds from unix epoch.



For example, the following filter can be used to fetch memories where the `fact` includes the substring "allergies" and `update_time` was after January 1, 2026.
    
    
    filter_string = 'fact=~".*allergies.*" AND update_time>="2026-01-01T00:00:00Z"'
    
    client.memory_banks.memories.retrieve(
      ...,
      config={"filter": filter_string}
    )
    
    client.memory_banks.memories.list(
      ...,
      config={"filter": filter_string}
    )
    

#### Filter by topics

Generated memories are automatically labeled with the relevant [memory topic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories#memory-topics).

To filter on managed topics, use `topics.managed_memory_topic` as the field name and the expected `ManagedTopicEnum` as the value, like `topics.managed_memory_topic: USER_PREFERENCES`.

To filter on custom topics, use `topics.custom_memory_topic_label` as the field name and the label of the expected topic as the value, like `topics.custom_memory_topic_label: custom-label`.
    
    
    filter_string = "topics.managed_memory_topic: USER_PREFERENCES " + \
    "OR topics.custom_memory_topic_label: custom-label"
    
    client.memory_banks.memories.retrieve(
      ...,
      config={"filter": filter_string}
    )
    
    client.memory_banks.memories.list(
      ...,
      config={"filter": filter_string}
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
