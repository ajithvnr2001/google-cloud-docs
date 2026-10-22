---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance/
title: Configuring a SQL Server failover cluster instance that uses Storage Spaces Direct \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:23.761420+00:00
---

# Configuring a SQL Server failover cluster instance that uses Storage Spaces Direct  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configuring a SQL Server failover cluster instance that uses Storage Spaces Direct Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft SQL Server [Always On Failover Cluster Instances](https://docs.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/always-on-failover-cluster-instances-sql-server?view=sql-server-ver15) (FCI) let you run a single SQL Server instance across multiple Windows Server Failover Cluster (WSFC) nodes. At any point in time, one of the cluster nodes actively hosts the SQL instance. In the event of a failure, WSFC automatically transfers ownership of the instance's resources to another node.

SQL Server FCI requires data to be located on shared storage so that it can be accessed across all WSFC nodes. This guide describes how you can deploy a SQL Server 2019 failover cluster instance that uses [Storage Spaces Direct](https://docs.microsoft.com/en-us/windows-server/storage/storage-spaces/storage-spaces-direct-overview) (S2D) for shared storage. S2D provides a software-based virtual SAN that can use Compute Engine VM data disks to store the SQL database.

The following diagram illustrates the deployment:

![Architecture](https://docs.cloud.google.com/static/compute/images/sqlserver-fci-s2d-architecture.svg)

Implementing a hyper-converged architecture, the VM instances `node-1` and `node-2` serve as WSFC nodes and also host the shared storage. A third VM instance, `witness`, is used to achieve a quorum in a failover scenario. The three VM instances are distributed over three zones and share a common subnet.

Clients communicate with the SQL Server instance over an [internal TCP load balancer](https://docs.cloud.google.com/load-balancing/docs/internal). This load balancer uses a custom health check to determine which WSFC node is currently hosting the SQL instance and routes traffic to that instance.

The article assumes that you have already deployed Active Directory on Google Cloud and that you have basic knowledge of SQL Server, Active Directory, and Compute Engine.

## Objectives

  * Deploy a WSFC comprising two SQL Server VM instances and a third VM instance that acts as a file share witness.
  * Deploy a SQL Server FCI on the WSFC.
  * Verify that the cluster is working by simulating a failover.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Compute Engine](https://cloud.google.com/products/compute/pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



Use the [pricing calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

## Before you begin

To complete this guide, you need the following:

  * An Active Directory domain with at least one domain controller. You can create an Active Directory domain [by using Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain). Alternatively, you can deploy a [custom Active Directory environment on Compute Engine](https://docs.cloud.google.com/solutions/deploy-fault-tolerant-active-directory-environment) and [set up a private DNS forwarding zone](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones) that forwards DNS queries to your domain controllers.
  * An Active Directory user that has permission to join computers to the domain and can log in by using RDP. If you're using Managed Microsoft AD, you can use the `setupadmin` user.
  * A Google Cloud project and VPC with connectivity to your Active Directory domain controllers.
  * A subnet to use for the WSFC VM instances.



To complete the guide, you also need a Google Cloud project:

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




When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more information, see Cleaning up.

## Preparing the project and network

To prepare your Google Cloud project and VPC for the deployment of SQL Server FCI, do the following:

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Initialize the following variables:
         
         VPC_NAME=VPC_NAME
         SUBNET_NAME=SUBNET_NAME
         

Where:

     * `VPC_NAME`: name of your VPC
     * `SUBNET_NAME`: name of your subnet
  3. Set your default [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  4. Set your default region:
         
         gcloud config set compute/region REGION
         

Replace `REGION` with the ID of the region you want to deploy in.




### Create firewall rules

To allow clients to connect to SQL Server, allow communication between the WSFC nodes, and to enable the load balancer to [perform health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule), you need to create several firewall rules. To simplify the creation of these firewall rules, you use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags):

  * The 2 WSFC nodes are annotated with the `wsfc-node` tag.
  * All servers (including the witness) are annotated with the `wsfc` tag.



Create firewall rules that use these network tags:

  1. Return to your existing Cloud Shell session.
  2. Create firewall rules for the WSFC nodes:
         
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

You now deploy two VM instances for the failover cluster. At any point in time, only one of these VMs serves as the active FCI node while the other node serves as the failover node. The two VM instances must meet the following requirements:

  * They are located in the same region so that they can be accessed by an internal TCP load balancer.
  * Their guest agent is [configured to use WSFC mode](https://github.com/GoogleCloudPlatform/guest-agent#windows-failover-cluster-support). In this mode, the guest agent ignores the IP addresses of internal load balancers when configuring the local network interface. This behavior is necessary to prevent IP address conflicts during WSFC failover events.



You use a [SQL Server premium image](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server) which has SQL Server 2019 preinstalled.

**Note:** If you plan to bring your own licenses for SQL Server by using the [license mobility](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) program, select Windows Server base images for these nodes and install SQL Server using your own product keys.

To provide a tie-breaking vote and achieve a quorum for the failover scenario, you deploy a third VM that serves as a [file share witness](https://docs.microsoft.com/en-us/windows-server/failover-clustering/manage-cluster-quorum#quorum-configuration-options).

  1. Return to your existing Cloud Shell session.
  2. Create a [specialize script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the WSFC nodes. The script installs the necessary Windows feature and creates firewall rules for WSFC and SQL Server:
         
         cat << "EOF" > specialize-node.ps1
         
         $ErrorActionPreference = "stop"
         
         # Install required Windows features
         Install-WindowsFeature Failover-Clustering -IncludeManagementTools
         Install-WindowsFeature RSAT-AD-PowerShell
         
         # Open firewall for WSFC
         netsh advfirewall firewall add rule name="Allow SQL Server health check" dir=in action=allow protocol=TCP localport=59997
         
         # Open firewall for SQL Server
         netsh advfirewall firewall add rule name="Allow SQL Server" dir=in action=allow protocol=TCP localport=1433
         
         EOF
         

  3. Create the VM instances. On the two VMs that serve as S2D and WSFC nodes, attach additional data disks and enable the WSFC mode by setting the metadata key `enable-wsfc` to `true`:
         
         REGION=$(gcloud config get-value compute/region)
         PD_SIZE=50
         MACHINE_TYPE=n2-standard-8
         
         gcloud compute instances create node-1 \
           --zone $REGION-a \
           --machine-type $MACHINE_TYPE \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2019-win-2022 \
           --image-project windows-sql-cloud \
           --tags wsfc,wsfc-node \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --boot-disk-device-name "node-1" \
           --create-disk=name=node-1-datadisk-1,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --create-disk=name=node-1-datadisk-2,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --create-disk=name=node-1-datadisk-3,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --create-disk=name=node-1-datadisk-4,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --metadata enable-wsfc=true \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-node.ps1
         
         gcloud compute instances create node-2 \
           --zone $REGION-b \
           --machine-type $MACHINE_TYPE \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2019-win-2022 \
           --image-project windows-sql-cloud \
           --tags wsfc,wsfc-node \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd \
           --boot-disk-device-name "node-2" \
           --create-disk=name=node-2-datadisk-1,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --create-disk=name=node-2-datadisk-2,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --create-disk=name=node-2-datadisk-3,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
           --create-disk=name=node-2-datadisk-4,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
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
         

**Note:** Depending on your [performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance#optimize_disk_performance), consider using a machine type larger than `n2-standard-8` for the WSFC nodes.**Note:** For the purpose of this tutorial, and to fit within the default regional SSD persistent disk quota, the size of the disks attached to each VM is smaller than it would be in a production environment. For better performance and to accommodate a larger database, you would increase the size of each disk. For more information about choosing S2D drives, refer to the [S2D documentation](https://docs.microsoft.com/en-us/windows-server/storage/storage-spaces/choosing-drives).
  4. To join the 3 VM instances to Active Directory, do the following for each of the 3 VM instances:

     1. Monitor the initialization process of the VM by viewing its serial port output:
            
            gcloud compute instances tail-serial-port-output NAME
            

Replace `NAME` with the name of the VM instance.

Wait for a few minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

     2. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

     3. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and log in using the username and password created in the previous step.

     4. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

     5. Confirm the elevation prompt by clicking **Yes**.

     6. Join the computer to your Active Directory domain and restart:
            
            Add-Computer -Domain DOMAIN -Restart
            

Replace `DOMAIN` with the DNS name of your Active Directory domain.

Wait for approximately 1 minute for the restart to complete.




### Reserve cluster IP addresses

You now reserve two static IP addresses in your VPC network. The two addresses serve different purposes:

  * **Load balancer IP** : This IP address is used by clients to connect to SQL Server.
  * **Cluster IP** : This IP address is only used internally by WSFC.



To reserve the static IP addresses, do the following:

  1. Reserve a static IP for the internal load balancer and capture the address in a new environment variable named `LOADBALANCER_ADDRESS`:
         
         gcloud compute addresses create wsfc \
           --subnet $SUBNET_NAME \
           --region $(gcloud config get-value compute/region)
         
         LOADBALANCER_ADDRESS=$(gcloud compute addresses describe wsfc \
           --region $(gcloud config get-value compute/region) \
           --format=value\(address\)) && \
         echo "Load Balancer IP: $LOADBALANCER_ADDRESS"
         

Note the IP address, you need it later.

  2. Reserve another static IP address that you use as cluster IP:
         
         gcloud compute addresses create wsfc-cluster \
           --subnet $SUBNET_NAME \
           --region $(gcloud config get-value compute/region) && \
         CLUSTER_ADDRESS=$(gcloud compute addresses describe wsfc-cluster \
             --region $(gcloud config get-value compute/region) \
             --format=value\(address\)) && \
         echo "Cluster IP: $CLUSTER_ADDRESS"
         

Note the IP address, you need it later.




Your project and VPC are now ready for the deployment of the WSFC and SQL Server.

### Create a witness file share

To prepare `witness` to serve as file share witness, create a file share and grant yourself and the two WSFC nodes access to the file share:

  1. Connect to `witness` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Log in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create the witness folder and share the folder:
         
         New-Item "C:\QWitness" -Type directory
         
         icacls C:\QWitness\ /grant 'node-1$:(OI)(CI)(M)'
         icacls C:\QWitness\ /grant 'node-2$:(OI)(CI)(M)'
         
         New-SmbShare `
           -Name QWitness `
           -Path "C:\QWitness" `
           -Description "SQL File Share Witness" `
           -FullAccess  $env:username,node-1$,node-2$
         




## Deploying the failover cluster

You now use the VM instances to deploy a WSFC and SQL Server.

### Deploy WSFC

You are now ready to create the failover cluster:

  1. Connect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Log in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a new cluster:
         
         New-Cluster `
           -Name windows-fci `
           -Node node-1,node-2 `
           -NoStorage `
           -StaticAddress CLUSTER_ADDRESS
         

Replace `CLUSTER_ADDRESS` with the cluster IP address that you created earlier.

The command creates a computer account `windows-fci` in your Active Directory domain.

  5. Return to the PowerShell session on `witness` and grant the computer account `windows-fci` permission to access the file share:
         
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
         
         WARNING: System Configuration - Validate All Drivers Signed: The test reported some warnings..
         WARNING: Network - Validate Network Communication: The test reported some warnings..
         WARNING:
         Test Result:
         HadUnselectedTests, ClusterConditionallyApproved
         Testing has completed for the tests you selected. You should review the warnings in the Report.  A cluster solution is
         supported by Microsoft only if you run all cluster validation tests, and all tests succeed (with or without warnings).
         

You can also launch the Failover Cluster Manager MMC snap-in to review the cluster's health by running `cluadmin.msc`.

  8. If you're using Managed AD, add the computer account used by WSFC to the **Cloud Service Domain Join Accounts** group so that it can join computers to the domain:
         
         Install-WindowsFeature RSAT-ADDS
         Add-ADGroupMember `
           -Identity "Cloud Service Domain Join Accounts" `
           -Members windows-fci$
         




### Enabling Storage Spaces Direct

You now enable S2D and create a cluster shared volume which combines the three persistent disks that you created earlier:

  1. Return to the PowerShell session on `node-1`.
  2. Enable S2D:
         
         Enable-ClusterStorageSpacesDirect
         

Optionally, if you want better disk performance, you can add SCSI [local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd) to your S2D nodes in addition to standard SSD persistent disks. The local SSDs can serve as the S2D caching layer. Make the number of capacity drives (SSD persistent disks in our case) a multiple of the number of local SSDs. Run the following command instead for enabling S2D with caching:
         
         Enable-ClusterStorageSpacesDirect -CacheDeviceModel "EphemeralDisk"
         

Accept the default when prompted to confirm. You might see some warnings that can be safely ignored:
         
         WARNING: 2021/04/08-13:12:26.159 Node node-1: No disks found to be used for cache
         WARNING: 2021/04/08-13:12:26.159 Node node-2: No disks found to be used for cache
         

  3. Optionally, set the Cluster Shared Volume (CSV) in-memory cache to 2048 MB for better read throughput:
         
         (Get-Cluster).BlockCacheSize = 2048
         

  4. Create a new volume that uses the cluster shared volume versions of ReFS and a 64 KB cluster size:
         
         New-Volume `
           -StoragePoolFriendlyName S2D* `
           -FriendlyName FciVolume `
           -FileSystem CSVFS_ReFS `
           -UseMaximumSize `
           -AllocationUnitSize 65536
         




### Testing storage pool failover

Optionally, you can now test whether the storage pool failover works properly:

  1. Connect to `node-2` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Log in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and select **Run**
  3. Enter `cluadmin.msc` and select **OK**.
  4. In the left window pane, navigate to **Failover Cluster Manager > windows-fci > Storage > Pools**.

You should see a pool named **Cluster Pool 1** with **Owner node** set to `node-1`.

  5. Return to Cloud Shell and reset `node-1` VM to simulate a failover:
         
         gcloud compute instances reset node-1 --zone $REGION-a
         

  6. Return to the **Failover Cluster Manager** on `node-2`.

  7. Observe the status of the storage pool by repeatedly pressing **F5** to refresh the view.

After about 30 seconds, the **owner node** should automatically switch to `node-2`.




### Remove the default SQL Server installation

You now remove the default SQL Server installation from the two nodes and replace it with a new FCI configuration.

For each of the two WSFC nodes, `node-1` and `node-2`, perform the following steps:

  1. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  2. Confirm the elevation prompt by clicking **Yes**.
  3. Remove the default SQL Server instance:
         
         C:\sql_server_install\Setup.exe /Action=Uninstall /FEATURES=SQL,AS,IS,RS /INSTANCENAME=MSSQLSERVER /Q
         

  4. Remove Microsoft OLE Driver:
         
         Get-Package -Name "Microsoft OLE*" | Uninstall-Package -Force
         

  5. Remove Microsoft ODBC Driver:
         
         Get-Package -Name "Microsoft ODBC*" | Uninstall-Package -Force
         

  6. Restart the computer:
         
         Restart-Computer
         

  7. Wait for approximately 1 minute for the restart to complete.




### Install SQL Server FCI

Before you install the new FCI configuration, verify that the `node-1` is the active node in the cluster:

  1. Reconnect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and log in using your domain user.
  2. Right-click the **Start** button (or press **Win+X**) and select **Run**
  3. Enter `cluadmin.msc` and select **OK**.
  4. In the left window pane, navigate to **Failover Cluster Manager > windows-fci**.

Verify that the **current host server** is set to `node-1`.

If the **current host server** is set to `node-2`, right-click **windows-fci** in the left window pane and select **More actions > Move core cluster resources > Select node… > node-1** and click **OK**.

  5. In the left window pane, navigate to **Failover Cluster Manager > windows-fci > Storage > Pools**.

Verify that the **owner node** of **Cluster Pool 1** is set to `node-1`.

If the **owner node** is set to `node-2`, right-click the pool, select **Move > Select Node > node-1** and click **OK**.




You now create a new SQL Server failover cluster installation on `node-1`:

  1. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  2. Confirm the elevation prompt by clicking **Yes**.
  3. Create a domain user account for SQL server and the SQL agent and assign a password:

###  Active Directory 
         
         $Credential = Get-Credential -UserName sql_server -Message 'Enter password'
         New-ADUser `
           -Name "sql_server" `
           -Description "SQL Agent and SQL Admin account." `
           -AccountPassword $Credential.Password `
           -Enabled $true -PasswordNeverExpires $true
         

###  Managed Microsoft AD 
         
         $Credential = Get-Credential -UserName sql_server -Message 'Enter password'
         New-ADUser `
           -Name "sql_server" `
           -Description "SQL Agent and SQL Admin account." `
           -AccountPassword $Credential.Password `
           -Enabled $true -PasswordNeverExpires $true `
           -Path "OU=Cloud,DOMAIN"
         

Replace `DOMAIN` with the distinguished name of your domain, for example `DC=example,DC=org`.

  4. Start the SQL Server setup:
         
         & c:\sql_server_install\setup.exe
         

  5. In the menu on the left, select **Installation**.

  6. Select **New SQL Server failover cluster installation**

  7. On the **Microsoft Update** page, select **Next** to start the installation.

  8. On the **Install Failover Cluster Rules** page, you see a Warning **MSCS cluster verification warnings** and **Windows firewall**. You can ignore these warnings and select **Next**.

  9. On the **Product Key** page, keep the defaults and select **Next**.

  10. On the **License Terms** page, review the terms and, if you accept, select **Next**.

  11. On the **Feature Selection** page, select **Database Engine Services** and select **Next**.

  12. On the **Instance Configuration** page, enter `sql` for the network name and the named instance, and select **Next**.

  13. On the **Cluster Resource Group** page, keep the defaults and select **Next**.

  14. On the **Cluster Disk Selection** page, enable **Cluster Virtual Disk (FciVolume)** and disable all other disks. Select **Next**.

  15. On the **Cluster Network Configuration** page, configure the following settings, then select **Next** :

     * **DHCP** : clear
     * **IP address:** enter the IP address of the internal load balancer.
  16. On the **Server configuration** page, configure the following settings for both **SQL Server Agent** and **SQL Server Database Engine** :

     * **Account name** : `DOMAIN\sql_server` where `DOMAIN` is the NetBIOS name of your Active Directory domain
     * **Password** : Enter the password that you created earlier
  17. Select the **Collation** tab and select the collation that you want to use. Then click **Next**.

  18. On the **Database Engine Configuration** page, select **Add current user** to designate the current user as SQL Server administrator. Then select **Next**.

  19. On the **Ready to Install** page, review the settings, then select **Install**.

  20. After the installation completes, select **Close**.




Your Active Directory domain now contains a computer account `sql` that represents the SQL Server instance and a corresponding DNS entry that points to the IP address of the internal load balancer.

Now add `node-2` to the SQL Server failover cluster:

  1. Connect to `node-2` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and log in using your domain user.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
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

To provide a single endpoint for SQL Server clients, you now deploy an [internal load balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal#deploying_internal_load_balancing). The load balancer uses a health check which ensures that traffic is directed to the active node of the WSFC.

  1. Return to your existing Cloud Shell session.
  2. Create two [unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances), one per zone, and add the two nodes to the groups:
         
         gcloud compute instance-groups unmanaged create wsfc-group-1 --zone $REGION-a
         gcloud compute instance-groups unmanaged add-instances wsfc-group-1 --zone $REGION-a \
           --instances node-1
         
         gcloud compute instance-groups unmanaged create wsfc-group-2 --zone $REGION-b
         gcloud compute instance-groups unmanaged add-instances wsfc-group-2 --zone $REGION-b \
           --instances node-2
         

  3. Create a health check that the load balancer can use to determine which is the active node.
         
         gcloud compute health-checks create tcp wsfc-healthcheck \
           --check-interval="2s" \
           --healthy-threshold=1 \
           --unhealthy-threshold=2 \
           --port=59997 \
           --timeout="1s"
         

The health check probes port `59997`, which is the port you previously configured as `ProbePort` for the SQL Server IP address resource.

  4. Create a backend service and add the two instance groups:
         
         gcloud compute backend-services create wsfc-backend \
           --load-balancing-scheme internal \
           --region $(gcloud config get-value compute/region) \
           --health-checks wsfc-healthcheck \
           --protocol tcp
         
         gcloud compute backend-services add-backend wsfc-backend \
           --instance-group wsfc-group-1 \
           --instance-group-zone $REGION-a \
           --region $REGION
         
         gcloud compute backend-services add-backend wsfc-backend \
           --instance-group wsfc-group-2 \
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
           --zone $REGION-a \
           --machine-type n2-standard-2 \
           --subnet $SUBNET_NAME \
           --image-family sql-ent-2019-win-2022 \
           --image-project windows-sql-cloud \
           --boot-disk-size 50 \
           --boot-disk-type pd-ssd
         

  3. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output sqlclient
         

Wait for a few minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

  4. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

  5. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and log in using the username and password created in the previous step.

  6. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

  7. Confirm the elevation prompt by clicking **Yes**.

  8. Join the computer to your Active Directory domain:
         
         Add-Computer -Domain DOMAIN
         

Replace `DOMAIN` with the DNS name of your Active Directory domain.

  9. Restart the computer:
         
         Restart-Computer
         

Wait for approximately 1 minute for the restart to complete.




### Run the test

Use the `sqlclient` VM to test that you can connect to the failover cluster and to verify that the failover works correctly:

  1. Connect to `sqlclient` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and log in using your domain user.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell**.
  3. Connect to the SQL Server cluster by using TCP/IP and the DNS name `sql` and query the `dm_os_cluster_nodes` table:
         
         & "$env:ProgramFiles\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE" `
            -S tcp:sql -E -Q "SELECT * FROM sys.dm_os_cluster_nodes"
         

The output should look like this:
         
         NodeName                       status      status_description is_current_owner
         ------------------------------ ----------- ------------------ ----------------
         NODE-1                                   0 up                                1
         NODE-2                                   0 up                                0
         
         (2 rows affected)
         

Notice that `node-1` is the current owner of the SQL Server failover cluster resource.

  4. Return to Cloud Shell and bring down the node-1 VM to test the failover scenario.
         
         gcloud compute instances stop node-1 --zone $REGION-a
         

  5. Repeat the query:
         
         & "$env:ProgramFiles\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE" `
            -S tcp:sql -E -Q "SELECT * FROM sys.dm_os_cluster_nodes"
         

The output should now look like this:
         
         NodeName                       status      status_description is_current_owner
         ------------------------------ ----------- ------------------ ----------------
         NODE-1                                   1 down                              0
         NODE-2                                   0 up                                1
         
         (2 rows affected)
         

Notice that despite the loss of `node-1`, the query succeeds, and shows that `node-2` is now the current owner of the failover cluster.




## Limitations

  * S2D is only supported for Windows Server 2016 and above.
  * With S2D, each disk only contains a partial view of the overall data. So taking a snapshot of a persistent disk won't be enough to back up your data. Use [native SQL backup](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases) instead.



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



## What's next

  * Learn how you can [configure a SQL Server failover cluster instance that uses persistent disks in multi-writer mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
