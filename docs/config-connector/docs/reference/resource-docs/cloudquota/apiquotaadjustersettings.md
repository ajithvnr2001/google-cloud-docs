---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/cloudquota/apiquotaadjustersettings/
title: APIQuotaAdjusterSettings \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:55.576989+00:00
---

# APIQuotaAdjusterSettings  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/cloudquota/apiquotaadjustersettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APIQuotaAdjusterSettings

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud Quotas  
Google Cloud Service Documentation | [/docs/quotas/](https://docs.cloud.google.com/docs/quotas)  
Google Cloud REST Resource Documentation | [/docs/quotas/reference/rest/v1beta/projects.locations.quotaAdjusterSettings](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaAdjusterSettings)  
Config Connector Resource Short Names | APIQuotaAdjusterSettings  
apiquotaadjustersettings  
gcpapiquotaadjustersettings  
Config Connector Service Name | cloudquotas.googleapis.com  
Config Connector Resource Fully Qualified Name | apiquotaadjustersettings.cloudquota.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    enablement: string
    projectRef:
      external: string
      kind: string
      name: string
      namespace: string
    resourceID: string
    

Fields  
---  
`enablement` _Required_ |  `string` Required. The configured value of the enablement at the given resource.  
`projectRef` _Required_ |  `object` The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.kind` _Optional_ |  `string` The kind of the Project resource; optional but must be `Project` if provided.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`resourceID` _Optional_ |  `string` The APIQuotaAdjusterSettings name. If not given, the metadata.name will be used.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    externalRef: string
    observedGeneration: integer
    observedState:
      etag: string
      updateTime: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`externalRef` |  `string` A unique specifier for the APIQuotaAdjusterSettings resource in Google Cloud.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
`observedState.etag` |  `string` Optional. The current etag of the QuotaAdjusterSettings. If an etag is provided on update and does not match the current server's etag of the QuotaAdjusterSettings, the request will be blocked and an ABORTED error will be returned. See https://google.aip.dev/134#etags for more details on etags.  
`observedState.updateTime` |  `string` Output only. The timestamp when the QuotaAdjusterSettings was last updated.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2025 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: cloudquota.cnrm.cloud.google.com/v1beta1
    kind: APIQuotaAdjusterSettings
    metadata:
      name: apiquotaadjustersettings-sample
    spec:
      resourceID: quotaAdjusterSettings
      projectRef:
        external: projects/${PROJECT_ID?}
      enablement: ENABLED
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
