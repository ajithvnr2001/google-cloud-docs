---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpns/
title: Configure connectivity using VPNs \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:28.106881+00:00
---

# Configure connectivity using VPNs  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Configure connectivity using VPNs Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-vpns "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpns "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

If your source database is inside a VPN (in AWS, for example, or your on-premises VPN), you also need to use a VPN on the destination side to connect to the source.

There are many VPN products you can use. The steps to configure VPNs vary from one product to another, but all of them are fundamentally similar. This section contains examples using AWS and Google Cloud VPNs.

The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the [VPC network that the AlloyDB destination instance is going to use](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#dest).

To find the **internal IP range** in the console:

  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.

  2. Select the VPC network that you want to use.

  3. Select **Private services access** > **Allocated IP ranges for services**.

  4. Find the **Internal IP range** associated with the connection created by **servicenetworking-googleapis-com**.


Note: To use Virtual Private Cloud networking, you must enable the [Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) for your Google Cloud project. 

## Example 1: AWS with Google Cloud Classic VPN with static routes

Find more complete, step-by-step documentation in the following links: 

  * On the AWS side, set up a [Site to Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html).
  * On the Google Cloud side, create a [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns) using static routing.



Put together, the overall sequence of steps looks like the following:

  1. In Google Cloud console > VPC Networks > External IP addresses, reserve a static IP address to use for the Cloud VPN.
  2. In the AWS VPC console: 
     1. Create a customer gateway.
     2. Create a new virtual private gateway or add an existing one to the VPC associated with your database.
     3. In **Routes Tables** add **route propagation** :
     4. Click **Edit** , check the **propagate** checkbox and **Save** to add the IP address range of your Google Cloud VPC network as the destination range.
  3. In the AWS VPC console, create the VPN: 
     1. Under **VPN Connections** , select **Site-to-site VPN Connections**.
     2. Select **Create VPN Connection**.
     3. Enter a name for the VPN connection.
     4. For **Virtual Private Gateway** , select the private gateway that you created or selected earlier in this procedure.
     5. For **Customer Gateway** , select the customer gateway that you created earlier in this procedure.
     6. For **Routing Options** , select **Static** , and specify the static IP address you reserved for the Cloud VPN as a CIDR (add /32).
     7. Download the configuration to save the settings. 
        1. Save the file as **Default**.
        2. Find the sections **IP Sec Tunnels** #1 and #2.
        3. Note the IKE version and **Pre-Shared Key** for each tunnel.
        4. Note the IP address for the **Virtual Private Gateway** for each tunnel.
        5. Note the IP address for the **Static Route Configuration option** for each tunnel.
  4. In Google Cloud, create a [Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns). 
     1. In Google Cloud console > Hybrid Connectivity > VPN:
     2. Click **Create VPN connection**. 
        1. Select your VPC network and region.
        2. For the Cloud VPN, use the static IP address you reserved earlier in this procedure.
        3. Use a `Pre-shared key` and key type from the AWS configuration you downloaded earlier in this procedure.
        4. Select the **Route based** routing option and add two tunnels; for each tunnel's **Remote network IP range** field, use an IP address for the **Static Route Configuration option** from the `IP Sec Tunnel` sections of the AWS configuration file you downloaded earlier in this procedure.
        5. Click **Create**.**Remote network IP range**


  5. In the AWS RDS console: 
     1. Select a security group.
     2. Add inbound firewall rules to allow all protocols and ports from the Cloud VPN.



The VPN tunnels should begin communicating shortly. On the AWS side, in the VPC Dashboard, the tunnel statuses are `UP`. On the GCP side, view the traffic between the VPNs in the [Cloud Logging](https://console.cloud.google.com/logs) console in the `Cloud VPN gateway` project.

## Example 2: AWS with Google Cloud HA VPN with dynamic routes

To get VPC Peering with an HA VPN (dynamic routes) to AWS, you need to export BGP routes to the AlloyDB peered VPC, and create a custom advertised route in Cloud Router for the AlloyDB peered VPC imported route. At that point, Cloud Router is advertising AWS routes to the AlloyDB VPC and the other way around. The firewall rules on both sides also need to match the AlloyDB peering route CIDR. 

On the AWS side, you can follow the first three steps in Example 1, except select **Dynamic** instead of **Static** under **Routing options**.

  1. Select your AlloyDB VPC Peering configuration in the [Console](https://console.cloud.google.com/networking/peering) and note the **Destination IP ranges** under **IMPORTED ROUTES**. For more information, see [Importing and exporting custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes). 
  2. Edit this VPC peering and check `Import Custom Routes` and `Export Custom Routes` in the VPC Peering connection details, and click **SAVE**. 

The peering now receives dynamic routes from your VPC like the routes coming from BGP peers. This allows traffic from the VPN to the peered network. However, Cloud Router is not yet advertising this route to other networks. To do so, you need to add custom advertised routes in the Cloud Router so that your VPC advertises the imported routes to other networks. For more information, see [Importing and exporting custom routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am).

  3. Add your DESTINATION_IP_RANGE custom IP range as a custom route in the Cloud Router configuration advertised routes. BGP peered networks are now receiving advertisements of the **imported AlloyDB network routes** , DESTINATION_IP_RANGE. Traffic on those VPN-connected networks bound for the AlloyDB peered VPC are now routed through the VPN tunnel. 
  4. Allow routes to propagate in AWS route tables. Make sure AWS route tables for the subnets that contain your source database contain an entry for the DESTINATION_IP_RANGE range that routes to the VPN Virtual Private Gateway. 
  5. Add a security group firewall inbound rule to allow traffic for DESTINATION_IP_RANGE `TCP port 5432`. Connectivity can now be established. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


