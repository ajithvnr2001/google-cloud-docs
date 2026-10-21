---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization/
title: Binary Authorization roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:14:51.534527+00:00
---

# Binary Authorization roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Binary Authorization roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Binary Authorization. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Binary Authorization roles

Role | Permissions  
---|---  
  
#### Binary Authorization Admin 

(`roles/binaryauthorization.admin`) Admin role for Binary Authorization  |  `binaryauthorization.*`

  * `binaryauthorization.attestors.create`
  * `binaryauthorization.attestors.delete`
  * `binaryauthorization.attestors.get`
  * `binaryauthorization.attestors.getIamPolicy`
  * `binaryauthorization.attestors.list`
  * `binaryauthorization.attestors.setIamPolicy`
  * `binaryauthorization.attestors.update`
  * `binaryauthorization.attestors.verifyImageAttested`
  * `binaryauthorization.continuousValidationConfig.get`
  * `binaryauthorization.continuousValidationConfig.getIamPolicy`
  * `binaryauthorization.continuousValidationConfig.setIamPolicy`
  * `binaryauthorization.continuousValidationConfig.update`
  * `binaryauthorization.platformPolicies.create`
  * `binaryauthorization.platformPolicies.delete`
  * `binaryauthorization.platformPolicies.evaluatePolicy`
  * `binaryauthorization.platformPolicies.get`
  * `binaryauthorization.platformPolicies.list`
  * `binaryauthorization.platformPolicies.replace`
  * `binaryauthorization.policy.evaluatePolicy`
  * `binaryauthorization.policy.get`
  * `binaryauthorization.policy.getIamPolicy`
  * `binaryauthorization.policy.setIamPolicy`
  * `binaryauthorization.policy.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Editor 

(`roles/binaryauthorization.editor`) Editor role for Binary Authorization  |  `binaryauthorization.attestors.create` `binaryauthorization.attestors.delete` `binaryauthorization.attestors.get` `binaryauthorization.attestors.getIamPolicy` `binaryauthorization.attestors.list` `binaryauthorization.attestors.update` `binaryauthorization.attestors.verifyImageAttested` `binaryauthorization.continuousValidationConfig.get` `binaryauthorization.continuousValidationConfig.getIamPolicy` `binaryauthorization.continuousValidationConfig.update` `binaryauthorization.platformPolicies.*`

  * `binaryauthorization.platformPolicies.create`
  * `binaryauthorization.platformPolicies.delete`
  * `binaryauthorization.platformPolicies.evaluatePolicy`
  * `binaryauthorization.platformPolicies.get`
  * `binaryauthorization.platformPolicies.list`
  * `binaryauthorization.platformPolicies.replace`

`binaryauthorization.policy.evaluatePolicy` `binaryauthorization.policy.get` `binaryauthorization.policy.getIamPolicy` `binaryauthorization.policy.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Viewer 

(`roles/binaryauthorization.viewer`) Viewer role for Binary Authorization  |  `binaryauthorization.attestors.get` `binaryauthorization.attestors.getIamPolicy` `binaryauthorization.attestors.list` `binaryauthorization.attestors.verifyImageAttested` `binaryauthorization.continuousValidationConfig.get` `binaryauthorization.continuousValidationConfig.getIamPolicy` `binaryauthorization.platformPolicies.evaluatePolicy` `binaryauthorization.platformPolicies.get` `binaryauthorization.platformPolicies.list` `binaryauthorization.policy.evaluatePolicy` `binaryauthorization.policy.get` `binaryauthorization.policy.getIamPolicy` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Attestor Admin 

(`roles/binaryauthorization.attestorsAdmin`) Administrator of Binary Authorization Attestors  |  `binaryauthorization.attestors.*`

  * `binaryauthorization.attestors.create`
  * `binaryauthorization.attestors.delete`
  * `binaryauthorization.attestors.get`
  * `binaryauthorization.attestors.getIamPolicy`
  * `binaryauthorization.attestors.list`
  * `binaryauthorization.attestors.setIamPolicy`
  * `binaryauthorization.attestors.update`
  * `binaryauthorization.attestors.verifyImageAttested`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Attestor Editor 

(`roles/binaryauthorization.attestorsEditor`) Editor of Binary Authorization Attestors  |  `binaryauthorization.attestors.create` `binaryauthorization.attestors.delete` `binaryauthorization.attestors.get` `binaryauthorization.attestors.list` `binaryauthorization.attestors.update` `binaryauthorization.attestors.verifyImageAttested` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Attestor Image Verifier 

(`roles/binaryauthorization.attestorsVerifier`) Caller of Binary Authorization Attestors VerifyImageAttested  |  `binaryauthorization.attestors.get` `binaryauthorization.attestors.list` `binaryauthorization.attestors.verifyImageAttested` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Attestor Viewer 

(`roles/binaryauthorization.attestorsViewer`) Viewer of Binary Authorization Attestors  |  `binaryauthorization.attestors.get` `binaryauthorization.attestors.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Policy Administrator 

(`roles/binaryauthorization.policyAdmin`) Administrator of Binary Authorization Policy  |  `binaryauthorization.continuousValidationConfig.*`

  * `binaryauthorization.continuousValidationConfig.get`
  * `binaryauthorization.continuousValidationConfig.getIamPolicy`
  * `binaryauthorization.continuousValidationConfig.setIamPolicy`
  * `binaryauthorization.continuousValidationConfig.update`

`binaryauthorization.platformPolicies.*`

  * `binaryauthorization.platformPolicies.create`
  * `binaryauthorization.platformPolicies.delete`
  * `binaryauthorization.platformPolicies.evaluatePolicy`
  * `binaryauthorization.platformPolicies.get`
  * `binaryauthorization.platformPolicies.list`
  * `binaryauthorization.platformPolicies.replace`

`binaryauthorization.policy.*`

  * `binaryauthorization.policy.evaluatePolicy`
  * `binaryauthorization.policy.get`
  * `binaryauthorization.policy.getIamPolicy`
  * `binaryauthorization.policy.setIamPolicy`
  * `binaryauthorization.policy.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Policy Editor 

(`roles/binaryauthorization.policyEditor`) Editor of Binary Authorization Policy  |  `binaryauthorization.continuousValidationConfig.get` `binaryauthorization.continuousValidationConfig.update` `binaryauthorization.platformPolicies.*`

  * `binaryauthorization.platformPolicies.create`
  * `binaryauthorization.platformPolicies.delete`
  * `binaryauthorization.platformPolicies.evaluatePolicy`
  * `binaryauthorization.platformPolicies.get`
  * `binaryauthorization.platformPolicies.list`
  * `binaryauthorization.platformPolicies.replace`

`binaryauthorization.policy.evaluatePolicy` `binaryauthorization.policy.get` `binaryauthorization.policy.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Policy Evaluator 

(`roles/binaryauthorization.policyEvaluator`) Evaluator of Binary Authorization Policy  |  `binaryauthorization.platformPolicies.evaluatePolicy` `binaryauthorization.platformPolicies.get` `binaryauthorization.platformPolicies.list` `binaryauthorization.policy.evaluatePolicy` `binaryauthorization.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Binary Authorization Policy Viewer 

(`roles/binaryauthorization.policyViewer`) Viewer of Binary Authorization Policy  |  `binaryauthorization.continuousValidationConfig.get` `binaryauthorization.platformPolicies.get` `binaryauthorization.platformPolicies.list` `binaryauthorization.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Binary Authorization Service Agent 

(`roles/binaryauthorization.serviceAgent`) Can read Notes and Occurrences from the Container Analysis Service to find and verify signatures.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.dockerimages.get` `artifactregistry.repositories.downloadArtifacts` `binaryauthorization.attestors.get` `binaryauthorization.attestors.list` `binaryauthorization.attestors.verifyImageAttested` `binaryauthorization.platformPolicies.evaluatePolicy` `binaryauthorization.policy.evaluatePolicy` `cloudasset.assets.exportResource` `cloudasset.feeds.create` `cloudasset.feeds.delete` `cloudasset.feeds.get` `cloudasset.feeds.update` `containeranalysis.notes.get` `containeranalysis.notes.list` `containeranalysis.notes.listOccurrences` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.objects.list`  
  
## Binary Authorization permissions

Permission | Included in roles  
---|---  
  
#### `binaryauthorization.attestors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Binary Authorization Attestor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsEditor) (`roles/binaryauthorization.attestorsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 

  
  
#### `binaryauthorization.attestors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Binary Authorization Attestor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsEditor) (`roles/binaryauthorization.attestorsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 

  
  
#### `binaryauthorization.attestors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Binary Authorization Attestor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsEditor) (`roles/binaryauthorization.attestorsEditor`)  [Binary Authorization Attestor Image Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsVerifier) (`roles/binaryauthorization.attestorsVerifier`)  [Binary Authorization Attestor Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsViewer) (`roles/binaryauthorization.attestorsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 

  
  
#### `binaryauthorization.attestors.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `binaryauthorization.attestors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Binary Authorization Attestor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsEditor) (`roles/binaryauthorization.attestorsEditor`)  [Binary Authorization Attestor Image Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsVerifier) (`roles/binaryauthorization.attestorsVerifier`)  [Binary Authorization Attestor Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsViewer) (`roles/binaryauthorization.attestorsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 

  
  
#### `binaryauthorization.attestors.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)   
  
#### `binaryauthorization.attestors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Binary Authorization Attestor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsEditor) (`roles/binaryauthorization.attestorsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 

  
  
#### `binaryauthorization.attestors.verifyImageAttested`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Attestor Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsAdmin) (`roles/binaryauthorization.attestorsAdmin`)  [Binary Authorization Attestor Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsEditor) (`roles/binaryauthorization.attestorsEditor`)  [Binary Authorization Attestor Image Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.attestorsVerifier) (`roles/binaryauthorization.attestorsVerifier`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 

  
  
#### `binaryauthorization.continuousValidationConfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Binary Authorization Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyViewer) (`roles/binaryauthorization.policyViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `binaryauthorization.continuousValidationConfig.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `binaryauthorization.continuousValidationConfig.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `binaryauthorization.continuousValidationConfig.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `binaryauthorization.platformPolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `binaryauthorization.platformPolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `binaryauthorization.platformPolicies.evaluatePolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Binary Authorization Policy Evaluator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 

  
  
#### `binaryauthorization.platformPolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Binary Authorization Policy Evaluator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`)  [Binary Authorization Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyViewer) (`roles/binaryauthorization.policyViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 

  
  
#### `binaryauthorization.platformPolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Binary Authorization Policy Evaluator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`)  [Binary Authorization Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyViewer) (`roles/binaryauthorization.policyViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 

  
  
#### `binaryauthorization.platformPolicies.replace`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `binaryauthorization.policy.evaluatePolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Binary Authorization Policy Evaluator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Binary Authorization Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent) (`roles/binaryauthorization.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 

  
  
#### `binaryauthorization.policy.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Binary Authorization Policy Evaluator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`)  [Binary Authorization Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyViewer) (`roles/binaryauthorization.policyViewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 
  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 
  * [Security Center Control Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.controlServiceAgent) (`roles/securitycenter.controlServiceAgent`) 
  * [Security Health Analytics Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.securityHealthAnalyticsServiceAgent) (`roles/securitycenter.securityHealthAnalyticsServiceAgent`) 
  * [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) 

  
  
#### `binaryauthorization.policy.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.viewer) (`roles/binaryauthorization.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `binaryauthorization.policy.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `binaryauthorization.policy.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Binary Authorization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.admin) (`roles/binaryauthorization.admin`)  [Binary Authorization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.editor) (`roles/binaryauthorization.editor`)  [Binary Authorization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyAdmin) (`roles/binaryauthorization.policyAdmin`)  [Binary Authorization Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
