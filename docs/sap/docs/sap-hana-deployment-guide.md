---
url: https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide/
title: Deployment Manager: SAP HANA scale-up deployment guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:44.606509+00:00
---

# Deployment Manager: SAP HANA scale-up deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deployment Manager: SAP HANA scale-up deployment guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reaches end of support on March 31, 2026. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To automate the deployment of an SAP HANA scale-up or multi-host scale-out system on Google Cloud, we recommend that you use Terraform. For more information, see the following guides:

  * [Terraform: SAP HANA scale-up deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf)
  * [Terraform: SAP HANA multi-host scale-out deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-deployment-tf)



This deployment guide shows you how to deploy a SAP HANA system on Google Cloud by using [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/fundamentals) and a configuration file template to define your installation. The guide helps you configure Compute Engine virtual machines (VMs) and persistent disks, as well as the Linux operating system, to achieve the best performance for your SAP HANA system. The Deployment Manager template incorporates best practices from both Compute Engine and SAP.

Use this guide to deploy either a single-host scale-up or a multi-host scale-out SAP HANA system that does not include standby hosts.

If you need to include SAP HANA automatic host failover, use the [SAP HANA Scale-Out System with Host Auto-Failover Deployment Guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-deployment-guide) instead.

If you need to deploy SAP HANA in a Linux high-availability cluster, use one of the following guides:

  * [Terraform: SAP HANA high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment)
  * [Deployment Manager: SAP HANA high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment)
  * The [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * The [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)



## Prerequisites

Before you begin, make sure that you meet the following prerequisites:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide). 
  * You have a Google Cloud account and project.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * Virtual Private Cloud networking is set up with firewall rules or other methods to control access to your VMs.
  * You have access to the SAP HANA installation media.

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata and you are deploying scale-out nodes, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules. If you use the Deployment Manager template that Google Cloud provides, specify a tag with `networkTag: [TAG]`.
    * Create the VMs without an external IP. If you use the Deployment Manager templates that Google Cloud provides, specify `publicIP: No`.



### Setting up your Google account

A Google account is required to work with Google Cloud.

  1. [Sign up for a Google account](https://accounts.google.com/SignUp) if you don't already have one.
  2. (Optional) If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  3. Log in to the Google Cloud console, and [create a new project](https://console.cloud.google.com/project).
  4. [Enable your billing account](https://docs.cloud.google.com/resource-manager/docs/quickstart#create_a_billing_account).
  5. Configure SSH keys so that you are able to use them to SSH into your Compute Engine VM instances. Use the Google Cloud CLI to [create a new SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).
  6. Use the gcloud CLI or Google Cloud console to [add the SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#add_ssh_keys_to_project_metadata) to your project metadata. This allows you to access any Compute Engine VM instance created within this project, except for instances that explicitly disable project-wide SSH keys. 



### Creating a network

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



### Setting up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

### Adding firewall rules

By default, an _implied firewall rule_ blocks incoming connections from outside your Virtual Private Cloud (VPC) network. To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.
  * Communication between VMs in the SAP HANA subnetwork, including communication between nodes in an SAP HANA scale-out system or communication between the database server and application servers in a 3-tier architecture. You can enable communication between VMs by creating a firewall rule to allow traffic that originates from within the subnetwork.
  * SSH connections to your VM instance, including [SSH-in-browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser).
  * Connection to your VM by using a third-party tool in Linux. Create a rule to allow access for the tool through your firewall.

**Note:** The following procedure is a simplified version of the instructions for creating firewall rules. For more detailed instructions, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

To create a firewall rule:

###  Console 

  1. In the Google Cloud console, go to the VPC network **Firewall** page.

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

  2. At the top of the page, click **Create firewall rule**.

     * In the **Network** field, select the network where your VM is located.
     * In the **Targets** field, specify the resources on Google Cloud that this rule applies to. For example, specify **All instances in the network**. Or to to limit the rule to specific instances on Google Cloud, enter tags in **Specified target tags**.
     * In the **Source filter** field, select one of the following: 
       * **IP ranges** to allow incoming traffic from specific IP addresses. Specify the range of IP addresses in the **Source IP ranges** field.
       * **Subnets** to allow incoming traffic from a particular subnetwork. Specify the subnetwork name in the following **Subnets** field. You can use this option to allow access between the VMs in a 3-tier or scaleout configuration.
     * In the **Protocols and ports** section, select **Specified protocols and ports** and enter `tcp:PORT_NUMBER`.
  3. Click **Create** to create your firewall rule.




###  gcloud 

Create a firewall rule by using the following command:
    
    
    $ [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) FIREWALL_NAME
    --direction=INGRESS --priority=1000 \
    --network=NETWORK_NAME --action=ALLOW --rules=PROTOCOL:PORT \
    --source-ranges IP_RANGE --target-tags=NETWORK_TAGS

### Creating a Cloud Storage bucket for the SAP HANA installation files

Before you use Deployment Manager to install SAP HANA on your Compute Engine VM, you must upload the installation files that contain the SAP HANA binaries to a Cloud Storage bucket.

Deployment Manager expects the SAP HANA installation files in the file formats provided by SAP. Depending on your version of SAP HANA, the file format might be ZIP, EXE, or RAR. 

To download the SAP HANA installation files, you must create a Cloud Storage bucket, and then upload the files to that bucket as follows:

  1. Download the base installation files for the required SAP HANA version:

     1. Go to the [SAP Support Portal](https://support.sap.com/en/index.html).
     2. Click **Software Downloads**.
     3. Under the **Installations & Upgrades** tab, click **By Alphabetical Index (A-Z) > H > SAP HANA Platform Edition > SAP HANA Platform Edition 2.0**.
     4. Click **Installation**.
     5. For the required service pack, select the Linux x86_64 distribution, and then click **Download Basket**.

**Note:** We recommend that you download the latest revision of the latest service pack.

If your SAP Support Portal account does not allow access to the software and you believe that you are entitled to the software, then contact the [SAP Global Support Customer Interaction Center](http://support.sap.com/contactus).

  2. Download the files required for upgrading the SAP HANA database to the required version. These files are of the SAR format, and the file names start with `IMDB_SERVER`, `IMDB_CLIENT`, and `IMDB_AFL`.

     1. Go to the [SAP Support Portal](https://support.sap.com/en/index.html).

     2. Click **Software Downloads**.

     3. Navigate to the **Support Packages & Patches** tab.

     4. Click **By Alphabetical Index (A-Z) > H > SAP HANA Platform Edition > SAP HANA Platform Edition 2.0**.

     5. Click the required component. For example, SAP HANA Database 2.0, SAP HANA Client 2.0, or SAP HANA AFL 2.0.

     6. Select the required file, and then click **Download Basket**.

**Note:** You don't need to download the SAPCAR binaries for unpacking the SAR files because the upgrade process uses the local SAPCAR that is available after installing SAP HANA.
  3. In your Google Cloud project, create a Cloud Storage bucket. For instructions, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

The bucket name must be unique across Google Cloud. During bucket creation, choose **Standard** for your storage class.

  4. Configure bucket permissions. By default, as owner of the bucket, you have read-write access to the bucket. To give access to other principals, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  5. Upload the downloaded SAP HANA binaries to the Cloud Storage bucket, or a folder in the bucket. For instructions, see [Uploading objects from a filesystem](https://docs.cloud.google.com/storage/docs/uploading-objects).

  6. Ensure that your bucket or folder contains only one installation file for each file type. For example:
         
         510056441.ZIP
         IMDB_SERVER20_059_11-80002031.SAR
         IMDB_CLIENT20_005_111-80002082.SAR
         IMDB_AFL20_059_11-80002031.SAR
         

  7. Note the name of the bucket and folder to which you uploaded the SAP binaries. You need to use them later when you install SAP HANA.




## Creating a VM with SAP HANA installed

The following instructions use the Deployment Manager to install SAP HANA on one or more VM instances with all of the persistent disks that SAP HANA requires. You define the values for the installation in a Deployment Manager configuration file template.

Deployment Manager treats your SAP HANA system and all of the VMs, disks, and other resources that are created for the SAP HANA system as a single entity called a _deployment_. You can view all of the deployments for your Google Cloud project on the Deployment Manager [Deployments](https://console.cloud.google.com/dm/deployments) page.

**Note:** Do not delete a deployment unless you need to delete everything associated with the deployment, including the SAP HANA system, the VMs, and the persistent disks that were deployed with it. Deployments are a permanent representation of your SAP HANA installation on Google Cloud.

The following instructions use Cloud Shell, but are generally applicable to the Google Cloud CLI.

  1. Confirm that your current quotas for resources such as persistent disks and CPUs are sufficient for the SAP HANA system you are about to install. If your quotas are insufficient, deployment fails. For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to the quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Open the Cloud Shell or, if you installed the Google Cloud CLI on your local workstation, open a terminal.

[Go to the Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `template.yaml` configuration file template to your working directory by entering the following command in the Cloud Shell or gcloud CLI:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/template.yaml

  4. Optionally, rename the template.yaml file to identify the configuration it defines.

  5. Open the `template.yaml` file in Cloud Shell code editor or, if you are using the gcloud CLI, the text editor of your choice.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  6. In the `template.yaml` file, update the following property values by replacing the brackets and their contents with the values for your installation.

Some of the property values that you specify for the SAP HANA system, such as [SID] or [PASSWORD], are subject to rules that are defined by SAP. For more information, see the Parameter Reference in the [SAP HANA Server Installation and Update Guide](https://help.sap.com/viewer/2c1988d620e04368aa4103bf26f17727/LATEST/en-US).

If you want to create a VM instance without installing SAP HANA, delete all of the lines that begin with `sap_hana_`.

Property | Data type | Description  
---|---|---  
type | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
instanceName | String | The name of the VM instance for the SAP HANA master host. The name must be specified in lowercase letters, numbers, or hyphens. If any other characters are used, such as "_" (underscore) or a capital letter, deployment fails. The VM instances for any worker hosts use the same name with a "w" and the host number appended to the name.  
instanceType | String | The type of Compute Engine virtual machine that you need to run SAP HANA on. If you need a custom VM type, specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations).  
zone | String | The zone in which you are deploying your SAP HANA system to run. It must be in the region that you selected for your subnet.   
subnetwork | String | The name of the subnetwork you created in a previous step. If you are deploying to a shared VPC, specify this value as `[SHAREDVPC_PROJECT]/[SUBNETWORK]`. For example, `myproject/network1`.  
linuxImage | String | The name of the Linux operating-system image or image family that you are using with SAP HANA. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-7-4-sap` or `family/sles-12-sp2-sap`. To specify a specific image, specify only the image name. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Cloud console.  
linuxImageProject | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project, such as `rhel-sap-cloud` or `suse-sap-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
sap_hana_deployment_bucket | String | The name of the Cloud Storage bucket in your project that contains the SAP HANA installation and revision files that you uploaded in a previous step. Any upgrade revision files in the bucket are applied to SAP HANA during the deployment process.  
sap_hana_sid | String | The SAP HANA system ID. The ID must consist of three alphanumeric characters and begin with a letter. All letters must be uppercase.  
sap_hana_instance_number | Integer | The instance number, 0 to 99, of the SAP HANA system. The default is 0.  
sap_hana_sidadm_password | String | A temporary password for the operating system administrator. Passwords must be at least eight characters and include at least one uppercase letter, one lowercase letter, and one number. **Caution** : Change the password after the installation is complete.   
sap_hana_system_password | String | A temporary password for the database superuser. Passwords must be at least 8 characters and include at least one uppercase letter, one lowercase letter, and one number. **Caution** : Change the password after the installation is complete.   
sap_hana_scaleout_nodes | Integer | The number of additional SAP HANA worker hosts that you need. The worker hosts are in addition to the primary SAP HANA instance. For example, if you specify `3`, four SAP HANA instances are deployed in a scale-out cluster.  
`sap_hana_shared_nfs` | String | For a multi-host deployment that uses an NFS solution to share the `/hana/shared` volume with the worker hosts, specify the NFS mount point for that volume. For example, `10.151.91.122:/hana_shared_nfs`.  If you don't specify `sap_hana_shared_nfs` but specify a value of 1 or more for `sap_hana_scaleout_nodes`, then the deployment script creates an NFS export for the `/hana/shared` volume on the primary SAP HANA VM instance and shares that volume with the worker nodes for a distributed setup with the required shared `/hana/shared` mount.  This argument is available in Deployment Manager template versions `202302060649` or later. **Note** : The NFS mount point for the `/hana/shared` volume must be empty before you run Deployment Manager.  
`sap_hana_backup_nfs` | String | For a multi-host deployment that uses an NFS solution to share the `/hanabackup` volume with the worker hosts, specify the NFS mount point for that volume. For example, `10.216.41.122:/hana_backup_nfs`.  If you don't specify `sap_hana_backup_nfs` but specify a value of 1 or more for `sap_hana_scaleout_nodes`, then the deployment script creates an NFS export for the `/hanabackup` volume on the primary SAP HANA VM instance and shares that volume with the worker nodes for a distributed setup with the required shared `/hanabackup` mount.  This argument is available in Deployment Manager template versions `202302060649` or later.   
`networkTag` | String | Optional. A network tag that represents your VM instance for firewall or routing purposes. If you specify `publicIP: No` and do not specify a network tag, be sure to provide another means of access to the internet.   
`nic_type` | String | Optional but recommended if available for the target machine and OS version. Specifies the network interface to use with the VM instance. You can specify the value `GVNIC` or `VIRTIO_NET`. To use a [Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) (gVNIC), you need to specify an OS image that supports gVNIC as the value for the `linuxImage` property. For the OS image list, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).  If you do not specify a value for this property, then the network interface is automatically selected based on the machine type that you specify for the `instanceType` property.  This argument is available in Deployment Manager template versions `202302060649` or later.   
`publicIP` | Boolean | Optional. Determines whether a public IP address is added to your VM instance. The default is `Yes`. **Note** : Do not specify `No` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
  
The following example shows a completed configuration file, which directs the Deployment Manager to deploy an `n2-highmem-32` virtual machine with a scale-out HANA system that includes a master SAP HANA instance with three worker hosts. SAP HANA is running on a SLES 15 SP2 operating system.
         
         resources:
         - name: sap_hana
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/sap_hana.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/yyyymmddhhmm/dm-templates/sap_hana/sap_hana.py
           #
           properties:
             instanceName: example-vm
             instanceType: n2-highmem-32
             zone: us-central1-f
             subnetwork: example-subnet-us-central1
             linuxImage: family/sles-15-sp2-sap
             linuxImageProject: suse-sap-cloud
             sap_hana_deployment_bucket: mybucketname
             sap_hana_sid: ABC
             sap_hana_instance_number: 00
             sap_hana_sidadm_password: TempPa55word
             sap_hana_system_password: TempPa55word
             sap_hana_scaleout_nodes: 3

  7. Create the instances:
         
         gcloud deployment-manager deployments create [DEPLOYMENT-NAME] --config [TEMPLATE-NAME].yaml
         

The above command invokes the Deployment Manager, which deploys the VM and persistent disks. Deployment Manager then calls another script that configures the operating system and installs SAP HANA.

While Deployment Manager has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the logs.

Time to completion can vary, but the entire process usually takes less than 30 minutes.




## Verifying deployment

To verify deployment, you check the deployment logs in Cloud Logging and check the disks and services on the VMs of primary and worker hosts.

### Check the logs

  1. In the Google Cloud console, open Cloud Logging to monitor installation progress and check for errors.

**Note:** You might incur costs when completing this step in Cloud Logging. For more information, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing).

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Filter the logs:

     1. In the **Logs Explorer** page, go to the **Query** pane.

     2. From the **Resource** drop-down menu, select **Global** , and then click **Add**.

If you don't see the **Global** option, then in the query editor, enter the following query:
            
            resource.type="global"
            "Deployment"
            

     3. Click **Run query**.

  3. Analyze the filtered logs:

     * If `"--- Finished"` is displayed, then the deployment processing is complete and you can proceed to the next step.
     * If you see a quota error:

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the SAP HANA requirements that are listed in the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#quotas).

       2. On the Deployment Manager [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.

       3. Rerun your deployment.




### Check the configuration of the VM and SAP HANA system

  1. After the SAP HANA system deploys without errors, connect to each VM by using SSH. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for each VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ssh-button.png)

  2. Change to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output similar to the following, with the volumes and sizes that you expect. The following example is from the master node of a scale-out system that has three worker nodes.
         
         example-vm:~ # df -h
         Filesystem                        Size  Used Avail Use% Mounted on
         devtmpfs                          126G  8.0K  126G   1% /dev
         tmpfs                             189G     0  189G   0% /dev/shm
         tmpfs                             126G   18M  126G   1% /run
         tmpfs                             126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                          30G  5.4G   25G  18% /
         /dev/sda2                          20M  2.9M   18M  15% /boot/efi
         /dev/mapper/vg_hana-shared        251G   50G  201G  20% /hana/shared
         /dev/mapper/vg_hana-sap            32G  282M   32G   1% /usr/sap
         /dev/mapper/vg_hana-data          426G  7.4G  419G   2% /hana/data
         /dev/mapper/vg_hana-log           125G  4.3G  121G   4% /hana/log
         /dev/mapper/vg_hanabackup-backup  2.0T  2.1G  2.0T   1% /hanabackup
         tmpfs                              26G     0   26G   0% /run/user/473
         tmpfs                              26G     0   26G   0% /run/user/900
         tmpfs                              26G     0   26G   0% /run/user/1003

  4. Switch to the SAP admin user:
         
         su - SID_LCadm
         

Replace `SID_LC` with the SID value that you specified in the configuration file template. Use lowercase for any letters.

  5. Ensure that SAP HANA services, such as `hdbnameserver`, `hdbindexserver`, and others, are running on the instance:
         
         HDB info
         

  6. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




If any of the validation steps show that the installation failed, resolve any errors, delete the deployment from the [Deployments](https://console.cloud.google.com/dm/deployments) page, and then recreate the instances, as described in the last step of the previous section.

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



## Set up monitoring for SAP HANA

Optionally, you can monitor your SAP HANA instances using Google Cloud's Agent for SAP. From version 2.0, you can configure the agent to collect the SAP HANA monitoring metrics and send them to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Cloud Monitoring lets you create dashboards to visualize these metrics, set up alerts based on metric thresholds, and more.

For more information about the collection of SAP HANA monitoring metrics using Google Cloud's Agent for SAP, see [SAP HANA monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics).

## Installing SAP HANA Studio on a Compute Engine Windows VM

You can connect from a SAP HANA instance outside of Google Cloud or from an instance on Google Cloud. To do so, you might need to enable network access to the target VMs from within SAP HANA Studio.

To install SAP HANA Studio on a Windows VM on Google Cloud, use the following procedure.

  1. Use the Cloud Shell to invoke the following commands.

[OPEN THE CLOUD SHELL](https://console.cloud.google.com/?cloudshell=true)
         
         export NETWORK_NAME="[YOUR_NETWORK_NAME]"
         export REGION="[YOUR_REGION]"
         export ZONE="[YOUR_ZONE]"
         export SUBNET="[YOUR_SUBNETWORK_NAME]"
         export SOURCE_IP_RANGE="[YOUR_WORKSTATION_IP]"
         
         gcloud compute instances create saphanastudio --zone=$ZONE \
         --machine-type=n1-standard-2  --subnet=$SUBNET --tags=hanastudio \
         --image-family=windows-2016  --image-project=windows-cloud \
         --boot-disk-size=100 --boot-disk-type=pd-standard \
         --boot-disk-device-name=saphanastudio
         
         gcloud compute firewall-rules create ${NETWORK_NAME}-allow-rdp \
         --network=$NETWORK_NAME --allow=tcp:3389 --source-ranges=$SOURCE_IP_RANGE \
         --target-tags=hanastudio

The above commands set variables for the current Cloud Shell session, create a Windows server in the subnetwork that you created earlier, and create a firewall rule that allows access from your local workstation to the instance through the [Remote Desktop Protocol](https://wikipedia.org/wiki/Remote_Desktop_Protocol) (RDP).

  2. [Install SAP HANA Studio](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/LATEST/en-US) on this server.

     1. [Upload](https://cloud.google.com/storage/docs/uploading-objects) the SAP HANA Studio installation files and the SAPCAR extraction tool to a Cloud Storage bucket in your Google Cloud project.
     2. Connect to the new Windows VM by using RDP or your preferred method.
     3. In Windows, with administrator permissions, open the Google Cloud CLI Shell or other command-line interface.
     4. Copy the SAP HANA Studio installation files and the SAPCAR extraction tool from the storage bucket to the VM by entering the [`gcloud storage cp` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) in the command interface. For example:
            
            gcloud storage cp gs://[SOURCE_BUCKET]/IMC_STUDIO2_232_0-80000323.SAR C:\[TARGET_DIRECTORY] &
            gcloud storage cp gs://[SOURCE_BUCKET]/SAPCAR_1014-80000938.EXE C:\[TARGET_DIRECTORY]
            

     5. Change the directory to your target directory.
            
            cd C:\[TARGET_DIRECTORY]
            

     6. Run the SAPCAR program to extract the SAP HANA Studio installation file.
            
            SAPCAR_1014-80000938.EXE -xvf IMC_STUDIO2_232_0-80000323.SAR
            

     7. Run the extracted `hdbinst` program to install SAP HANA Studio.




## Enable SAP HANA Fast Restart

Google Cloud **strongly** recommends enabling SAP HANA Fast Restart for each instance of SAP HANA, especially for larger instances. SAP HANA Fast Restart reduces restart time in the event that SAP HANA terminates, but the operating system remains running.

**Note:** If you deploy SAP HANA using Google Cloud's Terraform module `sap_hana` or `sap_hana_ha`, version `202309280828` or later, or the Terraform module `manual_sap_hana_scaleup_ha`, then fast restart is automatically enabled.

As configured by the automation scripts that Google Cloud provides, the operating system and kernel settings already support SAP HANA Fast Restart. You need to define the `tmpfs` file system and configure SAP HANA.

To define the `tmpfs` file system and configure SAP HANA, you can follow the manual steps or use the automation script that Google Cloud provides to enable SAP HANA Fast Restart. For more information, see:

  * Manual steps: Enable SAP HANA Fast Restart
  * Automated steps: Enable SAP HANA Fast Restart



For the complete authoritative instructions for SAP HANA Fast Restart, see the [SAP HANA Fast Restart Option documentation](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/ce158d28135147f099b761f8b1ee43fc.html).

### Manual steps

#### Configure the `tmpfs` file system

After the host VMs and the base SAP HANA systems are successfully deployed, you need to create and mount directories for the NUMA nodes in the `tmpfs` file system.

##### Display the NUMA topology of your VM

Before you can map the required `tmpfs` file system, you need to know how many NUMA nodes your VM has. To display the available NUMA nodes on a Compute Engine VM, enter the following command:
    
    
    lscpu | grep NUMA

For example, an `m2-ultramem-208` VM type has four NUMA nodes, numbered 0-3, as shown in the following example:
    
    
    NUMA node(s):        4
    NUMA node0 CPU(s):   0-25,104-129
    NUMA node1 CPU(s):   26-51,130-155
    NUMA node2 CPU(s):   52-77,156-181
    NUMA node3 CPU(s):   78-103,182-207

##### Create the NUMA node directories

Create a directory for each NUMA node in your VM and set the permissions.

For example, for four NUMA nodes that are numbered 0-3:
    
    
    mkdir -pv /hana/tmpfs{0..3}/SID
    chown -R SID_LCadm:sapsys /hana/tmpfs*/SID
    chmod 777 -R /hana/tmpfs*/SID

##### Mount the NUMA node directories to `tmpfs`

Mount the `tmpfs` file system directories and specify a NUMA node preference for each with `mpol=prefer`:

SID specify the SID with uppercase letters.
    
    
    mount tmpfsSID0 -t tmpfs -o mpol=prefer:0 /hana/tmpfs0/SID
    mount tmpfsSID1 -t tmpfs -o mpol=prefer:1 /hana/tmpfs1/SID
    mount tmpfsSID2 -t tmpfs -o mpol=prefer:2 /hana/tmpfs2/SID
    mount tmpfsSID3 -t tmpfs -o mpol=prefer:3 /hana/tmpfs3/SID

**Note:** if you change machine types and the NUMA nodes increase or decrease, you need to modify the `tmpfs` file system and the `[persistence]` section of the SAP HANA INI file, shown in the next section, to match the new number of NUMA nodes.

##### Update `/etc/fstab`

To ensure that the mount points are available after an operating system reboot, add entries into the file system table, `/etc/fstab`:
    
    
    tmpfsSID0 /hana/tmpfs0/SID tmpfs rw,nofail,relatime,mpol=prefer:0
    tmpfsSID1 /hana/tmpfs1/SID tmpfs rw,nofail,relatime,mpol=prefer:1
    tmpfsSID1 /hana/tmpfs2/SID tmpfs rw,nofail,relatime,mpol=prefer:2
    tmpfsSID1 /hana/tmpfs3/SID tmpfs rw,nofail,relatime,mpol=prefer:3

#### Optional: set limits on memory usage

The `tmpfs` file system can grow and shrink dynamically.

To limit the memory used by the `tmpfs` file system, you can set a size limit for a NUMA node volume with the `size` option. For example:
    
    
    mount tmpfsSID0 -t tmpfs -o mpol=prefer:0,size=250G /hana/tmpfs0/SID

You can also limit overall `tmpfs` memory usage for all NUMA nodes for a given SAP HANA instance and a given server node by setting the `persistent_memory_global_allocation_limit` parameter in the `[memorymanager]` section of the `global.ini` file.

#### SAP HANA configuration for Fast Restart

To configure SAP HANA for Fast Restart, update the `global.ini` file and specify the tables to store in persistent memory.

##### Update the `[persistence]` section in the `global.ini` file

Configure the `[persistence]` section in the SAP HANA `global.ini` file to reference the `tmpfs` locations. Separate each `tmpfs` location with a semicolon:
    
    
    [persistence]
    basepath_datavolumes = /hana/data
    basepath_logvolumes = /hana/log
    basepath_persistent_memory_volumes = /hana/tmpfs0/SID;/hana/tmpfs1/SID;/hana/tmpfs2/SID;/hana/tmpfs3/SID

The preceding example specifies four memory volumes for four NUMA nodes, which corresponds to the `m2-ultramem-208`. If you were running on the `m2-ultramem-416`, you would need to configure eight memory volumes (0..7).

Restart SAP HANA after modifying the `global.ini` file.

SAP HANA can now use the `tmpfs` location as persistent memory space.

##### Specify the tables to store in persistent memory

Specify specific column tables or partitions to store in persistent memory.

For example, to turn on persistent memory for an existing table, execute the SQL query:
    
    
    ALTER TABLE exampletable persistent memory ON immediate CASCADE

To change the default for new tables add the parameter `table_default` in the `indexserver.ini` file. For example:
    
    
    [persistent_memory]
    table_default = ON

For more information on how to control columns, tables and which monitoring views provide detailed information, see [SAP HANA Persistent Memory](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/1f61b13e096d4ef98e62c676debf117e.html).

### Automated steps

The automation script that Google Cloud provides to enable SAP HANA Fast Restart makes changes to directories `/hana/tmpfs*`, file `/etc/fstab`, and SAP HANA configuration. When you run the script, you might need to perform additional steps depending on whether this is the initial deployment of your SAP HANA system or you are resizing your machine to a different NUMA size.

For the initial deployment of your SAP HANA system or resizing the machine to increase the number of NUMA nodes, make sure that SAP HANA is running during the execution of automation script that Google Cloud provides to enable SAP HANA Fast Restart.

When you resize your machine to decrease the number of NUMA nodes, make sure that SAP HANA is stopped during the execution of the automation script that Google Cloud provides to enable SAP HANA Fast Restart. After the script is executed, you need to manually update the SAP HANA configuration to complete the SAP HANA Fast Restart setup. For more information, see SAP HANA configuration for Fast Restart.

**Note:** We strongly recommend that you run the script that Google Cloud provides to enable SAP HANA Fast Restart in a non-production environment and verify the results thoroughly before running the script in production environments. You assume the responsibility for correctly enabling SAP HANA Fast Restart.

To enable SAP HANA Fast Restart, follow these steps:

  1. Establish an SSH connection with your host VM.

  2. Switch to root: 
         
         sudo su -

  3. Download the `sap_lib_hdbfr.sh` script:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/lib/sap_lib_hdbfr.sh

  4. Make the file executable:
         
         chmod +x sap_lib_hdbfr.sh

  5. Verify that the script has no errors: 
         
         vi sap_lib_hdbfr.sh
         ./sap_lib_hdbfr.sh -help

If the command returns an error, contact Cloud Customer Care. For more information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

  6. Run the script after replacing SAP HANA system ID (SID) and password for the SYSTEM user of the SAP HANA database. To securely provide the password, we recommend that you use a secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

Run the script by using the name of a secret in Secret Manager. This secret must exist in the Google Cloud project that contains your host VM instance.
         
         sudo ./sap_lib_hdbfr.sh -h 'SID' -s SECRET_NAME 

Replace the following:

     * `SID`: specify the SID with uppercase letters. For example, `AHA`.
     * `SECRET_NAME`: specify the name of the secret that corresponds to the password for the SYSTEM user of the SAP HANA database. This secret must exist in the Google Cloud project that contains your host VM instance.

Alternatively, you can run the script using a plain text password. After SAP HANA Fast Restart is enabled, make sure to change your password. Using plain text password is not recommended as your password would be recorded in the command-line history of your VM.
    
    sudo ./sap_lib_hdbfr.sh -h 'SID' -p 'PASSWORD'

Replace the following:

     * `SID`: specify the SID with uppercase letters. For example, `AHA`.
     * `PASSWORD`: specify the password for the SYSTEM user of the SAP HANA database.



For a successful initial run, you should see an output similar to the following:
    
    
    INFO - Script is running in standalone mode
    ls: cannot access '/hana/tmpfs*': No such file or directory
    INFO - Setting up HANA Fast Restart for system 'TST/00'.
    INFO - Number of NUMA nodes is 2
    INFO - Number of directories /hana/tmpfs* is 0
    INFO - HANA version 2.57
    INFO - No directories /hana/tmpfs* exist. Assuming initial setup.
    INFO - Creating 2 directories /hana/tmpfs* and mounting them
    INFO - Adding /hana/tmpfs* entries to /etc/fstab. Copy is in /etc/fstab.20220625_030839
    INFO - Updating the HANA configuration.
    INFO - Running command: select * from dummy
    DUMMY
    "X"
    1 row selected (overall time 4124 usec; server time 130 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('persistence', 'basepath_persistent_memory_volumes') = '/hana/tmpfs0/TST;/hana/tmpfs1/TST;'
    0 rows affected (overall time 3570 usec; server time 2239 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('persistent_memory', 'table_unload_action') = 'retain';
    0 rows affected (overall time 4308 usec; server time 2441 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('indexserver.ini', 'SYSTEM') SET ('persistent_memory', 'table_default') = 'ON';
    0 rows affected (overall time 3422 usec; server time 2152 usec)
    

## Connecting to SAP HANA

Note that because these instructions don't use an external IP for SAP HANA, you can only connect to the SAP HANA instances through the bastion instance using SSH or through the Windows server through SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instance(s) by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server instance. After connection, manually [install SAP HANA Studio](https://help.sap.com/hana/SAP_HANA_Studio_Installation_Update_Guide_en.pdf) and access your SAP HANA database.




## Performing post-deployment tasks

Before using your SAP HANA instance, we recommend that you perform the following post-deployment steps. For more information, see [SAP HANA Installation and Update Guide](http://help.sap.com/hana/SAP_HANA_Server_Installation_Guide_en.pdf).

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser. For example:
         
         sudo passwd SID_LCadm

See [Reset the SYSTEM User Password of the System Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/6b13cdd1982f4aa6b90b443663d17d7e.html).

  2. Install your permanent SAP HANA license. If you do not, SAP HANA might go into _database lockdown_ after the temporary license expires.

For more information from SAP about managing your SAP HANA licenses, see [License Keys for the SAP HANA Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/9fd02a6c45eb485b9b3b0bc845586a6a.html).

  3. Update the SAP HANA software with the latest patches.

  4. Install any additional components such as Application Function Libraries (AFL) or Smart Data Access (SDA).

  5. Configure and backup your new SAP HANA database. For more information, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).




## What's next

  * If you need to use Google Cloud NetApp Volumes instead of Persistent Disk or Hyperdisk volumes to host SAP HANA directories such as `/hana/shared` or `/hanabackup`, then see NetApp Volumes deployment information in the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#netapp_cvs).
  * For more information about VM administration of and monitoring, see the [SAP HANA Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
