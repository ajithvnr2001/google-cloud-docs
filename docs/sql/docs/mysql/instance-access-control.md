---
url: https://docs.cloud.google.com/sql/docs/mysql/instance-access-control/
title: About access control \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:43.465021+00:00
---

# About access control  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/instance-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About access control Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/instance-access-control "View this page for the SQL Server database engine")

This page discusses the two levels of access control for Cloud SQL instances. You must configure both levels of access control before you can manage your instance.

## Levels of access control

Configuring access control involves controlling who or what can access the instance. Access control occurs on two levels: 

Instance-level access
     Instance-level access authorizes access to your Cloud SQL instance from an application or client (running on an App Engine standard environment or externally) or from another Google Cloud service, such as Compute Engine.
Database access
     Database access uses [ MySQL's access control system](https://dev.mysql.com/doc/refman/8.4/en/access-control.html) to allow MySQL users to have access to the data in your instance. 

**Note:** For information about controlling who can _manage_ your instance, see [Project access control](https://docs.cloud.google.com/sql/docs/project-access-control).

### Instance-level access

Configuring instance-level access depends on the connection source: Connection source | Configuration method | More information  
---|---|---  
Compute Engine | 

  * Cloud SQL Auth Proxy
  * Authorize static IP address

| 

  * [ Connecting from Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine)

  
App Engine standard environment | 

  * Same project: preconfigured
  * Between projects: configure IAM

| 

  * [ Connecting from App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard)

  
App Engine flexible environment | 

  * Same project: preconfigured
  * Between projects: configure IAM

| 

  * [ Connecting from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible)

  
External applications | 

  * Cloud SQL Auth Proxy
  * Authorize client IP address

| 

  * [ Connecting overview](https://docs.cloud.google.com/sql/docs/mysql/connect-overview)

  
Cloud Run | 

  * A Cloud SQL instance set up with a public IP.
  * Between projects: also configure IAM

| 

  * [ Connecting Using Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)

  
Google Kubernetes Engine | 

  * Private IP
  * If Public IP, Cloud SQL Auth Proxy is required

| 

  * [ Connecting Using Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine)

  
  
### Database access

After a user or application connects to a database instance, the user or application must log in with a user or service account. As part of creating a Cloud SQL instance, you set up the default user (root) account. You can also create more users to give you finer-grained control over access to your instance. 

For more information, see [MySQL users](https://docs.cloud.google.com/sql/docs/mysql/users) and [Configuring the default user account](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#user-root).

## What's next

  * Learn more about [how Cloud SQL works with MySQL users](https://docs.cloud.google.com/sql/docs/mysql/users). 
  * Learn more about the [MySQL Access Privilege System](https://dev.mysql.com/doc/refman/8.4/en/access-control.html).
  * Learn more about your [options for connecting from an external application](https://docs.cloud.google.com/sql/docs/mysql/connect-overview). 
  * Learn about [controlling who can manage your Google Cloud Platform project](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
