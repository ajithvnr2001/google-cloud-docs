---
url: https://docs.cloud.google.com/batch/docs/job-without-external-access/
title: Block external access for a job \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:45.713287+00:00
---

# Block external access for a job  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/job-without-external-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Block external access for a job Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure a Batch job to block external access for all of its VMs or specific containers.

Block external access for a job to meet networking requirements or improve security. You must block external access for a job's VMs by using VMs without external IP addresses if any of the following are true:

  * Your project is restricted by the `compute.vmExternalIpAccess` organization policy constraint.
  * The network you specify for the job uses [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) to configure private connectivity to Google APIs and services. Private Google Access has no effect on VMs that have external IP addresses.

If the network you specify for the job uses [Private Google Access with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity) for Batch, see [Use VPC Service Controls and Batch](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls).




Alternatively, if you do not want to block all direct external access for a job, you can block external access for any containers that a job runs.

**Note:** If you block external access for all of a job's VMs, you don't need to also explicitly block external access for the job's containers—they already do not have access because they run on the job's VMs.

For more information about networking concepts and when to configure networking, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job that blocks external access, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * To identify the network and subnet for a job: [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. If you block external access for a job's VMs, you need to identify the network that you want to use for the job. The network you specify for a job that blocks external access for its VMs must meet the following requirements: 
     * The network is a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) that is in the same project as the job or is a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the project for the job. 
     * The network includes a [subnetwork (subnet)](https://docs.cloud.google.com/vpc/docs/subnets) in the location where you want to run the job. 
     * The network allows any access required for your job. If you block external access for a job's VMs, the network must use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) or [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) to allow access to the domains for the APIs and services that your job uses. For example, all jobs use the Batch and Compute Engine APIs and very often use the Cloud Logging API. 
For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 



## Create a job that blocks external access for all VMs

Block external access for a job's VMs when you are creating the job. When you block external access for all the VMs a job runs on, you also need to specify a network and subnet that allow the job to access required APIs.

If you want to [use a VM instance template while creating this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), you must specify the network and disable external IP addresses in the VM instance template. Otherwise, use the following steps to block external access for a job's VMs by using the gcloud CLI or Batch API.

### gcloud

To create a job that blocks external access using the gcloud CLI, select one of the following options:

  * Use gcloud flags to block external access for all VMs
  * Use JSON fields to block external access for all VMs



### Use gcloud flags to block external access for all VMs

To create a job and use gcloud flags to block external access for the job, complete the following steps:

  1. Create a JSON file that specifies your job's configuration details.

For example, to create a basic script job, create a JSON file with the following contents.
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "script": {
                       "text": "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                     }
                   }
                 ]
               },
               "taskCount": 3
             }
           ],
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

  2. Create the job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit). To block external access for all VMs, include the `--no-external-ip-address`, `--network`, and `--subnetwork` flags.
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE \
             --no-external-ip-address \
             --network projects/HOST_PROJECT_ID/global/networks/NETWORK \
             --subnetwork projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET
         

Replace the following:

     * `JOB_NAME`: the name for this job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) for this job.
     * `JSON_CONFIGURATION_FILE`: the path for the JSON file with the job's configuration details.
     * `HOST_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project for the network you specify: 
       * If you are using a Shared VPC network, specify the host project.
       * Otherwise, specify the current project.
     * `NETWORK`: the name of a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) in the current project or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the current project.
     * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where the subnet for the job and the job's Compute Engine resources are located. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).
     * `SUBNET`: the name of a [subnet](https://docs.cloud.google.com/vpc/docs/subnets) that is part of the VPC network and is located in the same region as the job's Compute Engine resources.



### Use JSON fields to block external access for all VMs

To create a job and use fields in the JSON configuration file to block external access for all VMs, complete the following steps:

  1. Create a JSON file that specifies your job's configuration details. To block external access for all VMs, do the following:

     * Set the [`noExternalIpAddress` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface) to `true`.

     * Specify the network for the job in the [`network` and `subnetwork` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface).

For example, to create a basic script job that block external access for all VMs, create a JSON file with the following contents.
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy": {
        "network": {
          "networkInterfaces": [
            {
              "network": "projects/HOST_PROJECT_ID/global/networks/NETWORK",
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET",
              "noExternalIpAddress": true
            }
          ]
        }
      },
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

     * `HOST_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project for the network you specify: 
       * If you are using a Shared VPC network, specify the host project.
       * Otherwise, specify the current project.
     * `NETWORK`: the name of a network that provides the access required for this job. The network must be either a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) in current project or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the current project.
     * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where the subnet for the job and the job's Compute Engine resources are located. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).
     * `SUBNET`: the name of a [subnet](https://docs.cloud.google.com/vpc/docs/subnets) that is part of the VPC network and is located in the same region as the job's Compute Engine resources.
  2. Create the job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name you want for this job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) you want for this job.
     * `JSON_CONFIGURATION_FILE`: the path for the JSON file with the job's configuration details.



### API

To create a job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify your job's configuration details. To block external access for all VMs, do the following:

  * Set the [`noExternalIpAddress` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface) to `true`.

  * Specify the network for the job in the [`network` and `subnetwork` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface).




For example, to create a basic script job that block external access for all VMs, make the following `POST` request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy": {
        "network": {
          "networkInterfaces": [
            {
              "network": "projects/HOST_PROJECT_ID/global/networks/NETWORK",
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET",
              "noExternalIpAddress": true
            }
          ]
        }
      },
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) you want for this job.
  * `JOB_NAME`: the name you want for this job.
  * `HOST_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project for the network you specify: 
    * If you are using a Shared VPC network, specify the host project.
    * Otherwise, specify the current project (`PROJECT_ID`).
  * `NETWORK`: the name of a network that provides the access required for this job. The network must be either a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) in current project or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the current project.
  * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where the subnet for the job and the job's Compute Engine resources are located. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).
  * `SUBNET`: the name of a [subnet](https://docs.cloud.google.com/vpc/docs/subnets) that is part of the VPC network and is located in the same region as the job's Compute Engine resources.



## Create a job that blocks external access for one or more containers

Block external access for any of a job's containers when you are creating the job.

You can block external access for any of job's containers by using the gcloud CLI or Batch API.

### gcloud

To create a job that blocks external access for one or more containers using the gcloud CLI, complete the following steps:

  1. Create a JSON file that specifies your job's configuration details. For each container in the job that you want to restrict, set the [`blockExternalNetwork` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container) to `true`.

For example, to create a basic container job that blocks external access for the container, create a JSON file with the following contents.
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "container": {
                       "imageUri": "gcr.io/google-containers/busybox",
                       "entrypoint": "/bin/sh",
                       "commands": [
                         "-c",
                         "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                       ],
                       "blockExternalNetwork": true
                     }
                   }
                 ]
               },
               "taskCount": 4,
               "parallelism": 2
             }
           ],
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

  2. Create the job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name you want for this job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) you want for this job.
     * `JSON_CONFIGURATION_FILE`: the path for the JSON file with the job's configuration details.



### API

To create a job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify your job's configuration details. For each container in the job that you want to restrict, set the [`blockExternalNetwork` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container) to `true`.

For example, to create a basic container job that blocks external access for the container, make the following `POST` request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "container": {
                  "imageUri": "gcr.io/google-containers/busybox",
                  "entrypoint": "/bin/sh",
                  "commands": [
                    "-c",
                    "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                  ],
                  "blockExternalNetwork": true
                }
              }
            ]
          },
          "taskCount": 4,
          "parallelism": 2
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) you want for this job.
  * `JOB_NAME`: the name you want for this job.



## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn more about [networking](https://docs.cloud.google.com/batch/docs/networking-overview).
  * Learn more about [creating a job](https://docs.cloud.google.com/batch/docs/create-run-job).
  * Learn how to [view jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
