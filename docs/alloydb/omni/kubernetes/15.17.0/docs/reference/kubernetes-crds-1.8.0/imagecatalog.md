---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog/
title: ImageCatalog v1.8.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:59.423506+00:00
---

# ImageCatalog v1.8.0 custom resource definition  |  AlloyDB Omni using the container orchestrator: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog/

This page documents AlloyDB Omni version **15.17.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/database-flags)



Send feedback 

#  ImageCatalog v1.8.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.17.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.8.0/imagecatalog)



## Spec schema

ImageCatalogSpec defines the desired state of ImageCatalog.
    
    
    controlPlaneAgents:
    - imageDigests:
        backupinit: string
        dbinit: string
        logrotate: string
        monitoring-agent: string
      version: string
    dataPlane:
    - imageDigests:
        database: string
      osType: string
      version: string
    

FieldType  
Required or optional |  Description  
---|---  
`controlPlaneAgents`  
`list (object)`  
_Required_ |  ControlPlaneAgentsRelease defines the image digests for a particular CPA version.   
`controlPlaneAgents[].imageDigests`  
`object`  
 _Required_ |  ControlPlaneAgentsDigestSet contains the SHA digests for CPA container images.   
`controlPlaneAgents[].imageDigests.backupinit`  
`string`  
 _Optional_ |  SHA-256 image digest for a specific version's backupinit component.   
`controlPlaneAgents[].imageDigests.dbinit`  
`string`  
 _Optional_ |  SHA-256 image digest for a specific version's dbinit component.   
`controlPlaneAgents[].imageDigests.logrotate`  
`string`  
 _Optional_ |  SHA-256 image digest for a specific version's logrotate component.   
`controlPlaneAgents[].imageDigests.monitoring-agent`  
`string`  
 _Optional_ |  SHA-256 image digest for a specific version's monitoring-agent component.   
`controlPlaneAgents[].version`  
`string`  
 _Required_ |  The control plane agents version for the set of image digests. For example, "1.7.0".   
`dataPlane`  
`list (object)`  
_Required_ |  DataPlaneRelease defines the image digests for a particular database version.   
`dataPlane[].imageDigests`  
`object`  
 _Required_ |  DataPlaneDigestSet contains the SHA digests for data plane container images.   
`dataPlane[].imageDigests.database`  
`string`  
 _Optional_ |  SHA-256 image digest for a specific version's database component.   
`dataPlane[].osType`  
`string`  
 _Optional_ |  The base operating system type for the database image. Accepted values are `Debian` and `UBI9`.   
`dataPlane[].version`  
`string`  
 _Required_ |  The database version for the set of image digests. For example, "16.11.0".   
  
## Status schema

ImageCatalogStatus defines the observed state of ImageCatalog.
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
    criticalIncidents:
    - code: string
      createTime: string
      message: string
      messageTemplateParams: object
      resource:
        component: string
        location:
          cluster: string
          group: string
          kind: string
          name: string
          namespace: string
          version: string
      stackTrace:
      - component: string
        message: string
      transientUntil: string
    observedGeneration: integer
    reconciled: boolean
    

FieldType  
Required or optional |  Description  
---|---  
`conditions`  
`list (object)`  
_Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`conditions[].message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This may be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For example, if .metadata.generation is 12 but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  Status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  Type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`criticalIncidents`  
`list (object)`  
_Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  The error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  The timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident/error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  Contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Contains information about the Database Service component that reported the incident as well as about the K8s resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  An internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location.   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  The name of the cluster of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  The Group name of the Kubernetes resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  The Kind of the Kubernetes resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  The name of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  The namespace of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  The Version of the Kubernetes resource.   
`criticalIncidents[].stackTrace`  
`list (object)`  
_Optional_ |  An unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace[].component`  
`string`  
 _Optional_ |  The name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace[].message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  If present indicates that the issue should be considered transient until the specified time.   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
