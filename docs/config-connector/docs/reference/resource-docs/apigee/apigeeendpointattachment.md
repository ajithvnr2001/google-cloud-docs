---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/apigee/apigeeendpointattachment/
title: ApigeeEndpointAttachment \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:05.875242+00:00
---

# ApigeeEndpointAttachment  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/apigee/apigeeendpointattachment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ApigeeEndpointAttachment

**Property** | **Value**  
---|---  
Google Cloud Service Name | Apigee  
Google Cloud Service Documentation | [/apigee/docs/](https://docs.cloud.google.com/apigee/docs)  
Google Cloud REST Resource Name |  organizations.endpointAttachments   
Google Cloud REST Resource Documentation |  [/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments)  
Config Connector Resource Short Names | apigeeendpointattachment  
gcpapigeeendpointattachment  
gcpapigeeendpointattachments  
Config Connector Service Name | apigee.googleapis.com  
Config Connector Resource Fully Qualified Name | apigeeendpointattachments.apigee.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    location: string
    organizationRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    serviceAttachmentRef:
      external: string
      name: string
      namespace: string
    

Fields  
---  
`location` _Optional_ |  `string` Required. Location of the endpoint attachment.  
`organizationRef` _Required_ |  `object` Reference to parent Apigee Organization.  
`organizationRef.external` _Optional_ |  `string` A reference to an externally managed ApigeeOrganization resource. Should be in the format "organizations/{{organizationID}}".  
`organizationRef.name` _Optional_ |  `string` The name of an ApigeeOrganization resource.  
`organizationRef.namespace` _Optional_ |  `string` The namespace of an ApigeeOrganization resource.  
`resourceID` _Optional_ |  `string` The ApigeeEndpointAttachment name. If not given, the metadata.name will be used.  
`serviceAttachmentRef` _Optional_ |  `object` Reference to the ServiceAttachment for the EndpointAttachment.  
`serviceAttachmentRef.external` _Optional_ |  `string` The ComputeServiceAttachment selflink in the form "projects/{{project}}/regions/{{region}}/serviceAttachments/{{name}}" when not managed by Config Connector.  
`serviceAttachmentRef.name` _Optional_ |  `string` The `name` field of a `ComputeServiceAttachment` resource.  
`serviceAttachmentRef.namespace` _Optional_ |  `string` The `namespace` field of a `ComputeServiceAttachment` resource.  
  
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
      connectionState: string
      host: string
      state: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`externalRef` |  `string` A unique specifier for the ApigeeEndpointAttachment resource in Google Cloud.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
`observedState.connectionState` |  `string` Output only. State of the endpoint attachment connection to the service attachment.  
`observedState.host` |  `string` Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server.  
`observedState.state` |  `string` Output only. State of the endpoint attachment. Values other than `ACTIVE` mean the resource is not ready to use.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2025 Google LLC
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
    
    apiVersion: apigee.cnrm.cloud.google.com/v1beta1
    kind: ApigeeEndpointAttachment
    metadata:
      name: apgepa-sample
    spec:
      organizationRef:
        external: organizations/${PROJECT_ID?}
      location: us-west3
      serviceAttachmentRef:
        name: computeserviceattachment-dep
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
      name: computebackendservice-dep
    spec:
      location: us-west3
      networkRef:
        name: computenetwork-dep
      loadBalancingScheme: INTERNAL
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeForwardingRule
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
      name: computeforwardingrule-dep
    spec:
      location: us-west3
      networkRef:
        name: computenetwork-dep
      subnetworkRef:
        name: computesubnetwork-dep1
      loadBalancingScheme: INTERNAL
      backendServiceRef:
        name: computebackendservice-dep
      networkTier: PREMIUM
      allPorts: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: computenetwork-dep
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeServiceAttachment
    metadata:
      name: computeserviceattachment-dep
    spec:
      projectRef:
        external: projects/${PROJECT_ID?}
      location: us-west3
      description: A sample service attachment
      targetServiceRef:
        name: computeforwardingrule-dep
      connectionPreference: ACCEPT_AUTOMATIC
      natSubnets:
        - name: computesubnetwork-dep2
      enableProxyProtocol: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: computesubnetwork-dep1
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
    spec:
      ipCidrRange: 10.180.0.0/20
      region: us-west3
      networkRef:
        name: computenetwork-dep
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: ${PROJECT_ID?}
      name: computesubnetwork-dep2
    spec:
      region: us-west3
      ipCidrRange: 10.0.0.0/24
      networkRef:
        name: computenetwork-dep
      purpose: PRIVATE_SERVICE_CONNECT
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
