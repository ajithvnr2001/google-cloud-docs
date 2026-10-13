---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/sdk-migration/
title: Agent Runtime SDK migration guide \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:39.673042+00:00
---

# Agent Runtime SDK migration guide  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/sdk-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Agent Runtime SDK migration guide Stay organized with collections  Save and categorize content based on your preferences. 

In version 2.0.1 of the Agent Platform SDK, the `agent_engines` module within the SDK was refactored and renamed to `runtimes` under the standalone `agentplatform` package. The page describes the key changes to the module and how to migrate your existing code to the new SDK structure. For general information about Agent Runtime, see [Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime). 

## Key changes

At a high level, service client parameters are initialized on a per-client basis, and the client contains the relevant modules for service interactions. Namely,
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html)
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(project=GCP_PROJECT, location=GCP_REGION)
    [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html).[create](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(...)
    

is replaced by
    
    
    import agentplatform
    # Mandatory for cross-project deployment and for use of the framework-specific templates.
    client = agentplatform.Client(project=GCP_PROJECT, location=GCP_REGION)
    client.runtimes.create(...)
    

The following namespaces in the SDK are in the deprecation phase. Use the equivalent namespaces from the client-based Agent Platform SDK, which has full feature parity with the deprecated modules and packages.

Legacy namespace | Impacted code | Replacement (`agentplatform`)  
---|---|---  
`vertexai.agent_engines` |  Impacted methods:  


  * `vertexai.agent_engines.create`
  * `vertexai.agent_engines.get`
  * `vertexai.agent_engines.list`
  * `vertexai.agent_engines.update`
  * `vertexai.agent_engines.delete`

|  Replacement:  


  * `client.runtimes.create`
  * `client.runtimes.get`
  * `client.runtimes.list`
  * `client.runtimes.update`
  * `client.runtimes.delete`

  
`client.agent_engines` |  Impacted methods:  


  * `client.agent_engines.create_memory`
  * `client.agent_engines.delete_memory`
  * `client.agent_engines.generate_memories`
  * `client.agent_engines.get_memory`
  * `client.agent_engines.list_memories`
  * `client.agent_engines.retrieve_memories`
  * `client.agent_engines.create_session`
  * `client.agent_engines.delete_session`
  * `client.agent_engines.get_session`
  * `client.agent_engines.list_sessions`
  * `client.agent_engines.append_session_event`
  * `client.agent_engines.list_session_events`

|  Replacement:  


  * `client.memory_banks.memories.create`
  * `client.memory_banks.memories.delete`
  * `client.memory_banks.memories.generate`
  * `client.memory_banks.memories.get`
  * `client.memory_banks.memories.list`
  * `client.memory_banks.memories.retrieve`
  * `client.sessions.create`
  * `client.sessions.delete`
  * `client.sessions.get`
  * `client.sessions.list`
  * `client.sessions.events.append`
  * `client.sessions.events.list`

  
  
## Migrate to the client-based design

This section contains code snippets that demonstrate how to migrate your existing Agent Runtime code to the `agentplatform` SDK design. Note: The examples may omit imports, dependencies, and other boilerplate code to improve readability.

### Creating an Agent Runtime instance

###  Before 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html)
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(
      project=PROJECT,
      location=LOCATION,
      staging_bucket=STAGING_BUCKET,
    )
    [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html).[create](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(
        local_agent,
        requirements=REQUIREMENTS,
        extra_packages=EXTRA_PACKAGES,
        # ...
    )
    

###  After 
    
    
    import agentplatform
    client = agentplatform.Client(
      project=PROJECT,
      location=LOCATION,
    )
    client.runtimes.create(
        agent=local_agent,
        config={
            "staging_bucket": STAGING_BUCKET,
            "requirements": REQUIREMENTS,
            "extra_packages": EXTRA_PACKAGES,
            # ...
        },
    )
    

### Updating an Agent Runtime instance

###  Before 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html)
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(
      project=PROJECT,
      location=LOCATION,
      staging_bucket=STAGING_BUCKET,
    )
    [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html).[update](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(
        resource_name,
        agent_engine=local_agent,
        requirements=REQUIREMENTS,
        extra_packages=EXTRA_PACKAGES,
        # ...
    )
    

###  After 
    
    
    import agentplatform
    client = agentplatform.Client(
      project=PROJECT,
      location=LOCATION,
    )
    client.runtimes.update(
        name=resource_name,
        agent=local_agent,
        config={
            "staging_bucket": STAGING_BUCKET,
            "requirements": REQUIREMENTS,
            "extra_packages": EXTRA_PACKAGES,
            # ...
        },
    )
    

### Getting an Agent Runtime instance

###  Before 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html)
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(
      project=PROJECT,
      location=LOCATION,
    )
    agent_engine = [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html).[get](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(resource_name)
    

###  After 
    
    
    import agentplatform
    client = agentplatform.Client(
      project=PROJECT,
      location=LOCATION,
    )
    remote_agent = client.runtimes.get(name=resource_name)
    

### Listing Agent Runtime instances

###  Before 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html)
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(
      project=PROJECT,
      location=LOCATION,
    )
    agent_engine = [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html).[list](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)()
    

###  After 
    
    
    import agentplatform
    client = agentplatform.Client(
      project=PROJECT,
      location=LOCATION,
    )
    runtimes = client.runtimes.list()
    

### Deleting an Agent Runtime instance

###  Before 
    
    
    agent_engine.delete(
        force=True,  # Optional
    )
    

Alternatively,
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html)
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(
      project=PROJECT,
      location=LOCATION,
    )
    agent_engine = [agent_engines](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.agent_engines.html).[delete](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(
        resource_name,  # Required.
        force=True,  # Optional
    )
    

###  After 
    
    
    remote_agent.delete(
        force=True,     # Optional.
    )
    

Alternatively,
    
    
    import agentplatform
    client = agentplatform.Client(
      project=PROJECT,
      location=LOCATION,
    )
    remote_agent = client.runtimes.delete(
        name=resource_name,  # Required.
        force=True,          # Optional.
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


