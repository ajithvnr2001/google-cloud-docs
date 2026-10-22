---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/run-flex-templates/
title: Run Flex Templates in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:16.682176+00:00
---

# Run Flex Templates in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/run-flex-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Run Flex Templates in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to run a Dataflow job by using a Flex Template. Flex Templates let you package a Dataflow pipeline so that you can run the pipeline without having an Apache Beam development environment.

## Required permissions

When you run a Flex Template, Dataflow creates a job for you. To create the job, the Dataflow service account needs the following permission:

  * `dataflow.serviceAgent`



When you first use Dataflow, the service assigns this role for you, so you don't need to grant this permission.

By default, the Compute Engine service account is used for launcher VMs and worker VMs. The service account needs the following roles and abilities:

  * Storage Object Admin (`roles/storage.objectAdmin`)
  * Viewer (`roles/viewer`)
  * Dataflow Worker (`roles/dataflow.worker`)
  * Read and write access to the staging bucket
  * Read access to the Flex Template image



To grant read and write access to the staging bucket, you can use the role Storage Object Admin (`roles/storage.objectAdmin`). For more information, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

To grant read access to the Flex Template image, you can use the role Storage Object Viewer (`roles/storage.objectViewer`). For more information, see [Configuring access control](https://docs.cloud.google.com/artifact-registry/docs/access-control).

## Run a Flex Template

To run a Flex Template, use the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command:
    
    
    gcloud dataflow flex-template run JOB_ID \
      --template-file-gcs-location gs://TEMPLATE_FILE_LOCATION \
      --region REGION \
      --staging-location STAGING_LOCATION \
      --temp-location TEMP_LOCATION \
      --parameters  PARAMETERS \
      --additional-user-labels LABELS \

Replace the following:

  * `JOB_ID`: the ID for your job

  * `TEMPLATE_FILE_LOCATION`: the Cloud Storage location of the template file

  * `REGION`: the region in which to run the Dataflow job

  * `STAGING_LOCATION`: the Cloud Storage location to stage local files

  * `TEMP_LOCATION`: the Cloud Storage location to write temporary files. If not set, defaults to the staging location.

  * `PARAMETERS`: pipeline parameters for the job

  * `LABELS`: Optional. Labels attached to your job, using the format `KEY_1=VALUE_1,KEY_2=VALUE_2,...`.




During the staging step of launching a template, Dataflow writes files to the staging location. Dataflow reads these staged files to create the job graph. During the execution step, Dataflow writes files to the temporary location.

## Set pipeline options

To set pipeline options when you run a Flex Template, use the following flags in the `gcloud dataflow flex-template run` command:

  * [`parameters`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--parameters): Use this flag to set the following types of pipeline option:

    * Pipeline options supported by Flex Templates. For a list of which options are supported by Flex Templates, see [Pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options).

    * Pipeline options declared in [template metadata](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#metadata).

  * [`additional-pipeline-options`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-pipeline-options): Use this flag to set other Apache Beam pipeline options that are not directly supported by Flex Templates.

  * [`additional-experiments`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-experiments): Use this flag to set [experimental pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental) (equivalent to the `experiments` option).




### gcloud

  * Include pipeline options by using the [`parameters`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--parameters) flag.

  * Include runtime experiments and pipeline options by using the [`additional-experiments`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-experiments) and [`additional-pipeline-options`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--additional-pipeline-options) flags.




When passing parameters or options that contain commas, or when passing parameters of `List` or `Map` type, you might need to do one of the following:

  * Use the [`gcloud topic escaping`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) syntax to change delimiters.
  * Define parameters in a YAML file and use the [`flags-file`](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file) flag.
  * Supply multiple `--additional-pipeline-options` or `--additional-experiments` flags with the appropriate option, such as resource hints.



### API

  * Include pipeline options by using the [`parameters`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch#launchflextemplateparameter) field.

  * Include runtime experiments and pipeline options by using the [`additionalExperiments` and `additionalPipelineOptions`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch#flextemplateruntimeenvironment) fields.




The following example shows how to include pipeline options, experiments, and additional options in a request body:

**Note:** For Beam SDK versions 2.74 and later, use `"additionalExperiments": [ "enable_portable_runner" ]` in the `environment` object.
    
    
    {
      "jobName": "my-flex-template-job",
      "parameters": {
        "option_defined_in_metadata": "value"
      },
      "environment": {
        "additionalExperiments": [
          "use_runner_v2"
        ],
        "additionalPipelineOptions": {
          "common_pipeline_option": "value"
        }
      }
    }
    

When using Flex Templates, you can configure some pipeline options during pipeline initialization, but other pipeline options can't be changed. If the command line arguments required by the Flex Template are overwritten, the job might ignore, override, or discard the pipeline options passed by the template launcher. The job might fail to launch, or a job that doesn't use the Flex Template might launch. For more information, see [Failed to read the job file](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates#read-job-file).

During pipeline initialization, don't change the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options):

### Java

  * `runner`
  * `project`
  * `jobName`
  * `templateLocation`
  * `region`



### Python

  * `runner`
  * `project`
  * `job_name`
  * `template_location`
  * `region`



### Go

  * `runner`
  * `project`
  * `job_name`
  * `template_location`
  * `region`



## Block project SSH keys from VMs that use metadata-based SSH keys

You can prevent VMs from accepting SSH keys that are stored in project metadata by blocking project SSH keys from VMs. Use the `additional-experiments` flag with the `block_project_ssh_keys` service option:
    
    
    --additional-experiments=block_project_ssh_keys
    

For more information, see [Dataflow service options](https://docs.cloud.google.com/dataflow/docs/reference/service-options).

## Update a Flex Template job

The following example request shows you how to update a template streaming job by using the [projects.locations.flexTemplates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch) method. If you want to use the gcloud CLI, see [Update an existing pipeline](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline).

If you want to update a classic template, use [projects.locations.templates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch) instead.

  1. Follow the steps to create a streaming job from a Flex Template. Send the following HTTP POST request with the modified values:
         
         POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/flexTemplates:launch
         {
             "launchParameter": {
               "update": true
               "jobName": "JOB_NAME",
               "parameters": {
                 "input_subscription": "projects/PROJECT_ID/subscriptions/SUBSCRIPTION_NAME",
                 "output_table": "PROJECT_ID:DATASET.TABLE_NAME"
               },
             "containerSpecGcsPath": "STORAGE_PATH"
             },
         }
         

     * Replace `PROJECT_ID` with your project ID.
     * Replace `REGION` with the Dataflow [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) of the job that you're updating.
     * Replace `JOB_NAME` with the exact name of the job that you want to update.
     * Set `parameters` to your list of key-value pairs. The parameters listed are specific to this template example. If you're using a custom template, modify the parameters as needed. If you're using the example template, replace the following variables. 
       * Replace `SUBSCRIPTION_NAME` with your Pub/Sub subscription name.
       * Replace `DATASET` with your with your BigQuery dataset name.
       * Replace `TABLE_NAME` with your with your BigQuery table name.
     * Replace `STORAGE_PATH` with the Cloud Storage location of the template file. The location should start with `gs://`.
  2. Use the `environment` parameter to change environment settings. For more information, see [`FlexTemplateRuntimeEnvironment`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch#FlexTemplateRuntimeEnvironment).

  3. Optional: To send your request using curl (Linux, macOS, or Cloud Shell), save the request to a JSON file, and then run the following command:
         
         curl -X POST -d "@FILE_PATH" -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)"  https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/flexTemplates:launch
         

Replace FILE_PATH with the path to the JSON file that contains the request body.

  4. Use the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/jobs-list) to verify that a new job with the same name was created. This job has the status **Updated**.




## What's next

  * Learn how to [build a Flex Template for your Apache Beam pipeline](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates).
  * To know more about Classic Templates, Flex Templates, and their use-case scenarios, see [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * For Flex Templates troubleshooting information, see [Troubleshoot Flex Template timeouts](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
