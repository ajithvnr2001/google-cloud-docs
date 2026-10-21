---
url: https://docs.cloud.google.com/batch/docs/create-run-basic-job/
title: Create and run a basic job \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:20.359857+00:00
---

# Create and run a basic job  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-basic-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run a basic job Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the basics for Batch job creation: how to create and run a job that is based on a script or container image and use predefined and custom variables. To learn more about creating and running jobs, see [Job creation and execution overview](https://docs.cloud.google.com/batch/docs/create-run-job).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. Each time you create a job, make sure the job has a valid resource configuration. 
     * Unless the default values are sufficient, you must specify the compute resources per task (`computeResource`) fields required for each task to run, as shown in this document.
     * If you specify any VM resources for a job (any `instances[].policy`, `instances[].instanceTemplate`, or `instanceFlexibilityPolicy` field), you must make sure that these fields are compatible with each other and the job.
For more information about resource configuration for jobs, see [Job resources](https://docs.cloud.google.com/batch/docs/create-run-job#resources).
  4. Each time you create a job, make sure the job has a valid network configuration. 
     * If you don't have any specific networking requirements for your workload or project and you haven't modified the default network for your project, no action is required. 
     * Otherwise, you need to configure networking when you create a job. Learn how to configure networking for a job before you create a basic job, so you can modify the examples below to meet your networking requirements. 
For more information about the network configuration for a job, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview). 
  5. Each time you create a job, make sure the job has a valid VM operating system (OS) environment. 
     * If you don't have any specific VM OS image or boot disk requirements for your workload or project, no action is required. 
     * Otherwise, you need to prepare a valid VM OS environment option. Before creating a basic job, either allow the default configuration for the VM OS environment or learn how to customize the VM OS environment so you can modify the examples below to meet your requirements. 
For more information about the VM OS environment for a job, see [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview). 



## Create a basic job

For information about all the fields you can specify for a job, see the reference documentation for the [`projects.locations.jobs` REST resource](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs). To summarize, a job consists of [an array of one or more tasks](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#taskgroup) that all run one or more [runnables](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#runnable), which are the executable script(s) and/or container(s) for your job. To cover the basics, this section explains how to create an example job with just one runnable, either a script or a container image:

  * If you want to use Batch to write jobs that run a container image, see create a container job.
  * Otherwise, if you aren't sure if you want to use container images or if you are unfamiliar with containers, creating a script job is recommended.



The example job for both types of jobs contains a task group with an array of 4 tasks. Each task prints a message and its index to the standard output and Cloud Logging. The definition for this job specifies a parallelism of 2, which indicates that the job should run on 2 VMs to allow 2 tasks to run at a time.

### Create a basic container job

You can select or create a container image to provide the code and dependencies for your job to run from any compute environment. For more information, see [Working with container images](https://docs.cloud.google.com/artifact-registry/docs/docker) and [Running containers on VM instances](https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-container-instance).

You can create a basic container job using the Google Cloud console, gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

### Console

**Important:** Some options for job creation aren't available in the Google Cloud console. For details, see [Job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options). For more features and flexibility for creating jobs, use the gcloud CLI or Batch API instead.

To create a basic container job using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-basic-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, to add one container, do the following:

           1. Select **Container image URL** (default).

           2. In the **Container image URL** field, enter the URL for a container image that you want to run for each task in this job.

For example, to use the [`busybox` Docker container image](https://busybox.net/), enter the following URL:
                  
                  gcr.io/google-containers/busybox
                  

           3. Optional: To override the container image's `ENTRYPOINT` command, enter a command in the **Entry point** field.

For example, enter the following:
                  
                  /bin/sh
                  

           4. Optional: To override the container image's `CMD` command, do the following:

              1. Select the **Override container image's CMD command** checkbox. A field appears.

              2. In the field, enter one or more commands, separating each command with a new line.

For example, enter the following commands:
                     
                     -c
                     echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.
                     

              3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits).

For example, enter `4`.

        3. In the **Parallelism** field, enter the number of tasks to run concurrently. The number cannot be larger than the total number of tasks and must be a whole number between `1` and the [parallel tasks per job limit](https://docs.cloud.google.com/batch/quotas#job_limits).

For example, enter `2`.

  4. Configure the **Resource specifications** page:

     1. In the left pane, click **Resource specifications**. The **Resource specifications** page opens.

     2. In the **VM provisioning model** section, select one of the following options for the [provisioning model](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#select-provisioning-method) for this job's VMs:

        * If your job can withstand preemption and you want discounted VMs, select **Spot**. Learn more about [recommendations for Spot VMs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview#spot-vms-recommendations).

        * Otherwise, select **Standard**.

For example, select **Standard** (default).

     3. Select the [location](https://docs.cloud.google.com/batch/docs/locations) for this job:

        1. In the **Region** field, select a region.

For example, select **`us-central1 (Iowa)`** (default).

        2. In the **Zone** field, do one of the following:

           * If you want to restrict this job to run in a specific zone only, select a zone.

           * Otherwise, select **any**.

For example, select **any** (default).

     4. Select one of the following [machine families](https://docs.cloud.google.com/compute/docs/machine-resource):

        * For common workloads, click **General purpose**.

        * For performance-intensive workloads, click **Compute optimized**.

        * For memory-intensive workloads, click **Memory optimized**.

        * For accelerator-optimized workloads, click **GPUs**. For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

For example, click **General purpose** (default).

     5. In the **Series** field, select a [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) for this job's VMs.

For example, if you selected **General purpose** for the machine family, select **E2** (default).

     6. In the **Machine type** field, select a machine type for this job's VMs.

For example, if you selected **E2** for the machine series, select **e2-medium (2 vCPU, 4 GB memory)** (default).

     7. Configure the amount of VM resources required for each task:

        1. In the **Cores** field, enter the amount of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms) per task.

For example, enter `1` (default).

        2. In the **Memory** field, enter the amount of RAM in GB per task.

For example, enter `0.5` (default).

  5. Optional: To review the job configuration, in the left pane, click **Preview**.

  6. Click **Create**.




The **Job details** page displays the job that you created.

### gcloud

To create a basic container job using the gcloud CLI, do the following:

  1. Create a JSON file that specifies your job's configuration details. For example, to create a basic container job, create a JSON file with the following contents. For more information about all the fields you can specify for a job, see the reference documentation for the [`projects.locations.jobs` REST resource](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs).

**Note:** If you prefer, you can specify your job's configuration details in a YAML file instead of a JSON file by converting JSON syntax to YAML syntax yourself. However, the Batch documentation only provides examples for JSON syntax. For more information, see the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "container": {
                                     CONTAINER
                                 }
                             }
                         ],
                         "computeResource": {
                             "cpuMilli": CORES,
                             "memoryMib": MEMORY
                         },
                         "maxRetryCount": MAX_RETRY_COUNT,
                         "maxRunDuration": "MAX_RUN_DURATION"
                     },
                     "taskCount": TASK_COUNT,
                     "parallelism": PARALLELISM
                 }
             ]
         }
         

Replace the following:

     * `CONTAINER`: the container that each task runs. At minimum, a container must specify an image in the `imageUri` subfield, but additional subfields might also be required. For more information, see the [`container` subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container) and the example container job in this section.
     * `CORES`: Optional. The amount of cores—specifically [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms), which usually represent half a physical core—to allocate for each task in milliCPU units. If the `cpuMilli` field is not specified, the value is set to `2000` (2 vCPUs).
     * `MEMORY`: Optional. The amount of memory to allocate for each task in MB. If the `memoryMib` field is not specified, the value is set to `2000` (2 GB).
     * `MAX_RETRY_COUNT`: Optional. The maximum number of retries for a task. The value must be a whole number between `0` and `10`. If the `maxRetryCount` field is not specified, the value is set to `0`, which means to not retry the task. For more information about the `maxRetryCount` field, see [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).
     * `MAX_RUN_DURATION`: Optional. The maximum time a task is allowed to run before being retried or failing, formatted as a value in seconds followed by `s`—for example, `3600s` for 1 hour. If the `maxRunDuration` field is not specified, the value is set to the [maximum run time for a job](https://docs.cloud.google.com/batch/quotas#max-job-duration). For more information about the `maxRunDuration` field, see [Limit run times for tasks and runnables using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).
     * `TASK_COUNT`: Optional. The number of tasks for the job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `taskCount` field is not specified, the value is set to `1`.
     * `PARALLELISM`: Optional. The number of tasks the job runs concurrently. The number cannot be larger than the number of tasks and must be a whole number between `1` and the [parallel tasks per job limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `parallelism` field is not specified, the value is set to `1`.
  2. Create a job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



For example, to create a job that runs tasks using the [`busybox` Docker container image](https://busybox.net/):

  1. Create a JSON file in the current directory named `hello-world-container.json` with the following contents:
         
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
                                     ]
                                 }
                             }
                         ],
                         "computeResource": {
                             "cpuMilli": 2000,
                             "memoryMib": 16
                         },
                         "maxRetryCount": 2,
                         "maxRunDuration": "3600s"
                     },
                     "taskCount": 4,
                     "parallelism": 2
                 }
             ],
             "allocationPolicy": {
                 "instances": [
                     {
                         "policy": { "machineType": "e2-standard-4" }
                     }
                 ]
             },
             "labels": {
                 "department": "finance",
                 "env": "testing"
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

  2. Run the following command:
         
         gcloud batch jobs submit example-container-job \
           --location us-central1 \
           --config hello-world-container.json
         




### API

To create a basic container job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create). For more information about all the fields you can specify for a job, see the reference documentation for the [`projects.locations.jobs` REST resource](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs).
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "container": {
                                CONTAINER
                            }
                        }
                    ],
                    "computeResource": {
                        "cpuMilli": CORES,
                        "memoryMib": MEMORY
                    },
                    "maxRetryCount": MAX_RETRY_COUNT,
                    "maxRunDuration": "MAX_RUN_DURATION"
                },
                "taskCount": TASK_COUNT,
                "parallelism": PARALLELISM
            }
        ]
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
  * `JOB_NAME`: the name of the job.
  * `CONTAINER`: the container that each task runs. At minimum, a container must specify an image in the `imageUri` subfield, but additional subfields might also be required. For more information, see the [`container` subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#container) and the example container job in this section.
  * `CORES`: Optional. The amount of cores—specifically [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms), which usually represent half a physical core—to allocate for each task in milliCPU units. If the `cpuMilli` field is not specified, the value is set to `2000` (2 vCPUs).
  * `MEMORY`: Optional. The amount of memory to allocate for each task in MB. If the `memoryMib` field is not specified, the value is set to `2000` (2 GB).
  * `MAX_RETRY_COUNT`: Optional. The maximum number of retries for a task. The value must be a whole number between `0` and `10`. If the `maxRetryCount` field is not specified, the value is set to `0`, which means to not retry the task. For more information about the `maxRetryCount` field, see [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).
  * `MAX_RUN_DURATION`: Optional. The maximum time a task is allowed to run before being retried or failing, formatted as a value in seconds followed by `s`—for example, `3600s` for 1 hour. If the `maxRunDuration` field is not specified, the value is set to the [maximum run time for a job](https://docs.cloud.google.com/batch/quotas#max-job-duration). For more information about the `maxRunDuration` field, see [Limit run times for tasks and runnables using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).
  * `TASK_COUNT`: Optional. The number of tasks for the job, which must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `taskCount` field is not specified, the value is set to `1`.
  * `PARALLELISM`: Optional. The number of tasks the job runs concurrently. The number cannot be larger than the number of tasks and must be a whole number between `1` and the [parallel tasks per job limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `parallelism` field is not specified, the value is set to `1`.



For example, to create a job that runs tasks using the [`busybox` Docker container image](https://busybox.net/), use the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs?job_id=example-container-job
    
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
                                ]
                            }
                        }
                    ],
                    "computeResource": {
                        "cpuMilli": 2000,
                        "memoryMib": 16
                    },
                    "maxRetryCount": 2,
                    "maxRunDuration": "3600s"
                },
                "taskCount": 4,
                "parallelism": 2
            }
        ],
        "allocationPolicy": {
            "instances": [
                {
                    "policy": { "machineType": "e2-standard-4" }
                }
            ]
        },
        "labels": {
            "department": "finance",
            "env": "testing"
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

where `PROJECT_ID` is the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

###  Go 

### Go

For more information, see the [Batch Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job that runs the specified container
    func createContainerJob(w io.Writer, projectID, region, jobName string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	container := &batchpb.Runnable_Container{
    		ImageUri:   "gcr.io/google-containers/busybox",
    		Commands:   []string{"-c", "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."},
    		Entrypoint: "/bin/sh",
    	}
    
    	// We can specify what resources are requested by each task.
    	resources := &batchpb.ComputeResource{
    		// CpuMilli is milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    		CpuMilli:  2000,
    		MemoryMib: 16,
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		Runnables: []*batchpb.Runnable{{
    			Executable: &batchpb.Runnable_Container_{Container: container},
    		}},
    		ComputeResource: resources,
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    	}
    
    	// Tasks are grouped inside a job using TaskGroups.
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	// Policies are used to define on what kind of virtual machines the tasks will run on.
    	// In this case, we tell the system to use "e2-standard-4" machine type.
    	// Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_Policy{
    				Policy: &batchpb.AllocationPolicy_InstancePolicy{
    					MachineType: "e2-standard-4",
    				},
    			},
    		}},
    	}
    
    	// We use Cloud Logging as it's an out of the box available option
    	logsPolicy := &batchpb.LogsPolicy{
    		Destination: batchpb.[LogsPolicy_CLOUD_LOGGING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_LogsPolicy_DESTINATION_UNSPECIFIED_LogsPolicy_CLOUD_LOGGING_LogsPolicy_PATH),
    	}
    
    	jobLabels := map[string]string{"env": "testing", "type": "container"}
    
    	// The job's parent is the region in which the job will run
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    
    	job := batchpb.Job{
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           jobLabels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	req := &batchpb.CreateJobRequest{
    		Parent: parent,
    		JobId:  jobName,
    		Job:    &job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    
    	return nil
    }
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWithContainerNoMounting {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
    
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
    
        createContainerJob(projectId, region, jobName);
      }
    
      // This method shows how to create a sample Batch Job that will run a simple command inside a
      // container on Cloud Compute instances.
      public static void createContainerJob(String projectId, String region, String jobName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setContainer_com_google_cloud_batch_v1_Runnable_Container_)(
                      [Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.html).newBuilder()
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
                  // In milliseconds per cpu-second. This means the task requires 2 whole CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(2000)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(16)
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
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(4).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder().setMachineType("e2-standard-4").build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder().[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy).build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "container")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING).build())
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
        }
      }
    }

###  Node.js 

### Node.js

For more information, see the [Batch Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    /**
     * The region you want to the job to run in. The regions that support Batch are listed here:
     * https://cloud.google.com/batch/docs/get-started#locations
     */
    // const region = 'us-central-1';
    /**
     * The name of the job that will be created.
     * It needs to be unique for each project and region pair.
     */
    // const jobName = 'YOUR_JOB_NAME';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    // Define what will be done as part of the job.
    const task = new batch.TaskSpec();
    const runnable = new batch.Runnable();
    runnable.container = new batch.Runnable.Container();
    runnable.container.imageUri = 'gcr.io/google-containers/busybox';
    runnable.container.entrypoint = '/bin/sh';
    runnable.container.commands = [
      '-c',
      'echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.',
    ];
    task.runnables = [runnable];
    
    // We can specify what resources are requested by each task.
    const resources = new batch.ComputeResource();
    resources.cpuMilli = 2000; // in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    resources.memoryMib = 16;
    task.computeResource = resources;
    
    task.maxRetryCount = 2;
    task.maxRunDuration = {seconds: 3600};
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup();
    group.taskCount = 4;
    group.taskSpec = task;
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const allocationPolicy = new batch.AllocationPolicy();
    const policy = new batch.AllocationPolicy.InstancePolicy();
    policy.machineType = 'e2-standard-4';
    const instances = new batch.AllocationPolicy.InstancePolicyOrTemplate();
    instances.policy = policy;
    allocationPolicy.instances = [instances];
    
    const job = new batch.Job();
    job.name = jobName;
    job.taskGroups = [group];
    job.allocationPolicy = allocationPolicy;
    job.labels = {env: 'testing', type: 'container'};
    // We use Cloud Logging as it's an option available out of the box
    job.logsPolicy = new batch.LogsPolicy();
    job.logsPolicy.destination = batch.LogsPolicy.Destination.CLOUD_LOGGING;
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const response = await batchClient.createJob(request);
      console.log(response);
    }
    
    await callCreateJob();

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import batch_v1
    
    
    def create_container_job(project_id: str, region: str, job_name: str) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command inside a container on Cloud Compute instances.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
    
        Returns:
            A job object representing the job created.
        """
        client = batch_v1.BatchServiceClient()
    
        # Define what will be done as part of the job.
        runnable = batch_v1.Runnable()
        runnable.container = batch_v1.Runnable.Container()
        runnable.container.image_uri = "gcr.io/google-containers/busybox"
        runnable.container.entrypoint = "/bin/sh"
        runnable.container.commands = [
            "-c",
            "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.",
        ]
    
        # Jobs can be divided into tasks. In this case, we have only one task.
        task = batch_v1.TaskSpec()
        task.runnables = [runnable]
    
        # We can specify what resources are requested by each task.
        resources = batch_v1.ComputeResource()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = batch_v1.TaskGroup()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = batch_v1.AllocationPolicy.InstancePolicy()
        policy.machine_type = "e2-standard-4"
        instances = batch_v1.AllocationPolicy.InstancePolicyOrTemplate()
        instances.policy = policy
        allocation_policy = batch_v1.AllocationPolicy()
        allocation_policy.instances = [instances]
    
        job = batch_v1.Job()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "container"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = batch_v1.LogsPolicy()
        job.logs_policy.destination = batch_v1.LogsPolicy.Destination.CLOUD_LOGGING
    
        create_request = batch_v1.CreateJobRequest()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.create_job(create_request)
    
    

###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id) {
        // Initialize the request; start with the fields that depend on the sample
        // input.
        google::cloud::batch::v1::CreateJobRequest request;
        request.set_parent("projects/" + project_id + "/locations/" + location_id);
        request.set_job_id(job_id);
        // Most of the job description is fixed in this example; use a string to
        // initialize it.
        auto constexpr kText = R"pb(
          task_groups {
            task_count: 4
            task_spec {
              compute_resource { cpu_milli: 500 memory_mib: 16 }
              max_retry_count: 2
              max_run_duration { seconds: 3600 }
              runnables {
                container {
                  image_uri: "gcr.io/google-containers/busybox"
                  entrypoint: "/bin/sh"
                  commands: "-c"
                  commands: "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                }
              }
            }
          }
          allocation_policy {
            instances {
              policy { machine_type: "e2-standard-4" provisioning_model: STANDARD }
            }
          }
          labels { key: "env" value: "testing" }
          labels { key: "type" value: "container" }
          logs_policy { destination: CLOUD_LOGGING }
        )pb";
        auto* job = request.mutable_job();
        if (!google::protobuf::TextFormat::ParseFromString(kText, job)) {
          throw std::runtime_error("Error parsing Job description");
        }
        // Create a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.CreateJob(request);
        if (!response) throw std::move(response).status();
        std::cout << "Job : " << response->DebugString() << "\n";
      }

### Create a basic script job

You can create a basic script job using the Google Cloud console, gcloud CLI, Batch API, Go, Java, Node.js, Python, or C++.

### Console

**Important:** Some options for job creation are not available in the Google Cloud console. For details, see the documentation for each feature. For more features and flexibility for creating jobs, use the gcloud CLI or Batch API instead.

To create a basic script job using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. Click add_box **Create**. The **Create batch job** page opens. In the left pane, the **Job details** page is selected.

  3. Configure the **Job details** page:

     1. Optional: In the **Job name** field, customize the job name.

For example, enter `example-basic-job`.

     2. Configure the **Task details** section:

        1. In the **New runnable** window, add at least one script or container for this job to run.

For example, to add one script, do the following:

           1. Select **Script**. A field appears.

           2. In the field, enter a script that you want to run for each task in this job.

For example, enter the following script:
                  
                  echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.
                  

           3. Click **Done**.

        2. In the **Task count** field, enter the number of tasks for this job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits).

For example, enter `4`.

        3. In the **Parallelism** field, enter the number of tasks to run concurrently. The number cannot be larger than the total number of tasks and must be a whole number between `1` and the [parallel tasks per job limit](https://docs.cloud.google.com/batch/quotas#job_limits).

For example, enter `2`.

  4. Configure the **Resource specifications** page:

     1. In the left pane, click **Resource specifications**. The **Resource specifications** page opens.

     2. In the **VM provisioning model** section, select one of the following options for the [provisioning model](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#select-provisioning-method) for this job's VMs:

        * If your job can withstand preemption and you want discounted VMs, select **Spot**. Learn more about [recommendations for Spot VMs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview#spot-vms-recommendations).

        * Otherwise, select **Standard**.

For example, select **Standard** (default).

     3. Select the [location](https://docs.cloud.google.com/batch/docs/locations) for this job:

        1. In the **Region** field, select a region.

For example, select **`us-central1 (Iowa)`** (default).

        2. In the **Zone** field, do one of the following:

           * If you want to restrict this job to run in a specific zone only, select a zone.

           * Otherwise, select **any**.

For example, select **any** (default).

     4. Select one of the following [machine families](https://docs.cloud.google.com/compute/docs/machine-resource):

        * For common workloads, click **General purpose**.

        * For performance-intensive workloads, click **Compute optimized**.

        * For memory-intensive workloads, click **Memory optimized**.

        * For accelerator-optimized workloads, click **GPUs**. For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

For example, click **General purpose** (default).

     5. In the **Series** field, select a [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) for this job's VMs.

For example, if you selected **General purpose** for the machine family, select **E2** (default).

     6. In the **Machine type** field, select a machine type for this job's VMs.

For example, if you selected **E2** for the machine series, select **e2-medium (2 vCPU, 4 GB memory)** (default).

     7. Configure the amount of VM resources required for each task:

        1. In the **Cores** field, enter the amount of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms) per task.

For example, enter `1` (default).

        2. In the **Memory** field, enter the amount of RAM in GB per task.

For example, enter `0.5` (default).

  5. Optional: To review the job configuration, in the left pane, click **Preview**.

  6. Click **Create**.

The **Job details** page displays the job that you created.




### gcloud

To create a basic script job using the gcloud CLI, do the following:

  1. Create a JSON file that specifies your job's configuration details. For example, to create a basic script job, create a JSON file with the following contents. For more information about all the fields you can specify for a job, see the reference documentation for the [`projects.locations.jobs` REST resource](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs).

**Note:** If you prefer, you can specify your job's configuration details in a YAML file instead of a JSON file by converting JSON syntax to YAML syntax yourself. However, the Batch documentation only provides examples for JSON syntax. For more information, see the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     SCRIPT
                                 }
                             }
                         ],
                         "computeResource": {
                             "cpuMilli": CORES,
                             "memoryMib": MEMORY
                         },
                         "maxRetryCount": MAX_RETRY_COUNT,
                         "maxRunDuration": "MAX_RUN_DURATION"
                     },
                     "taskCount": TASK_COUNT,
                     "parallelism": PARALLELISM
                 }
             ]
         }
         

Replace the following:

     * `SCRIPT`: the script that each task runs. A script must be defined either as text using the `text` subfield or as the path to an accessible file using the `path` subfield. For more information, see the [`script` subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#script) and the example script job in this section.
     * `CORES`: Optional. The amount of cores—specifically [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms), which usually represent half a physical core—to allocate for each task in milliCPU units. If the `cpuMilli` field is not specified, the value is set to `2000` (2 vCPUs).
     * `MEMORY`: Optional. The amount of memory to allocate for each task in MB. If the `memoryMib` field is not specified, the value is set to `2000` (2 GB).
     * `MAX_RETRY_COUNT`: Optional. The maximum number of retries for a task. The value must be a whole number between `0` and `10`. If the `maxRetryCount` field is not specified, the value is set to `0`, which means to not retry the task. For more information about the `maxRetryCount` field, see [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).
     * `MAX_RUN_DURATION`: Optional. The maximum time a task is allowed to run before being retried or failing, formatted as a value in seconds followed by `s`—for example, `3600s` for 1 hour. If the `maxRunDuration` field is not specified, the value is set to the [maximum run time for a job](https://docs.cloud.google.com/batch/quotas#max-job-duration). For more information about the `maxRunDuration` field, see [Limit run times for tasks and runnables using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).
     * `TASK_COUNT`: Optional. The number of tasks for the job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `taskCount` field is not specified, the value is set to `1`.
     * `PARALLELISM`: Optional. The number of tasks the job runs concurrently. The number cannot be larger than the number of tasks and must be a whole number between `1` and the [parallel tasks per job limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `parallelism` field is not specified, the value is set to `1`.
  2. Create a job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



For example, to create a job that runs tasks using a script:

  1. Create a JSON file in the current directory named `hello-world-script.json` with the following contents:
         
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
                         ],
                         "computeResource": {
                             "cpuMilli": 2000,
                             "memoryMib": 16
                         },
                         "maxRetryCount": 2,
                         "maxRunDuration": "3600s"
                     },
                     "taskCount": 4,
                     "parallelism": 2
                 }
             ],
             "allocationPolicy": {
                 "instances": [
                     {
                         "policy": { "machineType": "e2-standard-4" }
                     }
                 ]
             },
             "labels": {
                 "department": "finance",
                 "env": "testing"
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

  2. Run the following command:
         
         gcloud batch jobs submit example-script-job \
           --location us-central1 \
           --config hello-world-script.json
         




### API

To create a basic script job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create). For more information about all the fields you can specify for a job, see the reference documentation for the [`projects.locations.jobs` REST resource](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs).
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                SCRIPT
                            }
                        }
                    ],
                    "computeResource": {
                        "cpuMilli": CORES,
                        "memoryMib": MEMORY
                    },
                    "maxRetryCount": MAX_RETRY_COUNT,
                    "maxRunDuration": "MAX_RUN_DURATION"
                },
                "taskCount": TASK_COUNT,
                "parallelism": PARALLELISM
            }
        ]
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
  * `JOB_NAME`: the name of the job.
  * `SCRIPT`: the script that each task runs. A script must be defined either as text using the `text` subfield or as the path to an accessible file using the `path` subfield. For more information, see the [`script` subfields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#script) and the example script job in this section.
  * `CORES`: Optional. The amount of cores—specifically [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms), which usually represent half a physical core—to allocate for each task in milliCPU units. If the `cpuMilli` field is not specified, the value is set to `2000` (2 vCPUs).
  * `MEMORY`: Optional. The amount of memory to allocate for each task in MB. If the `memoryMib` field is not specified, the value is set to `2000` (2 GB).
  * `MAX_RETRY_COUNT`: Optional. The maximum number of retries for a task. The value must be a whole number between `0` and `10`. If the `maxRetryCount` field is not specified, the value is set to `0`, which means to not retry the task. For more information about the `maxRetryCount` field, see [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).
  * `MAX_RUN_DURATION`: Optional. The maximum time a task is allowed to run before being retried or failing, formatted as a value in seconds followed by `s`—for example, `3600s` for 1 hour. If the `maxRunDuration` field is not specified, the value is set to the [maximum run time for a job](https://docs.cloud.google.com/batch/quotas#max-job-duration). For more information about the `maxRunDuration` field, see [Limit run times for tasks and runnables using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).
  * `TASK_COUNT`: Optional. The number of tasks for the job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `taskCount` field is not specified, the value is set to `1`.
  * `PARALLELISM`: Optional. The number of tasks the job runs concurrently. The number cannot be larger than the number of tasks and must be a whole number between `1` and the [parallel tasks per job limit](https://docs.cloud.google.com/batch/quotas#job_limits). If the `parallelism` field is not specified, the value is set to `1`.



For example, to create a job that runs tasks using a script, use the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs?job_id=example-script-job
    
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
                    ],
                    "computeResource": {
                        "cpuMilli": 2000,
                        "memoryMib": 16
                    },
                    "maxRetryCount": 2,
                    "maxRunDuration": "3600s"
                },
                "taskCount": 4,
                "parallelism": 2
            }
        ],
        "allocationPolicy": {
            "instances": [
                {
                    "policy": { "machineType": "e2-standard-4" }
                }
            ]
        },
        "labels": {
            "department": "finance",
            "env": "testing"
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

where `PROJECT_ID` is the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

###  Go 

### Go

For more information, see the [Batch Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	batch "cloud.google.com/go/batch/apiv1"
    	"cloud.google.com/go/batch/apiv1/batchpb"
    	durationpb "google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Creates and runs a job that executes the specified script
    func createScriptJob(w io.Writer, projectID, region, jobName string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// jobName := "some-job"
    
    	ctx := context.Background()
    	batchClient, err := batch.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1.html#cloud_google_com_go_batch_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer batchClient.Close()
    
    	// Define what will be done as part of the job.
    	command := &batchpb.Runnable_Script_Text{
    		Text: "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.",
    	}
    	// You can also run a script from a file. Just remember, that needs to be a script that's
    	// already on the VM that will be running the job.
    	// Using runnable.script.text and runnable.script.path is mutually exclusive.
    	// command := &batchpb.Runnable_Script_Path{
    	// 	Path: "/tmp/test.sh",
    	// }
    
    	// We can specify what resources are requested by each task.
    	resources := &batchpb.ComputeResource{
    		// CpuMilli is milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    		CpuMilli:  2000,
    		MemoryMib: 16,
    	}
    
    	taskSpec := &batchpb.TaskSpec{
    		Runnables: []*batchpb.Runnable{{
    			Executable: &batchpb.Runnable_Script_{
    				Script: &batchpb.Runnable_Script{Command: command},
    			},
    		}},
    		ComputeResource: resources,
    		MaxRunDuration: &durationpb.Duration{
    			Seconds: 3600,
    		},
    		MaxRetryCount: 2,
    	}
    
    	// Tasks are grouped inside a job using TaskGroups.
    	taskGroups := []*batchpb.TaskGroup{
    		{
    			TaskCount: 4,
    			TaskSpec:  taskSpec,
    		},
    	}
    
    	// Policies are used to define on what kind of virtual machines the tasks will run on.
    	// In this case, we tell the system to use "e2-standard-4" machine type.
    	// Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    	allocationPolicy := &batchpb.AllocationPolicy{
    		Instances: []*batchpb.AllocationPolicy_InstancePolicyOrTemplate{{
    			PolicyTemplate: &batchpb.AllocationPolicy_InstancePolicyOrTemplate_Policy{
    				Policy: &batchpb.AllocationPolicy_InstancePolicy{
    					MachineType: "e2-standard-4",
    				},
    			},
    		}},
    	}
    
    	// We use Cloud Logging as it's an out of the box available option
    	logsPolicy := &batchpb.LogsPolicy{
    		Destination: batchpb.[LogsPolicy_CLOUD_LOGGING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/batch/latest/apiv1/batchpb.html#cloud_google_com_go_batch_apiv1_batchpb_LogsPolicy_DESTINATION_UNSPECIFIED_LogsPolicy_CLOUD_LOGGING_LogsPolicy_PATH),
    	}
    
    	jobLabels := map[string]string{"env": "testing", "type": "script"}
    
    	// The job's parent is the region in which the job will run
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    
    	job := batchpb.Job{
    		TaskGroups:       taskGroups,
    		AllocationPolicy: allocationPolicy,
    		Labels:           jobLabels,
    		LogsPolicy:       logsPolicy,
    	}
    
    	req := &batchpb.CreateJobRequest{
    		Parent: parent,
    		JobId:  jobName,
    		Job:    &job,
    	}
    
    	created_job, err := batchClient.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job created: %v\n", created_job)
    
    	return nil
    }
    

###  Java 

### Java

For more information, see the [Batch Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/overview). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html);
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
    import com.google.cloud.batch.v1.[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html);
    import com.google.cloud.batch.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.html);
    import com.google.cloud.batch.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html);
    import com.google.cloud.batch.v1.[LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html);
    import com.google.cloud.batch.v1.[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).[Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html);
    import com.google.cloud.batch.v1.[TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html);
    import com.google.cloud.batch.v1.[TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWithScriptNoMounting {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
    
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
    
        createScriptJob(projectId, region, jobName);
      }
    
      // This method shows how to create a sample Batch Job that will run
      // a simple command on Cloud Compute instances.
      public static void createScriptJob(String projectId, String region, String jobName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `batchServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html) batchServiceClient = [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html).create()) {
    
          // Define what will be done as part of the job.
          [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html) runnable =
              [Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.html).newBuilder()
                  .[setScript](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder.html#com_google_cloud_batch_v1_Runnable_Builder_setScript_com_google_cloud_batch_v1_Runnable_Script_)(
                      [Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.html).newBuilder()
                          .[setText](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder.html#com_google_cloud_batch_v1_Runnable_Script_Builder_setText_java_lang_String_)(
                              "echo Hello world! This is task ${BATCH_TASK_INDEX}. "
                                  + "This job has a total of ${BATCH_TASK_COUNT} tasks.")
                          // You can also run a script from a file. Just remember, that needs to be a
                          // script that's already on the VM that will be running the job.
                          // Using setText() and setPath() is mutually exclusive.
                          // .setPath("/tmp/test.sh")
                          .build())
                  .build();
    
          // We can specify what resources are requested by each task.
          [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html) computeResource =
              [ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.html).newBuilder()
                  // In milliseconds per cpu-second. This means the task requires 2 whole CPUs.
                  .[setCpuMilli](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setCpuMilli_long_)(2000)
                  // In MiB.
                  .[setMemoryMib](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder.html#com_google_cloud_batch_v1_ComputeResource_Builder_setMemoryMib_long_)(16)
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
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder().[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(4).[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task).build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html).newBuilder().setMachineType("e2-standard-4").build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.html).newBuilder().[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy).build())
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  .putLabels("env", "testing")
                  .putLabels("type", "script")
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING).build())
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
        }
      }
    }

###  Node.js 

### Node.js

For more information, see the [Batch Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    /**
     * The region you want to the job to run in. The regions that support Batch are listed here:
     * https://cloud.google.com/batch/docs/get-started#locations
     */
    // const region = 'us-central-1';
    /**
     * The name of the job that will be created.
     * It needs to be unique for each project and region pair.
     */
    // const jobName = 'YOUR_JOB_NAME';
    
    // Imports the Batch library
    const batchLib = require('[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)');
    const batch = batchLib.protos.google.cloud.batch.v1;
    
    // Instantiates a client
    const batchClient = new batchLib.v1.[BatchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)();
    
    // Define what will be done as part of the job.
    const task = new batch.TaskSpec();
    const runnable = new batch.Runnable();
    runnable.script = new batch.Runnable.Script();
    runnable.script.text =
      'echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.';
    // You can also run a script from a file. Just remember, that needs to be a script that's
    // already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
    // exclusive.
    // runnable.script.path = '/tmp/test.sh'
    task.runnables = [runnable];
    
    // We can specify what resources are requested by each task.
    const resources = new batch.ComputeResource();
    resources.cpuMilli = 2000; // in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
    resources.memoryMib = 16;
    task.computeResource = resources;
    
    task.maxRetryCount = 2;
    task.maxRunDuration = {seconds: 3600};
    
    // Tasks are grouped inside a job using TaskGroups.
    const group = new batch.TaskGroup();
    group.taskCount = 4;
    group.taskSpec = task;
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const allocationPolicy = new batch.AllocationPolicy();
    const policy = new batch.AllocationPolicy.InstancePolicy();
    policy.machineType = 'e2-standard-4';
    const instances = new batch.AllocationPolicy.InstancePolicyOrTemplate();
    instances.policy = policy;
    allocationPolicy.instances = [instances];
    
    const job = new batch.Job();
    job.name = jobName;
    job.taskGroups = [group];
    job.allocationPolicy = allocationPolicy;
    job.labels = {env: 'testing', type: 'script'};
    // We use Cloud Logging as it's an option available out of the box
    job.logsPolicy = new batch.LogsPolicy();
    job.logsPolicy.destination = batch.LogsPolicy.Destination.CLOUD_LOGGING;
    
    // The job's parent is the project and region in which the job will run
    const parent = `projects/${projectId}/locations/${region}`;
    
    async function callCreateJob() {
      // Construct request
      const request = {
        parent,
        jobId: jobName,
        job,
      };
    
      // Run request
      const response = await batchClient.createJob(request);
      console.log(response);
    }
    
    await callCreateJob();

###  Python 

### Python

For more information, see the [Batch Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import batch_v1
    
    
    def create_script_job(project_id: str, region: str, job_name: str) -> batch_v1.Job:
        """
        This method shows how to create a sample Batch Job that will run
        a simple command on Cloud Compute instances.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
    
        Returns:
            A job object representing the job created.
        """
        client = batch_v1.BatchServiceClient()
    
        # Define what will be done as part of the job.
        task = batch_v1.TaskSpec()
        runnable = batch_v1.Runnable()
        runnable.script = batch_v1.Runnable.Script()
        runnable.script.text = "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
        # You can also run a script from a file. Just remember, that needs to be a script that's
        # already on the VM that will be running the job. Using runnable.script.text and runnable.script.path is mutually
        # exclusive.
        # runnable.script.path = '/tmp/test.sh'
        task.runnables = [runnable]
    
        # We can specify what resources are requested by each task.
        resources = batch_v1.ComputeResource()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = batch_v1.TaskGroup()
        group.task_count = 4
        group.task_spec = task
    
        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        allocation_policy = batch_v1.AllocationPolicy()
        policy = batch_v1.AllocationPolicy.InstancePolicy()
        policy.machine_type = "e2-standard-4"
        instances = batch_v1.AllocationPolicy.InstancePolicyOrTemplate()
        instances.policy = policy
        allocation_policy.instances = [instances]
    
        job = batch_v1.Job()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "script"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = batch_v1.LogsPolicy()
        job.logs_policy.destination = batch_v1.LogsPolicy.Destination.CLOUD_LOGGING
    
        create_request = batch_v1.CreateJobRequest()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
    
        return client.create_job(create_request)
    
    

###  C++ 

### C++

For more information, see the [Batch C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest). 

To authenticate to Batch, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/batch/v1/batch_client.h"
    
      [](std::string const& project_id, std::string const& location_id,
         std::string const& job_id) {
        // Initialize the request; start with the fields that depend on the sample
        // input.
        google::cloud::batch::v1::CreateJobRequest request;
        request.set_parent("projects/" + project_id + "/locations/" + location_id);
        request.set_job_id(job_id);
        // Most of the job description is fixed in this example; use a string to
        // initialize it.
        auto constexpr kText = R"pb(
          task_groups {
            task_count: 4
            task_spec {
              compute_resource { cpu_milli: 500 memory_mib: 16 }
              max_retry_count: 2
              max_run_duration { seconds: 3600 }
              runnables {
                script {
                  text: "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                }
              }
            }
          }
          allocation_policy {
            instances {
              policy { machine_type: "e2-standard-4" provisioning_model: STANDARD }
            }
          }
          labels { key: "env" value: "testing" }
          labels { key: "type" value: "script" }
          logs_policy { destination: CLOUD_LOGGING }
        )pb";
        auto* job = request.mutable_job();
        if (!google::protobuf::TextFormat::ParseFromString(kText, job)) {
          throw std::runtime_error("Error parsing Job description");
        }
        // Create a client and issue the request.
        auto client = google::cloud::batch_v1::BatchServiceClient(
            google::cloud::batch_v1::MakeBatchServiceConnection());
        auto response = client.CreateJob(request);
        if (!response) throw std::move(response).status();
        std::cout << "Job : " << response->DebugString() << "\n";
      }

## Use environment variables

Use [environment variables](https://en.wikipedia.org/wiki/Environment_variable) when you write a container image or script that you want a job to run. You can use any of the environment variables that are predefined for all Batch jobs and any custom environment variables that you define while creating the job.

### Use predefined environment variables

By default, the runnables in your job can use the following predefined environment variables:

  * `BATCH_TASK_COUNT`: the total number of tasks in this task group.
  * `BATCH_TASK_INDEX`: the index number of this task in the task group. The index of the first task is `0` and is incremented for each additional task.
  * `BATCH_HOSTS_FILE`: the path to a file listing all the running VM instances in this task group. To use this environment variable, the [`requireHostsFile` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#taskgroup) must be set to `true`.
  * `BATCH_TASK_RETRY_ATTEMPT`: the number of times that this task has already been attempted. The value is `0` during the first attempt of a task and is incremented for each following retry. The total number of retries allowed for a task is determined by the value of the `maxRetryCount` field, which is `0` if undefined. For more information about retries, see [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).



For an example of how to use predefined environment variables, see the previous example runnables in Create a basic job in this document.

### Define and use custom environment variables

Optionally, you can define one or more custom environment variables in a job.

You define each variable in a specific environment based on the desired scope of its data:

  * For a variable that has the _same value for all tasks_ , use one of the following:

    * If the variable has the _same value for all runnables_ , use the [environment of all runnables (`environment` subfield of `taskSpec`)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.environment).

    * Otherwise, if the variable has a _separate value for all runnables_ , use one or more [environments of specific runnables (`environment` subfield of `runnables[]`)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Runnable.FIELDS.environment).

  * Otherwise, for an [array](https://en.wikipedia.org/wiki/Array_\(data_structure\)) variable that has a _separate value for each task_ , use the [environment of all tasks (`taskEnvironment`)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskGroup.FIELDS.task_environments).




In the selected environment, you define the name and value(s) of each variable by using one of the following environment subfields:

  * To define the variable _directly_ in the job configuration JSON file, use the [standard variables (`variables`) subfield](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment.FIELDS.variables), as shown in this section. This option is recommended for data that you don't want to encrypt.

  * To define the variable _using encrypted data_ , you can use [Secret Manager or Cloud Key Management Service](https://docs.cloud.google.com/secret-manager/docs/overview#secret_manager):

    * To use the encrypted contents of an existing Secret Manager secret, use the [secret variables (`secretVariables`) subfield](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment.FIELDS.secret_variables). For more information about using secrets in a job, see [Protect sensitive data using Secret Manager](https://docs.cloud.google.com/batch/docs/create-run-job-secret-manager).

    * To use the encrypted contents of an existing Cloud Key Management Service key, use the [encrypted variables (`encryptedVariables`) subfield](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment.FIELDS.encrypted_variables). For more information about Cloud KMS keys, see the documentation for [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service).




You can define and use custom environment variables for your job using the gcloud CLI or Batch API. The following examples explain how to create two jobs that define and use standard variables. The first example job has a variable for a specific runnable. The second example job has an array variable, which has a different value for each task.

### gcloud

If you want to define a job that passes an environment variable to a runnable that each task runs, see the example for how to Define and use an environment variable for a runnable. Otherwise, if you want to define a job that passes a list of environment variables to different tasks based on the task index, see the example for how to Define and use an environment variable for each task.

#### Define and use an environment variable for a runnable

To create a job that passes environment variables to a runnable using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit) and specify the environment variables in the job's configuration file.

For example, to create a script job that defines an environment variable and passes it to the scripts of 3 tasks, make the following request:

  1. Create a JSON file in the current directory named `hello-world-environment-variables.json` with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "echo Hello ${VARIABLE_NAME}! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                                 },
                                 "environment": {
                                     "variables": {
                                         "VARIABLE_NAME": "VARIABLE_VALUE"
                                     }
                                 }
                             }
                         ],
                         "computeResource": {
                             "cpuMilli": 2000,
                             "memoryMib": 16
                         }
                     },
                     "taskCount": 3,
                     "parallelism": 1
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
             }
         }
         

Replace the following:

     * `VARIABLE_NAME`: the name of the [environment variable](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment) passed to each task. By convention, environment variable names are [capitalized](https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names).
     * `VARIABLE_VALUE`: Optional. The value of the environment variable passed to each task.
  2. Run the following command:
         
         gcloud batch jobs submit example-environment-variables-job \
           --location us-central1 \
           --config hello-world-environment-variables.json
         




#### Define and use an environment variable for each task

To create a job that passes environment variables to a task based on task index using the gcloud CLI, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit) and specify the `taskEnvironments` array field in the job's configuration file.

For example, to create a job that includes an array of 3 environment variables with matching names and different values, and passes the environment variables to the scripts of the tasks which indices match the environment variables' indices in the array:

  1. Create a JSON file in the current directory named `hello-world-task-environment-variables.json` with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "echo Hello ${TASK_VARIABLE_NAME}! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                                 },
                             }
                         ],
                         "computeResource": {
                             "cpuMilli": 2000,
                             "memoryMib": 16
                         }
                     },
                     "taskCount": 3,
                     "taskEnvironments": [
                         {
                             "variables": {
                                 "TASK_VARIABLE_NAME": "TASK_VARIABLE_VALUE_0"
                             }
                         },
                         {
                             "variables": {
                                 "TASK_VARIABLE_NAME": "TASK_VARIABLE_VALUE_1"
                             }
                         },
                         {
                             "variables": {
                                 "TASK_VARIABLE_NAME": "TASK_VARIABLE_VALUE_2"
                             }
                         }
                     ]
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
             }
         }
         

Replace the following:

     * `TASK_VARIABLE_NAME`: the name of the [task environment variables](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#taskgroup) passed to the tasks with matching indices. By convention, environment variable names are [capitalized](https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names).
     * `TASK_VARIABLE_VALUE_0`: the value of the environment variable passed to the first task, for which `BATCH_TASK_INDEX` is equal to `0`.
     * `TASK_VARIABLE_VALUE_1`: the value of the environment variable passed to the second task, for which `BATCH_TASK_INDEX` is equal to `1`.
     * `TASK_VARIABLE_VALUE_2`: the value of the environment variable passed to the third task, for which `BATCH_TASK_INDEX` is equal to `2`.
**Note:** If an environment variable is specified in the `taskEnvironments` array field, the value of the `taskCount` field must then equal the length of the `taskEnvironments` array. The maximum length of the `taskEnvironments` array is 200.
  2. Run the following command:
         
         gcloud batch jobs submit example-task-environment-variables-job \
           --location us-central1 \
           --config hello-world-task-environment-variables.json
         




### API

If you want to define a job that passes an environment variable to a runnable that each task runs, see the example for how to Define and use an environment variable for a runnable. Otherwise, if you want to define a job that passes a list of environment variables to different tasks based on the task index, see the example for how to Define and use an environment variable for each task.

#### Define and use an environment variable for a runnable

To create a job that passes environment variables to a runnable using Batch API, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit) and specify the environment variables in the `environment` field.

For example, to create a job that includes an environment variable and passes it to the scripts of 3 tasks, make the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/<var>PROJECT_ID</var>/locations/us-central1/jobs?job_id=example-environment-variables-job
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "echo Hello ${VARIABLE_NAME}! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                            },
                            "environment": {
                                "variables": {
                                    "VARIABLE_NAME": "VARIABLE_VALUE"
                                }
                            }
                        }
                    ],
                    "computeResource": {
                        "cpuMilli": 2000,
                        "memoryMib": 16
                    }
                },
                "taskCount": 3,
                "parallelism": 1
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
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `VARIABLE_NAME`: the name of the [environment](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Environment) variable passed to each task. By convention, environment variable names are [capitalized](https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names).
  * `VARIABLE_VALUE`: the value of the environment variable passed to each task.



#### Define and use an environment variable for each task

To create a job that passes environment variables to a task based on task index using Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify the environment variables in the `taskEnvironments` array field.

For example, to create a job that includes an array of 3 environment variables with matching names and different values, and passes the environment variables to the scripts of 3 tasks based on their indices, make the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/<var>PROJECT_ID</var>/locations/us-central1/jobs?job_id=example-task-environment-variables-job
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "echo Hello ${TASK_VARIABLE_NAME}! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
                            },
                        }
                    ],
                    "computeResource": {
                        "cpuMilli": 2000,
                        "memoryMib": 16
                    }
                },
                "taskCount": 3,
                "taskEnvironments": [
                    {
                        "variables": {
                            "TASK_VARIABLE_NAME": "TASK_VARIABLE_VALUE_0"
                        }
                    },
                    {
                        "variables": {
                            "TASK_VARIABLE_NAME": "TASK_VARIABLE_VALUE_1"
                        }
                    },
                    {
                        "variables": {
                            "TASK_VARIABLE_NAME": "TASK_VARIABLE_VALUE_2"
                        }
                    }
                ]
            }
        ],
        "allocationPolicy": {
            "instances": [
                {
                    "policy": { "machineType": "e2-standard-4" }
                }
            ]
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `TASK_VARIABLE_NAME`: the name of the environment variables passed to the tasks with matching indices. By convention, environment variable names are [capitalized](https://google.github.io/styleguide/shellguide.html#constants-and-environment-variable-names).
  * `TASK_VARIABLE_VALUE_0`: the value of the environment variable passed to the first task, for which `BATCH_TASK_INDEX` is equal to `0`.
  * `TASK_VARIABLE_VALUE_1`: the value of the environment variable passed to the second task, for which `BATCH_TASK_INDEX` is equal to `1`.
  * `TASK_VARIABLE_VALUE_2`: the value of the environment variable passed to the third task, for which `BATCH_TASK_INDEX` is equal to `2`.

**Note:** If an environment variable is specified in the `taskEnvironments` array field, the `taskCount` field's value must then equal the length of the `taskEnvironments` array. The maximum length of the `taskEnvironments` array is 200.

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
