---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesharedvpchostproject/
title: ComputeSharedVPCHostProject \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:16.518916+00:00
---

# ComputeSharedVPCHostProject  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesharedvpchostproject/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ComputeSharedVPCHostProject

**Property** | **Value**  
---|---  
Google Cloud Service Name | Compute Engine  
Google Cloud Service Documentation | [/compute/docs/](https://docs.cloud.google.com/compute/docs)  
Google Cloud REST Resource Name | v1.projects.enableXpnHost  
Google Cloud REST Resource Documentation | [/compute/docs/reference/rest/v1/projects/enableXpnHost](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/enableXpnHost)  
Config Connector Resource Short Names | computesharedvpchostproject  
gcpcomputesharedvpchostproject  
gcpcomputesharedvpchostprojects  
Config Connector Service Name | compute.googleapis.com  
Config Connector Resource Fully Qualified Name | computesharedvpchostprojects.compute.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    ComputeSharedVPCHostProject has an empty Spec
    

Fields  
---  
  
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
`conditions` |  `list (object)` Conditions represent the latest available observation of the resource's current state.  
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
    
    # This resource will enable the project this namespace is bound to as a Shared
    # VPC host. You should only create one of these resources per project. If you
    # have multiple namespaces mapping to the same project, ensure that only one
    # ComputeSharedVPCHostProject resource exists across these namespaces.
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSharedVPCHostProject
    metadata:
      annotations:
        # Replace ${HOST_PROJECT_ID?} with the ID of the project that you want to enable as a Shared VPC host.
        cnrm.cloud.google.com/project-id: "${HOST_PROJECT_ID?}"
      name: computesharedvpchostproject-sample
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
