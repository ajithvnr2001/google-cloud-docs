---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes/
title: NetApp Cloud Volumes Service roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:32.372206+00:00
---

# NetApp Cloud Volumes Service roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  NetApp Cloud Volumes Service roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for NetApp Cloud Volumes Service. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## NetApp Cloud Volumes Service roles

Role | Permissions  
---|---  
  
#### NetApp Cloud Volumes Admin Beta

(`roles/netappcloudvolumes.admin`) This role is managed by NetApp, not Google.  |  `cloudvolumesgcp-api.netapp.com/*`

  * `cloudvolumesgcp-api.netapp.com/activeDirectories.create`
  * `cloudvolumesgcp-api.netapp.com/activeDirectories.delete`
  * `cloudvolumesgcp-api.netapp.com/activeDirectories.get`
  * `cloudvolumesgcp-api.netapp.com/activeDirectories.list`
  * `cloudvolumesgcp-api.netapp.com/activeDirectories.update`
  * `cloudvolumesgcp-api.netapp.com/ipRanges.list`
  * `cloudvolumesgcp-api.netapp.com/jobs.get`
  * `cloudvolumesgcp-api.netapp.com/jobs.list`
  * `cloudvolumesgcp-api.netapp.com/regions.list`
  * `cloudvolumesgcp-api.netapp.com/serviceLevels.list`
  * `cloudvolumesgcp-api.netapp.com/snapshots.create`
  * `cloudvolumesgcp-api.netapp.com/snapshots.delete`
  * `cloudvolumesgcp-api.netapp.com/snapshots.get`
  * `cloudvolumesgcp-api.netapp.com/snapshots.list`
  * `cloudvolumesgcp-api.netapp.com/snapshots.update`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.authorize`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.break`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.create`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.delete`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.get`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.list`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.release`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.resync`
  * `cloudvolumesgcp-api.netapp.com/volumereplication.update`
  * `cloudvolumesgcp-api.netapp.com/volumes.create`
  * `cloudvolumesgcp-api.netapp.com/volumes.delete`
  * `cloudvolumesgcp-api.netapp.com/volumes.get`
  * `cloudvolumesgcp-api.netapp.com/volumes.list`
  * `cloudvolumesgcp-api.netapp.com/volumes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### NetApp Cloud Volumes Viewer Beta

(`roles/netappcloudvolumes.viewer`) This role is managed by NetApp, not Google.  |  `cloudvolumesgcp-api.netapp.com/activeDirectories.get` `cloudvolumesgcp-api.netapp.com/activeDirectories.list` `cloudvolumesgcp-api.netapp.com/ipRanges.list` `cloudvolumesgcp-api.netapp.com/jobs.*`

  * `cloudvolumesgcp-api.netapp.com/jobs.get`
  * `cloudvolumesgcp-api.netapp.com/jobs.list`

`cloudvolumesgcp-api.netapp.com/regions.list` `cloudvolumesgcp-api.netapp.com/serviceLevels.list` `cloudvolumesgcp-api.netapp.com/snapshots.get` `cloudvolumesgcp-api.netapp.com/snapshots.list` `cloudvolumesgcp-api.netapp.com/volumes.get` `cloudvolumesgcp-api.netapp.com/volumes.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## NetApp Cloud Volumes Service permissions

Permission | Included in roles  
---|---  
  
#### `cloudvolumesgcp-api.netapp.com/activeDirectories.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/activeDirectories.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/activeDirectories.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/activeDirectories.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/activeDirectories.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/ipRanges.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/regions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/serviceLevels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/snapshots.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/snapshots.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/snapshots.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/snapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/snapshots.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.authorize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.break`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.release`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.resync`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumereplication.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)  [NetApp Cloud Volumes Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.viewer) (`roles/netappcloudvolumes.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudvolumesgcp-api.netapp.com/volumes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [NetApp Cloud Volumes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/netappcloudvolumes#netappcloudvolumes.admin) (`roles/netappcloudvolumes.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
