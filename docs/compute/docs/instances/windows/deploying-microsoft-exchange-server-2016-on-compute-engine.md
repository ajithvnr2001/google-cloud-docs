---
url: https://docs.cloud.google.com/compute/docs/instances/windows/deploying-microsoft-exchange-server-2016-on-compute-engine/
title: Deploying Microsoft Exchange Server 2016 on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:34.250406+00:00
---

# Deploying Microsoft Exchange Server 2016 on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/deploying-microsoft-exchange-server-2016-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deploying Microsoft Exchange Server 2016 on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how you can deploy Microsoft Exchange Server 2016 on Compute Engine and configure it for [high availability and site resilience](https://docs.microsoft.com/en-us/exchange/high-availability/high-availability?view=exchserver-2016).

The Exchange deployment will span two zones within a single region. In each zone, you will deploy a mailbox server and an edge transport server. The mailbox servers will be part of a database availability group so that mailbox data is replicated across zones.

The following diagram illustrates the deployment:

![Deployment of Microsoft Exchange](https://docs.cloud.google.com/static/architecture/images/exchange-architecture.svg)

The article assumes that you have already deployed Active Directory on [Google Cloud](https://docs.cloud.google.com/) and that you have basic knowledge of Exchange Server 2016, Active Directory, and Compute Engine.

## Objectives

  * Set up a project and a VPC network, and prepare them for the deployment of Exchange Server 2016.
  * Deploy Exchange mailbox servers across two zones and create a [database availability group](https://docs.microsoft.com/en-us/exchange/high-availability/database-availability-groups/database-availability-groups?view=exchserver-2016).
  * Deploy Exchange edge transport servers across two zones.
  * Configure load balancing and firewall rules.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)



Use the [Pricing Calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

## Before you begin

To complete this guide, you need the following:

  * An existing Active Directory domain with at least one domain controller. The Active Directory domain must use a valid, publicly routable DNS domain name. Local domain names such as `corp.local` or [reserved domain names](https://tools.ietf.org/html/rfc2606) such as `example.com` can't be used.

Refer to [Deploying a fault-tolerant Microsoft Active Directory environment](https://docs.cloud.google.com/solutions/deploy-fault-tolerant-active-directory-environment) for further details on how you can deploy an Active Directory environment on Compute Engine.

  * A private DNS forwarding zone for the DNS domain name of Active Directory that forwards DNS queries to your domain controllers.

  * Administrative access to your Active Directory domain.

  * A Google Cloud project and VPC with connectivity to your Active Directory domain controllers.

  * A subnet to use for the Exchange VM instances. The subnet must span at least two zones.


**Note:** Deploying Exchange Server requires that you extend the schema of your Active Directory domain. Managed AD currently does not support schema extensions. The tutorial therefore requires you to use self-managed Active Directory domain controllers.

Before you begin the deployment, review the [high availability and site resilience requirements for Exchange Server.](https://docs.microsoft.com/en-us/exchange/high-availability/plan-ha?view=exchserver-2016).

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Preparing the project and network

To prepare your Google Cloud project and VPC for the deployment of Exchange Server, do the following:

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




### Creating an installation disk

You now create a disk that contains the installation Exchange Server installation media. By creating a disk that you can attach to multiple VM instances, you avoid having to download the installation media to each VM instance individually.

  1. Follow the instructions in [Creating an image from an ISO file](https://docs.cloud.google.com/compute/docs/images/creating-an-image-from-an-iso-file). Use the following URL as download URL:
         
         https://download.microsoft.com/download/6/6/F/66F70200-E2E8-4E73-88F9-A1F6E3E04650/ExchangeServer2016-x64-cu11.iso
         

  2. Use the new image to create a disk in the first zone:
         
         gcloud compute disks create exchange-media-1 \
           --zone=$SUBNET_ZONE_1 \
           --image-project=$GOOGLE_CLOUD_PROJECT \
           --image=IMAGE
         

Replace IMAGE with the name of the image that you created in the previous step.

  3. Create a disk in the second zone:
         
         gcloud compute disks create exchange-media-2 \
           --zone=$SUBNET_ZONE_2 \
           --image-project=$GOOGLE_CLOUD_PROJECT \
           --image=IMAGE
         

Replace IMAGE with the name of the image that you created in the first step.




### Creating firewall rules

To allow [clients to connect to Exchange and to enable communication between Exchange servers](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2016), you need to create several firewall rules. To simplify the creation of these firewall rules, you use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags):

  * Edge transport servers are annotated with the `exchange-transport` tag.
  * Mailbox servers are annotated with the `exchange-mailbox` tag.
  * The witness server is annotated with the `exchange-witness` tag.
  * All servers are annotated with the `exchange` tag.



Create firewall rules that use these network tags:

  1. Return to your existing Cloud Shell session.
  2. Create firewall rules for the mailbox servers:
         
         gcloud compute firewall-rules create allow-all-between-exchange-servers \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp,udp,icmp \
           --enable-logging \
           --source-tags=exchange \
           --target-tags=exchange \
           --network=$VPC_NAME \
           --priority 10000
         
         gcloud compute firewall-rules create allow-smtp-from-transport-to-mailbox \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:25 \
           --enable-logging \
           --source-tags=exchange-transport \
           --target-tags=exchange-mailbox \
           --network=$VPC_NAME \
           --priority 10000
         
         gcloud compute firewall-rules create allow-edgesync-from-mailbox-to-transport \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:50636 \
           --enable-logging \
           --source-tags=exchange-mailbox \
           --target-tags=exchange-transport \
           --network=$VPC_NAME \
           --priority 10000
         
         gcloud compute firewall-rules create allow-mail-to-mailbox \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:25,tcp:110,tcp:135,tcp:143,tcp:443,tcp:993,tcp:995 \
           --enable-logging \
           --target-tags=exchange-mailbox \
           --network=$VPC_NAME \
           --priority 10000
         
         gcloud compute firewall-rules create allow-smb-within-dag \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:135,tcp:445,udp:445,tcp:49152-65535 \
           --enable-logging \
           --source-tags=exchange-mailbox,exchange-witness \
           --target-tags=exchange-mailbox,exchange-witness \
           --network=$VPC_NAME \
           --priority 10000
         

  3. Create a firewall rule for the edge transport server:
         
         gcloud compute firewall-rules create allow-smtp-to-transport \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:25 \
           --enable-logging \
           --target-tags=exchange-transport \
           --network=$VPC_NAME \
           --priority 10000
         




Your project and VPC are now ready for the deployment of Exchange Server.

## Deploying the mailbox role

You now deploy the [mailbox servers](https://docs.microsoft.com/en-us/exchange/architecture/architecture?view=exchserver-2016#mailbox-servers) and a management server that you use to administer Exchange.

The VM instances will use the `n1-standard-8` [machine type](https://docs.cloud.google.com/compute/docs/machine-types). For a more detailed analysis of your needs and their system requirements, see the [Find the permissions required to run any Exchange cmdlet](https://learn.microsoft.com/powershell/exchange/find-exchange-cmdlet-permissions?view=exchange-ps).

### Deploying the management server

Follow these steps to create a VM instance that serves as the management server:

  1. Return to your existing Cloud Shell session.
  2. Create a [specialize script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the VM instance. The script runs during VM initialization and installs the [client prerequisites for the Exchange 2016 management tools](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016#windows-client-prerequisites-for-the-exchange-2016-management-tools):
         
         cat << "EOF" > specialize-admin.ps1
         
         $ErrorActionPreference = "stop"
         
         # Install required Windows features
         Install-WindowsFeature RSAT-ADDS,RSAT-DNS-Server
         Enable-WindowsOptionalFeature -Online -FeatureName IIS-ManagementScriptingTools, `
             IIS-ManagementScriptingTools, `
             IIS-IIS6ManagementCompatibility, `
             IIS-LegacySnapIn, `
             IIS-ManagementConsole, `
             IIS-Metabase, `
             IIS-WebServerManagementTools, `
             IIS-WebServerRole
         
         # Install Visual C++ Redistributable Package for Visual Studio 2012
         (New-Object System.Net.WebClient).DownloadFile(
             'http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU3/vcredist_x64.exe',
             "$env:Temp\vcredist_2012_x64.exe")
         & $env:Temp\vcredist_2012_x64.exe /passive /norestart | Out-Default
         
         EOF
         

  3. Create a VM instance that uses `specialize-admin.ps1` as a specialize script and attach the Exchange installation disk as a secondary disk. You use the secondary disk later to install the Exchange management tools:
         
         gcloud compute instances create exchange-admin \
           --image-family=windows-2019 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-2 \
           --subnet=$SUBNET_NAME \
           --zone=$SUBNET_ZONE_1 \
           --tags=exchange \
           --disk=name=exchange-media-1,auto-delete=no,mode=ro \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-admin.ps1
         

  4. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output exchange-admin --zone=$SUBNET_ZONE_1
         

Wait about 5 minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

  5. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

  6. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using the username and password created in the previous step.

  7. Right-click the **Start** button (or press **Win+X**) and click **Command Prompt (Admin)**.

  8. Confirm the elevation prompt by clicking **Yes**.

  9. In the elevated command prompt, start a PowerShell session:
         
         powershell
         

  10. Join the computer to your Active Directory domain:
         
         Add-Computer -Domain DOMAIN
         

Replace DOMAIN with the DNS name of your Active Directory domain.

  11. Restart the computer:
         
         Restart-Computer
         

Wait approximately 1 minute for the restart to complete.

  12. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using a domain user that is a member of the **Enterprise Admins** group.

  13. Follow the instructions to [prepare the Active Directory schema and domains for Exchange Server](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2016). You can find the Exchange installation media on drive `D:`.

  14. Follow the instructions to [install the Exchange management tools](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/install-management-tools?view=exchserver-2016).




### Deploying the mailbox servers

You are now ready to deploy the VM instances that serve as mailbox servers:

  1. Return to your existing Cloud Shell session.
  2. Create a specialize script for the VM instance. The script runs during VM initialization and installs the [prerequisites for installing mailbox servers](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016#exchange-2016-mailbox-servers-on-windows-server-2016):
         
         cat << "EOF" > specialize-mailbox.ps1
         
         $ErrorActionPreference = "stop"
         
         # Install required Windows features
         Install-WindowsFeature RSAT-ADDS
         Install-WindowsFeature `
             NET-Framework-45-Features, `
             Server-Media-Foundation, `
             RPC-over-HTTP-proxy, `
             RSAT-Clustering, `
             RSAT-Clustering-CmdInterface, `
             RSAT-Clustering-Mgmt, `
             RSAT-Clustering-PowerShell, `
             WAS-Process-Model, `
             Web-Asp-Net45, `
             Web-Basic-Auth, `
             Web-Client-Auth, `
             Web-Digest-Auth, `
             Web-Dir-Browsing, `
             Web-Dyn-Compression, `
             Web-Http-Errors, `
             Web-Http-Logging, `
             Web-Http-Redirect, `
             Web-Http-Tracing, `
             Web-ISAPI-Ext, `
             Web-ISAPI-Filter, `
             Web-Lgcy-Mgmt-Console, `
             Web-Metabase, `
             Web-Mgmt-Console, `
             Web-Mgmt-Service, `
             Web-Net-Ext45, `
             Web-Request-Monitor, `
             Web-Server, `
             Web-Stat-Compression, `
             Web-Static-Content, `
             Web-Windows-Auth, `
             Web-WMI, `
             Windows-Identity-Foundation, `
             RSAT-ADDS
         
         # Install Visual C++ Redistributable Package for Visual Studio 2012
         (New-Object System.Net.WebClient).DownloadFile(
             'http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU3/vcredist_x64.exe',
             "$env:Temp\vcredist_2012_x64.exe")
         & $env:Temp\vcredist_2012_x64.exe /passive /norestart | Out-Default
         
         # Visual C++ Redistributable Package for Visual Studio 2013
         (New-Object System.Net.WebClient).DownloadFile(
             'http://download.microsoft.com/download/2/E/6/2E61CFA4-993B-4DD4-91DA-3737CD5CD6E3/vcredist_x64.exe',
             "$env:Temp\vcredist_2013_x64.exe")
         & $env:Temp\vcredist_2013_x64.exe /passive /norestart | Out-Default
         
         # Install Microsoft Unified Communications Managed API
         (New-Object System.Net.WebClient).DownloadFile(
             'https://download.microsoft.com/download/2/C/4/2C47A5C1-A1F3-4843-B9FE-84C0032C61EC/UcmaRuntimeSetup.exe',
             "$env:Temp\UcmaRuntimeSetup.exe")
         & $env:Temp\UcmaRuntimeSetup.exe /passive /norestart | Out-Default
         
         EOF
         

  3. Create a VM instance in the first zone and pass `specialize-mailbox.ps1` as the specialize script. Attach the Exchange installation disk as secondary disk. You use the secondary disk later to install the Exchange Server mailbox role:
         
         gcloud compute instances create mailbox-1-a \
           --image-family=windows-2016 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-8 \
           --subnet=$SUBNET_NAME \
           --tags exchange,exchange-mailbox \
           --zone=$SUBNET_ZONE_1 \
           --boot-disk-type pd-ssd \
           --disk=name=exchange-media-1,auto-delete=no,mode=ro \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-mailbox.ps1
         

  4. Create another VM instance in the second zone:
         
         gcloud compute instances create mailbox-1-b \
           --image-family=windows-2016 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-8 \
           --subnet=$SUBNET_NAME \
           --tags exchange,exchange-mailbox \
           --zone=$SUBNET_ZONE_2 \
           --boot-disk-type pd-ssd \
           --disk=name=exchange-media-2,auto-delete=no,mode=ro \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-mailbox.ps1
         

  5. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output mailbox-1-b --zone=$SUBNET_ZONE_2
         

Wait about 5 minutes until you see the output `Instance setup finished` and then press Ctrl+C. At this point, the VM instance is ready to use.

  6. For each of the two VM instances, perform the following steps:

     1. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance
     2. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using the username and password created in the previous step.
     3. Right-click the **Start** button (or press **Win+X**) and click **Command Prompt (Admin)**.
     4. Confirm the elevation prompt by clicking **Yes**.
     5. In the elevated command prompt, start a PowerShell session:
            
            powershell
            

     6. Join the computer to your Active Directory domain:
            
            Add-Computer -Domain DOMAIN
            

Replace DOMAIN with the DNS name of your Active Directory domain.

     7. Restart the computer:
            
            Restart-Computer
            

Wait for approximately 1 minute for the restart to complete.

     8. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using a domain user that is a member of the **Enterprise Admins** group.

     9. Install the Exchange Server mailbox role by using the [setup wizard](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/install-mailbox-role?view=exchserver-2016) or [unattended mode](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/unattended-installs?view=exchserver-2016). You can find the Exchange installation media on drive `D:`.




### Deploying the witness Server

To set up a database availability group (DAG) for the two mailbox servers, you need an extra VM instance to serve as witness server. To deploy the witness server, follow these steps:

  1. Return to your existing Cloud Shell session.
  2. Create a witness server in the first zone:
         
         gcloud compute instances create witness \
           --image-family=windows-2016 \
           --image-project=windows-cloud \
           --machine-type n1-standard-8 \
           --subnet $SUBNET_NAME \
           --tags exchange,exchange-witness \
           --zone $SUBNET_ZONE_1 \
           --boot-disk-type pd-ssd \
           "--metadata=sysprep-specialize-script-ps1=add-windowsfeature FS-FileServer"
         

  3. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output witness --zone=$SUBNET_ZONE_1
         

Wait about 3 minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

  4. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance

  5. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using the username and password created in the previous step.

  6. Right-click the **Start** button (or press **Win+X**) and click **Command Prompt (Admin)**.

  7. Confirm the elevation prompt by clicking **Yes**.

  8. In the elevated command prompt, start a PowerShell session:
         
         powershell
         

  9. Join the computer to your Active Directory domain:
         
         Add-Computer -Domain DOMAIN
         

Replace DOMAIN with the DNS name of your Active Directory domain.

  10. Restart the computer:
         
         Restart-Computer
         

Wait approximately 1 minute for the restart to complete.

  11. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using a domain user that is a member of the **Enterprise Admins** group.

  12. Right-click the **Start** button (or press **Win+X**) and click **Command Prompt (Admin)**.

  13. Confirm the elevation prompt by clicking **Yes**.

  14. In the elevated command prompt, start a PowerShell session:
         
         powershell
         

  15. Add the **Exchange Trusted Subsystem** universal security group to the local **Administrators** group:
         
         Add-LocalGroupMember -Group Administrators -Member "DOMAIN\Exchange Trusted Subsystem"
         

Replace DOMAIN with the NetBIOS name of your Active Directory domain.




The two mailbox servers and the witness server are now fully deployed, but you still need to add them to a database availability group.

### Creating a database availability group

To create a DAG, follow these steps:

  1. [Connect to the management VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using a domain user that is a member of the **Enterprise Admins** group.
  2. Right-click the **Start** button (or press **Win+X**) and click **Command Prompt (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. In the elevated command prompt, start a PowerShell session:
         
         powershell
         

  5. Download and install the Chrome browser:
         
         Start-BitsTransfer `
             -Source 'https://dl.google.com/chrome/install/latest/chrome_installer.exe' `
             -Destination "$env:Temp\chrome_installer.exe"
         & $env:Temp\chrome_installer.exe
         

  6. To open the Exchange Admin Center (EAC), launch Chrome and navigate to the following URL:
         
         https://mailbox-1-a/ecp/?ExchClientVer=15
         

  7. Sign in using a domain user that is a member of the **Enterprise Admins** group.

  8. In the EAC menu, select **servers > database availability groups**.

  9. Click **+**.

  10. In the dialog, enter the following settings to [create a database availability group](https://docs.microsoft.com/en-us/exchange/high-availability/manage-ha/create-dags?view=exchserver-2016):

     1. **Database availability group name:`mailbox`**
     2. **Witness server:`witness`**
  11. Click **Save**.

  12. Click the **Managed DAG membership** icon.

  13. In the dialog, click **+** to add a member server.

  14. Select **mailbox-1-a** and **mailbox-1-b** and click **add.**

  15. Click **OK.**

  16. Click **Save**.




Optionally, perform any [Exchange Server post-installation tasks](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/post-installation-tasks?view=exchserver-2016).

### Setting up load balancing

To allow clients to connect to the mailbox servers, you now create an [internal load balancer](https://docs.cloud.google.com/load-balancing/docs/internal) resource:

  1. Return to your existing Cloud Shell session.
  2. Create one [unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances) per zone:
         
         gcloud compute instance-groups unmanaged create mailbox-a --zone=$SUBNET_ZONE_1
         gcloud compute instance-groups unmanaged create mailbox-b --zone=$SUBNET_ZONE_2
         

  3. Add the VM instances running the mailbox servers to the instance groups:
         
         gcloud compute instance-groups unmanaged add-instances mailbox-a \
           --zone=$SUBNET_ZONE_1 \
           --instances=mailbox-1-a
         gcloud compute instance-groups unmanaged add-instances mailbox-b \
           --zone=$SUBNET_ZONE_2 \
           --instances=mailbox-1-b
         

  4. Create a health check that probes the HTTP path `/owa/healthcheck.htm`:
         
         gcloud compute health-checks create http http-80\
           --port=80 \
           --request-path=/owa/healthcheck.htm
         

  5. Create a load balancer backend and add the two instance groups:
         
         gcloud compute backend-services create mailbox-backend \
           --load-balancing-scheme=internal \
           --protocol=tcp \
           --region=$SUBNET_REGION \
           --health-checks=http-80 \
           --session-affinity=CLIENT_IP_PORT_PROTO
         
         gcloud compute backend-services add-backend mailbox-backend \
           --region=$SUBNET_REGION \
           --instance-group=mailbox-a \
           --instance-group-zone=$SUBNET_ZONE_1
         
         gcloud compute backend-services add-backend mailbox-backend \
           --region=$SUBNET_REGION \
           --instance-group=mailbox-b \
           --instance-group-zone=$SUBNET_ZONE_2
         

  6. Reserve a static IP address for the load balancer:
         
         gcloud compute addresses create mailbox-frontend \
           --region=$SUBNET_REGION \
           --subnet=$SUBNET_NAME
         

  7. Create a forwarding rule for the load balancer:
         
         gcloud compute forwarding-rules create mailbox-frontend \
           --region=$SUBNET_REGION \
           --address=mailbox-frontend  \
           --load-balancing-scheme=internal \
           --network=$VPC_NAME \
           --subnet=$SUBNET_NAME \
           --ip-protocol=TCP \
           --ports=ALL \
           --backend-service=mailbox-backend  \
           --backend-service-region=$SUBNET_REGION
         

  8. Look up the IP address of the load balancer:
         
         gcloud compute addresses describe mailbox-frontend  \
           --region=$SUBNET_REGION \
           --format=value\(address\)
         




### Testing the mailbox servers

To verify that the mailbox servers have been deployed successfully, perform the following steps:

  1. On the management VM, open Chrome and navigate to `https://<var>IP</var>/owa/`, where IP is the IP address of the load balancer that you looked up earlier.
  2. Sign in using a domain user.

You should now see the user interface of Outlook Web Access.




## Deploying the edge transport role

You now deploy the [edge transport servers](https://docs.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-transport-servers?view=exchserver-2016). The edge transport servers [handle all inbound and outbound mail flow](https://docs.microsoft.com/en-us/exchange/mail-flow/mail-flow?view=exchserver-2016#understanding-the-transport-pipeline).

Unlike mailbox servers, edge transport servers are exposed to the internet. In an on-premises deployment, you might therefore deploy edge transport servers into a perimeter network that is isolated from the internal network by firewalls.

On Google Cloud, deploying edge transport servers into a separate VPC or subnet is not necessary. Instead, you use firewall rules to micro-segment your network and restrict network communication from and to the edge transport servers.

Unlike mailbox servers, the edge transport servers are not members of your Active Directory domain.

The VM instances will use the `n1-standard-8` [machine type](https://docs.cloud.google.com/compute/docs/machine-types). Depending on how you plan to use the Exchange deployment, you might need to use larger machine types. Consult the [Find the permissions required to run any Exchange cmdlet](https://learn.microsoft.com/powershell/exchange/find-exchange-cmdlet-permissions?view=exchange-ps) for a more detailed analysis of your needs and their system requirements.

### Deploying the edge transport servers

To deploy the edge transport servers, follow these steps:

  1. Return to your existing Cloud Shell session.
  2. Create a [specialize script](https://docs.cloud.google.com/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) for the VM instance. The script runs during VM initialization and installs the [prerequisites for installing edge transport servers](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016#exchange-2016-edge-transport-servers-on-windows-server-2016):
         
         cat << "EOF" > specialize-transport.ps1
         
         # Install required Windows features
         Install-WindowsFeature ADLDS
         
         # Install Visual C++ Redistributable Package for Visual Studio 2012
         (New-Object System.Net.WebClient).DownloadFile(
             'http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU3/vcredist_x64.exe',
             "$env:Temp\vcredist_2012_x64.exe")
         & $env:Temp\vcredist_2012_x64.exe /passive /norestart | Out-Default
         
         EOF
         

  3. Create a VM instance in the first zone and pass `specialize-transport.ps1` as the specialize script. Attach the Exchange installation disk in read-only mode so that you can later install the Exchange Server transport server role:
         
         gcloud compute instances create transport-1-a \
           --image-family=windows-2016 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-8 \
           --subnet=$SUBNET_NAME \
           --tags exchange,exchange-transport \
           --zone=$SUBNET_ZONE_1 \
           --boot-disk-type pd-ssd \
           --disk=name=exchange-media-1,auto-delete=no,mode=ro \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-transport.ps1
         

  4. Create another VM instance in the second zone:
         
         gcloud compute instances create transport-1-b \
           --image-family=windows-2016 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-8 \
           --subnet=$SUBNET_NAME \
           --tags exchange,exchange-transport \
           --zone=$SUBNET_ZONE_2 \
           --boot-disk-type pd-ssd \
           --disk=name=exchange-media-2,auto-delete=no,mode=ro \
           --metadata-from-file=sysprep-specialize-script-ps1=specialize-transport.ps1
         

  5. Monitor the initialization process of the VM by viewing its serial port output:
         
         gcloud compute instances tail-serial-port-output transport-1-b --zone=$SUBNET_ZONE_2
         

Wait about 5 minutes until you see the output `Instance setup finished`, then press Ctrl+C. At this point, the VM instance is ready to be used.

  6. For each of the two edge transport server VM instances, perform the following steps:

     1. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance.
     2. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) and log in using the username and password created in the previous step.
     3. [Configure the primary DNS suffix](https://docs.microsoft.com/en-us/exchange/primary-dns-suffix-is-missing-exchange-2013-help?redirectedfrom=MSDN) to match the DNS domain name used by your Active Directory domain.
     4. Install the Exchange Server edge transport server role by using the [setup wizard](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/install-edge-transport-role?view=exchserver-2016) or [unattended mode](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/unattended-installs?view=exchserver-2016). You can find the Exchange installation media on drive `D:`.



### Registering the edge transport servers in DNS

Before you can set up an edge subscription for the edge transport servers, you have to assign DNS names to the server. Because the edge transport servers are not members of your Active Directory domain, you have to assign these names manually:

  1. On the management server, open a PowerShell console.
  2. Create a CNAME record for `transport-1-a` and `transport-1-b`:
         
         Add-DnsServerResourceRecordCName `
           -ComputerName (Get-ADDomainController).Hostname `
           -HostNameAlias "transport-1-a.REGION-a.c.PROJECT-ID.internal." `
           -Name "transport-1-a" `
           -ZoneName "DOMAIN"
         
         Add-DnsServerResourceRecordCName `
           -ComputerName (Get-ADDomainController).Hostname `
           -HostNameAlias "transport-1-b.REGION-b.c.PROJECT-ID.internal." `
           -Name "transport-1-b" `
           -ZoneName "DOMAIN"
         

Where:

     * PROJECT-ID is the project ID of the project in which your Exchange VM instances are deployed.
     * REGION is the region in which your Exchange VM instances are deployed.
     * DOMAIN is the DNS domain of your Active Directory domain.



### Setting up edge subscriptions

To populate the Active Directory Lightweight Directory Services (AD LDS) instances on the edge transport server with Active Directory data, you now set up [edge subscriptions](https://docs.microsoft.com/en-us/Exchange/architecture/edge-transport-servers/edge-subscriptions?view=exchserver-2016).

**Note:** Perform the following steps on each of the two edge transport servers.

  1. Open an elevated Exchange management shell by right-clicking **Start** > **Exchange Management Shell** and selecting **More** > **Run as Administrator**.
  2. Create an edge subscription:
         
         New-EdgeSubscription -FileName "$env:UserProfile\Desktop\EdgeSubscriptionInfo-$env:computername.xml"
         

You should now see the subscription file on the desktop.

  3. Export the Exchange AD LDS server certificate:

     1. Open the Microsoft Management Console by clicking **Start** > **Run** , entering `mmc` and selecting **OK**.
     2. Select **File** > **Add/remove snap-in.**
     3. In the list of snap-ins, select **Certificates** and click **Add**.
     4. Select **Service account** , then click **Next**.
     5. Select **Local computer** , then click **Next**.
     6. Select **Microsoft Exchange ADAM** , then click **Finish**.
     7. Click **OK**.
     8. In the left pane, navigate to **Certificates** > **ADAM_MSExchange\Personal** > **Certificates**
     9. Right-click the certificate in the right pane and select **All tasks** > **Export**.
     10. Click **Next**.
     11. Select **No, do not export the private key** and click **Next**.
     12. Select **Base-64 encoded X.509 (.cer)** and click **Next**.
     13. Select a location to save the certificate to and click **Next**.
  4. For each of the two mailbox server VM instances, perform the following steps:

     1. Copy the Exchange AD LDS server certificate of both edge transport servers to a temporary location.
     2. Copy the subscription files of both edge transport servers to a temporary location.
     3. Open an elevated Exchange management shell by right-clicking **Start** > **Exchange Management Shell** and selecting **More** > **Run as Administrator**.
     4. Import the Exchange AD LDS server certificate of `transport-1-a`:
            
            Import-Certificate -FilePath "PATH" -CertStoreLocation cert:\LocalMachine\Root
            

Replace PATH with the path to the Exchange AD LDS server certificate of `transport-1-a`.

     5. Import the Exchange AD LDS server certificate of `transport-1-b`:
            
            Import-Certificate -FilePath "PATH" -CertStoreLocation cert:\LocalMachine\Root
            

Replace PATH with the path to the Exchange AD LDS server certificate of `transport-1-b`.

     6. [Import the Edge Subscription files](https://docs.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscriptions?view=exchserver-2016#import-the-edge-subscription-file-on-a-mailbox-server) of `transport-1-a` and `transport-1-b`.

     7. [Manually start the EdgeSync process](https://docs.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscription-procedures?view=exchserver-2016#run-edgesync-manually) on a mailbox server and [verify that the synchronization succeeded](https://docs.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscription-procedures?view=exchserver-2016#verify-edgesync-results).




### Setting up load balancing for inbound mail flow

To enable inbound email flow to the edge transport servers, you now create a [network load balancer](https://docs.cloud.google.com/load-balancing/docs/network) resource:

  1. Return to your existing Cloud Shell session.
  2. Create a target pool:
         
         gcloud compute target-pools create transport-pool --region $SUBNET_REGION
         

  3. Add the edge transport server VM instances to the target pool:
         
         gcloud compute target-pools add-instances transport-pool \
           --instances-zone $SUBNET_ZONE_1 \
           --instances transport-1-a
         
         gcloud compute target-pools add-instances transport-pool \
           --instances-zone $SUBNET_ZONE_2 \
           --instances transport-1-b
         

  4. Reserve an external IP address for the load balancer:
         
         gcloud compute addresses create transport-frontend --region=$SUBNET_REGION
         

  5. Create a forwarding rule:
         
         gcloud compute forwarding-rules create www-rule \
           --region $SUBNET_REGION \
           --ports 25 \
           --address transport-frontend \
           --target-pool transport-pool
         

  6. Look up the IP address of the load balancer:
         
         gcloud compute addresses describe transport-frontend  \
           --region=$SUBNET_REGION \
           --format=value\(address\)
         

The transport servers are now available to receive email on port 25 of this IP address and will pass incoming email to the mailbox servers.

  7. Verify that email delivery works by following the instructions in [Use Telnet to test SMTP communication on Exchange servers](https://docs.microsoft.com/en-us/exchange/mail-flow/test-smtp-with-telnet?view=exchserver-2016).

**Note:** To prevent potential email service abuse and protect IP address reputation, outgoing connections to port 25 are [blocked for VM instances and Cloud Shell](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail). To test SMTP communication, perform the tests on your workstations instead of on a VM instance or Cloud Shell.
  8. To complete the setup of your edge transport servers, follow the steps in [Configure mail flow and client access on Exchange servers](https://docs.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/configure-mail-flow-and-client-access?view=exchserver-2016).




### Setting up outbound email flow by using SendGrid

Because Google Cloud [does not allow outbound connections on port 25](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail#using_standard_email_ports), you now set up a custom send connector to handle outbound email.

**Note:** This section shows how to use SendGrid to deliver internet email. You can use other third-party providers such as Mailgun or Mailjet to deliver internet email.

  1. Use the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/sendgrid-app/sendgrid-email) to sign up for the SendGrid email service.
  2. On the SendGrid website, create a new API key.
  3. Add the public IP addresses of the VM instances `transport-1-a` and `transport-1-b` to the list of allowed IP addresses.



#### Creating a send connector

You now create an [outbound send connector](https://docs.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscriptions?view=exchserver-2016#outbound-send-connector-to-send-messages-to-the-internet) that uses SendGrid as smart host:

  1. Return to the Exchange Admin Center (EAC).
  2. In the EAC menu, select **mail flow** > **send connectors**.
  3. Click **+**.
  4. In the **New send connector** dialog, enter the following settings: 
     * **Name** : `SendGrid`
     * **Type** : **Internet (for example, to send internet mail)**
  5. Click **Next**.
  6. Under **Network settings** , select **Route mail through smart hosts** and click **+**.
  7. On the **Add smart host** page, enter `smtp.sendgrid.net`.
  8. Click **Save**.
  9. Click **Next**.
  10. Under **Smart host authentication** , select **Basic authentication**.
  11. Enter the following information: 
     * **User name** : `apikey`
     * **Password** : Paste the API key created on the SendGrid website
  12. Click **Next**.
  13. Under **Address space** , click **+**.
  14. Enter the following information: 
     * **Type:`SMTP`**
     * **Full Qualified Domain Name (FQDN)** : `*`
     * **Cost** : `1`
  15. Click **Next**.
  16. Under **Source server** , click **+**.
  17. Select `transport-1-a` and `transport-1-b` and click **OK**.
  18. Click **Finish**.



#### Changing the SMTP port

You now configure the send connector to use a custom port:

  1. On one of the mailbox servers, open the Exchange management shell by right-clicking **Start** > **Exchange Management Shell**.
  2. Modify the send connector to use port `2525`:
         
         Set-SendConnector -Identity "SendGrid" -port 2525
         

  3. Trigger an edge synchronization to ensure that the configuration change is propagated to all edge transport servers:
         
         Start-EdgeSynchronization -ForceFullSync
         


**Note:** To troubleshoot issues related to outbound email flow, check the [Send connectors log file](https://docs.microsoft.com/en-us/exchange/mail-flow/transport-logs/transport-logs?view=exchserver-2019#protocol-logging) on the edge transport servers.

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
