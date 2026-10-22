---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/database-users/overview/
title: AlloyDB Omni user role overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:09.548654+00:00
---

# AlloyDB Omni user role overview  |  AlloyDB Omni using the container orchestrator: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/database-users/overview/

This page documents AlloyDB Omni version **15.15.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)



Send feedback 

#  AlloyDB Omni user role overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/database-users/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/database-users/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/database-users/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/database-users/overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/database-users/overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/database-users/overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/database-users/overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/database-users/overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/database-users/overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/database-users/overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/database-users/overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/database-users/overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/database-users/overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/database-users/overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/database-users/overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/database-users/overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/database-users/overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/database-users/overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/database-users/overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/database-users/overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/database-users/overview)

This page describes how AlloyDB Omni works with PostgreSQL roles. This page assumes that you are familiar with PostgreSQL. 

An AlloyDB Omni database uses [the standard PostgreSQL concept of roles](https://www.postgresql.org/docs/current/database-roles.html). A role can act as a database user, a group of users, or both.

A _user role_ has the `LOGIN` privilege that lets users sign in to the AlloyDB Omni system. A _group role_ has member roles with various privileges, which you can grant to or revoke from all members at once.

## AlloyDB Omni predefined PostgreSQL roles

PostgreSQL has a set of [predefined roles](https://www.postgresql.org/docs/current/predefined-roles.html) with various privileges. AlloyDB Omni adds several user and group roles to this set of PostgreSQL's predefined roles.

The following table lists the PostgreSQL roles that AlloyDB Omni predefines:

Role name | Privileges  
---|---  
`alloydbadmin` | `SUPERUSER` (which includes `CREATEROLE`, `CREATEDB`, and `LOGIN`).  
`alloydbmetadata` | By default, this role does not have any privileges.  
In addition, AlloyDB Omni reserves the following role names that are unused but might be used in the future. Role name | Privileges  
---|---  
`alloydbagent` | `NOLOGIN`  
`alloydbexport` | `NOLOGIN`  
`alloydbiamgroupuser` | `NOLOGIN`  
`alloydbiamuser` | `NOLOGIN`  
`alloydbimportexport` | `NOLOGIN`  
`alloydbobservability` | `NOLOGIN`  
`alloydbreplica` | `NOLOGIN`  
`alloydbsqllogical` | `NOLOGIN`  
`alloydbsuperuser` | `NOLOGIN`  
  
### The `alloydbadmin` user role

The `alloydbadmin` role is a predefined role that sets up the database system and performs other superuser tasks. This role has the following privileges:

  * Create extensions that require superuser privileges
  * Create event triggers
  * Create replication users
  * Create replication publications and subscriptions



This role is only used by AlloyDB Omni internal tools and shouldn't be used by users.

### The `alloydbmetadata` role

The `alloydbmetadata` role is a predefined role with fewer privileges, also used by AlloyDB Omni internally. Similar to `alloydbadmin`, this role shouldn't be used by other users.

## What's next

  * [Manage AlloyDB Omni users and roles](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/database-users/manage-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
