---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-gce-monitoring-points/
title: Deploy Compute Engine Monitoring Points \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:30.802750+00:00
---

# Deploy Compute Engine Monitoring Points  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-gce-monitoring-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Deploy Compute Engine Monitoring Points Stay organized with collections  Save and categorize content based on your preferences. 

Embed Google Cloud optimized Monitoring Points in your Google Cloud infrastructure to monitor your network or web application performance.

To deploy the Compute Engine Monitoring Point, download the installation bundle from Google Cloud, and then follow the instructions from AppNeta to install it using Terraform or Google Cloud Marketplace.

## Before you begin

The deployment environment and Monitoring Points have specific networking requirements to ensure that the Monitoring Point can be installed successfully and communicate back to the Cloud Network Insights control plane.

### Required roles

To get the permissions that you need to add Monitoring Points, ask your administrator to grant you the following IAM roles: 

  * [Cloud Network Insights Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`) on the project that has Cloud Network Insights enabled
  * Deploy Compute Engine Monitoring Points by using Terraform: [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project in which you're deploying the Compute Engine Monitoring Point 
  * Deploy a Monitoring Point by using Google Cloud Marketplace: 
    * [Cloud Infrastructure Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.admin) (`roles/config.admin`) on on the project in which you're deploying the Compute Engine Monitoring Point
    * [Consumer Procurement Entitlement Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`) on on the project in which you're deploying the Compute Engine Monitoring Point
    * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on on the deployment service account
    * [Cloud Infrastructure Manager Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`) on on the deployment service account
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on on the deployment service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you want to use OS Login, specific Identity and Access Management (IAM) roles must be granted to the user accounts who connect to the VMs. See [Assign OS Login IAM roles](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#configure_users) in the Compute Engine documentation.

### Firewall requirements

Since we recommend installing Monitoring Points behind your firewalls, you might need to modify your firewall rules. Monitoring Points require outbound internet access to communicate back to the Cloud Network Insights control plane.

  
**Protocol** |   
**Port** |   
**Description**  
---|---|---  
  
TCP |   
443 (HTTPS) |   
Required. Connectivity to the Cloud Network Insights control plane  
  
UDP |   
123 (NTP) |   
Required. Network Time Protocol. The Monitoring Point will fail to connect if time is not synced   
  
UDP/TCP |   
53 (DNS) |   
Required. Domain Name Service to resolve Cloud Network Insights endpoints   
  
UDP |   
3239, 33434 |   
Test Traffic. Required for standard Network Path monitoring (dual-ended)  
  
ICMP |   
Type 8 (echo request) |   
Test Traffic. Required for single-ended paths (for example, pinging 8.8.8.8).  
  
For more information, see [Firewall Configuration from AppNeta](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-firewall.html).

### Monitoring Point requirements

Review AppNeta's documentation for [Google CE Cloud Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro/gce-specifications1.html) to ensure that you can successfully deploy the Monitoring Point.

## Deploy Compute Engine VMs

You can deploy a Compute Engine VM to Google Cloud by using Terraform. The Terraform configuration files (TF) are available through the Google Cloud console or through Cloud Marketplace.

###  Console 

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. Click **Add monitoring point**.

  3. In the **Platform Type** list, select **Google Cloud** , and then click **Continue**.

  4. Enter the **Hostname** of the VM. This name is used as the VM name and as the Monitoring Point's name by default.

  5. Optional: Select **Connect via Private Service Connect (PSC)** so that the Monitoring Point can communicate with AppNeta using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). You must already have Private Service Connect endpoints in your Virtual Private Cloud (VPC).

For more information, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro/gce-configuration/gce-mp-private-connections.html).

  6. Click **Continue**.

  7. In **Select a Monitoring Point deployment option** , select **Terraform**.

  8. In **Download the Monitoring Point** , choose how you want to download the installation bundle.

     * To download the installation bundle locally, select **Download locally**. 
       1. Click **Download Monitoring Point**.
       2. Extract the archive in the directory where you want to deploy the Terraform configuration files.
     * To download the installation bundle on a host using a terminal, select **Run a command on the host**. 
       1. Click **Open shell and generate token**. You might need to authorize Cloud Shell.
       2. Press **Enter** to generate a token, and then copy and paste it in the text field.
       3. Open a terminal to your host using administrator credentials, and run the generated command to download an archive of the Terraform configuration files. The curl command is valid for one hour.
     * To generate a Google Cloud CLI command to download the installation bundle on the target host with Google Cloud CLI installed, select **Download with gcloud**.



###  gcloud 

Use this method if your target host has Google Cloud CLI installed. You can use the Google Cloud console to generate the command or modify the following command.
    
    
    gcloud network-management network-monitoring-providers \
    monitoring-points download-install-script \
      --project="PROJECT_NAME" \
      --network-monitoring-provider="PROVIDER_NAME" \
      --location="global" \
      --monitoring-point-type="gce-vm" \
      --hostname="HOST_NAME" \
      --output-file="terraform.HOST_NAME.zip"
    

Replace the following:

  * `PROJECT_NAME`: the name of the project that has Cloud Network Insights enabled.
  * `PROVIDER_NAME`: the provider name, `external` by default.
  * `HOST_NAME`: the name of the host you're installing the Monitoring Point on.



###  Marketplace 

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights/monitoring-points)

  2. Click **Add monitoring point**.

  3. In the **Platform Type** list, select **Google Cloud** , and then click **Continue**.

  4. Enter the **Hostname** of the VM. This name is used as the VM name and as the Monitoring Point's name by default.

  5. Optional: Select **Connect via Private Service Connect (PSC)** so that the Monitoring Point can communicate with AppNeta using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). You must already have Private Service Connect endpoints in your VPC.

For more information, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro/gce-configuration/gce-mp-private-connections.html#private-connections_about-private-connections).

  6. Click **Continue**.

  7. Select **Google Cloud Marketplace** , and select the project you want to deploy the Monitoring Point in.

  8. Copy the configuration code snippet for the Monitoring Point. If you've deployed a Monitoring Point from Cloud Marketplace before, the code snippet is entered in the **Configuration** field automatically.

  9. Click **Open through Google Cloud Marketplace**.

  10. You might need to review the Marketplace Terms of Service. To install Cloud Network Insights using Cloud Marketplace accept the Terms of service.

  11. Click either the **Terraform** tab or the **Command-Line Deployment** tab and follow the on-screen instructions.

     * In **Network interfaces** , configure an external IP address to allow the Monitoring Point to communicate with AppNeta.
     * In **Configuration** , paste the Monitoring Point configuration code snippet.
  12. Click **Deploy**.




#### Install with Terraform

Once the install bundle is on the host, follow the instructions from AppNeta to install the Monitoring Point.

  * [Deploy Using Terraform](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro/gce-setup/gce-mp-setup-cloud-mp.html#mp-setup-cmp_deploy-terraform)
  * [Deploy Using Google Cloud Marketplace](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro/gce-setup/gce-mp-setup-cloud-mp.html#mp-setup-cmp_deploy-marketplace)



For more information about deploying a VM from Cloud Marketplace, see either [Deploy a software package](https://docs.cloud.google.com/marketplace/docs/get-products#deploy_a_software_package) or [Deploy virtual machine (VM) products using the command-line interface (CLI)](https://docs.cloud.google.com/marketplace/docs/deploy-through-CLI).

## Verify the install

Open the Google Cloud console and navigate to **Network Intelligence Center** > **Cloud Network Insights**. After 2–5 minutes, the Monitoring Point appears in the table with the status Active. If it doesn't appear within ten minutes, see [Troubleshooting](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/troubleshooting).

## Remove Monitoring Points

To remove a Monitoring Point, delete it in AppNeta. For more information about removing a Monitoring Point, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/managing-monitoring-points/appliance-delete.html).

## What's next

After you add Monitoring Points, it's time to [create monitoring policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies) to populate Cloud Network Insights with data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
