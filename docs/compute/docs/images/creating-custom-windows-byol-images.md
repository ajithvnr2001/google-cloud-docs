---
url: https://docs.cloud.google.com/compute/docs/images/creating-custom-windows-byol-images/
title: Create custom Windows BYOL images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:04.266973+00:00
---

# Create custom Windows BYOL images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/creating-custom-windows-byol-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create custom Windows BYOL images Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

To create a Windows VM on Google Cloud, you must use a VM image that has Windows or Windows Server preinstalled. Google Cloud provides [public images](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) for commonly used versions of Windows Server, but these images are only suitable for [on-demand licensing](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#on-demand). To bring your own Windows license (BYOL), you must either [import an existing image](https://docs.cloud.google.com/compute/docs/import), or you must build a custom image.

This guide describes how you can create a custom image by using the same tools and processes that Google Cloud uses to create the public images.

To complete this guide, you need:

  * An ISO file containing the Windows or Windows Server installation media.
  * Optionally, one or more Windows update packages (in `.msu` format) to apply to the image.

**Note:** To test the image building process, you can use the [Windows Server Evaluation](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019) media.

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




## Understand the build process

To install Windows from scratch, a common approach is to boot a computer from a DVD or ISO file that contains the Windows installation files. Unlike some on-premises hypervisors, Compute Engine does not let you boot from an ISO file.

To install Windows from scratch, you must therefore follow a different approach that entails the following steps:

  1. Creating a new disk.
  2. Extracting the Windows image (`install.wim` from the installation media) to the disk.
  3. Adding necessary drivers, configuring Windows Setup so that it runs unattended, and making the disk bootable.
  4. Booting from the new disk to run Windows Setup.
  5. Installing additional software including the Guest OS agent.
  6. Creating an image from the disk.



Instead of performing these steps manually, this guide describes how you can use [Cloud Build](https://docs.cloud.google.com/build/docs/overview), the `daisy` tool, and the reference workflows which are [available on GitHub](https://github.com/GoogleCloudPlatform/compute-image-tools/tree/master/daisy_workflows/image_build/windows) to automate the process.

`daisy` is an [open source command-line tool](https://github.com/GoogleCloudPlatform/compute-image-tools/blob/master/daisy/README.md) that lets you execute workflows. Workflows are authored as JSON files and contain a sequence of steps. Each such step describes a Compute Engine operation – for example, creating a disk, or shutting down a VM instance. Daisy workflows are therefore suitable to automate the steps required to build a Windows image from scratch.

The daisy workflows for building custom Windows images create two temporary VM instances. The first VM instance (prefixed `bootstrap`) performs the necessary steps to create a bootable disk. The second VM instance (prefixed `install`) runs Windows Setup and performs all the remaining steps.

## Prepare the project for building images

To prevent the daisy tool from interfering with your existing VM instances or infrastructure, create a dedicated project for building images:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, Cloud Build API, and Cloud Storage API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=storage.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, Cloud Build API, and Cloud Storage API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=storage.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com)


**Note:** The build process assumes that your project contains a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network). If you've [disabled the creation of default networks](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) in your organization, you must manually create an auto-mode VPC network named `default`.

The next steps differ depending on whether you use Windows or Linux on your local computer:

###  Windows 

  1. On your local computer, open a Windows PowerShell window.
  2. Initialize a variable:
         
         $PROJECT_ID = "PROJECT_ID"
         

where `PROJECT_ID` is the project ID of the Google Cloud project that you created in the previous section.

  3. Initialize another variable so that it contains the project number of the project:
         
         $PROJECT_NUMBER = gcloud projects describe $PROJECT_ID --format=value`(projectNumber`)
         




###  Linux 

  1. On your local computer, open a terminal window.
  2. Initialize a variable:
         
         PROJECT_ID=PROJECT_ID
         

where `PROJECT_ID` is the project ID of the Google Cloud project that you created in the previous section.

  3. Initialize another variable so that it contains the project number of the project:
         
         PROJECT_NUMBER=`gcloud projects describe $PROJECT_ID --format=value\(projectNumber\)`
         




## Upload installation files

You now collect all the installation files required for the custom image and upload them to a Cloud Storage bucket. By storing the files in a Cloud Storage bucket, you ensure that the files are accessible by `daisy` and by the temporary VM instances that `daisy` uses to build the image.

In the following steps, replace `UNIQUE_SUFFIX` with a short sequence of random characters to create a unique bucket name. For example, use `PROJECT_ID-media-a7g19`. Appending a random suffix to the bucket name helps prevent [bucket squatting](https://owasp.org/www-community/attacks/Bucket_Name_Squatting), a vulnerability where an attacker might gain control over your build process by pre-claiming a bucket with a predictable name.

  1. On your local computer, download required installation packages:

     * [gcloud CLI](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe)
     * [Microsoft .NET Framework 4.8 offline installer for Windows](https://support.microsoft.com/en-us/help/4503548/microsoft-net-framework-4-8-offline-installer-for-windows)
     * [PowerShell 7.0 (or later)](https://learn.microsoft.com/en-au/powershell/scripting/install/installing-powershell-on-windows#installing-the-msi-package) (`.msi`)
  2. Create a new Cloud Storage bucket to store the installation files:
         
         gcloud storage buckets create gs://$PROJECT_ID-media-UNIQUE_SUFFIX --project=$PROJECT_ID
         

  3. Grant the [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) role to Cloud Build so that it can read the installation files:
         
         gcloud storage buckets add-iam-policy-binding gs://$PROJECT_ID-media-UNIQUE_SUFFIX --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role=roles/storage.objectViewer
         

  4. Upload the PowerShell installation package:
         
         gcloud storage cp POWERSHELL_PACKAGE gs://$PROJECT_ID-media-UNIQUE_SUFFIX/PowerShell.msi
         

where `POWERSHELL_PACKAGE` is the path to the PowerShell installation package.

  5. Upload the .NET Framework installation package:
         
         gcloud storage cp DOTNET_PACKAGE gs://$PROJECT_ID-media-UNIQUE_SUFFIX/dotnet-sdk.exe
         

where `DOTNET_PACKAGE` is the path to the NET Framework installation package.

  6. Upload the gcloud CLI installation package:
         
         gcloud storage cp CLOUDSDK_PACKAGE gs://$PROJECT_ID-media-UNIQUE_SUFFIX/GoogleCloudSDKInstaller.exe
         

where `CLOUDSDK_PACKAGE` is the path to the gcloud CLI installation package.

  7. Upload the ISO file containing your Windows installation media:
         
         gcloud storage cp ISO gs://$PROJECT_ID-media-UNIQUE_SUFFIX/
         

where `ISO` is the name of the ISO file.

  8. Optionally, upload additional update packages:
         
         gcloud storage cp UPDATE_DIR/*.msu gs://$PROJECT_ID-media-UNIQUE_SUFFIX/updates/
         

where `UPDATE_DIR` is the directory containing the update packages.




You are now ready to build the custom image.

## Build the image

Executing the `daisy` workflow to build a custom image takes up to four hours. Instead of running `daisy` locally, you now create a Cloud Build configuration so that you can let Cloud Build execute the workflow in the background.

  1. On your local computer, clone the Git repository containing the `daisy` workflows for building Windows images:
         
         git clone https://github.com/GoogleCloudPlatform/compute-image-tools.git
         

  2. Switch to `windows` directory:
         
         cd compute-image-tools/daisy_workflows/image_build/windows/
         

  3. In the `windows` directory, you find a selection of files with the suffix `.wf.json`. These files contain Daisy workflow definitions for commonly used Windows versions:

Windows version | Workflow file  
---|---  
Windows Server Core 2022 (64-bit)  | `windows-server-2022-dc-core-uefi-byol.wf.json`  
Windows Server 2019 (64-bit)  | `windows-server-2019-dc-uefi-byol.wf.json`  
Windows Server Core 2019 (64-bit)  | `windows-server-2019-dc-core-uefi-byol.wf.json`  
Windows Server 2016 (64-bit)  | `windows-server-2016-dc-uefi-byol.wf.json`  
Windows Server Core 2016 (64-bit)  | `windows-server-2016-dc-core-uefi-byol.wf.json`  
Windows 11 21H2 (64-bit)  | `windows-11-21h2-ent-x64-uefi.wf.json`  
Windows 11 22H2 (64-bit)  | `windows-11-22h2-ent-x64-uefi.wf.json`  
Windows 11 23H2 (64-bit)  | `windows-11-23h2-ent-x64-uefi.wf.json`  
Windows 10 21H2 (64-bit)  | `windows-10-21h2-ent-x64-uefi.wf.json`  
Windows 10 22H2 (64-bit)  | `windows-10-22h2-ent-x64-uefi.wf.json`  
  
Open the workflow file that most closely matches the Windows version that you want to install. If necessary, change the Windows edition (`edition`) and license key (`product_key`) settings in the workflow files so that they match your installation media.

If you are unsure about the correct edition name, open an elevated PowerShell prompt and run the following commands to list all editions supported by your installation media:
         
         $IsoFile = "ISO"
         
         $Mount = Mount-DiskImage -ImagePath (Resolve-Path $IsoFile)
         
         $DriveLetter = ($Mount | Get-Volume).DriveLetter
         Get-WindowsImage -ImagePath "$($DriveLetter):\sources\install.wim" | select ImageName
         
         Dismount-DiskImage -InputObject $Mount | Out-Null
         

Replace `ISO` with the local path to the ISO image.

  4. In the `windows` directory, create a new file named `cloudbuild.yaml` and paste the following code:
         
         timeout: 14400s  # 4 hour timeout for entire build
         steps:
         - name: 'gcr.io/compute-image-tools/daisy'
           timeout: 14400s  # 4 hour timeout for build step
           waitFor: ['-']
           args:
             - -project=$PROJECT_ID
             - -zone=us-central1-a
             - -var:updates=gs://$PROJECT_ID-media-UNIQUE_SUFFIX/updates/
             - -var:pwsh=gs://$PROJECT_ID-media-UNIQUE_SUFFIX/PowerShell.msi
             - -var:dotnet48=gs://$PROJECT_ID-media-UNIQUE_SUFFIX/dotnet-sdk.exe
             - -var:cloudsdk=gs://$PROJECT_ID-media-UNIQUE_SUFFIX/GoogleCloudSDKInstaller.exe
             - -var:media=gs://$PROJECT_ID-media-UNIQUE_SUFFIX/ISO
             - WORKFLOW
         

Replace:

     * `ISO`: name of the ISO file on Cloud Storage.
     * `WORKFLOW`: name of the workflow file that corresponds to the Windows version that you're using.
**Note:** Some workflows support additional, optional parameters to customize the build process. You can find the complete list of parameters in the `Vars` section of the workflow file.
  5. Submit the build to Cloud Build:
         
         gcloud builds submit --project $PROJECT_ID --async
         

The build takes around up to four hours to complete. You can track the status of the build in the Google Cloud console under **Cloud Build > History**.

[ Cloud Build History](https://console.cloud.google.com/cloud-build/builds)




## Use the custom image

After the build has completed, you can find the custom BYOL image in the Google Cloud console under **Compute Engine > Images**.

To help differentiate between multiple versions of the same image, the build process embeds a timestamp into the image name, for example `windows-server-2019-dc-v1613488342`. In addition, the process associates the image with a custom [image family](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#custom-families), for example `windows-server-2019`.

To create a VM instance that uses the custom BYOL image, you must [provision the VM instance on a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).

**Note:** The image build process does not configure a KMS server. If you're using a volume licensed copy of Windows Server, you must [configure a KMS server](https://docs.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options#kms-client-options) before you can activate Windows Server.

## Troubleshooting

If you suspect that the build process failed or is not progressing, use the following approaches to diagnose the situation:

  * Verify that you've uploaded the right installation packages and ISO file.
  * Verify that you selected a workflow that matches the Windows version of the ISO file.
  * Review the [build log in Cloud Build ](https://docs.cloud.google.com/build/docs/view-build-results#console) and check whether there are any error messages.
  * If the build seems stuck, review the [serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) of the VM instance created by the build and check for error messages.



## What's next

  * Find out more [about the daisy tool](https://github.com/GoogleCloudPlatform/compute-daisy).
  * Learn more about [daisy workflows for building images](https://github.com/GoogleCloudPlatform/compute-image-tools/tree/master/daisy_workflows/image_build).
  * Learn how to [bring existing licenses to Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license).
  * Read about [best practices for working with image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
