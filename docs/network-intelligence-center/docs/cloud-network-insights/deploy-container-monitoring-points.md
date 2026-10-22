---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-container-monitoring-points/
title: Deploy container Monitoring Points \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:36.811312+00:00
---

# Deploy container Monitoring Points  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-container-monitoring-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Deploy container Monitoring Points Stay organized with collections  Save and categorize content based on your preferences. 

Deploy a Monitoring Point to a Docker, Podman, or Kubernetes (Helm) environment inside your cloud, hybrid, or multi-cloud network to monitor your network or web application performance.

To start monitoring, download the container Monitoring Point installation bundle from Google Cloud, and then follow the instructions from AppNeta to install it on the target host.

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

  * [Specifications – c50-Docker/Podman](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/docker-mp-intro/docker-specifications1/docker-mp-port-descriptions.html)
  * [Specifications – c50-Kubernetes (Helm)](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/kubernetes-mp-intro/kubernetes-specifications1.html)



## Download Monitoring Point installation bundle

Get the installation bundle and ensure that the bundle is on the target host.

###  Console 

If you have administrator credentials to the target host or if you need to download the installation bundle locally before transferring the file to the target host, use the Google Cloud console.

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. Click **Add monitoring point**.

  3. In the **Platform Type** list, select **Docker/Podman** or **Helm (Kubernetes)** , and then click **Continue**.

  4. Enter the **Hostname** of the container. This is the name of the host you're installing the Monitoring Point on.

  5. In **Download the Monitoring Point** , choose how you want to download the installation bundle.

     * To download the installation bundle on the target host using a terminal, select **Run a command on the host**. 
       1. Click **Open shell and generate token**. You might need to authorize Cloud Shell.
       2. Press **Enter** to generate a token, and then copy and paste it in the text field.
       3. Open a terminal to your target host using administrator credentials, and run the generated command to download the installation bundle. The curl command is valid for one hour.
     * To download the installation bundle locally, select **Download locally**. 
       1. Click **Download Monitoring Point**.
       2. Move the installation bundle to the target host.
     * To generate a Google Cloud CLI command to download the installation bundle on the target host with Google Cloud CLI installed, select **Download with gcloud**.



###  gcloud 

Use this method if your target host has Google Cloud CLI installed. You can use the Google Cloud console to generate the command or modify the following command.
    
    
    gcloud network-management network-monitoring-providers \
    monitoring-points download-install-script \
      --project="PROJECT_NAME" \
      --network-monitoring-provider="PROVIDER_NAME" \
      --location="global" \
      --monitoring-point-type="MP_TYPE" \
      --hostname="HOST_NAME" \
      --output-file="TAR_FILE"
    

Replace the following:

  * `PROJECT_NAME`: the name of the project that has Cloud Network Insights enabled.
  * `PROVIDER_NAME`: the provider name, `external` by default.
  * `MP_TYPE`: the Monitoring Point container type. Use one of the following values: 
    * Specify `CONTAINER` for Docker or Podman.
    * Specify `HELM` for Helm (Kubernetes).
  * `HOST_NAME`: the name of the host you're installing the Monitoring Point on.
  * `TAR_FILE`: the compressed installation package. Use one of the following values: 
    * Specify `compose.HOST_NAME.tar.gz` for Docker or Podman.
    * Specify `helm.HOST_NAME.tar.gz` for Helm (Kubernetes).



## Install your container-based Monitoring Point

Once the install bundle is on the target host, follow the instruction from AppNeta to install the Monitoring Point.

  * [Docker or Podman](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/docker-mp-intro/docker-setup/docker-mp-setup-cmp.html#mp-setup-cmp_prerequisites-docker)
  * [Kubernetes (Helm)](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/kubernetes-mp-intro/kubernetes-setup/kubernetes-mp-setup-cmp.html)



You can't change the configuration settings for containers. If you need to change the proxy, NTP, or timezone settings later, you delete the Monitoring Point and add a new one.

## Verify the install

Open the Google Cloud console and navigate to **Network Intelligence Center** > **Cloud Network Insights**. After 2–5 minutes, the Monitoring Point appears in the table with the status Active. If it doesn't appear within ten minutes, see [Troubleshooting](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/troubleshooting).

## Remove Monitoring Points

To remove a Monitoring Point, delete it in AppNeta. For more information about removing a Monitoring Point, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/managing-monitoring-points/appliance-delete.html).

## What's next

After you add Monitoring Points, it's time to [create monitoring policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies) to populate Cloud Network Insights with data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
