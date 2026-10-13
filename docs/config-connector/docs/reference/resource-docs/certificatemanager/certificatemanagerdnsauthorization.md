---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagerdnsauthorization/
title: CertificateManagerDNSAuthorization \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:50.711156+00:00
---

# CertificateManagerDNSAuthorization  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagerdnsauthorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CertificateManagerDNSAuthorization

**Property** | **Value**  
---|---  
Google Cloud Service Name | Certificate Manager  
Google Cloud Service Documentation | [/certificate-manager/docs/](https://docs.cloud.google.com/certificate-manager/docs)  
Google Cloud REST Resource Name | v1.projects.locations.dnsAuthorizations  
Google Cloud REST Resource Documentation | [/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.dnsAuthorizations](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.dnsAuthorizations)  
Config Connector Resource Short Names | certificatemanagerdnsauthorization  
gcpcertificatemanagerdnsauthorization  
gcpcertificatemanagerdnsauthorizations  
Config Connector Service Name | certificatemanager.googleapis.com  
Config Connector Resource Fully Qualified Name | certificatemanagerdnsauthorizations.certificatemanager.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    description: string
    domain: string
    location: string
    projectRef:
      external: string
      kind: string
      name: string
      namespace: string
    resourceID: string
    type: string
    

Fields  
---  
`description` _Optional_ |  `string` A human-readable description of the resource.  
`domain` _Required_ |  `string` Immutable. A domain which is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for "example.com" can be used to issue certificates for "example.com" and "*.example.com".  
`location` _Optional_ |  `string` Immutable. Optional. Location represents the geographical location of the DnsAuthorization. If not specified, "global" is used.  
`projectRef` _Required_ |  `object` The project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.kind` _Optional_ |  `string` The kind of the Project resource; optional but must be `Project` if provided.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`resourceID` _Optional_ |  `string` Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`type` _Optional_ |  `string` Immutable. Optional. The type of DNS Authorization. If not specified, "FIXED_RECORD" is used. Possible values: FIXED_RECORD, PER_PROJECT_RECORD.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    dnsResourceRecord:
    - data: string
      name: string
      type: string
    externalRef: string
    observedGeneration: integer
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the CertificateManagerDNSAuthorization's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`dnsResourceRecord` |  `list (object)` The structure describing the DNS Resource Record that needs to be added to DNS configuration for the authorization to be usable by certificate.  
`dnsResourceRecord[]` |  `object`  
`dnsResourceRecord[].data` |  `string` Output only. Data of the DNS Resource Record.  
`dnsResourceRecord[].name` |  `string` Output only. Fully qualified name of the DNS Resource Record. e.g. `_acme-challenge.example.com`  
`dnsResourceRecord[].type` |  `string` Output only. Type of the DNS Resource Record. Currently always set to "CNAME".  
`externalRef` |  `string` A unique specifier for the CertificateManagerDNSAuthorization resource in GCP.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    apiVersion: certificatemanager.cnrm.cloud.google.com/v1beta1
    kind: CertificateManagerDNSAuthorization
    metadata:
      name: certificatemanagerdnsauthorization-sample
    spec:
      location: us-central1
      description: sample dns authorization
      domain: subdomain.hashicorptest.com
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: ${PROJECT_ID?}
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
