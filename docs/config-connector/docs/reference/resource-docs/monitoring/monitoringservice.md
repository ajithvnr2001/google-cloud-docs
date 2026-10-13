---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringservice/
title: MonitoringService \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:43.310445+00:00
---

# MonitoringService  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringservice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MonitoringService

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud Monitoring  
Google Cloud Service Documentation | [/monitoring/docs/](https://docs.cloud.google.com/monitoring/docs)  
Google Cloud REST Resource Name | v3.services  
Google Cloud REST Resource Documentation | [/monitoring/api/ref_v3/rest/v3/services](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services)  
Config Connector Resource Short Names | gcpmonitoringservice  
gcpmonitoringservices  
monitoringservice  
Config Connector Service Name | monitoring.googleapis.com  
Config Connector Resource Fully Qualified Name | monitoringservices.monitoring.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    displayName: string
    projectRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    telemetry:
      resourceName: string
    

Fields  
---  
`displayName` _Optional_ |  `string` Name used for UI elements listing this Service.  
`projectRef` _Required_ |  `object` Immutable. The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`telemetry` _Optional_ |  `object` Configuration for how to query telemetry on a Service.  
`telemetry.resourceName` _Optional_ |  `string` The full name of the resource that defines this service. Formatted as described in https://cloud.google.com/apis/design/resource_names.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    observedGeneration: integer
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringService
    metadata:
      name: monitoringservice-sample
      labels:
        test1: "value1"
    spec:
      projectRef:
         # Replace ${PROJECT_ID?} with your project ID
         external: "projects/${PROJECT_ID?}"
      displayName: "A basic monitoring service."
      telemetry:
        resourceName: "//storage.googleapis.com/buckets/bucket-id1"
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
