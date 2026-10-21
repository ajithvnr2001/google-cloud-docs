---
url: https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control/
title: Access control with IAM \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:31.848123+00:00
---

# Access control with IAM  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Analysis uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) to grant granular access to specific resources depending on the task you are going to perform.

This page describes permissions to control access to Artifact Analysis.

## Before you begin

  1. Read about [metadata storage concepts](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage).
  2. Read [how to grant, revoke, and change access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to resources.



## IAM roles for metadata providers and customers

Metadata management in Artifact Analysis involves two entities that require different level of access:

  * A **provider** that creates metadata stored in [notes](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#note).
  * A **customer** that identifies [occurrences](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#occurrence) of notes.



### Metadata providers

A metadata provider in Artifact Analysis is a writer of resource metadata. It creates notes, which describe something that can happen to a resource.

We recommend that you create a Google Cloud project dedicated exclusively to storing notes. In that project, restrict access to a user or service account with the following roles:

  * **Container Analysis Notes Editor** \- To create notes your customers can attach occurrences to.

  * **Container Analysis Occurrences for Notes Viewer** \- To list all the occurrences attached to a note.




### Metadata customers

A metadata customer in Artifact Analysis attaches information to metadata resources. It creates occurrences, which are instances of notes and target a specific image within a project.

As a customer, to be able to attach occurrences to notes and to list them, grant the following roles to your user or service account:

  * **Container Analysis Occurrences Editor** \- Grant this role in the **customer** project to create occurrences.

  * **Container Analysis Notes Attacher** \- Grant this role in the **provider** project to attach occurrences to notes.

  * **Container Analysis Occurrences Viewer** \- Grant this role in the **customer** project to list occurrences within that project.




## Vulnerability metadata

An additional security measure for vulnerability metadata is that Artifact Analysis allows providers to create and manage vulnerability occurrences on behalf of many customers. The metadata customers don't have write permission to third-party provider vulnerability occurrences in their own projects.

This means, for example, that Artifact Analysis can create vulnerability occurrences for images in your project, but you cannot add or remove any vulnerability information that Artifact Analysis detects.

This helps to enforce security policies by preventing manipulation of vulnerability metadata on the customer side.

## IAM roles

The following table lists the Artifact Analysis IAM roles and the permissions that they include:

Role | Permissions  
---|---  
  
#### Container Analysis Admin 

(`roles/containeranalysis.admin`) Access to all Container Analysis resources.  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.getIamPolicy` `containeranalysis.notes.list` `containeranalysis.notes.setIamPolicy` `containeranalysis.notes.update` `containeranalysis.occurrences.*`

  * `containeranalysis.occurrences.create`
  * `containeranalysis.occurrences.delete`
  * `containeranalysis.occurrences.get`
  * `containeranalysis.occurrences.getIamPolicy`
  * `containeranalysis.occurrences.list`
  * `containeranalysis.occurrences.setIamPolicy`
  * `containeranalysis.occurrences.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Editor 

(`roles/containeranalysis.editor`) Editor role for Container Analysis  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.getIamPolicy` `containeranalysis.notes.list` `containeranalysis.notes.listOccurrences` `containeranalysis.notes.update` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.getIamPolicy` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Viewer 

(`roles/containeranalysis.viewer`) Viewer role for Container Analysis  |  `containeranalysis.notes.get` `containeranalysis.notes.getIamPolicy` `containeranalysis.notes.list` `containeranalysis.occurrences.get` `containeranalysis.occurrences.getIamPolicy` `containeranalysis.occurrences.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Notes Attacher 

(`roles/containeranalysis.notes.attacher`) Can attach Container Analysis Occurrences to Notes.  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.get`  
  
#### Container Analysis Notes Editor 

(`roles/containeranalysis.notes.editor`) Can edit Container Analysis Notes.  |  `containeranalysis.notes.attachOccurrence` `containeranalysis.notes.create` `containeranalysis.notes.delete` `containeranalysis.notes.get` `containeranalysis.notes.list` `containeranalysis.notes.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Occurrences for Notes Viewer 

(`roles/containeranalysis.notes.occurrences.viewer`) Can view all Container Analysis Occurrences attached to a Note.  |  `containeranalysis.notes.get` `containeranalysis.notes.listOccurrences`  
  
#### Container Analysis Notes Viewer 

(`roles/containeranalysis.notes.viewer`) Can view Container Analysis Notes.  |  `containeranalysis.notes.get` `containeranalysis.notes.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Occurrences Editor 

(`roles/containeranalysis.occurrences.editor`) Can edit Container Analysis Occurrences.  |  `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Container Analysis Occurrences Viewer 

(`roles/containeranalysis.occurrences.viewer`) Can view Container Analysis Occurrences.  |  `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Container Analysis Service Agent 

(`roles/containeranalysis.ServiceAgent`) Gives Container Analysis API the access it needs to function  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `containeranalysis.notes.list` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `pubsub.messageTransforms.validate` `pubsub.schemas.attach` `pubsub.schemas.commit` `pubsub.schemas.create` `pubsub.schemas.delete` `pubsub.schemas.get` `pubsub.schemas.getIamPolicy` `pubsub.schemas.list` `pubsub.schemas.listRevisions` `pubsub.schemas.rollback` `pubsub.schemas.validate` `pubsub.snapshots.create` `pubsub.snapshots.delete` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.listEffectiveTags` `pubsub.snapshots.listTagBindings` `pubsub.snapshots.seek` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.listEffectiveTags` `pubsub.subscriptions.listTagBindings` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.listEffectiveTags` `pubsub.topics.listTagBindings` `pubsub.topics.publish` `pubsub.topics.update` `pubsub.topics.updateTag` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.values.test` `storage.objects.get` `storage.objects.list`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
