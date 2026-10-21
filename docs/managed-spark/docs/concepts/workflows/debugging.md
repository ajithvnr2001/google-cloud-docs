---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/debugging/
title: Monitor and debug workflows \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:43.817397+00:00
---

# Monitor and debug workflows  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/debugging/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Monitor and debug workflows Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information to help you monitor and debug [Managed Service for Apache Spark workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview).

## List workflows

An instantiated [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#resource-workflowtemplate) is a called a "workflow" and is modeled as an "operation."

Run the following `gcloud` command to list your project's workflows:
    
    
    gcloud dataproc operations list \
        --region=region \
        --filter="operationType = WORKFLOW"
    
    
    
    ...
    OPERATION_NAME                                                DONE
    projects/.../operations/07282b66-2c60-4919-9154-13bd4f03a1f2  True
    projects/.../operations/1c0b0fd5-839a-4ad4-9a57-bbb011956690  True
    

Here's a sample request to list all workflows started from a "terasort" template:
    
    
    gcloud dataproc operations list \
        --region=region \
        --filter="labels.goog-dataproc-workflow-template-id=terasort"
    
    
    
    ...
    OPERATION_NAME                                     DONE
    projects/.../07282b66-2c60-4919-9154-13bd4f03a1f2  True
    projects/.../1c0b0fd5-839a-4ad4-9a57-bbb011956690  True
    

Note that only the UUID portion of `OPERATION_NAME` is used in subsequent queries.

## Using WorkflowMetadata

The `operation.metadata` field provides information to help you diagnose workflow failures.

Here's a sample [`WorkflowMetadata`](https://docs.cloud.google.com/managed-spark/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata), including a graph of nodes (jobs), embedded in an operation:
    
    
    {
      "name": "projects/my-project/regions/us-central1/operations/671c1d5d-9d24-4cc7-8c93-846e0f886d6e",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.dataproc.v1.WorkflowMetadata",
        "template": "terasort",
        "version": 1,
        "createCluster": {
          "operationId": "projects/my-project/regions/us-central1/operations/8d472870-4a8b-4609-9f7d-48daccb028fc",
          "Done": true
        },
        "graph": {
          "nodes": [
            {
              "stepId": "teragen",
              "jobId": "teragen-vtrprwcgepyny",
              "state": "COMPLETED"
            },
            {
              "stepId": "terasort",
              "prerequisiteStepIds": [
                "teragen"
              ],
              "jobId": "terasort-vtrprwcgepyny",
              "state": "FAILED",
              "error": "Job failed"
            },
            {
              "stepId": "teravalidate",
              "prerequisiteStepIds": [
                "terasort"
              ],
              "state": "FAILED",
              "error": "Skipped, node terasort failed"
            }
          ]
        },
        "deleteCluster": {
          "operationId": "projects/my-project/regions/us-central1/operations/9654c67b-2642-4142-a145-ca908e7c81c9",
          "Done": true
        },
        "state": "DONE",
        "clusterName": "terasort-cluster-vtrprwcgepyny"
      },
      "done": true,
      "error": {
        "message": "Workflow failed"
      }
    }
    Done!
    

## Retrieve a template

As shown in the previous example, the `metadata` contains the template id and version.
    
    
    "template": "terasort",
    "version": 1,
    

If a template is not deleted, instantiated template versions can be retrieved by a describe-with-version request.
    
    
    gcloud dataproc workflow-templates describe terasort \
        --region=region \
        --version=1
    

List cluster operations started by a template:
    
    
    gcloud dataproc operations list \
        --region=region \
        --filter="labels.goog-dataproc-workflow-instance-id = 07282b66-2c60-4919-9154-13bd4f03a1f2"
    
    
    
    ...
    OPERATION_NAME                                     DONE
    projects/.../cf9ce692-d6c9-4671-a909-09fd62041024  True
    projects/.../1bbaefd9-7fd9-460f-9adf-ee9bc448b8b7  True
    

Here's a sample request to list jobs submitted from a template:
    
    
    gcloud dataproc jobs list \
        --region=region \
        --filter="labels.goog-dataproc-workflow-template-id = terasort"
    
    
    
    ...
    JOB_ID                TYPE     STATUS
    terasort2-ci2ejdq2ta7l6  pyspark  DONE
    terasort2-ci2ejdq2ta7l6  pyspark  DONE
    terasort1-ci2ejdq2ta7l6  pyspark  DONE
    terasort3-3xwsy6ubbs4ak  pyspark  DONE
    terasort2-3xwsy6ubbs4ak  pyspark  DONE
    terasort1-3xwsy6ubbs4ak  pyspark  DONE
    terasort3-ajov4nptsllti  pyspark  DONE
    terasort2-ajov4nptsllti  pyspark  DONE
    terasort1-ajov4nptsllti  pyspark  DONE
    terasort1-b262xachbv6c4  pyspark  DONE
    terasort1-cryvid3kreea2  pyspark  DONE
    terasort1-ndprn46nesbv4  pyspark  DONE
    terasort1-yznruxam4ppxi  pyspark  DONE
    terasort1-ttjbhpqmw55t6  pyspark  DONE
    terasort1-d7svwzloplbni  pyspark  DONE
    

List jobs submitted from a workflow instance:
    
    
    gcloud dataproc jobs list \
        --region=region \
        --filter="labels.goog-dataproc-workflow-instance-id = 07282b66-2c60-4919-9154-13bd4f03a1f2"
    
    
    
    ...
    JOB_ID                TYPE     STATUS
    terasort3-ci2ejdq2ta7l6  pyspark  DONE
    terasort2-ci2ejdq2ta7l6  pyspark  DONE
    terasort1-ci2ejdq2ta7l6  pyspark  DONE
    

## Workflow timeouts

You can set a workflow timeout that will cancel the workflow if the workflow's jobs do not finish within the timeout period. The timeout period applies to the [DAG (Directed Acyclic Graph)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) of jobs in the workflow (the sequence of jobs in the workflow), not to the entire workflow operation. The timeout period starts when the first workflow job starts—it does not include the time taken to create a [managed cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster). If any job is running at the end of the timeout period, all running jobs are stopped, the workflow is ended, and if the workflow was running on a managed cluster, the cluster is deleted.

**Benefit:** Use this feature to avoid having to manually end a workflow that does not complete due to stuck jobs.

### Set a workflow template timeout

You can set a workflow template timeout period when you [create a workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#creating_a_template). You can also add a workflow timeout to an existing workflow template by updating the workflow template.

Workflow timeouts apply to any workflow [instantiated](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#running_a_workflow) after the timeout is set on the template. Existing workflows are not affected by a new or updated template.

### gcloud

To set a workflow timeout on a new template, use the `--dag-timeout` flag with the [gcloud dataproc workflow-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create) command. You can use "s", "m", "h", and "d" suffixes to set second, minute, hour, and day duration values, respectively. The timeout duration must be from 10 minutes ("10m") to 24 hours ("24h" or "1d").
    
    
    gcloud dataproc workflow-templates create template-id (such as "my-workflow") \
        --region=region \
        --dag-timeout=duration (from "10m" to "24h" or "1d"") \
        ... other args ...
    

### API

To set a workflow timeout, complete the `WorkflowTemplate` [`dagTimeout`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#WorkflowTemplate.FIELDS.dag_timeout) field as part of a [workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/create) request.

### Console

Currently, the Google Cloud console does not support creating a [workflow template](https://console.cloud.google.com/dataproc/workflows/templates).

### Update a workflow template timeout

You can update an existing workflow template to change, add, or remove a workflow timeout.

Workflow timeouts apply to any workflow [instantiated](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#running_a_workflow) after the timeout is set on the template. Existing workflows are not affected by a new or updated template.

### gcloud

**Adding or changing a workflow timeout**

To add or change a workflow timeout on an existing template, use the `--dag-timeout` flag with the [gcloud dataproc workflow-templates set-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-dag-timeout) command. You can use "s", "m", "h", and "d" suffixes to set second, minute, hour, and day duration values, respectively. The timeout duration must be from 10 minutes ("10m") to 24 hours ("24h").
    
    
    gcloud dataproc workflow-templates set-dag-timeout template-id (such as "my-workflow") \
        --region=region \
        --dag-timeout=duration (from "10m" to "24h" or "1d")
    

**Removing a workflow timeout**

To remove a workflow timeout from an existing template, use the [gcloud dataproc workflow-templates remove-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/remove-dag-timeout) command.
    
    
    gcloud dataproc workflow-templates remove-dag-timeout template-id (such as "my-workflow") \
        --region=region
    

### API

**Adding or changing a workflow timeout**

To add or change a workflow timeout on an existing template, [update the workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#updating_a_workflow_template) by filling in the template's [`dagTimeout`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#WorkflowTemplate.FIELDS.dag_timeout) field with the new or changed timeout value.

**Removing a workflow timeout**

To remove a workflow timeout from an existing template, [update the workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#updating_a_workflow_template) by removing the template's [`dagTimeout`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#WorkflowTemplate.FIELDS.dag_timeout) field. 

### Console

Currently, the Google Cloud console does not support updating a [workflow template](https://console.cloud.google.com/dataproc/workflows/templates).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
