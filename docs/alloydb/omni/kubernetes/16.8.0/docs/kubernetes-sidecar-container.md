---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-sidecar-container/
title: Use a sidecar container in Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:36.225387+00:00
---

# Use a sidecar container in Kubernetes  |  AlloyDB Omni for Kubernetes: 16.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-sidecar-container/

This page documents AlloyDB Omni version **16.8.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/overview)



Send feedback 

#  Use a sidecar container in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.8.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-sidecar-container)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/kubernetes-sidecar-container)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/kubernetes-sidecar-container)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/kubernetes-sidecar-container)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/kubernetes-sidecar-container)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-sidecar-container)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/kubernetes-sidecar-container)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/kubernetes-sidecar-container)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/kubernetes-sidecar-container)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-sidecar-container)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/kubernetes-sidecar-container)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/kubernetes-sidecar-container)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-sidecar-container)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/kubernetes-sidecar-container)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/kubernetes-sidecar-container)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/kubernetes-sidecar-container)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/kubernetes-sidecar-container)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-sidecar-container)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/kubernetes-sidecar-container)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-sidecar-container)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/kubernetes-sidecar-container)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-sidecar-container)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/kubernetes-sidecar-container)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/kubernetes-sidecar-container)

The information on this page applies only to AlloyDB Omni for Kubernetes. It does not apply to AlloyDB Omni for containers.

If your database runs in a Kubernetes cluster, then you can add sidecar containers to your database cluster using the AlloyDB Omni Kubernetes operator. AlloyDB Omni operator sidecar containers are regular Kubernetes [containers](https://kubernetes.io/docs/concepts/containers/) that run independently alongside the main application container within the same Pod. You can use these sidecar containers to serve requests for application monitoring, logging, and tracing.

AlloyDB Omni operator sidecar containers are distinct from Kubernetes built-in [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/#pod-sidecar-containers).

To manually add a sidecar container to an existing AlloyDB Omni installation, you create a sidecar custom resource (CR) and add it to your database cluster.

**Caution:** Making changes to an active sidecar container restarts the Pod that it runs on, which might result in database downtime.

## Create a sidecar CR

  1. Apply the following manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Sidecar
         metadata:
           name: SIDECAR_CR_NAME
         spec:
           sidecars:
           - image: CONTAINER_IMAGE
             command: ["CONTAINER_COMMAND"]
             args: ["CONTAINER_ARGS"]
             name: CONTAINER_NAME
         

**Note:** If you configure volumes in the `spec.additionalVolumes` field of your Sidecar custom resource (CR), AlloyDB Omni operator only supports the `configMap`, `secret`, and `downwardAPI` volume types. No other volume types are supported. 

Replace the following variables:

     * `SIDECAR_CR_NAME`: the name for your sidecar container.
     * `CONTAINER_IMAGE`: the name of the image file to run in your sidecar container. For example, `busybox`.
     * `CONTAINER_COMMAND`: the command for the container that runs in the Pod. The command can be a list of quoted strings. For more information, see [Define a command and arguments when you create a Pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/).
     * `CONTAINER_ARGS`: arguments for `CONTAINER_COMMAND`.
     * `CONTAINER_NAME`: the name of the container. You can have multiple containers in the same sidecar CR, and each container has a different container name, image, command, and arguments.
  2. To verify that the sidecar CR is created, run the following command:
         
         kubectl describe Sidecar/SIDECAR_CR_NAME

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

To register the sidecar container name to your database cluster, use the following command to apply the updated specification:
    
    
    kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -p '{"spec":{"primarySpec":{"sidecarRef":{"name":"SIDECAR_CR_NAME"}}}}' --type=merge

Replace the following variables:

  * `DB_CLUSTER_NAME`: the name of your database cluster.
  * `SIDECAR_CR_NAME`: the name for your sidecar container.



## Access logs from a sidecar container

  1. Create, or modify an existing, sidecar container so that `spec.sidecars.volumeMounts.name` is set to `obsdisk` and `spec.sidecars.volumeMounts.mountPath` to a path visible within the sidecar container.
         
         apiVersion: alloydbomni.dbadmin.goog/v1
           kind: Sidecar
           metadata:
             name: SIDECAR_CR_NAME
           spec:
             sidecars:
             - image: CONTAINER_IMAGE
               command: ["CONTAINER_COMMAND"]
               args: ["CONTAINER_ARGS"]
               name: CONTAINER_NAME
               volumeMounts:
                 - name: obsdisk
                   mountPath: LOGS_PATH
         

Replace the following:

     * `SIDECAR_CR_NAME`: the name for your sidecar container.
     * `CONTAINER_IMAGE`: the name of the image file to run in your sidecar container. For example, `busybox`.
     * `CONTAINER_COMMAND`: the command for the container that runs in the Pod. The command can be a list of quoted strings. For more information, see [Define a command and arguments when you create a Pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/).
     * `CONTAINER_ARGS`: the arguments for `CONTAINER_COMMAND`.
     * `CONTAINER_NAME`: the name of the container. You can have multiple containers in the same sidecar CR, and each container has a different container name, image, command, and arguments.
     * `LOGS_PATH`: the path within the sidecar container that AlloyDB Omni should output logs to.
  2. Register your new, or modified, sidecar container.




## What's next

  * [Configure AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/configure-omni).
  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/manage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
