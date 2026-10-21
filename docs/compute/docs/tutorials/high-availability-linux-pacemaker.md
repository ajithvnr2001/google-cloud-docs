---
url: https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker/
title: Set up a SQL Server cluster on Linux with Always On availability groups and Pacemaker \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:05.611403+00:00
---

# Set up a SQL Server cluster on Linux with Always On availability groups and Pacemaker  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set up a SQL Server cluster on Linux with Always On availability groups and Pacemaker Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to deploy a Microsoft SQL Server database system on Linux using an Always On availability group (AOAG) and Pacemaker as a high-availability (HA) and disaster recovery (DR) solution. For the purposes of this document, a disaster is an event in which a primary database fails or becomes unavailable.

A primary database can fail when the region it's located in fails or becomes inaccessible. Even if a region is available and operating normally, a primary database can fail because of a system error. In these cases, disaster recovery is the process of making a secondary database available to clients for continued processing.

This tutorial is intended for database architects, administrators, and engineers.

## Objectives

  * [Deploy SQL Server on Linux](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#install_and_configure_sql_server)
  * [Create an Always On availability group](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#enable_always_on_availability_group) for high-availability and disaster recovery
  * [Install and configure Pacemaker](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#install_and_configure_pacemaker) to manage failover of the SQL Server cluster
  * [Configure a load balancer](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#set_up_load_balancer_and_availability_group_listener) to route traffic to your availability group with SQL Server
  * [Setup a STONITH (Shoot The Other Node In The Head) fence](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#setup-stonith-fence) to ensure HA integrity
  * [Perform a failover test](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#test_failover) to ensure SQL Server cluster is working as expected



## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



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

  3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




## Prepare the project and network

To prepare your Google Cloud project and VPC for the deployment of SQL Server Always On availability groups, do the following:

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Set your default [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  3. Set your default region:
         
         gcloud config set compute/region REGION
         

Replace `REGION` with the ID of the region you want to deploy in.

  4. Set your default zone:
         
         gcloud config set compute/zone ZONE
         

Replace `ZONE` with the ID of the zone you want to deploy in. It should be a valid zone in the region specified in the previous step.




## Create Linux VMs

To achieve HA and quorum for the SQL Server cluster deploy three Linux virtual machines (VMs) to host the SQL Server cluster.

  1. Initialize the following variables:
         
         PD_SIZE=30
         MACHINE_TYPE=n2-standard-8
         

  2. Create the Linux VMs:
         
         gcloud compute instances create node-1 \
         --project=PROJECT_ID \
         --zone REGION-a \
         --machine-type $MACHINE_TYPE \
         --subnet SUBNET_NAME \
         --create-disk=auto-delete=yes,boot=yes,device-name=node-1,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20240426,mode=rw,size=$PD_SIZE,type=projects/PROJECT_ID/zones/REGION-a/diskTypes/pd-balanced \
         --scopes=https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/devstorage.read_write
         
         gcloud compute instances create node-2 \
         --project=PROJECT_ID \
         --zone REGION-b \
         --machine-type $MACHINE_TYPE \
         --subnet SUBNET_NAME \
         --create-disk=auto-delete=yes,boot=yes,device-name=node-2,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20240426,mode=rw,size=$PD_SIZE,type=projects/PROJECT_ID/zones/REGION-b/diskTypes/pd-balanced \
         --scopes=https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/devstorage.read_write
         
         gcloud compute instances create node-3 \
         --project=PROJECT_ID \
         --zone REGION-c \
         --machine-type $MACHINE_TYPE \
         --subnet SUBNET_NAME \
         --create-disk=auto-delete=yes,boot=yes,device-name=node-3,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20240426,mode=rw,size=$PD_SIZE,type=projects/PROJECT_ID/zones/REGION-c/diskTypes/pd-balanced \
         --scopes=https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/devstorage.read_write
         

Replace `SUBNET_NAME` with the name of your VPC subnet.

  3. Update the hosts file on `node-1`, `node-2`, and `node-3`:

**Note:** For production use, the domain resolution should be managed by a dedicated Domain Name System (DNS) server.
     1. Connect to each of your VMs using SSH. Refer to the Connect to Linux VMs [documentation](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) for more information.
     2. Open the hosts file for edit.
            
            sudo vi /etc/hosts
            

     3. Find the internal IP address for each Linux VM and append the host entries to the bottom of the file.

[Go to Compute Engine](https://console.cloud.google.com/compute)
            
            NODE1_INTERNAL_IP node-1
            NODE2_INTERNAL_IP node-2
            NODE3_INTERNAL_IP node-3
            

Replace `NODE1_INTERNAL_IP`, `NODE2_INTERNAL_IP` and `NODE3_INTERNAL_IP` with the internal IP address of each Linux VM.

  4. Check the communication between your VMs. All VMs that participate in the Always On availability group must be able to communicate with other VMs:

     1. Return to each Linux VM, run the commands from each VM, and verify that all VMs can communicate with each other.
            
            ping -c 4 node-1
            ping -c 4 node-2
            ping -c 4 node-3
            




## Install and configure SQL Server

Download, install and configure the SQL Server engine on the three Linux VMs that will participate in the Always On availability group.

  1. SSH to `node-1`, `node-2`, and `node-3` and run the following steps:

     1. Import the public repository keys.
            
            wget -qO- https://packages.microsoft.com/keys/microsoft.asc \
            | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
            

     2. Register the SQL Server Ubuntu repository.
            
            sudo add-apt-repository \
            "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"
            

     3. Update the package index files and install SQL Server.
            
            sudo apt-get update
            sudo apt-get install -y mssql-server
            
            

  2. Configure SQL Server:

     1. Run the mssql-conf tool.
            
            sudo /opt/mssql/bin/mssql-conf setup
            

     2. Choose **Developer** edition for the SQL Server edition and accept the license agreement.

The developer edition has all the enterprise features included, but you can use it only for non-production environments. More information is available regarding [SQL Server editions](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver16#sql-server-editions) and [Microsoft licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing).

**Note:** For each VM instance a SQL Server license is required. If you are running Microsoft application servers, License Mobility through Software Assurance helps you transition to Google Cloud. For more information, see [Using License Mobility with Microsoft server applications](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#license-mobility). If you are not bringing your own license and require to purchase a license through Google (PAYG), follow the steps in [Add a SQL Server license to a boot disk](https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license) to ensure you purchase a license for each VM instance.
     3. Specify a password for the SA account.

     4. Verify that the `mssql-server` service is running.
            
            systemctl status mssql-server --no-pager
            

  3. If you have a firewall enabled on your VMs, open the firewall for SQL Server:

     1. Check if `Uncomplicated Firewall` is installed and enabled by running the following command.
            
            sudo ufw status
            

     2. If the status is active, run the following commands to open the ports.
            
            sudo ufw allow 1433
            sudo ufw allow 5022
            sudo ufw reload
            

**Note:** If you are using other ports for SQL Server or for your availability group endpoint, change the firewalls rules accordingly.



### Connect to SQL Server

At this point, SQL Server is installed. To connect to it, create a windows machine in the same VPC, install SQL Server management Studio (SSMS) to connect to your newly created SQL Server instance on your VMs:

  1. Create a Windows VM:

     1. Return to your [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) and run the following command.
            
            gcloud compute instances create node4 \
            --project=PROJECT_ID \
            --zone ZONE \
            --subnet SUBNET_NAME \
            --machine-type=n2-standard-4 \
            --create-disk=auto-delete=yes,boot=yes,device-name=node4,image=projects/windows-cloud/global/images/windows-server-2022-dc-v20240415,mode=rw,size=50,type=projects/p3rf-sqlserver/zones/ZONE/diskTypes/pd-balanced
            

  2. Connect to the Windows VM on `node-4` using Remote Desktop:

  3. Update the hosts file on `node-4`:

     1. Open notepad in administrator mode.
     2. Click **File** > **Open** and open the hosts file.
            
            c:\Windows\System32\drivers\etc\hosts
            

     3. Append the host entries to the bottom of the file.
            
            NODE1_INTERNAL_IP node-1
            NODE2_INTERNAL_IP node-2
            NODE3_INTERNAL_IP node-3
            

Replace `NODE1_INTERNAL_IP`, `NODE2_INTERNAL_IP`, and `NODE3_INTERNAL_IP` with the respective internal IP address of each VM.

     4. Save and exit.

  4. Verify connectivitiy to the Linux VMs:

     1. Connect to the Windows VM on `node-4`
     2. Click the **Start** button, and enter powershell into the search bar.
     3. Click to open the Windows PowerShell ISE app.
     4. Tests connectivity by executing the following commands.
            
            ping node-1
            ping node-2
            ping node-3
            

  5. Install [Microsoft SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) (SSMS) with the following steps:

     1. Connect to the Windows VM on `node-4` using Remote Desktop.

     2. In your RDP session, minimize all windows, and start the Windows PowerShell ISE app.

     3. At the PowerShell prompt, download and execute the SSMS installer.
            
            Start-BitsTransfer `
            -Source "https://aka.ms/ssmsfullsetup" `
            -Destination "$env:Temp\ssms-setup.exe"
            & $env:Temp\ssms-setup.exe
            

     4. In the SSMS installer, click **Install**.

     5. Accept the prompt to allow changes to be made.

     6. When the installation is finished, click **Restart** to restart the remote machine. This closes the RDP session.

  6. Connect to the SQL Server instance on node-1:

     1. Return to `node-4` VM using RDP.

     2. Open SSMS and connect to `node-1` using the following parameters.
            
            Server name: node-1
            Authentication: SQL Server Authentication
            Login: sa
            

For more information refer to [connecting to a SQL Server instance](https://learn.microsoft.com/en-us/sql/ssms/quickstarts/ssms-connect-query-sql-server?view=sql-server-ver16) using [SQL Server Management Studio documentation](https://learn.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver16).

     3. Enter the password for the SA account created during installation.

     4. Select **Trust server certificate**.

     5. Click **Connect**.




## Enable Always On availability group

On Linux, you must first create an availability group before you can add it as a resource to be managed by Pacemaker:

  1. Enable the Always On availability group feature for each SQL Server instance participating in the availability group. Run the following commands on `node-1`, `node-2`, and `node-3`:

**Note:** Restart the `mssql-server` service for the changes to take effect.
         
         sudo /opt/mssql/bin/mssql-conf set hadr.hadrenabled 1
         sudo systemctl restart mssql-server
         

  2. Connect to the instance that is the primary host in the availability group using SSMS:

**Tip:** We recommend choosing `node-1` as the primary host.
     1. Open a new query window.

     2. Run the following code snippet to create an encryption key, certificate, and private key.

**Tip:** Choose strong passwords for the encryption key and the private key. Remember these passwords as you will use them later.**Note:** The password must be at least 8 characters long and contain characters from three of the following four sets: uppercase letters, lowercase letters, base 10 digits, and symbols.
            
            USE MASTER;
            
            CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'ENCRYPTION_KEY_PASSWORD';
            CREATE CERTIFICATE my_ag_certificate WITH SUBJECT = 'my_ag_cert';
            BACKUP CERTIFICATE my_ag_certificate
            TO FILE = '/var/opt/mssql/data/my_ag_certificate.cer'
            WITH PRIVATE KEY (
                FILE = '/var/opt/mssql/data/my_ag_certificate.pvk',
                ENCRYPTION BY PASSWORD = 'PRIVATE_KEY_PASSWORD'
            );
            

Replace `ENCRYPTION_KEY_PASSWORD` and `PRIVATE_KEY_PASSWORD` with the passwords for the encryption key and private key.




### Transfer the certificate and key files

The certificate and key files created in the previous steps need to be moved to the secondary nodes of SQL Server. There are several methods to move the certificate and key files to the secondary nodes on `node-2` and `node-3`.

For other transfer options, see [Transfer files to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files)

#### Transfer the certificate and key files using Cloud Storage

Create a Cloud Storage to transfer files from the primary to the secondary cluster nodes.

  1. Create a Cloud Storage bucket:

     1. Return to your [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell), run the following command:
            
            gcloud storage buckets create gs://BUCKET_NAME \
            --project=PROJECT_ID \
            --location=REGION \
            --public-access-prevention
            

Replace `BUCKET_NAME` with the name of the bucket to create. Replace `PROJECT_ID` with the ID of your Google Cloud project and replace `REGION` with the ID of the region you want the bucket deployed.

For more information, see [Create Buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

  2. Return to SSh on `node-1`, `node-2`, and `node-3` to initialize Google Cloud CLI:

     1. Run the following command to initialize Google Cloud CLI.
            
            gcloud init
            

     2. Choose `option [1]` to use the preinstalled service account.

     3. Enter the name of your project.

     4. Enter `n` to the question to set up the default Region and Zone.

  3. Return to `node-1` to copy the files to Cloud Storage:

     1. Upload the two newly created files to your Cloud Storage by un the following commands.
            
            sudo gcloud storage cp /var/opt/mssql/data/my_ag_certificate.cer gs://BUCKET_NAME/
            sudo gcloud storage cp /var/opt/mssql/data/my_ag_certificate.pvk gs://BUCKET_NAME/
            

Replace `BUCKET_NAME` with the name of the bucket created.

  4. Return to `node-2` and `node-3` to copy the files from the Cloud Storage:

     1. Download the two files from your Cloud Storage to `node-2`.
            
            sudo gcloud storage cp gs://BUCKET_NAME/my_ag_certificate.cer /var/opt/mssql/data/
            sudo gcloud storage cp gs://BUCKET_NAME/my_ag_certificate.pvk /var/opt/mssql/data/
            

Replace `BUCKET_NAME` with the name of the bucket created.

     2. Change the ownership of the files on `node-2` and `node-3` by running the command in a root shell.
            
            chown mssql:mssql /var/opt/mssql/data/my_ag_certificate.*
            chmod 660 /var/opt/mssql/data/my_ag_certificate.*
            
            

**Tip:** Remember to exit the root shell after running the commands.



### Set up database mirroring endpoint

In this section you will create the database endpoint using an encryption key and certificate shared by each node in the SQL Server cluster to ensure secure data replication.

  1. Return to the Windows VM on `node-4` to create the database mirroring endpoints:

     1. Connect to the SQL Server databases on `node-1`, `node-2`, and `node-3` using SSMS. Follow the steps from [Connect to SQL Server](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker#connect_to_sql_server) using `node-1`, `node-2`, and `node-3` as the Server name and the respective passwords you set for the SA account.

     2. Create the certificate on the secondary VMs `node-2` and `node-3` from the copied files. Use the passwords you provided when you created the certificate and key on the primary node.
            
            USE MASTER;
            
            CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'ENCRYPTION_KEY_PASSWORD';
            CREATE CERTIFICATE my_ag_certificate
            FROM FILE = '/var/opt/mssql/data/my_ag_certificate.cer'
            WITH PRIVATE KEY (
                FILE = '/var/opt/mssql/data/my_ag_certificate.pvk',
                DECRYPTION BY PASSWORD = 'PRIVATE_KEY_PASSWORD'
            );
            

Replace `ENCRYPTION_KEY_PASSWORD` and `PRIVATE_KEY_PASSWORD` with the passwords for the encryption key and private key.

     3. Return to SSMS to create database mirroring endpoints by running the T-SQL command for `node-1`, `node-2`, and `node-3`.

**Tip:** The default listening port is 5022, but you can use any other available ports.
            
            CREATE ENDPOINT [my_ag_endpoint]
                AS TCP (LISTENER_PORT = 5022)
                FOR DATABASE_MIRRORING (
                    ROLE = ALL,
                    AUTHENTICATION = CERTIFICATE my_ag_certificate,
                    ENCRYPTION = REQUIRED ALGORITHM AES
                );
            
            ALTER ENDPOINT [my_ag_endpoint] STATE = STARTED;
            




### Create and configure the Always On availability group

Next, create the SQL Server Always On availability group using SQL Server Management Studio and use the previously created endpoints for replication.

**Note:** A database for replication is necessary to create an Always On availability group. In this tutorial you will create a dummy database named bookshelf. Once the AOAG is created additional databases can be added or removed from the availability group.

  1. Return to the Windows VM and open SSMS:

     1. Connect to the SQL Server database engine on `node-1` and open a new query windows.
  2. Create a database and backup the database in preparation for replication:
         
         USE MASTER;
         
         CREATE DATABASE [bookshelf];
         ALTER DATABASE [bookshelf] SET RECOVERY FULL;
         BACKUP DATABASE [bookshelf]
         TO DISK = N'/var/opt/mssql/data/bookshelf.bak';
         

  3. Create the Always On availability group:

     1. Run the following T-SQL command in SSMS on `node-1`, `node-2`, and `node-3`. This will ensure that the endpoints are enabled and SQL Server on each node is ready for data replication.
            
            IF (SELECT state FROM sys.endpoints WHERE name = N'my_ag_endpoint') <> 0
            BEGIN
                ALTER ENDPOINT [my_ag_endpoint] STATE = STARTED
            END
            GO
            
            IF EXISTS(SELECT * FROM sys.server_event_sessions WHERE name='AlwaysOn_health')
            BEGIN
                ALTER EVENT SESSION [AlwaysOn_health] ON SERVER WITH (STARTUP_STATE=ON);
            END
            IF NOT EXISTS(SELECT * FROM sys.dm_xe_sessions WHERE name='AlwaysOn_health')
            BEGIN
                ALTER EVENT SESSION [AlwaysOn_health] ON SERVER STATE=START;
            END
            GO
            

     2. Run the following T-SQL command on `node-1` to create the AOAG.
            
            USE [master]
            GO
            
            CREATE AVAILABILITY GROUP [aoag1]
            WITH (
                AUTOMATED_BACKUP_PREFERENCE = SECONDARY,
                DB_FAILOVER = OFF,
                DTC_SUPPORT = NONE,
                CLUSTER_TYPE = EXTERNAL,
                REQUIRED_SYNCHRONIZED_SECONDARIES_TO_COMMIT = 0
            )
            FOR DATABASE [bookshelf]
            REPLICA ON N'node-1' WITH (
                ENDPOINT_URL = N'TCP://node-1:5022', FAILOVER_MODE = EXTERNAL, AVAILABILITY_MODE = SYNCHRONOUS_COMMIT, BACKUP_PRIORITY = 50, SEEDING_MODE = AUTOMATIC, SECONDARY_ROLE(ALLOW_CONNECTIONS = NO)),
                N'node-2' WITH (ENDPOINT_URL = N'TCP://node-2:5022', FAILOVER_MODE = EXTERNAL, AVAILABILITY_MODE = SYNCHRONOUS_COMMIT, BACKUP_PRIORITY = 50, SEEDING_MODE = AUTOMATIC, SECONDARY_ROLE(ALLOW_CONNECTIONS = NO)),
                N'node-3' WITH (ENDPOINT_URL = N'TCP://node-3:5022', FAILOVER_MODE = EXTERNAL, AVAILABILITY_MODE = SYNCHRONOUS_COMMIT, BACKUP_PRIORITY = 50, SEEDING_MODE = AUTOMATIC, SECONDARY_ROLE(ALLOW_CONNECTIONS = NO)
            );
            GO
            

     3. Run the following T-SQL command on `node-2` and `node-3` for each SQL Server instance to join the new availability group.
            
            ALTER AVAILABILITY GROUP [aoag1] JOIN WITH (CLUSTER_TYPE = EXTERNAL);
            GO
            
            ALTER AVAILABILITY GROUP [aoag1] GRANT CREATE ANY DATABASE;
            GO
            

You have created a new database named **bookshelf** and added the new database to a new availability group named **aoag1** on SQL Server instance running on `node-1`. `Node-2` and `node-3` were added to the availability group and the data in the **bookshelf** database will be synchronously replicated across the SQL Server instances across all three nodes.




## Install and configure Pacemaker

[Pacemaker](https://clusterlabs.org/pacemaker/) is an open-source high availability resource manager software, used with the [Corosync](https://corosync.github.io/corosync/) Cluster engine. In this section you install and configure Pacemaker on each of your VMs.

### Create a SQL Server login for the pacemaker cluster manager

In this section you will create a new SQL Server account for Pacemaker to use to log into each SQL Server instance and manage the availability group.

  1. Run the following T-SQL command on `node-1`, `node-2`, and `node-3`:
         
         USE [master];
         
         CREATE LOGIN [pacemaker] with PASSWORD= N'PACEMAKER_LOGIN_PASSWORD';
         GO
         

Replace `PACEMAKER_LOGIN_PASSWORD` with a password for the pacemaker account.

  2. Run the T-SQL command to grant the pacemaker login permissions to the availability group:
         
         GRANT ALTER, CONTROL, VIEW DEFINITION ON AVAILABILITY GROUP::[aoag1] TO [pacemaker];
         GRANT VIEW SERVER STATE TO [pacemaker];
         GO
         

  3. Return to SSH on `node-1`, `node-2`, and `node-3` to run the commands to save the Pacemaker login and password in the SQL Server secrets folder:
         
         echo 'pacemaker' >> ~/pacemaker-passwd
         echo 'PACEMAKER_LOGIN_PASSWORD' >> ~/pacemaker-passwd
         sudo mv ~/pacemaker-passwd /var/opt/mssql/secrets/passwd
         sudo chown root:root /var/opt/mssql/secrets/passwd
         sudo chmod 400 /var/opt/mssql/secrets/passwd
         

Replace `PACEMAKER_LOGIN_PASSWORD` with the password for the pacemaker account.




### Install Pacemaker

Next, install Pacemaker and set up a logon account on all Linux VMs for resource management.

  1. Open firewall ports for pacemaker:

     1. Check if `Uncomplicated Firewall` is installed and enabled by running the following command on `node-1`, `node-2`, and `node-3`.
            
            sudo ufw status
            

     2. If the ufw is enabled, open the firewall ports on `node-1`, `node-2`, and `node-3`.
            
            sudo ufw allow 2224/tcp
            sudo ufw allow 3121/tcp
            sudo ufw allow 5405/udp
            sudo ufw allow 21064/tcp
            sudo ufw allow 1433/tcp
            sudo ufw allow 5022/tcp
            sudo ufw reload
            

**Note:** If you are using other ports for SQL Server or for your availability group endpoint, change the firewalls rules accordingly
  2. Install Pacemaker on `node-1`, `node-2`, and `node-3`:
         
         sudo apt-get install -y pacemaker pacemaker-cli-utils crmsh resource-agents  fence-agents corosync python3-azure pcs
         

  3. Set a new password for the `hacluster` user on `node-1`, `node-2`, and `node-3`:

**Note:** Set the same password on all three nodes. This password will be needed for the during the rest of the setup.
         
         sudo passwd hacluster
         




### Set up Corosync

You will now configure Corosync to manage the cluster membership and messaging across the cluster.

  1. Create an authentication key for Corosync on `node-1`:
         
         sudo corosync-keygen
         

  2. Modify the Corosync configuration file:

     1. Return to `node-1` and modify the `corosync.conf` file.
            
            sudo vi /etc/corosync/corosync.conf
            

     2. Update the highlighted sections. After editing, the file should look like the following example.
            
            # Please read the corosync.conf.5 manual page
            totem {
                version: 2
            
                # Corosync itself works without a cluster name, but DLM needs one.
                # The cluster name is also written into the VG metadata of newly
                # created shared LVM volume groups, if lvmlockd uses DLM locking.
                cluster_name: my_agcluster
            
                # crypto_cipher and crypto_hash: Used for mutual node authentication.
                # If you choose to enable this, then do remember to create a shared
                # secret with "corosync-keygen".
                # enabling crypto_cipher, requires also enabling of crypto_hash.
                # crypto works only with knet transport
                transport: udpu
                crypto_cipher: none
                crypto_hash: none
            }
            
            logging {
                # Log the source file and line where messages are being
                # generated. When in doubt, leave off. Potentially useful for
                # debugging.
                fileline: off
                # Log to standard error. When in doubt, set to yes. Useful when
                # running in the foreground (when invoking "corosync -f")
                to_stderr: yes
                # Log to a log file. When set to "no", the "logfile" option
                # must not be set.
                to_logfile: yes
                logfile: /var/log/corosync/corosync.log
                # Log to the system log daemon. When in doubt, set to yes.
                to_syslog: yes
                # Log debug messages (very verbose). When in doubt, leave off.
                debug: off
                # Log messages with time stamps. When in doubt, set to hires (or on)
                #timestamp: hires
                logger_subsys {
                    subsys: QUORUM
                    debug: off
                }
            }
            quorum {
                # Enable and configure quorum subsystem (default: off)
                # see also corosync.conf.5 and votequorum.5
                provider: corosync_votequorum
            }
            nodelist {
                # Change/uncomment/add node sections to match cluster configuration
            
                node {
                    # Hostname of the node
                    name: node-1
                    # Cluster membership node identifier
                    nodeid: 1
                    # Address of first link
                    ring0_addr: NODE1_INTERNAL_IP
                    # When knet transport is used it's possible to define up to 8 links
                    #ring1_addr: 192.168.1.1
                }
                node {name: node-2nodeid: 2ring0_addr: NODE2_INTERNAL_IP}node {name: node-3nodeid: 3ring0_addr: NODE3_INTERNAL_IP}
                # ...
            }
            

Replace `NODE1_INTERNAL_IP`, `NODE2_INTERNAL_IP`, and `NODE3_INTERNAL_IP` with the internal IP addresses of each node.




### Transfer the config files using Cloud Storage

  1. Upload the generated authentication key and corosync configuration files from `node-1` to your Cloud Storage bucket:
         
         sudo gcloud storage cp /etc/corosync/authkey gs://BUCKET_NAME/
         sudo gcloud storage cp  /etc/corosync/corosync.conf gs://BUCKET_NAME/
         

Replace `BUCKET_NAME` with the name of the bucket previously created.

  2. Download the Authkey and config files to `node-2` and `node-3`:
         
         sudo gcloud storage cp gs://BUCKET_NAME/authkey /etc/corosync/
         sudo gcloud storage cp gs://BUCKET_NAME/corosync.conf /etc/corosync/
         

Replace `BUCKET_NAME` with the name of the bucket where the Corosync configuration files were transferred.

  3. Update the permissions of the files on `node-2` and `node-3`:
         
         sudo chmod 400 /etc/corosync/authkey
         sudo chmod 400 /etc/corosync/corosync.conf
         




### Restart and verify Cluster communication

  1. Restart the Pacemaker and Corosync services on `node-1`, `node-2`, and `node-3`:
         
         sudo systemctl restart pacemaker corosync
         

  2. Confirm the status of cluster by running the command on `node-1`:
         
         sudo crm status
         

You should see all three nodes online.




### Set up the Cluster

Next, you will set up the Pacemaker cluster by creating a new resource for the SQL Server Always On availability group.

  1. Run the following command on `node-1` to set the Cluster properties:
         
         sudo crm configure property stonith-enabled=false
         sudo crm configure property cluster-recheck-interval=2min
         sudo crm configure property start-failure-is-fatal=true
         

For more information, see [Cluster Options](https://clusterlabs.org/pacemaker/doc/deprecated/en-US/Pacemaker/1.1/html/Pacemaker_Explained/_cluster_options.html).

  2. Authorize the nodes in the cluster by running the command on `node-1`. Use the password set previously for the `hacluster` account:
         
         sudo pcs cluster auth -u hacluster
         

You should see all three nodes are authorized.

  3. Install SQL Server resource agent for integration with Pacemaker on `node-1`, `node-2`, and `node-3`:
         
         sudo apt-get install mssql-server-ha
         

  4. Return to `node-1` and create an availability group resource in the cluster:

     1. Run the Cluster Resource Manager.
            
            sudo crm
            

     2. Type in `configure` to enter the configuration menu.

     3. Enter the following configuration.
            
            primitive aoag1-cluster \
            ocf:mssql:ag \
            params ag_name="aoag1" \
            meta failure-timeout=60s \
            op start timeout=60s \
            op stop timeout=60s \
            op promote timeout=60s \
            op demote timeout=10s \
            op monitor timeout=60s interval=10s \
            op monitor timeout=60s on-fail=demote interval=11s role="Master" \
            op monitor timeout=60s interval=12s role="Slave" \
            op notify timeout=60s
            ms ms-ag1 aoag1-cluster \
            meta master-max="1" master-node-max="1" clone-max="3" \
            clone-node-max="1" notify="true"
            

     4. Type in `commit` to commit the changes.

**Note:** You will receive a warning that no fencing rule has been set up. Ignore this message, a fencing rule will be set up in a later step.
     5. Type in `exit` to exit the Cluster resource manager.

     6. Verify the configuration.
            
            sudo crm status
            

You should see that `node-1` has been promoted to the primary node. `Node-2` and `node-3` should be set as the secondary nodes.




## Set up load balancer and Availability Group listener

In this section, you create a virtual IP address and a health check resource in the cluster using an internal passthrough TCP load balancer that routes traffic to the availability group.

  1. Return to your Cloud Shell and reserve a static IP address that you will use as the cluster IP:
         
         gcloud compute addresses create aoag1-cluster \
         --region REGION \
         --subnet SUBNET_NAME
         CLUSTER_ADDRESS=$(gcloud compute addresses describe aoag1-cluster \
         --region $(gcloud config get-value compute/region) \
         --format=value\(address\)) && \
         echo "Cluster IP address: $CLUSTER_ADDRESS"
         

Replace `REGION` and `SUBNET_NAME` with the region and subnet where the Linux VMs are deployed.

**Note:** Save the reserved IP address, you will use this in a later step.
  2. Create unmanaged instance groups for each of your cluster nodes and assign them to the newly created instance group. Run the following commands in the Cloud Shell:
         
         gcloud compute instance-groups unmanaged create node-1-uig \
         --zone=REGION-a
         gcloud compute instance-groups unmanaged add-instances node-1-uig \
         --zone=REGION-a \
         --instances=node-1
         
         gcloud compute instance-groups unmanaged create node-2-uig \
         --zone=REGION-b
         gcloud compute instance-groups unmanaged add-instances node-2-uig \
         --zone=REGION-b \
         --instances=node-2
         
         gcloud compute instance-groups unmanaged create node-3-uig \
         --zone=REGION-c
         gcloud compute instance-groups unmanaged add-instances node-3-uig \
         --zone=REGION-c \
         --instances=node-3
         

Replace `REGION` with the region where the Linux VMs are deployed.

  3. Create a TCP health check. Load balancers use health checks to determine which backend instances respond properly to traffic.
         
         gcloud compute health-checks create tcp aoag1-healthcheck \
         --port=HEALTH_CHECK_PORT --proxy-header=NONE \
         --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
         --healthy-threshold=2
         

Choose and replace `HEALTH_CHECK_PORT` with value of a port that is free and in the private range of 49152-65535 . For example, 60000.

For more information, read the [health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

  4. Add network tags to your cluster nodes. The network tag is used by the firewall rule for the health check:
         
         gcloud compute instances add-tags node-1 \
         --tags NETWORK_TAG_NAME \
         --zone REGION-a
         gcloud compute instances add-tags node-2 \
         --tags NETWORK_TAG_NAME \
         --zone REGION-b
         gcloud compute instances add-tags node-3 \
         --tags NETWORK_TAG_NAME \
         --zone REGION-c
         

Replace `NETWORK_TAG_NAME` with a name for the network tag.

  5. Create a firewall rule to allow the health checks to reach the cluster nodes based on the tag name:
         
         gcloud compute firewall-rules create mssql-aoag1-fw-rule \
         --network VPC_NAME \
         --action ALLOW \
         --direction INGRESS \
         --source-ranges 35.191.0.0/16,130.211.0.0/22 \
         --target-tags NETWORK_TAG_NAME \
         --rules tcp:HEALTH_CHECK_PORT
         

For more information, see [Firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

  6. Create the load balancer backend service:
         
         gcloud compute backend-services create aoag1-backend \
         --load-balancing-scheme internal \
         --health-checks aoag1-healthcheck \
         --no-connection-drain-on-failover \
         --drop-traffic-if-unhealthy \
         --failover-ratio 1.0 \
         --region REGION \
         --global-health-checks
         

  7. Add the three unmanaged instance groups to the backend service:
         
         gcloud compute backend-services add-backend aoag1-backend \
         --instance-group node-1-uig \
         --instance-group-zone REGION-a \
         --region REGION
         
         gcloud compute backend-services add-backend aoag1-backend \
         --instance-group node-2-uig \
         --instance-group-zone REGION-b \
         --failover \
         --region REGION
         
         gcloud compute backend-services add-backend aoag1-backend \
         --instance-group node-3-uig \
         --instance-group-zone REGION-c \
         --failover \
         --region REGION
         

  8. Define a forwarding rule for your load balancer. A forwarding rule specifies the protocol and ports on which the load balancer accepts traffic:
         
         gcloud compute forwarding-rules create aoag1-fwd-rule \
         --load-balancing-scheme internal \
         --address CLUSTER_ADDRESS \
         --subnet SUBNET_NAME \
         --region REGION \
         --backend-service aoag1-backend \
         --ports ALL
         

Replace `CLUSTER_ADDRESS` with the IP address reserved earlier.

**Tip:** If you need your cluster to be accessible by clients in any region of the VPC network or a connected network, you need to include the `--allow-global-access` in the definition of the forwarding rule.

For more information, see [Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding_rule)

  9. To complete the setup and test whether your network load balancer is set up correctly, install and configure the `HAProxy tcp listener` on `node-1`, `node-2`, and `node-3`:

     1. Install the HAProxy. 
            
            sudo apt-get install haproxy
            

     2. Choose `Y` to complete installation.

     3. Edit the `haproxy.cfg` file.
            
            sudo vi /etc/haproxy/haproxy.cfg
            

     4. In the defaults section of the `haproxy.cfg file`, change the mode to `tcp`.

     5. Append the following section at the end of the `haproxy.cfg` file
            
            #---------------------------------------------------------------
            # Set up health check listener for SQL Server Availability Group
            #---------------------------------------------------------------
            listen healthcheck
            bind *:HEALTH_CHECK_PORT
            

Replace `HEALTH_CHECK_PORT` with the health check port previously selected. For example, 6000.

     6. Start the service to confirm it is correctly configured:
            
            sudo systemctl start haproxy.service
            sudo systemctl enable haproxy.service
            sudo systemctl restart haproxy.service
            

     7. Go to the Load balancing page, click your load balancer. Observe your three unmanaged instance groups, they should now report as healthy.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing)

        * Alternatively, you can run the following command in the Cloud Shell to see the status of the backend service.
              
              gcloud compute backend-services get-health aoag1-backend \
              --region REGION
              

Replace `REGION` with the region where the Linux VMs are deployed.

     8. Once all three unmanaged instance groups are reporting healthy, continue to the next step.

**Note:** If the unmanaged instance group does not report healthy, you may need to restart the `haproxy.service` from the node in question.
            
            sudo systemctl restart haproxy.service
            

  10. Create the health check resource in Pacemaker:

     1. SSH to `node-1` and create a health check resource for the HAProxy service in your pacemaker cluster:
            
            sudo pcs resource create aoag1-healthcheck \
            service:haproxy \
            op monitor interval=10s timeout=20s
            

     2. Check that the health resource is started on the primary node `node-1`:
            
            sudo crm status
            

     3. If the health check resource is not started on the primary node, move it with the following commands:
            
            sudo pcs resource move aoag1-healthcheck node-1
            sudo pcs resource clear aoag1-healthcheck
            

You will see that the health check for the load balancer will be healthy only for `node-1`.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing)

  11. Create a virtual IP address resource in your Pacemaker cluster:

     1. Return to SSH on `node-1` and find the name of the network interface of your node. You will need it in the next step.
            
            ip -c link
            

     2. Create the virtual IP address resource.
            
            sudo pcs resource create aoag1-vip ocf:heartbeat:IPaddr2 \
            ip="CLUSTER_ADDRESS" nic=NIC_NAME cidr_netmask=32 \
            op monitor interval=3600s timeout=60s
            

Replace `NIC_NAME` with the network interface name from the previous step and `CLUSTER_ADDRESS` with the reserved IP address.

     3. Check that the virtual IP address resource is started on the primary host.
            
            sudo crm status
            

     4. If the virtual IP address resource is not started on the primary node, move it with the following commands.
            
            sudo pcs resource move aoag1-vip node-1
            

     5. Group the health check and virtual IP address resources together.
            
            sudo pcs resource group add aoag1-group \
            aoag1-healthcheck aoag1-vip
            

     6. Create a constraint that locates the new group on the same node as the primary.
            
            sudo pcs constraint colocation add master aoag1-group with master ms-ag1 score=INFINITY
            




### Create a listener for your SQL Server availability group

Connections to SQL Server with availability groups should use an availability group listener name instead of the server name. If there is a failover, the listener will automatically redirect connections to the new primary node in the cluster.

  1. Return to SSMS and connect to the `node-1` database.

  2. Run the following query:
         
         ALTER AVAILABILITY GROUP aoag1
         ADD LISTENER 'aoag1-listener' (
             WITH IP (('CLUSTER_ADDRESS','255.255.255.0')), PORT=1433
         );
         GO
         

Replace `CLUSTER_ADDRESS` with the reserved IP address.




## Set up a STONITH fence

STONITH is a fencing strategy for maintaining the integrity of nodes in a HA cluster. STONITH service works at the node level and protects the cluster from nodes that are either unresponsive or in an unknown state. We recommend the `fence_gce` fencing device specialized for Compute Engine on Google Cloud.

### Set up fencing devices

  1. Check if the `fence_gce` \- Fence agent for Compute Engine is installed on `node1`:
         
         sudo pcs stonith list | grep fence_gce
         

For more information, see:

     * [Fence agent for Google Compute Engine](https://manpages.ubuntu.com/manpages/kinetic/en/man8/fence_gce.8.html).
     * To see the parameters associated with the agent run.
           
           sudo pcs stonith describe fence_gce
           

  2. On `node-1`, create the `fence_gce` fencing type resources for each of the participating nodes:
         
         sudo pcs stonith create node-1-fence fence_gce \
         plug=node-1 \
         zone=REGION-a \
         project=PROJECT_ID \
         pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30 \
         op monitor interval="300s" timeout="120s" \
         op start interval="0" timeout="60s"
         
         sudo pcs stonith create node-2-fence fence_gce \
         plug=node-2 \
         zone=REGION-b \
         project=PROJECT_ID \
         pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30 \
         op monitor interval="300s" timeout="120s" \
         op start interval="0" timeout="60s"
         
         sudo pcs stonith create node-3-fence fence_gce \
         plug=node-3 \
         zone=REGION-c \
         project=PROJECT_ID \
         pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30 \
         op monitor interval="300s" timeout="120s" \
         op start interval="0" timeout="60s"
         

Replace `REGION` with the region where the Linux VMs are deployed and replace `PROJECT_ID` with your project ID.

  3. You can test the status of the fencing agents by running the status command:
         
         sudo fence_gce -o status -n node-1 --zone=REGION-a
         sudo fence_gce -o status -n node-2 --zone=REGION-b
         sudo fence_gce -o status -n node-3 --zone=REGION-c
         

  4. Create location constraints for your fencing devices to ensure that they are running only on the intended instances:
         
         sudo pcs constraint location node-1-fence avoids node-1
         sudo pcs constraint location node-2-fence avoids node-2
         sudo pcs constraint location node-3-fence avoids node-3
         

  5. Enable fencing in your pacemaker cluster and set the cluster fencing timeout:
         
         sudo pcs -f stonith_cfg property set stonith-enabled=true
         sudo pcs property set stonith-timeout="300s"
         

  6. Check the status of the cluster:
         
         sudo crm status
         




### Test the fencing devices

After the setup of the fencing devices, we recommend you test them using the following steps.

  1. Stop the fence on `node-2`:

     1. Connect to `node-1` and run the following command to test the fence device associated with `node-2` from your cluster.
            
            fence_gce -o off -n node-2 --zone=REGION-b
            

     2. Check the status of the cluster.
            
            sudo crm status
            

     3. You will also see that `node-2` is turned off in Compute Engine.

[Go to Compute Engine](https://console.cloud.google.com/compute)

  2. Restart the fence on `node-2`:

     1. Return to `node-1` and restart the instance again by running the following command.
            
            fence_gce -o on -n node-2 --zone=REGION-b
            

     2. Check the status of the cluster in Pacemaker and Compute Engine. After a short time, you will see that `node-2` is back online.
            
            sudo crm status
            




### Configure Corosync for delayed restart

To avoid timing issues and ensure a proper order of operations performed in case of a fencing action, we recommend delaying the restart of Corosync service for 60 seconds. 

For more information, see the [Red Hat knowledgebase article](https://access.redhat.com/solutions/5644441).

  1. Create a systemd drop-in file that sets a delay of the Corosync service start on `node-1`, `node-2`, and `node-3`:

     1. Open the corosync.service for edit. 
            
            sudo systemctl edit corosync.service
            

     2. Append the following lines, save the file and exit the editor.
            
            [Service]
            ExecStartPre=/bin/sleep 60
            

     3. Reload the service manager and check if the configuration is taken into account.
            
            sudo systemctl daemon-reload
            systemctl status corosync.service --no-pager
            
            

If you see the Drop-In section, then the settings in your drop-in file were successfully taken into account




## Test failover

You are now ready to test if the failover works as expected.

  1. Connect to the Windows VM on `node-4` through Remote Desktop:
  2. Open a PowerShell session:
  3. Run the following script:
         
         while ($True){
           $Conn = New-Object System.Data.SqlClient.SqlConnection
           $Conn.ConnectionString = "Server=CLUSTER_ADDRESS;User ID=sa;Password=SA_PASSWORD;Initial Catalog=master"
           $Conn.Open()
         
           $Cmd = New-Object System.Data.SqlClient.SqlCommand
           $Cmd.Connection = $Conn
           $Cmd.CommandText = "SELECT @@SERVERNAME"
         
           $Adapter = New-Object System.Data.SqlClient.SqlDataAdapter $Cmd
           $Data = New-Object System.Data.DataSet
           $Adapter.Fill($Data) | Out-Null
           $Data.Tables[0] + (Get-Date -Format "MM/dd/yyyy HH:mm:ss")
         
           Start-Sleep -Seconds 2
         }
         

Replace `CLUSTER_ADDRESS` with the listener IP address and `SA_PASSWORD` with the password of the **SA** account on SQL Server.

Every 2 seconds, the script connects to SQL Server by using the availability group listener or DNN listener, and queries the server name.

Leave the script running.

  4. Return to SSH on `node-1` and run the commands to trigger a failover to `node-2`:
         
         sudo pcs resource move ms-ag1 node-2 --master
         sudo pcs resource move aoag1-group  node-2
         sudo pcs resource move aoag1-vip node-2
         

  5. Return to the PowerShell session on `node-4`:

     1. Observe the output of the running script and notice that the server name changes from `node-1` to `node-2` as a result of the failover.
  6. Return to `node-1` and initiate a failback to `node-1`:
         
         sudo pcs resource move ms-ag1 node-1 --master
         sudo pcs resource move aoag1-group  node-1
         sudo pcs resource move aoag1-vip node-1
         

  7. Return to Powershell on `node-4` and stop the script by pressing `Ctrl+C`.




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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
