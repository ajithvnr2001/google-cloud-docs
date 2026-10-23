---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/use-workflows/
title: Use workflows \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:23.774146+00:00
---

# Use workflows  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/use-workflows/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use workflows Stay organized with collections  Save and categorize content based on your preferences. 

You set up and run a workflow by:

  1. Creating a workflow template
  2. Configuring a managed (ephemeral) cluster or selecting an existing cluster
  3. Adding jobs
  4. Instantiating the template to run the workflow

You can [parameterize a workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-parameters) to use it dynamically for different workflows. You can also [use YAML files](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-yamls) or call the [InstantiateInline](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/instantiateInline) API to define and run an [inline](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview#inline) workflow that does not create or modify workflow template resources.

## Create a template

### Google Cloud console

Select **Create Workflow Template** from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console, then confirm or provide template, cluster, job, and dependencies settings.

### gcloud CLI

Run the following `command` to create a Managed Service for Apache Spark workflow template resource.
    
    
    gcloud dataproc workflow-templates create TEMPLATE_ID \
        --region=REGION
    

Notes:

  * REGION: Specify the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your template will run.
  * TEMPLATE_ID: Provide an ID for your template, such as, "workflow-template-1".
  * CMEK encryption. You can add the [\--kms-key](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/create#--kms-key) flag to use [CMEK encryption](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption#use_cmek_with_workflow_template_data) on workflow template job arguments.



### REST API

Submit a [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) as part of a [workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/create) request. You can add the [WorkflowTemplate.EncryptionConfig.kmsKey](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#encryptionconfig) field to use [CMEK encryption](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/customer-managed-encryption#use_cmek_with_workflow_template_data) on workflow template job arguments.

### Configure or select a cluster

Managed Service for Apache Spark can create and use a new, "managed" cluster for your workflow or an existing cluster.

  * **Existing cluster:** See [Using cluster selectors with workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors) to select an existing cluster for your workflow.

  * **Managed cluster:** You must configure a managed cluster for your workflow. Managed Service for Apache Spark will create this new cluster to run workflow jobs, then delete the cluster at the end of the workflow.

You can configure a managed cluster for your workflow using the Google Cloud console, Google Cloud CLI, or the Dataproc API. 

### Google Cloud console

Select **Create Workflow Template** from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console, then confirm or provide template, cluster, job, and dependencies settings.

### Google Cloud CLI

Use flags inherited from [gcloud dataproc cluster create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) to configure the managed cluster, such as the number of workers and the master and worker machine type.
        
        gcloud dataproc workflow-templates set-managed-cluster TEMPLATE_ID \
            --cluster-name=CLUSTER_NAME \
            --region=REGION \
            --master-machine-types="type=MACHINE_TYPE_1,rank=0" \
            --master-machine-types="type=MACHINE_TYPE_2,rank=1" \
            --worker-machine-types="type=PRIMARY_WORKER_MACHINE_TYPE_1,rank=0" \
            --worker-machine-types="type=PRIMARY_WORKER_MACHINE_TYPE_2,rank=1" \
            --num-workers=NUMBER \
            --service-account=SERVICE_ACCOUNT
        

Notes:

    * **CLUSTER_NAME:** Managed Service for Apache Spark adds a suffix to the cluster name to ensure uniqueness.
    * **MACHINE_TYPE:** You can use [flexible VM](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) ranked machine types to provide resiliency against resource unavailability.
    * **SERVICE_ACCOUNT:** You can specify a [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) for the managed cluster.

### REST API

See [WorkflowTemplatePlacement.ManagedCluster](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#managedcluster), which you can provide as part of a completed [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) submitted with a [workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/create) or [workflowTemplates.update](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/update) request.

You can use the [`GceClusterConfig.serviceAccount`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#gceclusterconfig) field to specify a [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) for the managed cluster.




## Add jobs to a template

All jobs run concurrently unless you specify one or more job dependencies. A job's dependencies are expressed as a list of other jobs that must finish successfully before the ultimate job can start. You must provide a `step-id` for each job. The ID must be unique within the workflow, but does not need to be unique globally.

### gcloud CLI

Use job type and flags inherited from [gcloud dataproc jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit) to define the job to add to the template. You can optionally use the `‑‑start-after job-id of another workflow job` flag to have the job start after the completion of one or more other jobs in the workflow.

The `--max-failures-per-hour` and `--max-failures-total` [restartable job flags](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/restartable-jobs#creating_and_using_restartable_jobs) are not supported in Managed Service for Apache Spark workflow template jobs.

**Examples:**

Add Hadoop job "foo" to the "my-workflow" template.
    
    
    gcloud dataproc workflow-templates add-job hadoop \
        --region=REGION \
        --step-id=foo \
        --workflow-template=my-workflow \
        -- space separated job args
    

Add job "bar" to the "my-workflow" template, which will be run after workflow job "foo" has completed successfully.
    
    
    gcloud dataproc workflow-templates add-job JOB_TYPE \
        --region=REGION \
        --step-id=bar \
        --start-after=foo \
        --workflow-template=my-workflow \
        -- space separated job args
    

Add another job "baz" to "my-workflow" template to be run after the successful completion of both "foo" and "bar" jobs.
    
    
    gcloud dataproc workflow-templates add-job JOB_TYPE \
        --region=REGION \
        --step-id=baz \
        --start-after=foo,bar \
        --workflow-template=my-workflow \
        -- space separated job args
    

### REST API

See [WorkflowTemplate.OrderedJob](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#orderedjob). This field is provided as part of a completed [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) submitted with a [workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/create) or [workflowTemplates.update](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/update) request.

The `maxFailuresPerHour` and `maxFailuresTotal` [OrderedJob.JobScheduling](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/JobScheduling) fields are not supported in Managed Service for Apache Spark workflow template jobs.

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

The `Max restarts per hour` [ restartable job option](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/restartable-jobs#creating_and_using_restartable_jobs) is not supported in Managed Service for Apache Spark workflow template jobs.

## Run a workflow

The instantiation of a workflow template runs the workflow defined by the template. Multiple instantiations of a template are supported—you can run a workflow multiple times.

### gcloud command
    
    
    gcloud dataproc workflow-templates instantiate TEMPLATE_ID \
        --region=REGION
    

The command returns an operation ID, which you can use to track workflow status.

**Example command and output:**
    
    
    gcloud beta dataproc workflow-templates instantiate my-template-id \
        --region=us-central1
    ...
    WorkflowTemplate [my-template-id] RUNNING
    ...
    Created cluster: my-template-id-rg544az7mpbfa.
    Job ID teragen-rg544az7mpbfa RUNNING
    Job ID teragen-rg544az7mpbfa COMPLETED
    Job ID terasort-rg544az7mpbfa RUNNING
    Job ID terasort-rg544az7mpbfa COMPLETED
    Job ID teravalidate-rg544az7mpbfa RUNNING
    Job ID teravalidate-rg544az7mpbfa COMPLETED
    ...
    Deleted cluster: my-template-id-rg544az7mpbfa.
    WorkflowTemplate [my-template-id] DONE
    
    

### REST API

See [workflowTemplates.instantiate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/instantiate). 

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

## Workflow job failures

A failure in any job in a workflow will cause the workflow to fail. Managed Service for Apache Spark will seek to mitigate the effect of failures by causing all concurrently executing jobs to fail and preventing subsequent jobs from starting.

## Monitor and list a workflow

### gcloud CLI

To monitor a workflow:
    
    
    gcloud dataproc operations describe OPERATION_ID \
        --region=REGION
    

**Note:** The operation-id is returned when you instantiate the workflow with `gcloud dataproc workflow-templates instantiate` (see Run a workflow). 

To list workflow status:
    
    
    gcloud dataproc operations list \
        --region=REGION \
        --filter="labels.goog-dataproc-operation-type=WORKFLOW AND status.state=RUNNING"
    

### REST API

To monitor a workflow, use the Managed Service for Apache Spark [operations.get](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.operations/get) API.

To list running workflows, use the Managed Service for Apache Spark [operations.list](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.operations/list) API with a label filter.

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

## Terminate a workflow

You can end a workflow using the Google Cloud CLI or by calling the Dataproc API.

**Note:** Ending a workflow cancels running workflow jobs and, if the workflow runs on a managed (ephemeral) cluster, deletes the managed cluster.

### gcloud command
    
    
    gcloud dataproc operations cancel OPERATION_ID \
        --region=REGION
    

**Note:** The operation-id that is returned when you instantiate the workflow with `gcloud dataproc workflow-templates instantiate` (see Run a workflow). 

### REST API

See the [operations.cancel](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.operations/cancel) API.

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

## Update a workflow template

Updates don't affect running workflows. The new template version will only apply to new workflows.

### gcloud CLI

Workflow templates can be updated by issuing new `gcloud workflow-templates` commands that reference an existing workflow template-id:

  * `gcloud dataproc workflow-templates add job`
  * `gcloud dataproc workflow-templates set-managed-cluster`
  * [`gcloud dataproc workflow-templates set-cluster-selector`](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors#add_a_cluster_selector_to_a_template)

to an existing workflow template. 

### REST API

To make an update to a template with the REST API:

  1. Call [workflowTemplates.get](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/get), which returns the current template with the `version` field filled in with the current server version.
  2. Make updates to the fetched template.
  3. Call [workflowTemplates.update](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/update) with the updated template.

As a guard against concurrent modifications, a request to update a template must specify the current server version in the `workflowTemplate.version` field.

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

## Delete a workflow template

### gcloud CLI
    
    
    gcloud dataproc workflow-templates delete TEMPLATE_ID \
        --region=REGION
    

**Note:** The operation-id that is returned when you instantiate the workflow with `gcloud dataproc workflow-templates instantiate` (see Run a workflow).

### REST API

See [workflowTemplates.delete](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/delete). 

### Console

You can view existing workflow templates and instantiated workflows from the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/instances) page in Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
