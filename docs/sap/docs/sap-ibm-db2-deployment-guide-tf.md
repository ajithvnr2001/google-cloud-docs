---
url: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf/
title: Automated VM deployment for IBM Db2 on Linux for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:49.678497+00:00
---

# Automated VM deployment for IBM Db2 on Linux for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Automated VM deployment for IBM Db2 on Linux for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This deployment guide shows you how to deploy the Google Cloud resources for an IBM Db2 instance on Linux that supports SAP applications.

The instructions in this guide use [Terraform](https://docs.cloud.google.com/docs/terraform) to deploy and configure the VM, the Linux operating system, the required disk volumes for IBM Db2, and install Google Cloud's Agent for SAP.

For details on planning your deployment, see the [IBM Db2 for SAP planning guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide).

## Prerequisites

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

If you don't already have a Google Cloud project with billing enabled, then you must create one before you can deploy a virtual machine (VM) for your IBM Db2 installation.

### Creating a project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Configuring the `gcloud` command environment

These instructions use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to enter `gcloud` commands that deploy or configure your Google Cloud resources. Cloud Shell is accessed through the Google Cloud console in your browser.

Cloud Shell runs on a VM that Google Cloud provisions each time you start Cloud Shell. The first time you use Cloud Shell, Google Cloud also creates a persistent `$HOME` directory for you, which is restored each time you open Cloud Shell.

The provisioned VM includes the latest [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). Therefore, the `gcloud` commands that you use in Cloud Shell are the same as those you would use in a locally installed instance of the gcloud CLI.

If you have the gcloud CLI installed, you can issue the `gcloud` commands that are used in these instructions from your local machine. However, with a locally installed gcloud CLI you must always make sure that you are using the latest version of the gcloud CLI.

Whether you use Cloud Shell or gcloud CLI, you can set and change the properties of your `gcloud` command environment and save them as a _configuration_. Configurations are collections of key-value pairs that influence the behavior of the `gcloud` commands.

Some basic actions you can take with a configuration in Cloud Shell include:

  * Initialize a configuration:
        
        gcloud init

  * Check the settings of your current gcloud configuration:
        
        gcloud config list

  * Switch to the required Google Cloud project. Replace `PROJECT_ID` with your Google Cloud project ID.
        
        gcloud config set project PROJECT_ID

  * Set a default region. Replace `REGION` with a Google Cloud region.
        
        gcloud config set compute/region REGION

  * Set a default zone. Replace `ZONE` with a Google Cloud zone.
        
        gcloud config set compute/zone ZONE

  * Create a new configuration. Replace `NAME` with the name for the configuration.
        
        gcloud config configurations create NAME




For more information about working with configurations, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/configurations).

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

## Adding firewall rules

By default, incoming connections from outside your Google Cloud network are blocked. To allow incoming connections, set up a firewall rule for your VM. Firewall rules regulate only new incoming connections to a VM. After a connection is established with a VM, traffic is permitted in both directions over that connection.

You can create a firewall rule to allow access to specified ports, or to allow access between VMs on the same subnetwork.

Create firewall rules to allow access for such things as:

  * The default ports used by SAP NetWeaver, as documented in [TCP/IP Ports of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine VM instance. If you are unsure of what IP address to use, talk to your company's network admin.
  * Communication between VMs in a 3-tier, scaleout, or high-availability configuration. For example, if you are deploying a 3-tier system, you will have at least 2 VMs in your subnetwork: the VM for SAP NetWeaver, and another VM for the database server. To enable communication between the two VMs, you must create a firewall rule to allow traffic that originates from the subnetwork. 



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

## Deploying a Linux VM for Db2 with Terraform

The following instructions use Terraform to deploy a VM instance with Linux and all of the persistent disks that IBM Db2 requires to support SAP applications. You define the values for the installation in a `sap_db2.tf` configuration file that Google Cloud provides.

The following instructions use Cloud Shell, but if you prefer, you can use [Terraform](https://docs.cloud.google.com/docs/terraform) in your local terminal instead.

  1. Open the Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the `sap_db2.tf` configuration file to your working directory by entering the following command in the Cloud Shell:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_db2/terraform/sap_db2.tf

  3. Open the `sap_db2.tf` file in the Cloud Shell code editor.

To open the Cloud Shell code editor, click **Open Editor**.

  4. In the `sap_db2.tf` file, update the following argument values by replacing the content inside the double quotation marks with the values for your installation.

Most optional arguments have a default value. When you don't specify an optional argument, the Terraform configuration uses that argument's default value, if any.

Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `sap_db2.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`zone` | String | Specify the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which you are deploying your SAP system. The zone must be in the same region that you selected for your subnet. For example, if your subnet is deployed in the `us-central1` region, then you can specify a zone such as `us-central1-a`.  
`machine_type` | String |  Specify the type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms) (VM) on which you need to run your SAP system. If you need a custom VM type, then specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-custom) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations). For example, `n1-highmem-32`.  
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `rhel-9-2-sap-ha` or `sles-15-sp5-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify either `rhel-sap-cloud` or `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`instance_name` | String | Specify a name for the compute instance that Terraform deploys to run your IBM Db2 workload. The name can contain lowercase letters, numbers, and hyphens.  
`db2_sid` | String | Specify the SID of your IBM Db2 database instance. The ID must consist of three alphanumeric characters and begin with a letter. All letters must be in uppercase. For example, `ED1`.  
`db2_sid_size` | Integer | Optional. Specify the size in GB for `/db2/DBSID` volume, which is the root directory of your IBM Db2 database instance. The minimum size is 8 GB. The default value is `8`.   
`db2_home_size` | Integer | Optional. Specify the size in GB for the `/db2/db2DBSID` volume, which is the home directory of your IBM Db2 database instance. The minimum size is 8 GB. The default value is `8`.   
`db2_dump_size` | Integer | Optional. Specify the size in GB for the `/db2/DBSID/db2dump` volume, which holds the dump files from your IBM Db2 database instance. The minimum size is 8 GB. The default value is `8`.   
`db2_sap_temp_size` | Integer | Optional. Specify the size in GB for the `/db2/DBSID/saptmp` volume, which holds the database instance's temporary tablespace. The minimum size is 8 GB. The default value is `8`.   
`db2_sap_data_size` | Integer | Optional. Specify the size in GB for the `/db2/DBSID/sapdata` volume, which holds the database data files. The minimum size is 30 GB. The default value is `30`.   
`db2_sap_data_ssd` | Boolean | Optional. Specify `true` to provision an SSD persistent disk for the `/db2/DBSID/sapdata` volume. If you specify `false`, then a balanced persistent disk is provisioned. The default value is `true`.   
`db2_log_size` | Integer | Optional. Specify the size in GB for the `/db2/DBSID/logdir` volume, which holds the database transaction logs. The minimum size is 8 GB. The default value is `8`.   
`db2_log_ssd` | Boolean | Optional. Specify `true` to provision an SSD persistent disk for the `/db2/DBSID/logdir` volume. If you specify `false`, then a balanced persistent disk is provisioned. The default value is `true`.   
`db2_backup_size` | Integer | Optional. Specify the size in GB for the `/db2backup` volume, which holds the database backups. If you don't specify this argument or set its value to `0`, then no disk is provisioned for the `/db2backup` volume.   
`usr_sap_size` | Integer |  To run IBM Db2 and SAP NetWeaver on the same VM instance, specify the size of the `/usr/sap` disk in GB.  If you don't specify this argument or set its value to `0`, then no disk is provisioned for the `/usr/sap` volume.   
`sap_mnt_size` | Integer |  To run IBM Db2 and SAP NetWeaver on the same VM instance, specify the size of the `/sapmnt` disk in GB.  If you don't specify this argument or set its value to `0`, then no disk is provisioned for the `/sapmnt` volume.   
`swap_size` | Integer |  To run IBM Db2 and SAP NetWeaver on the same VM instance, specify the size of the swap volume in GB.  If you don't specify this argument or set its value to `0`, then no disk is provisioned for the swap volume.   
`network_tags` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for firewall or routing purposes.  If you specify `public_ip = false` and don't specify a network tag, then make sure to provide another means of access to the internet.   
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
  
The following example `sap_db2.tf` configuration file creates a VM that is configured to run both the IBM Db2 database server and SAP NetWeaver. The configuration file directs Terarform to deploy an `n1-standard-16` VM that is running a SLES 15 SP3 operating system. The VM includes all of the directories that are required to run IBM Db2 with SAP NetWeaver.
    
    #
    # ...
    module "sap_db2" {
      source = https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_db2/sap_db2_module.zip
      #
      # By default, this source file uses the latest release of the terraform module
      # for SAP on Google Cloud. To fix your deployments to a specific release
      # of the module, comment out the source property above and uncomment the source property below.
      #
      # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/YYYYMMDDHHMM/terraform/sap_db2/sap_db2_module.zip"
      # ...
      project_id = "example-project-123456"
      zone = "us-central1-f"
      machine_type = "n1-standard-16"
      subnetwork = "example-subnet-us-central1"
      linux_image = "sles-15-sp3-sap"
      linux_image_project = "suse-sap-cloud"
    
      instance_name = "ex-vm-db2-lin"
    
      db2_sid = "AS1"
      db2_sid_size = 15
      db2_home_size = 15
      db2_dump_size = 15
      db2_sap_temp_size = 20
      db2_sap_data_size = 50
      db2_sap_data_ssd = true
      db2_log_size = 30
      db2_log_ssd = true
      db2_backup_size = 100
    
      usr_sap_size = 15
      sap_mnt_size = 15
      swap_size = 24
      # ...
    }

  5. To initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud:
         
         terraform init

The `terraform init` command prepares your working directory for other Terraform commands.

To force a refresh of the provider plugin and configuration files in your working directory, specify the `--upgrade` flag. If the `--upgrade` flag is omitted and you don't make any changes in your working directory, Terraform uses the locally cached copies, even if `latest` is specified in the `source` URL.
         
         terraform init --upgrade 

  6. Optionally, to create the Terraform execution plan:
         
         terraform plan

The `terraform plan` command shows the changes required by your current configuration. If you skip this step, the `terraform apply` command automatically creates a new plan and prompts you to approve it.

  7. To apply the execution plan:
         
         terraform apply

When you are prompted to approve the actions, enter `yes`.

The terraform `apply` command sets up the Google Cloud infrastructure according to the arguments defined in the Terraform configuration file. The process can take a few minutes. To check the progress of your deployment, follow the steps in the next section.

  8. After the VM instance deploys, if you need Compute Engine to save the boot disk in the event the VM instance is deleted, then follow these steps:

     1. In the Google Cloud console, go to the Compute Engine **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. To open the **VM instance details** page for your VM instance, click the name of the VM instance.

     3. Click **Edit**.

     4. In the **Boot disk** section, for the **Deletion rule** , ensure that the **Keep disk** option is selected.

     5. Click **Save**.




## Verifying deployment

To verify deployment, you check the deployment logs in Cloud Logging and check the configuration of the VM.

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

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the IBM Db2 requirements that are listed in the 

       2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

       3. Go to your working directory and delete the deployment to clean up the VMs and persistent disks from the failed installation:
              
              terraform destroy

When you are prompted to approve the action, enter `yes`.

       4. Rerun your deployment.




### Check the configuration of the VM

  1. After the VM instance deploys without errors, connect to your VM using SSH. From the Compute Engine [VM instances](https://console.cloud.google.com/compute/instances) page, you can click the **SSH** button for your VM, or you can use your preferred SSH method.

  2. Switch to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see an output similar to the following:
         
         Filesystem                     Size  Used Avail Use% Mounted on
         devtmpfs                       4.0M  8.0K  4.0M   1% /dev
         tmpfs                           52G     0   52G   0% /dev/shm
         tmpfs                           21G   18M   21G   1% /run
         tmpfs                          4.0M     0  4.0M   0% /sys/fs/cgroup
         /dev/sda3                       30G  4.3G   26G  15% /
         /dev/sda2                       20M  2.9M   18M  15% /boot/efi
         tmpfs                           11G     0   11G   0% /run/user/0
         /dev/mapper/vg_db2sid-vol       15G   48M   15G   1% /db2/AS1
         /dev/mapper/vg_db2dump-vol      15G   48M   15G   1% /db2/AS1/db2dump
         /dev/mapper/vg_db2sapdata-vol   50G   84M   50G   1% /db2/AS1/sapdata
         /dev/mapper/vg_db2saptmp-vol    20G   53M   20G   1% /db2/AS1/saptmp
         /dev/mapper/vg_db2log-vol       30G   63M   30G   1% /db2/AS1/log_dir
         /dev/mapper/vg_db2home-vol      15G   48M   15G   1% /db2/db2as1
         /dev/mapper/vg_db2backup-vol   100G  135M  100G   1% /db2backup
         /dev/mapper/vg_usrsap-vol       15G  200M   15G   2% /usr/sap
         /dev/mapper/vg_sapmnt-vol       15G   48M   15G   1% /sapmnt
         tmpfs                           11G     0   11G   0% /run/user/1000
         

  4. To confirm that the swap directory is created, run the following command:
         
         cat /proc/meminfo | grep Swap

You should see an output similar to the following:
         
         SwapCached:            0 kB
         SwapTotal:      25161724 kB
         SwapFree:       25161724 kB
         




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




## Installing the database server

Now that your operating system is configured, you can install your IBM Db2 database server.

For guidance on installing SAP NetWeaver with IBM Db2, see the [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) that is specific to your SAP NetWeaver system.

To install IBM Db2 on your Linux VM, follow these steps:

  1. Establish an SSH connection to your Linux-based VM.
  2. Download or copy the complete SAP media set for IBM Db2 to your VM.

You can download the SAP media set from the [SAP support portal](http://support.sap.com/swdc).

  3. Install the IBM Db2 database server with the SAP Software Provisioning Manager.

  4. Install your IBM Db2 license file.

For more information about installing an IBM Db2 license that you obtained from SAP, see the SAP note [816773 - DB6: Installing the Application-Specific Db2 License from SAP](https://me.sap.com/notes/816773).




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



## Performing post-deployment tasks

Before using your IBM Db2 instance, we recommend that you perform the following post-deployment steps:

  1. Update your IBM Db2 software with the latest patches, if available.
  2. Install any additional components.
  3. Configure and back up your new IBM Db2 database.



For additional post-deployment guidance, see the Post-installation Tasks section of the [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) that applies to the SAP system that you are using with IBM Db2.

## Troubleshooting

This section contains information about how to correct common issues.

### Troubleshooting connecting to your VM

If you are having issues connecting to your VM through `ssh`, ensure that you have created a firewall rule to open port `22` on the Google Cloud network you are using.

For other possible issues, see [Known issues](https://docs.cloud.google.com/compute/docs/ssh-in-browser#known_issues) for connecting through `ssh` from the browser.

### Troubleshooting Google Cloud's Agent for SAP

To troubleshoot issues concerning Google Cloud's Agent for SAP, see [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
