---
url: https://docs.cloud.google.com/sql/docs/sqlserver/instance-access-control/
title: About access control \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:38.064295+00:00
---

# About access control  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/instance-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  About access control Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control "View this page for the PostgreSQL database engine") | SQL Server

This page discusses the two levels of access control for Cloud SQL instances. You must configure both levels of access control before you can manage your instance.

## Levels of access control

Configuring access control involves controlling who or what can access the instance. Access control occurs on two levels: 

Instance-level access
     Instance-level access authorizes access to your Cloud SQL instance from an application or client (running on an App Engine standard environment or externally) or from another Google Cloud service, such as Compute Engine.
Database access
     Database access uses [ server-level roles](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles) to control which SQL Server users can access the data in your instance. 

**Note:** For information about controlling who can _manage_ your instance, see [Project access control](https://docs.cloud.google.com/sql/docs/project-access-control).

### Instance-level access

How you configure instance-level access depends on where you are connecting from: Connection source | Access configuration options | More information  
---|---|---  
Google Kubernetes Engine | 

  * Cloud SQL Auth Proxy Docker image

| 

  * [ Connecting from Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/sqlserver/connect-kubernetes-engine)

  
App Engine standard environment | 

  * Same project: configure IAM
  * Between projects: configure IAM

| 

  * [ Connecting from standard environment standard environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-standard)

  
flexible environment | 

  * Same project: preconfigured
  * Between projects: configure IAM

| 

  * [ Connecting from standard environment flexible environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-flexible)

  
`sqlcmd` client | 

  * Cloud SQL Auth Proxy
  * Authorize client IP address

| 

  * [ Connecting a client using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy)
  * [ Connecting a client using public IP](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip)

  
External applications | 

  * Cloud SQL Auth Proxy
  * Authorize client IP address

| 

  * [ Connecting to Cloud SQL from external applications](https://docs.cloud.google.com/sql/docs/sqlserver/connect-external-app)

  
Cloud Run | 

  * A Cloud SQL instance set up with a public IP.
  * Between projects: also configure IAM

| 

  * [ Connecting from Cloud Run (fully managed) to Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run)

  
Google Kubernetes Engine | 

  * Private IP
  * If Public IP, Cloud SQL Auth Proxy is required

| 

  * [ Connecting from Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/sqlserver/connect-kubernetes-engine)

  
  
### Database access

After a user or application connects to a database instance, the user or application must log in with a user or service account. As part of creating a Cloud SQL instance, you set up the default user (root) account. You can also create more users to give you finer-grained control over access to your instance. 

For more information, see [SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/users) and [ Creating and managing SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).

## What's next

  * Learn more about [how Cloud SQL works with SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/users). 
  * Learn more about [SQL Server roles](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles).
  * Learn more about your [options for connecting from an external application](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview). 
  * Learn about [controlling who can manage your Google Cloud Platform project](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
