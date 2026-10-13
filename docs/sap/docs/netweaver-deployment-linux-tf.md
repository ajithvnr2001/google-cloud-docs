---
url: https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-tf/
title: Terraform: Automated VM deployment for SAP NetWeaver on Linux \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:10.493001+00:00
---

# Terraform: Automated VM deployment for SAP NetWeaver on Linux  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Terraform: Automated VM deployment for SAP NetWeaver on Linux Stay organized with collections  Save and categorize content based on your preferences. 

This guide uses [Terraform](https://docs.cloud.google.com/docs/terraform) to deploy all of the required Google Cloud resources to run SAP NetWeaver on Linux, including the Compute Engine virtual machine (VM), the Linux operating system, and the persistent disks. You define the values for the installation, such as machine type, resource names, disk sizes, and so forth, in a Terraform configuration file.

If your SAP NetWeaver installation requires more control over the deployment process than the Terraform configuration file provides, see [Manual VM deployment for SAP NetWeaver on Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-manual).

To deploy a VM that is running Windows, see the [Windows deployment guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows).

## VM configuration deployed by these instructions

The VM that is deployed by these instructions is for use in a 3-tier configuration, where SAP NetWeaver runs on one VM and the database server runs on another.

To set up a 2-tier configuration, where SAP NetWeaver runs on the same VM as the database server, you deploy the database server first and create the VM and the required disk drives for both the database server and for SAP NetWeaver at that time. You then install SAP NetWeaver on the same VM as the database server.

For instructions about deploying the VM for a database server, see the [database deployment guide](https://docs.cloud.google.com/sap/docs) for your database server.

## Google Cloud resources deployed by these instructions

The Google Cloud resources that are deployed by Terraform configuration file include:

  * A VM that uses an SAP-certified version of Linux.
  * A persistent disk for the boot disk.
  * A persistent disk for SAP binaries.
  * A persistent disk for swap space.
  * The recommended APIs.
  * Google Cloud's Agent for SAP.



The following instructions use Cloud Shell, but if you prefer, you can use the Google Cloud CLI in your local terminal instead.

For more details on planning your implementation, see the [Planning guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide). For an overview of IT ops for your system, see the [Operations guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide).

## Creating a project

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

To create a project:

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




## Configuring the `gcloud` command environment

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
  * SSH connections to your VM instance, including [SSH from the browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser), through port `22`.
  * Connections to your VM instance from third-party tools, such as a local terminal or PuTTY. Create a rule to allow access for the tool through your firewall. For more information, see [Connect to Linux VMs using third-party tools](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools). 



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

## Deploying a Linux VM for SAP NetWeaver with Terraform

The following instructions use Cloud Shell to deploy a VM instance with Linux and all of the persistent disks that SAP NetWeaver requires.

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules. If you use the Terraform configuration file that Google Cloud provides, specify a tag with `network_tags = "TAG"`.
    * Create the VMs without an external IP. If you use the Terraform configuration file that Google Cloud provides, specify `public_ip = false`.



### Deployment procedure

  1. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the `sap_nw.tf` configuration file to your working directory:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_nw/terraform/sap_nw.tf

**Note:** Ensure that you have only a single Terraform configuration file in your working directory.
  3. Open the `sap_nw.tf` file in the Cloud Shell code editor.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  4. In the `sap_nw.tf` file, update the argument values by replacing the contents inside the double quotation marks with the values for your installation. The arguments are described in the following table.

Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `sap_nw.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`zone` | String | Specify the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which you are deploying your SAP system. The zone must be in the same region that you selected for your subnet. For example, if your subnet is deployed in the `us-central1` region, then you can specify a zone such as `us-central1-a`.  
`machine_type` | String |  Specify the type of Compute Engine [virtual machine](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms) (VM) on which you need to run your SAP system. If you need a custom VM type, then specify a [predefined VM type](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-custom) with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the number of vCPUs and the amount of memory](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations). For example, `n1-highmem-32`.  
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `rhel-9-2-sap-ha` or `sles-15-sp5-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify either `rhel-sap-cloud` or `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`instance_name` | String | Specify a name for the compute instance that Terraform deploys to run your SAP NetWeaver workload. The name can contain lowercase letters, numbers, and hyphens.  
`usr_sap_size` | Integer |  Optional. Specify the size of the `/usr/sap` disk in GB. The minimum size is 8 GB. The default value is `8`.   
`sap_mnt_size` | Integer |  Optional. Specify the size of the `/sapmnt` disk in GB. The minimum size is 8 GB. The default value is `8`.   
`swap_size` | Integer |  Optional. Specify the size of the swap volume in GB. The minimum size is 8 GB. The default value is `8`.   
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
`can_ip_forward` | Boolean | Specify whether sending and receiving of packets with non-matching source or destination IPs is allowed, which enables a VM to act like a router. The default value is `true`. If you only intend to use Google's internal load balancers to manage virtual IPs for the deployed VMs, then set the value to `false`. An internal load balancer is automatically deployed as part of high availability templates.  
  
The following configuration file creates a VM that is configured to run SAP NetWeaver. The configuration file deploys an `n1-standard-16` VM that is running a SLES 15 SP3 operating system. The VM includes all of the directories that are required in order to run SAP NetWeaver.
    
    # ...
      module "sap_nw" {
      source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_nw/sap_nw_module.zip"
      #
      # By default, this source file uses the latest release of the terraform module
      # for SAP on Google Cloud.  To fix your deployments to a specific release
      # of the module, comment out the source property above and uncomment the source property below.
      #
      # source = "https://storage.googleapis.com/cloudsapdeploy/terraform/YYYYMMDDHHMM/terraform/sap_nw/sap_nw_module.zip"
      #
      # ...
      #
      project_id = "example-project-123456"
      zone = "us-central1-f"
      machine_type = "n1-standard-16"
      subnetwork = "example-sub-network-sap"
      linux_image = "sles-15-sp3-sap"
      linux_image_project = "suse-sap-cloud"
    
      instance_name = "ex-vm-nw-lin"
      # ...
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

  8. After the VM instance deploys, if you need Compute Engine to save the boot disk in the event the VM instance is deleted:

     1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. To open the **VM instance details** page for your VM instance, click the name of the VM instance.

     3. Click **Edit**.

     4. In the **Boot disk** section, for the **Deletion rule** , ensure that the **Keep disk** option is selected.

     5. Click **Save**.




### Verifying deployment

To verify deployment, you check the deployment logs in Cloud Logging and check the configuration of the VM.

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

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the SAP NetWeaver requirements that are listed in the [SAP NetWeaver planning guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#pricing-and-quotas).

       2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

       3. Go to your working directory and delete the deployment to clean up the VMs and persistent disks from the failed installation:
              
              terraform destroy

When you are prompted to approve the action, enter `yes`.

       4. Rerun your deployment.




#### Check the configuration of the VM

  1. After the VM instance deploys, connect to your VM by using `ssh`.

     1. If you haven't already done so, create a firewall rule to allow an SSH connection on port `22`.
     2. Go to the **VM Instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     3. Click **SSH** for your VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/netweaver-ssh-button.png)

  2. Change to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output similar to the following.

![Data volumes created by the script.](https://docs.cloud.google.com/static/sap/docs/images/netweaver-data-volumes-linux.png)

  4. Confirm that the swap directory was created:
         
         cat /proc/meminfo | grep Swap

You see results similar to the following example:

![Example of terminal output when the swap directory exists.](https://docs.cloud.google.com/static/sap/docs/images/netweaver-swap-verify-linux.png)

  5. If you are using RHEL for SAP 9.0 or later, then make sure that the packages `chkconfig` and `compat-openssl11` are installed on your VM instance.

For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316).




If any of the validation steps show that the installation failed:

  1. Correct the error.

  2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Go to the directory that contains the Terraform configuration file.

  4. Delete the deployment:
         
         terraform destroy

When you are prompted to approve the action, enter `yes`.

  5. Rerun your deployment.




### Connecting to your VM

If you have defined a firewall rule that allows access on port `22`, you can connect to a Linux VM using common SSH tools.

You can connect through the Google Cloud console or you can connect from a terminal by using a `gcloud` command.

### Console

To connect by using `ssh` directly from your browser in the [Google Cloud console](https://console.cloud.google.com/):

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




### gcloud

The Google Cloud CLI manages your SSH keys for you by generating and applying new project-wide SSH keys when you need them.

Connect to your VM instance:
    
    
    gcloud compute --project "[VM_PROJECT_ID]" ssh --zone "[VM_ZONE]" "[VM_NAME]"

where:

  * `[VM_PROJECT_ID]` is the ID of the Google Cloud project in which you have created your VM.
  * `[VM_ZONE]` is the zone in which you have located your VM.
  * `[VM_NAME]` is the name of your VM instance.



After you submit this command, the terminal is connected to your VM on Google Cloud and you can run commands on your Linux VM. When you are done, use the `exit` command to disconnect from the VM.

**Note:** New VMs can take some time to boot up before an SSH connection is established. If you fail to connect to a new instance, retry after a few minutes.

You can also generate a new key-pair for your Linux VM and apply it to your project, which allows you to connect using third-party tools such as [PuTTY on Windows workstations](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools#putty-app). For more details, see [Create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).

Other connection options, which aren't discussed here, are also possible.

For more detailed information about connecting to a Linux VM on Google Cloud, see [Connecting to Linux instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools).

## Setting up the database

If you haven't yet deployed your database on Google Cloud, then follow the instructions for setting up your database in both the Google Cloud deployment guide for your database, and in the database documentation that is provided by your database vendor.

Google Cloud provides deployment guides for the following SAP-certified databases:

  * [SAP HANA guides](https://docs.cloud.google.com/sap/docs/sap-hana-guides)
  * [SAP ASE guides](https://docs.cloud.google.com/sap/docs/sap-ase-guides)
  * [SAP MaxDB guides](https://docs.cloud.google.com/sap/docs/sap-maxdb-guides)
  * [IBM Db2 guides](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-guides)
  * [Oracle Database guides](https://docs.cloud.google.com/sap/docs/oracle-all-guides). To run an Oracle Database with SAP NetWeaver, you must use an SAP-certified version of Oracle Linux. Also, all components of your SAP system must run the same Oracle Linux version. This includes the database, app servers, and any other closely-coupled auxiliary system.
  * [Windows SQL Server guide](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances): when SAP NetWeaver is running on Linux, Windows SQL Server is supported only in 3-tier architectures. 



When SAP NetWeaver and the database server are running on different compute instances in a 3-tier architecture, make sure that your firewall rules are defined to allow communication between the instances.

## Installing the Cloud Logging agent

The Cloud Logging agent provides you with a solution for Google Cloud system-activity logging, including operating system events and, if you are using SAP HANA, SAP HANA events. The Cloud Logging agent is an optional but recommended component. See the [SAP NetWeaver on Google Cloud operations guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide#use_stackdriver_logging) for more information about Google Cloud logging.

To install the Cloud Logging agent in your new VM, see the instructions for Linux and Windows in [Installing the agent](https://docs.cloud.google.com/logging/docs/agent/installation#joint-install).

## Installing SAP NetWeaver

For instructions on installing SAP NetWeaver on your new VM, see [the SAP help portal](https://help.sap.com/viewer/p/SAP_NETWEAVER_750) and the [SAP NetWeaver Master Guide](https://help.sap.com/doc/18cb1a50b9924bc3b94c2988cc8c51d9/7.5/en-US/mg_nw_75.pdf).

**Important:** The Software Provisioning Manager (SWPM) chooses the disk drive with the most free space as an installation suggestion for each component. On Google Cloud, it's important that you don't accept the defaults. Be sure to assign the disks to their proper roles in the SWPM dialog boxes.

After you install SAP NetWeaver:

  1. Update the SAP kernel to the minimum supported patch level.

For details on the supported SAP kernel patch levels, see SAP note [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441). 

  2. Install your permanent SAP NetWeaver license.

For more information from SAP about managing your SAP NetWeaver licenses, see [SAP Licensing Procedure](https://help.sap.com/viewer/0643d547dfad4ce497bd7da1264fce77/7.5.6/en-US/fbde4502adef496988fe13d459d66b8b.html).




### Installing the SAP Host Agent

The SAP Host Agent has been enhanced for running on Google Cloud. Ensure that you run at least the minimum SAP Host Agent version required for the Google Cloud environment.

For more information, see the following SAP note [2460297 - SAP on Linux on Google Cloud Platform: Enhanced Monitoring](https://me.sap.com/notes/2460297).

To update your SAP Host Agent by default on a regular basis, see the SAP note [1473974 - Using the SAP Host Agent Auto Upgrade Feature](https://me.sap.com/notes/1473974).

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



## Evaluate your SAP NetWeaver workload

To automate continuous validation checks for your SAP NetWeaver workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager allows you to automatically scan and evaluate your SAP NetWeaver workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP NetWeaver workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## Troubleshooting

This section contains information about how to correct common issues.

### Troubleshooting communication problems to the database server

If you are setting up a 3-tier SAP system and having connection issues between your VMs, ensure that you have created a firewall rule to allow traffic between VMs on your subnetwork.

### Troubleshooting connecting to your VM

If you are having issues connecting to your VM through `ssh`, ensure that you have created a firewall rule to open port `22` on the Google Cloud network you are using.

For other possible issues, see [Known issues](https://docs.cloud.google.com/compute/docs/ssh-in-browser#known_issues) for SSH from the browser. 

### Troubleshooting Google Cloud's Agent for SAP

To troubleshoot Google Cloud's Agent for SAP, see the [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
