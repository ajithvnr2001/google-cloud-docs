---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/part-1-deploy-active-directory/
title: Deploy an Active Directory resource forest \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:29.177979+00:00
---

# Deploy an Active Directory resource forest  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/part-1-deploy-active-directory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Deploy an Active Directory resource forest Stay organized with collections  Save and categorize content based on your preferences. 

This series walks you through using Managed Microsoft AD to deploy an Active Directory [resource forest](https://docs.cloud.google.com/solutions/patterns-for-using-active-directory-in-a-hybrid-environment#resource_forest) on Google Cloud. You'll learn how to:

  * Set up a Shared VPC that enables you to access Managed Microsoft AD from multiple projects, and connect Managed Microsoft AD to an on-premises Active Directory using a forest trust.
  * Configure firewall rules that protect access to Active Directory from unauthorized sources.
  * Deploy Managed Microsoft AD in a single region and connect it to an existing Shared VPC.
  * Create a management VM and join it to the domain.
  * Use a delegated administrator to connect to Managed Microsoft AD.



## Architecture overview

To allow VMs from multiple projects to use Active Directory, you'll need a Shared VPC and three separate subnets:

  * **Managed Microsoft AD subnet** : Used by Managed Microsoft AD to run domain controllers.
  * **Management subnet** : Contains machines that are exclusively used for the purpose of managing Active Directory.
  * **Resource subnets:** Contains Active Directory member servers (such as application or database servers). Each resource subnet is scoped to a single region. In this guide, you will only create a single resource subnet, but you can add additional resource subnets later if you plan to deploy servers across multiple regions.



![Deployment outline](https://docs.cloud.google.com/static/managed-microsoft-ad/img/deploy-1.png)

To reduce security risks, you'll deploy a management VM with an internal RFC 1918 IP address and no internet access. To log in to VM instances, you'll use [IAP TCP tunneling](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#general_tcp_tunneling).

Following the best practice of using separate projects for management and servers, you'll create two separate projects:

  * **VPC host project** : Contains the Shared VPC configuration as well as Managed Microsoft AD.
  * **Management project** : Dedicated to managing Active Directory. You'll create a management VM within this project and use it to configure Active Directory.



## Before you begin

This tutorial uses a Shared VPC, which requires the use of a Google Cloud Organization. If you do not have an organization, [create one first](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). Additionally, some setup activities require [administrative roles](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc). Ensure you are granted the following IAM roles before proceeding.

  * [Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager)
  * [Shared VPC Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute)
  * [Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute)



This article assumes you are using a Windows machine with the [Google Cloud CLI installed](https://docs.cloud.google.com/sdk/install). You'll need to adjust some of the steps if you are using a different operating system.

Finally, collect the following information before you begin:

  * Project names for the **VPC host project** and the **management project**. These two projects will serve a central role in your deployment, so pick names that are easy to recognize and follow [your corporate naming conventions](https://docs.cloud.google.com/architecture/security-foundations/summary#naming-conventions).
  * [Folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) to create the **VPC host project** and the **management project** project in. If you don't have a suitable folder already, consider creating a [separate sub-folder for cross-functional resources](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) and services such as Active Directory.
  * A DNS domain name to use for the forest root domain of the new Active Directory forest.
  * An initial [region](https://cloud.google.com/about/locations/) to deploy resources in. Note that you can only deploy Managed Microsoft AD in [some regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions#regions) (this doesn't affect the general availability of your domain, which is available in all regions where your VPC has a presence). Consult the [best practices on region selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection) if you are unsure which region best suits your needs. You will be able to extend the deployment to additional regions later.
  * The name of the shared VPC to create. As the VPC will be shared across multiple projects, make sure to pick a name that is easy to recognize.
  * Subnet ranges for the following subnets:

    * **Managed Microsoft AD subnet** : Must be at least /24 in size.
    * **Management subnet** : Needs to accommodate all management servers. A subnet range sized /28 or larger is recommended.
    * **Resource subnet** : Size this subnet so it can accommodate all the servers you plan to deploy in the initial region.

Make sure your subnets do not overlap with any on-premises subnets and allow sufficient room for growth.




## Costs

The tutorial uses billable components of Google Cloud, including [Compute Engine](https://docs.cloud.google.com/compute), [Cloud DNS](https://docs.cloud.google.com/dns), and [Google Cloud Observability](https://docs.cloud.google.com/logging). See the [Pricing calculator](https://cloud.google.com/products/calculator/#id=beb5326f-90c3-4842-9c3f-a3761b40fbe3) to calculate the costs of completing this tutorial. Be sure to include any other resources specific to your deployment.

## Setting up VPC networking

### Creating the VPC host project

A VPC host project is used to create a Shared VPC and manage network-related configuration, such as subnets, firewall rules, and routes.

  1. In the Google Cloud console, open the **Manage resources** page. 

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the **Organization** drop-down list at upper left, select your organization.

  3. Click **Create Project** and enter the following settings:

     1. **Project Name** : The ID you chose as the project name.
     2. **Billing account** : Your billing account.
     3. **Location** : The folder to create the project in.
  4. Click **Create**.


**Warning:** Changes in the VPC host project can have far-reaching consequences on the functionality and security of projects and applications using the Shared VPC. Therefore, only a small group of administrative staff should be allowed to access this project. Before granting users access to this project, review the [best practices to verify access attempts](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust#verify_every_access_attempt_explicitly).

### Protecting the project against accidental deletion

Deleting a project also deletes any Managed Microsoft AD domains deployed inside it. In addition to using IAM policies to limit access to the project, you should protect the [project against accidental deletion](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#protectsharedvpc).

  1. In the [Google Cloud console](https://console.cloud.google.com), open [Cloud Shell](https://docs.cloud.google.com/shell/docs/overview). Cloud Shell gives you access to the command line in Google Cloud console, and includes Google Cloud CLI and other tools you need for Google Cloud administration. Cloud Shell can take several minutes to provision.  
[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Initialize variables to contain your organization name and the project ID of the VPC host project:
         
         ORG_NAME=[ORG-NAME] \
         VPCHOST_PROJECT_ID=[PROJECT-ID]
         

Replace `[ORG-NAME]` by the name of your organization and `[PROJECT-ID]` with the ID of the VPC host project. For example:
         
         ORG_NAME=example.com
         VPCHOST_PROJECT_ID=ad-host-123
         

  3. Run the following command to look up the ID of your organization, replacing `ORG-NAME` with the name of your organization (such as `example.com`):
         
         ORG_ID=$(gcloud organizations list \
           --filter="DISPLAY_NAME=$ORG_NAME" \
           --format=value\(ID\)) && \
         echo "ID of $ORG_NAME is $ORG_ID"
         

  4. Enforce `compute.restrictXpnProjectLienRemoval` policy for your organization:
         
         gcloud resource-manager org-policies enable-enforce \
           --organization $ORG_ID compute.restrictXpnProjectLienRemoval
         




### Deleting the default VPC

Compute Engine creates a `default` VPC in each project you create. This VPC is configured in [auto mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges), which means a subnet is pre-allocated for each region and automatically assigned a subnet range.

If you are planning to connect the VPC to an on-premises network, the predefined IP ranges that Compute Engine uses in auto mode are unlikely to suit your needs; they might overlap with existing IP ranges, or be inadequately sized. You should delete the default VPC and replace it with a custom mode VPC.

  1. Return to your existing Cloud Shell session.

  2. Enable the [Compute Engine](https://docs.cloud.google.com/compute) API in the VPC host project:
         
         gcloud services enable compute.googleapis.com --project=$VPCHOST_PROJECT_ID
         

  3. Delete all firewall rules associated with the `default` VPC:
         
         gcloud compute firewall-rules list \
           --filter="network=default" \
           --project=$VPCHOST_PROJECT_ID \
           --format=value\(name\) | \
         xargs gcloud compute firewall-rules delete \
           --project=$VPCHOST_PROJECT_ID
         

  4. Delete the default VPC:
         
         gcloud compute networks delete default --project=$VPCHOST_PROJECT_ID
         




### Creating the Shared VPC and subnets

With the `default` VPC deleted, you can now create the custom VPC (you'll turn this into into a shared VPC later).

  1. Return to your existing Cloud Shell session.

  2. Create variables for the VPC name, initial region, and subnet ranges:
         
         SHAREDVPC_NAME=[NAME] \
         SUBNET_REGION=[REGION] \
         SUBNET_RANGE_MANAGEMENT=[MANAGEMENT-RANGE] \
         SUBNET_RANGE_RESOURCES=[RESOURCES-RANGE] \
         SUBNET_RANGE_MANAGEDAD=[MANAGED-AD-RANGE] \
         SUBNET_RANGE_ONPREMAD=[ONPREM-AD-RANGE]
         

Replace the placeholder variables with the following:

     * `[NAME]` with a name, such as `ad-network-env-test.`
     * `[REGION]` with the region to deploy the Active Directory domain controllers in. You can extend the VPC and your domain to cover additional regions at any time.
     * `[MANAGEMENT-RANGE]` with the subnet range to use for the **management subnet**.
     * `[RESOURCES-RANGE]`with the subnet range to use for the **resource subnet**.
     * `[MANAGED-AD-RANGE]` with the subnet range to use for the **Managed Microsoft AD subnet**.
     * `[ONPREM-AD-RANGE]` with the subnet range to use for the **on-prem AD subnet**.

For example:
    
    SHAREDVPC_NAME=ad-network \
    SUBNET_REGION=us-central1 \
    SUBNET_RANGE_MANAGEMENT=10.0.0.0/24 \
    SUBNET_RANGE_RESOURCES=10.0.1.0/24 \
    SUBNET_RANGE_MANAGEDAD=10.0.2.0/24 \
    SUBNET_RANGE_ONPREMAD=192.168.0.0/24
    

  3. Enable the VPC host project to host a Shared VPC:
         
         gcloud compute shared-vpc enable $VPCHOST_PROJECT_ID
         

  4. Create a new [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges):
         
         gcloud compute networks create $SHAREDVPC_NAME \
             --subnet-mode=custom \
             --project=$VPCHOST_PROJECT_ID
         

  5. Create the management and resource subnet, and enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) so that Windows can [be activated](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) without granting the VMs direct internet access.
         
         gcloud compute networks subnets create $SUBNET_REGION-management \
           --network=$SHAREDVPC_NAME \
           --range=$SUBNET_RANGE_MANAGEMENT \
           --region=$SUBNET_REGION \
           --enable-private-ip-google-access \
           --project=$VPCHOST_PROJECT_ID && \
         gcloud compute networks subnets create $SUBNET_REGION-resources \
           --network=$SHAREDVPC_NAME \
           --range=$SUBNET_RANGE_RESOURCES \
           --region=$SUBNET_REGION \
           --enable-private-ip-google-access \
           --project=$VPCHOST_PROJECT_ID
         




### Securing the Shared VPC

Your VPC host project now contains a Shared VPC with two subnets. By [attaching service projects](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared) to this Shared VPC, you can make the Shared VPC available for use across multiple projects.

Rather than granting members of service projects [permission to use all subnets](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#networkuseratproject) of the Shared VPC, you should [grant access by subnet](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#networkuseratsubnet).

For security reasons, grant only a small group of administrative staff the right to access the **management subnet**. This ensures the subnet is only used to manage Active Directory. You can apply more lenient access control to the **resource subnet**.

### Creating firewall rules

Before you deploy Active Directory, you'll need to create firewall rules that allow you to administer and use it.

  1. Return to your existing Cloud Shell session.

  2. Enable firewall logging for ingress traffic so that all failed access attempts are logged:
         
         gcloud compute firewall-rules create deny-ingress-from-all \
             --direction=INGRESS \
             --action=deny \
             --rules=tcp:0-65535,udp:0-65535 \
             --enable-logging \
             --source-ranges=0.0.0.0/0 \
             --network=$SHAREDVPC_NAME \
             --project=$VPCHOST_PROJECT_ID \
             --priority 65000
         

  3. You will administer Active Directory using a dedicated management server deployed in the management subnet. Because this server will be deployed without an external IP address, you'll need to use [IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) to connect to the server.

Create the following firewall rule to allow RDP ingress from IAP:
         
         gcloud compute firewall-rules create allow-rdp-ingress-from-iap \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:3389 \
           --enable-logging \
           --source-ranges=35.235.240.0/20 \
           --network=$SHAREDVPC_NAME \
           --project=$VPCHOST_PROJECT_ID \
           --priority 10000
         




Your Shared VPC is now ready to be used for deploying Managed Microsoft AD.

## Deploying Active Directory

Managed Microsoft AD handles the provisioning and maintenance of Active Directory domain controllers. The following roles are deployed on the domain controllers:

  * Active Directory Domain Services
  * DNS



The domain controllers are deployed outside of your project, and will not appear as VM instances in your project. To make the domain controllers available for you to use, the following changes are applied to your project when you deploy Managed Microsoft AD:

  * [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) is added to your VPC. This connects your VPC to the service VPC that contains the domain controllers.
  * A [Cloud DNS private DNS peered zone](https://docs.cloud.google.com/dns/docs/overview#dns-peering) is created in the project. It forwards DNS queries matching your Active Directory domain to the DNS service run as part of Managed Microsoft AD.



Because you are using a Shared VPC, you need to deploy Managed Microsoft AD in the VPC host project in order for Active Directory to be usable across all service projects.

### Creating the Active Directory forest and domain

Follow these steps to deploy Managed Microsoft AD in the **VPC host project** created in the previous part of the guide:

  1. In the Google Cloud console, return to Cloud Shell.

  2. Initialize a variable to contain the forest root domain name of the new Active Directory forest to create. Refer to the [Microsoft naming conventions](https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and) for guidance on choosing a name.
         
         AD_DNS_DOMAIN=[AD-DNS-NAME]
         

For example:
         
         AD_DNS_DOMAIN=cloud.example.com
         

  3. Enable [Cloud DNS](https://docs.cloud.google.com/dns) in the VPC host project:
         
         gcloud services enable dns.googleapis.com --project $VPCHOST_PROJECT_ID
         

  4. Enable Managed Microsoft AD API in the VPC host project:
         
         gcloud services enable managedidentities.googleapis.com --project $VPCHOST_PROJECT_ID
         

  5. Provision the domain controllers and create a new forest:
         
         gcloud active-directory domains create $AD_DNS_DOMAIN \
           --admin-name=SetupAdmin \
           --reserved-ip-range=$SUBNET_RANGE_MANAGEDAD \
           --region=$SUBNET_REGION \
           --authorized-networks=projects/$VPCHOST_PROJECT_ID/global/networks/$SHAREDVPC_NAME \
           --project=$VPCHOST_PROJECT_ID
         

Allow 15 to 20 minutes for the command to complete.

  6. The previous command creates an initial Active Directory user named `SetupAdmin@[AD_DNS_DOMAIN]` for you. This user has delegated administrator privileges, and you can use it to finish configuring the new Active Directory forest.

To reveal the credentials of the user, run the following command. You will need to confirm that it is safe for the password to be revealed on screen.
         
         gcloud active-directory domains reset-admin-password $AD_DNS_DOMAIN \
           --project=$VPCHOST_PROJECT_ID
         

Copy the password; you will need it later.

The password can be reset by project owners and project editors of the VPC Host project at any time.




### Creating the management project

The Active Directory forest and forest root domain created by Managed Microsoft AD is now fully operational, and you have a first user (`SetupAdmin`) to perform further configuration. However, because Managed Microsoft AD domain controllers cannot be accessed directly using RDP, any configuration must be handled using a management VM.

You'll create this VM instance in a project dedicated to Active Directory management, and then connect the VM instance to the management subnet of the Shared VPC.

Once joined to the domain, you can use the [Remote Server Administration Tools](https://www.microsoft.com/en-us/download/details.aspx?id=45520), the [Group Policy Management Console](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753298\(v=ws.11\)), and PowerShell to administer Active Directory and Active Directory-related resources.

To create the management project:

  1. In the Google Cloud console, open the **Manage resources** page.  


[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the **Organization** drop-down list at upper left, select your organization.
  3. Click **Create Project** and complete the following fields: 
     1. **Project Name** : The ID you chose as the project name.
     2. **Billing account** : Your billing account. If you have access to several billing accounts, review your internal policies for each of them and choose the appropriate one.
     3. **Location** : A folder to create the project in.
  4. Click **Create**.



The management project will contain VM instances for administering Active Directory. In the tiered administration model, this means that highly privileged users from Tier 0 will be signing in to these VM instances.

These instances can be attractive targets for attackers; they potentially offer the opportunity to capture passwords, password hashes, or Kerberos tokens. And since these credentials have administrative access to Active Directory, they could be used to compromise the domain.

VM instances in the management project should be treated equivalently to [privileged access workstations](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/privileged-access-workstations). This implies:

  * Only a small group of administrative staff should be granted privileges to log in to these instances (whether by RDP or other means).
  * Access to the containing management project should be granted on a [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) basis. Only a selected few users should be allowed to view and access resources in the Google Cloud project.



To learn more about securing a Google Cloud project, review the [best practices to verify access attempts](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust#verify_every_access_attempt_explicitly).

### Using the Shared VPC instead of the default VPC

The management project currently has its own `default` VPC. Since you'll be using a Shared VPC instead, you can delete this VPC.

  1. In the Google Cloud console, return to Cloud Shell.

  2. Initialize a variable to contain the project ID of the management project (replace `[MANAGEMENT_PROJECT_ID]` with the project ID of the management project you just created):
         
         MANAGEMENT_PROJECT_ID=[MANAGEMENT_PROJECT_ID]
         

  3. Enable the [Compute Engine](https://docs.cloud.google.com/compute) API in the VPC host project:
         
         gcloud services enable compute.googleapis.com \
           --project=$MANAGEMENT_PROJECT_ID
         

  4. Delete all firewall rules associated with the `default` VPC:
         
         gcloud compute firewall-rules list \
           --filter="network=default" \
           --project=$MANAGEMENT_PROJECT_ID \
           --format=value\(name\) | \
         xargs gcloud compute firewall-rules delete \
             --project=$MANAGEMENT_PROJECT_ID
         

  5. Delete the `default` VPC:
         
         gcloud compute networks delete default --project=$MANAGEMENT_PROJECT_ID
         

  6. Associate the management project with the Shared VPC:
         
         gcloud compute shared-vpc associated-projects add $MANAGEMENT_PROJECT_ID \
           --host-project=$VPCHOST_PROJECT_ID
         




The management project is now a [service project](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_host_project_and_service_project_associations), and you can use the Shared VPC from within the management project.

## Connecting to Active Directory

You are now ready to create a first management VM instance and join it to Active Directory. You can use this VM to configure your Active Directory forest and forest root domain.

### Creating a management VM

To create a management VM instance, follow these steps:

  1. In the Google Cloud console, return to Cloud Shell.
  2. Create a new VM instance running Windows Server 2019 with [Remote Server Admin Tools (RSAT)](https://docs.microsoft.com/en-us/windows-server/remote/remote-server-administration-tools), DNS server administration tools, and Group Policy Management Console (GPMC) preinstalled.

Since you'll access the machine using [IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview), the instance does not need to be assigned an [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses).
         
         gcloud compute instances create admin-01 \
           --image-family=windows-2019 \
           --image-project=windows-cloud \
           --machine-type=n1-standard-2 \
           --no-address \
           --zone=$SUBNET_REGION-a \
           --subnet=projects/$VPCHOST_PROJECT_ID/regions/$SUBNET_REGION/subnetworks/$SUBNET_REGION-management \
           --project=$MANAGEMENT_PROJECT_ID \
           --metadata="sysprep-specialize-script-ps1=Install-WindowsFeature -Name RSAT-AD-Tools;Install-WindowsFeature -Name GPMC;Install-WindowsFeature -Name RSAT-DNS-Server"
         

  3. Run the following command to observe the boot process.
         
         gcloud compute instances tail-serial-port-output admin-01 \
           --zone=$SUBNET_REGION-a \
           --project=$MANAGEMENT_PROJECT_ID
         

  4. Wait about 4 minutes until you see the output `Instance setup finished`, then press Ctrl+C. The VM instances is now ready for use.

  5. Create a local SAM user `LocalAdmin`on the instance:
         
         gcloud compute reset-windows-password admin-01 \
           --user=LocalAdmin \
           --project=$MANAGEMENT_PROJECT_ID \
           --zone=$SUBNET_REGION-a \
           --quiet
         

Copy the password; you'll need it later.




### Joining the management VM to the domain

You can now log in to the management VM and join it to Active Directory

  1. On your local Windows workstation, open a command prompt (`cmd`).

  2. If this is the first time using `gcloud`on your local workstation, make sure to [authenticate](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) first.

  3. Run the following command to establish an IAP TCP tunnel from your local workstation to the `admin-01` VM, replacing `[MANAGEMENT_PROJECT_ID]` with the ID of the management project.
         
         gcloud compute start-iap-tunnel admin-01 3389 ^
           --local-host-port=localhost:13389 ^
           --project=[MANAGEMENT_PROJECT_ID]
         

Wait for the following output to appear
         
         Listening on port [13389]`
         

The tunnel is now ready for use.

  4. Open the **Windows Remote Desktop Connection** client (`mstsc.exe`).

  5. Click **Show Options**.

  6. Enter the following values:

     1. **Computer** : `localhost:13389`
     2. **User name** : `localhost\LocalAdmin`
  7. Click **Connect**.

  8. In the **Enter your credentials** dialog, paste the password you generated previously for the local `LocalAdmin` user. Then click **OK**.

  9. Since you have not set up RDP certificates for the management VM, a warning message will appear indicating that the identity of the remote computer cannot be verified. Dismiss this warning by clicking **Yes**.

  10. You should now see the Windows Server desktop of the `admin-01` VM.

  11. Right-click the **Start** button (or press **Win+X**) and click **Command Prompt (Admin)**.

  12. Confirm the elevation prompt by clicking **Yes**.

  13. In the elevated command prompt, start a PowerShell session by running `powershell`.

  14. Run the following command to initiate a domain join.
         
         Add-Computer -DomainName [AD-DNS-NAME]
         

Replace `[AD-DNS-NAME]` by the DNS name of the DNS name for the forest root domain.

  15. In the **Windows PowerShell credential request** dialog, enter the following values:

     1. **User name** : `SetupAdmin`
     2. **Password** : Enter the password created for `SetupAdmin` when deploying Managed Microsoft AD. Do not use the password of the local `LocalAdmin` user.
  16. Restart the computer by running `Restart-Computer`. Allow about one minute for the VM to restart.




### Launching Active Directory Users and Computers

The management VM is now a member of your Active Directory domain. You can use it to administer Active Directory:

  1. On your local Windows workstation, open the **Windows Remote Desktop Connection** client (`mstsc.exe`).
  2. Click **Show Options**.
  3. Enter the following values: 
     1. **Computer** : `localhost:13389`
     2. **User name** : `SetupAdmin@[AD-DNS-NAME]`. Replace `[AD-DNS-NAME]` with the DNS name of the DNS name for the forest root domain.
  4. Click **Connect**.
  5. In the **Enter your credentials** dialog, paste the password you generated previously for the `SetupAdmin` user. Then click **OK**.
  6. Since you have not set up RDP certificates for the management VM, a warning message will appear indicating that the identity of the remote computer cannot be verified. Dismiss this warning by clicking **Yes**.
  7. You should now see the Windows Server desktop of the `admin-01` VM.
  8. Right-click the **Start** button (or press **Win+X**) and select **Run**.
  9. Enter `dsa.msc` and click **OK**.



You should now see the **Active Directory Users and Computers** :

![AD users](https://docs.cloud.google.com/static/managed-microsoft-ad/img/deploy-2.png)

Congratulations! You are connected to your Managed Microsoft AD domain!

## Cleaning up

If you don't plan to use the resources from this tutorial in the future, clean them up so you won't be billed for them.

**Warning:** When you delete a project, **all resources inside it are deleted.** If you used an existing project for this tutorial, you'll also delete any other work you've done inside it. Additionally, any **custom project IDs will be lost.** If you created a custom project ID that you want to use in the future (such as an `appspot.com` URL), only delete selected resources instead of the entire project.

### Deleting the Active Directory forest and domain

  1. In the Google Cloud console, open Cloud Shell.

  2. Run the following command to delete the Active Directory forest and domain, replacing `[AD_DNS_DOMAIN]` with the DNS domain name used for Managed Microsoft AD domain, and `[VPCHOST_PROJECT_ID]` with the ID of your VPC host project:
         
         gcloud active-directory domains delete [AD_DNS_DOMAIN] \
           --project=[VPCHOST_PROJECT_ID]
         




### Deleting the management project

  1. In the Google Cloud console, go to the **Projects** page. 

[Open the Projects page](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the management project and click **Delete**.
  3. In the dialog, type the project ID, then click **Shut down** to delete the project.



### Deleting the VPC host project

  1. In the Google Cloud console, go to the **Projects** page. 

[Open the Projects page](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the VPC host project and click **Delete**.
  3. In the dialog, type the project ID, then click **Shut down** to delete the project.



## What's next

  * Learn about how to use [access levels](https://docs.cloud.google.com/iam/docs/conditions-base) and [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to restrict access to resources through IAP.
  * Protect the management project against accidental deletion by [placing a lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) on the project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
