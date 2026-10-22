---
url: https://docs.cloud.google.com/compute/docs/images/creating-an-image-from-an-iso-file/
title: Create a persistent disk image from an ISO file \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:19.809933+00:00
---

# Create a persistent disk image from an ISO file  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/creating-an-image-from-an-iso-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a persistent disk image from an ISO file Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

Installation media for Windows applications is often provided as an ISO file, but Compute Engine does not let you expose an ISO file as a virtual DVD drive to a VM instance.

To access the contents of the ISO file on a single Windows VM, you can do either of the following:

  * Copy the ISO file to the VM and [mount it locally](https://docs.microsoft.com/en-us/powershell/module/storage/mount-diskimage?view=win10-ps). This approach works well if you only need to access the contents of the ISO file on a single VM instance.

  * Create a Persistent Disk from the ISO file and attach the disk in read-only mode to one or more VM instances. This approach works well if multiple VMs need access to the contents of the ISO file.




This document describes how you can create a Persistent Disk from the ISO file and attach the disk in read-only mode to one or more VMs.

**Note:** The process described in this document does not apply to creating bootable operating system images from ISO files. For creating a bootable operating system image, see [Creating custom Windows BYOL images](https://docs.cloud.google.com/compute/docs/images/creating-custom-windows-byol-images).

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




## Prepare the ISO file

If the ISO file is publicly available via HTTP, you do not need to download the ISO file first. To use a local ISO file, you can upload the ISO file to Cloud Storage.

###  HTTP URL 

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Create an environment variable for the download URL. The URL can be an HTTP or HTTPS URL, but it must be accessible anonymously.
         
         ISO_URL=https://example.com/big.iso
         




###  Local ISO file 

  1. In the Google Cloud console, [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. [Upload the ISO file](https://docs.cloud.google.com/storage/docs/uploading-objects).

Depending on the size of the ISO file, the upload can take several minutes or hours.

  3. In the [Storage browser](https://console.cloud.google.com/storage/browser), navigate to the uploaded object.

  4. On the **Object details** page, copy the URI of the object. The URI starts with `gs://`.

  5. Open [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  6. Create an environment variable for the download URL. Replace `URI` with the URI that you copied.
         
         ISO_URL=URI
         




## Create a disk containing the contents of the ISO file

To copy the contents of the ISO file to a new disk, create a temporary VM, then create an image from the disk:

  1. From Cloud Shell, specify the name that you want to assign to the new disk:
         
         DISK_NAME=iso
         

  2. Create a new disk to which to copy the contents of the ISO files:
         
         gcloud compute disks create $DISK_NAME \
           --size=10GB \
           --zone=$(gcloud config get-value compute/zone)
         

Use a larger disk size if your ISO file exceeds 9 GB.

  3. Create a startup script for the temporary VM. The startup script performs the following actions:

     1. Format the secondary disk with the NTFS file system.
     2. Download the ISO file from the HTTP or Cloud Storage URL you specified.
     3. Mount the ISO file and copy its contents to the secondary disk.
    
    cat << "EOF" > startup.ps1
    
    $DownloadDirectory = 'c:\download\'
    $ErrorActionPreference = 'Stop'
    $MetadataUrl = 'http://metadata.google.internal/computeMetadata/v1/instance'
    
    $DownloadUrl = (Invoke-RestMethod `
        -Headers @{"Metadata-Flavor" = "Google"} `
        -Uri "$MetadataUrl/attributes/iso")
    
    mkdir $DownloadDirectory\Source -Force
    
    Write-Host '== Formatting secondary disk... ===' -ForegroundColor Black -BackgroundColor Yellow
    Set-Disk -Number 1 -IsOffline $false
    Clear-Disk -Number 1 -RemoveData -Confirm:$false -ErrorAction SilentlyContinue
    Initialize-Disk -Number 1 -PartitionStyle MBR
    New-Partition -DiskNumber 1 -UseMaximumSize -DriveLetter D -IsActive |
    Format-Volume -FileSystem 'NTFS' -Confirm:$false
    
    Write-Host '== Downloading ISO... =============' -ForegroundColor Black -BackgroundColor Yellow
    if ($DownloadUrl.StartsWith('gs:')) {
        & gcloud storage cp $DownloadUrl "$DownloadDirectory\Source\image.iso" | Out-Default
    }
    else {
        Import-Module BitsTransfer
        Start-BitsTransfer -Source $DownloadUrl -Destination "$DownloadDirectory\Source\image.iso"
    }
    
    Write-Host '== Mounting ISO... ================' -ForegroundColor Black -BackgroundColor Yellow
    Mount-DiskImage -ImagePath "$DownloadDirectory\Source\image.iso" -StorageType ISO
    
    Write-Host '== Copying ISO contents... ========' -ForegroundColor Black -BackgroundColor Yellow
    Copy-Item 'e:\*' 'd:\' -Force -Recurse -PassThru `
        | Where-Object { -Not $_.PSIsContainer } `
        | Set-ItemProperty -Name IsReadOnly -Value $False
    
    Write-Host '== Completed. =====================' -ForegroundColor Black -BackgroundColor Yellow
    Invoke-RestMethod `
        -Headers @{'Metadata-Flavor'='Google'}  `
        -Method PUT  `
        -Uri "$MetadataUrl/guest-attributes/vm/ready" `
        -Body true
    EOF
    

  4. Create a Windows Server 2019 VM that uses the startup script and the disk that you created previously:
         
         gcloud compute instances create iso-copier \
             --machine-type=n1-standard-2 \
             --image-family=windows-2019-core \
             --image-project=windows-cloud \
             --disk=name=$DISK_NAME,auto-delete=no \
             --metadata=enable-guest-attributes=true,iso=$ISO_URL \
             --metadata-from-file=windows-startup-script-ps1=startup.ps1 \
             --scopes=https://www.googleapis.com/auth/devstorage.read_only
         

The VM takes about 2 minutes to start. Depending on the size of the ISO file, it can take another 5-15 minutes for the file copy operation to complete. You can observe the progress by running the following command:
         
         gcloud compute instances tail-serial-port-output iso-copier \
             --zone=$(gcloud config get-value compute/zone)
         

  5. Wait for the VM to finish running the startup script:
         
         until gcloud compute instances get-guest-attributes iso-copier \
             --zone=$(gcloud config get-value compute/zone) \
             --query-path=vm/ready > /dev/null 2>&1
         do
             sleep 5 && echo waiting for VM to finish...
         done
         

  6. Shut down and delete the VM:
         
         gcloud compute instances delete iso-copier \
             --zone=$(gcloud config get-value compute/zone) \
             --quiet
         

Notice that the secondary disk is not deleted because it was mounted with the parameter `auto-delete=no`.




The disk is now ready to be used. You can [attach the disk in read-only mode to one or more VM instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms) within the same zone.

## Share the disk across zones and regions by creating an image

To make the contents of the ISO file available in other zones or regions, create a Compute Engine image:

  1. From Cloud Shell, create an image from the disk that you created in the previous section:
         
         gcloud compute images create $DISK_NAME \
             --source-disk=$DISK_NAME \
             --source-disk-zone=$(gcloud config get-value compute/zone)
         




## Clean up

To avoid incurring further costs after you have completed this process, you can delete the resources that you created:

  1. Delete the disk:
         
         gcloud compute disks delete $DISK_NAME \
             --zone=$(gcloud config get-value compute/zone) \
             --quiet
         

  2. Delete the image:
         
         gcloud compute images delete $DISK_NAME
         




## What's next

  * Learn how to [create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images).

  * Learn how to [manage access to custom images](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images).

  * Learn more about [Windows workloads on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
