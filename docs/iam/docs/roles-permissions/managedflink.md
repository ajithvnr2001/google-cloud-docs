---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink/
title: BigQuery Engine for Apache Flink roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:19.546075+00:00
---

# BigQuery Engine for Apache Flink roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  BigQuery Engine for Apache Flink roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for BigQuery Engine for Apache Flink. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## BigQuery Engine for Apache Flink roles

Role | Permissions  
---|---  
  
#### Managed Flink Admin Beta

(`roles/managedflink.admin`) Full access to Managed Flink resources.  |  `managedflink.*`

  * `managedflink.deployments.create`
  * `managedflink.deployments.delete`
  * `managedflink.deployments.get`
  * `managedflink.deployments.list`
  * `managedflink.deployments.update`
  * `managedflink.jobs.create`
  * `managedflink.jobs.delete`
  * `managedflink.jobs.get`
  * `managedflink.jobs.list`
  * `managedflink.jobs.update`
  * `managedflink.locations.get`
  * `managedflink.locations.list`
  * `managedflink.operations.cancel`
  * `managedflink.operations.delete`
  * `managedflink.operations.get`
  * `managedflink.operations.list`
  * `managedflink.sessions.create`
  * `managedflink.sessions.delete`
  * `managedflink.sessions.get`
  * `managedflink.sessions.list`
  * `managedflink.sessions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Managed Flink Viewer Beta

(`roles/managedflink.viewer`) Readonly access to Managed Flink resources.  |  `managedflink.deployments.get` `managedflink.deployments.list` `managedflink.jobs.get` `managedflink.jobs.list` `managedflink.locations.*`

  * `managedflink.locations.get`
  * `managedflink.locations.list`

`managedflink.operations.get` `managedflink.operations.list` `managedflink.sessions.get` `managedflink.sessions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Managed Flink Developer Beta

(`roles/managedflink.developer`) Full access to Managed Flink Jobs and Sessions and read access to Deployments.  |  `managedflink.deployments.get` `managedflink.deployments.list` `managedflink.jobs.*`

  * `managedflink.jobs.create`
  * `managedflink.jobs.delete`
  * `managedflink.jobs.get`
  * `managedflink.jobs.list`
  * `managedflink.jobs.update`

`managedflink.locations.*`

  * `managedflink.locations.get`
  * `managedflink.locations.list`

`managedflink.operations.get` `managedflink.operations.list` `managedflink.sessions.*`

  * `managedflink.sessions.create`
  * `managedflink.sessions.delete`
  * `managedflink.sessions.get`
  * `managedflink.sessions.list`
  * `managedflink.sessions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Managed Flink Service Agent 

(`roles/managedflink.serviceAgent`) Gives Managed Flink Service Agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.networkAttachments.create` `compute.networkAttachments.delete` `compute.networkAttachments.get` `compute.networkAttachments.list` `compute.networkAttachments.update` `compute.networks.get` `compute.networks.list` `compute.regionOperations.get` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `dns.networks.targetWithPeeringZone` `managedkafka.clusters.get` `managedkafka.clusters.list` `managedkafka.clusters.update` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `serviceusage.services.use` `storage.objects.get`  
  
## BigQuery Engine for Apache Flink permissions

Permission | Included in roles  
---|---  
  
#### `managedflink.deployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)   
  
#### `managedflink.deployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)   
  
#### `managedflink.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.deployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)   
  
#### `managedflink.jobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.jobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.jobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)   
  
#### `managedflink.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)   
  
#### `managedflink.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.sessions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.sessions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.sessions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.sessions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.viewer) (`roles/managedflink.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
#### `managedflink.sessions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Managed Flink Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.admin) (`roles/managedflink.admin`)  [Managed Flink Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/managedflink#managedflink.developer) (`roles/managedflink.developer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
