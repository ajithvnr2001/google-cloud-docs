---
url: https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles/
title: HA cluster manual configuration guide for SAP NetWeaver on SLES \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:12.395093+00:00
---

# HA cluster manual configuration guide for SAP NetWeaver on SLES  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  HA cluster manual configuration guide for SAP NetWeaver on SLES Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to deploy and configure a performance-optimized SUSE Linux Enterprise Server (SLES) high-availability (HA) cluster for SAP NetWeaver system.

Except for the procedures that are specific to the Standalone Enqueue Server 2 (ENSA2), which is available only in ABAP, this guide applies to both ABAP and Java SAP NetWeaver stacks. 

Unless an exception is indicated in the guide, examples that use "ASCS" are valid for both ABAP SAP Central Services (ASCS) and Java SAP Central Services (SCS). 

If you are using a Java stack, before you use the commands or examples in this guide, replace any instances of "ASCS" with "SCS". 

This guide includes the steps for: 

  * Configuring an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) to reroute traffic in the event of a failure.
  * Configuring a Pacemaker cluster on SLES to manage the SAP systems and other resources during a failover. [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) configuration is also provided for SLES 15 for SAP and later.



This guide also includes steps for configuring the SAP NetWeaver system for HA, but refer to the SAP documentation for the definitive instructions. 

For information about deploying Compute Engine VMs for SAP NetWeaver that is not specific to high-availability, see the [SAP NetWeaver deployment guide](https://docs.cloud.google.com/sap/docs/netweaver-guides) that is specific to your operating system.

To configure an HA cluster for SAP HANA on Red Hat Enterprise Linux (RHEL), see the [HA cluster manual configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel).

This guide is intended for advanced SAP NetWeaver users who are familiar with Linux high-availability configurations for SAP NetWeaver.

## The system that this guide deploys

Following this guide, you will deploy two SAP NetWeaver instances and set up an HA cluster on SLES. You deploy each SAP NetWeaver instance on a Compute Engine VM in a different zone within the same region. A high-availability installation of the underlying database is not covered in this guide.

![Overview of a high-availability Linux cluster for a single-node SAP NetWeaver system](https://docs.cloud.google.com/static/sap/docs/images/netweaver-ha-linux.svg)

The deployed cluster includes the following functions and features:

  * Two host VMs, one for the active ASCS instance and one for the active instance of the ENSA2 Enqueue Replicator or the ENSA1 Enqueue Replication Server (ENSA1). Both ENSA2 and ENSA1 instances are referred to as _ERS_.
  * The Pacemaker high-availability cluster resource manager.
  * A STONITH fencing mechanism.
  * Automatic restart of the failed instance as the new secondary instance.

This guide has you use the Cloud Deployment Manager templates that are provided by Google Cloud to deploy the Compute Engine virtual machines (VMs), which ensures that the VMs meet SAP supportability requirements and conform to current best practices. 

To use Terraform to automate the deployment of SAP NetWeaver HA systems, see [Terraform: HA cluster configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf).

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



## Related information from SUSE

Except where required for the Google Cloud environment, the information in this guide is consistent with the following related guides from SUSE:

  * [SAP NetWeaver Enqueue Replication 1 High Availability Cluster - Setup Guide for SAP NetWeaver 7.40 and 7.50 | SUSE Linux Enterprise Server for SAP Applications 12](https://documentation.suse.com/sbp/all/html/SAP_NW740_SLE12_SetupGuide/index.html)
  * [SAP NetWeaver Enqueue Replication 1 High Availability Cluster - Setup Guide for SAP NetWeaver 7.40 and 7.50 | SUSE Linux Enterprise Server for SAP Applications 15](https://documentation.suse.com/sbp/sap-15/html/SAP-nw740-sle15-setupguide/index.html)
  * [SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster - Setup Guide | SUSE Linux Enterprise Server for SAP Applications 12](https://documentation.suse.com/sbp/all/single-html/SAP_S4HA10_SetupGuide-SLE12/)
  * [SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster - Setup Guide | SUSE Linux Enterprise Server for SAP Applications 15](https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-sle15/index.html)



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

  3. Optionally, rename the `template.yaml` file to identify the configuration it defines. For example, `nw-ha-sles15sp3.yaml`.

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
`linuxImage` | String | The name of the Linux operating-system image or image family that you are using with SAP NetWeaver. To specify an image family, add the prefix `family/` to the family name. For example, `family/sles-15-sp3-sap`. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.   
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or the Google Cloud image project `suse-sap-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
`usrsapSize` | Integer | The size of the `/usr/sap` disk. The minimum size is 8 GB.   
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
        linuxImage: family/sles-15-sp3-sap
        linuxImageProject: suse-sap-cloud
        usrsapSize: 15
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
        linuxImage: family/sles-15-sp3-sap
        linuxImageProject: suse-sap-cloud
        usrsapSize: 15
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



## Update the Google Cloud CLI

The Deployment Manager template installed the Google Cloud CLI on the VMs during deployment. Update the gcloud CLI to ensure that it includes all of the latest updates.

  1. SSH into the primary VM.

  2. Update the gcloud CLI:
         
         ~>  sudo gcloud components update

  3. Follow the prompts.

  4. Repeat the steps on the secondary VM. 




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

You need to set up an NFS file sharing solution that provides highly-available shared file storage that both nodes of your HA cluster can access. You then create directories on both nodes that map to the shared file storage. The cluster software ensures that the appropriate directories mounted only on the correct instances.

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

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following commands instead:
         
         ~> sudo mkdir /mnt/nfs/sapmntSID
         ~> sudo mkdir /mnt/nfs/usrsap{trans,SID}

Replace the following:

     * `SID`: the SAP system ID (SID). Use uppercase for any letters. For example, `AHA`.
     * `ASCS_INSTANCE_NUMBER`: the instance number of the ASCS system. For example, `00`.
     * `ERS_INSTANCE_NUMBER`: the instance number of the ERS system. For example, `10`.
  4. On both servers, create the necessary mount points:
         
         ~> sudo mkdir -p /sapmnt/SID
         ~> sudo mkdir -p /usr/sap/trans
         ~> sudo mkdir -p /usr/sap/SID/ASCSASCS_INSTANCE_NUMBER
         ~> sudo mkdir -p /usr/sap/SID/ERSERS_INSTANCE_NUMBER

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following commands instead:
         
         ~> sudo mkdir -p /sapmnt/SID
         ~> sudo mkdir -p /usr/sap/trans
         ~> sudo mkdir -p /usr/sap/SID

  5. Configure `autofs` to mount the common shared file directories when the file directories are first accessed. The mounting of the `ASCSASCS_INSTANCE_NUMBER` and `ERSERS_INSTANCE_NUMBER` directories is managed by the cluster software, which you configure in a later step.

Adjust the NFS options in the commands as needed for your file-sharing solution.

On both servers, configure `autofs`:
         
         ~> echo "/- /etc/auto.sap" | sudo tee -a /etc/auto.master
         ~> NFS_OPTS="-rw,relatime,vers=3,hard,proto=tcp,timeo=600,retrans=2,mountvers=3,mountport=2050,mountproto=tcp"
         ~> echo "/sapmnt/SID ${NFS_OPTS} NFS_PATH/sapmntSID" | sudo tee -a /etc/auto.sap
         ~> echo "/usr/sap/trans ${NFS_OPTS} NFS_PATH/usrsaptrans" | sudo tee -a /etc/auto.sap

For information about `autofs`, see [autofs - how it works](https://www.kernel.org/doc/html/latest/filesystems/autofs.html).

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following commands instead:
         
         ~> echo "/- /etc/auto.sap" | sudo tee -a /etc/auto.master
         ~> NFS_OPTS="-rw,relatime,vers=3,hard,proto=tcp,timeo=600,retrans=2,mountvers=3,mountport=2050,mountproto=tcp"
         ~> echo "/sapmnt/SID ${NFS_OPTS}/sapmnt" | sudo tee -a /etc/auto.sap
         ~> echo "/usr/sap/trans ${NFS_OPTS}/usrsaptrans" | sudo tee -a /etc/auto.sap
         ~> echo "/usr/sap/SID  ${NFS_OPTS}/usrsapSID" | sudo tee -a /etc/auto.sap

  6. On both servers, start the `autofs` service:
         
         ~> sudo systemctl enable autofs
         ~> sudo systemctl restart autofs
         ~> sudo automount -v

  7. Trigger `autofs` to mount shared directories by accessing each directory by using the `cd` command. For example:
         
         ~> cd /sapmnt/SID
         ~> cd /usr/sap/trans
         

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead:
         
         ~> cd /sapmnt/SID
         ~> cd /usr/sap/trans
         ~> cd /usr/sap/SID

  8. After you access all the directories, issue the `df -Th` command to confirm the directories are mounted.
         
         ~> df -Th | grep FILE_SHARE_NAME

Replace `FILE_SHARE_NAME` with the name of your NFS file share solution. For example, `nfs_share_nw_ha`.

You see mount points and directories similar to the following example:
         
         10.49.153.26:/nfs_share_nw_ha              nfs      1007G   76M  956G   1% /mnt/nfs
         10.49.153.26:/nfs_share_nw_ha/usrsaptrans  nfs      1007G   76M  956G   1% /usr/sap/trans
         10.49.153.26:/nfs_share_nw_ha/sapmntAHA    nfs      1007G   76M  956G   1% /sapmnt/AHA

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then you see mount points and directories similar to the following example:
         
         10.49.153.26:/nfs_share_nw_ha              nfs      1007G   76M  956G   1% /mnt/nfs
         10.49.153.26:/nfs_share_nw_ha/usrsaptrans  nfs      1007G   76M  956G   1% /usr/sap/trans
         10.49.153.26:/nfs_share_nw_ha/sapmntAHA    nfs      1007G   76M  956G   1% /sapmnt/AHA
         10.49.153.26:/nfs_share_nw_ha/usrsapAHA   nfs      1007G   76M  956G   1% /usr/sap/AHA




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

You can use the `socat` utility to temporarily listen on a health check port. You need to install the `socat`utility anyway, because you use it later when you configure cluster resources.

  1. On both host VMs as root, install the `socat` utility:
         
         # zypper install socat

  2. On the primary VM, assign the VIP to the 'lo' loopback interface temporarily:
         
         ip addr add VIP_ADDRESS dev lo

  3. On the primary VM, start a `socat` process to listen for 60 seconds on the ASCS health check port:
         
         # timeout 60s socat - TCP-LISTEN:ASCS_HEALTHCHECK_PORT_NUM,fork

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




## Set up Pacemaker

The following procedure configures the SUSE implementation of a Pacemaker cluster on Compute Engine VMs for SAP NetWeaver.

For more information about the configuring high-availability clusters on SLES, see the [SUSE Linux Enterprise High Availability Extension](https://documentation.suse.com/#sle-ha) documentation for your version of SLES.

### Install the required cluster packages

  1. As root on both the primary and secondary hosts, download the following required cluster packages:

     * The `ha_sles` pattern:
           
           # zypper install -t pattern ha_sles

     * The `sap-suse-cluster-connector` package:
           
           # zypper install -y sap-suse-cluster-connector

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then additionally run the following command:
           
           # zypper install -y sapstartsrv-resource-agents

     * If you didn't already install it, the `socat` utility: 
           
           # zypper install -y socat

  2. Confirm that the latest high-availability agents are loaded:
         
         # zypper se -t patch SUSE-SLE-HA




### Initialize, configure, and start the cluster on the primary VM

You initialize the cluster by using the `ha-cluster-init` SUSE script. You then need to edit the Corosync configuration file and sync it with the secondary node. After starting the cluster, you then set additional cluster properties and defaults by using `crm` commands.

You might receive the following warnings while initializing or joining the cluster:

  * **No firewall detected** \- This warning indicates that the cluster initialization process could not find or update the operating system firewall. If you are using an operating system firewall, you need to allow access to these ports. You also need to create a VPC firewall rule that allows access to these ports, as well as those used by the SAP application.
  * **No watchdog device found** \- You can ignore this. These instructions do not use SBD.
  * **You should change the `hacluster` password** \- Change the password after you have completed these instructions.



### Create the Corosync configuration files

  1. Create a Corosync configuration file on the primary host:

     1. Using your preferred text editor, create the following file:
            
            /etc/corosync/corosync.conf

     2. In the `corosync.conf` file on the primary host, add the following configuration, replacing the italic variable text with your values:
            
            totem {
             version: 2
             secauth: off
             crypto_hash: sha1
             crypto_cipher: aes256
             cluster_name: hacluster
             clear_node_high_bit: yes
             token: 20000
             token_retransmits_before_loss_const: 10
             join: 60
             max_messages:  20
             transport: udpu
             interface {
               ringnumber: 0
               Bindnetaddr: STATIC_IP_OF_THIS_HOST
               mcastport: 5405
               ttl: 1
             }
            }
            logging {
             fileline:  off
             to_stderr: no
             to_logfile: no
             logfile: /var/log/cluster/corosync.log
             to_syslog: yes
             debug: off
             timestamp: on
             logger_subsys {
               subsys: QUORUM
               debug: off
             }
            }
            nodelist {
             node {
               ring0_addr: THIS_HOST_NAME
               nodeid: 1
             }
             node {
               ring0_addr: OTHER_HOST_NAME
               nodeid: 2
             }
            }
            quorum {
             provider: corosync_votequorum
             expected_votes: 2
             two_node: 1
            }

Replace the following:

     * `STATIC_IP_OF_THIS_HOST`: specify the static primary internal IP address of this VM, as shown under **Network interfaces in the Google Cloud console or as displayed by`gcloud compute instances describe VM_NAME`**. 
     * `THIS_HOST_NAME`: specify the host name of this VM.
     * `OTHER_HOST_NAME`: specify the host name of the other VM in the cluster.
  2. Create a Corosync configuration file on the secondary host by repeating the same steps you used for the primary host. Except for the static IP of the HDB on the `Bindnetaddr` property and the order of the host names in the `nodelist`, the configuration file property values are the same for each host.




#### Initialize the cluster

To initialize the cluster:

  1. Change the password for the `hacluster` user:
         
         # passwd hacluster

  2. On the primary host as root, initialize the cluster.

The following commands name the cluster and create the configuration file `corosync.conf`:configure it, and set up synching between the cluster nodes.
         
         # crm cluster init --name CLUSTER_NAME --yes ssh
         # crm cluster init --name CLUSTER_NAME --yes csync2
         # crm cluster init --name CLUSTER_NAME --yes corosync

  3. Start Pacemaker on the primary host:
         
         # systemctl enable pacemaker
         # systemctl start pacemaker




#### Set the additional cluster properties

  1. Set the general cluster properties:
         
         # crm configure property stonith-timeout="300s"
         # crm configure property stonith-enabled="true"
         # crm configure rsc_defaults resource-stickiness="1"
         # crm configure rsc_defaults migration-threshold="3"
         # crm configure op_defaults timeout="600"

When you define the individual cluster resources, the values that you set for `resource-stickiness` and `migration-threshold` override the default values that you set here.

You can see the resource defaults, as well as the values for any defined resources, by entering `crm config show`.




### Join the secondary VM to the cluster

From the open terminal on the primary VM, join and start the cluster on the secondary VM via SSH.

  1. Change the password for the `hacluster` user:
         
         # passwd hacluster

  2. From the primary VM, run the following `crm cluster join` script options on the secondary VM via SSH. If you have configured your HA cluster as described by these instructions, then you can disregard the warnings about the watchdog device.

     1. Run the `--yes ssh` option to set up `ssh` between the cluster nodes:
            
            # ssh SECONDARY_VM_NAME 'crm cluster join --cluster-node PRIMARY_VM_NAME --yes ssh'

     2. Run the `--yes csync2` option:
            
            # ssh SECONDARY_VM_NAME 'crm cluster join --cluster-node PRIMARY_VM_NAME --yes csync2'

     3. Run the `ssh_merge` option:
            
            # ssh SECONDARY_VM_NAME 'crm cluster join --cluster-node PRIMARY_VM_NAME --yes ssh_merge'

     4. Run the `cluster` option:
            
            # ssh SECONDARY_VM_NAME 'crm cluster join --cluster-node PRIMARY_VM_NAME --yes cluster'

  3. Start Pacemaker on the secondary host:

     1. Enable Pacemaker:
            
            # ssh SECONDARY_VM_NAME systemctl enable pacemaker

     2. Start Pacemaker:
            
            # ssh SECONDARY_VM_NAME systemctl start pacemaker

  4. On either host as root, confirm that the cluster shows both nodes:
         
         # crm_mon -s

You should see output similar to the following:
         
         CLUSTER OK: 2 nodes online, 0 resource instances configured




## Configure the cluster resources for the infrastructure

You define the resources that Pacemaker manages in a high-availability cluster. You need to define resources for the following cluster components:

  * The fencing device, which prevents split brain scenarios
  * The ASCS and ERS directories in the shared file system
  * The health checks
  * The VIPs
  * The ASCS and ERS components



You define the resources for ASCS and ERS components later than the rest of the resources, because you need to install SAP NetWeaver first.

### Enable maintenance mode

  1. On either host as root, put the cluster in maintenance mode:
         
         # crm configure property maintenance-mode="true"

  2. Confirm maintenance mode:
         
         # crm status

The output should indicate that resource management is disabled, as shown in the following example:
         
         Cluster Summary:
         * Stack: corosync
         * Current DC: nw-ha-vm-1 (version 2.0.4+20200616.2deceaa3a-3.3.1-2.0.4+20200616.2deceaa3a) - partition with quorum
         * Last updated: Fri May 14 15:26:08 2021
         * Last change:  Thu May 13 19:02:33 2021 by root via cibadmin on nw-ha-vm-1
         * 2 nodes configured
         * 0 resource instances configured
         
                     *** Resource management is DISABLED ***
         The cluster will not attempt to start, stop or recover services
         
         Node List:
         * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Full List of Resources:
         * No resources




### Set up fencing

You set up fencing by defining a cluster resource with the `fence_gce` agent for each host VM.

To ensure the correct sequence of events after a fencing action, you also configure the operating system to delay the restart of Corosync after a VM is fenced. You also adjust the Pacemaker timeout for reboots to account for the delay.

#### Create the fencing device resources

For each VM in the cluster, you create a cluster resource for the fencing device that can restart that VM. The fencing device for a VM must run on a different VM, so you configure the location of the cluster resource to run on any VM except the VM it can restart.

  1. On the primary host as root, create a cluster resource for a fencing device for the primary VM:
         
         # crm configure primitive FENCING_RESOURCE_PRIMARY_VM stonith:fence_gce \
           op monitor interval="300s" timeout="120s" \
           op start interval="0" timeout="60s" \
           params port="PRIMARY_VM_NAME" zone="PRIMARY_ZONE" \
           project="CLUSTER_PROJECT_ID" \
           pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30

  2. Configure the location of the fencing device for the primary VM so that it is active on only the secondary VM:
         
         # crm configure location FENCING_LOCATION_NAME_PRIMARY_VM \
           FENCING_RESOURCE_PRIMARY_VM -inf: "PRIMARY_VM_NAME"

  3. Confirm the newly created configuration:
         
         # crm config show related:FENCING_RESOURCE_PRIMARY_VM

You should see output similar to the following example:
         
         primitive FENCING_RESOURCE_PRIMARY_VM stonith:fence_gce \
                 op monitor interval=300s timeout=120s \
                 op start interval=0 timeout=60s \
                 params PRIMARY_VM_NAME zone=PRIMARY_ZONE project=CLUSTER_PROJECT_ID pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30
         location FENCING_RESOURCE_PRIMARY_VM FENCING_RESOURCE_PRIMARY_VM -inf: PRIMARY_VM_NAME

  4. On the primary host as root, create a cluster resource for a fencing device for the secondary VM:
         
         # crm configure primitive FENCING_RESOURCE_SECONDARY_VM stonith:fence_gce \
           op monitor interval="300s" timeout="120s" \
           op start interval="0" timeout="60s" \
           params port="SECONDARY_VM_NAME" zone="SECONDARY_VM_ZONE" \
           project="CLUSTER_PROJECT_ID" \
           pcmk_reboot_timeout=300 pcmk_monitor_retries=4

  5. Configure the location of the fencing device for the secondary VM so that it is active on only the primary VM:
         
         # crm configure location FENCING_LOCATION_NAME_SECONDARY_VM \
           FENCING_RESOURCE_SECONDARY_VM -inf: "SECONDARY_VM_NAME"

  6. Confirm the newly created configuration:
         
         # crm config show related:FENCING_RESOURCE_SECONDARY_VM

You should see output similar to the following example:
         
         primitive FENCING_RESOURCE_SECONDARY_VM stonith:fence_gce \
             op monitor interval=300s timeout=120s \
             op start interval=0 timeout=60s \
             params SECONDARY_VM_NAME zone=SECONDARY_ZONE project=CLUSTER_PROJECT_ID pcmk_reboot_timeout=300 pcmk_monitor_retries=4
         location FENCING_RESOURCE_SECONDARY_VM FENCING_RESOURCE_SECONDARY_VM -inf: SECONDARY_VM_NAME




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

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then you skip this section because a Simple Mount setup doesn't use instance specific file system resources that are managed by the cluster.

Now that you have created the shared file system directories, you can define the cluster resources.

**Note:** If you are using a [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) volume for your shared NFS storage, then you must adjust the Pacemaker resource timeout settings for the `Filesystem` resources to accommodate potential I/O pauses during NetApp Volumes maintenance events. 

To prevent cluster failovers during maintenance events, make sure that you perform the following:

  * Add the `options="rw,hard"` mount option to make sure that the NFS client retries connections during pauses.
  * Adjust the `interval` and `timeout` monitor settings based on your NFS protocol version (NFSv3 or NFSv4.1) and NetApp Volumes service level.



For more information, see [NetApp Volumes maintenance events](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#maintenance_event-related_application_disruptions) and [Recommended timeout and interval values](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#use_cluster_software_applications_to_automate_failovers).

  1. Configure the file system resources for the instance specific directories.
         
         # crm configure primitive ASCS_FILE_SYSTEM_RESOURCE Filesystem \
         device="NFS_PATH/usrsapSIDASCSASCS_INSTANCE_NUMBER" \
         directory="/usr/sap/SID/ASCSASCS_INSTANCE_NUMBER" fstype="nfs" \
         op start timeout=60s interval=0 \
         op stop timeout=60s interval=0 \
         op monitor interval=20s timeout=40s

Replace the following:

     * `ASCS_FILE_SYSTEM_RESOURCE`: specify a name for for the cluster resource for the ASCS file system.
     * `NFS_PATH`: specify the path to the NFS file system for ASCS.
     * `SID`: specify the system ID (SID). Use uppercase for any letters.
     * `ASCS_INSTANCE_NUMBER`: specify the ASCS instance number.
    
    # crm configure primitive ERS_FILE_SYSTEM_RESOURCE Filesystem \
    device="NFS_PATH/usrsapSIDERSERS_INSTANCE_NUMBER" \
    directory="/usr/sap/SID/ERSERS_INSTANCE_NUMBER" fstype="nfs" \
    op start timeout=60s interval=0 \
    op stop timeout=60s interval=0 \
    op monitor interval=20s timeout=40s

Replace the following:

     * `ERS_FILE_SYSTEM_RESOURCE`: specify a name for for the cluster resource for the ERS file system.
     * `NFS_PATH`: specify the path to the NFS file system for ERS.
     * `SID`: specify the system ID (SID). Use uppercase for any letters.
     * `ERS_INSTANCE_NUMBER`: specify the ASCS instance number.
  2. Confirm the newly created configuration:
         
         # crm configure show ASCS_FILE_SYSTEM_RESOURCE ERS_FILE_SYSTEM_RESOURCE

You should see output similar to the following example:
         
         primitive ASCS_FILE_SYSTEM_RESOURCE Filesystem \
             params device="NFS_PATH/usrsapSIDASCSASCS_INSTANCE_NUMBER" directory="/usr/sap/SID/ASCSASCS_INSTANCE_NUMBER" fstype=nfs \
             op start timeout=60s interval=0 \
             op stop timeout=60s interval=0 \
             op monitor interval=20s timeout=40s
         primitive ERS_FILE_SYSTEM_RESOURCE Filesystem \
             params device="NFS_PATH/usrsapSIDERSERS_INSTANCE_NUMBER" directory="/usr/sap/SID/ERSERS_INSTANCE_NUMBER" fstype=nfs \
             op start timeout=60s interval=0 \
             op stop timeout=60s interval=0 \
             op monitor interval=20s timeout=40s




### Create the health check resources

  1. Configure the cluster resources for the ASCS and ERS health checks:
         
         # crm configure primitive ASCS_HEALTH_CHECK_RESOURCE anything \
           params binfile="/usr/bin/socat" \
           cmdline_options="-U TCP-LISTEN:ASCS_HEALTHCHECK_PORT_NUM,backlog=10,fork,reuseaddr /dev/null" \
           op monitor timeout=20s interval=10s \
           op_params depth=0
         
         # crm configure primitive ERS_HEALTH_CHECK_RESOURCE anything \
           params binfile="/usr/bin/socat" \
           cmdline_options="-U TCP-LISTEN:ERS_HEALTHCHECK_PORT_NUM,backlog=10,fork,reuseaddr /dev/null" \
           op monitor timeout=20s interval=10s \
           op_params depth=0

  2. Confirm the newly created configuration:
         
         # crm configure show ERS_HEALTH_CHECK_RESOURCE ASCS_HEALTH_CHECK_RESOURCE

You should see output similar to the following example:
         
         primitive ERS_HEALTH_CHECK_RESOURCE anything \
                 params binfile="/usr/bin/socat" cmdline_options="-U TCP-LISTEN:ASCS_HEALTHCHECK_PORT_NUM,backlog=10,fork,reuseaddr /dev/null" \
                 op monitor timeout=20s interval=10s \
                 op_params depth=0
             primitive ASCS_HEALTH_CHECK_RESOURCE anything \
                 params binfile="/usr/bin/socat" cmdline_options="-U TCP-LISTEN:ERS_HEALTHCHECK_PORT_NUM,backlog=10,fork,reuseaddr /dev/null" \
                 op monitor timeout=20s interval=10s \
                 op_params depth=0




### Create the VIP resources

Define the cluster resources for the VIP addresses.

  1. If you need to look up the numerical VIP address, you can use:

     * `gcloud compute addresses describe ASCS_VIP_NAME   
--region=CLUSTER_REGION --format="value(address)"`
     * `gcloud compute addresses describe ERS_VIP_NAME   
--region=CLUSTER_REGION --format="value(address)"`
  2. Create the cluster resources for the ASCS and ERS VIPs.
         
         # crm configure primitive ASCS_VIP_RESOURCE IPaddr2 \
          params ip=ASCS_VIP_ADDRESS cidr_netmask=32 nic="lo" \
          op monitor interval=3600s timeout=60s
         
         # crm configure primitive ERS_VIP_RESOURCE IPaddr2 \
          params ip=ERS_VIP_ADDRESS cidr_netmask=32 nic="lo" \
          op monitor interval=3600s timeout=60s




**Note:** To ensure that the SAP NetWeaver Central services cluster is future compatible and supports `systemd` dynamic NIC naming convention, use the loopback interface (`lo`) with the `IPaddr2` resource configuration instead of a static interface name like `ethX` or `ensX`.

  1. Confirm the newly created configuration: 
         
         # crm configure show ASCS_VIP_RESOURCE ERS_VIP_RESOURCE

You should see output similar to the following example:
         
         primitive ASCS_VIP_RESOURCE IPaddr2 \
                 params ip=ASCS_VIP_ADDRESS cidr_netmask=32 nic=lo \
                 op monitor interval=3600s timeout=60s
             primitive ERS_VIP_RESOURCE IPaddr2 \
                 params ip=ERS_VIP_RESOURCE cidr_netmask=32 nic=lo \
                 op monitor interval=3600s timeout=60s




### View the defined resources

  1. To see all of the resources that you have defined so far, enter the following command:
         
         # crm status

You should see output similar to the following example:
         
         Stack: corosync
         Current DC: nw-ha-vm-1 (version 1.1.24+20201209.8f22be2ae-3.12.1-1.1.24+20201209.8f22be2ae) - partition with quorum
         Last updated: Wed May 26 19:10:10 2021
         Last change: Tue May 25 23:48:35 2021 by root via cibadmin on nw-ha-vm-1
         
         2 nodes configured
         8 resource instances configured
         
                       *** Resource management is DISABLED ***
           The cluster will not attempt to start, stop or recover services
         
         Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         **Full list of resources:
         
          fencing-rsc-nw-aha-vm-1        (stonith:fence_gce):    Stopped (unmanaged)
          fencing-rsc-nw-aha-vm-2        (stonith:fence_gce):    Stopped (unmanaged)
          filesystem-rsc-nw-aha-ascs      (ocf::heartbeat:Filesystem):    Stopped (unmanaged)
          filesystem-rsc-nw-aha-ers      (ocf::heartbeat:Filesystem):    Stopped (unmanaged)
          health-check-rsc-nw-ha-ascs     (ocf::heartbeat:anything):      Stopped (unmanaged)
          health-check-rsc-nw-ha-ers     (ocf::heartbeat:anything):      Stopped (unmanaged)
          vip-rsc-nw-aha-ascs     (ocf::heartbeat:IPaddr2):       Stopped (unmanaged)
          vip-rsc-nw-aha-ers     (ocf::heartbeat:IPaddr2):       Stopped (unmanaged)**

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then you see an output similar to the following example:
         
         Stack: corosync
         Current DC: nw-ha-vm-1 (version 1.1.24+20201209.8f22be2ae-3.12.1-1.1.24+20201209.8f22be2ae) - partition with quorum
         Last updated: Wed Sep 26 19:10:10 2024
         Last change: Tue Sep 25 23:48:35 2024 by root via cibadmin on nw-ha-vm-1
         
         2 nodes configured
         8 resource instances configured
         
                       *** Resource management is DISABLED ***
           The cluster will not attempt to start, stop or recover services
         
         Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         **Full list of resources:
         
          fencing-rsc-nw-aha-vm-1        (stonith:fence_gce):    Stopped (unmanaged)
          fencing-rsc-nw-aha-vm-2        (stonith:fence_gce):    Stopped (unmanaged)
          health-check-rsc-nw-ha-ascs     (ocf::heartbeat:anything):      Stopped (unmanaged)
          health-check-rsc-nw-ha-ers     (ocf::heartbeat:anything):      Stopped (unmanaged)
          vip-rsc-nw-aha-ascs     (ocf::heartbeat:IPaddr2):       Stopped (unmanaged)
          vip-rsc-nw-aha-ers     (ocf::heartbeat:IPaddr2):       Stopped (unmanaged)**




## Install ASCS and ERS

The following section covers only the requirements and recommendations that are specific to installing SAP NetWeaver on Google Cloud.

For complete installation instructions, see the [SAP NetWeaver documentation](https://help.sap.com/viewer/product/SAP_NETWEAVER/ALL/en-US).

### Prepare for installation

To ensure consistency across the cluster and simplify installation, before you install the SAP NetWeaver ASCS and ERS components, define the users, groups, and permissions and put the secondary server in standby mode.

  1. Take the cluster out of maintenance mode:
         
         # crm configure property maintenance-mode="false"

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

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following commands instead, on both servers as root. Specify the user and group IDs that are appropriate for your environment.
         
         # groupadd -g GID_SAPINST sapinst
         # groupadd -g GID_SAPSYS sapsys
         # useradd -u UID_SIDADM SID_LCadm -g sapsys
         # usermod -a -G sapinst SID_LCadm
         # useradd -u UID_SAPADM sapadm -g sapinst
         
         # chown SID_LCadm:sapsys /usr/sap/SID
         # chown SID_LCadm:sapsys /sapmnt/SID -R
         # chown SID_LCadm:sapsys /usr/sap/trans -R
         # chown SID_LCadm:sapsys /usr/sap/SID -R
         # chown SID_LCadm:sapsys /usr/sap/SID/SYS

Replace the following:

     * `GID_SAPINST`: specify the Linux group ID for the SAP provisioning tool.
     * `GID_SAPSYS`: specify the Linux group ID for the SAPSYS user.
     * `UID_SIDADM`: specify the Linux user ID for the administrator of the SAP system (SID).
     * `SID_LC`: specify the system ID (SID). Use lowercase for any letters.
     * `UID_SAPADM`: specify the user ID for the SAP Host Agent. 
     * `SID`: specify the system ID (SID). Use uppercase for any letters.

For example, the following shows a practical GID and UID numbering scheme:
    
    Group sapinst      1001
    Group sapsys       1002
    Group dbhshm       1003
    
    
    
    User  en2adm       2001
    User  sapadm       2002
    User  dbhadm       2003




### Install the ASCS component

  1. On the secondary server, enter the following command to put the secondary server in standby mode:
         
         # crm_standby -v on -N ${HOSTNAME};

Putting the secondary server in standby mode consolidates all of the cluster resources on the primary server, which simplifies installation.

  2. Confirm that the secondary server is in standby mode:
         
         # crm status

The output is similar to the following example: 
         
         Stack: corosync
          Current DC: nw-ha-vm-1 (version 1.1.24+20201209.8f22be2ae-3.12.1-1.1.24+20201209.8f22be2ae) - partition with quorum
          Last updated: Thu May 27 17:45:16 2021
          Last change: Thu May 27 17:45:09 2021 by root via crm_attribute on nw-ha-vm-2
         
          2 nodes configured
          8 resource instances configured
         
          Node nw-ha-vm-2: standby
          Online: [ nw-ha-vm-1 ]
         
          Full list of resources:
         
           fencing-rsc-nw-aha-vm-1        (stonith:fence_gce):    Stopped
           fencing-rsc-nw-aha-vm-2        (stonith:fence_gce):    Started nw-ha-vm-1
           filesystem-rsc-nw-aha-scs      (ocf::heartbeat:Filesystem):    Started nw-ha-vm-1
           filesystem-rsc-nw-aha-ers      (ocf::heartbeat:Filesystem):    Started nw-ha-vm-1
           health-check-rsc-nw-ha-scs     (ocf::heartbeat:anything):      Started nw-ha-vm-1
           health-check-rsc-nw-ha-ers     (ocf::heartbeat:anything):      Started nw-ha-vm-1
           vip-rsc-nw-aha-scs     (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-1
           vip-rsc-nw-aha-ers     (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-1
         

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then the output is similar to the following:
         
         Stack: corosync
          Current DC: nw-ha-vm-1 (version 1.1.24+20201209.8f22be2ae-3.12.1-1.1.24+20201209.8f22be2ae) - partition with quorum
          Last updated: Wed Sep 26 19:30:10 2024
          Last change: Tue Sep 25 23:58:35 2024 by root via crm_attribute on nw-ha-vm-2
         
          2 nodes configured
          8 resource instances configured
         
          Node nw-ha-vm-2: standby
          Online: [ nw-ha-vm-1 ]
         
          Full list of resources:
         
           fencing-rsc-nw-aha-vm-1        (stonith:fence_gce):    Stopped
           fencing-rsc-nw-aha-vm-2        (stonith:fence_gce):    Started nw-ha-vm-1
           health-check-rsc-nw-ha-scs     (ocf::heartbeat:anything):      Started nw-ha-vm-1
           health-check-rsc-nw-ha-ers     (ocf::heartbeat:anything):      Started nw-ha-vm-1
           vip-rsc-nw-aha-scs     (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-1
           vip-rsc-nw-aha-ers     (ocf::heartbeat:IPaddr2):       Started nw-ha-vm-1
         

  3. On the primary server as the root user, change your directory to a temporary installation directory, such as `/tmp`, to install the ASCS instance by running the SAP Software Provisioning Manager (SWPM).

     * To access the web interface of SWPM, you need the password for the `root` user. If your IT policy does not allow the SAP administrator to have access to the root password, you can use the `SAPINST_REMOTE_ACCESS_USER`.

     * When you start SWPM, use the `SAPINST_USE_HOSTNAME` parameter to specify the virtual host name that you defined for the ASCS VIP address in the `/etc/hosts` file.

For example: 
           
           cd /tmp; /mnt/nfs/install/SWPM/sapinst SAPINST_USE_HOSTNAME=ascs-aha-vip

     * On the final SWPM confirmation page, ensure that the virtual host name is correct.

  4. After the configuration completes, take the secondary VM out of standby mode:
         
         # crm_standby -v off -N ${HOSTNAME}; # On SECONDARY




### Install the ERS component

  1. On the primary server as root or `SID_LCadm`, stop the ASCS service.
         
         # su - SID_LCadm -c "sapcontrol -nr ASCS_INSTANCE_NUMBER -function Stop"
         # su - SID_LCadm -c "sapcontrol -nr ASCS_INSTANCE_NUMBER -function StopService"

  2. On the primary server, enter the following command to put the primary server in standby mode:
         
         # crm_standby -v on -N ${HOSTNAME};

Putting the primary server in standby mode consolidates all of the cluster resources on the secondary server, which simplifies installation.

  3. Confirm that the primary server is in standby mode:
         
         # crm status

  4. On the secondary server as the root user, change your directory to a temporary installation directory, such as `/tmp`, to install the ERS instance by running the SAP Software Provisioning Manager (SWPM).

     * Use the same user and password to access SWPM that you used when you installed the ASCS component.

     * When you start SWPM, use the `SAPINST_USE_HOSTNAME` parameter to specify the virtual host name that you defined for the ERS VIP address in the `/etc/hosts` file.

For example: 
           
           cd /tmp; /mnt/nfs/install/SWPM/sapinst SAPINST_USE_HOSTNAME=ers-aha-vip

     * On the final SWPM confirmation page, ensure that the virtual host name is correct.

  5. Take the primary VM out of standby to have both active:
         
         # crm_standby -v off -N ${HOSTNAME};




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

For more information, see the SUSE document [Disabling `systemd` services of the ASCS and the ERS SAP instances](https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-sle15/index.html#id-disabling-systemd-services-of-the-ascs-and-the-ers-sap-instance).




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




### Enable `sapping` and `sappong`

If you're not using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then skip this section.

Because the start and stop procedures in the cluster are managed by Pacemaker, you need to ensure that `sapstartsrv` doesn't initiate automatically during system boot. During system boot, `sapping` runs prior to `sapinit`, which hides the `sapservices` files. Upon the completion of `sapinit`, `sappong` unhides the `sapservices` files.

To activate this flow, you need to enable the `systemd` services `sapping` and `sappong` by using the following commands:
    
    
    # systemctl enable sapping sappong
    # systemctl status sapping sappong

### Edit the ASCS and ERS profiles

  1. On either server, switch to the profile directory, by using either of the following commands:
         
         # cd /usr/sap/SID/SYS/profile
         
         # cd /sapmnt/SID/profile

  2. If necessary, you can find the files names of your ASCS and ERS profiles by listing the files in the profile directory or use the following formats:
         
         SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME
         
         SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME

  3. Enable the package `sap-suse-cluster-connector` by adding the following lines to the profiles ASCS and ERS instance profiles:
         
         #-----------------------------------------------------------------------
         # SUSE HA library
         #-----------------------------------------------------------------------
         service/halib = $(DIR_CT_RUN)/saphascriptco.so
         service/halib_cluster_connector = /usr/bin/sap_suse_cluster_connector
         

  4. If you are using ENSA1, enable the keepalive function by setting the following in the ASCS profile:
         
         enque/encni/set_so_keepalive = true

For more information, see [SAP Note 1410736 - TCP/IP: setting keepalive interval](https://launchpad.support.sap.com/#/notes/1410736).

  5. If necessary, edit the ASCS and ERS profiles to change the startup behavior of the Enqueue Server and the Enqueue Replication Server.

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




### Add the `sidadm` user to the `haclient` user group

When you installed the `sap-suse-cluster-connector`, the installation created an `haclient` user group. To enable the `SID_LCadm` user to work with the cluster, add it to the `haclient` user group.

  1. On both servers, add the `SID_LCadm` user to the `haclient` user group:
         
         # usermod -aG haclient SID_LCadm




## Configure the cluster resources for ASCS and ERS

**Note:** If you are using a [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) volume for your shared NFS storage, then you must adjust the Pacemaker resource timeout settings for the `SAPInstance` resources to accommodate potential I/O pauses during NetApp Volumes maintenance events. 

To prevent cluster failovers during maintenance events, adjust the `interval` and `timeout` monitor settings for the `SAPInstance` resources. The monitor interval must align with the filesystem resource monitor interval ,or be set to a similar value if the filesystem resource is not managed by the cluster), and the timeout must be larger than the filesystem timeout.

For more information, see [NetApp Volumes maintenance events](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#maintenance_event-related_application_disruptions) and [Recommended timeout and interval values](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#use_cluster_software_applications_to_automate_failovers).

  1. As root from either server, place the cluster in maintenance mode:
         
         # crm configure property maintenance-mode="true"

  2. Confirm that the cluster is in maintenance mode:
         
         # crm status

If the cluster is in maintenance mode, the status includes the following lines:
         
         *** Resource management is DISABLED ***
         The cluster will not attempt to start, stop or recover services

  3. If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then create the `sapstartsrv` cluster resources for the ASCS and ERS services. If you're not using a Simple Mount setup, then skip this step.

     1. For ASCS, create a configuration file named `sapstartsrv_scs.txt` with the following content:
            
            primitive rsc_SAPStartSrv_SID_ASCSINSTANCENUMBER ocf:suse:SAPStartSrv \
            params InstanceName=SID_ASCSINSTANCE_NUMBER_ASCS_VIRTUAL_HOSTNAME

     2. To load the configuration for ASCS, run the following command:
            
            # crm configure load update sapstartsrv_scs.txt

     3. For ERS, create a configuration file named `sapstartsrv_ers.txt` with the following content:
            
            primitive rsc_SAPStartSrv_SID_ERSINSTANCENUMBER ocf:suse:SAPStartSrv \
            params InstanceName=SID_ERSINSTANCE_NUMBER_ERS_VIRTUAL_HOSTNAME

     4. To load the configuration for ERS, run the following command:
            
            # crm configure load update sapstartsrv_ers.txt

  4. Create the cluster resources for the ASCS and ERS services:

###  ENSA1 

     1. Create the cluster resource for the ASCS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ASCS.
            
            # crm configure primitive ASCS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false \
              meta resource-stickiness=5000 failure-timeout=60 \
                 migration-threshold=1 priority=10

In you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead:
            
            # crm configure primitive ASCS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false MINIMAL_PROBE=true \
              meta resource-stickiness=5000 failure-timeout=60 \
                 migration-threshold=1 priority=10

     2. Create the cluster resource for the ERS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ERS. The parameter `IS_ERS=true` tells Pacemaker to set the `runs _ers_ SID` flag to `1` on the node where ERS is active.
            
            # crm configure primitive ERS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME  \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false IS_ERS=true \
              meta priority=1000

In you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead:
            
            # crm configure primitive ERS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME  \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false MINIMAL_PROBE=true IS_ERS=true \
              meta priority=1000

     3. Confirm the newly created configuration:
            
            # crm configure show ASCS_INSTANCE_RESOURCE ERS_INSTANCE_RESOURCE

The output similar to the following example:
            
            primitive ASCS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false \
            meta resource-stickiness=5000 failure-timeout=60 migration-threshold=1 priority=10
            
            
            primitive ERS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false IS_ERS=true \
            meta priority=1000
            

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then the output is similar to the following example:
            
            primitive ASCS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false MINIMAL_PROBE=true \
            meta resource-stickiness=5000 failure-timeout=60 migration-threshold=1 priority=10
            
            
            primitive ERS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false MINIMAL_PROBE=true IS_ERS=true \
            meta priority=1000
            

###  ENSA2 

     1. Create the cluster resource for the ASCS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ASCS.
            
            # crm configure primitive ASCS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false \
              meta resource-stickiness=5000 failure-timeout=60

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead:
            
            # crm configure primitive ASCS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false MINIMAL_PROBE=true \
              meta resource-stickiness=5000 failure-timeout=60

     2. Create the cluster resource for the ERS instance. The value of `InstanceName` is the name of the instance profile that SWPM generated when you installed ERS.
            
            # crm configure primitive ERS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME  \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false IS_ERS=true

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead:
            
            # crm configure primitive ERS_INSTANCE_RESOURCE SAPInstance \
              operations \$id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
              op monitor interval=11 timeout=60 on-fail=restart \
              params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME  \
                 START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" \
                 AUTOMATIC_RECOVER=false IS_ERS=true MINIMAL_PROBE=true \
                 meta priority=1000

     3. Confirm the newly created configuration:
            
            # crm configure show ASCS_INSTANCE_RESOURCE ERS_INSTANCE_RESOURCE

The output similar to the following example:
            
            primitive ASCS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false \
            meta resource-stickiness=5000 failure-timeout=60
            
            
            primitive ERS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false IS_ERS=true \
            

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then the output is similar to the following:
            
            primitive ASCS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ASCS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ASCSASCS_INSTANCE_NUMBER_ASCS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false MINIMAL_PROBE=true \
            meta resource-stickiness=5000 failure-timeout=60 \
            migration-threshold=1 priority=10
            
            
            primitive ERS_INSTANCE_RESOURCE SAPInstance \
            operations $id=ERS_INSTANCE_RSC_OPERATIONS_NAME \
            op monitor interval=11 timeout=60 on-fail=restart \
            params InstanceName=SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME START_PROFILE="/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME" AUTOMATIC_RECOVER=false MINIMAL_PROBE=true IS_ERS=true \
            meta priority=1000




### Configure the resource groups and location constraints

  1. Group the ASCS and ERS resources. You can display the names of all your previously defined resources by entering the command `crm resource status`:

     * # crm configure group ASCS_RESOURCE_GROUP ASCS_FILE_SYSTEM_RESOURCE \
             ASCS_HEALTH_CHECK_RESOURCE ASCS_VIP_RESOURCE \
             ASCS_INSTANCE_RESOURCE \
             meta resource-stickiness=3000

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead: 
           
           # crm configure group ASCS_RESOURCE_GROUP ASCS_SAPSTARTSRV_RESOURCE \
             ASCS_HEALTH_CHECK_RESOURCE ASCS_VIP_RESOURCE \
             ASCS_INSTANCE_RESOURCE \
             meta resource-stickiness=3000

Replace the following: 
       * `ASCS_RESOURCE_GROUP`: specify a unique group name for the ASCS cluster resources. You can ensure uniqueness by using a convention such as `SID_LC_ASCSINSTANCE_NUMBER_group`. For example, `nw1_ASCS00_group`. 
       * `ASCS_FILE_SYSTEM_RESOURCE`: specify the name of the cluster resource that you defined for the ASCS file system earlier. This placeholder variable is not applicable when you're using a Simple Mount setup.
       * `ASCS_SAPSTARTSRV_RESOURCE`: specify the name of the cluster resource that you defined for the ASCS `sapstartsrv` earlier. This placeholder variable is applicable only when you're using a Simple Mount setup.
       * `ASCS_HEALTH_CHECK_RESOURCE`: specify the name of the cluster resource that you defined for the ASCS health check earlier.
       * `ASCS_VIP_RESOURCE`: specify the name of the cluster resource that you defined for the ASCS VIP earlier.
       * `ASCS_INSTANCE_RESOURCE`: specify the name of the cluster resource that you defined for the ASCS instance earlier.
     * # crm configure group ERS_RESOURCE_GROUP ERS_FILE_SYSTEM_RESOURCE \
             ERS_HEALTH_CHECK_RESOURCE ERS_VIP_RESOURCE \
             ERS_INSTANCE_RESOURCE

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then run the following command instead: 
           
           # crm configure group ERS_RESOURCE_GROUP ERS_SAPSTARTSRV_RESOURCE \
             ERS_HEALTH_CHECK_RESOURCE ERS_VIP_RESOURCE \
             ERS_INSTANCE_RESOURCE

Replace the following: 
       * `ERS_RESOURCE_GROUP`: specify a unique group name for the ERS cluster resources. You can ensure uniqueness by using a convention like "SID_ERSinstance number_group". For example, `nw1_ERS10_group`. 
       * `ERS_SAPSTARTSRV_RESOURCE`: specify the name of the cluster resource that you defined for the ERS `sapstartsrv` earlier. This placeholder variable is applicable only when you're using a Simple Mount setup.
       * `ERS_FILE_SYSTEM_RESOURCE`: specify the name of the cluster resource that you defined for the ERS file system earlier. This placeholder variable is not applicable when you're using a Simple Mount setup.
       * `ERS_HEALTH_CHECK_RESOURCE`: specify the name of the cluster resource that you defined for the ERS health check earlier.
       * `ERS_VIP_RESOURCE`: specify the name of the cluster resource that you defined for the ERS VIP earlier.
       * `ERS_INSTANCE_RESOURCE`: specify the name of the cluster resource that you defined for the ERS instance earlier.
  2. Confirm the newly created configuration:
         
         # crm configure show type:group

The output similar to the following example:
         
         group ERS_RESOURCE_GROUP ERS_FILE_SYSTEM_RESOURCE ERS_HEALTH_CHECK_RESOURCE ERS_VIP_RESOURCE ERS_INSTANCE_RESOURCE
         group ASCS_RESOURCE_GROUP ASCS_FILE_SYSTEM_RESOURCE ASCS_HEALTH_CHECK_RESOURCE ASCS_VIP_RESOURCE ASCS_INSTANCE_RESOURCE \
                 meta resource-stickiness=3000

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then the output is similar to the following example:
         
         group ERS_RESOURCE_GROUP ERS_SAPSTARTSRV_RESOURCE ERS_HEALTH_CHECK_RESOURCE ERS_VIP_RESOURCE ERS_INSTANCE_RESOURCE
         group ASCS_RESOURCE_GROUP ASCS_SAPSTARTSRV_RESOURCE ASCS_HEALTH_CHECK_RESOURCE ASCS_VIP_RESOURCE ASCS_INSTANCE_RESOURCE

  3. Create the colocation constraints:

###  ENSA1 

     1. Create a colocation constraint that prevents the ASCS resources from running on the same server as the ERS resources:
            
            # crm configure colocation PREVENT_SCS_ERS_COLOC -5000: ERS_RESOURCE_GROUP ASCS_RESOURCE_GROUP

     2. Configure ASCS to failover to the server where ERS is running, as determined by the flag `runs _ers_ SID` being equal to `1`:
            
            # crm configure location LOC_SCS_SID_FAILOVER_TO_ERS ASCS_INSTANCE_RESOURCE \
            rule 2000: runs_ers_SID eq 1

     3. Configure ASCS to start before ERS moves to the other server after a failover:
            
            # crm configure order ORD_SAP_SID_FIRST_START_ASCS \
             Optional: ASCS_INSTANCE_RESOURCE:start \
             ERS_INSTANCE_RESOURCE:stop symmetrical=false

     4. Confirm the newly created configuration:
            
            # crm configure show type:colocation type:location type:order

You should see output similar to the following example:
            
            order ORD_SAP_SID_FIRST_START_ASCS Optional: ASCS_INSTANCE_RESOURCE:start ERS_INSTANCE_RESOURCE:stop symmetrical=false
            colocation PREVENT_SCS_ERS_COLOC -5000: ERS_RESOURCE_GROUP ASCS_RESOURCE_GROUP
            location LOC_SCS_SID_FAILOVER_TO_ERS ASCS_INSTANCE_RESOURCE \
            rule 2000: runs_ers_SID eq 1

###  ENSA2 

     1. Create a colocation constraint that prevents the ASCS resources from running on the same server as the ERS resources:
            
            # crm configure colocation PREVENT_SCS_ERS_COLOC -5000: ERS_RESOURCE_GROUP ASCS_RESOURCE_GROUP

     2. Configure ASCS to start before ERS moves to the other server after a failover:
            
            # crm configure order ORD_SAP_SID_FIRST_START_ASCS \
             Optional: ASCS_INSTANCE_RESOURCE:start \
             ERS_INSTANCE_RESOURCE:stop symmetrical=false

     3. Confirm the newly created configuration:
            
            # crm configure show type:colocation type:order

You should see output similar to the following example:
            
            colocation PREVENT_SCS_ERS_COLOC -5000: ERS_RESOURCE_GROUP ASCS_RESOURCE_GROUP
            order ORD_SAP_SID_FIRST_START_ASCS  Optional: ASCS_INSTANCE_RESOURCE:start ERS_INSTANCE_RESOURCE:stop symmetrical=false

  4. Disable maintenance mode.
         
         # crm configure property maintenance-mode="false"




## Validate and test your cluster

This section shows you how to run the following tests:

  * Check for configuration errors
  * Confirm that the ASCS and ERS resources switch servers correctly during failovers
  * Confirm that locks are retained
  * Simulate a Compute Engine maintenance event to make sure that live migration doesn't trigger a failover



### Check the cluster configuration

  1. As root on either server, check which nodes your resources are running on:
         
         # crm status

In the following example, the ASCS resources are running on the `nw-ha-vm-1` server and the ERS resources are running on the `nw-ha-vm-2` server.
         
         Cluster Summary:
           * Stack: corosync
           * Current DC: nw-ha-vm-2 (version 2.0.4+20200616.2deceaa3a-3.3.1-2.0.4+20200616.2deceaa3a) - partition with quorum
           * Last updated: Thu May 20 16:58:46 2021
           * Last change:  Thu May 20 16:57:31 2021 by ahaadm via crm_resource on nw-ha-vm-2
           * 2 nodes configured
           * 10 resource instances configured
         
         Node List:
           * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Active Resources:
           * fencing-rsc-nw-aha-vm-1     (stonith:fence_gce):     Started nw-ha-vm-2
           * fencing-rsc-nw-aha-vm-2     (stonith:fence_gce):     Started nw-ha-vm-1
           * Resource Group: ascs-aha-rsc-group-name:
             * filesystem-rsc-nw-aha-ascs (ocf::heartbeat:Filesystem):     Started nw-ha-vm-1
             * health-check-rsc-nw-ha-ascs        (ocf::heartbeat:anything):       Started nw-ha-vm-1
             * vip-rsc-nw-aha-ascs        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-1
             * ascs-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-1
           * Resource Group: ers-aha-rsc-group-name:
             * filesystem-rsc-nw-aha-ers (ocf::heartbeat:Filesystem):     Started nw-ha-vm-2
             * health-check-rsc-nw-ha-ers        (ocf::heartbeat:anything):       Started nw-ha-vm-2
             * vip-rsc-nw-aha-ers        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-2
             * ers-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-2

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then the output is similar to the following example:
         
         Cluster Summary:
           * Stack: corosync
           * Current DC: nw-ha-vm-2 (version 2.0.4+20200616.2deceaa3a-3.3.1-2.0.4+20200616.2deceaa3a) - partition with quorum
           * Last updated: Thu Sep 20 19:44:26 2024
           * Last change:  Thu Sep 20 19:53:41 2024 by ahaadm via crm_resource on nw-ha-vm-2
           * 2 nodes configured
           * 10 resource instances configured
         
         Node List:
           * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Active Resources:
           * fencing-rsc-nw-aha-vm-1     (stonith:fence_gce):     Started nw-ha-vm-2
           * fencing-rsc-nw-aha-vm-2     (stonith:fence_gce):     Started nw-ha-vm-1
           * Resource Group: ascs-aha-rsc-group-name:
             * SAPStartSrv-rsc-nw-aha-ascs (ocf::heartbeat:SAPStartSrv):     Started nw-ha-vm-1
             * health-check-rsc-nw-ha-ascs        (ocf::heartbeat:anything):       Started nw-ha-vm-1
             * vip-rsc-nw-aha-ascs        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-1
             * ascs-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-1
           * Resource Group: ers-aha-rsc-group-name:
             * SAPStartSrv-rsc-nw-aha-ers (ocf::heartbeat:SAPStartSrv):     Started nw-ha-vm-2
             * health-check-rsc-nw-ha-ers        (ocf::heartbeat:anything):       Started nw-ha-vm-2
             * vip-rsc-nw-aha-ers        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-2
             * ers-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-2
         

  2. Switch to the `SID_LCadm` user:
         
         # su - SID_LCadm

  3. Check the cluster configuration. For `INSTANCE_NUMBER`, specify the instance number of the ASCS or ERS instance that is active on the server where you are entering the command:
         
         > sapcontrol -nr INSTANCE_NUMBER -function HAGetFailoverConfig

`HAActive` should be `TRUE`, as shown in the following example:
         
         20.05.2021 01:33:25
         HAGetFailoverConfig
         OK
         HAActive: TRUE
         HAProductVersion: SUSE Linux Enterprise Server for SAP Applications 15 SP2
         HASAPInterfaceVersion: SUSE Linux Enterprise Server for SAP Applications 15 SP2 (sap_suse_cluster_connector 3.1.2)
         HADocumentation: https://www.suse.com/products/sles-for-sap/resource-library/sap-best-practices/
         HAActiveNode: nw-ha-vm-1
         HANodes: nw-ha-vm-1, nw-ha-vm-2

  4. As `SID_LCadm`, check for errors in the configuration:
         
         > sapcontrol -nr INSTANCE_NUMBER -function HACheckConfig

You should see output similar to the following example:
         
         20.05.2021 01:37:19
         HACheckConfig
         OK
         state, category, description, comment
         SUCCESS, SAP CONFIGURATION, Redundant ABAP instance configuration, 0 ABAP instances detected
         SUCCESS, SAP CONFIGURATION, Redundant Java instance configuration, 0 Java instances detected
         SUCCESS, SAP CONFIGURATION, Enqueue separation, All Enqueue server separated from application server
         SUCCESS, SAP CONFIGURATION, MessageServer separation, All MessageServer separated from application server
         SUCCESS, SAP STATE, SCS instance running, SCS instance status ok
         SUCCESS, SAP CONFIGURATION, SAPInstance RA sufficient version (ascs-aha-vip_AHA_00), SAPInstance includes is-ers patch
         SUCCESS, SAP CONFIGURATION, Enqueue replication (ascs-aha-vip_AHA_00), Enqueue replication enabled
         SUCCESS, SAP STATE, Enqueue replication state (ascs-aha-vip_AHA_00), Enqueue replication active

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
         
         # echo c > /proc/sysrq-trigger

  3. Reconnect to either host using SSH and change to the root user.

  4. Enter `crm status` to confirm that the primary host is now active on the VM that used to contain the secondary host. Automatic restart is enabled in the cluster, so the stopped host will restart and assume the role of secondary host, as shown in the following example.
         
         Cluster Summary:
         * Stack: corosync
         * Current DC: nw-ha-vm-2 (version 2.0.4+20200616.2deceaa3a-3.3.1-2.0.4+20200616.2deceaa3a) - partition with quorum
         * Last updated: Fri May 21 22:31:32 2021
         * Last change:  Thu May 20 20:36:36 2021 by ahaadm via crm_resource on nw-ha-vm-1
         * 2 nodes configured
         * 10 resource instances configured
         
         Node List:
         * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Full List of Resources:
         * fencing-rsc-nw-aha-vm-1     (stonith:fence_gce):     Started nw-ha-vm-2
         * fencing-rsc-nw-aha-vm-2     (stonith:fence_gce):     Started nw-ha-vm-1
         * Resource Group: scs-aha-rsc-group-name:
           * filesystem-rsc-nw-aha-scs (ocf::heartbeat:Filesystem):     Started nw-ha-vm-2
           * health-check-rsc-nw-ha-scs        (ocf::heartbeat:anything):       Started nw-ha-vm-2
           * vip-rsc-nw-aha-scs        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-2
           * scs-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-2
         * Resource Group: ers-aha-rsc-group-name:
           * filesystem-rsc-nw-aha-ers (ocf::heartbeat:Filesystem):     Started nw-ha-vm-1
           * health-check-rsc-nw-ha-ers        (ocf::heartbeat:anything):       Started nw-ha-vm-1
           * vip-rsc-nw-aha-ers        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-1
           * ers-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-1

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then you see an output similar to the following:
         
         Cluster Summary:
          * Stack: corosync
          * Current DC: nw-ha-vm-2 (version 2.0.4+20200616.2deceaa3a-3.3.1-2.0.4+20200616.2deceaa3a) - partition with quorum
          * Last updated: Wed Sep 26 19:10:10 2024
          * Last change:  Tue Sep 25 23:48:35 2024 by ahaadm via crm_resource on nw-ha-vm-1
          * 2 nodes configured
          * 10 resource instances configured
         
         Node List:
          * Online: [ nw-ha-vm-1 nw-ha-vm-2 ]
         
         Full List of Resources:
          * fencing-rsc-nw-aha-vm-1     (stonith:fence_gce):     Started nw-ha-vm-2
          * fencing-rsc-nw-aha-vm-2     (stonith:fence_gce):     Started nw-ha-vm-1
          * Resource Group: scs-aha-rsc-group-name:
            * SAPStartSrv-rsc-nw-aha-scs (ocf::heartbeat:SAPStartSrv):     Started nw-ha-vm-2
            * health-check-rsc-nw-ha-scs        (ocf::heartbeat:anything):       Started nw-ha-vm-2
            * vip-rsc-nw-aha-scs        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-2
            * scs-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-2
          * Resource Group: ers-aha-rsc-group-name:
            * SAPStartSrv-rsc-nw-aha-ers (ocf::heartbeat:SAPStartSrv):     Started nw-ha-vm-1
            * health-check-rsc-nw-ha-ers        (ocf::heartbeat:anything):       Started nw-ha-vm-1
            * vip-rsc-nw-aha-ers        (ocf::heartbeat:IPaddr2):        Started nw-ha-vm-1
            * ers-aha-instance-rsc-name (ocf::heartbeat:SAPInstance):    Started nw-ha-vm-1
         




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
         
         # [gcloud compute instances simulate-maintenance-event PRIMARY_VM_NAME](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event)

  2. Confirm that the primary node does not change:
         
         # crm status




## Evaluate your SAP NetWeaver workload

To automate continuous validation checks for your SAP NetWeaver high-availability workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager allows you to automatically scan and evaluate your SAP NetWeaver high-availability workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP NetWeaver high-availability workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## Troubleshooting

To troubleshoot problems with high-availability configurations for SAP NetWeaver, see [Troubleshooting high-availability configurations for SAP](https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha).

## Collect diagnostic information for SAP NetWeaver high-availability clusters

If you need help resolving a problem with high-availability clusters for SAP NetWeaver, gather the required diagnostic information and contact Cloud Customer Care.

To collect diagnostic information, see [High-availability clusters on SLES diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-sles). 

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

  * [SUSE Best Practices](https://documentation.suse.com/sbp/all/)


  * [High-availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide)

  * For more information about VM administration and monitoring, see the [SAP NetWeaver Operations Guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide#the-monitoring-agent-for-sap-netweaver)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
