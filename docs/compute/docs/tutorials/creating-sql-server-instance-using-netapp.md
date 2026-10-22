---
url: https://docs.cloud.google.com/compute/docs/tutorials/creating-sql-server-instance-using-netapp/
title: Use Google Cloud NetApp Volumes file storage to configure a SQL Server failover cluster instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:55.722283+00:00
---

# Use Google Cloud NetApp Volumes file storage to configure a SQL Server failover cluster instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/creating-sql-server-instance-using-netapp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use Google Cloud NetApp Volumes file storage to configure a SQL Server failover cluster instance Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to configure a highly resilient Google Cloud environment for SQL Server. You install this environment on Server Message Block (SMB) fileshare storage by using Google Cloud NetApp Volumes.

Microsoft SQL Server [Always On availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver15) (AG) allow you to replicate databases across multiple SQL Server Enterprise instances. Traditional SQL Server Always On instances typically require each node to maintain a copy of the data, which can quickly become costly as the databases grow. For example, in a traditional SQL Server Always On deployment, if the databases are 10TB in size, each replica must have at least 10TB of storage provisioned. One of the benefits of having a Windows Server Failover Cluster (WSFC) deployed for SQL Server is that you only need to have one copy of the data, which is shared between the nodes of the cluster. Therefore, running SQL Server Always On in a failover cluster instance (FCI) on a WSFC can immediately realize cost savings by reducing the amount of storage required.

NetApp Volumes is a cloud storage solution for running high-performance SQL Server workloads in combination with Compute Engine instances. SQL Server database over SMB on NetApp Volumes provides a very high level of resiliency between the Google Cloud instances and the storage service. SMB transparent failover enables maintenance operations on the NetApp Volumes without interrupting connectivity to server applications storing and accessing data on SMB volumes. To support SMB transparent failover, NetApp Volumes supports the SMB continuous availability (CA) shares option for use with SQL Server workloads. This option provides performance improvements, scalability, and cost benefits for single instances, Always On failover cluster (AOFC) instances, and Always On availability group deployments.

**Note:** [Filestream](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-with-smb-fileshare-as-a-storage-option?view=sql-server-ver16&viewFallbackFrom=sql-server-ver16Note) (memory optimized tables) is currently not supported on an SMB file share.

This page is intended for NetApp Volumes and SQL Server database administrators who are responsible for deploying Microsoft SQL Server on Google Cloud. It assumes the following:

  * You are familiar with the various components of the solution
  * You have already deployed Active Directory on Google Cloud



## Objectives

This tutorial aims to achieve the following objectives: 

  * Create a NetApp volume for SQL Server
  * Deploy Always On failover cluster over SMB on NetApp Volumes



## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [NetApp Volumes](https://cloud.google.com/netapp-volumes#section-5)



Use the [pricing calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage. 

## Before you begin

For this tutorial, you need a Google Cloud project. You can create a new one, or select a project you already created:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. An Active Directory domain with at least one domain controller. You can create an Active Directory domain [by using Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain). Alternatively, you can deploy a [custom Active Directory environment on Compute Engine](https://docs.cloud.google.com/solutions/deploy-fault-tolerant-active-directory-environment) and [set up a private DNS forwarding zone](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones) that forwards DNS queries to your domain controllers.
  4. An Active Directory user that has permission to join computers to the domain and can log in by using RDP. If you're using Managed Microsoft AD, you can use the `setupadmin` user.
  5. A Google Cloud project and VPC with connectivity to your Active Directory domain controllers.
  6. Make sure that [NetApp Volumes API is enabled for your Google Cloud project](https://console.cloud.google.com/apis/library/netapp.googleapis.com).
  7. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




## Prepare your project and network

To prepare your Google Cloud project and Virtual Private Cloud (VPC) for the deployment of SQL Server Always On availability groups, do the following:

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Initialize the following variables:
         
         VPC_NAME=VPC_NAME
         SUBNET_NAME=SUBNET_NAME
         

Replace the following:

     * `VPC_NAME`: name of your VPC
     * `SUBNET_NAME`: name of your subnet
  3. Set your default [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  4. Set your default region:
         
         gcloud config set compute/region REGION
         

Replace `REGION` with the ID of the region you want to deploy in.

  5. Set your default zone:
         
         gcloud config set compute/zone ZONE
         

Replace `ZONE` with the ID of the zone you want to deploy in.




### Create SMB on NetApp Volumes for SQL Server

To create a NetApp Volumes, you must create an Active Directory policy, private services access, storage pool, and storage volume.

  1. Create a new **Private Service Access** for NetApp Volumes using the instructions provided in [Configure private services access](https://docs.cloud.google.com/netapp/volumes/docs/get-started/configure-access/networking#configure_private_services_access).

  2. To create a new **Active Directory policy** , do the following:

     1. In the Google Cloud console, go to the **NetApp Volumes** page.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

     2. In the Navigation pane, click **Active Directory policies** under the **Policies** section.

     3. Click **Create** button.

     4. Specify a name for the active directory policy.

     5. Under **Region** , select the available region closest to where the SQL Server instances will be hosted.

     6. In the **Active Directory connection details** section, provide the following information:

        1. Name of the domain
        2. Active Directory DNS server addresses
        3. Active Directory site name
        4. Name of the organizational unit
        5. NetBIOS name prefix
     7. In the **Active Directory credentials** section, provide the credentials for a user who is allowed to join computers to the specified domain.

     8. In the **SMB settings** section, provide the **Backup Operators** and **Security privilege users** , if applicable.

     9. Click **Create** to complete the process of creating a new Active Directory policy.

  3. To create a new storage pool, do the following:

     1. In the Navigation pane, click **Storage pools** under the **Storage** section.
     2. Click **Create** button.
     3. Enter a name for the storage pool.
     4. Under **Location** , select the available region closest to where the SQL Server instances will be hosted.
     5. Select a **Service Level** that would satisfy the expected storage performance.

**Warning:** SMB continuously available (CA) shares aren't supported on Flex File service level. Use Flex Unified (Preview for SMB), Standard, Premium, or Extreme service levels for Microsoft SQL Server. For more information about comparison of features across service levels, see [service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).
     6. Enter the **Capacity** for the storage pool. Storage pool capacity defines the total storage capacity that can be allocated for all the volumes within the pool.

     7. In the **Network** list, select the VPC that the SQL Server instances will be hosted in.

     8. In the **Active Directory policy** section, select **Assign an Active Directory policy to the storage pool** and select the Active Directory policy created in the previous step.

     9. Click **Create** button to complete the process of creating a new storage pool.

  4. To test the connection between the storage pool and the active directory, do the following:

     1. In the Google Cloud console, go to the **Active Directory policy** page.

[Go to Active Directory policies](https://console.cloud.google.com/netapp/active-directories)

     2. Click the Active Directory policy you assigned to the storage pool in the previous step.

     3. Locate **Associated storage pools** and click **Test Active Directory connection**.

**Note:** If the connection fails, see [Firewall rules for volumes access](https://docs.cloud.google.com/netapp/volumes/docs/before-you-begin/security-considerations#firewall_rules_for_volumes_access) to create any missing firewall rules.
  5. To create a new **storage volume** , do the following:

     1. In the Navigation pane, click **Volumes** under the **Storage** section.
     2. Click **Create** button.
     3. Specify a name for the storage volume.
     4. Under **Storage pool details** , click **Select storage pool** to select the storage pool created in the previous step.
     5. In the **Volume details** section, provide the following information: 
        1. Share name
        2. Volume capacity
     6. In the **Protocol(s) configuration** section, select **SMB** protocol and **Enable CA share support for SQL Server, FSLogix**.
     7. Click **Create** button to complete the process of creating a new storage volume.



### Create firewall rules

To allow clients to connect to SQL Server, allow communication between the Windows Server Failover Cluster (WSFC) nodes, and to enable the load balancer to [perform health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule), you need to create several firewall rules. To simplify the creation of these firewall rules, you can use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags):

  * The WSFC you use are annotated with the `wsfc-node` tag.
  * All servers, including the witness, are annotated with the `wsfc` tag.



To create firewall rules that use these network tags, use the following steps:

  1. Return to your existing Cloud Shell session.
  2. Create firewall rules for the WSFC nodes.
         
         SUBNET_CIDR=$(gcloud compute networks subnets describe $SUBNET_NAME --format=value\('ipCidrRange'\))
         
         gcloud compute firewall-rules create allow-all-between-wsfc-nodes \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp,udp,icmp \
           --enable-logging \
           --source-tags=wsfc \
           --target-tags=wsfc \
           --network=$VPC_NAME \
           --priority 10000
         
         gcloud compute firewall-rules create allow-sql-to-wsfc-nodes \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:1433 \
           --enable-logging \
           --source-ranges=$SUBNET_CIDR \
           --target-tags=wsfc-node \
           --network=$VPC_NAME \
           --priority 10000
         

  3. Create a firewall rule that allows health checks from the [IP ranges of the Google Cloud probers](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges):
         
         gcloud compute firewall-rules create allow-health-check-to-wsfc-nodes \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp \
           --source-ranges=130.211.0.0/22,35.191.0.0/16 \
           --target-tags=wsfc-node \
           --network=$VPC_NAME \
           --priority 10000
         


**Note:** Depending on how you've deployed Active Directory, you might need to create additional firewall rules to allow servers to join the domain. See [Accessing Managed Microsoft AD from within your VPC](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls#accessing_from_within_your_vpc) for further details.

### Create VM instances

You will now deploy three VM instances for the failover cluster.

`Node-1` will host the primary replica of the SQL Server database and `node-2` will host the secondary replica. The two VM instances must:

  * be located in the same region so that they can be accessed by an internal passthrough Network Load Balancer
  * have WSFC and SQL Server 2022 installed using [SQL Server premium image](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server)

**Note:** If you plan to bring your own licenses for SQL Server by using the [license mobility](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) program, select Windows Server base images for these nodes and install SQL Server using your own product keys.
  * have [Compute Engine WSFC support](https://github.com/GoogleCloudPlatform/guest-agent#windows-failover-cluster-support) enabled




To provide a tie-breaking vote and achieve a quorum for the failover scenario, you deploy a third VM instance `node-3` that serves as a [file share witness](https://docs.microsoft.com/en-us/windows-server/failover-clustering/manage-cluster-quorum#quorum-configuration-options).

  1. Return to your existing Cloud Shell session.
  2. Create a [script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the WSFC nodes. The script installs the necessary Windows feature and creates firewall rules for WSFC and SQL Server:
         
         cat << "EOF" > specialize-node.ps1
         
         $ErrorActionPreference = "stop"
         
         # Install required Windows features
         Install-WindowsFeature Failover-Clustering -IncludeManagementTools
         Install-WindowsFeature RSAT-AD-PowerShell
         
         # Open firewall for WSFC
         netsh advfirewall firewall add rule name="Allow SQL Server health check" dir=in action=allow protocol=TCP localport=59997
         
         # Open firewall for SQL Server
         netsh advfirewall firewall add rule name="Allow SQL Server" dir=in action=allow protocol=TCP localport=1433
         
         # Open firewall for SQL Server replication
         netsh advfirewall firewall add rule name="Allow SQL Server replication" dir=in action=allow protocol=TCP localport=5022
         
         EOF
         

  3. Create the VM instances. On the two VMs that serve as WSFC nodes, attach an additional data disk and enable the Windows Server Failover Clustering by setting the metadata key `enable-wsfc` to `true`:
         
         REGION=$(gcloud config get-value compute/region)
         PD_SIZE=200
         MACHINE_TYPE=n2-standard-8
         
         gcloud compute instances create node-1 \
           --zone $REGION-a \
           --machine-type $MACHINE_TYPE \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2022-win-2022 \
           --image-project windows-sql-cloud \
           --tags wsfc,wsfc-node \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --boot-disk-device-name "node-1" \
           --metadata enable-wsfc=true \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-node.ps1
         
         gcloud compute instances create node-2 \
           --zone $REGION-b \
           --machine-type $MACHINE_TYPE \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2022-win-2022 \
           --image-project windows-sql-cloud \
           --tags wsfc,wsfc-node \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --boot-disk-device-name "node-2" \
           --metadata enable-wsfc=true \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-node.ps1
         
         gcloud compute instances create "witness" \
           --zone $REGION-c \
           --machine-type n2-standard-2 \
           --subnet $SUBNET_NAME \
           --image-family=windows-2022 \
           --image-project=windows-cloud \
           --tags wsfc \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --metadata sysprep-specialize-script-ps1="add-windowsfeature FS-FileServer"
         

**Note:** Depending on your [performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance#optimize_disk_performance), consider using a machine type larger than `n2-standard-8` for the WSFC nodes.
  4. To join the 3 VM instances to Active Directory, do the following for each of the 3 VM instances:

     1. Monitor the initialization process of the VM by viewing its serial port output:
            
            gcloud compute instances tail-serial-port-output NAME
            

Replace `NAME` with the name of the VM instance.

Wait for a few minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

     2. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

     3. [Connect to the VM using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using the username and password created in the previous step.

     4. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

     5. Confirm the elevation prompt by clicking **Yes**.

     6. Join the VM instance to your Active Directory domain and restart:
            
            Add-Computer -Domain DOMAIN -Restart
            

Replace `DOMAIN` with the DNS name of your Active Directory domain.

Wait for the VM instance to restart.




### Assign storage permissions

To assign permissions to the cloud volume storage, complete the following steps:

  1. From the Google Cloud console, select Cloud Volumes and select the volume that was just created.

![Cloud Volume](https://docs.cloud.google.com/static/compute/docs/tutorials/images/cloud-volume-service-netapp-cloud-volume.png)

  2. Connect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.

  3. Open Windows Explorer and right-click **This PC**.

  4. Select **Map network drive**.

  5. Paste the copied SMB path in the folder.

![Cloud Volume](https://docs.cloud.google.com/static/compute/docs/tutorials/images/cloud-volume-service-netapp-map-drive.png)

  6. At sign-in, disable the Reconnect option.

  7. Click **Finish**.

  8. Right-click the mapped network drive and select **Properties**.

![Cloud Volume](https://docs.cloud.google.com/static/compute/docs/tutorials/images/cloud-volume-service-netapp-map-drive-properties.png)

  9. From the **Security** tab, click **Edit**.

  10. Remove Everyone and add the SQL Server installer and SQL Server service accounts with full control permissions.

![Cloud Volume](https://docs.cloud.google.com/static/compute/docs/tutorials/images/cloud-volume-service-netapp-map-drive-securities.png)

  11. Confirm the elevation prompt by clicking **Yes**.




### Reserve cluster IP addresses

Reserve two static IP addresses in your VPC, one for the WSFC cluster IP address and another for the internal load balancer.

  1. Reserve a static IP for the internal load balancer and capture the address in a new environment variable named `LOADBALANCER_ADDRESS`:
         
         gcloud compute addresses create wsfc \
           --region $(gcloud config get-value compute/zone | rev | cut -c 3- | rev) \
           --subnet $SUBNET_NAME
         
         LOADBALANCER_ADDRESS=$(gcloud compute addresses describe wsfc \
           --region $(gcloud config get-value compute/zone | rev | cut -c 3- | rev) \
           --format=value\(address\))
         
         echo "Load Balancer IP: $LOADBALANCER_ADDRESS"
         

Note the IP address, you'll need it later.

  2. Reserve another static IP address that you use as cluster IP:
         
         gcloud compute addresses create wsfc-cluster \
           --subnet $SUBNET_NAME \
           --region $(gcloud config get-value compute/zone | rev | cut -c 3- | rev)
         
         CLUSTER_ADDRESS=$(gcloud compute addresses describe wsfc-cluster \
           --region $(gcloud config get-value compute/zone | rev | cut -c 3- | rev) \
           --format=value\(address\))
         
         echo "Cluster IP: $CLUSTER_ADDRESS"
         

Note the IP address, you'll need it later.




Your project and VPC are now ready for the deployment of the WSFC and SQL Server.

### Create a witness file share

To prepare `witness` to serve as file share witness, create a file share and grant yourself and the two WSFC nodes access to the file share:

  1. Connect to `witness` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.
  2. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create the witness folder and share the folder:
         
         New-Item "C:\QWitness" –type directory
         
         icacls C:\QWitness\ /grant 'node-1$:(OI)(CI)(M)'
         icacls C:\QWitness\ /grant 'node-2$:(OI)(CI)(M)'
         
         New-SmbShare `
           -Name QWitness `
           -Path "C:\QWitness" `
           -Description "SQL File Share Witness" `
           -FullAccess  $env:username,node-1$,node-2$
         




## Deploying the failover cluster

You will now use the VM instances to deploy a WSFC and SQL Server.

### Deploy WSFC

You are now ready to create the failover cluster:

  1. Connect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.
  2. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a new cluster:
         
         New-Cluster `
           -Name windows-fci `
           -Node node-1,node-2 `
           -NoStorage `
           -StaticAddress CLUSTER_ADDRESS
         

Replace `CLUSTER_ADDRESS` with the cluster IP address that you created earlier.

  5. Return to the PowerShell session on `witness` and grant the virtual computer object of the cluster permission to access the file share:
         
         icacls C:\QWitness\ /grant 'windows-fci$:(OI)(CI)(M)'
         Grant-SmbShareAccess `
           -Name QWitness `
           -AccountName 'windows-fci$' `
           -AccessRight Full `
           -Force
         

  6. Return to the PowerShell session on `node-1` and configure the cluster to use the file share on `witness` as a cluster quorum:
         
         Set-ClusterQuorum -FileShareWitness \\witness\QWitness
         

  7. Verify that the cluster was created successfully:
         
         Test-Cluster
         

You might see some warnings that can be safely ignored:
         
         WARNING: System Configuration - Validate All Drivers Signed: The test
         reported some warnings..
         WARNING: Network - Validate Network Communication: The test reported some
         warnings..
         WARNING:
         Test Result:
         HadUnselectedTests, ClusterConditionallyApproved
         Testing has completed for the tests you selected. You should review the
         warnings in the Report.  A cluster solution is supported by Microsoft only
         if you run all cluster validation tests, and all tests succeed (with or
         without warnings).
         

You can also launch the Failover Cluster Manager MMC snap-in to review the cluster's health by running `cluadmin.msc`.

  8. If you're using Managed AD, add the computer account used by WSFC to the **Cloud Service Domain Join Accounts** group so that it can join VM instances to the domain:
         
         Add-ADGroupMember `
           -Identity "Cloud Service Domain Join Accounts" `
           -Members windows-fci$
         




### Remove the default SQL Server installation

You will now remove the default SQL Server installation from the two nodes and replace it with a new FCI configuration.

For each of the two WSFC nodes, `node-1` and `node-2`, perform the following steps:

  1. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  2. Confirm the elevation prompt by clicking **Yes**.
  3. Remove the default SQL Server instance:
         
         C:\sql_server_install\Setup.exe /Action=Uninstall /FEATURES=SQL,AS,IS,RS /INSTANCENAME=MSSQLSERVER /Q
         

  4. Remove Microsoft OLE Driver:
         
         Get-Package -Name "Microsoft OLE*" | Uninstall-Package -Force
         

  5. Remove Microsoft ODBC Driver:
         
         Get-Package -Name "Microsoft ODBC*" | Uninstall-Package -Force
         

  6. Restart the computer:
         
         Restart-Computer
         

  7. Wait for the VM instance to restart.




### Install SQL Server FCI

Before you install the new FCI configuration, verify that the `node-1` is the active node in the cluster:

  1. Reconnect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using your domain user.
  2. Right-click **Start** button (or press **Win+X**) and select **Run**
  3. Enter `cluadmin.msc` and select **OK**.
  4. In the left window pane, navigate to **Failover Cluster Manager > windows-fci**, and do the following:

     1. Verify that the **current host server** is set to `node-1`.

     2. If the **current host server** is set to `node-2`, right-click **windows-fci** in the left window pane and select **More actions > Move core cluster resources > Select node… > node-1** and click **OK**.




You will create a new SQL Server failover cluster installation on `node-1`:

  1. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  2. Confirm the elevation prompt by clicking **Yes**.

  3. Start the SQL Server setup:
         
         & c:\sql_server_install\setup.exe
         

  4. In the menu on the left, select **Installation**.

  5. Select **New SQL Server failover cluster installation**.

  6. On the **Edition** page, enter the product key, select the software license type, and click **Next**.

  7. On the **License Terms** page, review the terms and, if you accept, click **Next**.

  8. On the **Microsoft Update** page, click **Next** to start the installation.

  9. On the **Install Failover Cluster Rules** page, you see a Warning **MSCS cluster verification warnings** and **Windows firewall**. You can ignore these warnings and click **Next**.

  10. On the **Feature Selection** page, select **Database Engine Services** and click **Next**.

  11. On the **Instance Configuration** page, enter `sql` as network name and click **Next**.

  12. On the **Cluster Resource Group** page, you can ignore the qualification warnings and click **Next**.

  13. On the **Cluster Disk Selection** page, click **Next**.

  14. On the **Cluster Network Configuration** page, configure the following settings, then click **Next** :

     * **DHCP** : clear
     * **IP address:** enter the IP address of the internal load balancer
  15. On the **Server configuration** page, configure the following settings for both **SQL Server Agent** and **SQL Server Database Engine** :

     * **Account name** : `DOMAIN\sql_server` where `DOMAIN` is the NetBIOS name of your Active Directory domain
     * **Password** : enter `sql_server` user's password
  16. Select the **Collation** tab and select the collation that you want to use. Then click **Next**.

  17. On the **Database Engine Configuration** page, select **Add current user** to designate the current user as SQL Server administrator. In the **Data Directories** tab, enter the SMB path in the **Data root directory** field and select **Next**. A message window will appear informing you to verify that the SQL Server service account has full control share permission. Select **Yes** to proceed.

![Cloud Volume](https://docs.cloud.google.com/static/compute/docs/tutorials/images/cloud-volume-service-netapp-failover-cluster-setup-database-engine-config.png)

  18. On the **Ready to Install** page, review the settings, then select **Install**.

  19. After the installation completes, select **Close**.




Now add `node-2` to the SQL Server failover cluster:

  1. Connect to `node-2` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using your domain user.
  2. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Start the SQL Server setup:
         
         & c:\sql_server_install\setup.exe
         

  5. In the menu on the left, select **Installation**.

  6. Select **Add node to a SQL Server failover cluster**.

  7. Follow the instructions of the installation wizard and accept the default settings until you reach the page **Service Accounts**.

  8. On the **Service Accounts** page, enter the password that you created earlier for both **SQL Server Agent** and **SQL Server Database Engine**. Then select **Next**.

  9. On the **Ready to Install** page, review the settings, then select **Install**.

  10. After the installation completes, select **Close**.




### Configure health checks

As a final step, configure the cluster to expose a health check endpoint that can be used by an internal load balancer:

  1. Return to the PowerShell session on `node-2`
  2. Initialize a variable with the IP address of the load balancer.
         
         $LoadBalancerIP = 'IP_ADDRESS'
         

Replace `IP_ADDRESS` with the IP address of the `wsfc` address that you reserved earlier.

  3. Configure the Failover Cluster to respond to the health check service:
         
         $SqlGroup = Get-ClusterGroup |
           Where-Object {$_.Name.StartsWith("SQL Server")}
         $SqlIpAddress = Get-ClusterResource |
           Where-Object {$_.Name.StartsWith("SQL IP Address")}
         
         $SqlIpAddress | Set-ClusterParameter -Multiple @{
          'Address'=$LoadBalancerIP;
          'ProbePort'= 59997;
          'SubnetMask'='255.255.255.255';
          'Network'= (Get-ClusterNetwork).Name;
          'EnableDhcp'=0; }
         

  4. Restart the cluster resource:
         
         $SqlIpAddress | Stop-ClusterResource
         $SqlIpAddress | Start-ClusterResource
         

  5. Restart the cluster group:
         
         $SqlGroup | Stop-ClusterGroup
         $SqlGroup | Start-ClusterGroup
         




## Create an internal load balancer

To provide a single endpoint for SQL Server clients, you will now deploy an [internal load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal#deploying_internal_load_balancing). The load balancer uses a health check which ensures that traffic is directed to the active node of the WSFC.

  1. Return to your existing Cloud Shell session.
  2. Create an [unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances), and add the two nodes to the group:
         
         REGION=$(gcloud config get-value compute/region)
         
         gcloud compute instance-groups unmanaged create wsfc-group-a \
           --zone $REGION-a
         gcloud compute instance-groups unmanaged add-instances wsfc-group-a \
           --zone $REGION-a --instances node-1
         
         gcloud compute instance-groups unmanaged create wsfc-group-b \
           --zone $REGION-b
         gcloud compute instance-groups unmanaged add-instances wsfc-group-b \
         --zone $REGION-b --instances node-2
         

  3. Create a health check that the load balancer can use to determine which is the active node.
         
         gcloud compute health-checks create tcp wsfc-healthcheck \
           --check-interval="2s" \
           --healthy-threshold=1 \
           --unhealthy-threshold=2 \
           --port=59997 \
           --timeout="1s"
         

The health check probes port `59997`, which is the port you previously configured as `ProbePort` for the WSFC cluster IP address.

  4. Create a backend service and add the instance group:
         
         gcloud compute backend-services create wsfc-backend \
           --load-balancing-scheme internal \
           --region $REGION \
           --health-checks wsfc-healthcheck \
           --protocol tcp
         
         gcloud compute backend-services add-backend wsfc-backend \
           --instance-group wsfc-group-a \
           --instance-group-zone $REGION-a \
           --region $REGION
         gcloud compute backend-services add-backend wsfc-backend \
           --instance-group wsfc-group-b \
           --instance-group-zone $REGION-b \
           --region $REGION
         

  5. Create the internal load balancer:
         
         gcloud compute forwarding-rules create wsfc-sql \
           --load-balancing-scheme internal \
           --address $LOADBALANCER_ADDRESS \
           --ports 1433 \
           --network $VPC_NAME \
           --subnet $SUBNET_NAME \
           --region $REGION \
           --backend-service wsfc-backend
         




## Testing the failover cluster

You've completed the installation of the failover cluster, but you still have to test whether the cluster works correctly.

### Prepare a client

Create a new VM instance which you can use to connect to the failover cluster:

  1. Return to your existing Cloud Shell session.
  2. Create a new VM instance:
         
         gcloud compute instances create sqlclient \
           --machine-type n2-standard-2 \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2022-win-2022 \
           --image-project windows-sql-cloud \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd
         

  3. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output sqlclient
         

Wait for a few minutes until you see the output Instance setup finished, then press Ctrl+C. At this point, the VM instance is ready to be used.

  4. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

  5. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using the username and password created in the previous step.

  6. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

  7. Confirm the elevation prompt by clicking **Yes**.

  8. Join the VM instance to your Active Directory domain:
         
         Add-Computer -Domain DOMAIN
         

Replace `DOMAIN` with the DNS name of your Active Directory domain.

  9. Restart the VM instance:
         
         Restart-Computer
         

Wait for the VM instance to restart.




### Run the test

Use the `sqlclient` VM to test that you can connect to the failover cluster and to verify that the failover works correctly:

  1. Connect to `sqlclient` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using your domain user.
  2. Right-click **Start** button (or press **Win+X**) and click **Windows PowerShell**.
  3. Connect to SQL Server cluster by using its network name `sql` and query the `dm_os_cluster_nodes` table:
         
         & "$env:ProgramFiles\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE" `
            -S sql -E -Q "SELECT * FROM sys.dm_os_cluster_nodes"
         

The output should look like this:
         
         NodeName                       status      status_description is_current_owner
         ------------------------------ ----------- ------------------ ----------------
         NODE-1                                   0 up                                1
         NODE-2                                   0 up                                0
         
         (2 rows affected)
         

Notice that `node-1` is the current owner of the SQL Server failover cluster resource.

  4. Return to Cloud Shell and bring down the node-1 VM to test the failover scenario:
         
         gcloud compute instances stop node-1
         

  5. Repeat the query:
         
         & "$env:ProgramFiles\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE" `
            -S sql -E -Q "SELECT * FROM sys.dm_os_cluster_nodes"
         

The output should now look like this:
         
         NodeName                       status      status_description is_current_owner
         ------------------------------ ----------- ------------------ ----------------
         NODE-1                                   1 down                              0
         NODE-2                                   0 up                                1
         
         (2 rows affected)
         

Notice that despite the loss of `node-1`, the query succeeds, and shows that `node-2` is now the current owner of the failover cluster.




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
