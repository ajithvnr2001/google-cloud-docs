---
url: https://docs.cloud.google.com/compute/docs/instance-groups/manually-suspend-or-stop-vms-in-mig/
title: Manually suspend or stop VMs in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:42.091738+00:00
---

# Manually suspend or stop VMs in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/manually-suspend-or-stop-vms-in-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manually suspend or stop VMs in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to suspend and stop virtual machine (VM) instances in a managed instance group (MIG), and how to resume their operation.

## Before you begin

  * Review the introductory page about [suspended and stopped VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig).
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




## Suspend specific VMs in a MIG

You can suspend a running VM in a MIG using the Google Cloud console, the Google Cloud CLI, or the Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the instance group name where you want to suspend VMs.
  3. In the instance group **Overview** page, under **VM instances** , select all the VMs that you want to suspend.
  4. Click **Suspend**.
  5. In the confirmation dialog that appears, click **Suspend** to confirm.



###  gcloud 

Use the [`instance-groups managed suspend-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/suspend-instances).
    
    
    gcloud compute instance-groups managed suspend-instances MIG_NAME \
      --instances=INSTANCE_NAME \
      [--region=REGION | --zone=ZONE]
    

Replace the following:

  * `MIG_NAME`: the name of the MIG in which to suspend an instance.
  * `INSTANCE_NAME`: the name of the instance to suspend. To suspend multiple instances, provide a comma-separated list of names.
  * `REGION`: for a regional MIG, the region where the MIG is located.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located.



###  REST 

Use the [`instanceGroupManager.suspendInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/suspendInstances) and specify the instances in the request body. For regional MIGs, use the [`regionInstanceGroupManager.suspendInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/suspendInstances).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/suspendInstances
    
    {
      "instances": [
        "INSTANCE_NAME_URL"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located. 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `MIG_NAME`: the name of the MIG in which to suspend an instance.
  * `INSTANCE_NAME_URL`: the URL of the instance to suspend—for example, `zones/us-central1-a/instances/example-instance-name1`. To suspend multiple instances, provide a comma-separated list of URLs—for example, `"zones/us-central1-a/instances/example-instance-name1","zones/us-central1-a/instances/example-instance-name2"`.



## Resume selected VMs in a MIG

You can resume a suspended VM in a MIG using the Google Cloud console, the gcloud CLI, or the Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the instance group name where you want to resume VMs.
  3. In the instance group **Overview** page, under **VM instances** , select all the suspended VMs that you want to resume, then click **Start/Resume**.



###  gcloud 

Use the [`instance-groups managed resume-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resume-instances).
    
    
    gcloud compute instance-groups managed resume-instances MIG_NAME \
      --instances=INSTANCE_NAME \
      [--region=REGION | --zone=ZONE]
    

Replace the following:

  * `MIG_NAME`: the name of the MIG in which to resume an instance.
  * `INSTANCE_NAME`: the name of the instance to resume. To resume multiple instances, provide a comma-separated list of names.
  * `REGION`: for a regional MIG, the region where the MIG is located.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located.



###  REST 

Use the [`instanceGroupManager.resumeInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/resumeInstances) and specify the instances in the request body. For regional MIGs, use the [`regionInstanceGroupManager.resumeInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/resumeInstances).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resumeInstances
    
    {
      "instances": [
        "INSTANCE_NAME_URL"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located. 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `MIG_NAME`: the name of the MIG in which to resume an instance.
  * `INSTANCE_NAME_URL`: the URL of the instance to resume—for example, `zones/us-central1-a/instances/example-instance-name1`. To resume multiple instances, provide a comma-separated list of URLs—for example, `"zones/us-central1-a/instances/example-instance-name1","zones/us-central1-a/instances/example-instance-name2"`.



## Stop selected VMs in a MIG

If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in the instance template that your MIG uses, then the running VMs in your MIG gracefully shut down when you stop them. When you stop a running VM, you can optionally skip a graceful shutdown, or end an ongoing graceful shutdown when all tasks have finished running, to reduce unnecessary costs.

You can stop a running VM in a MIG by using the Google Cloud console, the Google Cloud CLI, or the Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG where you want to stop VMs. The **Overview** page appears.

  3. In the **VM instances** list, select all the VMs that you want to stop, then click **Stop**. If there is no **Stop** option, then click **More actions** , and then select **Stop**.

  4. In the dialog that appears, do the following:

     1. Optional: To stop VMs without using graceful shutdown, or to end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Stop**.




###  gcloud 

Use the [`instance-groups managed stop-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/stop-instances).
    
    
    gcloud compute instance-groups managed stop-instances MIG_NAME \
        --instances=INSTANCE_NAME \
        [--region=REGION | --zone=ZONE]
    

Replace the following:

  * `MIG_NAME`: the name of the MIG in which to stop an instance.
  * `INSTANCE_NAME`: the name of the instance to stop. To stop multiple instances, provide a comma-separated list of names.
  * `REGION`: for a regional MIG, the region where the MIG is located.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located.



If you want to skip or end a graceful shutdown, then use the same command with the `--no-graceful-shutdown` flag:
    
    
    gcloud compute instance-groups managed stop-instances MIG_NAME \
        --instances=INSTANCE_NAME \
        **--no-graceful-shutdown** \
        [--region=REGION | --zone=ZONE]
    

###  REST 

Use the [`instanceGroupManager.stopInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/stopInstances) and specify the instances in the request body. For regional MIGs, use the [`regionInstanceGroupManager.stopInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/stopInstances).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/stopInstances
    
    {
        "instances": [
          "INSTANCE_NAME_URL"
        ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located. 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `MIG_NAME`: the name of the MIG in which to stop an instance.
  * `INSTANCE_NAME_URL`: the URL of the instance to stop—for example, `zones/us-central1-a/instances/example-instance-name1`. To stop multiple instances, provide a comma-separated list of URLs—for example, `"zones/us-central1-a/instances/example-instance-name1","zones/us-central1-a/instances/example-instance-name2"`.



If you want to skip or end a graceful shutdown, then include the `noGracefulShutdown` query parameter set to `true` in the request URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/stopInstances**?noGracefulShutdown=true**
    
    {
        "instances": [
          "INSTANCE_NAME_URL"
        ]
    }
    

## Start selected VMs in a MIG

You can start a stopped VM in a MIG using the Google Cloud console, the gcloud CLI, or the Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the instance group name where you want to start VMs.
  3. In the instance group **Overview** page, under **VM instances** , select all the stopped VMs that you want to start, then click **Start/Resume**.



###  gcloud 

Use the [`instance-groups managed start-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/start-instances).
    
    
    gcloud compute instance-groups managed start-instances MIG_NAME \
      --instances=INSTANCE_NAME \
      [--region=REGION | --zone=ZONE]
    

Replace the following:

  * `MIG_NAME`: the name of the MIG in which to start an instance.
  * `INSTANCE_NAME`: the name of the instance to start. To start multiple instances, provide a comma-separated list of names.
  * `REGION`: for a regional MIG, the region where the MIG is located.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located.



###  REST 

Use the [`instanceGroupManager.startInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/startInstances) and specify the instances in the request body. For regional MIGs, use the [`regionInstanceGroupManager.startInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/startInstances).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/startInstances
    
    {
      "instances": [
        "INSTANCE_NAME_URL"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located. 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `MIG_NAME`: the name of the MIG in which to start an instance.
  * `INSTANCE_NAME_URL`: the URL of the instance to start—for example, `zones/us-central1-a/instances/example-instance-name1`. To start multiple instances, provide a comma-separated list of URLs—for example, `"zones/us-central1-a/instances/example-instance-name1","zones/us-central1-a/instances/example-instance-name2"`.



## What's next

  * Learn how to [accelerate scale out with the standby pool](https://docs.cloud.google.com/compute/docs/instance-groups/accelerate-mig-scale-out-with-standby-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
