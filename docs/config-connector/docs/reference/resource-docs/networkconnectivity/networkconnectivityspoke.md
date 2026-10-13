---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/networkconnectivity/networkconnectivityspoke/
title: NetworkConnectivitySpoke \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:25.371778+00:00
---

# NetworkConnectivitySpoke  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/networkconnectivity/networkconnectivityspoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# NetworkConnectivitySpoke

**Property** | **Value**  
---|---  
Google Cloud Service Name | Network Connectivity  
Google Cloud Service Documentation | [/network-connectivity/docs/](https://docs.cloud.google.com/network-connectivity/docs)  
Google Cloud REST Resource Name | v1.projects.locations.spokes  
Google Cloud REST Resource Documentation | [/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/a>](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes)  
Config Connector Resource Short Names | gcpnetworkconnectivityspoke  
gcpnetworkconnectivityspokes  
networkconnectivityspoke  
Config Connector Service Name | networkconnectivity.googleapis.com  
Config Connector Resource Fully Qualified Name | networkconnectivityspokes.networkconnectivity.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    description: string
    hubRef:
      external: string
      name: string
      namespace: string
    linkedInterconnectAttachments:
      siteToSiteDataTransfer: boolean
      uris:
      - external: string
        name: string
        namespace: string
    linkedRouterApplianceInstances:
      instances:
      - ipAddress: string
        virtualMachineRef:
          external: string
          name: string
          namespace: string
      siteToSiteDataTransfer: boolean
    linkedVPCNetwork:
      excludeExportRanges:
      - string
      uriRef:
        external: string
        name: string
        namespace: string
    linkedVpnTunnels:
      siteToSiteDataTransfer: boolean
      uris:
      - external: string
        name: string
        namespace: string
    location: string
    projectRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    

Fields  
---  
`description` _Optional_ |  `string` An optional description of the spoke.  
`hubRef` _Required_ |  `object` Immutable.  
`hubRef.external` _Optional_ |  `string` Immutable. The URI of the hub that this spoke is attached to. Allowed value: The Google Cloud resource name of a `NetworkConnectivityHub` resource (format: `projects/{{project}}/locations/global/hubs/{{name}}`).  
`hubRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`hubRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`linkedInterconnectAttachments` _Optional_ |  `object` Immutable. A collection of VLAN attachment resources. These resources should be redundant attachments that all advertise the same prefixes to Google Cloud. Alternatively, in active/passive configurations, all attachments should be capable of advertising the same prefixes.  
`linkedInterconnectAttachments.siteToSiteDataTransfer` _Required*_ |  `boolean` Immutable. A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.  
`linkedInterconnectAttachments.uris` _Required*_ |  `list (object)` Immutable.  
`linkedInterconnectAttachments.uris[]` _Required*_ |  `object`  
`linkedInterconnectAttachments.uris[].external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeInterconnectAttachment` resource.  
`linkedInterconnectAttachments.uris[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`linkedInterconnectAttachments.uris[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`linkedRouterApplianceInstances` _Optional_ |  `object` Immutable. The URIs of linked Router appliance resources  
`linkedRouterApplianceInstances.instances` _Required*_ |  `list (object)` Immutable. The list of router appliance instances  
`linkedRouterApplianceInstances.instances[]` _Required*_ |  `object`  
`linkedRouterApplianceInstances.instances[].ipAddress` _Optional_ |  `string` Immutable. The IP address on the VM to use for peering.  
`linkedRouterApplianceInstances.instances[].virtualMachineRef` _Optional_ |  `object` Immutable.  
`linkedRouterApplianceInstances.instances[].virtualMachineRef.external` _Optional_ |  `string` The URI of the virtual machine resource Allowed value: The `selfLink` field of a `ComputeInstance` resource.  
`linkedRouterApplianceInstances.instances[].virtualMachineRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`linkedRouterApplianceInstances.instances[].virtualMachineRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`linkedRouterApplianceInstances.siteToSiteDataTransfer` _Required*_ |  `boolean` Immutable. A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.  
`linkedVPCNetwork` _Optional_ |  `object` Immutable. VPC network that is associated with the spoke.  
`linkedVPCNetwork.excludeExportRanges` _Optional_ |  `list (string)` Immutable. IP ranges encompassing the subnets to be excluded from peering.  
`linkedVPCNetwork.excludeExportRanges[]` _Optional_ |  `string`  
`linkedVPCNetwork.uriRef` _Required*_ |  `object` Immutable.  
`linkedVPCNetwork.uriRef.external` _Optional_ |  `string` The URI of the VPC network resource. Allowed value: The `selfLink` field of a `ComputeNetwork` resource.  
`linkedVPCNetwork.uriRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`linkedVPCNetwork.uriRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`linkedVpnTunnels` _Optional_ |  `object` Immutable. The URIs of linked VPN tunnel resources  
`linkedVpnTunnels.siteToSiteDataTransfer` _Required*_ |  `boolean` Immutable. A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations.  
`linkedVpnTunnels.uris` _Required*_ |  `list (object)` Immutable.  
`linkedVpnTunnels.uris[]` _Required*_ |  `object`  
`linkedVpnTunnels.uris[].external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `ComputeVPNTunnel` resource.  
`linkedVpnTunnels.uris[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`linkedVpnTunnels.uris[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`location` _Required_ |  `string` Immutable. The location for the resource  
`projectRef` _Required_ |  `object` Immutable. The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The project for the resource Allowed value: The Google Cloud resource name of a `Project` resource (format: `projects/{{name}}`).  
`projectRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`projectRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    createTime: string
    observedGeneration: integer
    state: string
    uniqueId: string
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
`createTime` |  `string` Output only. The time the spoke was created.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`state` |  `string` Output only. The current lifecycle state of this spoke. Possible values: STATE_UNSPECIFIED, CREATING, ACTIVE, DELETING  
`uniqueId` |  `string` Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different unique_id.  
`updateTime` |  `string` Output only. The time the spoke was last updated.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2021 Google LLC
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
    
    apiVersion: networkconnectivity.cnrm.cloud.google.com/v1beta1
    kind: NetworkConnectivitySpoke
    metadata:
      name: networkconnectivityspoke-sample
      labels:
        label-one: "value-one"
    spec:
      location: us-central1
      description: "A sample spoke with a linked router appliance instance"
      hubRef:
        name: networkconnectivityspoke-dep
      linkedRouterApplianceInstances:
        instances:
          - virtualMachineRef:
              name: networkconnectivityspoke-dep
            ipAddress: "10.0.0.2"
        siteToSiteDataTransfer: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeInstance
    metadata:
      annotations:
        cnrm.cloud.google.com/allow-stopping-for-update: "true"
      name: networkconnectivityspoke-dep
      labels:
        created-from: "image"
        network-type: "subnetwork"
    spec:
      machineType: n1-standard-1
      zone: us-central1-a
      bootDisk:
        initializeParams:
          sourceImageRef:
            external: debian-cloud/debian-11
      networkInterface:
        - subnetworkRef:
            name: networkconnectivityspoke-dep
          networkIp: "10.0.0.2"
          accessConfig:
            - networkTier: "PREMIUM"
      canIpForward: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      labels:
        label-one: "value-one"
      name: networkconnectivityspoke-dep
    spec:
      autoCreateSubnetworks: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      labels:
        label-one: "value-one"
      name: networkconnectivityspoke-dep
    spec:
      ipCidrRange: 10.0.0.0/28
      region: us-central1
      networkRef:
        name: networkconnectivityspoke-dep
    ---
    apiVersion: networkconnectivity.cnrm.cloud.google.com/v1beta1
    kind: NetworkConnectivityHub
    metadata:
      name: networkconnectivityspoke-dep
      labels:
        label-one: "value-one"
    spec:
      description: "A sample hub"
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
