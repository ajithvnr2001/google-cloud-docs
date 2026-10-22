---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates/
title: Running classic templates \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:26.137653+00:00
---

# Running classic templates  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Running classic templates Stay organized with collections  Save and categorize content based on your preferences. 

After you create and stage your Dataflow template, run the template with the Google Cloud console, REST API, or the Google Cloud CLI. You can deploy Dataflow template jobs from many environments, including App Engine standard environment, Cloud Run functions, and other constrained environments.

**Note:** In addition to the template file, templated pipelines rely on files that were staged and referenced at the time of template creation. If you move or remove the staged files, your pipeline job will fail.

## Use the Google Cloud console

You can use the Google Cloud console to run Google-provided and custom Dataflow templates.

### Google-provided templates

To run a Google-provided template:

  1. Go to the Dataflow page in the Google Cloud console.
[Go to the Dataflow page](https://console.cloud.google.com/dataflow)
  2. Click _add_box_**CREATE JOB FROM TEMPLATE**. 
![Google Cloud console Create Job From Template Button](https://docs.cloud.google.com/static/dataflow/images/console_run_job_button.png)
  3. Select the Google-provided template that you want to run from the **Dataflow template** drop-down menu.
![WordCount Template Execution Form](https://docs.cloud.google.com/static/dataflow/images/wordcount_template_execute.png)
  4. Enter a job name in the **Job Name** field.
  5. Enter your parameter values in the provided parameter fields. You don't need the **Additional Parameters** section when you use a Google-provided template.
  6. Click **Run Job**.



### Custom templates

To run a custom template:

  1. Go to the Dataflow page in the Google Cloud console.
[Go to the Dataflow page](https://console.cloud.google.com/dataflow)
  2. Click **CREATE JOB FROM TEMPLATE**.
![Google Cloud console Create Job From Template Button](https://docs.cloud.google.com/static/dataflow/images/console_run_job_button.png)
  3. Select **Custom Template** from the **Dataflow template** drop-down menu.
![Custom Template Execution Form](https://docs.cloud.google.com/static/dataflow/images/custom_template_execute.png)
  4. Enter a job name in the **Job Name** field.
  5. Enter the Cloud Storage path to your template file in the template Cloud Storage path field.
  6. If your template needs parameters, click _add_**ADD PARAMETER** in the **Additional parameters** section. Enter in the **Name** and **Value** of the parameter. Repeat this step for each needed parameter.
  7. Click **Run Job**.



## Use the REST API

To run a template with a [REST API request](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch), send an HTTP POST request with your project ID. This request requires [authorization](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch#authorization-scopes). 

See the REST API reference for [projects.locations.templates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch) to learn more about the available parameters.

In the JSON request body, set [runtime environment values](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/RuntimeEnvironment) in the `environment` property, not the `parameters` property. The `environment` property defines the runtime environment for the job.

### Create a custom template batch job

This example [projects.locations.templates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch) request creates a batch job from a template that reads a text file and writes an output text file. If the request is successful, the response body contains an instance of [LaunchTemplateResponse](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/LaunchTemplateResponse).

Modify the following values:

  * Replace `YOUR_PROJECT_ID` with your project ID.
  * Replace `LOCATION` with the Dataflow [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) of your choice.
  * Replace `JOB_NAME` with a job name of your choice.
  * Replace `YOUR_BUCKET_NAME` with the name of your Cloud Storage bucket.
  * Set `gcsPath` to the Cloud Storage location of the template file.
  * Set `parameters` to your list of key-value pairs.
  * Set `tempLocation` to a location where you have write permission. This value is required to run Google-provided templates.


    
    
        POST https://dataflow.googleapis.com/v1b3/projects/YOUR_PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=gs://YOUR_BUCKET_NAME/templates/TemplateName
        {
            "jobName": "JOB_NAME",
            "parameters": {
                "inputFile" : "gs://YOUR_BUCKET_NAME/input/my_input.txt",
                "output": "gs://YOUR_BUCKET_NAME/output/my_output"
            },
            "environment": {
                "tempLocation": "gs://YOUR_BUCKET_NAME/temp",
                "zone": "us-central1-f"
            }
        }
    

### Create a custom template streaming job

This example [projects.locations.templates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch) request creates a streaming job from a classic template that reads from a Pub/Sub subscription and writes to a BigQuery table. If you want to launch a Flex Template, use [projects.locations.flexTemplates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch) instead. The [example template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-subscription-to-bigquery) is a Google-provided template. You can modify the path in the template to point to a custom template. The same logic is used to launch Google-provided and custom templates. In this example, the BigQuery table must already exist with the appropriate schema. If successful, the response body contains an instance of [LaunchTemplateResponse](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/LaunchTemplateResponse).

Modify the following values:

  * Replace `YOUR_PROJECT_ID` with your project ID.
  * Replace `LOCATION` with the Dataflow [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) of your choice.
  * Replace `JOB_NAME` with a job name of your choice.
  * Replace `YOUR_BUCKET_NAME` with the name of your Cloud Storage bucket.
  * Replace `GCS_PATH` with the Cloud Storage location of the template file. The location should start with gs://
  * Set `parameters` to your list of key-value pairs. The parameters listed are specific to this template example. If you're using a custom template, modify the parameters as needed. If you're using the example template, replace the following variables. 
    * Replace `YOUR_SUBSCRIPTION_NAME` with your Pub/Sub subscription name.
    * Replace `YOUR_DATASET` with your BigQuery dataset, and replace `YOUR_TABLE_NAME` with your BigQuery table name.
  * Set `tempLocation` to a location where you have write permission. This value is required to run Google-provided templates.


    
    
        POST https://dataflow.googleapis.com/v1b3/projects/YOUR_PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=GCS_PATH
        {
            "jobName": "JOB_NAME",
            "parameters": {
                "inputSubscription": "projects/YOUR_PROJECT_ID/subscriptions/YOUR_SUBSCRIPTION_NAME",
                "outputTableSpec": "YOUR_PROJECT_ID:YOUR_DATASET.YOUR_TABLE_NAME"
            },
            "environment": {
                "tempLocation": "gs://YOUR_BUCKET_NAME/temp",
                "zone": "us-central1-f"
            }
        }
    

### Update a custom template streaming job

This example [projects.locations.templates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch) request shows you how to update a template streaming job. If you want to update a Flex Template, use [projects.locations.flexTemplates.launch](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch) instead. 

  1. Run [Example 2: Creating a custom template streaming job](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates#example-2-custom-template-streaming-job) to start a streaming template job.
  2. Send the following HTTP POST request, with the following modified values: 
     * Replace `YOUR_PROJECT_ID` with your project ID.
     * Replace `LOCATION` with the Dataflow [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) of the job that you're updating.
     * Replace `JOB_NAME` with the exact name of the job that you want to update.
     * Replace `GCS_PATH` with the Cloud Storage location of the template file. The location should start with gs://
     * Set `parameters` to your list of key-value pairs. The parameters listed are specific to this template example. If you're using a custom template, modify the parameters as needed. If you're using the example template, replace the following variables. 
       * Replace `YOUR_SUBSCRIPTION_NAME` with your Pub/Sub subscription name.
       * Replace `YOUR_DATASET` with your BigQuery dataset, and replace `YOUR_TABLE_NAME` with your BigQuery table name.
     * Use the `environment` parameter to change environment settings, such as the machine type. This example uses the n2-highmem-2 machine type, which has more memory and CPU per worker than the default machine type.
    
    POST https://dataflow.googleapis.com/v1b3/projects/YOUR_PROJECT_ID/locations/LOCATION/templates:launch?gcsPath=GCS_PATH
        {
            "jobName": "JOB_NAME",
            "parameters": {
                "inputSubscription": "projects/YOUR_PROJECT_ID/subscriptions/YOUR_TOPIC_NAME",
                "outputTableSpec": "YOUR_PROJECT_ID:YOUR_DATASET.YOUR_TABLE_NAME"
            },
            "environment": {
                "machineType": "n2-highmem-2"
            },
            "update": true
        }
    

  3. Access the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/jobs-list) and verify that a new job with the same name was created. This job has the status **Updated**. 



### Use the Google API Client Libraries

Consider using the [Google API Client Libraries](https://developers.google.com/api-client-library/) to easily make calls to the Dataflow REST APIs. This sample script uses the [Google API Client Library for Python](https://developers.google.com/api-client-library/python/).

In this example, you must set the following variables:

  * `project`: Set to your project ID.
  * `job`: Set to a unique job name of your choice.
  * `template`: Set to the Cloud Storage location of the template file.
  * `parameters`: Set to a dictionary with the template parameters.



To set the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations), include the [`location`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch#path-parameters) parameter.
    
    
    from googleapiclient.discovery import build
    
    # project = 'your-gcp-project'
    # job = 'unique-job-name'
    # template = 'gs://dataflow-templates/latest/Word_Count'
    # parameters = {
    #     'inputFile': 'gs://dataflow-samples/shakespeare/kinglear.txt',
    #     'output': 'gs://<your-gcs-bucket>/wordcount/outputs',
    # }
    
    dataflow = build("dataflow", "v1b3")
    request = (
        dataflow.projects()
        .templates()
        .launch(
            projectId=project,
            gcsPath=template,
            body={
                "jobName": job,
                "parameters": parameters,
            },
        )
    )
    
    response = request.execute()

For more information about the available options, see the [`projects.locations.templates.launch` method](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates/launch) in the Dataflow REST API reference.

## Use gcloud CLI

**Note:** To use the gcloud CLI to run templates, you must have [Cloud SDK](https://docs.cloud.google.com/sdk/downloads) version 138.0.0 or higher.

The gcloud CLI can run either a custom or a [Google-provided](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates) template using the `gcloud dataflow jobs run` command. Examples of running Google-provided templates are documented in the [Google-provided templates page](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates). 

For the following custom template examples, set the following values:

  * Replace `JOB_NAME` with a job name of your choice.
  * Replace `YOUR_BUCKET_NAME` with the name of your Cloud Storage bucket.
  * Set `--gcs-location` to the Cloud Storage location of the template file. 
  * Set `--parameters` to the comma-separated list of parameters to pass to the job. Spaces between commas and values are not allowed.
  * To prevent VMs from accepting SSH keys that are stored in project metadata, use the `additional-experiments` flag with the [`block_project_ssh_keys`](https://docs.cloud.google.com/dataflow/docs/reference/service-options) service option: `--additional-experiments=block_project_ssh_keys`.



### Create a custom template batch job

This example creates a batch job from a template that reads a text file and writes an output text file.
    
    
        gcloud dataflow jobs run JOB_NAME \
            --gcs-location gs://YOUR_BUCKET_NAME/templates/MyTemplate \
            --parameters inputFile=gs://YOUR_BUCKET_NAME/input/my_input.txt,output=gs://YOUR_BUCKET_NAME/output/my_output
    

The request returns a response with the following format.
    
    
        id: 2016-10-11_17_10_59-1234530157620696789
        projectId: YOUR_PROJECT_ID
        type: JOB_TYPE_BATCH
    

### Create a custom template streaming job

This example creates a streaming job from a template that reads from a Pub/Sub topic and writes to a BigQuery table. The BigQuery table must already exist with the appropriate schema.
    
    
        gcloud dataflow jobs run JOB_NAME \
            --gcs-location gs://YOUR_BUCKET_NAME/templates/MyTemplate \
            --parameters topic=projects/project-identifier/topics/resource-name,table=my_project:my_dataset.my_table_name
    

The request returns a response with the following format.
    
    
        id: 2016-10-11_17_10_59-1234530157620696789
        projectId: YOUR_PROJECT_ID
        type: JOB_TYPE_STREAMING
    

For a complete list of flags for the `gcloud dataflow jobs run` command, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run).

## Monitoring and Troubleshooting

The [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf) lets you to monitor your Dataflow jobs. If a job fails, you can find troubleshooting tips, debugging strategies, and a catalog of common errors in the [Troubleshooting Your Pipeline](https://docs.cloud.google.com/dataflow/pipelines/troubleshooting-your-pipeline) guide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
