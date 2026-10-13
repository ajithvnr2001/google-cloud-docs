---
url: https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel/
title: HA scale-up cluster configuration guide for SAP HANA on RHEL \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:22.222410+00:00
---

# HA scale-up cluster configuration guide for SAP HANA on RHEL  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  HA scale-up cluster configuration guide for SAP HANA on RHEL Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reached end of support on December 31, 2025. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To manually configure a high-availability (HA) cluster for an SAP HANA scale-up system on RHEL on Google Cloud, we recommend that you instead see [HA scale-up cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-scaleup-ha-manual-config-rhel), which uses Terraform.

This guide shows you how to deploy and configure a Red Hat Enterprise Linux (RHEL) high-availability (HA) cluster for an SAP HANA 1.0 SPS 12 or later scale-up system on Google Cloud.

This guide includes the steps for:

  * Configuring an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) to reroute traffic in the event of a failure
  * Configuring a Pacemaker cluster on RHEL to manage the SAP systems and other resources during a failover



This guide also includes steps for configuring SAP HANA system replication, but refer to the SAP documentation for the definitive instructions.

To deploy a SAP HANA system without a Linux high-availability cluster or a standby node host, use the [SAP HANA deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide).

To configure an HA cluster for SAP HANA on SUSE Linux Enterprise Server (SLES), see the [HA cluster configuration guide for SAP HANA scale-up on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles). 

This guide is intended for advanced SAP HANA users who are familiar with Linux high-availability configurations for SAP HANA.

## The system that this guide deploys

Following this guide, you will deploy two SAP HANA instances and set up an HA cluster on RHEL. You deploy each SAP HANA instance on a Compute Engine VM in a different zone within the same region. A high-availability installation of SAP NetWeaver is not covered in this guide.

![Overview of a high-availability Linux cluster for a single-node SAP HANA scaleup system](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-scaleup-overview.svg)

The deployed cluster includes the following functions and features:

  * Two host VMs, each with an instance of SAP HANA
  * Synchronous SAP HANA system replication.
  * The Pacemaker high-availability cluster resource manager.
  * A STONITH fencing mechanism.
  * Automatic restart of the failed instance as the new secondary instance.



This guide has you use the Cloud Deployment Manager templates that are provided by Google Cloud to deploy the Compute Engine virtual machines (VMs) and the SAP HANA instances, which ensures that the VMs and the base SAP HANA systems meet SAP supportability requirements and conform to current best practices.

SAP HANA Studio is used in this guide to test SAP HANA system replication. You can use SAP HANA Cockpit instead, if you prefer. For information about installing SAP HANA Studio, see:

  * [Installing SAP HANA Studio on a Compute Engine Windows VM](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#install_hana_studio)
  * [SAP HANA Studio Installation and Update Guide](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/2.0.02/en-US)



## Prerequisites

Before you create the SAP HANA high availability cluster, make sure that the following prerequisites are met:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide) and the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide). 
  * You or your organization has a Google Cloud account and you have created a project for the SAP HANA deployment. For information about creating Google Cloud accounts and projects, see [Setting up your Google account](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#setting-up-your-google-account) in the SAP HANA Deployment Guide.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * The SAP HANA installation media is stored in a Cloud Storage bucket that is available in your deployment project and region. For information about how to upload SAP HANA installation media to a Cloud Storage bucket, see [Downloading SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#creating_a_cloud_storage_bucket_for_the_sap_hana_installation_files) in the SAP HANA Deployment Guide.

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)
  * If you are using [VPC internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns), the value of the `vmDnsSetting` variable in your project metadata must be either `GlobalOnly` or `ZonalPreferred` to enable the resolution of the node names across zones. The default setting of `vmDnsSetting` is `ZonalOnly`. For more information, see:

    * [Configuring DNS names for your project or instances](https://docs.cloud.google.com/compute/docs/networking/zonal-dns#setting-zonal-dns)
    * [Querying custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#querying_custom_metadata)
    * [Setting project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide)

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules. If you use the Deployment Manager template that Google Cloud provides, specify a tag with `networkTag: [TAG]`.
    * Create the VMs without an external IP. If you use the Deployment Manager templates that Google Cloud provides, specify `publicIP: No`.



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

By default, an _implied firewall rule_ blocks incoming connections from outside your Virtual Private Cloud (VPC) network. To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.
  * Communication between VMs in the SAP HANA subnetwork, including communication between nodes in an SAP HANA scale-out system or communication between the database server and application servers in a 3-tier architecture. You can enable communication between VMs by creating a firewall rule to allow traffic that originates from within the subnetwork.

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

## Deploying the VMs and SAP HANA

Before you begin configuring the HA cluster, you define and deploy the VM instances and SAP HANA systems that serve as the primary and secondary nodes in your HA cluster.

To define and deploy the systems, you use the same Cloud Deployment Manager template that you use to deploy a SAP HANA system in the [SAP HANA deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide).

However, to deploy two systems instead of one, you need to add the definition for the second system to the configuration file by copying and pasting the definition of the first system. After you create the second definition, you need to change the resource and instance names in the second definition. To protect against a zonal failure, specify a different zone in the same region. All other property values in the two definitions stay the same.

After the SAP HANA systems have deployed successfully, you define and configure the HA cluster.

The following instructions use the Cloud Shell, but are generally applicable to the Google Cloud CLI.

  1. Confirm that your current quotas for resources such as persistent disks and CPUs are sufficient for the SAP HANA systems you are about to install. If your quotas are insufficient, deployment fails. For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to the quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Open the Cloud Shell or, if you installed the gcloud CLI on your local workstation, open a terminal.

[Go to the Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `template.yaml` configuration file template for the SAP HANA high-availability cluster to your working directory by entering the following command in the Cloud Shell or gcloud CLI:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/template.yaml

  4. Optionally, rename the `template.yaml` file to identify the configuration it defines.

  5. Open the `template.yaml` file in the Cloud Shell code editor or, if you are using the gcloud CLI, the text editor of your choice.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  6. In the `template.yaml` file, complete the definition of the primary SAP HANA system. Specify the property values by replacing the brackets and their contents with the values for your installation. The properties are described in the following table.

To create the VM instances without installing SAP HANA, delete or comment out all of the lines that begin with `sap_hana_`.

Property | Data type | Description  
---|---|---  
type | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
`instanceName` | String | The name of the VM instance currently being defined. Specify different names in the primary and secondary VM definitions. Names must be specified in lowercase letters, numbers, or hyphens.   
`instanceType` | String | The type of Compute Engine virtual machine that you need to run SAP HANA on. If you need a custom VM type, specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations) .  
`zone` | String | The Google Cloud zone in which to deploy the VM instance that your are defining. Specify different zones in the same region for the primary and secondary HANA definitions. The zones must be in the same region that you selected for your subnet.   
`subnetwork` | String | The name of the subnetwork you created in a previous step. If you are deploying to a shared VPC, specify this value as `[SHAREDVPC_PROJECT]/[SUBNETWORK]`. For example, `myproject/network1`.  
`linuxImage` | String | The name of the Linux operating-system image or image family that you are using with SAP HANA. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-7-6-sap-ha`. To specify a specific image, specify only the image name. For the list of available images and families, see the [Images](https://console.cloud.google.com/compute/images) page in Google Cloud console.  
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project, such as `rhel-sap-cloud`. For more information about Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
`sap_hana_deployment_bucket` | String | The name of the Google Cloud storage bucket in your project that contains the SAP HANA installation and revision files that you uploaded in a previous step. Any upgrade revision files in the bucket are applied to SAP HANA during the deployment process.  
`sap_hana_sid` | String | The SAP HANA system ID (SID). The ID must consist of three alphanumeric characters and begin with a letter. All letters must be uppercase.  
`sap_hana_instance_number` | Integer | The instance number, 0 to 99, of the SAP HANA system. The default is 0.  
`sap_hana_sidadm_password` | String | The password for the operating system (OS) administrator. Passwords must be at least eight characters and include at least one uppercase letter, one lowercase letter, and one number. **Caution** : Change the password after the installation is complete.   
`sap_hana_system_password` | String | The password for the database superuser. Passwords must be at least 8 characters and include at least one uppercase letter, one lowercase letter, and one number. **Caution** : Change the password after the installation is complete.   
`sap_hana_sidadm_uid` | Integer | The default value for the `SID_LCadm` user ID is `900` to avoid user-created groups conflicting with SAP HANA. You can change this to a different value if you need to.  
`sap_hana_sapsys_gid` | Integer | The default group ID for sapsys is `79`. By specifying a value above you can override this value to your requirements.  
`sap_hana_scaleout_nodes` | Integer | Specify `0`. These instructions are for scale-up SAP HANA systems only.  
`networkTag` | String | A network tag that represents your VM instance for firewall or routing purposes. If you specify `publicIP: No` and do not specify a network tag, be sure to provide another means of access to the internet.   
`nic_type` | String | Optional but recommended if available for the target machine and OS version. Specifies the network interface to use with the VM instance. You can specify the value `GVNIC` or `VIRTIO_NET`. To use a [Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) (gVNIC), you need to specify an OS image that supports gVNIC as the value for the `linuxImage` property. For the OS image list, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).  If you do not specify a value for this property, then the network interface is automatically selected based on the machine type that you specify for the `instanceType` property.  This argument is available in Deployment Manager template versions `202302060649` or later.   
`publicIP` | Boolean | Optional. Determines whether a public IP address is added to your VM instance. The default is `Yes`. **Note** : Do not specify `No` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`serviceAccount` | String | Optional. Specifies a service account to be used by the host VMs and by the programs that run on the host VMs. Specify the email address of the service account. For example, svc-acct-name@project-id.iam.gserviceaccount.com. By default, the Compute Engine default service account is used. For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).   
  7. Create the definition of the secondary SAP HANA system by copying the definition of the primary SAP HANA system and pasting the copy after the primary SAP HANA system definition. See the example following these steps.

  8. In the definition of the secondary SAP HANA system, specify different values for the following properties than you specified in the primary SAP HANA system definition:

     * `name`
     * `instanceName`
     * `zone`
  9. Create the instances:
         
         gcloud deployment-manager deployments create DEPLOYMENT_NAME --config TEMPLATE_NAME.yaml

The above command invokes the Deployment Manager, which deploys the VMs, downloads the SAP HANA software from your storage bucket, and installs SAP HANA, all according to the specifications in your `template.yaml` file.

Deployment processing consists of two stages. In the first stage, Deployment Manager writes its status to the console. In the second stage, the deployment scripts write their status to Cloud Logging.




### Example of a complete `template.yaml` configuration file

The following example shows a completed `template.yaml` configuration file that deploys two VM instances with a SAP HANA system installed.

The file contains the definitions of two resources to deploy: `sap_hana_primary` and `sap_hana_secondary`. Each resource definition contains the definitions for a VM and a SAP HANA instance.

The `sap_hana_secondary` resource definition was created by copying and pasting the first definition, and then modifying the values of `name`, `instanceName`, and `zone` properties. All other property values in the two resource definitions are the same.

The properties `networkTag`, `serviceAccount`, `sap_hana_sidadm_uid`, and `sap_hana_sapsys_gid` are from the Advanced Options section of the configuration file template. The properties `sap_hana_sidadm_uid` and `sap_hana_sapsys_gid` are included to show their default values, which are used because the properties are commented out.
    
    
    resources:
    - **name: sap_hana_primary**
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/sap_hana.py
      #
      # By default, this configuration file uses the latest release of the deployment
      # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
      # of the scripts, comment out the type property above and uncomment the type property below.
      #
      # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/yyyymmddhhmm/dm-templates/sap_hana/sap_hana.py
      #
      properties:
        **instanceName: hana-ha-vm-1**
        instanceType: n2-highmem-32
        **zone: us-central1-a**
        subnetwork: example-subnet-us-central1
        linuxImage: family/rhel-8-1-sap-ha
        linuxImageProject: rhel-sap-cloud
        sap_hana_deployment_bucket: hana2-sp4-rev46
        sap_hana_sid: HA1
        sap_hana_instance_number: 22
        sap_hana_sidadm_password: Tempa55word
        sap_hana_system_password: Tempa55word
        sap_hana_scaleout_nodes: 0
        networkTag: cluster-ntwk-tag
        serviceAccount: limited-roles@example-project-123456.iam.gserviceaccount.com
        # sap_hana_sidadm_uid: 900
        # sap_hana_sapsys_gid: 79
    
    - **name: sap_hana_secondary**
      type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana/sap_hana.py
      #
      # By default, this configuration file uses the latest release of the deployment
      # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
      # of the scripts, comment out the type property above and uncomment the type property below.
      #
      # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/yyyymmddhhmm/dm-templates/sap_hana/sap_hana.py
      #
      properties:
        **instanceName: hana-ha-vm-2**
        instanceType: n2-highmem-32
        **zone: us-central1-c**
        subnetwork: example-subnet-us-central1
        linuxImage: family/rhel-8-1-sap-ha
        linuxImageProject: rhel-sap-cloud
        sap_hana_deployment_bucket: hana2-sp4-rev46
        sap_hana_sid: HA1
        sap_hana_instance_number: 22
        sap_hana_sidadm_password: Google123
        sap_hana_system_password: Google123
        sap_hana_scaleout_nodes: 0
        networkTag: cluster-ntwk-tag
        serviceAccount: limited-roles@example-project-123456.iam.gserviceaccount.com
        # sap_hana_sidadm_uid: 900
        # sap_hana_sapsys_gid: 79
        

## Create firewall rules that allow access to the host VMs

If you haven't done so already, create firewall rules that allow access to each host VM from the following sources:

  * For configuration purposes, your local workstation, a bastion host, or a jump server
  * For access between the cluster nodes, the other host VMs in the HA cluster



When you create VPC firewall rules, you specify the network tags that you defined in the `template.yaml` configuration file to designate your host VMs as the target for the rule.

To verify deployment, define a rule to allow SSH connections on port 22 from a bastion host or your local workstation.

For access between the cluster nodes, add a firewall rule that allows all connection types on any port from other VMs in the same subnetwork.

Make sure that the firewall rules for verifying deployment and for intra-cluster communication are created before proceeding to the next section. For instructions, see Adding firewall rules.

## Verifying the deployment of the VMs and SAP HANA

To verify deployment, you check the deployment logs in Cloud Logging and check the disks and services on the VMs of primary and secondary hosts.

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




### Check the configuration of the VMs and SAP HANA

  1. After the SAP HANA system deploys without errors, connect to each VM by using SSH. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for each VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ha-ssh-button.png)

  2. Change to the root user.
         
         $ sudo su -

  3. At the command prompt, enter `df -h`. On each VM, ensure that you see the `/hana` directories, such as `/hana/data`.
         
         Filesystem                        Size  Used Avail Use% Mounted on
         /dev/sda2                          30G  4.0G   26G  14% /
         devtmpfs                          126G     0  126G   0% /dev
         tmpfs                             126G     0  126G   0% /dev/shm
         tmpfs                             126G   17M  126G   1% /run
         tmpfs                             126G     0  126G   0% /sys/fs/cgroup
         /dev/sda1                         200M  9.7M  191M   5% /boot/efi
         /dev/mapper/vg_hana-shared        251G   49G  203G  20% /hana/shared
         /dev/mapper/vg_hana-sap            32G  240M   32G   1% /usr/sap
         /dev/mapper/vg_hana-data          426G  7.0G  419G   2% /hana/data
         /dev/mapper/vg_hana-log           125G  4.2G  121G   4% /hana/log
         /dev/mapper/vg_hanabackup-backup  512G   33M  512G   1% /hanabackup
         tmpfs                              26G     0   26G   0% /run/user/900
         tmpfs                              26G     0   26G   0% /run/user/899
         tmpfs                              26G     0   26G   0% /run/user/1000

  4. Change to the SAP admin user by replacing `SID_LC` in the following command with the system ID that you specified in the configuration file template. Use lowercase for any letters.
         
         # su - SID_LCadm

  5. Ensure that the SAP HANA services, such as `hdbnameserver`, `hdbindexserver`, and others, are running on the instance by entering the following command:
         
         > HDB info

  6. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




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
    

## Optional: Configure SSH keys on the primary and secondary VMs

The SAP HANA secure store (SSFS) keys need to be synchronized between the hosts in the HA cluster. To simplify the synchronization, and to allow files like backups to be copied between the hosts in the HA cluster, these instructions authorize direct SSH connections between the two hosts.

Your organization is likely to have guidelines that govern internal network communications. If necessary, after deployment is complete you can remove the metadata from the VMs and the keys from the `authorized_keys` directory.

If setting up direct SSH connections does not comply with your organization's guidelines, you can synchronize the SSFS keys and transfer files by using other methods, such as:

  * Transfer smaller files through your local workstation by using the Cloud Shell **Upload file** and **Download file** menu options. See [Managing files with Cloud Shell](https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files).
  * Exchange files by using a Cloud Storage bucket. See [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs).
  * Use the Cloud Storage Backint agent for SAP HANA to backup and restore HANA databases. See [Cloud Storage Backint agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backint_operations).
  * Use a file storage solution such as Filestore or Google Cloud NetApp Volumes to create a shared folder. For more information, see [File server options](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#file_server_options).



To enable SSH connections between the primary and secondary instances, follow these steps.

  1. On the primary host VM:

     1. SSH into the VM.

     2. Generate an SSH key for the user that needs the host-to-host SSH connection. The user is typically you.
            
            $ ssh-keygen

     3. At the prompts, accept the defaults by pressing enter.

     4. Update the primary VM's metadata with information about the SSH key for the secondary VM.
            
            $ gcloud compute instances add-metadata secondary-host-name \
                 --metadata "ssh-keys=$(whoami):$(cat ~/.ssh/id_rsa.pub)" \
                 --zone secondary-zone

     5. Authorize the primary VM to itself
            
            $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

  2. On the secondary host VM:

     1. SSH into the VM.

     2. Generate an SSH key for the user that needs the host-to-host SSH connection.
            
            $ ssh-keygen

     3. Update the secondary VM's metadata with information about the SSH key for the primary VM.
            
            $ gcloud compute instances add-metadata primary-host-name \
                  --metadata "ssh-keys=$(whoami):$(cat ~/.ssh/id_rsa.pub)" \
                  --zone primary-zone

     4. Authorize the secondary VM to itself
            
            $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

     5. Confirm that the SSH keys are set up properly by opening an SSH connection from the secondary system to the primary system.
            
            $ ssh primary-host-name

  3. On the primary host VM, confirm the connection by opening an SSH connection to the secondary host VM:
         
         $ ssh secondary-host-name




## Back up the databases

Create backups of your databases to initiate database logging for SAP HANA system replication and create a recovery point.

If you have multiple tenant databases in an MDC configuration, then back up each tenant database.

The Deployment Manager template uses `/hanabackup/data/SID` as the default backup directory. 

To create backups of new SAP HANA databases, complete the following steps:

  1. On the primary host, switch to the `SID_LCadm` user. Depending on your OS image, the command might be different.
         
         sudo -i -u SID_LCadm

  2. Create database backups:

     * For a SAP HANA single-database-container system:
           
           > hdbsql -t -u system -p SYSTEM_PASSWORD -i INST_NUM \
             "backup data using file ('full')"

The following example shows a successful response from a new SAP HANA system:
           
           0 rows affected (overall time 18.416058 sec; server time 18.414209 sec)

     * For a SAP HANA multi-database-container system (MDC), create a backup of the system database as well as any tenant databases:
           
           > hdbsql -t -d SYSTEMDB -u system -p SYSTEM_PASSWORD -i INST_NUM \
             "backup data using file ('full')"
           
           > hdbsql -t -d SID -u system -p SYSTEM_PASSWORD -i INST_NUM \
             "backup data using file ('full')"

The following example shows a successful response from a new SAP HANA system:
           
           0 rows affected (overall time 16.590498 sec; server time 16.588806 sec)

  3. Confirm that the logging mode is set to normal:
         
         > hdbsql -u system -p SYSTEM_PASSWORD -i INST_NUM \
           "select value from "SYS"."M_INIFILE_CONTENTS" where key='log_mode'"

The output is similar to the following:
         
         VALUE
         "normal"




## Enable SAP HANA system replication

As a part of enabling SAP HANA system replication, you need to copy the data and key files for the SAP HANA secure stores on the file system (SSFS) from the primary host to the secondary host. The method that this procedure uses to copy the files is just one possible method that you can use.

  1. On the primary host as `SID_LCadm`, enable system replication:
         
         > hdbnsutil -sr_enable --name=primary-host-name

  2. On the secondary host as `SID_LCadm`, stop SAP HANA:
         
         > HDB stop

  3. On the primary host, using the same user account that you used to set up SSH between the host VMs, copy the key files to the secondary host. For convenience, the following commands also define an environment variable for your user account ID:
         
         $ sudo cp /usr/sap/SID/SYS/global/security/rsecssfs ~/rsecssfs -r
         $ myid=$(whoami)
         $ sudo chown ${myid} -R /home/"${myid}"/rsecssfs
         $ scp -r rsecssfs $(whoami)@secondary-host-name:rsecssfs
         $ rm -r /home/"${myid}"/rsecssfs
         

  4. On secondary host, as the same user as the preceding step:

     1. Replace the existing key files in the rsecssfs directories with the files from the primary host and set the file permissions to limit access:
            
            $ SAPSID=SID
            $ sudo rm /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/data/SSFS_"${SAPSID}".DAT
            $ sudo rm /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/key/SSFS_"${SAPSID}".KEY
            $ myid=$(whoami)
            $ sudo cp /home/"${myid}"/rsecssfs/data/SSFS_"${SAPSID}".DAT \
              /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/data/SSFS_"${SAPSID}".DAT
            $ sudo cp /home/"${myid}"/rsecssfs/key/SSFS_"${SAPSID}".KEY \
              /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/key/SSFS_"${SAPSID}".KEY
            $ sudo chown "${SAPSID,,}"adm:sapsys \
              /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/data/SSFS_"${SAPSID}".DAT
            $ sudo chown "${SAPSID,,}"adm:sapsys \
              /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/key/SSFS_"${SAPSID}".KEY
            $ sudo chmod 644 \
              /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/data/SSFS_"${SAPSID}".DAT
            $ sudo chmod 640 \
              /usr/sap/"${SAPSID}"/SYS/global/security/rsecssfs/key/SSFS_"${SAPSID}".KEY

     2. Cleanup the files in your home directory.
            
            $ rm -r /home/"${myid}"/rsecssfs

     3. As `SID_LCadm`, register the secondary SAP HANA system with SAP HANA system replication:
            
            > hdbnsutil -sr_register --remoteHost=primary-host-name --remoteInstance=inst_num \
            --replicationMode=syncmem --operationMode=logreplay --name=secondary-host-name

     4. As `SID_LCadm`, start SAP HANA:
            
            > HDB start




### Validating system replication

On the primary host as `SID_LCadm`, confirm that SAP HANA system replication is active by running the following python script:
    
    
    $ python $DIR_INSTANCE/exe/python_support/systemReplicationStatus.py

If replication is set up properly, among other indicators, the following values are displayed for the `xsengine`, `nameserver`, and `indexserver` services:

  * The `Secondary Active Status` is `YES`
  * The `Replication Status` is `ACTIVE`



Also, the `overall system replication status` shows `ACTIVE`.

## Configure the Cloud Load Balancing failover support

The internal passthrough Network Load Balancer service with failover support routes traffic to the active host in an SAP HANA cluster based on a health check service.

### Reserve an IP address for the virtual IP

The virtual IP (VIP) address , which is sometimes referred to as a _floating_ IP address, follows the active SAP HANA system. The load balancer routes traffic that is sent to the VIP to the VM that is currently hosting the active SAP HANA system.

  1. Open Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address for the virtual IP. This is the IP address that applications use to access SAP HANA. If you omit the `--addresses` flag, an IP address in the specified subnet is chosen for you:
         
         $ [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) VIP_NAME \
           --region CLUSTER_REGION --subnet CLUSTER_SUBNET \
           --addresses VIP_ADDRESS

For more information about reserving a static IP, see [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

  3. Confirm IP address reservation:
         
         $ [gcloud compute addresses describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) VIP_NAME \
           --region CLUSTER_REGION

You should see output similar to the following example:
         
         address: 10.0.0.19
         addressType: INTERNAL
         creationTimestamp: '2020-05-20T14:19:03.109-07:00'
         description: ''
         id: '8961491304398200872'
         kind: compute#address
         name: vip-for-hana-ha
         networkTier: PREMIUM
         purpose: GCE_ENDPOINT
         region: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/addresses/vip-for-hana-ha
         status: RESERVED
         subnetwork: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/subnetworks/example-subnet-us-central1




### Create instance groups for your host VMs

  1. In Cloud Shell, create two unmanaged instance groups and assign the primary master host VM to one and the secondary master host VM to the other:
         
         $ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) PRIMARY_IG_NAME \
           --zone=PRIMARY_ZONE
         $ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) PRIMARY_IG_NAME \
           --zone=PRIMARY_ZONE \
           --instances=PRIMARY_HOST_NAME
         $ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) SECONDARY_IG_NAME \
           --zone=SECONDARY_ZONE
         $ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) SECONDARY_IG_NAME \
           --zone=SECONDARY_ZONE \
           --instances=SECONDARY_HOST_NAME
         

  2. Confirm the creation of the instance groups:
         
         $ [gcloud compute instance-groups unmanaged list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/list)

You should see output similar to the following example:
         
         NAME          ZONE           NETWORK          NETWORK_PROJECT        MANAGED  INSTANCES
         hana-ha-ig-1  us-central1-a  example-network  example-project-123456 No       1
         hana-ha-ig-2  us-central1-c  example-network  example-project-123456 No       1




### Create a Compute Engine health check

  1. In Cloud Shell, create the health check. For the port used by the health check, choose a port that is in the private range, 49152-65535, to avoid clashing with other services. The check-interval and timeout values are slightly longer than the defaults so as to increase failover tolerance during Compute Engine live migration events. You can adjust the values, if necessary:
         
         $ [gcloud compute health-checks create tcp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp) HEALTH_CHECK_NAME --port=HEALTHCHECK_PORT_NUM \
           --proxy-header=NONE --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
           --healthy-threshold=2

  2. Confirm the creation of the health check:
         
         $ [gcloud compute health-checks describe HEALTH_CHECK_NAME](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/describe)

You should see output similar to the following example:
         
         checkIntervalSec: 10
         creationTimestamp: '2020-05-20T21:03:06.924-07:00'
         healthyThreshold: 2
         id: '4963070308818371477'
         kind: compute#healthCheck
         name: hana-health-check
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/hana-health-check
         tcpHealthCheck:
          port: 60000
          portSpecification: USE_FIXED_PORT
          proxyHeader: NONE
         timeoutSec: 10
         type: TCP
         unhealthyThreshold: 2




### Create a firewall rule for the health checks

Define a firewall rule for a port in the private range that allows access to your host VMs from the IP ranges that are used by Compute Engine health checks, `35.191.0.0/16` and `130.211.0.0/22`. For more information, see [Creating firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

  1. If you don't already have one, add a network tag to your host VMs. This network tag is used by the firewall rule for health checks.
         
         $ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) PRIMARY_HOST_NAME \
           --tags NETWORK_TAGS \
           --zone PRIMARY_ZONE
         $ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) SECONDARY_HOST_NAME \
           --tags NETWORK_TAGS \
           --zone SECONDARY_ZONE
         

  2. If you don't already have one, create a firewall rule to allow the health checks:
         
         $ [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) RULE_NAME \
           --network NETWORK_NAME \
           --action ALLOW \
           --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags NETWORK_TAGS \
           --rules tcp:HLTH_CHK_PORT_NUM

For example:
         
         gcloud compute firewall-rules create  fw-allow-health-checks \
         --network example-network \
         --action ALLOW \
         --direction INGRESS \
         --source-ranges 35.191.0.0/16,130.211.0.0/22 \
         --target-tags cluster-ntwk-tag \
         --rules tcp:60000




### Configure the load balancer and failover group

  1. Create the load balancer backend service:
         
         $ [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) BACKEND_SERVICE_NAME \
           --load-balancing-scheme internal \
           --health-checks HEALTH_CHECK_NAME \
           --no-connection-drain-on-failover \
           --drop-traffic-if-unhealthy \
           --failover-ratio 1.0 \
           --region CLUSTER_REGION \
           --global-health-checks

  2. Add the primary instance group to the backend service:
         
         $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) BACKEND_SERVICE_NAME \
           --instance-group PRIMARY_IG_NAME \
           --instance-group-zone PRIMARY_ZONE \
           --region CLUSTER_REGION

  3. Add the secondary, failover instance group to the backend service:
         
         $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) BACKEND_SERVICE_NAME \
           --instance-group SECONDARY_IG_NAME \
           --instance-group-zone SECONDARY_ZONE \
           --failover \
           --region CLUSTER_REGION

  4. Create a forwarding rule. For the IP address, specify the IP address that you reserved for the VIP. If you need to access the SAP HANA system from outside of the region that is specified below, include the flag `--allow-global-access` in the definition:
         
         $ [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) RULE_NAME \
           --load-balancing-scheme internal \
           --address VIP_ADDRESS \
           --subnet CLUSTER_SUBNET \
           --region CLUSTER_REGION \
           --backend-service BACKEND_SERVICE_NAME \
           --ports ALL

For more information about cross-region access to your SAP HANA high-availability system, see [Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal#client-access).


**Note:** Your backend instance groups won't register as healthy until you have completed the Pacemaker cluster configuration.

### Test the load balancer configuration

Even though your backend instance groups won't register as healthy until later, you can test the load balancer configuration by setting up a listener to respond to the health checks. After setting up a listener, if the load balancer is configured correctly, the status of the backend instance groups changes to healthy.

The following sections present different methods that you can use to test the configuration.

#### Testing the load balancer with the `socat` utility

You can use the `socat` utility to temporarily listen on the health check port. 

  1. On both host VMs, install the `socat` utility:
         
         $ sudo yum install -y socat

  2. Start a `socat` process to listen for 60 seconds on the health check port:
         
         $ sudo timeout 60s socat - TCP-LISTEN:HLTH_CHK_PORT_NUM,fork

  3. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your backend instance groups:
         
         $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/hana-ha-ig-1
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/hana-ha-vm-1
            ipAddress: 10.0.0.35
            port: 80
          kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/hana-ha-ig-2
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/hana-ha-vm-2
            ipAddress: 10.0.0.34
            port: 80
          kind: compute#backendServiceGroupHealth




#### Testing the load balancer using port 22

If port 22 is open for SSH connections on your host VMs, you can temporarily edit the health checker to use port 22, which has a listener that can respond to the health checker.

To temporarily use port 22, follow these steps:

  1. Click your health check in the console:

[Go to Health checks page](https://console.cloud.google.com/compute/healthChecks)

  2. Click **Edit**.

  3. In the **Port** field, change the port number to 22.

  4. Click **Save** and wait a minute or two.

  5. In Cloud Shell, check the health of your backend instance groups:
         
         $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/hana-ha-ig-1
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/hana-ha-vm-1
            ipAddress: 10.0.0.35
            port: 80
          kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/hana-ha-ig-2
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/hana-ha-vm-2
            ipAddress: 10.0.0.34
            port: 80
          kind: compute#backendServiceGroupHealth

  6. When you are done, change the health check port number back to the original port number.




## Set up Pacemaker

The following procedure configures the Red Hat implementation of a Pacemaker cluster on Compute Engine VMs for SAP HANA.

The procedure is based on Red Hat documentation for configuring high-availability clusters, including (a Red Hat subscription is required):

  * [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Cloud](https://access.redhat.com/articles/3479821)
  * [Automated SAP HANA System Replication in Scale-Up in pacemaker cluster](https://access.redhat.com/articles/3004101)



### Install the cluster agents on both nodes

Complete the following steps on both nodes.

  1. As root, install the Pacemaker components:
         
         # yum -y install pcs pacemaker fence-agents-gce resource-agents-gcp resource-agents-sap-hana
         # yum update -y

If you are using a Google-provided RHEL-for-SAP image, these packages are already installed, but some updates might be required.

  2. Set the password for the `hacluster` user, which is installed as part of the packages:
         
         # passwd hacluster

  3. Specify a password for `hacluster` at the prompts.

  4. In the RHEL images provided by Google Cloud, the OS firewall service is active by default. Configure the firewall service to allow high-availability traffic:
         
         # firewall-cmd --permanent --add-service=high-availability
         
         # firewall-cmd --reload

  5. Start the pcs service and configure it to start at boot time:
         
         # systemctl start pcsd.service
         # systemctl enable pcsd.service

  6. Check the status of the pcs service:
         
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

  7. In the `/etc/hosts` file, add the full host name and the internal IP addresses of both hosts in the cluster. For example:
         
         127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
         ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
         **10.0.0.40 hana-ha-vm-1.us-central1-a.c.example-project-123456.internal hana-ha-vm-1**  # Added by Google
         **10.0.0.41 hana-ha-vm-2.us-central1-c.c.example-project-123456.internal hana-ha-vm-2**
         169.254.169.254 metadata.google.internal  # Added by Google

For more information from Red Hat about setting up the `/etc/hosts` file on RHEL cluster nodes, see <https://access.redhat.com/solutions/81123>.




### Create the cluster

  1. As root on either node, authorize the `hacluster` user. Click the tab for your RHEL version to see the command:

### RHEL 8 and later
         
         # pcs host auth primary-host-name secondary-host-name

### RHEL 7
         
         # pcs cluster auth primary-host-name secondary-host-name

  2. At the prompts, enter the `hacluster` user name and the password that you set for the `hacluster` user.

  3. Create the cluster:

### RHEL 8 and later
         
         # pcs cluster setup cluster-name primary-host-name secondary-host-name

### RHEL 7
         
         # pcs cluster setup --name cluster-name primary-host-name secondary-host-name




### Edit the corosync.conf default settings

Edit the `/etc/corosync/corosync.conf` file on the primary host to set a more appropriate starting point for testing the fault tolerance of your HA cluster on Google Cloud.

  1. On either host, use your preferred text editor to open the `/etc/corosync/corosync.conf` file for editing:
         
         # /etc/corosync/corosync.conf

  2. If `/etc/corosync/corosync.conf` is a new file or is empty, you can check the `/etc/corosync/` directory for an example file to use as the base for the corosync file.

  3. In the `totem` section of the corosync.conf file, add the following properties with the suggested values as shown for your RHEL version:

### RHEL 8 and later

     * `transport: knet`
     * `token: 20000`
     * `token_retransmits_before_loss_const: 10`
     * `join: 60`
     * `max_messages: 20`

For example:
    
    totem {
    version: 2
    cluster_name: hacluster
    secauth: off
    **transport: knet**
    **token: 20000**
    **token_retransmits_before_loss_const: 10**
    **join: 60**
    **max_messages: 20**
    }
    ...

### RHEL 7

     * `transport: udpu`
     * `token: 20000`
     * `token_retransmits_before_loss_const: 10`
     * `join: 60`
     * `max_messages: 20`

For example:
    
    totem {
    version: 2
    cluster_name: hacluster
    secauth: off
    **transport: udpu**
    **token: 20000**
    **token_retransmits_before_loss_const: 10**
    **join: 60**
    **max_messages: 20**
    }
    ...

  4. From the host that contains the edited `corosync.conf` file, sync the corosync configuration across the cluster:

### RHEL 8 and later
         
         # pcs cluster sync corosync

### RHEL 7
         
         # pcs cluster sync

  5. Set the cluster to start automatically:

     1. # pcs cluster enable --all

     2. # pcs cluster start --all

  6. Confirm that the new corosync settings are active in the cluster by using the corosync-cmapctl utility:
         
         # corosync-cmapctl




### Set up fencing

RHEL images that are provided by Google Cloud include a `fence_gce` fencing agent that is specific to Google Cloud. You use `fence_gce` to create fence devices for each host VM.

To ensure the correct sequence of events after a fencing action, you configure the operating system to delay the restart of Corosync after a VM is fenced. You also adjust the Pacemaker timeout for reboots to account for the delay.

To see all of the options that are available with the `fence_gce` fencing agent, issue `fence_gce -h`.

**Note:** If you have changed the host names so that they are no longer the same as the VM instance names, see [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Compute Cloud](https://access.redhat.com/articles/3479821). The following steps require the host names and VM instance names to be the same.

#### Create the fencing device resources

  1. On the primary host as root:

     1. Create a fencing device for each host VM:
            
            # pcs stonith create primary-fence-name fence_gce \
              port=primary-host-name \
              zone=primary-host-zone \
              project=project-id \
              pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30 \
              op monitor interval="300s" timeout="120s" \
              op start interval="0" timeout="60s"
            # pcs stonith create secondary-fence-name fence_gce \
              port=secondary-host-name \
              zone=secondary-host-zone \
              project=project-id \
              pcmk_reboot_timeout=300 pcmk_monitor_retries=4 \
              op monitor interval="300s" timeout="120s" \
              op start interval="0" timeout="60s"

     2. Constrain each fence device to the other host VM:
            
            # pcs constraint location primary-fence-name avoids primary-host-name
            # pcs constraint location secondary-fence-name avoids secondary-host-name

  2. On the primary host as root, test the secondary fence device:

     1. Shut down the secondary host VM:
            
            # fence_gce -o off -n secondary-host-name --zone=secondary-host-zone

If the command is successful, you lose connectivity to the secondary host VM and it appears stopped on the [**VM instances** page](https://console.cloud.google.com/compute/instances) in the Google Cloud console. You might need to refresh the page.

     2. Restart the secondary host VM:
            
            # fence_gce -o on -n secondary-host-name --zone=secondary-host-zone

  3. On the secondary host as root, test the primary fence device by repeating the preceding steps using the values for the primary host in the commands.

  4. On either host as root, check the status of the cluster:
         
         # pcs status

The fence resources appear in the resources section of the cluster status, similar to the following example:
         
         [root@hana-ha-vm-2 ~]# pcs status
         Cluster name: hana-ha-cluster
         Stack: corosync
         Current DC: hana-ha-vm-1 (version 1.1.19-8.el7_6.5-c3c624ea3d) - partition with quorum
         Last updated: Mon Jun 15 17:19:07 2020
         Last change: Mon Jun 15 17:18:33 2020 by root via cibadmin on hana-ha-vm-1
         
         2 nodes configured
         2 resources configured
         
         Online: [ hana-ha-vm-1 hana-ha-vm-2 ]
         
         Full list of resources:
         
          STONITH-hana-ha-vm-1   (stonith:fence_gce):    Started hana-ha-vm-2
          STONITH-hana-ha-vm-2   (stonith:fence_gce):    Started hana-ha-vm-1
         
         Daemon Status:
           corosync: active/enabled
           pacemaker: active/enabled
           pcsd: active/enabled




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




## Enable the SAP HANA HA/DR provider hooks

Red Hat recommends that you enable the SAP HANA HA/DR provider hooks, which let SAP HANA to send out notifications for certain events and improves failure detection. The SAP HANA HA/DR provider hooks require SAP HANA 2.0 SPS 03 or a later version. 

**Note:** If you want to implement the HA/DR provider hooks on a pre-existing SAP HANA system with near-zero downtime, then instead refer to the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide). 

On both the primary and secondary site, complete the following steps:

  1. As `SID_LCadm`, stop SAP HANA:
         
         > HDB stop



  1. As root or `SID_LCadm`, open the `global.ini` file for editing:
         
         > vi /hana/shared/SID/global/hdb/custom/config/global.ini

  2. Add the following definitions to the `global.ini` file:

**Note:** To implement the `chksrv.py` hook, you require RHEL 8 for SAP SP6 or later.
         
         [ha_dr_provider_SAPHanaSR]
         provider = SAPHanaSR
         path = /usr/share/SAPHanaSR/srHook
         execution_order = 1
         
         
         [ha_dr_provider_chksrv]
         provider = ChkSrv
         path = /usr/share/SAPHanaSR/srHook
         execution_order = 2
         action_on_lost = stop
         
         [trace]
         ha_dr_saphanasr = info
         ha_dr_chksrv = info

  3. As root, create a custom configuration file in the `/etc/sudoers.d` directory by running the following command. This new configuration file allows the `SID_LCadm` user to access the cluster node attributes when the `srConnectionChanged()` hook method is called.
         
         > visudo -f /etc/sudoers.d/20-saphana

  4. In the `/etc/sudoers.d/20-saphana` file, add the following text:

Replace the following: 
     * `SITE_A`: the site name of the primary SAP HANA server
     * `SITE_B`: the site name of the secondary SAP HANA server
     * `SID_LC`: the SID should be specified in lowercase letters
To view the site names, you can run the `crm_mon -A1 | grep site` command as the root user, on either the SAP HANA primary server or the secondary server. 
    
    Cmnd_Alias SITEA_SOK = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_A -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SITEA_SFAIL = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_A -v SFAIL -t crm_config -s SAPHanaSR
    Cmnd_Alias SITEB_SOK = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_B -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SITEB_SFAIL = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_B -v SFAIL -t crm_config -s SAPHanaSR
    SID_LCadm ALL=(ALL) NOPASSWD: SITEA_SOK, SITEA_SFAIL, SITEB_SOK, SITEB_SFAIL
    Defaults!SITEA_SOK, SITEA_SFAIL, SITEB_SOK, SITEB_SFAIL !requiretty

  5. In your `/etc/sudoers` file, make sure that the following text is included:
         
         **#** includedir /etc/sudoers.d

Note that the `#` in this text is part of the syntax and does not mean that the line is a comment.

**Note:** While the procedure in this section is recommended by Red Hat, you can use an alternative approach. Instead of creating a drop-in configuration file, you can add the required access directly to your `/etc/sudoers` file.
  6. As `SID_LCadm`, start SAP HANA:
         
         > HDB start

  7. On the primary host as `SID_LCadm`, test the status reported by the hook script:
         
         > cdtrace
         > awk '/ha_dr_SAPHanaSR.*crm_attribute/ { printf "%s %s %s %s\n",$2,$3,$5,$16 }' nameserver_*




## Set the cluster defaults

Set up migration thresholds and stickiness to determine the number of failovers to attempt before failure and to set the system to try restarting on the current host first. This only needs to be set on one node to apply to the cluster.

  1. As root on either host, start the cluster:
         
         # pcs cluster start --all #start the cluster

  2. Set the resource defaults:
         
         # pcs resource defaults resource-stickiness=1000
         # pcs resource defaults migration-threshold=5000

The property `resource-stickiness` controls how likely a service is to stay running where it is. Higher values make the service more sticky. A value of `1000` means that the service is very sticky.

The property `migration-threshold` specifies the number of failures that must occur before a service fails over to another host. A value of 5000 is high enough to prevent failover for shorter-lived error situations.

You can check the resource defaults by entering `pcs resource defaults`.

  3. Set the resource operation timeout defaults:
         
         # pcs resource op defaults timeout=600s

You can check the resource op defaults by entering `pcs resource op defaults`.

  4. Set below cluster properties:
         
         # pcs property set stonith-enabled="true"
         # pcs property set stonith-timeout="300s"
         

You can check your property settings with `pcs property list`.




### Create the `SAPHanaTopology` resource

The `SAPHanaTopology` resource gets the status and configuration of HANA System Replication on the nodes. It also checks the SAP host agent.

  1. As root on either host, create the `SAPHanaTopology` resource:
         
         # pcs resource create topology_resource_name SAPHanaTopology SID=SID \
            InstanceNumber=inst_num \
            op start timeout=600 \
            op stop timeout=300 \
            op monitor interval=10 timeout=600 \
            clone clone-max=2 clone-node-max=1 interleave=true

  2. After the resource is created, check the configuration. Append `-clone` to the resource name to include the clone set information in the response:

### RHEL 8 and later
         
         # pcs resource config topology_resource_name-clone

### RHEL 7
         
         # pcs resource show topology_resource_name-clone

You should see output similar to the following:
         
         Clone: SAPHanaTopology_HA1_22-clone
         Meta Attrs: clone-max=2 clone-node-max=1 interleave=true
         Resource: SAPHanaTopology_HA1_22 (class=ocf provider=heartbeat type=SAPHanaTopology)
          Attributes: InstanceNumber=22 SID=HA1
          Operations: methods interval=0s timeout=5 (SAPHanaTopology_HA1_22-methods-interval-0s)
                      monitor interval=10 timeout=600 (SAPHanaTopology_HA1_22-monitor-interval-10)
                      reload interval=0s timeout=5 (SAPHanaTopology_HA1_22-reload-interval-0s)
                      start interval=0s timeout=600 (SAPHanaTopology_HA1_22-start-interval-0s)
                      stop interval=0s timeout=300 (SAPHanaTopology_HA1_22-stop-interval-0s)




You can also check the cluster attributes by using the `crm_mon -A1` command.

### Create the SAPHana resource

The SAPHana resource agent manages the databases that are configured for SAP HANA system replication.

The following parameters in the SAPHana resource definition are optional:

  * `AUTOMATED_REGISTER`, which, when set to `true`, automatically registers the former primary as secondary when the DUPLICATE_PRIMARY_TIMEOUT expires after a takeover. The default is `false`.

For a [multi-tier](https://help.sap.com/viewer/4e9b18c116aa42fc84c7dbfd02111aba/2.0.05/en-US/2e6c71ab55f147e19b832565311a8e4e.html) an SAP HANA HA cluster, if you are using a version earlier than SAP HANA 2.0 SP03, set `AUTOMATED_REGISTER` to `false`. This prevents a recovered instance from attempting to self-register for replication to a HANA system that already has a replication target configured. For SAP HANA 2.0 SP03 or later, you can set `AUTOMATED_REGISTER` to `true` for SAP HANA configurations that use multitier system replication.

  * `DUPLICATE_PRIMARY_TIMEOUT`, which sets the time difference in seconds between two primary timestamps if a dual-primary situation occurs. The default is `7200`.

  * `PREFER_SITE_TAKEOVER`, which determines if local restarts are tried before failover is initiated. The default is `false`.




For additional information about these parameters see, [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Cloud](https://access.redhat.com/articles/3479821). A Red Hat subscription is required.

  1. As root on either host, create the SAP HANA resource:

### RHEL 8 and later
         
         # pcs resource create sap_hana_resource_name SAPHana SID=SID \
         InstanceNumber=inst_num \
         PREFER_SITE_TAKEOVER=true DUPLICATE_PRIMARY_TIMEOUT=7200 AUTOMATED_REGISTER=true \
         op start timeout=3600 \
         op stop timeout=3600 \
         op monitor interval=61 role="Slave" timeout=700 \
         op monitor interval=59 role="Master" timeout=700 \
         op promote timeout=3600 \
         op demote timeout=3600 \
         promotable meta notify=true clone-max=2 clone-node-max=1 interleave=true

### RHEL 7
         
         # pcs resource create sap_hana_resource_name SAPHana SID=SID \
         InstanceNumber=inst_num \
         PREFER_SITE_TAKEOVER=true DUPLICATE_PRIMARY_TIMEOUT=7200 AUTOMATED_REGISTER=true \
         op start timeout=3600 \
         op stop timeout=3600 \
         op monitor interval=61 role="Slave" timeout=700 \
         op monitor interval=59 role="Master" timeout=700 \
         op promote timeout=3600 \
         op demote timeout=3600 \
         master meta notify=true clone-max=2 clone-node-max=1 interleave=true

  2. Check the resulting resource attributes:

### RHEL 8 and later
         
         # pcs resource config sap_hana_resource_name

### RHEL 7
         
         # pcs resource show sap_hana_resource_name

You should see output similar to the following example:
         
         Resource: SAPHana_HA1_22 (class=ocf provider=heartbeat type=SAPHana)
           Attributes: AUTOMATED_REGISTER=true DUPLICATE_PRIMARY_TIMEOUT=7200 InstanceNumber=22 PREFER_SITE_TAKEOVER=true SID=HA1
           Meta Attrs: clone-max=2 clone-node-max=1 interleave=true notify=true
           Operations: demote interval=0s timeout=3600 (SAPHana_HA1_22-demote-interval-0s)
                       methods interval=0s timeout=5 (SAPHana_HA1_22-methods-interval-0s)
                       monitor interval=61 role=Slave timeout=700 (SAPHana_HA1_22-monitor-interval-61)
                       monitor interval=59 role=Master timeout=700 (SAPHana_HA1_22-monitor-interval-59)
                       promote interval=0s timeout=3600 (SAPHana_HA1_22-promote-interval-0s)
                       reload interval=0s timeout=5 (SAPHana_HA1_22-reload-interval-0s)
                       start interval=0s timeout=3600 (SAPHana_HA1_22-start-interval-0s)
                       stop interval=0s timeout=3600 (SAPHana_HA1_22-stop-interval-0s)

  3. After the resource is started, check the node attributes to see the current state of the SAP HANA databases on the nodes:
         
         # crm_mon -A1

You should see output similar to the following:
         
         Stack: corosync
         Current DC: hana-ha-vm-2 (version 1.1.19-8.el7_6.5-c3c624ea3d) - partition with quorum
         Last updated: Tue Jun 16 20:07:51 2020
         Last change: Tue Jun 16 20:07:26 2020 by root via crm_attribute on hana-ha-vm-1
         
         2 nodes configured
         6 resources configured
         
         Online: [ hana-ha-vm-1 hana-ha-vm-2 ]
         
         Active resources:
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):    Started hana-ha-vm-2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):    Started hana-ha-vm-1
         Clone Set: SAPHanaTopology_HA1_22-clone [SAPHanaTopology_HA1_22]
             Started: [ hana-ha-vm-1 hana-ha-vm-2 ]
         Master/Slave Set: SAPHana_HA1_22-master [SAPHana_HA1_22]
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-2 ]
         
         Node Attributes:
         * Node hana-ha-vm-1:
            + hana_ha1_clone_state              : PROMOTED
            + hana_ha1_op_mode                  : logreplay
            + hana_ha1_remoteHost               : hana-ha-vm-2
            + hana_ha1_roles                    : 4:P:master1:master:worker:master
            + hana_ha1_site                     : hana-ha-vm-1
            + hana_ha1_srmode                   : syncmem
            + hana_ha1_sync_state               : PRIM
            + hana_ha1_version                  : 1.00.122.27.1568902538
            + hana_ha1_vhost                    : hana-ha-vm-1
            + lpa_ha1_lpt                       : 1592338046
            + master-SAPHana_HA1_22             : 150
         * Node hana-ha-vm-2:
            + hana_ha1_clone_state              : DEMOTED
            + hana_ha1_op_mode                  : logreplay
            + hana_ha1_remoteHost               : hana-ha-vm-1
            + hana_ha1_roles                    : 4:S:master1:master:worker:master
            + hana_ha1_site                     : hana-ha-vm-2
            + hana_ha1_srmode                   : syncmem
            + hana_ha1_sync_state               : SOK
            + hana_ha1_version                  : 1.00.122.27.1568902538
            + hana_ha1_vhost                    : hana-ha-vm-2
            + lpa_ha1_lpt                       : 30
            + master-SAPHana_HA1_22             : 100




### Create a virtual IP address resource

You need to create a cluster resource for the VIP. The VIP resource is localized to the primary operating system and is not routable by other hosts. The load balancer routes traffic that is sent to the VIP to the backend host based on the health check.

As root on either host:
    
    
    # pcs resource create resource_name \
      IPaddr2 ip="vip-address" nic=lo cidr_netmask=32 \
      op monitor interval=3600s timeout=60s

The `vip-address` value is the same IP address that you reserved earlier and specified in the forwarding rule for the front-end of your load balancer. Change the network interface as appropriate for your configuration.

**Note:** To ensure that the SAP HANA cluster is future compatible and supports `systemd` dynamic NIC naming convention, use the loopback interface (`lo`) with the `IPaddr2` resource configuration instead of a static interface name like `ethX` or `ensX`.

### Create the constraints

You create constraints to define which services need to start first, and which services need to run together on the same host. For example, the IP address must be on the same host as the primary HANA instance.

  1. Define the start order constraint:

### RHEL 8 and later
         
         # pcs constraint order topology_resource_name-clone \
         then sap_hana_resource_name-clone symmetrical=false

### RHEL 7
         
         # pcs constraint order topology_resource_name-clone \
         then sap_hana_resource_name-master symmetrical=false

The specification of `symmetrical=false` means that the constraint applies to startup only and not to shutdown.

However, because you set `interleave=true` for these resources in a previous step, the processes can start in parallel. In other words, you can start SAPHana on any node as soon as SAPHanaTopology is running.

  2. Check the constraints:
         
         # pcs constraint

You should see output similar to the following:
         
         Location Constraints:
          Resource: STONITH-hana-ha-vm-1
            Disabled on:
              Node: hana-ha-vm-1 (score:-INFINITY)
          Resource: STONITH-hana-ha-vm-2
            Disabled on:
              Node: hana-ha-vm-2 (score:-INFINITY)
         Ordering Constraints:
          start SAPHanaTopology_HA1_22-clone then start SAPHana_HA1_22-master (kind:Mandatory) (non-symmetrical)
         Colocation Constraints:
         Ticket Constraints:




## Install listeners and create a health check resource

To configure a health check resource, you need to install the listeners first.

### Install a listener

The load balancer uses a listener on the health-check port of each host to determine where the primary instance of the SAP HANA cluster is running. 1\. As root on the master instance on the primary and secondary systems, install a TCP listener. These instructions install and use HAProxy as the listener. 
    
    
    # yum install haproxy

  1. Open the configuration file `haproxy.cfg` for editing:
         
         # vi /etc/haproxy/haproxy.cfg

     1. In the **defaults** section of the `haproxy.cfg`, change the `mode` to `tcp`.

     2. After the **defaults** section, create a new section by adding:
            
            #---------------------------------------------------------------------
            # Health check listener port for SAP HANA HA cluster
            #---------------------------------------------------------------------
            listen healthcheck
              bind *:healthcheck-port-num

The bind port is the same port that you used when you created the health check.

When you are done, your updates should look similar to the following example:
            
            #---------------------------------------------------------------------
            # common defaults that all the 'listen' and 'backend' sections will
            # use if not designated in their block
            #---------------------------------------------------------------------
            defaults
              **mode                    tcp**
              log                     global
              **option                  tcplog**
              option                  dontlognull
              option http-server-close
              # option forwardfor       except 127.0.0.0/8
              option                  redispatch
              retries                 3
              timeout http-request    10s
              timeout queue           1m
              timeout connect         10s
              timeout client          1m
              timeout server          1m
              timeout http-keep-alive 10s
              timeout check           10s
              maxconn                 3000
            
            **#---------------------------------------------------------------------
            # Set up health check listener for SAP HANA HA cluster
            #---------------------------------------------------------------------
            listen healthcheck
             bind *:60000**

  2. On each host as root, start the service to confirm it is correctly configured:
         
         # systemctl start haproxy.service

  3. On the Load balancer page in the Google Cloud console, click your load balancer entry:

[Load balancing page](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

In the **Backend** section on the **Load balancer details** page, if the HAProxy service is active on both hosts, you see `1/1` in the **Healthy** column of each instance group entry.

![Screen capture shows `1/1` in the Healthy column of both instance groups,
indicating that they are both healthy.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-ilb-backend-both-healthy.png)

  4. On each host, stop the HAProxy service:
         
         # systemctl stop haproxy.service

After you stop the HAProxy service on each host, `0/1` displays in the **Healthy** column of each instance group.

![Screen capture shows `0/1` in the Healthy column of each
instance group, indicating that there is no active listener.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-ilb-backend-both-unhealthy.png)

Later, when the health check is configured, the cluster restarts the listener on the master node.




### Create the health check resource

  1. On either host as root, create a health check resource for the HAProxy service:
         
         # pcs resource create healthcheck_resource_name service:haproxy op monitor interval=10s timeout=20s

  2. Confirm that the health check service is active on the same host as your master SAP HANA instance and VIP resource:
         
         # pcs status

If the health check resource is not on the primary host, move it with the following command:
         
         # pcs resource move healthcheck_resource_name target_host_name
         # pcs resource clear healthcheck_resource_name

The command `pcs resource clear` leaves the resource at its new location but removes the unwanted location constraint that the `pcs resource move` command created.

In the status, the resources section should look similar to the following example:
         
         Full list of resources:
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):    Started hana-ha-vm-2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):    Started hana-ha-vm-1
         Clone Set: SAPHanaTopology_HA1_22-clone [SAPHanaTopology_HA1_22]
             Started: [ hana-ha-vm-1 hana-ha-vm-2 ]
         Master/Slave Set: SAPHana_HA1_22-master [SAPHana_HA1_22]
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-2 ]
         rsc_vip_HA1_22 (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-1
         rsc_healthcheck_HA1    (service:haproxy):      Started hana-ha-vm-2

  3. Group the VIP and health check resources together:
         
         # pcs resource group add rsc-group-name healthcheck_resource_name vip_resource_name

In the cluster status, the resources section should look similar to the following example:
         
         Full list of resources:
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):    Started hana-ha-vm-2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):    Started hana-ha-vm-1
         Clone Set: SAPHanaTopology_HA1_22-clone [SAPHanaTopology_HA1_22]
             Started: [ hana-ha-vm-1 hana-ha-vm-2 ]
         Master/Slave Set: SAPHana_HA1_22-master [SAPHana_HA1_22]
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-2 ]
         **Resource Group: g-primary
             rsc_healthcheck_HA1        (service:haproxy):      Started hana-ha-vm-1
             rsc_vip_HA1_22     (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-1**

  4. Create a constraint that locates the new group on the same node as the master SAP HANA instance.

### RHEL 8 and later
         
         # pcs constraint colocation add rsc-group-name with master sap_hana_resource_name-clone 4000

### RHEL 7
         
         # pcs constraint colocation add rsc-group-name with master sap_hana_resource_name-master 4000

Your final constraints should look similar to the following example:
         
         # pcs constraint
         Location Constraints:
          Resource: STONITH-hana-ha-vm-1
            Disabled on:
              Node: hana-ha-vm-1 (score:-INFINITY)
          Resource: STONITH-hana-ha-vm-2
            Disabled on:
              Node: hana-ha-vm-2 (score:-INFINITY)
         Ordering Constraints:
          start SAPHanaTopology_HA1_22-clone then start SAPHana_HA1_22-master (kind:Mandatory) (non-symmetrical)
         Colocation Constraints:
          g-primary with SAPHana_HA1_22-master (score:4000) (rsc-role:Started) (with-rsc-role:Master)
         Ticket Constraints:




## Test failover

Test your cluster by simulating a failure on the primary host. Use a test system or run the test on your production system before you release the system for use.

Backup the system before the test.

You can simulate a failure in a variety of ways, including:

  * `HDB stop`
  * `HDB kill`
  * `iptables ... DROP` for instances with multiple network interfaces
  * `echo c > /proc/sysrq-trigger`



These instructions use `iptables` to simulate a network disruption between your two hosts in the cluster. Use the `ip link` command on an instance with a single network interface and use the `iptables` command on instances with one or more network interfaces. The test validates both failover as well as fencing. In the case where your instances have multiple network interfaces defined, you use the `iptables` command on the secondary host to drop incoming and outgoing traffic based on the IP used by the primary host for cluster communication, thereby simulating a network connection loss to the primary.

  1. On the secondary host, as root, use the `iptables` command to drop all incoming and outgoing network traffic to primary host.
         
         # iptables -A INPUT -s PRIMARY_CLUSTER_IP -j DROP; iptables -A OUTPUT -d PRIMARY_CLUSTER_IP -j DROP

  2. Once the primary host is fenced and restarted, delete the added lines from iptable on secondary host to re-initiate the network traffic to primary host. Reconnect to either host by using SSH and change to the root user.
         
         # iptables -D INPUT -s PRIMARY_CLUSTER_IP -j DROP; iptables -D OUTPUT -d PRIMARY_CLUSTER_IP -j DROP

  3. Enter `pcs status` to confirm that the primary host is now active on the VM that used to contain the secondary host. Automatic restart is enabled in the cluster, so the stopped host will restart and assume the role of secondary host, as shown in the following example.
         
         Cluster name: hana-ha-cluster
         Stack: corosync
         Current DC: hana-ha-vm-2 (version 1.1.19-8.el7_6.5-c3c624ea3d) - partition with quorum
         Last updated: Wed Jun 17 01:04:36 2020
         Last change: Wed Jun 17 01:03:58 2020 by root via crm_attribute on hana-ha-vm-2
         
         2 nodes configured
         8 resources configured
         
         Online: [ hana-ha-vm-1 hana-ha-vm-2 ]
         
         Full list of resources:
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):    Started hana-ha-vm-2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):    Started hana-ha-vm-1
         
         Clone Set: SAPHanaTopology_HA1_22-clone [SAPHanaTopology_HA1_22]
             Started: [ hana-ha-vm-1 hana-ha-vm-2  ]
         Master/Slave Set: SAPHana_HA1_22-master [SAPHana_HA1_22]
             Masters: [ hana-ha-vm-2 ]
             Slaves: [ hana-ha-vm-1  ]
         Resource Group: g-primary
             rsc_healthcheck_HA1        (service:haproxy):      Started hana-ha-vm-2
             rsc_vip_HA1_22     (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-2
         
         Daemon Status:
          corosync: active/enabled
          pacemaker: active/enabled
          pcsd: active/enabled




## Configure HANA Active/Active (Read Enabled)

Starting with SAP HANA 2.0 SPS1, you can configure [HANA Active/Active (Read Enabled)](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#sap_hana_activeactive_read_enabled) in a Pacemaker cluster. This is optional.

To configure HANA Active/Active (Read Enabled) in a Pacemaker cluster, complete the following steps.

### Configure the Cloud Load Balancing failover support for the secondary host

The internal passthrough Network Load Balancer service with failover support routes traffic to the secondary host in an SAP HANA cluster based on a health check service.

To configure failover support for the secondary host, follow these steps:

  1. Open Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address for the virtual IP by running the following command.

The virtual IP (VIP) address follows the secondary SAP HANA system. This is the IP address that applications use to access your secondary SAP HANA system. The load balancer routes traffic that is sent to the VIP to the VM instance that currently hosts the secondary system.

If you omit the `--addresses` flag in the following command, then an IP address in the specified subnet is chosen for you. For more information about reserving a static IP, see [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).
         
         $ [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) secondary-vip-name \
           --region cluster-region --subnet cluster-subnet \
           --addresses secondary-vip-address

  3. Create a Compute Engine health check by running the following command.

For the port used by the health check, choose a port that is in the private range, 49152-65535, to avoid clashing with other services. The port should be different from the one configured for the health check used for the HANA primary system access. The check-interval and timeout values are slightly longer than the defaults so as to increase failover tolerance during Compute Engine live migration events. You can adjust the values if necessary.
         
         $ [gcloud compute health-checks create tcp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp) secondary-health-check-name \
           --port=secondary-healthcheck-port-num \
           --proxy-header=NONE --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
           --healthy-threshold=2

  4. Configure the load balancer and failover group by running the following commands.

Here you create an additional backend service and use the same instance groups that you created earlier for the backend service behind the Internal TCP/UDP Load Balancer for your SAP HANA primary system.

     1. Create the load balancer backend service:
            
            $ [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) secondary-backend-service-name \
              --load-balancing-scheme internal \
              --health-checks secondary-health-check-name \
              --no-connection-drain-on-failover \
              --drop-traffic-if-unhealthy \
              --failover-ratio 1.0 \
              --region cluster-region \
              --global-health-checks

     2. Add the primary instance group to the backend service:
            
            $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) secondary-backend-service-name \
              --instance-group primary-ig-name \
              --instance-group-zone primary-zone \
              --region cluster-region

     3. Add the secondary, failover instance group to the backend service:
            
            $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) secondary-backend-service-name \
              --instance-group secondary-ig-name \
              --instance-group-zone secondary-zone \
              --failover \
              --region cluster-region

     4. Create a forwarding rule.

For the IP address flag, specify the IP address that you reserved for the VIP. If you need to access the HANA secondary system from outside of the region that you specify in the following command, then include the flag `--allow-global-access` in the forwarding rule's definition.
            
            $ [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) secondary-rule-name \
              --load-balancing-scheme internal \
              --address secondary-vip-name \
              --subnet cluster-subnet \
              --region cluster-region \
              --backend-service secondary-backend-service-name \
              --ports ALL

For more information about cross-region access to your SAP HANA high-availability system, see [Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal#client-access).




### Enable HANA Active/Active (Read Enabled)

On your secondary host, enable Active/Active (read enabled) for SAP HANA system replication by following these steps:

  1. As root, place the cluster in maintenance mode:
         
         $ pcs property set maintenance-mode=true

  2. As `SID_LCadm`, stop SAP HANA:
         
         > HDB stop

  3. As `SID_LCadm`, re-register the HANA secondary system with SAP HANA system replication using the operation mode `logreplay_readaccess`:
         
         > hdbnsutil -sr_register --remoteHost=primary-host-name --remoteInstance=inst_num \
          --replicationMode=syncmem --operationMode=logreplay_readaccess --name=secondary-host-name

  4. As `SID_LCadm`, start SAP HANA:
         
         > HDB start

  5. As `SID_LCadm`, confirm that HANA synchronization status is `ACTIVE`:
         
         > cdpy; python systemReplicationStatus.py --sapcontrol=1 | grep overall_replication_status

You should see an output similar to the following example:
         
         overall_replication_status=ACTIVE




### Configure Pacemaker

Configure your Pacemaker HA cluster for Active/Active (read enabled) by running the following commands as root:

  1. Set up listeners for the health checks:

     1. Copy and rename the default `haproxy.service` configuration file to make it into a template file for the multiple haproxy instances:
            
            # cp /usr/lib/systemd/system/haproxy.service \
                 /etc/systemd/system/haproxy@.service

     2. Edit the _[Unit]_ and _[Service]_ sections of the _haproxy@.service_ file to include the _%i_ instance parameter, as shown in the following example:

### RHEL 7
            
            [Unit]
            Description=**HAProxy Load Balancer %i**
            After=network-online.target
            
            
            
            [Service]
            EnvironmentFile=/etc/sysconfig/haproxy
            ExecStart=/usr/sbin/haproxy-systemd-wrapper -f /etc/haproxy/**haproxy-%i.cfg** -p /run/**haproxy-%i.pid** $OPTIONS
            ...
            

### RHEL 8
            
            [Unit]
            Description=**HAProxy Load Balancer %i**
            After=network-online.target
            Wants=network-online.target
            
            
            
            [Service]
            Environment="CONFIG=/etc/haproxy/**haproxy-%i.cfg** " "PIDFILE=/run/**haproxy-%i.pid** "
            ...
            

For more information from Red Hat about `systemd` unit templates, see [Working with instantiated units](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-systemd_configuring-basic-system-settings#con_working-with-instantiated-units_assembly_working-with-systemd-unit-files).

     3. Create an `haproxy.cfg` configuration file for your SAP HANA primary system. For example:
            
            # vi /etc/haproxy/haproxy-primary.cfg

     4. In the `haproxy-primary.cfg` configuration file for your SAP HANA primary system, insert the following configuration and replace `healthcheck-port-num` with the port number that you specified when you created the Compute Engine healthcheck for the HANA primary system earlier:
            
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
              bind *:healthcheck-port-num

     5. Create an `haproxy.cfg` configuration file for yor SAP HANA secondary system. For example:
            
            # vi /etc/haproxy/haproxy-secondary.cfg

     6. In the `haproxy-secondary.cfg` configuration file for your SAP HANA secondary system, insert the following configuration and replace `secondary-healthcheck-port-num` with the port number that you specified when you created the Compute Engine healthcheck for the HANA secondary system earlier:
            
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
              bind *:secondary-healthcheck-port-num

     7. Remove the existing listener configuration from `/etc/haproxy/haproxy.cfg`:
            
            #---------------------------------------------------------------------
            # Health check listener port for SAP HANA HA cluster
            #---------------------------------------------------------------------
            listen healthcheck
              bind *:healthcheck-port-num

     8. Reload the `systemd` services to load the changes:
            
            # systemctl daemon-reload

     9. Confirm that the two haproxy services are set up correctly:
            
            # systemctl start haproxy@primary
            # systemctl start haproxy@secondary
            
            # systemctl status haproxy@primary
            # systemctl status haproxy@secondary

The returned status should show the `haproxy@primary.service` and `haproxy@secondary.service` as `active (running)`. The following is an example output for `haproxy@primary.service`:
            
            ● haproxy@primary.service - Cluster Controlled haproxy@primary
              Loaded: loaded (/etc/systemd/system/haproxy@.service; disabled; vendor preset: disabled)
              Drop-In: /run/systemd/system/haproxy@primary.service.d
                       └─50-pacemaker.conf
              Active: **active (running)** since Fri 2022-10-07 23:36:09 UTC; 1h 13min ago
            Main PID: 21064 (haproxy-systemd)
              CGroup: /system.slice/system-haproxy.slice/haproxy@primary.service
                      ├─21064 /usr/sbin/haproxy-systemd-wrapper -f /etc/haproxy/haproxy-primary.cfg -p /run/hapro...
                      ├─21066 /usr/sbin/haproxy -f /etc/haproxy/haproxy-primary.cfg -p /run/haproxy-primary.pid -...
                      └─21067 /usr/sbin/haproxy -f /etc/haproxy/haproxy-primary.cfg -p /run/haproxy-primary.pid -...
            
            Oct 07 23:36:09 hana-ha-vm-1 systemd[1]: Started Cluster Controlled haproxy@primary.

     10. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your backend instance groups in both the primary and secondary backend services:
            
            $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) backend-service-name \
              --region cluster-region
            
            $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) secondary-backend-service-name \
              --region cluster-region

You should see an output similar to the following showing the VM you are currently working on, the `healthState` is `HEALTHY`:
            
            ---
            backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/hana-ha-ig-1
            status:
            healthStatus:
            ‐ healthState: HEALTHY
              instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/hana-ha-vm-1
              ipAddress: 10.0.0.35
              port: 80
            kind: compute#backendServiceGroupHealth
            

     11. Stop both services to let Pacemaker manage the services:
            
            # systemctl stop haproxy@primary
            # systemctl stop haproxy@secondary

     12. Repeat the preceding steps on each host in the cluster.

  2. Create a local cluster IP resource for the VIP address that you reserved for the secondary system:
         
         # pcs resource create secondary_vip_resource_name \
           IPaddr2 ip="secondary-vip-address" nic=lo cidr_netmask=32 \
           op monitor interval=3600s timeout=60s

  3. Set up the helper health-check service by running the following commands.

The load balancer uses a listener on the health-check port of each host to determine where the secondary instance of the SAP HANA cluster is running.

     1. To manage the listeners in the cluster, you create a resource for the listener:

        1. Delete the resource for the health check service for the HANA primary system:
               
               # pcs resource delete healthcheck_resource_name --force

        2. Add a new resource for the health check service for the HANA primary system:
               
               # pcs resource create primary_healthcheck_resource_name \
                service:haproxy@primary op monitor interval=10s timeout=20s

        3. Add a new resource for the health check service for the HANA secondary system:
               
               # pcs resource create secondary_healthcheck_resource_name \
                service:haproxy@secondary op monitor interval=10s timeout=20s

     2. Group the VIP and the helper health check service resources

        1. Add the new health check resource to the existing resource group for primary VIP resources:
               
               # pcs resource group add rsc-group-name primary_healthcheck_resource_name \
                --before vip_resource_name

        2. Add a new resource group to group the VIP and helper health check service resources for the HANA secondary system:
               
               # pcs resource group add secondary-rsc-group-name \
                secondary_healthcheck_resource_name secondary_vip_resource_name

  4. Create two location constraints by running the following commands:

These constraints are to ensure that the secondary VIP resource group is placed on the correct cluster node:
         
         # pcs constraint location secondary-rsc-group-name rule score=INFINITY \
           hana_sid_sync_state eq SOK and hana_sid_roles eq 4:S:master1:master:worker:master
         
         # pcs constraint location secondary-rsc-group-name rule score=2000 \
           hana_sid_sync_state eq PRIM and hana_sid_roles eq 4:P:master1:master:worker:master

  5. Exit cluster maintenance mode:
         
         # pcs property set maintenance-mode=false

  6. Check the status of the cluster:
         
         # pcs status

The following examples shows the status of an active, properly configured cluster for SAP HANA system replication with Active/Active (read enabled). You should see an additional resource group for the secondary system's VIP resources. In the following example, the name of that resource group is `g-secondary`.
         
         Cluster name: hacluster
           Stack: corosync
           Current DC: hana-ha-vm-1 (version 1.1.23-1.el7_9.1-9acf116022) - partition with quorum
           Last updated: Sat Oct  8 00:37:08 2022
           Last change: Sat Oct  8 00:36:57 2022 by root via crm_attribute on hana-test-2
         
           2 nodes configured
           10 resource instances configured
         
         Online: [ hana-ha-vm-1 hana-ha-vm-2 ]
         
         Full list of resources:
           STONITH-hana-ha-vm-1    (stonith:fence_gce):    Started hana-ha-vm-2
           STONITH-hana-ha-vm-2    (stonith:fence_gce):    Started hana-ha-vm-1
           Resource Group: g-primary
             rsc_healthcheck_HA1-primary        (service:haproxy@primary):      Started hana-ha-vm-1
             rsc_vip_HA1_00     (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-1
           Clone Set: SAPHanaTopology_HA1_00-clone [SAPHanaTopology_HA1_00]
             Started: [ hana-ha-vm-1 hana-ha-vm-2 ]
           Master/Slave Set: SAPHana_HA1_00-master [SAPHana_HA1_00]
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-2 ]
           Clone Set: msl_SAPHana_HA1_HDB00 [rsc_SAPHana_HA1_HDB00] (promotable):
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-2 ]
           Resource Group: g-secondary
             rsc_healthcheck_HA1-secondary        (service:haproxy@secondary):      Started hana-ha-vm-2
             rsc_vip_HA1_00-secondary     (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-2
         




## Evaluate your SAP HANA workload

To automate continuous validation checks for your SAP HANA high-availability workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager allows you to automatically scan and evaluate your SAP HANA high-availability workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP HANA high-availability workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## Troubleshooting

To troubleshoot problems with high-availability configurations for SAP HANA on RHEL, see [Troubleshooting high-availability configurations for SAP](https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha).

## Getting support for SAP HANA on RHEL

If you need help resolving a problem with high-availability clusters for SAP HANA on RHEL, gather the required diagnostic information and contact Cloud Customer Care. For more information, see [High-availability clusters on RHEL diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-rhel).

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



### Connecting to SAP HANA

If the host VMs don't have an external IP address for SAP HANA, you can only connect to the SAP HANA instances through the bastion instance using SSH or through the Windows server through SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instance(s) by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server instance. After connection, manually [install SAP HANA Studio](https://help.sap.com/hana/SAP_HANA_Studio_Installation_Update_Guide_en.pdf) and access your SAP HANA database.




## Post-deployment tasks

After you complete the deployment, finish with the following steps:

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser. For example:
         
         sudo passwd SID_LCadm

For information from SAP about changing the password, see [Reset the SYSTEM User Password of the System Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/6b13cdd1982f4aa6b90b443663d17d7e.html).

  2. Before using your SAP HANA instance, configure and backup your new SAP HANA database.

  3. If your SAP HANA system is deployed on a VirtIO network interface, then we recommend that you ensure the value of the TCP parameter `/proc/sys/net/ipv4/tcp_limit_output_bytes` is set to `1048576`. This modification helps improve the overall network throughput on the VirtIO network interface without affecting the network latency. 




For more information, see:

  * [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).
  * [SAP HANA Installation and Update Guide](http://help.sap.com/hana/SAP_HANA_Server_Installation_Guide_en.pdf).



## What's next

See the following resource for more information: 

  * [Installing and Configuring a Red Hat Enterprise Linux 7.6 (and later) High-Availability Cluster on Google Compute Cloud](https://access.redhat.com/articles/3479821)
  * [Automated SAP HANA System Replication in Scale-Up in pacemaker cluster](https://access.redhat.com/articles/3004101)
  * [Support Policies for RHEL High Availability Clusters - General Requirements for Fencing/STONITH](https://access.redhat.com/articles/2881341)
  * [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide)
  * [SAP HANA disaster recovery planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide)
  * For more information about VM administration and monitoring, see the [SAP HANA Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
