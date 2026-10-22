---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning/
title: Container Scanning roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:06.941495+00:00
---

# Container Scanning roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Container Scanning roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Container Scanning. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Container Scanning roles

Container Scanning offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Container Scanner Service Agent 

(`roles/containerscanning.ServiceAgent`) Gives Container Scanner the access it needs to analyze containers for vulnerabilities and create occurrences using the Container Analysis API  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

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

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `containeranalysis.notes.list` `containeranalysis.occurrences.create` `containeranalysis.occurrences.delete` `containeranalysis.occurrences.get` `containeranalysis.occurrences.list` `containeranalysis.occurrences.update` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.objects.get` `storage.objects.list`  
  
## Container Scanning permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
