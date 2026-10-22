---
url: https://docs.cloud.google.com/batch/docs/organize-resources-using-labels/
title: Organize resources using labels \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:28.498900+00:00
---

# Organize resources using labels  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/organize-resources-using-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Organize resources using labels Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use labels to organize your Batch resources.

Labels are key-value pairs that are applied to resources to group and describe them. Batch has _predefined labels_ , which are automatically applied to resources, and _custom labels_ , which you can define and apply when creating a job.

Labels allow you to filter the results of resource lists and Cloud Billing reports. For example, you can use labels to do the following:

  * Clarify and organize your project's list of jobs.

  * Distinguish a job's runnables by using labels to describe the type of container or script they specify.

  * Analyze costs by filtering Cloud Billing reports for the resources created by Batch or specific jobs.




For more information about labels, also see the [Compute Engine documentation for labels](https://docs.cloud.google.com/compute/docs/labeling-resources)

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Restrictions

In addition to the [requirements for labels](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements) specified in the Compute Engine documentation, applying labels to a Batch job and its resources has the following restrictions:

  * Batch only supports labels for resources that are created using Batch and of the following types:

    * Jobs

    * Runnables

    * [Graphics processing units (GPUs)](https://docs.cloud.google.com/batch/docs/create-run-job-gpus) for a job (if any)

    * Persistent disks ([boot disks](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks) and any [storage volumes](https://docs.cloud.google.com/batch/docs/create-run-job-storage)) for a job

    * Virtual machine (VM) instances for a job

  * After accounting for the predefined labels that Batch automatically applies to a job, you can define the following amounts of custom labels:

    * You can define a maximum of 63 custom labels to apply to the job and its runnables.

    * You can define a maximum of 61 custom labels to apply to each GPU, persistent disk, and VM created for the job.

  * Batch only supports defining custom labels with unique names. This has the following consequences:

    * Attempting to override a predefined label causes errors.

    * Defining a duplicate custom label overrides the existing custom label.

  * Batch only supports defining labels when creating a job.

    * Labels for jobs and runnables can't be added, updated, or removed.

    * Although it's possible to use Compute Engine to add, update, or remove labels for the persistent disks and VMs created for jobs, this is _not_ recommended. The timeframe that the resources for a job exist can't be reliably estimated, and any changes might not work correctly with Batch.

  * To use labels to filter your list of jobs, you must [view your list of jobs using the gcloud CLI or Batch API](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-jobs).




## Predefined labels

Each predefined label has a key that begins with the `batch-` prefix. By default, Batch automatically applies the following predefined labels:

  * To each job you create:

    * `batch-job-id`: The value of this label is set to the job's name.
  * To each GPU, persistent disk, and VM created for a job:

    * `batch-job-id`: The value of this label is set to the job's name.

    * `batch-job-uid`: The value of this label is set to the job's unique identifier (UID).

    * `batch-node`: The value of this label is null—it just groups all of the GPUs, persistent disks, and VMs that are created for jobs. For example, use this label when you [view a Cloud Billing report](https://cloud.google.com/batch/pricing#view-report) to identify the costs of all the GPUs, persistent disks, and VMs created by Batch.


**Note:** Batch has also created labels that let you optionally enable workarounds for known issues; for example, `goog-batch-skip-quota-check` and `goog-batch-allow-insecure-linux-headers-installation`. Consequently, we recommend that any custom labels that you define don't use the `goog-batch-` prefix. 

## Define custom labels

You can optionally define one or more custom labels when creating a job. You can define custom labels with new keys or keys that your project already uses. To define custom labels, select one or more of the following methods in this document based on the label's purpose:

  * Define custom labels for the job and its resources.

This section explains how to apply one or more custom labels to the job and to each GPU, persistent disk, and VM created for the job. After creating the job, you can use these labels to filter Cloud Billing reports and your project's lists of jobs, persistent disks, and VMs.

**Note:** The persistent disks and VMs created for a job only appear in your project's lists during the job's run time (after they are created and before they are deleted).
  * Define custom labels for the job.

This section explains how to apply one or more custom labels to the job. After creating the job, you can use these labels to filter your project's lists of jobs.

  * Define custom labels for runnables.

This section explains how to apply one or more custom labels to one or more runnables for the job. After creating the job, you can use these labels to filter your project's lists of jobs.




### Define custom labels for the job and its resources

Labels defined in the [`labels` field for a job's allocation policy](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#allocationpolicy) are applied to the job, as well as to each GPU (if any), persistent disk (all boot disks and any new storage volumes), and VM created for the job.

You can define labels for a job and its resources when creating a job using the gcloud CLI or Batch API.

### gcloud

For example, to create a basic container job in `us-central1` that defines two custom labels that apply to the job and the resources created for the job, follow these steps:

  1. Create a JSON file that specifies the job's configuration details and the [`allocationPolicy.labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#AllocationPolicy.FIELDS.labels).
         
         {
           "allocationPolicy": {
             "instances": [
               {
                 "policy": {
                   "machineType": "e2-standard-4"
                 }
               }
             ],
             **"labels" : {
               "VM_LABEL_NAME1": "VM_LABEL_VALUE1",
               "VM_LABEL_NAME2": "VM_LABEL_VALUE2"
             }**
           },
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
                         "echo Hello world!"
                       ]
                     }
                   }
                 ]
               }
             }
           ]
         }
         

Replace the following:

     * `VM_LABEL_NAME1`: The name of the first label to apply to the VMs created for the job.

     * `VM_LABEL_VALUE1`: The value of the first label to apply to the VMs created for the job.

     * `VM_LABEL_NAME2`: The name of the second label to apply to the VMs created for the job.

     * `VM_LABEL_VALUE2`: The value of the second label to apply to the VMs created for the job.

**Note:** To avoid confusing custom labels with predefined labels applied by Batch or other Google Cloud services, it's recommended to not specify label names that start with `batch-`, `goog-`, or `google-`.
  2. Create the job in `us-central1` using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit example-job \
             --config=JSON_CONFIGURATION_FILE \
             --location=us-central1
         

Replace `JSON_CONFIGURATION_FILE` with the path to the JSON file with the job's configuration details you created in the previous step.




### API

For example, to create a basic container job in `us-central1` that defines two custom labels that apply to the job and the resources created for the job, make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify the [`allocationPolicy.labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#AllocationPolicy.FIELDS.labels).
    
    
    POST https://batch.googleapis.com/v1/projects/example-project/locations/us-central1/jobs?job_id=example-job
    
    {
      "allocationPolicy": {
        "instances": [
          {
            "policy": {
              "machineType": "e2-standard-4"
            }
          }
        ],
        **"labels" : {
          "VM_LABEL_NAME1": "VM_LABEL_VALUE1",
          "VM_LABEL_NAME2": "VM_LABEL_VALUE2"
        }**
      },
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
                    "echo Hello world!"
                  ]
                }
              }
            ]
          }
        }
      ]
    }
    

Replace the following:

  * `VM_LABEL_NAME1`: The name of the first label to apply to the VMs created for the job.

  * `VM_LABEL_VALUE1`: The value of the first label to apply to the VMs created for the job.

  * `VM_LABEL_NAME2`: The name of the second label to apply to the VMs created for the job.

  * `VM_LABEL_VALUE2`: The value of the second label to apply to the VMs created for the job.


**Note:** To avoid confusing custom labels with predefined labels applied by Batch or other Google Cloud services, it's recommended to not specify label names that start with `batch-`, `goog-`, or `google-`.

###  Java 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateBatchAllocationPolicyLabel {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "us-central1";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "example-job";
        // Name of the label1 to be applied for your Job.
        String labelName1 = "VM_LABEL_NAME1";
        // Value for the label1 to be applied for your Job.
        String labelValue1 = "VM_LABEL_VALUE1";
        // Name of the label2 to be applied for your Job.
        String labelName2 = "VM_LABEL_NAME2";
        // Value for the label2 to be applied for your Job.
        String labelValue2 = "VM_LABEL_VALUE2";
    
        createBatchAllocationPolicyLabel(projectId, region, jobName, labelName1,
            labelValue1, labelName2, labelValue2);
      }
    
      // This method shows how to create a job with labels defined 
      // in the labels field of a job's allocation policy. These are 
      // applied to the job, as well as to each GPU (if any), persistent disk 
      // (all boot disks and any new storage volumes), and VM created for the job.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchAllocationPolicyLabel(String projectId, String region,
                                   String jobName, String labelName1,
                                   String labelValue1, String labelName2, String labelValue2)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setContainer_com_google_cloud_batch_v1_Runnable_Container_)(
                      [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).Container.newBuilder()
                          .[setImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_setImageUri_java_lang_String_)("gcr.io/google-containers/busybox")
                          .[setEntrypoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_setEntrypoint_java_lang_String_)("/bin/sh")
                          .[addCommands](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_addCommands_java_lang_String_)("-c")
                          .[addCommands](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_addCommands_java_lang_String_)(
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                  + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          .build())
                  .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(2000)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(2000)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(1).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).InstancePolicy.newBuilder().setMachineType("e2-standard-4").build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).InstancePolicyOrTemplate.newBuilder()
                      .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy)
                      .build())
                  // Labels and their value to be applied to the job and its resources
                  .putLabels(labelName1, labelValue1)
                  .putLabels(labelName2, labelValue2)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder()
                          .[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).Destination.CLOUD_LOGGING).build())
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-labels-allocation-job';
    // Name of the label1 to be applied for your Job.
    const labelName1 = 'vm_label_name_1';
    // Value for the label1 to be applied for your Job.
    const labelValue1 = 'vmLabelValue1';
    // Name of the label2 to be applied for your Job.
    const labelName2 = 'vm_label_name_2';
    // Value for the label2 to be applied for your Job.
    const labelValue2 = 'vmLabelValue2';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      script: new batch.Runnable.Script({
        commands: ['-c', 'echo Hello world! This is task ${BATCH_TASK_INDEX}.'],
      }),
    });
    
    // Specify what resources are requested by each task.
    const computeResource = new batch.ComputeResource({
      // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
      cpuMilli: 500,
      // In MiB.
      memoryMib: 16,
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable],
      computeResource,
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      machineType: 'e2-standard-4',
    });
    
    const allocationPolicy = new batch.AllocationPolicy({
      instances: [{policy: instancePolicy}],
    });
    // Labels and their value to be applied to the job and its resources.
    allocationPolicy.labels[labelName1] = labelValue1;
    allocationPolicy.labels[labelName2] = labelValue2;
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      labels: {env: 'testing', type: 'script'},
      allocationPolicy,
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchLabelsAllocation() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchLabelsAllocation();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_job_with_custom_allocation_policy_labels(
        project_id: str, region: str, job_name: str, labels: dict
    ) -> batch_v1.Job:
        """
        This method shows the creation of a Batch job with custom labels which describe the allocation policy.
        Args:
            project_id (str): project ID or project number of the Cloud project you want to use.
            region (str): name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            job_name (str): the name of the job that will be created.
            labels (dict): a dictionary of key-value pairs that will be used as labels
                E.g., {"label_key1": "label_value2", "label_key2": "label_value2"}
        Returns:
            batch_v1.Job: The created Batch job object containing configuration details.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.container = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Container](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Container.html)()
        runnable.container.image_uri = "gcr.io/google-containers/busybox"
        runnable.container.entrypoint = "/bin/sh"
        runnable.container.commands = [
            "-c",
            "echo Hello world!",
        ]
    
        # Create a task specification and assign the runnable and volume to it
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        task.runnables = [runnable]
    
        # Specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Create a task group and assign the task specification to it
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 3
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        # Assign the provided labels to the allocation policy
        allocation_policy.labels = labels
    
        # Create the job and assign the task group and allocation policy to it
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
    
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        # Create the job request and set the job and job ID
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

### Define custom labels for the job

Labels defined in the [`labels` field for the job](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#resource:-job) are only applied to the job.

You can define labels for a job when creating a job using the gcloud CLI or Batch API.

### gcloud

For example, to create a basic container job in `us-central1` that defines two custom labels that apply to the job itself, follow these steps:

  1. Create a JSON file that specifies the job's configuration details and the [`labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.labels).
         
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
                         "echo Hello World!"
                       ]
                     }
                   }
                 ]
               }
             }
           ],
           **"labels" : {
             "JOB_LABEL_NAME1": "JOB_LABEL_VALUE1",
             "JOB_LABEL_NAME2": "JOB_LABEL_VALUE2"
           }**
         }
         

Replace the following:

     * `JOB_LABEL_NAME1`: The name of the first label to apply to your job.

     * `JOB_LABEL_VALUE1`: The value of the first label to apply to your job.

     * `JOB_LABEL_NAME2`: The name of the second label to apply to your job.

     * `JOB_LABEL_VALUE2`: The value of the second label to apply to your job.

  2. Create the job in `us-central1` using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit) with the following flags:
         
         gcloud batch jobs submit example-job \
             --config=JSON_CONFIGURATION_FILE \
             --location=us-central1
         

Replace `JSON_CONFIGURATION_FILE` with the path to the JSON file with the job's configuration details you created in the previous step.




### API

For example, to create a container job in `us-central1` that defines two custom labels to apply to the jobs itself, make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify the [`labels` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.labels).
    
    
    POST https://batch.googleapis.com/v1/projects/example-project/locations/us-central1/jobs?job_id=example-job
    
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
                    "echo Hello World!"
                  ]
                }
              }
            ]
          }
        }
      ],
      **"labels" : {
        "JOB_LABEL_NAME1": "JOB_LABEL_VALUE1",
        "JOB_LABEL_NAME2": "JOB_LABEL_VALUE2"
      }**
    }
    

Replace the following:

  * `JOB_LABEL_NAME1`: The name of the first label to apply to your job.

  * `JOB_LABEL_VALUE1`: The value of the first label to apply to your job.

  * `JOB_LABEL_NAME2`: The name of the second label to apply to your job.

  * `JOB_LABEL_VALUE2`: The value of the second label to apply to your job.




###  Java 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    
    public class CreateBatchLabelJob {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "us-central1";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "example-job";
        // Name of the label1 to be applied for your Job.
        String labelName1 = "JOB_LABEL_NAME1";
        // Value for the label1 to be applied for your Job.
        String labelValue1 = "JOB_LABEL_VALUE1";
        // Name of the label2 to be applied for your Job.
        String labelName2 = "JOB_LABEL_NAME2";
        // Value for the label2 to be applied for your Job.
        String labelValue2 = "JOB_LABEL_VALUE2";
    
        createBatchLabelJob(projectId, region, jobName, labelName1,
            labelValue1, labelName2, labelValue2);
      }
    
      // Creates a job with labels defined in the labels field.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchLabelJob(String projectId, String region, String jobName,
                        String labelName1, String labelValue1, String labelName2, String labelValue2)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setContainer_com_google_cloud_batch_v1_Runnable_Container_)(
                      [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).Container.newBuilder()
                          .[setImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_setImageUri_java_lang_String_)("gcr.io/google-containers/busybox")
                          .[setEntrypoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_setEntrypoint_java_lang_String_)("/bin/sh")
                          .[addCommands](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_addCommands_java_lang_String_)("-c")
                          .[addCommands](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_addCommands_java_lang_String_)(
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                  + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          .build())
                  .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(2000)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(2000)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(1).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder()
                  .[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).Destination.CLOUD_LOGGING).build())
                  // Labels and their value to be applied to the job.
                  .putLabels(labelName1, labelValue1)
                  .putLabels(labelName2, labelValue2)
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'batch-labels-job';
    // Name of the label1 to be applied for your Job.
    const labelName1 = 'job_label_name_1';
    // Value for the label1 to be applied for your Job.
    const labelValue1 = 'job_label_value1';
    // Name of the label2 to be applied for your Job.
    const labelName2 = 'job_label_name_2';
    // Value for the label2 to be applied for your Job.
    const labelValue2 = 'job_label_value2';
    
    // Define what will be done as part of the job.
    const runnable = new batch.Runnable({
      container: new batch.Runnable.Container({
        imageUri: 'gcr.io/google-containers/busybox',
        entrypoint: '/bin/sh',
        commands: ['-c', 'echo Hello world! This is task ${BATCH_TASK_INDEX}.'],
      }),
    });
    
    // Specify what resources are requested by each task.
    const computeResource = new batch.ComputeResource({
      // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
      cpuMilli: 500,
      // In MiB.
      memoryMib: 16,
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable],
      computeResource,
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    
    // Labels and their value to be applied to the job and its resources.
    job.labels[labelName1] = labelValue1;
    job.labels[labelName2] = labelValue2;
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchLabelsJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchLabelsJob();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_job_with_custom_job_labels(
        project_id: str,
        region: str,
        job_name: str,
        labels: dict,
    ) -> batch_v1.Job:
        """
        This method creates a Batch job with custom labels.
        Args:
            project_id (str): project ID or project number of the Cloud project you want to use.
            region (str): name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            job_name (str): the name of the job that will be created.
            labels (dict): A dictionary of custom labels to be added to the job.
                E.g., {"label_key1": "label_value2", "label_key2": "label_value2"}
        Returns:
            batch_v1.Job: The created Batch job object containing configuration details.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.container = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Container](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Container.html)()
        runnable.container.image_uri = "gcr.io/google-containers/busybox"
        runnable.container.entrypoint = "/bin/sh"
        runnable.container.commands = [
            "-c",
            "echo Hello world!",
        ]
    
        # Create a task specification and assign the runnable and volume to it
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        task.runnables = [runnable]
    
        # Specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Create a task group and assign the task specification to it
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 3
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        # Create the job and assign the task group and allocation policy to it
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
    
        # Set the labels for the job
        job.labels = labels
    
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        # Create the job request and set the job and job ID
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

### Define custom labels for runnables

Labels defined in the [`labels` field for a runnable](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#runnable) are only applied to that runnable.

You can define labels for one or more runnables when creating a job using the gcloud CLI or Batch API.

### gcloud

For example, to create a job in `us-central1` that defines two custom labels, one custom label for each of the two job's runnables, follow these steps:

  1. Create a JSON file that specifies the job's configuration details and the [`runnables.labels` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Runnable.FIELDS.labels).
         
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
                         "echo Hello from task ${BATCH_TASK_INDEX}!"
                       ]
                     },
                     **"labels" : {
                       "RUNNABLE1_LABEL_NAME1": "RUNNABLE1_LABEL_VALUE1"
                     }**
                   },
                   {
                     "script": {
                       "text": "echo Hello from task ${BATCH_TASK_INDEX}!"
                     },
                     **"labels" : {
                       "RUNNABLE2_LABEL_NAME1": "RUNNABLE2_LABEL_VALUE1"
                     }**
                   }
                 ]
               }
             }
           ]
         }
         

Replace the following:

     * `RUNNABLE1_LABEL_NAME1`: The name of the label to apply to the first runnable of the job.

     * `RUNNABLE1_LABEL_VALUE1`: The value of the label to apply to the first runnable of the job.

     * `RUNNABLE2_LABEL_NAME1`: The name of the label to apply to the second runnable of the job.

     * `RUNNABLE2_LABEL_VALUE1`: The value of the label to apply to the second runnable of the job.

  2. Create the job in `us-central1` using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit example-job \
             --config=JSON_CONFIGURATION_FILE \
             --location=us-central1
         

Replace `JSON_CONFIGURATION_FILE` with the path to the JSON file with the job's configuration details you created in the previous step.




### API

For example, to create a job in `us-central1` that defines two custom labels, one for each of the two job's runnables, make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify the [`runnables.labels` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Runnable.FIELDS.labels).
    
    
    POST https://batch.googleapis.com/v1/projects/example-project/locations/us-central1/jobs?job_id=example-job
    
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
                    "echo Hello from ${BATCH_TASK_INDEX}!"
                  ]
                },
                **"labels" : {
                  "RUNNABLE1_LABEL_NAME1": "RUNNABLE1_LABEL_VALUE1"
                }**
              },
              {
                "script": {
                  "text": "echo Hello from ${BATCH_TASK_INDEX}!"
                },
                **"labels" : {
                  "RUNNABLE2_LABEL_NAME1": "RUNNABLE2_LABEL_VALUE1"
                }**
              }
            ]
          }
        }
      ]
    }
    

Replace the following:

  * `RUNNABLE1_LABEL_NAME1`: The name of the label to apply to the first job's runnable.

  * `RUNNABLE1_LABEL_VALUE1`: The value of the label to apply to the first job's runnable.

  * `RUNNABLE2_LABEL_NAME1`: The name of the label to apply to the second job's runnable.

  * `RUNNABLE2_LABEL_VALUE1`: The value of the label to apply to the second job's runnable.




###  Java 
    
    
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateBatchRunnableLabel {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "us-central1";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "example-job";
        // Name of the label1 to be applied for your Job.
        String labelName1 = "RUNNABLE_LABEL_NAME1";
        // Value for the label1 to be applied for your Job.
        String labelValue1 = "RUNNABLE_LABEL_VALUE1";
        // Name of the label2 to be applied for your Job.
        String labelName2 = "RUNNABLE_LABEL_NAME2";
        // Value for the label2 to be applied for your Job.
        String labelValue2 = "RUNNABLE_LABEL_VALUE2";
    
        createBatchRunnableLabel(projectId, region, jobName, labelName1,
            labelValue1, labelName2, labelValue2);
      }
    
      // Creates a job with labels defined in the labels field
      // for a runnable. The labels are only applied to that runnable.
      // In Batch, a runnable represents a single task or unit of work within a job.
      // It can be a container (like a Docker image) or a script.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchRunnableLabel(String projectId, String region, String jobName,
                       String labelName1, String labelValue1, String labelName2, String labelValue2)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setContainer_com_google_cloud_batch_v1_Runnable_Container_)(
                      [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).Container.newBuilder()
                          .[setImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_setImageUri_java_lang_String_)("gcr.io/google-containers/busybox")
                          .[setEntrypoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_setEntrypoint_java_lang_String_)("/bin/sh")
                          .[addCommands](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_addCommands_java_lang_String_)("-c")
                          .[addCommands](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder.html#com_google_cloud_batch_v1_Runnable_Container_Builder_addCommands_java_lang_String_)(
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                  + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          .build())
                  // Label and its value to be applied to the container
                  // that processes data from a specific region.
                  .putLabels(labelName1, labelValue1)
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)([Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).Script.newBuilder()
                  .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)("echo Hello world! This is task ${BATCH_TASK_INDEX}. ").build())
                  // Label and its value to be applied to the script
                  // that performs some analysis on the processed data.
                  .putLabels(labelName2, labelValue2)
                  .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(2000)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(2000)
                  .build();
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task =
              [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
                  // Jobs can be divided into tasks. In this case, we have only one task.
                  .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
                  .[setComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setComputeResource_com_google_cloud_batch_v1_ComputeResource_)(computeResource)
                  .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
                  .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(1).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder()
                  .[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).Destination.CLOUD_LOGGING).build())
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html).newBuilder()
                  // The job's parent is the region in which the job will run for the specific project.
                  .setParent(String.format("projects/%s/locations/%s", projectId, region))
                  .setJob(job)
                  .[setJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder.html#com_google_cloud_batch_v1_CreateJobRequest_Builder_setJobId_java_lang_String_)(jobName)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) result =
              batchServiceClient
                  .[createJobCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html#com_google_cloud_batch_v1_BatchServiceClient_createJobCallable__)()
                  .futureCall(createJobRequest)
                  .get(5, TimeUnit.MINUTES);
    
          System.out.printf("Successfully created the job: %s", result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getName__)());
    
          return result;
        }
      }
    
    }

###  Node.js 
    
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await batchClient.getProjectId();
    // Name of the region you want to use to run the job. Regions that are
    // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
    const region = 'us-central1';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'example-job';
    // Name of the label1 to be applied for your Job.
    const labelName1 = 'RUNNABLE_LABEL_NAME1';
    // Value for the label1 to be applied for your Job.
    const labelValue1 = 'RUNNABLE_LABEL_VALUE1';
    // Name of the label2 to be applied for your Job.
    const labelName2 = 'RUNNABLE_LABEL_NAME2';
    // Value for the label2 to be applied for your Job.
    const labelValue2 = 'RUNNABLE_LABEL_VALUE2';
    
    const container = new batch.Runnable.Container({
      imageUri: 'gcr.io/google-containers/busybox',
      entrypoint: '/bin/sh',
      commands: ['-c', 'echo Hello world! This is task ${BATCH_TASK_INDEX}.'],
    });
    
    const script = new batch.Runnable.Script({
      commands: ['-c', 'echo Hello world! This is task ${BATCH_TASK_INDEX}.'],
    });
    
    const runnable1 = new batch.Runnable({
      container,
      // Label and its value to be applied to the container
      // that processes data from a specific region.
      labels: {
        [labelName1]: labelValue1,
      },
    });
    
    const runnable2 = new batch.Runnable({
      script,
      // Label and its value to be applied to the script
      // that performs some analysis on the processed data.
      labels: {
        [labelName2]: labelValue2,
      },
    });
    
    // Specify what resources are requested by each task.
    const computeResource = new batch.ComputeResource({
      // In milliseconds per cpu-second. This means the task requires 50% of a single CPUs.
      cpuMilli: 500,
      // In MiB.
      memoryMib: 16,
    });
    
    const task = new batch.TaskSpec({
      runnables: [runnable1, runnable2],
      computeResource,
      maxRetryCount: 2,
      maxRunDuration: {seconds: 3600},
    });
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup({
      taskCount: 3,
      taskSpec: task,
    });
    
    const job = new batch.Job({
      name: jobName,
      taskGroups: [group],
      // We use Cloud Logging as it's an option available out of the box
      logsPolicy: new batch.LogsPolicy({
        destination: batch.LogsPolicy.Destination.CLOUD_LOGGING,
      }),
    });
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateBatchLabelsRunnable() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const [response] = await batchClient.createJob(request);
      console.log(JSON.stringify(response));
    }
    
    await callCreateBatchLabelsRunnable();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_job_with_custom_runnables_labels(
        project_id: str,
        region: str,
        job_name: str,
        labels: dict,
    ) -> batch_v1.Job:
        """
        This method creates a Batch job with custom labels for runnable.
        Args:
            project_id (str): project ID or project number of the Cloud project you want to use.
            region (str): name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            job_name (str): the name of the job that will be created.
            labels (dict): a dictionary of key-value pairs that will be used as labels
                E.g., {"label_key1": "label_value2"}
        Returns:
            batch_v1.Job: The created Batch job object containing configuration details.
        """
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.display_name = "Script 1"
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world from Script 1 for task ${BATCH_TASK_INDEX}"
        # Add custom labels to the first runnable
        runnable.labels = labels
    
        # Create a task specification and assign the runnable and volume to it
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        task.runnables = [runnable]
    
        # Specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Create a task group and assign the task specification to it
        group = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.html)()
        group.task_count = 3
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy.html)()
        policy.machine_type = "e2-standard-4"
        instances = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate.html)()
        instances.policy = policy
        allocation_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html)()
        allocation_policy.instances = [instances]
    
        # Create the job and assign the task group and allocation policy to it
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
    
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        # Create the job request and set the job and job ID
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

## What's next

  * Use labels as filters when you do the following:

    * [View a list of your jobs](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-jobs).

    * [View Cloud Billing reports](https://cloud.google.com/batch/pricing#view-billing-report).

    * [View a list of persistent disks or VMs](https://docs.cloud.google.com/compute/docs/labeling-resources#filter).

  * Learn how to [delete jobs](https://docs.cloud.google.com/batch/docs/delete-job).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
