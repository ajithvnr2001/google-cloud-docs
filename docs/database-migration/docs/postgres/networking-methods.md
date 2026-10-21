---
url: https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods/
title: Networking methods \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:39.229966+00:00
---

# Networking methods  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Networking methods Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

To create a migration in Database Migration Service, connectivity must be established between the source instance and the Cloud SQL destination instance. There are various methods supported. Choose the one that works best for the specific workload. 

Networking method | Description | Advantages | Disadvantages  
---|---|---|---  
**IP allowlist** |  This method works by configuring the source database server to accept connections from the outgoing IP of the Cloud SQL instance. If you choose this method, then Database Migration Service guides you through the setup process during the migration creation. | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.

| 

  * Network traffic occurs over the public Internet.
  * Less secure.
  * Decreased performance.

  
**Reverse-SSH tunnel via cloud hosted VM** |  Establishes connectivity from the destination to the source through a secure reverse SSH tunnel. Requires a bastion host VM in the Google Cloud Platform project as well as a machine (for example, a laptop on the network) that has connectivity to the source. Database Migration Service collects the required information at migration creation time, and auto-generates the script for setting it all up. | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.
  * Recommended for short-lived migration scenarios (POC or small database migrations).

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

  * This connectivity method is only available when you [ migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance). 
  * Requires setting up a network attachment and adjusting firewall rules.
  * You can't modify the network attachment after you establish the connection. 

For more information about private services access and Private Service Connect in Cloud SQL for PostgreSQL see [ Private Service Connect outbound connections](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound) in the Cloud SQL documentation.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

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
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

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


