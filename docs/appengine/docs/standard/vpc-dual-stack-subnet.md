---
url: https://docs.cloud.google.com/appengine/docs/standard/vpc-dual-stack-subnet/
title: Set up dual-stack (IPv4 and IPv6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:48.095657+00:00
---

# Set up dual-stack (IPv4 and IPv6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/vpc-dual-stack-subnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Set up dual-stack (IPv4 and IPv6) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Dual-stack support for App Engine**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Dual-stack subnets let your App Engine resources send IPv4 and IPv6 traffic to a VPC network with Direct VPC egress. You can change an existing IPv4 only (single-stack) subnet to a dual-stack subnet.

## Subnet types

VPC networks support the following [Compute Engine subnet types](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types):

  * IPv4 only (single-stack) subnets, with only [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges)

  * IPv4 and IPv6 (dual-stack) subnets, with both IPv4 and [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges)




## Dual-stack limitations

Before you change the stack type on an existing App Engine resource, consider the following limitations:

  * Dual-stack support is only available with subnets in a custom-mode VPC network. To have the internal access type available for dual-stack subnets, the VPC network internal IPv6 range must be enabled. Set up or [convert](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode) the VPC network to custom mode.

  * Compared to IPv4-only subnets, dual-stack subnets might experience elevated cold-start latencies, limiting how quickly your application can scale up.

  * [NAT64](https://tools.ietf.org/html/rfc6146) isn't supported.




## Before you begin

Be sure that the App Engine service agent has the [Compute Public IP Admin role (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) to use the subnet with external IPv6.

## Set up a dual-stack subnet

Dual-stack subnets have both IPv4 and IPv6 address ranges.

To set up a dual-stack subnet, you can either use the Google Cloud console or the Google Cloud CLI:

###  Console 

  1. Go to the Google Cloud console and enable the Compute Engine API:

[Enable the Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)

  2. Navigate to the **VPC networks** page:

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  3. Click **Create VPC network** if you are creating a new custom-mode network. If you are using an existing VPC network, click the name of the VPC network to show its _VPC network details_ page.

  4. If you are creating a new network or converting an existing one, enter the name and be sure that the **Subnet creation mode** is set to **Custom** , then select **Configure a ULA internal IPv6 range for this VPC Network**.

  5. From the **Subnets** tab, click **Add subnet**. In the panel that appears:

     1. Provide a **Name**.
     2. Select a **Region**.
     3. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.
     4. Enter an **IPv4 range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.
     5. Select the **IPv6 access type**.

If the **Internal** option is not available and you need it, check that an internal IPv6 range is assigned on the network.

     6. Click **Add**.




###  gcloud 

  1. To create a custom-mode network that supports dual-stack subnets, run the `gcloud compute networks create` command.

To configure _internal_ IPv6 ranges on any subnets in this network, use the `--enable-ula-internal-ipv6` flag. This option assigns a `/48` ULA prefix from within the `fd20::/20` range used by Google Cloud for internal IPv6 subnet ranges.
         
         gcloud compute networks create NETWORK \
           --subnet-mode=custom \
           --enable-ula-internal-ipv6

Replace NETWORK with the name of the VPC network that will contain the new subnet.

  2. To convert to or update a custom-mode network so that it supports dual-stack subnets, run the following command:
         
         gcloud compute networks update NETWORK \
           --switch-to-custom-subnet-mode \
           --enable-ula-internal-ipv6

Replace NETWORK with the name of the VPC network that will contain the new subnet.

  3. To create a dual-stack subnet with an IPv6 range, run the [`subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) using the dual-stack settings:
         
         gcloud compute networks subnets create SUBNET \
           --network=NETWORK \
           --range=PRIMARY_IPv4_RANGE \
           --stack-type=IPV4_IPV6 \
           --ipv6-access-type=IPV6_ACCESS_TYPE \
           --region=REGION

Replace the following:

     * SUBNET: a name for the new subnet.
     * NETWORK: the name of the VPC network that will contain the new subnet.
     * PRIMARY_IPv4_RANGE: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * IPV6_ACCESS_TYPE: the IPv6 access type for the new subnet, either `internal` or `external`.
     * REGION: the Google Cloud region that the new subnet will be created in.



## Add the dual-stack subnet to an App Engine resource

After you create a dual-stack subnet, configure your App Engine service to use the subnet:

  1. In your `app.yaml` file, specify the network and subnet in the `vpc_access` field:
         
         vpc_access:
           network_interface:
             network: NETWORK
             subnet: SUBNET
           vpc_egress: EGRESS_SETTING

Replace the following:

     * NETWORK: the name of network you created in the previous step.

     * SUBNET: the name of the subnet you created in the previous step.

     * Optional: EGRESS_SETTING: controls how outbound traffic is routed. This field supports the following configuration settings:

       * `all-traffic`: All outbound requests are routed through the VPC network.
       * `private-ranges-only` (default): Only traffic to internal IP addresses is routed through the VPC network. Internet traffic uses the default App Engine path.
  2. Deploy to App Engine by running the following command:
         
         gcloud beta app deploy




## Change a subnet from single-stack to dual-stack

To add an IPv6 subnet range to an existing IPv4-only subnet in a custom-mode VPC network, see [Change a subnet's stack type to dual-stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6). Then, deploy the App Engine service on the dual-stack subnet.

## Change a subnet from dual-stack to single-stack

To change a resource's dual-stack subnet to a single-stack subnet, see [Change a dual-stack subnet to IPv4 only](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-change-stacktype). Then, deploy the App Engine service on the dual-stack subnet.

## Verify the network and subnet

To check that your resource is on the VPC network, run the following command:
    
    
    gcloud beta app versions describe VERSION --service=SERVICE

Replace the following:

  * VERSION: the deployed version of your service
  * SERVICE: the deployed service



The following example output shows your network and subnet:
    
    
      vpcAccess:
      networkInterfaces:
      - network: projects/YOUR_PROJECT/global/networks/YOUR_NETWORK
        subnet: projects/YOUR_PROJECT/regions/YOUR_REGION/subnetworks/YOUR_SUBNET
      vpcEgress: ALL_TRAFFIC/PRIVATE_RANGES_ONLY
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
