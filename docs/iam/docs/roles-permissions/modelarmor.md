---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor/
title: Model Armor roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:09.175085+00:00
---

# Model Armor roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Model Armor roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Model Armor. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Model Armor roles

Role | Permissions  
---|---  
  
#### Model Armor Admin 

(`roles/modelarmor.admin`) Grants full access to all modelarmor resources. Intended for administrators & owners.  |  `modelarmor.callouts.invoke` `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`modelarmor.templates.*`

  * `modelarmor.templates.create`
  * `modelarmor.templates.delete`
  * `modelarmor.templates.get`
  * `modelarmor.templates.list`
  * `modelarmor.templates.update`
  * `modelarmor.templates.useToSanitizeInput`
  * `modelarmor.templates.useToSanitizeModelResponse`
  * `modelarmor.templates.useToSanitizeOutput`
  * `modelarmor.templates.useToSanitizeUserPrompt`
  * `modelarmor.templates.useToStreamSanitizeModelResponse`
  * `modelarmor.templates.useToStreamSanitizeUserPrompt`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Model Armor Editor 

(`roles/modelarmor.editor`) Grants access to create and update all model armor resources. Intended for editors.  |  `modelarmor.callouts.invoke` `modelarmor.floorSettings.computeEffectiveFloorSetting` `modelarmor.floorSettings.get` `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`modelarmor.templates.*`

  * `modelarmor.templates.create`
  * `modelarmor.templates.delete`
  * `modelarmor.templates.get`
  * `modelarmor.templates.list`
  * `modelarmor.templates.update`
  * `modelarmor.templates.useToSanitizeInput`
  * `modelarmor.templates.useToSanitizeModelResponse`
  * `modelarmor.templates.useToSanitizeOutput`
  * `modelarmor.templates.useToSanitizeUserPrompt`
  * `modelarmor.templates.useToStreamSanitizeModelResponse`
  * `modelarmor.templates.useToStreamSanitizeUserPrompt`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Model Armor Viewer 

(`roles/modelarmor.viewer`) Grants read access to all model armor resources. Intended for viewers.  |  `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`modelarmor.templates.get` `modelarmor.templates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Model Armor Callout User Beta

(`roles/modelarmor.calloutUser`) Grants access to use Model Armor Callout service. Intended for users & applications which plan to use Model Armor Callout service.  |  `modelarmor.callouts.invoke` `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Model Armor Floor Setting Admin 

(`roles/modelarmor.floorSettingsAdmin`) Grants full access to all Model Armor Floor Setting resources. Intended for administrators & owners.  |  `modelarmor.floorSettings.*`

  * `modelarmor.floorSettings.computeEffectiveFloorSetting`
  * `modelarmor.floorSettings.get`
  * `modelarmor.floorSettings.update`

`modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Model Armor Floor Setting Viewer 

(`roles/modelarmor.floorSettingsViewer`) Grants read access to all Model Armor Floor Setting resources. Intended for viewers.  |  `modelarmor.floorSettings.get` `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Model Armor User 

(`roles/modelarmor.user`) Grants access to sanitize APIs for templates, to use and test topics, and to use Model Armor Callout service. Intended for users & applications which plan to use a template, topic, or callout service for sanitization.  |  `modelarmor.callouts.invoke` `modelarmor.locations.*`

  * `modelarmor.locations.get`
  * `modelarmor.locations.list`

`modelarmor.templates.useToSanitizeInput` `modelarmor.templates.useToSanitizeModelResponse` `modelarmor.templates.useToSanitizeOutput` `modelarmor.templates.useToSanitizeUserPrompt` `modelarmor.templates.useToStreamSanitizeModelResponse` `modelarmor.templates.useToStreamSanitizeUserPrompt` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Model Armor Service Agent 

(`roles/modelarmor.serviceAgent`) Gives Model Armor Service Account permission to make DLP calls.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `dlp.analyzeRiskTemplates.get` `dlp.analyzeRiskTemplates.list` `dlp.deidentifyTemplates.get` `dlp.deidentifyTemplates.list` `dlp.inspectFindings.list` `dlp.inspectTemplates.get` `dlp.inspectTemplates.list` `dlp.jobTriggers.get` `dlp.jobTriggers.list` `dlp.jobs.get` `dlp.jobs.list` `dlp.kms.encrypt` `dlp.locations.*`

  * `dlp.locations.get`
  * `dlp.locations.list`

`dlp.storedInfoTypes.get` `dlp.storedInfoTypes.list` `serviceusage.services.use`  
  
## Model Armor permissions

Permission | Included in roles  
---|---  
  
#### `modelarmor.callouts.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor Callout User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.calloutUser) (`roles/modelarmor.calloutUser`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 

  
  
#### `modelarmor.floorSettings.computeEffectiveFloorSetting`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Model Armor Floor Setting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsAdmin) (`roles/modelarmor.floorSettingsAdmin`)   
  
#### `modelarmor.floorSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Model Armor Floor Setting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsAdmin) (`roles/modelarmor.floorSettingsAdmin`)  [Model Armor Floor Setting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsViewer) (`roles/modelarmor.floorSettingsViewer`)   
  
#### `modelarmor.floorSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor Floor Setting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsAdmin) (`roles/modelarmor.floorSettingsAdmin`)   
  
#### `modelarmor.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Model Armor Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.viewer) (`roles/modelarmor.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Model Armor Callout User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.calloutUser) (`roles/modelarmor.calloutUser`)  [Model Armor Floor Setting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsAdmin) (`roles/modelarmor.floorSettingsAdmin`)  [Model Armor Floor Setting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsViewer) (`roles/modelarmor.floorSettingsViewer`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 

  
  
#### `modelarmor.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Model Armor Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.viewer) (`roles/modelarmor.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Model Armor Callout User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.calloutUser) (`roles/modelarmor.calloutUser`)  [Model Armor Floor Setting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsAdmin) (`roles/modelarmor.floorSettingsAdmin`)  [Model Armor Floor Setting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsViewer) (`roles/modelarmor.floorSettingsViewer`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 

  
  
#### `modelarmor.templates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Model Armor Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.viewer) (`roles/modelarmor.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Model Armor Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.viewer) (`roles/modelarmor.viewer`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.useToSanitizeInput`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 

  
  
#### `modelarmor.templates.useToSanitizeModelResponse`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.useToSanitizeOutput`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 

  
  
#### `modelarmor.templates.useToSanitizeUserPrompt`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `modelarmor.templates.useToStreamSanitizeModelResponse`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)   
  
#### `modelarmor.templates.useToStreamSanitizeUserPrompt`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Model Armor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`)  [Model Armor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.editor) (`roles/modelarmor.editor`)  [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)  [Model Armor User](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
