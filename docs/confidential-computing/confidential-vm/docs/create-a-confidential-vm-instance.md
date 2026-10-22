---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance/
title: Create a Confidential VM instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:29.591033+00:00
---

# Create a Confidential VM instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Create a Confidential VM instance Stay organized with collections  Save and categorize content based on your preferences. 

You can create a Confidential VM instance as part of creating a new Compute Engine virtual machine.

## Before you begin

Before creating a Confidential VM instance, you need to set up your environment as follows:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  8. Optional: To use the gcloud CLI examples in this guide: 
     * Install or update to the latest version of the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). 
     * [ Set a default region and zone for your client](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client) that [supports Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations). 
  9. Optional: To use the API examples in this guide, [set up authentication](https://docs.cloud.google.com/docs/authentication/rest) for your requests. Learn more about [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2). 



## Create an instance

### Console

To create a Confidential VM instance with the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Machine configuration** pane, do the following:

     1. Select a [supported region and zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).

     2. Select one of the following machine families:

        * **General purpose**

        * **Compute optimized**

        * **GPUs**

     3. If you selected the **GPUs** family, select the appropriate **GPU type** and the **Number of GPUs** based on the [supported machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

     4. Select a [supported machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone) for the Confidential Computing technology you want to use.

  4. In the navigation menu, click **Security**.

  5. In the **Confidential VM service** section, click **Enable**.

  6. In the **Select a type** box, select one of the following [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) types:

     * **AMD SEV**

     * **AMD SEV-SNP**

     * **Intel TDX**

  7. In the **Enable Confidential Computing** dialog, review the list of settings that are updated when you enable the service. They can include the following fields, if they were set to incompatible values.

     * **Series** and **Machine type**. For more information, see [Machine types, CPUs, and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

     * **Region** and **zone**. For more information, see [Machine types, CPUs, and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

     * **Boot disk image**. For more information, see [Operating systems](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#operating-systems).

     * **On-host maintenance**. For more information, see [Set host maintenance policy of a VM](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#settingoptions).

     * **Network interface card**. For more information, see [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

  8. Click **Confirm** , and then click **Create**.




After you click **Create** , the **VM instances** page opens. On this page you can view the status and details for your new instance. When an ![green checkmark available icon](https://docs.cloud.google.com/static/confidential-computing/confidential-vm/docs/images/status-success.svg)**Available** icon appears in the **Status** column for your Confidential VM instance, it's ready to use.

### gcloud

To create a Confidential VM instance with the gcloud CLI, use the [`instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) sub-command with the `--confidential-compute-type` flag.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --confidential-compute-type=CONFIDENTIAL_COMPUTING_TECHNOLOGY \
        --machine-type=MACHINE_TYPE_NAME \
        --min-cpu-platform="CPU_PLATFORM" \
        --maintenance-policy=MAINTENANCE_POLICY \
        --zone=ZONE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY_NAME \
        --project=PROJECT_ID
    

Provide the following values:

  * `INSTANCE_NAME`: The name of the new VM instance.

  * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following values:

    * `SEV`

    * `SEV_SNP`

    * `TDX`

  * `MACHINE_TYPE_NAME`: The VM machine type, for example, `n2d-standard-2`. Valid machine types for Confidential VM instances are determined by the Confidential Computing technology you've chosen. See [Machine types, CPUs, and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

  * `CPU_PLATFORM`: Choose one of the following values:

    * For AMD SEV: Either `AMD Milan` (C2D or N2D machine types), `AMD Genoa` (C3D machine types), or `AMD Turin` (C4D machine types).

    * For AMD SEV-SNP: `AMD Milan` (N2D machine types).

    * For Intel TDX: Remove this flag.

  * `MAINTENANCE_POLICY`: For N2D and C3D machine types that use SEV, set this to `MIGRATE` for live migration support. For all other machine types, set this value to `TERMINATE`, as they [don't support live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration).

  * `ZONE_NAME`: The [Confidential VM-supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) in which to create the instance.

  * `IMAGE_PROJECT`: The project containing the supported operating system image.

  * `IMAGE_FAMILY_NAME`: The family for the [Confidential VM-supported operating system image](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#operating-systems). When you don't additionally specify `--image`, the latest image version is selected.

  * `PROJECT_ID`: Optional. The ID of the project to create the VM in.




### Example

Run the following command to create an `n2d-standard-2` instance called `my-instance` in the `us-central1-a` zone, using AMD SEV-SNP:
    
    
    gcloud compute instances create my-instance \
        --machine-type=n2d-standard-2 \
        --min-cpu-platform="AMD Milan" \
        --zone=us-central1-a \
        --confidential-compute-type=SEV_SNP \
        --maintenance-policy=TERMINATE \
        --image-project=ubuntu-os-cloud \
        --image-family=ubuntu-2404-lts-amd64
    

### Response

A response to a creation request looks similar to the following example:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance].
    NAME: my-instance
    ZONE: us-central1-a
    MACHINE_TYPE: n2d-standard-2
    PREEMPTIBLE:
    INTERNAL_IP: 0.0.0.0
    EXTERNAL_IP: 0.0.0.0
    STATUS: RUNNING
    

### REST

To create a Confidential VM instance, you need to send a POST request with the appropriate body content.

The HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE_NAME/instances
    

Request JSON body:
    
    
    {
      "name": "INSTANCE_NAME",
      "confidentialInstanceConfig": {
        "confidentialInstanceType": "CONFIDENTIAL_COMPUTING_TECHNOLOGY"
      },
      "machineType": "zones/ZONE_NAME/machineTypes/MACHINE_TYPE_NAME",
      "minCpuPlatform": "CPU_PLATFORM",
      "scheduling": {
        "automaticRestart": true,
        "nodeAffinities": [],
        "onHostMaintenance": "MAINTENANCE_POLICY",
        "preemptible": false
      },
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY_NAME"
          }
        }
      ],
      "networkInterfaces": [
        {
          "nicType": "gVNIC"
        }
      ]
    }
    

Provide the following values:

  * `PROJECT_ID`: The ID of the project to create the VM in.

  * `ZONE_NAME`: The [Confidential VM-supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) in which to create the instance.

  * `INSTANCE_NAME`: The name of the new VM instance.

  * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following values:

    * `SEV`

    * `SEV_SNP`

    * `TDX`

  * `MACHINE_TYPE_NAME`: The VM machine type, for example, `n2d-standard-2`. Valid machine types for Confidential VM instances are determined by the Confidential Computing technology you've chosen. See [Machine types, CPUs, and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

  * `CPU_PLATFORM`: Choose one of the following values:

    * For AMD SEV: Either `AMD Milan` (C2D or N2D machine types), `AMD Genoa` (C3D machine types), or `AMD Turin` (C4D machine types).

    * For AMD SEV-SNP: `AMD Milan` (N2D machine types).

    * For Intel TDX: Remove this key-value pair.

  * `MAINTENANCE_POLICY`: For N2D machine types that use SEV, set this to `MIGRATE` for live migration support. For all other machine types, set this value to `TERMINATE`, as they [don't support live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration).

  * `IMAGE_PROJECT`: The project containing the supported operating system image.

  * `IMAGE_FAMILY_NAME`: The family for the [Confidential VM-supported operating system image](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#operating-systems). When you don't additionally specify `--image`, the latest image version is selected.




### Example

Run one of the following commands to create an `n2d-standard-2` instance called `my-instance` in the `us-central1-a` zone, in the `my-project` project, using AMD SEV-SNP:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d '{
                "name": "my-instance",
                "confidentialInstanceConfig": {
                  "confidentialInstanceType": "SEV_SNP"
                },
                "machineType": "zones/us-central1-a/machineTypes/n2d-standard-2",
                "minCpuPlatform": "AMD Milan",
                "scheduling": {
                  "automaticRestart": true,
                  "nodeAffinities": [],
                  "onHostMaintenance": "TERMINATE",
                  "preemptible": false
                },
                "disks": [
                  {
                    "boot": true,
                    "initializeParams": {
                      "sourceImage": "projects/ubuntu-os-cloud/global/images/family/ubuntu-2404-lts-amd64"
                    }
                  }
                ],
                "networkInterfaces": [
                  {
                    "nicType": "gVNIC"
                  }
                ]
              }' \
          https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    $body = @"
    {
      "name": "my-instance",
      "confidentialInstanceConfig": {
        "confidentialInstanceType": "SEV_SNP"
      },
      "machineType": "zones/us-central1-a/machineTypes/n2d-standard-2",
      "minCpuPlatform": "AMD Milan",
      "scheduling": {
        "automaticRestart": true,
        "nodeAffinities": [],
        "onHostMaintenance": "TERMINATE",
        "preemptible": false
      }
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/ubuntu-os-cloud/global/images/family/ubuntu-2404-lts-amd64"
          }
        }
      ],
      "networkInterfaces": [
        {
          "nicType": "gVNIC"
        }
      ]
    }
    "@
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://compute.googleapis.com/compute/projects/my-project/zones/us-central1-a/instances" | Select-Object -Expand Content

### Response

A response to a creation request looks similar to the following example:
    
    
    {
      "kind": "compute#operation",
      "id": "0000000000000000000",
      "name": "operation-0000000000000-0000000000000-00000000-00000000",
      "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a",
      "operationType": "insert",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance",
      "targetId": "0000000000000000000",
      "status": "RUNNING",
      "user": "alex@example.com",
      "progress": 0,
      "insertTime": "2024-09-29T18:06:52.174-07:00",
      "startTime": "2024-09-29T18:06:52.175-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/operations/operation-0000000000000-0000000000000-00000000-00000000"
    }
    

You can check the VM creation progress by making a `GET` request to the `selfLink`:
    
    
    GET https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE_NAME/operations/OPERATION_ID
    

## Enable higher network bandwidth for specific machine types

Larger machine types support high-bandwidth networking. When you select a Tier_1 network bandwidth configuration, the data transfer out bandwidth increases from the default 32 Gbps to 50 to 200 Gbps, depending on the machine type. To achieve the higher Tier_1 bandwidth speeds, your instance must be running the [gVNIC virtual network driver](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-gvnic). Learn more about [configuring a VM with higher bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

## What's next

Learn how to use [Cloud Monitoring to validate your Confidential VM instances](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/monitor-integrity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
