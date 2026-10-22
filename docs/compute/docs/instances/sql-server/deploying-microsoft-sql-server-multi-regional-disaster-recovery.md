---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/deploying-microsoft-sql-server-multi-regional-disaster-recovery/
title: Deploying Microsoft SQL Server for multi-regional disaster recovery \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:13.645166+00:00
---

# Deploying Microsoft SQL Server for multi-regional disaster recovery  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/deploying-microsoft-sql-server-multi-regional-disaster-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deploying Microsoft SQL Server for multi-regional disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to deploy and manage a Microsoft SQL Server database system across two Google Cloud regions as a disaster recovery (DR) solution and how to fail over from a failed database instance to a normally operating instance. For the purposes of this document, a _disaster_ is an event in which a primary database fails or becomes unavailable.

A primary database can fail when the region it's located in fails or becomes inaccessible. Even if a region is available and operating normally, a primary database can fail because of a system error. In these cases, disaster recovery is the process of making a secondary database available to clients for continued processing.

This tutorial is intended for database architects, administrators, and engineers.

## Objectives

  * Deploy a multi-regional disaster-recovery environment on Google Cloud by using Microsoft SQL Server's AlwaysOn Availability Groups.
  * Simulate a disaster event and perform a complete disaster-recovery process to validate the disaster-recovery configuration.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [SQL Server VMs](https://cloud.google.com/sql-server)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

For this tutorial, you need a Google Cloud project. You can create a new one, or select a project you already created:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




## Understanding disaster recovery

In Google Cloud, disaster recovery (DR) is about providing continuity of processing, especially when a region fails or becomes inaccessible. For systems such as a database management system, you implement DR by deploying the system in at least two regions. With this setup, the system continues to operate if one region becomes unavailable.

### Database system disaster recovery

The process of making a secondary database available when the primary database instance fails is called _database disaster recovery_ (or _database DR_). For a detailed discussion about this concept, see [Disaster recovery for Microsoft SQL Server](https://docs.cloud.google.com/solutions/disaster-recovery-for-microsoft-sql-server). Ideally, the state of the secondary database is consistent with the primary database at the point the primary becomes unavailable, or the secondary database is missing only a small set of recent transactions from the primary database.

### Disaster recovery architecture

For Microsoft SQL Server, the following diagram shows a minimal architecture that supports database DR.

![Primary and standby instances are located across two zones in region R1, and a secondary instance is located in region R2.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-standard.png)

**Figure 1.** Standard disaster recovery architecture with Microsoft SQL Server.

This architecture works as follows:

  * Two instances of Microsoft SQL Server (a primary instance and a standby instance) are located in the same region (R1) but different zones (zones A and B). The two instances in R1 coordinate their states by using the synchronous-commit mode. Synchronous mode is used because it supports high availability and maintains a consistent data state.
  * One instance of Microsoft SQL Server (the secondary or disaster recovery instance) is located in a second region (R2). For DR, the secondary instance in R2 synchronizes with the primary instance in R1 by using the asynchronous-commit mode. Asynchronous mode is used because of its performance (it doesn't slow down the commit processing in the primary instance).



In the preceding diagram, the architecture shows an availability group. The availability group, if used with a listener, provides the same connect string to clients if the clients are served by the following:

  * The primary instance
  * The standby instance (after a zone failure)
  * The secondary instance (after a region failure and after the secondary instance becomes the new primary instance)



In a variant of the above architecture, you deploy the two instances that are in the first region (R1) into the same zone. This approach might improve performance but is not highly available; a single zone outage might be required to initiate the DR process.

### Basic disaster recovery process

The DR process starts when a region becomes unavailable and the primary database fails over to resume processing in another operational region. The DR process prescribes the operational steps that must be taken, either manually or automatically, to mitigate the region failure and establish a running primary instance in an available region.

A basic database DR process consists of the following steps:

  1. The first region (R1), which is running the primary database instance, becomes unavailable.
  2. The operations team recognizes and formally acknowledges the disaster and decides whether a failover is required.
  3. If a failover is required, the secondary database instance in the second region (R2) is made the new primary instance.
  4. Clients resume processing on the new primary database and access the primary instance in R2.



Although this basic process establishes a working primary database again, it doesn't establish a complete DR architecture, where the new primary has a standby and a secondary database instance.

### Complete disaster recovery process

A complete DR process extends the basic DR process by adding steps to establish a complete DR architecture after a failover. The following diagram shows a complete database DR architecture.

![In a complete database DR architecture, the secondary instance in region R2 becomes the primary, and a new secondary instance is created in region R3.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-complete.png)

**Figure 2.** Disaster recovery with an unavailable primary region (R1).

This complete database DR architecture works as follows:

  1. The first region (R1), which is running the primary database instance, becomes unavailable.
  2. The operations team recognizes and formally acknowledges the disaster and decides whether a failover is required.
  3. If a failover is required, the secondary database instance in the second region (R2) is made the primary instance.
  4. Another secondary instance, the new standby instance, is created and started in R2 and added to the primary instance. The standby instance is in a different zone from the primary instance. The primary database now consists of two instances (primary and standby) that are highly available.
  5. In a third region (R3), a new secondary (standby) database instance is created and started. This secondary instance is asynchronously connected to the new primary instance in R2. At this point, the original disaster-recovery architecture is recreated and operational.



### Fallback to a recovered region

After the first region (R1) is brought back online, it can host the new secondary database. If R1 becomes available soon enough, you can implement step 5 in the complete recovery process in R1 instead of R3 (the third region). In this case, a third region is not needed.

The following diagram shows the architecture if R1 becomes available in time.

![If region R1 is recovered in time, secondary instances are created in region R1.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-fallback.png)

**Figure 3.** Disaster recovery after failed region R1 becomes available again.

In this architecture, the recovery steps are the same as those outlined earlier in Complete disaster recovery process, with the difference that R1 becomes the location for the secondary instances instead of R3.

## Choosing a SQL Server edition

This tutorial supports the following versions of Microsoft SQL Server:

  * SQL Server 2016 Enterprise Edition
  * SQL Server 2017 Enterprise Edition
  * SQL Server 2019 Enterprise Edition
  * SQL Server 2022 Enterprise Edition



The tutorial uses the AlwaysOn Availability Groups feature in SQL Server.

If you don't require a highly available (HA) Microsoft SQL Server primary database, and a single database instance suffices as your primary, you can use the following versions of SQL Server:

  * SQL Server 2016 Standard Edition
  * SQL Server 2017 Standard Edition
  * SQL Server 2019 Standard Edition
  * SQL Server 2022 Standard Edition



The 2016, 2017, 2019, and 2022 versions of SQL Server have Microsoft SQL Server Management Studio installed in the image; you don't need to install it separately. However, in a production environment, we recommend that you install one instance of Microsoft SQL Server Management Studio on a separate VM in each region. If you set up an HA environment, you should install Microsoft SQL Server Management Studio once for each zone to ensure that it remains available if another zone becomes unavailable.

## Setting up Microsoft SQL Server for multi-regional DR

This section uses the following images for Microsoft SQL Server:

  * `sql-ent-2016-win-2016` for Microsoft SQL Server 2016 Enterprise Edition
  * `sql-ent-2017-win-2016` for Microsoft SQL Server 2017 Enterprise Edition
  * `sql-ent-2019-win-2019` for Microsoft SQL Server 2019 Enterprise Edition
  * `sql-ent-2022-win-2022` for Microsoft SQL Server 2022 Enterprise Edition



For a complete list of images, see [Images](https://docs.cloud.google.com/compute/docs/images).

### Set up a two-instance high availability cluster

To set up a multi-regional database DR architecture for SQL Server, you first create a two-instance high availability (HA) cluster in a region. One instance serves as the primary, and the other instance serves as the secondary. To accomplish this step, follow the instructions in [Configuring SQL Server AlwaysOn Availability Groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability). This tutorial uses `us-central1` for the primary region (referred to as _R1_). Before you begin, review the following considerations:

  * If you followed the steps in [Configuring SQL Server AlwaysOn availability groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability), you will have created two SQL Server instances in the same region (`us-central1`). You will have deployed primary SQL Server instance (`node-1`) in `us-central1-a`, and a standby instance (`node-2`) in `us-central1-b`.

  * Although you implement the architecture in **Figure 4** for this tutorial, it's a best practice to set up a domain controller in more than one zone. This approach ensures that you establish an HA and DR-enabled database architecture. For example, if an outage occurs in one zone, that zone doesn't become a single point of failure for your deployed architecture.




![Primary and standby instances in synchronous mode are in different zones in one region, and a secondary instance in asynchronous mode is in another region.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-two-instance-ha.png)

**Figure 4.** Standard disaster recovery architecture implemented in this tutorial.

### Add a secondary instance for disaster recovery

Next, you set up a third SQL Server instance (a secondary instance that is named `node-3`), and configure the network as follows:

  1. Create a [specialize script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the Windows Server Failover Cluster nodes. The script installs the necessary Windows feature and creates firewall rules for WSFC and SQL Server. It also formats the data disk and creates data and log folders for SQL Server:
         
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
         

  2. Initialize the following variables:
         
         VPC_NAME=VPC_NAME
         SUBNET_NAME=SUBNET_NAME
         REGION=us-east1
         PD_SIZE=200
         MACHINE_TYPE=n2-standard-8
         

Where:

     * `VPC_NAME`: name of your VPC
     * `SUBNET_NAME`: name of your subnet for the `us-east1` region
  3. Create a SQL Server instance:
         
         gcloud compute instances create node-3 \
         --zone $REGION-b \
         --machine-type $MACHINE_TYPE \
         --subnet $SUBNET_NAME \
         --image-family sql-ent-2022-win-2022 \
         --image-project windows-sql-cloud \
         --tags wsfc,wsfc-node \
         --boot-disk-size 50 \
         --boot-disk-type pd-ssd \
         --boot-disk-device-name "node-3" \
         --create-disk=name=node-3-datadisk,size=$PD_SIZE,type=pd-ssd,auto-delete=no \
         --metadata enable-wsfc=true \
         --metadata-from-file=sysprep-specialize-script-ps1=specialize-node.ps1
         

  4. Set a Windows password for the new SQL Server instance:

     1. In the Google Cloud console, go to the Compute Engine page.

[Go to Compute Engine](https://console.cloud.google.com/compute)

     2. In the **Connect** column for the Compute Engine cluster `node-3`, select the **Set windows password** drop-down list.

     3. Set the username and password. Note them for later use.

  5. Click **RDP** to connect to the `node-3` instance.

  6. Enter the username and password from the previous step, and then click **OK**.

  7. Add the instance to the Windows domain:

     1. Right-click the Start button (or press Win+X) and click Windows PowerShell (Admin).

     2. Confirm the elevation prompt by clicking Yes.

     3. Join the computer to your Active Directory domain and restart:
            
            Add-Computer -Domain DOMAIN -Restart
            

Replace `DOMAIN` with the DNS name of your Active Directory domain.

Wait for approximately 1 minute for the restart to complete.




### Add the secondary instance to the failover cluster

Next, you add the secondary instance (`node-3`) to the Windows failover cluster:

  1. Connect to the `node-1` or `node-2` instances using RDP, and sign in as an Administrator user.

  2. Open a PowerShell window as an Administrator user and set variables for the cluster environment in this tutorial:
         
         $node3 = "node-3"
         $nameWSFC = "SQLSRV_CLUSTER" # Name of cluster 
         

Replace `SQLSRV_CLUSTER` with the name of the SQL Server cluster.

  3. Add the secondary instance to the cluster:
         
         Get-Cluster | WHERE Name -EQ $nameWSFC | Add-ClusterNode -NoStorage -Name $node3
         

This command might take a while to run. Because the process can stop responding and not return automatically, occasionally press `Enter`.

  4. In the node, enable the AlwaysOn high availability feature:
         
         Enable-SqlAlwaysOn -ServerInstance $node3 -Force
         




The node is now a part of the failover cluster.

### Add the secondary instance to the existing availability group

Next, add the SQL Server instance (the secondary instance) and database to the availability group:

  1. Connect to `node-3` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.

  2. Open **SQL Server Configuration Manager**.

  3. In the navigation pane, select **SQL Server Services**

  4. In the list of services, right-click **SQL Server (MSSQLSERVER)** and select **Properties**.

  5. Under **Log on as** , change the account:

     * **Account name** : `DOMAIN\sql_server` where `DOMAIN` is the NetBIOS name of your Active Directory domain.
     * **Password** : Enter the password you chose previously for the sql_server domain account.
  6. Click **OK**.

  7. When prompted to restart SQL Server, select **Yes**.

  8. In any of the three instance nodes `node-1`, `node-2`, or `node-3`, open Microsoft SQL Server Management Studio and connect to the primary instance—`node-1`.

     1. Go to the Object Explorer.
     2. Select the **Connect** drop-down list.
     3. Select **Database Engine**.
     4. From the **Server Name** drop-down list, select **`node-1`**. If the cluster is not listed, enter it in the field.
  9. Click **New Query**.

**Note:** Steps 9 and 10 are not necessary if a distributed network name was used to set up your AlwaysOn availability group.
  10. Paste the following command to add an IP address to the listener that is used for the node, and then click **Execute** :
         
         ALTER AVAILABILITY GROUP [bookshelf-ag] MODIFY LISTENER 'bookshelf' (ADD IP ('LOAD_BALANCER_IP_ADDRESS', '255.255.255.0'))
         

Replace `LOAD_BALANCER_IP_ADDRESS` with the IP Address of the load balancer in the `us-east1` region.

  11. In the Object Explorer, expand the **AlwaysOn High Availability** node, and then expand the **Availability Groups** node.

  12. Right-click the availability group that is named **`bookshelf-ag`** , and then select **Add Replica**.

  13. On the **Introduction** page, click the **AlwaysOn High Availability** node, and then click the **Availability Groups** node.

  14. On the **Connect to Replicas** page, click **Connect** to connect to the existing secondary replica **`node-2`**.

  15. On the **Specify Replicas** page, click **Add Replica** , and then add the new node **`node-3`**. Don't select **Automatic Failover** because automatic failover causes a synchronous commit. Such a setup crosses regional boundaries, which we don't recommend.

  16. On the **Select Data Synchronization** page, select **Automatic seeding**.

Because there is no listener, the **Validation** page generates a warning, which you can ignore.

  17. Complete the wizard steps.




The failover mode for `node-1` and `node-2` is automatic, whereas it's manual for `node-3`. This difference is one way to distinguish high availability from disaster recovery.

The availability group is now ready. You configured two nodes for high availability and a third node for disaster recovery.

## Simulating a disaster recovery

In this section, you test the disaster recovery architecture for this tutorial and consider optional DR implementations.

### Simulate an outage and execute a DR failover

  1. Simulate a failure or outage in the primary region:

     1. In Microsoft SQL Server Management Studio on `node-1`, connect to `node-1`.

     2. Create a table. After you add replicas in later steps, you verify the replica works by checking whether this table is present.
            
            USE bookshelf
            GO
            CREATE TABLE dbo.TestTable_Before_DR (ID INT NOT NULL)
            GO
            

     3. In Cloud Shell, shut down both servers in the primary region `us-central1`:
            
            gcloud compute instances stop node-2 --zone us-central1-b --quiet
            gcloud compute instances stop node-1 --zone us-central1-a --quiet
            

**Note:** An alternative way of creating a failure is to stop the VMs that run `node-1` and `node-2`. This approach simulates a hard failure instead of an ordinary instance shutdown.
  2. In Microsoft SQL Server Management Studio on `node-3`, connect to `node-3`.

  3. Execute a failover, and set the availability mode to synchronous-commit. Forcing a failover is necessary because the node is in asynchronous-commit mode.
         
         ALTER AVAILABILITY GROUP [bookshelf-ag] FORCE_FAILOVER_ALLOW_DATA_LOSS
         GO
         ALTER AVAILABILITY GROUP [bookshelf-ag]
         MODIFY REPLICA ON 'node-3' WITH (AVAILABILITY_MODE = SYNCHRONOUS_COMMIT)
         GO
         

You can resume processing; `node-3` is now the primary instance.

  4. (Optional) Create a new table in `node-3`. After you synchronize the replicas with the new primary, check whether this table is replicated to the replicas.
         
         USE bookshelf
         GO
         CREATE TABLE dbo.TestTable_After_DR (ID INT NOT NULL)
         GO
         




Although `node-3` is the primary at this point, you might want to fall back to the original region or set up a new secondary instance and standby instance in order to recreate a complete DR architecture again. The next section discusses these options.

### (Optional) Recreate a DR architecture that completely replicates transactions

This use case addresses a failure in which all transactions are replicated from the primary to the secondary database before the primary fails. In this ideal scenario, no data is lost; the state of the secondary is consistent with the primary at the point of failure.

In this scenario, you can recreate a complete DR architecture in two ways:

  * Fall back to the original primary and the original standby (if those are available).
  * Create a new standby and secondary for `node-3` in case the original primary and standby are unavailable.



#### Approach 1: Fall back to the original primary and standby

  1. In the Cloud Shell, start up the original (old) primary and standby:
         
         gcloud compute instances start node-1 --zone us-central1-a --quiet
         gcloud compute instances start node-2 --zone us-central1-b --quiet
         

  2. In Microsoft SQL Server Management Studio, add `node-1` and `node-2` back as secondary replicas:

     1. On `node-3`, add the two servers in asynchronous-commit mode:
            
            USE [master]
            GO
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-1' WITH (FAILOVER_MODE = MANUAL)
            GO
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-1' WITH (AVAILABILITY_MODE = ASYNCHRONOUS_COMMIT)
            GO
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-2' WITH (FAILOVER_MODE = MANUAL)
            GO
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-2' WITH (AVAILABILITY_MODE = ASYNCHRONOUS_COMMIT)
            GO
            

     2. On `node-1`, start synchronizing the databases again:
            
            USE [master]
            GO
            ALTER DATABASE [bookshelf] SET HADR RESUME;
            GO
            

     3. On `node-2`, start synchronizing the databases again:
            
            USE [master]
            GO
            ALTER DATABASE [bookshelf] SET HADR RESUME;
            GO
            

  3. Make `node-1` the primary again:

     1. On `node-3`, change the availability mode of `node-1` to synchronous-commit. The instance `node-1` becomes the primary again.
            
            USE [master]
            GO
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-1' WITH (AVAILABILITY_MODE = SYNCHRONOUS_COMMIT)
            GO
            

     2. On `node-1`, change `node-1` to be the primary and the two other nodes to be the secondaries:
            
            USE [master]
            GO
            -- Node 1 becomes primary
            ALTER AVAILABILITY GROUP [bookshelf-ag] FORCE_FAILOVER_ALLOW_DATA_LOSS;
            GO
            
            -- Node 2 has synchronous commit
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-2' WITH (AVAILABILITY_MODE = SYNCHRONOUS_COMMIT)
            GO
            
            -- Node 3 has asynchronous commit
            ALTER AVAILABILITY GROUP [bookshelf-ag]
            MODIFY REPLICA ON 'node-3' WITH (AVAILABILITY_MODE = ASYNCHRONOUS_COMMIT)
            GO
            




After all commands succeed, `node-1` is the primary, and the other nodes are secondary, as shown in the following diagram.

![The Object Explorer shows the availability groups.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-clusters-replicas.png)

#### Approach 2: Set up a new primary and standby

It is possible that you cannot recover the original primary and standby instances from the failure, or it takes too long to recover them, or the region is inaccessible. One approach is to keep `node-3` as the primary and then create a new standby and a new secondary instance, as shown in the following diagram.

![The standby instance is created in a separate zone but the same region as the primary, and a secondary instance is created in a separate region.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-new-primary-standby.png)

**Figure 5.** Disaster recovery with unavailable original primary region R1.

This implementation requires you to do the following:

  * Keep `node-3` as the primary in `us-east1`.

  * Add a new standby instance (`node-4`) in a different zone in `us-east1`. This step establishes the new deployment as highly available.

  * Create a new secondary instance (`node-5`) in a separate region, for example, `us-west2`. This step sets up the new deployment for disaster recovery. The overall deployment is now completed. The database architecture fully supports HA and DR.




### (Optional) Execute a fallback when transactions are missing

A less-than-ideal failure is when one or more transactions committed on the primary are not replicated to the secondary at the point of failure (also known as a _hard failure_). In a failover, all committed transactions that are not replicated are lost.

To test failover steps for this scenario, you need to generate a hard failure. The best approach for generating a hard failure is the following:

  * Change the network so that there is no connectivity between the primary and the secondary instances.
  * Change the primary in some way—for example, add a table or insert some data.
  * Step through the failover process as outlined earlier so that the secondary becomes the new primary.



The steps for the failover process are identical to the ideal scenario, except that the table added to the primary after network connectivity is interrupted isn't visible in the secondary.

Your only option for dealing with a hard failure is to remove the replicas (`node-1` and `node-2`) from the availability group and synchronize the replicas again. The synchronization changes their state to match the secondary. Any transaction that was not replicated before the failure is lost.

To add `node-1` as a secondary instance, you can follow the same steps for adding `node-3` earlier (see Add the secondary instance to the failover cluster earlier) with the following difference: `node-3` is now the primary, not `node-1`. You need to replace any instance of `node-3` with the name of the server you add to the availability group. If you re-use the same VM (`node-1` and `node-2`), you don't need to add the server to the Windows Server Failover Cluster; only add the SQL Server instance back to the availability group.

At this point, `node-3` is the primary, and `node-1` and `node-2` are secondaries. It's now possible to fall back to `node-1`, to make `node-2` the standby, and to make `node-3` the secondary. The system now has the same state it had before the failure.

## Automatic failover

Automatically failing over to a secondary instance as the primary can create problems. After the original primary becomes available again, a split-brain situation can occur if some clients access the secondary while others write to the restored primary. In this case, the primary and the secondary are possibly updated in parallel, and their states diverge. To avoid this situation, this tutorial provides [instructions](https://docs.cloud.google.com/compute/docs/instances/sql-server/deploying-microsoft-sql-server-multi-regional-disaster-recovery#dr-replicate-transactions) for a manual failover in which you decide whether (or when) to fail over.

If you implement an automatic failover, you must ensure that only one of the configured instances is the primary and can be modified. Any standby or secondary instance must not provide write access to any client (except the primary for state replication). Furthermore, you must avoid a rapid chain of subsequent failovers in a short time. For example, a failover every five minutes would not be a dependable disaster recovery strategy. For automated failover processes, you can build in safeguards against problematic scenarios such as these, and even involve a database administrator for complex decisions, if necessary.

## Alternative deployment architecture

This tutorial sets up a disaster recovery architecture with a secondary instance that becomes the primary instance in a failover, as shown in the following diagram.

![Primary and standby instances in synchronous mode are in different zones in one region, and a secondary instance in asynchronous mode is in another region.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-two-instance-ha-2.png)

**Figure 6.** Standard disaster recovery architecture using Microsoft SQL Server.

This means that in case of a failover, the resulting deployment has a single instance until a fallback is possible, or until you configure a standby (for HA) and a secondary (for DR).

An alternative deployment architecture is to configure two secondary instances. Both instances are replicas of the primary. If a failover occurs, you can reconfigure one of the secondaries as a standby. The following diagrams show the deployment architecture before and after a failover.

![The two secondary instances are located in separate zones in region R2.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-complete-alternative-1.png)

**Figure 7.** Standard disaster recovery architecture with two secondary instances.

![After the failover, one of the secondary instances in region R2 becomes a standby instance.](https://docs.cloud.google.com/static/compute/images/deploying-microsoft-sql-server-multi-regional-disaster-recovery-complete-alternative-2.png)

**Figure 8.** Standard disaster recovery architecture with two secondary instances after failover.

While you must still make one of the two secondaries a standby (Figure 8), this process is a lot faster than creating and configuring a new standby from scratch.

You can also address DR with a setup that is analogous to this architecture of using two secondary instances. In addition to having two secondaries in a second region (Figure 7), you can deploy another two secondaries in a third region. This setup lets you efficiently create an HA and DR-enabled deployment architecture after a primary region failure.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial:

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
