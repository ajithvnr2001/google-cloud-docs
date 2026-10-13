---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.3.0/dbinstance/
title: DBInstance v1.3.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:35.740187+00:00
---

# DBInstance v1.3.0 custom resource definition  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.3.0/dbinstance/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  DBInstance v1.3.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/kubernetes-crds-1.3.0/dbinstance)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/kubernetes-crds-1.3.0/dbinstance)



## Spec schema

DBInstanceSpec defines the desired state of DBInstance.
    
    
    conditions:
    - lastTransactionTime: string
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
    lastBackupTime: string
    nextBackupTime: string
    observedGeneration: integer
    dbcParent:
      name: string
    instanceType: string
    isStopped: boolean
    nodeCount: integer
    progressTimeout: string
    resources:
      cpu:
      - disks:
        accessModes: string
        annotations: object
        name: string
        selector:
          matchExpressions:
          - key: string
            operator: string
            values: string
            matchLabels: object
        size: string
        storageClass: string
        volumeName: string
      memory: integer or string
    schedulingconfig:
      nodeaffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
          preference:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchFields:
            - key: string
              operator: string
              values: string
          weight: integer
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchFields:
            - key: string
              operator: string
              values: string
      podAffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
          podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels:
            namespaceSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels: object
            namespaces: string
            topologyKey: string
          weight: integer
        requiredDuringSchedulingIgnoredDuringExecution:
          labelSelector:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchLabels: object
          namespaceSelector:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchLabels: object
          namespaces: string
          topologyKey: string
      podAntiAffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
          podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels:
            namespaceSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels: object
            namespaces: string
            topologyKey: string
          weight: integer
        requiredDuringSchedulingIgnoredDuringExecution:
          labelSelector:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchLabels: object
          namespaceSelector:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchLabels: object
          namespaces: string
          topologyKey: string
      tolerations:
      - effect: string
        key: string
        operator: string
        tolerationSeconds: integer
        value: string
    

FieldType  
Required or optional |  Description  
---|---  
`dbcParent`  
`object`  
 _Optional_ |  DBClusterParent is the DBCluster that this DBInstance replicates from.   
`dbcParent.name`  
`string`  
 _Optional_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`instanceType`  
`string`  
 _Optional_ |  InstanceType indicates the type of the DBInstance. Currently only supports "ReadPool" type.   
`isStopped`  
`boolean`  
 _Optional_ |  IsStopped stops the DBNodes in this DBInstance when true. This field defaults to false. Stopping the DBCluster's Primary DBNode does not automatically stop the DBNodes of ReadPool DBInstances. When stopped, the compute resources (CPU, memory) of the instance are released. However, the DBNode still keeps the storage resource.   
`nodeCount`  
`integer`  
 _Required_ |  NodeCount determines the number of DBNodes that must be created for this DBInstance.   
`progressTimeout`  
`string`  
 _Optional_ |  ProgressTimeout determines the number of seconds the controller attempts to provision a DBNode, or which a DBNode could be not-ready for, before it considers the DBNode to have failed. A value of 0 means that no timeout is used.   
`resources`  
`object`  
 _Optional_ |  Resource specifices the resources used for the Instances -in other words, DBNodes- belonging to this DBInstance. If omitted, the instance uses the same resources as the DBCluster's Primary Instance.   
`resources.cpu`  
`integer or string`  
 _Required_ |  The amount of CPU allocated to the database container.   
`resources.disks`  
`object`  
 _Required_ |  The specifications of the disks allocated to the database container.   
`resources.disks.accessModes`  
`string`  
 _Optional_ |  AccessModes contains the desired access modes for the volume. For more information, see [Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).   
`resources.disks.annotations`  
`object`  
 _Optional_ |  Additional annotations added to the Persistent Volume Claim. This allows integration with other tools.   
`resources.disks.name`  
`string`  
 _Required_ |  Name of the disk.The allowed values are: "DataDisk", "LogDisk" , "BackupDisk", and "ObsDisk".   
`resources.disks.selector`  
`object`  
 _Optional_ |  A label query over volumes to consider for binding. This field is optional. If this field is set, then the volume with matching labels is used as the backing volume for the disk. For more information, see [PersistentVolumeClaimSpec](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#PersistentVolumeClaimSpec).   
`resources.disks.selector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`resources.disks.selector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`resources.disks.selector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`resources.disks.selector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`resources.disks.selector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`resources.disks.size`  
`string`  
 _Required_ |  Disk size in bytes for example, "10Gi" for 10 Gibibytes. The allowed size unit prefixes are: "Ki", "Mi", "Gi", "Ti, "Pi" and "Ei" for 2-base. Also "K", "M", "G", "T, "P" and "E" for 10-base. For more information, see [Unit prefix](https://en.wikipedia.org/wiki/Unit_prefix).   
`resources.disks.storageClass`  
`string`  
 _Optional_ |  StorageClass points to a particular CSI storage class. This field is optional. If the field is not set, then the default CSI storage class for the Kubernetes cluster is used. If there is no default for the Kubernetes cluster, then the Persistence Volume Claim will fail and the database cluster will fail to provision. For more information, see [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/).   
`resources.disks.volumeName`  
`string`  
 _Optional_ |  VolumeName is the binding reference to the Persistent Volume tied to this disk. This field is optional. This allows to reuse an existing volume. Note that if this field is specified, the value "storageClass" will not take effect. For more information, see [Binding](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding).   
`resources.memory`  
`integer or string`  
 _Required_ |  The amount of memory allocated to the database container.   
`schedulingConfig`  
`object`  
 _Optional_ |  SchedulingConfig specifies how the instance should be scheduled on Kubernetes nodes. If omitted, the instance will use the same scheduling config as the DBCluster's Primary Instance. When any field inside the scheduling config changes, it can lead to rescheduling of the Kubernetes pod onto a different node based on the config.   
`schedulingConfig.nodeAffinity`  
`object`  
 _Optional_ |  NodeAffinity describes node affinity scheduling rules for the instance.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prefers to schedule pods to nodes that satisfy the affinity expressions specified by this field. The scheduler might choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, in other words, for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum, if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference`  
`object`  
 _Required_ |  A node selector term, associated with the corresponding weight.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's labels.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist, Gt, and Lt.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's fields.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist, Gt, and Lt.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the affinity requirements specified by this field isn't met at scheduling time, the pod is not scheduled onto the node. If the affinity requirements specified by this field aren't met at some point during pod execution, for example, due to an update, the system might or might not try to eventually evict the pod from its node.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms`  
`object`  
 _Required_ |  A list of node selector terms. The terms are ORed.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's labels.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist, Gt, and Lt.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's fields.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist, Gt, and Lt.   
`schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAffinity`  
`object`  
 _Optional_ |  PodAffinity describes pod affinity scheduling rules for the instance.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prefers to schedule pods to nodes that satisfy the affinity expressions specified by this field. The scheduler might choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights. For each node that meets all of the scheduling requirements -for example, resource request, and requiredDuringScheduling affinity expressions- you compute a sum by iterating through the elements of this field and adding "weight" to the sum, if the node has pods that match the corresponding podAffinityTerm. The nodes with the highest sum are the most preferred.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm`  
`object`  
 _Required_ |  A pod affinity term, associated with the corresponding weight.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the affinity requirements specified by this field isn't met at scheduling time, the pod is not scheduled onto the node. If the affinity requirements specified by this field aren't met at some point during pod execution -for example, due to a pod label update- the system might or might not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected; in other words, all terms must be satisfied.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`schedulingConfig.podAntiAffinity`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`schedulingConfig.podAntiAffinity`  
`object`  
 _Optional_ |  PodAntiAffinity describes pod anti-affinity scheduling rules for the instance.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prefers to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but the scheduler might choose a node that violates one or more of the expressions The node that is most preferred is the one with the greatest sum of weights, in other words, for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum, if the node has pods that match the corresponding podAffinityTerm. The nodes with the highest sum are the most preferred.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm`  
`object`  
 _Required_ |  A pod affinity term, associated with the corresponding weight.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels`  
`string`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods. matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the anti-affinity requirements specified by this field isn't met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field aren't met at some point during pod execution - for example, due to a pod label update - the system might or might not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, which means that all terms must be satisfied.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`schedulingConfig.tolerations`  
`object`  
 _Optional_ |  Tolerations to enable the management of whether to allow or disallow scheduling an instance on a Kubernetes node that has a specific taint applied.   
`schedulingConfig.tolerations.effect`  
`string`  
 _Optional_ |  Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.   
`schedulingConfig.tolerations.key`  
`string`  
 _Optional_ |  Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists. This combination means to match all values and all keys.   
`schedulingConfig.tolerations.operator`  
`string`  
 _Optional_ |  Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.   
`schedulingConfig.tolerations.tolerationSeconds`  
`integer`  
 _Optional_ |  TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values are treated as 0 (evict immediately) by the system.   
`schedulingConfig.tolerations.value`  
`string`  
 _Optional_ |  Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise it's just a regular string.   
  
## Status schema

DBInstanceStatus defines the observed state of DBInstance.
    
    
    conditions:
    - lastTransitionTime:
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
`object`  
 _Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`conditions.lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another, which occurs when the underlying condition changed. If the time when the underlying condition changed is unknown, use the time when the API field changed.   
`conditions.message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This can be an empty string.   
`conditions.observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions.reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types can define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value must be a CamelCase string. This field might not be empty.   
`conditions.status`  
`string`  
 _Required_ |  The status of the condition, one of True, False, Unknown.   
`conditions.type`  
`string`  
 _Required_ |  type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`criticalIncidents`  
`object`  
 _Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents.code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents.createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`criticalIncidents.message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`criticalIncidents.messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents.resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident, as well as information about the Kubernetes resource.   
`criticalIncidents.resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents.resource.location`  
`object`  
 _Optional_ |  Location   
`criticalIncidents.resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`criticalIncidents.resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`criticalIncidents.resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind of the Kubernetes resource.   
`criticalIncidents.resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`criticalIncidents.resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`criticalIncidents.resource.location.version`  
`string`  
 _Optional_ |  Group is the Version of the Kubernetes resource.   
`criticalIncidents.stackTrace`  
`object`  
 _Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`criticalIncidents.stackTrace.component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`criticalIncidents.stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents.transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`endpoints`  
`object`  
 _Optional_ |  Endpoints are the endpoints from which the DBNodes in the DBInstance can be accessed.   
`endpoints.name`  
`string`  
 _Required_ |  Name contains the name of the endpoint.   
`endpoints.value`  
`string`  
 _Optional_ |  Value contains the endpoint information.   
`observedGeneration`  
`integer`  
 _Optional_ |  The generation observed by the controller.   
`reconciled`  
`boolean`  
 _Optional_ |  Indicates whether the resource is reconciled by the controller.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
