---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods/
title: Networking methods \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:23.014542+00:00
---

# Networking methods  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Networking methods Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

To create a migration in Database Migration Service, connectivity must be established between the source instance and the AlloyDB destination instance. There are various methods supported. Choose the one that works best for the specific workload. 

Networking method | Description | Advantages | Disadvantages  
---|---|---|---  
**IP allowlist** |  This method works by configuring the source database server to accept connections from the outgoing IP of the Cloud SQL instance. If you choose this method, then Database Migration Service guides you through the setup process during the migration creation. | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.

| 

  * Network traffic occurs over the public Internet.
  * Less secure.
  * Decreased performance.

  
**Proxy via cloud-hosted VM - Reverse-SSH tunnel** |  Establishes connectivity from the destination to the source through a secure reverse SSH tunnel. Requires a bastion host VM in the Google Cloud Platform project as well as a machine (for example, a laptop on the network) that has connectivity to the source. Database Migration Service collects the required information at migration creation time, and auto-generates the script for setting it all up. | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.
  * Recommended for short-lived migration scenarios (POC or small database migrations).

| 

  * The bastion VM is owned and managed by you, and may incur additional costs.

  
**Proxy via cloud-hosted VM - TCP** |  Establishes connectivity from the destination to the source using a TCP proxy through a cloud hosted VM. Database Migration Service collects the required information at migration creation time, and auto-generates the script for setting it all up. Relevant on AlloyDB migrations where the source is on the old network architecture. | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.

| 

  * The bastion VM is owned and managed by you, and may incur additional costs.

  
**VPC peering** |  This method works by configuring the VPCs to communicate with one another.  | 

  * Native Google Cloud solution.
  * Easy to configure.
  * High bandwidth.
  * Recommended for long-running or high-volume migrations.

| 

  * Applicable if both the source and destination databases are hosted in Google Cloud, or if the source is connected to the destination VPC using a VPN (cloud-hosted or on-premises) or Cloud Interconnect.

  
**Private Service Connect interfaces** |  [ Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) let your destination database initiate connections to the private IP of your source database without consuming peering quota. Instead, this connectivity method utilizes network attachments you create in your VPC.  | 

  * Establishes connections to your source private IP by using a network attachment. This method doesn't consume peering quota in your VPC. 
  * The easiest source private connectivity method to configure.

| 

  * This connectivity method is only available when you [ migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance). 
  * Requires setting up a network attachment and adjusting firewall rules.
  * You can't modify the network attachment after you establish the connection. 

For more information about private services access and Private Service Connect in AlloyDB for PostgreSQL, see [Private IP overview](https://docs.cloud.google.com/alloydb/docs/private-ip) in the AlloyDB for PostgreSQL documentation.   
  
## Connectivity limitations

The PostgreSQL to AlloyDB connectivity has the following limitations:

  * AlloyDB supports private connectivity using [private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity). Assigning a public IP address to a cluster is not supported. 
  * You can't change the VPC with which the AlloyDB cluster is peered after the cluster is created.
  * Because AlloyDB uses private services access which internally uses VPC peering, [transitive peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#specifications) isn't supported. Your AlloyDB cluster can only reach internal IP addresses in the same VPC with which it is peered. In order to reach other VPCs, you must use an intermediary proxy. For more details, see the following section.



## Common connectivity scenarios and solutions

### Migrate from a Cloud SQL instance in the old producer network architecture

![An architecture diagram for a private database connection that uses the TCP proxy VM.](https://docs.cloud.google.com/static/database-migration/docs/images/tcp-proxy-diagram-vpc.svg) **Figure 1.** A private connection facilitated by the TCP proxy VM (click to enlarge) ![An architecture diagram for a private database connection that uses the TCP proxy VM.](https://docs.cloud.google.com/static/database-migration/docs/images/tcp-proxy-diagram-vpc.svg)

To migrate from a Cloud SQL for PostgreSQL instance in the old producer network architecture, you must establish connectivity using an intermediary proxy. This is because it isn't possible to have direct connectivity between the source Cloud SQL instance and the AlloyDB destination. You can set up your own proxy solution, although we recommend setting up the TCP proxy VM with the auto-generated script provided by Database Migration Service. See [TCP proxy connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm).

### Migrate from a source in the same Google Cloud project but in a different VPC

Because the VPC in which the AlloyDB cluster resides can't be changed after the cluster is created, you have the following options:

  * The recommended option is to change the VPC of the source instance to match the VPC of the destination instance. For example, if you want to migrate a Cloud SQL instance to AlloyDB, [update the Cloud SQL VPC](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#existing-private-instance) to match the AlloyDB VPC. 

**Caution:** Configuring a private IP address for an existing Cloud SQL instance causes the instance to restart, resulting in downtime.
  * If it's not possible to change the VPC of the source instance to match the VPC of the destination instance, then use an intermediary virtual machine (VM) as a proxy. You can set up your own proxy solution, although we recommend using the [TCP proxy connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm). After Database Migration Service generates your script in the Google Cloud console, add another network interface to the command for creating a TCP proxy instance, and configure it to match the VPC of the source instance. This way, the proxy has connectivity to both the source and destination VPCs.

To add another network interface, append `--network-interface network=SOURCE_NETWORK_NAME` to the `gcloud compute instances create-with-container` command that appears in the script.

**Note:** For custom mode VPC networks, you have to explicitly specify the subnet. The argument you need to append is `--network-interface network=SOURCE_NETWORK_NAME,subnet=SOURCE_SUBNET_NAME`.

An example command to create the proxy:
        
        gcloud compute instances create-with-container … \
          --network-interface subnet=DESTINATION-SUBNET-NAME \
          --network-interface network=SOURCE-NETWORK-NAME

Replace the following:

    * DESTINATION-SUBNET-NAME: The name of the destination subnet. 
    * SOURCE-NETWORK-NAME: The name of the source network.



For more information, see [Create VM instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#creating_virtual_machine_instances_with_multiple_network_interfaces).

### Migrate over the public internet

This method is recommended when migrating from an on-premise instance or from other cloud providers, where there's no existing VPN or Interconnect connection to Google Cloud. To use this method, you need to [configure your destination AlloyDB cluster to use an outbound public IP address](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#add-outbound-connectivity).

### Migrate from a source in a different Google Cloud project

To migrate from a source in a different Google Cloud project, you must either migrate over the internet, or, for internal Google Cloud connectivity, use a shared VPC. Select one of the following options:

  * Use a shared VPC without a proxy. If you want your AlloyDB cluster to reside in a shared VPC, then simply select the VPC where your source resides when creating the cluster. This way, source and destination have direct connectivity.

  * Use a shared VPC with a proxy. If you don't want your AlloyDB cluster to reside in a shared VPC, then you must use an intermediary proxy. You can set up your own proxy solution, but we recommend using the [TCP proxy connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm). Follow these guidelines to create a TCP proxy with an additional network interface on a shared VPC.




### Migrate without allowing the destination to reach the network of the source

This method is recommended when migrating from an on-premise network, where there's a concern of opening the network's firewall to incoming Google Cloud traffic. For this scenario, you can set up a reverse proxy using a Compute Engine instance as an intermediary proxy. We recommend using the [reverse SSH connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel).

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


