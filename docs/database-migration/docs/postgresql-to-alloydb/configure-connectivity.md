---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity/
title: Configure connectivity \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:04.236162+00:00
---

# Configure connectivity  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Configure connectivity Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  
  
  
  


During database migration, the destination database needs to connect to the source database. Database Migration Service provides several ways to configure this connectivity. The connectivity method you choose depends on the type of source database, and whether it resides on-premises, in Google Cloud, or in another cloud provider.

You can configure the following connectivity methods:

  * [ IP allowlists](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-ip-allowlists): Choose this method if you want to use public connectivity. 
  * [ Reverse SSH tunnel using a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel): Choose this method if you want to use secure connectivity, and when you don't have a virtual private cloud (VPC) network in Google Cloud from which you can reach the source database. 
  * Private connectivity: Choose this method if you want the destination database to connect to the private IP of your source. There are two types of private connectivity available: 
    * [ Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering#psc-interfaces): This connectivity method lets your destination database initiate connections to the private IP of your source database without consuming peering quota. Instead, Private Service Connect interfaces use network attachments you create in your VPC. 
    * [ VPC peering](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering#vpc-peering): This method requires that you have a VPC network in Google Cloud from which you can reach the source database. Use VPC peering if you have a [VPN](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpns) or Cloud Interconnect connection set up in Google Cloud. 
  * [ TCP Proxy via cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm): Choose this method when migrating from a Cloud SQL for PostgreSQL instance that uses the old producer network architecture. 



## What's next

  * Learn more about [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).
  * Learn more about [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).
  * Learn more about [using VPC peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 

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


