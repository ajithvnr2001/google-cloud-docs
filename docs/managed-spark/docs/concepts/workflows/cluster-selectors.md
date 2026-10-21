---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors/
title: Use cluster selectors with workflows \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:36.494256+00:00
---

# Use cluster selectors with workflows  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use cluster selectors with workflows Stay organized with collections  Save and categorize content based on your preferences. 

As an alternative to running a workflow on a [managed cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster), you can use a cluster selector to choose an existing cluster for your workflow. At the conclusion of the workflow, the selected cluster is not deleted.

Selectors specify one or more [Managed Service for Apache Spark user labels](https://docs.cloud.google.com/managed-spark/docs/concepts/labels). Clusters in same [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) as the workflow whose labels match all of the selector labels are eligible to run workflow jobs. If multiple clusters match the selector, Managed Service for Apache Spark will choose the cluster with the most free YARN memory.

## Add a cluster selector to a template

You can add a cluster selector to a workflow template using the Google Cloud CLI or the Dataproc API.

### gcloud command
    
    
    gcloud dataproc workflow-templates set-cluster-selector template-id \
        --region=region \
        --cluster-labels=name=value[[,name=value]...]
    

### REST API

See [WorkflowTemplatePlacement.ClusterSelector](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#clusterselector). This field is provided as part of a completed [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) submitted with a [workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/create) or [workflowTemplates.update](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/update) request. 

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

## Use automatically applied labels

You can point a cluster selector to an existing cluster by using one of the following [automatically-applied cluster labels](https://docs.cloud.google.com/managed-spark/docs/concepts/labels#automatically-applied_labels):

  * `goog-dataproc-cluster-name`
  * `goog-dataproc-cluster-uuid`



**Example:**
    
    
    gcloud dataproc workflow-templates set-cluster-selector template-id \
        --region=region \
        --cluster-labels=goog-dataproc-cluster-name=my-cluster
    

## Select from a cluster pool

You can let Managed Service for Apache Spark choose a cluster from a pool of clusters. The cluster pools can be defined with labels.

**Example:**
    
    
    gcloud dataproc clusters create cluster-1 --labels cluster-pool=pool-1 \
        --region=region
    gcloud dataproc clusters create cluster-2 --labels cluster-pool=pool-1 \
        --region=region
    gcloud dataproc clusters create cluster-3 --labels cluster-pool=pool-2 \
        --region=region
    

After cluster creation ...
    
    
    gcloud dataproc workflow-templates create my-template \
        --region=region
    gcloud dataproc workflow-templates set-cluster-selector my-template \
        --region=region \
        --cluster-labels=cluster-pool=pool-1
    

The workflow will be run on either cluster-1 or cluster-2, but not on cluster-3.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
