---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-aws-monitoring-points/
title: Deploy AWS Monitoring Points \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:01.633641+00:00
---

# Deploy AWS Monitoring Points  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-aws-monitoring-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Deploy AWS Monitoring Points Stay organized with collections  Save and categorize content based on your preferences. 

Deploy Amazon Web Services (AWS) optimized EC2 Monitoring Points to your AWS infrastructure to monitor your network or web application performance.

To start monitoring, download the AWS Monitoring Point CloudFormation provisioning template from the Google Cloud console or open a quick-create link. Then follow the instructions from AppNeta to provision an EC2 Monitoring Point.

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

Review AppNeta's [Specifications – AWS EC2 Cloud Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/aws-ec2-mp-intro/aws-ec2-specifications1.html) to ensure that you can successfully deploy the Monitoring Point.

## Download Monitoring Point provisioning template

Get the AWS CloudFormation provisioning template and move it to the target host.

###  Console 

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. Click **Add monitoring point**.

  3. In the **Platform Type** list, select **AWS** , and then click **Continue**.

  4. Enter the **Hostname** of the container. This is the name of the host you're installing the Monitoring Point on.

  5. In **Select a Monitoring Point deployment option** , select **AWS CloudFormation**.

  6. In **Download the Monitoring Point** , choose how you want to download the provisioning template.

     * To download the provisioning template on the target host using a terminal, select **Run a command on the host**. 
       1. Click **Open shell and generate token**. You might need to authorize Cloud Shell.
       2. Press **Enter** to generate a token, and then copy and paste it in the text field.
       3. Open a terminal to your target host using administrator credentials, and run the generated command to download the provisioning template. The curl command is valid for one hour.
     * To download the provisioning template locally, select **Download locally**. 
       1. Click **Download Monitoring Point**.
       2. Move the provisioning template to the target host.



###  gcloud 

Use this method if your target host has Google Cloud CLI installed.
    
    
    gcloud network-management network-monitoring-providers \
    monitoring-points download-install-script \
      --project="PROJECT_NAME" \
      --network-monitoring-provider="PROVIDER_NAME" \
      --location=global \
      --monitoring-point-type="aws-ec2" \
      --hostname="HOST_NAME" \
      --output-file="cloudformation.HOST_NAME.zip"
    

Replace the following:

  * `PROJECT_NAME`: the name of the project that has Cloud Network Insights enabled.
  * `PROVIDER_NAME`: the provider name, `external` by default.
  * `HOST_NAME`: the name of the host you're installing the Monitoring Point on.



## Deploy the AWS Monitoring Point using an AWS CloudFormation quick-create link

Open a quick-create link with a pre-populated AWS CloudFormation Create stack. Some advanced configuration options aren't available with this option.

###  Console 

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. Click **Add Monitoring Point**.

  3. In the **Platform Type** list, select **AWS** , and then click **Continue**.

  4. Enter the **Hostname** of the container. This is the name of the host you're installing the Monitoring Point on.

  5. In **Select a Monitoring Point deployment option** , select **AWS Quick-Create Link**.

  6. Click **Launch** , and sign in to your AWS account. The deployment workflow pre-populates a single AWS CloudFormation Create stack.




### Install your AWS Monitoring Point

Once the provisioning template is on the target host or you've followed the quick-create link, follow the instruction from AppNeta to [install the Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/aws-ec2-mp-intro/aws-ec2-setup/aws-ec2-mp-setup-cloud-mp.html).

## Verify the install

Open the Google Cloud console and navigate to **Network Intelligence Center** > **Cloud Network Insights**. After 2–5 minutes, the Monitoring Point appears in the table with the status Active. If it doesn't appear within ten minutes, see [Troubleshooting](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/troubleshooting).

## Remove Monitoring Points

To remove a Monitoring Point, delete it in AppNeta. For more information about removing a Monitoring Point, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/managing-monitoring-points/appliance-delete.html).

## What's next

After you add Monitoring Points, it's time to [create monitoring policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies) to populate Cloud Network Insights with data.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
