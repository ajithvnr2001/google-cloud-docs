---
url: https://docs.cloud.google.com/compute/docs/architecture/access-global-resources-regionally/
title: Access global resources regionally for high availability \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:20:04.061302+00:00
---

# Access global resources regionally for high availability  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/architecture/access-global-resources-regionally/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Access global resources regionally for high availability Stay organized with collections  Save and categorize content based on your preferences. 

By using autoscaling scripts or runtime services on Compute Engine, you can automate continuous integration and continuous deployment (CI/CD) pipelines. However, because these resources depend heavily on global resource definitions when they query global API endpoints, this approach can introduce a single point of failure across your multi-region architecture.

To mitigate this risk, you can configure your services to access regional views of global resources. By sending `GET` and `LIST` requests to regionalized read-only endpoints within the exact region where your compute workloads run, your services isolate their API consumption from potential outages in the global control plane or in other regions. For more information about regionalized read-only endpoints and resilience best practices, see [Use regional views for resilient control-plane reads](https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to access global resources regionally, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project or OS images. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to access global resources regionally. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to access global resources regionally:

  * To get regional views for a project: `compute.projects.get` on the project 
  * To get regional views for OS images: `compute.images.get` and `compute.images.list` on the project or OS images 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Project resource

You can get regional views of your global project resource by using the `projectViews` read-only endpoint. When you query the `projectViews` endpoint, Compute Engine returns the standard global [`compute.Project`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects#project) resource object. The resource itself remains global. 

**Note:** When you query a `compute.Project` resource by using regional `projectViews.get` endpoints, the `quota` array is excluded from the response. For accurate quota configuration and real-time usage metrics across all regions and zones, query the global [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get) endpoint.

### Get a regional view of a project resource

You can get a regional view of your global project by using the Google Cloud CLI or the REST API.

###  gcloud 

To describe your global project through the control plane for a specific region, run the [`gcloud compute project-views describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-views/describe):
    
    
    gcloud compute project-views describe \
        --region=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `REGION`: the Google Cloud region for the API request—for example, `us-central1`.
  * `PROJECT_ID`: your project ID.



###  REST 

To describe your global project through the control plane for a specific region, send a `GET` request to the [`projectViews` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projectViews).
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/projectViews"
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `REGION`: the Google Cloud region for the API request—for example, `us-central1`.



The API returns the standard `compute.Project` resource representation directly.
    
    
    {
      "kind": "compute#project",
      "id": "1234567890123456789",
      "creationTimestamp": "2024-01-15T10:00:00.000-08:00",
      "name": "my-project12345",
      "commonInstanceMetadata": {
        "items": [
          {
            "key": "example-key",
            "value": "example-value"
          }
        ]
      },
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project12345",
      "defaultServiceAccount": "SERVICE_ACCOUNT_EMAIL"
    }
    

## OS image resource

You can get regional views of your global OS image resource by using the `imageViews` read-only endpoint. When you query the `imageViews` endpoint, Compute Engine returns the standard global [`compute.Image`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images) resource object. The resource itself remains global. 

### Get a regional list of OS image resources

You can list all of the global OS images that are available to your project through a specific regional endpoint by using the gcloud CLI or the REST API.

###  gcloud 

To list global OS images by using a regional endpoint, run the [`gcloud compute image-views list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/image-views/list):
    
    
    gcloud compute image-views list \
        --region=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `REGION`: the Google Cloud region for the API request—for example, `us-central1`.
  * `PROJECT_ID`: your project ID.



###  REST 

To list global OS images by using a regional endpoint, send a `GET` request to the [`imageViews` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/imageViews):
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/imageViews"
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `REGION`: the Google Cloud region for the API request—for example, `us-central1`.



### Get a regional view of an OS image resource

You can retrieve information for a specific global OS image through a regional endpoint by using the gcloud CLI or the REST API.

###  gcloud 

To retrieve details for a global OS image using a regional endpoint, run the [`gcloud compute image-views describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/image-views/describe):
    
    
    gcloud compute image-views describe IMAGE_NAME \
        --region=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `IMAGE_NAME`: the name of the global OS image resource.
  * `REGION`: the Google Cloud region for the API request—for example, `us-central1`.
  * `PROJECT_ID`: your project ID.



###  REST 

To retrieve details for a global OS image using a regional endpoint, send a `GET` request to the specific [`imageViews` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/imageViews):
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/imageViews/IMAGE_NAME"
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `REGION`: the Google Cloud region for the API request—for example, `us-central1`.
  * `IMAGE_NAME`: the name of the global OS image resource.



The API returns the standard `compute.Image` resource representation directly.
    
    
    {
      "kind": "compute#image",
      "id": "1234567890123456789",
      "creationTimestamp": "2024-01-15T10:00:00.000-08:00",
      "name": "my-image12345",
      "sourceDisk": "https://www.googleapis.com/compute/v1/projects/my-project12345/zones/us-central1-a/disks/my-disk12345",
      "sourceDiskId": "1234567890123456789",
      "sourceType": "RAW",
      "status": "READY",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project12345/global/images/my-image12345"
    }
    

## What's next

  * Learn more about [The project resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects).
  * Learn more about [OS images](https://docs.cloud.google.com/compute/docs/images).
  * Learn how to [Troubleshoot regional views of global resources](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-regional-views-global-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
