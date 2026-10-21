---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-case-qualification/
title: Use case qualification criteria \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:51:58.323941+00:00
---

# Use case qualification criteria  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-case-qualification/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Use case qualification criteria Stay organized with collections  Save and categorize content based on your preferences. 

To determine whether a use case is a suitable fit for AlphaEvolve, evaluate it against the following three key considerations.

  1. Problem formulation feasibility:

Assess how straightforward it is to express the problem as an algorithm optimization problem.

     * Direct code optimization: The problem involves directly optimizing code performance.

       * Suitability: Possible good fit.
     * General mathematical search or combinatorial optimization: The decision variables and constraints on feasible solutions can be described as a program in a standard programming language, supported by a corresponding set of unit and functional tests. This applies to most mathematical optimization use cases.

       * Suitability: Possible good fit.
     * Specialized mathematical search with unique data modalities: The optimization involves data modalities that cannot be expressed as parameters and variables in a computer program (for example, protein structures, genomics data, or image and video content optimization).

       * Suitability: Not a fit. Consider a domain-specific optimization model or agent instead, such as AlphaFold or AlphaGenome for life sciences, or a GenMedia agent for marketing and creative use cases.

Ensure that the core logic and constraints of the problem can be completely translated into code before proceeding.

  2. Optimization problem complexity:

Evaluate whether the complexity of the optimization problem aligns with AlphaEvolve's capabilities.

     * For algorithm discovery and optimization: Evaluate the complexity of the design space for potentially correct programs:

       * Narrow and well-defined design choices: Not a fit.

       * Exponentially large or unbounded design choices: Possible good fit.

     * For general mathematical search and combinatorial optimization

Evaluate the nature of the feasible decision variables and the objective function:

       * Convex, linear, or both objective function: Not a fit.

       * Non-convex, highly non-linear, or both objective function: Possible good fit.

AlphaEvolve delivers the highest ROI when exact solvers encounter combinatorial scaling limitations.

  3. Evaluation feasibility and runtime:

Determine if the performance of a proposed solution can be measured and within a reasonable timeframe (typically in the order of a few minutes).

For large and complex code problems that take too long to run locally or on individual Cloud Run machines, you can use the AlphaEvolve HPC solution. This solution is deployed with the Cluster Toolkit and uses Batch and Cloud Build to run evaluations in parallel on high-resource machine types. For more information, see [AlphaEvolve HPC solution](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve-hpc).

A use case is a good fit if the solution validation metrics and optimization objectives can be evaluated using any of the following methods:

     * Deterministic calculation: Computed analytically using formulas or baseline runtime tests.

     * Data-driven estimation: Estimated by validating against out-of-sample test datasets or simulated using specialized simulation tools and models.

     * Infrastructure testing: Measured directly using load tests and performance testing on the target infrastructure components.

Fast, automated, and deterministic evaluation loops are critical to enabling successful evolutionary search cycles.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
