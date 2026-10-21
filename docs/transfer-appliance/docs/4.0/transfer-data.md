---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data/
title: Transfer data \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:18.927111+00:00
---

# Transfer data  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Transfer data Stay organized with collections  Save and categorize content based on your preferences. 

Transfer Appliance supports the following methods to copy data to the appliance:

  * SCP or SFTP for Microsoft Windows, Linux, and macOS.
  * NFS share for Linux and macOS.
  * SMB share for Microsoft Windows and Linux.
  * Mount on the Appliance for NFS and CIFS.

**Note:** Each Transfer Appliance can only be configured to support one file sharing protocol at a time. You cannot use multiple file sharing protocols concurrently or switch between them after configuration. To change the configured protocol, the appliance must be reset, which will erase all data previously transferred to it. If your transfer requires multiple file sharing protocols, such as NFS and SMB, order separate appliances.

After you copy data to the Transfer Appliance, [verify that the data transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/access-data) to the Cloud Storage bucket is complete before you delete your source data.

## File size and naming requirements

Files that are uploaded to the appliance must comply with Cloud Storage file size limits and naming guidelines:

  * File size limits are documented on the Cloud Storage [Quotas & limits](https://docs.cloud.google.com/storage/quotas#objects) page.
  * File name guidelines are documented on the [Object naming guidelines](https://docs.cloud.google.com/storage/docs/naming-objects) page.



Transfer Appliance does not validate file size or names. If the appliance contains files that don't comply with these rules when the appliance is shipped back to Google, we may be unable to transfer those files.

## Use SCP or SFTP to copy data

To copy data to the appliance using SCP or SFTP, follow these steps:

### Microsoft Windows

  1. Download an SCP or SFTP client that supports UTF-8 filenames, such as [WinSCP](https://winscp.net/eng/index.php).

  2. Using the SCP tool, connect to the appliance using the following settings:

     * **File protocol** : SFTP
     * **Host name** : The IP address for the appliance.
     * **Port number** : 22
     * **Username** : The appliance username provided by the Transfer Appliance Team.
     * **Password** : The appliance password provided by the Transfer Appliance Team.

The destination directory on the Transfer Appliance must be `/mnt/ta_data`.




### Linux

  1. Run the following command:
         
         scp PATH_TO_FILES USERNAME@IP_ADDRESS:/mnt/ta_data
         

Replace the following:

     * `PATH_TO_FILES`: The path to the files you are copying.
     * `USERNAME`: The appliance username provided by the Transfer Appliance Team.
     * `IP_ADDRESS`: The IP address for the appliance.
  2. When prompted, enter the appliance password provided by the Transfer Appliance Team.




### Apple macOS

  1. Run the following command:
         
         scp PATH_TO_FILES USERNAME@IP_ADDRESS:/mnt/ta_data
         

Replace the following:

     * `PATH_TO_FILES`: The path to the files you are copying.
     * `USERNAME`: The appliance username provided by the Transfer Appliance Team.
     * `IP_ADDRESS`: The IP address for the appliance.
  2. When prompted, enter the appliance password provided by the Transfer Appliance Team.




## Use NFS share to copy data

To copy data to the appliance using NFS share, follow these steps:

  1. To mount Transfer Appliance, run the following commands on your data source:

### Linux

     1. sudo mkdir /mnt/data
            

     2. sudo mount -o vers=4 IP_ADDRESS:/mnt/ta_data /mnt/data
            

Replace `IP_ADDRESS` with the IP address for the appliance.

### Apple macOS

     1. cd ~
            

     2. mkdir ta_data
            

     3. sudo mount -t nfs -o vers=4,resvport IP_ADDRESS:/mnt/ta_data ~/ta_data
            

Replace `IP_ADDRESS` with the IP address for the appliance.

  2. To copy data to the appliance, use a copy utility of your choice.

Copying data is a long-running operation. On Apple macOS or Linux, we recommend using `tmux` or `screen` to ensure the copy process survives logout or network disconnects.




## Save your SSH key

Save your SSH key for quicker logins to your Transfer Appliance. Saving your SSH key can also improve transfer speeds.

  1. On your workstation, generate a key pair using the following command:
         
         posix-terminal
         ssh-keygen -t rsa
         

  2. Create a `/tmp/ssh_key` file on the appliance.

  3. Copy the contents of the public key file from your workstation into `/tmp/ssh_key` on the appliance. The public key file is at the following location on your workstation:

     * **Linux** : `~/.ssh/id_rsa.pub`
     * **Windows** : `C:Users/`USERNAME`/.ssh`

To authorize multiple keys, add each key on a new line in `/tmp/ssh_key`.

  4. Run the following command on the appliance. Any existing keys are overwritten.
         
         ta copy_ssh_keys
         

  5. Log in to the appliance.

     * If the private key is in the default location on your workstation, use the following command to log into the appliance:
           
           ssh ta_customer@IP_ADDRESS
           

     * If the private key isn't in the default location, use the following command to log into the appliance:
           
           ssh -i PRIVATE_KEY_PATH ta_customer@IP_ADDRESS
           




## Use SMB to transfer data

To enable SMB file share, follow the steps below:

  1. Configure the appliance to use SMB using the following file share protocol flag:
         
         ta config --data_port=PORT --ip=IP_ADDRESS --fileshare=smb
         

The `ta_data` directory is shared and the following user is created:

     * Username: `ta_customer`
     * Password: `ta_customer`
  2. Based on your host type, connect to the SMB file share:

### Microsoft Windows

### File manager

     1. Open the file manager and edit the file path to `\\IP_ADDRESS\ta_data`.

     2. Enter your username and password when prompted.

### Command line

     1. Enter the following at the Windows command prompt: `net use X: \\IP_ADDRESS\ta_data`

     2. Enter your username and password when prompted.

### Linux

### File manager

     1. Open the default file manager and click **Connect to server**.

     2. Enter `smb://IP_ADDRESS/ta_data`.

     3. Enter your username and password when prompted.

### Command line

     1. Install SMB client: `sudo apt-get install smbclient`.

     2. Connect to the SMB file share: `smbclient //IP_ADDRESS/ta_data -U USERNAME`

An `smb:\>` prompt appears.




## Use your own fileshares on the appliance

The appliance utilizes a wrapped Linux mount command to mount shares on the appliance:

  1. Run the following commands:

### NFS

     1. Update the /etc/exports file on your device hosting the NFS server granting IP_ADDRESS access to the server. 

     2. Run the following commands on the appliance:
            
            mkdir /mnt/ta_data_base/ta_mounts/MOUNT_POINT
            
            
            ta mount --types=nfs --source=NFS_SERVER_IP:/NFS_DIRECTORY
            --target=/mnt/ta_data_base/ta_mounts/MOUNT_POINT
            --options=OPTIONS
            

Replace the following:

        * `IP_ADDRESS`: The IP address of the appliance.
        * `MOUNT_POINT`: The name of the mount point for this share.
        * `NFS_SERVER_IP`: The IP address of your device hosting the NFS server
        * `NFS_DIRECTORY`: The path to your NFS share.
        * `OPTIONS`: The comma separated list of options. These options are those allowed by the Linux's mount command.

### CIFS

     1. Run the following commands on the appliance:
            
            mkdir /mnt/ta_data_base/ta_mounts/MOUNT_POINT
            
            
            ta mount --types=cifs --source=//CIFS_SERVER_IP/CIFS_NAME
            --target=/mnt/ta_data_base/ta_mounts/MOUNT_POINT
            --options=OPTIONS
            

Replace the following:

        * `MOUNT_POINT`: The name of the mount point for this share.
        * `CIFS_SERVER_IP`: The IP address of your device hosting the CIFS server.
        * `CIFS_NAME`: The CIFS share name.
        * `OPTIONS`: The comma separated list of options, including the password and username of the CIFS share. These options are those allowed by the Linux's mount command.

Unless otherwise specified in the mount options, the mount point will be re-mounted upon reboot until you remove it with the 'ta unmount' command.

  2. To unmount any mounts on the appliance run the following:
         
         ta unmount --target=/mnt/ta_data_base/ta_mounts/MOUNT_POINT

  3. To copy data to the appliance, use a copy utility of your choice.

### RClone

     1. To run a copy command with RClone on the appliance run the following:
            
            rclone copy /mnt/ta_data_base/ta_mounts/MOUNT_POINT /mnt/ta_data

Replace the following:

        * `MOUNT_POINT`: The directory containing the data to be transferred.

### Archive Pull

     1. To archive your data into tar files during transfer, run the following:
            
            ta pull --target=/mnt/ta_data_base/ta_mounts/MOUNT_POINT --size=ARCHIVE_SIZE_BYTES
            --destination=/mnt/ta_data --count=THREAD_COUNT

Replace the following:

        * `MOUNT_POINT`: The directory containing the data to be transferred.
        * `ARCHIVE_SIZE_BYTES`: The target size of the tar balls to be generated at destination. Defaulted to 1GB, expected to be between 5MB and 20GB inclusive.
        * `THREAD_COUNT`: The number of threads running simultaneously creating archives. Defaulted to 20, expected to be between 1 and 10000 inclusive.

Archive pull runs in the background do you can safely exit out of the terminal. Pull begins with a phase of listing the data before transferring can begin. 

     2. An ID is returned when you begin a pull, this value can be used to interact with the pull:

To check the status of a pull, run the following: 
            
            ta pull --id=ID --status

To pause a pull, run the following: 
            
            ta pull --id=ID --pause

To resume a paused or interrupted pull, run the following: 
            
            ta pull --id=ID --resume

Replace the following:

        * `ID`: The pull ID.
     3. Once the pull completes the tar balls can be found under `/mnt/ta_data/TA_ARCHIVE_ID/` directory. A manifest file will be generated and saved at `/mnt/ta_data/manifest_ID.tsv`. This file will contain information of the files transferred, detailing what tar ball file holds what files. An error manifest file will similarly be saved at `/mnt/ta_data/manifest_ID_ERROR.tsv` detailing any errors that were encountered during the pull. 

It is recommended to run one pull command at a time.

**Note:** Pull is not designed to handle datasets with directories containing more than 50,000 subdirectories. To avoid extended wait times, consider using other copying methods.




## Data Transfer Benchmarks

These data transfer speeds represent the performance of Transfer Appliance when using standard copy tools. To isolate write performance and eliminate potential read bottlenecks from the data source, data was generated directly on the appliance. The appliance (TA300 V2) was connected to the data source with a 10Gb port, and speeds were measured across NFS and SSH copy methods for the following file sizes:

  * 100 GB files
  * 1 GB files
  * 10 MB files

File Size | CP (NFS) | Rsync (NFS) | SCP (SSH) | Rsync (SSH) | Estimated Time for 40 TB Transfer | Estimated Time for 300 TB Transfer  
---|---|---|---|---|---|---  
100 GB | 740 MBps | 735 MBps | 675 MBps | 640 MBps | 16 hours | 5 days  
1 GB | 648 MBps | 611 MBps | 600 MBps | 600 MBps | 18 hours | 5 days 15 hours  
10 MB | 512 MBps | 422 MBps | 14 MBps | 12 MBps | 23 hours | 7 days  
**Note:** Estimated transfer times are calculated based on peak NFS transfer speeds. For SSH and SCP transfers with smaller files (such as 10 MB), transfer times will be longer due to SSH encryption and session overhead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
