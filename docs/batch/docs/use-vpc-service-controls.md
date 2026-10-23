---
url: https://docs.cloud.google.com/batch/docs/use-vpc-service-controls/
title: Use VPC Service Controls with Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:59.256156+00:00
---

# Use VPC Service Controls with Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/use-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Use VPC Service Controls with Batch Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use VPC Service Controls with Batch. [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview#capabilities) allows you to protect the resources and data of Google Cloud services by isolating specific resources into service perimeters. A service perimeter blocks connections with Google Cloud services outside the perimeter and any connections from the internet that are not explicitly allowed.

  * To configure a VPC Service Controls service perimeter to use Batch, see Configure a service perimeter for Batch in this document.
  * If your project or network uses VPC Service Controls to restrict networking access for Batch, you must configure your Batch jobs to run in the required service perimeter. To learn how, see Create a job that runs in a service perimeter in this document.



For more information about networking concepts and when to configure networking, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview).

**Caution:** Batch does not guarantee VPC Service Controls support for jobs with custom VM OS images. Only default Batch VM OS images are recommended for jobs that use VPC Service Controls. For more information about VM OS images and how to restrict VM OS images, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to use VPC Service Controls with Batch, ask your administrator to grant you the following IAM roles: 

     * To configure a service perimeter: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) on the project 
     * To create a job: 
       * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
       * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * To identify the service perimeter for a project or network: [Access Context Manager Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`) on the project 
     * To identify the network and subnet for a job: [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. If you create a job that runs in a service perimeter, you need to identify the network that you want to use for the job. The network you specify for a job that runs in a service perimeter must meet the following requirements: 
     * The network is a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) that is in the same project as the job or is a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the project for the job. 
     * The network includes a [subnetwork (subnet)](https://docs.cloud.google.com/vpc/docs/subnets) in the location where you want to run the job. 
     * The network is in the required service perimeter and uses Private Google Access to allow access to the domains for the APIs and services that your job uses. For more information, see Configure a service perimeter for Batch in this document. 
For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 



## Configure a service perimeter for Batch

To configure a service perimeter for Batch, do the following:

  1. Plan the configuration for your service perimeter. For an overview of the configuration stages for service perimeters, see VPC Service Controls documentation for [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

To use Batch, the service perimeter must meet the following requirements:

     * **Restricted services:** To secure Batch within a service perimeter, you must include the Google Cloud services that are required for your Batch jobs in that perimeter, such as the following services:

       * **Batch API** (`batch.googleapis.com`)
       * **Cloud Logging API** (`logging.googleapis.com`): Required if you want your jobs to write logs into Cloud Logging. (Recommended)
       * **Container Registry API** (`containerregistry.googleapis.com`): Required if you submit a job that uses any containers with an image from Container Registry.
       * **Artifact Registry API** (`artifactregistry.googleapis.com`): Required if you submit a job that uses any containers with an image from Artifact Registry.
       * **Filestore API** (`file.googleapis.com`): Required if your job uses a [Filestore file share](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-nfs).
       * **Cloud Storage API** (`storage.googleapis.com`): Required for some jobs that use a [Cloud Storage bucket](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-bucket). Required if you use an image for your Batch job that does not have the [Batch service agent](https://docs.cloud.google.com/batch/docs/get-started) pre-installed.

To learn how to enable each of these services in your service perimeter, see [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

**Caution:** For your Batch jobs to be fully protected by the service perimeter, you must specify _all_ services that you plan to use.

For each service you include other than Batch, you also need to verify that your service perimeter meets the requirements listed for that service in the [VPC Service Controls supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) documentation.

     * **VPC networks:** Each Batch job requires a VPC network, so your service perimeter must include a VPC network that Batch jobs can run on. To learn how to configure a VPC network that can run your Batch jobs inside a service perimeter, see the following documents:

       * For an overview of using VPC networks in a service perimeter, see [VPC networks management in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management).
       * To learn how to use Private Google Access with VPC Service Controls to configure access to the Google Cloud services that are required for your Batch jobs, see [Set up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).
       * For more information about the networking requirements for Batch jobs, see [Job networking overview](https://docs.cloud.google.com/batch/docs/networking-overview).
  2. [Create a new service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) or [update an existing service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to meet these requirements.




## Create a job that runs in a service perimeter

When you create a job that runs in a service perimeter, you must also block external access for all the VMs a job runs on and specify a network and subnet that allow the job to access required APIs.

To create a job that runs in a service perimeter, follow the steps in the documentation for [Create a job that blocks external access for all VMs](https://docs.cloud.google.com/batch/docs/job-without-external-access) and specify a network that meets the network requirements for a job that runs in a service perimeter.

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn more about [networking](https://docs.cloud.google.com/batch/docs/networking-overview).
  * Learn more about [creating a job](https://docs.cloud.google.com/batch/docs/create-run-job).
  * Learn how to [view jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
