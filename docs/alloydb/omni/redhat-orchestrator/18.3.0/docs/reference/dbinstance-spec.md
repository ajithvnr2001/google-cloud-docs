---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/dbinstance-spec/
title: DBInstance Custom Resource Definition \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:52.938581+00:00
---

# DBInstance Custom Resource Definition  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/dbinstance-spec/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/database-flags)



Send feedback 

#  DBInstance Custom Resource Definition Stay organized with collections  Save and categorize content based on your preferences. 

## Spec schema

DBInstanceSpec defines the selected state of DBInstance.
    
    
    DBInstance:
      metadata:
        name: string
      spec:
        dbcParent:
          name: string
        instanceType: string
        nodeCount: integer
        readPoolPort: integer
        resources:
          cpu: integer or string
          memory: string or integer
          disks:
          - name: string
            path: string
            size: string
    

FieldType  
Required or optional |  Description  
---|---  
`name`  
`string`  
 _Required_ |  Name of the `DBInstance` resource.   
`dbcParent`  
`object`  
 _Required_ |  The parent `DBCluster` that this `DBInstance` replicates from.   
`dbcParent.name`  
`string`  
 _Required_ |  Name of the referent `DBCluster`.   
`instanceType`  
`string`  
 _Optional_ |  Indicates the type of the `DBInstance`. Supports `ReadPool` type. The default value is `ReadPool`.   
`nodeCount`  
`integer`  
 _Optional_ |  Determines the number of DBNodes to create for this `DBInstance`. Supported values are between 0 and 20. The default value is `1`.   
`readPoolPort`  
`integer`  
 _Optional_ |  Dedicated HAProxy frontend port for a ReadPool `DBInstance`.   
`resources`  
`object`  
 _Optional_ |  Specifies the compute and storage resources used for the instances (DBNodes) belonging to this `DBInstance`. If omitted, the instance uses the same resources as the `DBCluster`'s Primary Instance.   
`resources.cpu`  
`integer or string`  
 _Required_ |  The amount of CPU allocated to the database process (for example, `2` or `"2"`).   
`resources.memory`  
`string or integer`  
 _Required_ |  The amount of memory allocated to the database process (for example, `"6Gi"`).   
`resources.disks`  
`list (object)`  
_Required_ |  The specifications of the disks allocated to the database process.   
`resources.disks[].name`  
`string`  
 _Required_ |  Name of the disk. The allowed values are: `DataDisk` and `ObsDisk`.   
`resources.disks[].path`  
`string`  
 _Optional_ |  Path where the disk is mounted on the host file system.   
`resources.disks[].size`  
`string`  
 _Optional_ |  Disk size in bytes (for example, `"15Gi"`).   
  
## Status schema

DBInstanceStatus defines the observed state of DBInstance.
    
    
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
    endpoints:
    - name: string
      value: string
    observedGeneration: integer
    reconciled: boolean
    

FieldType  
Required or optional |  Description  
---|---  
`conditions`  
`list (object)`  
_Optional_ |  Represents the latest available observations of the `DBInstance`'s current state.   
`conditions[]`  
`object`  
 _Optional_ |  Condition describes one aspect of the current state of this API resource.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  Indicates when the condition transitioned from one status to another. If this time is unknown, use the time the API field changed.   
`conditions[].message`  
`string`  
 _Required_ |  A human-readable string that describes details about the transition. This string can be empty.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  Represents the `.metadata.generation` that the condition was set based upon.   
`conditions[].reason`  
`string`  
 _Required_ |  Contains a programmatic identifier indicating the reason for the condition's last transition. The value is a CamelCase string. Expected values for `DBInstance` include: 

  * `AllDBNodesReady`: The DBInstance has the required number of ready DBNodes.
  * `MinDBNodesReady`: At least the minimum number of DBNodes specified in the spec are ready.
  * `DBNodesNotReady`: The minimum number of DBNodes are not ready.
  * `AllDBNodesStreaming`: The DBInstance has the required number of DBNodes actively replicating from the primary.
  * `MinDBNodesStreaming`: At least the minimum number of DBNodes are replicating from the primary.
  * `DBNodesNotStreaming`: The minimum number of DBNodes are not replicating.
  * `NetworkReady`: The LoadBalancer has been created and is ready to serve the DBNodes.
  * `NetworkNotReady`: The LoadBalancer is not ready to serve the DBNodes.
  * `DBNodesAvailable`: The required number of DBNodes are successfully provisioned and accessible using the LoadBalancer.
  * `InvalidSpec`: Indicates that something in the Spec is invalid.

  
`conditions[].status`  
`string`  
 _Required_ |  Status of the condition. The valid values are `True`, `False`, and `Unknown`.   
`conditions[].type`  
`string`  
 _Required_ |  The type of condition in CamelCase. Expected types include: 

  * `DBNodesReady`: Indicates whether all DBNodes required for this DBInstance have been provisioned and are ready.
  * `Streaming`: Indicates whether the DBNodes are actively replicating from the primary.
  * `NetworkReady`: Shows whether a LoadBalancer has been created and is ready to serve the DBNodes.
  * `Available`: Indicates whether the required number of DBNodes are provisioned and accessible using the LoadBalancer.

  
`criticalIncidents`  
`list (object)`  
_Optional_ |  List of all active critical incidents.   
`criticalIncidents[]`  
`object`  
 _Optional_ |  Describes an ongoing critical incident.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  Error code of the error. Error codes are DBSE+numeric strings; for example, `DBSE1012`.   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  Timestamp when the incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Describes the incident or error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  Includes key-value pairs to generate a user-friendly, data-driven message in the UI.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Contains information about the Database Service component that reported the incident.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  Internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  The location of the originating resource.   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  Name of the cluster of the affected resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  Group name of the resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  Kind of the resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  Name of the affected resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  Namespace of the affected resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  Version of the resource.   
`criticalIncidents[].stackTrace`  
`list (object)`  
_Optional_ |  Unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace[].component`  
`string`  
 _Optional_ |  Name of the Database Service component that logged the message.   
`criticalIncidents[].stackTrace[].message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  Indicates that the issue should be considered transient until the specified time.   
`endpoints`  
`list (object)`  
_Optional_ |  Endpoints contains all the endpoints through which you can access this instance.   
`endpoints[].name`  
`string`  
 _Required_ |  Name is the name of the endpoint—for example, `Read-Only`.   
`endpoints[].value`  
`string`  
 _Required_ |  Value contains the endpoint information to connect to and access the instance.   
`observedGeneration`  
`integer`  
 _Optional_ |  The generation observed by the controller.   
`reconciled`  
`boolean`  
 _Optional_ |  Whether the resource was reconciled by the controller.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
