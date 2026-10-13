---
url: https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-deployment-guide/
title: Deployment Manager: SAP HANA scale-out system with host auto-failover deployment guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:22.957878+00:00
---

# Deployment Manager: SAP HANA scale-out system with host auto-failover deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deployment Manager: SAP HANA scale-out system with host auto-failover deployment guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reaches end of support on March 31, 2026. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To automate the deployment of an SAP HANA scale-out system with host auto-failover on Google Cloud, we recommend that you use Terraform. For more information, see [Terraform: SAP HANA scale-out system with host auto-failover deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-tf-deployment-guide).

This guide shows you how to use [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs) to deploy an SAP HANA scale-out system that includes the SAP HANA host auto-failover fault-recovery solution. By using Deployment Manager, you can deploy a system that meets SAP support requirements and adheres to both SAP and Compute Engine best practices.

The resulting SAP HANA system includes a master host, up to 15 worker hosts, and up to 3 standby hosts all within a single Compute Engine zone.

The system also includes the Google Cloud storage manager for SAP HANA standby nodes (storage manager for SAP HANA), which manages the transfer of storage devices to the standby node during a failover. The storage manager for SAP HANA is installed in the SAP HANA `/shared` volume. For information about the storage manager for SAP HANA and required IAM permissions, see [The storage manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).

If you need to deploy SAP HANA in a Linux high-availability cluster, use one of the following guides:

  * The [Deployment Manager: SAP HANA HA cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment)
  * The [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * The [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)



This guide is intended for advanced SAP HANA users who are familiar with SAP scale-out configurations that include standby hosts for high-availability, as well as network file systems.

## Prerequisites

Before you create the SAP HANA high availability scale-out system, make sure that the following prerequisites are met:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide) and the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide). 
  * You or your organization has a Google Cloud account and you have created a project for the SAP HANA deployment. For information about creating Google Cloud accounts and projects, see [Setting up your Google account](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#setting-up-your-google-account) in the SAP HANA Deployment Guide.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * The SAP HANA installation media is stored in a Cloud Storage bucket that is available in your deployment project and region. For information about how to upload SAP HANA installation media to a Cloud Storage bucket, see [Creating a Cloud Storage bucket](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#creating_a_cloud_storage_bucket_for_the_sap_hana_installation_files). in the SAP HANA Deployment Guide.
  * You have an NFS solution, such as the managed [Filestore](https://docs.cloud.google.com/filestore) solution, for sharing the SAP HANA `/hana/shared` and `/hanabackup` volumes among the hosts in the scale-out SAP HANA system. You specify the mount points for the NFS servers in the Deployment Manager configuration file before you can deploy the system. To deploy Filestore NFS servers, see [Creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * Communication must be allowed between all VMs in the SAP HANA subnetwork that host an SAP HANA scale-out node.

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)

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

## Creating an SAP HANA scale-out system with standby hosts

In the following instructions, you complete the following actions:

  * Create the SAP HANA system by invoking Deployment Manager with a configuration file template that you complete.
  * Verify deployment.
  * Test the standby host(s) by simulating a host failure.



Some of the steps in the following instructions use Cloud Shell to enter the `gcloud` commands. If you have the latest version of Google Cloud CLI installed, you can enter the `gcloud` commands from a local terminal instead.

### Define and create the SAP HANA system

In the following steps, you download and complete a Deployment Manager configuration file template and invoke Deployment Manager, which deploys the VMs, persistent disks, and SAP HANA instances.

  1. Confirm that your current quotas for project resources, such as persistent disks and CPUs, are sufficient for the SAP HANA system you are about to install. If your quotas are insufficient, deployment fails. For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to the quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `template.yaml` configuration file template for the SAP HANA high-availability scale-out system to your working directory:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana_scaleout/template.yaml

  4. Optionally, rename the `template.yaml` file to identify the configuration it defines. For example, you could use a file name like `hana2sp3rev30-scaleout.yaml`.

  5. Open the `template.yaml` file in the Cloud Shell code editor.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  6. In the `template.yaml` file, update the following property values by replacing the brackets and their contents with the values for your installation. For example, you might replace "[ZONE]" with "us-central1-f".

Property | Data type | Description  
---|---|---  
type | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
`instanceName` | String | The name of the VM instance for the SAP HANA master host. The name must be specified in lowercase letters, numbers, or hyphens. The VM instances for the worker and standby hosts use the same name with a "w" and the host number appended to the name.  
`instanceType` | String | The type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#vm_types) that you need to run SAP HANA on. If you need a custom VM type, specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#vm_types) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations).  
`zone` | String | The zone in which you are deploying your SAP HANA systems to run. It must be in the region that you selected for your subnet.   
`subnetwork` | String | The name of the subnetwork you created in a previous step. If you are deploying to a shared VPC, specify this value as `[SHAREDVPC_PROJECT]/[SUBNETWORK]`. For example, `myproject/network1`.  
`linuxImage` | String | The name of the Linux operating-system image or image family that you are using with SAP HANA. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-8-1-sap-ha` or `family/sles-15-sp2-sap`. To specify a specific image, specify only the image name. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify either `rhel-sap-cloud` or `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).  
`sap_hana_deployment_bucket` | String | The name of the Cloud Storage bucket in your project that contains the SAP HANA installation files that you uploaded in a previous step.  
`sap_hana_sid` | String | The SAP HANA system ID. The ID must consist of 3 alphanumeric characters and begin with a letter. All letters must be uppercase.  
`sap_hana_instance_number` | Integer | The instance number, 0 to 99, of the SAP HANA system. The default is 0.  
`sap_hana_sidadm_password` | String | A temporary password for the operating system administrator to be used during deployment. Passwords must be at least 8 characters and include at least 1 uppercase letter, 1 lowercase letter, and 1 number. **Caution** : Change the password after the installation is complete.   
`sap_hana_system_password` | String | A temporary password for the database superuser to be used during deployment. Passwords must be at least 8 characters and include at least 1 uppercase letter, 1 lowercase letter, and 1 number. **Caution** : Change the password after the installation is complete.   
`sap_hana_worker_nodes` | Integer | The number of additional SAP HANA worker hosts that you need. You can specify 1 to 15 worker hosts. The default is value is 1.  
`sap_hana_standby_nodes` | Integer | The number of additional SAP HANA standby hosts that you need. You can specify 1 to 3 standby hosts. The default value is 1.  
`sap_hana_shared_nfs` | String | The NFS mount point for the `/hana/shared` volume. For example, `10.151.91.122:/hana_shared_nfs`. **Note** : The NFS mount point for the `/hana/shared` volume must be empty before you run Deployment Manager.  
`sap_hana_backup_nfs` | String | The NFS mount point for the `/hanabackup` volume. For example, `10.216.41.122:/hana_backup_nfs`.  
`networkTag` | String | Optional. One or more comma-separated network tags that represents your VM instance for firewall or routing purposes. If you specify `publicIP: No` and do not specify a network tag, be sure to provide another means of access to the internet.   
`nic_type` | String | Optional but recommended if available for the target machine and OS version. Specifies the network interface to use with the VM instance. You can specify the value `GVNIC` or `VIRTIO_NET`. To use a [Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) (gVNIC), you need to specify an OS image that supports gVNIC as the value for the `linuxImage` property. For the OS image list, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).  If you do not specify a value for this property, then the network interface is automatically selected based on the machine type that you specify for the `instanceType` property.  This argument is available in Deployment Manager template versions `202302060649` or later.   
`publicIP` | Boolean | Optional. Determines whether a public IP address is added to your VM instance. The default is `Yes`. **Note** : Do not specify `No` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`sap_hana_double_volume_size` | Integer | Optional. Doubles the HANA volume size. Useful if you wish to deploy multiple SAP HANA instances or a disaster recovery SAP HANA instance on the same VM. By default, the volume size is automatically calculated to be the minimum size required for your memory footprint, while still meeting the SAP certification and support requirements.   
`sap_hana_sidadm_uid` | Integer | Optional. Overrides the default value of the `SID_LCadm` user ID. The default value is 900\. You can change this to a different value for consistency within your SAP landscape.   
`sap_hana_sapsys_gid` | Integer | Optional. Overrides the default group ID for sapsys. The default is 79.  
`sap_deployment_debug` | Boolean | Optional. If this value is set to `Yes`, the deployment generates verbose deployment logs. Do not turn this setting on unless a Google support engineer asks you to enable debugging.   
`post_deployment_script` | Boolean | Optional. The URL or storage location of a script to run after the deployment is complete. The script should be hosted on a web server or in a Cloud Storage bucket. Begin the value with http:// https:// or gs://. Note that this script will be executed on all VMs that the template creates. If you only want to run it on the master instance, you will need to add a check at the top of your script.   
  
The following example shows a completed configuration file that deploys an SAP HANA scale-out system with three worker hosts and one standby host in the us-central1-f zone. Each host is installed on an n2-highmem-32 VM that is running a Linux operating system provided by a Compute Engine public image. The NFS volumes are provided by Filestore. Temporary passwords are used during deployment and configuration processing only. The custom service account that is specified will become the service account of the deployed VMs.
         
         resources:
         - name: sap_hana_ha_scaleout
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_hana_scaleout/sap_hana_scaleout.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/YYYYMMDDHHMM/dm-templates/sap_hana_scaleout/sap_hana_scaleout.py
           #
           properties:
             instanceName: hana-scaleout-w-failover
             instanceType: n2-highmem-32
             zone: us-central1-f
             subnetwork: example-sub-network-sap
             linuxImage: family/sles-15-sp2-sap
             linuxImageProject: suse-sap-cloud
             sap_hana_deployment_bucket: hana2-sp5-rev53
             sap_hana_sid: HF0
             sap_hana_instance_number: 00
             sap_hana_sidadm_password: TempPa55word
             sap_hana_system_password: TempPa55word
             sap_hana_worker_nodes: 3
             sap_hana_standby_nodes: 1
             sap_hana_shared_nfs: 10.74.146.58:/hana_shr
             sap_hana_backup_nfs: 10.188.249.170:/hana_bup
             serviceAccount: sap-deploy-example@example-project-123456.iam.gserviceaccount.com
         

  7. Create the instances:
         
         gcloud deployment-manager deployments create [DEPLOYMENT_NAME] --config [TEMPLATE_NAME].yaml
         

The above command invokes the Deployment Manager, which sets up the Google Cloud infrastructure and then invokes another script that configures the operating system and installs SAP HANA.

While Deployment Manager has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Checking the Logging logs.

Time to completion can vary, but the entire process usually takes less than 30 minutes.




### Verifying deployment

To verify deployment, you check the deployment logs in Cloud Logging, check the disks and services on the VMs of the primary and worker hosts, display the system in SAP HANA Studio, and test the takeover by a standby host.

#### Check the logs

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




#### Connect to the VMs to check the disks and SAP HANA services

After deployment is complete, confirm that the disks and SAP HANA services have deployed properly by checking the disks and services of the master host and one worker host.

  1. On the Compute Engine **VM instances** page, connect to the VM of the master host and the VM of one worker host by clicking the SSH button on the row of each of the two VM instances.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

When connecting to the worker host, make sure that you aren't connecting to a standby host. The standby hosts use the same naming convention as the worker hosts, but have the highest numbered worker-host suffix before the first takeover. For example, if you have three worker hosts and one standby host, before the first takeover the standby host has a suffix of "w4".

  2. In each terminal window, switch to the root user.
         
         sudo su -

  3. In each terminal window, display the disk file system.
         
         df -h

On the master host, you should see output similar to the following.
         
         hana-scaleout-w-failover:~ # df -h
         Filesystem                Size  Used Avail Use% Mounted on
         devtmpfs                  126G  8.0K  126G   1% /dev
         tmpfs                     189G     0  189G   0% /dev/shm
         tmpfs                     126G   18M  126G   1% /run
         tmpfs                     126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                  45G  5.6G   40G  13% /
         /dev/sda2                  20M  2.9M   18M  15% /boot/efi
         10.135.35.138:/hana_shr  1007G   50G  906G   6% /hana/shared
         tmpfs                      26G     0   26G   0% /run/user/473
         10.197.239.138:/hana_bup 1007G     0  956G   0% /hanabackup
         tmpfs                      26G     0   26G   0% /run/user/900
         /dev/mapper/vg_hana-data  709G  7.7G  702G   2% /hana/data/HF0/mnt00001
         /dev/mapper/vg_hana-log   125G  5.3G  120G   5% /hana/log/HF0/mnt00001
         tmpfs                      26G     0   26G   0% /run/user/1003

On a worker host, notice that the `/hana/data` and `/hana/log` directories have different mounts.
         
         hana-scaleout-w-failoverw2:~ # df -h
         Filesystem                Size  Used Avail Use% Mounted on
         devtmpfs                  126G  8.0K  126G   1% /dev
         tmpfs                     189G     0  189G   0% /dev/shm
         tmpfs                     126G  9.2M  126G   1% /run
         tmpfs                     126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                  45G  5.6G   40G  13% /
         /dev/sda2                  20M  2.9M   18M  15% /boot/efi
         tmpfs                      26G     0   26G   0% /run/user/0
         10.135.35.138:/hana_shr  1007G   50G  906G   6% /hana/shared
         10.197.239.138:/hana_bup 1007G     0  956G   0% /hanabackup
         /dev/mapper/vg_hana-data  709G  821M  708G   1% /hana/data/HF0/mnt00003
         /dev/mapper/vg_hana-log   125G  2.2G  123G   2% /hana/log/HF0/mnt00003
         tmpfs                      26G     0   26G   0% /run/user/1003

On a standby host, the data and log directories are not mounted until the standby host takes over for a failed host.
         
         hana-scaleout-w-failoverw4:~ # df -h
         Filesystem                Size  Used Avail Use% Mounted on
         devtmpfs                  126G  8.0K  126G   1% /dev
         tmpfs                     189G     0  189G   0% /dev/shm
         tmpfs                     126G   18M  126G   1% /run
         tmpfs                     126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                  45G  5.6G   40G  13% /
         /dev/sda2                  20M  2.9M   18M  15% /boot/efi
         tmpfs                      26G     0   26G   0% /run/user/0
         10.135.35.138:/hana_shr  1007G   50G  906G   6% /hana/shared
         10.197.239.138:/hana_bup 1007G     0  956G   0% /hanabackup
         tmpfs                      26G     0   26G   0% /run/user/1003

  4. In each terminal window, change to the SAP HANA operating system user.
         
         su - SID_LCadm

Replace `SID_LC` with the SID value that you specified in the configuration file template. Use lowercase for any letters.

  5. In each terminal window, ensure that SAP HANA services, such as `hdbnameserver`, `hdbindexserver`, and others, are running on the instance.
         
         HDB info

On the master host, you should see output similar to the output in the following truncated example:
         
         hf0adm@hana-scaleout-w-failover:/usr/sap/HF0/HDB00> HDB info
         USER          PID     PPID  %CPU        VSZ        RSS COMMAND
         hf0adm       5936     5935   0.7      18540       6776 -sh
         hf0adm       6011     5936   0.0      14128       3856  \_ /bin/sh /usr/sap/HF0/HDB00/HDB info
         hf0adm       6043     6011   0.0      34956       3568      \_ ps fx -U hf0adm -o user:8,pid:8,ppid:8,pcpu:5,vsz:10
         hf0adm      17950        1   0.0      23052       3168 sapstart pf=/hana/shared/HF0/profile/HF0_HDB00_hana-scaleout
         hf0adm      17957    17950   0.0     457332      70956  \_ /usr/sap/HF0/HDB00/hana-scaleout-w-failover/trace/hdb.sa
         hf0adm      17975    17957   1.8    9176656    3432456      \_ hdbnameserver
         hf0adm      18334    17957   0.4    4672036     229204      \_ hdbcompileserver
         hf0adm      18337    17957   0.4    4941180     257348      \_ hdbpreprocessor
         hf0adm      18385    17957   4.5    9854464    4955636      \_ hdbindexserver -port 30003
         hf0adm      18388    17957   1.2    7658520    1424708      \_ hdbxsengine -port 30007
         hf0adm      18865    17957   0.4    6640732     526104      \_ hdbwebdispatcher
         hf0adm      14230        1   0.0     568176      32100 /usr/sap/HF0/HDB00/exe/sapstartsrv pf=/hana/shared/HF0/profi
         hf0adm      10920        1   0.0     710684      51560 hdbrsutil  --start --port 30003 --volume 3 --volumesuffix mn
         hf0adm      10575        1   0.0     710680      51104 hdbrsutil  --start --port 30001 --volume 1 --volumesuffix mn
         hf0adm      10217        1   0.0      72140       7752 /usr/lib/systemd/systemd --user
         hf0adm      10218    10217   0.0     117084       2624  \_ (sd-pam)

On a worker host, you should see output similar to the output in the following truncated example:
         
         hf0adm@hana-scaleout-w-failoverw2:/usr/sap/HF0/HDB00> HDB info
         USER          PID     PPID  %CPU        VSZ        RSS COMMAND
         hf0adm      22136    22135   0.3      18540       6804 -sh
         hf0adm      22197    22136   0.0      14128       3892  \_ /bin/sh /usr/sap/HF0/HDB00/HDB info
         hf0adm      22228    22197   100      34956       3528      \_ ps fx -U hf0adm -o user:8,pid:8,ppid:8,pcpu:5,vsz:10
         hf0adm       9138        1   0.0      23052       3064 sapstart pf=/hana/shared/HF0/profile/HF0_HDB00_hana-scaleout
         hf0adm       9145     9138   0.0     457360      70900  \_ /usr/sap/HF0/HDB00/hana-scaleout-w-failoverw2/trace/hdb.
         hf0adm       9163     9145   0.7    7326228     755772      \_ hdbnameserver
         hf0adm       9336     9145   0.5    4670756     226972      \_ hdbcompileserver
         hf0adm       9339     9145   0.6    4942460     259724      \_ hdbpreprocessor
         hf0adm       9385     9145   2.0    7977460    1666792      \_ hdbindexserver -port 30003
         hf0adm       9584     9145   0.5    6642012     528840      \_ hdbwebdispatcher
         hf0adm       8226        1   0.0     516532      52676 hdbrsutil  --start --port 30003 --volume 5 --volumesuffix mn
         hf0adm       7756        1   0.0     567520      31316 /hana/shared/HF0/HDB00/exe/sapstartsrv pf=/hana/shared/HF0/p

On a standby host, you should see output similar to the output in the following truncated example:
         
         hana-scaleout-w-failoverw4:~ # su - hf0adm
         hf0adm@hana-scaleout-w-failoverw4:/usr/sap/HF0/HDB00> HDB info
         USER          PID     PPID  %CPU        VSZ        RSS COMMAND
         hf0adm      19926    19925   0.2      18540       6748 -sh
         hf0adm      19987    19926   0.0      14128       3864  \_ /bin/sh /usr/sap/HF0/HDB00/HDB info
         hf0adm      20019    19987   0.0      34956       3640      \_ ps fx -U hf0adm -o user:8,pid:8,ppid:8,pcpu:5,vsz:10
         hf0adm       8120        1   0.0      23052       3232 sapstart pf=/hana/shared/HF0/profile/HF0_HDB00_hana-scaleout
         hf0adm       8127     8120   0.0     457348      71348  \_ /usr/sap/HF0/HDB00/hana-scaleout-w-failoverw4/trace/hdb.
         hf0adm       8145     8127   0.6    7328784     708284      \_ hdbnameserver
         hf0adm       8280     8127   0.4    4666916     223892      \_ hdbcompileserver
         hf0adm       8283     8127   0.4    4939904     256740      \_ hdbpreprocessor
         hf0adm       8328     8127   0.4    6644572     534044      \_ hdbwebdispatcher
         hf0adm       7374        1   0.0     633568      31520 /hana/shared/HF0/HDB00/exe/sapstartsrv pf=/hana/shared/HF0/p

  6. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




#### Connect SAP HANA Studio

  1. Connect to the master SAP HANA host from SAP HANA Studio.

You can connect from an instance of SAP HANA Studio that is outside of Google Cloud or from an instance on Google Cloud. You might need to enable network access between the target VMs and SAP HANA Studio.

To use SAP HANA Studio on Google Cloud and enable access to the SAP HANA system, see [Installing SAP HANA Studio on a Compute Engine Windows VM](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#install_hana_studio).

  2. In SAP HANA Studio, click the **Landscape** tab on the default system administration panel. You should see a display similar to the following example.

![Screenshot of the Landscape view in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/hana-studio-scaleout-landscape.png)




If any of the validation steps show that the installation failed:

  1. Correct the error.
  2. On the [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment.
  3. Rerun your deployment.



### Performing a failover test

After you have confirmed that the SAP HANA system deployed successfully, test the failover function.

The following instructions trigger a failover by switching to the SAP HANA operating system user and entering the `HDB stop` command. The `HDB stop` command initiates a graceful shutdown of SAP HANA and detaches the disks from the host, which enables a relatively quick failover.

**Note:** To simulate a failure of the entire VM, you can enter `sudo ip link set eth0 down` command. The `ip link set eth0 down` command shuts down the network interface to the VM. Failover in this case takes longer, because the system performs additional processing to confirm that the host is down and to move the disks.

To perform a failover test:

  1. Connect to the VM of a worker host by using SSH. You can connect from the Compute Engine VM instances page by clicking the SSH button for each VM instance, or you can use your preferred SSH method.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Change to the SAP HANA operating system user. In the following example, replace `SID_LC` with the SID that you defined for your system.
         
         su - SID_LCadm

  3. Simulate a failure by stopping SAP HANA:
         
         HDB stop

The `HDB stop` command initiates a shutdown of SAP HANA, which triggers a failover. During the failover, the disks are detached from the failed host and reattached to the standby host. The failed host is restarted and becomes a standby host.

  4. After allowing time for the takeover to complete, reconnect to the host that took over for the failed host by using SSH.

  5. Change to the root user.
         
         sudo su -

  6. Display the disk file system of the VMs for the master and worker hosts.
         
         df -h

You should see output similar to the following. The `/hana/data` and `/hana/log` directories from the failed host are now mounted to the host that took over.
         
         hana-scaleout-w-failoverw4:~ # df -h
         Filesystem                Size  Used Avail Use% Mounted on
         devtmpfs                  126G  8.0K  126G   1% /dev
         tmpfs                     189G     0  189G   0% /dev/shm
         tmpfs                     126G  9.2M  126G   1% /run
         tmpfs                     126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                  45G  5.6G   40G  13% /
         /dev/sda2                  20M  2.9M   18M  15% /boot/efi
         tmpfs                      26G     0   26G   0% /run/user/0
         10.74.146.58:/hana_shr   1007G   50G  906G   6% /hana/shared
         10.188.249.170:/hana_bup 1007G     0  956G   0% /hanabackup
         /dev/mapper/vg_hana-data  709G  821M  708G   1% /hana/data/HF0/mnt00003
         /dev/mapper/vg_hana-log   125G  2.2G  123G   2% /hana/log/HF0/mnt00003
         tmpfs                      26G     0   26G   0% /run/user/1003

  7. In SAP HANA Studio, open the **Landscape** view of the SAP HANA system to confirm that the failover over was successful:

     * The status of the hosts involved in the failover should be `INFO`.
     * The **Index Server Role (Actual)** column should show the failed host as the new standby host.

![Screenshot of the Landscape view in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/hana-studio-scaleout-landscape-failover.png)




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
    

## Connecting to SAP HANA

Note that because these instructions don't use an external IP for SAP HANA, you can only connect to the SAP HANA instances through the bastion instance using SSH or through the Windows server using SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instance(s) by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server instance. After connection, manually [install SAP HANA Studio](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/LATEST/en-US/c13cec2b7c2c46bdb0762ce5f1410260.html) and access your SAP HANA database.




## Performing post-deployment tasks

Before using your SAP HANA instance, we recommend that you perform the following post-deployment steps. For more information, see [SAP HANA Installation and Update Guide](https://help.sap.com/viewer/2c1988d620e04368aa4103bf26f17727/LATEST/en-US/7eb0167eb35e4e2885415205b8383584.html).

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser.

  2. Update the SAP HANA software with the latest patches.

  3. Install any additional components such as Application Function Libraries (AFL) or Smart Data Access (SDA).

  4. If you are upgrading an existing SAP HANA system, load the data from the existing system either by using standard backup and restore procedures or by using SAP HANA system replication.

  5. Configure and backup your new SAP HANA database. For more information, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).




## What's next

  * For more information about VM administration of and monitoring, see the [SAP HANA Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
