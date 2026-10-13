---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/edgenetwork/edgenetworksubnet/
title: EdgeNetworkSubnet \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:42.786509+00:00
---

# EdgeNetworkSubnet  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/edgenetwork/edgenetworksubnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# EdgeNetworkSubnet

**Property** | **Value**  
---|---  
Google Cloud Service Name | Edge Network  
Google Cloud Service Documentation | [/distributed-cloud/edge/latest/docs/](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs)  
Google Cloud REST Resource Name | projects.locations.zones.subnets  
Google Cloud REST Resource Documentation | [/distributed-cloud/edge/latest/docs/reference/network/rest/v1/projects.locations.zones.subnets](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/reference/network/rest/v1/projects.locations.zones.subnets)  
Config Connector Resource Short Names | edgenetworksubnet  
gcpedgenetworksubnet  
gcpedgenetworksubnets  
Config Connector Service Name | edgenetwork.googleapis.com  
Config Connector Resource Fully Qualified Name | edgenetworksubnets.edgenetwork.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    description: string
    ipv4Cidr:
    - string
    ipv6Cidr:
    - string
    location: string
    networkRef:
      external: string
      name: string
      namespace: string
    projectRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    vlanId: integer
    zone: string
    

Fields  
---  
`description` _Optional_ |  `string` Immutable. A free-text description of the resource. Max length 1024 characters.  
`ipv4Cidr` _Optional_ |  `list (string)` Immutable. The ranges of ipv4 addresses that are owned by this subnetwork, in CIDR format.  
`ipv4Cidr[]` _Optional_ |  `string`  
`ipv6Cidr` _Optional_ |  `list (string)` Immutable. The ranges of ipv6 addresses that are owned by this subnetwork, in CIDR format.  
`ipv6Cidr[]` _Optional_ |  `string`  
`location` _Required_ |  `string` Immutable. The Google Cloud region to which the target Distributed Cloud Edge zone belongs.  
`networkRef` _Required_ |  `object`  
`networkRef.external` _Optional_ |  `string` Allowed value: The `name` field of an `EdgeNetworkNetwork` resource.  
`networkRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`networkRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`projectRef` _Required_ |  `object` The project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` Allowed value: The `name` field of a `Project` resource.  
`projectRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`projectRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`resourceID` _Optional_ |  `string` Immutable. Optional. The subnetId of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`vlanId` _Optional_ |  `integer` Immutable. VLAN ID for this subnetwork. If not specified, one is assigned automatically.  
`zone` _Required_ |  `string` Immutable. The name of the target Distributed Cloud Edge zone.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    createTime: string
    name: string
    observedGeneration: integer
    state: string
    updateTime: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observation of the resource's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`createTime` |  `string` The time when the subnet was created. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'.  
`name` |  `string` The canonical name of this resource, with format 'projects/{{project}}/locations/{{location}}/zones/{{zone}}/subnets/{{subnet_id}}'.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`state` |  `string` Current stage of the resource to the device by config push.  
`updateTime` |  `string` The time when the subnet was last updated. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2023 Google LLC
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
    
    apiVersion: edgenetwork.cnrm.cloud.google.com/v1beta1
    kind: EdgeNetworkSubnet
    metadata:
      name: edgenetworksubnet-sample
    spec:
      description: "A sample edgenetwork subnet"
      location: us-central1
      # Replace ${ZONE_LOCATION?} with the machine zone location
      zone: ${ZONE_LOCATION}
      networkRef:
        name: edgenetworksubnet-dep
      ipv4Cidr:
        - 1.1.1.1/24
        - 2.2.2.2/32
    ---
    apiVersion: edgenetwork.cnrm.cloud.google.com/v1beta1
    kind: EdgeNetworkNetwork
    metadata:
      name: edgenetworksubnet-dep
    spec:
      description: "A sample edgenetwork network"
      location: us-central1
      # Replace ${ZONE_LOCATION?} with the machine zone location
      zone: ${ZONE_LOCATION}
      mtu: 9000
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
