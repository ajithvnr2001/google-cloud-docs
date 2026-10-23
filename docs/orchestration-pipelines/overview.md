---
url: https://docs.cloud.google.com/orchestration-pipelines/overview/
title: Orchestration Pipelines overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:59.679516+00:00
---

# Orchestration Pipelines overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Guides ](https://docs.cloud.google.com/orchestration-pipelines/overview)



Send feedback 

#  Orchestration Pipelines overview Stay organized with collections  Save and categorize content based on your preferences. 

Orchestration Pipelines is a unified, declarative orchestration and automated deployment framework optimized for seamlessly managing data and AI pipelines on Google Cloud.

With Orchestration Pipelines, you can define your pipelines and their deployment configurations using a declarative YAML-based Domain Specific Language (DSL). This framework abstracts the underlying infrastructure, allowing you to focus on the logic of your data and AI workflows while Orchestration Pipelines handles the deployment, versioning, and orchestration.

## Intended usage scenarios

Orchestration Pipelines is designed for data engineers and data scientists who need to:

  * **Establish robust CI/CD for data pipelines:** Automatically validate and deploy pipelines whenever changes are committed to a repository.
  * **Manage multiple deployment environments:** Maintain separate configurations for development, staging, and production environments, each with its own runner settings and resources.
  * **Build pipelines using preferred tools:** Use your choice of IDEs (such as Colab, VS Code, or JupyterLab) and languages to develop pipelines that run across different engines.
  * **Ensure deployment consistency:** Use versioned pipeline bundles to ensure that all assets and configurations for a specific release are deployed and executed together.



## Key product features

  * **Declarative DSL:** A YAML-based language for defining pipelines, actions, and deployment configurations.
  * **Deployment Environments:** Support for multiple environments, each configured with its own runner environment (such as Managed Service for Apache Airflow) and artifact storage.
  * **Pipeline Bundles with Version Control and Reproducibility:** Versioned packages containing pipeline definitions and associated assets (like Python scripts) that are deployed as a single unit. Every deployment is tracked, making it easy to roll back or reproduce specific runs.
  * **Variable Substitution and Secret Management:** Flexible system for parameterizing pipelines using custom variables, environment variables, and secrets from CI/CD providers.
  * **Validation Tooling:** Built-in commands to check the syntax and semantic correctness of your pipelines before deployment.
  * **Manual and Scheduled Triggers:** Support for both automated scheduling and manual execution of pipelines.



## Supported frameworks and integrations

Orchestration Pipelines is designed to integrate with a wide variety of tools and services:

  * **Orchestration Engines:** Managed Service for Apache Airflow (Gen 2 and Gen 3), including support for Airflow 2 and Airflow 3.
  * **Compute and Data Engines:** BigQuery, Managed Service for Apache Spark, Managed Service for Apache Spark, Dataform, DBT.
  * **Development Environments:** VS Code, and Antigravity through Google Cloud Data Agent Kit extension.
  * **Git Providers:** GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
