---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/reward-hacking-prevention/
title: Reward hacking prevention \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:46.275314+00:00
---

# Reward hacking prevention  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/reward-hacking-prevention/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Reward hacking prevention Stay organized with collections  Save and categorize content based on your preferences. 

There are a number of risks associated with reward hacking. See the following for risks and the corresponding mitigation strategies.

## Risk 1:

Greedy reward hacking. If `Obj = w1*S1 + w2*S2 + w3*S3`, AlphaEvolve may discover S2 to increase and focus entirely on it, ignoring S1 and S3.

### Mitigation:

Decrease the weight of the sub-score. May require 2-3 trial runs to calibrate weights. Preliminary baseline simulations of a few scoring outcomes help.

## Risk 2:

Constraint penalty ignoring. If soft constraints are penalties `(Obj = Score - w*Penalty)`, AlphaEvolve may discover that ignoring constraints yields higher `Obj`.

### Mitigation:

Increase the penalty weight substantially. If behavior persists, add explicit instructions in the problem description like "Solutions violating constraint X are invalid regardless of score."

## Risk 3:

Evaluation function exploitation. AlphaEvolve may find inputs that cause the evaluator to return artificially high scores (floating-point edge cases, test data leakage).

### Mitigation:

Deterministic evaluation with fixed random seeds. Validate winners on held-out data after the experiment.

To prevent reward hacking, implement the following general techniques:

  * Use AST checks for forbidden primitives (sys, os, inspect, eval, exec, getattr, setattr) and return `None` if found.

  * Verify code outside `EVOLVE-BLOCK` is unchanged (text diff or AST).

  * Run the evolved function twice with the same input and verify identical output (catches randomness hacking).

  * Check evaluation time. If it finishes in microseconds, it probably hard-coded the answer.

  * Put scoring logic in a separate file invisible to the LLM.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
