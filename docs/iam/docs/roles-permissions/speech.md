---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/speech/
title: Speech-to-Text roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:50.870688+00:00
---

# Speech-to-Text roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/speech/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Speech-to-Text roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Speech-to-Text. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Speech-to-Text roles

Role | Permissions  
---|---  
  
#### Cloud Speech Administrator 

(`roles/speech.admin`) Grants full access to all resources in Speech-to-text  |  `speech.*`

  * `speech.adaptations.execute`
  * `speech.config.get`
  * `speech.config.update`
  * `speech.customClasses.create`
  * `speech.customClasses.delete`
  * `speech.customClasses.get`
  * `speech.customClasses.list`
  * `speech.customClasses.undelete`
  * `speech.customClasses.update`
  * `speech.locations.get`
  * `speech.locations.list`
  * `speech.operations.cancel`
  * `speech.operations.delete`
  * `speech.operations.get`
  * `speech.operations.list`
  * `speech.operations.wait`
  * `speech.phraseSets.create`
  * `speech.phraseSets.delete`
  * `speech.phraseSets.get`
  * `speech.phraseSets.list`
  * `speech.phraseSets.undelete`
  * `speech.phraseSets.update`
  * `speech.recognizers.create`
  * `speech.recognizers.delete`
  * `speech.recognizers.get`
  * `speech.recognizers.list`
  * `speech.recognizers.recognize`
  * `speech.recognizers.undelete`
  * `speech.recognizers.update`

  
  
#### Cloud Speech Editor 

(`roles/speech.editor`) Grants access to edit resources in Speech-to-text  |  `speech.adaptations.execute` `speech.customClasses.*`

  * `speech.customClasses.create`
  * `speech.customClasses.delete`
  * `speech.customClasses.get`
  * `speech.customClasses.list`
  * `speech.customClasses.undelete`
  * `speech.customClasses.update`

`speech.locations.*`

  * `speech.locations.get`
  * `speech.locations.list`

`speech.operations.*`

  * `speech.operations.cancel`
  * `speech.operations.delete`
  * `speech.operations.get`
  * `speech.operations.list`
  * `speech.operations.wait`

`speech.phraseSets.*`

  * `speech.phraseSets.create`
  * `speech.phraseSets.delete`
  * `speech.phraseSets.get`
  * `speech.phraseSets.list`
  * `speech.phraseSets.undelete`
  * `speech.phraseSets.update`

`speech.recognizers.*`

  * `speech.recognizers.create`
  * `speech.recognizers.delete`
  * `speech.recognizers.get`
  * `speech.recognizers.list`
  * `speech.recognizers.recognize`
  * `speech.recognizers.undelete`
  * `speech.recognizers.update`

  
  
#### Cloud Speech Client 

(`roles/speech.client`) Grants access to the recognition APIs.  |  `speech.adaptations.execute` `speech.customClasses.get` `speech.customClasses.list` `speech.locations.*`

  * `speech.locations.get`
  * `speech.locations.list`

`speech.operations.get` `speech.operations.list` `speech.operations.wait` `speech.phraseSets.get` `speech.phraseSets.list` `speech.recognizers.get` `speech.recognizers.list` `speech.recognizers.recognize`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Speech-to-Text Service Agent 

(`roles/speech.serviceAgent`) Gives Speech-to-Text service account access to Cloud Storage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Speech-to-Text permissions

Permission | Included in roles  
---|---  
  
#### `speech.adaptations.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.config.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `speech.config.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)   
  
#### `speech.customClasses.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.customClasses.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.customClasses.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.customClasses.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.customClasses.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.customClasses.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)   
  
#### `speech.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)   
  
#### `speech.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `speech.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)   
  
#### `speech.operations.wait`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)   
  
#### `speech.phraseSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.phraseSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.phraseSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.phraseSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.phraseSets.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.phraseSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.recognizers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `speech.recognizers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.recognizers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.recognizers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speech.recognizers.recognize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Cloud Speech Client](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.client) (`roles/speech.client`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `speech.recognizers.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)   
  
#### `speech.recognizers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Speech Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.admin) (`roles/speech.admin`)  [Cloud Speech Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.editor) (`roles/speech.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
