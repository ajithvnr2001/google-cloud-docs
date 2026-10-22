---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/memory-bank/
title: Troubleshooting Agent Platform Memory Bank \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:44:06.452575+00:00
---

# Troubleshooting Agent Platform Memory Bank  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/memory-bank/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Troubleshooting Agent Platform Memory Bank Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to resolve common issues when using Agent Platform Memory Bank on Agent Platform. It provides troubleshooting steps for cases where no memories are generated and explains how to verify operation completion. 

## No memories were generated

The memory generation process includes a crucial step: determining if information in the source content is meaningful enough to persist. An empty response indicates the process ran successfully but found no information that met the criteria for being saved. If you were expecting memories to be generated, this guide can help you identify a potential error or misconfiguration.

To troubleshoot why memories are not being generated, follow these steps in order:

### Check if memory generation was triggered

First, confirm that the memory generation process was actually initiated. Memory generation is initiated by invoking `GenerateMemories` (`client.agent_engines.memories.generate(...)`).

If you're using ADK's `VertexAiMemoryBankService`, memory generation is not automatically triggered. You must ensure your agent or application has explicitly called the `add_session_to_memory` method to trigger the process.

The `add_session_to_memory` method takes a [`Session`](https://google.github.io/adk-docs/runtime/#session) object as input and uses the session's events as the data source for memory generation. The method only calls your Memory Bank instance if there are events populated in the session object. If your ADK application or agent is invoking `add_session_to_memory` but memory generation was not triggered, the `Session` object's events may not be populated. This is possible even if you have interacted with the session, especially if you're using `adk.Runner`. To address this issue, fetch the session and its events to the environment where you're invoking `add_session_to_memory`:
    
    
    session = await session_service.get_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session.id
    )
    # Confirm that events are populated.
    print(session.events)
    memory_service.add_session_to_memory(session)
    

### Verify that the memory generation LRO is complete

Memory generation is a [long-running operation (LRO)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations) and can take a few seconds to complete. The exact latency depends on the length of the input conversation and the complexity of the information being processed.

When using the Agent Engine SDK, memory generation is a blocking operation [by default](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories#background-memory-generation). So, `client.generate_memories(...)` blocks your code's execution until the memory generation LRO is complete.

When using ADK's `VertexAiMemoryBankService`, `add_session_to_memory` is a non-blocking operation. It only triggers memory generation and does not wait for the LRO to complete.

### Look for errors in the operation response

The LRO response may an error message similar that indicates that memory generation was unsuccessful. For example:
    
    
    RuntimeError: Failed to generate memory: {'code': 3, 'message': 'Failed to extract memories: Please use a valid role: user, model.'}
    

Common errors include:

  * Resource exhausted errors for Gemini when you use pay-as-you-go. With [dynamic shared quota (DSQ)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo), there are no predefined quota limits on your usage. To help ensure high availability for Memory Bank and to get predictable service levels for your production workloads, see [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/resources/throughput-quota).

  * Invalid source data, like using roles other than `model` and `user` in your `Content`.




### Determine if the conversation was meaningful

If the process was triggered, completed successfully, and produced no errors, it's likely that Memory Bank determined that no information in the source conversation was meaningful enough to persist.

Memory Bank uses ["memory topics"](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories#memory-topics) to identify what information is meaningful. If the content of your conversation doesn't align with any configured topics, no memories are generated.

If you believe information should have been persisted, you can [customize](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup#customization-config) your Memory Bank instance's configuration to better align with your expectations.

[Configuring memory topics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup#configure-memory-topics) lets you define what information should be persisted. [Configuring few-shot examples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/setup#configure-few-shots) helps your Memory Bank instance adapt to your expectations by teaching it the nuances in what information should be persisted and with what phrasing. You can think of customizing your Memory Bank in two steps: Telling and Showing. Memory Topics _tell_ Memory Bank what information to persist. Few-shots _show_ Memory Bank what kind of information should result in a specific memory, helping it learn the patterns, nuance, and phrasing that you expect it to understand.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
