---
url: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide/
title: Manual VM deployment for IBM Db2 on Linux and Windows for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:49.549403+00:00
---

# Manual VM deployment for IBM Db2 on Linux and Windows for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manual VM deployment for IBM Db2 on Linux and Windows for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This deployment guide shows you how to deploy the Google Cloud resources for an IBM Db2 for Linux, Unix, and Windows system that supports SAP applications.

To use Terraform to automate the deployment of Google Cloud resources for an IBM Db2 instance that supports SAP applications, see [Automated VM deployment for IBM Db2 on Linux](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf).

For details on planning your deployment, see the [IBM Db2 for SAP planning guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide).

## Prerequisites

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

If you don't already have a Google Cloud project with billing enabled, then you must create one before you can deploy a virtual machine (VM) for your IBM Db2 installation.

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




## Deploying a VM for Db2 on Google Cloud

When you create a VM, you can specify several options, including the operating system, region, machine type, and persistent disks.

To create a VM:

  1. In the Google Cloud console, go to the Compute Engine **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. To use a public image, choose a supported image from the list. SAP has certified the following images for IBM Db2 on Google Cloud:

     * Red Hat Enterprise Linux 7.4
     * SUSE Linux Enterprise Server 12 SP2 or later
     * Windows Server 2016 or later
  3. Click **Create Instance**.

  4. Enter a name for your VM. Limit the name to 13 characters, as this is the maximum supported by SAP. For more information, see the SAP note [611361 \- Hostnames of SAP ABAP platform servers](https://me.sap.com/notes/611361).

  5. Select the zone for your VM based on the location of your internal resources and users, and the machine type you want to use.

See the following guides and SAP notes for more details on the zones supported for SAP Netweaver:

     * [SAP Netweaver on Google Cloud planning guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#plan_regions_and_zones)
     * SAP note [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441)
**Note:** The list of zones displayed in the Google Cloud console is randomized within each region to encourage use across multiple zones.
  6. Change the machine type to one of the supported machine types. To see the supported machine types and their persistent-disk limitations, see the [IBM Db2 for SAP planning guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide).

  7. Optionally, in the **Boot disk** section, click **Change**. In the **Boot disk** dialog, you can configure the size and type of your boot disk. After you finish configuring your boot disk, click **Select** to commit your changes.

  8. Expand the **Management, security, disks, networking, sole tenancy** section.

  9. On the **Management** tab, under **Availability policy** , verify that the following defaults are set:

     * To ensure availability of your SAP systems, keep the **Preemptibility** setting set to **Off (recommended)**.
     * To ensure that your VM can restart if there's a maintenance or failure event, keep the **Automatic restart** setting set to **On (recommended)**.
     * To ensure that your VM is migrated to other hardware during infrastructure maintenance, keep the **On host maintenance** setting set to **Migrate VM instance (recommended)**.
  10. On the **Disks** tab, clear the **Delete boot disk when instance is deleted** checkbox.




Next, create a set of disk volumes for your database data, database logs, and stored procedures. For each disk volume, perform the following steps:

  1. On the **Disks** tab, under **Additional disks** , click **Add new disk** to add persistent disks for storage.
  2. Optionally, enter a name in the **Name** field.
  3. Under **Type** , select the disk type for the disk.
  4. Under **Source type** , select **None (blank disk)**.
  5. Specify the size of your disk. Disk sizes are subject to SAP and IBM Db2 requirements. See: 
     * SAP note [1707361 - Inst. Systems Based on NW 7.1 and Higher: UNIX Db2 for LUW](https://launchpad.support.sap.com/#/notes/1707361)
     * The appropriate [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) for your SAP system with IBM Db2
  6. To add the disk, click **Done**.
  7. Repeat the preceding steps for each disk you need for your system.



Finally, configure your networking details and create the VM:

  1. On the **Networking** tab, under **Network interfaces** , choose the network that you created earlier.
  2. On the **SSH Keys** tab, select **Block project-wide SSH keys**.
  3. To create and start the VM, click **Create**.

**Note:** At the bottom of the page, you can click **REST** or **command line** to see the equivalent REST and `gcloud` commands for the instance you are creating. These can be useful for creating additional VMs.

### Connecting to your VM

Next, establish a connection to your VM.

#### Linux

The easiest ways to connect to a Linux VM are to connect from your browser through the Google Cloud console, or from the command line through the Google Cloud CLI. You can also connect to a Linux VM by using common SSH tools.

Alternatively, you can generate a new key-pair for your Linux VM and apply it to your project, which lets you connect by using third-party tools, such as [PuTTY on Windows workstations](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools). For more details, see [Create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).

You can also connect to your VM by using other configurations. For a list of supported environments and known issues, see [SSH from the browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser).

### Console

To connect by using `ssh` directly from your browser in the [Google Cloud console](https://console.cloud.google.com/):

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




### gcloud

The Google Cloud CLI manages your SSH keys for you by generating and applying new project-wide SSH keys when you need them. To connect through the gcloud CLI:
    
    
    gcloud compute ssh VM_NAME

Replace `VM_NAME` with your VM name.

You can now use the terminal to run commands on your Linux VM. When you are done, use the `exit` command to disconnect from the VM.

#### Windows

To connect to a Windows-based VM, you must first generate a password for the VM. You can then connect to the VM by using RDP or PowerShell.

##### Generating passwords

After you create a Windows VM, you must generate a password for the VM before you can connect to it:

  1. In the Google Cloud console, go to the Compute Engine **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the Windows instance where you want to generate a new password.

  3. On the **Instance details** page, click **Create or reset Windows Password**. A password is generated for you.

**Note:** You can change your password later by signing into the system and using the command: 
         
         net user USERNAME NEW_PASSWORD

  4. To create a new user and password, specify a user name.

  5. Click **Set**. Note the username and password so you can sign in to the VM.




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

  1. If you haven't created a username and password on the Windows VM yet, [create or reset your Windows password](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-dm#connecting_to_your_vm).
  2. [Add a firewall rule](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-dm#adding_firewall_rules) or edit your existing firewall rule to open port `5986` on the [Google Cloud network](https://docs.cloud.google.com/compute/docs/networking) where your Windows Server VM is located.
  3. On your local workstation, open the PowerShell terminal.
  4. Optionally, you can initialize a variable to hold your user credentials so you don't need to enter them each time you connect to the instance. If you skip this step, you receive a prompt for your username and password later.
         
         $credentials = Get-Credential
         

  5. Use the [`Enter-PSSession` command](https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.core/enter-pssession) to start a remote PowerShell session and include the flags to use SSL and skip credentials checks.
         
         Enter-PSSession -ComputerName [IP_ADDRESS] -UseSSL -SessionOption
         (New-PSSessionOption -SkipCACheck -SkipCNCheck) -Credential $credentials
         




### Formatting and mounting disk drives

Next, format your disk drives and mount them to your VM.

#### Linux

After you connect to your VM, format and mount your disk drives.

Optionally, you can use Logical Volume Manager (LVM) to format a single disk and split it into the required directories. Both LVM and non-LVM methods are shown in the following procedures.

##### Formatting and mounting disk drives without LVM

To format and mount your disk drives without LVM:

  1. In the terminal where you are connected to your VM, create directories to which you can mount each device:
         
         sudo mkdir -p /db2
          sudo mkdir -p /db2/DBSID
          sudo mkdir -p /db2/DBSID/log_dir
          sudo mkdir -p /db2/DBSID/db2dump
          sudo mkdir -p /db2/DBSID/sapdata
          sudo mkdir -p /db2/DBSID/saptmp
         

  2. In the terminal, use the `ls` command to identify the disks that you want to mount.
         
         ls /dev/disk/by-id/
         

You see an output similar to the following. The disk ID usually includes the name of the disk with a `google-` prefix or a `scsi-0Google_` prefix. This example uses the `google-` ID.
         
         google-example-instance
         google-example-instance-db2
         google-example-instance-db2-dbsid
         google-example-instance-db2-dump
         google-example-instance-db2-log-dir
         google-example-instance-db2-sapdata
         google-example-instance-db2-saptmp
         

  3. Format the disks. If you are using Db2 V11.1, either the `xfs` or `ext4` file system is recommended, because both support the fast preallocation file system feature. Db2 V10.5 doesn't support `xfs` or `ext4`.

The following commands format each disk with a single `ext3` file system and no partition table:
         
         sudo mkfs.ext3 -F /dev/disk/by-id/google-example-instance-db2
         sudo mkfs.ext3 -F /dev/disk/by-id/google-example-instance-db2-dbsid
         sudo mkfs.ext3 -F /dev/disk/by-id/google-example-instance-db2-dump
         sudo mkfs.ext3 -F /dev/disk/by-id/google-example-instance-db2-sapdata
         sudo mkfs.ext3 -F /dev/disk/by-id/google-example-instance-db2-saptmp
         sudo mkfs.ext3 -F /dev/disk/by-id/google-example-instance-db2-log-dir
         

**Note:** For more information about the Db2-supported file systems, see SAP note [405827 - Linux: Recommended file systems](https://launchpad.support.sap.com/#/notes/405827).
  4. Mount each disk to the VM:
         
         sudo mount -o discard,defaults /dev/disk/by-id/google-example-instance-db2 /db2
          sudo mount -o discard,defaults /dev/disk/by-id/google-example-instance-db2-dbsid /db2/DBSID
          sudo mount -o discard,defaults /dev/disk/by-id/google-example-instance-db2-dump /db2/DBSID/db2dump
          sudo mount -o discard,defaults /dev/disk/by-id/google-example-instance-db2-sapdata /db2/DBSID/sapdata
          sudo mount -o discard,defaults /dev/disk/by-id/google-example-instance-db2-saptmp /db2/DBSID/saptmp
          sudo mount -o discard,defaults /dev/disk/by-id/google-example-instance-db2-log-dir /db2/DBSID/log_dir
         

  5. Configure read and write access to the device. For this example, grant write access to the device for all users:
         
         sudo chmod a+w /db2
          sudo chmod a+w /db2/DBSID
          sudo chmod a+w /db2/DBSID/db2dump
          sudo chmod a+w /db2/DBSID/sapdata
          sudo chmod a+w /db2/DBSID/saptmp
          sudo chmod a+w /db2/DBSID/log_dir
         

  6. Optionally, you can add the persistent disks to the `/etc/fstab` file so that the device automatically mounts again when the VM restarts.

When you specify the entry `/etc/fstab` file, include the `nofail` option so that the instance can continue to boot even if the disk isn't present. For example, if you take a snapshot of the boot disk and create a new instance without any persistent disks attached, the instance can continue through the startup process and not pause indefinitely.

  7. Create the `/etc/fstab` entry. Use the `blkid` command to find the UUID for the file system on the device and edit the `/etc/fstab` file to include that UUID with the mount options. You can complete this step with a single command for each disk drive:
         
         echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-example-instance-db2` /db2 ext3 discard,defaults,[NOFAIL] 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-example-instance-db2-dbsid` /db2/DBSID ext3 discard,defaults,[NOFAIL] 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-example-instance-db2-log-dir` /db2/DBSID/log_dir ext3 discard,defaults,[NOFAIL] 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-example-instance-db2-dump` /db2/DBSID/db2dump ext3 discard,defaults,[NOFAIL] 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-example-instance-db2-sapdata` /db2/DBSID/sapdata ext3 discard,defaults,[NOFAIL] 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-example-instance-db2-saptmp` /db2/DBSID/saptmp ext3 discard,defaults,[NOFAIL] 0 2 | sudo tee -a /etc/fstab
         

In this, `[NOFAIL]` is the option that specifies what the system should do if it is unable to mount this disk.

  8. Use the `cat` command to verify that your `/etc/fstab` entries are correct:
         
         cat /etc/fstab
         




If you detach this persistent disk or create a snapshot from the boot disk for this instance, edit the `/etc/fstab` file and remove the entry for this persistent disk. Even with the `nofail` option in place, keep the `/etc/fstab` file in sync with the devices that are attached to your instance and remove these entries before you create your boot disk snapshot.

##### Formatting and mounting drives with LVM

To format and mount a single disk with logical volumes for all required drives by using LVM:

  1. Make sure the disk you have created for your drives is large enough to provide all volumes with the storage that they require. For example, in the following procedure, the size specified for the disk is 100 GB.

  2. Run `pvscan` to scan all disks for physical volumes:
         
         sudo mkdir -p /db2
          sudo mkdir -p /db2/DBSID
          sudo mkdir -p /db2/DBSID/log_dir
          sudo mkdir -p /db2/DBSID/db2dump
          sudo mkdir -p /db2/DBSID/sapdata
          sudo mkdir -p /db2/DBSID/saptmp
         

  3. Initialize the disk or a partition for use by LVM:
         
         pvcreate /dev/sdb
         

  4. Create a volume group:
         
         vgcreate vg_db2 /dev/sdb
         

  5. Create logical volumes for each drive, using the sizes you need:
         
         lvcreate -L 8G -n db2 vg_db2
         lvcreate -L 8G -n db2dbsid vg_db2
         lvcreate -L 8G -n db2logdir vg_db2
         lvcreate -L 8G -n db2dump vg_db2
         lvcreate -L 8G -n db2saptmp vg_db2
         lvcreate -L 50G -n db2sapdata vg_db2
         

  6. Format the volumes. If you are using Db2 V11.1, either the `xfs` or `ext4` file system is recommended, because both support the fast preallocation file system feature. Db2 V10.5 doesn't support `xfs` or `ext4`.

The following commands format each volume with a single `ext3` file system and no partition table:
         
         mkfs -t ext3 /dev/vg_db2/db2
         mkfs -t ext3 /dev/vg_db2/db2dbsid
         mkfs -t ext3 /dev/vg_db2/db2logdir
         mkfs -t ext3 /dev/vg_db2/db2dump
         mkfs -t ext3 /dev/vg_db2/db2saptmp
         mkfs -t ext3 /dev/vg_db2/db2sapdata
         

**Note:** For the Db2-supported file systems, see SAP note [405827 - Linux: Recommended file systems](https://launchpad.support.sap.com/#/notes/405827)
  7. Create a mount point:
         
         mkdir /db2
         

  8. Mount the file systems to the mount point:
         
         sudo mount -o discard,defaults /dev/vg_db2/db2dbsid /db2/DBSID
          mkdir /db2/DBSID/log_dir
          sudo mount -o discard,defaults /dev/vg_db2/db2logdir /db2/DBSID/log_dir
          mkdir /db2/DBSID/db2dump
          sudo mount -o discard,defaults /dev/vg_db2/db2dump /db2/DBSID/db2dump
          mkdir /db2/DBSID/saptmp
          sudo mount -o discard,defaults /dev/vg_db2/db2saptmp /db2/DBSID/saptmp
          mkdir /db2/DBSID/sapdata
          sudo mount -o discard,defaults /dev/vg_db2/db2sapdata /db2/DBSID/sapdata
         

The resulting drives look similar to this:
         
         Filesystem             1K-blocks    Used  Available  Use%  Mounted
         ...                          ...
         dev/mapper/vg_db2-db2    8378368   32976    8345392    1%  /db2
         dev/mapper/vg_db2-db2    8378368   33024    8345344    1%  /db2/DBSID
         dev/mapper/vg_db2-db2   52403200   32976   52370224    1%  /db2/DBSID/sapdata
         dev/mapper/vg_db2-db2    8378368   32976    8345392    1%  /db2/DBSID/saptmp
         dev/mapper/vg_db2-db2    8378368   32976    8345392    1%  /db2/DBSID/log_dir
         dev/mapper/vg_db2-db2    8378368   32976    8345392    1%  /db2/DBSID/db2dump
         

  9. Optionally, you can add the persistent disk to the `/etc/fstab` file so that the device automatically mounts again when the VM restarts.

When you specify the entry `/etc/fstab` file, include the `nofail` option so that the instance can continue to boot even if the disk isn't present. For example, if you take a snapshot of the boot disk and create a new instance without any persistent disks attached, the instance can continue through the startup process and not pause indefinitely.

  10. Create the `/etc/fstab` entry. Use the `blkid` command to find the UUID for the file system on the device and edit the `/etc/fstab` file to include that UUID with the mount options. You can complete this step with a single command for each disk drive:
         
         echo UUID=`sudo blkid -s UUID -o value /dev/vg_db2/db2` /db2 ext3 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/vg_db2/db2dbsid` /db2/DBSID ext3 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/vg_db2/db2logdir` /db2/DBSID/log_dir ext3 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/vg_db2/db2dump` /db2/DBSID/db2dump ext3 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/vg_db2/db2saptmp` /db2/DBSID/saptmp ext3 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
          echo UUID=`sudo blkid -s UUID -o value /dev/vg_db2/db2sapdata` /db2/DBSID/sapdata ext3 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
         

In this, `[NOFAIL]` is the option that specifies what the system should do if it is unable to mount this disk.

  11. Use the `cat` command to verify that your `/etc/fstab` entries are correct:
         
         cat /etc/fstab
         




If you detach this persistent disk or create a snapshot from the boot disk for this instance, edit the `/etc/fstab` file and remove the entry for this persistent disk. Even with the `nofail` option in place, keep the `/etc/fstab` file in sync with the devices that are attached to your instance and remove these entries before you create your boot disk snapshot.

You can also follow a hybrid approach by using LVM to simplify volume resizing and management, while retaining separate persistent disks. This lets you take snapshots of independent volumes, or remove some volumes to instead make use of shared file systems hosted on NFS services such as [Filestore](https://docs.cloud.google.com/filestore/docs) or [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).

#### Windows

After you have connected to your Windows VM, format your disks so that you can begin using them. You also configure the Windows pagefile in the following steps:

  1. From the **Start** menu, search for and open the Server Manager.
  2. Select **File and Storage Services** , and then select **Disks**.

![Server Manager](https://docs.cloud.google.com/static/sap/docs/images/server-mgr-disks.png)

  3. In the **Disks** dialog, right-click the first non-MBR disk, and then click **New Volume**.

  4. Proceed with the defaults and enter a disk label.

  5. When you get to the file-system-settings step, change the **Allocation unit size** to a value from the following list:

     * Database disks: `32` KB
     * Pagefile: `8` KB
     * Other disks: default of `4` KB.
  6. Enter a volume label that describes the disk with a meaningful name.

![New Volume Wizard](https://docs.cloud.google.com/static/compute/docs/tutorials/images/high-perf-sql-new-vol-wiz.png)

  7. Repeat the preceding steps for each additional disk.




### Preparing the operating system

After you format and mount your disk drives, prepare your operating system.

#### Linux

After you create your VM, consult the relevant SAP notes on installation and ensure that your system includes the software components specified:

  * SAP note [1984787 - SUSE LINUX Enterprise Server 12: Installation Notes](https://launchpad.support.sap.com/#/notes/1984787)

**Note:** On SLES 12 SP2, use `zypper update` to update OS packages. Otherwise, some software that runs on Java, such as JDBC, might core dump.
  * SAP note [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)

  * SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)

  * SAP note [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)

  * SAP note [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)




#### Windows

  * If planned, join the Windows Server OS to a domain.
  * [Configure the High Performance power plan](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance#setting_the_power_profile).
  * Calculate the page file size referencing SAP note [1518419: Page file and virtual memory required by the SAP system](https://launchpad.support.sap.com/#/notes/1518419) and [configure the Windows Pagefile](https://help.sap.com/saphelp_nw73ehp1/helpdata/EN/4d/0b7b6d277f5ca8e10000000a42189e/content.htm).



### Installing the database server

Now that your operating system is configured, you can install your IBM Db2 database server.

For guidance on installing SAP NetWeaver with IBM Db2, see the [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) that is specific to your SAP NetWeaver system.

#### Linux

To install IBM Db2 on your VM:

  1. Establish an `ssh` connection to your Linux-based VM.
  2. Download or copy the complete SAP media set for Db2 to your VM. You can download the SAP media set from the [SAP support portal](http://support.sap.com/swdc).
  3. Install the IBM Db2 database server with the SAP Software Provisioning Manager.
  4. Install your IBM Db2 license file. For more information about installing a Db2 license that you obtained from SAP, see the SAP note [816773 - DB6: Installing the Application-Specific Db2 License from SAP](https://me.sap.com/notes/816773).



#### Windows

To install IBM Db2 on your VM:

  1. Use RDP or Windows PowerShell to connect to your Windows-based VM.
  2. Download or copy the complete SAP media set for Db2 to your VM. You can download the SAP media set from the [SAP support portal](http://support.sap.com/swdc).
  3. Install the IBM Db2 database server.
  4. Install your IBM Db2 license file. For more information about installing a Db2 license that you obtained from SAP, see the SAP note [816773 - DB6: Installing the Application-Specific Db2 License from SAP](https://me.sap.com/notes/816773).



## Installing Google Cloud's Agent for SAP

For support and monitoring, Google Cloud provides the _Agent for SAP_ , for SAP workloads running on Compute Engine instances and Bare Metal Solution servers.

As mandated by SAP, to get support from SAP and to enable SAP to meet its service-level agreements (SLAs), you must install Google Cloud's Agent for SAP on all Compute Engine instances and Bare Metal Solution servers that run any SAP system. For more information on the support prerequisites, see [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406).

**Version 3.15 (latest)** of Google Cloud's Agent for SAP is the successor of Google Cloud's monitoring agent for SAP NetWeaver version 2, monitoring agent for SAP HANA version 2, and the Cloud Storage Backint agent for SAP HANA. Therefore, in addition to the collection of metrics, version 3.15 (latest) of Google Cloud's Agent for SAP includes the optional feature: _Backint based backup and recovery for SAP HANA_.

You can opt in to these features that enable products and services such as [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview) for your SAP workloads.

**Note:** SAP Host Agent, with the `saposcol program`, is required on any host that is running an SAP system. SAP Host Agent is installed automatically during the installation of new SAP system instances with SAP kernel 7.20 or higher. For more information, see [SAP Host Agent](https://help.sap.com/docs/SAP%20Host%20Agent/8661d17ee5c047a887f686b33e990ede/e817cfb89dbc4d799825c94da59c7867.html).

You install Google Cloud's Agent for SAP on the host alongside the SAP system. For instructions about how to install and configure the agent, validate your installation, and verify that the agent is running as expected, see [Install the agent on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm). 

If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



## Performing post-deployment tasks

Before using your IBM Db2 instance, we recommend that you perform the following post-deployment steps:

  1. Update your IBM Db2 software with the latest patches, if available.
  2. Install any additional components.
  3. Configure and back up your new IBM Db2 database.



For additional post-deployment guidance, see the Post-installation Tasks section of the [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) that applies to the SAP system that you are using with IBM Db2.

## Troubleshooting

This section contains information about how to correct common issues.

### Troubleshooting connecting to your VM

If you are having issues connecting to your VM through `ssh`, ensure that you have created a firewall rule to open port `22` on the Google Cloud network you are using.

For other possible issues, see [Known issues](https://docs.cloud.google.com/compute/docs/ssh-in-browser#known_issues) for connecting through `ssh` from the browser.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
