---
url: https://docs.cloud.google.com/colab/docs/schedule-notebook-run/
title: Schedule a notebook run in Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:21.272553+00:00
---

# Schedule a notebook run in Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/schedule-notebook-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schedule a notebook run

This page shows you how to schedule a notebook run in Colab Enterprise.

## Overview

You can schedule a notebook to run immediately one time, or on a recurring schedule.

When you schedule the notebook run, you select a runtime template. Colab Enterprise uses this runtime template to create the runtime that runs your notebook.

The runtime needs specific permissions to run the notebook's code and access Google Cloud services and APIs.

  * If your runtime template configuration has end-user credentials enabled, then the runtime uses the permissions associated with your user credentials.

  * If end-user credentials aren't enabled, you must specify a service account when you schedule the notebook run. Colab Enterprise uses this service account's credentials to run your notebook.




For more information, see Required roles for running the notebook.

After Colab Enterprise completes the notebook run, the results are stored in a shareable Cloud Storage bucket.

## Limitations

Colab Enterprise runtimes use Compute Engine quota. See the Compute Engine [Allocation quotas page](https://docs.cloud.google.com/compute/resource-usage).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs. 

**Roles required to enable APIs**

To enable APIs, you need the Service Usage Admin IAM role (`roles/serviceusage.serviceUsageAdmin`), which contains the `serviceusage.services.enable` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs. 

**Roles required to enable APIs**

To enable APIs, you need the Service Usage Admin IAM role (`roles/serviceusage.serviceUsageAdmin`), which contains the `serviceusage.services.enable` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles for scheduling the notebook run

To get the permissions that you need to schedule a notebook run in Colab Enterprise, ask your administrator to grant you the following IAM roles on the project: 

  * [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

### Required roles for running the notebook

The principal that runs the notebook needs specific permissions. The principal is either your user account or a service account that you specify, as described in the overview.

To get the permissions that you need to run a notebook in Colab Enterprise, ask your administrator to grant you the following IAM roles: 

  * [Code Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeViewer) (`roles/dataform.codeViewer`) on the notebook
  * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project
  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on the project
  * [Storage Legacy Bucket Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`) on the notebook
  * [Storage Legacy Object Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectReader) (`roles/storage.legacyObjectReader`) on the output bucket



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to run a notebook in Colab Enterprise. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to run a notebook in Colab Enterprise:

  * `dataform.locations.list` on the notebook
  * `dataform.repositories.computeAccessTokenStatus` on the notebook
  * `dataform.repositories.fetchHistory` on the notebook
  * `dataform.repositories.fetchRemoteBranches` on the notebook
  * `dataform.repositories.get` on the notebook
  * `dataform.repositories.getIamPolicy` on the notebook
  * `dataform.repositories.list` on the notebook
  * `dataform.repositories.queryDirectoryContents` on the notebook
  * `dataform.repositories.readFile` on the notebook
  * `logging.logEntries.create` on the project
  * `logging.logEntries.route` on the project
  * `monitoring.metricDescriptors.create` on the project
  * `monitoring.metricDescriptors.get` on the project
  * `monitoring.metricDescriptors.list` on the project
  * `monitoring.monitoredResourceDescriptors.get` on the project
  * `monitoring.monitoredResourceDescriptors.list` on the project
  * `monitoring.timeSeries.create` on the project
  * `resourcemanager.projects.get` on the project
  * `resourcemanager.projects.list` on the project
  * `storage.buckets.get` on the notebook
  * `storage.managedFolders.create` on the notebook
  * `storage.managedFolders.delete` on the notebook
  * `storage.managedFolders.get` on the notebook
  * `storage.managedFolders.list` on the notebook
  * `storage.multipartUploads.abort` on the notebook
  * `storage.multipartUploads.create` on the notebook
  * `storage.multipartUploads.list` on the notebook
  * `storage.multipartUploads.listParts` on the notebook
  * `storage.objects.create` on the notebook
  * `storage.objects.delete` on the notebook
  * `storage.objects.get` on the notebook
  * `storage.objects.list` on the notebook
  * `storage.objects.restore` on the notebook
  * `storage.objects.setRetention` on the notebook



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

### Use scheduled notebook runs in a Shared VPC network

To use scheduled notebook runs in a Shared VPC network, you must grant additional permissions. See [Use Colab Enterprise in a Shared VPC network](https://docs.cloud.google.com/colab/docs/create-runtime-template#shared-vpc).

## Run a notebook once

To run a notebook one time, you can use the Google Cloud console, the Google Cloud CLI, the Agent Platform Python client library, or Terraform.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Next to a notebook, click the more_vert**Notebook actions** menu and select **Schedule**. 

  4. In the **Schedule name** field, enter a name for your schedule. 

  5. Click the **Runtime template** list, and select a runtime template. The runtime template determines the specifications of the runtime that runs your notebook. 

  6. Under **Run schedule** , select **One-off** to run your notebook as soon as you submit the notebook run. 

  7. Next to the **Cloud Storage output location** field, click **Browse** to open the **Select folder** dialog. 

  8. Select a Cloud Storage bucket. Or, to create a bucket, click ![](https://docs.cloud.google.com/static/colab/images/icon-create-bucket.png) **Create new bucket** and complete the dialog. 

  9. If you selected a runtime template without end-user credentials enabled, the dialog includes a **Service account** field. In the **Service account** field, enter a service account's email address. 

  10. Click **Submit**.

The notebook run starts immediately. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * `DISPLAY_NAME`: the display name for your notebook run.
  * `NOTEBOOK_RUNTIME_TEMPLATE`: the notebook runtime template that specifies your runtime's compute configuration. 
  * `NOTEBOOK_URI`: the Cloud Storage URI of the notebook to run. 
  * `OUTPUT_URI`: the Cloud Storage location where you want to store results. 
  * `USER_EMAIL`: the user account email address that specifies the notebook run's access to Google Cloud resources. 
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your notebook will run.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions create --display-name="DISPLAY_NAME" \
        --notebook-runtime-template=NOTEBOOK_RUNTIME_TEMPLATE \
        --gcs-notebook-uri=NOTEBOOK_URI \
        --gcs-output-uri=OUTPUT_URI \
        --user-email=USER_EMAIL \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions create --display-name="DISPLAY_NAME" `
        --notebook-runtime-template=NOTEBOOK_RUNTIME_TEMPLATE `
        --gcs-notebook-uri=NOTEBOOK_URI `
        --gcs-output-uri=OUTPUT_URI `
        --user-email=USER_EMAIL `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions create --display-name="DISPLAY_NAME" ^
        --notebook-runtime-template=NOTEBOOK_RUNTIME_TEMPLATE ^
        --gcs-notebook-uri=NOTEBOOK_URI ^
        --gcs-output-uri=OUTPUT_URI ^
        --user-email=USER_EMAIL ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about managing Colab Enterprise notebook runs from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/executions). 

### Python

Before trying this sample, [install the Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk). The Agent Platform Python client library is installed when you install the Agent Platform SDK for Python. For more information, see the [API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To run the following code sample, you'll need the Dataform repository ID of your notebook. To get the repository ID of your notebook, you can use Dataform's [list_repositories](https://docs.cloud.google.com/python/docs/reference/dataform/latest/summary_method#google_cloud_dataform_v1beta1_services_dataform_DataformClient_list_repositories_summary) method. 
    
    
    from google.cloud import aiplatform_v1
    
    PROJECT_ID = "my-project"
    LOCATION = "us-central1"
    REPOSITORY_ID = "b223577f-a3fb-482c-a22c-0658c6602598"
    TEMPLATE_ID = "6524523989455339520"
    
    API_ENDPOINT = f"{LOCATION}-aiplatform.googleapis.com"
    PARENT = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    
    notebook_service_client = aiplatform_v1.[NotebookServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.notebook_service.NotebookServiceClient.html)(client_options = {
        "api_endpoint": API_ENDPOINT,
    })
    
    operation = notebook_service_client.[create_notebook_execution_job](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_aiplatform_v1_services_notebook_service_NotebookServiceClient_create_notebook_execution_job)(parent=PARENT, notebook_execution_job={
        "display_name": "my-execution-job",
    
        # Specify a NotebookRuntimeTemplate to source compute configuration from
        "notebook_runtime_template_resource_name": f"projects/{PROJECT_ID}/locations/{LOCATION}/notebookRuntimeTemplates/{TEMPLATE_ID}",
    
        # Specify a Colab Enterprise notebook to run
        "dataform_repository_source": {
            "dataform_repository_resource_name": f"projects/{PROJECT_ID}/locations/{LOCATION}/repositories/{REPOSITORY_ID}",
        },
    
        # Specify a Cloud Storage bucket to store output artifacts
        "gcs_output_uri": "gs://my-bucket/",
    
        # Specify the identity that runs the notebook
        "execution_user": "{EMAIL}",
    
        # Run as the service account instead
        # "service_account": "my-service-account",
    })
    print("Waiting for operation to complete...")
    result = operation.result()

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

The following sample uses the [`google_colab_notebook_execution` ](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/colab_notebook_execution) Terraform resource to run a Colab Enterprise notebook. 
    
    
    resource "google_colab_runtime_template" "my_runtime_template" {
      provider = google-beta
      name = "{{index $.Vars "runtime_template_name"}}"
      display_name = "Runtime template"
      location = "us-central1"
    
      machine_spec {
        machine_type     = "e2-standard-4"
      }
    
      network_spec {
        enable_internet_access = true
      }
    }
    
    resource "google_storage_bucket" "output_bucket" {
      provider = google-beta
      name          = "{{index $.Vars "bucket"}}"
      location      = "US"
      force_destroy = true
      uniform_bucket_level_access = true
    }
    
    resource "google_storage_bucket_object" "notebook" {
      provider = google-beta
      name   = "hello_world.ipynb"
      bucket = google_storage_bucket.output_bucket.name
      content = <<EOF
        {
          "cells": [
            {
              "cell_type": "code",
              "execution_count": null,
              "metadata": {},
              "outputs": [],
              "source": [
                "print(\"Hello, World!\")"
              ]
            }
          ],
          "metadata": {
            "kernelspec": {
              "display_name": "Python 3",
              "language": "python",
              "name": "python3"
            },
            "language_info": {
              "codemirror_mode": {
                "name": "ipython",
                "version": 3
              },
              "file_extension": ".py",
              "mimetype": "text/x-python",
              "name": "python",
              "nbconvert_exporter": "python",
              "pygments_lexer": "ipython3",
              "version": "3.8.5"
            }
          },
          "nbformat": 4,
          "nbformat_minor": 4
        }
        EOF
    }
    
    resource "google_colab_notebook_execution" "{{$.PrimaryResourceId}}" {
      provider = google-beta
      notebook_execution_job_id = "{{index $.Vars "notebook_execution_job_id"}}"
      display_name = "Notebook execution full"
      location = "us-central1"
    
      execution_timeout = "86400s"
      gcs_notebook_source {
      uri = "gs://${google_storage_bucket_object.notebook.bucket}/${google_storage_bucket_object.notebook.name}"
      generation = google_storage_bucket_object.notebook.generation
      }
    
      service_account = "{{index $.TestEnvVars "service_account"}}"
    
      gcs_output_uri = "gs://${google_storage_bucket.output_bucket.name}"
      notebook_runtime_template_resource_name = "projects/${google_colab_runtime_template.my_runtime_template.project}/locations/${google_colab_runtime_template.my_runtime_template.location}/notebookRuntimeTemplates/${google_colab_runtime_template.my_runtime_template.name}"
    
      depends_on = [
        google_storage_bucket_object.notebook,
        google_storage_bucket.output_bucket,
        google_colab_runtime_template.my_runtime_template,
      ]
    
    }
    

You can view results from completed notebook runs on the [**Executions** page](https://console.cloud.google.com/agent-platform/colab/execution-jobs).

## Schedule a notebook run

To schedule a notebook run, you can use the Google Cloud console, the gcloud CLI, the Agent Platform Python client library, or Terraform.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Next to a notebook, click the more_vert**Notebook actions** menu and select **Schedule**. 

  4. In the **Schedule name** field, enter a name for your schedule. 

  5. Click the **Runtime template** list, and select a runtime template. The runtime template determines the specifications of the runtime that runs your notebook. 

  6. Under **Run schedule** , select **Recurring** to schedule the notebook run for a specific interval of time. 

  7. Complete the scheduling dialog.

  8. Next to the **Cloud Storage output location** field, click **Browse** to open the **Select folder** dialog. 

  9. Select a Cloud Storage bucket. Or, to create a bucket, click ![](https://docs.cloud.google.com/static/colab/images/icon-create-bucket.png) **Create new bucket** and complete the dialog. 

  10. If you selected a runtime template without end-user credentials enabled, the dialog includes a **Service account** field. In the **Service account** field, enter a service account's email address. 

  11. Click **Submit**.

Scheduled notebook runs start automatically on the schedule that you set. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * `DISPLAY_NAME`: the display name of your schedule.
  * `CRON_SCHEDULE`: the schedule that you set, in [unix-cron format](https://man7.org/linux/man-pages/man5/crontab.5.html). For example, `00 19 * * MON` means weekly on Monday, at 1900 hours Greenwich Mean Time (GMT). 
  * `NOTEBOOK_RUN_NAME`: the display name for notebook runs generated by this schedule. 
  * `NOTEBOOK_RUNTIME_TEMPLATE`: the notebook runtime template that specifies your runtime's compute configuration. 
  * `NOTEBOOK_URI`: the Cloud Storage URI of the notebook to run. 
  * `OUTPUT_URI`: the Cloud Storage location where you want to store results. 
  * `USER_EMAIL`: the user account email address that specifies the notebook run's access to Google Cloud resources. 
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your schedule will run.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules create --display-name="DISPLAY_NAME" \
        --cron-schedule=CRON_SCHEDULE \
        --execution-display-name=NOTEBOOK_RUN_NAME \
        --notebook-runtime-template=NOTEBOOK_RUNTIME_TEMPLATE \
        --gcs-notebook-uri=NOTEBOOK_URI \
        --gcs-output-uri=OUTPUT_URI \
        --user-email=USER_EMAIL \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules create --display-name="DISPLAY_NAME" `
        --cron-schedule=CRON_SCHEDULE `
        --execution-display-name=NOTEBOOK_RUN_NAME `
        --notebook-runtime-template=NOTEBOOK_RUNTIME_TEMPLATE `
        --gcs-notebook-uri=NOTEBOOK_URI `
        --gcs-output-uri=OUTPUT_URI `
        --user-email=USER_EMAIL `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules create --display-name="DISPLAY_NAME" ^
        --cron-schedule=CRON_SCHEDULE ^
        --execution-display-name=NOTEBOOK_RUN_NAME ^
        --notebook-runtime-template=NOTEBOOK_RUNTIME_TEMPLATE ^
        --gcs-notebook-uri=NOTEBOOK_URI ^
        --gcs-output-uri=OUTPUT_URI ^
        --user-email=USER_EMAIL ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about creating Colab Enterprise notebook schedules from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/schedules/create). 

### Python

Before trying this sample, [install the Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk). The Agent Platform Python client library is installed when you install the Agent Platform SDK for Python. For more information, see the [API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To run the following code sample, you'll need the Dataform repository ID of your notebook. To get the repository ID of your notebook, you can use Dataform's [list_repositories](https://docs.cloud.google.com/python/docs/reference/dataform/latest/summary_method#google_cloud_dataform_v1beta1_services_dataform_DataformClient_list_repositories_summary) method. 
    
    
    from google.cloud import aiplatform_v1
    
    PROJECT_ID = "my-project"
    LOCATION = "us-central1"
    REPOSITORY_ID = "b223577f-a3fb-482c-a22c-0658c6602598"
    TEMPLATE_ID = "6524523989455339520"
    
    API_ENDPOINT = f"{LOCATION}-aiplatform.googleapis.com"
    PARENT = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    
    schedules_service_client = aiplatform_v1.[ScheduleServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.schedule_service.ScheduleServiceClient.html)(client_options = {
        "api_endpoint": API_ENDPOINT,
    })
    
    schedule = schedules_service_client.[create_schedule](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.schedule_service.ScheduleServiceClient.html#google_cloud_aiplatform_v1_services_schedule_service_ScheduleServiceClient_create_schedule)(parent=PARENT, schedule={
        "display_name": "my-notebook-schedule",
    
        # Time specification. TZ is optional.
        # cron = "* * * * *" to run it in the next minute.
        "cron": "TZ=America/Los_Angeles * * * * *",
    
        # How many runs the schedule will trigger before it becomes COMPLETED.
        # A Schedule in COMPLETED state will not trigger any more runs.
        "max_run_count": 1,
        "max_concurrent_run_count": 1,
    
        "create_notebook_execution_job_request": {
          "parent": PARENT,
          "notebook_execution_job": {
            "display_name": "my-execution-job",
    
            # Specify a NotebookRuntimeTemplate to source compute configuration from
            "notebook_runtime_template_resource_name": f"projects/{PROJECT_ID}/locations/{LOCATION}/notebookRuntimeTemplates/{TEMPLATE_ID}",
    
            # Specify a Colab Enterprise notebook to run
            "dataform_repository_source": {
                "dataform_repository_resource_name": f"projects/{PROJECT_ID}/locations/{LOCATION}/repositories/{REPOSITORY_ID}",
            },
    
            # Specify a Cloud Storage bucket to store output artifacts
            "gcs_output_uri": "gs://my-bucket/",
    
    
            # Specify the identity that runs the notebook
            "execution_user": "{EMAIL}",
    
            # Run as the service account instead
            # "service_account": "my-service-account",
        }
      }
    })

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

The following sample uses the [`google_colab_schedule` ](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/colab_schedule) Terraform resource to schedule a Colab Enterprise notebook run. 
    
    
    resource "google_colab_runtime_template" "my_runtime_template" {
      provider = google-beta
      name = "{{index $.Vars "runtime_template_name"}}"
      display_name = "Runtime template"
      location = "us-central1"
    
      machine_spec {
        machine_type     = "e2-standard-4"
      }
    
      network_spec {
        enable_internet_access = true
      }
    }
    
    resource "google_storage_bucket" "output_bucket" {
      provider = google-beta
      name          = "{{index $.Vars "bucket"}}"
      location      = "US"
      force_destroy = true
      uniform_bucket_level_access = true
    }
    
    resource "google_secret_manager_secret" "secret" {
      provider = google-beta
      secret_id = "{{index $.Vars "secret"}}"
      replication {
        auto {}
      }
    }
    
    resource "google_secret_manager_secret_version" "secret_version" {
      provider = google-beta
      secret = google_secret_manager_secret.secret.id
      secret_data = "secret-data"
    }
    
    resource "google_dataform_repository" "dataform_repository" {
      provider = google-beta
      name = "{{index $.Vars "dataform_repository"}}"
      display_name = "dataform_repository"
      npmrc_environment_variables_secret_version = google_secret_manager_secret_version.secret_version.id
      kms_key_name = "{{index $.Vars "key_name"}}"
    
      labels = {
        label_foo1 = "label-bar1"
      }
    
      git_remote_settings {
          url = "https://github.com/OWNER/REPOSITORY.git"
          default_branch = "main"
          authentication_token_secret_version = google_secret_manager_secret_version.secret_version.id
      }
    
      workspace_compilation_overrides {
        default_database = "database"
        schema_suffix = "_suffix"
        table_prefix = "prefix_"
      }
    
    }
    
    resource "google_colab_schedule" "{{$.PrimaryResourceId}}" {
      provider = google-beta
      display_name = "{{index $.Vars "display_name"}}"
      location = "{{index $.TestEnvVars "location"}}"
      allow_queueing = true
      max_concurrent_run_count = 2
      cron = "TZ=America/Los_Angeles * * * * *"
      max_run_count = 5
      start_time = "{{index $.Vars "start_time"}}"
      end_time = "{{index $.Vars "end_time"}}"
    
      desired_state = "ACTIVE"
    
      create_notebook_execution_job_request {
        notebook_execution_job {
          display_name = "Notebook execution"
          execution_timeout = "86400s"
    
          dataform_repository_source {
            commit_sha = "randomsha123"
            dataform_repository_resource_name = "projects/{{index $.TestEnvVars "project_id"}}/locations/{{index $.TestEnvVars "location"}}/repositories/${google_dataform_repository.dataform_repository.name}"
          }
    
          notebook_runtime_template_resource_name = "projects/${google_colab_runtime_template.my_runtime_template.project}/locations/${google_colab_runtime_template.my_runtime_template.location}/notebookRuntimeTemplates/${google_colab_runtime_template.my_runtime_template.name}"
    
          gcs_output_uri = "gs://${google_storage_bucket.output_bucket.name}"
          service_account = "{{index $.TestEnvVars "service_account"}}"
        }
      }
    
      depends_on = [
        google_colab_runtime_template.my_runtime_template,
        google_storage_bucket.output_bucket,
        google_secret_manager_secret_version.secret_version,
        google_dataform_repository.dataform_repository,
      ]
    }
    

In the Google Cloud console, you can view your schedules on the [**Schedules** page](https://console.cloud.google.com/agent-platform/colab/schedules). You can view results from the completed notebook runs on the [**Executions** page](https://console.cloud.google.com/agent-platform/colab/execution-jobs).

## View results

To view notebook run results, you can use the Google Cloud console, the gcloud CLI, or the Agent Platform Python client library.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **Executions** page. 

[Go to Executions](https://console.cloud.google.com/agent-platform/colab/execution-jobs)

  2. Next to the notebook run that you want to view results for, click **View result**. 

Colab Enterprise opens the result of the notebook run in a new tab.

  3. To view the result, click the tab.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your notebook run results are located.
  * `SCHEDULE_NAME`: the name of the schedule to view results for. To see results from all schedules, omit the `--filter` flag. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions list --project=PROJECT_ID \
        --region=REGION \
        --filter="scheduleResourceName:SCHEDULE_NAME"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions list --project=PROJECT_ID `
        --region=REGION `
        --filter="scheduleResourceName:SCHEDULE_NAME"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions list --project=PROJECT_ID ^
        --region=REGION ^
        --filter="scheduleResourceName:SCHEDULE_NAME"

For more information about listing Colab Enterprise notebook runs from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/executions/list). 

### Python

Before trying this sample, [install the Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk). The Agent Platform Python client library is installed when you install the Agent Platform SDK for Python. For more information, see the [API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To run the following code sample, you'll need the Dataform repository ID of your notebook. To get the repository ID of your notebook, you can use Dataform's [list_repositories](https://docs.cloud.google.com/python/docs/reference/dataform/latest/summary_method#google_cloud_dataform_v1beta1_services_dataform_DataformClient_list_repositories_summary) method. 
    
    
    from google.cloud import aiplatform_v1
    
    PROJECT_ID = "my-project"
    LOCATION = "us-central1"
    
    API_ENDPOINT = f"{LOCATION}-aiplatform.googleapis.com"
    PARENT = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    
    notebook_service_client = aiplatform_v1.[NotebookServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.notebook_service.NotebookServiceClient.html)(client_options = {
        "api_endpoint": API_ENDPOINT,
    })
    
    notebook_execution_jobs = notebook_service_client.[list_notebook_execution_jobs](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_aiplatform_v1_services_notebook_service_NotebookServiceClient_list_notebook_execution_jobs)(parent=PARENT)
    notebook_execution_jobs

## Delete results

To delete a result from one of your notebook runs, you can use the Google Cloud console or the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **Executions** page. 

[Go to Executions](https://console.cloud.google.com/agent-platform/colab/execution-jobs)

  2. Select the notebook run that you want to delete the result for.

  3. Click delete **Delete**. 

  4. To confirm the deletion, click **Confirm**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `NOTEBOOK_RUN_ID`: the ID of the notebook run that you want to delete. 
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your notebook run is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions delete NOTEBOOK_RUN_ID \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions delete NOTEBOOK_RUN_ID `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab executions delete NOTEBOOK_RUN_ID ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about deleting Colab Enterprise notebook runs from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/executions/delete). 

## Share a notebook run's results

You can share notebook run results by providing access to the Cloud Storage bucket that contains your notebook run. Providing this access also grants users access to any other resources in the same Cloud Storage bucket (see Security considerations).

For more information, see the Cloud Storage [Sharing and collaboration page](https://docs.cloud.google.com/storage/docs/collaboration).

### Security considerations

Your notebook run results are stored as notebook (IPYNB) files in a Cloud Storage bucket. Consider the following when you grant access to this bucket:

  * Anyone with access to the bucket can see the notebook file's code and the results of the notebook run.

  * Anyone with the ability to change the contents of the bucket can change the contents of the notebook file.




When your schedule is configured to use personal credentials, only the specified user is able to modify the schedule or trigger the schedule.

When your schedule is configured to use a service account, only users with the `iam.serviceAccounts.actAs` permission on the service account is able to modify the schedule or trigger the schedule.

## View schedule details

You can view information about a schedule, including:

  * The Cloud Storage bucket that the schedule stores results in.
  * The start and end time.
  * The frequency.



To view schedule details, you can use the Google Cloud console or the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **Schedules** page. 

[Go to Schedules](https://console.cloud.google.com/agent-platform/colab/schedules)

  2. Click the name of a schedule. 

The **Schedule details** page opens.

  3. To go back to the **Schedules** page, click arrow_back **Back to previous page**. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * `SCHEDULE`: your schedule ID.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your schedule is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules describe SCHEDULE \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules describe SCHEDULE `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules describe SCHEDULE ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about viewing Colab Enterprise schedules from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/schedules/describe). 

## Pause, resume, or delete a schedule

To pause, resume, or delete a schedule, you can use the Google Cloud console, the gcloud CLI, or Terraform.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **Schedules** page. 

[Go to Schedules](https://console.cloud.google.com/agent-platform/colab/schedules)

  2. Select a schedule. 

  3. Click pause **Pause** , play_arrow **Resume** , or delete **Delete**. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * `ACTION`: one of `pause`, `resume`, or `delete`. 
  * `SCHEDULE_ID`: your schedule ID.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your schedule is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules ACTION SCHEDULE_ID \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules ACTION SCHEDULE_ID `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab schedules ACTION SCHEDULE_ID ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about managing Colab Enterprise schedules from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/schedules). 

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

The following sample uses the [`google_colab_schedule` ](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/colab_schedule) Terraform resource to pause or resume a schedule. 

To use this sample, change the value of `desired_state` according to the following: 

  * `PAUSED` to pause the schedule
  * `ACTIVE` to resume the schedule


    
    
    resource "google_colab_runtime_template" "my_runtime_template" {
      name = "{{index $.Vars "runtime_template_name"}}"
      display_name = "Runtime template"
      location = "us-central1"
    
      machine_spec {
        machine_type     = "e2-standard-4"
      }
    
      network_spec {
        enable_internet_access = true
      }
    }
    
    resource "google_storage_bucket" "output_bucket" {
      name          = "{{index $.Vars "bucket"}}"
      location      = "US"
      force_destroy = true
      uniform_bucket_level_access = true
    }
    
    resource "google_storage_bucket_object" "notebook" {
      name   = "hello_world.ipynb"
      bucket = google_storage_bucket.output_bucket.name
      content = <<EOF
        {
          "cells": [
            {
              "cell_type": "code",
              "execution_count": null,
              "metadata": {},
              "outputs": [],
              "source": [
                "print(\"Hello, World!\")"
              ]
            }
          ],
          "metadata": {
            "kernelspec": {
              "display_name": "Python 3",
              "language": "python",
              "name": "python3"
            },
            "language_info": {
              "codemirror_mode": {
                "name": "ipython",
                "version": 3
              },
              "file_extension": ".py",
              "mimetype": "text/x-python",
              "name": "python",
              "nbconvert_exporter": "python",
              "pygments_lexer": "ipython3",
              "version": "3.8.5"
            }
          },
          "nbformat": 4,
          "nbformat_minor": 4
        }
        EOF
    }
    
    resource "google_colab_schedule" "{{$.PrimaryResourceId}}" {
      display_name = "{{index $.Vars "display_name"}}"
      location = "{{index $.TestEnvVars "location"}}"
      max_concurrent_run_count = 2
      cron = "TZ=America/Los_Angeles * * * * *"
    
      desired_state = "PAUSED"
    
      create_notebook_execution_job_request {
        notebook_execution_job {
          display_name = "Notebook execution"
          gcs_notebook_source {
            uri = "gs://${google_storage_bucket_object.notebook.bucket}/${google_storage_bucket_object.notebook.name}"
            generation = google_storage_bucket_object.notebook.generation
          }
    
          notebook_runtime_template_resource_name = "projects/${google_colab_runtime_template.my_runtime_template.project}/locations/${google_colab_runtime_template.my_runtime_template.location}/notebookRuntimeTemplates/${google_colab_runtime_template.my_runtime_template.name}"
          gcs_output_uri = "gs://${google_storage_bucket.output_bucket.name}"
          service_account = "{{index $.TestEnvVars "service_account"}}"
          }
      }
    
      depends_on = [
        google_colab_runtime_template.my_runtime_template,
        google_storage_bucket.output_bucket,
      ]
    }
    

**Note:** Deleting a schedule doesn't delete the notebook runs that were generated from that schedule.

## What's next

  * To find a notebook that can help you get your project started quickly, see the [notebook gallery](https://console.cloud.google.com/agent-platform/colab/notebook-gallery).

  * Learn more about [runtimes and runtime templates](https://docs.cloud.google.com/colab/docs/runtimes).

  * Learn how to [create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template).

  * Learn more about [accessing Google Cloud services and APIs](https://docs.cloud.google.com/colab/docs/run-code-adc) in your notebook.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
