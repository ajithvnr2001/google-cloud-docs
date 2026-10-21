---
url: https://docs.cloud.google.com/database-center/docs/best-practices-managing-database-fleet-health/
title: Best practices for managing database fleet health \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:12.762237+00:00
---

# Best practices for managing database fleet health  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/best-practices-managing-database-fleet-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Best practices for managing database fleet health Stay organized with collections  Save and categorize content based on your preferences. 

To optimize your database fleet health, we recommend that you follow these best practices for monitoring, availability, and data protection.

## Monitoring

Database monitoring, which entails tracking a database's performance and resources, is critical for maintaining the health of a database management system.

### Perform regular, frequent database health checks

To ensure the health of your database, we recommend that you check the Database Center dashboard regularly (for example, once a week). Database Center doesn't notify you about database health issues. A regular check of your organization's database health issues helps you proactively identify and resolve database health issues.

### View recently added database resources

To verify that the number of recently added database resources match your expectations, we recommend that you check the Database Center dashboard regularly. For more information, see [View recently added database resources](https://docs.cloud.google.com/database-center/docs/view-filter-database-fleet-health-information#view-recently-added-resources).

## Availability configuration

You can edit configurations to improve the durability and reliability of your databases.

### Ensure your resource is failover-protected

When a resource is available in multiple zones, it is considered highly available (HA) and is protected by automatic failover. The purpose of an HA configuration is to reduce downtime when a zone or instance becomes unavailable. This might happen during a zonal outage or when a resource runs out of memory. High availability means that regardless of outages, your data will be available to client applications.

Configuring a resource to have high availability provides data redundancy within a region. Highly available resources have a primary node and a standby node, each in a different zone. Through synchronous replication to each zone's persistent disk, all writes made to the primary node are replicated to disks in both zones before a transaction is reported as committed. In the event of a node or zone failure, the standby node becomes the new primary node, and users are rerouted to the new primary node. This process is called a _failover_.

For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

### Use cross-region replication

When a database group is available in multiple regions, it's using a feature called _cross-region replication_ , which is a way to asynchronously replicate data and applications across regions. We recommend that you use cross-region replication for the following reasons:

  * **Disaster recovery:** If the region for a primary resource becomes unavailable, you can promote a secondary resource in another region to become the primary resource and use it to serve requests.
  * **Geographically distributed data:** Locating your data closer to the applications that need the data can reduce read latency.
  * **Geographic load balancing:** If slow or overloaded connections occur in one region, you can route traffic to another region.
  * **Improved read performance:** Provisioning read-only resources around the world can improve capacity and performance in those areas.



## Data protection

Data protection is important because it can help protect organization data against loss, manipulation, and illegal access.

### Enable automated backups

Backups help you restore lost data to your database resources, and they protect your data from loss or damage. If a database resource experiences a problem, you can restore it to a previous state. Enable automated backups for any resource that contains necessary data.

### Set up long backup retention windows

Your backup retention settings determine the window during which you can recover data if your data experiences errors, corruption, or losses. The longer your backup retention period, the larger your recovery window is for that resource.

### Use enhanced backup protection

Use enhanced protection to back up your Cloud SQL databases. Enhanced protection is a Backup and DR Service feature. To check whether your resource is protected with enhanced backup protection, complete these steps:

  1. Go to the **Resources** page in Database Center.

[Go to Database Center](https://console.cloud.google.com/database-center/resources)

  2. Click  **Column display options**.

  3. If **Backup protection** isn't already selected, select it, and then click **OK**.

  4. Verify that **Backup protection** shows **Enhanced**.




To learn how to configure enhanced backups for Cloud SQL resources, see [Enhanced backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
