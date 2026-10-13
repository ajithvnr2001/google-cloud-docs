---
url: https://docs.cloud.google.com/sql/docs/mysql/iam-roles/
title: Cloud SQL roles \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:20.976391+00:00
---

# Cloud SQL roles  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL roles Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/iam-roles "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles "View this page for the SQL Server database engine")

## Predefined Cloud SQL IAM roles

Cloud SQL provides some predefined roles you can use to provide finer-grained permissions to project members.

The role you grant to a project member controls what actions the member can take. Project members can be individuals, groups, or service accounts. You can grant multiple roles to the same project member, and you can change the roles granted to a project member at any time, provided you have the permissions to do so.

The broader roles include the more narrowly defined roles. For example, the Cloud SQL Editor role includes all of the permissions of the Cloud SQL Viewer role, along with the addition permissions of the Cloud SQL Editor role.

Likewise, the Cloud SQL Admin role includes all of the permissions of the Cloud SQL Editor role, along with its additional permissions.

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud. The roles specific to Cloud SQL provide only Cloud SQL permissions, except for the following Google Cloud permissions, which are needed for general Google Cloud usage:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.quotas.get`
  * `serviceusage.services.get`
  * `serviceusage.services.use`



The following table lists the predefined roles available for Cloud SQL, along with their Cloud SQL permissions: 

Role  
Name | Description  
Cloud SQL permissions  
---|---  
`roles/owner`  
Owner | Full access and control for all Google Cloud resources; manage user access.   
  
`cloudsql.*`  
`roles/editor`  
Editor | Read-write access to all Google Cloud and Cloud SQL resources (full control except for the ability to modify permissions).   
  
All `cloudsql` permissions except for   
`cloudsql.*.getIamPolicy` `cloudsql.*.setIamPolicy`  
`roles/viewer`  
Viewer | Read-only access to all Google Cloud resources, including Cloud SQL resources.  
  
`cloudsql.backupRuns.export`  
`cloudsql.*.get`  
`cloudsql.*.list`  
`roles/cloudsql.admin`  
Cloud SQL Admin | Full control for all Cloud SQL resources.  
  
`cloudsql.*`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.*`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.*`  
`recommender.cloudsqlInstancePerformanceInsights.*`  
`recommender.cloudsqlInstancePerformanceRecommendations.*`  
`recommender.cloudsqlInstanceSecurityInsights.*`  
`recommender.cloudsqlInstanceSecurityRecommendations.*`  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.*`  
`recommender.cloudsqlInstanceOomProbabilityInsights.*`  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.*`  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.*`  
`roles/cloudsql.editor`  
Cloud SQL Editor | Manage Cloud SQL resources. No ability to see or modify permissions, nor modify users or ssl Certs. No ability to import data or restore from a backup, nor clone, delete, or promote instances. No ability to start or stop replicas. No ability to delete databases, replicas, or backups.  
  
`cloudsql.instances.addServerCa`  
`cloudsql.instances.addServerCertificate`  
`cloudsql.instances.connect`  
`cloudsql.instances.export`  
`cloudsql.instances.failover`  
`cloudsql.instances.get`  
`cloudsql.instances.list`  
`cloudsql.instances.listServerCas`  
`cloudsql.instances.listServerCertificates`  
`cloudsql.instances.migrate`  
`cloudsql.instances.reencrypt`  
`cloudsql.instances.restart`  
`cloudsql.instances.rotateServerCa`  
`cloudsql.instances.rotateServerCertificate`  
`cloudsql.instances.truncateLog`  
`cloudsql.instances.update`  
`cloudsql.databases.create`  
`cloudsql.databases.get`  
`cloudsql.databases.list`  
`cloudsql.databases.update`  
`cloudsql.backupRuns.create`  
`cloudsql.backupRuns.export`  
`cloudsql.backupRuns.get`  
`cloudsql.backupRuns.list`  
`cloudsql.backupRuns.update`  
`cloudsql.schemas.view`  
`cloudsql.sslCerts.get`  
`cloudsql.sslCerts.list`  
`cloudsql.users.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update` `recommender.cloudsqlInstancePerformanceInsights.get`  
`recommender.cloudsqlInstancePerformanceInsights.list`  
`recommender.cloudsqlInstancePerformanceInsights.update`  
`recommender.cloudsqlInstancePerformanceRecommendations.get`  
`recommender.cloudsqlInstancePerformanceRecommendations.list`  
`recommender.cloudsqlInstancePerformanceRecommendations.update`  
`recommender.cloudsqlInstanceSecurityInsights.get`  
`recommender.cloudsqlInstanceSecurityInsights.list`  
`recommender.cloudsqlInstanceSecurityInsights.update`  
`recommender.cloudsqlInstanceSecurityRecommendations.get`  
`recommender.cloudsqlInstanceSecurityRecommendations.list`  
`recommender.cloudsqlInstanceSecurityRecommendations.update`  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.get`  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.list`  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.update`  
`recommender.cloudsqlInstanceOomProbabilityInsights.get`  
`recommender.cloudsqlInstanceOomProbabilityInsights.list`  
`recommender.cloudsqlInstanceOomProbabilityInsights.update`  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.get`  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.list`  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.update`  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.list`  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.update`  
`roles/cloudsql.viewer`  
Cloud SQL Viewer | Read-only access to all Cloud SQL resources.  
  
`cloudsql.backupRuns.export`  
`cloudsql.*.get`  
`cloudsql.*.list`  
`cloudsql.instances.listServerCas`  
`cloudsql.instances.listServerCertificates`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get`  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.get`  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list`  
`recommender.cloudsqlInstancePerformanceInsights.get`  
`recommender.cloudsqlInstancePerformanceInsights.list`  
`recommender.cloudsqlInstancePerformanceRecommendations.get`  
`recommender.cloudsqlInstancePerformanceRecommendations.list`  
`recommender.cloudsqlInstanceSecurityInsights.get`  
`recommender.cloudsqlInstanceSecurityInsights.list`  
`recommender.cloudsqlInstanceSecurityRecommendations.get`  
`recommender.cloudsqlInstanceSecurityRecommendations.list`  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.get`  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.list`  
`recommender.cloudsqlInstanceOomProbabilityInsights.get`  
`recommender.cloudsqlInstanceOomProbabilityInsights.list`  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.get`  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.list`  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.get`  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.list`  
`roles/cloudsql.client`  
Cloud SQL Client | Connectivity access to Cloud SQL instances from App Engine and the Cloud SQL Auth Proxy. Not required for accessing an instance using IP addresses.  
  
`cloudsql.instances.connect`  
`cloudsql.instances.get`  
`roles/cloudsql.instanceUser`  
Cloud SQL Instance User | Role allowing access to a Cloud SQL instance.  
  
`cloudsql.instances.get`  
`cloudsql.instances.login`  
`roles/cloudsql.schemaViewer`  
Cloud SQL Schema Viewer  | Role allowing access to a Cloud SQL instance schema in Knowledge Catalog.  
  
`cloudsql.schemas.view`  
`roles/cloudsql.studioUser`  
Cloud SQL Studio User  | Role allowing access to Cloud SQL Studio.  
  
`cloudsql.databases.list`  
`cloudsql.instances.executeSql`  
`cloudsql.instances.get`  
`cloudsql.instances.login`  
`cloudsql.users.list`  
`serviceusage.services.get`  
`serviceusage.services.list`  
  
## Permissions and their roles

The following table lists each permission that Cloud SQL supports, the Cloud SQL roles that include it, and its basic role. 

Permission | Cloud SQL roles | Legacy role  
---|---|---  
`cloudsql.backupRuns.update` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.backupRuns.create` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.backupRuns.delete` | Cloud SQL Admin | Editor  
`cloudsql.backupRuns.export` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`cloudsql.backupRuns.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.backupRuns.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.databases.create` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.databases.delete` | Cloud SQL Admin | Editor  
`cloudsql.databases.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.databases.getIamPolicy` | Cloud SQL Admin | Owner  
`cloudsql.databases.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Studio User  
Cloud SQL Viewer | Viewer  
`cloudsql.databases.setIamPolicy` | Cloud SQL Admin | Owner  
`cloudsql.databases.update` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.addServerCa` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.addServerCertificate` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.clone` | Cloud SQL Admin | Editor  
`cloudsql.instances.connect` | Cloud SQL Admin  
Cloud SQL Client  
Cloud SQL Editor | Editor  
`cloudsql.instances.create` | Cloud SQL Admin | Editor  
`cloudsql.instances.delete` | Cloud SQL Admin | Editor  
`cloudsql.instances.demoteMaster` | Cloud SQL Admin | Editor  
`cloudsql.instances.executeSql` | Cloud SQL Admin  
Cloud SQL Studio User  
| Owner  
`cloudsql.instances.export` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.failover` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.get` | Cloud SQL Admin  
Cloud SQL Client  
Cloud SQL Editor  
Cloud SQL Studio User  
Cloud SQL Viewer | Viewer  
`cloudsql.instances.getIamPolicy` | Cloud SQL Admin | Owner  
`cloudsql.instances.import` | Cloud SQL Admin | Editor  
`cloudsql.instances.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.instances.listServerCas` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.instances.listServerCertificates` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.instances.promoteReplica` | Cloud SQL Admin | Editor  
`cloudsql.instances.resetSslConfig` | Cloud SQL Admin | Editor  
`cloudsql.instances.reencrypt` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.restart` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.restoreBackup` | Cloud SQL Admin | Editor  
`cloudsql.instance.rotateServerCa` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instance.rotateServerCertificate` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.setIamPolicy` | Cloud SQL Admin | Owner  
`cloudsql.instances.startReplica` | Cloud SQL Admin | Editor  
`cloudsql.instances.stopReplica` | Cloud SQL Admin | Editor  
`cloudsql.instances.truncateLog` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.instances.update` | Cloud SQL Admin  
Cloud SQL Editor | Editor  
`cloudsql.schemas.view` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Schema Viewer  
| Viewer  
`cloudsql.sslCerts.create` | Cloud SQL Admin | Editor  
`cloudsql.sslCerts.delete` | Cloud SQL Admin | Editor  
`cloudsql.sslCerts.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.sslCerts.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | Viewer  
`cloudsql.users.create` | Cloud SQL Admin | Editor  
`cloudsql.users.delete` | Cloud SQL Admin | Editor  
`cloudsql.users.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Studio User  
Cloud SQL Viewer | Viewer  
`cloudsql.users.update` | Cloud SQL Admin | Editor  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceDiskUsageTrendInsights.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceOutOfDiskRecommendations.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstancePerformanceInsights.get ` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstancePerformanceInsights.list ` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstancePerformanceInsights.update ` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstancePerformanceRecommendations.get ` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstancePerformanceRecommendations.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstancePerformanceRecommendations.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstanceOomProbabilityInsights.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlInstanceOomProbabilityInsights.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlInstanceOomProbabilityInsights.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstanceSecurityInsights.get ` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceSecurityInsights.list ` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceSecurityInsights.update ` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstanceSecurityRecommendations.get ` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceSecurityRecommendations.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer | N/A  
`recommender.cloudsqlInstanceSecurityRecommendations.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlInstanceUnderprovisionedCpuUsageInsights.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlInstanceUnderprovisionedMemoryUsageInsights.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.get` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.list` | Cloud SQL Admin  
Cloud SQL Editor  
Cloud SQL Viewer  
| N/A  
`recommender.cloudsqlUnderProvisionedInstanceRecommendations.update` | Cloud SQL Admin  
Cloud SQL Editor  
| N/A  
  
## Custom roles

If the predefined roles don't address your unique business requirements, you can define your own custom roles with permissions that you specify. To support this, IAM offers [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

When you create custom roles for Cloud SQL, make sure that if you include either `cloudsql.instances.list` or `cloudsql.instances.get`, that you include them both. Otherwise, the Google Cloud console won't function correctly for Cloud SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
