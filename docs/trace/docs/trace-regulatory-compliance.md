---
url: https://docs.cloud.google.com/trace/docs/trace-regulatory-compliance/
title: Regulatory support in Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:28.891277+00:00
---

# Regulatory support in Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Resources ](https://docs.cloud.google.com/trace/docs/quotas)



Send feedback 

#  Regulatory support in Cloud Trace Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Trace that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview). 

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Trace APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
cloudtrace.googleapis.com | v1 |  SUPPORTED   
cloudtrace.googleapis.com | v2 |  SUPPORTED   
cloudtrace.googleapis.com | v2beta1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Trace is available for Data Boundary for ITAR in the following Google Cloud regions:

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

#### Resource: No resource

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudtrace.googleapis.com` REST API: `GET` `/v1/projects/{project_id}/traces` RPC methods:

  * `google.devtools.cloudtrace.v1.TraceService.ListTraces`

| 

  * `filter`

  
Service: `cloudtrace.googleapis.com` REST API: `PATCH` `/v1/projects/{project_id}/traces` RPC methods:

  * `google.devtools.cloudtrace.v1.TraceService.PatchTraces`

| 

  * `traces.traces.spans.labels.key`
  * `traces.traces.spans.labels.value`

  
Service: `cloudtrace.googleapis.com` REST API: `POST` `/v2/{name=projects/*}/traces:batchWrite` RPC methods:

  * `google.devtools.cloudtrace.v2.TraceService.BatchWriteSpans`

| 

  * `spans.attributes.attributeMap.key`
  * `spans.attributes.attributeMap.value.boolValue`
  * `spans.attributes.attributeMap.value.intValue`
  * `spans.attributes.attributeMap.value.stringValue.truncatedByteCount`
  * `spans.attributes.attributeMap.value.stringValue.value`
  * `spans.links.link.attributes.attributeMap.key`
  * `spans.links.link.attributes.attributeMap.value.boolValue`
  * `spans.links.link.attributes.attributeMap.value.intValue`
  * `spans.links.link.attributes.attributeMap.value.stringValue.truncatedByteCount`
  * `spans.links.link.attributes.attributeMap.value.stringValue.value`
  * `spans.stackTrace.stackFrames.frame.functionName.truncatedByteCount`
  * `spans.stackTrace.stackFrames.frame.functionName.value`
  * `spans.stackTrace.stackFrames.frame.originalFunctionName.truncatedByteCount`
  * `spans.stackTrace.stackFrames.frame.originalFunctionName.value`
  * `spans.status.code`
  * `spans.status.details.typeUrl`
  * `spans.status.details.value`
  * `spans.status.message`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap.key`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap.value.boolValue`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap.value.intValue`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap.value.stringValue.truncatedByteCount`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap.value.stringValue.value`
  * `spans.timeEvents.timeEvent.annotation.description.truncatedByteCount`
  * `spans.timeEvents.timeEvent.annotation.description.value`

  
  
#### Resource: cloudtrace.googleapis.com/Span

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudtrace.googleapis.com` REST API: `POST` `/v2/{name=projects/*/traces/*/spans/*}` RPC methods:

  * `google.devtools.cloudtrace.v2.TraceService.CreateSpan`

| 

  * `attributes.attributeMap.key`
  * `attributes.attributeMap.value.boolValue`
  * `attributes.attributeMap.value.intValue`
  * `attributes.attributeMap.value.stringValue.truncatedByteCount`
  * `attributes.attributeMap.value.stringValue.value`
  * `links.link.attributes.attributeMap.key`
  * `links.link.attributes.attributeMap.value.boolValue`
  * `links.link.attributes.attributeMap.value.intValue`
  * `links.link.attributes.attributeMap.value.stringValue.truncatedByteCount`
  * `links.link.attributes.attributeMap.value.stringValue.value`
  * `stackTrace.stackFrames.frame.functionName.truncatedByteCount`
  * `stackTrace.stackFrames.frame.functionName.value`
  * `stackTrace.stackFrames.frame.originalFunctionName.truncatedByteCount`
  * `stackTrace.stackFrames.frame.originalFunctionName.value`
  * `status.code`
  * `status.details.typeUrl`
  * `status.details.value`
  * `status.message`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap.key`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap.value.boolValue`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap.value.intValue`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap.value.stringValue.truncatedByteCount`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap.value.stringValue.value`
  * `timeEvents.timeEvent.annotation.description.truncatedByteCount`
  * `timeEvents.timeEvent.annotation.description.value`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Pagination and ordering | 

  * `orderBy`
  * `pageToken`

  
Project and resource identification | 

  * `name`
  * `parent`
  * `projectId`
  * `traceSink.name`
  * `traceSink.outputConfig.destination`
  * `traceSink.outputConfig.pubsubConfig.openTelemetryFormat.version`

  
Scope and resource filtering | 

  * `scope.resourceNames`
  * `scope.traceId`
  * `traceScope.resourceNames`

  
Span display and context | 

  * `displayName.value`
  * `spans.displayName.value`
  * `spans.name`
  * `traces.traces.spans.name`

  
Stack trace build information | 

  * `spans.stackTrace.stackFrames.frame.loadModule.buildId.value`
  * `stackTrace.stackFrames.frame.loadModule.buildId.value`

  
Stack trace file information | 

  * `spans.stackTrace.stackFrames.frame.fileName.value`
  * `stackTrace.stackFrames.frame.fileName.value`

  
Stack trace module information | 

  * `spans.stackTrace.stackFrames.frame.loadModule.module.value`
  * `stackTrace.stackFrames.frame.loadModule.module.value`

  
Stack trace version information | 

  * `spans.stackTrace.stackFrames.frame.sourceVersion.value`
  * `stackTrace.stackFrames.frame.sourceVersion.value`

  
Trace scope details | 

  * `traceScope.description`
  * `traceScope.name`

  
Trace specific identifiers | 

  * `spans.parentSpanId`
  * `spans.spanId`
  * `traceId`

  
OpenTelemetry semantic convention attributes | 

  * `spans.attributes.attributeMap["cloud.account.id"]`
  * `spans.attributes.attributeMap["cloud.availability_zone"]`
  * `spans.attributes.attributeMap["cloud.platform"]`
  * `spans.attributes.attributeMap["cloud.provider"]`
  * `spans.attributes.attributeMap["cloud.region"]`
  * `spans.attributes.attributeMap["cloud.resource_id"]`
  * `spans.attributes.attributeMap["error.type"]`
  * `spans.attributes.attributeMap["faas.name"]`
  * `spans.attributes.attributeMap["gcp.apphub.application.container"]`
  * `spans.attributes.attributeMap["gcp.apphub.application.id"]`
  * `spans.attributes.attributeMap["gcp.apphub.application.location"]`
  * `spans.attributes.attributeMap["gcp.apphub.service.id"]`
  * `spans.attributes.attributeMap["gcp.apphub.workload.id"]`
  * `spans.attributes.attributeMap["gcp.cloud_run.job.execution"]`
  * `spans.attributes.attributeMap["gcp.gce.instance_group_manager.name"]`
  * `spans.attributes.attributeMap["gcp.gce.instance_group_manager.region"]`
  * `spans.attributes.attributeMap["gcp.gce.instance_group_manager.zone"]`
  * `spans.attributes.attributeMap["gcp.project_id"]`
  * `spans.attributes.attributeMap["gcp.resource.location"]`
  * `spans.attributes.attributeMap["gcp.resource.name"]`
  * `spans.attributes.attributeMap["http.response.status.code"]`
  * `spans.attributes.attributeMap["k8s.cluster.name"]`
  * `spans.attributes.attributeMap["k8s.cronjob.name"]`
  * `spans.attributes.attributeMap["k8s.daemonset.name"]`
  * `spans.attributes.attributeMap["k8s.deployment.name"]`
  * `spans.attributes.attributeMap["k8s.namespace"]`
  * `spans.attributes.attributeMap["k8s.statefulset.name"]`
  * `spans.attributes.attributeMap["rpc.grpc.status_code"]`
  * `spans.attributes.attributeMap["rpc.system"]`
  * `spans.links.link.attributes.attributeMap["cloud.account.id"]`
  * `spans.links.link.attributes.attributeMap["cloud.availability_zone"]`
  * `spans.links.link.attributes.attributeMap["cloud.platform"]`
  * `spans.links.link.attributes.attributeMap["cloud.provider"]`
  * `spans.links.link.attributes.attributeMap["cloud.region"]`
  * `spans.links.link.attributes.attributeMap["cloud.resource_id"]`
  * `spans.links.link.attributes.attributeMap["error.type"]`
  * `spans.links.link.attributes.attributeMap["faas.name"]`
  * `spans.links.link.attributes.attributeMap["gcp.apphub.application.container"]`
  * `spans.links.link.attributes.attributeMap["gcp.apphub.application.id"]`
  * `spans.links.link.attributes.attributeMap["gcp.apphub.application.location"]`
  * `spans.links.link.attributes.attributeMap["gcp.apphub.service.id"]`
  * `spans.links.link.attributes.attributeMap["gcp.apphub.workload.id"]`
  * `spans.links.link.attributes.attributeMap["gcp.cloud_run.job.execution"]`
  * `spans.links.link.attributes.attributeMap["gcp.gce.instance_group_manager.name"]`
  * `spans.links.link.attributes.attributeMap["gcp.gce.instance_group_manager.region"]`
  * `spans.links.link.attributes.attributeMap["gcp.gce.instance_group_manager.zone"]`
  * `spans.links.link.attributes.attributeMap["gcp.project_id"]`
  * `spans.links.link.attributes.attributeMap["gcp.resource.location"]`
  * `spans.links.link.attributes.attributeMap["gcp.resource.name"]`
  * `spans.links.link.attributes.attributeMap["http.response.status.code"]`
  * `spans.links.link.attributes.attributeMap["k8s.cluster.name"]`
  * `spans.links.link.attributes.attributeMap["k8s.cronjob.name"]`
  * `spans.links.link.attributes.attributeMap["k8s.daemonset.name"]`
  * `spans.links.link.attributes.attributeMap["k8s.deployment.name"]`
  * `spans.links.link.attributes.attributeMap["k8s.namespace"]`
  * `spans.links.link.attributes.attributeMap["k8s.statefulset.name"]`
  * `spans.links.link.attributes.attributeMap["rpc.grpc.status_code"]`
  * `spans.links.link.attributes.attributeMap["rpc.system"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.account.id"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.availability_zone"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.platform"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.provider"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.region"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.resource_id"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["error.type"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["faas.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.application.container"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.application.id"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.application.location"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.service.id"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.workload.id"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.cloud_run.job.execution"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.gce.instance_group_manager.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.gce.instance_group_manager.region"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.gce.instance_group_manager.zone"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.project_id"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.resource.location"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.resource.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["http.response.status.code"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.cluster.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.cronjob.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.daemonset.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.deployment.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.namespace"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.statefulset.name"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["rpc.grpc.status_code"]`
  * `spans.timeEvents.timeEvent.annotation.attributes.attributeMap["rpc.system"]`
  * `attributes.attributeMap["cloud.account.id"]`
  * `attributes.attributeMap["cloud.availability_zone"]`
  * `attributes.attributeMap["cloud.platform"]`
  * `attributes.attributeMap["cloud.provider"]`
  * `attributes.attributeMap["cloud.region"]`
  * `attributes.attributeMap["cloud.resource_id"]`
  * `attributes.attributeMap["error.type"]`
  * `attributes.attributeMap["faas.name"]`
  * `attributes.attributeMap["gcp.apphub.application.container"]`
  * `attributes.attributeMap["gcp.apphub.application.id"]`
  * `attributes.attributeMap["gcp.apphub.application.location"]`
  * `attributes.attributeMap["gcp.apphub.service.id"]`
  * `attributes.attributeMap["gcp.apphub.workload.id"]`
  * `attributes.attributeMap["gcp.cloud_run.job.execution"]`
  * `attributes.attributeMap["gcp.gce.instance_group_manager.name"]`
  * `attributes.attributeMap["gcp.gce.instance_group_manager.region"]`
  * `attributes.attributeMap["gcp.gce.instance_group_manager.zone"]`
  * `attributes.attributeMap["gcp.project_id"]`
  * `attributes.attributeMap["gcp.resource.location"]`
  * `attributes.attributeMap["gcp.resource.name"]`
  * `attributes.attributeMap["http.response.status.code"]`
  * `attributes.attributeMap["k8s.cluster.name"]`
  * `attributes.attributeMap["k8s.cronjob.name"]`
  * `attributes.attributeMap["k8s.daemonset.name"]`
  * `attributes.attributeMap["k8s.deployment.name"]`
  * `attributes.attributeMap["k8s.namespace"]`
  * `attributes.attributeMap["k8s.statefulset.name"]`
  * `attributes.attributeMap["rpc.grpc.status_code"]`
  * `attributes.attributeMap["rpc.system"]`
  * `links.link.attributes.attributeMap["cloud.account.id"]`
  * `links.link.attributes.attributeMap["cloud.availability_zone"]`
  * `links.link.attributes.attributeMap["cloud.platform"]`
  * `links.link.attributes.attributeMap["cloud.provider"]`
  * `links.link.attributes.attributeMap["cloud.region"]`
  * `links.link.attributes.attributeMap["cloud.resource_id"]`
  * `links.link.attributes.attributeMap["error.type"]`
  * `links.link.attributes.attributeMap["faas.name"]`
  * `links.link.attributes.attributeMap["gcp.apphub.application.container"]`
  * `links.link.attributes.attributeMap["gcp.apphub.application.id"]`
  * `links.link.attributes.attributeMap["gcp.apphub.application.location"]`
  * `links.link.attributes.attributeMap["gcp.apphub.service.id"]`
  * `links.link.attributes.attributeMap["gcp.apphub.workload.id"]`
  * `links.link.attributes.attributeMap["gcp.cloud_run.job.execution"]`
  * `links.link.attributes.attributeMap["gcp.gce.instance_group_manager.name"]`
  * `links.link.attributes.attributeMap["gcp.gce.instance_group_manager.region"]`
  * `links.link.attributes.attributeMap["gcp.gce.instance_group_manager.zone"]`
  * `links.link.attributes.attributeMap["gcp.project_id"]`
  * `links.link.attributes.attributeMap["gcp.resource.location"]`
  * `links.link.attributes.attributeMap["gcp.resource.name"]`
  * `links.link.attributes.attributeMap["http.response.status.code"]`
  * `links.link.attributes.attributeMap["k8s.cluster.name"]`
  * `links.link.attributes.attributeMap["k8s.cronjob.name"]`
  * `links.link.attributes.attributeMap["k8s.daemonset.name"]`
  * `links.link.attributes.attributeMap["k8s.deployment.name"]`
  * `links.link.attributes.attributeMap["k8s.namespace"]`
  * `links.link.attributes.attributeMap["k8s.statefulset.name"]`
  * `links.link.attributes.attributeMap["rpc.grpc.status_code"]`
  * `links.link.attributes.attributeMap["rpc.system"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.account.id"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.availability_zone"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.platform"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.provider"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.region"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["cloud.resource_id"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["error.type"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["faas.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.application.container"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.application.id"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.application.location"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.service.id"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.apphub.workload.id"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.cloud_run.job.execution"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.gce.instance_group_manager.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.gce.instance_group_manager.region"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.gce.instance_group_manager.zone"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.project_id"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.resource.location"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["gcp.resource.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["http.response.status.code"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.cluster.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.cronjob.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.daemonset.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.deployment.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.namespace"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["k8s.statefulset.name"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["rpc.grpc.status_code"]`
  * `timeEvents.timeEvent.annotation.attributes.attributeMap["rpc.system"]`

  
  
### Appendix

Key/value pairs in protected map fields, which have well-established semantic conventions in OpenTelemetry, are not protected, and aren't suitable for sensitive information: 

  * cloud.account.id
  * cloud.availability_zone
  * cloud.platform
  * cloud.provider
  * cloud.region
  * cloud.resource_id
  * error.type
  * faas.name
  * gcp.apphub.application.container
  * gcp.apphub.application.id
  * gcp.apphub.application.location
  * gcp.apphub.service.id
  * gcp.apphub.workload.id
  * gcp.cloud_run.job.execution
  * gcp.gce.instance_group_manager.name
  * gcp.gce.instance_group_manager.region
  * gcp.gce.instance_group_manager.zone
  * gcp.project_id
  * gcp.resource.location
  * gcp.resource.name
  * http.response.status.code
  * k8s.cluster.name
  * k8s.cronjob.name
  * k8s.daemonset.name
  * k8s.deployment.name
  * k8s.namespace
  * k8s.statefulset.name
  * rpc.grpc.status_code
  * rpc.system

  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
