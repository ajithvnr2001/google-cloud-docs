---
url: https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp/
title: Use Cloud NAT for Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:26.681496+00:00
---

# Use Cloud NAT for Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Use Cloud NAT for Secure Web Proxy Stay organized with collections  Save and categorize content based on your preferences. 

When you provision a Secure Web Proxy instance, a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway is automatically created in the same region and Virtual Private Cloud (VPC) network. This gateway then manages internet access by mapping private IPs to public IPs for all outbound web traffic that originates from your Secure Web Proxy instances.

By default, this auto-provisioned Cloud NAT gateway is set to `Automatic NAT IP address allocation`. This means that Google Cloud dynamically assigns and scales the public IP addresses that your Secure Web Proxy instances use. However, you can reconfigure this gateway to [use a set of static public IP addresses](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic) that you can manually reserve and assign.

**Note:** This is an advanced configuration setting for Secure Web Proxy. We recommend that you use the process explained on this page only if it's necessary to implement this specific setting for your workload.

## Before you begin

  * Complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  * Identify the VPC network and region where your Secure Web Proxy instance is deployed.

  * Verify that you have the Google Cloud CLI version 406.0.0 or later installed:
        
        gcloud version | head -n1
        

If you have an earlier gcloud CLI version installed, update the version:
        
        gcloud components update --version=406.0.0
        




## Configure Cloud NAT IPs for Secure Web Proxy

###  Console 

  1. To reserve a specific set of static external IP addresses, follow these steps:

     1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

     2. Click **Reserve external**. The **Reserve external static IP address** page opens.

     3. In the **Name** field, enter a name for the IP address, such as `swp-nat-ip-1`.

     4. In the **Description** field, enter a description for the IP address.

     5. For **Network Service Tier** , select the required option.

     6. For **IP version** , select **IPv4**.

     7. For **Type** , select **Regional**.

     8. For **Region** , select the same region where your Secure Web Proxy instance is deployed.

     9. For **Attached** , keep the selected option as **None**.

     10. Click **Reserve**. Repeat this process for each static IP address that you want to use for the Cloud NAT gateway.

  2. To locate and modify the Cloud NAT gateway for your Secure Web Proxy instance, follow these steps:

     1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

     2. Locate the Cloud NAT gateway that your Secure Web Proxy instance uses. Its name would be `swg-autogen-nat`, and it would be in the appropriate region and VPC network.

     3. Click **Edit**.

     4. For **Cloud NAT IP addresses** , change the setting from **Automatic (recommended)** to **Manual**.

     5. For **IP addresses** , select the static IP addresses that you reserved.

To add multiple IP addresses, click add_box**Add IP address**.

     6. Click **Save**.




###  Cloud Shell 

  1. Specify your project and region details.
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/region REGION
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `REGION`: region where your Secure Web Proxy instance is deployed
  2. Reserve your static external IP addresses.
         
         gcloud compute addresses create swp-nat-ip-1 \
             --region=REGION
         gcloud compute addresses create swp-nat-ip-2 \
             --region=REGION
         # Repeat for more IPs if required.
         

  3. Identify the Cloud Router name that's associated with your Cloud NAT gateway.
         
         gcloud compute routers list \
             --region REGION \
             --filter="network:(NETWORK_NAME) AND name:(swg-autogen-router-*)" \
             --format="get(name)"
         

Replace the following:

     * `REGION`: region where the Cloud Router is deployed for your Secure Web Proxy instance
     * `NETWORK_NAME`: name of your VPC network

The output is similar to the following:
    
    swg-autogen-router-1
    

  4. List the Cloud NAT configurations associated with that Cloud Router to verify the name of your Cloud NAT gateway, which would be `swg-autogen-nat`.
         
         gcloud compute routers nats list \
             --router=swg-autogen-router-1 \
             --region=REGION
         

  5. Update the Cloud NAT gateway to use manual IP addresses.
         
         gcloud compute routers nats update swg-autogen-nat \
             --router=swg-autogen-router-1 \
             --region=REGION \
             --nat-external-ip-pool=swp-nat-ip-1,swp-nat-ip-2
             # You can list multiple reserved IP names separated by commas.
         




## Limitations

You must deploy your Cloud NAT gateway in the same region as its associated Secure Web Proxy instances. This is because it's mandatory for each proxy to have its associated Cloud NAT gateway in its specific region.

When you provision the first proxy in a VPC network region, a Cloud NAT gateway is created automatically. However, the gateway can provide internet access for only those Secure Web Proxy instances that are deployed in that particular region and VPC network.

## What's next?

  * [Assign static IP addresses for outbound traffic](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic)
  * [Use tags to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags)
  * [Use a URL list to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
