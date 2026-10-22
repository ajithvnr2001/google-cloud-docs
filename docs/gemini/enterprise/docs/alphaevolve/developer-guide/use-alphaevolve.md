---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve/
title: Use AlphaEvolve \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:15.069649+00:00
---

# Use AlphaEvolve  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  Use AlphaEvolve Stay organized with collections  Save and categorize content based on your preferences. 

After you have a working Gemini Enterprise environment and have confirmed API access, you are ready to get started with the AlphaEvolve API.

Several assets and artifacts are available in the AlphaEvolve repository to help you execute your first AlphaEvolve experiment:

  * AlphaEvolve Skills: Use these skills with a coding assistant to facilitate the end-to-end workflow for AlphaEvolve experiments.

  * Example use case experiments (code): Explore sample code encompassing a range of optimization challenges and AlphaEvolve use cases, such as combinatorial optimization, multi-objective signal processing, and LLM fine-tuning.

  * Cluster Toolkit examples: Simplify the process of deploying high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads on Google Cloud. For more information, see [AlphaEvolve for HPC use cases](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve-hpc).




To begin, clone the AlphaEvolve repository or download the provided TAR file.

## AlphaEvolve skills for agentic development

The AlphaEvolve skills allow you to run AlphaEvolve experiments directly from an agentic coding assistant, such as the Antigravity. Using these skills, your coding assistant guides you through the entire AlphaEvolve workflow, including configuring the experiment, running the evolutionary loop, monitoring progress, and integrating the best results back into your code.

The [repository](https://github.com/Google-Cloud-AI/alphaevolve-on-googlecloud) includes six specific AlphaEvolve skills, with a `README.md` and a `SKILLS.md` file provided for each:

  * `alpha_evolve_consultant`
  * `alpha_evolve_experiment_design`
  * `alpha_evolve_monitor`
  * `alpha_evolve_orchestrator`
  * `alpha_evolve_post_experiment`
  * `alpha_evolve_runner`



### Current limitations

  * Python only: The skills only support evolving Python code.

  * Single code location: The system is tested to evolve one code location at a time. While context from multiple files can be included, simultaneously optimizing multiple evolve blocks is not yet validated.




## Usage

Authenticate with the Google Cloud CLI:
    
    
       gcloud auth application-default login
    

Prompt your coding assistant to optimize your code with AlphaEvolve. Example prompts include the following:

  * "Use AlphaEvolve to optimize the code of this model to make it faster."

  * "Set up an AlphaEvolve experiment to find a better algorithm for this scheduling function."

  * "Evolve this loss function to improve convergence on this XYZ benchmark."




The assistant walks you through configuration, runs the evaluation loop, and helps you integrate the best result back into your codebase.

In addition to workflow skills, the `alpha_evolve_consultant` skill acts as an expert Q&A assistant for AlphaEvolve. It can help you determine whether a problem is suitable for AlphaEvolve, advise on evaluator implementation, explain runtime configuration options, and troubleshoot issues based on the official AlphaEvolve reference guide.

**Note:** The consultant skill is purely advisory and does not execute experiments or modify code. Invoke it by asking questions like "Is my problem a good fit for AlphaEvolve?" or "How should I design my evaluator?".**Tip:** Google recommends using Gemini 3.5 Flash as the coding assistant model. The skill works best when you provide a Markdown file that defines the problem, the objective, and relevant background details (such as constraints, evaluation criteria, or known baselines). Your code requires `# EVOLVE-BLOCK-START` and `# EVOLVE-BLOCK-END` markers around the code targeted for evolution, alongside an evaluation function. You can add these manually or ask the coding assistant for help (for example, "prepare this file for optimization with AlphaEvolve").

## AlphaEvolve use cases

The AlphaEvolve repository contains the client-side Python library and example experiments in the `use-cases` folder. Review the `README` file before getting started with these curated examples:

Use Case / Level | Description | Core Learning Focus  
---|---|---  
**Getting started: Combinatorial optimization (basic)** |  Evolve a pure-Python heuristic to pack circles into a unit square or find the shortest TSP tour using local `exec()` evaluation with zero cloud infrastructure.  |  Learn core loop mechanics (seed program → EVOLVE-BLOCK markers → evaluator → controller) and observe iterative improvement on baseline.   
**Multi-objective evaluation: Signal processing (Intermediate)** |  Evolve an adaptive time-series filter judged on over 14 competing metrics (smoothness, lag, false reversals, noise reduction, etc.) across 5 non-stationary test signals.  |  Learn to design weighted composite objectives, return structured insights for LLM self-correction, and protect evaluators with explicit timeouts.   
**Remote evaluation at scale: ML pipeline (intermediate)** |  Evolve a complete scikit-learn pipeline (feature engineering and model selection) scored by a containerized evaluator on Cloud Run.  |  Learn remote evaluation patterns using a `Dockerfile`, `cloudbuild.yaml`, and Terraform-provisioned Artifact Registry / IAM resources.   
**Production GPU infrastructure: LLM fine-tuning (advanced)** |  Evolve LoRA hyperparameters for Gemma on a function-calling dataset, trained on autoscaling L4 GPUs using a persistent RayCluster on GKE.  |  Learn to connect AlphaEvolve into production training infrastructure with cost controls and full observability.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
