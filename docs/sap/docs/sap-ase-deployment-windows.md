---
url: https://docs.cloud.google.com/sap/docs/sap-ase-deployment-windows/
title: Deployment Manager: Automated VM deployment for SAP ASE on Windows \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:43.991867+00:00
---

# Deployment Manager: Automated VM deployment for SAP ASE on Windows  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-ase-deployment-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deployment Manager: Automated VM deployment for SAP ASE on Windows Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Deployment Manager reaches end of support on March 31, 2026. For more information, see [Cloud Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

To automate the deployment of a single-node SAP ASE system on Windows on Google Cloud, contact [Cloud Customer Care](https://cloud.google.com/support).

This deployment guide shows you how to deploy and connect to a Compute Engine virtual machine (VM) that is ready for the installation of SAP Adaptive Server Enterprise (ASE) on a Windows Server operating system.

The instructions in this guide use [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/fundamentals) to deploy and configure the VM, the Windows Server operating system, and the required disk volumes for SAP ASE.

For details on planning your deployment, see the [SAP ASE planning guide](https://docs.cloud.google.com/sap/docs/sap-ase-planning-guide).

## Prerequisites

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

If you do not already have a Google Cloud project with billing enabled, you must create one before you can deploy a VM for your SAP ASE installation.

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
  * RDP connections to your VM instance. The default RDP port number is `3389`.
  * PowerShell connections to your VM instance. The default RDP port number is `5986`.

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

## Deploying a Windows VM for SAP ASE with Deployment Manager

The following instructions use Deployment Manager to deploy a VM instance with Windows and all of the persistent disks that SAP ASE requires. You define the values for the installation in a Deployment Manager configuration file template.

Deployment Manager treats all of the resources that are created for the SAP ASE system as a single entity called a _deployment._ You can view all of the deployments for your Google Cloud project on the [Deployments](https://console.cloud.google.com/dm/deployments) page in the Google Cloud console.

**Note:** Deleting a deployment deletes all of the resources associated with the deployment, including the SAP ASE system, the VMs, and the persistent disks that were deployed with it.

The following instructions use Cloud Shell, but if you prefer, you can use the Google Cloud CLI in your local terminal instead.

  1. Open the Cloud Shell.

[Go to the Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the `template.yaml` configuration file template to your working directory by entering the following command in the Cloud Shell:
         
         wget https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_ase-win/template.yaml

  3. Optionally, rename the `template.yaml` file to identify the configuration it defines.

  4. Open the `template.yaml` file in Cloud Shell code editor.

To open the Cloud Shell code editor, click the pencil icon in the upper-right corner of the Cloud Shell terminal window.

  5. In the `template.yaml` file, update the following property values by replacing the brackets and their contents with the values for your installation.

Property | Data type | Description  
---|---|---  
type | String |  Specifies the location, type, and version of the Deployment Manager template to use during deployment.  The YAML file includes two `type` specifications, one of which is commented out. The `type` specification that is active by default specifies the template version as `latest`. The `type` specification that is commented out specifies a specific template version with a timestamp.  If you need all of your deployments to use the same template version, use the `type` specification that includes the timestamp.   
instanceName | String | The name of the VM instance on which SAP ASE will be installed. The name must be 13 characters or less and be specified in lowercase letters, numbers, or hyphens.   
instanceType | String | The type of Compute Engine [virtual machine](https://docs.cloud.google.com/compute/docs/machine-types) on which SAP ASE will be installed. If you are running SAP ASE with SAP NetWeaver on the same VM, select a machine type that includes enough CPUs and memory to support both systems. See the [SAP NetWeaver Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types).   
zone | String | The zone in which you are deploying your SAP ASE. It must be in the same region that you selected for your subnetwork.   
subnetwork | String | The name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, specify this value as `[SHAREDVPC_PROJECT]/[SUBNETWORK]`. For example, `myproject/network1`.  
windowsImage | String | The name of the Windows operating- system image or image family that you are using with SAP ASE. To specify an image family, add the prefix `family/` to the family name. For example, `family/windows-2012-r2`. To specify a specific image, specify only the image name. For the list of available image families, see the [Images](https://console.cloud.google.com/compute/images) page in the Cloud console.  
windowsImageProject | String | The Google Cloud project that contains the image you are going to use. This project might be your own project or a Google Cloud image project, such as `windows-cloud`. For a list of Google Cloud image projects, see the [Images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.  
asesidSize | Integer | The size in GB of **ASE (D:)** , which is the root directory of the database instance.   
asesaptempSize | Integer | The size of **ASE Temp (T:)** , which holds the database temporary table space.  
asesapdataSize | Integer | The size of **ASE Data (E:)** , which holds the database data files. In the deployed VM, this volume is labeled `ASE Data`.   
aselogSize | Integer | The size of **ASE Log (L:)** , which holds the database transaction logs. In the deployed VM, this volume is labeled `ASE Log`.   
asebackupSize | Integer | The size of **Backup (X:)**. If set to 0 or omitted, no disk is created. In the deployed VM, this volume is labeled `Backup`.   
asesapdataSSD | boolean | The SSD toggle for the data drive. If set to true, the data disk will be SSD.  
aselogSSD | boolean | The SSD toggle for the log drive. If set to true, the log disk will be SSD.  
usrsapSize | Integer | Required only if you are installing SAP ASE to run with SAP NetWeaver on the same VM instance. In the deployed VM, this volume is labeled **SAP (S:)**.   
swapSize | Integer | Required only if you are installing SAP ASE to run with SAP NetWeaver on the same VM instance. In the deployed VM, this volume is labeled **Pagefile (P:)**.   
  
The following configuration file creates a VM that is configured to run both the SAP ASE database server and SAP NetWeaver. The configuration file directs Deployment Manager to deploy an n1-standard-16 virtual that is running a Windows Server 2012 operating system. The VM includes all of the directories that are required to run SAP ASE with NetWeaver.
         
         resources:
         - name: sap_ase-win
           type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/latest/dm-templates/sap_ase-win/sap_ase-win.py
           #
           # By default, this configuration file uses the latest release of the deployment
           # scripts for SAP on Google Cloud.  To fix your deployments to a specific release
           # of the scripts, comment out the type property above and uncomment the type property below.
           #
           # type: https://storage.googleapis.com/cloudsapdeploy/deploymentmanager/202103310846/dm-templates/sap_ase-win/sap_ase-win.py
           #
           properties:
             instanceName: ex-vm-ase-win
             instanceType: n1-standard-16
             zone: us-central1-f
             subnetwork: example-sub-network
             windowsImage: family/windows-2012-r2
             windowsImageProject: windows-cloud
             asesidSize: 10
             asesaptempSize: 20
             asesapdataSize: 50
             aselogSize: 30
             asebackupSize: 100
             asesapdataSSD: Yes
             aselogSSD: Yes
             usrsapSize: 15
             swapSize: 24

  6. Deploy the VM:
         
         gcloud deployment-manager deployments create [DEPLOYMENT-NAME] --config [TEMPLATE-NAME].yaml

The above command invokes the Deployment Manager, which deploys the VM, all according to the specifications in your template.yaml file. The process might take a few minutes. To check the progress of your deployment, follow the steps in the next section.




### Verifying deployment

To verify deployment, you check the deployment logs in Cloud Logging.

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




After the SAP ASE system deploys without errors, connect to your VM as described in the next section, Connecting to your VM, to confirm that all of the required data volumes exist and that they have the expected capacities. The `Pagefile` drive should be almost full.

![Disk drives created by Deployment Manager for ASE.](https://docs.cloud.google.com/static/sap/docs/images/ase-disk-drives-win.png)

If any of the validation steps show that the installation failed:

  1. Correct the error.
  2. On the [Deployments](https://console.cloud.google.com/dm/deployments) page, delete the deployment to clean up the VMs and persistent disks from the failed installation.
  3. Rerun your deployment.



## Connecting to your VM

To connect to a Windows-based VM, you must first generate a password for the VM. After you have a password, you can connect to the VM using RDP or PowerShell.

### Generating passwords

To generate or reset a password for a Windows VM on Google Cloud:

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Open the VM instance details page by clicking the name of the VM that you just created.

![VM name on the VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ase-select-win-vm.png)

  3. On the instance details page, click the **Set Windows Password** button. A password is generated for you. Copy the password and store it in a secure place.

![Set Windows password by clicking button on VM instance details page.](https://docs.cloud.google.com/static/sap/docs/images/ase-set-win-password.png)




### Using RDP

If your firewall rule allows access on port `3389`, you can use RDP to connect to a Windows instance and start a Remote Desktop session. Alternatively, you can connect to Windows instances using the PowerShell terminal.

Connect to the remote desktop on Windows instances by manually connecting through the Windows Remote Desktop Connection client or a third-party client:

  1. If you don't already have an RDP client, install one now. For information from Microsoft about available RDP clients, see [Remote Desktop clients](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).
  2. Get your Windows VM's external IP address. To find the VM IP address, you can use either of the following methods: 
     * In the Google Cloud console, go to the [VM Instances page](https://console.cloud.google.com/compute/instances).
     * Use the gcloud CLI to run `gcloud compute instances list` to list your VM instances with their external IP addresses.
  3. In your RDP client, provide your VM's external IP address as the IP address to connect to.
  4. Enter your sign-in information and leave the **Domain** field blank. If this is your first time connecting to this VM, or if you have forgotten your password, [create or reset your Windows password](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-dm#connecting_to_your_vm).



### Using PowerShell

  1. If you have not created a username and password on the Windows VM yet, create your Windows password.
  2. Add a firewall rule or edit your existing firewall rule to open port 5986 on the [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) where your Windows Server VM instance is located.
  3. On your local workstation, open the PowerShell terminal.
  4. Optionally, you can initialize a variable to hold your user credentials so you do not need to enter them each time you connect to the instance. If you skip this step, you receive a prompt for your username and password later.
         
         $credentials = Get-Credential
         

  5. Use the [Enter-PSSession command](https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.core/enter-pssession) to start a remote PowerShell session and include the flags to use SSL and skip credentials checks.
         
         Enter-PSSession -ComputerName [IP_ADDRESS] -UseSSL -SessionOption
         (New-PSSessionOption -SkipCACheck -SkipCNCheck) -Credential $credentials
         




## Installing the database

Now that your Windows operating system is configured, you can install your SAP ASE database.

To install SAP ASE on your VM:

  1. Use RDP or Windows PowerShell to connect to your Windows-based VM.
  2. Download or copy your SAP ASE installation media from SAP to your VM.
  3. Prepare your SAP ASE SySAM license file or license server for use with the installation.
  4. Install the SAP ASE database. See the [SAP ASE installation and upgrade guide for Windows](https://help.sap.com/viewer/36031975851a4f82b1022a9df877280b/latest) for guidance.



If you are using the always-on HADR option, repeat the above steps for your standby server. For additional HADR installation and configuration details, see the [SAP ASE HADR users guide](https://help.sap.com/viewer/efe56ad3cad0467d837c8ff1ac6ba75c/latest).

## Validate your installation of Google Cloud's Agent for SAP

After you have deployed a VM and installed your SAP system, validate that Google Cloud's Agent for SAP is functioning properly.

### Verify that Google Cloud's Agent for SAP is running

To verify that the agent is running, follow these steps:

  1. Use RDP to connect to the Compute Engine instance.

  2. As an administrator, run the following command from PowerShell: 
         
         $(Get-Service -Name 'google-cloud-sap-agent' -ErrorAction Ignore).Status

If the agent is running, then the status shows `Running`.



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



For additional post-deployment guidance, see the Post-installation Tasks section of the [SAP ASE installation and upgrade guide for Windows](https://help.sap.com/viewer/36031975851a4f82b1022a9df877280b/latest/en-US/a6e8dcfbbc2b1014a59bceaf9d7f47ce.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
