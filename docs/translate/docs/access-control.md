---
url: https://docs.cloud.google.com/translate/docs/access-control/
title: Control access with IAM \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:07.572043+00:00
---

# Control access with IAM  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control access with IAM

The Cloud Translation - Advanced API (v3) uses Identity and Access Management (IAM) to control access. Assign one or more IAM roles to a principal to grant permissions. For more information, see [IAM basic and predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note:** Cloud Translation - Basic (v2) supports authentication through IAM but not authorization; you cannot specify granular IAM permissions for Cloud Translation - Basic.

## Predefined Cloud Translation roles for v3

The following table lists the predefined roles that give you access to Cloud Translation resources:

Role | Permissions  
---|---  
  
#### Cloud Translation API Admin 

(`roles/cloudtranslate.admin`) Full access to all Cloud Translation resources  |  `automl.models.get` `automl.models.predict` `cloudtranslate.*`

  * `cloudtranslate.adaptiveMtDatasets.create`
  * `cloudtranslate.adaptiveMtDatasets.delete`
  * `cloudtranslate.adaptiveMtDatasets.get`
  * `cloudtranslate.adaptiveMtDatasets.import`
  * `cloudtranslate.adaptiveMtDatasets.list`
  * `cloudtranslate.adaptiveMtDatasets.predict`
  * `cloudtranslate.adaptiveMtFiles.delete`
  * `cloudtranslate.adaptiveMtFiles.get`
  * `cloudtranslate.adaptiveMtFiles.list`
  * `cloudtranslate.adaptiveMtSentences.list`
  * `cloudtranslate.customModels.create`
  * `cloudtranslate.customModels.delete`
  * `cloudtranslate.customModels.get`
  * `cloudtranslate.customModels.list`
  * `cloudtranslate.customModels.predict`
  * `cloudtranslate.datasets.create`
  * `cloudtranslate.datasets.delete`
  * `cloudtranslate.datasets.export`
  * `cloudtranslate.datasets.get`
  * `cloudtranslate.datasets.import`
  * `cloudtranslate.datasets.list`
  * `cloudtranslate.generalModels.batchDocPredict`
  * `cloudtranslate.generalModels.batchPredict`
  * `cloudtranslate.generalModels.docPredict`
  * `cloudtranslate.generalModels.get`
  * `cloudtranslate.generalModels.predict`
  * `cloudtranslate.glossaries.batchDocPredict`
  * `cloudtranslate.glossaries.batchPredict`
  * `cloudtranslate.glossaries.create`
  * `cloudtranslate.glossaries.delete`
  * `cloudtranslate.glossaries.docPredict`
  * `cloudtranslate.glossaries.get`
  * `cloudtranslate.glossaries.list`
  * `cloudtranslate.glossaries.predict`
  * `cloudtranslate.glossaries.update`
  * `cloudtranslate.glossaryentries.create`
  * `cloudtranslate.glossaryentries.delete`
  * `cloudtranslate.glossaryentries.get`
  * `cloudtranslate.glossaryentries.list`
  * `cloudtranslate.glossaryentries.update`
  * `cloudtranslate.languageDetectionModels.predict`
  * `cloudtranslate.locations.get`
  * `cloudtranslate.locations.list`
  * `cloudtranslate.operations.cancel`
  * `cloudtranslate.operations.delete`
  * `cloudtranslate.operations.get`
  * `cloudtranslate.operations.list`
  * `cloudtranslate.operations.wait`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Translation API Editor 

(`roles/cloudtranslate.editor`) Editor of all Cloud Translation resources  |  `automl.models.get` `automl.models.predict` `cloudtranslate.*`

  * `cloudtranslate.adaptiveMtDatasets.create`
  * `cloudtranslate.adaptiveMtDatasets.delete`
  * `cloudtranslate.adaptiveMtDatasets.get`
  * `cloudtranslate.adaptiveMtDatasets.import`
  * `cloudtranslate.adaptiveMtDatasets.list`
  * `cloudtranslate.adaptiveMtDatasets.predict`
  * `cloudtranslate.adaptiveMtFiles.delete`
  * `cloudtranslate.adaptiveMtFiles.get`
  * `cloudtranslate.adaptiveMtFiles.list`
  * `cloudtranslate.adaptiveMtSentences.list`
  * `cloudtranslate.customModels.create`
  * `cloudtranslate.customModels.delete`
  * `cloudtranslate.customModels.get`
  * `cloudtranslate.customModels.list`
  * `cloudtranslate.customModels.predict`
  * `cloudtranslate.datasets.create`
  * `cloudtranslate.datasets.delete`
  * `cloudtranslate.datasets.export`
  * `cloudtranslate.datasets.get`
  * `cloudtranslate.datasets.import`
  * `cloudtranslate.datasets.list`
  * `cloudtranslate.generalModels.batchDocPredict`
  * `cloudtranslate.generalModels.batchPredict`
  * `cloudtranslate.generalModels.docPredict`
  * `cloudtranslate.generalModels.get`
  * `cloudtranslate.generalModels.predict`
  * `cloudtranslate.glossaries.batchDocPredict`
  * `cloudtranslate.glossaries.batchPredict`
  * `cloudtranslate.glossaries.create`
  * `cloudtranslate.glossaries.delete`
  * `cloudtranslate.glossaries.docPredict`
  * `cloudtranslate.glossaries.get`
  * `cloudtranslate.glossaries.list`
  * `cloudtranslate.glossaries.predict`
  * `cloudtranslate.glossaries.update`
  * `cloudtranslate.glossaryentries.create`
  * `cloudtranslate.glossaryentries.delete`
  * `cloudtranslate.glossaryentries.get`
  * `cloudtranslate.glossaryentries.list`
  * `cloudtranslate.glossaryentries.update`
  * `cloudtranslate.languageDetectionModels.predict`
  * `cloudtranslate.locations.get`
  * `cloudtranslate.locations.list`
  * `cloudtranslate.operations.cancel`
  * `cloudtranslate.operations.delete`
  * `cloudtranslate.operations.get`
  * `cloudtranslate.operations.list`
  * `cloudtranslate.operations.wait`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Translation API User 

(`roles/cloudtranslate.user`) User of Cloud Translation and AutoML models  |  `automl.models.get` `automl.models.predict` `cloudtranslate.adaptiveMtDatasets.get` `cloudtranslate.adaptiveMtDatasets.list` `cloudtranslate.adaptiveMtDatasets.predict` `cloudtranslate.adaptiveMtFiles.get` `cloudtranslate.adaptiveMtFiles.list` `cloudtranslate.adaptiveMtSentences.list` `cloudtranslate.customModels.get` `cloudtranslate.customModels.list` `cloudtranslate.customModels.predict` `cloudtranslate.datasets.get` `cloudtranslate.datasets.list` `cloudtranslate.generalModels.*`

  * `cloudtranslate.generalModels.batchDocPredict`
  * `cloudtranslate.generalModels.batchPredict`
  * `cloudtranslate.generalModels.docPredict`
  * `cloudtranslate.generalModels.get`
  * `cloudtranslate.generalModels.predict`

`cloudtranslate.glossaries.batchDocPredict` `cloudtranslate.glossaries.batchPredict` `cloudtranslate.glossaries.docPredict` `cloudtranslate.glossaries.get` `cloudtranslate.glossaries.list` `cloudtranslate.glossaries.predict` `cloudtranslate.glossaryentries.get` `cloudtranslate.glossaryentries.list` `cloudtranslate.languageDetectionModels.predict` `cloudtranslate.locations.*`

  * `cloudtranslate.locations.get`
  * `cloudtranslate.locations.list`

`cloudtranslate.operations.get` `cloudtranslate.operations.list` `cloudtranslate.operations.wait` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Translation API Viewer 

(`roles/cloudtranslate.viewer`) Viewer of all Translation resources  |  `automl.models.get` `cloudtranslate.adaptiveMtDatasets.get` `cloudtranslate.adaptiveMtDatasets.list` `cloudtranslate.adaptiveMtFiles.get` `cloudtranslate.adaptiveMtFiles.list` `cloudtranslate.adaptiveMtSentences.list` `cloudtranslate.customModels.get` `cloudtranslate.customModels.list` `cloudtranslate.datasets.get` `cloudtranslate.datasets.list` `cloudtranslate.generalModels.get` `cloudtranslate.glossaries.get` `cloudtranslate.glossaries.list` `cloudtranslate.glossaryentries.get` `cloudtranslate.glossaryentries.list` `cloudtranslate.locations.*`

  * `cloudtranslate.locations.get`
  * `cloudtranslate.locations.list`

`cloudtranslate.operations.get` `cloudtranslate.operations.list` `cloudtranslate.operations.wait` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Translation API Service Agent 

(`roles/cloudtranslate.serviceAgent`) Gives Cloud Translation Service Account access to consumer resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `automl.datasets.export` `automl.datasets.get` `automl.datasets.list` `automl.models.get` `automl.models.list` `automl.operations.get` `storage.buckets.get` `storage.objects.create` `storage.objects.get` `storage.objects.list`  
  
## Custom roles

If a predefined role doesn't offer the right set of permissions for your use case, create a custom role. Custom roles can include any permissions that you specify. For example, you can create a custom role with specific administrative operations, such as creating glossaries or managing custom models. To create custom roles, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## What's next

  * For more information about granting a role on a project, see [Grant a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role). You can grant predefined or custom roles in this way.
  * To learn more about IAM, see [IAM overview](https://cloud.google.com/iam/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
