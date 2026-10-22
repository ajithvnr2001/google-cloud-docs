---
url: https://docs.cloud.google.com/compute/docs/instances/transfer-files/
title: Transfer files to Linux VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:07.385818+00:00
---

# Transfer files to Linux VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/transfer-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Transfer files to Linux VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

To transfer files to Compute Engine VM instances, different options are available depending on your workstation OS and the target VM instance OS.

Transfer from | To Linux VMs  
---|---  
Linux or macOS | 

  * Cloud Storage
  * Google Cloud CLI
  * SSH-in-browser
  * SCP

  
Windows | 

  * Cloud Storage
  * Google Cloud CLI
  * WinSCP



## Transfer files through Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage) buckets can be used as a transfer point between you and your VMs. You can use a web browser, the Google Cloud CLI, or a programming language to transfer files between Cloud Storage and Compute Engine VMs.  Different credential types can be used for the upload and download step to best suit your needs: 

  * [Accessing data on a user's behalf](https://docs.cloud.google.com/storage/docs/user-accounts) is best for single use operations, or resources that you are primarily responsible for. 
  * Consider [ service account credentials](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) for scaled deployments and shared resource scenarios. 

To use Cloud Storage to transfer files between a computer and a VM, do the following: 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) if you don't have an existing bucket to use for file transfers. 
  2. [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to modify the access to the bucket: 
     * Accounts uploading file(s) to the bucket should have the **Storage Object Admin** granted. 
     * Accounts downloading file(s) should have the **Storage Object Viewer** role granted. 
  3. Log in to the source device and [upload the files](https://docs.cloud.google.com/storage/docs/uploading-objects) to the bucket. 
  4. Log in to the destination device and [download the files](https://docs.cloud.google.com/storage/docs/downloading-objects) from the bucket completing the file transfer. 
  5. Optional: [Delete files](https://docs.cloud.google.com/storage/docs/deleting-objects) that you no longer need to prevent any unwanted storage charges. 

If you need to transfer files in the other direction, you can reverse the process. Ensure that the account uploading the file has write access to the bucket. 

## Transfer files using SSH-in-browser

If you can establish an SSH connection to a VM by using [SSH-in-browser](https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser), you can use that connection to transfer files to and from the VM.

###  Upload to the VM 

  1. In the Google Cloud console, go to the **VM instances** page. [Go to VM instances](https://console.cloud.google.com/compute/instances)
  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. ![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)
  3. After the connection is established, click the upload icon upload. ![](https://docs.cloud.google.com/static/compute/images/upload-file-ssh-in-browser.png)The upload dialog opens.
  4. Choose the files to upload.
  5. Upload the files by clicking **Upload Files**. The file uploads to your `/home/USER` directory.



###  Download from the VM 

  1. In the Google Cloud console, go to the **VM instances** page. [Go to VM instances](https://console.cloud.google.com/compute/instances)
  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. ![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)
  3. After the connection is established, click the download icon download. ![](https://docs.cloud.google.com/static/compute/images/download-file-ssh-in-browser.png)The download dialog opens.
  4. In the **Path** field, enter the relative path of the file to download.
  5. Download the file by clicking **Download**. The file downloads to the default download folder of your workstation.



## Transfer files using the Google Cloud CLI

Google Cloud CLI provides a Secure Copy Protocol (SCP) file transfer utility over an established SSH connection.  To transfer files using SCP, do the following: 

  1. [Review your firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#listing-firewall-rules-vpc) and confirm that SSH connections in on port `22` are permitted; if not [create a SSH firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#common-use-cases-allow-ssh). 
  2. Ensure [gcloud CLI is installed](https://docs.cloud.google.com/sdk/docs/install) on the source device containing the files to be transferred. 
  3. Use the `[gcloud compute scp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp)` command to transfer the files to the destination machine. 

The following example copies a file from your workstation to the home directory of the VM:
    
    
    gcloud compute scp LOCAL_FILE_PATH VM_NAME:REMOTE_DIR
    

Replace the following:

  * `LOCAL_FILE_PATH`: the path to the file on your machine
  * `VM_NAME`: the name of your VM
  * `REMOTE_DIR`: a directory on the remote machine

You can also copy files and directories in reverse from the remote machine. The following example recursively copies a directory from the source to the destination:
    
    
    gcloud compute scp --recurse VM_NAME:REMOTE_DIR LOCAL_FILE_PATH
    

For more information, see the [ `gcloud compute scp` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp).

## Transfer files using SCP on Linux and macOS workstations

The `scp` command-line tool works similarly to the `gcloud compute scp` command but requires you to [manually manage your SSH keys](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys). To transfer files using SCP, you must have a firewall rule on the network that your VM uses that allows SSH connections on port `22`. You can verify that this firewall rules exists by looking for a firewall rule that allows `tcp:22` connections in the Google Cloud console. [Go to Firewall rules](https://console.cloud.google.com/networking/firewalls) If you don't have a firewall rule that allows SSH connections on port `22`, [create the firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules). The `scp` tool uses the same key files that you use to [connect to your instances using standard SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  1. If you have not yet applied a public key to your Google Cloud console project or VM instance, [create an SSH key pair](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys) and [add the public key to project or instance metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys).
  2. Find the external IP for the VM that you want to send files to.
     1. In the Google Cloud console, go to the **VM instances** page. [Go to VM instances](https://console.cloud.google.com/compute/instances)
     2. In the list of VMs, find the external IP address in the **External IP** column for the target VM.
  3. Use the `scp` tool to copy a file from your workstation to the home directory of the target VM. For this example, the private key is at `~/.ssh/my-ssh-key`.
         
         scp -i ~/.ssh/my-ssh-key LOCAL_FILE_PATH USERNAME@IPv4_ADDRESS:~
         

For an external IPv6 address, use the following syntax:
         
         scp -6 -i ~/.ssh/IDENTITY_FILE LOCAL_FILE_PATH USERNAME@[IPv6_ADDRESS]:~/
         

Replace the following:
     * `IDENTITY_FILE`: the file containing the identity (private key) for public key authentication
     * `LOCAL_FILE_PATH`: the name of the local file that you want to upload
     * `USERNAME`: your username
     * `IPv4_ADDRESS` or `IPv6_ADDRESS`: the external IP address for your VM

You can also copy files from a VM to your local workstation by reversing the source and destination variables. For this example, copy a file from your VM to a path on your workstation.
    
    
    scp -i ~/.sshIDENTITY_FILE USERNAME@IP_ADDRESS:REMOTE_FILE_PATH LOCAL_FILE_PATH
    

Replace the following:

  * `IDENTITY_FILE`: the file containing the identity (private key) for public key authentication
  * `USERNAME`: your username
  * `IP_ADDRESS`: the external IP address for your VM
  * `REMOTE_FILE_PATH`: the name of the remote file that you want to download
  * `LOCAL_FILE_PATH`: the location on your workstation where you want to download the file to



## Transfer files using WinSCP on Windows workstations

On Windows workstations, the WinSCP client lets you manage files on your instances through a graphical file browser interface. WinSCP uses the same key files that you use to [connect to VMs using PuTTY](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#putty-app).

  1. Do the following if you haven't configured key-based SSH authentication for your instance:
     1. [Create an SSH key pair using PuTTYgen](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys#windows-8-or-earlier). The private ssh key must use the `.ppk` format, which is the default for keys created by PuTTYgen.
     2. Add your public SSH key to your project's metadata or to your VM's metadata. For more information, see [Add SSH keys to project metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#add_ssh_keys_to_project_metadata) or [Add SSH keys to instance metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#add_ssh_keys_to_instance_metadata).
  2. Find the external IP for the VM that you want to send files to.
     1. In the Google Cloud console, go to the **VM instances** page. [Go to VM instances](https://console.cloud.google.com/compute/instances)
     2. In the list of VMs, find the external IP address in the **External IP** column for your VM.
  3. [Download and install WinSCP](https://winscp.net/eng/docs/guide_install). The default install settings work for most users.
  4. Start the WinSCP program. A login window opens where you can configure your connection settings.
  5. In WinSCP, configure your connection settings.
     1. Select `SCP` as the file transfer protocol in the **File protocol** field.
     2. In the **Host Name** field, specify the external IP address for the VM that you want to connect to.
     3. In the **User name** field, specify the Google username that you use to access your project. For this example, the user is `example-user`. ![Setting the file protocol to SCP, the hostname to 104.196.31.103, and the username to example-user.](https://docs.cloud.google.com/static/compute/images/connecting/winscp_configure_connection.png)
  6. Click the **Advanced** drop-down list to open the advanced settings, and navigate to **SSH** > **Authentication**.
  7. In the **Private key file** box, specify the path to your private key file of the [SSH key pair that you created for the VM](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). ![Setting the private key file to my-ssh-key.ppk in the Advanced Site Settings dialog.](https://docs.cloud.google.com/static/compute/images/connecting/winscp_advanced_settings.png)
  8. Click **Ok** to save the advanced settings.
  9. Click **Login** to connect to your VM. If the connection is successful, the window opens your local file system on the left and the VM's file system on the right. You can navigate to different directories in these file systems and drag files to transfer them to and from your VM.
  10. You likely don't have permission to manage most files outside of your home directory of the VM. Navigate to the home directory of the VM:
         
         /home/USERNAME
         

  11. Use the WinSCP interface to move files between your workstation and the VM.
  12. After you copy your files to the VM, [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) so that you can execute or move files with full `sudo` permissions.



## What's next

  * [Connect to your instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) to use the files that you uploaded.

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-20 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
