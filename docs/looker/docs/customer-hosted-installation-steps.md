---
url: https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps/
title: Customer-hosted installation steps \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:45.947444+00:00
---

# Customer-hosted installation steps  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Customer-hosted installation steps Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to install the Looker application for customers who are hosting an [on-premises](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) Looker deployment. Throughout our documentation, we refer to these as "customer-hosted" deployments.

We also offer the option for Looker to host your Looker deployment. Throughout our documentation we refer to these as "[Looker-hosted](https://docs.cloud.google.com/looker/docs/glossary#looker-hosted)" deployments. Using a Looker-hosted instance greatly reduces the effort required to [install](https://docs.cloud.google.com/looker/docs/looker-hosted-installation-steps), configure, and maintain the Looker application, because Looker handles all necessary IT functions that are related to the Looker application for you.

**Note:** Hosting the Looker application is independent of where your data resides; data always remains in-database and is not copied to the Looker instance. Some Looker features are not available for customer-hosted deployments, or they may require additional configuration or software. To learn more about feature differences between the two hosted options, see the [Choosing a hosting option for a Looker (original) instance](https://docs.cloud.google.com/looker/docs/choosing-hosting-option) documentation page.

Complete the following steps:

  1. Install Looker:

     * [Add Looker to your server](https://docs.cloud.google.com/looker/docs/installing-looker-application).

     * [Configure Looker startup options](https://docs.cloud.google.com/looker/docs/startup-options).

     * [Configure your SSL certificate for proper HTTPS](https://docs.cloud.google.com/looker/docs/ssl-certificate-for-proper-https).

     * [Consider port forwarding for a cleaner URL](https://docs.cloud.google.com/looker/docs/port-forwarding).

     * [Allow Looker support to access your instance](https://docs.cloud.google.com/looker/docs/support-access-customer-hosted-deployment).

     * [Set up Looker monitoring](https://docs.cloud.google.com/looker/docs/monitoring-looker).

     * [Set up a MySQL backend database](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql).

**Note:** We recommend that all new customer-hosted instances set up a MySQL backend database rather than use the default HyperSQL database.
     * [Set up Looker backups](https://docs.cloud.google.com/looker/docs/creating-backups).

     * [Ensure that Looker can access necessary services](https://docs.cloud.google.com/looker/docs/outbound-port-requirements).

     * [Install rendering software](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software).

     * [Determine if your Looker instance can accommodate the Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub#considerations_for_customer-hosted_instances).

  2. [Enable secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access).

  3. [Configure your database for Looker](https://docs.cloud.google.com/looker/docs/dialects).

  4. [Connect Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

  5. [Test your database connectivity](https://docs.cloud.google.com/looker/docs/testing-db-connectivity).

  6. [Configure Looker sign-in options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).




Once your instance is set up, you're ready to [get started with development](https://docs.cloud.google.com/looker/docs/data-modeling).

## Features that require additional configuration

The following Looker features require additional configuration or software to use:

Feature | Additional configuration or alternative  
---|---  
[Paper Size](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#paper_size) | [Install Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium)  
[Expand tables](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#expand_tables_to_show_all_rows)  
[Sending, scheduling, downloading](https://docs.cloud.google.com/looker/docs/managing-business-user-features): 

  * Dashboards in PDF or Visualization format
  * Looks in Visualization or HTML format
  * Explores in PNG (Image of Visualization) or HTML format

  
[Downloading custom visualizations](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations)  
Maintenance tasks: 

  * Updating an instance to a new Looker release
  * Auto-provisioning a new Looker instance
  * Moving to a new host
  * Clustering
  * Configuration management
  * Java memory settings
  * Archiving log files
  * Restoring backups
  * Migrating Looker backend database to MySQL
  * Migrating to AES-256 encryption
  * Changing Looker's encryption keys
  * Enabling Redis cache

| [Self-manage](https://docs.cloud.google.com/looker/docs/managing-customer-hosted-deployment)  
[Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) | [Set up a read replica of the Looker backend database](https://docs.cloud.google.com/looker/docs/system-activity-read-replica-db)  
[Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub) | To address the potential issue of the Looker Action Hub not being able to communicate with the Looker instance, Looker admins can implement one of the [following solutions](https://docs.cloud.google.com/looker/docs/action-hub#considerations_for_customer-hosted_instances). The appropriate solution or combination of solutions will depend on the architecture of the Looker instance: 

  1. Enable the `public_host_url` license feature
  2. Allowlist the egress IP address for the Looker Action Hub
  3. Set up a customer-hosted action hub server

  
Unpackaged JDBC drivers | [Install JDBC driver](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers)  
Load Assets from CDN | Enable the [**Load Assets from CDN** admin setting](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#load_assets_from_cdn) to load assets from the CDN  
Enabling secure database access | If your customer-hosted Looker instance is not on the same private network as its connected database, be sure to secure your data as well, perhaps using one of the following options: 

  1. [Configure an IP address allowlist.](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_1_ip_address_allowlist) Add to the allowlist the IP address or addresses where your Looker instance is hosted
  2. [Configure SSL encryption](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_2_ssl_encryption)
  3. Configure an [SSH tunnel](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_3_ssh_tunnel)

  
Create a backup of a Looker instance | [Generate a keystore-independent backup](https://docs.cloud.google.com/looker/docs/creating-backups#generating_a_keystore-independent_backup)  
[Installing tools from the Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace#installing_a_tool_from_the_marketplace) | [Set up a shared (network) file system](https://docs.cloud.google.com/looker/docs/clustering-looker#shared_file_system)  
[Auto Install assets from the Looker Marketplace / API Explorer](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace#auto_install) |  If you are installing the API Explorer on a customer-hosted Looker instance, for users to view API examples, the server running the Looker instance must be configured to access the public internet server running at the URL `https://githubusercontent.com`.  
Upgrading from OpenJDK 8 to OpenJDK 11 | [Manual upgrade](https://docs.cloud.google.com/looker/docs/upgrading-to-openjdk-11-customer-hosted-instance)  
Upgrading from OpenJDK 11 to OpenJDK 21 | [Manual upgrade](https://docs.cloud.google.com/looker/docs/upgrading-to-openjdk-21-customer-hosted-instance)  
Allowing Looker Support to access a customer-hosted deployment | [Allowlist the IP address for Looker Support](https://docs.cloud.google.com/looker/docs/support-access-customer-hosted-deployment)  
Git security sandboxing for SSH connections | To opt in to the Git CLI security sandboxing enhancement (planned to be available starting in release 26.10), install the [`proot` package](https://proot-me.github.io/) on the host machine running the Looker instance. Looker projects that use HTTPS connections are not affected. If `proot` is not installed, SSH-connected Git operations will still execute successfully but will not have sandboxing active.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
