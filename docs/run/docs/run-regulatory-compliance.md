---
url: https://docs.cloud.google.com/run/docs/run-regulatory-compliance/
title: Regulatory support in Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:54.637358+00:00
---

# Regulatory support in Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/run-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Resources ](https://docs.cloud.google.com/run/docs/resources)



Send feedback 

#  Regulatory support in Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Run that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Run APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
run.googleapis.com | v1 |  SUPPORTED   
run.googleapis.com | v2 |  SUPPORTED   
  
### Compliance supported regions

Cloud Run is available for Data Boundary for ITAR in the following Google Cloud regions:

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



### API fields for sensitive data

#### Resource: run.googleapis.com/Service

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `run.googleapis.com` REST API: `PATCH` `/v2/{service.name=projects/*/locations/*/services/*}` RPC methods:

  * `google.cloud.run.v2.Services.UpdateService`

| 

  * `service.template.containers.sourceCode.inlinedSource.sources.content`
  * `service.template.containers.sourceCode.inlinedSource.sources.filename`

  
Service: `run.googleapis.com` REST API: `POST` `/v2/{parent=projects/*/locations/*}/services` RPC methods:

  * `google.cloud.run.v2.Services.CreateService`

| 

  * `service.template.containers.sourceCode.inlinedSource.sources.content`
  * `service.template.containers.sourceCode.inlinedSource.sources.filename`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Container configuration - command and arguments | 

  * `job.spec.template.spec.template.spec.containers.args`
  * `job.spec.template.spec.template.spec.containers.command`
  * `overrides.containerOverrides.args`
  * `service.spec.template.spec.containers.command`
  * `workerPool.spec.template.spec.containers.args`
  * `workerPool.spec.template.spec.containers.command`

  
Container configuration - environment variables | 

  * `job.spec.template.spec.template.spec.containers.env.valueFrom.configMapKeyRef.name`
  * `job.spec.template.spec.template.spec.containers.env.valueFrom.secretKeyRef.name`
  * `overrides.containerOverrides.env.valueFrom.configMapKeyRef.localObjectReference.name`
  * `overrides.containerOverrides.env.valueFrom.configMapKeyRef.name`
  * `overrides.containerOverrides.env.valueFrom.secretKeyRef.localObjectReference.name`
  * `overrides.containerOverrides.env.valueFrom.secretKeyRef.name`

  
Container configuration - image and resources | 

  * `buildpackBuild.baseImage`
  * `job.spec.template.spec.template.spec.containers.image`
  * `job.spec.template.spec.template.spec.containers.resources.limits.key`
  * `job.spec.template.spec.template.spec.containers.resources.requests.key`
  * `workerPool.spec.template.spec.containers.image`
  * `workerPool.spec.template.spec.containers.resources.limits.key`

  
Container configuration - networking and probes | 

  * `job.spec.template.spec.template.spec.containers.livenessProbe.httpGet.host`
  * `job.spec.template.spec.template.spec.containers.ports.name`
  * `job.spec.template.spec.template.spec.containers.readinessProbe.httpGet.host`
  * `workerPool.spec.template.spec.containers.livenessProbe.httpGet.host`
  * `workerPool.spec.template.spec.containers.ports.name`
  * `workerPool.spec.template.spec.containers.readinessProbe.httpGet.host`

  
Container configuration - secrets and configmaps | 

  * `job.spec.template.spec.template.spec.containers.envFrom.configMapRef.localObjectReference.name`
  * `job.spec.template.spec.template.spec.containers.envFrom.configMapRef.name`
  * `job.spec.template.spec.template.spec.containers.envFrom.secretRef.localObjectReference.name`
  * `job.spec.template.spec.template.spec.containers.envFrom.secretRef.name`
  * `workerPool.spec.template.spec.containers.envFrom.configMapRef.name`
  * `workerPool.spec.template.spec.containers.envFrom.secretRef.name`

  
Container configuration - volumes | 

  * `job.spec.template.spec.template.spec.volumes.configMap.items.key`
  * `job.spec.template.spec.template.spec.volumes.configMap.name`
  * `job.spec.template.spec.template.spec.volumes.secret.items.key`
  * `job.spec.template.spec.template.spec.volumes.secret.secretName`
  * `workerPool.spec.template.spec.volumes.secret.items.key`
  * `workerPool.spec.template.spec.volumes.secret.secretName`

  
Filtering and pagination | 

  * `fieldSelector`
  * `filter`
  * `labelSelector`
  * `continue`

  
Metadata and annotations | 

  * `domainMapping.metadata.annotations.key`
  * `domainMapping.metadata.annotations.value`
  * `job.metadata.annotations.key`
  * `job.metadata.annotations.value`
  * `service.metadata.annotations.key`
  * `service.metadata.annotations.value`

  
Operational control | 

  * `dryRun`
  * `operationId`
  * `propagationPolicy`

  
Resource identification | 

  * `apiVersion`
  * `kind`
  * `name`
  * `parent`
  * `region`
  * `serviceId`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
