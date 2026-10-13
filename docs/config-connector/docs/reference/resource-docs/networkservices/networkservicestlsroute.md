---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/networkservices/networkservicestlsroute/
title: NetworkServicesTLSRoute \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:31.950684+00:00
---

# NetworkServicesTLSRoute  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/networkservices/networkservicestlsroute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# NetworkServicesTLSRoute

**Property** | **Value**  
---|---  
Google Cloud Service Name | Network Services  
Google Cloud Service Documentation | [/traffic-director/docs/](https://docs.cloud.google.com/traffic-director/docs)  
Google Cloud REST Resource Name | v1.projects.locations.tlsRoutes  
Google Cloud REST Resource Documentation | [/traffic-director/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes](https://docs.cloud.google.com/traffic-director/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes)  
Config Connector Resource Short Names | gcpnetworkservicestlsroute  
gcpnetworkservicestlsroutes  
networkservicestlsroute  
Config Connector Service Name | networkservices.googleapis.com  
Config Connector Resource Fully Qualified Name | networkservicestlsroutes.networkservices.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    description: string
    gateways:
    - external: string
      name: string
      namespace: string
    location: string
    meshes:
    - external: string
      name: string
      namespace: string
    projectRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    rules:
    - action:
        destinations:
        - serviceRef:
            external: string
            name: string
            namespace: string
          weight: integer
      matches:
      - alpn:
        - string
        sniHost:
        - string
    

Fields  
---  
`description` _Optional_ |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`gateways` _Optional_ |  `list (object)`  
`gateways[]` _Optional_ |  `object`  
`gateways[].external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `NetworkServicesGateway` resource.  
`gateways[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`gateways[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`location` _Required_ |  `string` Immutable. The location for the resource  
`meshes` _Optional_ |  `list (object)`  
`meshes[]` _Optional_ |  `object`  
`meshes[].external` _Optional_ |  `string` Allowed value: The `selfLink` field of a `NetworkServicesMesh` resource.  
`meshes[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`meshes[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`projectRef` _Required_ |  `object` Immutable. The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The project for the resource Allowed value: The Google Cloud resource name of a `Project` resource (format: `projects/{{name}}`).  
`projectRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`projectRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`rules` _Required_ |  `list (object)` Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.  
`rules[]` _Required_ |  `object`  
`rules[].action` _Required_ |  `object` Required. The detailed rule defining how to route matched traffic.  
`rules[].action.destinations` _Required_ |  `list (object)` Required. The destination services to which traffic should be forwarded. At least one destination service is required.  
`rules[].action.destinations[]` _Required_ |  `object`  
`rules[].action.destinations[].serviceRef` _Required_ |  `object`  
`rules[].action.destinations[].serviceRef.external` _Optional_ |  `string` Required. The URL of a BackendService to route traffic to. Allowed value: The Google Cloud resource name of a `ComputeBackendService` resource (format: `projects/{{project}}/global/backendServices/{{name}}`).  
`rules[].action.destinations[].serviceRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`rules[].action.destinations[].serviceRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`rules[].action.destinations[].weight` _Optional_ |  `integer` Optional. Specifies the proportion of requests forwareded to the backend referenced by the service_name field. This is computed as: weight/Sum(weights in destinations) Weights in all destinations does not need to sum up to 100.  
`rules[].matches` _Required_ |  `list (object)` Required. RouteMatch defines the predicate used to match requests to a given action. Multiple match types are "OR"ed for evaluation.  
`rules[].matches[]` _Required_ |  `object`  
`rules[].matches[].alpn` _Optional_ |  `list (string)` Optional. ALPN (Application-Layer Protocol Negotiation) to match against. Examples: "http/1.1", "h2". At least one of sni_host and alpn is required. Up to 5 alpns across all matches can be set.  
`rules[].matches[].alpn[]` _Optional_ |  `string`  
`rules[].matches[].sniHost` _Optional_ |  `list (string)` Optional. SNI (server name indicator) to match against. SNI will be matched against all wildcard domains, i.e. www.example.com will be first matched against www.example.com, then *.example.com, then *.com. Partial wildcards are not supported, and values like *w.example.com are invalid. At least one of sni_host and alpn is required. Up to 5 sni hosts across all matches can be set.  
`rules[].matches[].sniHost[]` _Optional_ |  `string`  
  
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
    selfLink: string
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
`createTime` |  `string` Output only. The timestamp when the resource was created.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`selfLink` |  `string` Output only. Server-defined URL of this resource  
`updateTime` |  `string` Output only. The timestamp when the resource was updated.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2022 Google LLC
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
    
    apiVersion: networkservices.cnrm.cloud.google.com/v1beta1
    kind: NetworkServicesTLSRoute
    metadata:
      name: networkservicestlsroute-sample
    spec:
      meshes:
      - name: "networkservicestlsroute-dep"
      gateways:
      - name: "networkservicestlsroute-dep"
      description: "A test TcpRoute"
      location: "global"
      rules:
      - matches:
        - sniHost:
          - "*.foo.example.com"
          - "foo.example.com"
          alpn:
          - "h2"
          - "http/1.1"
        action:
          destinations:
          - serviceRef:
              name: "networkservicestlsroute-dep"
            weight: 1
      projectRef:
        # Replace "${PROJECT_ID?}" with your project ID
        external: "projects/${PROJECT_ID?}"
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      name: networkservicestlsroute-dep
    spec:
      loadBalancingScheme: "INTERNAL_SELF_MANAGED"
      location: "global"
    ---
    apiVersion: networkservices.cnrm.cloud.google.com/v1beta1
    kind: NetworkServicesGateway
    metadata:
      name: networkservicestlsroute-dep
    spec:
      location: "global"
      type: "OPEN_MESH"
      scope: "networkservicestlsroute-sample-scope"
      ports:
      - 80
      - 443
      projectRef:
        # Replace "${PROJECT_ID?}" with your project ID
        external: "projects/${PROJECT_ID?}"
    ---
    apiVersion: networkservices.cnrm.cloud.google.com/v1beta1
    kind: NetworkServicesMesh
    metadata:
      name: networkservicestlsroute-dep
    spec:
      location: "global"
      projectRef:
        # Replace "${PROJECT_ID?}" with your project ID
        external: "projects/${PROJECT_ID?}"
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
