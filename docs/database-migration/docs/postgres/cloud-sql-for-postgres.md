---
url: https://docs.cloud.google.com/database-migration/docs/postgres/cloud-sql-for-postgres/
title: Cloud SQL for PostgreSQL \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:39.180970+00:00
---

# Cloud SQL for PostgreSQL  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/cloud-sql-for-postgres/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Cloud SQL for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Cloud SQL for PostgreSQL is a fully-managed database service that makes it easy to set up, maintain, manage, and administer your PostgreSQL relational databases on Google Cloud. For information specific to PostgreSQL, see the [PostgreSQL documentation](https://www.postgresql.org/docs/).

## Features

Cloud SQL provides extensive [documentation](https://docs.cloud.google.com/sql/docs). If you're new to Cloud SQL for PostgreSQL, then be sure to check out the [Cloud SQL for PostgreSQL features](https://docs.cloud.google.com/sql/docs/postgres/features) page.

## Instance settings

Many configuration settings go into the creation of a Cloud SQL instance. Your needs may vary from the defaults. See the [Creating instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance) and [Instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings) pages for more information.

## Connectivity

Cloud SQL offers [connectivity](https://docs.cloud.google.com/sql/docs/postgres/connect-overview) through [public](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) IP addresses, [private](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) IP addresses, or both public and private addresses.

For Database Migration Service, the [IP allowlist](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-ip-allowlists) connectivity method is appropriate when using a public IP address, and the [VPC peering](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering) connectivity method is used for private IP addresses.

Cloud SQL recommends using [SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl) when connecting to a Cloud SQL instance.

## Cloud SQL users

The first time you connect to a new Cloud SQL instance, use the `postgres` account. 

Because it's a managed service, Cloud SQL doesn't allow PostgreSQL users to have `SUPER` privileges.

## Cascading read replicas

Database Migration Service lets you migrate data to a Cloud SQL destination instance, and then set up cascading read replicas for that instance. For more information, see [Set up cascading read replicas](https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica).

## High availability

After you [promote](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration) a Cloud SQL replica to become a primary instance, you can configure it for [high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/high-availability). If your HA-configured instance becomes unresponsive, then Cloud SQL automatically switches to serving data from a standby instance.

## What's next

Learn more about [everything you can do](https://docs.cloud.google.com/sql/docs/postgres/how-to) with your Cloud SQL instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
