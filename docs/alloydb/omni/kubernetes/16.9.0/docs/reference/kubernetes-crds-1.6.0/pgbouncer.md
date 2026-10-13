---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer/
title: PgBouncer v1.6.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:29.109102+00:00
---

# PgBouncer v1.6.0 custom resource definition  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  PgBouncer v1.6.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer)



## Spec schema

PgBouncerSpec defines the selected state of PgBouncer.
    
    
    accessMode: string
    allowSuperUserAccess: boolean
    dbclusterRef: string
    parameters: object
    podSpec:
      image: string
      resources:
        cpu: integer or string
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
          - podAffinityTerm:
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
                  type: string
                matchLabels: object
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
                type: string
              matchLabels: object
            namespaces: string
            topologyKey: string
        tolerations:
        - effect: string
          key: string
          operator: string
          tolerationSeconds: integer
          value: string
    replicaCount: integer
    serverTLS:
      certSecret:
        name: string
    serviceOptions:
      annotations: object
      gcp:
        loadBalancerIP: string
        loadBalancerType: string
      loadBalancerSourceRanges: array
        items: string
      type: object
    

FieldType  
Required or optional |  Description  
---|---  
`accessMode`  
`string`  
 _Optional_ |  Defines `rw` (read-write) or `ro` (read-only) access modes for PgBouncer connections. The default value is `ro`.   
`allowSuperUserAccess`  
`boolean`  
 _Optional_ |  AllowSuperUserAccess can be set to true or false   
`dbclusterRef`  
`string`  
 _Required_ |  DBClusterRef is the DBCluster name that PgBouncer pools the connections for. You must create the `PgBouncer` object in the same namespace as the DBCluster that it references. This field is required for PgBouncer connection pooling.   
`parameters`  
`object`  
 _Optional_ |  Parameters will hold key-value pairs of various PgBouncer configurations that can be set. Read <https://www.pgbouncer.org/config.html> for various options that are available. [ Create a PgBouncer Service ](https://cloud.google.com/alloydb/omni/16.9.0/docs/use-connection-pooler-kubernetes#create-pgbouncer-service) provides some sample examples with this spec.   
`podspec`  
`object`  
 _Required_ |  PodSpec contains the specifications of the PgBouncer pod. This contains the image, compute and storage resources serving the PgBouncer pod along with scheduling options.   
`podSpec.image`  
`string`  
 _Required_ |  Image is the Uniform Resource Identifier of a customized pgbouncer image within the artifact registry.   
`podSpec.resources`  
`object`  
 _Required_ |  Resources represents the current configuration of memory and cpu.   
`podSpec.resources.cpu`  
`integer or string`  
 _Required_ |  The amount of CPU allocated to the pgbouncer container.   
`podSpec.resources.memory`  
`integer or string`  
 _Required_ |  The amount of memory allocated to the PgBouncer container.   
`podSpec.schedulingConfig`  
`object`  
 _Optional_ |  Use the SchedulingConfig field to specify how the instance is scheduled on Kubernetes nodes. Changing any field within the scheduling config may cause Kubernetes to reschedule the Pod onto a different node, depending on the new configuration.   
`podSpec.schedulingConfig.nodeAffinity`  
`object`  
 _Optional_ |  NodeAffinity describes node affinity scheduling rules for the instance.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  This field lets you specify affinity preferences for scheduling pods. The scheduler tries to place pods on nodes that match your preferences. However, it is not always possible. The scheduler calculates a "weight" for each node based on how well it matches your preferences and chooses the node with the highest weight.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference`  
`object`  
 _Required_ |  A node selector term, associated with the corresponding weight.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's labels.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt`, and `Lt`.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is `In` or `NotIn`, the values array must not be empty. If the operator is `Exists` or `DoesNotExist`, the values array must be empty. If the operator is `Gt` or `Lt`, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's fields.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt`, and `Lt`.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  The weight associated with matching the corresponding nodeSelectorTerm is in the range from 1 to 100 (inclusive).   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If this field's affinity requirements are not met, the scheduler doesn't schedule the Pod onto the node. If the affinity requirements specified by this field aren't met at some point during pod execution, for example due to an update, the system might or might not try to eventually evict the pod from its node.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms`  
`object`  
 _Required_ |  A list of node selector terms. The terms are ORed.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's labels.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt`, and `Lt`.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's fields.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt`, and `Lt`.   
`podSpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAffinity`  
`object`  
 _Optional_ |  PodAffinity describes pod affinity scheduling rules for the instance.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prioritizes nodes that meet the affinity expressions specified in this field when scheduling Pods. The scheduler might still choose a node that doesn't fully meet the criteria. The most preferred node is the one with the highest total weight. This weight is calculated by adding up values for each node that satisfies all scheduling requirements (such as resource requests or requiredDuringScheduling affinity expressions). For each matching podAffinityTerm, the node's weight increases, and the node(s) with the highest total weight are selected as the most preferred.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm`  
`object`  
 _Required_ |  A pod affinity term, associated with the corresponding weight.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  All matchExpressions within the list must be true for a match to occur.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`podSpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the affinity requirements specified by this field isn't met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field aren't met at some point during pod execution - for example, due to a pod label update - the system might or might not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, which means that all terms must be satisfied.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  All matchExpressions within the list must be true for a match to occur.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt`, and `Lt`.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`podSpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`podSpec.schedulingConfig.podAntiAffinity`  
`object`  
 _Optional_ |  PodAntiAffinity describes pod anti-affinity scheduling rules for the instance.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prefers to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but the scheduler might choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, in other words, for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum, if the node has pods which matches the corresponding podAffinityTerm. The node(s) with the highest sum are the most preferred.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm`  
`object`  
 _Required_ |  A pod affinity term, associated with the corresponding weight.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  A map of key-value pairs. Each key-value pair acts as a requirement. The scheduler matches Pods to nodes that have all the labels specified in `matchLabels`.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`podSpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the anti-affinity requirements specified by this field isn't met at scheduling time, the pod is not scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (for example, due to a pod label update), the system might or might not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, which means that all terms must be satisfied.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists`, and `DoesNotExist`.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`podSpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`podSpec.schedulingConfig.tolerations`  
`object`  
 _Optional_ |  Tolerations enable the management of whether to allow or disallow scheduling an instance on a Kubernetes node that has a specific taint applied.   
`podSpec.schedulingConfig.tolerations.effect`  
`string`  
 _Optional_ |  Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.   
`podSpec.schedulingConfig.tolerations.key`  
`string`  
 _Optional_ |  Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists. This combination means to match all values and all keys.   
`podSpec.schedulingConfig.tolerations.operator`  
`string`  
 _Optional_ |  Operator represents a key's relationship to the value. Valid operators are `Exists` and `Equal`. Defaults to `Equal`. `Exists` is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.   
`podSpec.schedulingConfig.tolerations.tolerationSeconds`  
`integer`  
 _Optional_ |  TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, this field isn't set, which means tolerate the taint forever (do not evict). Zero and negative values are treated as 0 (evict immediately) by the system.   
`podSpec.schedulingConfig.tolerations.value`  
`string`  
 _Optional_ |  Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty; otherwise, it must be a regular string.   
`replicaCount`  
`integer`  
 _Optional_ |  ReplicaCount defines the number of PgBouncer replicas to be deployed.   
`serverTLS`  
`object`  
 _Optional_ |  ServerTLSSpec defines the certificate secret for encrypted communication used by PgBouncer to connect to database cluster for auth query.   
`serverTLS.certSecret`  
`object`  
 _Optional_ |  CertSecret references the certificate secret within the same namespace. The secret must contain entries ca.crt (CA certificate), tls.key (private key), and tls.crt (leaf certificate). The values within this secret are used to populate the server_tls_ca_file, server_tls_cert_file, and server_tls_key_file in pgbouncer.ini. The CA certificate must match the CA that signed the database cluster's leaf certificate. The leaf certificate must contain the CommonName "alloydbpgbouncer".   
`serverTLS.certSecret.name`  
`string`  
 _Optional_ |  'Name of the referent. More info: [ Working with Objects#Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`serviceOptions`  
`object`  
 _Required_ |  ServiceOptions defines the connectivity options for accessing the PgBouncer pods.   
`serviceOptions.annotations`  
`object`  
 _Optional_ |  Annotation provided by the customer will be added to the service object of type loadbalancer.   
`serviceOptions.gcp`  
`object`  
 _Optional_ |  GCP contains Google Cloud specific attributes for the Kubernetes LoadBalancer.   
`serviceOptions.gcp.loadBalancerIP`  
`integer or string`  
 _Optional_ |  LoadBalancerIP is a static IP address, see [Reserve Static External IP Address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address).   
`serviceOptions.gcp.loadBalancerType`  
`string`  
 _Optional_ |  A LoadBalancer can be internal or external. See [Internal Load Balancer](https://kubernetes.io/docs/concepts/services-networking/service/#internal-load-balancer).   
`serviceOptions.loadBalancerSourceRanges`  
`array`  
 _Optional_ |  The CIDR ranges for source IP addresses that are allowed for a client. This parameter is applicable only for `LoadBalancer`.   
`serviceOptions.loadBalancerSourceRanges.items`  
`string`  
 _Optional_ |  Each CIDR range for a source IP address.   
`serviceOptions.type`  
`string`  
 _Required_ |  Type of Kubernetes service to access the PgBouncer pod. It can have the following values: `LoadBalancer` or `ClusterIP`.   
  
## Status schema

PgBouncerStatus defines the observed state of PgBouncer.
    
    
    ipAddress: string
    phase: string
    

FieldType  
Required or optional |  Description  
---|---  
`ipAddress`  
`string`  
 _Required_ |  ipAddress is the PgBouncer endpoint that can be connected to access the database.   
`phase`  
`string`  
 _Required_ |  phase describes the state of PgBouncer Deployment. Values like WaitingForDeploymentReady, Acquiring IP, Ready appear here.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
