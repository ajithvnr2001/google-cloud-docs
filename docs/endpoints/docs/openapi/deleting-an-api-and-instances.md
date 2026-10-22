---
url: https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances/
title: Deleting an API and API instances \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:53.862556+00:00
---

# Deleting an API and API instances  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Deleting an API and API instances Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/deleting-an-api-and-instances "View this page for the Cloud Endpoints gRPC docs")

Cloud Endpoints uses the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) and Service Management to manage your API. When you deployed your OpenAPI document by using the `gcloud endpoints services deploy` command, the command used Service Management to create a managed service for your API.

To delete your API you need to:

  * Delete the instance that ESP and your API backend is running on.
  * Delete the managed service that was created for your API.



The easiest way to do both of these tasks is to delete the Google Cloud project that your API is in. If you want to preserve your Google Cloud project, then you need to delete the instance and the managed service.

**Note:** If you encounter issues with Google Cloud project deletion, refer to the [troubleshooting](https://docs.cloud.google.com/resource-manager/docs/troubleshooting-project-deletion) section for resolution. 

## Deleting instances

### App Engine

To delete an instance running in the App Engine flexible environment:

You can either disable the application on the **App Engine Settings** page in the Google Cloud console, or you can delete the Google Cloud project. See [Disabling an application and shutting down a project](https://cloud.google.com/appengine/docs/flexible/python/managing-projects-apps-billing#disabling_an_application) for more information.

### Compute Engine

Use the [`gcloud compute instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) command. When you delete an instance in this way, the instance shuts down and is removed from the list of instances, and all resources attached to the instance are released, such as persistent disks and any static IP addresses.

To delete an instance, use the following command:
    
    
    gcloud compute instances delete [INSTANCE_NAME] --zone = [ZONE]

For more information on deleting Compute Engine instances, see the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance). 

### GKE

To delete a GKE cluster with the Google Cloud CLI:
    
    
    gcloud container clusters delete [NAME] --zone [ZONE]

Replace `[NAME]` with the name of your cluster and `[ZONE]` with the compute zone that the cluster is in.

For more information on deleting a GKE cluster, see the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster). 

## Deleting the managed service

If you don't need the data on the **Endpoints Services** page and in the **Produced API** log on the **Logs Explorer** page, you can delete the managed service for your API, which removes the data from the Google Cloud console.

To delete the managed service:

  1. Make sure that the gcloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login
         

  2. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list
         

  3. Using the applicable project ID from the previous step, set the default Google Cloud project to the one that your application is in:
         
         gcloud config set project [YOUR_PROJECT_ID]
         

  4. Obtain the name of all managed services in your Google Cloud project:
         
         gcloud endpoints services list
         

  5. Delete the service from Service Management. Replace `SERVICE_NAME` with the name of the service you want to remove.
         
         gcloud endpoints services delete SERVICE_NAME
         

Running `gcloud endpoints services delete` doesn't immediately delete the managed service. Service Management disables the managed service for 30 days, which allows you time to restore it if you need to. After 30 days, Service Management permanently deletes the managed service.




## What's next

  * To restore a managed service, see [Restoring a managed service](https://docs.cloud.google.com/endpoints/docs/openapi/restore-managed-service).

  * For information on the `gcloud` commands used on this page, see the [gcloud reference](https://docs.cloud.google.com/sdk/gcloud/reference).

  * For information on Service Management, see [Creating and deleting managed services](https://docs.cloud.google.com/service-infrastructure/docs/create-services).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
