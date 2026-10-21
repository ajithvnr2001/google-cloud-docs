---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery/
title: Talent Solution roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:40:17.068097+00:00
---

# Talent Solution roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Talent Solution roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Talent Solution. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Talent Solution roles

Role | Permissions  
---|---  
  
#### Cloud Talent Solution Admin 

(`roles/cloudjobdiscovery.admin`) Access to Cloud Talent Solution Self-Service Tools.  |  `cloudjobdiscovery.*`

  * `cloudjobdiscovery.companies.create`
  * `cloudjobdiscovery.companies.delete`
  * `cloudjobdiscovery.companies.get`
  * `cloudjobdiscovery.companies.list`
  * `cloudjobdiscovery.companies.update`
  * `cloudjobdiscovery.events.create`
  * `cloudjobdiscovery.jobs.create`
  * `cloudjobdiscovery.jobs.delete`
  * `cloudjobdiscovery.jobs.get`
  * `cloudjobdiscovery.jobs.search`
  * `cloudjobdiscovery.jobs.update`
  * `cloudjobdiscovery.profiles.create`
  * `cloudjobdiscovery.profiles.delete`
  * `cloudjobdiscovery.profiles.get`
  * `cloudjobdiscovery.profiles.search`
  * `cloudjobdiscovery.profiles.update`
  * `cloudjobdiscovery.tenants.create`
  * `cloudjobdiscovery.tenants.delete`
  * `cloudjobdiscovery.tenants.get`
  * `cloudjobdiscovery.tenants.update`
  * `cloudjobdiscovery.tools.access`

`iam.serviceAccounts.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Talent Solution Viewer 

(`roles/cloudjobdiscovery.viewer`) Viewer role for Cloud Talent Solution.  |  `cloudjobdiscovery.companies.get` `cloudjobdiscovery.companies.list` `cloudjobdiscovery.jobs.get` `cloudjobdiscovery.jobs.search` `cloudjobdiscovery.profiles.get` `cloudjobdiscovery.profiles.search` `cloudjobdiscovery.tenants.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Talent Solution Job Editor 

(`roles/cloudjobdiscovery.jobsEditor`) Write access to all job data in Cloud Talent Solution.  |  `cloudjobdiscovery.companies.*`

  * `cloudjobdiscovery.companies.create`
  * `cloudjobdiscovery.companies.delete`
  * `cloudjobdiscovery.companies.get`
  * `cloudjobdiscovery.companies.list`
  * `cloudjobdiscovery.companies.update`

`cloudjobdiscovery.events.create` `cloudjobdiscovery.jobs.*`

  * `cloudjobdiscovery.jobs.create`
  * `cloudjobdiscovery.jobs.delete`
  * `cloudjobdiscovery.jobs.get`
  * `cloudjobdiscovery.jobs.search`
  * `cloudjobdiscovery.jobs.update`

`cloudjobdiscovery.tenants.*`

  * `cloudjobdiscovery.tenants.create`
  * `cloudjobdiscovery.tenants.delete`
  * `cloudjobdiscovery.tenants.get`
  * `cloudjobdiscovery.tenants.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Talent Solution Job Viewer 

(`roles/cloudjobdiscovery.jobsViewer`) Read access to all job data in Cloud Talent Solution.  |  `cloudjobdiscovery.companies.get` `cloudjobdiscovery.companies.list` `cloudjobdiscovery.jobs.get` `cloudjobdiscovery.jobs.search` `cloudjobdiscovery.tenants.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Talent Solution Profile Editor 

(`roles/cloudjobdiscovery.profilesEditor`) Write access to all profile data in Cloud Talent Solution.  |  `cloudjobdiscovery.events.create` `cloudjobdiscovery.profiles.*`

  * `cloudjobdiscovery.profiles.create`
  * `cloudjobdiscovery.profiles.delete`
  * `cloudjobdiscovery.profiles.get`
  * `cloudjobdiscovery.profiles.search`
  * `cloudjobdiscovery.profiles.update`

`cloudjobdiscovery.tenants.*`

  * `cloudjobdiscovery.tenants.create`
  * `cloudjobdiscovery.tenants.delete`
  * `cloudjobdiscovery.tenants.get`
  * `cloudjobdiscovery.tenants.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Talent Solution Profile Viewer 

(`roles/cloudjobdiscovery.profilesViewer`) Read access to all profile data in Cloud Talent Solution.  |  `cloudjobdiscovery.profiles.get` `cloudjobdiscovery.profiles.search` `cloudjobdiscovery.tenants.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Talent Solution permissions

Permission | Included in roles  
---|---  
  
#### `cloudjobdiscovery.companies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)   
  
#### `cloudjobdiscovery.companies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)   
  
#### `cloudjobdiscovery.companies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsViewer) (`roles/cloudjobdiscovery.jobsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.companies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsViewer) (`roles/cloudjobdiscovery.jobsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.companies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)   
  
#### `cloudjobdiscovery.events.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.jobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)   
  
#### `cloudjobdiscovery.jobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)   
  
#### `cloudjobdiscovery.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsViewer) (`roles/cloudjobdiscovery.jobsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.jobs.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsViewer) (`roles/cloudjobdiscovery.jobsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.jobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)   
  
#### `cloudjobdiscovery.profiles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.profiles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.profiles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)  [Cloud Talent Solution Profile Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesViewer) (`roles/cloudjobdiscovery.profilesViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.profiles.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)  [Cloud Talent Solution Profile Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesViewer) (`roles/cloudjobdiscovery.profilesViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.profiles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.tenants.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.tenants.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.tenants.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.viewer) (`roles/cloudjobdiscovery.viewer`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Job Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsViewer) (`roles/cloudjobdiscovery.jobsViewer`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)  [Cloud Talent Solution Profile Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesViewer) (`roles/cloudjobdiscovery.profilesViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudjobdiscovery.tenants.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)  [Cloud Talent Solution Job Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.jobsEditor) (`roles/cloudjobdiscovery.jobsEditor`)  [Cloud Talent Solution Profile Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.profilesEditor) (`roles/cloudjobdiscovery.profilesEditor`)   
  
#### `cloudjobdiscovery.tools.access`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Talent Solution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudjobdiscovery#cloudjobdiscovery.admin) (`roles/cloudjobdiscovery.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
