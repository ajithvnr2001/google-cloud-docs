---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/concurreny-and-parallelism/
title: Concurrency and parallelism \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:00.121640+00:00
---

# Concurrency and parallelism  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/concurreny-and-parallelism/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Concurrency and parallelism Stay organized with collections  Save and categorize content based on your preferences. 

The `concurrency` parameter controls how many programs are generated and evaluated simultaneously. This parameter is the most impactful runtime hyperparameter.

## How concurrency affects search

  * `n = 1` (Sequential chain): Generate one program, wait for evaluation, and then generate the next. Each generation sees the previous result, creating a chain of incremental improvements that zooms in on a local optimum. This approach results in the slowest throughput but the most focused exploitation. Use this mode to intentionally converge on a specific region.

  * `n = 3-12` (Sweet spot): This is the most widely used range in practice, balancing exploration and exploitation. Multiple programs are in flight simultaneously, so some generations don't see the latest results, introducing natural diversity. The evolutionary database maintains enough throughput for healthy population dynamics.

  * `n = 13-30` (High exploration): Many programs run in parallel. Most generations don't see each other's results. This mode is useful for highly non-convex problems with many local optima where broad exploration matters more than deep exploitation.

  * `n = 23-30` (Throttled; avoid): Exceeding 30 parallel generators throttles the LLM backend. Requests queue up, increasing latency per generation. Unless you have a dedicated quota, stay less than 30.




## Recommendations

The following recommendations serve as a starting point for configuring concurrency and parallelism for AlphaEvolve.

Problem Type | Concurrency | Rationale  
---|---|---  
Well-understood, tuning known approach | 3–5 | Focused exploitation  
General optimization, unknown landscape | 8–12 | Balanced exploration/exploitation  
Highly non-convex, many local optima | 15–25 | Broad exploration  
Intentional local optimum zoom-in | 1 | Sequential chain  
  
Start with `concurrency=10` and adjust based on the following indicators:

  * Score plateau: Increase concurrency to escape local optima.

  * Many failing evaluations: Decrease concurrency to reduce wasted compute.

  * Slow evaluations (greater than 5 minutes): Higher concurrency keeps the evaluation pipeline busy.

  * Fast evaluations (lesser than 10 seconds): Lower concurrency allows successive generations to build directly on each other's results.




## Concurrency versus active experiment limits

It's important to distinguish between program-level concurrency and project-level experiment limits:

  * **Program concurrency (`concurrency`):** Configured in `runSettings` (between `1` and `30`), this controls the number of candidate programs generated and evaluated simultaneously within a single experiment.
  * **Active experiment limit:** A project is subject to a cap of **30 concurrently active (`STARTED` or `RUNNING`) experiments per location**. Attempting to start or resume an experiment beyond this cap returns a `RESOURCE_EXHAUSTED` error. To resolve this, stop or complete existing running experiments before starting new ones (modifying `concurrency` within an experiment doesn't change your active experiment count).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
