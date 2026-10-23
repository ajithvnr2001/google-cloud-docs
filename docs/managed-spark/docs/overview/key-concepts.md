---
url: https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts/
title: Managed Service for Apache Spark key concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:51.969432+00:00
---

# Managed Service for Apache Spark key concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark key concepts Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the key concepts, fundamental building blocks, core features, and benefits of Managed Service for Apache Spark. Understanding these fundamentals help you effectively use Managed Service for Apache Spark for your data processing tasks.

## The serverless model

[Managed Service for Apache Spark serverless](https://docs.cloud.google.com/managed-spark/docs/serverless-overview) is the modern, automated-execution Managed Service for Apache Spark model. It lets you run jobs without provisioning, managing, or scaling the underlying infrastructure: Managed Service for Apache Spark handles the details for you.

  * **Batches** : A batch (also called a _batch workload_) is the serverless equivalent of a Managed Service for Apache Spark job. You submit your code, such as a Spark job, to the service. Managed Service for Apache Spark provisions the necessary resources on-demand, runs the job, and then tears them down. You don't create or manage cluster or job resources; the service does the work for you.
  * **Interactive sessions** : Interactive sessions provide a live, on-demand environment for exploratory data analysis, typically within a Jupyter notebook. Interactive sessions provide the convenience of a temporary, serverless workspace that you can use to run queries and develop code without having to provision and manage cluster and notebook resources.
  * **Session templates** : A session template is a reusable configuration you can use to define interactive sessions. The template contains session settings, such as Spark properties and library dependencies. You use the template to create interactive session environments for development, typically within a Jupyter notebook.



## The cluster-based model

[Managed Service for Apache Spark on clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/clusters-overview) is the standard, infrastructure-centric way of using Managed Service for Apache Spark. It gives you full control over a dedicated set of virtual machines for your data processing tasks.

  * **Clusters** : A cluster is your personal data processing engine, made up of Google Cloud virtual machines. You create a cluster to run open-source frameworks such as Apache Spark and Apache Hadoop. You have full control over cluster size, machine types, and configuration.
  * **Jobs** : A job is a specific task, such as a PySpark script or Hadoop query. Instead of running a job directly on a cluster, you submit the job to Managed Service for Apache Spark, which manages job execution for you. You can submit multiple jobs to the cluster.
  * **Workflow Templates** : A workflow template is a reusable definition that orchestrates a series of jobs (a workflow). It can define dependencies between jobs, for example to run a machine learning job only after a data cleaning job successfully completes. The templated workflow can run on an existing cluster or on a temporary (ephemeral) cluster that is created to run the workflow, and then deleted after the workflow completes. You can use the template to run the defined workflow whenever needed.
  * **Autoscaling policies** : An autoscaling policy contains rules that you define to add or remove worker machines from a cluster based upon cluster workload in order to dynamically optimize cluster cost and performance.



### Environment customization

Managed Service for Apache Spark on clusters offers cluster features and [components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview) you can use to customize your application environment.

### Notebook and development environments

Managed Service for Apache Spark serverless notebooks and IDEs link to integrated development environments where you can write and execute your code.

  * **BigQuery Studio & Workbench**: These are unified analytics and notebook environments. They allow you to write code (for example in a Jupyter notebook) and use a Managed Service for Apache Spark cluster or serverless session as the powerful backend engine to execute your code on large datasets.
  * **Managed Service for Apache Spark JupyterLab Plugin** : This official [`JupyterLabextension`](https://github.com/GoogleCloudDataproc/dataproc-jupyter-plugin) acts as a control panel for Managed Service for Apache Spark serverless inside your notebook environment. It simplifies your workflow by allowing you to browse, create, and manage clusters and submit jobs without having to leave the Jupyter interface.
  * **Google Cloud Data Agent Kit** : [Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) lets data scientists, engineers, and developers manage their entire data workload lifecycle within their IDE. Data Agent Kit provides support for Managed Service for Apache Spark, enabling you to develop code, create interactive sessions, and [build pipelines](https://docs.cloud.google.com/data-agent-kit/build-pipelines) directly from VS Code or a supported agentic CLI.
  * **Managed Service for Apache Spark Connect Python Connector** : This Python library streamlines the process of using [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html) with Managed Service for Apache Spark. It handles authentication and endpoint configuration, making it much simpler to connect your local Python environment, such as a notebook or IDE, to a remote Managed Service for Apache Spark cluster for interactive development.



## The container model

Managed Service for Apache Spark on Google Kubernetes Engine deploys Managed Service for Apache Spark **virtual** clusters on a GKE cluster. Unlike Managed Service for Apache Spark clusters, Managed Service for Apache Spark virtual clusters don't provision separate master and worker VMs. Instead, they provision node pools within a GKE cluster. Managed Service for Apache Spark on GKE jobs are run as pods on these node pools. The node pools and scheduling of pods on the node pools are managed by Managed Service for Apache Spark on GKE.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
