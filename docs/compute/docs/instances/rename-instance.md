---
url: https://docs.cloud.google.com/compute/docs/instances/rename-instance/
title: Rename a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:16.434816+00:00
---

# Rename a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/rename-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Rename a VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you create a virtual machine (VM) instance, you must specify a name. After creating the VM, you can optionally rename it. Changing a VM name might be useful in the following scenarios:

  * To better represent the workload running on the VM.
  * To refer to the operating system running on the VM.
  * To adhere to any naming conventions required by your organization.



## VM uniform resource identifiers (URIs)

Changing the name of a VM might affect your projects. Instead of referencing VM resources by their name, you can reference them by their URI, which is permanent. The URI has the following format:
    
    
    projects/PROJECT_ID/zones/ZONE/instances/VM_ID
    

The URI includes the following values:

  * `PROJECT_ID`: the ID of the project where the VM is located.

  * `ZONE`: the zone where the VM is located.

  * `VM_ID`: the ID of an existing VM. To view the ID of an existing VM, [view the details of the VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details) and then view the value of the `id` field.




## Pricing

Renaming a VM does not change the amount that you are billed. Also, because your bill shows VMs according to their stock keeping units (SKUs) and not their names, you won't see the names of your VMs on your bill.

## Limitations

Limitations on the following apply when renaming a VM:

  * **Automatically named resources:**

    * When you rename a VM, the names of any resources that were based on the original VM name are not updated. For example, when you create a VM, the name of the boot disk is the same as the name of the VM. If you rename the VM, the name of the boot disk does not change.
  * **Static IP addresses:**

    * Static IP addresses used by a renamed VM might not update to indicate that they're being used by the VM's new name. 
  * **DHCP server:**

    * After renaming a VM, the DHCP server responds to DHCP requests with the updated hostname with the format `HOSTNAME.c.PROJECT_ID.internal` for global DNS and `HOSTNAME.ZONE.c.PROJECT_ID.internal` for zonal DNS. For more information, see [Types of internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).
  * **Google Cloud console:**

    * You must refresh your browser for the Google Cloud console to update the name of the VM.
  * **Hostnames:**

    * Hostnames are modified on Linux when you change the name of the instance. On Windows, the hostname is not updated, even after you restart the instance.

    * VMs that have [custom hostnames](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm) are not updated.

    * Changing the hostname directly on the host does not affect the name of the VM resource.

  * **Instance groups:**

    * You can't rename instances that are part of an unmanaged or managed instance group (MIG).
  * **Naming conventions:**

    * You can't rename a VM with a name that is already in use by another VM in the project.

    * VM names must adhere to the [resource naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  * **VM states:**

    * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) before renaming it because you can only rename VMs that are in the `TERMINATED` state. You can't, for example, rename a VM that is in the `SUSPENDED` state.



## Before you begin

  * Review, and if applicable, update the following: 
    * [Cloud Monitoring groups, charts, and alerts: ](https://docs.cloud.google.com/monitoring/docs) Monitoring matches strings, and when you rename a VM, these strings are not updated. If you rename a VM, update your Monitoring rules to include the renamed VMs in your reports. 
    * [Console URLs](https://console.cloud.google.com/): Renaming a VM changes its console URL. If you rename a VM, you must update links, such as browser bookmarks that reference the VM's console URL. 
    * [Identity and Access Management (IAM) conditional role bindings](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings): Conditional role bindings support granting permissions on the name of the resource. For example, IAM might grant a role to a user if the name of a VM begins with a particular string. These bindings are not updated when you change the name of a VM, so a user's access to the VM resource might be affected because you are changing the set of VMs that the prefixed name applies to. If you rename a VM, update these bindings. 
    * [Internal DNS service cache](https://docs.cloud.google.com/compute/docs/internal-dns): The internal DNS service assigns internal DNS names to VMs, in which the hostname is of the format `HOSTNAME.c.PROJECT_ID.internal` for global DNS and `HOSTNAME.ZONE.c.PROJECT_ID.internal` for zonal DNS. After renaming a VM, these hostnames change. Then, the internal DNS service begins resolving to the new hostname, and requests to the previous DNS name fail. If you rename a VM, you might need to update your DNS cache to update the hostname. For more information about global DNS and zonal DNS hostnames, see [Types of internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names). 
    * [Metadata queries](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata): After renaming a VM, the metadata server reports the new name. If you rename a VM, update any scripts or programs that query the metadata server so they query for the VM's new name. 
    * [ Organization policies restricting external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip): Constraints against VMs that have an external IP address reference the VM name. When you rename a VM, this constraint is not updated. If you rename a VM, update the external IP organization policy with the VM's new name. 
    * [ SQL Server host names](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances): If you rename a VM that hosts SQL Server, you must update the SQL server VM name. For more information, see [Rename a computer that hosts a stand-alone instance of SQL Server](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/rename-a-computer-that-hosts-a-stand-alone-instance-of-sql-server?view=sql-server-ver15#rename-a-computer-that-hosts-a-stand-alone-instance-of-). 
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

To get the permission that you need to rename a VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.instances.setName` permission, which is required to rename a VM. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Rename a VM

You can only rename stopped VMs that are in the `TERMINATED` state.

###  Console 

To rename a VM, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM.

  3. If you haven't already, click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

  4. Click edit **Edit**.

  5. In the **VM instance name** field, enter a new name for the VM.

  6. Click **Save**.

Renaming the VM can take up to a minute to complete. If, after renaming the VM, you get an error that Google Cloud is unable to find the VM, refresh your browser.

  7. If you need to, restart the VM by clicking play_arrow **Start / Resume**.




###  gcloud 

To rename a VM, do the following:

  1. If you haven't already, [stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. To rename the VM, use the [`gcloud compute instances set-name` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-name).
         
         gcloud compute instances set-name VM_NAME \
             --new-name=NEW_VM_NAME \
             --project=PROJECT_ID \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of an existing VM.

     * `NEW_VM_NAME`: the new name for the specified VM.

     * `PROJECT_ID`: the ID of the project where the VM is located.

     * `ZONE`: the zone where the VM is located.

Renaming the VM can take up to a minute to complete.

  3. If you need to, [restart the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance).




###  REST 

To rename a VM, do the following:

  1. If you haven't already, [stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. To rename the VM, make a `POST` request to the [`instances.setName` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setName).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setName
         
         {
           "currentName": "VM_NAME",
           "name": "NEW_VM_NAME"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the VM is located.

     * `ZONE`: the zone where the VM is located.

     * `VM_NAME`: the name of an existing VM.

     * `NEW_VM_NAME`: the new name for the specified VM.

Renaming the VM can take up to a minute to complete. To monitor the status of the renaming, poll the operation ID returned by the rename API. For more information, see [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses).

  3. If you need to, [restart the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance).




## What's next

  * Learn how to [view the details of the VM](https://docs.cloud.google.com/compute/docs/instances/get-instance-id).

  * Learn how to [stop or restart a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

  * Learn how to [suspend or resume a VM](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance).

  * Learn more about [VMs lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
