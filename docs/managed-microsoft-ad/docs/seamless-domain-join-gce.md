---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce/
title: Join a Windows VM automatically to a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:50.792312+00:00
---

# Join a Windows VM automatically to a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Join a Windows VM automatically to a domain Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to join a Windows Compute Engine VM instance to a domain using the automated domain join feature in Managed Service for Microsoft Active Directory.

## How Managed Microsoft AD joins a Windows VM automatically to a domain

To use Managed Microsoft AD for authenticating the applications running on your VMs, you need to join the VMs to your Managed Microsoft AD domain. The domain join process usually involves performing some manual steps.

When you create or update a Windows Compute Engine VM, you can join the VM to your Managed Microsoft AD domain by automating [the manual approach](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows) using scripts. However, to execute these scripts on a Compute Engine VM, you require AD credentials that need to be securely stored and maintained, and an environment to provision and run these scripts. To eliminate the need for credentials and an additional service, you can automate the domain join process with ready-made scripts that are available from Managed Microsoft AD.

When you create Compute Engine VMs, you can use scripts to automatically join the VMs to your Managed Microsoft AD domain. After Compute Engine creates the VMs, Managed Microsoft AD initiates the domain join request and attempts to join the VMs with your domain. If the domain join request succeeds, Managed Microsoft AD joins the created VMs to your domain. If the domain join request fails, the created VMs continue to run. For security or billing purposes, you can customize this behavior and Managed Microsoft AD can stop the VMs when the domain join request fails.

When you update Compute Engine VMs, you can use scripts to automatically join the existing VMs to your Managed Microsoft AD domain. For the domain join request to succeed, Managed Microsoft AD restarts the VMs after running the scripts.

## Before you begin

  1. [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain).

  2. Make sure that the VM name has a maximum of 15 characters.

  3. Make sure that the VM runs on a [Windows version that Managed Microsoft AD supports](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions#windows-domain-join).

  4. [Configure domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-peering) between the Managed Microsoft AD domain and the VM's network, or have both the Managed Microsoft AD domain and the VM in the same network.

  5. Create a service account with the Google Cloud Managed Identities Domain Join (`roles/managedidentities.domainJoin`) IAM role on the project that has the Managed Microsoft AD domain. For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).

     * For more information about granting roles, see [Grant a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#grant-single-role).

     * For information about creating a service account, see [Authenticate workloads using service accounts](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

  6. Set the full `cloud-platform` access scope on the VM. For more information, see [Authorization](https://docs.cloud.google.com/compute/docs/access/service-accounts#authorization).




## Metadata

You need the following metadata keys to join a Windows VM to a domain.

Metadata keys | Description  
---|---  
`windows-startup-script-url` | Use this metadata key to specify the publicly-accessible location of the Windows startup script that the VM executes during the startup process. To use the Windows startup script that is pre-delivered by Managed Microsoft AD, you can enter the following URL: `<https://raw.githubusercontent.com/GoogleCloudPlatform/managed-microsoft-activedirectory/main/domain_join.ps1>`.  
  
If the VM doesn't have access to this URL, you can pass the startup script using any one of the other supported methods. For more information, see [Using startup scripts on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows).   
`managed-ad-domain` | Use this metadata key to specify the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Managed Microsoft AD domain to join, in the form of: `projects/PROJECT_ID/locations/global/domains/DOMAIN_NAME`. For example, `projects/my-project-123/locations/global/domains/my-domain.example.com`.  
`managed-ad-domain-join-failure-stop` | Optional: By default, the VM continues to run even after the domain join request fails. You can set this metadata key to `TRUE` if you want to stop the VM when the request fails. Managed Microsoft AD can stop the VM after you set this metadata key, but it doesn't delete the VM.  
`enable-guest-attributes` | Optional: By default, the guest attributes are disabled on a VM. You can set this metadata key to `TRUE` if you want to use the VM's [guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes) to log the domain join status after the execution of startup script.  
  
Managed Microsoft AD writes the domain join status in the following keys under the `managed-ad` namespace of `guest-attributes`: 
* `domain-join-status`: This key provides the status of the domain join request after the execution of script.
* `domain-join-failure-message`: If the domain join request fails, this key provides the error message.
When you [get the guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes#get_guest_attributes), you can use these namespace and keys to view the domain join status.   
`managed-ad-ou-name` | Optional: By default, Managed Microsoft AD joins the VM to the `GCE Instances` organizational unit (OU) that is pre-created under the `Cloud` OU to better manage the policies. For more information about the `Cloud` OU, see [Organizational units](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#organizational_units).  
  
If you want to join the VM to a custom OU, you need to create the custom OU either under the `GCE Instances` OU or the `Cloud` OU in Managed Microsoft AD and use this metadata key to specify the custom OU. Managed Microsoft AD doesn't support a custom OU that you create anywhere other than under the `Cloud` OU or the `GCE Instances` OU.  
  
If you create a custom OU under the `Cloud` OU, specify the path of the custom OU in the following format: `/cloud/SUB_OU1/SUB_OU2/…/CUSTOM_OU`. For example, `/cloud/my-sub-ou/my-custom-ou`.  
  
For more information about managing AD objects in Managed Microsoft AD, see [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).   
`managed-ad-force` | Optional: When you delete a VM that you have joined with a domain, the computer account of the VM continues to exist in Managed Microsoft AD. When you try to join another VM with the same computer account, the domain join request fails by default. Managed Microsoft AD can reuse an existing computer account if you set this metadata key to `TRUE`.   
  
## Join the Windows VM

You can use these [metadata keys](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#metadata) when you either create a Windows VM or update an existing VM. The following sections illustrate how to use these metadata keys in gcloud CLI commands when you create a VM or update a VM.

However, you can use these metadata keys with a VM using the other available options as well. For more information about using metadata with a Windows Compute Engine VM, see [Set custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

### Join a Windows VM during creation

To create and join a Windows Compute Engine VM, run the following gcloud CLI command:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --metadata=windows-startup-script-url=URL,managed-ad-domain=DOMAIN_RESOURCE_PATH,managed-ad-domain-join-failure-stop=TRUE,enable-guest-attributes=TRUE \
        --service-account=SERVICE_ACCOUNT \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --image-project windows-cloud \
        --image-family IMAGE_FAMILY
    

Replace the following:

  * INSTANCE_NAME: Name of the Windows Compute Engine VM to create. For example, `my-instance-1`.
  * URL: A publicly-accessible location of the Windows startup script that the VM executes during the startup process.
  * DOMAIN_RESOURCE_PATH: Full resource name of your Managed Microsoft AD domain to join. For example, `projects/my-project-123/locations/global/domains/my-domain.example.com`.
  * SERVICE_ACCOUNT: A service account that you want to attach to the VM. For example, `my-sa-123@my-project-123.iam.gserviceaccount.com`.
  * `--scopes`: The default access scopes configured in the VM restricts the domain join request. You need to set the full `cloud-platform` access scope on the VM. For more information, see [Authorization](https://docs.cloud.google.com/compute/docs/access/service-accounts#authorization).
  * `--image-project`: You need to set this flag as `windows-cloud` to create a Windows VM. For more information, see [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
  * IMAGE_FAMILY: Specify one of the [public image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that has images for the [supported Windows versions](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions#windows-domain-join). For example, `windows-2019-core`.



For more information about adding metadata during VM creation, see [Set metadata during VM creation](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set_during_creation).

### Join an existing Windows VM

You can update the [metadata keys](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#metadata) on an existing Windows Compute Engine VM and join the VM to your domain. After you add these metadata keys to the VM, restart the VM so that the domain join request succeeds.

**Caution:** If you already have a startup script that is passed to the VM using the `windows-startup-script-url` metadata key, the following approach can replace the existing startup script with the automated domain join startup script. Instead, you can use any other suitable [metadata key](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#metadata-keys) to pass the existing startup script, except the `windows-startup-script-url` metadata key. For example, `windows-startup-script-ps1`. For information about the script execution sequence, see [Order of execution of Windows startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#order_of_execution_of_windows_startup_scripts).

To join an existing Windows Compute Engine VM, run the following gcloud CLI command:
    
    
    gcloud compute instances add-metadata INSTANCE_NAME \
        --metadata=windows-startup-script-url=URL,managed-ad-domain=DOMAIN_RESOURCE_PATH,managed-ad-domain-join-failure-stop=TRUE,enable-guest-attributes=TRUE \
        --service-account=SERVICE_ACCOUNT \
        --scopes=https://www.googleapis.com/auth/cloud-platform
    

Replace the following:

  * INSTANCE_NAME: Name of the Windows Compute Engine VM that you want to join. For example, `my-instance-1`.
  * URL: A publicly-accessible location of the Windows startup script that the VM executes after restart.
  * DOMAIN_RESOURCE_PATH: Full resource name of your Managed Microsoft AD domain to join. For example, `projects/my-project-123/locations/global/domains/my-domain.example.com`.
  * SERVICE_ACCOUNT: The service account that you have attached the VM during creation. For example, `my-sa-123@my-project-123.iam.gserviceaccount.com`.
  * `--scopes`: The default access scopes configured in the VM restricts the domain join request. You need to set the full `cloud-platform` access scope on the VM. For more information, see [Authorization](https://docs.cloud.google.com/compute/docs/access/service-accounts#authorization).



For more information about adding metadata to an existing VM, see [Updating metadata on a running VM](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#update_metadata).

## Clean up unjoined VMs

We recommend to delete the computer account manually from Managed Microsoft AD in the following scenarios:

  * If you delete a VM that you have joined with the Managed Microsoft AD domain.
  * If a VM has failed to join with the Managed Microsoft AD domain.



## View debug logs

If the domain join request fails, you can check the logs for the startup script to identify and troubleshoot the issue. To check the logs for the startup script, you can [view Serial port 1 output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#viewing_serial_port_output). If you have enabled guest attributes on the VM, you can [get the guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes#get_guest_attributes) to view the logs.

For information about the common errors that you can encounter while joining a VM to a domain, see [Unable to join a Windows VM automatically to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#domain-join-windows).

## What's next

  * [Join GKE Windows Server nodes automatically to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
