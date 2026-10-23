---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/context-and-prompt-configuration/
title: Context and prompt configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:51.804006+00:00
---

# Context and prompt configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/context-and-prompt-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Context and prompt configuration Stay organized with collections  Save and categorize content based on your preferences. 

AlphaEvolve guides its operations by utilizing the provided code baseline as well as the specific context provided by the user.

## User context

The user-provided context is injected into every generation prompt. It balances the search space by providing the LLM with domain knowledge, mathematical formulations, and system constraints.

  * Token budget: Up to 200,000 tokens performs well. Beyond a 200k token threshold, the context window becomes loaded, the LLM's attention is decreased, and the mutation quality is reduced. If your combined context (problem description, code, and previous programs) exceeds 200k tokens, then you must reduce it.



### What to include

  * Precise mathematical formulation of the optimization problem.

  * Key constraints and their clear rationale.

  * Domain-specific terminology and definitions.

  * Known good approaches or prior art to guide the LLM's search direction.

  * Specific, explicit instructions detailing what NOT to do.




### What NOT to include

  * General programming tutorials.

  * Standard library documentation (the LLM already knows `numpy`, `sklearn`, etc.). However, DO include documentation for niche or domain-specific libraries the LLM might not know well (custom kernel APIs, proprietary SDKs, or specialized DSLs).

  * Raw arbitrary data, spreadsheets, or large data dumps. Data belongs in the evaluator harness, not in the prompt context.

  * Unrelated context that consumes tokens without adding a search signal.




Every piece of context you include must deliver clear value by actively helping the LLM produce better, structurally sound mutations.

## Evaluation feedback (Insights)

After each execution loop, the evaluator can return diagnostic feedback text alongside numerical scores. This feedback is automatically appended to future prompt structures.

  * Quality baseline: Strong feedback is specific, actionable, and concise. Poor feedback is generic (such as _"evaluation failed"_) or excessively verbose.

  * Operational purpose: These insights are displayed to the LLM in subsequent generations, allowing it to learn explicitly from execution failures and avoid repetitive bugs.




## Built-in prompt diversification

AlphaEvolve automatically diversifies the prompts it transmits to the backend LLM ensemble. This operation is handled internally and requires no manual user configuration. 

The system varies its core instructions across successive generations to encourage diverse mutations and prevent the LLM from falling into repetitive coding patterns. This behavior serves as one of the primary mechanisms helping AlphaEvolve explore a broad landscape rather than getting trapped in narrow local optima.

## Code readability

Code complexity acts as an effective auxiliary metric. If final code readability is a factor for your production use case, consider adding code length or cognitive complexity as a secondary target metric. 

AlphaEvolve can achieve up to 50% file compression without degrading functional performance. However, the LLM will exploit naive simplicity metrics (such as removing all inline comments to reduce raw character counts). To prevent this, implement metrics that capture meaningful structural complexity, such as cyclomatic complexity or Abstract Syntax Tree (AST) node counts, rather than evaluating raw string lengths.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
