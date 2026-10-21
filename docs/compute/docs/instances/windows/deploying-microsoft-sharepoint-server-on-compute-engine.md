---
url: https://docs.cloud.google.com/compute/docs/instances/windows/deploying-microsoft-sharepoint-server-on-compute-engine/
title: Deploying Microsoft SharePoint Server on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:36.588993+00:00
---

# Deploying Microsoft SharePoint Server on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/deploying-microsoft-sharepoint-server-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deploying Microsoft SharePoint Server on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how you can deploy Microsoft SharePoint Server on Compute Engine. The guide applies to Microsoft SharePoint Server 2016 and Microsoft SharePoint Server 2019.

The SharePoint deployment will use six servers across two zones. This setup corresponds to the [Medium High Availability (Search optimized)](https://docs.microsoft.com/en-us/sharepoint/install/planning-for-a-minrole-server-deployment-in-sharepoint-server) MinRole farm topology.

The following diagram illustrates the deployment:

![Deployment of Microsoft Exchange](https://docs.cloud.google.com/static/architecture/images/sharepoint-architecture.svg)

The article assumes that you have already deployed Active Directory and SQL Server on [Google Cloud](https://docs.cloud.google.com/) and that you have basic knowledge of SharePoint Server, Active Directory, and Compute Engine.

## Objectives

  * Prepare a project for the deployment of SharePoint Server.
  * Deploy a [MinRole SharePoint farm](https://docs.microsoft.com/en-us/sharepoint/install/overview-of-minrole-server-roles-in-sharepoint-server) that uses six servers:

    * Two frontend with servers with distributed cache
    * Two application servers
    * Two search servers
  * Configure load balancing and firewall rules




## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



Use the [Pricing Calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

## Before you begin

To complete this guide, you need the following:

  * An existing Active Directory domain with at least one domain controller. You can use either [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) or a self-managed Active Directory domain.
  * An administrative Active Directory that has permission to join computers, create user accounts, and add DNS records.
  * A Google Cloud project and VPC with connectivity to your Active Directory domain controllers.
  * A SQL Server instance that is joined to the Active Directory domain and can be used for SharePoint. For further details on how to set up a highly available SQL Server deployment on Google Cloud, see [Deploying a Multi-Subnet SQL Server Always-On Availability Group](https://docs.cloud.google.com/solutions/deploy-multi-subnet-sql-server).
  * A subnet for the SharePoint VM instances. The subnet must span at least two zones.

**Note:** If you use a self-managed Active Directory domain, make sure you have a private DNS forwarding zone set up that [forwards DNS queries to your domain controllers](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones).

Before you begin the deployment, review the [system requirements for SharePoint Server 2016 and 2019.](https://docs.microsoft.com/en-us/sharepoint/install/system-requirements-for-sharepoint-server-2016).

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Preparing the project and network

To prepare your Google Cloud project and VPC for the deployment of SharePoint Server, do the following:

  1. Switch to your project in the Google Cloud console and open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Initialize the following variables:
         
         VPC_NAME=VPC_NAME
         SUBNET_NAME=SUBNET_NAME
         SUBNET_REGION=SUBNET_REGION
         SUBNET_ZONE_1=$SUBNET_REGION-a
         SUBNET_ZONE_2=$SUBNET_REGION-b
         

Where:

     * VPC_NAME is the name of your VPC.
     * SUBNET_NAME is the name of your subnet.
     * SUBNET_REGION is the region of your subnet.
  3. Set your default [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):
         
         gcloud config set project PROJECT_ID
         

Replace PROJECT_ID with the ID of your Google Cloud project.




### Creating firewall rules

To enable communication between the servers of your SharePoint farm, you need to create several firewall rules. To simplify the creation of these firewall rules, you use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags):

  * Frontend servers are annotated with the `sharepoint-frontend` tag.
  * Application servers are annotated with the `sharepoint-application` tag.
  * Search servers are annotated with the `sharepoint-search` tag.
  * All servers are also annotated with the `sharepoint`tag.



Create firewall rules that use these network tags and permit communication over the [ports that SharePoint requires](https://docs.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/security-hardening):

  1. Return to your existing Cloud Shell session.
  2. Create firewall rules for the SharePoint servers:
         
         gcloud compute firewall-rules create allow-http-between-sharepoint-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:80,tcp:443,tcp:32843,tcp:32844 \
           --enable-logging \
           --source-tags=sharepoint \
           --target-tags=sharepoint \
           --network=$VPC_NAME \
           --priority=10000
         
         gcloud compute firewall-rules create allow-search-between-sharepoint-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:16500-16519 \
           --enable-logging \
           --source-tags=sharepoint \
           --target-tags=sharepoint \
           --network=$VPC_NAME \
           --priority=10000
         
         gcloud compute firewall-rules create allow-rpc-between-sharepoint-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:135,tcp:49152-65535 \
           --enable-logging \
           --source-tags=sharepoint \
           --target-tags=sharepoint \
           --network=$VPC_NAME \
           --priority=10000
         
         gcloud compute firewall-rules create allow-wcf-between-sharepoint-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:808 \
           --enable-logging \
           --source-tags=sharepoint \
           --target-tags=sharepoint \
           --network=$VPC_NAME \
           --priority=10000
         
         gcloud compute firewall-rules create allow-appfabric-from-sharepoint-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:22233-22236 \
           --enable-logging \
           --source-tags=sharepoint \
           --target-tags=sharepoint-frontend \
           --network=$VPC_NAME \
           --priority=10000
         

  3. Create a firewall rule that permits all servers to connect to the SQL Server instances. If your SQL Server instances use a network tag `sql-server`, you can use the following command to create a firewall rule:
         
         gcloud compute firewall-rules create allow-sql-from-sharepoint-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:1433 \
           --enable-logging \
           --source-tags=sharepoint \
           --target-tags=sql-server \
           --network=$VPC_NAME \
           --priority=10000
         

See [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) for alternative ways to create a firewall rule if your SQL Server instance does not use a network tag.


**Note:** Depending on how you've deployed Active Directory, you might need to create additional firewall rules to allow SharePoint servers to join the domain. See [Accessing Managed Microsoft AD from within your VPC](https://docs.cloud.google.com/managed-microsoft-ad/docs/firewalls#accessing_from_within_your_vpc) for further details.

Your project and VPC are now ready for the deployment of SharePoint.

### Creating an installation disk

Your next step is to create a disk that contains the SharePoint Server installation media. By creating a disk that you can attach to multiple VM instances, you avoid having to download the installation media to each VM instance individually.

  1. Follow the instructions in [Creating an image from an ISO file](https://docs.cloud.google.com/compute/docs/images/creating-an-image-from-an-iso-file). Use the following URL as the download URL:

###  SharePoint Server 2016 
         
         https://download.microsoft.com/download/0/0/4/004EE264-7043-45BF-99E3-3F74ECAE13E5/officeserver.img
         

###  SharePoint Server 2019 
         
         https://download.microsoft.com/download/C/B/A/CBA01793-1C8A-4671-BE0D-38C9E5BBD0E9/officeserver.img
         

  2. Use the new image to create a disk in the first zone:
         
         gcloud compute disks create sharepoint-media-1 \
           --zone=$SUBNET_ZONE_1 \
           --image-project=$GOOGLE_CLOUD_PROJECT \
           --image=IMAGE
         

Replace IMAGE with the name of the image that you created in the previous step.

  3. Create a disk in the second zone:
         
         gcloud compute disks create sharepoint-media-2 \
           --zone=$SUBNET_ZONE_2 \
           --image-project=$GOOGLE_CLOUD_PROJECT \
           --image=IMAGE
         

Replace IMAGE with the name of the image that you created in the first step.




### Creating a SharePoint image

To avoid the repetitive task of installing SharePoint components on all servers individually, you now create a custom [VM image](https://docs.cloud.google.com/compute/docs/images). You later use this VM image as a [virtual machine template](https://docs.microsoft.com/en-us/sharepoint/install/deploy-sharepoint-virtual-machines#virtual-machine-templates) to deploy the SharePoint servers.

  1. Return to your existing Cloud Shell session.
  2. Create a [specialize script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the VM instance. The script will run during VM initialization and install the [SharePoint prerequisites](https://docs.microsoft.com/en-us/sharepoint/install/prerequisites-2019):
         
         cat << "EOF" > specialize.ps1
         $ErrorActionPreference = "stop"
         
         # Allow HTTP/HTTPS redirects so that the prerequisite installer can run
         Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name WarnonZoneCrossing -Value 0 -Type DWord
         
         # Install prerequisites
         & d:\prerequisiteinstaller.exe /unattended | Out-Default
         
         # Install logging agent
         (New-Object Net.WebClient).DownloadFile(
             "https://dl.google.com/cloudagents/windows/StackdriverLogging-v1-10.exe",
             "$env:Temp\StackdriverLogging-v1-10.exe")
         & $env:Temp\StackdriverLogging-v1-10.exe /S | Out-Default
         
         # Disable Windows firewall (because VPC firewall rules are used instead)
         & netsh advfirewall set allprofiles state off | Out-Default
         EOF
         

  3. Create the VM instance and assign `specialize.ps1` for the specialize script value. Attach the SharePoint installation disk in read-only mode so that you can launch the SharePoint installer from this disk:
         
         gcloud compute instances create sp-template \
           --image-family=windows-2019 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-2 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --zone=$SUBNET_ZONE_1 \
           --tags=sharepoint \
           --disk=name=sharepoint-media-1,auto-delete=no,mode=ro \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize.ps1
          

  4. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output sp-template --zone=$SUBNET_ZONE_1
         

Wait about 10 minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the installation of prerequisites is complete and the VM instance is ready to be used.

  5. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

  6. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using the username and password created in the previous step.

  7. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

  8. Confirm the elevation prompt by clicking **Yes**.

  9. Start the SharePoint installer:
         
         & d:\setup.exe
         

  10. Follow the instructions of the wizard. When you're prompted for a product key, use the **Enterprise trial product key** that's listed under **Install Instructions** on the Sharepoint download page, or use a key that you already have.

     * [SharePoint Server 2016 download page](https://www.microsoft.com/en-us/download/details.aspx?id=51493)
     * [SharePoint Server 2019 download page](https://www.microsoft.com/en-us/download/details.aspx?id=57462)
  11. When the installation is finished, click **Close**.

**Note:** Don't run the SharePoint Products Configuration wizard, and don't reboot the server yet.
  12. In PowerShell, download and install Chrome:
         
         Start-BitsTransfer `
             -Source 'https://dl.google.com/chrome/install/latest/chrome_installer.exe' `
             -Destination "$env:Temp\chrome_installer.exe"
         & $env:Temp\chrome_installer.exe
         

  13. In Chrome, download and install the following updates:

###  SharePoint Server 2016 

     1. [Security Update for Microsoft SharePoint Enterprise Server 2016 (KB4011127)](https://www.microsoft.com/en-us/download/details.aspx?id=55914).
     2. [Update for Microsoft SharePoint Enterprise Server 2016 (KB4011053)](https://www.microsoft.com/en-us/download/details.aspx?id=55720).

     3. Check and install [additional updates](https://docs.microsoft.com/en-us/officeupdates/sharepoint-updates#sharepoint-2016-update-history) if necessary.

###  SharePoint Server 2019 

     1. Check and install [updates](https://docs.microsoft.com/en-us/officeupdates/sharepoint-updates#sharepoint-2016-update-history) if necessary.

  14. Return to the PowerShell console and [generalize the image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image):
         
         & gcesysprep
         

The command automatically shuts down the VM. Wait about 5 minutes for this process to complete.

  15. In Cloud Shell, create a VM image from the VM's boot disk:
         
         gcloud compute images create sharepoint \
           --source-disk=sp-template \
           --source-disk-zone=$SUBNET_ZONE_1
         

  16. Delete the VM instance:
         
         gcloud compute instances delete sp-template --zone=$SUBNET_ZONE_1
         




### Creating VMs and joining them to Active Directory

Follow these steps to create the VM instances for the SharePoint farm and join them to your existing Active Directory domain:

  1. Return to your existing Cloud Shell session.
  2. Create two VM instances for the frontend servers:
         
         gcloud compute instances create sp-frontend-1 \
           --zone=$SUBNET_ZONE_1 \
           --machine-type=n1-standard-8 \
           --boot-disk-size=200 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --tags=sharepoint,sharepoint-frontend \
           --image=sharepoint \
           --image-project=$GOOGLE_CLOUD_PROJECT
         
         gcloud compute instances create sp-frontend-2 \
           --zone=$SUBNET_ZONE_2 \
           --machine-type=n1-standard-8 \
           --boot-disk-size=200 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --tags=sharepoint,sharepoint-frontend \
           --image=sharepoint \
           --image-project=$GOOGLE_CLOUD_PROJECT
         

  3. Create two VM instances for the application servers:
         
         gcloud compute instances create sp-app-1 \
           --zone=$SUBNET_ZONE_1 \
           --machine-type=n1-standard-8 \
           --boot-disk-size=200 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --tags=sharepoint,sharepoint-application \
           --image=sharepoint \
           --image-project=$GOOGLE_CLOUD_PROJECT \
           "--metadata=sysprep-specialize-script-ps1=Add-WindowsFeature RSAT-AD-PowerShell;Add-WindowsFeature RSAT-DNS-Server"
         
         gcloud compute instances create sp-app-2 \
           --zone=$SUBNET_ZONE_2 \
           --machine-type=n1-standard-8 \
           --boot-disk-size=200 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --tags=sharepoint,sharepoint-application \
           --image=sharepoint \
           --image-project=$GOOGLE_CLOUD_PROJECT \
           "--metadata=sysprep-specialize-script-ps1=Add-WindowsFeature RSAT-AD-PowerShell;Add-WindowsFeature RSAT-DNS-Server"
         

  4. Create two VM instances for the search servers:
         
         gcloud compute instances create sp-search-1 \
           --zone=$SUBNET_ZONE_1 \
           --machine-type=n1-standard-8 \
           --boot-disk-size=200 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --tags=sharepoint,sharepoint-search \
           --image=sharepoint \
           --image-project=$GOOGLE_CLOUD_PROJECT
         
         gcloud compute instances create sp-search-2 \
           --zone=$SUBNET_ZONE_2 \
           --machine-type=n1-standard-8 \
           --boot-disk-size=200 \
           --boot-disk-type=pd-ssd \
           --subnet=$SUBNET_NAME \
           --tags=sharepoint,sharepoint-search \
           --image=sharepoint \
           --image-project=$GOOGLE_CLOUD_PROJECT
         

  5. Monitor the initialization process of the last VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output sp-search-2 --zone=$SUBNET_ZONE_2
         

Wait about 2 minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

  6. For each of the six VM instances, perform the following steps:

     1. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance.
     2. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using the username and password created in the previous step.
     3. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
     4. Confirm the elevation prompt by clicking **Yes**.
     5. Join the computer to your Active Directory domain:
            
            Add-Computer -Domain DOMAIN
            

Replace DOMAIN with the DNS name of your Active Directory domain.

     6. Restart the computer:
            
            Restart-Computer
            

Wait for approximately 1 minute for the restart to complete.




## Creating the SharePoint servers

You now use the custom image to create the VM instances for your SharePoint farm.

The VM instances use the `n1-standard-8` machine type. Depending on how you plan to use the SharePoint farm, you might need to use larger machine types. Consult the hardware requirements for a more detailed analysis of your needs and their system requirements:

  * [Hardware and software requirements for SharePoint Server 2016](https://docs.microsoft.com/en-us/sharepoint/install/hardware-and-software-requirements)
  * [Hardware and software requirements for SharePoint Server 2019](https://docs.microsoft.com/en-us/sharepoint/install/hardware-and-software-requirements-2019)



### Setting up load balancing

To enable clients to access SharePoint by using a single virtual IP address, you use an [internal load balancer](https://docs.cloud.google.com/load-balancing/docs/internal). The load balancer distributes requests among the two frontend servers, `sp-frontend-1` and `sp-frontend-2`.

To associate the two frontend servers with the load balancer, you first create two [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups), and then assign these instance group to the load balancer:

  1. Return to your existing Cloud Shell session.
  2. Create one [unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances) per zone:
         
         gcloud compute instance-groups unmanaged create sp-frontend-1 --zone=$SUBNET_ZONE_1
         
         gcloud compute instance-groups unmanaged create sp-frontend-2 --zone=$SUBNET_ZONE_2
         

  3. Add the VM instances running the frontend servers to the instance groups:
         
         gcloud compute instance-groups unmanaged add-instances sp-frontend-1 \
           --instances sp-frontend-1 \
           --zone=$SUBNET_ZONE_1
         
         gcloud compute instance-groups unmanaged add-instances sp-frontend-2 \
           --instances sp-frontend-2 \
           --zone=$SUBNET_ZONE_2
         

  4. Create a health check that probes the HTTP path of Sharepoint:
         
         gcloud compute health-checks create tcp sp-health-check --port 80
         

  5. Create a load balancer backend and add the two instance groups:
         
         gcloud compute backend-services create sp-backend \
           --load-balancing-scheme internal \
           --region=$SUBNET_REGION \
           --health-checks sp-health-check \
           --protocol=tcp
         
         gcloud compute backend-services add-backend sp-backend \
           --instance-group=sp-frontend-1 \
           --instance-group-zone=$SUBNET_ZONE_1 \
           --region=$SUBNET_REGION
         
         gcloud compute backend-services add-backend sp-backend \
           --instance-group=sp-frontend-2 \
           --instance-group-zone=$SUBNET_ZONE_2 \
           --region=$SUBNET_REGION
         

  6. Reserve a static IP address for the load balancer: \
         
         gcloud compute addresses create sp-frontend \
           --region=$SUBNET_REGION \
           --subnet=$SUBNET_NAME
         

  7. Create a forwarding rule for the load balancer:
         
         gcloud compute forwarding-rules create sp-frontend \
           --load-balancing-scheme=internal \
           --ports=80 \
           --network=$VPC_NAME \
           --subnet=$SUBNET_NAME \
           --region=$SUBNET_REGION \
           --address=sp-frontend \
           --backend-service=sp-backend
         

  8. Create a firewall rule to allow traffic from the load balancer to the backend services:
         
         gcloud compute firewall-rules create allow-http-health-checks \
           --network=$VPC_NAME --allow tcp:80 \
           --source-ranges=130.211.0.0/22,35.191.0.0/16 \
           --target-tags="sharepoint-frontend"
         

The source ranges are the IP ranges for the internal load balancer. For more information, see [Configure a firewall rule to allow internal load balancing](https://docs.cloud.google.com/compute/docs/load-balancing/internal#configure-a-firewall-rule-to-allow-internal-load-balancing).

  9. Look up the IP address of the load balancer:
         
         gcloud compute addresses describe sp-frontend \
           --region=$SUBNET_REGION \
           --format=value\(address\)
         

You need this IP address later after you have deployed the SharePoint farm.

**Note:** The load balancer won't be in a healthy state until the SharePoint farm is deployed and fully configured.



### Registering the load balancer in DNS

To allow clients to use a human-readable URL to access SharePoint, register a name for the load balancer in DNS:

  1. Connect to `sp-app-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in as a user that is a member of the `DnsAdmins` group.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell**.
  3. Create a record that maps the name `sharepoint` to the IP address of the load balancer:
         
         Add-DnsServerResourceRecordA `
           -ComputerName (Get-ADDomainController).Hostname `
           -Name "sharepoint" `
           -ZoneName "DOMAIN" `
           -IPv4Address LOADBALANCER-IP
         

Where:

     * LOADBALANCER-IP is the IP address of the load balancer.
     * DOMAIN is the DNS domain of your Active Directory domain.



## Creating the SharePoint farm

Although the six servers have all required software packages installed, they are not yet part of a SharePoint farm. You now create the farm and add the servers to the farm by assigning them roles.

### Creating a farm service account

To create the SharePoint farm, you need to create a farm service account. The farm service account is an Active Directory user account that's used to run SharePoint services and to access SQL Server.

For further details on the farm service account, see [Account permissions and security settings in SharePoint Servers](https://docs.microsoft.com/en-us/sharepoint/install/account-permissions-and-security-settings-in-sharepoint-server-2016).

To create a farm service account in Active Directory, do the following:

  1. Return to the PowerShell prompt on `sp-app-1`.
  2. Define a password for the farm service account:
         
         $FarmServicePassword = Read-Host -Prompt "Enter password for Farm service account" -AsSecureString
         

  3. Create the farm service account in Active Directory:
         
         New-ADUser `
           -Name "SharePoint Service" `
           -SamAccountName sp-farm  `
           -UserPrincipalName "sp-farm@$((Get-ADDomain).DNSRoot)" `
           -AccountPassword $FarmServicePassword `
           -PassThru | Enable-ADAccount
         

  4. Grant the farm service account access to SQL Server by [creating a login](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-login?view=sql-server-ver15#SSMSProcedure) for `sp-farm`. Configure the login to use Windows authentication so that you don't need to assign a new password.




### Configuring the first server

You now create the SharePoint farm by configuring the first server. The first server is special because it hosts the central administration website. You use this site later to configure the farm.

  1. Return to the RDP session on `sp-app-1`.
  2. Click **Start** > **Microsoft SharePoint Products** > **SharePoint Products Configuration Wizard**.
  3. Follow the steps in [Create and configure the farm](https://docs.microsoft.com/en-us/sharepoint/install/install-sharepoint-server-2016-across-multiple-servers#create-and-configure-the-farm): 
     1. On the **Specify Configuration Database Settings** page, specify the name and password of the `sp-farm` user that you created earlier.
     2. On the **Specify Server Role** page, select **Application**.
     3. On the **Configure SharePoint Central Administration Web Application** page, specify port `8000`.
     4. After the configuration is complete, a browser window opens. Close the window and skip the remaining steps.
  4. Click **Start** > **Microsoft SharePoint Products** > **SharePoint Management Shell**.
  5. Apply pending SharePoint updates:
         
         PSConfig.exe -cmd upgrade -inplace b2b -force -cmd applicationcontent -install -cmd installfeatures
         




### Configuring remaining servers

You can now add the remaining servers to the SharePoint farm.

**VM instance** | **Role**  
---|---  
`sp-app-2` | **Application**  
`sp-frontend-1` | **Frontend with distributed cache**  
`sp-frontend-2` | **Frontend with distributed cache**  
`sp-search-1` | **Search**  
`sp-search-2` | **Search**  
  
For each VM, do the following:

  1. Connect to the VM [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in as a domain administrator user.
  2. Click **Start** > **Microsoft SharePoint Products** > **SharePoint Products Configuration Wizard**.
  3. On the **Welcome to SharePoint Products** page, click **Next**.
  4. In the dialog box that notifies you that some services might have to be restarted during configuration, click **Yes**.
  5. On the **Connect to a server farm** page, select **Connect to an existing server farm**.
  6. On the **Specify configuration database settings** page, specify the same database server and database name that you used for the first server.
  7. On the next page, enter the passphrase that you defined previously.
  8. On the **Specify server role** page, select the role that corresponds to the VM and click **Next**.
  9. On the **Completing the SharePoint products configuration wizard** page, confirm your configuration and click **Next**.
  10. On the **Configuration Successful** page, click **Finish**.

**Note:** If deploying the **Frontend with distributed cache** fails with the error `System.InvalidOperationException was thrown. Additional exception information: cacheHostInfo is null`, run the PowerShell script provided in [SharePoint 2016 Troubleshooting: Configuration Wizard failed with error 'CacheHostInfo is null'](https://social.technet.microsoft.com/wiki/contents/articles/34617.sharepoint-2016-troubleshooting-configuration-wizard-failed-with-error-cachehostinfo-is-null.aspx#PS_Script). Then run the configuration wizard again.
  11. Close the browser window.

  12. Click **Start** > **Microsoft SharePoint Products** > **SharePoint Management Shell**

  13. Apply pending SharePoint updates:
         
         PSConfig.exe -cmd upgrade -inplace b2b -force -cmd applicationcontent -install -cmd installfeatures
         

**Note:** Run the command on only one server at a time.



### Configuring the farm

You now use the SharePoint configuration wizard to finalize the configuration of the farm:

  1. Connect to `sp-app-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui).
  2. Click **Start** > **Google Chrome** to open the Chrome browser.
  3. Navigate to `http://sp-app-1:8000/configurationwizards.aspx`
  4. Log in using a domain admin user.
  5. Select **Launch the Farm Configuration Wizard**.
  6. On the **Welcome** page, select **Start the Wizard**.
  7. On the **Service Applications and Services** page, click **Use existing managed account** and select the `sp-farm` user.
  8. Verify the list of services to install and customize the selection according to your requirements.
  9. Select **Next** to start the configuration process.

The process takes approximately 10 to 15 minutes to complete.

  10. On the **Create Site Collection** page, specify a title and select a template, then click **OK**. See [Create a site collection by using Central Administration](https://docs.microsoft.com/en-us/sharepoint/sites/create-a-site-collection#create-a-site-collection-by-using-central-administration) for further details about creating sites.

  11. On the **This completes the Farm Configuration Wizard** page, select **Finish**.

  12. On the Central Administration home page, select **System Settings** > **Manage servers in farm**.

  13. Verify that all servers are marked as **Compliant** and that the status is marked as **No Action Required**.




For further information about managing the SharePoint farm, see [Managing a MinRole Server Farm in SharePoint Servers 2016 and 2019](https://docs.microsoft.com/en-us/sharepoint/administration/managing-a-minrole-server-farm-in-sharepoint-server-2016)

### Configuring alternate access mappings

To allow users to access the SharePoint site by using the DNS name of the load balancer, you now configure an alternate access mapping:

  1. On the Central Administration home page, select **System Settings** > **Configure alternate access mappings**.
  2. Next to **Alternate Access Mapping Collection** , select **Show All** > **Change alternate access mapping collection**.
  3. In the **Select alternate access mapping collection** dialog, select **SharePoint - 80**.
  4. Select **Edit public URLs**.
  5. Configure the following mapping:

     1. **Default** :
            
            http://sharepoint.DOMAIN
            

Where DOMAIN is the DNS domain of your Active Directory domain.

     2. Clear all other fields.

  6. Click **Save**.

  7. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

  8. To have the alternate access mapping take effect, restart IIS on all servers:
         
         "sp-app-1", "sp-app-2", "sp-frontend-1", "sp-frontend-2", "sp-search-1", "sp-search-2" | %  { & iisreset $_ }
         




Your SharePoint farm is now ready to use.

## Testing the SharePoint site

To verify that you can access the SharePoint site by using the DNS name of the load balancer, follow these steps:

  1. In Chrome, navigate to the following address:
         
         http://sharepoint.DOMAIN
         

Replace DOMAIN with the DNS domain of your Active Directory domain.

  2. Log in using an administrative domain user.

Because this is the first time you open the site, it takes several minutes for the site to initialize.

  3. Verify that you see the homepage of your SharePoint site.

  4. Under **Documents** , select **Upload**.

  5. Select a test document to upload to the site. You can use an empty Rich Text Document (`.rtf`) if you don't have a document available for testing.

  6. Click **OK** to upload the document.




SharePoint periodically crawls documents to update its search index. To avoid waiting for the crawl to happen, initiate a crawl manually:

  1. On `sp-app-1`, click **Start** > **Microsoft SharePoint Products** > **SharePoint Management Shell**.
  2. Start a full crawl:
         
         $Crawler = (Get-SPEnterpriseSearchServiceApplication |Get-SPEnterpriseSearchCrawlContentSource)
         $Crawler.StartFullCrawl()
         




Wait about 5 minutes for the crawl process to complete in the background.

You can now verify that the SharePoint search works by searching for the document that you uploaded previously:

  1. Return to Chrome and the SharePoint site.
  2. Search for the filename of the file you uploaded by using the search box.
  3. Verify that the file shows up in the search results.



## Clean up

To avoid incurring further costs after you have completed this tutorial, delete the entities that you've created.

### Delete the Google Cloud project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
