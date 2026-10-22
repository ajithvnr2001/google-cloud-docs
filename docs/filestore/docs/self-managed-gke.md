---
url: https://docs.cloud.google.com/filestore/docs/self-managed-gke/
title: Use Filestore agent volumes with self-managed GKE workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:54.763847+00:00
---

# Use Filestore agent volumes with self-managed GKE workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/self-managed-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Use Filestore agent volumes with self-managed GKE workloads Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

If you run standard AI agent benchmarks, developer environments, or automated pipeline workloads on Google Kubernetes Engine (GKE), you can use standard Kubernetes `PersistentVolumeClaim` (PVC) and `Deployment` resources directly with Filestore agent volumes.

This pattern uses familiar Kubernetes resource definitions without requiring custom sandboxing controllers or `DaemonSet` resources.

## Before you begin

Complete the cluster and CSI driver setup in [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).

## Create a PersistentVolumeClaim

Create a manifest named `agent-pvc.yaml` requesting storage from the `volume-pool-sc` `StorageClass` you created earlier:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: agent-workspace-pvc
      namespace: default
    spec:
      accessModes:
        - ReadWriteMany
      storageClassName: volume-pool-sc
      resources:
        requests:
          storage: 1Gi
    

Apply the manifest:
    
    
    kubectl apply -f agent-pvc.yaml
    

Verify that the PVC transitions to `Bound`:
    
    
    kubectl get pvc agent-workspace-pvc
    

The output is similar to the following:
    
    
    NAME                  STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     AGE
    agent-workspace-pvc   Bound    pvc-12345678-abcd-ef01-2345-6789abcdef01   1Gi        RWX            volume-pool-sc   5s
    

The Filestore CSI driver provisions a new volume within your volume pool in under one second and binds the PVC.

## Deploy an agent workload

Create a Deployment manifest named `agent-deployment.yaml` that mounts the bound PVC:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: agent-worker
      namespace: default
      labels:
        app: agent-worker
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: agent-worker
      template:
        metadata:
          labels:
            app: agent-worker
        spec:
          containers:
            - name: worker
              image: busybox:latest
              command: ["/bin/sh", "-c"]
              args:
                - |
                  echo "Agent worker started. Workspace mounted at /workspace:"
                  ls -la /workspace
                  echo "Writing benchmark results..."
                  date > /workspace/run-status.txt
                  cat /workspace/run-status.txt
                  sleep infinity
              resources:
                requests:
                  cpu: "250m"
                  memory: "256Mi"
                limits:
                  cpu: "500m"
                  memory: "512Mi"
              volumeMounts:
                - name: workspace-storage
                  mountPath: /workspace
          volumes:
            - name: workspace-storage
              persistentVolumeClaim:
                claimName: agent-workspace-pvc
    

Apply the manifest:
    
    
    kubectl apply -f agent-deployment.yaml
    

## Verify the deployment and file access

  1. Check that the deployment pod is running:
         
         kubectl get pods -l app=agent-worker
         

The output is similar to the following:
         
         NAME                            READY   STATUS    RESTARTS   AGE
         agent-worker-6789bcdef-ghijk    1/1     Running   0          30s
         

  2. Check container logs to confirm successful file operations:
         
         kubectl logs -l app=agent-worker -c worker
         

The output is similar to the following:
         
         Agent worker started. Workspace mounted at /workspace:
         total 8
         drwxr-xr-x    2 root     root          4096 Sep 14 12:00 .
         drwxr-xr-x    1 root     root          4096 Sep 14 12:00 ..
         Writing benchmark results...
         Mon Sep 14 12:00:05 UTC 2026
         




Because Filestore agent volumes support `ReadWriteMany` (RWX) access, multiple replicas or distinct pods can concurrently mount the same PVC for collaborative agent workflows.

## What's next

  * Explore [Agent Sandbox](https://docs.cloud.google.com/filestore/docs/agent-sandbox).
  * Configure [Agent Sandbox with dynamic storage late-binding](https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind).
  * Create and configure [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
