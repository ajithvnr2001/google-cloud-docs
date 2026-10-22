---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/prepare-vm/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:13.473278+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/prepare-vm/




Stay organized with collections  Save and categorize content based on your preferences. 

You use a [SQL Server premium image](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server) which has SQL Server 2022 preinstalled.

**Note:** If you plan to bring your own licenses for SQL Server by using the [license Mobility](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) program, select Windows Server base images for these nodes and install SQL Server using your own product keys.

To provide a tie-breaking vote and achieve a quorum for the failover scenario, you deploy a third VM that serves as a [file share witness](https://docs.microsoft.com/en-us/windows-server/failover-clustering/manage-cluster-quorum#quorum-configuration-options).

  1. Return to your existing Cloud Shell session.
  2. Create a [specialize script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the cluster nodes. The script installs the necessary Windows feature and creates firewall rules for the failover cluster and SQL Server.
         
         cat << "EOF" > specialize-node.ps1
         
         $ErrorActionPreference = "stop"
         
         # Install required Windows features
         Install-WindowsFeature Failover-Clustering -IncludeManagementTools
         Install-WindowsFeature RSAT-AD-PowerShell
         
         # Open firewall for availability group listener
         netsh advfirewall firewall add rule name="Allow SQL Server Listener health check" dir=in action=allow protocol=TCP localport=59997
         
         # Open firewall for the Failover Cluster
         netsh advfirewall firewall add rule name="Allow SQL Server health check" dir=in action=allow protocol=TCP localport=59998
         
         # Open firewall for SQL Server
         netsh advfirewall firewall add rule name="Allow SQL Server" dir=in action=allow protocol=TCP localport=1433
         
         # Open firewall for SQL Server replication
         netsh advfirewall firewall add rule name="Allow SQL Server replication" dir=in action=allow protocol=TCP localport=5022
         
         # Format data disk
         Get-Disk |
          Where partitionstyle -eq 'RAW' |
          Initialize-Disk -PartitionStyle MBR -PassThru |
          New-Partition -AssignDriveLetter -UseMaximumSize |
          Format-Volume -FileSystem NTFS -NewFileSystemLabel 'Data' -Confirm:$false
         
         # Create data and log folders for SQL Server
         md d:\Data
         md d:\Logs
         EOF
         

  3. Create the VM instances. On the two VMs that serve as cluster nodes, attach an additional data disk and enable the Windows Server Failover Clustering by setting the metadata key `enable-wsfc` to `true`.
         
         REGION=$(gcloud config get-value compute/region)
         ZONE1=$(gcloud config get-value compute/zone)
         ZONE2=$(gcloud config get-value compute/zone)
         ZONE3=$(gcloud config get-value compute/zone)
         PD_SIZE=200
         MACHINE_TYPE=n2-standard-8
         
         gcloud compute instances create node-1 \
           --zone $ZONE1 \
           --machine-type $MACHINE_TYPE \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2022-win-2022 \
           --image-project windows-sql-cloud \
           --tags wsfc,wsfc-node \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --boot-disk-device-name "node-1" \
           --create-disk=name=node-1-datadisk,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --metadata enable-wsfc=true \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-node.ps1
         
         gcloud compute instances create node-2 \
           --zone $ZONE2 \
           --machine-type $MACHINE_TYPE \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2022-win-2022 \
           --image-project windows-sql-cloud \
           --tags wsfc,wsfc-node \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --boot-disk-device-name "node-2" \
           --create-disk=name=node-2-datadisk,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --metadata enable-wsfc=true \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-node.ps1
         
         gcloud compute instances create "witness" \
           --zone $ZONE3 \
           --machine-type n2-standard-2 \
           --subnet $SUBNET_NAME \
           --image-family=windows-2022 \
           --image-project=windows-cloud \
           --tags wsfc \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --metadata sysprep-specialize-script-ps1="add-windowsfeature FS-FileServer"
         

**Note:** Depending on your [performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance#optimize_disk_performance), consider using a machine type larger than `n2-standard-8` for the cluster nodes.**Note:** For the purpose of this tutorial, and to fit within the default regional SSD Persistent Disk quota, the size of the disks attached to each VM is smaller than it would be in a production environment. For better performance and to accommodate a larger database, you would increase the size of each disk.
  4. To join the 3 VM instances to Active Directory, do the following for each of the 3 VM instances.

     1. Monitor the initialization process of the VM by viewing its serial port output.
            
            gcloud compute instances tail-serial-port-output NAME
            

Replace `NAME` with the name of the VM instance.

Wait about 3 minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

     2. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance.

     3. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using the username and password created in the previous step.

     4. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

**Note:** In this guide, we used Powershell 5.1.
     1. Confirm the elevation prompt by clicking **Yes**.
     2. Join the computer to your Active Directory domain and restart.
            
            Add-Computer -Domain DOMAIN -Restart
            

Replace `DOMAIN` with the DNS name of your Active Directory domain.

     3. Enter the credentials of an account that has permissions to join a VM to the domain. Wait for approximately 1 minute for the restart to complete.




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
