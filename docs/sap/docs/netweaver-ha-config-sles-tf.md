---
url: https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf/
title: Terraform: HA cluster configuration guide for SAP NetWeaver on SLES \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:27.410130+00:00
---

# Terraform: HA cluster configuration guide for SAP NetWeaver on SLES  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Terraform: HA cluster configuration guide for SAP NetWeaver on SLES Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to automate the deployment of a performance-optimized SUSE Linux Enterprise Server (SLES) high-availability (HA) cluster for SAP NetWeaver. [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) configuration is also provided for SLES 15 for SAP and later.

The guide uses [Terraform](https://docs.cloud.google.com/docs/terraform) to deploy two Compute Engine virtual machines (VMs), a virtual IP address (VIP) with an internal passthrough Network Load Balancer implementation, and an OS-based HA cluster, all according to the best practices from Google Cloud, SAP, and the OS vendor.

Except for the procedures that are specific to the Standalone Enqueue Server 2 (ENSA2), which is available only in ABAP, this guide applies to both ABAP and Java SAP NetWeaver stacks. 

Unless an exception is indicated in the guide, examples that use "ASCS" are valid for both ABAP SAP Central Services (ASCS) and Java SAP Central Services (SCS). 

If you are using a Java stack, before you use the commands or examples in this guide, replace any instances of "ASCS" with "SCS". 

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
  * When you create your VMs, specify a network tag for each VM for use in routing and firewall rules. When you use the Terraform configuration file that Google Cloud provides, specify a tag with `network_tags = "TAG"`.



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

To create a VPC network for your project, complete the following steps:

  1. Create a custom mode network. For more information, see [Creating a custom mode network](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_1).

  2. Create a subnetwork, and specify the region and IP range. For more information, see [Adding subnets](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_2).




## Setting up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#terraform).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

## Adding firewall rules

By default, incoming connections from outside your Google Cloud network are blocked. To allow incoming connections, set up a firewall rule for your VM. Firewall rules regulate only new incoming connections to a VM. After a connection is established with a VM, traffic is permitted in both directions over that connection.

You can create a firewall rule to allow access to specified ports, or to allow access between VMs on the same subnetwork.

Create firewall rules to allow access for such things as:

  * The default ports used by SAP NetWeaver, as documented in [TCP/IP Ports of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine VM instance. If you are unsure of what IP address to use, talk to your company's network admin.
  * Communication between VMs in a 3-tier, scaleout, or high-availability configuration. For example, if you are deploying a 3-tier system, you will have at least 2 VMs in your subnetwork: the VM for SAP NetWeaver, and another VM for the database server. To enable communication between the two VMs, you must create a firewall rule to allow traffic that originates from the subnetwork. 
  * Cloud Load Balancing health checks. 



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

## Creating a high-availability Linux cluster for SAP NetWeaver

The following instructions use a Terraform configuration file to create a SLES cluster with two SAP NetWeaver systems, a primary single-host SAP NetWeaver system on one VM instance and a standby SAP NetWeaver system on another VM instance in the same Compute Engine region.

You define configuration options for the SAP NetWeaver high-availability cluster in a Terraform configuration file.

  1. Open the Cloud Shell.

[Go to the Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the `sap_nw_ha.tf` configuration file for the SAP NetWeaver high-availability cluster to your working directory:
         
         $ wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_nw_ha/terraform/sap_nw_ha.tf

**Note:** Ensure that you have only a single Terraform configuration file in your working directory.
  3. Open the `sap_nw_ha.tf` file in the Cloud Shell code editor.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  4. In the `sap_nw_ha.tf` file, update the argument values by replacing the contents inside the double quotation marks with the values for your installation. The arguments are described in the following table.

Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `sap_nw_ha.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`machine_type` | String |  Specify the type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms) (VM) on which you need to run your SAP system. If you need a custom VM type, then specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-custom) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations). For example, `n1-highmem-32`.  
`network` | String |  Specify the name of the network in which you need to create the load balancer that manages the VIP.  If you are using a shared VPC network, you must add the ID of the host project as a parent directory of the network name. For example, `HOST_PROJECT_ID/NETWORK_NAME`.   
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `sles-15-sp6-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`sap_primary_instance` | String | Specify a name for the VM instance for the primary SAP NetWeaver system. This is your initial ASCS location. The name can contain lowercase letters, numbers, or hyphens and must not exceed 13 characters.  
`sap_primary_zone` | String | Specify a zone in which the primary SAP NetWeaver system is deployed. The primary and secondary zones must be in the same region. For example, `us-east1-b`.   
`sap_secondary_instance` | String | Specify a name for the VM instance for the secondary SAP NetWeaver system. This is your initial ERS location. The name can contain lowercase letters, numbers, or hyphens and must not exceed 13 characters.  
`sap_secondary_zone` | String | Specify a zone in which the secondary SAP NetWeaver system is deployed. The primary and secondary zones must be in the same region. For example, `us-east1-c`.  
`nfs_path` | String | Specify the NFS mount point for the shared file system. For example, `10.163.58.114:/ssd_nfs`. **Note** : The NFS mount point for the shared file system must be empty before you apply the Terraform configuration.  
`sap_sid` | String | Specify an SAP system ID. The ID must consist of three alpha-numeric characters and begin with a letter. All letters must be in uppercase. For example, `ED1`.  
`hc_firewall_rule_name` | String | Optional. Specify a name for the health check firewall rule. The default value is `SAP_SID-hc-allow`.  
`hc_network_tag` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for the health check firewall rule. The default value is `SAP_SID-hc-allow-tag`.  
`scs_inst_group_name` | String | Optional. Specify a name for the ASCS instance group. The default value is `SAP_SID-scs-ig`.  
`scs_hc_name` | String | Optional. Specify a name for the ASCS health check. The default value is `SAP_SID-scs-hc`.  
`scs_hc_port` | String | Optional. Specify a port for the ASCS health check. To avoid clashing with other services, designate the port number for the ASCS health check in the private range, 49152-65535. The default value is `60000`.  
`scs_vip_address` | String | Optional. Specify an unused IP address within the subnetwork specified on `subnetwork` earlier to use as the virtual IP address for the ASCS instance. If nothing is specified, the deployment scripts automatically select an unused IP address from the specified subnetwork.  
`scs_vip_name` | String | Optional. Specify a name for the ASCS virtual IP. The default value is `SAP_SID-scs-vip`.  
`scs_backend_svc_name` | String | Optional. Specify a name for the ASCS backend service. The default value is `SAP_SID-scs-backend-svc`.  
`scs_forw_rule_name` | String | Optional. Specify a name for the ASCS forwarding rule. The default value is `SAP_SID-scs-fwd-rule`.  
`ers_inst_group_name` | String | Optional. Specify a name for the ERS instance group. The default value is `SAP_SID-ers-ig`.  
`ers_hc_name` | String | Optional. Specify a name for the ERS health check. The default value is `SAP_SID-ers-hc`.  
`ers_hc_port` | String | Optional. Specify a port for the ERS health check. To avoid clashing with other services, designate the port number for ERS health check in the private range, 49152-65535. The default value is `60010`.  
`ers_vip_address` | String | Optional. Specify an unused IP address within the subnetwork specified on `subnetwork` earlier to use as the virtual IP address for the ERS instance. If nothing is specified, the deployment scripts automatically select an unused IP address from the specified subnetwork.  
`ers_vip_name` | String | Optional. Specify a name for the ERS virtual IP. The default value is `SAP_SID-ers-vip`.  
`ers_backend_svc_name` | String | Optional. Specify a name for the ERS backend service. The default value is `SAP_SID-ers-backend-svc`.  
`ers_forw_rule_name` | String | Optional. Specify a name for the ERS forwarding rule. The default value is `SAP_SID-ers-fwd-rule`.  
`usr_sap_size` | Integer |  Optional. Specify the size of the `/usr/sap` disk in GB. The minimum size is 8 GB. The default value is `8`.   
`swap_size` | Integer |  Optional. Specify the size of the swap volume in GB. The minimum size is 8 GB. The default value is `8`.   
`sap_scs_instance_number` | String | Optional. Specify the ASCS instance number. The `sap_scs_instance_number` must be a two-digit number. If you need to specify a single digit number, then add a `0` in front of the number. For example, `07`. The default value is `00`.   
`sap_ers_instance_number` | String | Optional. Specify the ERS instance number. The `sap_ers_instance_number` must be a two-digit number. If you need to specify a single digit number, then add a `0` in front of the number. For example, `07`. The default value is `10`.   
`sap_nw_abap` | Boolean | Optional. Specify whether you are deploying an ABAP stack or a Java stack of SAP NetWeaver. For a Java stack of SAP NetWeaver, specify `false`. The default value is `true`.  
`pacemaker_cluster_name` | String | Optional. Specify a name for the pacemaker cluster. The default value is `SAP_SID-cluster`.  
`public_ip` | Boolean |  Optional. To create an ephemeral public IP address for the VM instances, set the `public_ip` to `true`. The default value is `false`. **Caution:** When the `public_ip` is `false`, ensure that you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`service_account` | String | Optional. Specify the email address of a user-managed service account to be used by the host VMs and by the programs that run on the host VMs. For example, `svc-acct-name@project-id.iam.gserviceaccount.com`.  If you specify this argument without a value, or omit it, then the installation script uses the Compute Engine default service account. For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).   
`network_tags` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for firewall or routing purposes.  A network tag for the ILB components is automatically added to VM's **Network tags**.  If `public_ip = false` and you don't specify a network tag, then make sure to provide another means of access to the internet.   
`sap_deployment_debug` | Boolean | Optional. Only when Cloud Customer Care asks you to enable debugging for your deployment, specify `true`, which makes the deployment generate verbose deployment logs. The default value is `false`.   
`primary_reservation_name` | String | Optional. To use a specific [Compute Engine VM reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) for provisioning the VM instance that hosts your HA cluster's primary SAP HANA instance, specify the name of the reservation. By default, the installation script selects any available Compute Engine reservation based on the following conditions.  For a reservation to be usable, regardless of whether you specify a name or the installation script selects it automatically, the reservation must be set with the following: 
     * The `specificReservationRequired` option is set to `true` or, in the Google Cloud console, the **Select specific reservation** option is selected. 
     * Some Compute Engine machine types support CPU platforms that are not covered by the SAP certification of the machine type. If the target reservation is for any of the following machine types, then the reservation must specify the minimum CPU platforms as indicated: 
       * `n1-highmem-32`: Intel Broadwell
       * `n1-highmem-64`: Intel Broadwell
       * `n1-highmem-96`: Intel Skylake
       * `m1-megamem-96`: Intel Skylake
The minimum CPU platforms for all of the other machine types that are certified by SAP for use on Google Cloud conform to the SAP minimum CPU requirement.   
`secondary_reservation_name` | String | Optional. To use a specific [Compute Engine VM reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) for provisioning the VM instance that hosts your HA cluster's secondary SAP HANA instance, specify the name of the reservation. By default, the installation script selects any available Compute Engine reservation based on the following conditions.  For a reservation to be usable, regardless of whether you specify a name or the installation script selects it automatically, the reservation must be set with the following: 
     * The `specificReservationRequired` option is set to `true` or, in the Google Cloud console, the **Select specific reservation** option is selected. 
     * Some Compute Engine machine types support CPU platforms that are not covered by the SAP certification of the machine type. If the target reservation is for any of the following machine types, then the reservation must specify the minimum CPU platforms as indicated: 
       * `n1-highmem-32`: Intel Broadwell
       * `n1-highmem-64`: Intel Broadwell
       * `n1-highmem-96`: Intel Skylake
       * `m1-megamem-96`: Intel Skylake
The minimum CPU platforms for all of the other machine types that are certified by SAP for use on Google Cloud conform to the SAP minimum CPU requirement.   
`can_ip_forward` | Boolean | Specify whether sending and receiving of packets with non-matching source or destination IPs is allowed, which enables a VM to act like a router. The default value is `true`. If you only intend to use Google's internal load balancers to manage virtual IPs for the deployed VMs, then set the value to `false`. An internal load balancer is automatically deployed as part of high availability templates.  
  
The following example shows a completed configuration file that defines a high-availability cluster for SAP NetWeaver. The cluster uses an internal passthrough Network Load Balancer to manage the VIP.

Terraform deploys the Google Cloud resources that are defined in the configuration file and then scripts take over to configure the operating system and configure the Linux HA cluster.

For clarity, comments in the configuration file are omitted in the example.
    
    # ...
         module "sap_nw_ha" {
         source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_nw_ha/sap_nw_ha_module.zip"
       #
       # By default, this source file uses the latest release of the terraform module
       # for SAP on Google Cloud.  To fix your deployments to a specific release
       # of the module, comment out the source argument above and uncomment the source argument below.
       #
       # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/202201240926/terraform/sap_nw_ha/sap_nw_ha_module.zip"
       #
       # ...
       #
       project_id = "example-project-123456"
       machine_type = "n2-highmem-32"
       network = "example-network"
       subnetwork = "example-subnet-us-central1"
       linux_image = "sles-15-sp3-sap"
       linux_image_project = "suse-sap-cloud"
    
       sap_primary_instance = "example-nw1"
       sap_primary_zone = "us-central1-a"
    
       sap_secondary_instance = "example-nw2"
       sap_secondary_zone = "us-central1-c"
    
       nfs_path = "10.223.55.130:/pr1_nw"
    
       sap_sid = "PR1"
       # ...
    }

  5. Initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud:
         
         terraform init

The `terraform init` command prepares your working directory for other Terraform commands.

To force a refresh of the provider plugin and configuration files in your working directory, specify the `--upgrade` flag. If the `--upgrade` flag is omitted and you don't make any changes in your working directory, Terraform uses the locally cached copies, even if `latest` is specified in the `source` URL.
         
         terraform init --upgrade 

  6. Optionally, create the Terraform execution plan:
         
         terraform plan

The `terraform plan` command shows the changes that are required by your current configuration. If you skip this step, the `terraform apply` command automatically creates a new plan and prompts you to approve it.

  7. Apply the execution plan:
         
         terraform apply

When you are prompted to approve the actions, enter `yes`.

The `terraform apply` command sets up the Google Cloud infrastructure and then hands control over to a script that configures the HA cluster according to the arguments defined in the terraform configuration file.

While Terraform has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the Logging logs.

Time to completion can vary, but the entire process usually takes less than 30 minutes.




## Verifying the deployment of your SAP NetWeaver HA system

Verifying an SAP NetWeaver HA cluster involves several different procedures:

  * Check the logs
  * Check the configuration of the VM



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

       2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

       3. Go to your working directory and delete the deployment to clean up the VMs and persistent disks from the failed installation:
              
              terraform destroy

When you are prompted to approve the action, enter `yes`.

       4. Rerun your deployment.




### Check the configuration of the VM

  1. After the VM instances deploy without errors, connect to each VM by using SSH. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for each VM instance, or you can use your preferred SSH method.

  2. Change to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output that includes the `/usr/sap` directories, such as `/usr/sap/trans`.
         
         example-nw1:~ # df -h
           Filesystem                             Size  Used Avail Use% Mounted on
           ...
           /dev/mapper/vg_usrsap-vol              8.0G   41M  8.0G   1% /usr/sap
           /dev/mapper/vg_sapmnt-vol              8.0G   41M  8.0G   1% /sapmnt
           10.233.55.130:/pr1_nw/sapmntPR1       1007G     0  956G   0% /sapmnt/PR1
           10.223.55.130:/pr1_nw/usrsaptrans     1007G     0  956G   0% /usr/sap/trans
           10.223.55.130:/pr1_nw/usrsapPR1       1007G     0  956G   0% /usr/sap/PR1
           ...
           

`autofs` is automatically configured during the deployment to mount the common shared file directories when the file directories are first accessed. The mounting of the `ASCSASCS_INSTANCE_NUMBER` and `ERSERS_INSTANCE_NUMBER` directories is managed by the cluster software, which is also set up during deployment.
  4. Check the status of the new cluster by entering the status command:
         
         crm status

You should see results similar to the following the example, in which both VM instances are started and `example-nw1` is the active primary instance: 
         
         example-nw1:~ # crm status
         Cluster Summary:
           * Stack: corosync
           * Current DC: example-nw1 (version 2.0.4+20200616.2deceaa3a-3.6.1-2.0.4+20200616.2deceaa3a) - partition with quorum
           * Last updated: Fri Jun 18 05:47:48 2021
           * Last change:  Fri Jun 18 05:41:32 2021 by root via cibadmin on example-nw1
           * 2 nodes configured
           * 8 resource instances configured
         Node List:
           * Online: [ example-nw1 example-nw2 ]
         Full List of Resources:
           * fence-PR1-example-nw1     (stonith:fence_gce):           Started example-nw2
           * fence-PR1-example-nw2     (stonith:fence_gce):           Started example-nw1
           * file-system-PR1-ASCS00    (ocf::heartbeat:Filesystem):      Started example-nw1
           * file-system-PR1-ERS10     (ocf::heartbeat:Filesystem):      Started example-nw2
           * health-check-PR1-ASCS00   (ocf::heartbeat:anything):        Started example-nw1
           * health-check-PR1-ERS10    (ocf::heartbeat:anything):        Started example-nw2
           * vip-PR1-ASCS00      (ocf::heartbeat:IPaddr2):             Started example-nw1
           * vip-PR1-ERS10       (ocf::heartbeat:IPaddr2):             Started example-nw2

If you're using a [Simple Mount](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform) setup, then you see an output similar to the following example:
         
         Stack: corosync
         Current DC: example-nw1 (version 1.1.24+20201209.8f22be2ae-3.12.1-1.1.24+20201209.8f22be2ae) - partition with quorum
         Last updated: Wed Sep 26 19:10:10 2024
         Last change: Tue Sep 25 23:48:35 2024 by root via cibadmin on example-nw1
         2 nodes configured
         8 resource instances configured
         Node List:
           * Online: [ example-nw1 example-nw2 ]
         Full list of resources:
          * fence-PR1-example-nw1     (stonith:fence_gce):           Started example-nw2
           * fence-PR1-example-nw2     (stonith:fence_gce):           Started example-nw1
           * health-check-PR1-ASCS00   (ocf::heartbeat:anything):        Started example-nw1
           * health-check-PR1-ERS10    (ocf::heartbeat:anything):        Started example-nw2
           * vip-PR1-ASCS00      (ocf::heartbeat:IPaddr2):             Started example-nw1
           * vip-PR1-ERS10       (ocf::heartbeat:IPaddr2):             Started example-nw2

  5. Test the ASCS and ERS load balancer setup by using the `socat` utility:

     1. On each VM instance, temporarily start a `socat` process that returns its own hostname:
            
            socat TCP-LISTEN:80,bind=0.0.0.0,fork,reuseaddr,crlf SYSTEM:"echo HTTP/1.0 200; echo Content-Type\: text/plain; echo; echo $(hostname)" & 

     2. On each node, use `curl` and try reaching the following IP addresses and hostnames. The IP addresses and hostnames can be found in `/etc/hosts`.

        * `127.0.0.1`
        * `localhost`
        * `ASCS_VIRTUAL_HOST_NAME`
        * `ASCS_IP_ADDRESS`
        * `ERS_VIRTUAL_HOST_NAME`
        * `ERS_IP_ADDRESS`
        * SCS VIP name, which is specified for the parameter `scs_vip_name`
        * SCS VIP IP address, which is specified for the parameter `scs_vip_address`
        * ERS VIP name, which is specified for the parameter `ers_vip_name`
        * ERS VIP IP address, which is specified for the parameter `ers_vip_address`

The following is an example output from such a test:
    
    example-nw1:~ # cat /etc/hosts
    ...
    10.128.1.182 example-nw1.c.myproject.internal example-nw1
    10.128.1.169 example-nw2.c.myproject.internal example-nw2
    10.128.1.46 pr1-scs-vip.c.myproject.internal pr1-scs-vip
    10.128.0.75 pr1-ers-vip.c.myproject.internal pr1-ers-vip
    example-nw1:~ # curl 127.0.0.1
    example-nw1
    example-nw1:~ # curl localhost
    example-nw1
    example-nw1:~ # curl example-nw1
    example-nw1
    example-nw1:~ # curl 10.128.1.182
    example-nw1
    example-nw1:~ # curl example-nw2
    example-nw2
    example-nw1:~ # curl 10.128.1.169
    example-nw2
    example-nw1:~ # curl pr1-scs-vip
    example-nw1
    example-nw1:~ # curl 10.128.1.46
    example-nw1
    example-nw1:~ # curl pr1-ers-vip
    example-nw2
    example-nw1:~ # curl 10.128.0.75
    example-nw2




If any of the validation steps show that the installation failed:

  1. Resolve the errors.

  2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Go to the directory that contains the Terraform configuration file.

  4. Delete the deployment:
         
         terraform destroy

When you are prompted to approve the action, enter `yes`.

  5. Rerun your deployment.




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

     * When you start SWPM, use the `SAPINST_USE_HOSTNAME` parameter to specify the virtual hostname that you defined for the ASCS VIP address in the `/etc/hosts` file.

For example: 
           
           cd /tmp; /mnt/nfs/install/SWPM/sapinst SAPINST_USE_HOSTNAME=pr1-scs-vip

     * On the final SWPM confirmation page, ensure that the virtual hostname is correct.

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

     * When you start SWPM, use the `SAPINST_USE_HOSTNAME` parameter to specify the virtual hostname that you defined for the ERS VIP address in the `/etc/hosts` file.

For example: 
           
           cd /tmp; /mnt/nfs/install/SWPM/sapinst SAPINST_USE_HOSTNAME=pr1-ers-vip

     * On the final SWPM confirmation page, ensure that the virtual hostname is correct.

  5. Take the primary VM out of standby to have both active:
         
         # crm_standby -v off -N ${HOSTNAME};




## Configure the SAP services

You need to confirm that the services are configured correctly, check the settings in the ASCS and ERS profiles, and add the SID_LCadm user to the `haclient` user group.

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

When you installed the `sap-suse-cluster-connector`, the installation created an `haclient` user group. To enable the SID_LCadm user to work with the cluster, add it to the `haclient` user group.

  1. On both servers, add the SID_LCadm user to the `haclient` user group:
         
         # usermod -aG haclient SID_LCadm




## Configure the cluster resources for ASCS and ERS

**Note:** If you are using a [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) volume for your shared NFS storage, then you must adjust the Pacemaker resource timeout settings for the `SAPInstance` resources to accommodate potential I/O pauses during NetApp Volumes maintenance events. 

To prevent cluster failovers during maintenance events, adjust the `interval` and `timeout` monitor settings for the `SAPInstance` resources. The monitor interval must align with the filesystem resource monitor interval , and the timeout must be larger than the filesystem timeout.

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
         SUCCESS, SAP CONFIGURATION, SAPInstance RA sufficient version (pr1-scs-vip_PR1_00), SAPInstance includes is-ers patch
         SUCCESS, SAP CONFIGURATION, Enqueue replication (pr1-scs-vip_PR1_00), Enqueue replication enabled
         SUCCESS, SAP STATE, Enqueue replication state (pr1-scs-vip_PR1_00), Enqueue replication active

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

If you created 10 locks, you should see output similar to the following example:
         
         locks_now: 10

  3. As `SID_LCadm`, on the server where ERS is active, start the monitoring function, `OpCode=20`, of the `enqt` program:
         
         > enqt pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME 20 1 1 9999

For example:
         
         > enqt pf=/sapmnt/PR1/profile/PR1_ERS10_pr1-ers-vip 20 1 1 9999

  4. Where ASCS is active, reboot the server.

On the monitoring server, by the time Pacemaker stops ERS to move it to the other server, you should see output similar to the following.
         
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

If you created 10 locks, you should see output similar to the following example:
         
         locks_now: 10

  3. Where ERS is active, confirm that the lock entries were replicated:
         
         > sapcontrol -nr ERS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

The number of returned locks should be the same as on the ASCS instance.

  4. Where ASCS is active, reboot the server.

  5. Optionally, as root on either server, monitor the cluster failover:
         
         # crm_mon

  6. As `SID_LCadm`, on the server where ASCS was restarted, verify that the lock entries were retained:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

  7. As `SID_LCadm`, on the server where ERS is active, after you confirm the locks were retained, release the locks:
         
         > enq_admin --release_locks=NUMBER_OF_LOCKS:X:DIAG::TAB:%u pf=/PATH_TO_PROFILE/SID_ERSERS_INSTANCE_NUMBER_ERS_VIRTUAL_HOST_NAME

  8. As `SID_LCadm`, on the server where ASCS is active, verify that the lock entries are removed:
         
         > sapcontrol -nr ASCS_INSTANCE_NUMBER -function EnqGetStatistic | grep locks_now

You should see output similar to the following example:
         
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
