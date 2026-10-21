---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs/
title: Use an EFS resource \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:11.476310+00:00
---

# Use an EFS resource  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use an EFS resource Stay organized with collections  Save and categorize content based on your preferences. 

The [Elastic File System](https://aws.amazon.com/efs/) (EFS) is the underlying AWS mechanism for providing storage (disk space) to your cluster. A PersistentVolume is a cluster resource that makes EFS storage available to your workloads and ensures that it persists even when no workloads are connected to it. This topic describes how a workload can access a PersistentVolume with a PersistentVolumeClaim.

This page is for Operators and Storage specialists who want to configure and manage storage. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

GKE on AWS supports static provisioning of PersistentVolumes for all supported Kubernetes versions. For clusters at Kubernetes version 1.24 or later, GKE on AWS also supports dynamic provisioning. To use dynamic provisioning, your cluster administrator must configure it. To learn how, see [configure a `PersistentVolume`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-efs).

**Note:** Dynamic provisioning is available in GKE on AWS as a preview feature. Contact Google Cloud your support team for access.

## Create a PersistentVolumeClaim

Choose the appropriate tab below depending on whether you want your workload to connect to a statically or dynamically-provisioned persistent volume.

### Static

These instructions assume that your cluster administrator has already provisioned at least one PersistentVolume. To access this PersistentVolume and use its underlying EFS with your workloads, create a PersistentVolumeClaim.

To create a PersistentVolumeClaim for a statically-provisioned PersistentVolume, copy the following YAML manifest into a file named `efs-claim.yaml`.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: CLAIM_NAME
    spec:
      accessModes:
        - ReadWriteMany
      storageClassName: "" # Leave as empty string for static provisioning
      resources:
        requests:
          storage: 5Gi
    

Replace:

  * CLAIM_NAME: a name you choose for your PersistentVolumeClaim to bind to - for example, `efs-claim1`. Leave blank to bind to the default storage class

**Note:** You must use the same `storageClassName` value for your PersistentVolume and PersistentVolumeClaim resources.

  1. Apply the YAML to your cluster.
         
         kubectl apply -f efs-claim.yaml
         

This output confirms the PersistentVolumeClaim's creation.
         
         persistentvolumeclaim/CLAIM_NAME created
         




### Dynamic

These instructions assume that your cluster administrator has already provisioned at least one StorageClass for dynamic provisioning. To create a dynamically-provisioned PersistentVolume with this StorageClass and use the underlying EFS access point with your workloads, create a PersistentVolumeClaim.

To create a PersistentVolumeClaim, follow these steps. The EFS CSI driver uses this PersistentVolumeClaim with the indicated StorageClass to dynamically provision a PersistentVolume.

  1. Copy the following YAML manifest into a file named `efs-claim.yaml`.


    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: CLAIM_NAME
    spec:
      accessModes:
        - ReadWriteMany
      storageClassName: "EFS_STORAGE_CLASS_NAME"
      resources:
        requests:
          storage: 5Gi
    

Replace:

  * CLAIM_NAME: a name you choose for your PersistentVolumeClaim - for example, `efs-claim1`
  * EFS_STORAGE_CLASS_NAME: the name of the StorageClass you want your PersistentVolumeClaim to bind to. Leave this field blank to bind to the default storage class


  1. Apply the YAML to your cluster.
         
         kubectl apply -f efs-claim.yaml
         

The output confirms the PersistentVolumeClaim's creation.
         
         persistentvolumeclaim/CLAIM_NAME created
         




## Create a StatefulSet

After you have created a PersistentVolumeClaim, you can use it in a workload. This section creates a sample StatefulSet that uses a PersistentVolumeClaim. You can also use a PersistentVolumeClaim with other workload types such as Pods and Deployments by referencing the claim in `spec.volumes`.

To create a StatefulSet that mounts the EFS resource referenced in your PersistentVolumeClaim, perform the following steps.

  1. Copy the following YAML manifest into a file named `efs-statefulset.yaml`. This example manifest launches an Ubuntu Linux container that mounts your EFS resource at `/efs-data`. The container writes every five seconds to a file on your EFS resource named `out.txt`.
         
         apiVersion: apps/v1
         kind: StatefulSet
         metadata:
           name: efs-shell
         spec:
           selector:
             matchLabels:
               app: test-efs
           serviceName: efs-app
           replicas: 1
           template:
             metadata:
               labels:
                 app: test-efs
             spec:
               terminationGracePeriodSeconds: 10
               containers:
               - name: linux
                 image: ubuntu:bionic
                 command: ["/bin/sh"]
                 args: ["-c", "while true; do echo $(date -u) >> /efs-data/out.txt; sleep 5; done"]
                 volumeMounts:
                 - name: efs-volume
                   mountPath: /efs-data
               volumes:
               - name: efs-volume
                 persistentVolumeClaim:
                   claimName: CLAIM_NAME
         

Replace CLAIM_NAME with the name of the PersistentVolumeClaim you specified previously - for example, `efs-claim1`.

  2. Apply the YAML to your cluster.
         
         kubectl apply -f efs-statefulset.yaml
         

The output confirms the StatefulSet's creation.
         
         statefulset.apps/efs-shell created
         

The StatefulSet might take several minutes to download and launch the container image.

  3. Confirm the StatefulSet's Pod is in `Running` status with `kubectl get pods`.
         
         kubectl get pods -l app=test-efs
         

The output includes the name of the Pod and its status. In the following response, the Pod's name is `efs-shell-0`.
         
         NAME          READY   STATUS    RESTARTS   AGE
         efs-shell-0   1/1     Running   0          1m
         

  4. After the Pod is in Running status, use `kubectl exec` to connect to the Pod hosting the StatefulSet.
         
         kubectl exec -it efs-shell-0 -- bash
         

The `kubectl` command launches a shell on the Pod.

  5. To confirm that your EFS resource is mounted, check the contents of the `out.txt` file with the `tail` command.
         
         tail /efs-data/out.txt
         

The output contains recent times in UTC.

  6. Disconnect from the Pod with the `exit` command.
         
         exit
         

Your shell returns to your local machine.




## Clean up

To remove the StatefulSet, use `kubectl delete`.
    
    
      kubectl delete -f efs-statefulset.yaml
    

## What's next

  * Learn how to [configure an EFS resource](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-efs)
  * Learn how to [use StorageClasses with your workloads](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
