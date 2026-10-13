---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-creation/
title: Troubleshoot creating an agent using Agent Runtime \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:19.687711+00:00
---

# Troubleshoot creating an agent using Agent Runtime  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/agent-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Troubleshoot creating an agent using Agent Runtime Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to resolve errors that you might encounter when [creating an agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent).

## Content generation errors

**Issue** :

You receive an error message similar to the following:
    
    
    ValueError: Cannot get the Candidate text.
    Response candidate content part has no text.
    

**Possible cause** :

This error might be caused by using a version of `langchain-google-vertexai` that's not compatible with `google-cloud-aiplatform`. Version `1.0.2` or later of `langchain-google-vertexai` is required. To check which version you're using, run the following command in your terminal:
    
    
    pip show langchain-google-vertexai

**Recommended solution** :

Install version `1.0.2` of `langchain-google-vertexai`. This version includes the [LangChain tool-calling](https://github.com/langchain-ai/langchain-google/pull/166) updates that are required to work with `google-cloud-aiplatform`. To update your version of `langchain-google-vertexai`, run the following command in your terminal:
    
    
    pip install langchain-google-vertexai --upgrade

After running the update command, verify that you're using version `1.0.2` or later by running the following command in your terminal:
    
    
    pip show langchain-google-vertexai

If you're in a notebook instance (for example, Jupyter or Colab or Workbench), you might need to restart your runtime to use the updated packages.

## Bring your own container (BYOC) first-time creation error

**Issue** :

You deploy agents through [BYOC](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent#from-container-image) in your Google Cloud project for the first time in the region you are in, and you receive an error message similar to the following:
    
    
    Reasoning Engine resource <reasoning-engine-id> failed to start and cannot serve traffic.
    

**Possible cause** :

The failure was likely due to Agent Runtime on Gemini Enterprise Agent Platform internal IAM provisioning. The changes take time to complete and propagate.

**Recommended solution** :

Retry the same agent deployment request, and it will succeed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
