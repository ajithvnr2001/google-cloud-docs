---
url: https://docs.cloud.google.com/workflows/docs/choose-orchestration/
title: Choose Workflows or Managed Airflow for service orchestration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:14.401784+00:00
---

# Choose Workflows or Managed Airflow for service orchestration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/choose-orchestration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Choose Workflows or Managed Airflow for service orchestration Stay organized with collections  Save and categorize content based on your preferences. 

Both [Workflows](https://docs.cloud.google.com/workflows/docs/overview) and [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/concepts/overview) can be used for service orchestration to combine services to implement application functionality or perform data processing. Although they are conceptually similar, each is designed for a different set of use cases. This page helps you choose the right product for your use case.

## Key differences

The core difference between Workflows and Managed Airflow is what type of architecture each product is designed to support.

**Workflows** orchestrates multiple HTTP-based services into a durable and stateful workflow. It has low latency and can handle a high number of executions. It's also completely serverless.

Workflows is great for chaining microservices together, automating infrastructure tasks like starting or stopping a VM, and integrating with external systems. Workflows connectors also support simple sequences of operations in Google Cloud services such as Cloud Storage and BigQuery.

**Managed Airflow** is designed to orchestrate data driven workflows (particularly ETL/ELT). It's built on the Apache Airflow project, but Managed Airflow is fully managed. Managed Airflow supports your pipelines wherever they are, including on-premises or across multiple cloud platforms. All logic in Managed Airflow, including tasks and scheduling, is expressed in Python as Directed Acyclic Graph (DAG) definition files.

Managed Airflow is best for batch workloads that can handle a few seconds of latency between task executions. You can use Managed Airflow to orchestrate services in your data pipelines, such as triggering a job in BigQuery or starting a Dataflow pipeline. You can use pre-existing operators to communicate with various services, and there are over 150 operators for Google Cloud alone.

## Detailed feature comparison

Feature | Workflows | Managed Airflow  
---|---|---  
Syntax | Workflows syntax in YAML or JSON format | Python  
State model | Imperative flow control | Declarative [DAG with automatic dependency resolution](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html#dags)  
Integrations | [HTTP requests](https://docs.cloud.google.com/workflows/docs/http-requests) and [connectors](https://docs.cloud.google.com/workflows/docs/connectors) | Airflow [Operators](https://docs.cloud.google.com/composer/docs/how-to/using/writing-dags#operators) and [Sensors](https://airflow.apache.org/docs/apache-airflow/stable/concepts/sensors.html)  
Passing data between steps | [512 KB for variables](https://docs.cloud.google.com/workflows/quotas#resource_limits) | 48 KB1 for [XCom](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html)  
Execution triggers and scheduling | gcloud CLI, Google Cloud console, Workflows API, Workflows client libraries, Cloud Scheduler | [Cron-like schedules](https://docs.cloud.google.com/composer/docs/triggering-dags#trigger_a_dag_on_a_schedule) in the DAG definition file, Airflow Sensors  
Asynchronous patterns | 

  * Polling
  * [Callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints)
  * Waiting for long-running Google Cloud operations

| Polling  
Parallel execution | Either concurrent executions of the same workflow or within a workflow using [parallel steps](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps) | Automatic based on dependencies  
Execution latency | Milliseconds | Seconds  
Based on open source | No | Yes (Apache Airflow)  
Scaling model | Serverless (scales up to demand and down to zero) | Provisioned  
Billing model | [Usage-based (per step executed)](https://docs.cloud.google.com/workflows/pricing) | [Based on provisioned capacity](https://docs.cloud.google.com/composer/pricing)  
Data processing features | No | [Backfills](https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html#backfill), ability to [re-run DAGs](https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html#re-run-dag)  
  
* * *

  1. [Source code for airflow.models.xcom](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/models/xcom.html). _Apache Airflow documentation_. August 2, 2021. ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
