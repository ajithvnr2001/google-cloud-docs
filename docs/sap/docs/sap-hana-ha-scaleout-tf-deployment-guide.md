---
url: https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-tf-deployment-guide/
title: Terraform: SAP HANA scale-out system with host auto-failover deployment guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:39.924096+00:00
---

# Terraform: SAP HANA scale-out system with host auto-failover deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-tf-deployment-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Terraform: SAP HANA scale-out system with host auto-failover deployment guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to use [Terraform](https://docs.cloud.google.com/docs/terraform) to deploy an SAP HANA scale-out system that includes the SAP HANA host auto-failover fault-recovery solution. By using Terraform, you can deploy a system that meets SAP support requirements and adheres to both SAP and Compute Engine best practices.

The resulting SAP HANA system includes a master host, up to 15 worker hosts, and up to 3 standby hosts all within a single Compute Engine zone.

The system also includes the Google Cloud storage manager for SAP HANA standby nodes (storage manager for SAP HANA), which manages the transfer of storage devices to the standby node during a failover. The storage manager for SAP HANA is installed in the SAP HANA `/shared` volume. For information about the storage manager for SAP HANA and required IAM permissions, see [The storage manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).

For more information from SAP about the host auto-failover solution, see [Host Auto-Failover](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/ae60cab98173431c97e8724856641207.html)

Do not use this guide if you do not need the host auto-failover feature. Instead, use the [Terraform: SAP HANA deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf).

If you need to deploy SAP HANA in a Linux high-availability cluster, use one of the following guides:

  * The [Terraform: SAP HANA HA cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment)
  * The [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * The [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)



This guide is intended for advanced SAP HANA users who are familiar with SAP scale-out configurations that include standby hosts for high-availability, as well as network file systems.

## Prerequisites

Before you create the SAP HANA high availability scale-out system, make sure that the following prerequisites are met:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide) and the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide). 
  * You or your organization has a Google Cloud account and you have created a project for the SAP HANA deployment. For information about creating Google Cloud accounts and projects, see [Setting up your Google account](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#setting-up-your-google-account) in the SAP HANA Deployment Guide.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * The SAP HANA installation media is stored in a Cloud Storage bucket that is available in your deployment project and region. For information about how to upload SAP HANA installation media to a Cloud Storage bucket, see [Creating a Cloud Storage bucket](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#creating_a_cloud_storage_bucket_for_the_sap_hana_installation_files). in the SAP HANA Deployment Guide.
  * You have an NFS solution, such as the managed [Filestore](https://docs.cloud.google.com/filestore) solution, for sharing the SAP HANA `/hana/shared` and `/hanabackup` volumes among the hosts in the scale-out SAP HANA system. You specify the mount points for the NFS servers in the Terraform configuration file before you can deploy the system. To deploy Filestore NFS servers, see [Creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * Communication must be allowed between all VMs in the SAP HANA subnetwork that host an SAP HANA scale-out node.

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

By default, an _implied firewall rule_ blocks incoming connections from outside your Virtual Private Cloud (VPC) network. To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.
  * Communication between VMs in the SAP HANA subnetwork, including communication between nodes in an SAP HANA scale-out system or communication between the database server and application servers in a 3-tier architecture. You can enable communication between VMs by creating a firewall rule to allow traffic that originates from within the subnetwork.



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

## Creating an SAP HANA scale-out system with standby hosts

In the following instructions, you complete the following actions:

  * Create the SAP HANA system by invoking Terraform with a configuration file that you complete.
  * Verify deployment.
  * Test the standby host(s) by simulating a host failure.



Some of the steps in the following instructions use Cloud Shell to enter the `gcloud` commands. If you have the latest version of Google Cloud SDK installed, you can enter the `gcloud` commands from a local terminal instead.

### Define and create the SAP HANA system

In the following steps, you download and complete a Terraform configuration file, use the standard Terraform commands to initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud, and apply the configuration, which deploys the VMs, persistent disks, and SAP HANA instances.

  1. Confirm that your current quotas for project resources, such as persistent disks and CPUs, are sufficient for the SAP HANA system you are about to install. If your quotas are insufficient, deployment fails. For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to the quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `sap_hana_scaleout.tf` configuration file for the SAP HANA high-availability scale-out system to your working directory:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_scaleout/terraform/sap_hana_scaleout.tf

**Note:** Ensure that you have only a single Terraform configuration file in your working directory.
  4. Open the `sap_hana_scaleout.tf` file in the Cloud Shell code editor.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  5. In the `sap_hana_scaleout.tf` file, update the following argument values by replacing the contents inside the double quotation marks with the values for your installation. For example, you might replace "ZONE" with "us-central1-f".

Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `sap_hana_scaleout.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`zone` | String | Specify the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which you are deploying your SAP system. The zone must be in the same region that you selected for your subnet. For example, if your subnet is deployed in the `us-central1` region, then you can specify a zone such as `us-central1-a`.  
`machine_type` | String |  Specify the type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms) (VM) on which you need to run your SAP system. If you need a custom VM type, then specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations). For example, `n1-highmem-32`.  
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `rhel-9-2-sap-ha` or `sles-15-sp5-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify either `rhel-sap-cloud` or `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`instance_name` | String | Specify a name for the compute instance that Terraform deploys to run your SAP HANA workload. The name can contain lowercase letters, numbers, and hyphens. Terraform also uses this value to name the compute instances that it deploys to run the worker and standby nodes. To help you identify these compute instances, Terraform appends their names with the letter `w` and an index. For example, if you set `instance_name = "my-instance"` and choose to deploy 2 worker nodes and 1 standby node, then the compute instance names are set as follows:
     * `my-instance` is the name of the compute instance that runs the master node
     * `my-instancew1` and `my-instancew2` are the names of the compute instances that run the worker nodes
     * `my-instancew3` is the name of the compute instance that runs the standby node  
`sap_hana_shared_nfs` | String |  Specify the NFS mount point for the `/hana/shared` volume. For example, `10.151.91.122:/hana_shared_nfs`. **Note** : The NFS mount point for the `/hana/shared` volume must be empty before you apply the Terraform configuration.  
`sap_hana_backup_nfs` | String |  Specify the NFS mount point for the `/hanabackup` volume. For example, `10.216.41.122:/hana_backup_nfs`.   
`sap_hana_deployment_bucket` | String | To automatically install SAP HANA on the deployed VMs, specify the path of the Cloud Storage bucket that contains the SAP HANA installation files. Don't include `gs://` in the path; include only the bucket name and the names of any folders. For example, `my-bucket-name/my-folder`. The Cloud Storage bucket must exist in the Google Cloud project that you specify for the `project_id` argument.  
`sap_hana_sid` | String | To automatically install SAP HANA on the deployed VMs, specify the SAP HANA system ID. The ID must consist of three alpha-numeric characters and begin with a letter. All letters must be in uppercase. For example, `HS4`.   
`sap_hana_instance_number` | Integer | Optional. Specify the instance number, 0 to 99, of the SAP HANA system. The default is `0`.  
`sap_hana_sidadm_password` | String | To automatically install SAP HANA on the deployed VMs, specify a temporary `SIDadm` password for the installation scripts to use during deployment. The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and a number. **Important:** After the installation is complete, make sure to change the password.  Instead of specifying password as plain text, we recommend that you use a secret. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_sidadm_password_secret` | String | Optional. If you are using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the `SIDadm` password, then specify the **Name** of the secret that corresponds to this password. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the Google Cloud project that you specify for the `project_id` argument. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_system_password` | String | To automatically install SAP HANA on the deployed VMs, specify a temporary database superuser password for the installation scripts to use during deployment. The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and a number. **Important** : After the installation is complete, make sure to change the password.  Instead of specifying password as plain text, we recommend that you use a secret. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_system_password_secret` | String | Optional. If you are using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the database superuser password, then specify the **Name** of the secret that corresponds to this password. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the Google Cloud project that you specify for the `project_id` argument. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_double_volume_size` | Boolean | Optional. To double the HANA volume size, specify `true`. This argument is useful when you want to deploy multiple SAP HANA instances or a disaster-recovery SAP HANA instance on the same VM. By default, the volume size is automatically calculated to be the minimum size required for the size of your VM, while still meeting the SAP certification and support requirements. The default value is `false`.   
`configure_backint` | Boolean |  Optional. To use Backint based backup and recovery for your SAP HANA deployment, do the following:
     * Specify the argument `configure_backint` with the value `true`.
     * Specify the argument `backint_gcs_bucket` with the name of the Cloud Storage bucket where you want to store your database backups.
When you specify these arguments, Terraform enables the Backint feature in the instances of Google Cloud's Agent for SAP in your SAP HANA deployment. For information about Backint based backup and recovery, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). The default value of this argument is `false`. This argument is available in `sap_hana_scaleout` module version `1.5.807307812` or later.  
`backint_gcs_bucket` | String |  Optional. To use Backint based backup and recovery for your SAP HANA deployment, do the following:
     * Specify the argument `backint_gcs_bucket` with the name of the Cloud Storage bucket where you want to store your database backups. Don't include `gs://` in the value; include only the bucket name and the names of any folders. For example, `my-bucket/my-folder`.
     * Specify the argument `configure_backint` with the value `true`.
When you specify these arguments, Terraform enables the Backint feature in the instances of Google Cloud's Agent for SAP in your SAP HANA deployment. For information about Backint based backup and recovery, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). This argument is available in `sap_hana_scaleout` module version `1.5.807307812` or later.  
`sap_hana_sidadm_uid` | Integer | Optional. Specify a value to override the default value of the SID_LCadm user ID. The default value is `900`. You can change this to a different value for consistency within your SAP landscape.   
`sap_hana_sapsys_gid` | Integer | Optional. Overrides the default group ID for `sapsys`. The default value is `79`.   
`sap_hana_worker_nodes` | Integer | Specify the number of additional SAP HANA worker hosts that you need. You can specify 1 to 15 worker hosts. The default value is 1.  
`sap_hana_standby_nodes` | Integer | Specify the number of additional SAP HANA standby hosts that you need. You can specify 1 to 3 standby hosts. The default value is 1.   
`sap_hana_volume_encryption` | String |  Optional. During the installation of SAP HANA, if you want to enable the [ data and log volume encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/dc01f36fbb5710148b668201a6e95cf2.html), then specify this argument with the value `on`. The default value of this argument depends on the version of SAP HANA you're installing:
     * For SAP HANA 2.0 SPS 07 or later, the default value for this argument is `on`.
     * For SAP HANA 2.0 SPS 06 or earlier, the default value for this argument is `off`.  
`sap_hana_backup_encryption` | String |  Optional. During the installation of SAP HANA, if you want to enable the [backup encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/e5c51c31ecaf4b7188a76776ba3c0797.html), then specify this argument with the value `on`. The default value of this argument depends on the version of SAP HANA you're installing:
     * For SAP HANA 2.0 SPS 07 or later, the default value for this argument is `on`.
     * For SAP HANA 2.0 SPS 06 or earlier, the default value for this argument is `off`.  
`network_tags` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for firewall or routing purposes.  If you specify `public_ip = false` and don't specify a network tag, then make sure to provide another means of access to the internet.   
`disk_type` | String | Optional. Specify the default type of Persistent Disk or Hyperdisk volume that you want to deploy for the `/hana/data`, `/hana/log`, and `/usr/sap` directories in your deployment. For information about the default disk deployment performed by the Terraform configurations provided by Google Cloud, see [ Disk deployment by Terraform](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#disk-deployment-by-terraform). The following are valid values for this argument: `hyperdisk-extreme`, `hyperdisk-balanced`, `pd-ssd`, `pd-balanced`, and `pd-extreme`.  You can override this default disk type and the associated default disk size and default IOPS using some advanced arguments. For more information, navigate to your working directory, then run the `terraform init` command, and then see the `/.terraform/modules/sap_hana_scaleout/variables.tf` file. Before you use these arguments in production, make sure to test them in a non-production environment.  If you want to use [SAP HANA Native Storage Extension](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/4efaa94f8057425c8c7021da6fc2ddf5.html) (NSE), then you need to provision larger disks by using the advanced arguments.  
`use_single_shared_data_log_disk` | Boolean | Optional. The default value is `false`, which directs Terraform to deploy a separate persistent disk or Hyperdisk for each of the following SAP volumes: `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap`. To mount these SAP volumes on the same persistent disk or Hyperdisk, specify `true`.   
`public_ip` | Boolean |  Optional. Determines whether or not a public IP address is added to your VM instance. The default value is `true`. **Caution:** don't specify `false` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`service_account` | String | Optional. Specify the email address of a user-managed service account to be used by the host VMs and by the programs that run on the host VMs. For example, `svc-acct-name@project-id.iam.gserviceaccount.com`.  If you specify this argument without a value, or omit it, then the installation script uses the Compute Engine default service account. For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).   
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
  
The following example shows a completed configuration file that deploys an SAP HANA scale-out system with three worker hosts and one standby host in the `us-central1-f` zone. Each host is installed on an `n2-highmem-32` VM that is running a Linux operating system provided by a Compute Engine public image. The NFS volumes are provided by Filestore. Temporary passwords are used during deployment and configuration processing only.

For clarity, comments in the configuration file are omitted in the example.
    
    # ...
    module "hana_scaleout" {
    source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_scaleout/sap_hana_scaleout_module.zip"
    #
    # By default, this source file uses the latest release of the terraform module
    # for SAP on Google Cloud. To fix your deployments to a specific release
    # of the module, comment out the source property above and uncomment the source property below.
    #
    # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/YYYYMMDDHHMM/terraform/sap_hana_scaleout/sap_hana_scaleout_module.zip"
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
    sap_hana_shared_nfs = "10.74.146.58:/hana_shr"
    sap_hana_backup_nfs = "10.188.249.170:/hana_bup"
    # ...
    sap_hana_deployment_bucket = "installables/hana2-sp5-rev53"
    sap_hana_sid = "HS4"
    sap_hana_instance_number = 11
    sap_hana_sidadm_password = "TempPa55word"
    sap_hana_system_password = "TempPa55word"
    # ...
    sap_hana_worker_nodes = 3
    sap_hana_standby_nodes = 1
    vm_static_ip = "10.0.0.1"
    worker_static_ips = ["10.0.0.2", "10.0.0.3", "10.0.0.4"]
    standby_static_ips = ["10.0.0.5"]
    # ...
    }

  6. Initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud:
         
         terraform init

The `terraform init` command prepares your working directory for other Terraform commands.

To force a refresh of the provider plugin and configuration files in your working directory, specify the `--upgrade` flag. If the `--upgrade` flag is omitted and you don't make any changes in your working directory, Terraform uses the locally cached copies, even if `latest` is specified in the `source` URL.

  7. Optionally, create the Terraform execution plan:
         
         terraform plan

The `terraform plan` command shows the changes required by your current configuration. If you skip this step, the `terraform apply` command automatically creates a new plan and prompts you to approve it.

  8. Apply the execution plan:
         
         terraform apply

When you are prompted to approve the actions, enter `yes`.

The `terraform apply` command sets up the Google Cloud infrastructure. When the Compute Engine machine boots, the Google Cloud infrastructure invokes startup scripts that configure the operating system and install SAP HANA.

While Terraform has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the Logging logs.

Time to completion can vary, but the entire process usually takes 45 minutes to 1 hour.




## Verifying the deployment

To verify deployment, you check the deployment logs in Cloud Logging, check the disks and services on the VMs of the primary and worker hosts, display the system in SAP HANA Studio, and test the takeover by a standby host.

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




### Connect to the VMs to check the disks and SAP HANA services

After deployment is complete, confirm that the disks and SAP HANA services have deployed properly by checking the disks and services of the master host and one worker host.

  1. On the Compute Engine **VM instances** page, connect to the compute instance that runs the master host and a worker host of your SAP HANA instance. You can click the **SSH** button available against each compute instance, of you can choose your preferred SSH method.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

When connecting to the worker host, make sure that you aren't connecting to a standby host. The standby hosts use the same naming convention as the worker hosts, but have the highest numbered worker-host suffix before the first takeover. For example, if you have three worker hosts and one standby host, before the first takeover the standby host has a suffix of "w4".

  2. In each terminal window, switch to the root user:
         
         sudo su -

  3. In each terminal window, display information about the disk file system:
         
         df -h

On the master host, your output is similar to the following example:
         
         hana-scaleout-w-failover:~ # df -h
         hana-scaleout-w-failover:~ # su - hs4adm
         Filesystem                         Size  Used Avail Use% Mounted on
         /dev/sda3                           45G  7.2G   38G  16% /
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         tmpfs                              154G     0  154G   0% /dev/shm
         efivarfs                           256K   27K  225K  11% /sys/firmware/efi/efivars
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
         /dev/mapper/vg_hana_data-data      414G   19G  396G   5% /hana/data/HS4/mnt00001
         /dev/mapper/vg_hana_log-log        104G  9.2G   95G   9% /hana/log/HS4/mnt00001
         tmpfs                               21G  8.0K   21G   1% /run/user/471
         10.55.104.130:/hana_backup         1.0T     0  1.0T   0% /hanabackup
         tmpfs                               21G  8.0K   21G   1% /run/user/101
         tmpfs                               21G  8.0K   21G   1% /run/user/1000

On a worker host, notice that the `/hana/data` and `/hana/log` directories have different mounts:
         
         hana-scaleout-w-failoverw1:~ # df -h
         Filesystem                         Size  Used Avail Use% Mounted on
         /dev/sda3                           45G  7.2G   38G  16% /
         devtmpfs                           4.0M  8.0K  4.0M   1% /dev
         tmpfs                              154G     0  154G   0% /dev/shm
         efivarfs                           256K   27K  225K  11% /sys/firmware/efi/efivars
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
         /dev/mapper/vg_hana_data-data      414G  8.1G  406G   2% /hana/data/HS4/mnt00002
         /dev/mapper/vg_hana_log-log        104G  5.1G   99G   5% /hana/log/HS4/mnt00002
         tmpfs                               21G  8.0K   21G   1% /run/user/1000

On a standby host, the `/hana/data` and `/hana/log` directories are not mounted until the standby host takes over for a failed host:
         
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
         0.142.81.194:/hana_shared         1.0T   62G  963G   7% /hana/shared
         tmpfs                               21G  8.0K   21G   1% /run/user/0
         10.55.104.130:/hana_backup         1.0T     0  1.0T   0% /hanabackup
         tmpfs                               21G  8.0K   21G   1% /run/user/101
         tmpfs                               21G  8.0K   21G   1% /run/user/1000

  4. In each terminal window, switch to the `SID_LCadm` user:
         
         su - SID_LCadm

Replace SID_LC with the value you specified for the `sap_hana_sid` argument in your Terraform configuration file. The SID_LC value must be in lowercase. In the example configuration shown in a preceding step, the SID is `HS4`.

  5. In each terminal window, verify that SAP HANA services such as `hdbnameserver`, `hdbindexserver`, and others, are running on the compute instance:
         
         HDB info

On the master host, your output is similar to the following truncated example:
         
         hana-scaleout-w-failover:~ # su - hs4adm
         hs4adm@hana-scaleout-w-failover:/usr/sap/HS4/HDB15> HDB info
         USER          PID     PPID  %CPU        VSZ        RSS COMMAND
         hs4adm     310795   310793   1.1       9640       5632 -sh
         hs4adm     310913   310795   2.1       5052       3584  \_ /bin/sh /usr/sap/HS4/HDB15/HDB info
         hs4adm     310948   310913  18.1       7976       3072      \_ ps fx -U hs4adm -o user:8,pid:8,ppid:8,pcpu:5,vsz:10,rss:10,args
         hs4adm      23943        1   0.0       9440       3124 sapstart pf=/hana/shared/HS4/profile/HS4_HDB15_hana-scaleout-w-failover
         hs4adm      23950    23943   0.0     455548      86688  \_ /usr/sap/HS4/HDB15/hana-scaleout-w-failover/trace/hdb.sapHS4_HDB15 -d -nw -f /usr/sap/HS4/HDB15/hsfai
         hs4adm      23972    23950   2.6    9974768    4227280      \_ hdbnameserver
         hs4adm      24635    23950   0.6    4623364     230308      \_ hdbcompileserver
         hs4adm      24638    23950   0.7    4870844     260244      \_ hdbpreprocessor
         hs4adm      24676    23950   5.6    9982012    5950880      \_ hdbindexserver -port 31503
         hs4adm      24679    23950   1.6    8156876    1702172      \_ hdbxsengine -port 31507
         hs4adm      25013    23950   0.6    6809528     553128      \_ hdbwebdispatcher
         hs4adm      14772        1   0.0     576236      39120 hdbrsutil  --start --port 31503 --volume 3 --volumesuffix mnt00001/hdb00003.00003 --identif
         hs4adm      14180        1   0.0     576168      38792 hdbrsutil  --start --port 31501 --volume 1 --volumesuffix mnt00001/hdb00001 --identifier 17
         hs4adm      13744        1   0.0     544304      31472 /usr/sap/HS4/HDB15/exe/sapstartsrv pf=/hana/shared/HS4/profile/HS4_HDB15_hana-scaleout-w-failover -D -u h
         hs4adm      13663        1   0.0      29812      11776 /usr/lib/systemd/systemd --user
         hs4adm      13664    13663   0.0      39948       6236  \_ (sd-pam)

On a worker host, you output is similar to the following truncated example:
         
         hana-scaleout-w-failoverw1:~ # su - hs4adm
         hs4adm@hana-scaleout-w-failoverw1:/usr/sap/HS4/HDB15> HDB info
         USER          PID     PPID  %CPU        VSZ        RSS COMMAND
         hs4adm     299569   299568   0.7       9640       5632 -sh
         hs4adm     299631   299569   0.0       5056       3584  \_ /bin/sh /usr/sap/HS4/HDB15/HDB info
         hs4adm     299666   299631   8.3       7976       3072      \_ ps fx -U hs4adm -o user:8,pid:8,ppid:8,pcpu:5,vsz:10,rss:10,args
         hs4adm      15776        1   0.0       9444       3100 sapstart pf=/hana/shared/HS4/profile/HS4_HDB15_hana-scaleout-w-failoverw1
         hs4adm      15783    15776   0.0     456552      86892  \_ /usr/sap/HS4/HDB15/hana-scaleout-w-failoverw1/trace/hdb.sapHS4_HDB15 -d -nw -f /usr/sap/HS4/HDB15/hana-scaleout-w-failoverw1/daemon
         hs4adm      15805    15783   0.8    7712788     809548      \_ hdbnameserver
         hs4adm      16701    15783   0.6    4623364     224252      \_ hdbcompileserver
         hs4adm      16704    15783   0.6    4870844     255472      \_ hdbpreprocessor
         hs4adm      16794    15783   2.4    8478348    1870872      \_ hdbindexserver -port 31503
         hs4adm      17035    15783   0.6    6808236     546852      \_ hdbwebdispatcher
         hs4adm      14101        1   0.0     510732      39124 hdbrsutil  --start --port 31503 --volume 4 --volumesuffix mnt00002/hdb00004.00003 --identifier 1781134788
         hs4adm      13423        1   0.0     478240      31292 /hana/shared/HS4/HDB15/exe/sapstartsrv pf=/hana/shared/HS4/profile/HS4_HDB15_hana-scaleout-w-failoverw1 -D -u hs4adm

On a standby host, your output is similar to the following truncated example:
         
         hana-scaleout-w-failoverw4:~ # su - hs4adm
         hs4adm@hana-scaleout-w-failoverw4:/usr/sap/HS4/HDB15> HDB info
         USER          PID     PPID  %CPU        VSZ        RSS COMMAND
         hs4adm     295258   295257   0.6       9640       5376 -sh
         hs4adm     295320   295258   1.8       5056       3328  \_ /bin/sh /usr/sap/HS4/HDB15/HDB info
         hs4adm     295355   295320   6.6       7976       3072      \_ ps fx -U hs4adm -o user:8,pid:8,ppid:8,pcpu:5,vsz:10,rss:10,args
         hs4adm      13819        1   0.0       9440       3120 sapstart pf=/hana/shared/HS4/profile/HS4_HDB15_hana-scaleout-w-failoverw4
         hs4adm      13826    13819   0.0     456532      87172  \_ /usr/sap/HS4/HDB15/hana-scaleout-w-failoverw4/trace/hdb.sapHS4_HDB15 -d -nw -f /usr/sap/HS4/HDB15/hana-scaleout-w-failoverw4/daemon.ini pf=/usr
         hs4adm      13849    13826   0.8    7711492     753872      \_ hdbnameserver
         hs4adm      14173    13826   0.6    4622076     210084      \_ hdbcompileserver
         hs4adm      14176    13826   0.6    4869556     245600      \_ hdbpreprocessor
         hs4adm      14211    13826   0.6    6806944     533604      \_ hdbwebdispatcher
         hs4adm      13120        1   0.0     610344      31788 /hana/shared/HS4/HDB15/exe/sapstartsrv pf=/hana/shared/HS4/profile/HS4_HDB15_hana-scaleout-w-failoverw4 -D -u hs4adm

  6. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




### Connect SAP HANA Studio

  1. Connect to the master SAP HANA host from SAP HANA Studio.

You can connect from an instance of SAP HANA Studio that is outside of Google Cloud or from an instance on Google Cloud. You might need to enable network access between the target VMs and SAP HANA Studio.

To use SAP HANA Studio on Google Cloud and enable access to the SAP HANA system, see [Installing SAP HANA Studio on a Compute Engine Windows VM](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#install_hana_studio).

  2. In SAP HANA Studio, click the **Landscape** tab on the default system administration panel. You should see a display similar to the following example.

![Screenshot of the Landscape view in SAP HANA Studio](https://docs.cloud.google.com/static/sap/docs/images/hana-studio-scaleout-landscape.png)




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




### Performing a failover test

After you have confirmed that the SAP HANA system deployed successfully, test the failover function.

The following instructions trigger a failover by switching to the SAP HANA operating system user and entering the `HDB stop` command. The `HDB stop` command initiates a graceful shutdown of SAP HANA and detaches the disks from the host, which enables a relatively quick failover.

**Note:** To simulate a failure of the entire VM, you can enter `sudo ip link set eth0 down` command. The `ip link set eth0 down` command shuts down the network interface to the VM. Failover in this case takes longer, because the system performs additional processing to confirm that the host is down and to move the disks.

To perform a failover test:

  1. Connect to the VM of a worker host by using SSH. You can connect from the Compute Engine **VM instances** page by clicking the SSH button for each VM instance, or you can use your preferred SSH method.

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

Your output is similar to the following. Note that the `/hana/data` and `/hana/log` directories from the failed host are now mounted to the host that took over.
         
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

  3. If your SAP HANA system is deployed on a VirtIO network interface, then we recommend that you ensure the value of the TCP parameter `/proc/sys/net/ipv4/tcp_limit_output_bytes` is set to `1048576`. This modification helps improve the overall network throughput on the VirtIO network interface without affecting the network latency. 

  4. Install any additional components such as Application Function Libraries (AFL) or Smart Data Access (SDA).

  5. If you are upgrading an existing SAP HANA system, load the data from the existing system either by using standard backup and restore procedures or by using SAP HANA system replication.

  6. Configure and backup your new SAP HANA database. For more information, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).




## Evaluate your SAP HANA workload

To automate continuous validation checks for your SAP HANA workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager allows you to automatically scan and evaluate your SAP HANA workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP HANA workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## What's next

  * If you need to use Google Cloud NetApp Volumes instead of Persistent Disk or Hyperdisk volumes to host SAP HANA directories such as `/hana/shared` or `/hanabackup`, see the NetApp Volumes deployment information in the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#netapp_cvs).
  * For more information about VM administration of and monitoring, see the [SAP HANA Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
