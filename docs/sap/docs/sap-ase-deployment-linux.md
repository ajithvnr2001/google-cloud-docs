---
url: https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux/
title: Deployment Manager: Automated VM deployment for SAP ASE on Linux \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:45.749103+00:00
---

# Deployment Manager: Automated VM deployment for SAP ASE on Linux  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deployment Manager: Automated VM deployment for SAP ASE on Linux Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reaches end of support on March 31, 2026. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To automate the deployment of a single-node SAP ASE system on Linux on Google Cloud, we recommend that you use Terraform. For more information, see [Terraform: SAP Automated VM deployment for SAP ASE on Linux](https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux-tf).

This deployment guide shows you how to deploy and connect to a Compute Engine virtual machine (VM) that is ready for the installation of SAP Adaptive Server Enterprise (ASE) on a Linux operating system.

The instructions in this guide use [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/fundamentals) to deploy and configure the VM, the Linux operating system, and the required disk volumes for SAP ASE.

For details on planning your deployment, see the [SAP ASE planning guide](https://docs.cloud.google.com/sap/docs/sap-ase-planning-guide).

## Prerequisites

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

If you do not already have a Google Cloud project with billing enabled, then you must create one before you can deploy a VM for your SAP ASE installation.

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
     * `REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want the subnetwork If you are using SAP ASE with SAP NetWeaver, use a region that is [supported for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#plan_regions_and_zones). 
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

  * ASE network listener for client connections. The default ASE port number is `5000`.
  * The ports required by SAP ASE Cockpit. For a list of ports that ASE Cockpit uses, see the [SAP ASE](https://help.sap.com/viewer/p/SAP_ASE) Cockpit documentation in the SAP Help Portal.
  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.
  * Communication between VMs in the SAP HANA subnetwork, including communication between nodes in an SAP HANA scale-out system or communication between the database server and application servers in a 3-tier architecture. You can enable communication between VMs by creating a firewall rule to allow traffic that originates from within the subnetwork.
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

## Deploying a Linux VM for SAP ASE with Deployment Manager

The following instructions use Deployment Manager to deploy a VM instance with Linux and all of the persistent disks that SAP ASE requires. You define the values for the installation in a Deployment Manager configuration file template.

Deployment Manager treats all of the resources that are created for the SAP ASE system as a single entity called a _deployment._ You can view all of the deployments for your Google Cloud project on the [Deployments](https://console.cloud.google.com/dm/deployments) page in the Google Cloud console.

**Note:** Deleting a deployment deletes all of the resources associated with the deployment, including the SAP ASE system, the VMs, and the persistent disks that were deployed with it.

The following instructions use Cloud Shell, but if you prefer, you can use the Google Cloud CLI in your local terminal instead.

  1. Open the Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the `template.yaml` configuration file template to your working directory by entering the following command in the Cloud Shell:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_ase/template.yaml

  3. Optionally, rename the `template.yaml` file to identify the configuration it defines.

  4. Open the `template.yaml` file in the Cloud Shell code editor.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  5. In the `template.yaml` file, update the following property values by replacing the brackets and their contents with the values for your installation.

Property | Data type | Description  
---|---|---  
`type` | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
`instanceName` | String | The name of the VM instance on which SAP ASE will be installed. The name must be 13 characters or less and be specified in lowercase letters, numbers, or hyphens.   
`instanceType` | String | The type of Compute Engine [virtual machine](https://docs.cloud.google.com/compute/docs/machine-types) on which SAP ASE will be installed. If you are running SAP ASE with SAP NetWeaver on the same VM, select a machine type that includes enough CPUs and memory to support both systems. See the [SAP NetWeaver planning guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types).   
`zone` | String | The zone in which you are deploying your SAP ASE. It must be in the same region that you selected for your subnetwork.   
`subnetwork` | String | The name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, specify this value as `SHARED_VPC_PROJECT/SUBNETWORK`. For example, `myproject/network1`.  
`linuxImage` | String | The name of the Linux operating- system image or image family that you are using with SAP ASE. To specify an image family, add the prefix `family/` to the family name. For example, `family/rhel-7` or `family/sles-12-sp2-sap`. To use a specific image, enter only the image name. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Cloud console.  
`linuxImageProject` | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project, such as `rhel-sap-cloud` or `suse-sap-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
`aseSID` | String | The database instance ID.   
`asesidSize` | Integer | The size in GB of `/sybase/DBSID`, which is the root directory of the database instance. In the deployed VM, this volume is labeled `ASE`.   
`asediagSize` | Integer | The size of `/sybase/DBSID/sapdiag`, which holds the diagnostic tablespace for SAPTOOLS.   
`asesaptempSize` | Integer | The size of `/sybase/DBSID/saptmp`, which holds the database temporary table space.  
`asesapdataSize` | Integer | The size of `/sybase/DBSID/sapdata`, which holds the database data files.   
`aselogSize` | Integer | The size of `/sybase/DBSIDlogdir`, which holds the database transaction logs.   
`asebackupSize` | Integer | The size of the `/sybasebackup` volume. If set to `0` or omitted, then no disk is created.   
`asesapdataSSD` | boolean | The SSD toggle for the data drive. If set to `true`, then the data disk is SSD.  
`aselogSSD` | boolean | The SSD toggle for the log drive. If set to `true`, then the log disk is SSD.  
`usrsapSize` | Integer | Required only if you are installing SAP ASE to run with SAP NetWeaver on the same VM instance.   
`sapmntSize` | Integer | Required only if you are installing SAP ASE to run with SAP NetWeaver on the same VM instance.   
`swapSize` | Integer | Required only if you are installing SAP ASE to run with SAP NetWeaver on the same VM instance.   
  
The following configuration file creates a VM that is configured to run both the SAP ASE database server and SAP NetWeaver. The configuration file directs Deployment Manager to deploy an `n1-standard-16` VM that is running a SLES 12 SP2 operating system. The VM includes all of the directories that are required to run SAP ASE with SAP NetWeaver.
         
         resources:
         - name: sap_ase
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_ase/sap_ase.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/202103310846/dm-templates/sap_ase/sap_ase.py
           #
           properties:
             instanceName: ex-vm-ase-lin
             instanceType: n1-standard-16
             zone: us-central1-f
             subnetwork: example-sub-network
             linuxImage: family/sles-12-sp2-sap
             linuxImageProject: suse-sap-cloud
             aseSID: AS1
             asesidSize: 10
             asediagSize: 15
             asesaptempSize: 20
             asesapdataSize: 50
             aselogSize: 30
             asebackupSize: 100
             asesapdataSSD: Yes
             aselogSSD: Yes
             usrsapSize: 15
             sapmntSize: 15
             swapSize: 24

  6. Create the VM instance:
         
         gcloud deployment-manager deployments create DEPLOYMENT_NAME --config TEMPLATE_NAME.yaml

The above command invokes the Deployment Manager, which deploys the VM according to the specifications in your `template.yaml` file. The process might take a few minutes. To check the progress of your deployment, follow the steps in the next section.




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

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the SAP ASE requirements that are listed in the [SAP ASE planning guide](https://docs.cloud.google.com/sap/docs/sap-ase-planning-guide#pricing-and-quotas).

       2. On the Deployment Manager [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.

       3. Rerun your deployment.




#### Check the configuration of the VM

  1. After the SAP ASE system deploys without errors, connect to your VM by using SSH. From the Compute Engine [VM instances page](https://console.cloud.google.com/compute/instances), you can click the SSH button for your VM instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ase-ssh-button.png)

  2. Switch to the root user.
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output similar to the following, such as the `//sybase/DBSID/sapdata` directory.

![Data volumes created by the script.](https://docs.cloud.google.com/static/sap/docs/images/ase-data-volumes-linux.png)

  4. Confirm that the swap directory was created by entering the following command:
         
         cat /proc/meminfo | grep Swap

You should see results similar to the following example:

![Example of terminal output when the swap directory exits.](https://docs.cloud.google.com/static/sap/docs/images/ase-swap-verify-linux.png)




If any of the validation steps show that the installation failed:

  1. Correct the error.
  2. On the [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.
  3. Rerun your deployment.



## Installing the database

Now that your operating system is configured, you can install your SAP ASE database:

To install SAP ASE on your VM:

  1. Establish an SSH connection to your Linux-based VM.
  2. Download or copy your SAP ASE installation media from SAP to your VM.
  3. Prepare your SAP ASE SySAM license file or license server for use with the installation.
  4. Install the SAP ASE database. See the [SAP ASE Installation and Upgrade Guide for Linux](https://help.sap.com/viewer/23c3bb4a29be443ea887fa10871a30f8/latest) for guidance.



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

Before using your SAP ASE instance, we recommend that you perform the following post-deployment steps:

  1. Update your SAP ASE software with the latest patches, if available.
  2. Install any additional components.
  3. Configure and back up your new SAP ASE database.



For additional post-deployment guidance, see the Post-installation Tasks section of the [SAP ASE Installation and Upgrade Guide for Linux](https://help.sap.com/viewer/23c3bb4a29be443ea887fa10871a30f8/latest/en-US/a6e8dcfbbc2b1014a59bceaf9d7f47ce.html).

## Troubleshooting

This section contains information about how to correct common issues.

### Troubleshooting connecting to your VM

If you are having issues connecting to your VM through SSH, then make sure that you have created a firewall rule to open port `22` on the Google Cloud network you are using.

For other possible issues, see [Known issues](https://docs.cloud.google.com/compute/docs/ssh-in-browser#known_issues) for SSH from the browser.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
