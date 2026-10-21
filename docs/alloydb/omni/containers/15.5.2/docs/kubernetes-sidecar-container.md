---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-sidecar-container/
title: Use a sidecar container in Kubernetes \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:17.425379+00:00
---

# Use a sidecar container in Kubernetes  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-sidecar-container/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Use a sidecar container in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-sidecar-container)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-sidecar-container)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/kubernetes-sidecar-container)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/kubernetes-sidecar-container)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/kubernetes-sidecar-container)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-sidecar-container)

The information on this page applies only to AlloyDB Omni for Kubernetes. It does not apply to AlloyDB Omni for containers.

If your database runs in a Kubernetes cluster, then you can add _sidecar containers_ to your database cluster. Sidecar containers run independently alongside the main container and serve requests for application monitoring, logging, and tracing. You can export logs, metrics, and traces to the backend of your choice using custom agents to AlloyDB Omni.

If your database runs in a Kubernetes cluster, then you can add sidecar containers to your database cluster using the AlloyDB Omni Kubernetes Operator. AlloyDB Omni Operator sidecar containers are regular Kubernetes [containers](https://kubernetes.io/docs/concepts/containers/) that run independently alongside the main application container within the same Pod. You can use these sidecar containers to serve requests for application monitoring, logging, and tracing.

AlloyDB Omni Operator sidecar containers are distinct from Kubernetes built-in [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/#pod-sidecar-containers).

To manually add a sidecar container to an existing AlloyDB Omni installation, you create a sidecar custom resource (CR) and add it to your database cluster.

**Caution:** Making changes to an active sidecar container restarts the Pod that it runs on, which might lead to database downtime.

## Create a sidecar CR

  1. Apply the following manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Sidecar
         metadata:
          name: SIDECAR_CR_NAME
         spec:
          sidecars:
          — image: CONTAINER_IMAGE
            command: ["CONTAINER_COMMAND"]
            args: ["CONTAINER_ARGS"]
            name: CONTAINER_NAME
         

Replace the following:

     * `SIDECAR_CR_NAME`: the name to apply to your sidecar container.
     * `CONTAINER_IMAGE`: the name of the file containing the image to run in the sidecar container, for example, `busybox`.
     * `CONTAINER_COMMAND`: the command for the container that runs in the Pod. The command can be a list of quoted strings. For more information, see [Define a command and arguments when you create a Pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/).
     * `CONTAINER_ARGS`: the arguments for the command for the container that runs in the Pod.
     * `CONTAINER_NAME`: the name of the container. You can have multiple containers in the same sidecar CR, and each container has a different container name, image, command, and arguments.
  2. To verify that the sidecar CR is created, run the following command:
         
         kubectl describe SIDECAR_CR_NAME
         

The output is similar to the following:
         
         Name:  SIDECAR_CR_NAME
         Labels:       <none>
         Annotations:  <none>
         API Version:  alloydbomni.dbadmin.goog/v1
         Kind:         Sidecar
         Metadata:
           Creation Timestamp:  2024-04-15T21:49:00Z
           Finalizers:
             sidecars.dbadmin.goog/finalizer
           Generation:        2
           Resource Version:  2561336
           UID:               e57f2e13-20c5-4905-b13b-39203bab36b4
         Spec:
           Sidecars:
             Args:
               CONTAINER_ARGS
             Command:
               CONTAINER_COMMAND
             Image:  CONTAINER_IMAGE
             Name:   CONTAINER_NAME
             Resources:
         Status:
           Observed Generation:  2
           Reconciled:           true
         Events:                 <none>
         




## Register a sidecar container

To register the sidecar container name to your database cluster, complete the following steps:

  1. Add the `sidecarRef` attribute to your database cluster `spec` object specification in its manifest:
         
         sidecarRef:
           name: SIDECAR_CR_NAME
         

  2. Use the following command to apply the updated specification:
         
         kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -p '{"spec":{"primarySpec":{"sidecarRef":{"name":SIDECAR_CR_NAME}}}}' --type=merge

Replace the following:

     * `DB_CLUSTER_NAME`: the name of your database cluster.
     * `SIDECAR_CR_NAME`: the name to apply to your sidecar container.



## What's next

  * [Configure AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/configure-omni)
  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
