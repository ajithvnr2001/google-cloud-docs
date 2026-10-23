---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/managing-deployed-agents/
title: Troubleshoot managing deployed agents for Agent Runtime \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:29.842263+00:00
---

# Troubleshoot managing deployed agents for Agent Runtime  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/managing-deployed-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Troubleshoot managing deployed agents for Agent Runtime Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to resolve errors that you might encounter when [managing deployed agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents).

## Error when filtering the list of agents

**Issue** :

You receive an error message similar to the following:
    
    
    InvalidArgument: 400 Provided filter is not valid.
    

**Possible cause** :

Your filter isn't formatted properly.

**Recommended solution** :

Update the formatting of your filter so it's formatted correctly. For example, you might be using the following to filter by display name. This filter isn't formatted correctly because it's missing quotation marks:
    
    
    from vertexai import agent_engines
    
    agent_engines.[list](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(filter=f'display_name={DISPLAY_NAME}')
    

In this case, enclose `{DISPLAY_NAME}` in double-quotation marks:
    
    
    from vertexai import agent_engines
    
    agent_engines.[list](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(filter=f'display_name="{DISPLAY_NAME}"')
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
