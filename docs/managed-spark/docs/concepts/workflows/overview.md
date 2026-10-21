---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview/
title: Overview of Managed Service for Apache Spark Workflow Templates \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:38.198292+00:00
---

# Overview of Managed Service for Apache Spark Workflow Templates  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Overview of Managed Service for Apache Spark Workflow Templates Stay organized with collections  Save and categorize content based on your preferences. 

The Managed Service for Apache Spark [WorkflowTemplates API](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates) provides a flexible and easy-to-use mechanism for managing and executing workflows. A Workflow Template is a reusable workflow configuration. It defines a graph of jobs with information on where to run those jobs.

**Key Points:**

  * [Instantiating a Workflow Template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#running_a_workflow) launches a Workflow. A Workflow is an operation that runs a [Directed Acyclic Graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) of jobs on a cluster. 
    * If the workflow uses a managed cluster, it creates the cluster, runs the jobs, and then deletes the cluster when the jobs are finished.
    * If the workflow uses a cluster selector, it runs jobs on a selected existing cluster.
  * Workflows are ideal for complex job flows. You can create job dependencies so that a job starts only after its dependencies complete successfully.
  * When you [create a workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#creating_a_template) Managed Service for Apache Spark does not create a cluster or submit jobs to a cluster. Managed Service for Apache Spark creates or selects a cluster and runs workflow jobs on the cluster when a workflow template is **instantiated**.



## Kinds of Workflow Templates

### Managed cluster

A workflow template can specify a managed cluster. The workflow will create an "ephemeral" cluster to run workflow jobs, and then delete the cluster when the workflow is finished.

### Cluster selector

A workflow template can specify an existing cluster on which to run workflow jobs by specifying one or more [user labels](https://docs.cloud.google.com/managed-spark/docs/concepts/labels) previously attached to the cluster. The workflow will run on a cluster that matches all of the labels. If multiple clusters match all labels, Managed Service for Apache Spark selects the cluster with the most YARN available memory to run all workflow jobs. At the end of workflow, Managed Service for Apache Spark does not delete the selected cluster. See [Use cluster selectors with workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors) for more information.

A workflow can select a specific cluster by matching the `goog-dataproc-cluster-name` label (see [Using Automatically Applied Labels](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors#using_automatically_applied_labels)).

### Parameterized

If you will run a workflow template multiple times with different values, use parameters to avoid editing the workflow template for each run:

  1. define parameters in the template, then

  2. pass different values for the parameters for each run.




See [Parameterization of Workflow Templates](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-parameters) for more information.

### Inline

Workflows can be instantiated inline using the `gcloud` command with [workflow template YAML files](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-yamls#instantiate_a_workflow_using_a_yaml_file) or by calling the Managed Service for Apache Spark [InstantiateInline](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/instantiateInline) API (see [Using inline Dataproc workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/inline-workflows)). Inline workflows do not create or modify workflow template resources.

Inline workflows can be useful for rapid prototyping or automation. 

## Workflow Template use cases

  * **Automation of repetitive tasks.** Workflows encapsulate frequently used cluster configurations and jobs.

  * **Transactional fire-and-forget API interaction model.** Workflow Templates replace the steps involved in a typical flow, which include:

    1. creating the cluster
    2. submitting jobs
    3. polling
    4. deleting the cluster

Workflow Templates use a single token to track progress from cluster creation to deletion, and automate error handling and recovery. They also simplify the integration of Managed Service for Apache Spark with other tools, such as Cloud Run functions and Managed Service for Apache Airflow.

  * **Support for ephemeral and long-lived clusters.** A common complexity associated with running Apache Hadoop is tuning and right-sizing clusters. Ephemeral (managed) clusters are easier to configure since they run a single workload. Cluster selectors can be used with longer-lived clusters to repeatedly execute the same workload without incurring the amortized cost of creating and deleting clusters.

  * **Granular IAM security.** Creating Managed Service for Apache Spark clusters and submitting jobs require all-or-nothing IAM permissions. Workflow Templates use a per-template [workflowTemplates.instantiate](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#workflow_templates_methods_required_permissions) permission, and do not depend on cluster or job permissions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
