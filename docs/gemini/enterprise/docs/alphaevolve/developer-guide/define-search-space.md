---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/define-search-space/
title: Define the search space and decision variables \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:50.486224+00:00
---

# Define the search space and decision variables  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/define-search-space/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Define the search space and decision variables Stay organized with collections  Save and categorize content based on your preferences. 

Defining the search space and decision variables for an AlphaEvolve use case requires proper formulation of the problem as code and providing a working baseline solution that the evolutionary heuristic can iterate on and improve.

This process includes:

  * Providing the target context: Establish the background, domain rules, and performance boundaries for the optimization use case.

  * Providing a clean baseline: Supply clear and well-structured code that correctly implements a baseline solution for the target problem.

  * Tagging degrees of freedom: Annotate the codebase with explicit `EVOLVE-BLOCK` comments to mark the specific decision variables, logic structures, or routines that the agent can mutate and explore to identify higher-performing solutions.


**Note:** Ensure that the baseline code passes all functional verification tests before handing it over to the evolutionary loop.

## Structure of an initial program

An initial program is composed of two primary block types that determine the boundaries of the evolutionary search:

  1. Immutable code blocks: Boilerplate code, helper functions, and dependencies that constrain the search space or execute tasks that don't impact solution performance (such as standard preprocessing steps or data handling routines).

  2. Mutable code blocks (`EVOLVE-BLOCK`): The targeted regions containing specific decision variables, logic structures, or analytical expressions that the agent is allowed to explore and mutate.
         
         import numpy as np
         # Code to constrain the search space (Immutable)
         def def_preprocessing():
             """Feature engineering and preprocessing."""
             pass
         
         # EVOLVE-BLOCK-START
         # Mutable block: Provides degrees of freedom for AlphaEvolve to optimize
         def model_tuning():
             """Model tuning function: parametrized to take features."""
             pass
         # EVOLVE-BLOCK-END
         
         # Boilerplate code that does not impact solution performance (Immutable)
         def batch_predictions():
             """Inference function: batch predictions to test performance."""
             pass
         




`EVOLVE-BLOCK` formatting rules include the following:

  * Standalone lines: The `EVOLVE-BLOCK-START` and `EVOLVE-BLOCK-END` comment markers must appear alone on their own lines. Don't place code or other content on the same line as a marker, except for whitespace and comment prefixes (such as `#` or `//`).
  * Editable code required: The region between the start and end markers must contain at least one line of editable code. Blocks containing only whitespace, comments, or docstrings are rejected with a validation error because there is no mutable logic for AlphaEvolve to evolve.
  * No nesting: Nested evolve blocks aren't supported.

**Note:** Your initial program code must be clear and organized. Unstructured code introduces noise into the search space and degrades mutation quality.

## Best practices for constraining the search space

How you arrange your immutable imports and place your evolve blocks explicitly shows AlphaEvolve's operational boundaries.

### Manage library imports and dependencies

AlphaEvolve cannot inherently determine which external libraries are valid for your production environment.

To allow open exploration: If any machine learning or mathematical package is acceptable to maximize your metric, place the imports inside the mutable `EVOLVE-BLOCK`. This gives AlphaEvolve freedom to substitute alternative frameworks (such as replacing sklearn with TensorFlow or xgboost).

To enforce strict tool chains: If all models must come from a specific package, declare that package as an immutable import outside the evolve block. If AlphaEvolve requires additional internal modules from that package during search, it can still import them locally within its mutable space without violating the global constraint.

### Avoid an over-constrained search space

Formulate as many hard constraints as possible as immutable code blocks in the initial program or within the additional user-provided text context. This minimizes the chances of the agent exploring structurally infeasible solutions.

However, don't narrow the search space to the point where an evolutionary approach becomes redundant. For example, forcing AlphaEvolve to only use single-parameter linear regressions reduces the problem to a narrow configuration space that could be parsed by standard grid-search utilities. Instead, use soft constraints as negative penalties in your evaluation criteria to guide exploration without choking it.

### Strategic block placement for targeted objectives

Varying the scope of your `EVOLVE-BLOCK` shifts the entire optimization objective of your pipeline:

Optimizing out-of-sample (OOS) calibration: If your goal is broad algorithmic discovery, wrap the block around the entire model tuning and initialization routine.

Optimizing structural fit: If you want to preserve a linear framework but discover complex analytical expressions or custom mathematical transformations, isolate your mutable block strictly around the feature transformation logic, keeping the downstream model architecture fixed and immutable.

Preserving modular hierarchy (HDL/Verilog examples): When optimizing structural code block configurations, keep the `EVOLVE-BLOCK-START` and `EVOLVE-BLOCK-END` tags strictly inside the module definition boundaries. This prevents the search heuristic from making structurally invalid moves, such as trying to replace a single cleanly contained module with multiple unmapped, floating sub-modules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
