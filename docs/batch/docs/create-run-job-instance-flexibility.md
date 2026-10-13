---
url: https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility/
title: Improve obtainability by using instance flexibility \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:50.522600+00:00
---

# Improve obtainability by using instance flexibility  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Improve obtainability by using instance flexibility Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create and run a Batch job that uses instance flexibility. Instance flexibility lets you allow a job to run on multiple machine types that you specify and can optionally rank.

By allowing more machine types for a job, you can use instance flexibility to improve _obtainability_ , which is the probability that resources are available to run your job. For more information about choosing which obtainability features to use for your workload, see [Improve resource obtainability](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview). For example, using instance flexibility can help you do the following:

  * Reduce the probability of [resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability) and related scheduling delays.
  * Select resources with higher obtainability to help jobs finish sooner—for example: 
    * Increase the probability of obtaining more instances for jobs that support [parallel processing](https://docs.cloud.google.com/batch/docs/create-run-job#vms-per-job).
    * Obtain [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) that are less likely to be preempted.



## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Restrictions

When a job uses instance flexibility, all of the following restrictions apply:

  * Obtainability improvement increases with the number of machine types that you allow a job to use.

**Important:** If a job doesn't have any machine type requirements, then, instead of using instance flexibility, you can improve obtainability even more by omitting the machine type entirely. However, you can't omit the machine type when creating a job through the Google Cloud console or when creating a job that uses an instance template.
  * The job can't specify the `FLEX_START` provisioning model or `RESERVATION_BOUND` provisioning model.

  * The job can't consume a specifically targeted reservation. (The [`reservation` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicy) must be undefined or set to `NO_RESERVATION`.)

A specifically targeted reservation includes all reservations for the `RESERVATION_BOUND` provisioning model and some reservations for the `STANDARD` provisioning model. These features are inherently incompatible because instance creation can only succeed for the reservation's machine type.

  * Each job can have up to 50 instance selections.

  * Each instance selection in a job must have a unique name, a unique rank, and one or more unique machine types.

  * Machine types can't repeat; include each machine type in only one instance selection per job.

  * Each job can have up to 200 unique machine types across its instance selections.

  * Although specifying multiple machine types in the same instance selection is optional, it is required if you want resources with higher obtainability.

    * Batch attempts to select one or more machine types with the highest obtainability only when the instance selection for a rank has multiple machine types. For example, this selection is important if you want your job to have Spot VMs that are less likely to be preempted or more instances for a job that can run tasks in parallel.
    * Otherwise, when the instance selection for a rank only has one machine type, instance flexibility only helps prevent resource availability errors.
  * The job can't include the [`machineType` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs#instancepolicy), and the machine type for any instance template that the job specifies is ignored.

  * You must verify that every property that you specify for the job is compatible with every allowed machine type. Otherwise, the job might fail after being submitted because it can't create instances. For example, we recommend you verify that at least the following properties for a job are compatible with all machine types:

    * location (if specified, `allowedLocations[]` field; otherwise `location`)
    * compute resources per task (`computeResource` field)
    * disks and images (`volumes[]` field, `disk[]` field, and `bootDisk` field)
    * network (`network` field)
    * all other instance properties (`instances[]` subfields):

      * minimum CPU platform (`minCpuPlatform` field)
      * provisioning model (`provisioningModel` field)
      * GPUs (`accelerators[]` field)
  * You can't [override disks and minimum CPU platforms](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#overrides-for-instance-properties) for Batch jobs. All machine types use either your specified values (in the `policy` subfields or an instance template) or, if unspecified, use the default values for a machine type in the highest-priority instance selection. Consequently, we recommend you do all of the following:

    * Verify that the boot disk type is compatible for every allowed machine type. In summary, 4th generation and later machine types don't support persistent disks, 2nd generation and earlier machine types don't support Hyperdisk, and 3rd generation and earlier machine types use persistent boot disks by default.

**Key Point:** You can't combine 4th generation and later machine types with 2nd generation and earlier machine types due to boot disk incompatibilities. To combine 3rd generation machine types with later machine types, ensure the boot disk type is a Hyperdisk.
    * Don't specify a minimum CPU platform or optional disks unless you've verified that they are supported for every allowed machine type.




## Create a job that is allowed to use multiple machine types

To [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job) that is allowed to use multiple machine types, select one of the following methods.

###  gcloud 

To configure multiple machine types while using the Google Cloud CLI to create a job, complete the following steps:

  1. Include the [`instanceFlexibilityPolicy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs#allocationpolicy) and [subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs#instanceflexibilitypolicy) in the `allocationPolicy` field in the JSON file that specifies your job's configuration details. The `instanceFlexibilityPolicy` field supports one or more instance selections, which each have a unique name, a unique rank, and a list of one or more machine types.
         
         "allocationPolicy":{
           "instanceFlexibilityPolicy":{
             "instanceSelections":{
               "INSTANCE_SELECTION_NAME":{
                 "rank": RANK,
                 "machineTypes": [MACHINE_TYPES]
               }
             }
           }
         }
         

Replace the following:

     * `INSTANCE_SELECTION_NAME`: a name for the instance selection. If the job has multiple instance selections, then ensure each name in this job is unique.

     * `RANK`: Optional: an integer of zero or greater that represents the priority for this instance selection, where the lowest value is the highest priority. If not specified, the default value is `0` (highest priority). If the job has multiple instance selections, then ensure each rank in this job is unique.

     * `MACHINE_TYPES`: a comma-separated list of one or more machine types, which are written as strings, for this instance selection. You can include each machine type in only one instance selection per job. For example, a list of three machine types can be written as follows:
           
           "MACHINE_TYPE_1", "MACHINE_TYPE_2", "MACHINE_TYPE_3"
           

Replace `MACHINE_TYPE_1`, `MACHINE_TYPE_2`, `MACHINE_TYPE_3` each with a machine type—for example, `e2-micro`, `e2-small`, and `n1-standard-2`.

For more information, also see the example job.

  2. While this feature is in [Preview](https://cloud.google.com/products#product-launch-stages), you must use the [`gcloud alpha batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/submit) to create and submit the job.
         
         gcloud alpha batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



###  REST 

To use the Batch API to create a job that uses multiple machine types, use the [v1alpha `jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs/create) while this feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

To specify multiple machine types for a job, include the [`instanceFlexibilityPolicy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs#allocationpolicy) and [subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs#instanceflexibilitypolicy) in the `allocationPolicy` field in the main body in the JSON file. The `instanceFlexibilityPolicy` field supports one or more instance selections, which each have a unique name, a unique rank, and a list of one or more machine types.
    
    
    "allocationPolicy":{
      "instanceFlexibilityPolicy":{
        "instanceSelections":{
          "INSTANCE_SELECTION_NAME":{
            "rank": RANK,
            "machineTypes": [MACHINE_TYPES]
          }
        }
      }
    }
    

Replace the following:

  * `INSTANCE_SELECTION_NAME`: a name for the instance selection. If the job has multiple instance selections, then ensure each name in this job is unique.

  * `RANK`: Optional: an integer of zero or greater that represents the priority for this instance selection, where the lowest value is the highest priority. If not specified, the default value is `0` (highest priority). If the job has multiple instance selections, then ensure each rank in this job is unique.

  * `MACHINE_TYPES`: a comma-separated list of one or more machine types, which are written as strings, for this instance selection. You can include each machine type in only one instance selection per job. For example, a list of three machine types can be written as follows:
        
        "MACHINE_TYPE_1", "MACHINE_TYPE_2", "MACHINE_TYPE_3"
        

Replace `MACHINE_TYPE_1`, `MACHINE_TYPE_2`, `MACHINE_TYPE_3` each with a machine type—for example, `e2-micro`, `e2-small`, and `n1-standard-2`.




For more information, also see the example job.

### Example job JSON configuration file

For example, when using the gcloud CLI or Batch API, you can use the following JSON configuration file to create a basic script job that has two instance selections:

  * The instance selection named `first-choice` has the top priority (`"rank": 0`) and three machine types (`e2-micro`, `e2-small`, and `n1-standard-2`).
  * The instance selection named `second-choice` has the second priority (`"rank": 1`) and one machine type (`e2-medium`).


    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello World! This is task $BATCH_TASK_INDEX."
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy":{
        "instanceFlexibilityPolicy":{
          "instanceSelections":{
            "first-choice":{
              "rank": 0,
              "machineTypes": ["e2-micro", "e2-small", "n1-standard-2"]
            },
            "second-choice":{
              "rank": 1,
              "machineTypes": ["e2-medium"]
            }
          }
        }
      }
    }
    

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
