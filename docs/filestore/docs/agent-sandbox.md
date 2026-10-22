---
url: https://docs.cloud.google.com/filestore/docs/agent-sandbox/
title: Use Filestore agent volumes with GKE Agent Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:48.312114+00:00
---

# Use Filestore agent volumes with GKE Agent Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/agent-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Use Filestore agent volumes with GKE Agent Sandbox Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

Google Kubernetes Engine (GKE) Agent Sandbox provides kernel-level isolation for untrusted model-generated code by using gVisor. By combining GKE Agent Sandbox with Filestore agent volumes, you can deliver secure, isolated environments backed by persistent, high-density file storage.

This guide demonstrates how to configure a gVisor-enabled node pool, define a `SandboxTemplate` with Filestore volume claim templates, pre-warm sandboxes with `SandboxWarmPool`, and claim sandboxes with `SandboxClaim`.

## Before you begin

Complete the cluster and CSI driver setup in [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).

## Create a gVisor-enabled node pool

Create a dedicated node pool configured with gVisor sandbox isolation:
    
    
    gcloud container node-pools create gvisor-pool \
        --cluster=CLUSTER_NAME \
        --location=REGION \
        --project=PROJECT_ID \
        --image-type=cos_containerd \
        --sandbox=type=gvisor \
        --num-nodes=2 \
        --machine-type=n2-standard-16 \
        --enable-autoscaling \
        --min-nodes=1 \
        --max-nodes=10 \
        --scopes=cloud-platform
    

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE cluster.
  * `REGION`: the region where the cluster resides.
  * `PROJECT_ID`: your Google Cloud project ID.



## Create a SandboxTemplate

Define a `SandboxTemplate` manifest named `warmpool-filestore-template.yaml`. The template configures gVisor runtime settings, non-root security contexts, and a `volumeClaimTemplates` block targeting the `volume-pool-sc` `StorageClass`:
    
    
    apiVersion: extensions.agents.x-k8s.io/v1alpha1
    kind: SandboxTemplate
    metadata:
      name: warmpool-filestore-template
      namespace: default
    spec:
      podTemplate:
        spec:
          runtimeClassName: gvisor
          automountServiceAccountToken: false
          securityContext:
            runAsNonRoot: true
            runAsUser: 1000
            fsGroup: 1000
          nodeSelector:
            sandbox.gke.io/runtime: gvisor
          tolerations:
            - key: "sandbox.gke.io/runtime"
              value: "gvisor"
              effect: "NoSchedule"
          containers:
            - name: agent-container
              image: busybox
              command: ["/bin/sh", "-c"]
              args:
                - |
                  echo "Sandbox started with Filestore volume mounted!"
                  ls -la /workspace
                  date > /workspace/session-init.txt
                  cat /workspace/session-init.txt
                  sleep 3600
              securityContext:
                capabilities:
                  drop: ["ALL"]
                allowPrivilegeEscalation: false
              resources:
                requests:
                  cpu: "250m"
                  memory: "256Mi"
                limits:
                  cpu: "500m"
                  memory: "512Mi"
              volumeMounts:
                - name: agent-workspace
                  mountPath: /workspace
      volumeClaimTemplates:
        - metadata:
            name: agent-workspace
          spec:
            accessModes: ["ReadWriteMany"]
            storageClassName: "volume-pool-sc"
            resources:
              requests:
                storage: "1Gi"
    

Apply the manifest:
    
    
    kubectl apply -f warmpool-filestore-template.yaml
    

## Create a SandboxWarmPool

To minimize sandbox startup latency, define a `SandboxWarmPool` manifest named `sandbox-warmpool.yaml` that maintains pre-warmed pod instances:
    
    
    apiVersion: extensions.agents.x-k8s.io/v1alpha1
    kind: SandboxWarmPool
    metadata:
      name: filestore-warmpool
      namespace: default
    spec:
      replicas: 3
      sandboxTemplateRef:
        name: warmpool-filestore-template
    

Apply the manifest:
    
    
    kubectl apply -f sandbox-warmpool.yaml
    

Verify that the warm pool pods are ready:
    
    
    kubectl get sandboxwarmpool filestore-warmpool -n default
    

## Claim a sandbox pod

When an agent session begins, submit a `SandboxClaim` manifest named `sandbox-claim.yaml` to claim a pre-warmed sandbox:
    
    
    apiVersion: extensions.agents.x-k8s.io/v1alpha1
    kind: SandboxClaim
    metadata:
      name: agent-session-1
      namespace: default
    spec:
      sandboxTemplateRef:
        name: warmpool-filestore-template
    

Apply the manifest:
    
    
    kubectl apply -f sandbox-claim.yaml
    

## Verify the mounted volume

  1. Check that the claim is bound to a pod:
         
         kubectl get sandboxclaim agent-session-1
         

  2. Find the pod associated with your claim:
         
         kubectl get pods -l extensions.agents.x-k8s.io/claimed-by=agent-session-1
         

  3. Verify that the volume is mounted inside the claimed container:
         
         kubectl logs POD_NAME -c agent-container
         

Replace `POD_NAME` with the name of the pod returned in the previous step.

The log confirms that `/workspace/session-init.txt` was created on the mounted Filestore volume.




## What's next

  * Explore [Agent Sandbox with late-binding](https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind).
  * Deploy self-managed [GKE workloads](https://docs.cloud.google.com/filestore/docs/self-managed-gke).
  * Learn how to create and manage [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
