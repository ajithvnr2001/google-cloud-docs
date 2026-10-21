---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/alloydb-for-postgresql/
title: AlloyDB for PostgreSQL \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:49.430529+00:00
---

# AlloyDB for PostgreSQL  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/alloydb-for-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

AlloyDB for PostgreSQL is a fully managed PostgreSQL-compatible database service for your most demanding enterprise database workloads. AlloyDB combines the best of Google Cloud with one of the most popular open-source database engines, PostgreSQL, for superior performance, scale, and availability. For information specific to AlloyDB for PostgreSQL, see the [AlloyDB for PostgreSQL documentation](https://docs.cloud.google.com/alloydb/docs).

## Features

If you're new to AlloyDB for PostgreSQL, then be sure to check out the [AlloyDB for PostgreSQL features](https://docs.cloud.google.com/alloydb#all-features) page.

## Instance settings

Many configuration settings go into the creation of a AlloyDB cluster. Your needs may vary from the defaults. See the [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) page for more information.

## Connectivity

AlloyDB for PostgreSQL offers [connectivity](https://docs.cloud.google.com/alloydb/docs/configure-connectivity) through private IP addresses.

In cases where you are migrating from a Cloud SQL for PostgreSQL source that is using the old Cloud SQL producer network architecture, and in several [other scenarios](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods#common_connectivity_scenarios_and_solutions), the recommended connectivity method is a [cloud-hosted TCP proxy](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm). Database Migration Service can provide a guided experience to help you set this up.

[VPC peering](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering) connectivity method is applicable to self-managed sources in Google Cloud, and to sources in other cloud platforms that are connected to your Google Cloud VPC via VPN or Interconnect. [Reverse SSH tunnel](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel) is also offered for scenarios where using unsecure connections are required.

In all cases, SSL/TLS can also be used to secure the underlying network connection between the source and destination databases.

## AlloyDB users

The first time you connect to a new AlloyDB cluster, use the `postgres` account. 

Because it's a managed service, AlloyDB doesn't allow PostgreSQL users to have `SUPER` privileges.

## High availability

AlloyDB instances are [high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/high-availability) by default.

## What's next

Learn more about [everything you can do](https://docs.cloud.google.com/alloydb/docs/overview) with your AlloyDB instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
