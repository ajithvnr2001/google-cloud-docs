---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/servicedirectory/servicedirectoryendpoint/
title: ServiceDirectoryEndpoint \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:28.398299+00:00
---

# ServiceDirectoryEndpoint  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/servicedirectory/servicedirectoryendpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ServiceDirectoryEndpoint

**Property** | **Value**  
---|---  
Google Cloud Service Name | Service Directory  
Google Cloud Service Documentation | [/service-directory/docs/](https://docs.cloud.google.com/service-directory/docs)  
Google Cloud REST Resource Name | v1beta1.projects.locations.namespaces.services.endpoints  
Google Cloud REST Resource Documentation | [/service-directory/docs/reference/rest/v1beta1/projects.locations.namespaces.services.endpoints](https://docs.cloud.google.com/service-directory/docs/reference/rest/v1beta1/projects.locations.namespaces.services.endpoints)  
Config Connector Resource Short Names | gcpservicedirectoryendpoint  
gcpservicedirectoryendpoints  
servicedirectoryendpoint  
Config Connector Service Name | servicedirectory.googleapis.com  
Config Connector Resource Fully Qualified Name | servicedirectoryendpoints.servicedirectory.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    addressRef:
      external: string
      name: string
      namespace: string
    networkRef:
      external: string
      name: string
      namespace: string
    port: integer
    resourceID: string
    serviceRef:
      external: string
      name: string
      namespace: string
    

Fields  
---  
`addressRef` _Optional_ |  `object` Optional. The ComputeAddress resource whose IP address this endpoint uses.  
`addressRef.external` _Optional_ |  `string` A reference to an externally managed ComputeAddress resource. Should be in the format "projects/{{projectID}}/global/addresses/{{addressID}}" or "projects/{{projectID}}/regions/{{region}}/addresses/{{addressID}}".  
`addressRef.name` _Optional_ |  `string` The name of a ComputeAddress resource.  
`addressRef.namespace` _Optional_ |  `string` The namespace of a ComputeAddress resource.  
`networkRef` _Optional_ |  `object` Optional. The ComputeNetwork resource representing the GCE network of this endpoint.  
`networkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNetwork resource. Should be in the format "projects/{{projectID}}/global/networks/{{networkID}}".  
`networkRef.name` _Optional_ |  `string` The name of a ComputeNetwork resource.  
`networkRef.namespace` _Optional_ |  `string` The namespace of a ComputeNetwork resource.  
`port` _Optional_ |  `integer` Optional. Port that the endpoint is running on, must be in the range of [0, 65535]. If unspecified, the default is 0.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The endpointId of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`serviceRef` _Required_ |  `object` Required. The ServiceDirectoryService that this endpoint belongs to.  
`serviceRef.external` _Optional_ |  `string` A reference to an externally managed ServiceDirectoryService resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/namespaces/{{namespaceID}}/services/{{serviceID}}".  
`serviceRef.name` _Optional_ |  `string` The name of a ServiceDirectoryService resource.  
`serviceRef.namespace` _Optional_ |  `string` The namespace of a ServiceDirectoryService resource.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    name: string
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
`name` |  `string` The resource name for the endpoint in the format 'projects/*/locations/*/namespaces/*/services/*/endpoints/*'.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2022 Google LLC
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
    apiVersion: servicedirectory.cnrm.cloud.google.com/v1beta1
    kind: ServiceDirectoryEndpoint
    metadata:
      name: servicedirectoryendpoint-sample
      labels:
        label-one: value-one
    spec:
      serviceRef:
        name: servicedirectoryendpoint-dep
      addressRef:
        name: servicedirectoryendpoint-dep
      port: 443
      networkRef:
        external: projects/${PROJECT_NUMBER?}/locations/global/networks/servicedirectory-dep
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: servicedirectoryendpoint-dep
      labels:
        label-one: "value-one"
    spec:
      location: us-central1
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      labels:
        label-one: "value-one"
      name: servicedirectoryendpoint-dep
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: servicedirectory.cnrm.cloud.google.com/v1beta1
    kind: ServiceDirectoryNamespace
    metadata:
      name: servicedirectoryendpoint-dep
    spec:
      location: us-central1
      projectRef:
        external: ${PROJECT_ID?}
    ---
    apiVersion: servicedirectory.cnrm.cloud.google.com/v1beta1
    kind: ServiceDirectoryService
    metadata:
      name: servicedirectoryendpoint-dep
    spec:
      namespaceRef:
        name: servicedirectoryendpoint-dep
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
