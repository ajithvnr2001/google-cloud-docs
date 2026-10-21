---
url: https://docs.cloud.google.com/batch/docs/use-image-streaming/
title: Use Image streaming to reduce container startup time \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:08.719243+00:00
---

# Use Image streaming to reduce container startup time  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/use-image-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Use Image streaming to reduce container startup time Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use Image streaming to pull container images into Batch container jobs.

Image streaming enables Batch jobs to initialize without waiting for a container image to finish downloading, which provides the following benefits:

  * Reduced latency when pulling large images
  * Faster time to begin job execution



## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. If you haven't already done so, enable the Container File System API by running the following command:
         
         gcloud services enable containerfilesystem.googleapis.com
         

  4. If your container images are protected by VPC Service Controls, [update your service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to include `containerfilesystem.googleapis.com`.



## Limitations

Batch Image streaming has the following limitations:

  * Batch only supports Image streaming for container images that are stored in Artifact Registry. If you currently use Container Registry to manage your container images, you can [transition to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr).
  * You must run your Batch job's VMs in the same [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) as where you store your container image in Artifact Registry.
  * Containers that use the Docker image manifest version 2, schema 1 aren't supported.
  * When you use Image streaming, [containers runnables](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container) only support the following fields: 
    * `imageUri`
    * `commands`
    * `entrypoint`
    * `volumes`
    * `enableImageStreaming`
  * Container images with empty layers or duplicate layers aren't supported.



## Create a job that uses Image streaming

Create a Batch container job that uses Image streaming by doing the following:

Use the Google Cloud CLI or REST API to [create a container job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-container-job). To enable Image streaming for a container runnable, set `enableImageStreaming` field to `true` and set the `imageUri` field to an image that is stored in an [Artifact Registry location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) that contains the location of the job's VM.
    
    
    "container": {
        ...
        "enableImageStreaming": true
            }
    

**Note:** When you use Image streaming, [containers runnables](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container) only support the `imageUri`, `commands`, `entrypoint`, `volumes`, and `enableImageStreaming` fields.

For example, a job that uses Image streaming would have a JSON configuration file similar to the following:
    
    
    {
        "taskGroups": [
            {
                "taskCount": "1",
                "taskCountPerNode": "1",
                "taskSpec": {
                    "runnables": [
                        {
                            "container": {
                                "imageUri": "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:TAG",
                                **"enableImageStreaming" : true**
                            }
                        }
                    ]
                }
            }
        ],
        "allocationPolicy": {
            "instances": [
                {
                    "policy": {
                        "machineType": "e2-standard-4"
                    }
                }
            ]
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

Replace the following values:

  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository where the image is stored, for example `us-east1` or `us`. The location of the container must be the same as the location of the Batch job's VMs.
  * `PROJECT-ID`: the project that contains the container image. If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `REPOSITORY`: the name of the repository where the image is stored.
  * `IMAGE`: the name of the container image.
  * `TAG`: the tag applied to the image.



## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
