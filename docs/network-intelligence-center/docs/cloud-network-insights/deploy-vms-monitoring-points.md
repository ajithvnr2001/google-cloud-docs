---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-vms-monitoring-points/
title: Deploy VM Monitoring Points \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:39.968747+00:00
---

# Deploy VM Monitoring Points  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-vms-monitoring-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Deploy VM Monitoring Points Stay organized with collections  Save and categorize content based on your preferences. 

Deploy a VM or KVM Monitoring Point inside your cloud, hybrid, or multi-cloud network to monitor your network or web application performance.

To start monitoring, download the Monitoring Point images from Google Cloud, and then deploy the image using VMware vSphere (vCenter or ESXi) or Linux KVM (QCOW2) by following the instructions from AppNeta.

## Before you begin

The deployment environment and Monitoring Points have specific networking requirements to ensure that the Monitoring Point can be installed successfully and communicate back to the Cloud Network Insights control plane.

### Required roles

To get the permissions that you need to add Monitoring Points, ask your administrator to grant you the [Cloud Network Insights Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`) IAM role on the project that has Cloud Network Insights enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

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

Review the AppNeta Monitoring Point specifications to ensure that you can successfully deploy them.

  * [Specifications – v35-VMware](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-vmware-mp-intro/v35-vmware-specifications1.html)
  * [Specifications – v35-KVM](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-kvm-mp-intro/v35-kvm-specifications1.html)



## Download Monitoring Point image and configuration

You can download a zip file locally with the Monitoring Point images and configuration files or generate a command to download the installation bundle on the machine you're installing the Monitoring Point on.

###  Console 

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. Click **Add monitoring point**.

  3. In the **Platform Type** list, select either **KVM** or **VMware** , and then click **Continue**.

  4. Enter the **Password** for the VM.

  5. Choose your **IP Configuration**.

     * If the target network assigns IP addresses automatically, select **Obtain settings using DHCP**.
     * If you want to use a static IP address, select **Static IP**.
  6. Complete the following IP configuration fields. Fields are based on what you selected for the **IP Configuration**.

     * **IP Address** : The IPv4 address that you want to assign to the Monitoring Point.
     * **Network Mask** :The subnet mask (for example, 255.255.255.0).
     * **Network Gateway** : The default gateway IP address.
     * **DNS 1** : The IPv4 address of your primary DNS servers (for example, 8.8.8.8).
     * **DNS 2** (optional): A backup name server to ensure connectivity if the primary fails (for example, 1.1.1.1)
     * **Domain name** : The default DNS search domain for the Monitoring Point.
     * **Hostname** : The unique name for this Monitoring Point.
     * **Timezone** (optional): The timezone of the VM the Monitoring Point is installed on.
     * **NTP 1** (optional): The primary Network Time Protocol address (IP or FQDN).
     * **NTP 2** (optional): A backup time server used if the primary address is unreachable.
  7. Click **Continue**.

  8. In **Download the Monitoring Point** , choose how you want to download the installation bundle.

     * To download the installation bundle locally, select **Download locally**. 
       1. Click **Download Monitoring Point**. 
          * **For KVM** : Download a ZIP file that contains an ISO file (boot/config drive).
          * **For VMware** : Download a ZIP file that contains a JSON file (deployment parameters).
       2. Download the disk image. The available options depends on your selected **Platform Type**.
       3. Move the configuration file and the disk image to your hypervisor management station.
     * To generate a command-line command to run on the host, select **Run a command on the host**. 
       1. Click **Open shell and generate token**. You might need to authorize Cloud Shell.
       2. Press **Enter** to generate a token, and then copy and paste it in the text field in **Generate the command**.
       3. Open a terminal to your host using administrator credentials, and run the generated command to download the configuration files.
       4. Download the disk image. The available options depends on your selected **Platform Type**.
       5. If necessary, move the configuration file and the disk image to your hypervisor management station.
     * To generate a Google Cloud CLI command to download the installation bundle on the target host with Google Cloud CLI installed, select **Download with gcloud**.



###  gcloud 

Use this method if your target host has Google Cloud CLI installed. You can use the Google Cloud console to generate the command or modify the following command.
    
    
    gcloud network-management network-monitoring-providers \
    monitoring-points download-install-script \
      --project="PROJECT_NAME" \
      --network-monitoring-provider="PROVIDER_NAME" \
      --location="global" \
      --monitoring-point-type="MP_TYPE>" \
      --hostname="HOST_NAME" \
      --password="HOST_PASSWORD" \
      --time-zone="HOST_TIMEZONE" \
      --use-dhcp \
      --output-file="ZIP_FILE"
    

Replace the following:

  * `PROJECT_NAME`: the name of the project that has Cloud Network Insights enabled.
  * `PROVIDER_NAME`: the provider name, `external` by default.
  * `MP_TYPE`: the Monitoring Point container type. Use one of the following values: 
    * Enter `vm` for VMware
    * Enter `kvm` for KVM
  * `HOST_NAME`: the name of the host VM you're installing the Monitoring Point on.
  * `HOST_PASSWORD`: the password for the VM. The password hash is added to the downloaded configuration file.
  * `HOST_TIMEZONE`: the timezone of the VM the Monitoring Point is installed on.
  * `ZIP_FILE`: the compressed installation package. Use one of the following values: 
    * Enter `vmwareApplianceConfig.zip` for VMware
    * Enter `kvmApplianceConfig.zip` for KVM



## Deploy VM-based Monitoring Point

Once you have the images, follow the instructions from AppNeta to deploy the Monitoring Point.

  * [VMware](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-vmware-mp-intro/v35-vmware-setup/v35-vmware-mp-setup-v35-vmware.html)

  * [Linux KVM (QCOW2)](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-kvm-mp-intro/v35-kvm-setup/v35-kvm-mp-setup-v35-kvm.html)




After deploying the VM, record the MAC Address of the primary network adapter (eth0 or Network Adapter 1) from your hypervisor (vCenter or KVM).

  * **Username** : admin
  * **Default Password** : The MAC address in UPPERCASE with no colons (for example, 00505681450A).



You need these credentials if you need to sign in to the Monitoring Point's Web Administration interface to troubleshoot connectivity issues. For more information, see [AppNeta's documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/managing-monitoring-points/appliance-config-methods/appliance-admin-web.html).

## Configure a web proxy

If your network requires a proxy for outbound access, you must configure it after the VM is powered on.

  * [KVM Web Proxy Configuration](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-kvm-mp-intro/v35-kvm-configuration/v35-kvm-mp-web-proxy.html?content_ref=navigate+to+monitoring+point+settings+proxy)
  * [VMWare Web Proxy Configuration](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-vmware-mp-intro/v35-vmware-configuration/v35-vmware-mp-web-proxy.html)



## Verify the install

Open the Google Cloud console and navigate to **Network Intelligence Center** > **Cloud Network Insights**. After 2–5 minutes, the Monitoring Point appears in the table with the status Active. If it doesn't appear within ten minutes, see [Troubleshooting](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/troubleshooting).

## Remove Monitoring Points

To remove a Monitoring Point, delete it in AppNeta. For more information about removing a Monitoring Point, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/managing-monitoring-points/appliance-delete.html).

## What's next

After you add Monitoring Points, it's time to [create monitoring policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies) to populate Cloud Network Insights with data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
