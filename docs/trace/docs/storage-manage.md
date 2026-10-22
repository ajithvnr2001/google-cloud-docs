---
url: https://docs.cloud.google.com/trace/docs/storage-manage/
title: List trace buckets and manage datasets \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:05.062361+00:00
---

# List trace buckets and manage datasets  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/storage-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  List trace buckets and manage datasets Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Observability API or the Google Cloud CLI to view your observability buckets, inspect datasets and views, and create links to analyze stored trace data with SQL. To create links, you can also use Terraform.

For conceptual background and storage details, see [Trace storage overview](https://docs.cloud.google.com/trace/docs/storage-overview) and [Trace schema](https://docs.cloud.google.com/trace/docs/reference/trace-schema).

## Before you begin

Configure your project and your Identity and Access Management (IAM) roles, and select the interface that you plan to use.

#### Configure your project and roles

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  8. To get the permissions that you need to list buckets, links, and views, ask your administrator to grant you the [Observability Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




#### Select the interface you plan to use

### gcloud

**Note** : You must use gcloud CLI version 586.0.0 or later.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## List observability buckets

This section describes how to list your observability buckets. An observability bucket is the management entity for datasets, which store data.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * LOCATION: The location of the observability buckets. To list all observability buckets, regardless of location, set the location to a hyphen (`-`).
  * PROJECT_ID: The identifier of the project..



Execute the [`gcloud observability buckets list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets list \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets list `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets list ^
     --location=LOCATION --project=PROJECT_ID

The response lists the name, description, and create time of each observability buckets. The following is an example of a response when the command is successful: 
    
    
    ---
    createTime: '2026-01-21T21:39:22.381083860Z'
    description: Bucket for storing spans from Cloud Trace.
    name: projects/my-project/locations/us/buckets/_Trace
    

###  Terraform 

You can't use Terraform to list observability buckets.

###  REST 

To list the observability buckets that are in your project and in a specific location, use the [`projects.locations.buckets.list`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets/list) method.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION
    

The fields in the previous expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations). If you set LOCATION to a hyphen (`-`), then all observability buckets in your project are listed.



The response is an array of [`Bucket`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets#Bucket) objects. For each object, the value of the `name` field has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    
    

The following shows a sample response:
    
    
    {
      "buckets": [
        {
          "name": "projects/my-project/locations/us/buckets/_Trace",
          "description": "Trace Bucket",
          "createTime": "2025-01-01T15:42:30.988919645Z",
          "updateTime": "2025-02-04T15:42:30.988919645Z",
          "retentionDays": 30
        }
      ]
    }
    

You can use the Observability API to get more information about the bucket whose ID is BUCKET_ID. For example, you can list the datasets on that bucket, and the views and links on each dataset. For more information, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

## List datasets on an observability bucket

This section describes how to list the observability datasets on an observability bucket. An observability bucket is the management container for datasets, which store data. When Google Cloud Observability creates a bucket, it automatically creates a dataset.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * PROJECT_ID: The identifier of the project.



Execute the [`gcloud observability buckets datasets list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/datasets/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets datasets list \
     --bucket=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID \
     --location=LOCATION \
     --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets datasets list `
     --bucket=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID `
     --location=LOCATION `
     --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets datasets list ^
     --bucket=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID ^
     --location=LOCATION ^
     --project=PROJECT_ID

The response lists the name, description, and create time of each dataset. The following is an example of a response when the command is successful: 
    
    
    ---
    createTime: '2026-01-21T21:39:22.381083860Z'
    description: Dataset for storing spans from Cloud Trace.
    name: projects/my-project/locations/us/buckets/_Trace/datasets/Spans
    

###  Terraform 

You can't use Terraform to list observability datasets.

###  REST 

To list the datasets for an observability bucket, use the [`projects.locations.buckets.datasets.list`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets/list) method.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.



The response is an array of [`Dataset`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets#Dataset) objects. For each object, the value of the `name` field has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID
    
    

The following shows a sample response:
    
    
    {
      "datasets": [
        {
          "name": "projects/my-project/locations/us/buckets/_Trace/datasets/Spans",
          "description": "Trace Spans",
          "createTime": "2025-01-01T15:42:30.988919645Z",
          "updateTime": "2025-02-04T15:42:30.988919645Z",
        }
      ]
    }
    

You can use the Observability API to get information about the dataset whose ID is DATASET_ID. For example, you can list the views and links on each dataset. For more information, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

## List views on a dataset

This section describes how to list your observability views. Each observability dataset hosts one or more views. A view provides read access to a subset of entries in the dataset. Google Cloud Observability creates a view when it creates a dataset. That view includes all data in the dataset.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * DATASET_ID: The ID of the dataset. Your trace data is stored in a dataset named `Spans`.
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * PROJECT_ID: The identifier of the project.



Execute the [`gcloud observability buckets datasets views list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/datasets/views/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets datasets views list \
     --dataset=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID \
     --bucket=BUCKET_ID \
     --location=LOCATION \
     --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets datasets views list `
     --dataset=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID `
     --bucket=BUCKET_ID `
     --location=LOCATION `
     --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets datasets views list ^
     --dataset=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID ^
     --bucket=BUCKET_ID ^
     --location=LOCATION ^
     --project=PROJECT_ID

The response lists the name, create time, and update time of each observability views. The following is an example of a response when the command is successful: 
    
    
    ---
    createTime: '2026-01-21T21:39:22.381083860Z'
    displayName: _AllSpans
    name: projects/pamstestproject1/locations/us/buckets/_Trace/datasets/Spans/views/_AllSpans
    updateTime: '2026-01-21T21:39:22.381083860Z'
    

###  Terraform 

You can't use Terraform to list observability views.

###  REST 

To list the views on a dataset, use the [`projects.locations.buckets.datasets.views.list`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.views/list) method.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/views
    
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * DATASET_ID: The ID of the dataset being queried. For example, this ID might be `Spans`.



The response is an array of [`View`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.views#View) objects. For each object, the value of the `name` field has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/views/OBS_VIEW_ID
    

In the preceding expression, the ID of a view is represented by OBS_VIEW_ID. For example, this field might have a value of `_AllSpans`.

The following shows a sample response:
    
    
    {
      "views": [
        {
          "name": "projects/my-project/locations/us/buckets/_Trace/datasets/Spans/views/_AllSpans",
          "filter": "",
          "createTime": "2025-01-01T15:42:30.988919645Z",
          "updateTime": "2025-02-04T15:42:30.988919645Z",
        }
      ]
    }
    

For more information, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

## List links on a dataset

This section describes how to list the links on your observability datasets. A link can let you query your data by using BigQuery services or it can let a Google Cloud service query a subset of that data.

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * DATASET_ID: The ID of the dataset. Your trace data is stored in a dataset named `Spans`.
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * PROJECT_ID: The identifier of the project.



Execute the [`gcloud observability buckets datasets links list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/datasets/links/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets datasets links list \
     --dataset=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID\
     --bucket=BUCKET_ID \
     --location=LOCATION \
     --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets datasets links list `
     --dataset=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID`
     --bucket=BUCKET_ID `
     --location=LOCATION `
     --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets datasets links list ^
     --dataset=projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID^
     --bucket=BUCKET_ID ^
     --location=LOCATION ^
     --project=PROJECT_ID

The response lists the name and create time of each link. The following is an example of a response when the command is successful: 
    
    
    ---
    createTime: '2026-04-02T21:23:09.272323714Z'
    name: projects/my-project/locations/us/buckets/_Trace/datasets/Spans/links/mydataset
    

###  Terraform 

You can't use Terraform to list links on observability datasets.

###  REST 

To list the links on a dataset, use the [`projects.locations.buckets.datasets.links.list`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.links/list) method.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID
    
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * DATASET_ID: The ID of the dataset being queried. For example, this ID might be `Spans`.



The response is an array of [`Link`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.links#Link) objects. For each object, the value of the `name` field has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID
    

The LINK_ID is the name of the BigQuery dataset. This field must be unique within your Google Cloud project.

The following shows a sample response:
    
    
    {
      "links": [
        {
          "name": "projects/my-project/locations/us/buckets/_Trace/datasets/Spans/links/my_link",
          "description": "My link for traces to BigQuery",
          "createTime": "2025-01-12T15:42:30.988919645Z"
        }
      ]
    }
    

For more information, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

## Create a link on a dataset

This section describes how to create a linked BigQuery dataset on an observability dataset, which lets you use BigQuery services to query your trace data. Each observability dataset supports one linked BigQuery dataset.

When you create a link on an observability dataset, the following occurs:

  * Google Cloud Observability might create the following service accounts or modify their IAM role grants:

    * [Monitoring Service Account](https://docs.cloud.google.com/iam/docs/service-agents#monitoring-service-account): Required to create a link to a linked BigQuery dataset. The Cloud Monitoring API must be enabled for Google Cloud Observability to create this service account.

    * [Cloud Observability Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-observability-service-account): Required to create a link on an observability dataset.

    * [Cloud Logging Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-logging-service-account): Required to create a link on a log bucket.

  * Audit logs record the request to create a link and the request from the service agent manager to grant the Monitoring Service Account the IAM role of [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent). These logs also record the completion of the long-running operation.




### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Monitoring and Observability APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Monitoring and Observability APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,observability.googleapis.com)

  8. To get the permissions that you need to create a link on an observability dataset, ask your administrator to grant you the [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Create a linked BigQuery dataset

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * LINK_ID: The name of the BigQuery dataset.
  * DATASET_ID: The ID of the dataset. Your trace data is stored in a dataset named `Spans`.
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * PROJECT_ID: The identifier of the project.



Execute the [`gcloud observability buckets datasets links create`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/datasets/links/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets datasets links create \
      projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID \
     --dataset=DATASET_ID\
     --bucket=BUCKET_ID \
     --location=LOCATION \
     --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets datasets links create `
      projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID `
     --dataset=DATASET_ID`
     --bucket=BUCKET_ID `
     --location=LOCATION `
     --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets datasets links create ^
      projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID ^
     --dataset=DATASET_ID^
     --bucket=BUCKET_ID ^
     --location=LOCATION ^
     --project=PROJECT_ID

The create command initiates a long-running operation. The following is an example of a response when the command is successful: 
    
    
    Create request issued for: [mydataset]
    Waiting for operation [projects/my-project/locations/us/operations/operation-1775164903749-64e80c9817833-9ff804b6-c3e9cbe7] to complete...done.
    Created link [mydataset].
    

###  Terraform 

To create a link on an observability dataset, use the Terraform resource [`google_observability_link`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_link) and set the following fields:

  * `project`: The ID of your project.
  * `location`: The location of the link. This location must match the location of the observability bucket.
  * `bucket`: The ID of the observability bucket. For example, `_Trace`.
  * `dataset`: The ID of the observability dataset. For example, `Spans`.
  * `link_id`: The ID of the BigQuery dataset.



You can also update and delete links.

###  REST 

To create a link to a BigQuery dataset, send a request to the [`projects.locations.buckets.datasets.links.create`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.links/create) endpoint.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID
    
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * DATASET_ID: The ID of the dataset being queried. For example, this ID might be `Spans`.



This command requires a query parameter and a request body:

  * The query parameter, `linkId`, must be specified and set to the name of the BigQuery dataset. For example, `linkId="my_link"`. The BigQuery dataset name must be unique for your Google Cloud project, and must be limited to 100 characters and can include only letters, digits, and underscores.

  * The request body is a [`Link`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.links#Link) object. The value of the `name` field has the following format:
        
        projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID
        

The value you provide for the `name` field must match the linked BigQuery dataset referenced by the query parameter.

The LINK_ID field is the name of the BigQuery dataset.




The response is an [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation) object. This object contains information about the progress of the method. When the method completes, the `Operation` object contains status data.

For a complete list of Observability API endpoints, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

If you encounter permission errors when creating a linked dataset, then see [Troubleshoot permission errors](https://docs.cloud.google.com/trace/docs/troubleshooting#linked-dataset-permission-error).

## What's next

  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces)

  * [Query and analyze traces with SQL](https://docs.cloud.google.com/trace/docs/analytics)

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets): Configure a default storage location and a default customer-managed encryption key (CMEK) for your observability buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
