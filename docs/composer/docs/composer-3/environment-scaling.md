---
url: https://docs.cloud.google.com/composer/docs/composer-3/environment-scaling/
title: About environment scaling \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:02.392192+00:00
---

# About environment scaling  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/environment-scaling/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  About environment scaling Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/environment-scaling "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/environment-scaling "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how environment scaling works.

Other pages about scaling:

  * For a guide about selecting optimal scale and performance parameters for your environment, see [Optimize environment performance and costs](https://docs.cloud.google.com/composer/docs/composer-3/optimize-environments).
  * For information about scaling your environments, see [Scale environments](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments).



## Autoscaling environments

Managed Airflow environments automatically scale in response to the demands of your executed DAGs and tasks:

  * If your environment experiences a heavy load, Managed Airflow automatically increases the number of workers in your environment.
  * If your environment doesn't use some of its workers, these workers are removed to save environment resources and costs.
  * You can set the minimum and maximum number of workers for your environment. Managed Airflow automatically scales your environment within the set limits. You can adjust these limits at any time.



The number of workers is adjusted based on the [Scaling Factor Target](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments#worker-metrics) metric. This metric is calculated based on:

  * Current number of workers
  * Number of Celery tasks in the Celery queue, that are not assigned to a worker
  * Number of idle workers
  * `celery.worker_concurrency` Airflow configuration option



Managed Airflow autoscaling uses three different autoscalers provided by GKE:

  * [Horizontal Pod Autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)
  * [Cluster Autoscaler (CA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
  * [Node auto-provisioning (NAP)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)



Managed Airflow configures these autoscalers in the environment's cluster. This automatically scales the number of nodes in the cluster, the machine type and the number of workers.

## Scale and performance parameters

In addition to autoscaling, you can control the scale and performance parameters of your environment by adjusting the CPU, memory, and disk limits of workers, schedulers, DAG processors, triggerers, and the web server. By doing so you can scale your environment vertically, in addition to the horizontal scaling provided by the autoscaling feature. You can adjust the scale and performance parameters at any time.

The _environment size_ performance parameter of your environment controls the performance parameters of the managed Managed Airflow infrastructure that includes the Airflow database. Consider selecting a larger environment size if you want to run a large number of DAGs and tasks with higher infrastructure performance. For example, larger environment's size increases the amount of Airflow task log entries that your environment can process with minimal delay.

Environment size is different from _environment presets_. Environment presets, which you can select when you create an environment in the Google Cloud console, determine the initial limits, scale, and performance parameters of your environment, including the environment size. Environment size determines only the performance parameters of the managed Managed Airflow infrastructure of your environment.

## Multiple schedulers

Your environment can run more than one Airflow scheduler and DAG processor at the same time:

  * You can set the number of schedulers and DAG processors for your environment and adjust it at any time.
  * Managed Airflow doesn't automatically scale the number of schedulers or DAG processors in your environment.



For more information about configuring the number of schedulers and DAG processors for your environment, see [Scale environments](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#scheduler-parameters).

## Database disk space

Disk space for the Airflow database automatically increases to accommodate the demand.

## What's next

  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments)
  * [Managed Airflow pricing](https://docs.cloud.google.com/composer/pricing)
  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
