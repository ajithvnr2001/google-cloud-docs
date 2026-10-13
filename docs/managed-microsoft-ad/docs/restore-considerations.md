---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/restore-considerations/
title: Considerations for restoring a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:44.528049+00:00
---

# Considerations for restoring a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/restore-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Considerations for restoring a domain Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the list of items you should consider for restoring a Managed Microsoft AD domain.

When you take a backup of your domain, Managed Microsoft AD captures a snapshot of the domain along with its configurations. To know how the backup and restore process impacts the Managed Microsoft AD features and decide how to restore a domain, read the following sections.

## SQL Server integration

For restoring from a backup associated with SQL Server integration, consider the following:

  * If you experience some errors after you restore your domain from a backup with an SQL Server integration, you must reauthenticate the SQL Server instances that are already connected to the domain.

  * If you restore your domain from a backup taken before the SQL Server integration, you can observe some stale resources. You can either ignore or clean them up by [removing Windows Authentication from the SQL Server instances](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#removing-windows-authentication-from-an-instance).




## Trust relationships

For restoring from a backup associated with trust relationships, consider the following:

  * If you restore your domain from a backup taken after creating the trust relationships, you must update the trust health by [validating the trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-trusts#validating-trust).

  * If you restore your domain from a backup taken before creating the trust relationships, you can observe stale entries that show as **Connected** in the **Trust relationships** section of the domain page. You must update the trust health by [validating the trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-trusts#validating-trust). You can then either delete the trust or [recreate the trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust).




## Domain peerings

For restoring from a backup associated with domain peerings, consider the following:

  * If you restore your domain from a backup with domain peerings, the domain peerings continue to exist and function as usual.

  * If you restore your domain from a backup taken before creating the domain peerings, the domain peerings continue to exist and function as usual. You must [delete the domain peerings](https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domain-peering#delete_domain_peering) manually.




## What's next

  * [Back up and restore a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore).

  * [Create a trust with an on-premises domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust).

  * To manage a one-way trust relationship between an on-premises domain and a Managed Microsoft AD domain, see [Manage trusts](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-trusts).

  * To integrate Microsoft SQL Server with Managed Microsoft AD, see [Connect Microsoft SQL Server](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-sql-server).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
