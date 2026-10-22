---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant/
title: Mandiant roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:18.367462+00:00
---

# Mandiant roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Mandiant roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Mandiant. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Mandiant roles

Role | Permissions  
---|---  
  
#### Mandiant Admin Beta

(`roles/mandiant.admin`) Admin role for mandiant  |  `mandiant.*`

  * `mandiant.genericAttackSurfaceManagements.create`
  * `mandiant.genericAttackSurfaceManagements.delete`
  * `mandiant.genericAttackSurfaceManagements.get`
  * `mandiant.genericAttackSurfaceManagements.update`
  * `mandiant.genericDigitalThreatMonitorings.create`
  * `mandiant.genericDigitalThreatMonitorings.get`
  * `mandiant.genericDigitalThreatMonitorings.update`
  * `mandiant.genericExpertiseOnDemands.create`
  * `mandiant.genericExpertiseOnDemands.delete`
  * `mandiant.genericExpertiseOnDemands.get`
  * `mandiant.genericExpertiseOnDemands.update`
  * `mandiant.genericPlatforms.create`
  * `mandiant.genericPlatforms.delete`
  * `mandiant.genericPlatforms.get`
  * `mandiant.genericPlatforms.update`
  * `mandiant.genericThreatIntels.create`
  * `mandiant.genericThreatIntels.delete`
  * `mandiant.genericThreatIntels.get`
  * `mandiant.genericThreatIntels.update`
  * `mandiant.genericValidations.create`
  * `mandiant.genericValidations.delete`
  * `mandiant.genericValidations.get`
  * `mandiant.genericValidations.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Viewer Beta

(`roles/mandiant.viewer`) Viewer role for mandiant  |  `mandiant.genericAttackSurfaceManagements.get` `mandiant.genericDigitalThreatMonitorings.get` `mandiant.genericExpertiseOnDemands.get` `mandiant.genericPlatforms.get` `mandiant.genericThreatIntels.get` `mandiant.genericValidations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Attack Surface Management Editor Beta

(`roles/mandiant.attackSurfaceManagementEditor`) Access to write Attack Surface Management  |  `mandiant.genericAttackSurfaceManagements.create` `mandiant.genericAttackSurfaceManagements.delete` `mandiant.genericAttackSurfaceManagements.update` `mandiant.genericPlatforms.create` `mandiant.genericPlatforms.delete` `mandiant.genericPlatforms.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Attack Surface Management Viewer Beta

(`roles/mandiant.attackSurfaceManagementViewer`) Access to read Attack Surface Management  |  `mandiant.genericAttackSurfaceManagements.get` `mandiant.genericPlatforms.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Digital Threat Monitoring Editor Beta

(`roles/mandiant.digitalThreatMonitoringEditor`) Access to write Digital Threat Monitoring  |  `mandiant.genericDigitalThreatMonitorings.create` `mandiant.genericDigitalThreatMonitorings.update` `mandiant.genericPlatforms.create` `mandiant.genericPlatforms.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Digital Threat Monitoring Viewer Beta

(`roles/mandiant.digitalThreatMonitoringViewer`) Access to read Digital Threat Monitoring  |  `mandiant.genericDigitalThreatMonitorings.get` `mandiant.genericPlatforms.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Expertise On Demand Editor Beta

(`roles/mandiant.expertiseOnDemandEditor`) Access to write Expertise On Demand  |  `mandiant.genericExpertiseOnDemands.create` `mandiant.genericExpertiseOnDemands.delete` `mandiant.genericExpertiseOnDemands.update` `mandiant.genericPlatforms.create` `mandiant.genericPlatforms.delete` `mandiant.genericPlatforms.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Expertise On Demand Viewer Beta

(`roles/mandiant.expertiseOnDemandViewer`) Access to read Expertise On Demand  |  `mandiant.genericExpertiseOnDemands.get` `mandiant.genericPlatforms.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Threat Intel Editor Beta

(`roles/mandiant.threatIntelEditor`) Access to write Threat Intel  |  `mandiant.genericPlatforms.create` `mandiant.genericPlatforms.delete` `mandiant.genericPlatforms.update` `mandiant.genericThreatIntels.create` `mandiant.genericThreatIntels.delete` `mandiant.genericThreatIntels.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Threat Intel Viewer Beta

(`roles/mandiant.threatIntelViewer`) Access to read Threat Intel  |  `mandiant.genericPlatforms.get` `mandiant.genericThreatIntels.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Validation Editor Beta

(`roles/mandiant.validationEditor`) Access to write Validation  |  `mandiant.genericPlatforms.create` `mandiant.genericPlatforms.delete` `mandiant.genericPlatforms.update` `mandiant.genericValidations.create` `mandiant.genericValidations.delete` `mandiant.genericValidations.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Mandiant Validation Viewer Beta

(`roles/mandiant.validationViewer`) Access to read Validation  |  `mandiant.genericPlatforms.get` `mandiant.genericValidations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Mandiant permissions

Permission | Included in roles  
---|---  
  
#### `mandiant.genericAttackSurfaceManagements.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Attack Surface Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementEditor) (`roles/mandiant.attackSurfaceManagementEditor`)   
  
#### `mandiant.genericAttackSurfaceManagements.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Attack Surface Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementEditor) (`roles/mandiant.attackSurfaceManagementEditor`)   
  
#### `mandiant.genericAttackSurfaceManagements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.viewer) (`roles/mandiant.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Mandiant Attack Surface Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementViewer) (`roles/mandiant.attackSurfaceManagementViewer`)   
  
#### `mandiant.genericAttackSurfaceManagements.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Attack Surface Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementEditor) (`roles/mandiant.attackSurfaceManagementEditor`)   
  
#### `mandiant.genericDigitalThreatMonitorings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Digital Threat Monitoring Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.digitalThreatMonitoringEditor) (`roles/mandiant.digitalThreatMonitoringEditor`)   
  
#### `mandiant.genericDigitalThreatMonitorings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.viewer) (`roles/mandiant.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Mandiant Digital Threat Monitoring Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.digitalThreatMonitoringViewer) (`roles/mandiant.digitalThreatMonitoringViewer`)   
  
#### `mandiant.genericDigitalThreatMonitorings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Digital Threat Monitoring Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.digitalThreatMonitoringEditor) (`roles/mandiant.digitalThreatMonitoringEditor`)   
  
#### `mandiant.genericExpertiseOnDemands.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Expertise On Demand Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandEditor) (`roles/mandiant.expertiseOnDemandEditor`)   
  
#### `mandiant.genericExpertiseOnDemands.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Expertise On Demand Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandEditor) (`roles/mandiant.expertiseOnDemandEditor`)   
  
#### `mandiant.genericExpertiseOnDemands.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.viewer) (`roles/mandiant.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Mandiant Expertise On Demand Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandViewer) (`roles/mandiant.expertiseOnDemandViewer`)   
  
#### `mandiant.genericExpertiseOnDemands.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Expertise On Demand Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandEditor) (`roles/mandiant.expertiseOnDemandEditor`)   
  
#### `mandiant.genericPlatforms.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Attack Surface Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementEditor) (`roles/mandiant.attackSurfaceManagementEditor`)  [Mandiant Digital Threat Monitoring Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.digitalThreatMonitoringEditor) (`roles/mandiant.digitalThreatMonitoringEditor`)  [Mandiant Expertise On Demand Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandEditor) (`roles/mandiant.expertiseOnDemandEditor`)  [Mandiant Threat Intel Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelEditor) (`roles/mandiant.threatIntelEditor`)  [Mandiant Validation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationEditor) (`roles/mandiant.validationEditor`)   
  
#### `mandiant.genericPlatforms.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Attack Surface Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementEditor) (`roles/mandiant.attackSurfaceManagementEditor`)  [Mandiant Expertise On Demand Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandEditor) (`roles/mandiant.expertiseOnDemandEditor`)  [Mandiant Threat Intel Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelEditor) (`roles/mandiant.threatIntelEditor`)  [Mandiant Validation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationEditor) (`roles/mandiant.validationEditor`)   
  
#### `mandiant.genericPlatforms.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.viewer) (`roles/mandiant.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Mandiant Attack Surface Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementViewer) (`roles/mandiant.attackSurfaceManagementViewer`)  [Mandiant Digital Threat Monitoring Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.digitalThreatMonitoringViewer) (`roles/mandiant.digitalThreatMonitoringViewer`)  [Mandiant Expertise On Demand Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandViewer) (`roles/mandiant.expertiseOnDemandViewer`)  [Mandiant Threat Intel Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelViewer) (`roles/mandiant.threatIntelViewer`)  [Mandiant Validation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationViewer) (`roles/mandiant.validationViewer`)   
  
#### `mandiant.genericPlatforms.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Attack Surface Management Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.attackSurfaceManagementEditor) (`roles/mandiant.attackSurfaceManagementEditor`)  [Mandiant Digital Threat Monitoring Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.digitalThreatMonitoringEditor) (`roles/mandiant.digitalThreatMonitoringEditor`)  [Mandiant Expertise On Demand Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.expertiseOnDemandEditor) (`roles/mandiant.expertiseOnDemandEditor`)  [Mandiant Threat Intel Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelEditor) (`roles/mandiant.threatIntelEditor`)  [Mandiant Validation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationEditor) (`roles/mandiant.validationEditor`)   
  
#### `mandiant.genericThreatIntels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Threat Intel Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelEditor) (`roles/mandiant.threatIntelEditor`)   
  
#### `mandiant.genericThreatIntels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Threat Intel Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelEditor) (`roles/mandiant.threatIntelEditor`)   
  
#### `mandiant.genericThreatIntels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.viewer) (`roles/mandiant.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Mandiant Threat Intel Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelViewer) (`roles/mandiant.threatIntelViewer`)   
  
#### `mandiant.genericThreatIntels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Threat Intel Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.threatIntelEditor) (`roles/mandiant.threatIntelEditor`)   
  
#### `mandiant.genericValidations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Validation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationEditor) (`roles/mandiant.validationEditor`)   
  
#### `mandiant.genericValidations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Validation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationEditor) (`roles/mandiant.validationEditor`)   
  
#### `mandiant.genericValidations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.viewer) (`roles/mandiant.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Mandiant Validation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationViewer) (`roles/mandiant.validationViewer`)   
  
#### `mandiant.genericValidations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Mandiant Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.admin) (`roles/mandiant.admin`)  [Mandiant Validation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/mandiant#mandiant.validationEditor) (`roles/mandiant.validationEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
