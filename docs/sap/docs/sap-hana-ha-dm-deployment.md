---
url: https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment/
title: Deployment Manager: SAP HANA scale-up high-availability cluster configuration guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:40.511727+00:00
---

# Deployment Manager: SAP HANA scale-up high-availability cluster configuration guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deployment Manager: SAP HANA scale-up high-availability cluster configuration guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reaches end of support on March 31, 2026. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To automate the deployment of an SAP HANA scale-up system in a high-availability cluster on Google Cloud, we recommend that you use Terraform. For more information, see [Terraform: SAP HANA scale-up high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment).

This guide shows you how to automate the deployment of SAP HANA in a Red Hat Enterprise Linux (RHEL) or SUSE Linux Enterprise Server (SLES) high-availability (HA) cluster that uses an internal passthrough Network Load Balancer to manage the virtual IP (VIP) address.

The guide uses [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs) to deploy two Compute Engine virtual machines (VMs), two SAP HANA scale up systems, a virtual IP address (VIP) with an internal passthrough Network Load Balancer implementation, and an OS-based HA cluster, all according to the best practices from Google Cloud, SAP, and the OS vendor.

One of the SAP HANA systems functions as the primary, active system and the other functions as a secondary, standby system. You deploy both SAP HANA systems within the same region, ideally in different zones.

![Overview of a high-availability Linux cluster for a single-node SAP HANA scaleup system](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-scaleup-overview.svg)

The deployed cluster includes the following functions and features:

  * The Pacemaker high-availability cluster resource manager.
  * A Google Cloud fencing mechanism.
  * A virtual IP (VIP) that uses a level 4 TCP internal load balancer implementation, including: 
    * A reservation of the IP address that you select for the VIP
    * Two Compute Engine instance groups
    * A TCP internal load balancer
    * A Compute Engine health check
  * In RHEL HA clusters: 
    * The Red Hat high-availability pattern
    * The Red Hat resource agent and fencing packages
  * In SLES HA clusters: 
    * The SUSE high-availability pattern.
    * The SUSE SAPHanaSR resource agent package.
  * Synchronous system replication.
  * Memory preload.
  * Automatic restart of the failed instance as the new secondary instance.



To deploy an SAP HANA system without a Linux high-availability cluster or standby hosts, use the [SAP HANA Deployment Guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide).

This guide is intended for advanced SAP HANA users who are familiar with Linux high-availability configurations for SAP HANA.

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

HA clusters for SAP HANA require at least two firewall rules, one that allows the Compute Engine health check to check the health of the cluster nodes and another that allows the cluster nodes to communicate with each other. 

If you are not using a shared VPC network, you need to create the firewall rule for the communication between the nodes, but not for the health checks. The Deployment Manager template creates the firewall rule for the health checks, which you can modify after deployment is complete, if needed.

If you are using a shared VPC network, a network administrator needs to create both firewall rules in the host project. 

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.
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

## Creating a high-availability Linux cluster with SAP HANA installed

The following instructions use the Cloud Deployment Manager to create a RHEL or SLES cluster with two SAP HANA systems: a primary single-host SAP HANA system on one VM instance and a standby SAP HANA system on another VM instance in the same Compute Engine region. The SAP HANA systems use synchronous system replication and the standby system preloads the replicated data.

You define configuration options for the SAP HANA high-availability cluster in a Deployment Manager configuration file template.

The following instructions use the Cloud Shell, but are generally applicable to the Google Cloud CLI.

  1. Confirm that your current quotas for resources such as persistent disks and CPUs are sufficient for the SAP HANA systems you are about to install. If your quotas are insufficient, deployment fails. For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to the quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Open the Cloud Shell or, if you installed the Google Cloud CLI on your local workstation, open a terminal.

[Go to the Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `template.yaml` configuration file template for the SAP HANA high-availability cluster to your working directory by entering the following command in the Cloud Shell or gcloud CLI:
         
         $ wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana_ha_ilb/template.yaml

  4. Optionally, rename the `template.yaml` file to identify the configuration it defines.

  5. Open the `template.yaml` file in the Cloud Shell code editor or, if you are using the gcloud CLI, the text editor of your choice.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  6. In the `template.yaml` file, update the property values by replacing the brackets and their contents with the values for your installation. The properties are described in the following table.

To create the VM instances without installing SAP HANA, delete or comment out all of the lines that begin with `sap_hana_`.

Property | Data type | Description  
---|---|---  
`type` | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
`primaryInstanceName` | String | The name of the VM instance for the primary SAP HANA system. Specify the name in lowercase letters, numbers, or hyphens.  
`secondaryInstanceName` | String | The name of the VM instance for the secondary SAP HANA system. Specify the name in lowercase letters, numbers, or hyphens.  
`primaryZone` | String | The zone in which the primary SAP HANA system is deployed. The primary and secondary zones must be in the same region.  
`secondaryZone` | String | The zone in which the secondary SAP HANA system will be deployed. The primary and secondary zones must be in the same region.  
`instanceType` | String | The type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#vm_types) that you need to run SAP HANA on. If you need a custom VM type, specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations).  
`network` | String | The name of the network in which to create the load balancer that manages the VIP.  If you are using a shared VPC network, you must add the ID of the host project as a parent directory of the network name. For example, `host-project-id/network-name`.   
`subnetwork` | String | The name of the subnetwork that you are using for your HA cluster.  If you are using a shared VPC network, you must add the ID of the host project as a parent directory of the subnetwork name. For example, `host-project-id/subnetwork-name`.   
`linuxImage` | String | The name of the Linux operating- system image or image family that you are using with SAP HANA. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-8-2-sap-ha` or `family/sles-15-sp2-sap`. To specify a specific image, specify only the image name. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Cloud console.  
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project. For RHEL, specify `rhel-sap-cloud`. For SLES, specify `suse-sap-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
`sap_hana_deployment_bucket` | String | The name of the Cloud Storage bucket in your project that contains the SAP HANA installation files that you uploaded in a previous step.  
`sap_hana_sid` | String | The SAP HANA system ID. The ID must consist of three alphanumeric characters and begin with a letter. All letters must be uppercase.  
`sap_hana_instance_number` | Integer | The instance number, 0 to 99, of the SAP HANA system. The default is 0.  
`sap_hana_sidadm_password` | String | A temporary password for the operating system administrator to be used during deployment. When deployment is complete, change the password. Passwords must be at least eight characters and include at least one uppercase letter, one lowercase letter, and one number. Change the password after the deployment is complete.  
`sap_hana_system_password` | String | A temporary password for the database superuser. When deployment is complete, change the password. Passwords must be at least 8 characters and include at least one uppercase letter, one lowercase letter, and one number.Change the password after the deployment is complete.  
`sap_vip` | String | The IP address that you are going to use for your VIP. The IP address must be within the range of IP addresses that are assigned to your subnetwork. The Deployment Manager template reserves this IP address for you. In an active HA cluster, this IP address is always assigned to the active SAP HANA instance.  
`primaryInstanceGroupName` | String | Defines the name of the unmanaged instance group for the primary node. If you omit the parameter, the default name is `ig-primaryInstanceName`.  
`secondaryInstanceGroupName` | String | Defines the name of the unmanaged instance group for the secondary node. If you omit this parameter, the default name is `ig-secondaryInstanceName`.  
`loadBalancerName` | String | Defines the name of the TCP internal load balancer.  
`nic_type` | String | Optional but recommended if available for the target machine and OS version. Specifies the network interface to use with the VM instance. You can specify the value `GVNIC` or `VIRTIO_NET`. To use a [Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) (gVNIC), you need to specify an OS image that supports gVNIC as the value for the `linuxImage` property. For the OS image list, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).  If you do not specify a value for this property, then the network interface is automatically selected based on the machine type that you specify for the `instanceType` property.  This argument is available in Deployment Manager template versions `202302060649` or later.   
  
The following examples show completed configuration file template that defines a high-availability cluster for SAP HANA. The cluster uses an internal passthrough Network Load Balancer to manage the VIP.

Deployment Manager deploys the Google Cloud resources that are defined in the configuration file and then scripts take over to configure the operating system, install SAP HANA, configure replication, and configure the Linux HA cluster.

Click `RHEL` or `SLES` to see the example that is specific to your operating system.

### RHEL
         
         resources:
         - name: sap_hana_ha
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates**/sap_hana_ha_ilb** /sap_hana_ha.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/yyyymmddhhmm/dm-templates**/sap_hana_ha_ilb** /sap_hana_ha.py
           #
           properties:
             primaryInstanceName: example-ha-vm1
             secondaryInstanceName: example-ha-vm2
             **primaryZone: us-central1-a
             secondaryZone: us-central1-c
             instanceType: n2-highmem-32**
             network: example-network
             subnetwork: example-subnet-us-central1
             linuxImage: family/rhel-8-1-sap-ha
             linuxImageProject: rhel-sap-cloud
             # SAP HANA parameters
             sap_hana_deployment_bucket: my-hana-bucket
             sap_hana_sid: HA1
             sap_hana_instance_number: 00
             sap_hana_sidadm_password: TempPa55word
             sap_hana_system_password: TempPa55word
             **# VIP parameters
             sap_vip: 10.0.0.100
             primaryInstanceGroupName: ig-example-ha-vm1
             secondaryInstanceGroupName: ig-example-ha-vm2
             loadBalancerName: lb-ha1**
             # Additional optional properties
             networkTag: hana-ha-ntwk-tag
             serviceAccount: sap-deploy-example@example-project-123456.iam.gserviceaccount.com

### SLES
         
         resources:
         - name: sap_hana_ha
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana_ha_ilb/sap_hana_ha.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/yyyymmddhhmm/dm-templates/sap_hana_ha_ilb/sap_hana_ha.py
           #
           properties:
             primaryInstanceName: example-ha-vm1
             secondaryInstanceName: example-ha-vm2
             primaryZone: us-central1-a
             secondaryZone: us-central1-c
             instanceType: n2-highmem-32
             network: example-network
             subnetwork: example-subnet-us-central1
             linuxImage: family/sles-15-sp1-sap
             linuxImageProject: suse-sap-cloud
             # SAP HANA parameters
             sap_hana_deployment_bucket: my-hana-bucket
             sap_hana_sid: HA1
             sap_hana_instance_number: 00
             sap_hana_sidadm_password: TempPa55word
             sap_hana_system_password: TempPa55word
             **# VIP parameters
             sap_vip: 10.0.0.100
             primaryInstanceGroupName: ig-example-ha-vm1
             secondaryInstanceGroupName: ig-example-ha-vm2
             loadBalancerName: lb-ha1**
             # Additional optional properties
             networkTag: hana-ha-ntwk-tag
             serviceAccount: sap-deploy-example@example-project-123456.iam.gserviceaccount.com

  7. Create the instances:
         
         $ gcloud deployment-manager deployments create deployment-name --config template-name.yaml

The above command invokes the Deployment Manager, which sets up the Google Cloud infrastructure and then hands control over to a script that installs and configures SAP HANA and the HA cluster.

While Deployment Manager has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the logs.

Time to completion can vary, but the entire process usually takes less than 30 minutes.




## Verifying the deployment of your HANA HA system

Verifying an SAP HANA HA cluster involves several different procedures:

  * Checking Logging
  * Checking the configuration of the VM and the SAP HANA installation
  * Checking the cluster configuration
  * Checking the load balancer and the health of the instance groups
  * Checking the SAP HANA system using SAP HANA Studio
  * Performing a failover test



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




### Check the configuration of the VM and the SAP HANA installation

  1. After the SAP HANA system deploys without errors, connect to each VM by using SSH. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for each VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ha-ssh-button.png)

  2. Change to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output that includes the `/hana` directories, such as `/hana/data`.

### RHEL
         
         [root@example-ha-vm1 ~]# df -h
         Filesystem                        Size  Used Avail Use% Mounted on
         devtmpfs                          126G     0  126G   0% /dev
         tmpfs                             126G   54M  126G   1% /dev/shm
         tmpfs                             126G   25M  126G   1% /run
         tmpfs                             126G     0  126G   0% /sys/fs/cgroup
         /dev/sda2                          30G  5.4G   25G  18% /
         /dev/sda1                         200M  6.9M  193M   4% /boot/efi
         /dev/mapper/vg_hana-shared        251G   52G  200G  21% /hana/shared
         /dev/mapper/vg_hana-sap            32G  477M   32G   2% /usr/sap
         /dev/mapper/vg_hana-data          426G  9.8G  417G   3% /hana/data
         /dev/mapper/vg_hana-log           125G  7.0G  118G   6% /hana/log
         /dev/mapper/vg_hanabackup-backup  512G  9.3G  503G   2% /hanabackup
         tmpfs                              26G     0   26G   0% /run/user/900
         tmpfs                              26G     0   26G   0% /run/user/899
         tmpfs                              26G     0   26G   0% /run/user/1003

### SLES
         
         example-ha-vm1:~ # df -h
         Filesystem                        Size  Used Avail Use% Mounted on
         devtmpfs                          126G  8.0K  126G   1% /dev
         tmpfs                             189G   54M  189G   1% /dev/shm
         tmpfs                             126G   34M  126G   1% /run
         tmpfs                             126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                          30G  5.4G   25G  18% /
         /dev/sda2                          20M  2.9M   18M  15% /boot/efi
         /dev/mapper/vg_hana-shared        251G   50G  202G  20% /hana/shared
         /dev/mapper/vg_hana-sap            32G  281M   32G   1% /usr/sap
         /dev/mapper/vg_hana-data          426G  8.0G  418G   2% /hana/data
         /dev/mapper/vg_hana-log           125G  4.3G  121G   4% /hana/log
         /dev/mapper/vg_hanabackup-backup  512G  6.4G  506G   2% /hanabackup
         tmpfs                              26G     0   26G   0% /run/user/473
         tmpfs                              26G     0   26G   0% /run/user/900
         tmpfs                              26G     0   26G   0% /run/user/0
         tmpfs                              26G     0   26G   0% /run/user/1003

  4. Check the status of the new cluster by entering the status command that is specific to your operating system:

### RHEL

`pcs status`

### SLES

`crm status`

You should see results similar to the following the example, in which both VM instances are started and `example-ha-vm1` is the active primary instance:

### RHEL
         
         [root@example-ha-vm1 ~]# pcs status
         Cluster name: hacluster
         Cluster Summary:
           * Stack: corosync
           * Current DC: example-ha-vm1 (version 2.0.3-5.el8_2.4-4b1f869f0f) - partition with quorum
           * Last updated: Wed Jul  7 23:05:11 2021
           * Last change:  Wed Jul  7 23:04:43 2021 by root via crm_attribute on example-ha-vm2
           * 2 nodes configured
           * 8 resource instances configured
         
         Node List:
           * Online: [ example-ha-vm1 example-ha-vm2 ]
         
         Full List of Resources:
           * STONITH-example-ha-vm1      (stonith:fence_gce):    Started example-ha-vm2
           * STONITH-example-ha-vm2      (stonith:fence_gce):    Started example-ha-vm1
           * Resource Group: g-primary:
             * rsc_healthcheck_HA1       (service:haproxy):      Started example-ha-vm2
             * rsc_vip_HA1_00    (ocf::heartbeat:IPaddr2):       Started example-ha-vm2
           * Clone Set: SAPHanaTopology_HA1_00-clone [SAPHanaTopology_HA1_00]:
             * Started: [ example-ha-vm1 example-ha-vm2 ]
           * Clone Set: SAPHana_HA1_00-clone [SAPHana_HA1_00] (promotable):
             * Masters: [ example-ha-vm2 ]
             * Slaves: [ example-ha-vm1 ]
         
         Failed Resource Actions:
           * rsc_healthcheck_HA1_start_0 on example-ha-vm1 'error' (1): call=29, status='complete', exitreason='', last-rc-change='2021-07-07 21:07:35Z', queued=0ms, exec=2097ms
           * SAPHana_HA1_00_monitor_61000 on example-ha-vm1 'not running' (7): call=44, status='complete', exitreason='', last-rc-change='2021-07-07 21:09:49Z', queued=0ms, exec=0ms
         
         Daemon Status:
           corosync: active/enabled
           pacemaker: active/enabled
           pcsd: active/enabled

### SLES
         
         example-ha-vm1:~ # crm status
         Cluster Summary:
           * Stack: corosync
           * Current DC: example-ha-vm1 (version 2.0.4+20200616.2deceaa3a-3.9.1-2.0.4+20200616.2deceaa3a) - partition with quorum
           * Last updated: Wed Jul  7 22:57:59 2021
           * Last change:  Wed Jul  7 22:57:03 2021 by root via crm_attribute on example-ha-vm1
           * 2 nodes configured
           * 8 resource instances configured
         
         Node List:
           * Online: [ example-ha-vm1 example-ha-vm2 ]
         
         Full List of Resources:
           * STONITH-example-ha-vm1      (stonith:external/gcpstonith):   Started example-ha-vm2
           * STONITH-example-ha-vm2      (stonith:external/gcpstonith):   Started example-ha-vm1
           * Resource Group: g-primary:
             * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started example-ha-vm1
             * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started example-ha-vm1
           * Clone Set: cln_SAPHanaTopology_HA1_HDB00 [rsc_SAPHanaTopology_HA1_HDB00]:
             * Started: [ example-ha-vm1 example-ha-vm2 ]
           * Clone Set: msl_SAPHana_HA1_HDB00 [rsc_SAPHana_HA1_HDB00] (promotable):
             * Masters: [ example-ha-vm1 ]
             * Slaves: [ example-ha-vm2 ]

  5. Change to the SAP admin user by replacing `SID_LC` in the following command with the SID value that you specified in the configuration file template. Use lowercase for any letters.
         
         su - SID_LCadm
         

  6. Ensure that the SAP HANA services, such as `hdbnameserver`, `hdbindexserver`, and others, are running on the instance by entering the following command:
         
         HDB info
         

  7. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




### Check your cluster configuration

Check the parameter settings of your cluster. Check both the settings that are displayed by your cluster software and the parameter settings in the cluster configuration file. Compare your settings to the settings in the examples below, which were created by the automation scripts that are used in this guide.

Click on the tab for your operating system.

###  RHEL 

  1. Display your cluster resource configurations:
         
         pcs config show

The following example shows the resource configurations that are created by the automation scripts on RHEL 8.1 and later.

If you are running RHEL 7.7 or earlier, the resource definition `Clone: SAPHana_HA1_00-clone` does not include `Meta Attrs: promotable=true`.
         
         Cluster Name: hacluster
          Corosync Nodes:
           example-rha-vm1 example-rha-vm2
          Pacemaker Nodes:
           example-rha-vm1 example-rha-vm2
         
          Resources:
           Group: g-primary
            Resource: rsc_healthcheck_HA1 (class=service type=haproxy)
             Operations: monitor interval=10s timeout=20s (rsc_healthcheck_HA1-monitor-interval-10s)
                         start interval=0s timeout=100 (rsc_healthcheck_HA1-start-interval-0s)
                         stop interval=0s timeout=100 (rsc_healthcheck_HA1-stop-interval-0s)
            Resource: rsc_vip_HA1_00 (class=ocf provider=heartbeat type=IPaddr2)
             Attributes: cidr_netmask=32 ip=10.128.15.100 nic=eth0
             Operations: monitor interval=3600s timeout=60s (rsc_vip_HA1_00-monitor-interval-3600s)
                         start interval=0s timeout=20s (rsc_vip_HA1_00-start-interval-0s)
                         stop interval=0s timeout=20s (rsc_vip_HA1_00-stop-interval-0s)
           Clone: SAPHanaTopology_HA1_00-clone
            Meta Attrs: clone-max=2 clone-node-max=1 interleave=true
            Resource: SAPHanaTopology_HA1_00 (class=ocf provider=heartbeat type=SAPHanaTopology)
             Attributes: InstanceNumber=00 SID=HA1
             Operations: methods interval=0s timeout=5 (SAPHanaTopology_HA1_00-methods-interval-0s)
                         monitor interval=10 timeout=600 (SAPHanaTopology_HA1_00-monitor-interval-10)
                         reload interval=0s timeout=5 (SAPHanaTopology_HA1_00-reload-interval-0s)
                         start interval=0s timeout=600 (SAPHanaTopology_HA1_00-start-interval-0s)
                         stop interval=0s timeout=300 (SAPHanaTopology_HA1_00-stop-interval-0s)
           Clone: SAPHana_HA1_00-clone
            Meta Attrs: promotable=true
            Resource: SAPHana_HA1_00 (class=ocf provider=heartbeat type=SAPHana)
             Attributes: AUTOMATED_REGISTER=true DUPLICATE_PRIMARY_TIMEOUT=7200 InstanceNumber=00 PREFER_SITE_TAKEOVER=true SID=HA1
             Meta Attrs: clone-max=2 clone-node-max=1 interleave=true notify=true
             Operations: demote interval=0s timeout=3600 (SAPHana_HA1_00-demote-interval-0s)
                         methods interval=0s timeout=5 (SAPHana_HA1_00-methods-interval-0s)
                         monitor interval=61 role=Slave timeout=700 (SAPHana_HA1_00-monitor-interval-61)
                         monitor interval=59 role=Master timeout=700 (SAPHana_HA1_00-monitor-interval-59)
                         promote interval=0s timeout=3600 (SAPHana_HA1_00-promote-interval-0s)
                         reload interval=0s timeout=5 (SAPHana_HA1_00-reload-interval-0s)
                         start interval=0s timeout=3600 (SAPHana_HA1_00-start-interval-0s)
                         stop interval=0s timeout=3600 (SAPHana_HA1_00-stop-interval-0s)
         
          Stonith Devices:
           Resource: STONITH-example-rha-vm1 (class=stonith type=fence_gce)
            Attributes: pcmk_delay_max=30 pcmk_monitor_retries=4 pcmk_reboot_timeout=300 port=example-rha-vm1 project=sap-certification-env zone=us-central1-a
            Operations: monitor interval=300s timeout=120s (STONITH-example-rha-vm1-monitor-interval-300s)
                        start interval=0 timeout=60s (STONITH-example-rha-vm1-start-interval-0)
           Resource: STONITH-example-rha-vm2 (class=stonith type=fence_gce)
            Attributes: pcmk_monitor_retries=4 pcmk_reboot_timeout=300 port=example-rha-vm2 project=sap-certification-env zone=us-central1-c
            Operations: monitor interval=300s timeout=120s (STONITH-example-rha-vm2-monitor-interval-300s)
                        start interval=0 timeout=60s (STONITH-example-rha-vm2-start-interval-0)
          Fencing Levels:
         
          Location Constraints:
            Resource: STONITH-example-rha-vm1
              Disabled on: example-rha-vm1 (score:-INFINITY) (id:location-STONITH-example-rha-vm1-example-rha-vm1--INFINITY)
            Resource: STONITH-example-rha-vm2
              Disabled on: example-rha-vm2 (score:-INFINITY) (id:location-STONITH-example-rha-vm2-example-rha-vm2--INFINITY)
          Ordering Constraints:
            start SAPHanaTopology_HA1_00-clone then start SAPHana_HA1_00-clone (kind:Mandatory) (non-symmetrical) (id:order-SAPHanaTopology_HA1_00-clone-SAPHana_HA1_00-clone-mandatory)
          Colocation Constraints:
            g-primary with SAPHana_HA1_00-clone (score:4000) (rsc-role:Started) (with-rsc-role:Master) (id:colocation-g-primary-SAPHana_HA1_00-clone-4000)
          Ticket Constraints:
         
          Alerts:
           No alerts defined
         
          Resources Defaults:
           migration-threshold=5000
           resource-stickiness=1000
          Operations Defaults:
           timeout=600s
         
          Cluster Properties:
           cluster-infrastructure: corosync
           cluster-name: hacluster
           dc-version: 2.0.2-3.el8_1.2-744a30d655
           have-watchdog: false
           stonith-enabled: true
           stonith-timeout: 300s
         
          Quorum:
            Options:
         

  2. Display your cluster configuration file, `corosync.conf`:
         
         cat /etc/corosync/corosync.conf

The following example shows the parameters that the automation scripts set for RHEL 8.1 and later.

If you are using RHEL 7.7 or earlier, the value of `transport:` is `udpu` instead of `knet`:
         
         totem {
              version: 2
              cluster_name: hacluster
              transport: knet
              join: 60
              max_messages: 20
              token: 20000
              token_retransmits_before_loss_const: 10
              crypto_cipher: aes256
              crypto_hash: sha256
          }
         
          nodelist {
              node {
                  ring0_addr: example-rha-vm1
                  name: example-rha-vm1
                  nodeid: 1
              }
         
              node {
                  ring0_addr: example-rha-vm2
                  name: example-rha-vm2
                  nodeid: 2
              }
          }
         
          quorum {
              provider: corosync_votequorum
              two_node: 1
          }
         
          logging {
              to_logfile: yes
              logfile: /var/log/cluster/corosync.log
              to_syslog: yes
              timestamp: on
          }
         




###  SLES 

  1. Display your cluster resource configurations:
         
         crm config show

The automation scripts that are used by this guide create the resource configurations that are shown in the following example:
         
         node 1: example-ha-vm1 \
                  attributes hana_ha1_op_mode=logreplay lpa_ha1_lpt=1635380335 hana_ha1_srmode=syncmem hana_ha1_vhost=example-ha-vm1 hana_ha1_remoteHost=example-ha-vm2 hana_ha1_site=example-ha-vm1
          node 2: example-ha-vm2 \
                  attributes lpa_ha1_lpt=30 hana_ha1_op_mode=logreplay hana_ha1_vhost=example-ha-vm2 hana_ha1_site=example-ha-vm2 hana_ha1_srmode=syncmem hana_ha1_remoteHost=example-ha-vm1
          primitive STONITH-example-ha-vm1 stonith:external/gcpstonith \
                  op monitor interval=300s timeout=120s \
                  op start interval=0 timeout=60s \
                  params instance_name=example-ha-vm1 gcloud_path="/usr/bin/gcloud" logging=yes pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30
          primitive STONITH-example-ha-vm2 stonith:external/gcpstonith \
                  op monitor interval=300s timeout=120s \
                  op start interval=0 timeout=60s \
                  params instance_name=example-ha-vm2 gcloud_path="/usr/bin/gcloud" logging=yes pcmk_reboot_timeout=300 pcmk_monitor_retries=4
          primitive rsc_SAPHanaTopology_HA1_HDB00 ocf:suse:SAPHanaTopology \
                  operations $id=rsc_sap2_HA1_HDB00-operations \
                  op monitor interval=10 timeout=600 \
                  op start interval=0 timeout=600 \
                  op stop interval=0 timeout=300 \
                  params SID=HA1 InstanceNumber=00
          primitive rsc_SAPHana_HA1_HDB00 ocf:suse:SAPHana \
                  operations $id=rsc_sap_HA1_HDB00-operations \
                  op start interval=0 timeout=3600 \
                  op stop interval=0 timeout=3600 \
                  op promote interval=0 timeout=3600 \
                  op demote interval=0 timeout=3600 \
                  op monitor interval=60 role=Master timeout=700 \
                  op monitor interval=61 role=Slave timeout=700 \
                  params SID=HA1 InstanceNumber=00 PREFER_SITE_TAKEOVER=true DUPLICATE_PRIMARY_TIMEOUT=7200 AUTOMATED_REGISTER=true
          primitive rsc_vip_hc-primary anything \
                  params binfile="/usr/bin/socat" cmdline_options="-U TCP-LISTEN:60000,backlog=10,fork,reuseaddr /dev/null" \
                  op monitor timeout=20s interval=10s \
                  op_params depth=0
          primitive rsc_vip_int-primary IPaddr2 \
                  params ip=10.128.15.101 cidr_netmask=32 nic=eth0 \
                  op monitor interval=3600s timeout=60s
          group g-primary rsc_vip_int-primary rsc_vip_hc-primary
          ms msl_SAPHana_HA1_HDB00 rsc_SAPHana_HA1_HDB00 \
                  meta notify=true clone-max=2 clone-node-max=1 target-role=Started interleave=true
          clone cln_SAPHanaTopology_HA1_HDB00 rsc_SAPHanaTopology_HA1_HDB00 \
                  meta clone-node-max=1 target-role=Started interleave=true
          location LOC_STONITH_example-ha-vm1 STONITH-example-ha-vm1 -inf: example-ha-vm1
          location LOC_STONITH_example-ha-vm2 STONITH-example-ha-vm2 -inf: example-ha-vm2
          colocation col_saphana_ip_HA1_HDB00 4000: g-primary:Started msl_SAPHana_HA1_HDB00:Master
          order ord_SAPHana_HA1_HDB00 Optional: cln_SAPHanaTopology_HA1_HDB00 msl_SAPHana_HA1_HDB00
          property cib-bootstrap-options: \
                  have-watchdog=false \
                  dc-version="1.1.24+20210811.f5abda0ee-3.18.1-1.1.24+20210811.f5abda0ee" \
                  cluster-infrastructure=corosync \
                  cluster-name=hacluster \
                  maintenance-mode=false \
                  stonith-timeout=300s \
                  stonith-enabled=true
          rsc_defaults rsc-options: \
                  resource-stickiness=1000 \
                  migration-threshold=5000
          op_defaults op-options: \
                  timeout=600
         

  2. Display your cluster configuration file, `corosync.conf`:
         
         cat /etc/corosync/corosync.conf

The automation scripts that are used by this guide specify parameters settings in the `corosync.conf` file as shown in the following example:
         
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
            max_messages: 20
            transport: udpu
            interface {
              ringnumber: 0
              bindnetaddr: 10.128.1.63
              mcastport: 5405
              ttl: 1
            }
          }
          logging {
            fileline: off
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
              ring0_addr: example-ha-vm1
              nodeid: 1
            }
            node {
              ring0_addr: example-ha-vm2
              nodeid: 2
            }
          }
          quorum {
            provider: corosync_votequorum
            expected_votes: 2
            two_node: 1
          }
         




### Check the load balancer and the health of the instance groups

To confirm that the load balancer and health check were set up correctly, check the load balancer and instance groups in the Google Cloud console.

  1. Open the **Load balancing** page in the Google Cloud console:

[Go to Cloud Load Balancing](https://console.cloud.google.com/net-services/loadbalancing)

  2. In the list of load balancers, confirm that a load balancer was created for your HA cluster.

**Note:** You can disregard the warning, "1 backend service is unhealthy". In an HA cluster, the load balancer only registers the active node as healthy.
  3. On the **Load balancer details** page in the **Healthy** column under **Instance group** in the **Backend** section, confirm that one of the instance groups shows "1/1" and the other shows "0/1". After a failover, the healthy indicator, "1/1", switches to the new active instance group.

![Shows the load balancer details page with the active primary instance group
indicated by "1/1" and the inactive secondary indicated by "0/1".](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-load-balancer-details.png)




### Check the SAP HANA system using SAP HANA Studio

You can use either SAP HANA Cockpit or SAP HANA Studio to monitor and manage your SAP HANA systems in a high-availability cluster.

**Note:** If your instance of SAP HANA Cockpit or SAP HANA Studio is in a different Google Cloud region that the SAP HANA system, you need to modify the forwarding rule of the load balancer to allow access from outside of the region of the SAP HANA system. 

To enable access to the SAP HANA system from other regions, see [Enabling global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access). 

  1. Connect to the HANA system by using SAP HANA Studio. When defining the connection, specify the following values:

     * On the Specify System panel, specify the floating IP address as the Host Name.
     * On the Connection Properties panel, for database user authentication, specify the database superuser name and the password that you specified for the sap_hana_system_password property in the template.yaml file.

For information from SAP about installing SAP HANA Studio, see [SAP HANA Studio Installation and Update Guide](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/2.0.02/en-US).

  2. After SAP HANA Studio is connected to your HANA HA system, display the system overview by double-clicking the system name in the navigation pane on the left side of the window.

![Screenshot of the navigation pane in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-hdbstudio-nav.png)

  3. Under General Information on the Overview tab, confirm that:

     * The Operational Status shows "All services started".
     * The System Replication Status shows "All services are active and in sync".

![Screenshot of the Overview tab in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-hdbstudio-system-info.png)

  4. Confirm the replication mode by clicking the **System Replication Status** link under General Information. Synchronous replication is indicated by `SYNCMEM` in the REPLICATION_MODE column on the System Replication tab.

![Screenshot of the System Replication Status tab in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-hdbstudio-replication-status.png)




If any of the validation steps show that the installation failed:

  1. Resolve the errors.
  2. Delete the deployment from the [Deployments](https://console.cloud.google.com/dm/deployments) page.
  3. Recreate the instances, as described in the last step of the previous section.



### Perform a failover test

To perform a failover test:

  1. Connect to the primary VM by using SSH. You can connect from the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances) by clicking the SSH button for each VM instance, or you can use your preferred SSH method.

  2. At the command prompt, enter the following command:
         
         sudo ip link set eth0 down

The `ip link set eth0 down` command triggers a failover by severing communications with the primary host.

  3. Reconnect to either host using SSH and change to the root user.

  4. Confirm that the primary host is now active on the VM that used to contain the secondary host. Automatic restart is enabled in the cluster, so the stopped host will restart and assume the role of secondary host.

### RHEL

`pcs status`

### SLES

`crm status`

The following examples show that the roles on each host have switched.

### RHEL
         
         [root@example-ha-vm1 ~]# pcs status
         Cluster name: hacluster
         Cluster Summary:
           * Stack: corosync
           * Current DC: example-ha-vm1 (version 2.0.3-5.el8_2.3-4b1f869f0f) - partition with quorum
           * Last updated: Fri Mar 19 21:22:07 2021
           * Last change:  Fri Mar 19 21:21:28 2021 by root via crm_attribute on example-ha-vm2
           * 2 nodes configured
           * 8 resource instances configured
         
         Node List:
           * Online: [ example-ha-vm1 example-ha-vm2 ]
         
         Full List of Resources:
           * STONITH-example-ha-vm1  (stonith:fence_gce):    Started example-ha-vm2
           * STONITH-example-ha-vm2  (stonith:fence_gce):    Started example-ha-vm1
           * Resource Group: g-primary:
             * rsc_healthcheck_HA1   (service:haproxy):  Started example-ha-vm2
             * rsc_vip_HA1_00    (ocf::heartbeat:IPaddr2):   Started example-ha-vm2
           * Clone Set: SAPHanaTopology_HA1_00-clone [SAPHanaTopology_HA1_00]:
             * Started: [ example-ha-vm1 example-ha-vm2 ]
           * Clone Set: SAPHana_HA1_00-clone [SAPHana_HA1_00] (promotable):
             * Masters: [ example-ha-vm2 ]
             * Slaves: [ example-ha-vm1 ]
         

### SLES
         
         example-ha-vm2:~ #
         Cluster Summary:
           * Stack: corosync
           * Current DC: example-ha-vm2 (version 2.0.4+20200616.2deceaa3a-3.9.1-2.0.4+20200616.2deceaa3a) - partition with quorum
           * Last updated: Thu Jul  8 17:33:44 2021
           * Last change:  Thu Jul  8 17:33:07 2021 by root via crm_attribute on example-ha-vm2
           * 2 nodes configured
           * 8 resource instances configured
         
         Node List:
           * Online: [ example-ha-vm1 example-ha-vm2 ]
         
         Full List of Resources:
           * STONITH-example-ha-vm1      (stonith:external/gcpstonith):   Started example-ha-vm2
           * STONITH-example-ha-vm2      (stonith:external/gcpstonith):   Started example-ha-vm1
           * Resource Group: g-primary:
             * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started example-ha-vm2
             * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started example-ha-vm2
           * Clone Set: cln_SAPHanaTopology_HA1_HDB00 [rsc_SAPHanaTopology_HA1_HDB00]:
             * Started: [ example-ha-vm1 example-ha-vm2 ]
           * Clone Set: msl_SAPHana_HA1_HDB00 [rsc_SAPHana_HA1_HDB00] (promotable):
             * Masters: [ example-ha-vm2 ]
             * Slaves: [ example-ha-vm1 ]

  5. On the **Load balancer details** page in the console, confirm that the new active primary instance shows "1/1" in the **Healthy** column. Refresh the page, if necessary.

[Go to Cloud Load Balancing](https://console.cloud.google.com/net-services/loadbalancing)

For example:

![Shows the load balancer details page with the "ig-example-ha-vm2" instance
showing "1/1" in the Healthy column.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-ig-failover.png)

  6. In SAP HANA Studio, confirm that you are still connected to the system by double-clicking the system entry in the navigation pane to refresh the system information.

  7. Click the **System Replication Status** link to confirm that the primary and secondary hosts have switched hosts and are active.

![Screenshot of the System Replication Status tab in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-hdbstudio-replication-status-failover.png)




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

To monitor an HA cluster using Google Cloud's Agent for SAP, make sure to follow the guidance given in [High-availability configuration for the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#high-availability_configuration_for_the_agent). 

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
    

## Connect to SAP HANA

Note that because these instructions don't use an external IP address for SAP HANA, you can only connect to the SAP HANA instances through the bastion instance using SSH or through the Windows server through SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instance(s) by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server instance. After connection, manually [install SAP HANA Studio](https://help.sap.com/hana/SAP_HANA_Studio_Installation_Update_Guide_en.pdf) and access your SAP HANA database.




## Configure HANA Active/Active (Read Enabled)

Starting with SAP HANA 2.0 SPS1, you can configure [HANA Active/Active (Read Enabled)](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#sap_hana_activeactive_read_enabled) in a Pacemaker cluster. For instructions, see:

  * [Configure HANA Active/Active (Read Enabled) in a SUSE Pacemaker cluster](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#configure_hana_activeactive_read_enabled)
  * [Configure HANA Active/Active (Read Enabled) in a Red Hat Pacemaker cluster](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#configure_hana_activeactive_read_enabled)



## Performing post-deployment tasks

Before using your SAP HANA instance, we recommend that you perform the following post-deployment steps. For more information, see [SAP HANA Installation and Update Guide](http://help.sap.com/hana/SAP_HANA_Server_Installation_Guide_en.pdf).

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser.

  2. Update the SAP HANA software with the latest patches.

  3. Install any additional components such as Application Function Libraries (AFL) or Smart Data Access (SDA).

  4. Configure and backup your new SAP HANA database. For more information, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).




## What's next

  * For more information about VM administration of and monitoring, see the [SAP HANA Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
