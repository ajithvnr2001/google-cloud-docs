---
url: https://docs.cloud.google.com/batch/docs/specify-job-network/
title: Specify the network for a job \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:23.581095+00:00
---

# Specify the network for a job  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/specify-job-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Specify the network for a job Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to specify the network for the VMs that run a job. 

You can control connections for the VMs that run a job by specifying a network with the desired access. For example, you might specify a network that allows a job to access required resources or limits access to improve security. Alternatively, if you don't have any networking requirements and don't want to configure networking for a job, skip specifying the network to use the default networking configuration instead.

For more information about networking concepts and when to configure networking, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job that runs on a specific network, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * To identify the network and subnet: [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. Identify the network that you want to use for the job. The network you specify for a job must meet the following requirements: 
     * The network is a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) that is in the same project as the job or is a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the project for the job. 
     * The network includes a [subnetwork (subnet)](https://docs.cloud.google.com/vpc/docs/subnets) in the location where you want to run the job. 
     * The network allows the access required for your job. For example, if your job requires communication between VMs—such as a [job that uses MPI libraries to communicate between tightly coupled tasks](https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library)—make sure the network has a firewall rule allowing connections between the job's VMs. 

Learn how to [Configure VPC firewall rules for common use cases](https://docs.cloud.google.com/vpc/docs/using-firewalls#rules-for-common-use-cases). 

For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 
  4. If you want a job to run on a subnet of a Shared VPC network that is hosted by another project, your project's [Batch service agent](https://docs.cloud.google.com/batch/docs/get-started#batch-service-agent) must be granted permission to use that subnet. 

To ensure that your project's Batch service agent has the necessary permissions to create a job that runs on a subnet of a Shared VPC network, ask your administrator to grant the [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) IAM role to your project's Batch service agent on the Shared VPC subnet. **Important:** You must grant this role to your project's Batch service agent, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

**Caution:** If you grant the Batch service agent the Compute Network User (`roles/compute.networkUser`) IAM role on a Shared VPC subnet, you allow _all_ principals in the project that are allowed to create Batch jobs to do so using this Shared VPC subnet.

For more information, see the documentation for [setting up Shared VPC for service accounts](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#sa-as-spa). 




## Create a job that runs on a specific network

Specify the network for a job when you are creating it. Specifically, you need to specify a VPC network and a subnet that is located where you want to run this job.

If you want to [use a VM instance template while creating this job](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template), you must specify the network in the VM instance template. Otherwise, use the following steps to specify the network for a job by using the gcloud CLI or Batch API.

### gcloud

To create a job that runs on a specific network using the gcloud CLI, select one of the following options:

  * Use gcloud flags to specify the network for a job
  * Use JSON fields to specify the network for a job



### Use gcloud flags to specify the network for a job

To create a job and use gcloud flags to specify the network for the job, complete the following steps:

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
         

  2. Create the job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit). To specify the network the job, include the `--network` and `--subnetwork` flags.
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE \
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



### Use JSON fields to specify the network for a job

To create a job and use fields in the JSON configuration file to specify the network for the job, complete the following steps:

  1. Create a JSON file that specifies your job's configuration details. To specify the network for the job, include the [`network` and `subnetwork` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface).

For example, to create a basic script job that runs on a specific network, create a JSON file with the following contents.
         
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
                   "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET"
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
     * `NETWORK`: the name of a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) in the current project or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the current project.
     * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where the subnet for the job and the job's Compute Engine resources are located. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).
     * `SUBNET`: the name of a [subnet](https://docs.cloud.google.com/vpc/docs/subnets) that is part of the VPC network and is located in the same region as the job's Compute Engine resources.
  2. Create the job by using the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit JOB_NAME \
             --location LOCATION \
             --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name for this job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) for this job.
     * `JSON_CONFIGURATION_FILE`: the path for the JSON file with the job's configuration details.



###  Java 
    
    
    import com.google.cloud.batch.v1.[AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html);
    import com.google.cloud.batch.v1.[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.html);
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
    
    public class CreateBatchCustomNetwork {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to use to run the job. Regions that are
        // available for Batch are listed on: https://cloud.google.com/batch/docs/get-started#locations
        String region = "europe-central2";
        // The name of the job that will be created.
        // It needs to be unique for each project and region pair.
        String jobName = "JOB_NAME";
        // The name of a VPC network in the current project or a Shared VPC network that is hosted by
        // or shared with the current project.
    
        String network = String.format("global/networks/%s", "test-network");
        // The name of a subnet that is part of the VPC network and is located
        // in the same region as the VMs for the job.
        String subnet = String.format("regions/%s/subnetworks/%s", region, "subnet");
    
        createBatchCustomNetwork(projectId, region, jobName, network, subnet);
      }
    
      // Create a job that runs on a specific network.
      public static [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) createBatchCustomNetwork(String projectId, String region, String jobName,
                                                 String network,  String subnet)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
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
    
          [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html) task = [TaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.html).newBuilder()
              // Jobs can be divided into tasks. In this case, we have only one task.
              .[addRunnables](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_addRunnables_com_google_cloud_batch_v1_Runnable_)(runnable)
              .[setMaxRetryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRetryCount_int_)(2)
              .[setMaxRunDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder.html#com_google_cloud_batch_v1_TaskSpec_Builder_setMaxRunDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
              .build();
    
          // Tasks are grouped inside a job using TaskGroups.
          // Currently, it's possible to have only one task group.
          [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html) taskGroup = [TaskGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.html).newBuilder()
              .[setTaskCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskCount_long_)(3)
              .[setParallelism](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setParallelism_long_)(1)
              .[setTaskSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder.html#com_google_cloud_batch_v1_TaskGroup_Builder_setTaskSpec_com_google_cloud_batch_v1_TaskSpec_)(task)
              .build();
    
          // Specifies a VPC network and a subnet for Allocation Policy
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy.html) networkPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).NetworkPolicy.newBuilder()
                  .[addNetworkInterfaces](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_NetworkPolicy_Builder_addNetworkInterfaces_com_google_cloud_batch_v1_AllocationPolicy_NetworkInterface_)([AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).NetworkInterface.newBuilder()
                      .setNetwork(network) // Set the network name
                      .[setSubnetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_NetworkInterface_Builder_setSubnetwork_java_lang_String_)(subnet) // Set the subnet name
                      .[setNoExternalIpAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_NetworkInterface_Builder_setNoExternalIpAddress_boolean_)(true) // Blocks external access for all VMs
                      .build())
                  .build();
    
          // Policies are used to define on what kind of virtual machines the tasks will run on.
          // In this case, we tell the system to use "e2-standard-4" machine type.
          // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).[InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.html) instancePolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).InstancePolicy.newBuilder().setMachineType("e2-standard-4")
                  .build();
    
          [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html) allocationPolicy =
              [AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).newBuilder()
                  .addInstances([AllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.html).InstancePolicyOrTemplate.newBuilder()
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder.html#com_google_cloud_batch_v1_AllocationPolicy_InstancePolicyOrTemplate_Builder_setPolicy_com_google_cloud_batch_v1_AllocationPolicy_InstancePolicy_)(instancePolicy).build())
                  .setNetwork(networkPolicy)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html).newBuilder()
                  .[addTaskGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_addTaskGroups_com_google_cloud_batch_v1_TaskGroup_)(taskGroup)
                  .[setAllocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setAllocationPolicy_com_google_cloud_batch_v1_AllocationPolicy_)(allocationPolicy)
                  // We use Cloud Logging as it's an out of the box available option.
                  .[setLogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder.html#com_google_cloud_batch_v1_Job_Builder_setLogsPolicy_com_google_cloud_batch_v1_LogsPolicy_)(
                      [LogsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.html).newBuilder().[setDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder.html#com_google_cloud_batch_v1_LogsPolicy_Builder_setDestination_com_google_cloud_batch_v1_LogsPolicy_Destination_)([Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination.html).CLOUD_LOGGING))
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
    const region = 'europe-central2';
    // The name of the job that will be created.
    // It needs to be unique for each project and region pair.
    const jobName = 'example-job';
    // The name of a VPC network in the current project or a Shared VPC network that is hosted by
    // or shared with the current project.
    const network = 'global/networks/test-network';
    // The name of a subnetwork that is part of the VPC network and is located
    // in the same region as the VMs for the job.
    const subnetwork = `regions/${region}/subnetworks/subnet`;
    
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
    
    // Specify VPC network and a subnet for Allocation Policy
    const networkPolicy = new batch.AllocationPolicy.NetworkPolicy({
      networkInterfaces: [
        new batch.AllocationPolicy.NetworkInterface({
          // Set the network name
          network,
          // Set the subnetwork name
          subnetwork,
          // Blocks external access for all VMs
          noExternalIpAddress: true,
        }),
      ],
    });
    
    // Policies are used to define on what kind of virtual machines the tasks will run on.
    // In this case, we tell the system to use "e2-standard-4" machine type.
    // Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
    const instancePolicy = new batch.AllocationPolicy.InstancePolicy({
      machineType: 'e2-standard-4',
    });
    
    const allocationPolicy = new batch.AllocationPolicy.InstancePolicyOrTemplate({
      policy: instancePolicy,
      network: networkPolicy,
    });
    
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
    
    async function callCreateBatchCustomNetwork() {
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
    
    await callCreateBatchCustomNetwork();

###  Python 
    
    
    from google.cloud import [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest)
    
    
    def create_with_custom_network(
        project_id: str,
        region: str,
        network_name: str,
        subnet_name: str,
        job_name: str,
    ) -> batch_v1.Job:
        """Create a Batch job that runs on a specific network and subnet.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use to run the job. Regions that are
                available for Batch are listed on: https://cloud.google.com/batch/docs/locations
            network_name: The name of a VPC network in the current project or a Shared VPC network.
            subnet_name: Name of the subnetwork to be used within the specified region.
            job_name: the name of the job that will be created.
                It needs to be unique for each project and region pair.
        Returns:
            A job object representing the job created.
        """
    
        client = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html)()
    
        # Define what will be done as part of the job.
        runnable = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html)()
        runnable.script = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.html).[Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script.html)()
        runnable.script.text = "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks."
    
        # Jobs can be divided into tasks. In this case, we have only one task.
        task = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.html)()
        task.runnables = [runnable]
    
        # We can specify what resources are requested by each task.
        resources = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource.html)()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources
    
        task.max_retry_count = 2
        task.max_run_duration = "3600s"
    
        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
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
    
        # Create a NetworkInterface object to specify network settings for the job
        network_interface = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.html).[NetworkInterface](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.NetworkInterface.html)()
        # Set the network to the specified network name within the project
        network_interface.network = f"projects/{project_id}/global/networks/{network_name}"
        # Set the subnetwork to the specified subnetwork within the region
        network_interface.subnetwork = (
            f"projects/{project_id}/regions/{region}/subnetworks/{subnet_name}"
        )
        allocation_policy.network.network_interfaces = [network_interface]
    
        job = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.html)()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html)()
        job.logs_policy.destination = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.html).[Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination.html).CLOUD_LOGGING
    
        create_request = [batch_v1](https://docs.cloud.google.com/python/docs/reference/batch/latest).[CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest.html)()
        create_request.job = job
        create_request.job_id = job_name
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{project_id}/locations/{region}"
        return client.[create_job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient.html#google_cloud_batch_v1_services_batch_service_BatchServiceClient_create_job)(create_request)
    
    

### API

To create a job using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify your job's configuration details. To specify the network for the job, include the [`network` and `subnetwork` fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#NetworkInterface).

For example, to create a basic script job that runs on a specific network, make the following `POST` request:
    
    
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
              "subnetwork": "projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET"
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
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) for this job.
  * `JOB_NAME`: the name for this job.
  * `HOST_PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project for the network you specify: 
    * If you are using a Shared VPC network, specify the host project.
    * Otherwise, specify the current project (`PROJECT_ID`).
  * `NETWORK`: the name of a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) in the current project or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is hosted by or shared with the current project.
  * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where the subnet for the job and the job's Compute Engine resources are located. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).
  * `SUBNET`: the name of a [subnet](https://docs.cloud.google.com/vpc/docs/subnets) that is part of the VPC network and is located in the same region as the job's Compute Engine resources.



## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn more about [networking](https://docs.cloud.google.com/batch/docs/networking-overview).
  * Learn more about [creating a job](https://docs.cloud.google.com/batch/docs/create-run-job).
  * Learn how to [view jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
