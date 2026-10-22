---
url: https://docs.cloud.google.com/deploy/docs/deploy-regulatory-compliance/
title: Regulatory support in Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:47.570458+00:00
---

# Regulatory support in Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Resources ](https://docs.cloud.google.com/deploy/docs/resources)



Send feedback 

#  Regulatory support in Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Deploy that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Deploy APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
clouddeploy.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Deploy is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Automation rules | 

  * `automation.rules.advanceRolloutRule.id`
  * `automation.rules.promoteReleaseRule.id`
  * `automation.rules.repairRolloutRule.id`
  * `automation.rules.timedPromoteReleaseRule.id`

  
Automation selector | 

  * `automation.selector.targets.id`
  * `automation.selector.targets.labels.key`
  * `automation.selector.targets.labels.value`

  
Custom target actions | 

  * `customTargetType.customActions.deployAction`
  * `customTargetType.customActions.renderAction`

  
Custom target configuration | 

  * `customTargetType.description`
  * `customTargetType.name`
  * `customTargetTypeId`

  
Custom target environment variables | 

  * `customTargetType.tasks.deploy.container.env.key`
  * `customTargetType.tasks.deploy.container.env.value`
  * `customTargetType.tasks.render.container.env.key`
  * `customTargetType.tasks.render.container.env.value`

  
Deploy parameters | 

  * `deployParameters.key`
  * `deployParameters.value`
  * `release.deployParameters.key`
  * `release.deployParameters.value`

  
Paging and filtering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Parent resource | 

  * `parent`

  
Release configuration | 

  * `release.skaffoldVersion`
  * `release.targetConfigs.config.runtimeConfigFiles.helmChart.helmRelease`
  * `release.targetConfigs.config.runtimeWorkloadDefinition.cloudRunService.template.encryptionKey`
  * `release.toolVersions.docker`
  * `release.toolVersions.kpt`
  * `release.toolVersions.skaffold`

  
Resource identification | 

  * `automationId`
  * `deliveryPipelineId`
  * `name`
  * `releaseId`
  * `rolloutId`
  * `targetId`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
