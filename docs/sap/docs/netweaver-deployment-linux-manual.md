---
url: https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-manual/
title: Manual VM deployment for SAP NetWeaver on Linux \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:32.012636+00:00
---

# Manual VM deployment for SAP NetWeaver on Linux  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-manual/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manual VM deployment for SAP NetWeaver on Linux Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to deploy and connect to a VM that is configured to run SAP NetWeaver on Linux-based systems on Google Cloud. To deploy a VM that is running Windows, see the [Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows).

Deploy your VM and associated resources manually only if you require more control over your system configuration than automated deployment methods provide. Using Terraform to deploy your Google Cloud resources is recommended because you can deploy SAP-certified VM configurations for SAP NetWeaver quickly, consistently, and with fewer errors. For information about automating the deployment of Google Cloud resources for SAP NetWeaver, see [Terraform: Automated VM deployment for SAP NetWeaver on Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-tf). 

## VM configuration deployed by these instructions

The VM that is deployed by these instructions is for use in a 3-tier configuration, where SAP NetWeaver runs on one VM and the database server runs on another. During deployment, you also install Google Cloud's Agent for SAP and can validate that it is sending metrics to SAP.

To set up a 2-tier configuration, where SAP NetWeaver runs on the same VM as the database server, you deploy the database server first and create the VM and the required disk drives for both the database server and for SAP NetWeaver at that time. You then install SAP NetWeaver on the same VM as the database server. In a 2-tier configuration, SAP NetWeaver and SAP HANA must use different SAP system IDs (SIDs).

For instructions about deploying the VM for a database server, see the [database deployment guide](https://docs.cloud.google.com/sap/docs) for your database server.

For more details on planning your implementation, see the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide). For an overview of IT ops for your system, see the [Operations Guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide).

## Creating a project

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

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
  * SSH connections to your VM instance, including [SSH from the browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser), through port `22`.
  * Connections to your VM instance from third-party tools, such as a local terminal or PuTTY. Create a rule to allow access for the tool through your firewall. For more information, see [Connect to Linux VMs using third-party tools](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools). 

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

The following instructions show you how to deploy an example 3-tier SAP system running Linux and either SAP HANA, SAP ASE, or IBM Db2 for Linux, UNIX and Windows (IBM Db2) as the database. The database components run on one VM, and the other SAP components, including the SAP central services, run on a second VM.

For general considerations for a scale-out system, see Deploying a 3-tier scale-out system.

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules.
    * Create the VMs without an external IP.



### Creating and setting up the VM

When you create a VM, you can specify several options, including the operating system, region, machine type, and persistent disks. Later, after the VM is deployed, you must also install Google Cloud's Agent for SAP on the VM.

To create a VM:

  1. Go to the **Images** page in Compute Engine:

[Go to the Images page](https://console.cloud.google.com/compute/images)

  2. To use a public image, choose an image from one of the following image families:

     * For RHEL, select an image that begins with `rhel-`, such as `rhel-7-sap-apps`.
     * For SLES, select an image that begins with `sles-`, such as `sles-12-sp3-sap`.
  3. Click the **Create instance** button.

  4. Enter a name for the VM.

Limit your name to 13 characters, because this is the maximum supported by SAP. For more information, see the SAP note [611361 \- Hostnames of SAP ABAP platform servers](https://me.sap.com/notes/611361).

  5. Select the region and zone for your VM based on the location of your internal resources and users, and based on the CPU platform you want to use.

For more details on the zones supported for SAP NetWeaver, see the following guides and SAP Notes:

     * [SAP Netweaver on Google Cloud Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#plan_regions_and_zones)
     * SAP note [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441)
  6. Under **Machine type** , select a pre-defined `n1-standard` or `n1-highmem` machine type, or customize a VM to more precisely match your expected workload.

**Note:** Before you customize a VM for SAP NetWeaver, review the information about custom machine types in the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types) and in [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

To compare the supported machine types and their persistent-disk limitations, see the [Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types).

  7. Optionally, in the **Boot disk** section, click **Change** to configure your boot disk. For Linux systems, ensure that the boot disk is at least 16 GB.

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
     * To ensure that your VM can restart if there's a maintenance or failure event, keep the **Automatic restart** setting **On (recommended)** .
     * To ensure that your VM is migrated to other hardware during infrastructure maintenance, keep the **On host maintenance** setting on **Migrate VM instance (recommended)**.
  13. Optionally, in the **Disks** tab, under **Boot disk > Deletion rule**, clear the **Delete boot disk when instance is deleted** checkbox.

  14. In the **Disks** tab, under **Additional disks** , click **Add new disk** to add persistent disks for storage.

For NetWeaver, add disks for the SAP NetWeaver binaries and the swap disk. For the database server, you also need disks for things like the database data and logs. For information about the types of persistent disks that you can choose, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disk_storage).

     1. Optionally, specify a name in the **Name** field.

     2. In the **Create a disk** window, under **Disk Type** , select the disk type based on the purpose of the disk.

     3. Under **Source type** , select **Blank disk**.

     4. Specify the size of your disk.

For the swap disk, size the disk according to your needs. The minimum recommended size is 24 GB. For larger instances, you may need more. Refer to the SAP documentation. For example, see [SAP Note 1597355 - Swap-space recommendation for Linux](https://launchpad.support.sap.com/#/notes/1597355).

     5. Click **Done**.

     6. Repeat these steps to create each disk you need for your system.

  15. In the **Networking** tab, under **Network interfaces** , click the pencil icon to edit the selected network interface.

     1. Select the network that you created previously.
     2. Select the subnetwork.
     3. Click **Done**.
  16. Click **Create** to create and start the instance.




At the bottom of the page, you can click **REST** or **command line** to see the equivalent REST and `gcloud` commands for the instance you are creating. These can be useful for creating additional VMs.

### Connecting to your VM

If you have defined a firewall rule that allows access on port 22, you can connect to a Linux VM using common SSH tools.

Google Cloud provides two easy connection methods. You can connect with a click of a button through the Google Cloud console or you can connect from a terminal by using a `gcloud` command.

### Console

To SSH directly from your web browser in the [Google Cloud console](https://console.cloud.google.com/):

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




### gcloud

The Google Cloud CLI manages your SSH keys for you by generating and applying new project-wide SSH keys when you need them. To connect through the gcloud CLI, replace the brackets and their contents with your values before entering the following command:
    
    
    gcloud compute --project "[VM-GC-PROJECT]" ssh --zone "[VM-ZONE]" "[VM-NAME]"

After you submit the preceding command, the terminal is connected to your VM on Google Cloud and you can run commands on your Linux VM. When you are done, use the `exit` command to disconnect from the VM.

**Note:** New VMs can take some time to boot up before an SSH connection can be established. If you fail to connect to a new instance, retry after a few minutes.

You can also generate a new key-pair for your Linux VM and apply it to your project, which allows you to connect using third-party tools such as [PuTTY on Windows workstations](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools). For more details, see [Create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).

Other connection options, which are not discussed here, are also possible.

For more detailed information about connecting to a Linux VM on Google Cloud, see [Connecting to Linux instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools).

### Formatting and mounting disk drives

After you connect to your VM, format and mount the disk drives, including the SAP disk drives and the swap disk drive.

#### Formatting and mounting SAP disk drives

The following steps format and mount the `/usr/sap` disk. For other disks, such as `/sapmnt` or `/backup`, replace the `usrsap` and `/usr/sap` volume and mount point identifiers in the example commands with identifiers for those disks.

  1. In a terminal connected to your VM, switch to super user:
         
         sudo su -

  2. Create a physical volume for the disk:
         
         pvcreate /dev/disk/by-id/google-[DISK]

  3. Create a volume group for the disk:
         
         vgcreate vg_usrsap /dev/disk/by-id/google-[DISK]

  4. Create a logical volume for the disk:
         
         lvcreate -l 100%FREE -n vol vg_usrsap

  5. Format the disk. The following command formats the disk with a single `xfs` file system and no partition table:
         
         mkfs -t xfs /dev/vg_usrsap/vol

**Note:** Earlier versions of IBM Db2 do not support the xfs file system. For the Db2-supported file systems, see [SAP Note 405827 - Linux: Recommended file systems](https://launchpad.support.sap.com/#/notes/405827).
  6. Update the file system table `fstab`:
         
         echo "/dev/vg_usrsap/vol /usr/sap xfs defaults,discard,nofail 0 2" >>/etc/fstab

The `nofail` option is specified so that the instance can continue to boot even if the disk is not present. For example, if you take a snapshot of the boot disk and create a new instance without any persistent disks attached, the instance can continue through the startup process and not pause indefinitely.

  7. Create a mount point:
         
         mkdir -p /usr/sap

  8. Mount the disk to the VM:
         
         mount -a

  9. Confirm that the disk is mounted properly:
         
         df -h

You should see output similar to the following: 
         
         Filesystem                 Size  Used Avail Use% Mounted on
          devtmpfs                    15G  8.0K   15G   1% /dev
          tmpfs                       23G     0   23G   0% /dev/shm
          tmpfs                       15G  9.7M   15G   1% /run
          /dev/sda1                   16G  1.8G   14G  12% /
          tmpfs                       15G     0   15G   0% /sys/fs/cgroup
          tmpfs                      3.0G     0  3.0G   0% /run/user/1001
          /dev/mapper/vg_usrsap-vol   15G   33M   15G   1% /usr/sap
          /dev/mapper/vg_sapmnt-vol   15G   33M   15G   1% /sapmnt

  10. Repeat these steps for each additional disk.




#### Format and mount the swap disk

  1. In a terminal connected to your VM, create a physical volume for the swap disk:
         
         pvcreate /dev/disk/by-id/google-[DISK]

  2. Create a volume group for the swap disk:
         
         vgcreate vg_swap /dev/disk/by-id/google-[DISK]

  3. Create a logical volume for the swap disk:
         
         lvcreate -l 100%FREE -n vol vg_swap

  4. Format the swap disk:
         
         mkswap /dev/vg_swap/vol

  5. Update `fstab`:
         
         echo "/dev/vg_swap/vol none swap defaults,nofail 0 2" >>/etc/fstab

  6. Mount the disk to the VM:
         
         swapon /dev/vg_swap/vol




### Preparing the operating system

After you have created your VM, consult the relevant SAP notes on installation and ensure that your system includes the software components specified in the following SAP notes:

  * [2578899 - SUSE Linux Enterprise Server 15: Installation Note](https://launchpad.support.sap.com/#/notes/2578899)
  * [1984787 - SUSE LINUX Enterprise Server 12: Installation notes](https://launchpad.support.sap.com/#/notes/1984787)
  * [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)
  * [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)
  * [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)
  * [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)



Before you install any SAP software on RHEL for SAP 9.x, additional packages must be installed on your host machines, especially `chkconfig` and `compat-openssl11`. If you use an image provided by Compute Engine, then these packages are automatically installed for you. For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316). 

## Setting up the database

If you haven't yet deployed your database on Google Cloud, then follow the instructions for setting up your database in both the Google Cloud deployment guide for your database, and in the database documentation that is provided by your database vendor.

Google Cloud provides deployment guides for the following SAP-certified databases:

  * [SAP HANA guides](https://docs.cloud.google.com/sap/docs/sap-hana-guides)
  * [SAP ASE guides](https://docs.cloud.google.com/sap/docs/sap-ase-guides)
  * [SAP MaxDB guides](https://docs.cloud.google.com/sap/docs/sap-maxdb-guides)
  * [IBM Db2 guides](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-guides)
  * [Oracle Database guides](https://docs.cloud.google.com/sap/docs/oracle-all-guides). To run an Oracle Database with SAP NetWeaver, you must use an SAP-certified version of Oracle Linux. Also, all components of your SAP system must run the same Oracle Linux version. This includes the database, app servers, and any other closely-coupled auxiliary system.
  * [Windows SQL Server guide](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances): when SAP NetWeaver is running on Linux, Windows SQL Server is supported only in 3-tier architectures. 



When SAP NetWeaver and the database server are running on different compute instances in a 3-tier architecture, make sure that your firewall rules are defined to allow communication between the instances.

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

### Prerequisites for the agent

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

To install the agent on a Compute Engine instance, follow these steps:

  1. Establish an SSH connection to your compute instance.
  2. In your terminal, install the agent by running the command that is specific to your operating system: 
     * (Recommended) To install version 3.15 (latest) of the agent: 

### RHEL
           
           sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
           [google-cloud-sap-agent]
           name=Google Cloud Agent for SAP
           baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM
           sudo yum install google-cloud-sap-agent

### SLES15
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent

### SLES 12
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent

     * To install a specific version of the agent: 

### RHEL
           
           sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
           [google-cloud-sap-agent]
           name=Google Cloud Agent for SAP
           baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM
           sudo yum install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES15
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES 12
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent).

For information about downgrading the agent to a specific version, see [ Downgrade Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-downgrade).




After you install Google Cloud's Agent for SAP and the SAP Host Agent, validate the installation of Google Cloud's Agent for SAP, as described in Validate your installation of the agent.

## Installing SAP NetWeaver

For instructions on installing SAP NetWeaver on your new VM, see [the SAP help portal](https://help.sap.com/viewer/p/SAP_NETWEAVER_750) and the [SAP NetWeaver Master Guide](https://help.sap.com/doc/18cb1a50b9924bc3b94c2988cc8c51d9/7.5/en-US/mg_nw_75.pdf).

**Important:** The Software Provisioning Manager (SWPM) chooses the disk drive with the most free space as an installation suggestion for each component. On Google Cloud, it's important that you don't accept the defaults. Be sure to assign the disks to their proper roles in the SWPM dialog boxes.

After you install SAP NetWeaver:

  1. Update the SAP kernel to the minimum supported patch level.

For details on the supported SAP kernel patch levels, see SAP note [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441). 

  2. Install your permanent SAP NetWeaver license.

For more information from SAP about managing your SAP NetWeaver licenses, see [SAP Licensing Procedure](https://help.sap.com/viewer/0643d547dfad4ce497bd7da1264fce77/7.5.6/en-US/fbde4502adef496988fe13d459d66b8b.html).




### Installing the SAP Host Agent

The SAP Host Agent has been enhanced for running on Google Cloud. Ensure that you run at least the minimum SAP Host Agent version required for the Google Cloud environment.

For more information, see the following SAP note [2460297 - SAP on Linux on Google Cloud Platform: Enhanced Monitoring](https://me.sap.com/notes/2460297).

To update your SAP Host Agent by default on a regular basis, see the SAP note [1473974 - Using the SAP Host Agent Auto Upgrade Feature](https://me.sap.com/notes/1473974).

## Validate your installation of Google Cloud's Agent for SAP

After you have deployed a VM and installed your SAP system, validate that Google Cloud's Agent for SAP is functioning properly.

### Verify that Google Cloud's Agent for SAP is running

To verify that the agent is running, follow these steps:

  1. Establish an SSH connection with your Compute Engine instance. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         




If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Evaluate your SAP NetWeaver workload

To automate continuous validation checks for your SAP NetWeaver workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager allows you to automatically scan and evaluate your SAP NetWeaver workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP NetWeaver workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## Troubleshooting

This section contains information about how to correct common issues.

### Troubleshooting communication problems to the database server

If you are setting up a 3-tier SAP system and having connection issues between your VMs, ensure that you have created a firewall rule to allow traffic between VMs on your subnetwork.

### Troubleshooting connecting to your VM

If you are having issues connecting to your VM through `ssh`, ensure that you have created a firewall rule to open port `22` on the Google Cloud network you are using.

For other possible issues, see [Known issues](https://docs.cloud.google.com/compute/docs/ssh-in-browser#known_issues) for SSH from the browser. 

### Troubleshooting Google Cloud's Agent for SAP

To troubleshoot Google Cloud's Agent for SAP, see the [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
