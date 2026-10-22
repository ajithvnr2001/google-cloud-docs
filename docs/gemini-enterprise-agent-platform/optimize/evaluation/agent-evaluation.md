---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation/
title: Agent evaluation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:44:48.436882+00:00
---

# Agent evaluation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Agent evaluation Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of End-to-end agent evaluation, run the "Multi-Turn Agent Evaluation with User Simulation, Metric Registration, and Auto Loss Analysis" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/multi_turn_agent_evaluation_with_user_simulation_metric_registration_auto_loss_analysis.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fmulti_turn_agent_evaluation_with_user_simulation_metric_registration_auto_loss_analysis.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fmulti_turn_agent_evaluation_with_user_simulation_metric_registration_auto_loss_analysis.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/multi_turn_agent_evaluation_with_user_simulation_metric_registration_auto_loss_analysis.ipynb)

This document describes how to use agent evaluation to measure and improve the performance, safety, and quality of your agents.

To learn more about model evaluation, see [Gen AI evaluation service overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview).

## Procedure summary

Phase | Activity | Goal  
---|---|---  
**Design** | Define eval cases | Specify agent tasks and expected outcomes.  
**Execution** | Run inferences | Generate real-world or simulated conversation traces.  
**Scoring** | Compute metrics | Grade traces using automated raters (Task Success, Safety).  
**Refinement** | Optimize agent | Propose and verify improvements to instructions or tools.  
  
## Evaluation process

Evaluation follows a structured, iterative workflow:

  1. **Define eval cases** : An _eval case_ is a specification that defines an agent's task. An eval case can include one or multiple conversation steps, the conversation context (the agent's state), and a specification for simulating user responses during inference.
  2. **Run inferences** : _Inference_ is the execution of an eval case. If an eval case contains a conversation plan, user responses are simulated during inference.
  3. **Generate traces** : Each inference run captures the agent's behavior in a trace. A _trace_ is a factual, immutable record of the agent's behavior, including model inputs, responses, and tool calls.
  4. **Compute metrics** : _Metrics_ are scores computed for each trace using prebuilt or custom raters. Some metrics, like **Exact Match** , are _reference-based_ and require an eval case with a reference answer. Others, like **Helpfulness** , are _reference-free_ and evaluate the trace on its own. This automated evaluation lets you score traces captured from production traffic or external logs, independent of a managed test environment.
  5. **Conduct analysis** : Analyze metrics, rubrics, and verdicts to identify key agent issues, link the agent issues back to test cases, and generate insights for improvement.
  6. **Optimize the agent** : Use optimization to manage the entire evaluation cycle. This automated process analyzes results, proposes improvements to the agent, and iteratively reruns the process to verify performance gains.



### Evaluation workflow

You can integrate evaluation into two main stages of your workflow:

  * **Local development iteration** : Evaluate an Agent Development Kit (ADK)-based agent locally to rapidly iterate on prompt engineering and tool configurations.
  * **Deployed agent assessment** : Measure the quality of deployed agents by analyzing historical traces or running synthetic benchmarks against agent endpoints.



## Core capabilities

Agent evaluation helps you build an initial evaluation suite, even without existing test data. The following features help automate the process of generating test cases and refining your agentic systems:

  * **Scenario generation and user simulation** : Automatically generate diverse, multi-turn synthetic test scenarios based on your agent's instructions and tool definitions. This automation allows you to start testing immediately by eliminating the need to manually author initial test cases.

  * **Environment simulation** : Intercept specific tool calls to inject custom behaviors, mocked data, or simulated errors (such as HTTP 503 errors or latency spikes). This simulation lets you validate agent resilience without impacting production backends.

  * **Multi-turn evaluation** : Automatically evaluate entire conversation histories using multi-turn autoraters. These raters analyze intent extraction, dynamically generate rubrics, and provide objective validation verdicts to help ensure instruction adherence.

  * **Prompt optimization** : Programmatically generate and validate refined system instructions by using prompt optimization. The optimization framework identifies points of failure and iteratively proposes targeted updates.




## Evaluate with AI coding assistants

If you use Gemini CLI or another AI coding assistant, you can install Agent [skills](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/skill-registry) that teach your assistant the agent evaluation methodology described on this page. Each skill provides the eval workflow, dataset schema, metric selection guidance, and failure analysis steps directly in your coding session, so your assistant can build, grade, and improve evaluations without leaving your editor.

Installation instructions follow each skill.

### Agents CLI eval skill

A CLI-driven workflow to evaluate and optimize Agent Development Kit (ADK) agents using the `agents-cli eval` commands. This skill covers:

  * Preparing eval datasets and synthesizing multi-turn scenarios with user simulation
  * Running inference, grading traces, and analyzing failure clusters
  * Iterating on prompts and tools with the eval-fix loop



To install, run the following command:
    
    
    npx skills add https://github.com/google/agents-cli --skill google-agents-cli-eval
    

### Agent Platform GenAI Evaluation Service flywheel skill

An SDK-driven playbook to evaluate and improve models and agents through the Agent Platform GenAI Evaluation Service, using the Agent Platform GenAI Evaluation SDK (`client.evals.evaluate()`). This skill covers:

  * Building eval datasets from session traces, DataFrames, or synthetic generation
  * Selecting, configuring, and writing custom metrics with LLM-as-judge scoring
  * Analyzing rubric verdicts and loss patterns to drive concrete improvements



To install, run the following command:
    
    
    npx skills add https://github.com/google/skills --skill agent-platform-eval-flywheel
    

## What's next

  * [Simulate agent behavior](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-simulated)
  * [Run evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-agents)
  * [Manage evaluation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/manage-metrics)
  * [View evaluation results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/view-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
