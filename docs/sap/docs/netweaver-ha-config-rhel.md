---
url: https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel/
title: HA cluster manual configuration guide for SAP NetWeaver on RHEL \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:12.084835+00:00
---

# HA cluster manual configuration guide for SAP NetWeaver on RHEL  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  HA cluster manual configuration guide for SAP NetWeaver on RHEL Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to deploy and configure a performance-optimized Red Hat Enterprise Linux (RHEL) high-availability (HA) cluster for SAP NetWeaver system.

Except for the procedures that are specific to the Standalone Enqueue Server 2 (ENSA2), which is available only in ABAP, this guide applies to both ABAP and Java SAP NetWeaver stacks. 

Unless an exception is indicated in the guide, examples that use "ASCS" are valid for both ABAP SAP Central Services (ASCS) and Java SAP Central Services (SCS). 

If you are using a Java stack, before you use the commands or examples in this guide, replace any instances of "ASCS" with "SCS". 

This guide includes the steps for: 

  * Configuring an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) to reroute traffic in the event of a failure.
  * Configuring a Pacemaker cluster on RHEL to manage the SAP systems and other resources during a failover. **Note:** From RHEL for SAP 9.0, you can deploy an SAP NetWeaver HA system that uses the Simple Mount file system configuration. For information about how to deploy such a system, see the Red Hat document [Deploying SAP NetWeaver or S/4HANA application server high availability with simple mount](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/pdf/deploying_sap_netweaver_or_s4hana_application_server_high_availability_with_simple_mount/Red_Hat_Enterprise_Linux_for_SAP_Solutions-9-Deploying_SAP_NetWeaver_or_S4HANA_Application_Server_High_Availability_with_simple_mount-en-US.pdf).



This guide also includes steps for configuring the SAP NetWeaver system for HA, but refer to the SAP documentation for the definitive instructions. 

For information about deploying Compute Engine VMs for SAP NetWeaver that is not specific to high-availability, see the [SAP NetWeaver deployment guide](https://docs.cloud.google.com/sap/docs/netweaver-guides) that is specific to your operating system.

To configure an HA cluster for SAP NetWeaver on SUSE Linux Enterprise Server (SLES), see the [HA cluster manual configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles). 

This guide is intended for advanced SAP NetWeaver users who are familiar with Linux high-availability configurations for SAP NetWeaver.

## The system that this guide deploys

Following this guide, you will deploy two SAP NetWeaver instances and set up an HA cluster on RHEL. You deploy each SAP NetWeaver instance on a Compute Engine VM in a different zone within the same region. A high-availability installation of the underlying database is not covered in this guide.

![Overview of a high-availability Linux cluster for a single-node SAP NetWeaver system](https://docs.cloud.google.com/static/sap/docs/images/netweaver-ha-linux.svg)

The deployed cluster includes the following functions and features:

  * Two host VMs, one for the active ASCS instance and one for the active instance of the ENSA2 Enqueue Replicator or the ENSA1 Enqueue Replication Server (ENSA1). Both ENSA2 and ENSA1 instances are referred to as _ERS_.
  * The Pacemaker high-availability cluster resource manager.
  * A STONITH fencing mechanism.
  * Automatic restart of the failed instance as the new secondary instance.

This guide has you use the Cloud Deployment Manager templates that are provided by Google Cloud to deploy the Compute Engine virtual machines (VMs), which ensures that the VMs meet SAP supportability requirements and conform to current best practices. 

To use Terraform to automate the deployment of SAP NetWeaver HA systems, see [Terraform: HA cluster configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel-tf).

## Prerequisites

Before you create the SAP NetWeaver high availability cluster, make sure that the following prerequisites are met:

  * You have read the [SAP NetWeaver planning guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide) and the [High-availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide). 
  * You or your organization has a Google Cloud account and you have created a project for the SAP NetWeaver deployment. For information about creating Google Cloud accounts and projects, see [Creating a project](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-dm#creating_a_project) in the SAP NetWeaver Deployment Guide for Linux.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * If you are using [VPC internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns), then the value of the `vmDnsSetting` variable in your project metadata must be either `GlobalOnly` or `ZonalPreferred` to enable the resolution of the node names across zones. The default setting of `vmDnsSetting` is `ZonalOnly`. For more information, see:

    * [Configuring DNS names for your project or instances](https://docs.cloud.google.com/compute/docs/networking/zonal-dns#setting-zonal-dns)
    * [Querying custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#querying_custom_metadata)
    * [Setting project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide)
  * You have set up a file share using an NFS shared file storage solution, like [Filestore Enterprise](https://cloud.google.com/filestore).

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules.
    * Create the VMs without an external IP.



## Related information from RHEL

Except where required for the Google Cloud environment, the information in this guide is consistent with the following related guides from Red Hat and SAP:

  * [Configure SAP NetWeaver ASCS/ERS ENSA1 with Standalone Resources in RHEL 7.5+ and RHEL 8](https://access.redhat.com/articles/3569681)
  * [Configure SAP S/4HANA ASCS/ERS with Standalone Enqueue Server 2 (ENSA2) in Pacemaker](https://access.redhat.com/articles/3974941)
  * SAP note [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)
  * SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)
  * SAP note [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)
  * SAP note [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)
  * SAP note [2641322 - Installation of ENSA2 and update from ENSA1 to ENSA2 when using the Red Hat HA solutions for SAP](https://launchpad.support.sap.com/#/notes/2641322)



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
  * Cloud Load Balancing health checks. For more information, see Create a firewall rule for the health checks. 

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




## Deploying the VMs for SAP NetWeaver

Before you begin configuring the HA cluster, you define and deploy the VM instances that will serve as the primary and secondary nodes in your HA cluster.

To define and deploy the VMs, you use the same Cloud Deployment Manager template that you use to deploy a VM for an SAP NetWeaver system in the [Automated VM deployment for SAP NetWeaver on Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-dm).

However, to deploy two VMs instead of one, you need to add the definition for the second VM to the configuration file by copying and pasting the definition of the first VM. After you create the second definition, you need to change the resource and instance names in the second definition. To protect against a zonal failure, specify a different zone in the same region. All other property values in the two definitions stay the same.

After the VMs have deployed successfully, you install SAP NetWeaver and define and configure the HA cluster.

The following instructions use the Cloud Shell, but are generally applicable to the Google Cloud CLI.

  1. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the YAML configuration file template, `template.yaml`, to your working directory:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_nw/template.yaml

  3. Optionally, rename the `template.yaml` file to identify the configuration it defines. For example, `nw-ha-rhel-8-4.yaml`.

  4. Open the YAML configuration file in the Cloud Shell code editor by clicking the pencil (_edit_) icon in the upper right corner of Cloud Shell terminal window to launch the editor.

  5. In the YAML configuration file template, define the first VM instance. You define the second VM instance in the next step after the following table.

Specify the property values by replacing the brackets and their contents with the values for your installation. The properties are described in the following table. For an example of a completed configuration file, see Example of a complete YAML configuration file.

Property | Data type | Description  
---|---|---  
`name` | String |  An arbitrary name that identifies the deployment resource that the following set of properties define.  
`type` | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
`instanceName` | String | The name for the VM instance that you are defining. Specify different names in the primary and secondary VM definitions. Consider using names that identify the instances as belonging to the same high-availability cluster.  Instance names must be 13 characters or less and be specified in lowercase letters, numbers, or hyphens. Use a name that is unique within your project.   
`instanceType` | String | The type of Compute Engine VMs that you need. Specify the same instance type for the primary and secondary VMs.  If you need a custom VM type, specify a small [predefined VM type](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types) and, after deployment is complete, [customize the VM](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations) as needed.   
`zone` | String | The Google Cloud zone in which to deploy the VM instance that your are defining. Specify different zones in the same region for the primary and secondary VM definitions. The zones must be in the same region that you selected for your subnet.   
`subnetwork` | String | The name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, specify this value as `SHAREDVPC_PROJECT/SUBNETWORK`. For example, `myproject/network1`.  
`linuxImage` | String | The name of the Linux operating-system image or image family that you are using with SAP NetWeaver. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-8-4-sap-ha`. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.   
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or the Google Cloud image project `rhel-sap-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
`usrsapSize` | Integer | The size of the `/usr/sap` disk. The minimum size is 8 GB.   
`sapmntSize` | Integer | The size of the `/sapmnt` disk. The minimum size is 8 GB.   
`swapSize` | Integer | The size of the swap volume. The minimum size is 1 GB.   
`networkTag` | String |  Optional. One or more comma-separated network tags that represents your VM instance for firewall or routing purposes.  For high-availability configurations, specify a network tag to use for a firewall rule that allows communication between the cluster nodes and a network tag to use in a firewall rule that allows the Cloud Load Balancing health checks to access the cluster nodes.  If you specify `publicIP: No` and do not specify a network tag, be sure to provide another means of access to the internet.   
`serviceAccount` | String |  Optional. Specifies a custom service account to use for the deployed VM. The service account must include the permissions that are required during deployment to configure the VM for SAP.  If `serviceAccount` is not specified, the default Compute Engine service account is used.  Specify the full service account address. For example, `sap-ha-example@example-project-123456.iam.gserviceaccount.com`  
`publicIP` | Boolean | Optional. Determines whether a public IP address is added to your VM instance. The default is `Yes`. **Note** : Do not specify `No` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`sap_deployment_debug` | Boolean | Optional. If this value is set to `Yes`, the deployment generates verbose deployment logs. Do not turn this setting on unless a Google support engineer asks you to enable debugging.   
  6. In the YAML configuration file, create the definition of the second VM by copying the definition of the first VM and pasting the copy after the first definition. For an example, see Example of a complete YAML configuration file.

  7. In the definition of the second VM, specify different values for the following properties than you specified in the first definition:

     * `name`
     * `instanceName`
     * `zone`
  8. Create the VM instances:
         
         gcloud deployment-manager deployments create DEPLOYMENT_NAME --config TEMPLATE_NAME.yaml

where:

     * `DEPLOYMENT_NAME` represents the name of your deployment.
     * `TEMPLATE_NAME` represents the name of your YAML configuration file.

The preceding command invokes the Deployment Manager, which deploys the VMs according to the specifications in the YAML configuration file.

Deployment processing consists of two stages. In the first stage, Deployment Manager writes its status to the console. In the second stage, the deployment scripts write their status to Cloud Logging.




### Example of a complete YAML configuration file

The following example shows a completed YAML configuration file that deploys two VM instances for an HA configuration for SAP NetWeaver by using the latest version of the Deployment Manager templates. The example omits the comments that the template contains when you first download it.

The file contains the definitions of two resources to deploy: `sap_nw_node_1` and `sap_nw_node_2`. Each resource definition contains the definitions for a VM.

The `sap_nw_node_2` resource definition was created by copying and pasting the first definition, and then modifying the values of `name`, `instanceName`, and `zone` properties. All other property values in the two resource definitions are the same.

The properties `networkTag` and `serviceAccount` are from the Advanced Options section of the configuration file template.
    
    
    resources:
    - name: sap_nw_node_1
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_nw/sap_nw.py
      properties:
        instanceName: nw-ha-vm-1
        instanceType: n2-standard-4
        zone: us-central1-b
        subnetwork: example-sub-network-sap
        linuxImage: family/rhel-8-4-sap-ha
        linuxImageProject: rhel-sap-cloud
        usrsapSize: 15  
    sapmntSize: 15
        swapSize: 24
        networkTag: cluster-ntwk-tag,allow-health-check
        serviceAccount: limited-roles@example-project-123456.iam.gserviceaccount.com
    - name: sap_nw_node_2
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_nw/sap_nw.py
      properties:
        instanceName: nw-ha-vm-2
        instanceType: n2-standard-4
        zone: us-central1-c
        subnetwork: example-sub-network-sap
        linuxImage: family/rhel-8-4-sap-ha
        linuxImageProject: rhel-sap-cloud
        usrsapSize: 15  
    sapmntSize: 15
        swapSize: 24
        networkTag: cluster-ntwk-tag,allow-health-check
        serviceAccount: limited-roles@example-project-123456.iam.gserviceaccount.com

## Create firewall rules that allow access to the host VMs

If you haven't done so already, create firewall rules that allow access to each host VM from the following sources:

  * For configuration purposes, your local workstation, a bastion host, or a jump server
  * For access between the cluster nodes, the other host VMs in the HA cluster
  * The health checks that are used by Cloud Load Balancing, as described in the later step Create a firewall rule for the health checks.



When you create VPC firewall rules, you specify the network tags that you defined in the `template.yaml` configuration file to designate your host VMs as the target for the rule.

To verify deployment, define a rule to allow SSH connections on port 22 from a bastion host or your local workstation.

For access between the cluster nodes, add a firewall rule that allows all connection types on any port from other VMs in the same subnetwork.

Make sure that the firewall rules for verifying deployment and for intra-cluster communication are created before proceeding to the next section. For instructions, see Adding firewall rules.

## Verifying the deployment of the VMs

Before you install SAP NetWeaver or begin configuring the HA cluster, verify that the VMs were deployed correctly by checking the logs and the OS storage mapping.

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

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the SAP NetWeaver requirements that are listed in the [SAP NetWeaver planning guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#pricing-and-quotas).

       2. On the Deployment Manager [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.

       3. Rerun your deployment.




### Check the configuration of the VMs

  1. After the VM instances deploy, connect to the VMs by using `ssh`.

     1. If you haven't already done so, create a firewall rule to allow an SSH connection on port `22`.
     2. Go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

     3. Connect to each VM instance by clicking the **SSH** button on the entry for each VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/netweaver-ha-ssh-button.png)

  2. Display the file system:
         
         ~> df -h

Ensure that you see output similar to the following:
         
         Filesystem                 Size  Used Avail Use% Mounted on
         devtmpfs                    32G  8.0K   32G   1% /dev
         tmpfs                       48G     0   48G   0% /dev/shm
         tmpfs                       32G  402M   32G   2% /run
         tmpfs                       32G     0   32G   0% /sys/fs/cgroup
         /dev/sda3                   30G  3.4G   27G  12% /
         /dev/sda2                   20M  3.7M   17M  19% /boot/efi
         /dev/mapper/vg_usrsap-vol   15G   48M   15G   1% /usr/sap  
         /dev/mapper/vg_sapmnt-vol   15G   48M   15G   1% /sapmnt
         tmpfs                      6.3G     0  6.3G   0% /run/user/1002
         tmpfs                      6.3G     0  6.3G   0% /run/user/0

  3. Confirm that the swap space was created:
         
         ~> cat /proc/meminfo | grep Swap

You see results similar to the following example:
         
         SwapCached:            0 kB
         SwapTotal:      25161724 kB
         SwapFree:       25161724 kB




If any of the validation steps show that the installation failed:

  1. Correct the error.
  2. On the [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.
  3. Rerun your deployment.



## Enable load balancer back-end communication between the VMs

After you have confirmed that the VMs deployed successfully, enable backend communication between the VMs that will serve as the nodes in your HA cluster.

You enable backend communication between the VMs by modifying the configuration of the `google-guest-agent`, which is included in the [Linux guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#linux) for all Linux public images that are provided by Google Cloud.

To enable load balancer back-end communications, perform the following steps on each VM that is a part of your cluster:

  1. Stop the agent:
         
         sudo service google-guest-agent stop

  2. Open or create the file `/etc/default/instance_configs.cfg` for editing. For example:
         
         sudo vi /etc/default/instance_configs.cfg

  3. In the `/etc/default/instance_configs.cfg` file, specify the following configuration properties as shown. If the sections don't exist, create them. In particular, make sure that both the `target_instance_ips` and `ip_forwarding` properties are set to `false`:
         
         [IpForwarding]
         ethernet_proto_id = 66
         ip_aliases = true
         **target_instance_ips = false**
         
         [NetworkInterfaces]
         dhclient_script = /sbin/google-dhclient-script
         dhcp_command =
         **ip_forwarding = false**
         setup = true
         

  4. Start the guest agent service:
         
         sudo service google-guest-agent start




The load balancer health check configuration requires both a listening target port for the health check and an assignment of the virtual IP to an interface. For more information, see [Test the load balancer configuration](https://cloud.google.com/sap/docs/netweaver-ha-config-sles#test_the_load_balancer_configuration).

## Configure SSH keys on the primary and secondary VMs

To let files to be copied between the hosts in the HA cluster, the steps in this section create root SSH connections between the two hosts.

The Deployment Manager templates that Google Cloud provides generate a key for you, but you can replace it with a key you generate if needed.

Your organization is likely to have guidelines that govern internal network communications. If necessary, after deployment is complete you can remove the metadata from the VMs and the keys from the `authorized_keys` directory.

If setting up direct SSH connections does not comply with your organization's guidelines, then you can transfer files by using other methods, such as:

  * Transfer smaller files through your local workstation by using the Cloud Shell **Upload file** and **Download file** menu options. See [Managing files with Cloud Shell](https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files).
  * Exchange files using a Cloud Storage bucket. See [Object uploads](https://docs.cloud.google.com/storage/docs/uploads) and [Object downloads](https://docs.cloud.google.com/storage/docs/reads-and-downloads).
  * Use a file storage solution such as Filestore or Google Cloud NetApp Volumes to create a shared folder. See [File sharing solutions](https://docs.cloud.google.com/sap/docs/filers-for-sap).



To enable SSH connections between the primary and secondary instances, follow these steps. The steps assume that you are using the SSH key that is generated by the Deployment Manager templates for SAP.

  1. On the primary host VM:

     1. Connect to the VM via SSH.

     2. Switch to root:
            
            $ sudo su -

     3. Confirm that the SSH key exists:
            
            # ls -l /root/.ssh/

You should see the id_rsa key files as in the following example:
            
            -rw-r--r-- 1 root root  569 May  4 23:07 authorized_keys
            -rw------- 1 root root 2459 May  4 23:07 id_rsa
            -rw-r--r-- 1 root root  569 May  4 23:07 id_rsa.pub

     4. Update the primary VM's metadata with information about the SSH key for the secondary VM.
            
            # gcloud compute instances add-metadata SECONDARY_VM_NAME \
            --metadata "ssh-keys=$(whoami):$(cat ~/.ssh/id_rsa.pub)" \
            --zone SECONDARY_VM_ZONE

     5. Confirm that the SSH keys are set up properly by opening an SSH connection from the primary system to the secondary system:
            
            # ssh SECONDARY_VM_NAME

  2. On the secondary host VM:

     1. SSH into the VM.

     2. Switch to root:
            
            $ sudo su -

     3. Confirm that the ssh key exists:
            
            # ls -l /root/.ssh/

You should see the id_rsa key files as in the following example:
            
            -rw-r--r-- 1 root root  569 May  4 23:07 authorized_keys
            -rw------- 1 root root 2459 May  4 23:07 id_rsa
            -rw-r--r-- 1 root root  569 May  4 23:07 id_rsa.pub

     4. Update the secondary VM's metadata with information about the SSH key for the primary VM.
            
            # gcloud compute instances add-metadata PRIMARY_VM_NAME \
            --metadata "ssh-keys=$(whoami):$(cat ~/.ssh/id_rsa.pub)" \
            --zone PRIMARY_VM_ZONE
            
            # cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

     5. Confirm that the SSH keys are set up properly by opening an SSH connection from the secondary system to the primary system.
            
            # ssh PRIMARY_VM_NAME




## Set up shared file storage and configure the shared directories

You need to set up an NFS file sharing solution that provides highly-available shared file storage that both nodes of your HA cluster can access. You then create directories on both nodes that map to the shared file storage. The cluster software ensures that the appropriate directories mounted only on the correct instances. **Note:** From RHEL for SAP 9.0, you can deploy an SAP NetWeaver HA system that uses the Simple Mount file system configuration. For information about how to deploy such a system, see the Red Hat document [Deploying SAP NetWeaver or S/4HANA application server high availability with simple mount](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_for_sap_solutions/9/pdf/deploying_sap_netweaver_or_s4hana_application_server_high_availability_with_simple_mount/Red_Hat_Enterprise_Linux_for_SAP_Solutions-9-Deploying_SAP_NetWeaver_or_S4HANA_Application_Server_High_Availability_with_simple_mount-en-US.pdf).

Setting up a file sharing solution is not covered in this guide. For instructions on setting up the file sharing system, see the instructions provided by the vendor of the solution you select. If you choose to use Filestore for your file sharing solution, we recommend using the [Enterprise tier](https://docs.cloud.google.com/filestore/docs/service-tiers) of Filestore. To learn how to create a Filestore instance, see [Creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances).

For information about file sharing solutions that are available on Google Cloud, see [Shared storage options for HA SAP systems on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide#ha-storage-options).

To configure the shared directories:

  1. If you did not already set up a highly available NFS shared file storage solution, do so now.

  2. Mount the NFS shared storage on both servers for initial configuration.
         
         ~> sudo mkdir /mnt/nfs
         ~> sudo mount -t nfs NFS_PATH /mnt/nfs

Replace `NFS_PATH` with the path to your NFS file share solution. For example, `10.49.153.26:/nfs_share_nw_ha`.

  3. From either server, create directories for `sapmnt`, the central transport directory and the instance-specific directory. If you are using a Java stack, replace "ASCS" with "SCS" before you use the following and any other example commands:
         
         ~> sudo mkdir /mnt/nfs/sapmntSID
         ~> sudo mkdir /mnt/nfs/usrsap{trans,SIDASCSASCS_INSTANCE_NUMBER,SIDERSERS_INSTANCE_NUMBER}

  4. On both servers, create the necessary mount points:
         
         ~> sudo mkdir -p /sapmnt/SID
         ~> sudo mkdir -p /usr/sap/trans
         ~> sudo mkdir -p /usr/sap/SID/ASCSASCS_INSTANCE_NUMBER
         ~> sudo mkdir -p /usr/sap/SID/ERSERS_INSTANCE_NUMBER

  5. Configure `autofs` to mount the common shared file directories when the file directories are first accessed. The mounting of the `ASCSASCS_INSTANCE_NUMBER` and `ERSERS_INSTANCE_NUMBER` directories is managed by the cluster software, which you configure in a later step.

Adjust the NFS options in the commands as needed for your file-sharing solution.

On both servers, configure `autofs`:
         
         ~> echo "/- /etc/auto.sap" | sudo tee -a /etc/auto.master
         ~> NFS_OPTS="-rw,relatime,vers=3,hard,proto=tcp,timeo=600,retrans=2,mountvers=3,mountport=2050,mountproto=tcp"
         ~> echo "/sapmnt/SID ${NFS_OPTS} NFS_PATH/sapmntSID" | sudo tee -a /etc/auto.sap
         ~> echo "/usr/sap/trans ${NFS_OPTS} NFS_PATH/usrsaptrans" | sudo tee -a /etc/auto.sap

For information about `autofs`, see [autofs - how it works](https://www.kernel.org/doc/html/latest/filesystems/autofs.html).

  6. On both servers, start the `autofs` service:
         
         ~> sudo systemctl enable autofs
         ~> sudo systemctl restart autofs
         ~> sudo automount -v

  7. Trigger `autofs` to mount shared directories by accessing each directory by using the `cd` command. For example:
         
         ~> cd /sapmnt/SID
         ~> cd /usr/sap/trans
         

  8. After you access all the directories, issue the `df -Th` command to confirm the directories are mounted.
         
         ~> df -Th | grep FILE_SHARE_NAME

Replace `FILE_SHARE_NAME` with the name of your NFS file share solution. For example, `nfs_share_nw_ha`.

You see mount points and directories similar to the following example:
         
         10.49.153.26:/nfs_share_nw_ha              nfs      1007G   76M  956G   1% /mnt/nfs
         10.49.153.26:/nfs_share_nw_ha/usrsaptrans  nfs      1007G   76M  956G   1% /usr/sap/trans
         10.49.153.26:/nfs_share_nw_ha/sapmntAHA    nfs      1007G   76M  956G   1% /sapmnt/AHA




## Configure the Cloud Load Balancing failover support

The internal passthrough Network Load Balancer service with failover support routes the ASCS and ERS traffic to the active instances of each in an SAP NetWeaver cluster. Internal passthrough Network Load Balancers use virtual IP (VIP) addresses, backend services, instance groups, and health checks to route the traffic appropriately.

### Reserve IP addresses for the virtual IPs

For an SAP NetWeaver high-availability cluster, you create two VIPs, which are sometimes referred to as _floating_ IP addresses. One VIP follows the active SAP Central Services (SCS) instance and the other follows the Enqueue Replication Server (ERS) instance. The load balancer routes traffic that is sent to each VIP to the VM that is currently hosting the active instance of the ASCS or ERS component of the VIP.

  1. Open Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address for the virtual IP of the ASCS and for the VIP of the ERS. For ASCS, the IP address is the IP address that applications use to access SAP NetWeaver. For ERS, the IP address is the IP address that is used for Enqueue Server replication. If you omit the `--addresses` flag, then an IP address in the specified subnet is chosen for you:
         
         ~ [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) ASCS_VIP_NAME \
           --region CLUSTER_REGION --subnet CLUSTER_SUBNET \
           --addresses ASCS_VIP_ADDRESS
         
         ~ [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) ERS_VIP_NAME \
           --region CLUSTER_REGION --subnet CLUSTER_SUBNET \
           --addresses ERS_VIP_ADDRESS

Replace the following:

     * `ASCS_VIP_NAME`: specify a name for the virtual IP address of the ASCS instance. For example, `ascs-aha-vip`. 
     * `CLUSTER_REGION`: specify the Google Cloud region in which your cluster is located. For example, `us-central1`
     * `CLUSTER_SUBNET`: specify the subnetwork that you are using with your cluster. For example, `example-sub-network-sap`. 
     * `ASCS_VIP_ADDRESS`: optionally, specify an IP address for the ASCS virtual IP in CIDR notation. For example, `10.1.0.2`. 
     * `ERS_VIP_NAME`: specify a name for the virtual IP address of the ERS instance. For example, `ers-aha-vip`.
     * `ERS_VIP_ADDRESS`: optionally, specify an IP address for the ERS virtual IP in CIDR notation. For example, `10.1.0.4`. 

For more information about reserving a static IP, see [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

  3. Confirm IP address reservation:
         
         ~ [gcloud compute addresses describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) VIP_NAME \
           --region CLUSTER_REGION

You should see output similar to the following example:
         
         **address: 10.1.0.2**
         addressType: INTERNAL
         creationTimestamp: '2022-04-04T15:04:25.872-07:00'
         description: ''
         id: '555067171183973766'
         kind: compute#address
         **name: ascs-aha-vip**
         networkTier: PREMIUM
         purpose: GCE_ENDPOINT
         region: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/addresses/ascs-aha-vip
         **status: RESERVED**
         subnetwork: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/subnetworks/example-sub-network-sap




### Define host names for the VIP address in `/etc/hosts`

Define a host name for each VIP address and then add the IP addresses and host names for both the VMs and the VIPs to the `/etc/hosts` file on each VM.

The VIP host names are not known outside of the VMs unless you also add them to your DNS service. Adding these entries to the local `/etc/hosts` file protects your cluster from any disruptions to your DNS service.

Your updates to the `/etc/hosts` file should look similar to the following example:
    
    
    127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
    ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
    10.1.0.113 nw-ha-vm-2.us-central1-c.c.example-project-123456.internal nw-ha-vm-2
    10.1.0.2   ascs-aha-vip
    10.1.0.4   ers-aha-vip
    10.1.0.114 nw-ha-vm-1.us-central1-b.c.example-project-123456.internal nw-ha-vm-1  # Added by Google
    169.254.169.254 metadata.google.internal  # Added by Google

### Create the Cloud Load Balancing health checks

Create health checks: one for the active ASCS instance and one for the active ERS.

  1. In Cloud Shell, create the health checks. To avoid clashing with other services, designate port numbers for the ASCS and ERS instances in the private range, 49152-65535. The check-interval and timeout values in the following commands are slightly longer than the defaults so as to increase failover tolerance during Compute Engine live migration events. You can adjust the values, if necessary:

     1. ~ [gcloud compute health-checks create tcp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp) ASCS_HEALTH_CHECK_NAME \
            --port=ASCS_HEALTHCHECK_PORT_NUM --proxy-header=NONE --check-interval=10 --timeout=10 \
            --unhealthy-threshold=2 --healthy-threshold=2

     2. ~ [gcloud compute health-checks create tcp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp) ERS_HEALTH_CHECK_NAME \
            --port=ERS_HEALTHCHECK_PORT_NUM --proxy-header=NONE --check-interval=10 --timeout=10 \
            --unhealthy-threshold=2 --healthy-threshold=2

  2. Confirm the creation of each health check:
         
         ~ [gcloud compute health-checks describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/describe) HEALTH_CHECK_NAME

You should see output similar to the following example:
         
         checkIntervalSec: 10
         creationTimestamp: '2021-05-12T15:12:21.892-07:00'
         healthyThreshold: 2
         id: '1981070199800065066'
         kind: compute#healthCheck
         name: ascs-aha-health-check-name
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/scs-aha-health-check-name
         tcpHealthCheck:
           port: 60000
           portSpecification: USE_FIXED_PORT
           proxyHeader: NONE
         timeoutSec: 10
         type: TCP
         unhealthyThreshold: 2




### Create a firewall rule for the health checks

If you haven't done so already, define a firewall rule for a port in the private range that allows access to your host VMs from the IP ranges that are used by Cloud Load Balancing health checks, `35.191.0.0/16` and `130.211.0.0/22`. For more information about firewall rules for load balancers, see [Creating firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

  1. If you don't already have one, add a network tag to your host VMs. This network tag is used by the firewall rule for health checks.

     * ~ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags)  PRIMARY_VM_NAME \
           --zone=PRIMARY_ZONE \
           --tags NETWORK_TAGS

     * ~ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags)  SECONDARY_VM_NAME \
           --zone=SECONDARY_ZONE \
           --tags NETWORK_TAGS

  2. Create a firewall rule that uses the network tag to allow the health checks:
         
         ~ [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)  RULE_NAME \
           --network=NETWORK_NAME \
           --action=ALLOW \
           --direction=INGRESS \
           --source-ranges=35.191.0.0/16,130.211.0.0/22 \
           --target-tags=NETWORK_TAGS \
           --rules=tcp:ASCS_HEALTHCHECK_PORT_NUM,tcp:ERS_HEALTHCHECK_PORT_NUM

For example:
         
         gcloud compute firewall-rules create  nw-ha-cluster-health-checks \
         --network=example-network \
         --action=ALLOW \
         --direction=INGRESS \
         --source-ranges=35.191.0.0/16,130.211.0.0/22 \
         --target-tags=allow-health-check \
         --rules=tcp:60000,tcp:60010




### Create Compute Engine instance groups

You need to create an instance group in each zone that contains a cluster-node VM and add the VM in that zone to the instance group.

  1. In Cloud Shell, create the primary instance group and add the primary VM to it:

     1. ~ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) PRIMARY_IG_NAME \
            --zone=PRIMARY_ZONE

     2. ~ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) PRIMARY_IG_NAME \
            --zone=PRIMARY_ZONE \
            --instances=PRIMARY_VM_NAME

  2. In Cloud Shell, create the secondary instance group and add the secondary VM to it:

     1. ~ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) SECONDARY_IG_NAME \
            --zone=SECONDARY_ZONE

     2. ~ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) SECONDARY_IG_NAME \
            --zone=SECONDARY_ZONE \
            --instances=SECONDARY_VM_NAME

  3. Confirm the creation of the instance groups:
         
         ~ [gcloud compute instance-groups unmanaged list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/list)

You should see output similar to the following example:
         
         NAME                              ZONE           NETWORK              NETWORK_PROJECT        MANAGED  INSTANCES
         sap-aha-primary-instance-group    us-central1-b  example-network-sap  example-project-123456  No       1
         sap-aha-secondary-instance-group  us-central1-c  example-network-sap  example-project-123456  No       1
         




### Configure the backend services

Create two backend services, one for ASCS and one for ERS. Add both instance groups to each backend service, designating the opposite instance group as the failover instance group in each backend service. Finally, create forwarding rules from the VIPs to the backend services.

  1. In Cloud Shell, create the backend service and failover group for ASCS:

     1. Create the backend service for ASCS:
            
            ~ [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) ASCS_BACKEND_SERVICE_NAME \
               --load-balancing-scheme internal \
               --health-checks ASCS_HEALTH_CHECK_NAME \
               --no-connection-drain-on-failover \
               --drop-traffic-if-unhealthy \
               --failover-ratio 1.0 \
               --region CLUSTER_REGION \
               --global-health-checks

     2. Add the primary instance group to the ASCS backend service:
            
            ~ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) ASCS_BACKEND_SERVICE_NAME \
              --instance-group PRIMARY_IG_NAME \
              --instance-group-zone PRIMARY_ZONE \
              --region CLUSTER_REGION

     3. Add the secondary instance group as the failover instance group for the ASCS backend service:
            
            ~ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) ASCS_BACKEND_SERVICE_NAME \
              --instance-group SECONDARY_IG_NAME \
              --instance-group-zone SECONDARY_ZONE \
              --failover \
              --region CLUSTER_REGION

  2. In Cloud Shell, create the backend service and failover group for ERS:

     1. Create the backend service for ERS:
            
            ~ [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) ERS_BACKEND_SERVICE_NAME \
            --load-balancing-scheme internal \
            --health-checks ERS_HEALTH_CHECK_NAME \
            --no-connection-drain-on-failover \
            --drop-traffic-if-unhealthy \
            --failover-ratio 1.0 \
            --region CLUSTER_REGION \
            --global-health-checks

     2. Add the secondary instance group to the ERS backend service:
            
            ~ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) ERS_BACKEND_SERVICE_NAME \
              --instance-group SECONDARY_IG_NAME \
              --instance-group-zone SECONDARY_ZONE \
              --region CLUSTER_REGION

     3. Add the primary instance group as the failover instance group for the ERS backend service:
            
            ~ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) ERS_BACKEND_SERVICE_NAME \
              --instance-group PRIMARY_IG_NAME \
              --instance-group-zone PRIMARY_ZONE \
              --failover \
              --region CLUSTER_REGION

  3. Optionally, confirm that the backend services contain the instance groups as expected:
         
         ~ [gcloud compute backend-services describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/describe) BACKEND_SERVICE_NAME \
          --region=CLUSTER_REGION

You should see output similar to the following example for the ASCS backend service. For ERS, `failover: true` would appear on the primary instance group:
         
         **backends:**
         - balancingMode: CONNECTION
           **group: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instanceGroups/sap-aha-primary-instance-group**
         - balancingMode: CONNECTION
           **failover: true
           group: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/sap-aha-secondary-instance-group**
         connectionDraining:
           drainingTimeoutSec: 0
         creationTimestamp: '2022-04-06T10:58:37.744-07:00'
         description: ''
         failoverPolicy:
           disableConnectionDrainOnFailover: true
           dropTrafficIfUnhealthy: true
           failoverRatio: 1.0
         fingerprint: s4qMEAyhrV0=
         healthChecks:
         - https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/ascs-aha-health-check-name
         id: '6695034709671438882'
         kind: compute#backendService
         loadBalancingScheme: INTERNAL
         name: ascs-aha-backend-service-name
         protocol: TCP
         region: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/backendServices/ascs-aha-backend-service-name
         sessionAffinity: NONE
         timeoutSec: 30

  4. In Cloud Shell, create forwarding rules for the ASCS and ERS backend services:

     1. Create the forwarding rule from the ASCS VIP to the ASCS backend service:
            
            ~ [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) ASCS_FORWARDING_RULE_NAME \
            --load-balancing-scheme internal \
            --address ASCS_VIP_ADDRESS \
            --subnet CLUSTER_SUBNET \
            --region CLUSTER_REGION \
            --backend-service ASCS_BACKEND_SERVICE_NAME \
            --ports ALL

     2. Create the forwarding rule from the ERS VIP to the ERS backend service:
            
            ~ [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) ERS_FORWARDING_RULE_NAME \
            --load-balancing-scheme internal \
            --address ERS_VIP_ADDRESS \
            --subnet CLUSTER_SUBNET \
            --region CLUSTER_REGION \
            --backend-service ERS_BACKEND_SERVICE_NAME \
            --ports ALL


**Note:** Your backend instance groups won't register as healthy until you have completed the Pacemaker cluster configuration.

### Test the load balancer configuration

Even though your backend instance groups won't register as healthy until later, you can test the load balancer configuration by setting up a listener to respond to the health checks. After setting up a listener, if the load balancer is configured correctly, the status of the backend instance groups changes to healthy.

The following sections present different methods that you can use to test the configuration.

#### Testing the load balancer with the `socat` utility

You can use the `socat` utility to temporarily listen on a health check port. 

  1. On both host VMs, install the `socat` utility:
         
         $ sudo yum install socat

  2. On the primary VM, assign the VIP to the 'lo' loopback interface temporarily:
         
         ip addr add VIP_ADDRESS dev lo

  3. On the primary VM, start a `socat` process to listen for 60 seconds on the ASCS health check port:
         
         $ timeout 60s socat - TCP-LISTEN:ASCS_HEALTHCHECK_PORT_NUM,fork

  4. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your ASCS backend instance group:
         
         ~ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) ASCS_BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following example for ASCS:
         
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instanceGroups/sap-aha-primary-instance-group
         status:
           healthStatus:
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/forwardingRules/scs-aha-forwarding-rule
             **forwardingRuleIp: 10.1.0.90
             healthState: HEALTHY**
             instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instances/nw-ha-vm-1
             **ipAddress: 10.1.0.89**
             port: 80
           kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/sap-aha-secondary-instance-group
         status:
           healthStatus:
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/forwardingRules/scs-aha-forwarding-rule
             **forwardingRuleIp: 10.1.0.90
             healthState: UNHEALTHY**
             instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/nw-ha-vm-2
             **ipAddress: 10.1.0.88**
             port: 80
           kind: compute#backendServiceGroupHealth

  5. Remove the VIP from the lo interface:
         
         ip addr del VIP_ADDRESS dev lo

  6. Repeat the steps for ERS, replacing the ASCS variable values with the ERS values.




#### Testing the load balancer using port 22

If port `22` is open for SSH connections on your host VMs, then you can temporarily edit the health checker to use port `22`, which has a listener that can respond to the health checker.

To temporarily use port `22`, follow these steps:

  1. In the Google Cloud console, go to the Compute Engine **Health checks** page:

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. Click on your health check name.

  3. Click **Edit**.

  4. In the **Port** field, change the port number to 22.

  5. Click **Save** and wait a minute or two.

  6. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your backend instance groups:
         
         ~ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instanceGroups/sap-aha-primary-instance-group
         status:
           healthStatus:
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/forwardingRules/scs-aha-forwarding-rule
             forwardingRuleIp: 10.1.0.85
             **healthState: HEALTHY**
             instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-b/instances/nw-ha-vm-1
             ipAddress: 10.1.0.79
             port: 80
           kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/sap-aha-secondary-instance-group
         status:
           healthStatus:
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/forwardingRules/scs-aha-forwarding-rule
             forwardingRuleIp: 10.1.0.85
             **healthState: HEALTHY**
             instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/nw-ha-vm-2
             ipAddress: 10.1.0.78
             port: 80
           kind: compute#backendServiceGroupHealth

  7. When you are done, change the health check port number back to the original port number.




## Install listeners for the health checks

To configure a health check resource, you need to install the listeners first.

The load balancer uses a listener on the health-check port of each host to determine where the primary instance of the SAP HANA cluster is running.

On each host in the cluster, install a listener by completing the following steps:

  1. As root, install a simple TCP listener. These instructions install and use HAProxy as the listener.
         
         # yum install haproxy

  2. Copy and rename the default `haproxy.cfg` configuration file to make it a template file for the multiple haproxy instances:
         
         # cp /usr/lib/systemd/system/haproxy.service \
             /etc/systemd/system/haproxy@.service
         

  3. Edit the `[Unit]` and `[Service]` sections of the `haproxy@.service` file to include the `%i` instance parameter, as shown in the following example:
         
         [Unit]
         Description=**HAProxy Load Balancer %i**
         After=network-online.target
         Wants=network-online.target
         
         [Service]
         Environment="CONFIG=/etc/haproxy/**haproxy-%i.cfg** " "PIDFILE=/run/**haproxy-%i.pid** "
         ...
         

For more information from Red Hat about `systemd` unit templates, see [Working with instantiated units](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-systemd_configuring-basic-system-settings#con_working-with-instantiated-units_assembly_working-with-systemd-unit-files).

  4. Create an `haproxy.cfg` configuration file for the ASCS instance. For example:
         
         # vi /etc/haproxy/haproxy-SIDscs.cfg

Replace `SID` with the SAP system ID (SID). Use uppercase for any letters. For example, `AHA`.

  5. In the `haproxy-SIDscs.cfg` ASCS configuration file, insert the following configuration and replace `ASCS_HEALTHCHECK_PORT_NUM` with the port number that you specified when you created the Compute Engine healthcheck for ASCS earlier:
         
         global
             chroot      /var/lib/haproxy
             pidfile     /var/run/haproxy-%i.pid
             user        haproxy
             group       haproxy
             daemon
         defaults
             mode                    tcp
             log                     global
             option                  dontlognull
             option                  redispatch
             retries                 3
             timeout queue           1m
             timeout connect         10s
             timeout client          1m
             timeout server          1m
             timeout check           10s
             maxconn                 3000
         
         # Listener for SAP healthcheck
         listen healthcheck
            bind *:ASCS_HEALTHCHECK_PORT_NUM

  6. Create an `haproxy.cfg` configuration file for the ERS instance. For example:
         
         # vi /etc/haproxy/haproxy-SIDers.cfg

  7. In the `haproxy-SIDers.cfg` ERS configuration file, insert the following configuration and replace `ERS_HEALTHCHECK_PORT_NUM` with the port number that you specified when you created the Compute Engine healthcheck for ERS earlier:
         
         global
             chroot      /var/lib/haproxy
             pidfile     /var/run/haproxy-%i.pid
             user        haproxy
             group       haproxy
             daemon
         defaults
             mode                    tcp
             log                     global
             option                  dontlognull
             option                  redispatch
             retries                 3
             timeout queue           1m
             timeout connect         10s
             timeout client          1m
             timeout server          1m
             timeout check           10s
             maxconn                 3000
         
         # Listener for SAP healthcheck
         listen healthcheck
            bind *:ERS_HEALTHCHECK_PORT_NUM

  8. Reload the `systemd` services:
         
         # systemctl daemon-reload

  9. Confirm that the haproxy service is set up correctly:
         
         # systemctl start haproxy
          # systemctl status haproxy
          # systemctl | grep haproxy

The returned status should show the `haproxy.service` as `active (running)`.
         
         ● haproxy.service - HAProxy Load Balancer
            Loaded: loaded (/usr/lib/systemd/system/haproxy.service; enabled; vendor preset: disabled)
            Active: **active (running)** since Sun 2022-04-10 16:48:10 UTC; 2 days ago
          Main PID: 1079 (haproxy)
             Tasks: 2 (limit: 100996)
            Memory: 5.1M
            CGroup: /system.slice/haproxy.service
                    ├─1079 /usr/sbin/haproxy -Ws -f /etc/haproxy/haproxy.cfg -p /run/haproxy.pid
                    └─1083 /usr/sbin/haproxy -Ws -f /etc/haproxy/haproxy.cfg -p /run/haproxy.pid
         
         Apr 10 16:48:10 dru-hanw-ascs systemd[1]: Starting HAProxy Load Balancer...
         Apr 10 16:48:10 dru-hanw-ascs systemd[1]: Started HAProxy Load Balancer.

  10. Repeat the preceding steps on each host in the cluster.




## Set up Pacemaker

The following procedure configures the RHEL implementation of a Pacemaker cluster on Compute Engine VMs for SAP NetWeaver.

The procedure is based on Red Hat documentation for configuring high-availability clusters, including the following publications (a Red Hat subscription is required):

  * [Configuring SAP NetWeaver ASCS/ERS ENSA1 with Standalone Resources in RHEL 7.5+ and RHEL 8](https://access.redhat.com/articles/3569681)
  * [Configuring SAP S/4HANA ASCS/ERS with Standalone Enqueue Server 2 (ENSA2) in Pacemaker](https://access.redhat.com/articles/3974941)



For information from SAP about the installation and configuration of RHEL, see the following SAP notes:

  * [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)
  * [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)
  * [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)
  * [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)



### Configure the required cluster packages and OS firewall on both hosts

As root on both the primary and secondary hosts, install and update the required cluster packages, configure `hacluster`, and configure the OS firewall service.

  1. Install the following required cluster packages:
         
         # yum install pcs pacemaker
         # yum install fence-agents-gce
         # yum install resource-agents-gcp
         # yum install resource-agents-sap
         # yum install sap-cluster-connector

  2. Update the installed packages:
         
         # yum update -y

  3. Set the password for the `hacluster` user, which is installed as part of the cluster packages:
         
         # passwd hacluster

  4. Specify a password for `hacluster` at the prompts.

  5. In the RHEL images that are provided by Google Cloud, the OS firewall service is active by default. Configure the firewall service to allow high-availability traffic:
         
         # firewall-cmd --permanent --add-service=high-availability
         
         # firewall-cmd --reload

  6. Start the pcs service and configure it to start at boot time:
         
         # systemctl start pcsd.service
         # systemctl enable pcsd.service

  7. Check the status of the pcs service:
         
         # systemctl status pcsd.service

You should see output similar to the following:
         
         ● pcsd.service - PCS GUI and remote configuration interface
           Loaded: loaded (/usr/lib/systemd/system/pcsd.service; enabled; vendor preset: disabled)
           Active: active (running) since Sat 2020-06-13 21:17:05 UTC; 25s ago
             Docs: man:pcsd(8)
                   man:pcs(8)
         Main PID: 31627 (pcsd)
           CGroup: /system.slice/pcsd.service
                   └─31627 /usr/bin/ruby /usr/lib/pcsd/pcsd
         Jun 13 21:17:03 hana-ha-vm-1 systemd[1]: Starting PCS GUI and remote configuration interface...
         Jun 13 21:17:05 hana-ha-vm-1 systemd[1]: Started PCS GUI and remote configuration interface.




### Create the cluster

  1. As root on either node, authorize the `hacluster` user. Click the tab for your RHEL version to see the command:

### RHEL 8 and later
         
         # pcs host auth PRIMARY_VM_NAME SECONDARY_VM_NAME

### RHEL 7
         
         # pcs cluster auth PRIMARY_VM_NAME SECONDARY_VM_NAME

  2. At the prompts, enter the `hacluster` user name and the password that you set for the `hacluster` user.

  3. Create the cluster:

### RHEL 8 and later
         
         # pcs cluster setup CLUSTER_NAME PRIMARY_VM_NAME SECONDARY_VM_NAME

### RHEL 7
         
         # pcs cluster setup --name CLUSTER_NAME PRIMARY_VM_NAME SECONDARY_VM_NAME




#### Update the Corosync configuration files

The following steps set recommended cluster values for Corosync. If the Corosync configuration file, `/etc/corosync/corosync.conf`, doesn't exist yet or is empty, you can use the sample file in the `/etc/corosync/` directory as the base for your configuration.

  1. Open the `corosync.conf` file for editing:
         
         # vi /etc/corosync/corosync.conf

  2. In the `totem` section of the `corosync.conf` file, set the parameters in the following excerpted example to the values that are shown. Some parameters might already be set to the correct values:

###  RHEL 8 
         
         totem {
         ...
           transport: **knet**
           token: **20000**
           token_retransmits_before_loss_const: **10**
           join: **60**
           max_messages: **20**
         ...
         }

###  RHEL 7 
         
         totem {
         ...
           transport: **udpu**
           token: **20000**
           token_retransmits_before_loss_const: **10**
           join: **60**
           max_messages: **20**
         ...
         }

  3. Synchronize the configuration to your second server:

### RHEL 8 and later
         
         # pcs cluster sync corosync

### RHEL 7
         
         # pcs cluster sync

  4. From the primary VM, enable and start the cluster
         
         # pcs cluster enable --all
         # pcs cluster start --all

  5. Confirm that the new corosync settings are active in the cluster by using the corosync-cmapctl utility:
         
         # corosync-cmapctl

  6. Check the status of the cluster:
         
         # pcs status

You should see output similar to the following example:
         
         Cluster name: nwha
         
         WARNINGS:
         No stonith devices and stonith-enabled is not false
         
         Cluster Summary:
         * Stack: corosync
         * Current DC: nw-ha-vm-2 (version 2.0.5-9.el8_4.3-ba59be7122) - partition with quorum
         * 2 nodes configured
         * 0 resource instances configured
         
         Node List:
         * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Full List of Resources:
         * No resources
         
         Daemon Status:
         corosync: active/enabled
         pacemaker: active/enabled
         pcsd: active/enabled




## Configure the cluster resources for the infrastructure

You need to define Pacemaker resources for the following cluster infrastructure:

  * The fencing device, which prevents split brain scenarios
  * The ASCS and ERS directories in the shared file system
  * The health checks
  * The VIPs
  * The ASCS and ERS components



You define the resources for the fencing device, the shared file system, the health checks, and the VIPs first. Then you install SAP NetWeaver. After SAP NetWeaver is installed, you finally define the cluster resources for the ASCS and ERS components.

### Set up fencing

You set up fencing by defining a cluster resource with the `fence_gce` agent for each host VM.

To ensure the correct sequence of events after a fencing action, you also configure the operating system to delay the restart of Corosync after a VM is fenced. You also adjust the Pacemaker timeout for reboots to account for the delay.

**Note:** The parameter `pcmk_delay_max=30` must be configured only on one fencing device resource.

#### Create the fencing device resources

For each VM in the cluster, create a cluster resource for the fencing device so that the cluster can restart the VM. The fencing device for a VM must run on a different VM, so you configure the location of the cluster resource to run on any VM except the VM it can restart.

  1. On the primary host as root, create a cluster resource for a fencing device for the primary VM:
         
         # pcs stonith create FENCING_RESOURCE_PRIMARY_VM fence_gce \
             port="PRIMARY_VM_NAME" \
             zone="PRIMARY_ZONE" \
             project="CLUSTER_PROJECT_ID" \
             pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30 \
             op monitor interval="300s" timeout="120s" \
             op start interval="0" timeout="60s"

  2. Configure the location of the fencing device for the primary VM so that it is active on only the secondary VM:
         
         # pcs constraint location FENCING_RESOURCE_PRIMARY_VM avoids PRIMARY_VM_NAME

  3. On the secondary host as root, create a cluster resource for a fencing device for the secondary VM:
         
         # pcs stonith create FENCING_RESOURCE_SECONDARY_VM fence_gce \
             port="SECONDARY_VM_NAME" \
             zone="SECONDARY_ZONE" \
             project="CLUSTER_PROJECT_ID" \
             pcmk_reboot_timeout=300 pcmk_monitor_retries=4 \
             op monitor interval="300s" timeout="120s" \
             op start interval="0" timeout="60s"

  4. Configure the location of the fencing device for the secondary VM so that it is active on only the primary VM:
         
         # pcs constraint location FENCING_RESOURCE_SECONDARY_VM avoids SECONDARY_VM_NAME




#### Set a delay for the restart of Corosync

  1. On both hosts as root, create a `systemd` drop-in file that delays the startup of Corosync to ensure the proper sequence of events after a fenced VM is rebooted:
         
         systemctl edit corosync.service

  2. Add the following lines to the file:
         
         [Service]
         ExecStartPre=/bin/sleep 60

  3. Save the file and exit the editor.

  4. Reload the systemd manager configuration.
         
         systemctl daemon-reload

  5. Confirm the drop-in file was created:
         
         service corosync status

You should see a line for the drop-in file, as shown in the following example:
         
         ● corosync.service - Corosync Cluster Engine
            Loaded: loaded (/usr/lib/systemd/system/corosync.service; disabled; vendor preset: disabled)
           **Drop-In: /etc/systemd/system/corosync.service.d
                    └─override.conf**
            Active: active (running) since Tue 2021-07-20 23:45:52 UTC; 2 days ago




### Create the file system resources

Define the cluster resources for the ASCS and ERS directories in the shared file system.

**Note:** If you are using a [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) volume for your shared NFS storage, then you must adjust the Pacemaker resource timeout settings for the `Filesystem` resources to accommodate potential I/O pauses during NetApp Volumes maintenance events. 

To prevent cluster failovers during maintenance events, make sure that you perform the following:

  * Add the `options="rw,hard"` mount option to make sure that the NFS client retries connections during pauses.
  * Adjust the `interval` and `timeout` monitor settings based on your NFS protocol version (NFSv3 or NFSv4.1) and NetApp Volumes service level.



For more information, see [NetApp Volumes maintenance events](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#maintenance_event-related_application_disruptions) and [Recommended timeout and interval values](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#use_cluster_software_applications_to_automate_failovers).

  1. Configure a file system resource for the ASCS directory.
         
         # pcs resource create ASCS_FILE_SYSTEM_RESOURCE Filesystem \
             device="NFS_PATH/usrsapSIDASCSASCS_INSTANCE_NUMBER" \
             directory="/usr/sap/SID/ASCSASCS_INSTANCE_NUMBER" \
             fstype=nfs force_unmount=safe fast_stop=no \
             --group ASCS_RESOURCE_GROUP \
             op start interval=0 timeout=60 \
             op stop interval=0 timeout=120 \
             op monitor interval=200 timeout=40

Replace the following:

     * `ASCS_FILE_SYSTEM_RESOURCE`: specify a name for for the cluster resource for the ASCS file system.
     * `NFS_PATH`: specify the directory path to the NFS file system.
     * `SID`: specify the system ID (SID). Use uppercase for any letters.
     * `ASCS_INSTANCE_NUMBER`: specify the ASCS instance number.
     * `ASCS_RESOURCE_GROUP`: specify a unique group name for the ASCS cluster resources. You can ensure uniqueness by using a convention like "SID_ASCSinstance_number_group". For example, `nw8_ASCS00_group`. 

Because a group doesn't exist yet, Pacemaker creates the group now. As you create other ASCS resources, you add them to this group. 

  2. Configure a file system resource for the ERS directory.
         
         # pcs resource create ERS_FILE_SYSTEM_RESOURCE Filesystem \
             device="NFS_PATH/usrsapSIDERSERS_INSTANCE_NUMBER" \
             directory="/usr/sap/SID/ERSERS_INSTANCE_NUMBER" \
             fstype=nfs force_unmount=safe fast_stop=no \
             --group ERS_RESOURCE_GROUP \
             op start interval=0 timeout=60 \
             op stop interval=0 timeout=120 \
             op monitor interval=200 timeout=40

Replace the following:

     * `ERS_FILE_SYSTEM_RESOURCE`: specify a name for the file system resource.
     * `NFS_PATH`: specify the directory path to the NFS file system.
     * `SID`: specify the system ID (SID). Use uppercase for any letters.
     * `ERS_INSTANCE_NUMBER`: specify the ERS instance number.
     * `ERS_RESOURCE_GROUP`: specify a unique group name for the ERS cluster resources. You can ensure uniqueness by using a convention like "SID_ERSinstance_number_group". For example, `nw8_ERS10_group`. 

Because a group doesn't exist yet, Pacemaker creates the group now. As you create other ERS resources, you add them to this group. 


**Note:** To ensure consistent behavior across all supported RHEL versions, explicitly set the `fast_stop=no` option. This setting is critical to prevent HA cluster issues on RHEL 8, where the default `fast_stop=yes` can cause problems. On RHEL 9 and later, `fast_stop=no` is the default. For more information, see the Red Hat Knowledgebase article [What is the fast_stop option for a Filesystem resource in a Pacemaker cluster?](https://access.redhat.com/solutions/4801371).

### Create a virtual IP address resource

Define the cluster resources for the VIP addresses.

  1. If you need to look up the VIP address, you can use:

     * `gcloud compute addresses describe ASCS_VIP_NAME   
--region=CLUSTER_REGION --format="value(address)"`
     * `gcloud compute addresses describe ERS_VIP_NAME   
--region=CLUSTER_REGION --format="value(address)"`
  2. Create the cluster resources for the ASCS and ERS VIPs.
         
         # pcs resource create ASCS_VIP_RESOURCE IPaddr2 \
             ip=ASCS_VIP_ADDRESS cidr_netmask=32 nic=lo \
             op monitor interval=3600 timeout=60 \
             --group ASCS_RESOURCE_GROUP
         
         # pcs resource create ERS_VIP_RESOURCE IPaddr2 \
             ip=ERS_VIP_ADDRESS cidr_netmask=32 nic=lo \
             op monitor interval=3600 timeout=60 \
             --group ERS_RESOURCE_GROUP




**Note:** To ensure that the SAP NetWeaver Central services cluster is future compatible and supports `systemd` dynamic NIC naming convention, use the loopback interface (`lo`) with the `IPaddr2` resource configuration instead of a static interface name like `ethX` or `ensX`.

### Create the health check resources

  1. Configure the cluster resource for the ASCS health check:
         
         # pcs resource create _HEALTHCHECK_SCS service:haproxy@SIDascs \
            op monitor interval=10s timeout=20s \
            --group ASCS_RESOURCE_GROUP

  2. Configure the cluster resource for the ERS health check:
         
         # pcs resource create _HEALTHCHECK_ERS service:haproxy@SIDers \
            op monitor interval=10s timeout=20s \
            --group ERS_RESOURCE_GROUP




### Set additional cluster defaults

  1. Set additional cluster properties:
         
         # pcs resource defaults resource-stickiness=1
         # pcs resource defaults migration-threshold=3




### View the defined resources

Display the cluster resources that you have defined so far to make sure that they are correct.

  1. Display the cluster status:
         
         # pcs status

You should see output similar to the following example:
         
         Cluster name: nwha
         Cluster Summary:
           * Stack: corosync
           * Current DC: nw-ha-vm-1 (version 2.0.5-9.el8_4.3-ba59be7122) - partition with quorum
           * 2 nodes configured
           * 8 resource instances configured
         
         Node List:
           * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Full List of Resources:
           * fence-nw-ha-vm-2    (stonith:fence_gce):     Started nw-ha-vm-1
           * fence-nw-ha-vm-1    (stonith:fence_gce):     Started nw-ha-vm-2
           * Resource Group: nw8_ascs00_group:
             * nw8_vip_ascs00    (ocf::heartbeat:IPaddr2):    Started nw-ha-vm-1
             * nw8_healthcheck_scs   (service:haproxy@nw8scs):    Started nw-ha-vm-1
             * nw8_fs_ascs00 (ocf::heartbeat:Filesystem):     Started nw-ha-vm-1
           * Resource Group: nw8_ers10_group:
             * nw8_vip_ers10 (ocf::heartbeat:IPaddr2):    Started nw-ha-vm-2
             * nw8_healthcheck_ers   (service:haproxy@nw8ers):    Started nw-ha-vm-2
             * nw8_fs_ers10  (ocf::heartbeat:Filesystem):     Started nw-ha-vm-2
         
         Daemon Status:
           corosync: active/enabled
           pacemaker: active/enabled
           pcsd: active/enabled
         




## Install ASCS and ERS

The following section covers only the requirements and recommendations that are specific to installing SAP NetWeaver on Google Cloud.

For complete installation instructions, see the [SAP NetWeaver documentation](https://help.sap.com/viewer/product/SAP_NETWEAVER/ALL/en-US).

### Prepare for installation

To ensure consistency across the cluster and simplify installation, before you install the SAP NetWeaver ASCS and ERS components, define the users, groups, and permissions and put the secondary server in standby mode.

  1. Take the cluster out of maintenance mode:
         
         # sudo pcs property set maintenance-mode="false"

  2. On both servers as root, enter the following commands, specifying the user and group IDs that are appropriate for your environment:
         
         # groupadd -g GID_SAPINST sapinst
         # groupadd -g GID_SAPSYS sapsys
         # useradd -u UID_SIDADM SID_LCadm -g sapsys
         # usermod -a -G sapinst SID_LCadm
         # useradd -u UID_SAPADM sapadm -g sapinst
         
         # chown SID_LCadm:sapsys /usr/sap/SID/SYS
         # chown SID_LCadm:sapsys /sapmnt/SID -R
         # chown SID_LCadm:sapsys /usr/sap/trans -R
         # chown SID_LCadm:sapsys /usr/sap/SID/SYS -R
         # chown SID_LCadm:sapsys /usr/sap/SID -R




### Install the ASCS component

  1. On the secondary server, enter the following command to put the secondary server in standby mode:
         
         # pcs node standby

Putting the secondary server in standby mode consolidates all of the cluster resources on the primary server, which simplifies installation.

  2. Confirm that the secondary server is in standby mode:
         
         # pcs status

The output is similar to the following example: 
         
         Cluster name: nwha
            Cluster Summary:
              * Stack: corosync
              * Current DC: nw-ha-vm-1 (version 2.0.5-9.el8_4.3-ba59be7122) - partition with quorum
              * 2 nodes configured
              * 8 resource instances configured
         
            Node List:
              * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
            Full List of Resources:
              * fence-nw-ha-vm-2  (stonith:fence_gce):     Started nw-ha-vm-1
              * fence-nw-ha-vm-1  (stonith:fence_gce):     Stopped
              * Resource Group: nw8_ascs00_group:
                * nw8_vip_ascs00  (ocf::heartbeat:IPaddr2):    Started nw-ha-vm-1
                * nw8_healthcheck_scs (service:haproxy@nw8scs):    Started nw-ha-vm-1
                * nw8_fs_ascs00   (ocf::heartbeat:Filesystem):     Started nw-ha-vm-1
              * Resource Group: nw8_ers10_group:
                * nw8_vip_ers10   (ocf::heartbeat:IPaddr2):    Started nw-ha-vm-1
                * nw8_healthcheck_ers (service:haproxy@nw8ers):    Started nw-ha-vm-1
                * nw8_fs_ers10    (ocf::heartbeat:Filesystem):     Started nw-ha-vm-1
         
            Daemon Status:
              corosync: active/enabled
         

  3. On the primary server as the root user, change your directory to a temporary installation directory, such as `/tmp`, to install the ASCS instance by running the SAP Software Provisioning Manager (SWPM).

     * To access the web interface of SWPM, you need the password for the `root` user. If your IT policy does not allow the SAP administrator to have access to the root password, you can use the `SAPINST_REMOTE_ACCESS_USER`.

     * When you start SWPM, use the `SAPINST_USE_HOSTNAME` parameter to specify the virtual host name that you defined for the ASCS VIP address in the `/etc/hosts` file.

For example: 
           
           cd /tmp; /mnt/nfs/install/SWPM/sapinst SAPINST_USE_HOSTNAME=ascs-aha-vip

     * On the final SWPM confirmation page, ensure that the virtual host name is correct.

  4. After the configuration completes, take the secondary VM out of standby mode:
         
         # pcs node unstandby




### Install the ERS component

  1. On the primary server as root or `SID_LCadm`, stop the ASCS service.
         
         # su - SID_LCadm -c "sapcontrol -nr ASCS_INSTANCE_NUMBER -function Stop"
         # su - SID_LCadm -c "sapcontrol -nr ASCS_INSTANCE_NUMBER -function StopService"

  2. On the primary server, enter the following command to put the primary server in standby mode:
         
         # pcs node standby

Putting the primary server in standby mode consolidates all of the cluster resources on the secondary server, which simplifies installation.

  3. Confirm that the primary server is in standby mode:
         
         # pcs status

  4. On the secondary server as the root user, change your directory to a temporary installation directory, such as `/tmp`, to install the ERS instance by running the SAP Software Provisioning Manager (SWPM).

     * Use the same user and password to access SWPM that you used when you installed the ASCS component.

     * When you start SWPM, use the `SAPINST_USE_HOSTNAME` parameter to specify the virtual host name that you defined for the ERS VIP address in the `/etc/hosts` file.

For example: 
           
           cd /tmp; /mnt/nfs/install/SWPM/sapinst SAPINST_USE_HOSTNAME=ers-aha-vip

     * On the final SWPM confirmation page, ensure that the virtual host name is correct.

  5. Take the primary VM out of standby to have both active:
         
         # pcs node unstandby




## Configure the SAP services

You need to confirm that the services are configured correctly, check the settings in the ASCS and ERS profiles, and add the `SID_LCadm` user to the `haclient` user group.

### Confirm the SAP service entries

  1. On both servers, confirm that your `/usr/sap/sapservices` file contains entries for both the ASCS and ERS services. To do this, you can use the `systemV` or `systemd` integration.

You can add any missing entries by using the `sapstartsrv` command with the `pf=PROFILE_OF_THE_SAP_INSTANCE` and `-reg` options.

For more information about these integrations, see the following SAP Notes:

     * [3139184 - Linux: `systemd` integration for `sapstartsrv` and SAP Host Agent](https://me.sap.com/notes/3139184)
     * [3115048 - `sapstartsrv` with native Linux `systemd` support](https://me.sap.com/notes/3115048)

###  `systemV`

The following is an example of how the entries for the ASCS and ERS services in the `/usr/sap/sapservices` file when you're using the `systemV` integration:
    
    # LD_LIBRARY_PATH=/usr/sap/hostctrl/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH
    /usr/sap/hostctrl/exe/sapstartsrv \
    pf=/usr/sap/SID/SYS/profile/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME \
    -D -u SID_LCadm
    /usr/sap/hostctrl/exe/sapstartsrv \
    pf=/usr/sap/SID/SYS/profile/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
    -D -u SID_LCadm

###  `systemd`

     1. Verify that your `/usr/sap/sapservices` file contains entries for the ASCS and ERS services. The following is an example of how these entries appear in the `/usr/sap/sapservices` file when you're using the `systemd` integration:
            
            systemctl --no-ask-password start SAPSID_ASCS_INSTANCE_NUMBER # sapstartsrv pf=/usr/sap/SID/SYS/profile/SID_ASCSASCS_INSTANCE_NUMBER_SID_LCascs
            systemctl --no-ask-password start SAPSID_ERS_INSTANCE_NUMBER # sapstartsrv pf=/usr/sap/SID/SYS/profile/SID_ERSERS_INSTANCE_NUMBER_SID_LCers

     2. Disable the `systemd` integration on the ASCS and the ERS instances:

**Caution:** Disabling the `systemd` integration also stops the SAP instances.
            
            # systemctl disable SAPSID_ASCS_INSTANCE_NUMBER.service
            # systemctl stop SAPSID_ASCS_INSTANCE_NUMBER.service
            # systemctl disable SAPSID_ERS_INSTANCE_NUMBER.service
            # systemctl stop SAPSID_ERS_INSTANCE_NUMBER.service

     3. Verify that the `systemd` integration is disabled:
            
            # systemctl list-unit-files | grep sap

An output similar to the following example means that the `systemd` integration is disabled. Note that some services, such as `saphostagent` and `saptune`, are enabled, and some services are disabled.
            
            SAPSID_ASCS_INSTANCE_NUMBER.service disabled
            SAPSID_ERS_INSTANCE_NUMBER.service disabled
            saphostagent.service enabled
            sapinit.service generated
            saprouter.service disabled
            saptune.service enabled




### Stop the SAP services

  1. On the secondary server, stop the ERS service:
         
         # su - SID_LCadm -c "sapcontrol -nr ERS_INSTANCE_NUMBER -function Stop"
         # su - SID_LCadm -c "sapcontrol -nr ERS_INSTANCE_NUMBER -function StopService"

  2. On each server, validate that all services are stopped:
         
         # su - SID_LCadm -c "sapcontrol -nr ASCS_INSTANCE_NUMBER -function GetSystemInstanceList"
         # su - SID_LCadm -c "sapcontrol -nr ERS_INSTANCE_NUMBER -function GetSystemInstanceList"

You should see output similar to the following example:
         
         GetSystemInstanceList
         FAIL: NIECONN_REFUSED (Connection refused), NiRawConnect failed in plugin_fopen()




### Disable automatic service restart in SAP

**Key Point:** This section is required ONLY for systemV.

Because the cluster software manages the restart of SAP services during a failover, to avoid conflicts, disable the ability of the SAP software to automatically restart the services.

  1. On both nodes, edit the `/usr/sap/sapservices` file to disable automatic restart in the SAP software by adding a comment character, `#` at the beginning of the `sapstartsrv` command for both the ASCS and ERS components.

For example:
         
         #!/bin/sh
         
          **#** LD_LIBRARY_PATH=/usr/sap/SID/ASCSASCS_INSTANCE_NUMBER/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/SID/ASCSASCS_INSTANCE_NUMBER/exe/sapstartsrv pf=/usr/sap/SID/SYS/profile/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME -D -u SID_LCadm
          **#** LD_LIBRARY_PATH=/usr/sap/SID/ERSERS_INSTANCE_NUMBER/exe:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; /usr/sap/SID/ERSERS_INSTANCE_NUMBER/exe/sapstartsrv pf=/usr/sap/SID/SYS/profile/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME -D -u SID_LCadm
          




### Edit the ASCS and ERS profiles

  1. On either server, switch to the profile directory, by using either of the following commands:
         
         # cd /usr/sap/SID/SYS/profile
         
         # cd /sapmnt/SID/profile

  2. If necessary, you can find the files names of your ASCS and ERS profiles by listing the files in the profile directory or use the following formats:
         
         SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME
         
         SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME

  3. If you are using ENSA1, enable the keepalive function by setting the following in the ASCS profile:
         
         enque/encni/set_so_keepalive = true

For more information, see [SAP Note 1410736 - TCP/IP: setting keepalive interval](https://launchpad.support.sap.com/#/notes/1410736).

  4. If necessary, edit the ASCS and ERS profiles to change the startup behavior of the Enqueue Server and the Enqueue Replication Server.

###  ENSA1 

In the "**Start SAP enqueue server** " section of the ASCS profile, if you see `Restart_Program_NN`, change "`Restart`" to "`Start`", as shown in the following example.
         
         Start_Program_01 = local $(_EN) pf=$(_PF)

In the "**Start enqueue replication server** " section of the ERS profile, if you see `Restart_Program_NN`, change "`Restart`" to "`Start`", as shown in the following example.
         
         Start_Program_00 = local $(_ER) pf=$(_PFL) NR=$(SCSID)

###  ENSA2 

In the "**Start SAP enqueue server** " section of the ASCS profile, if you see `Restart_Program_NN`, change "`Restart`" to "`Start`", as shown in the following example.
         
         Start_Program_01 = local $(_ENQ) pf=$(_PF)

In the "**Start enqueue replicator** " section of the ERS profile, if you see `Restart_Program_NN`, change "`Restart`" to "`Start`", as shown in the following example.
         
         Start_Program_00 = local $(_ENQR) pf=$(_PF) ...




## Configure the cluster resources for ASCS and ERS

**Note:** If you are using a [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) volume for your shared NFS storage, then you must adjust the Pacemaker resource timeout settings for the `SAPInstance` resources to accommodate potential I/O pauses during NetApp Volumes maintenance events. 

To prevent cluster failovers during maintenance events, adjust the `interval` and `timeout` monitor settings for the `SAPInstance` resources. The monitor interval must align with the filesystem resource monitor interval , and the timeout must be larger than the filesystem timeout.

For more information, see [NetApp Volumes maintenance events](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#maintenance_event-related_application_disruptions) and [Recommended timeout and interval values](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#use_cluster_software_applications_to_automate_failovers).

  1. As root from either server, place the cluster in maintenance mode:
         
         # pcs property set maintenance-mode="true"

  2. Confirm that the cluster is in maintenance mode:
         
         # pcs status

  3. Create the cluster resources for the ASCS and ERS services:

###  ENSA1 

     * Create the cluster resource for the ASCS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ASCS.
           
           # pcs resource create ASCS_INSTANCE_RESOURCE SAPInstance \
               InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
               START_PROFILE=/sapmnt/SID/profile/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
               AUTOMATIC_RECOVER=false meta resource-stickiness=5000 migration-threshold=1 \
               failure-timeout=60  --group ASCS_RESOURCE_GROUP \
               op monitor interval=20 on-fail=restart timeout=60 \
               op start interval=0 timeout=600 \
               op stop interval=0 timeout=600
           
           
           # pcs resource meta ASCS_RESOURCE_GROUP resource-stickiness=3000
           

     * Create the cluster resource for the ERS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ERS. The parameter `IS_ERS=true` tells Pacemaker to set the `runs _ers_ SID` flag to `1` on the node where ERS is active.
           
           # pcs resource create ERS_INSTANCE_RESOURCE SAPInstance \
               InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME \
               START_PROFILE=/sapmnt/SID/profile/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME \
               AUTOMATIC_RECOVER=false IS_ERS=true --group ERS_RESOURCE_GROUP \
               op monitor interval=20 on-fail=restart timeout=60 \
               op start interval=0 timeout=600 \
               op stop interval=0 timeout=600
           

###  ENSA2 

     * Create the cluster resource for the ASCS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ASCS.
           
           # pcs resource create ASCS_INSTANCE_RESOURCE SAPInstance \
               InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
               START_PROFILE=/sapmnt/SID/profile/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
               AUTOMATIC_RECOVER=false meta resource-stickiness=5000 \
               --group ASCS_RESOURCE_GROUP \
               op monitor interval=20 on-fail=restart timeout=60 \
               op start interval=0 timeout=600 \
               op stop interval=0 timeout=600
           
           
           # pcs resource meta ASCS_RESOURCE_GROUP resource-stickiness=3000
           

     * Create the cluster resource for the ERS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ERS.
           
           # pcs resource create ERS_INSTANCE_RESOURCE SAPInstance \
               InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME \
               START_PROFILE=/sapmnt/SID/profile/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME \
               AUTOMATIC_RECOVER=false IS_ERS=true --group ERS_RESOURCE_GROUP \
               op monitor interval=20 on-fail=restart timeout=60 \
               op start interval=0 timeout=600 \
               op stop interval=0 timeout=600
           




### Configure the location and ordering constraints

You create constraints to define which services need to start first, and which services need to run together on the same host. For example, the IP address must be on the same host as the primary SAP Central Services instance.

  1. Define the start order constraint:



###  ENSA1 

  1. Create a colocation constraint that prevents the ASCS resources from running on the same server as the ERS resources:
         
         # pcs constraint colocation add ERS_RESOURCE_GROUP with \
             ASCS_RESOURCE_GROUP -5000
         

  2. Configure ASCS to failover to the server where ERS is running, as determined by the flag `runs _ers_ SID` being equal to `1`:
         
         # pcs constraint location ASCS_INSTANCE_RESOURCE \
             rule score=2000 runs_ers_SID eq 1

  3. Configure ASCS to start before ERS moves to the other server after a failover:
         
         # pcs constraint order start ASCS_RESOURCE_GROUP then \
             stop ERS_RESOURCE_GROUP symmetrical=false kind=Optional
         




###  ENSA2 

  1. Create a colocation constraint that prevents the ASCS resources from running on the same server as the ERS resources:
         
         # pcs constraint colocation add ERS_RESOURCE_GROUP  with \
             ASCS_RESOURCE_GROUP -5000
         

  2. Configure ASCS to start before ERS moves to the other server after a failover:
         
         # pcs constraint order start ASCS_RESOURCE_GROUP then \
             stop ERS_RESOURCE_GROUP symmetrical=false kind=Optional
         




  1. Check the constraints:
         
         # pcs constraint

You should see output similar to the following:
         
         Location Constraints:
           Resource: ascs-aha-instance
             Constraint: location-ascs-instance
               Rule: score=2000
                 Expression: runs_ers_HKN eq 1
           Resource: fence-nw-ha-vm-1
             Disabled on: nw-ha-vm-1 (score:-INFINITY)
           Resource: fence-nw-ha-vm-2
             Disabled on: nw-ha-vm-2 (score:-INFINITY)
         Ordering Constraints:
           start ascs-group then stop ers-group (kind:Optional) (non-symmetrical)
         Colocation Constraints:
           ascs-group with ers-group (score:-5000)
         Ticket Constraints:

  2. As root from either server, disable cluster maintenance mode:
         
         # pcs property set maintenance-mode="false"




### Configure the Red Hat cluster connector for SAP

On each host in the cluster, configure the SAP Start Service `sapstartsrv` to communicate with the pacemaker cluster software through the HA interface.

  1. Add the SAP administrative user to the `haclient` group:
         
         usermod -a -G haclient SID_LCadm

  2. Edit the SAP instance profiles by adding the following lines to the end of each profile. The profiles can be found in the `/sapmnt/SID/profiles` directory.
         
         service/halib = $(DIR_CT_RUN)/saphascriptco.so
         service/halib_cluster_connector = /usr/bin/sap_cluster_connector

  3. If the ASCS and ERS instance resources are currently running in the cluster, disable them:
         
         pcs resource disable ERS_INSTANCE_RESOURCE
         pcs resource disable ASCS_INSTANCE_RESOURCE

  4. Stop the services on the ASCS host:
         
         sapcontrol -nr ASCS_INSTANCE_NUMBER -function StopService

  5. Stop the services on the ERS host:
         
         sapcontrol -nr ERS_INSTANCE_NUMBER -function StopService

  6. Enable the resources:
         
         pcs resource enable ERS_INSTANCE_RESOURCE
         pcs resource enable ASCS_INSTANCE_RESOURCE

  7. Repeat the preceding steps on each host in the cluster.




For more information from Red Hat, see [How to configure SAP `halib` for `SAPInstance` resources on RHEL 7 and 8](https://access.redhat.com/solutions/3606101).

## Install the Database and Application Servers on hosts outside of the cluster

In high-availability configuration, we recommend that you install the database and application servers on different hosts than the ASCS and ERS hosts in the cluster.

By using separate hosts for each server, you reduce complexity, reduce the risk of a failure affecting multiple servers, and you can tailor the size of each Compute Engine to each server type.

This allows you to choose the most appropriate certified machine size, avoid failures, and reduce complexity.

The installation of the database and application servers is not covered in this guide.

For information about installing the database servers, see:

  * [SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-guides)
  * [SAP ASE on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-ase-guides)
  * [SAP MaxDB on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-maxdb-guides)
  * [IBM Db2 for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-guides)



## Validate and test the cluster

This section shows you how to run the following tests:

  * Check for configuration errors
  * Confirm that the ASCS and ERS resources switch servers correctly during failovers
  * Confirm that locks are retained
  * Simulate a Compute Engine maintenance event to make sure that live migration doesn't trigger a failover



### Check the cluster configuration

  1. As root on either server, check which nodes your resources are running on:
         
         # pcs status

In the following example, the ASCS resources are running on the `nw-ha-vm-2` server and the ERS resources are running on the `nw-ha-vm-1` server.
         
         Stack: corosync
           Current DC: nw-ha-vm-1 (version 1.1.23-1.el7_9.1-9acf116022) - partition with quorum
           Last updated: Wed Apr 13 05:21:21 2022
           Last change: Wed Apr 13 05:21:18 2022 by hacluster via crmd on nw-ha-vm-2
         
           2 nodes configured
           10 resource instances configured
         
           Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
           Full list of resources:
         
           fence-nw-ha-vm-1     (stonith:fence_gce):    Started nw-ha-vm-2
           fence-nw-ha-vm-2     (stonith:fence_gce):    Started nw-ha-vm-1
            Resource Group: ascs-group
                ascs-file-system   (ocf::heartbeat:Filesystem):    Started nw-ha-vm-2
                ascs-vip   (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-2
                ascs-healthcheck   (service:haproxy@AHAascs):      Started nw-ha-vm-2
                ascs-aha-instance      (ocf::heartbeat:SAPInstance):   Started nw-ha-vm-2
            Resource Group: ers-group
                ers-file-system    (ocf::heartbeat:Filesystem):    Started nw-ha-vm-1
                ers-vip    (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-1
                ers-healthcheck    (service:haproxy@AHAers):       Started nw-ha-vm-1
                ers-aha-instance       (ocf::heartbeat:SAPInstance):   Started nw-ha-vm-1
         
           Migration Summary:
           * Node nw-ha-vm-1:
           * Node nw-ha-vm-2:

  2. Switch to the `SID_LCadm` user:
         
         # su - SID_LCadm

  3. Check the cluster configuration. For `INSTANCE_NUMBER`, specify the instance number of the ASCS or ERS instance that is active on the server where you are entering the command:
         
         > sapcontrol -nr INSTANCE_NUMBER -function HAGetFailoverConfig

`HAActive` should be `TRUE`, as shown in the following example:
         
         HAGetFailoverConfig
         
         14.04.2022 17:25:45
         HAGetFailoverConfig
         OK
         HAActive: TRUE
         HAProductVersion: Pacemaker
         HASAPInterfaceVersion: sap_cluster_connector
         HADocumentation: https://github.com/ClusterLabs/sap_cluster_connector
         HAActiveNode:
         HANodes:

  4. As `SID_LCadm`, check for errors in the configuration:
         
         > sapcontrol -nr INSTANCE_NUMBER -function HACheckConfig

You should see output similar to the following example:
         
         14.04.2022 21:43:39
         HACheckConfig
         OK
         state, category, description, comment
         SUCCESS, SAP CONFIGURATION, Redundant ABAP instance configuration, 0 ABAP instances detected
         SUCCESS, SAP CONFIGURATION, Enqueue separation, All Enqueue server separated from application server
         SUCCESS, SAP CONFIGURATION, MessageServer separation, All MessageServer separated from application server
         SUCCESS, SAP STATE, SCS instance running, SCS instance status ok
         SUCCESS, SAP CONFIGURATION, SAPInstance RA sufficient version (ascs-aha-vip_AHA_00), SAPInstance includes is-ers patch
         SUCCESS, SAP CONFIGURATION, Enqueue replication (ascs-aha-vip_AHA_00), Enqueue replication enabled
         SUCCESS, SAP STATE, Enqueue replication state (ascs-aha-vip_AHA_00), Enqueue replication active
         SUCCESS, SAP CONFIGURATION, SAPInstance RA sufficient version (ers-aha-vip_AHA_10), SAPInstance includes is-ers patch

  5. On the server where ASCS is active, as `SID_LCadm`, simulate a failover:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function HAFailoverToNode ""

  6. As root, if you follow the failover by using `crm_mon`, you should see ASCS move to the other server, ERS stop on that server, and then ERS move to the server that ASCS used to be running on.




### Simulate a failover

Test your cluster by simulating a failure on the primary host. Use a test system or run the test on your production system before you release the system for use.

You can simulate a failure by running the following command:

  * `echo c > /proc/sysrq-trigger`



These instructions use the `echo c > /proc/sysrq-trigger` command to simulate a kernel panic and force a hard, immediate restart.

  1. Backup your system.

  2. As root on the host with the active SCS instance, trigger a crash on the primary node:
         
         $ echo c > /proc/sysrq-trigger

  3. Reconnect to either host using SSH and change to the root user.

  4. Enter `pcs status` to confirm that the primary host is now active on the VM that used to contain the secondary host. Automatic restart is enabled in the cluster, so the stopped host will restart and assume the role of secondary host, as shown in the following example.
         
         Stack: corosync
           Current DC: nw-ha-vm-1 (version 1.1.23-1.el7_9.1-9acf116022) - partition with quorum
           Last updated: Wed Apr 13 05:21:21 2022
           Last change: Wed Apr 13 05:21:18 2022 by hacluster via crmd on nw-ha-vm-2
         
           2 nodes configured
           10 resource instances configured
         
           Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
           Full list of resources:
         
           fence-nw-ha-vm-1     (stonith:fence_gce):    Started nw-ha-vm-2
           fence-nw-ha-vm-2     (stonith:fence_gce):    Started nw-ha-vm-1
            Resource Group: ascs-group
                ascs-file-system   (ocf::heartbeat:Filesystem):    Started nw-ha-vm-1
                ascs-vip   (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-1
                ascs-healthcheck   (service:haproxy@AHAascs):      Started nw-ha-vm-1
                ascs-aha-instance      (ocf::heartbeat:SAPInstance):   Started nw-ha-vm-1
            Resource Group: ers-group
                ers-file-system    (ocf::heartbeat:Filesystem):    Started nw-ha-vm-2
                ers-vip    (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-2
                ers-healthcheck    (service:haproxy@AHAers):       Started nw-ha-vm-2
                ers-aha-instance       (ocf::heartbeat:SAPInstance):   Started nw-ha-vm-2
         
           Migration Summary:
           * Node nw-ha-vm-1:
           * Node nw-ha-vm-2:




### Confirm lock entries are retained

To confirm lock entries are preserved across a failover, first select the tab for your version of the Enqueue Server and the follow the procedure to generate lock entries, simulate a failover, and confirm that the lock entries are retained after ASCS is activated again.

###  ENSA1 

  1. As `SID_LCadm`, on the server where ERS is active, generate lock entries by using the `enqt` program:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 11 NUMBER_OF_LOCKS

  2. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are registered:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

If you created 10 locks, your output is similar to the following example:
         
         locks_now: 10

  3. As `SID_LCadm`, on the server where ERS is active, start the monitoring function, `OpCode=20`, of the `enqt` program:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 20 1 1 9999

For example:
         
         > enqt pf=/sapmnt/AHA/profile/AHA_ERS10_ers-aha-vip 20 1 1 9999

  4. Where ASCS is active, reboot the server.

On the monitoring server, by the time Pacemaker stops ERS to move it to the other server, your output is similar to the following:
         
         Number of selected entries: 10
         Number of selected entries: 10
         Number of selected entries: 10
         Number of selected entries: 10
         Number of selected entries: 10

  5. When the `enqt` monitor stops, exit the monitor by entering `Ctrl + c`.

  6. Optionally, as root on either server, monitor the cluster failover:
         
         # crm_mon

  7. As `SID_LCadm`, after you confirm the locks were retained, release the locks:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 12 NUMBER_OF_LOCKS

  8. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are removed:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now




###  ENSA2 

  1. As `SID_LCadm`, on the server where ASCS is active, generate lock entries by using the `enq_adm` program:
         
         > enq_admin --set_locks=NUMBER_OF_LOCKS:X:DIAG::TAB:%u pf=/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME

  2. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are registered:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

If you created 10 locks, your output is similar to the following example:
         
         locks_now: 10

  3. Where ERS is active, confirm that the lock entries were replicated:
         
         > sapcontrol -nr ERS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

The number of returned locks must be the same as on the ASCS instance.

  4. Where ASCS is active, reboot the server.

  5. Optionally, as the root user, on either server, monitor the cluster failover:
         
         # crm_mon

  6. As `SID_LCadm`, on the server where ASCS was restarted, verify that the lock entries were retained:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

  7. As `SID_LCadm`, on the server where ERS is active, after you confirm the locks were retained, release the locks:
         
         > enq_admin --release_locks=NUMBER_OF_LOCKS:X:DIAG::TAB:%u pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME

  8. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are removed:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

Your output is similar to the following example:
         
         locks_now: 0




### Simulate a Compute Engine maintenance event

Simulate a Compute Engine maintenance event to make sure that [_live migration_](https://docs.cloud.google.com/compute/docs/instances/live-migration) does not trigger a failover.

The timeout and interval values that are used in these instructions account for the duration of live migrations. If you use shorter values in your cluster configuration, the risk that live migration might trigger a failover is greater.

To test the tolerance of your cluster for live migration:

  1. On the primary node, trigger a simulated maintenance event by using following gcloud CLI command:
         
         $ [gcloud compute instances simulate-maintenance-event PRIMARY_VM_NAME](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event)

  2. Confirm that the primary node does not change:
         
         $ pcs status




## Evaluate your SAP NetWeaver workload

To automate continuous validation checks for your SAP NetWeaver high-availability workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager allows you to automatically scan and evaluate your SAP NetWeaver high-availability workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP NetWeaver high-availability workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## Troubleshooting

To troubleshoot problems with high-availability configurations for SAP NetWeaver, see [Troubleshooting high-availability configurations for SAP](https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha).

## Collect diagnostic information for SAP NetWeaver high-availability clusters

If you need help resolving a problem with high-availability clusters for SAP NetWeaver, gather the required diagnostic information and contact Cloud Customer Care.

To collect diagnostic information, see [High-availability clusters on RHEL diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-rhel). 

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



## Performing post-deployment tasks

Before using your SAP NetWeaver system, we recommend that you backup your new SAP NetWeaver HA system.

For more information, see [SAP NetWeaver operations guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide#capturing_system_state).

## What's next

For more information high-availability, SAP NetWeaver, and Google Cloud, see the following resources:

  * [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Compute Cloud](https://access.redhat.com/articles/3479821)

  * [Support Policies for RHEL High Availability Clusters - General Requirements for Fencing/STONITH](https://access.redhat.com/articles/2881341)



  * [High-availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide)

  * For more information about VM administration and monitoring, see the [SAP NetWeaver Operations Guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide#the-monitoring-agent-for-sap-netweaver)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
