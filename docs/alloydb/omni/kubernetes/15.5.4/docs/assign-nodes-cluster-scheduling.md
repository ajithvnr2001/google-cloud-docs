---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/assign-nodes-cluster-scheduling/
title: Assign nodes to a database cluster using scheduling \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:03:13.226632+00:00
---

# Assign nodes to a database cluster using scheduling  |  AlloyDB Omni for Kubernetes: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/assign-nodes-cluster-scheduling/

This page documents AlloyDB Omni version **15.5.4** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)



Send feedback 

#  Assign nodes to a database cluster using scheduling Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/assign-nodes-cluster-scheduling)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/assign-nodes-cluster-scheduling)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/assign-nodes-cluster-scheduling)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/assign-nodes-cluster-scheduling)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/assign-nodes-cluster-scheduling)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/assign-nodes-cluster-scheduling)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/assign-nodes-cluster-scheduling)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/assign-nodes-cluster-scheduling)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/assign-nodes-cluster-scheduling)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/assign-nodes-cluster-scheduling)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/assign-nodes-cluster-scheduling)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/assign-nodes-cluster-scheduling)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/assign-nodes-cluster-scheduling)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/assign-nodes-cluster-scheduling)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/assign-nodes-cluster-scheduling)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/assign-nodes-cluster-scheduling)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/assign-nodes-cluster-scheduling)

In [AlloyDB Omni Kubernetes Operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/deploy-kubernetes), _scheduling_ is a process for matching new database Pods to nodes to balance node distribution across the cluster and help optimize performance. Pods and nodes are matched based on several criteria and available resources, such as CPU and memory. 

For more information about scheduling, see [Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/) in the Kubernetes documentation.

This page shows how to specify tolerations and node affinity scheduling configurations for primary and read pool instances in your Kubernetes manifest.

For information about how to define _taints_ on nodes, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) in the Kubernetes documentation.

## Specify tolerations

To schedule your AlloyDB Omni Pods to nodes free of other application Pods or match a specific _taint_ defined on those nodes, apply one or more tolerations to the nodes as follows:

  1. Modify the AlloyDB Omni Kubernetes Operator cluster's manifest to include a `tolerations` section in the `schedulingConfig` section of either of the following sections: 
     * `primarySpec` for primary instances
     * `spec` for read pool instances
    
    tolerations:
          - key: "TAINT_KEY"
            operator: "OPERATOR_VALUE"
            value: "VALUE"
            effect: "TAINT_EFFECT"
       

Replace the following:

     * `TAINT_KEY`: The existing unique name of the taint key such as a node's hostname or another locally-inferred value that the toleration applies to. The taint key is already defined on a node. An empty field and the `OPERATOR_VALUE` set to `exists` signify that the toleration must match all values and all keys.
     * `OPERATOR_VALUE`: Represents a key's relationship to a set of values. Set the parameter to one of the following: 
       * `exists`: Kubernetes matches any value if the taint is defined regardless of the taint's value.
       * `equal`: Kubernetes does not schedule a Pod to a node if the values are different. The operator requires the taint `true` value.
     * `VALUE`: The taint value the toleration matches to. If the operator is Exists, the value is empty, otherwise it is a regular string. For example, `true`. 
     * `TAINT_EFFECT`: Indicates the taint effect to match. An empty field signifies that all taint effects must be matched. Set the parameter to one of the following: 
       * `NoSchedule`: Kubernetes does not schedule new Pods on the tainted node.
       * `PreferNoSchedule`: Kubernetes avoids placing new Pods on the tainted node unless necessary.
       * `NoExecute`: Kubernetes evicts existing Pods that don't tolerate the taint.
  2. Re-apply the manifest.



## Define node affinity

The Kubernetes scheduler uses node affinity as a set of rules to determine where to place a Pod. Node affinity is a more flexible and expressive version of node selectors.

To specify which nodes must be scheduled for running your database, follow these steps:

  1. Modify the database cluster manifest to include the `nodeaffinity`section after the `tolerations` section in the `schedulingConfig` section of either `primarySpec` for primary instances or `spec` for read pool instances: 
         
         nodeaffinity:
                  NODE_AFFINITY_TYPE:
                  - weight: WAIT_VALUE
                    preference:
                      matchExpressions:
                      - key: LABEL_KEY
                        operator: OPERATOR_VALUE
                        values:
                        - LABEL_KEY_VALUE
             

Replace the following:

     * `NODE_AFFINITY_TYPE`: Set the parameter to one of the following: 
       * `requiredDuringSchedulingIgnoredDuringExecution`: Kubernetes schedules the Pod based exactly on the defined rules.
       * `preferredDuringSchedulingIgnoredDuringExecution`: The Kubernetes scheduler tries to find a node that meets the defined rule for scheduling. However, if there is no such node, Kubernetes schedules to a different node in the cluster.
     * `WAIT_VALUE`: Indicates the preference weight for the specified nodes. Higher values indicate a stronger preference. Valid values are from `1` to `100`.
     * `LABEL_KEY`: The node's label for the key that serves as a location indicator and facilitates even Pod distribution across the cluster. For example, `disktype=ssd`.
     * `OPERATOR_VALUE`: Represents a key's relationship to a set of values. Set the parameter to one of the following: 
       * `In`: The values array must be non-empty.
       * `NotIn`: The values array must be non-empty.
       * `Exists`: The values array must be empty.
       * `DoesNotExist`: The values array must be empty.
       * `Gt`: The values array must have a single element, which is interpreted as an integer.
       * `Lt`: The values array must have a single element, which is interpreted as an integer.
     * `LABEL_KEY_VALUE`: The value for your label key. Set the parameter to an array of string values as follows: 
       * If the operator is `In` or `NotIn`, the values array must be non-empty.
       * If the operator is `Exists` or `DoesNotExist`, the values array must be empty.
       * If the operator is `Gt` or `Lt`, the values array must have a single element, which is interpreted as an integer.
  2. Reapply the manifest.



## Example

The following example illustrates scheduling Pods in AlloyDB Omni Kubernetes Operator primary and read pool instances. Such scheduling setup helps ensure that the primary instance of the database cluster is scheduled on appropriate nodes while allowing some flexibility in node selection. This flexibility can be useful for balancing load, optimizing resource usage, or adhering to specific node roles and characteristics.
    
    
        schedulingconfig:
          tolerations:
          - key: "node-role.kubernetes.io/control-plane"
            operator: "Exists"
            effect: "NoSchedule"
          nodeaffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1
              preference:
                matchExpressions:
                - key: another-node-label-key
                  operator: In
                  values:
                  - another-node-label-value
    

The example toleration allows the Pod to be scheduled on nodes that are marked as control plane nodes because of the following details:

  * The `node-role.kubernetes.io/control-plane` taint key indicates that the node has a control plane node.
  * The `Exists` operator means that the toleration matches any taint with the specified taint key regardless of the value.
  * The `NoSchedule` effect means that Pods aren't going to be scheduled on the control plane node unless they have a matching toleration.



The `preferredDuringSchedulingIgnoredDuringExecution` node affinity type specifies that the rules defined for the node affinity are preferred but are not required during scheduling. If the preferred nodes are not available, the Pod might still be scheduled on other nodes. The `1` weight value indicates a weak preference. Node selection criteria are defined in the `preference` section. The `matchExpressions` section contains an array of expressions used to match nodes. The `another-node-label-key` key represents the key of the node label to match. The `In` operator means the node must have the key with one of the specified values. The `another-node-label-key` key must have the `another-node-label-value` value.

The example node affinity rule indicates a preference for scheduling the Pod on nodes that have the `another-node-label-key` label with the `another-node-label-value` value. The preference is weak so it's not a strong requirement.

The example combines the following:

  * Tolerations that allow the Pod to be scheduled on control plane nodes by tolerating the `NoSchedule` taint.
  * A node affinity that prefers nodes with a specific label but does not strictly require it; hence, it offers flexibility in scheduling.



## What's next

  * [Set up AlloyDB Omni for production](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/configure-omni)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
