---
url: https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-manual/
title: Manual VM deployment for SAP NetWeaver on Windows \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:31.423770+00:00
---

# Manual VM deployment for SAP NetWeaver on Windows  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-manual/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manual VM deployment for SAP NetWeaver on Windows Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to manually deploy and connect to a VM that is configured to run SAP NetWeaver on Microsoft Windows Server-based systems on Google Cloud. To deploy a VM that is running Linux, see the [Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux).

These instructions give you the details for setting up a 2-tier system, with all the SAP components and the database running on a single VM. During deployment, you also install Google Cloud's Agent for SAP and can validate that it is sending metrics to SAP. This guide also includes considerations for migrating an existing system and for setting up a 3-tier scale-out system.

For more details on planning your implementation, see the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide). For an overview of IT ops for your system, see the [Operations Guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide).

## Creating a project

To create a project:

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




## Configuring the `gcloud` command environment

These instructions use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to enter `gcloud` commands that deploy or configure your Google Cloud resources. Cloud Shell is accessed through the Google Cloud console in your browser.

Cloud Shell runs on a VM that Google Cloud provisions each time you start Cloud Shell. The first time you use Cloud Shell, Google Cloud also creates a persistent `$HOME` directory for you, which is restored each time you open Cloud Shell.

The provisioned VM includes the latest [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). Therefore, the `gcloud` commands that you use in Cloud Shell are the same as those you would use in a locally installed instance of the gcloud CLI.

If you have the gcloud CLI installed, you can issue the `gcloud` commands that are used in these instructions from your local machine. However, with a locally installed gcloud CLI you must always make sure that you are using the latest version of the gcloud CLI.

Whether you use Cloud Shell or gcloud CLI, you can set and change the properties of your `gcloud` command environment and save them as a _configuration_. Configurations are collections of key-value pairs that influence the behavior of the `gcloud` commands.

Some basic actions you can take with a configuration in Cloud Shell include:

  * Initialize a configuration:
        
        gcloud init

  * Check the settings of your current gcloud configuration:
        
        gcloud config list

  * Switch to the required Google Cloud project. Replace `PROJECT_ID` with your Google Cloud project ID.
        
        gcloud config set project PROJECT_ID

  * Set a default region. Replace `REGION` with a Google Cloud region.
        
        gcloud config set compute/region REGION

  * Set a default zone. Replace `ZONE` with a Google Cloud zone.
        
        gcloud config set compute/zone ZONE

  * Create a new configuration. Replace `NAME` with the name for the configuration.
        
        gcloud config configurations create NAME




For more information about working with configurations, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/configurations).

## Creating a network

For security purposes, create a new network. You can control who has access by adding firewall rules or by using another access control method.

If your project has a default VPC network, then don't use it. Instead, create your own VPC network so that the only firewall rules in effect are those that you create explicitly.

During deployment, Compute Engine instances typically require access to the internet to download Google Cloud's Agent for SAP. If you are using one of the SAP-certified Linux images that are available from Google Cloud, then the compute instance also requires access to the internet in order to register the license and to access OS vendor repositories. A configuration with a NAT gateway and with VM network tags supports this access, even if the target compute instances don't have external IPs. 

To set up networking:

### Console

  1. In the Google Cloud console, go to the **VPC networks** page. 

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.
  3. Enter a **Name** for the network. 

The name must adhere to the [naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VPC networks use the Compute Engine naming convention. 

  4. For **Subnet creation mode** , choose **Custom**.
  5. In the **New subnet** section, specify the following configuration parameters for a subnet: 
     1. Enter a **Name** for the subnet.
     2. For **Region** , select the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to create the subnet.
     3. For **IP stack type** , select **IPv4 (single-stack)** and then enter an IP address range in the [CIDR format](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing), such as `10.1.0.0/24`. 

This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges) for the subnet. If you plan to add more than one subnet, then assign non-overlapping CIDR IP ranges for each subnetwork in the network. Note that each subnetwork and its internal IP ranges are mapped to a single region.

     4. Click **Done**. 
  6. To add more subnets, click **Add subnet** and repeat the preceding steps. You can add more subnets to the network after you have created the network.
  7. Click **Create**. 



### gcloud

  1. Go to Cloud Shell. 

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. To create a new network in the custom subnetworks mode, run: 
         
         gcloud compute networks create NETWORK_NAME --subnet-mode custom

Replace `NETWORK_NAME` with the name of the new network. The name must adhere to the [naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). VPC networks use the Compute Engine naming convention. 

Specify `--subnet-mode custom` to avoid using the default auto mode, which automatically creates a subnet in each Compute Engine region. For more information, see [Subnet creation mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).

  3. Create a subnetwork, and specify the region and IP range: 
         
         gcloud compute networks subnets create SUBNETWORK_NAME \
             --network NETWORK_NAME --region REGION --range RANGE

Replace the following:

     * `SUBNETWORK_NAME`: the name of the new subnetwork
     * `NETWORK_NAME`: the name of the network you created in the previous step
     * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want the subnetwork 
     * `RANGE`: the IP address range, [specified in CIDR format](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing), such as `10.1.0.0/24`

If you plan to add more than one subnetwork, assign non-overlapping CIDR IP ranges for each subnetwork in the network. Note that each subnetwork and its internal IP ranges are mapped to a single region.

  4. Optionally, repeat the previous step and add additional subnetworks.



## Setting up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

## Adding firewall rules

By default, incoming connections from outside your Google Cloud network are blocked. To allow incoming connections, set up a firewall rule for your VM. Firewall rules regulate only new incoming connections to a VM. After a connection is established with a VM, traffic is permitted in both directions over that connection.

You can create a firewall rule to allow access to specified ports, or to allow access between VMs on the same subnetwork.

Create firewall rules to allow access for such things as:

  * The default ports used by SAP NetWeaver, as documented in [TCP/IP Ports of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine VM instance. If you are unsure of what IP address to use, talk to your company's network admin.
  * Communication between VMs in a 3-tier, scaleout, or high-availability configuration. For example, if you are deploying a 3-tier system, you will have at least 2 VMs in your subnetwork: the VM for SAP NetWeaver, and another VM for the database server. To enable communication between the two VMs, you must create a firewall rule to allow traffic that originates from the subnetwork. 
  * RDP connections to your VM instance through port `3389`.
  * PowerShell connections to your VM instance through port `5986`. 

**Note:** The following procedure is a simplified version of the instructions for creating firewall rules. For more detailed instructions, see the [Virtual Private Cloud documentation](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

To create a firewall rule:

  1. In the Google Cloud console, go to the VPC network **Firewall** page.

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

  2. At the top of the page, click **Create firewall rule**.

     * In the **Network** field, select the network where your VM is located.
     * In the **Targets** field, select **All instances in the network**.
     * In the **Source filter** field, select one of the following: 
       * **IP ranges** to allow incoming traffic from specific IP addresses. Specify the range of IP addresses in the **Source IP ranges** field.
       * **Subnets** to allow incoming traffic from a particular subnetwork. Specify the subnetwork name in the following **subnets** field. You can use this option to allow access between the VMs in a 3-tier or scaleout configuration.
     * In the **Protocols and ports** section, select **Specified protocols and ports** and specify `tcp:PORT_NUMBER;`.
  3. Click **Create** to create your firewall rule.




## Deploying a VM manually

The following instructions show you how to deploy a VM for an example 2-tier SAP system running Microsoft Windows and Microsoft SQL Server, SAP ASE, or IBM Db2 for Linux, UNIX, and Windows (IBM Db2). All the SAP NetWeaver components and the central database run on one VM.

For general considerations for a 3-tier system, see Deploying a 3-tier scale-out system.

Before you begin, ensure that you have consulted the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide) and, if you are going to use Microsoft SQL Server, that you have decided how you want to install the SQL Server database from the following options:

  * Use a Google Cloud image that includes the database.
  * Install it using installation media.

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules.
    * Create the VMs without an external IP.



### Creating and setting up a VM

When you create a VM, you can specify several options, including the operating system, region, machine type, and persistent disks. Later, after the VM is deployed, you must also install Google Cloud's Agent for SAP on the VM.

To create a VM:

  1. Go to the **Images** page in Compute Engine:

[Go to the Images page](https://console.cloud.google.com/compute/images)

  2. Choose a public image that contains a version of Microsoft Windows Server that is supported by SAP.

If you are using Microsoft SQL Server as your database, you can migrate your existing license to Google Cloud or use a Compute Engine Windows Server image that has SQL Server preinstalled. For more information about the SQL Server images provided by Google Cloud, see [Windows on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows#sql_server).

For the versions of Windows Server and SQL Server that are supported by SAP on Google Cloud, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

  3. Click the **Create instance** button.

  4. Enter a name for the VM.

Limit your name to 13 characters, because this is the maximum supported by SAP. For more information, see the SAP note [611361 \- Hostnames of SAP ABAP platform servers](https://me.sap.com/notes/611361).

  5. Select the region and zone for your VM based on the location of your internal resources and users, and based on the CPU platform you want to use.

For more details on the zones supported for SAP NetWeaver, see the following:

     * [SAP Netweaver on Google Cloud Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#plan_regions_and_zones)
     * SAP note [2456953 - Windows on Google Cloud Platform (IaaS): Adaptation of your SAP License](https://me.sap.com/notes/2456953)
  6. Under **Machine type** , select a pre-defined `n1-standard` or `n1-highmem` machine type or customize a VM to more precisely match the VM's vCPUs and memory to your expected workload.

**Note:** Before you customize a VM for SAP NetWeaver, review the information about custom machine types in the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types) and in [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

To compare the supported machine types and their persistent-disk limitations, see the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types).

  7. Optionally, in the **Boot disk** section, click **Change** to adjust the size of your boot disk. Ensure that the boot disk is at least 50 GB.

  8. Under **Service account** , select a service account that appropriately limits access to Google Cloud resources from the VM.

If you haven't created a service account, you can use the default service account, but it is usually too permissive for most enterprise users. For more information about service accounts, see [IAM for SAP programs](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).

  9. Under **Access Scopes** :

     * If you are using the Compute Engine default service account, select **Set access for each API**.
     * If you are using a custom service account that limits access to Google Cloud resources, select **Allow full access to all APIs**.

Compute Engine recommends configuring your VM instances to allow full access to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you selected **Set access for each API** , to ensure that your VM instance can interact with Compute Engine and Cloud Monitoring and that Google Cloud's Agent for SAP functions correctly, the following API access scopes are recommended for the service account:

**API** | **Access**  
---|---  
Cloud Source Repositories | Read Write  
Compute Engine | Read Write  
Service Control | Enabled  
Service Management | Read Only  
Cloud Logging API | Full  
Cloud Monitoring API | Full  
Cloud Trace | Write Only  
Storage | Full  
  10. Expand the **Management, disks, networking, sole tenancy** section.

  11. If you are using a NAT gateway, in the **Networking** tab, under **Network tags** , add the tag that you specified as `[YOUR_TAG_NAME]` when you set up the route that directs traffic through the gateway.

  12. In the **Management** tab, under **Availability policy** , ensure that you leave the following default settings:

     * To ensure availability of your SAP systems, keep the **Preemptibility** setting **Off (recommended)**.
     * To ensure that your VM can restart if there's a maintenance or failure event, keep the **Automatic restart** setting **On (recommended)**.
     * To ensure that your VM is migrated to other hardware during infrastructure maintenance, keep the **On host maintenance** setting on **Migrate VM instance (recommended)**.
  13. Optionally, in the **Disks** tab, under **Boot disk > Deletion rule**, deselect the **Delete boot disk when instance is deleted checkbox**.

  14. In the **Disks** tab, under **Additional disks** , click **Add new disk** to add persistent disks for storage.

For NetWeaver, add disks for the SAP NetWeaver binaries and the pagefile disk. For the database server, you also need disks for things like the database data and logs. For information about the types of persistent disks that you can choose, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disk_storage).

     1. Optionally, specify a name in the **Name** field.

     2. In the **Create a disk** window, under **Disk Type** select the disk type.

     3. Under **Source type** , select **Blank disk**.

     4. Specify the size of your disk.

        * For the pagefile disk, size the disk according to your needs. The minimum recommended size is 24 GB. For larger instances, you might need more. For more information on calculating the size required for the page file, see the SAP note [1518419: Page file and virtual memory required by the SAP system](https://me.sap.com/notes/1518419).

Add more disks if needed.

        * If you want to sustain the [maximum throughput rates mentioned in the Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide), ensure that you have at least 834 GB of space for the database data.

     5. Click **Done** to save your disk settings.

     6. Repeat these steps for each disk you need to add to your system.

  15. In the **Networking** tab, under **Network interfaces** , click the pencil icon to edit the selected network interface. Select the network that you created previously.

  16. Click **Create** to create and start the instance.




At the bottom of the page, you can click **REST** or **command line** to see the equivalent REST and `gcloud` commands for the instance you are creating. These can be useful for creating additional VMs.

### Connecting to your VM

To connect to a Windows-based VM, you must first generate a password for the VM. You can then connect to the VM using RDP or PowerShell.

##### Generating passwords

  1. Go to the **VM instances** page.

[OPEN VM INSTANCES](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM instance for which you need a new password.

  3. On the instance details page, click the **Set Windows Password** button. A password is generated for you.




##### Using RDP

If your firewall rule allows access on port `3389`, you can use RDP to connect to a Windows instance and start a Remote Desktop session. Alternatively, you can connect to Windows instances using the PowerShell terminal.

Connect to the remote desktop on Windows instances by manually connecting through the Windows Remote Desktop Connection client or a third-party client:

  1. If you don't already have an RDP client, install one now. For information from Microsoft about available RDP clients, see [Remote Desktop clients](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).
  2. Get your Windows VM's external IP address. To find the VM IP address, you can use either of the following methods: 
     * In the Google Cloud console, go to the [VM Instances page](https://console.cloud.google.com/compute/instances).
     * Use the gcloud CLI to run `gcloud compute instances list` to list your VM instances with their external IP addresses.
  3. In your RDP client, provide your VM's external IP address as the IP address to connect to.
  4. Enter your sign-in information and leave the **Domain** field blank. If this is your first time connecting to this VM, or if you have forgotten your password, [create or reset your Windows password](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-dm#connecting_to_your_vm).



##### Using PowerShell

  1. If you have not created a username and password on the Windows VM yet, create your Windows password.

  2. Add a firewall rule or edit your existing firewall rule to open port 5986 on the [Google Cloud network](https://docs.cloud.google.com/compute/docs/networking) where your Windows Server VM is located.

  3. On your local workstation, open the PowerShell terminal.

  4. Optionally, you can initialize a variable to hold your user credentials so you don't need to enter them each time you connect to the instance. If you skip this step, you receive a prompt for your username and password later.
         
         $credentials = Get-Credential

  5. Use the [Enter-PSSession command](https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.core/enter-pssession) to start a remote PowerShell session and include the flags to use SSL and skip credentials checks.
         
         Enter-PSSession -ComputerName [IP_ADDRESS] -UseSSL -SessionOption (New-PSSessionOption -SkipCACheck -SkipCNCheck) -Credential $credentials




### Formatting and mounting disk drives

After you have connected to your Windows VM, format your disks so that you can begin using them. You also configure the Windows pagefile.

  1. From the Windows **Start** menu, search for and open the Server Manager.

  2. Select **File and Storage Services** and then select **Disks**.

![Server Manager](https://docs.cloud.google.com/static/sap/docs/images/netweaver-server-mgr-disks.png)

  3. In the **Disks** dialog, right-click the first disk, and then select **New Volume**. The **New Volume Wizard** opens.

  4. Optionally, on the **Drive Letter or Folder** panel, select a drive letter for the disk. For example, `S` for the SAP disk, or `P` for the pagefile disk. You can accept all other defaults.

  5. On the **File System Settings** panel, enter a volume label that describes the disk with a meaningful name, such as `SAP` or `Pagefile`.

![New Volume Wizard](https://docs.cloud.google.com/static/sap/docs/images/netweaver-new-vol-wiz.png)

  6. Accept all other defaults.

  7. Repeat these steps for the additional disks.


**Note:** Microsoft recommends that the SQL Server data and log disks be formatted as 64 KB, but the persistent disk technology inside Google Cloud aligns better with 32 KB. The 32 KB size also decreases the number of disk operations that count toward your persistent disk I/O limit.

### Preparing the operating system

After you have created your VM, configure the operating system:

  * If your configuration calls for it, join the Windows Server OS to a domain.
  * [Configure the High Performance power plan](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance#setting_the_power_profile).
  * Add Windows firewall rules to enable access to SAP NetWeaver from a remote connection.
  * To calculate the page file size, see the following SAP resources: 
    * SAP note [1518419: Page file and virtual memory required by the SAP system](https://me.sap.com/notes/1518419)
    * [Configure the Windows Pagefile](https://help.sap.com/saphelp_nw73ehp1/helpdata/EN/4d/0b7b6d277f5ca8e10000000a42189e/content.htm).



## Setting up the database

If you haven't yet deployed your database on Google Cloud, then follow the instructions for setting up your database in both the Google Cloud deployment guide for your database, and in the database documentation that is provided by your database vendor.

Google Cloud provides deployment guides for the following SAP-certified databases:

  * [SAP HANA guides](https://docs.cloud.google.com/sap/docs/sap-hana-guides): when SAP NetWeaver is running on Windows, SAP HANA is supported only in 3-tier architectures. 
  * [SAP ASE guides](https://docs.cloud.google.com/sap/docs/sap-ase-guides)
  * [SAP MaxDB guides](https://docs.cloud.google.com/sap/docs/sap-maxdb-guides)
  * [IBM Db2 guides](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-guides)
  * [Windows SQL Server guide](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances)



When SAP NetWeaver and the database server are running on different compute instances in a 3-tier architecture, make sure that your firewall rules are defined to allow communication between the instances.

If you used the Google Cloud-provided Windows image that contains SQL Server, you must change the collation to use the SAP collation. 

### Configuring the Google Cloud Microsoft SQL Server image

If you selected the Google-provided SQL Server Enterprise operating system image when you created your VM, you must configure SQL Server to use the SAP [collation](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support) (`SQL_Latin1_General_CP850_BIN2`) so that SQL Server is compatible with SAP systems. The default collation in the Google Cloud-provided SQL Server image is (`SQL_Latin1_General_CP1_CI_AS`).

To change the collation after the VM is deployed:

  1. Connect to your Windows instance by using either RDP or remote PowerShell.
  2. Sign in to Windows as an admin and stop the `MSSQLSERVER` service.
  3. Go to the directory that contains the binaries for your SQL Server instance, for example, `C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\Binn`.
  4. From an elevated command prompt, change the collation by running:
         
         sqlservr -m -T4022 -T3659 -s"[SQL_SERVER_INSTANCE_NAME]" -q"SQL_Latin1_General_CP850_BIN2"

where:

     * The parameter `-m` starts the SQL Server instance in single-user mode.
     * The trace flag `4022` forces SQL Server to skip any stored startup procedures.
     * The trace flag `3659` allows all errors to be logged to the SQL Server logs.
     * The parameter `-s` specifies the name of the SQL Server instance to start. Replace `[SQL_SERVER_INSTANCE_NAME]` with your SQL Server instance name.
     * The parameter `-q` rebuilds all databases and objects to the specified SAP collation, without reinstalling the instance or rebuilding system databases.
  5. Restart the SQL Server Service `MSSQLSERVER` after the collation is changed.

  6. Confirm your change in the most recent SQL Server `ERRORLOG` or the server's collation properties.




For more information about the configuration of SQL Server for SAP, see:

  * [Upgrade to and Installation of SQL Server 2016 in an SAP Environment](https://help.sap.com/viewer/upgrade_sql2016)
  * [SAP Note 2201060 - Setting up Microsoft SQL Server 2016](https://launchpad.support.sap.com/#/notes/2201060)



## Installing the Cloud Logging agent

The Cloud Logging agent provides you with a solution for Google Cloud system-activity logging, including operating system events and, if you are using SAP HANA, SAP HANA events. The Cloud Logging agent is an optional but recommended component. See the [SAP NetWeaver on Google Cloud operations guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide#use_stackdriver_logging) for more information about Google Cloud logging.

To install the Cloud Logging agent in your new VM, see the instructions for Linux and Windows in [Installing the agent](https://docs.cloud.google.com/logging/docs/agent/installation#joint-install).

## Install Google Cloud's Agent for SAP

Google Cloud's Agent for SAP is required for SAP support of SAP systems running on Google Cloud, including SAP NetWeaver, SAP HANA, SAP ASE, SAP MaxDB, and others.

When you install Google Cloud's Agent for SAP on a Compute Engine instance, for SAP Host Agent metrics, the agent combines monitoring data from Cloud Monitoring and the Compute Engine APIs and provides that data to the SAP Host Agent.

If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



For information about the operating systems supported by Google Cloud's Agent for SAP, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems).

Before you install Google Cloud's Agent for SAP, you need to ensure that the following prerequisites are met.

#### Set the required IAM roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect metrics from the Compute Engine instances that host your SAP workload: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Read the collected metrics from Cloud Monitoring: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * Write the collected metrics to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect metrics:

  * Collect the metrics from the host Compute Engine instance and write them to Cloud Monitoring and Workload Manager data warehouse: 
    * `compute.instances.get`
    * `compute.instances.list`
    * `monitoring.metricDescriptors.get`
    * `monitoring.metricDescriptors.list`
    * `monitoring.timeSeries.create`
    * `workloadmanager.insights.writer`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Enable access to Google Cloud APIs

Compute Engine recommends configuring your compute instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you do limit access to the Cloud APIs, then Google Cloud's Agent for SAP requires the following minimum Cloud API access scopes on the host Compute Engine instance:

  * **Cloud Platform** : **Enabled**
  * **Compute Engine** : **Read Only**
  * **Stackdriver Monitoring API** : **Read Only**



If you are running SAP applications on a compute instance that does not have an external IP address, then you need to enable [Private Google Access ](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet of the compute instance so that Google Cloud's Agent for SAP can access Google APIs and services. To enable Private Google Access on a subnet, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

### Install the Google Cloud's Agent for SAP

To install the agent on a Compute Engine instance, follow these steps:

  1. Use RDP to connect to the compute instance.
  2. As an administrator, run the following command from PowerShell: 
         
         googet addrepo google-cloud-sap-agent https://packages.cloud.google.com/yuck/repos/google-cloud-sap-agent-windows
         googet install google-cloud-sap-agent




After you install Google Cloud's Agent for SAP and the SAP Host Agent, validate the installation of Google Cloud's Agent for SAP, as described in Validate your installation of the agent.

## Installing SAP NetWeaver

For instructions on installing SAP NetWeaver on your new VM, see [the SAP help portal](https://help.sap.com/viewer/p/SAP_NETWEAVER_750) and the [SAP NetWeaver Master Guide](https://help.sap.com/doc/18cb1a50b9924bc3b94c2988cc8c51d9/7.5/en-US/mg_nw_75.pdf).

**Important:** The Software Provisioning Manager (SWPM) chooses the disk drive with the most free space as an installation suggestion for each component. On Google Cloud, it's important that you don't accept the defaults. Be sure to assign the disks to their proper roles in the SWPM dialog boxes.

After you install SAP NetWeaver:

  1. Update the SAP kernel to the minimum supported patch level.

For details on the supported SAP kernel patch levels, see the SAP note [2456953 - Windows on Google Cloud Platform (IaaS): Adaptation of your SAP License](https://me.sap.com/notes/2456953). 

  2. Install your permanent SAP NetWeaver license.

For more information from SAP about managing your SAP NetWeaver licenses, see [SAP Licensing Procedure](https://help.sap.com/viewer/0643d547dfad4ce497bd7da1264fce77/7.5.6/en-US/fbde4502adef496988fe13d459d66b8b.html).




### Installing the SAP Host Agent

The SAP Host Agent has been enhanced for running on Google Cloud. Ensure that you run at least the minimum SAP Host Agent version required for the Google Cloud environment.

For more information, see the following SAP note [1409604 - Virtualization on Windows: Enhanced Monitoring](https://me.sap.com/notes/1409604).

To update your SAP Host Agent by default on a regular basis, see the SAP note [1473974 - Using the SAP Host Agent Auto Upgrade Feature](https://me.sap.com/notes/1473974).

## Validate your installation of Google Cloud's Agent for SAP

After you have deployed a VM and installed your SAP system, validate that Google Cloud's Agent for SAP is functioning properly.

### Verify that Google Cloud's Agent for SAP is running

To verify that the agent is running, follow these steps:

  1. Use RDP to connect to the Compute Engine instance.

  2. As an administrator, run the following command from PowerShell: 
         
         $(Get-Service -Name 'google-cloud-sap-agent' -ErrorAction Ignore).Status

If the agent is running, then the status shows `Running`.



If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Deploying a 3-tier scale-out system

The steps to deploy each VM in a 3-tier system are very similar to the steps for deploying the example system. In a 3-tier scale-out system, you deploy several VMs, all in the same zone:

  * A primary VM that runs the SAP NetWeaver application server (AS) and ABAP central services. This VM also hosts a shared file system that contains the shared profile and must be accessible from each VM that runs SAP NetWeaver in the system.
  * Some number of additional VMs that run the AS, for scaling purposes.
  * A VM that is dedicated to the central database.



The high-level steps are as follows:

  1. Create the VM that hosts the database and then install the database. If you used a Compute Engine image that includes SQL Server, the database is already installed.

  2. Create the primary instance.

     * Run SWPM on the first VM that you want to run SAP NetWeaver.
     * Install central services.
     * Install the AS.
     * Point to the existing database.
  3. Create additional instances.

     * Run SWPM on each additional VM that you want to run SAP NetWeaver.
     * Install the AS.
     * Point to the existing database.
     * Point to the network share that contains the profiles and is managed by the primary instance.



## Troubleshooting

This section contains information about how to correct common issues.

### Troubleshooting communication problems to the database server

If you are setting up a 3-tier SAP system and having connection issues between your VMs, ensure that you have created a firewall rule to allow traffic between VMs on your subnetwork.

### Troubleshooting Google Cloud's Agent for SAP

To troubleshoot Google Cloud's Agent for SAP, see the [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
