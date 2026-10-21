---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/access-crash-looping-database-pod/
title: Troubleshoot a crashlooping database pod in AlloyDB Omni using the container orchestrator \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:53.252530+00:00
---

# Troubleshoot a crashlooping database pod in AlloyDB Omni using the container orchestrator  |  AlloyDB Omni using the container orchestrator: 16.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/access-crash-looping-database-pod/

This page documents AlloyDB Omni version **16.13.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/overview)



Send feedback 

#  Troubleshoot a crashlooping database pod in AlloyDB Omni using the container orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/access-crash-looping-database-pod)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/access-crash-looping-database-pod)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/access-crash-looping-database-pod)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/access-crash-looping-database-pod)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/access-crash-looping-database-pod)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/access-crash-looping-database-pod)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/access-crash-looping-database-pod)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/access-crash-looping-database-pod)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/access-crash-looping-database-pod)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/access-crash-looping-database-pod)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/access-crash-looping-database-pod)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/access-crash-looping-database-pod)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/access-crash-looping-database-pod)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/access-crash-looping-database-pod)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/access-crash-looping-database-pod)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/access-crash-looping-database-pod)



This page describes how to resolve issues with AlloyDB Omni for Kubernetes when you encounter the following situations:

  * You have a crashlooping database cluster in Kubernetes, and you know the name and namespace of the database, its internal instance, and the pod.
  * You need to access a file on the database pod, but the crash loop prevents access.



A _crashlooping_ database pod is a pod that repeatedly starts, crashes, and is then automatically restarted by Kubernetes. This cycle continues indefinitely until the underlying issue is resolved. The database becomes unavailable and unstable during this process.

## Before you begin

Before you follow the troubleshooting guidance in this document, try these solutions:

  * If high availability (HA) is available, trigger a failover. With HA, a synchronous standby instance is ready to replace the primary instance.
  * Recover from a backup, if one is available. This approach is automated and less error prone.



## Cannot access files on a crashlooping database pod

**Description:** A database pod in your Kubernetes cluster enters a `CrashLoopBackOff` state. This state prevents you from using `kubectl exec` to access the database container's file system for debugging.

**Recommended fix:** To resolve this issue, temporarily stop the crash loop by patching the pod's `StatefulSet` to override the container's command. Before you proceed, consider simpler alternatives, such as triggering a failover or recovering from a backup, if available.

To access the pod, follow these steps:

  1. Pause all related user-facing AlloyDB Omni resources to prevent them from interfering with the recovery process.

     1. List all AlloyDB Omni Kubernetes custom resource definitions:
            
            kubectl get crd | grep alloydbomni.dbadmin
            

     2. Review the list of resources for your database cluster. Keep a list of the resources that you pause so that you can unpause them later. At a minimum, you must pause the `dbclusters.alloydbomni.dbadmin.goog` resource.

     3. Pause each resource separately by adding the `ctrlfwk.internal.gdc.goog/pause` annotation.
            
            kubectl annotate RESOURCE_TYPE -n NAMESPACE RESOURCE_NAME ctrlfwk.internal.gdc.goog/pause=true
            

Replace the following:

        * `RESOURCE_TYPE`: the type of the resource to pause, for example, `dbclusters.alloydbomni.dbadmin.goog`.
        * `NAMESPACE`: the namespace of the database cluster.
        * `RESOURCE_NAME`: the name of the resource to pause.
  2. Pause the internal instance that manages the crashlooping pod.

     1. Find the name of the internal instance.
            
            kubectl get instances.alloydbomni.internal.dbadmin.goog -n NAMESPACE
            

Replace the following:

        * `NAMESPACE`: the name of the namespace that you're interested in.
     2. Pause the instance. The `ctrlfwk.internal.gdc.goog/pause=true` annotation tells the AlloyDB Omni controller to pause its management of the resource. This prevents the controller from automatically reconciling or changing the resource while you're manually performing troubleshooting steps, such as patching the underlying `StatefulSet`.
            
            kubectl annotate instances.alloydbomni.internal.dbadmin.goog -n NAMESPACE INSTANCE_NAME ctrlfwk.internal.gdc.goog/pause=true
            

Replace the following:

        * `NAMESPACE`: the name of the namespace that you're interested in.
        * `INSTANCE_NAME`: the name of the instance that you found.
  3. Prevent the pod from crashlooping.

Patch the pod's `StatefulSet` to override the main container's command. This change stops the application from starting and crashing, which lets you access the pod.

     1. Confirm the name of the crashlooping pod.
            
            kubectl get pod -n NAMESPACE
            

Replace `NAMESPACE`, which is the name of the namespace that you're interested in.

     2. Find the name of the `StatefulSet` that owns the pod.
            
            kubectl get pod -n NAMESPACE POD_NAME -ojsonpath='{.metadata.ownerReferences[0].name}'
            

Replace the following:

        * `NAMESPACE`: the name of the namespace that you're interested in.
        * `POD_NAME`: the name of the crashlooping pod.
     3. Patch the `StatefulSet` to replace the database container's command with `sleep infinity`:
            
            kubectl patch statefulset STATEFULSET_NAME -n NAMESPACE --type='strategic' -p '
            {
              "spec": {
                "template": {
                  "spec": {
                    "containers": [
                      {
                        "name": "database",
                        "command": ["sleep"],
                        "args": ["infinity"],
                        "livenessProbe": null,
                        "startupProbe": null
                      }
                    ]
                  }
                }
              }
            }
            '
            

Replace the following:

        * `NAMESPACE`: the name of the namespace that you're interested in.
        * `STATEFULSET_NAME`: the name of the `StatefulSet`.
     4. Delete the pod to apply the patch.
            
            kubectl delete pod -n NAMESPACE POD_NAME
            

Replace the following:

        * `NAMESPACE`: the name of the namespace that you're interested in.
        * `POD_NAME`: the name of the crashlooping pod.
  4. Access the database in the pod.
         
         kubectl exec -ti -n NAMESPACE POD_NAME -c database -- bash
         

Replace the following:

     * `NAMESPACE`: the name of the namespace that you're interested in.
     * `POD_NAME`: the name of the crashlooping pod.

After the new pod starts, it runs the `sleep` command instead of the database application. You can now access the pod's shell.

  5. Unpause all components.

After investigating, restore the original state by removing the `pause` annotations. You unpause the resources in the reverse order of pausing them; for example, unpause the instance before you unpause the DBCluster. This action reconciles the resources and restarts the database pod with its original command.

     1. For each resource that you paused, remove the annotation by appending a hyphen to the annotation name. The following example removes the annotation from an instance:
            
            kubectl annotate instances.alloydbomni.internal.dbadmin.goog -n NAMESPACE INSTANCE_NAME ctrlfwk.internal.gdc.goog/pause-
            

Replace the following:

        * `NAMESPACE`: the name of the namespace that you're interested in.
        * `INSTANCE_NAME`: the name of the instance that you found in the previous step.
     2. Repeat this process for all other resources that you paused in the first step.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
