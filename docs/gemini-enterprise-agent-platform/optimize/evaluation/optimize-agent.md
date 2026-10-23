---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent/
title: Optimize agent prompts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:31.031827+00:00
---

# Optimize agent prompts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Optimize agent prompts Stay organized with collections  Save and categorize content based on your preferences. 

The _Quality Flywheel_ is a continuous cycle of evaluation, analysis, and optimization. You evaluate your agent's performance, analyze the results to identify clusters of failures, and then optimize to address those specific issues. Each iteration improves agent quality.

The Agent Development Kit (ADK) provides an extensible framework for automated agent optimization. Automate agent optimization using the ADK's built-in `adk optimize` command. This command applies the [GEPA algorithm](https://github.com/gepa-ai/gepa) to iteratively refine root system instructions by evaluating them against your test suite.

The framework is extensible: you can implement custom optimization strategies, or develop custom samplers that integrate with your own evaluation pipelines.

For more details on how to get started with optimizing agents using ADK, see [Optimize agents](https://adk.dev/optimize/) in ADK's documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
