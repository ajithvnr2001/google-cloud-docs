---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/run-pipeline/
title: Run a pipeline \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:04.077534+00:00
---

# Run a pipeline  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/run-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Run a pipeline Stay organized with collections  Save and categorize content based on your preferences. 

Agent Platform Pipelines lets you run machine learning (ML) pipelines that were built using the Kubeflow Pipelines SDK or TensorFlow Extended in a serverless manner. This document describes how to run an ML pipeline.

You can also create pipeline runs using prebuilt templates in the **Template Gallery**. For more information about the **Template Gallery** , see [Use a prebuilt template from the Template Gallery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/use-template-gallery).

You can use Gemini Enterprise Agent Platform Experiments to track, analyze, and compare your pipeline runs by [associating the pipeline runs with an experiment or an experiment run](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/add-pipelinerun-experiment). By comparing the parameters, outputs, and performance metrics of the pipeline runs, you can identify the pipeline configuration that works best for your use case. For more information, see [Introduction to Gemini Enterprise Agent Platform Experiments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments).

## Before you begin

Before you run a pipeline with Agent Platform Pipelines, use the following instructions to set up your Google Cloud project and development environment:

  1. [Build a pipeline.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/build-pipeline)

  2. To run a pipeline using the Agent Platform SDK for Python, install the Vertex SDK.

     * Install the [Agent Platform SDK](https://github.com/googleapis/python-aiplatform).



## Create a pipeline run

Use the following instructions to run an ML pipeline using Google Cloud console or Python.

### Console

Use the following instructions to run an ML pipeline using Google Cloud console.

  1. In the Google Cloud console, in the **Agent Platform** section, go to the **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/agent-platform/pipelines)

  2. In the **Region** drop-down list, select the region to create the pipeline run.

  3. Click **add_box Create run** to open the **Create pipeline run** pane.

  4. In the **Run details** section, do the following:

     1. Click a **Run source**. The following options are available:

        * **Select from existing pipelines** : To create a pipeline run based on an existing pipeline template, click **Select from existing pipelines** and enter the following details:

          1. Select the **Repository** containing the pipeline or component definition file.

          2. Select the **Pipeline or component** and **Version**.

          3. Specify a **Run name** to uniquely identify the pipeline run.

        * **Select a Template Gallery pipeline** : To create a pipeline run based on a Google-authored pipeline template from the **Template Gallery** , click **Select a Template Gallery pipeline** and enter the following details:

          1. In the **Template Gallery pipeline** list, select the pipeline template.

          2. Optional: Modify the default **Run name** that uniquely identifies the pipeline run.

**Note:** These instructions describe how to create a pipeline run using the default interface of the **Create pipeline run** page, which includes the **Run details** and the **Runtime configuration** sections. For some templates from the **Template gallery** , this page has additional sections. For example, the **AutoML for Tabular Classification / Regression** template also includes the **Training Method** , **Training options** , and **Compute and pricing** sections.
        * **Upload file** : To upload a compiled pipeline definition, click **Upload file** and enter the following details:

          1. Click **Browse** to open the file selector. Navigate to the compiled pipeline YAML file that you want to run, select the pipeline, and click **Open**.

          2. The **Pipeline or component name** shows the name specified in the pipeline definition, by default. Optionally, specify a different Pipeline name.

          3. Specify a **Run name** to uniquely identify the pipeline run.

        * **Import from Cloud Storage** : To import a pipeline definition file from Cloud Storage, click **Import from Cloud Storage** and enter the following details:

          1. Click **Browse** to navigate to the Cloud Storage bucket containing the pipeline definition object, select the file, and then click **Select**.

Alternatively, enter the Cloud Storage URI or the HTTP/HTTPS URL of the pipeline definition file.

          2. Specify the **Pipeline or component name**.

          3. Specify a **Run name** to uniquely identify the pipeline run.

     2. Optional: To schedule recurring pipeline runs, specify the **Run schedule** , as follows:

        1. Select **Recurring**.

        2. Under **Start time** , specify when the schedule becomes active.

           * To schedule the first run to occur immediately after schedule creation, select **Immediately**.

           * To schedule the first run to occur at a specific time and date, select **On**.

        3. In the **Frequency** field, specify the frequency to schedule and execute the pipeline runs, using a cron schedule expression based on [unix-cron](https://man7.org/linux/man-pages/man5/crontab.5.html).

        4. Under **Ends** , specify when the schedule ends.

           * To indicate that the schedule creates pipeline runs indefinitely, select **Never**.

           * To indicate that the schedule ends on a specific date and time, select **On** , and specify the end date and time for the schedule.

        5. Optional: To specify that the pipeline run uses a custom service account, a customer-managed encryption key (CMEK), or a peered VPC network, click **Advanced options** , and then follow these instructions:

           * To specify a service account, select a service account from the **Service account** drop-down list.

If you don't specify a service account, Agent Platform Pipelines runs your pipeline using the default Compute Engine service account.

Learn more about [configuring a service account for use with Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-project#service-account).

           * To use a CMEK, select **Use a customer-managed encryption key**. The **Select a customer-managed key** drop-down list appears. In the **Select a customer-managed key** drop-down list, select the key that you want to use.

           * To use a peered VPC network in this pipeline run, enter the VPC network name in the **Peered VPC network** box.

     3. Click **Continue**.

  5. In the **Runtime configuration** section, configure the pipeline run, as follows:

     1. Under **Cloud storage location** , click **Browse** to select the Cloud Storage bucket for storing the pipeline output artifacts, and then click **Select**.

     2. Optional: To configure the failure policy and the cache for the pipeline run, click **Advanced options** , and then use the following instructions:

        * Under **Failure policy** , specify the failure policy for the entire pipeline. [Learn more about pipeline failure policies.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-failure-policy)

          * To configure the pipeline to continue scheduling tasks after one task fails, select **Run all steps to completion**. This option is selected, by default.

          * To configure the pipeline to fail after one task fails, select **Fail this run as soon as one step fails**.

        * Under **Caching configuration** , specify the cache configuration for the entire pipeline.

          * To use the task-level cache configuration for task in the pipeline, select **Do not override task-level cache configuration**.

          * To turn on caching for all the tasks in the pipeline and override any task-level cache configuration, select **Enable read from cache for all steps (fastest)**.

          * To turn off caching for all the tasks in the pipeline and override any task-level cache configuration, select **Disable read from cache for all steps (fastest)**.

     3. Optional: If your pipeline has parameters, under **Pipeline parameters** , specify your pipeline run parameters.

  6. To create your pipeline run, click **Submit**.




###  Python 

Use the following instructions to run an ML pipeline using the Agent Platform SDK for Python. Before you run the following code sample, you must set up authentication.

### Set up authentication

To set up authentication, you must create a service account key, and set an environment variable for the path to the service account key.

  1. Create a service account: 

     1. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. In the **Service account name** field, enter a name.
     3. Optional: In the **Service account description** field, enter a description.
     4. Click **Create**.
     5. Click the **Select a role** field. Under **All roles** , select **Gemini Enterprise Agent Platform** > **Agent Platform User**.
**Note** : The roles you select allow your service account to access resources. You can view and change these roles later by using the [Google Cloud console](https://console.cloud.google.com/). For more information, see [access control for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#predefined_roles). 
  2. Click **Done** to create the service account. 

Do not close your browser window. You will use it in the next step. 



* Create a service account key for authentication: 

  1. In the Google Cloud console, click the email address for the service account that you created.
  2. Click **Keys**.
  3. Click **Add key** , then **Create new key**.
  4. Click **Create**. A JSON key file is downloaded to your computer.
  5. Click **Close**.


* Grant your new service account access to the service account that you use to run pipelines. 

  1. Click arrow_back to return to the list of service accounts.
  2. Click the name of the service account that you use to run pipelines. The **Service account details** page appears.

If you followed the instructions in the guide to configuring your project for Gemini Enterprise Agent Platform Pipelines, this is the same service account that you created in the [Configure a service account with granular permissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-project#service-account) section. Otherwise, Gemini Enterprise Agent Platform uses the Compute Engine default service account to run pipelines. The Compute Engine default service account is named like the following: `PROJECT_NUMBER-compute@developer.gserviceaccount.com`

  3. Click the **Permissions** tab.
  4. Click **Grant access**. The **Add principals** panel appears.
  5. In the **New principals** box, enter the email address for the service account you created in a previous step.
  6. In the **Role** drop-down list, select **Service accounts** > **Service account user**.
  7. Click **Save**


* Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON file that contains your service account key. This variable only applies to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS

Replace [PATH] with the path of the JSON file that contains your service account key. 
    
    
    export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

For example:
    
    
    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

Replace [PATH] with the path of the JSON file that contains your service account key, and [FILE_NAME] with the filename. 

With PowerShell:
    
    
    $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

For example:
    
    
    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\[FILE_NAME].json"

With command prompt:
    
    
    set GOOGLE_APPLICATION_CREDENTIALS=[PATH]

### Run a pipeline

Running a Gemini Enterprise Agent Platform `PipelineJob` requires you to create a [`PipelineJob`](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob) resource and then invoke the `submit` method.

#### Special input types supported by KFP

While creating a pipeline run, you can also pass the following placeholders supported by the KFP SDK as inputs:

  * `{{$.pipeline_job_name_placeholder}}`

  * `{{$.pipeline_job_resource_name_placeholder}}`

  * `{{$.pipeline_job_id_placeholder}}`

  * `{{$.pipeline_task_name_placeholder}}`

  * `{{$.pipeline_task_id_placeholder}}`

  * `{{$.pipeline_job_create_time_utc_placeholder}}`

  * `{{$.pipeline_root_placeholder}}`




For more information, see [Special input types](https://www.kubeflow.org/docs/components/pipelines/v2/pipelines/pipeline-basics/#special-input-types) in the [Kubeflow Pipelines v2 documentation](https://www.kubeflow.org/docs/components/pipelines/v2/introduction/).
    
    
    from google.cloud import aiplatform
    job = aiplatform.PipelineJob(display_name = DISPLAY_NAME,
                                 template_path = COMPILED_PIPELINE_PATH,
                                 job_id = JOB_ID,
                                 pipeline_root = PIPELINE_ROOT_PATH,
                                 parameter_values = PIPELINE_PARAMETERS,
                                 enable_caching = ENABLE_CACHING,
                                 encryption_spec_key_name = CMEK,
                                 labels = LABELS,
                                 credentials = CREDENTIALS,
                                 project = PROJECT_ID,
                                 location = LOCATION,
                                 failure_policy = FAILURE_POLICY)
    job.submit(service_account=SERVICE_ACCOUNT,
               network=NETWORK,
               reserved_ip_ranges=RESERVED_IP_RANGES)

Replace the following:

  * DISPLAY_NAME: The name of the pipeline, this will show up in the Google Cloud console.
  * COMPILED_PIPELINE_PATH: The path to your compiled pipeline YAML file. It can be a Cloud Storage URI, a HTTP/HTTPS URL, or a local path.  


Optional: To specify a particular version of a compiled pipeline, include the version tag in any one of the following formats:

    * `COMPILED_PIPELINE_PATH:TAG`, where TAG is the version tag.

    * `COMPILED_PIPELINE_PATH@SHA256_TAG`, where SHA256_TAG is the `sha256` hash value of the pipeline version.

  * JOB_ID: (_optional_) A unique identifier for this pipeline run. If the job ID is not specified, Agent Platform Pipelines creates a job ID for you using the pipeline name and the timestamp of when the pipeline run was started.

  * PIPELINE_ROOT_PATH: (_optional_) To override the pipeline root path specified in the pipeline definition, specify a path that your pipeline job can access, such as a Cloud Storage bucket URI.

  * PIPELINE_PARAMETERS: (_optional_) The pipeline parameters to pass to this run. For example, create a `dict()` with the parameter names as the dictionary keys and the parameter values as the dictionary values.

  * ENABLE_CACHING: (_optional_) Specifies if this pipeline run uses execution caching. Execution caching reduces costs by skipping pipeline tasks where the output is known for the current set of inputs. If the enable caching argument is not specified, execution caching is used in this pipeline run. [Learn more about execution caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/build-pipeline#caching).

  * CMEK: (_optional_) The name of the customer-managed encryption key that you want to use for this pipeline run.

  * LABELS: (_optional_) The user defined labels to organize this `PipelineJob`. For more information about resource labels, see [Creating and managing labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) in the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs).

Agent Platform Pipelines automatically attaches the following label to your pipeline run:

`vertex-ai-pipelines-run-billing-id: pipeline_run_id`

where `pipeline_run_id` is the unique ID of the pipeline run.

This label connects the usage of Google Cloud resources generated by the pipeline run in billing reports.

  * CREDENTIALS: (_optional_) Custom credentials to use to create this `PipelineJob`. Overrides credentials set in `aiplatform.init`.

  * PROJECT_ID: (_optional_) The Google Cloud project that you want to run the pipeline in. If you don't set this parameter, the project set in `aiplatform.init` is used.

  * LOCATION: (_optional_) The region that you want to run the pipeline in. For more information about the regions that Agent Platform Pipelines is available in, see the [Gemini Enterprise Agent Platform locations guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#feature-availability). If you don't set this parameter, the default location set in `aiplatform.init` is used.

  * FAILURE_POLICY: (_optional_) Specify the failure policy for the entire pipeline. The following configurations are available:

    * To configure the pipeline to fail after one task fails, enter `fast`.

    * To configure the pipeline to continue scheduling tasks after one task fails, enter `slow`.

If you don't set this parameter, the failure policy configuration is set to `slow`, by default. [Learn more about pipeline failure policies.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-failure-policy)

  * SERVICE_ACCOUNT: (_optional_) The name of the service account to use for this pipeline run. If you don't specify a service account, Agent Platform Pipelines runs your pipeline using the default Compute Engine service account.

  * NETWORK: (_optional_) :The name of the VPC peered network to use for this pipeline run.

  * RESERVED_IP_RANGES: Optional. A list of names for the reserved IP ranges in the VPC network used for the workload of the pipeline run, for example: `['vertex-ai-ip-range']`.




## What's next

  * Learn how to [create and pipeline run and add it to an experiment or an experiment run](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/add-pipelinerun-experiment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
