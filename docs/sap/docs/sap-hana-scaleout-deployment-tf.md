---
url: https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-deployment-tf/
title: Terraform: SAP HANA multi-host scale-out deployment guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:39.093997+00:00
---

# Terraform: SAP HANA multi-host scale-out deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-deployment-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Terraform: SAP HANA multi-host scale-out deployment guide Stay organized with collections  Save and categorize content based on your preferences. 

This deployment guide shows you how to deploy an SAP HANA multi-host scale-out system on Google Cloud by using [Terraform](https://docs.cloud.google.com/docs/terraform) and a configuration file to define your installation. The guide helps you configure Compute Engine virtual machines (VMs) and persistent disks, as well as the Linux operating system, to achieve the best performance for your SAP HANA system. The Terraform configuration file incorporates best practices from both Compute Engine and SAP. 

If you need to include SAP HANA automatic host failover, then use the [Terraform: SAP HANA scale-out system with host auto-failover deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-tf-deployment-guide) instead.

If you need to deploy SAP HANA in a Linux high-availability cluster, use one of the following guides:

  * [Terraform: SAP HANA high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment)
  * The [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * The [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)



## Before you begin

Before you begin, make sure that you meet the following prerequisites:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide). 
  * You have a Google Cloud account and project.
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * Virtual Private Cloud networking is set up with firewall rules or other methods to control access to your compute instances.
  * You have access to the SAP HANA installation media.
  * Ensure that the terminal that you're using has the gcloud CLI and Terraform CLI installed. For more information about how to install Terraform CLI, see [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata and you are deploying scale-out nodes, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules. If you use the Terraform configuration file that Google Cloud provides, specify a tag with `network_tags = "TAG"`.
    * Create the VMs without an external IP. If you use the Terraform configuration file that Google Cloud provides, specify `public_ip = false`.



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

To create a VPC network for your project, complete the following steps:

  1. Create a custom mode network. For more information, see [Creating a custom mode network](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_1).

  2. Create a subnetwork, and specify the region and IP range. For more information, see [Adding subnets](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_2).




### Setting up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#terraform).

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



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

### Creating a Cloud Storage bucket for the SAP HANA installation files

Before you use Terraform to install SAP HANA on your Compute Engine VM, you must upload the installation files that contain the SAP HANA binaries to a Cloud Storage bucket.

Terraform expects the SAP HANA installation files in the file formats provided by SAP. Depending on your version of SAP HANA, the file format might be ZIP, EXE, or RAR. 

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




## Create compute instances with SAP HANA installed

The following instructions use Terraform to install SAP HANA on one or more VM instances with all of the persistent disks that SAP HANA requires. You define the values for the installation in a Terraform configuration file.

The following instructions use Cloud Shell, but are generally applicable to the Google Cloud CLI.

  1. Confirm that your current quotas for resources such as persistent disks and CPUs are sufficient for the SAP HANA system you are about to install. If your quotas are insufficient, deployment fails. For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. Open the Cloud Shell or, if you installed the Google Cloud CLI on your local workstation, open a terminal.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `sap_hana.tf` configuration file to your working directory by running the following command in the Cloud Shell or your terminal:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana/terraform/sap_hana.tf

**Note:** Ensure that you have only a single Terraform configuration file in your working directory.
  4. Open the `sap_hana.tf` file in Cloud Shell code editor or, if you are using your terminal, the text editor of your choice.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  5. In the `sap_hana.tf` file, update the following argument values by replacing the brackets and their contents with the values for your installation.

Some of the argument values that you specify for the SAP HANA system, such as values for `sap_hana_sid`, `sap_hana_sidadm_password`, or `sap_hana_system_password`, are subject to rules that are defined by SAP. For more information, see the Parameter Reference in the [SAP HANA Server Installation and Update Guide](https://help.sap.com/viewer/2c1988d620e04368aa4103bf26f17727/LATEST/en-US).

To specify passwords in the configuration file, you must either use secrets or, specify passwords in plain text. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).

If you want to create a VM instance without installing SAP HANA, then delete all of the lines that begin with `sap_hana_`.

Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `sap_hana.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`instance_name` | String | Specify a name for the compute instance that Terraform deploys to run your SAP HANA workload. The name can contain lowercase letters, numbers, and hyphens. Terraform also uses this value to name the compute instances that it deploys to run the worker and standby nodes. To help you identify these compute instances, Terraform appends their names with the letter `w` and an index. For example, if you set `instance_name = "my-instance"` and choose to deploy 2 worker nodes and 1 standby node, then the compute instance names are set as follows:
     * `my-instance` is the name of the compute instance that runs the master node
     * `my-instancew1` and `my-instancew2` are the names of the compute instances that run the worker nodes
     * `my-instancew3` is the name of the compute instance that runs the standby node  
`machine_type` | String |  Specify the type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms) (VM) on which you need to run your SAP system. If you need a custom VM type, then specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations). For example, `n1-highmem-32`.  
`zone` | String | Specify the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which you are deploying your SAP system. The zone must be in the same region that you selected for your subnet. For example, if your subnet is deployed in the `us-central1` region, then you can specify a zone such as `us-central1-a`.  
`sole_tenant_deployment` | Boolean |  Optional. If you want to provision a [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) for your SAP HANA deployment, then specify the value `true`. The default value is `false`. This argument is available in `sap_hana` module version `1.3.704310921` or later.   
`sole_tenant_name_prefix` | String |  Optional. If you're provisioning a sole-tenant node for your SAP HANA deployment, then you can use this argument to specify a prefix that Terraform sets for the names of the corresponding sole tenant template and sole tenant group. The default value is `st-SID_LC`. For information about sole tenant template and sole tenant group, see [Sole tenancy overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes). This argument is available in `sap_hana` module version `1.3.704310921` or later.   
`sole_tenant_node_type` | String |  Optional. If you want to provision a sole-tenant node for your SAP HANA deployment, then specify the [node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) that you want to set for the corresponding node template. This argument is available in `sap_hana` module version `1.3.704310921` or later.   
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `rhel-9-2-sap-ha` or `sles-15-sp5-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify either `rhel-sap-cloud` or `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`sap_hana_deployment_bucket` | String | To automatically install SAP HANA on the deployed VMs, specify the path of the Cloud Storage bucket that contains the SAP HANA installation files. Don't include `gs://` in the path; include only the bucket name and the names of any folders. For example, `my-bucket-name/my-folder`. The Cloud Storage bucket must exist in the Google Cloud project that you specify for the `project_id` argument.  
`sap_hana_sid` | String | To automatically install SAP HANA on the deployed VMs, specify the SAP HANA system ID. The ID must consist of three alpha-numeric characters and begin with a letter. All letters must be in uppercase. For example, `HS4`.   
`sap_hana_sidadm_uid` | Integer | Optional. Specify a value to override the default value of the SID_LCadm user ID. The default value is `900`. You can change this to a different value for consistency within your SAP landscape.   
`sap_hana_instance_number` | Integer | Optional. Specify the instance number, 0 to 99, of the SAP HANA system. The default is `0`.  
`sap_hana_sidadm_password` | String | To automatically install SAP HANA on the deployed VMs, specify a temporary `SIDadm` password for the installation scripts to use during deployment. The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and a number. **Important:** After the installation is complete, make sure to change the password.  Instead of specifying password as plain text, we recommend that you use a secret. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_sidadm_password_secret` | String | Optional. If you are using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the `SIDadm` password, then specify the **Name** of the secret that corresponds to this password. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the Google Cloud project that you specify for the `project_id` argument. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_system_password` | String | To automatically install SAP HANA on the deployed VMs, specify a temporary database superuser password for the installation scripts to use during deployment. The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and a number. **Important** : After the installation is complete, make sure to change the password.  Instead of specifying password as plain text, we recommend that you use a secret. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_system_password_secret` | String | Optional. If you are using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the database superuser password, then specify the **Name** of the secret that corresponds to this password. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the Google Cloud project that you specify for the `project_id` argument. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_scaleout_nodes` | Integer | Specify the number of worker hosts that you need in your scale-out system. To deploy a scale-out system, you need at least one worker host. Terraform creates the worker hosts in addition to the primary SAP HANA instance. For example, if you specify `3`, then four SAP HANA instances are deployed in your scale-out system.  
`sap_hana_shared_nfs` | String |  Optional. For a multi-host scale-out deployment that uses an NFS solution to share the `/hana/shared` volume with the worker hosts, specify the NFS mount point for that volume. For example, `10.151.91.122:/hana_shared_nfs`.  For more information, see [File sharing solutions for multi-host scale-out deployments](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#file_sharing_for_hana_scale_out).  This argument is available in `sap_hana` module version `202302060649` or later. **Note** : The NFS mount point for the `/hana/shared` volume must be empty before you apply the Terraform configuration.  
`sap_hana_backup_nfs` | String |  Optional. For a multi-host scale-out deployment that uses an NFS solution to share the `/hanabackup` volume with the worker hosts, specify the NFS mount point for that volume. For example, `10.216.41.122:/hana_backup_nfs`.  For more information, see [File sharing solutions for multi-host scale-out deployments](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#file_sharing_for_hana_scale_out).  This argument is available in `sap_hana` module version `202302060649` or later.   
`sap_hana_shared_nfs_resource` | Map/Object |  Optional. To deploy a Filestore instance that shares the `/hana/shared/` volume with the hosts in your multi-host scale-out SAP HANA system, specify the name of the file share that you set in the definition of your [`google_filestore_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/filestore_instance#argument-reference). To view an example, see the sample configuration in this guide.  For more information, see [File sharing solutions for multi-host scale-out deployments](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#file_sharing_for_hana_scale_out).  This argument is available in `sap_hana` module version `202302060649` or later.   
`sap_hana_backup_nfs_resource` | Map/Object |  Optional. To deploy a Filestore instance that shares the `/hanabackup` volume with the hosts in your multi-host scale-out SAP HANA system, specify the name of the file share that you set in the definition of your [`google_filestore_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/filestore_instance#argument-reference). To view an example, see the sample configuration in this guide.  For more information, see [File sharing solutions for multi-host scale-out deployments](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#file_sharing_for_hana_scale_out).  This argument is available in `sap_hana` module version `202302060649` or later.   
`configure_backint` | Boolean |  Optional. To use Backint based backup and recovery for your SAP HANA deployment, do the following:
     * Specify the argument `configure_backint` with the value `true`.
     * Specify the argument `backint_gcs_bucket` with the name of the Cloud Storage bucket where you want to store your database backups.
When you specify these arguments, Terraform enables the Backint feature in the instances of Google Cloud's Agent for SAP in your SAP HANA deployment. For information about Backint based backup and recovery, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). The default value of this argument is `false`. This argument is available in `sap_hana` module version `1.5.807307812` or later. You can use only one backup option in your Terraform configuration - Backint or disk based backup. For more information, see [Backup management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#backup_management).  
`backint_gcs_bucket` | String |  Optional. To use Backint based backup and recovery for your SAP HANA deployment, do the following:
     * Specify the argument `backint_gcs_bucket` with the name of the Cloud Storage bucket where you want to store your database backups. Don't include `gs://` in the value; include only the bucket name and the names of any folders. For example, `my-bucket/my-folder`.
     * Specify the argument `configure_backint` with the value `true`.
When you specify these arguments, Terraform enables the Backint feature in the instances of Google Cloud's Agent for SAP in your SAP HANA deployment. For information about Backint based backup and recovery, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). This argument is available in `sap_hana` module version `1.5.807307812` or later. You can use only one backup option in your Terraform configuration - Backint or disk based backup. For more information, see [Backup management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#backup_management).  
`sap_hana_backup_size` | Integer | Optional. Specify size of the `/hanabackup` volume in GB. If you don't specify this argument or set it to `0`, then the installation script provisions Compute Engine instance with a HANA backup volume of two times the total memory. `sap_hana_backup_size` is ignored when you specify a value for `sap_hana_backup_nfs` or `sap_hana_backup_nfs_resource`.  
`sap_hana_volume_encryption` | String |  Optional. During the installation of SAP HANA, if you want to enable the [ data and log volume encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/dc01f36fbb5710148b668201a6e95cf2.html), then specify this argument with the value `on`. The default value of this argument depends on the version of SAP HANA you're installing:
     * For SAP HANA 2.0 SPS 07 or later, the default value for this argument is `on`.
     * For SAP HANA 2.0 SPS 06 or earlier, the default value for this argument is `off`.  
`sap_hana_backup_encryption` | String |  Optional. During the installation of SAP HANA, if you want to enable the [backup encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/e5c51c31ecaf4b7188a76776ba3c0797.html), then specify this argument with the value `on`. The default value of this argument depends on the version of SAP HANA you're installing:
     * For SAP HANA 2.0 SPS 07 or later, the default value for this argument is `on`.
     * For SAP HANA 2.0 SPS 06 or earlier, the default value for this argument is `off`.  
`sap_hana_sapsys_gid` | Integer | Optional. Overrides the default group ID for `sapsys`. The default value is `79`.   
`network_tags` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for firewall or routing purposes.  If you specify `public_ip = false` and don't specify a network tag, then make sure to provide another means of access to the internet.   
`disk_type` | String | Optional. Specify the default type of Persistent Disk or Hyperdisk volume that you want to deploy for the `/hana/data`, `/hana/log`, and `/usr/sap` directories in your deployment. For information about the default disk deployment performed by the Terraform configurations provided by Google Cloud, see [ Disk deployment by Terraform](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#disk-deployment-by-terraform). The following are valid values for this argument: `hyperdisk-extreme`, `hyperdisk-balanced`, `pd-ssd`, `pd-balanced`, and `pd-extreme`.  You can override this default disk type and the associated default disk size and default IOPS using some advanced arguments. For more information, navigate to your working directory, then run the `terraform init` command, and then see the `/.terraform/modules/sap_hana/variables.tf` file. Before you use these arguments in production, make sure to test them in a non-production environment.  If you want to use [SAP HANA Native Storage Extension](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/4efaa94f8057425c8c7021da6fc2ddf5.html) (NSE), then you need to provision larger disks by using the advanced arguments.  
`use_single_shared_data_log_disk` | Boolean | Optional. The default value is `false`, which directs Terraform to deploy a separate persistent disk or Hyperdisk for each of the following SAP volumes: `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap`. To mount these SAP volumes on the same persistent disk or Hyperdisk, specify `true`.   
`enable_data_striping` | Boolean | Optional. This argument lets you deploy the `/hana/data` volume on two disks. The default value is `false`, which directs Terraform to deploy a single disk for hosting your `/hana/data` volume.  This argument is available in `sap_hana` module version `1.3.674800406` or later.   
`include_backup_disk` | Boolean | Optional. The default value is `true`, which directs Terraform to deploy a separate disk to host the `/hanabackup` directory. The disk type is determined by the `backup_disk_type` argument. The size of this disk is determined by the `sap_hana_backup_size` argument. If you set the value for `include_backup_disk` as `false`, then no disk is deployed for the `/hanabackup` directory.  You can use only one backup option in your Terraform configuration - either disk based backup or Backint based backup. For more information, see [Backup management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#backup_management).  
`backup_disk_type` | String | Optional. For scale-up deployments, specify the type of Persistent Disk or Hyperdisk that you want to deploy for the `/hanabackup` volume. For information about the default disk deployment performed by the Terraform configurations provided by Google Cloud, see [ Disk deployment by Terraform](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#disk-deployment-by-terraform). The following are the valid values for this argument: `hyperdisk-extreme`, `hyperdisk-balanced`, `pd-ssd`, `pd-balanced`, `pd-standard`, and `pd-extreme`. This argument is available in `sap_hana` module version `202307061058` or later.   
`enable_fast_restart` | Boolean | Optional. This argument determines whether or not the [SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#sap-hana-fast-restart-on-gc) is enabled for your deployment. The default value is `true`. Google Cloud strongly recommends enabling the SAP HANA Fast Restart option.  This argument is available in `sap_hana` module version `202309280828` or later.   
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
`vm_static_ip` | String |  Optional. Specify a valid static IP address for the VM instance. If you don't specify one, then an IP address is automatically generated for your VM instance. This argument is available in `sap_hana` module version `202306120959` or later.   
`worker_static_ips` | List(String) | Optional. Specify an array of valid static IP addresses for the worker instances in your scale-out system. If you don't specify a value for this argument, then an IP address is automatically generated for each worker VM instance. For example, `[ "1.0.0.1", "2.3.3.4" ]`. The static IP addresses are assigned in the order of instance creation. For example, if you choose to deploy 3 worker instances but specify only 2 IP addresses for the argument `worker_static_ips`, then these IP addresses are assigned to the first two VM instances that the Terraform configuration deploys. For the third worker VM instance, the IP address is automatically generated. This argument is available in `sap_hana` module version `202306120959` or later.   
`can_ip_forward` | Boolean | Specify whether sending and receiving of packets with non-matching source or destination IPs is allowed, which enables a VM to act like a router. The default value is `true`. If you only intend to use Google's internal load balancers to manage virtual IPs for the deployed VMs, then set the value to `false`. An internal load balancer is automatically deployed as part of high availability templates.  
  
The following example shows a completed configuration file that directs Terraform to deploy an `n2-highmem-32` virtual machine with a scale-out SAP HANA system that includes a master SAP HANA instance with three worker hosts, and [Filestore Basic](https://docs.cloud.google.com/filestore/docs/service-tiers#basic_hdd_and_basic_ssd_tiers) instances that share the `/hana/shared` and `/hanabackup` volumes with the worker hosts. The hosts run the operating system SLES for SAP 15 SP2.
    
    #
    resource "google_filestore_instance" "hana_shared_nfs" {
      name = "fs-basic-shared"
      tier = "PREMIUM"
      project = "example-project-123456"
      location = "us-central1-f"
      file_shares {
        name = "hana_shared_nfs"
        capacity_gb = 2600
      }
      networks {
        network = "example-network"
        modes   = ["MODE_IPV4"]
      }
    }
    
    resource "google_filestore_instance" "hana_backup_nfs" {
      name = "fs-basic-backup"
      tier = "PREMIUM"
      project = "example-project-123456"
      location = "us-central1-f"
      file_shares {
        name = "hana_backup_nfs"
        capacity_gb = 2600
      }
      networks {
        network = "example-network"
        modes   = ["MODE_IPV4"]
      }
    }
    
    #...
    module "sap_hana" {
      source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana/sap_hana_module.zip"
      #
      # By default, this source file uses the latest release of the terraform module
      # for SAP on Google Cloud. To fix your deployments to a specific release
      # of the module, comment out the source property above and uncomment the source property below.
      #
      # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/YYYYMMDDHHMM/terraform/sap_hana/sap_hana_module.zip"
      # ...
      project_id = "example-project-123456"
      zone = "us-central1-f"
      machine_type = "n2-highmem-32"
      subnetwork = "example-subnet-us-central1"
      linux_image = "sles-15-sp2-sap"
      linux_image_project = "suse-sap-cloud"
    
      instance_name = "example-vm"
      sap_hana_shared_nfs_resource  = resource.google_filestore_instance.hana_shared_nfs
      sap_hana_backup_nfs_resource  = resource.google_filestore_instance.hana_backup_nfs
    
      # sap_hana_shared_nfs = "10.151.91.122:/hana_shared_nfs"
      # sap_hana_backup_nfs = "10.216.41.122:/hana_backup_nfs"
    
      sap_hana_deployment_bucket = "mybucketname/installables"
      sap_hana_sid = "AB2"
      sap_hana_instance_number = 12
      sap_hana_sidadm_password = "TempPa55word"
      sap_hana_system_password = "TempPa55word"
      sap_hana_scaleout_nodes = 3
      sap_hana_sidadm_uid = 11
      vm_static_ip = "10.0.0.1"
      worker_static_ips = ["10.0.0.2", "10.0.0.3", "10.0.0.4"]
      enable_fast_restart = true
      # ...
    }

  6. To initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud:
         
         terraform init

The `terraform init` command prepares your working directory for other Terraform commands.

To force a refresh of the provider plugin and configuration files in your working directory, specify the `--upgrade` flag. If the `--upgrade` flag is omitted and you don't make any changes in your working directory, then Terraform uses the locally cached copies, even if `latest` is specified in the `source` URL.
         
         terraform init --upgrade

  7. Optionally, to create the Terraform execution plan:
         
         terraform plan

The `terraform plan` command shows the changes required by your current configuration. If you skip the `terraform plan` command, then the `terraform apply` command computes the plan before applying it.

  8. To apply the execution plan:
         
         terraform apply

When you are prompted to approve the actions, enter `yes`.

The `terraform apply` command sets up the Google Cloud infrastructure and then invokes another script that configures the operating system and installs SAP HANA.

While Terraform has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the logs.

Time to completion can vary, but the entire process usually takes less than 30 minutes.




## Verify deployment

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

       2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

       3. Go to your working directory and delete the deployment to clean up the VMs and persistent disks from the failed installation:
              
              terraform destroy

When you are prompted to approve the action, enter `yes`.

       4. Rerun your deployment.




### Check the configuration of the VM and SAP HANA system

  1. After the SAP HANA system deploys without errors, connect to each VM by using SSH. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for each VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ssh-button.png)

  2. Switch to the root user:
         
         sudo su -

  3. At the command prompt, enter `df -h`, and then make sure that you see an output similar to the following, with the volumes and sizes that you expect.

The following is an example output from the master node of a sample scale-out system that has three worker nodes. Note that there are no volumes for `/hana/shared` and `/hanabackup` because these volumes are hosted on Filestore instances.
         
         example-vm:~ # df -h
         Filesystem                         Size  Used Avail Use% Mounted on
         devtmpfs                           126G  8.0K  126G   1% /dev
         tmpfs                              189G     0  189G   0% /dev/shm
         tmpfs                              126G   18M  126G   1% /run
         tmpfs                              126G     0  126G   0% /sys/fs/cgroup
         /dev/sda3                           30G  6.5G   24G  22% /
         /dev/sda2                           20M  2.9M   18M  15% /boot/efi
         10.65.188.162:/hana_shared_nfs     2.5T   41G  2.4T   2% /hana/shared
         /dev/mapper/vg_hana_usrsap-usrsap   32G  265M   32G   1% /usr/sap
         /dev/mapper/vg_hana_data-data      308G   10G  298G   4% /hana/data
         /dev/mapper/vg_hana_log-log        128G  7.8G  121G   7% /hana/log
         10.160.217.66:/hana_backup_nfs     2.5T     0  2.4T   0% /hanabackup
         tmpfs                               26G     0   26G   0% /run/user/472
         tmpfs                               26G     0   26G   0% /run/user/900
         tmpfs                               26G     0   26G   0% /run/user/1000

  4. Switch to the SAP admin user:
         
         su - SID_LCadm
         

Replace `SID_LC` with the SID value that you specified in the configuration file. Use lowercase for any letters.

  5. Verify that SAP HANA services, such as `hdbnameserver`, `hdbindexserver`, and others, are running on the instance:
         
         HDB info
         

  6. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




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



## Install SAP HANA Studio on a Compute Engine Windows VM

You can connect from a SAP HANA instance outside of Google Cloud or from an instance on Google Cloud. To do so, you might need to enable network access to the target VMs from within SAP HANA Studio.

To install SAP HANA Studio on a Windows VM on Google Cloud, use the following procedure.

  1. Use the Cloud Shell to invoke the following commands:

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)
         
         export NETWORK_NAME="NETWORK_NAME"
         export REGION="REGION"
         export ZONE="ZONE"
         export SUBNET="SUBNETWORK_NAME"
         export SOURCE_IP_RANGE="WORKSTATION_IP"
         
         gcloud compute instances create saphanastudio --zone=$ZONE \
         --machine-type=n1-standard-2  --subnet=$SUBNET --tags=hanastudio \
         --image-family=windows-2016  --image-project=windows-cloud \
         --boot-disk-size=100 --boot-disk-type=pd-standard \
         --boot-disk-device-name=saphanastudio
         
         gcloud compute firewall-rules create ${NETWORK_NAME}-allow-rdp \
         --network=$NETWORK_NAME --allow=tcp:3389 --source-ranges=$SOURCE_IP_RANGE \
         --target-tags=hanastudio

The preceding commands set variables for the current Cloud Shell session, create a Windows server in the subnetwork that you created earlier, and create a firewall rule that allows access from your local workstation to the instance through the [Remote Desktop Protocol](https://wikipedia.org/wiki/Remote_Desktop_Protocol) (RDP).

  2. [Install SAP HANA Studio](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/LATEST/en-US) on this server.

     1. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) the SAP HANA Studio installation files and the SAPCAR extraction tool to a Cloud Storage bucket in your Google Cloud project.
     2. Connect to the new Windows VM by using RDP or your preferred method.
     3. In Windows, with administrator permissions, open the Google Cloud CLI Shell or other command-line interface.
     4. Copy the SAP HANA Studio installation files and the SAPCAR extraction tool from the storage bucket to the VM by entering the [`gcloud storage cp` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) in the command interface. For example:
            
            gcloud storage cp gs://SOURCE_BUCKET/IMC_STUDIO2_232_0-80000323.SAR C:\TARGET_DIRECTORY &
            gcloud storage cp gs://SOURCE_BUCKET/SAPCAR_1014-80000938.EXE C:\TARGET_DIRECTORY
            

     5. Change the directory to your target directory:
            
            cd C:\TARGET_DIRECTORY

     6. To extract the SAP HANA Studio installation file, run the `SAPCAR` program:
            
            SAPCAR_1014-80000938.EXE -xvf IMC_STUDIO2_232_0-80000323.SAR

     7. To install SAP HANA Studio, run the extracted `hdbinst` program.




## Set up monitoring for SAP HANA

Optionally, you can monitor your SAP HANA instances using Google Cloud's Agent for SAP. From version 2.0, you can configure the agent to collect the SAP HANA monitoring metrics and send them to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Cloud Monitoring lets you create dashboards to visualize these metrics, set up alerts based on metric thresholds, and more.

For more information about the collection of SAP HANA monitoring metrics using Google Cloud's Agent for SAP, see [SAP HANA monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics).

## Connect to SAP HANA

Note that because these instructions don't use an external IP for SAP HANA, you can only connect to the SAP HANA instances through the bastion instance using SSH or through the Windows server through SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instance(s) by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server instance. After connection, manually [install SAP HANA Studio](https://help.sap.com/hana/SAP_HANA_Studio_Installation_Update_Guide_en.pdf) and access your SAP HANA database.




## Perform post-deployment tasks

Before using your SAP HANA instance, we recommend that you perform the following post-deployment steps. For more information, see [SAP HANA Installation and Update Guide](http://help.sap.com/hana/SAP_HANA_Server_Installation_Guide_en.pdf).

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser. For example:
         
         sudo passwd SIDadm

See [Reset the SYSTEM User Password of the System Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/6b13cdd1982f4aa6b90b443663d17d7e.html).

  2. Install your permanent SAP HANA license. If you don't, then SAP HANA might go into _database lockdown_ after the temporary license expires.

For more information from SAP about managing your SAP HANA licenses, see [License Keys for the SAP HANA Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/9fd02a6c45eb485b9b3b0bc845586a6a.html).

  3. Update the SAP HANA software with the latest patches.

  4. If your SAP HANA system is deployed on a VirtIO network interface, then we recommend that you ensure the value of the TCP parameter `/proc/sys/net/ipv4/tcp_limit_output_bytes` is set to `1048576`. This modification helps improve the overall network throughput on the VirtIO network interface without affecting the network latency. 

  5. Install any additional components such as Application Function Libraries (AFL) or Smart Data Access (SDA).

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
