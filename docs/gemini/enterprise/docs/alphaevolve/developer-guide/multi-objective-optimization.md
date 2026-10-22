---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/multi-objective-optimization/
title: Multi-objective optimization \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:47.592154+00:00
---

# Multi-objective optimization  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/multi-objective-optimization/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Multi-objective optimization Stay organized with collections  Save and categorize content based on your preferences. 

AlphaEvolve can optimize against multiple concurrent objectives. While AlphaEvolve supports multi-objective optimization, keep the number of individual objectives limited to roughly the number a human expert can grasp when analyzing results.

Use the following approaches to structure your multi-objective search strategy:

  1. Combined objective function: One approach for multi-objective optimization is to leverage a combined objective function:
         
         obj = w1 * in_stock_rate - w2 * inventory_level
         

  2. Treat one objective as a constraint: Another approach is to treat one objective as a constraint. This is useful for optimizing one metric while keeping the other from dropping over or below a threshold.
         
         obj = in_stock_rate` # Optimize this
         
         # With: inventory_level <= budget (enforced as penalty where if inventory
         # level exceeds budget then a high negative value is returned)
         

This approach may require running multiple experiments at different constraint levels to trace out the Pareto front.

  3. Include different metrics as individual metrics in the dictionary. See the following key considerations associated with this approach:

     * Limit multi-objective optimization to 3-5 metrics. With too many metrics, the Pareto comparator fails – almost every program dominates on at least one metric. MAP Elites spends most of its time evolving parents that optimize trivial or noisy metrics. Reduce dimensionality through aggregation, selection, or PCA to 3-5 meaningful metrics.

     * Per-benchmark individual scores can cause overfitting. Passing individual scores for 5 benchmarks can lead to overfitting on some, while passing only the aggregated sum generalized better to unseen benchmarks. If generalization matters, consider aggregating scores before passing to AlphaEvolve rather than optimizing each benchmark independently.




When you enable this feature, AlphaEvolve tracks a Pareto frontier and MAP-Elites retains the best program for each metric. However, combined weighted scores offer simpler reasoning and debugging.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
