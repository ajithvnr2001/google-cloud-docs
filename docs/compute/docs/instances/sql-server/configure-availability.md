---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability/
title: Configure SQL Server Always On availability groups with synchronous commit using an internal load balancer \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:47.318202+00:00
---

# Configure SQL Server Always On availability groups with synchronous commit using an internal load balancer  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure SQL Server Always On availability groups with synchronous commit using an internal load balancer Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft SQL Server [Always On availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server) let you replicate databases across multiple SQL Server Enterprise instances.

Similar to [SQL Server Failover Cluster Instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance), Always On availability groups use Windows Server Failover Clustering (WSFC) to implement high availability. However, the two features differ in the following ways:

| Always On availability groups | Failover cluster instances  
---|---|---  
Scope of fail-over | Group of databases | Instance  
Storage | Not shared | Shared  
  
For a more detailed comparison, see [Comparison of failover cluster instances and availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/failover-clustering-and-always-on-availability-groups-sql-server#comparison-of-failover-cluster-instances-and-availability-groups).

Always On availability groups support [multiple availability modes](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/availability-modes-always-on-availability-groups#SupportedAvModes). This tutorial shows how you can deploy Always On availability groups in _synchronous commit mode_ to implement high availability for one or more databases.

In the setup, you will create three VM instances. Two VM instances, `node-1` and `node-2` serve as cluster nodes and run SQL Server. A third VM instance, `witness`, is used to achieve a [quorum](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/wsfc-quorum-modes-and-voting-configuration-sql-server) in a failover scenario. The three VM instances are distributed over three zones and share a common subnet.

Using a SQL Server Always On availability group, an example database, `bookshelf`, is synchronously replicated across the two SQL Server instances.

In an on-premises Windows cluster environment, [Address Resolution Protocol (ARP) announcements](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#ARP_announcements) trigger [IP address failover](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/mac-address-changes-for-virtual-server). Google Cloud, however, disregards ARP announcements. Consequently, you must implement one of the following two options: using an internal load balancer and a distributed network name (DNN).

The article assumes that you have already deployed Active Directory on Google Cloud and that you have basic knowledge of SQL Server, Active Directory, and Compute Engine. For more information about Active Directory on Google Cloud, see section Before you begin.

Using a SQL Server Always On availability group, an example database, `bookshelf`, is synchronously replicated across the two SQL Server instances. An internal load balancer ensures that traffic is directed to the active node.

For more information about Windows Server Failover Clustering with an internal load balancer, see [failover clustering](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering#understanding_the_network_routing).

![Architecture](https://docs.cloud.google.com/static/compute/images/sqlserver-ag-architecture.svg)

This diagram includes the following:

  * Two VM instances in the same region and different zones for the failover cluster called `node-1` and `node-2`. One hosts the primary replica of the SQL Server database while the other node hosts the secondary replica.
  * A third VM called `witness` serves as a file share witness to provide a tie-breaking vote and achieve a quorum for failover.
  * An internal load balancer in front of the cluster provides a single endpoint for SQL Server clients and uses a health check to ensure that traffic is directed to the active node.



## Objectives

This tutorial aims to achieve the following objectives:

  * Deploy a WSFC comprising two SQL Server VM instances, and a third VM instance that acts as a file share witness
  * Create an availability group with synchronous commit
  * Configure a load balancer
  * Verify that the setup is working by simulating a failover



## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



Use the [pricing calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

## Before you begin

To complete the tasks in this tutorial, ensure the following: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. You have an Active Directory domain with at least one domain controller. You can create an [Active Directory domain using Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain). Alternatively, you can deploy a [custom Active Directory environment on Compute Engine](https://docs.cloud.google.com/solutions/deploy-fault-tolerant-active-directory-environment) and set up a [private DNS forwarding zone](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones) that forwards DNS queries to your domain controllers. 
  7. You have an Active Directory user that has permission to join computers to the domain and can sign in by using RDP. If you're using Managed Microsoft AD, you can use the `setupadmin` user. For more information about Active Directory user account provisioning, see [Active Directory user account provisioning](https://cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts)
  8. A Google Cloud project and a Virtual Private Cloud (VPC) with connectivity to your Active Directory domain controllers. 
  9. A subnet to use for the Windows Server Failover Cluster VM instances. 

When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more information, see Cleaning up. 

## Prepare your project and network

To deploy your SQL Server Always On availability groups, you must prepare your Google Cloud project and VPC for the deployment. The following sections discuss how you can do this in detail.

### Configure your project and region

To prepare your Google Cloud project for the deployment of SQL Server Always On availability groups, do the following:

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Initialize the following variables.
         
         VPC_NAME=VPC_NAME
         SUBNET_NAME=SUBNET_NAME
         

Replace the following:

     * `VPC_NAME`: name of your VPC
     * `SUBNET_NAME`: name of your subnet
  3. Set your default [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  4. Set your default region.
         
         gcloud config set compute/region REGION
         

Replace `REGION` with the ID of the [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) you want to deploy in.




### Create firewall rules

To allow clients to connect to the SQL Server and the communication between the cluster nodes you need to create several firewall rules. You can use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) to simplify the creation of these firewall rules, as follows:

  * The two cluster nodes are annotated with the `wsfc-node` tag.
  * All servers (including the `witness`) are annotated with the `wsfc` tag.



To create firewall rules that use these network tags, use the following steps:

  1. Return to your existing Cloud Shell session.
  2. Create firewall rules to allow traffic between cluster nodes.
         
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
         


**Note:** Depending on how you've deployed the Active Directory, you might need to create additional firewall rules to allow servers to join the domain. For more information, see [Accessing Managed Microsoft AD from within your VPC](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls#accessing_from_within_your_vpc).

### Create VM instances

Create and deploy two VM instances for the failover cluster. At any point in time, one of these VMs hosts the primary replica of the SQL Server database while the other node hosts the secondary replica. The two VM instances must:

  * be located in the same region so that they can be accessed by an internal passthrough Network Load Balancer.
  * have Windows Server Failover Cluster and SQL Server installed.
  * have [Compute Engine WSFC support](https://github.com/GoogleCloudPlatform/guest-agent#windows-failover-cluster-support) enabled.



You use a [SQL Server premium image](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server) which has SQL Server 2022 preinstalled.

**Note:** If you plan to bring your own licenses for SQL Server by using the [License Mobility](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) program, select Windows Server base images for these nodes and install SQL Server using your own product keys.

To provide a tie-breaking vote and achieve a quorum for the failover scenario, deploy a third VM that serves as a [file share witness](https://docs.microsoft.com/en-us/windows-server/failover-clustering/manage-cluster-quorum#quorum-configuration-options) using the following steps:

  1. Return to your existing Cloud Shell session.
  2. Create a [specialized script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the WSFC nodes. This script installs the necessary Windows features and creates firewall rules for WSFC and SQL Server.
         
         cat << "EOF" > specialize-node.ps1
         
         $ErrorActionPreference = "stop"
         
         # Install required Windows features
         Install-WindowsFeature Failover-Clustering -IncludeManagementTools
         Install-WindowsFeature RSAT-AD-PowerShell
         
         # Open firewall for WSFC
         netsh advfirewall firewall add rule name="Allow WSFC health check" dir=in action=allow protocol=TCP localport=59998
         
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
         

  3. Create the VM instances. On the two cluster nodes, attach a data disk and set the `enable-wsfc` metadata key to `true`. This action enables [Windows Server Failover Clustering](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#windows-failover) and configures a local listener on the default port (59998).
         
         REGION=$(gcloud config get-value compute/region)
         ZONE1=ZONE1
         ZONE2=ZONE2
         ZONE3=ZONE3
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
           --machine-type e2-medium \
           --subnet $SUBNET_NAME \
           --image-family=windows-2022 \
           --image-project=windows-cloud \
           --tags wsfc \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --metadata sysprep-specialize-script-ps1="add-windowsfeature FS-FileServer"
         

Replace ZONE1, ZONE2, ZONE3 based on the zones you are using.

**Note:** Depending on your [performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance#optimize_disk_performance), consider using a machine type larger than `n2-standard-8` for the WSFC nodes. Consider [disabling Simultaneous multithreading (SMT)](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) for potential savings on licensing costs.**Note:** For the purpose of this tutorial, and to fit within the default regional SSD Persistent Disk quota, the size of the disks attached to each VM is smaller than it would be in a production environment. For better performance and to accommodate a larger database, increase the size of each disk.
  4. To join the three VM instances to Active Directory, do the following for each of the three VM instances:

     1. Monitor the initialization process of the VM by viewing its serial port output.
            
            gcloud compute instances tail-serial-port-output NAME
            

Replace `NAME` with the name of the VM instance.

Wait for a few minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

     2. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance.

     3. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using the username and password created in the previous step.

     4. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

**Note:** In this guide, we used Powershell 5.1.
     5. Confirm the elevation prompt by clicking **Yes**.

     6. Join the computer to your Active Directory domain and restart.
            
            Add-Computer -Domain DOMAIN -Restart
            

Replace `DOMAIN` with the DNS name of your Active Directory domain.

     7. Enter the credentials of an account that has permissions to join a VM to the domain

Wait for the VM to restart. You have now joined the VM instance to the Active Directory.




### Reserve static IP addresses

You now reserve two static IP addresses in your VPC. One IP address is used as the default WSFC cluster IP address, the other serves as the static IP for the SQL Server availability group listener.

In a WSFC cluster, the cluster IP address primarily serves administrative purposes and accessing cluster resources. This virtual IP address is assigned to the cluster itself, enabling administrators to manage the cluster and perform tasks such as configuring cluster settings, monitoring the health of nodes, and managing failover processes.

In the context of SQL Server availability group, a listener is a virtual network name (VNN) and IP address that allows clients to connect to the availability group without needing to know which specific server is the primary node.

An internal load balancer needs an internal IP address to efficiently route internal traffic and support high availability and load balancing in the context of a WSFC cluster. The internal load balancer ensures that requests are always directed to the current primary replica of the cluster. During failover events, the load balancer detects changes in the primary replica and redirects client connections to the new primary without requiring manual intervention, minimizing downtime and ensuring continuous availability of the database services.

In the context of a WSFC with SQL Server Always On availability groups, both reserved internal static IP addresses for the default WSFC cluster IP address and the availability group listener are also used by associated internal load balancers.

  1. To reserve two static IP addresses in your VPC, use the following steps.
         
         gcloud compute addresses create wsfc-cluster-ip \
           --subnet $SUBNET_NAME \
           --region $(gcloud config get-value compute/region) && \
         CLUSTER_IP=$(gcloud compute addresses describe wsfc-cluster-ip \
             --region $(gcloud config get-value compute/region) \
             --format=value\(address\)) && \
         echo "cluster IP: $CLUSTER_IP"
         

  2. Replace the cluster IP address in the `CLUSTER_IP` variable, you need it later to specify it as the cluster IP:
         
         CLUSTER_IP=CLUSTER_IP
         

  3. Reserve another static IP for the availability group listener and capture the address in a new environment variable named `LISTENER_IP`.
         
         gcloud compute addresses create wsfc-listener-ip \
           --subnet $SUBNET_NAME \
           --region $(gcloud config get-value compute/region)
         
         LISTENER_IP=$(gcloud compute addresses describe wsfc-listener-ip \
           --region $(gcloud config get-value compute/region) \
           --format=value\(address\)) && \
         echo "Listener IP: $LISTENER_IP"
         

**Note:** Make sure that the IP address is in the same region as your SQL Server cluster.
  4. Replace the load balancer's reserved IP address as the `LISTENER_IP` variable, you need it later to configure your availability group.
         
         LISTENER_IP=LISTENER_IP
         




Your project and VPC are now ready for the deployment of the Windows Server Failover Cluster and SQL Server.

## Deploying the failover cluster

You can now use the VM instances to deploy a Windows Server Failover Cluster and SQL Server. The following sections discuss how you can do this in detail.

### Preparing SQL Server

Create a new user account in Active Directory for SQL Server using the following steps.

  1. Connect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a domain user account for SQL server and the SQL agent and assign a password:
         
         $Credential = Get-Credential -UserName sql_server -Message 'Enter password'
         New-ADUser `
           -Name "sql_server" `
           -Description "SQL Admin account." `
           -AccountPassword $Credential.Password `
           -Enabled $true -PasswordNeverExpires $true
         

**Note:** If you use Managed AD, append `-Path "OU=Cloud,DC=example,DC=org"` to the command to create the user in the `Cloud` organizational units (OU). Ensure that the value of the path is the output of the following command: `Get-ADOrganizationalUnit -Filter "Name -eq 'Cloud'" | Select-Object -ExpandProperty DistinguishedName`



To configure SQL Server, perform the following steps on both `node-1` and `node-2`, use the following steps:

  1. Open **SQL Server Configuration Manager**.
  2. In the navigation pane, select **SQL Server Services**.
  3. In the list of services, right-click **SQL Server (MSSQLSERVER)** and select **Properties**.
  4. Under **Log on as** , change the account as follows:

     * **Account name:** `DOMAIN\sql_server` where `DOMAIN` is the NetBIOS name of your Active Directory domain.
     * **Password:** Enter the password you chose previously.
  5. Click **OK**.

  6. When prompted to restart SQL Server, select **Yes**.




SQL Server now runs under a domain user account.

**Warning:** Make sure you've completed the previous configuration steps on both VM instances, otherwise setting up the Always On availability group will fail.

### Create file shares

Create two file shares on the VM instance `witness` so that it can store SQL Server backups and act as a file share witness:

  1. Connect to `witness` by [using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a witness file share and grant yourself and the two cluster nodes access to the file share.
         
         New-Item "C:\QWitness" –type directory
         
         icacls C:\QWitness\ /grant 'node-1$:(OI)(CI)(M)'
         icacls C:\QWitness\ /grant 'node-2$:(OI)(CI)(M)'
         
         New-SmbShare `
           -Name QWitness `
           -Path "C:\QWitness" `
           -Description "SQL File Share Witness" `
           -FullAccess $env:username,node-1$,node-2$
         

  5. Create another file share to store backups and grant SQL Server full access:
         
         New-Item "C:\Backup" –type directory
         New-SmbShare `
           -Name Backup `
           -Path "C:\Backup" `
           -Description "SQL Backup" `
           -FullAccess  $env:USERDOMAIN\sql_server
         




### Create the failover cluster

To create the failover cluster, use the following steps:

  1. Return to the Remote Desktop session on `node-1`.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a new cluster.
         
         New-Cluster `
           -Name sql-cluster `
           -Node node-1,node-2 `
           -NoStorage `
           -StaticAddress CLUSTER_IP
         

Replace `CLUSTER_IP` with the cluster IP address that you created earlier.

**Note:** When _computer objects_ are created outside the container `Computers` (in an OU), the permission `Create Computer objects` must be delegated to the cluster's computer account in the OU.
  5. Return to the PowerShell session on `witness` and grant the virtual computer object of the cluster permission to access the file share.
         
         icacls C:\QWitness\ /grant 'sql-cluster$:(OI)(CI)(M)'
         Grant-SmbShareAccess `
           -Name QWitness `
           -AccountName 'sql-cluster$' `
           -AccessRight Full `
           -Force
         

  6. Return to the PowerShell session on `node-1` and configure the cluster to use the file share on `witness` as a cluster quorum.
         
         Set-ClusterQuorum -FileShareWitness \\witness\QWitness
         

  7. Verify that the cluster was created successfully.
         
         Test-Cluster
         

You might see the following warnings that you can safely ignore.
         
         WARNING: System Configuration - Validate All Drivers Signed: The test reported some warnings..
         WARNING: Network - Validate Network Communication: The test reported some warnings..
         WARNING:
         Test Result:
         HadUnselectedTests, ClusterConditionallyApproved
         Testing has completed for the tests you selected. You should review the warnings in the Report.  A cluster solution is
         supported by Microsoft only if you run all cluster validation tests, and all tests succeed (with or without warnings).
         

You can also launch the Failover Cluster Manager MMC snap-in to review the cluster's health by running `cluadmin.msc`.

  8. If you're using Managed AD, add the computer account used by the Windows cluster to the _Cloud Service Domain Join Accounts_ group so that it can join computers to the domain.
         
         Add-ADGroupMember `
           -Identity "Cloud Service Domain Join Accounts" `
           -Members sql-cluster$
         

  9. Enable Always On availability groups on both nodes.
         
         Enable-SqlAlwaysOn -ServerInstance node-1 -Force
         Enable-SqlAlwaysOn -ServerInstance node-2 -Force
         




## Creating an availability group

You now create a sample database `bookshelf`, include it in a new availability group named `bookshelf-ag` and configure high availability.

### Creating a database

Create a new database. For the purpose of this tutorial, the database doesn't need to contain any data.

  1. Return to the Remote Desktop session on `node-1`.
  2. Open the **SQL Server Management Studio**.
  3. In the **Connect to server** dialog, verify the server name is set to `node-1` and select **Connect**.
  4. In the menu, select **File > New > Query with current connection**.
  5. Paste the following SQL script into the editor:
         
         -- Create a sample database
         CREATE DATABASE bookshelf ON PRIMARY (
           NAME = 'bookshelf',
           FILENAME='d:\Data\bookshelf.mdf',
           SIZE = 256MB,
           MAXSIZE = UNLIMITED,
           FILEGROWTH = 256MB)
         LOG ON (
           NAME = 'bookshelf_log',
           FILENAME='d:\Logs\bookshelf.ldf',
           SIZE = 256MB,
           MAXSIZE = UNLIMITED,
           FILEGROWTH = 256MB)
         GO
         
         USE [bookshelf]
         SET ANSI_NULLS ON
         SET QUOTED_IDENTIFIER ON
         GO
         
         -- Create sample table
         CREATE TABLE [dbo].[Books] (
           [Id] [bigint] IDENTITY(1,1) NOT NULL,
           [Title] [nvarchar](max) NOT NULL,
           [Author] [nvarchar](max) NULL,
           [PublishedDate] [datetime] NULL,
           [ImageUrl] [nvarchar](max) NULL,
           [Description] [nvarchar](max) NULL,
           [CreatedById] [nvarchar](max) NULL,
           CONSTRAINT [PK_dbo.Books] PRIMARY KEY CLUSTERED ([Id] ASC) WITH (
             PAD_INDEX = OFF,
             STATISTICS_NORECOMPUTE = OFF,
             IGNORE_DUP_KEY = OFF,
             ALLOW_ROW_LOCKS = ON,
             ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
         ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
         GO
         
         -- Create a backup
         EXEC dbo.sp_changedbowner @loginame = 'sa', @map = false;
           ALTER DATABASE [bookshelf] SET RECOVERY FULL;
           GO
           BACKUP DATABASE bookshelf to disk = '\\witness\Backup\bookshelf.bak' WITH INIT
         GO
         

The script creates a new database with a single table and performs an initial backup to `witness`.

  6. Select **Execute** to run the SQL script.




### Configure high availability

You can now configure high availability for the availability group using either T-SQL or SQL Server Management Studio.

### Using T-SQL

To configure high availability for the availability group using T-SQL, use the following steps:

  1. Connect to `node-1` and then execute the following script to create the bookshelf-ag availability group.
         
         CREATE LOGIN [NET_DOMAIN\sql_server] FROM WINDOWS;
         GO
         
         USE [bookshelf];
         CREATE USER [NET_DOMAIN\sql_server] FOR LOGIN [NET_DOMAIN\sql_server];
         GO
         
         USE [master];
         CREATE ENDPOINT bookshelf_endpoint
           STATE=STARTED
           AS TCP (LISTENER_PORT=5022)
           FOR DATABASE_MIRRORING (ROLE=ALL);
         GO
         
         GRANT CONNECT ON ENDPOINT::[bookshelf_endpoint] TO [NET_DOMAIN\sql_server]
         GO
         

**Note:** In the `NET_DOMAIN\sql_server` login and user, `NET_DOMAIN` is the NetBIOS name of your Active Directory domain.
  2. Connect to `node-2` and execute the following script.
         
         CREATE LOGIN [NET_DOMAIN\sql_server] FROM WINDOWS;
         GO
         
         CREATE ENDPOINT bookshelf_endpoint
           STATE=STARTED
           AS TCP (LISTENER_PORT=5022)
           FOR DATABASE_MIRRORING (ROLE=ALL);
         GO
         
         GRANT CONNECT ON ENDPOINT::[bookshelf_endpoint] TO [NET_DOMAIN\sql_server]
         GO
         

**Note:** In the `NET_DOMAIN\sql_server` login and user, `NET_DOMAIN` is the NetBIOS name of your Active Directory domain.
  3. On `node-1` and then execute the following script to create the `bookshelf-ag` availability group.
         
         USE master;
         GO
         
         CREATE AVAILABILITY GROUP [bookshelf-ag]
         WITH (AUTOMATED_BACKUP_PREFERENCE = SECONDARY,
         CLUSTER_TYPE = WSFC,
         DB_FAILOVER = ON
         )
         FOR DATABASE [bookshelf]
         REPLICA ON
           N'node-1' WITH (
               ENDPOINT_URL = 'TCP://node-1:5022',
               AVAILABILITY_MODE = SYNCHRONOUS_COMMIT,
               FAILOVER_MODE = AUTOMATIC,
               BACKUP_PRIORITY = 50,
               SEEDING_MODE = AUTOMATIC,
               SECONDARY_ROLE(ALLOW_CONNECTIONS = NO)
           ),
           N'node-2' WITH (
               ENDPOINT_URL = 'TCP://node-2:5022',
               AVAILABILITY_MODE = SYNCHRONOUS_COMMIT,
               FAILOVER_MODE = AUTOMATIC,
               BACKUP_PRIORITY = 50,
               SEEDING_MODE = AUTOMATIC,
               SECONDARY_ROLE(ALLOW_CONNECTIONS = NO)
           );
         GO
         

  4. In the following script, replace `LISTENER_IP` with the IP address that you reserved earlier for the internal load balancer and execute it.
         
         USE master;
         GO
         
         ALTER AVAILABILITY GROUP [bookshelf-ag]
         ADD LISTENER N'bookshelf' (
         WITH IP (
           (N'LISTENER_IP', N'255.255.255.0')
         ),
         PORT = 1433);
         GO
         

  5. Connect to `node-2` and then execute the following script to join the secondary replica to the availability group and enable automatic seeding.
         
         USE master;
         GO
         
         ALTER AVAILABILITY GROUP [bookshelf-ag] JOIN;
         ALTER AVAILABILITY GROUP [bookshelf-ag] GRANT CREATE ANY DATABASE;
         
         

  6. Check the status of the availability group.
         
         SELECT * FROM sys.dm_hadr_availability_group_states;
         GO
         

You should see `synchronization_health_desc` as `HEALTHY`




### Using SQL Server Management Studio

To configure high availability for the availability group using SQL Server Management Studio, use the following steps:

  1. In the **Object Explorer** window, right-click **Always On High Availability** and then select **New Availability Group Wizard**.
  2. On the **Specify Options** page, set the availability group name to `bookshelf-ag`, then select **Next**.
  3. On the **Select Databases** page, select the `bookshelf` database, then select **Next**.
  4. On the **Specify Replicas** page, select the **Replicas** tab.

     1. Select **Add replica**.
     2. In the **Connect to server** dialog, enter the server name `node-2` and select **Connect**.

The list of availability replicas now contains SQL Server instances, `node-1` and `node-2`.

     3. Set the **Availability mode** to **Synchronous commit** for both instances.

     4. Set **Automatic failover** to **Enabled** for both instances.

     5. Select the **Listener** tab

        1. Select **Create an availability group listener**.
        2. Enter the following settings.

           * **Listener DNS name** : `bookshelf`
           * **Port** : `1433`
           * **Network mode** : **Static IP**
        3. Select **Add** and enter the listener IP address (``LISTENER_IP``) that you reserved earlier for the internal load balancer. Then select **OK**.

     6. Select **Next**.

  5. On the **Select Data Synchronization** page, select **Automatic Seeding**.

  6. On the **Validation** page, verify that all checks are successful.

  7. On the **Summary** page, select **Finish**.

  8. On the **Results** page, select **Close**.




### Create internal load balancers and health checks

The cluster IP represents a single endpoint for the Windows failover cluster. You use it for administrative purposes and managing cluster resources. The cluster IP always points to the host (or primary) node of the cluster. You deploy an [internal load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal#deploying_internal_load_balancing) that uses a health check that ensures that traffic is directed to the host node of the cluster. As WSFC tooling requires multiple protocols to be available for forwarding (ICMP, UDP, and TCP), we recommend deploying an internal load balancer with [multiple protocols that support all ports](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols).

To deploy an internal load balancer, use the following steps:

  1. Return to your existing Cloud Shell session.
  2. Create two [unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances), one per zone, and add the two nodes to the groups.
         
         REGION=$(gcloud config get-value compute/region)
         
         gcloud compute instance-groups unmanaged create wsfc-group-1 --zone $ZONE1
         gcloud compute instance-groups unmanaged add-instances wsfc-group-1 --zone $ZONE1 \
           --instances node-1
         
         gcloud compute instance-groups unmanaged create wsfc-group-2 --zone $ZONE2
         gcloud compute instance-groups unmanaged add-instances wsfc-group-2 --zone $ZONE2 \
           --instances node-2
         

  3. Create health check for the cluster IP that the load balancer can use to determine which is the active node from the Windows cluster perspective. The default port which the [Compute Engine guest agent](https://github.com/GoogleCloudPlatform/guest-agent) responds to health checks is `59998`. The health check provides the cluster IP address in the request and it expects _1_ as a response returned from the active node.
         
         gcloud compute health-checks create tcp wsfc-healthcheck \
           --request=$CLUSTER_IP \
           --response=1 \
           --check-interval="2s" \
           --healthy-threshold=2 \
           --unhealthy-threshold=2 \
           --port=59998 \
           --timeout="1s"
         

  4. Create a backend service and add the two existing instance groups.
         
         gcloud compute backend-services create wsfc-backend \
           --load-balancing-scheme internal \
           --region $REGION \
           --health-checks wsfc-healthcheck \
           --protocol UNSPECIFIED
         
         gcloud compute backend-services add-backend wsfc-backend \
           --instance-group wsfc-group-1 \
           --instance-group-zone $ZONE1 \
           --region $REGION
         
         gcloud compute backend-services add-backend wsfc-backend \
           --instance-group wsfc-group-2 \
           --instance-group-zone $ZONE2 \
           --region $REGION
         

  5. Create the internal load balancer associated with the cluster IP.
         
         gcloud compute forwarding-rules create wsfc \
           --load-balancing-scheme internal \
           --address $CLUSTER_IP \
           --ports ALL \
           --network $VPC_NAME \
           --subnet $SUBNET_NAME \
           --region $REGION \
           --ip-protocol L3_DEFAULT \
           --backend-service wsfc-backend
         




To provide a single endpoint for SQL Server clients that want to connect to any database in your `bookshelf` availability group, deploy a new internal load balancer dedicated to that availability group, use the following steps:

  1. Create a health check for the availability group listener that the load balancer can use to determine which is the primary node in the `bookshelf` SQL Server availability group.
         
         gcloud compute health-checks create tcp wsfc-bookshelf-healthcheck \
           --request=$LISTENER_IP \
           --response=1 \
           --check-interval="2s" \
           --healthy-threshold=1 \
           --unhealthy-threshold=2 \
           --port=59998 \
           --timeout="1s"
         

The health check uses the same Compute Engine guest agent port, but it provides in its request the listener IP address of the `bookshelf` availability group.

  2. Create a new backend service and add the two instance groups.
         
         gcloud compute backend-services create wsfc-bookshelf-backend \
           --load-balancing-scheme internal \
           --region $REGION \
           --health-checks wsfc-bookshelf-healthcheck \
           --protocol UNSPECIFIED
         
         gcloud compute backend-services add-backend wsfc-bookshelf-backend \
           --instance-group wsfc-group-1 \
           --instance-group-zone $ZONE1 \
           --region $REGION
         
         gcloud compute backend-services add-backend wsfc-bookshelf-backend \
           --instance-group wsfc-group-2 \
           --instance-group-zone $ZONE2 \
           --region $REGION
         

  3. Create the internal load balancer associated with the SQL Server `bookshelf-ag` availability group listener.
         
         gcloud compute forwarding-rules create wsfc-bookshelf \
           --load-balancing-scheme internal \
           --address $LISTENER_IP \
           --ports ALL \
           --network $VPC_NAME \
           --subnet $SUBNET_NAME \
           --region $REGION \
           --ip-protocol L3_DEFAULT \
           --backend-service wsfc-bookshelf-backend
         




You can now connect to SQL Server availability group listener by using the DNS name `bookshelf` and its port defined in the bookshelf availability group listener. The internal load balancer directs traffic to the primary node of the `bookshelf` availability group.

To create multiple availability groups on a single failover cluster, you must use separate backend services and a separate load balancer with its own healthcheck per availability group.

Each availability group might have different nodes designated as the primary, and they might be different than the host node of the Windows cluster. For multiple availability groups, you need the following:

  * A reserved static IP address for the availability group listener that the internal load balancer uses. Reserve one address for each availability group.

  * A separate health check rule for each availability group. The request of the health check provides the static IP address of the availability group listener ( which is also the reserved IP address at the previous step). The health check probes for response `1` returned by the GCE agent. All health checks use port `59998`.

  * A separate backend service for each availability group to which you add the existing two compute instance groups. The backend service uses the health check defined at the previous step.

  * An internal load balancer for each availability group for the backend service created at the previous step. The load balancer is associated with the availability group listener static IP address.




## Test the failover

You are now ready to test if the failover works as expected:

  1. Return to the PowerShell session on `witness`.
  2. Run the following script.
         
         while ($True){
           $Conn = New-Object System.Data.SqlClient.SqlConnection
           $Conn.ConnectionString = "Server=tcp:bookshelf,1433;Integrated Security=true;Initial Catalog=master"
           $Conn.Open()
         
           $Cmd = New-Object System.Data.SqlClient.SqlCommand
           $Cmd.Connection = $Conn
           $Cmd.CommandText = "SELECT SERVERPROPERTY('ServerName')"
         
           $Adapter = New-Object System.Data.SqlClient.SqlDataAdapter $Cmd
           $Data = New-Object System.Data.DataSet
           $Adapter.Fill($Data) | Out-Null
           $Data.Tables[0] + (Get-Date -Format "MM/dd/yyyy HH:mm:ss")
         
           Start-Sleep -Seconds 2
         }
         

In this guide, we used the DNS name `bookshelf` and the port value `1433` for the availability group listener in the server definition `tcp:bookshelf,1433`.

Every 2 seconds, the script connects to SQL Server by using the availability group listener, and queries the server name.

Leave the script running.

  3. Return to the Remote Desktop session on `node-1` to trigger a failover.

     1. In **SQL Server Management Studio** , navigate to **Always On High Availability > Availability Groups > bookshelf-ag (Primary)** and right-click the node.
     2. Select **Failover**.
     3. On the **Select new primary replica** page, verify that `node-2` is selected as new primary replica and that the **Failover readiness** column indicates `No data loss`. Then select **Next**.
     4. On the **Connect to replica** page, select **Connect**.
     5. In the **Connect to server** dialog, verify that the server name is `node-2` and click **Connect**.
     6. Select **Next** and then **Finish**.
     7. On the **Results** page, verify that the failover was successful.
  4. Return to the PowerShell session on `witness`.

  5. Observe the output of the running script and notice that the server name changes from `node-1` to `node-2` as a result of the failover.

  6. Stop the script by pressing `Ctrl+C`.




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Delete the project

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



## What's next

  * Learn how you can [configure a SQL Server failover cluster instance that uses Storage Spaces Direct](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance).
  * Learn how you can [configure a SQL Server failover cluster instance that uses Persistent Disk in multi-writer mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
