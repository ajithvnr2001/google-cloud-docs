---
url: https://docs.cloud.google.com/dataflow/docs/dataflow-regulatory-compliance/
title: Regulatory support in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:57:19.853529+00:00
---

# Regulatory support in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/dataflow-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dataflow/docs/resources)



Send feedback 

#  Regulatory support in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Dataflow that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Dataflow APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
dataflow.googleapis.com | v1beta3 |  SUPPORTED   
  
### Compliance supported regions

Dataflow is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-east1
  * us-east4
  * us-west1
  * us-west2
  * us-west3
  * us-west4
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
Job configuration - environment and worker settings | 

  * `job.environment.workerPools.diskType`
  * `job.environment.workerPools.machineType`
  * `job.environment.workerPools.network`
  * `job.environment.workerPools.subnetwork`
  * `job.environment.workerPools.zone`
  * `job.environment.workerZone`

  
Job configuration - general | 

  * `job.createdFromSnapshotId`
  * `job.id`
  * `job.replaceJobId`
  * `job.replacedByJobId`
  * `jobName`
  * `replaceJobId`

  
Job configuration - logging and monitoring | 

  * `job.environment.workerPools.taskrunnerSettings.logDir`
  * `job.environment.workerPools.taskrunnerSettings.logUploadLocation`
  * `workItemStatuses.metricUpdates.name.context.key`
  * `workItemStatuses.reportedProgress.position.key`
  * `workerMessages.perWorkerMetrics.perStepNamespaceMetrics.metricsNamespace`
  * `workerMessages.workerHealthReport.msg`

  
Job configuration - metadata and labels | 

  * `job.environment.workerPools.metadata.key`
  * `job.jobMetadata.userDisplayProperties.key`
  * `job.labels.key`
  * `launchParameter.containerSpec.metadata.parameters.customMetadata.key`
  * `launchParameter.environment.additionalUserLabels.key`
  * `workerMessages.labels.key`

  
Job configuration - pipeline and transform details | 

  * `job.pipelineDescription.displayData.namespace`
  * `job.pipelineDescription.executionPipelineStage.name`
  * `job.pipelineDescription.originalPipelineTransform.displayData.label`
  * `job.pipelineDescription.originalPipelineTransform.displayData.strValue`
  * `job.pipelineDescription.originalPipelineTransform.id`
  * `job.pipelineDescription.originalPipelineTransform.name`

  
Job configuration - sdk and version information | 

  * `job.environment.sdkPipelineOptions.fields.key`
  * `job.environment.version.fields.key`
  * `job.environment.workerPools.sdkHarnessContainerImages.containerImage`
  * `job.jobMetadata.sdkVersion.version`
  * `launchParameter.containerSpec.image`
  * `launchParameter.containerSpec.sdkInfo.version`

  
Job configuration - service accounts and credentials | 

  * `job.environment.serviceAccountEmail`
  * `job.environment.serviceKmsKeyName`
  * `job.environment.workerPools.taskrunnerSettings.oauthScopes`
  * `launchParameter.containerSpec.defaultEnvironment.kmsKeyName`
  * `launchParameter.environment.kmsKeyName`
  * `launchParameter.environment.serviceAccountEmail`

  
Job configuration - storage and data locations | 

  * `gcsPath`
  * `job.environment.tempStoragePrefix`
  * `job.environment.workerPools.taskrunnerSettings.tempStoragePrefix`
  * `job.stepsLocation`
  * `job.tempFiles`
  * `launchParameter.environment.stagingLocation`

  
Job configuration - taskrunner and worker settings | 

  * `job.environment.workerPools.taskrunnerSettings.harnessCommand`
  * `job.environment.workerPools.taskrunnerSettings.languageHint`
  * `job.environment.workerPools.taskrunnerSettings.parallelWorkerSettings.baseUrl`
  * `job.environment.workerPools.taskrunnerSettings.parallelWorkerSettings.servicePath`
  * `job.environment.workerPools.taskrunnerSettings.vmId`
  * `job.environment.workerPools.taskrunnerSettings.workflowFileName`

  
Project and resource identification | 

  * `componentId`
  * `jobId`
  * `location`
  * `name`
  * `projectId`
  * `snapshotId`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
