---
url: https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-with-standby-nodes-manual-config-sles/
title: Manual deployment: SAP HANA scale-out with host auto-failover on SLES \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:40.697060+00:00
---

# Manual deployment: SAP HANA scale-out with host auto-failover on SLES  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-with-standby-nodes-manual-config-sles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manual deployment: SAP HANA scale-out with host auto-failover on SLES Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to manually deploy an SAP HANA scale-out system on SUSE Linux Enterprise Server (SLES) on Google Cloud, with the host auto-failover fault-recovery solution. If you want to deploy an SAP HANA scale-out system without the host auto-failover solution, then see [Terraform: SAP HANA multi-host scale-out deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-deployment-tf). 

The instructions in this guide use a Terraform configuration provided by Google Cloud to automate the deployment of the resources required for this system. This Terraform configuration lets you deploy resources in a way that helps you meet SAP support requirements and adhere to SAP and Google Cloud best practices.

This guide is intended for advanced SAP HANA users who are familiar with SAP scale-out configurations that include standby hosts for high availability, as well as network file systems.

## System that this guide deploys

The resulting SAP HANA system includes the following components:

  * A master host, up to 15 worker hosts, and up to 3 standby hosts, all within a single Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones).
  * The storage manager for SAP HANA (`gceStorageClient`), which manages the transfer of storage devices from the faulty node to the standby node during failover events. This tool is installed in the `/hana/shared` directory. For more information about storage manager for SAP HANA, see [The storage manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).



## Before you begin

Before you deploy your SAP HANA scale-out system, make sure that the following prerequisites are met:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide) and the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide). 
  * You or your organization has a Google Cloud account and you have created a project for the SAP HANA deployment. For more information, see [Setting up your Google account](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf#setting-up-your-google-account).
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * You've set up an NFS solution, such as the managed [Filestore](https://docs.cloud.google.com/filestore) solution, for sharing the SAP HANA `/hana/shared` and `/hanabackup` directories among the hosts in your scale-out system. You specify the mount points for the NFS servers in the Terraform configuration that you use for this deployment.

For information about the file sharing solutions that you can use with SAP on Google Cloud, see [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap). For information about how to deploy Filestore instances to run your NFS servers, see [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

  * You've set up a new VPC subnetwork for this deployment and have set up firewall rules that allow communication between the compute instances that serve as nodes in your SAP HANA scale-out system. For more information, see the following:

    * Create a VPC network
    * Set up a Cloud NAT gateway
    * Add firewall rules
  * You've verified that the terminal you're using has the Google Cloud CLI and Terraform CLI installed. For information about how to install the Terraform CLI, see [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules. If you use the Terraform configuration file that Google Cloud provides, specify a tag with `network_tags = "TAG"`.
    * Create the VMs without an external IP. If you use the Terraform configuration file that Google Cloud provides, specify `public_ip = false`.



### Create a VPC network

For security purposes, create a new network. You can control who has access by adding firewall rules or by using another access control method.

If your project has a default VPC network, then don't use it. Instead, create your own VPC network so that the only firewall rules in effect are those that you create explicitly.

During deployment, Compute Engine instances typically require access to the internet to download Google Cloud's Agent for SAP. If you are using one of the SAP-certified Linux images that are available from Google Cloud, then the compute instance also requires access to the internet in order to register the license and to access OS vendor repositories. A configuration with a NAT gateway and with VM network tags supports this access, even if the target compute instances don't have external IPs. 

To create a VPC network for your project, complete the following steps:

  1. Create a custom mode network. For more information, see [Creating a custom mode network](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_1).

  2. Create a subnetwork, and specify the region and IP range. For more information, see [Adding subnets](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_2).




### Set up a Cloud NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#terraform).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

### Add firewall rules

By default, an _implied firewall rule_ blocks incoming connections from outside your Virtual Private Cloud (VPC) network. To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

## Deploy the SAP HANA scale-out system with the host auto-failover solution

In the following instructions, you complete the following actions:

  * Deploy resources for SAP HANA by using a Terraform configuration file that you complete.
  * Install SAP HANA by using `gceStorageClient` as the storage provider.
  * Test the standby host by simulating a host failure.



Some of the steps in the following instructions use Cloud Shell to run the `gcloud` commands. If you have installed the latest version of gcloud CLI, then you can run the `gcloud` commands from a local terminal instead.

### Set up a service account for the storage manager for SAP HANA

To enable host auto-failover for your SAP HANA scale-out system on Google Cloud, the storage manager for SAP HANA requires a service account. It is through this service account that the storage manager for SAP HANA performs actions such as detaching and attaching disks during a failover.

  1. Create a service account. For information about how to do this, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  2. Grant the following IAM permissions to the service account:

     * `compute.instances.reset permission`: to reset a compute instance by running the `gcloud compute instances reset` command.
     * `compute.disks.get permission`: to get information about the Hyperdisk or Persistent Disk volumes by running the `gcloud compute disks describe` command.
     * `compute.disks.list`: to list the Hyperdisk and Persistent Disk volumes by using the `gcloud compute disks list` command.
     * `compute.instances.attachDisk permission` and `iam.serviceAccounts.actAs`: to attach a disk to a compute instance by running the `gcloud compute instances attach-disk` command.
     * `compute.instances.detachDisk permission`: to detach a disk from a compute instance by using the `gcloud compute instances detach-disk` command.
     * `compute.instances.list`: to list the compute instances by using the `gcloud compute instances list` command.

You can grant these permissions by using either predefined or custom IAM roles. To view information about predefined roles and the permissions that they provide, see [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions). For information about how to create custom IAM roles, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  3. Make note of the email address of the service account you created. You need this in a later part of this guide.




### Deploy resources for SAP HANA

To deploy the Google Cloud resources for running SAP HANA, such as compute instances, you use the Terraform configuration provided by Google Cloud.

The following instructions use the Cloud Shell, but are generally applicable to the gcloud CLI.

To deploy the resources needed to run the SAP HANA scale-out system, complete the following steps:

  1. Verify that your current quotas for resources such as Compute Engine instances, Hyperdisk volumes, Persistent Disk volumes, and CPUs are sufficient for the SAP HANA systems that you are about to deploy. If your quotas are insufficient, then your deployment fails.

For information about quota requirements to run SAP HANA, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to Quotas & system limits](https://console.cloud.google.com/iam-admin/quotas)

  2. Open Cloud Shell, or the local terminal where you've installed the gcloud CLI and the Terraform CLI.

  3. Go to your working directory.

  4. Verify that your working directory doesn't contain any other Terraform configuration file. If it does, then create a new working directory.

  5. Download the `sap_hana_scaleout.tf` configuration file to your working directory:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_scaleout/terraform/sap_hana_scaleout.tf
         

  6. Open the `sap_hana_scaleout.tf` file in an editor.

If you're using Cloud Shell, then you can use its code editor. To launch the editor, click ![Code Editor Button](https://docs.cloud.google.com/static/shell/docs/images/open-editor.png)**Open Editor** on the toolbar of the Cloud Shell window.

  7. In the `sap_hana_scaleout.tf` file, update values for the following arguments. For example, you might update the value `**ZONE**` with `us-central1-f`.

To view an example of a completed configuration file, see Example configuration.

**Important:** Make sure to specify `deploy_infra_only = true` in your Terraform configuration file. This argument specification ensures that the Terraform configuration only deploys the Google Cloud resources and skips the installation of SAP HANA.Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `sap_hana_scaleout.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`zone` | String | Specify the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which you are deploying your SAP system. The zone must be in the same region that you selected for your subnet. For example, if your subnet is deployed in the `us-central1` region, then you can specify a zone such as `us-central1-a`.  
`machine_type` | String |  Specify the type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms) (VM) on which you need to run your SAP system. If you need a custom VM type, then specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations). For example, `n1-highmem-32`.  
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `sles-15-sp6-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`instance_name` | String | Specify a name for the compute instance that Terraform deploys to run your SAP HANA workload. The name can contain lowercase letters, numbers, and hyphens.  
`sap_hana_shared_nfs` | String |  Specify the NFS mount point for the `/hana/shared` volume. For example, `10.151.91.122:/hana_shared_nfs`. **Note** : The NFS mount point for the `/hana/shared` volume must be empty before you apply the Terraform configuration.  
`sap_hana_backup_nfs` | String |  Specify the NFS mount point for the `/hanabackup` volume. For example, `10.216.41.122:/hana_backup_nfs`.   
`sap_hana_sid` | String | To automatically install SAP HANA on the deployed VMs, specify the SAP HANA system ID. The ID must consist of three alpha-numeric characters and begin with a letter. All letters must be in uppercase. For example, `HS4`.   
`sap_hana_instance_number` | Integer | Optional. Specify the instance number, 0 to 99, of the SAP HANA system. The default is `0`.  
`sap_hana_sidadm_uid` | Integer | Optional. Specify a value to override the default value of the SID_LCadm user ID. The default value is `900`. You can change this to a different value for consistency within your SAP landscape.   
`sap_hana_sapsys_gid` | Integer | Optional. Overrides the default group ID for `sapsys`. The default value is `79`.   
`sap_hana_worker_nodes` | Integer | Specify the number of additional SAP HANA worker hosts that you need. You can specify 1 to 15 worker hosts. The default value is 1.  
`sap_hana_standby_nodes` | Integer | Specify the number of additional SAP HANA standby hosts that you need. You can specify 1 to 3 standby hosts. The default value is 1.   
`deploy_infra_only` | Boolean | Set the value `true` to deploy the Google Cloud resources and skip installation of SAP HANA on the deployed compute instances. The default value of this argument is `false`. When you're using the `sap_hana_scaleout.tf` configuration provided by Google Cloud, the deployed resources include the following:
     * Compute Engine instances to host the SAP HANA master, worker, and standby nodes.
     * Hyperdisk or Persistent Disk volumes to host the SAP HANA directories, such as `/hana/data` and `/hana/log`.
This argument is available in `sap_hana_scaleout` module version `1.9.947102001` or later.  
`disk_type` | String | Optional. Specify the default type of Persistent Disk or Hyperdisk volume that you want to deploy for the `/hana/data`, `/hana/log`, and `/usr/sap` directories in your deployment. For information about the default disk deployment performed by the Terraform configurations provided by Google Cloud, see [ Disk deployment by Terraform](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#disk-deployment-by-terraform). The following are valid values for this argument: `hyperdisk-extreme`, `hyperdisk-balanced`, `pd-ssd`, `pd-balanced`, and `pd-extreme`.  You can override this default disk type and the associated default disk size and default IOPS using some advanced arguments. For more information, navigate to your working directory, then run the `terraform init` command, and then see the `/.terraform/modules/sap_hana_scaleout/variables.tf` file. Before you use these arguments in production, make sure to test them in a non-production environment.  If you want to use [SAP HANA Native Storage Extension](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/4efaa94f8057425c8c7021da6fc2ddf5.html) (NSE), then you need to provision larger disks by using the advanced arguments.  
`use_single_shared_data_log_disk` | Boolean | Optional. The default value is `false`, which directs Terraform to deploy a separate persistent disk or Hyperdisk for each of the following SAP volumes: `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap`. To mount these SAP volumes on the same persistent disk or Hyperdisk, specify `true`.   
`sap_hana_double_volume_size` | Boolean | Optional. To double the HANA volume size, specify `true`. This argument is useful when you want to deploy multiple SAP HANA instances or a disaster-recovery SAP HANA instance on the same VM. By default, the volume size is automatically calculated to be the minimum size required for the size of your VM, while still meeting the SAP certification and support requirements. The default value is `false`.   
`network_tags` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for firewall or routing purposes.  If you specify `public_ip = false` and don't specify a network tag, then make sure to provide another means of access to the internet.   
`service_account` | String | Optional. Specify the email address of a user-managed service account to be used by the host VMs and by the programs that run on the host VMs. For example, `svc-acct-name@project-id.iam.gserviceaccount.com`.  If you specify this argument without a value, or omit it, then the installation script uses the Compute Engine default service account. For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).   
`public_ip` | Boolean |  Optional. Determines whether or not a public IP address is added to your VM instance. The default value is `true`. **Caution:** don't specify `false` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`sap_deployment_debug` | Boolean | Optional. Only when Cloud Customer Care asks you to enable debugging for your deployment, specify `true`, which makes the deployment generate verbose deployment logs. The default value is `false`.   
`reservation_name` | String | Optional. To use a specific [Compute Engine VM reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) for this deployment, specify the name of the reservation. By default, the installation script selects any available Compute Engine reservation based on the following conditions.  For a reservation to be usable, regardless of whether you specify a name or the installation script selects it automatically, the reservation must be set with the following: 
     * The `specificReservationRequired` option is set to `true` or, in the Google Cloud console, the **Select specific reservation** option is selected. 
     * Some Compute Engine machine types support CPU platforms that are not covered by the SAP certification of the machine type. If the target reservation is for any of the following machine types, then the reservation must specify the minimum CPU platforms as indicated: 
       * `n1-highmem-32`: Intel Broadwell
       * `n1-highmem-64`: Intel Broadwell
       * `n1-highmem-96`: Intel Skylake
       * `m1-megamem-96`: Intel Skylake
The minimum CPU platforms for all of the other machine types that are certified by SAP for use on Google Cloud conform to the SAP minimum CPU requirement.   
`vm_static_ip` | String |  Optional. Specify a valid static IP address for the VM instance. If you don't specify one, then an IP address is automatically generated for your VM instance. This argument is available in `sap_hana_scaleout` module version `202306120959` or later.   
`worker_static_ips` | List(String) | Optional. Specify an array of valid static IP addresses for the worker instances in your scale-out system. If you don't specify a value for this argument, then an IP address is automatically generated for each worker VM instance. For example, `[ "1.0.0.1", "2.3.3.4" ]`. The static IP addresses are assigned in the order of instance creation. For example, if you choose to deploy 3 worker instances but specify only 2 IP addresses for the argument `worker_static_ips`, then these IP addresses are assigned to the first two VM instances that the Terraform configuration deploys. For the third worker VM instance, the IP address is automatically generated. This argument is available in `sap_hana_scaleout` module version `202306120959` or later.   
`standby_static_ips` | List(String) | Optional. Specify an array of valid static IP addresses for the standby instances in your scale-out system. If you don't specify a value for this argument, then an IP address is automatically generated for each standby VM instance. For example, `[ "1.0.0.1", "2.3.3.4" ]`. The static IP addresses are assigned in the order of instance creation. For example, if you choose to deploy 3 standby instances but specify only 2 IP addresses for the argument `standby_static_ips`, then these IP addresses are assigned to the first two VM instances that the Terraform configuration deploys. For the third standby VM instance, the IP address is automatically generated. This argument is available in `sap_hana_scaleout` module version `202306120959` or later.   
  8. Initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud:
         
         terraform init
         

The `terraform init` command prepares your working directory for other Terraform commands.

To force a refresh of the provider plugin and configuration files in your working directory, specify the `--upgrade` flag. If the `--upgrade` flag is omitted and you don't make any changes in your working directory, Terraform uses the locally cached copies, even if `latest` is specified in the `source` URL.

  9. Optionally, create the Terraform execution plan:
         
         terraform plan
         

The `terraform plan` command shows the changes required by your current configuration. If you skip this step, then the `terraform apply` command automatically creates a new plan and prompts you to approve it.

  10. Apply the execution plan:
         
         terraform apply
         

When you are prompted to approve the actions, enter `yes`.

The `terraform apply` command sets up the Google Cloud infrastructure. When the Compute Engine machine boots, the Google Cloud infrastructure invokes startup scripts that configure the operating system and install SAP HANA.

While Terraform has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the Logging logs.

Time to completion can vary, but the entire process usually takes 20-30 minutes.




#### Example configuration

The following example shows a completed configuration file that deploys resources for an SAP HANA scale-out system with three worker hosts and one standby host in the `us-central1-f` zone. Each host is installed on an `n2-highmem-32` instance that runs on SLES for SAP 15 SP6 operating system provided by a Compute Engine public image. The NFS volumes are provided by Filestore.

For clarity, comments in the configuration file are omitted in the example.
    
    
    # ...
    module "hana_scaleout" {
    source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_scaleout/sap_hana_scaleout_module.zip"
    #
    # By default, this source file uses the latest release of the terraform module
    # for SAP on Google Cloud. To fix your deployments to a specific release
    # of the module, comment out the source property above and uncomment the source property below.
    #
    # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_scaleout/sap_hana_scaleout_module.zip"
    #
    # ...
    #
    project_id = "example-project-123456"
    zone = "us-central1-f"
    machine_type = "n1-highmem-32"
    subnetwork = "example-sub-network-sap"
    linux_image = "sles-15-sp6-sap"
    linux_image_project = "suse-sap-cloud"
    
    instance_name = "hana-scaleout-w-failover"
    sap_hana_sid = "HS4"
    sap_hana_shared_nfs = "10.74.146.58:/hana_shr"
    sap_hana_backup_nfs = "10.188.249.170:/hana_bup"
    # ...
    sap_hana_instance_number = 11
    # ...
    sap_hana_worker_nodes = 3
    sap_hana_standby_nodes = 1
    vm_static_ip = "10.0.0.1"
    worker_static_ips = ["10.0.0.2", "10.0.0.3", "10.0.0.4"]
    standby_static_ips = ["10.0.0.5"]
    deploy_infra_only  = true
    # ...
    }
    

### Create VPC firewall rules to verify deployment

To verify your deployment, create the following firewall rules:

  * A firewall rule that allows SSH connections on port 22 of each of the deployed compute instances from your local workstation, a bastion host, or a jump server.
  * A firewall rule that allows all connection types on any port of any of the deployed compute instances.



For information about how to create firewall rules, see [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).

### Verify the deployment of resources

To verify that your Terraform configuration file has successfully deployed the Google Cloud resources required for your SAP HANA scale-out system, you must perform the following:

  * Check the logs
  * Check the disks attached to the compute instances
  * Check the configured filesystems
  * If needed, clean up and retry deployment



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

       2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

       3. Go to your working directory and delete the deployment to clean up the VMs and persistent disks from the failed installation:
              
              terraform destroy

When you are prompted to approve the action, enter `yes`.

       4. Rerun your deployment.




### Check the disks attached to the compute instances

After the deployment is complete, check the disks attached to the deployed compute instances. The disk names indicate their role in the SAP HANA scale-out system.

To check the disks attached to the compute instances, complete the following steps:

  1. In the Google Cloud console, go to the Compute Engine **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. View the values in the **Name** and **In use by** fields.

The value in the **In use by** field is the name of the compute instance to which the disk is attached. The disk that has **data00001** in its name is deployed to host the `/hana/data` directory of the master node. Similarly, the disk that has **log00002** in its name is deployed to host the `/hana/log` directory of a worker node. Notice that the compute instance that hosts the standby node has only one disk attached in addition to the boot disk, which is to host the `/usr/sap` directory.




Alternatively, you can go to the [VM instances](https://console.cloud.google.com/compute/instances) page, click the deployed compute instances, and view disk details.

### Check the configured filesystems

Check the filesystems configured on the master node, a worker node, and a standby node as follows:

  1. In the Google Cloud console, go to the Compute Engine **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **SSH** button available against the compute instance deployed to run the SAP HANA master node.

You can identify this compute instance by viewing its name; it doesn't contain any suffix, unlike the worker and standby nodes.

  3. In the terminal of the compute instance, switch to the root user:
         
         sudo su -
         

  4. Display information about configured filesystems:
         
         df -h -x tmpfs
         

Your output is similar to the following example. Notice that the logical volumes and volume groups are yet to be created. These actions are performed later in this guide.
         
         hana-scaleout-w-failover:~ # df -h -x tmpfs
         Filesystem                         Size  Used Avail Use% Mounted on
         /dev/sda3                           45G  7.7G   38G  18% /
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         efivarfs                           256K   26K  226K  11% /sys/firmware/efi/efivars
         /dev/sda2                           20M  3.9M   17M  20% /boot/efi

  5. Repeat the preceding set of steps for a worker node and a standby node.

Similar to the master node, the `/hana/data` and `/hana/log` directories are **not mounted** on the worker and standby nodes.

On a worker node, your output is similar to the following example:
         
         hana-scaleout-w-failoverw1:~ # df -h -x tmpfs
         Filesystem                         Size  Used Avail Use% Mounted on
         /dev/sda3                           45G  7.6G   38G  17% /
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         efivarfs                           256K   27K  225K  11% /sys/firmware/efi/efivars
         /dev/sda2                           20M  3.9M   17M  20% /boot/efi

On a standby node, your output is similar to the following example:
         
         hana-scaleout-w-failoverw4:~ # df -h -x tmpfs
         Filesystem                         Size  Used Avail Use% Mounted on
         /dev/sda3                           45G  7.6G   38G  17% /
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         efivarfs                           256K   27K  225K  11% /sys/firmware/efi/efivars
         /dev/sda2                           20M  3.9M   17M  20% /boot/efi




### Clean up and retry deployment

If any of the deployment verification steps in the preceding sections show that the installation wasn't successful, then you must undo your deployment and retry it by completing the following steps:

  1. Resolve any errors to ensure that your deployment doesn't fail again for the same reason. For information about checking the logs, or resolving quota related errors, see Check the logs.

  2. Open Cloud Shell or, if you installed the Google Cloud CLI on your local workstation, then open a terminal.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Go to the directory that contains the Terraform configuration file that you used for this deployment.

  4. Delete all resources that are part of your deployment by running the following command:
         
         terraform destroy

When you are prompted to approve the action, enter `yes`.

  5. Retry your deployment as instructed earlier in this guide.




## Optimize OS configuration

Optimizing the Linux kernel network and memory management subsystems is critical for system performance and ensuring that the environment meets SAP support requirements. You must also ensure that the necessary OS packages are installed.

To optimize the OS configuration for your SAP HANA scale-out system, perform the following on all the underlying compute instances:

  * Tune the kernel and network settings
  * Install OS packages
  * Set up passwordless SSH access for all nodes



### Tune the kernel and network settings

  1. In the Google Cloud console, go to the Compute Engine **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **SSH** button available against the compute instance deployed to run the SAP HANA master node.

  3. Ensure that `SELINUX` is disabled by completing the following steps:

     1. Edit the `/etc/selinux/config` file and set `SELINUX=disabled`:
            
            sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config
            

     2. Apply the change:
            
            sudo setenforce 0
            

  4. In the `/etc/default/grub` file, verify that the following boot parameter values are set:
         
         transparent_hugepage=never
         intel_idle.max_cstate=1
         processor.max_cstate=1
         intel_iommu=off

You can run the following command to view these parameter values:
         
         grep -E "transparent_hugepage|intel_idle.max_cstate|processor.max_cstate|intel_iommu" /etc/default/grub
         

If the parameter values are different, then update them by completing the following steps:

     1. Edit the `/etc/default/grub` file:
            
            vi /etc/default/grub
             ```
            

     2. Append the following to the file's contents:
            
            GRUB_CMDLINE_LINUX_DEFAULT="transparent_hugepage=never intel_idle.max_cstate=1 processor.max_cstate=1 intel_iommu=off
             ```
            

     3. Regenerate the `/etc/default/grub` file:
            
            grub2-mkconfig -o /boot/grub2/grub.cfg
             ```
            

     4. Verify that the boot parameter values are set correctly:
            
            grep -E "transparent_hugepage|intel_idle.max_cstate|processor.max_cstate|intel_iommu" /etc/default/grub
             ```
            

  5. To help ensure the optimal performance and stability of the SAP HANA scale-out system, tune the kernel and network parameters by completing the following steps:

     1. Edit the `/etc/sysctl.conf` file:
            
            vi /etc/sysctl.conf
            

     2. Append the following parameter values to the file's contents:
            
            net.ipv4.tcp_slow_start_after_idle=0
            kernel.numa_balancing = 0
            net.core.somaxconn = 4096
            net.ipv4.tcp_tw_reuse = 1
            net.ipv4.tcp_timestamps = 1
            net.ipv4.tcp_syn_retries = 8
            net.ipv4.tcp_wmem = 4096 16384 4194304
            

  6. If your compute instance uses the VirtIO network interface card, then you must optimize it.

     * To check if your compute instance uses VirtIO:
           
           lsmod | grep -q virtio_net
           

     * If your compute instance uses VirtIO, then append the following parameter value to the `/etc/sysctl.conf` file:
           
           net.ipv4.tcp_limit_output_bytes = 1048576
           

  7. To force the OS to apply all updated parameter values instantly, without requiring the compute instance to reboot, run the following command:
         
         sysctl -p
         

  8. Repeat steps 3-7 for all the worker and standby nodes in your SAP HANA scale-out system.




### Install OS packages

  1. Prepare the OS by ensuring that it includes the software components specified in the following SAP notes:

     * [2578899 - SUSE Linux Enterprise Server 15: Installation Note](https://launchpad.support.sap.com/#/notes/2578899)
     * [1984787 - SUSE LINUX Enterprise Server 12: Installation notes](https://launchpad.support.sap.com/#/notes/1984787)
  2. Activate the SAP tuning profile by applying the standard SAP HANA solution profile and enabling the background daemon to maintain these configuration parameters across reboots:
         
         saptune solution apply HANA
         saptune service takeover
         systemctl enable saptune
         

  3. Install [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

Google Cloud's Agent for SAP is required for SAP support of SAP systems running on Google Cloud, including SAP NetWeaver, SAP HANA, SAP ASE, SAP MaxDB, and others. To install the agent, follow the instructions described in the guide of your choice:

     * To install the agent individually on all the deployed compute instances by using a package manager, see [Install and configure Google Cloud's Agent for SAP on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm).

     * To install and manage the agent on a fleet of VMs by using VM Extension Manager, see [Install and manage Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet).




### Set up passwordless SSH access for all nodes

An SAP HANA scale-out system that uses the host auto-failover solution requires seamless, passwordless communication between all nodes using the root user. For passwordless SSH access, you need to add the SSH public keys to the instance metadata of all deployed instances. The format of the metadata is `USERNAME: PUBLIC-KEY-VALUE`.

For information about adding SSH keys to compute instances, see [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata).

###  Use automation 

  1. Create a file named `nodes.txt` that includes details of all the deployed compute instances in the following format: zone name, whitespace, and then the compute instance name.
         
         # cat nodes.txt
         us-central1-f hana-scaleout-w-failover
         us-central1-f hana-scaleout-w-failoverw1
         us-central1-f hana-scaleout-w-failoverw2
         us-central1-f hana-scaleout-w-failoverw3
         us-central1-f hana-scaleout-w-failoverw4

  2. Create a list of public keys from all deployed instances:
         
         while read -u10 ZONE HOST ;  do echo "Collecting public-key from $HOST"; { echo 'root:'; gcloud compute ssh --quiet --zone $ZONE $HOST --tunnel-through-iap -- sudo cat /root/.ssh/id_rsa.pub; } | tr -ds '\n' " " >> public-ssh-keys.txt; done 10< nodes.txt
         

  3. Assign the SSH public keys as metadata entries to all instances:
         
         while read -u10 ZONE HOST ;  do echo "Adding public keys to $HOST"; gcloud compute instances add-metadata --metadata-from-file ssh-keys=public-ssh-keys.txt --zone $ZONE $HOST; done 10< nodes.txt
         




###  Follow manual steps 

  1. For each compute instance that is part of your SAP HANA scale-out system, collect the public key for the `root` user:
         
         gcloud compute ssh INSTANCE_NAME \
             --zone ZONE_ID \
             --quiet -- sudo cat /root/.ssh/id_rsa.pub
         

  2. Prepend the key with the string `root:` and write the key as a new line into the file named `public-ssh-keys.txt`. For example:
         
         root:ssh-rsa AAAAB3NzaC1JfuYnOI1vutCs= root@INSTANCE_NAME<

  3. After collecting all SSH public keys, upload the keys as metadata to all instances:
         
         gcloud compute instances add-metadata INSTANCE_NAME \
             --metadata-from-file ssh-keys=public-ssh-keys.txt \
             --zone ZONE_ID
         




## Configure storage for the scale-out system

To configure storage for the SAP HANA scale-out system, you must complete the following tasks:

  * Configure swap space
  * Set up NFS storage



### Configure swap space

  * On all the nodes that you've created for your SAP HANA scale-out system, you must configure the swap file or dedicated swap partition.

For information about SWAP space recommendations for SAP HANA, see the SAP note [1999997 - FAQ: SAP HANA memory](https://me.sap.com/notes/1999997).




### Set up NFS storage

An SAP HANA scale-out system requires an NFS solution, such as Filestore, to share the `/hana/shared` and `/hanabackup` directories between all nodes.

To set up NFS storage for the `/hana/shared` and `/hanabackup` directories, complete the following steps:

  1. Verify that you've set up the NFS solution.

  2. Verify that the NFS volumes that you've created are empty.

Any existing files can conflict with the deployment process, particularly if the files or folder reference the SAP system ID (SID) that you've assigned for your SAP HANA scale-out system. The deployment process cannot determine whether the files can be overwritten.

  3. Install and configure the `autofs` package to mount the `/hana/shared` and `/hanabackup` NFS volumes on the compute instance when the file directories are first accessed.

**Note:** The mounting of the `/hana/data` and `/hana/log` directories is managed by the storage manager for SAP HANA, which you configure in a later section.

To configure the `autofs` package, complete the following steps:

     1. Establish an SSH connection with the compute instance that you've deployed for the SAP HANA master node.

     2. Install the `autofs` package. This package ensures that the core `automounter` daemon is present on the system.
            
            zypper in -y autofs
            

     3. Append the direct map definition to the master configuration:
            
            echo "/- /etc/auto.hana" | sudo tee -a /etc/auto.master
            

     4. Define the production-optimized performance mount options:
            
            NFS_OPTS="-rsize=1048576,vers=3,mountvers=3,wsize=1048576,hard,intr,timeo=18,retrans=200"
            

     5. Create and populate the sub-map file with your NFS solution paths:
            
            echo "/hana/shared ${NFS_OPTS} HANA_SHARED_NFS_IP:/HANA_SHARED_NFS_EXPORT_PATH" | sudo tee -a /etc/auto.hana
            echo "/hanabackup ${NFS_OPTS} HANA_BACKUP_NFS_IP:/HANA_BACKUP_NFS_EXPORT_PATH" | sudo tee -a /etc/auto.hana
            

Replace the following:

        * `HANA_SHARED_NFS_IP`: the IP address of the NFS solution that you've created to host the `/hana/shared` directory
        * `HANA_SHARED_NFS_EXPORT_PATH`: the name of the file share that you've provisioned in the NFS solution, to host the `/hana/shared` directory
        * `HANA_BACKUP_NFS_IP`: the IP address of the NFS solution that you've created to host the `/hanabackup` directory
        * `HANA_BACKUP_NFS_EXPORT_PATH`: the name of the file share that you've provisioned in the NFS solution, to host the `/hana/backup` directory
     6. Refresh the system mount engine:
            
            sudo systemctl daemon-reload
            

     7. Enable and start the `autofs` service:
            
            sudo systemctl enable --now autofs
            

     8. Access each directory to trigger `autofs` and thereby mount the NFS volumes. For example:
            
            cd /hana/shared
            cd /hanabackup
            

     9. Verify that the directories have been mounted:
            
            df -Th | grep FILE_SHARE_NAME
            

Replace `FILE_SHARE_NAME` with the name of the file share that you've created in your NFS solution. The output is similar to the following example:
            
            10.52.158.66:/nfs_hana_shared              nfs       1.0T   37G  988G   4% /hana/shared
            10.52.158.2:/nfs_hana_bkp                  nfs       1.0T     0  1.0T   0% /hanabackup

     10. Configure the `autofs` package on all the compute instances that you've deployed to run the worker and standby. You do this by repeating steps a-h in this procedure.




## Set up disks and LVM configuration for storage manager for SAP HANA

In an SAP HANA scale-out system that uses the host auto-failover solution, the `/usr/sap` directory remains permanently mounted locally on each host. However, the production performance paths for the `/hana/data` and `/hana/log` directory must be managed dynamically.

The Google Cloud storage manager for SAP HANA standby nodes (`gceStorageClient`) requires that the volume groups (VG) and logical volumes (LV) for the `/hana/data` and `/hana/log` directories are initially formatted and initialized under strict ownership constraints, and then immediately unmounted and deactivated. This offline state is mandatory because it allows the `gceStorageClient` API scripts to safely attach, activate, and mount the block volumes over the Google Cloud infrastructure layer to whichever active node is assigned the partition identity during database initialization or host failover events.

The following steps create a permanent mount for your SAP HANA binaries (`/usr/sap`) while preparing the `/hana/data` and `/hana/log` directories for dynamic cloud orchestration by using the storage manager for SAP HANA.

To set up the disks and LVM configuration, complete the following steps:

  1. On the master node of your scale-out system, complete the following steps:

     1. Identify the disk device names for the Google Cloud storage volumes:
            
            sudo ls -l /dev/disk/by-id/google-*
            

The output is a symlink mapping, which looks like the following example:
            
            ~ # ls -l /dev/disk/by-id/google-*
            lrwxrwxrwx 1 root root  9 Jun  5 20:53 /dev/disk/by-id/google-hana-scaleout-w-failover-usrsap00001 -> ../../sdd
            lrwxrwxrwx 1 root root  9 Jun  5 20:53 /dev/disk/by-id/google-hana-scaleout-w-failover-data00001 -> ../../sde
            lrwxrwxrwx 1 root root  9 Jun  5 20:53 /dev/disk/by-id/google-hana-scaleout-w-failover-log00001 -> ../../sdf

     2. Make note of the disk device names that correspond to the `/hana/data`, `/hana/log`, and `/usr/sap` names. You use these in the next step.

     3. Define environment variables for the disk paths:
            
            DISK_USRSAP="/dev/disk/by-id/google-USR_SAP_DISK_NAME"
            DISK_DATA="/dev/disk/by-id/google-HANA_DATA_DISK_NAME"
            DISK_LOG="/dev/disk/by-id/google-HANA_LOG_DISK_NAME"
            SAPHANA_SID="SID"
            

Replace the following:

        * `USR_SAP_DISK_NAME`: the name of the disk that you've created for the `/usr/sap` directory on the master node
        * `HANA_DATA_DISK_NAME`: the name of the disk that you've created for the `/hana/data` directory on the master node
        * `HANA_LOG_DISK_NAME`: the name of the disk that you've created for the `/hana/log` directory on the master node
        * `SID`: the SAP system ID (SID) of the SAP HANA scale-out system
     4. Format and mount the `/hana/data` and `/hana/log` directories:

        1. Create and format the logical volume for `/hana/data`:
               
               sudo pvcreate ${DISK_DATA}
               sudo vgcreate vg_hana_data ${DISK_DATA}
               sudo lvcreate -l 100%FREE -n data vg_hana_data
               sudo mkfs.xfs /dev/vg_hana_data/data
               

        2. Create and format the logical volume for `/hana/log`:
               
               sudo pvcreate ${DISK_LOG}
               sudo vgcreate vg_hana_log ${DISK_LOG}
               sudo lvcreate -l 100%FREE -n log vg_hana_log
               sudo mkfs.xfs /dev/vg_hana_log/log
               

        3. Mount the logical volumes and update their ownership:
               
               sudo mkdir -p /hana/data /hana/log
               sudo mount -t xfs -o logbsize=256k /dev/vg_hana_data/data /hana/data
               sudo mount -t xfs -o logbsize=256k /dev/vg_hana_log/log /hana/log
               sudo chown -R 900:79 /hana/data /hana/log
               sudo chmod -R 755 /hana/data /hana/log
               

     5. Format and mount the `/usr/sap` directory:

        1. Initialize the raw disk as an LVM Physical Volume (PV):
               
               sudo pvcreate ${DISK_USRSAP}
               

        2. Combine the PV into a dedicated Volume Group (VG) for `/usr/sap`:
               
               sudo vgcreate vg_hana_usrsap ${DISK_USRSAP}
               

        3. Allocate 100% of the space to a Logical Volume (LV) named `usrsap`:
               
               sudo lvcreate -l 100%FREE -n usrsap vg_hana_usrsap
               

        4. Format the volume using XFS file system:
               
               sudo mkfs.xfs /dev/vg_hana_usrsap/usrsap
               

        5. Create the local anchor directory if it does not exist:
               
               sudo mkdir -p /usr/sap
               

        6. Append a permanent entry to the system file table (`/etc/fstab`):
               
               echo "/dev/vg_hana_usrsap/usrsap /usr/sap xfs defaults,nofail,logbsize=256k 0 2" | sudo tee -a /etc/fstab
               

        7. Refresh the system mount engine and mount the disk immediately:
               
               sudo systemctl daemon-reload && sudo mount -a
               

     6. Unmount and deactivate the logical volumes so that the storage manager for SAP HANA can control them:

        1. Flush all pending data from system cache blocks to physical disk:
               
               sudo sync
               

        2. Unmount the data and log directories:
               
               sudo umount /hana/log
               sudo umount /hana/data
               

        3. Deactivate the volume groups so they are offline:
               
               sudo vgchange -a n vg_hana_data
               sudo vgchange -a n vg_hana_log
               

     7. Recreate empty mount points for successful installation of SAP HANA.

Because the logical volumes for `/hana/data` and `/hana/log` were unmounted in the previous step, the physical paths `/hana/data/SID` and `/hana/log/SID` vanished from your root partition view. You must recreate the physical paths as empty baseline folders to avoid issues during SAP HANA installation.
            
            sudo mkdir -p /hana/data/${SAPHANA_SID} /hana/log/${SAPHANA_SID}
            

  2. Format and mount the `/hana/data`, `/hana/log`, and `/usr/sap` directories on all the worker nodes of your scale-out system by repeating the previous step for all of them.

  3. On all the standby nodes of your scale-out system, initialize and mount the `/usr/sap` disk:

     1. Identify the disk device names for the Google Cloud storage volumes:
            
            sudo ls -l /dev/disk/by-id/google-*
            

The output is a symlink mapping, which looks like the following example:
            
            ~ # ls -l /dev/disk/by-id/google-*
            lrwxrwxrwx 1 root root  9 Jun  5 20:53 /dev/disk/by-id/google-hana-scaleout-w-failoverw4-usrsap00001 -> ../../sdd

     2. Make note of the disk device name used by the `/usr/sap` directory. You use this in the next step.

     3. Define environment variable for the disk path:
            
            DISK_USRSAP="/dev/disk/by-id/google-USR_SAP_DISK_NAME_ON_STANDBY_NODE"
            SAPHANA_SID="SID"
            

Replace `USR_SAP_DISK_NAME_ON_STANDBY_NODE` with the name of the disk that noted in the previous step.

     4. Format and mount the `/usr/sap` directory:
            
            sudo pvcreate /dev/disk/by-id/google-USR_SAP_DISK_NAME_ON_STANDBY_NODE
            sudo vgcreate vg_hana_usrsap /dev/disk/by-id/google-USR_SAP_DISK_NAME_ON_STANDBY_NODE
            sudo lvcreate -l 100%FREE -n usrsap vg_hana_usrsap
            sudo mkfs.xfs /dev/vg_hana_usrsap/usrsap
            sudo mkdir -p /usr/sap
            echo "/dev/vg_hana_usrsap/usrsap /usr/sap xfs defaults,nofail,logbsize=256k 0 2" | sudo tee -a /etc/fstab
            sudo systemctl daemon-reload && sudo mount -a
            

     5. Recreate empty mount points for successful installation of SAP HANA.

Because the logical volumes for `/hana/data` and `/hana/log` were unmounted the previous step, the physical paths `/hana/data/SID` and `/hana/log/SID` vanished from your root partition view. You must recreate the physical paths as empty baseline folders to avoid issues during SAP HANA installation.
            
            sudo mkdir -p /hana/data/${SAPHANA_SID} /hana/log/${SAPHANA_SID}
            




## Install and configure storage manager for SAP HANA

The Google Cloud storage manager for SAP HANA (`gceStorageClient`) is a high-availability framework that you can use to handle dynamic disk attachment, disk detachment, fencing, and file system mounts during a host failover event.

When a takeover occurs, the host auto-failover solution uses the SAP HANA Storage Manager API and the Google Cloud storage manager for SAP HANA standby nodes to move the volume mounts from the failed host to the standby host.

On Google Cloud, the storage manager for SAP HANA is required for SAP HANA systems that use the SAP HANA host auto-failover solution. To deploy it successfully, you must install the OS level binaries across all hosts, delegate specific root-level execution privileges to the `SID_LCadm` user, and define the master topology mapping inside the `global.ini` under `/hana/shared`.

### Install the storage manager

You must install the storage manager for SAP HANA on all the nodes of your scale-out system as follows:

  1. Establish an SSH connection with a compute instance that you've deployed.

  2. Update mandatory Python dependency modules:
         
         sudo zypper in -f -y python3-pyasn1-modules
         

  3. Register the official Google Cloud `gceStorageClient` repository:
         
         sudo zypper addrepo --gpgcheck-allow-unsigned-package --refresh https://packages.cloud.google.com/yum/repos/google-sapgcestorageclient-sles$(grep -oP '(?<=^VERSION_ID=).+' /etc/os-release | tr -d '"' | cut -f1 -d.)-\$basearch google-sapgcestorageclient
         

  4. Install the `gceStorageClient` package:
         
         sudo zypper --no-gpg-checks install -y google-sapgcestorageclient
         

  5. Repeat the steps described in this section on all the other compute instances you've deployed to run your scale-out system.




### Configure the file system

To provision environment configurations in the `/hana/shared` file system, you must run the script provided by Google Cloud:

  1. Establish an SSH connection to the compute instance that you've deployed to run the SAP HANA master node.

  2. Configure the file system by running the provided script:
         
         sudo /usr/sap/google-sapgcestorageclient/install.sh
         sudo chmod +x /hana/shared/gceStorageClient/send_metrics.sh
         

Although you've run this script from the master node, the changes are instantly propagated to all the nodes of your scale-out system. This is because the `/hana/shared` directory is accessible from all the nodes.




### Configure OS for the storage manager

To help the SAP HANA databases worker tasks to securely interact with the underlying infrastructure, you must configure the OS for the `gceStorageClient` on all the nodes of your scale-out system. To do this, complete the following steps:

  1. Establish an SSH connection with a compute instance that you've deployed.

  2. Configure the gcloud CLI to work under the target SAP HANA `SID_LCadm` user account:
         
         mkdir -p /usr/sap/SID/home/.config/gcloud/
         chown -R 900:79 /usr/sap/SID/home/.config/gcloud/
         

  3. Enable the `gceStorageClient` tool to run low-level Linux administration actions, such as managing the volume groups and flushing the CSCI mappings. You do this by adding the necessary paths to an allowlist in the system `sudoers` registry as follows:

**Note:** While the procedure in this step is recommended by SUSE, you can use an alternative approach. Instead of creating a drop-in configuration file, you can add the required access directly to your `/etc/sudoers` file.
     1. Safely create a new `sudo` permission files by using `visudo`:
            
            sudo visudo -f /etc/sudoers.d/gceStorageClient
            

     2. Append the following block to this file:
            
            SID_LCadm ALL=NOPASSWD: /sbin/multipath,/sbin/multipathd,/usr/bin/sg_persist,/bin/mount,/bin/umount,/bin/kill,/usr/bin/lsof,/usr/bin/systemctl,/sbin/xfs_repair,/usr/bin/mkdir,/sbin/vgscan,/sbin/pvscan,/sbin/lvscan,/sbin/vgchange,/sbin/lvdisplay,/usr/bin/gcloud,/sbin/dmsetup
            

     3. Make sure that the `/etc/sudoers` file includes the following:

        * For SLES for SAP 15 SP3 or later:
              
              @includedir /etc/sudoers.d
              

        * For versions up to SLES for SAP 15 SP2:
              
              #includedir /etc/sudoers.d
              

The `#` in this text is part of the syntax and does not mean that the line is a comment.

  4. Repeat the steps described in this section on all the other compute instances you've deployed to run your scale-out system.




### Configure the storage manager

You must configure the Google Cloud storage manager for SAP HANA to link the disks you've deployed with their respective SAP HANA scale-out partition ID values. You do this by using the information available in the `global.ini` file of the SAP Storage Connector.

To configure storage manager for SAP HANA, complete the following steps:

  1. Establish an SSH connection with the compute instance that you've deployed to run the SAP HANA master node.

  2. Navigate to the `hana/shared/gceStorageClient` directory and edit the `global.ini` file:
         
         cd /hana/shared/gceStorageClient
         vi global.ini
         

  3. Include the disk-to-partition ID mapping by using the following format:
         
         partition_PARTITION_NUMBER_USAGE_TYPE__PARAMETER= VALUE
         

Replace the following:

     * `PARTITION_NUMBER`: the partition number, which can be a number or the wildcard `*`.
     * `USAGE_TYPE`: the usage type of the disk, which can be `data`, `log`, or the wildcard `*`.
     * PARAMETER and VALUE are user-defined values.

The following is an example of an edited `global.ini` file:
    
    [persistence]
    basepath_datavolumes = /hana/data/HS4
    basepath_logvolumes = /hana/log/HS4
    use_mountpoints = yes
    basepath_shared = no
    [storage]
    ha_provider = gceStorageClient
    ha_provider_path = /hana/shared/gceStorageClient
    partition_1_data__pd = hana-scaleout-w-failover-data00001
    partition_1_log__pd = hana-scaleout-w-failover-log00001
    partition_2_data__pd = hana-scaleout-w-failoverw1-data00002
    partition_2_log__pd = hana-scaleout-w-failoverw1-log00002
    partition_3_data__pd = hana-scaleout-w-failoverw2-data00003
    partition_3_log__pd = hana-scaleout-w-failoverw2-log00003
    partition_4_data__pd = hana-scaleout-w-failoverw3-data00004
    partition_4_log__pd = hana-scaleout-w-failoverw3-log00004
    partition_*_data__dev = /dev/vg_hana_data/data
    partition_*_log__dev = /dev/vg_hana_log/log
    partition_*_data__mountOptions = -t xfs -o logbsize=256k
    partition_*_log__mountOptions = -t xfs -o logbsize=256k
    partition_*_*__fencing = disabled
    [trace]
    ha_gcestorageclient = info

In this example:

     * `partition_**1_data** __pd` is the name of the disk that hosts the `/hana/data` directory on the first node of your SAP HANA system, which usually is the master node.
     * `partition_**1_log** __pd` is the name of the disk that hosts the `/hana/log` directory on the first node of your SAP HANA system, which usually is the master node.
     * `partition_***** _data__dev` is the path to the logical volume, such as `/dev/vg_hana_data/data`, inside the compute instance.
  4. Include the email address of the service account that you created for the storage manager for SAP HANA:
         
         partition_*_*__gcloudAccount = STORAGE_CLIENT_SERVICE_ACCOUNT
         

Replace `STORAGE_CLIENT_SERVICE_ACCOUNT` with the email address of the service that you created in the [Set up a service account for the storage manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-with-standby-nodes-manual-config-sles#set-up-service-account-for-sm4sh) section.




## Install and configure SAP HANA

This section uses the SAP HANA database lifecycle manager (HDBLCM) to install SAP HANA on the deployed compute instances.

Because you're using Google Cloud storage manager for SAP HANA (`gceStorageClient`), you also create a `hana_install.cfg` configuration file with the following parameter: `storage_cfg=/hana/shared/gceStorageClient`. This configuration directs HDBLCM to bypass standard storage checks and rely on `gceStorageClient` to handle the mounting profiles during failover events.

### Install and configure the SAP HANA master node

On the compute instance that you've deployed to run the SAP HANA master node, complete the following steps:

  1. Establish an SSH connection with the compute instance that you've deployed to run the SAP HANA master node.

You can identify this compute instance by viewing its name; it doesn't contain any suffix, unlike the worker and standby nodes. For example, in the example described in this guide, the name of the compute instance meant to run the SAP HANA master node is `hana-scaleout-w-failover`.

  2. Create the `hana_install.cfg` configuration file:

     1. Create the deployment directory
            
            sudo mkdir -p /root/.deploy
            

     2. Create the silent configuration file `hana_install.cfg`:
            
            sudo tee /root/.deploy/hana_install.cfg > /dev/null << 'EOF'
            [General]
            components=client,server
            [Server]
            sid=HS4
            number=00
            userid=900
            groupid=79
            apply_system_size_dependent_parameters=off
            autostart=y
            # Connects the core SAP HANA kernel parameters to the Google Storage Client hooks
            storage_cfg=/hana/shared/gceStorageClient
            EOF
            

  3. Download the SAP HANA installation media and extract it in a directory.

  4. In directory where you've extracted the SAP HANA installation media, initiate SAP HANA installation by using the HDBLCM tool. The following step also references the `hana_install.cfg` file that you've created:
         
         sudo ./hdblcm --configfile=/root/.deploy/hana_install.cfg
         




### Add the worker and standby nodes

After you've successfully configured the SAP HANA master node, you must add the worker and standby nodes to your deployment as follows:

  1. In the master node, create the `add_hosts.cfg` configuration file that defines the hostnames and their operational roles in the scale-out deployment as follows.

     * In the `[AddHosts]` section, add the hostnames and assign them the role of `worker` or `standby`.
     * Include the `storage_cfg=/hana/shared/gceStorageClient` parameter.

The following is an example configuration:
    
    sudo tee /root/.deploy/add_hosts.cfg > /dev/null << 'EOF'
    [AddHosts]
    # Register all target worker and standby hosts simultaneously
    addhosts=WORKER1_HOSTNAME:role=worker,WORKER2_HOSTNAME:role=worker,STANDBY1_HOSTNAME:role=standby
    storage_cfg=/hana/shared/gceStorageClient
    listen_interface=global
    root_user=root
    EOF
    

Replace the following:

     * `WORKER1_HOSTNAME`: the name of the compute instance that you've deployed to run a worker node in your SAP HANA scale-out system
     * `STANDBY1_HOSTNAME`: the name of the compute instance that you've deployed to run a standby node in your SAP HANA scale-out system
  2. Apply this configuration:

     1. Navigate to the directory where you've installed the HDBLCM tool:
            
            cd /hana/shared/SID/hdblcm
            

     2. Run the HDBLCM tool with reference to the `add_hosts.cfg` file that you've created:
            
            sudo ./hdblcm --action=add_hosts --configfile=/root/.deploy/add_hosts.cfg
            

     3. Follow the prompts on the screen to apply the configuration. This includes entering the storage partition ID for each node that you've defined in the `global.ini` file.




### Verify that `autostart` is active

  1. Establish an SSH connection with the compute instance that runs the SAP HANA master node.

  2. Verify that `autostart` is enabled in the SAP HANA instance profile:
         
         grep "Autostart" /hana/shared/SID/profile/*
         

The output must be similar to the following example and include `**Autostart=1**`:
         
         hana-scaleout-w-failover:hs4adm> grep "Autostart" /hana/shared/HS4/profile/*
         /hana/shared/HS4/profile/HS4_HDB00_hana-scaleout-w-failover:**Autostart=1**
         /hana/shared/HS4/profile/HS4_HDB00_hana-scaleout-w-failoverw1:**Autostart=1**
         /hana/shared/HS4/profile/HS4_HDB00_hana-scaleout-w-failoverw2:**Autostart=1**
         /hana/shared/HS4/profile/HS4_HDB00_hana-scaleout-w-failoverw3:**Autostart=1**
         /hana/shared/HS4/profile/HS4_HDB00_hana-scaleout-w-failoverw4:**Autostart=1**
         hana-scaleout-w-failover:hs4adm>




### Enable fencing

  1. Establish an SSH connection with the compute instance that runs the SAP HANA master node.

  2. To enable fencing in your SAP HANA scale-out system, update the `global.ini` file by running the following commands.

The `cdcoc` command navigates to the `/usr/sap/SID/SYS/global/hdb/custom/config` directory, which contains the `global.ini` file.
         
         sudo su - SID_LCadm
         cdcoc
         sed -i -e 's/partition_\*_\*__fencing = disabled/partition_*_*__fencing = enabled/g' global.ini
         

  3. Verify that fencing is enabled by reviewing the updated the `global.ini` file:
         
         cat global.ini | grep fencing
         

The output is similar to the following:
         
         partition_*_*__fencing = enabled
         




### Configure the secondary and tertiary master nodes

Configuring the secondary and tertiary master nodes helps SAP HANA clearly determine which active node in the scale-out system must be promoted as the new master node in case of a failover event.

To configure the secondary and tertiary master nodes, complete the following steps:

  1. Establish an SSH connection with the compute instance that runs the SAP HANA master node.

  2. Switch to the `SID_LCadm` user:
         
         sudo su - SID_LCadm
         

  3. Create the `update_landscape.sql` file and add the names and roles of all the nodes in your SAP HANA scale-out system.

In the following example, the first worker node and the first standby node are designated as the secondary and tertiary master nodes, respectively.
         
         cat << 'EOF' > update_landscape.sql
         CALL SYS.UPDATE_LANDSCAPE_CONFIGURATION('deploy','{
           "HOSTS": {
             "WORKER1_HOSTNAME": {
               "INDEXSERVER_CONFIG_ROLE": "WORKER",
               "NAMESERVER_CONFIG_ROLE": "MASTER 2"
             },
             "STANDBY1_HOSTNAME": {
               "INDEXSERVER_CONFIG_ROLE": "STANDBY",
               "NAMESERVER_CONFIG_ROLE": "MASTER 3"
             }
           }
         }');
         EOF
         

  4. Run the `update_landscape.sql` file:
         
         hdbsql -i INSTANCE_NUMBER -d SYSTEMDB -u SYSTEM -p 'SYSTEM_PASSWORD' -I update_landscape.sql
         

Replace `SYSTEM_PASSWORD` with the password of the `SYSTEM` user of your SAP HANA database.

  5. Verify that the **NameServer Config Role** configuration is updated such that the `master 2` and `master 3` roles are assigned to separate nodes in your system.

Conventionally, the `master 2` role is assigned to the first worker node and the `master 3` role is assigned to the first standby node.
         
         cdpy; python landscapeHostConfiguration.py
         

The output is similar to the following:
         
         hana-scaleout-w-failover:hs4adm> cdpy
         hana-scaleout-w-failover:hs4adm> python landscapeHostConfiguration.py
         | Host                       | Host   | Host   | Failover | Remove | Storage   | Storage   | Failover | Failover | NameServer | NameServer | IndexServer | IndexServer | Host    | Host    | Worker  | Worker  |
         |                            | Active | Status | Status   | Status | Config    | Actual    | Config   | Actual   | Config     | Actual     | Config      | Actual      | Config  | Actual  | Config  | Actual  |
         |                            |        |        |          |        | Partition | Partition | Group    | Group    | Role       | Role       | Role        | Role        | Roles   | Roles   | Groups  | Groups  |
         | -------------------------- | ------ | ------ | -------- | ------ | --------- | --------- | -------- | -------- | ---------- | ---------- | ----------- | ----------- | ------- | ------- | ------- | ------- |
         | hana-scaleout-w-failover   | yes    | ok     |          |        |         1 |         1 | default  | default  | master 1   | master     | worker      | master      | worker  | worker  | default | default |
         | hana-scaleout-w-failoverw1 | yes    | ok     |          |        |         2 |         2 | default  | default  | master 2   | slave      | worker      | slave       | worker  | worker  | default | default |
         | hana-scaleout-w-failoverw2 | yes    | ok     |          |        |         3 |         3 | default  | default  | slave      | slave      | worker      | slave       | worker  | worker  | default | default |
         | hana-scaleout-w-failoverw3 | yes    | ok     |          |        |         4 |         4 | default  | default  | slave      | slave      | worker      | slave       | worker  | worker  | default | default |
         | hana-scaleout-w-failoverw4 | yes    | ignore |          |        |         0 |         0 | default  | default  | master 3   | slave      | standby     | standby     | standby | standby | default | -       |
         overall host status: ok
         | hana-scaleout-w-failover:hs4adm>

  6. To reflect the changes that you've made in the preceding sections, stop and start your SAP HANA database.




### Connect to SAP HANA

Because the instructions in this guide didn't set up an external IP address for SAP HANA, you can connect to the SAP HANA instances only through a bastion instance by using SSH, or through SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instances by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server based compute instance. After connecting to this instance, [install SAP HANA Studio](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/LATEST/en-US/c13cec2b7c2c46bdb0762ce5f1410260.html) and access your SAP HANA database.




### Enable SAP HANA Fast Restart option

The SAP HANA Fast Restart option reduces the restart time in the event that SAP HANA terminates while the operating system remains running. Google Cloud recommends that you enable this option for your SAP HANA workload, especially for multi-terabyte workloads. For more information about this option, see the SAP document [SAP HANA Fast Restart Option](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html).

###  Use automation 

Google Cloud provides a script that you can use to enable SAP HANA Fast Restart option.

**Important:** Test the script that Google Cloud provides in a non-production environment before you use it in production. You are responsible for the configuration of the SAP HANA Fast Restart option.

To enable the SAP HANA Fast Restart option by using the automation script provided by Google Cloud, complete the following steps:

  1. Establish an SSH connection with the compute instance that's running your SAP HANA workload.

  2. As the `SID_LCadm` user, stop the SAP HANA database.

  3. Download the `sap_lib_hdbfr.sh` script, which is provided by Google Cloud:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/lib/sap_lib_hdbfr.sh
         

  4. Make the `sap_lib_hdbfr.sh` file executable:
         
         sudo chmod +x sap_lib_hdbfr.sh
         

  5. Verify that the script has no errors:
         
         ./sap_lib_hdbfr.sh -help
         

If the command returns an error, then contact Cloud Customer Care. For information about how to contact Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

  6. Enable the SAP HANA Fast Restart option by running the script:
         
         sudo ./sap_lib_hdbfr.sh -h 'SID' -s SECRET_NAME
         

If you're not using a Secret Manager secret to provide the password, you can provide the password in plain text. However, Google Cloud recommends against this because the password gets recorded in the command-line history of the compute instance.
         
         sudo ./sap_lib_hdbfr.sh -h 'SID' -p PASSWORD
         

Replace the following:

     * `SID`: the SAP system ID (SID) of your SAP HANA workload; for example `HS4`
     * `SECRET_NAME`: the name of the secret in Secret Manager that securely stores the password for the `SYSTEM` user of your SAP HANA database. The secret must exist in the same Google Cloud project that runs your SAP HANA workload.
     * `PASSWORD`: the password of the `SYSTEM` user of your SAP HANA database

The output is similar to the following:
    
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
    

  7. Repeat the steps 3-7 for all the compute instances running your scale-out workload.

  8. As the `SID_LCadm` user, start the SAP HANA database on all the compute instances running your scale-out workload.




###  Follow manual steps 

To manually enable the SAP HANA Fast Restart option for your workload, complete the following steps:

  1. Establish an SSH connection with the compute instance that's running your SAP HANA workload.

  2. As the `SID_LCadm` user, stop the SAP HANA database.

  3. Create directories for the NUMA nodes and mount them in the `tmpfs` file system:

     1. Review the NUMA topology of your compute instance:
            
            sudo lscpu | grep NUMA
            

The following is an example output for a compute instance based on the `m2-ultramem-208` machine type, which has four NUMA nodes numbered 0-3. Your output is similar to this example.
            
            NUMA node(s):        4
            NUMA node0 CPU(s):   0-25,104-129
            NUMA node1 CPU(s):   26-51,130-155
            NUMA node2 CPU(s):   52-77,156-181
            NUMA node3 CPU(s):   78-103,182-207
            

     2. Create a directory for each NUMA node and assign the ownership of these directories to the SAP HANA administrator user and group:
            
            mkdir -pv /hana/tmpfsNUMA_NODE_INDEX_RANGE/SID
            chown -R SID_LCadm:sapsys /hana/tmpfs*/SID
            chmod 777 -R /hana/tmpfs*/SID

Replace the following:

        * `SID`: the SAP system ID (SID) of your SAP HANA workload; for example `HS4`
        * `NUMA_NODE_INDEX_RANGE`: the index range for the NUMA nodes available on your compute instance. For example, if your compute instance was based on the `m2-ultramem-208` machine type, which has four NUMA nodes, then you'd specify the value `0..3`.
        * `SID_LC`: the SID in lowercase; for example `hs4`
     3. Mount the NUMA node directories to the `tmpfs` file system:
            
            sudo mount tmpfsSID0 -t tmpfs -o mpol=prefer:0 /hana/tmpfs0/SID
            sudo mount tmpfsSID1 -t tmpfs -o mpol=prefer:1 /hana/tmpfs1/SID
            sudo mount tmpfsSID2 -t tmpfs -o mpol=prefer:2 /hana/tmpfs2/SID
            sudo mount tmpfsSID3 -t tmpfs -o mpol=prefer:3 /hana/tmpfs3/SID
            

     4. To ensure that these mount points persist after an OS reboot, add the following entries to the `/etc/fstab` file:
            
            tmpfsSID0 /hana/tmpfs0/SID tmpfs rw,nofail,relatime,mpol=prefer:0
            tmpfsSID1 /hana/tmpfs1/SID tmpfs rw,nofail,relatime,mpol=prefer:1
            tmpfsSID2 /hana/tmpfs2/SID tmpfs rw,nofail,relatime,mpol=prefer:2
            tmpfsSID3 /hana/tmpfs3/SID tmpfs rw,nofail,relatime,mpol=prefer:3
            

  4. (Optional) Because the `tmpfs` file system can grow and shrink dynamically, you can limit its memory usage by using the following options:

     * Limit the size of a NUMA node volume:
           
           sudo mount tmpfsSID0 -t tmpfs -o mpol=prefer:0,size=SIZE /hana/tmpfs0/SID
           

Replace `SIZE` with the size to which you want to limit the NUMA node volume. For example, `250G`.

     * Limit the overall memory usage of `tmpfs` for all NUMA nodes for a given SAP HANA instance and given compute instance by setting the `persistent_memory_global_allocation_limit` in the `[memorymanager]` section of the SAP HANA `global.ini` file.

  5. Repeat the preceding steps for all the compute instance that run your scale-out workload.

  6. From the compute instance that's running your workload, inform the SAP HANA system about the `tmpfs` locations by updating the `[persistence]` section of the `global.ini` file to include paths to the `tmpfs` location that you created in the preceding steps. Separate each `tmpfs` location with a semicolon.

The following example is specific to an `m2-ultramem-208` instance, and specifies four memory volumes that correspond to the four NUMA nodes available on the M2 instance. If you were running SAP HANA on an `m2-ultramem-416` instance, then you'd need to configure eight memory volumes.
         
         [persistence]
         basepath_datavolumes = /hana/data
         basepath_logvolumes = /hana/log
         basepath_persistent_memory_volumes = /hana/tmpfs0/SID;/hana/tmpfs1/SID;/hana/tmpfs2/SID;/hana/tmpfs3/SID
         

  7. To turn on persistent memory for any SAP HANA tables or partitions, complete the following steps on the compute instance that's running your scale-out workload:

     1. Turn on persistent memory for the SAP HANA table or partition, run the following SQL query:
            
            ALTER TABLE TABLE_OR_PARTITION_NAME persistent memory ON immediate CASCADE
            

Replace `TABLE_OR_PARTITION_NAME` with the name of the table or partition.

     2. Update the memory persistence settings by adding the `table_default` parameter in the `indexserver.ini` file:
            
            [persistent_memory]
            table_default = ON
            

For information from SAP about how to control columns, tables, and which monitoring views provide detailed information, see [Persistent Memory](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/1f61b13e096d4ef98e62c676debf117e.html).

  8. As the `SID_LCadm` user, start the SAP HANA database.




### Perform a failover test

After you have verified that the SAP HANA scale-out system is successfully deployed, test the failover function.

The following instructions trigger a failover by switching to the SAP HANA operating system user and entering the `HDB stop` command. The `HDB stop` command initiates a graceful shutdown of SAP HANA and detaches the disks from the host, which enables a relatively quick failover.

**Note:** To simulate a failure of the entire compute instance, you can enter the `sudo ip link set eth0 down` command. The `ip link set eth0 down` command shuts down the network interface to the compute instance. Failover in this case takes longer, because the system performs additional processing to confirm that the host is down and to move the disks.

To perform a failover test, complete the following steps:

  1. Connect to the compute instance of a worker host by using SSH. You can connect from the Compute Engine **VM instances** page by clicking the SSH button for each compute instance, or you can use your preferred SSH method.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Switch to the SAP HANA operating system user:
         
         su - SID_LCadm

Replace SID_LC with the value that you specified for the `sap_hana_sid` argument in your Terraform configuration file. In the example configuration shown in a preceding section of this document, the SID is `HS4`.

  3. Simulate a failure by stopping SAP HANA:
         
         HDB stop

The `HDB stop` command initiates a shutdown of SAP HANA, which triggers a failover. During the failover, the disks are detached from the failed host and reattached to the standby host. The failed host is restarted and becomes a standby host.

  4. After allowing time for the takeover to complete, connect to the host that took over for the failed host by using SSH.

  5. Switch to the root user:
         
         sudo su -

  6. Display the disk file system information:
         
         df -h

Your output is similar to the following example. Note that the `/hana/data` and `/hana/log` directories from the failed host are now mounted to the host that took over.
         
         hana-scaleout-w-failoverw4:~ # df -h
         Filesystem                         Size  Used Avail Use% Mounted on
         /dev/sda3                           45G  7.2G   38G  16% /
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         tmpfs                              154G     0  154G   0% /dev/shm
         efivarfs                           256K   26K  226K  11% /sys/firmware/efi/efivars
         tmpfs                               41G   50M   41G   1% /run
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/systemd-tmpfiles-setup-dev-early.service
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/systemd-tmpfiles-setup-dev.service
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/systemd-vconsole-setup.service
         /dev/sda2                           20M  3.9M   17M  20% /boot/efi
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/systemd-tmpfiles-setup.service
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/systemd-sysctl.service
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/serial-getty@ttyS0.service
         tmpfs                              1.0M     0  1.0M   0% /run/credentials/getty@tty1.service
         /dev/mapper/vg_hana_usrsap-usrsap   32G  860M   32G   3% /usr/sap
         10.142.81.194:/hana_shared         1.0T   62G  963G   7% /hana/shared
         tmpfs                               21G  8.0K   21G   1% /run/user/0
         10.55.104.130:/hana_backup         1.0T     0  1.0T   0% /hanabackup
         tmpfs                               21G  8.0K   21G   1% /run/user/1000
         **/dev/mapper/vg_hana_data-data      414G  8.1G  406G   2% /hana/data/HS4/mnt00002
         /dev/mapper/vg_hana_log-log        104G  5.1G   99G   5% /hana/log/HS4/mnt00002**

  7. In SAP HANA Studio, open the **Landscape** view of the SAP HANA system to confirm that the failover over was successful:

     * The status of the hosts involved in the failover must be `INFO`.
     * The **Index Server Role (Actual)** column must show the failed host as the new standby host.



### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



### Perform post-deployment tasks

Before you use your SAP HANA system, Google Cloud recommends that you perform the following post-deployment tasks:

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser.

  2. Update the SAP HANA software with the latest patches.

  3. If your SAP HANA system is deployed on a VirtIO network interface, then we recommend that you ensure the value of the TCP parameter `/proc/sys/net/ipv4/tcp_limit_output_bytes` is set to `1048576`. This modification helps improve the overall network throughput on the VirtIO network interface without affecting the network latency. 

  4. Install any additional components such as Application Function Libraries (AFL) or Smart Data Access (SDA).

  5. If you are upgrading an existing SAP HANA system, then load the data from the existing system either by using standard backup and restore procedures or by using SAP HANA system replication.

  6. Configure and back up your new SAP HANA database. For more information, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).




For more information about these tasks, see [SAP HANA server installation and update guide](https://help.sap.com/viewer/2c1988d620e04368aa4103bf26f17727/LATEST/en-US/7eb0167eb35e4e2885415205b8383584.html).

## What's next

  * To operate SAP HANA, or the underlying compute instances, see [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide).
  * Automate continuous validation checks for your SAP HANA scale-out system by using Workload Manager. For more information, see [About Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).
  * Set up observability for your SAP HANA to improve by using Workload Manager. For more information, see [SAP observability overview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
