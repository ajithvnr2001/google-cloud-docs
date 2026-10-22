---
url: https://docs.cloud.google.com/compute/docs/instances/create-reservation-bound-instance/
title: Create an instance with the reservation-bound model \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:45.473851+00:00
---

# Create an instance with the reservation-bound model  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-reservation-bound-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance with the reservation-bound model Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a standalone Compute Engine instance by using the reservation-bound provisioning model. This provisioning model lets you create A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High with 8 GPUs, A3 Edge, or H4D instances by [consuming pre-reserved capacity](https://docs.cloud.google.com/compute/docs/instances/about-reservation-bound-instances#prerequisites).

For other methods to create compute instances by using the reservation-bound provisioning model, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation.

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

To get the permissions that you need to create compute instances by using the reservation-bound provisioning model, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create compute instances by using the reservation-bound provisioning model. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create compute instances by using the reservation-bound provisioning model:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an instance that uses the reservation-bound provisioning model

To create an A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High with 8 GPUs, A3 Edge, or H4D instance by using the reservation-bound provisioning model, you must wait until the auto-created reservation that you want to use reaches its start time. Additionally, the compute instance that you intend to create must meet all of the following requirements:

  * The compute instance and the reservation must have [matching properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).

  * The compute instance must [specifically target the reservation for consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * The compute instance must be [stopped or deleted at the reservation's end time](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm).




The following example creates a future reservation request in calendar mode for five A3 Ultra instances, and then creates an A3 Ultra instance by consuming the auto-created reservation for the request.

To create an example compute instance by using the reservation-bound provisioning model, select one of the following options:

###  Console 

  1. Create an example request for five A3 Ultra instances and submit it for review:

     1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

     2. Click the **Future reservations** tab.

     3. Click add_box **Create future reservation**. The **Create a future reservation** page appears.

     4. Click the **GPUs** tab, and then, in the **GPU type** list, select **NVIDIA H200 141GB**. This action specifies an A3 Ultra instance.

     5. In the **Total capacity needed** field, enter `5`.

     6. In the **Reservation period** section, specify the start time and duration for your reservation period.

     7. Click **Search for capacity** , and then, in the **Available capacity** section, select one of the available machines.

     8. Click **Create**.

  2. At the request start time, to create an A3 Ultra instance to consume the example auto-created reservation, do the following:

**Important:** The following steps show how to create a single-NIC A3 Ultra instance, which is useful for quick tests. To create a multi-NIC A3 Ultra instance, see instead [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-instance-overview).
     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

     2. In the **Name** field, enter a name for the compute instance. For this example, enter `example-instance`.

     3. Specify the **Region** and **Zone** where the auto-created reservation exists. For this example, select **us-central1** and **us-central1-b** respectively.

     4. Click the **GPUs** tab, and then, in the **GPU type** list, select **NVIDIA H200 141GB**. This action specifies an A3 Ultra instance and sets the provisioning model to **Reservation-bound**.

     5. In the navigation menu, click **Advanced**.

     6. In the **Reservations** section, select **Choose a reservation** , and then click **Choose a reservation**.

     7. On the **Choose a reservation** pane, do the following:

        1. Select the example auto-created reservation.

        2. Click **Choose**.

     8. In the **Provisioning model** section, expand the **VM provisioning model advanced settings** section.

     9. In the **On VM termination** list, select **Stop** (default) or **Delete**.

     10. Click **Create**.




###  gcloud 

  1. To create an example request for five A3 Ultra instances and submit it for review, use the [`gcloud beta compute future-reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/future-reservations/create):
         
         gcloud beta compute future-reservations create example-fr \
             --auto-delete-auto-created-reservations \
             --deployment-type=DENSE \
             --planning-status=SUBMITTED \
             --require-specific-reservation \
             --reservation-mode=CALENDAR \
             --reservation-name=example-reservation \
             --share-setting=local \
             --start-time=2026-03-05T00:00:00Z \
             --end-time=2026-03-19T00:00:00Z \
             --machine-type=a3-ultragpu-8g \
             --total-count=5 \
             --zone=us-central1-b
         

Assume that Google Cloud approves the request and Compute Engine automatically creates an empty reservation. At the request start time, on March 5, 2026, Compute Engine increases the number of reserved GPU instances in the reservation. You can then consume the reservation.

  2. At the request start time, to create an A3 Ultra instance to consume the example auto-created reservation, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the following flags:

     * The `--instance-termination-action` flag.

     * The `--provisioning-model` flag set to `RESERVATION_BOUND`.

     * The `--reservation` flag.

     * The `--reservation-affinity` flag set to `specific`.

The command is similar to the following. For the full requirements to create an A3 Ultra instance, see instead [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-instance-overview).
    
    gcloud compute instance create example-a3ultra-instance  \
        --machine-type=a3-ultragpu-8g \
        **--instance-termination-action= TERMINATION_ACTION** \
        **--provisioning-model=RESERVATION_BOUND** \
        **--reservation-affinity=specific** \
        **--reservation= RESERVATION_URL** \
        --zone=us-central1-b \
        ...
    

The command includes the following values:

     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the compute instance at the end of the reservation period.

     * `RESERVATION_URL`: the URL of the reservation, which is formatted as follows:

       * If the auto-created reservation exists in your project: `example-reservation`.

       * If the auto-created reservation exists in a different project: `projects/PROJECT_ID/reservations/example-reservation`.




###  REST 

  1. To create an example request for five A3 Ultra instances and submit it for review, make a `POST` request to the [beta `futureReservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/futureReservations/insert):
         
         POST https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-b/futureReservations
         
         {
           "name": "example-request-calendar-mode",
           "autoDeleteAutoCreatedReservations": true,
           "deploymentType": "DENSE",
           "planningStatus": "SUBMITTED",
           "reservationMode": "CALENDAR",
           "reservationName": "example-reservation",
           "shareSettings": {
             "shareType": "LOCAL"
           },
           "specificReservationRequired": true,
           "specificSkuProperties": {
             "machineType": "a3-ultragpu-8g",
             "totalCount": 5
           },
           "timeWindow": {
             "startTime": "2026-03-05T00:00:00Z",
             "endTime": "2026-03-19T00:00:00Z"
           }
         }
         

Assume that Google Cloud approves the request and Compute Engine automatically creates an empty reservation. At the request start time, on March 5, 2026, Compute Engine increases the number of reserved GPU instances in the reservation. You can then consume the reservation.

  2. At the request start time, to create an A3 Ultra instance to consume the example auto-created reservation, make a `POST` request to [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the following fields:

     * The `reservationAffinity.consumeReservationType` field set to `SPECIFIC_RESERVATION`.

     * The `reservationAffinity.key` field set to `compute.googleapis.com/reservation-name`.

     * The `reservationAffinity.values` field set to the URL of the reservation.

     * The `scheduling.instanceTerminationAction` field.

     * The `scheduling.provisioningModel` field set to `RESERVATION_BOUND`.

The request is similar to the following. For the full requirements to create an A3 Ultra instance, see instead [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-instance-overview).
    
    POST https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-b/instances
    
    {
      {
        "machineType": "projects/example-project/zones/us-central1-b/machineTypes/a3-ultragpu-8g",
        "name": "example-a3ultra-instance",
        "reservationAffinity": {
          **"consumeReservationType": "SPECIFIC_RESERVATION"** ,
          **"key": "compute.googleapis.com/reservation-name"** ,
          **"values":[
            " RESERVATION_URL"
          ]**,
        },
        "scheduling": {
          **"instanceTerminationAction": " TERMINATION_ACTION"**,
          **"provisioningModel": "RESERVATION_BOUND"**
        },
        ...
      }
    }
    

The request body includes the following values:

     * `RESERVATION_URL`: the URL of the reservation, which is formatted as follows:

       * If the auto-created reservation exists in your project: `example-reservation`.

       * If the auto-created reservation exists in a different project: `projects/PROJECT_ID/reservations/example-reservation`.

     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the compute instance at the end of the reservation period.




## What's next

  * [Connect to your compute instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance)

  * [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript)

  * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)

  * [Stop or restart an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
