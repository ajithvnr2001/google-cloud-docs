---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve-hpc/
title: AlphaEvolve for HPC use cases \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:15.427541+00:00
---

# AlphaEvolve for HPC use cases  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve-hpc/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  AlphaEvolve for HPC use cases Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces the _AlphaEvolve HPC solution_ , which lets you run scalable, containerized code optimization experiments on Google Cloud.

AlphaEvolve relies on an iterative evolutionary loop: it generates candidate code, measures the code's fitness, and feeds results back to the AlphaEvolve API to guide future iterations. The AlphaEvolve HPC solution deploys a distributed infrastructure using [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview), [Batch](https://docs.cloud.google.com/batch), and Pub/Sub. It treats each candidate evaluation as an isolated, ephemeral job that runs on containerized, highly-resourced virtual machines (VMs).

## When to use the AlphaEvolve HPC solution

Instead of running evaluations locally or on Cloud Run instances, use the AlphaEvolve HPC solution if your workload doesn't fit standard environments:

  * **Evaluations take too long:** Your code problems are complex and take too long to run locally, or they exceed the resource and runtime limits of individual Cloud Run instances.

  * **You need specialized hardware:** Your evaluations require hardware accelerators (such as GPUs or TPUs) or compute-optimized HPC machine families (like H3 instances).

  * **You need large-scale parallelism:** You want to build and evaluate multiple candidate realizations concurrently in isolated environments.

  * **You want Infrastructure as Code (IaC):** You want a repeatable, automated setup that simplifies deploying and tearing down high-resource clusters to save effort and cost.




## What the AlphaEvolve HPC solution provides

The AlphaEvolve HPC solution provides an end-to-end flow for the configuration, deployment, and execution of the infrastructure required for AlphaEvolve optimization problems:

  * **Deployment of base infrastructure** : Use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to deploy the base infrastructure required for running optimizations. In this step, necessary APIs are activated, service accounts set up, a Pub/Sub topic and a Colab Enterprise runtime are provisioned. This base infrastructure can be reused for multiple optimization problems.

  * **Configuration of the software environment** : Configure and deploy the software environment for your specific optimization problem.

  * **Execution of experiments** : Starting, stopping, and analyzing an experiment is done from within a Jupyter Notebook running in Colab Enterprise connected to the custom Colab Enterprise runtime.




## How AlphaEvolve works

After you configure and deploy the solution, the actual AlphaEvolve optimization process runs as follows:

  1. **Generation** : The controller invokes the AlphaEvolve API (backed by Gemini) to propose code candidates based on a target metric and previous successful runs.

  2. **Evaluation** : Candidates are evaluated for correctness and performance in parallel as [Batch](https://docs.cloud.google.com/batch) jobs.

  3. **Storage** : Generated candidate files, source code revisions, and numeric test metrics are archived in a secure Cloud Storage bucket. Because the AlphaEvolve HPC solution stores experimental artifacts in the Cloud Storage bucket, you can tear down the infrastructure when it's not in use.

  4. **Feedback** : Results and insight logs are fed back to the AlphaEvolve API, allowing it to learn from successes and failures and intelligently sample better code in the next generation.




The AlphaEvolve HPC solution deploys the resources as described in the following architecture diagram. ![AlphaEvolve Execution Workflow](https://services.google.com/fh/files/misc/ae_execution_workflow.png)

## Deploy the AlphaEvolve HPC solution

To deploy the base infrastructure, build the container images, and run your optimization experiments, do the following:

  1. Go to the [AlphaEvolve HPC GitHub repository](https://github.com/GoogleCloudPlatform/scientific-computing-examples/tree/main/alphaevolve-hpc) and follow the instructions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
