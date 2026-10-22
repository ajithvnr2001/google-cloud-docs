---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-storage/
title: Manage Agent Sandbox on GKE storage \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:37:28.841207+00:00
---

# Manage Agent Sandbox on GKE storage  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Manage Agent Sandbox on GKE storage Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides reference implementations for managing storage for Agent Sandbox on GKE tailored to your agents' data lifecycle needs.

Depending on your agents' data lifecycle needs, choose one of the following configurations:

  * Configure a stateful workspace
  * Configure a point-in-time restore and ownership transfer
  * Configure an ephemeral workspace



For more information about choosing a storage solution, see [Choose storage for AI agentic workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox-storage).

The following document uses the `dynamic-rwo` StorageClass for [automated disk type selection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#automated_disk_type_selection) to provision disks compatible with machine types of nodes where Agent Sandbox on GKE Pods are scheduled. To help ensure that GKE provisions Hyperdisk Balanced volumes for your agents' storage, you must schedule your Agent Sandbox on GKE Pods on the nodes of [compatible machine families](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#machine-series), such as N4; otherwise, GKE falls back to `pd-balanced`.

This document implements the _Private Isolated Workspace_ data access mode by using `ReadWriteOnce` (RWO) access. In this mode, an agent starts up with a private isolated storage directory it has sole read and write access to.

Unless otherwise specified, the reference implementations in this document use [direct sandbox creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#alternative_create_a_sandbox_directly), which is applicable to agents that tolerate multi-second startup latency. To achieve sub-second startup latency for stateful or point-in-time restore workspaces, you must use [Agent Sandbox on GKE Warm Pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox#warm-pools). Binding storage to a claimed Warm Pool Pod requires custom scripting and a privileged DaemonSet. For a reference implementation, see this [GitHub example](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/latebind-storage-gke-sandbox).

## Alternative access modes

To support alternative access modes, you can modify the volume and snapshot definitions in the configurations:

  * **Collaborative workspace** : change the `accessModes` to `ReadWriteMany` and use an RWX-capable StorageClass, such as [Filestore Multishares](https://docs.cloud.google.com/filestore/docs/multishares#storageclasses_and_dynamic_volume_provisioning) (Enterprise) (`enterprise-multishare-rwx`).
  * **Exploration branching workspace** : mount the template folder as read-only and providing a separate writable scratchpad. For the base template, you must use storage supporting multiple read-only attachments, such as [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml) with `ReadOnlyMany` (ROX) access mode or Filestore Multishares with RWX access mode.



## Before you begin

[Enable Agent Sandbox on GKE in your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#before_you_begin).

## Configure a stateful workspace

Use this pattern to preserve the latest state of an agent's files. It is useful when your agent must preserve the state when the agent session is paused or terminated (Agent Sandbox is deleted) and restore the data from the latest state when the agent session is activated (Agent Sandbox is re-created).

The reference implementation in this section uses direct sandbox creation and is applicable to agents that tolerate multi-second startup latency.

This approach uses standard GKE PersistentVolumeClaim (PVC) resources to link a sandbox to a pre-existing PVC containing a user's data.

The stateful workspace pattern follows this sequence of events:

  1. **Provisioning** : the administrator or orchestrator manually provisions a private PVC for each agent session using a deterministic identifier (for example, `pvc-agent-1`).
  2. **Referencing** : in the Sandbox resource, you use the `persistentVolumeClaim` field within the `volumes` block to specify the exact `claimName` of the existing volume.
  3. **Latency** : when the sandbox is created, GKE must dynamically attach the Compute Engine disk to the node VM, which incurs a standard multi-second delay.
  4. **Persistence** : on session termination (deleting the Sandbox), GKE detaches the disk but does not destroy the PVC, which helps to ensure that the latest state is preserved for the next session.



To configure a stateful workspace that preserves data between sessions, complete the steps in the following subsections.

### Provision a persistent workspace (PVC)

Create a private PersistentVolumeClaim (PVC) that uses a deterministic identifier, such as `pvc-agent-1`.

  1. Save the following manifest as `pvc-agent-1.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: pvc-agent-1 # Derived directly from the deterministic assignment ID
           namespace: default
         spec:
           accessModes:
             - ReadWriteOnce
           storageClassName: dynamic-rwo # Selects disk type compatible with the node machine family
           resources:
             requests:
               storage: 10Gi
         

  2. Apply the manifest:
         
         kubectl apply -f pvc-agent-1.yaml
         




Because the storage class uses dynamic volume binding, the disk is not attached to any node yet. It remains in a `Pending` state until a Pod requesting it is scheduled.

### Deploy the Agent Sandbox

Deploy the Sandbox custom resource, referencing the deterministic PVC.

  1. Save the following manifest as `sandbox-agent-1.yaml`:
         
         apiVersion: agents.x-k8s.io/v1alpha1
         kind: Sandbox
         metadata:
           name: sandbox-agent-1 # Traceable sandbox name
           namespace: default
         spec:
           replicas: 1
           podTemplate:
             spec:
               runtimeClassName: gvisor # Required
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
                 runAsUser: 1000
                 fsGroup: 1000 # Grant group access to the volume
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor # Required
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: agent
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 volumeMounts:
                 - name: workspace-disk
                   mountPath: /workspace # Mounts the private disk into the container
                 resources:
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               volumes:
               - name: workspace-disk
                 persistentVolumeClaim:
                   claimName: pvc-agent-1 # Binds this specific Sandbox to Agent 1's PVC
               restartPolicy: OnFailure
         

  2. Apply the manifest:
         
         kubectl apply -f sandbox-agent-1.yaml
         




GKE verifies node capacity and attaches the disk, which takes a few seconds. The container initializes inside a userspace gVisor kernel.

### Write data from the agent

Simulate an active AI agent executing file modifications inside its workspace by writing a text file to the mounted disk.
    
    
    # Set the active Pod name
    POD_NAME=sandbox-agent-1
    
    # Write a state file to the persistent directory
    kubectl exec $POD_NAME -- sh -c "echo 'Workspace State Saved - Agent 1' > /workspace/modified_data.txt"
    
    # Confirm the file exists on the disk
    kubectl exec $POD_NAME -- cat /workspace/modified_data.txt
    

### End the agent session

To simulate scaling down or terminating the session when the agent goes idle, delete the Sandbox resource but preserve the underlying storage.
    
    
    kubectl delete sandbox sandbox-agent-1
    

GKE unmounts and detaches the disk. The `pvc-agent-1` PVC remains, preserving the data.

### Reactivate the agent session

To reactivate the session, redeploy a fresh Sandbox resource that references the same PVC.
    
    
    kubectl apply -f sandbox-agent-1.yaml
    

The disk is re-attached (incurring the attachment delay), and the container boots up.

### Verify data preservation

Inspect the newly created sandbox container to verify that the previous session data was preserved.
    
    
    # Set the active Pod name of the new session
    NEW_POD_NAME=sandbox-agent-1
    
    # Read the file from the newly booted sandbox
    kubectl exec -it $NEW_POD_NAME -- cat /workspace/modified_data.txt
    

The output should show `Workspace State Saved - Agent 1`.

### Clean up resources

Delete the Agent Sandbox and the associated persistent volume claim:
    
    
    kubectl delete sandbox sandbox-agent-1
    kubectl delete pvc pvc-agent-1
    

## Configure a point-in-time restore and ownership transfer

Use this pattern to clone datasets for running parallel experiments, debugging, or independent work. An agent's workspace is initialized from a historical dataset (or shared state), saving subsequent modifications to a separate, private writable layer without modifying the base template.

The reference implementation in this section uses direct sandbox creation and is applicable to agents that tolerate multi-second startup latency. This approach relies on the orchestrator to dynamically provision new PersistentVolumeClaims (PVCs) from historical VolumeSnapshots before launching a fresh sandbox session.

### Create the VolumeSnapshotClass

Create a VolumeSnapshotClass that specifies the CSI driver and deletion policy. For Hyperdisk, use the `pd.csi.storage.gke.io` driver.

  1. Save the following manifest as `1-snapshot-class.yaml`:
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshotClass
         metadata:
           name: standard-rwo-snapshot
         driver: pd.csi.storage.gke.io
         deletionPolicy: Delete
         

  2. Apply the manifest:
         
         kubectl apply -f 1-snapshot-class.yaml
         




### Provision the initial workspace

Create a volume where the agent will perform its initial work.

  1. Save the following manifest as `2-source-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: agent-source-pvc
         spec:
           accessModes: ["ReadWriteOnce"]
           storageClassName: dynamic-rwo
           resources:
             requests:
               storage: 10Gi
         

  2. Apply the manifest:
         
         kubectl apply -f 2-source-pvc.yaml
         




### Generate state data

Deploy a sandbox Pod to write data to the volume.

  1. Save the following manifest as `3-source-sandbox.yaml`:
         
         apiVersion: agents.x-k8s.io/v1alpha1
         kind: Sandbox
         metadata:
           name: agent-session-v1
           namespace: default
         spec:
           replicas: 1
           podTemplate:
             spec:
               runtimeClassName: gvisor
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
                 runAsUser: 1000
                 fsGroup: 1000 # Grant group access to the volume
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor # Required
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: agent
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 volumeMounts:
                 - name: workspace
                   mountPath: /workspace
                 resources:
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               volumes:
               - name: workspace
                 persistentVolumeClaim:
                   claimName: agent-source-pvc
               restartPolicy: OnFailure
         

  2. Apply the manifest:
         
         kubectl apply -f 3-source-sandbox.yaml
         

  3. Wait for the Pod to be running, then write a state file:
         
         POD_NAME=agent-session-v1
         kubectl exec $POD_NAME -- sh -c "echo 'Point-in-Time Snapshot - v1' > /workspace/state.txt"
         




### Archive the historical state (CSI VolumeSnapshot)

Trigger a CSI VolumeSnapshot to freeze the current state. When taking a snapshot, follow the [best practices for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices).

  1. Save the following manifest as `4-volume-snapshot.yaml`:
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
           name: agent-session-v1-snapshot
         spec:
           volumeSnapshotClassName: standard-rwo-snapshot
           source:
             persistentVolumeClaimName: agent-source-pvc
         

  2. Apply the manifest:
         
         kubectl apply -f 4-volume-snapshot.yaml
         




### Restore the volume from the snapshot

Deploy a new PVC with its `dataSource` pointing to the CSI `VolumeSnapshot`.

  1. Save the following manifest as `5-restored-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: agent-restored-pvc
         spec:
           accessModes: ["ReadWriteOnce"]
           storageClassName: dynamic-rwo
           dataSource:
             name: agent-session-v1-snapshot
             kind: VolumeSnapshot
             apiGroup: snapshot.storage.k8s.io
           resources:
             requests:
               storage: 10Gi
         

  2. Apply the manifest:
         
         kubectl apply -f 5-restored-pvc.yaml
         




### Launch the restored Agent Sandbox session

Provision a fresh Sandbox resource that references the newly restored PVC.

  1. Save the following manifest as `6-restored-sandbox.yaml`:
         
         apiVersion: agents.x-k8s.io/v1alpha1
         kind: Sandbox
         metadata:
           name: agent-session-v2-restored
           namespace: default
         spec:
           replicas: 1
           podTemplate:
             spec:
               runtimeClassName: gvisor
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
                 runAsUser: 1000
                 fsGroup: 1000 # Grant group access to the volume
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor # Required
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: agent
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 volumeMounts:
                 - name: workspace
                   mountPath: /workspace
                 resources:
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               volumes:
               - name: workspace
                 persistentVolumeClaim:
                   claimName: agent-restored-pvc
               restartPolicy: OnFailure
         

  2. Apply the manifest:
         
         kubectl apply -f 6-restored-sandbox.yaml
         




### Verify persistence and restoration

Verify that the agent can read the historical data.
    
    
    NEW_POD_NAME=agent-session-v2-restored
    kubectl exec $NEW_POD_NAME -- cat /workspace/state.txt
    

Expected Output: `Point-in-Time Snapshot - v1`

### Clean up resources

Delete the Agent Sandboxes, PVCs, and the VolumeSnapshot:
    
    
    kubectl delete sandbox agent-session-v1
    kubectl delete sandbox agent-session-v2-restored
    kubectl delete pvc agent-source-pvc
    kubectl delete pvc agent-restored-pvc
    kubectl delete volumesnapshot agent-session-v1-snapshot
    kubectl delete volumesnapshotclass standard-rwo-snapshot
    

## Configure an ephemeral workspace

Use the ephemeral workspace pattern when an agent needs a storage volume for storing temporary files while the agent is active. No data needs to be preserved on Agent Sandbox deletion.

### Configure with sub-second startup

Use Agent Sandbox on GKE Warm Pools to pre-provision empty volumes in the background.

#### Define the SandboxTemplate

Define the ephemeral storage backing within the `volumeClaimTemplate` block.

  1. Save the following manifest as `stateless-template.yaml`:
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxTemplate
         metadata:
           name: stateless-sandbox-template
           namespace: default
         spec:
           podTemplate:
             spec:
               runtimeClassName: gvisor
               automountServiceAccountToken: false
               securityContext:
                 runAsNonRoot: true
                 runAsUser: 1000
                 fsGroup: 1000 # Grant group access to the volume
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule"
               containers:
               - name: agent
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 volumeMounts:
                 - name: ephemeral-disk
                   mountPath: /workspace
                 resources:
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
           volumeClaimTemplates:
           - metadata:
               name: ephemeral-disk
             spec:
               accessModes: ["ReadWriteOnce"]
               storageClassName: dynamic-rwo # Selects disk type compatible with node machine family
               resources:
                 requests:
                   storage: 10Gi
         




#### Launch the Sandbox Warm Pool

  1. Save the following manifest as `stateless-warmpool.yaml`:
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxWarmPool
         metadata:
           name: stateless-warmpool
           namespace: default
         spec:
           replicas: 5 # Keep five standby Pods with pre-attached empty disks
           sandboxTemplateRef:
             name: stateless-sandbox-template
         

  2. Apply both manifests:
         
         kubectl apply -f stateless-template.yaml
         kubectl apply -f stateless-warmpool.yaml
         




#### Claim the Sandbox

Define a SandboxClaim that triggers when a user starts a session.

  1. Save the following manifest as `stateless-sandbox-claim.yaml`:
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxClaim
         metadata:
           name: agent-1-claim
         spec:
           sandboxTemplateRef:
             name: stateless-sandbox-template
         

  2. Apply the manifest:
         
         kubectl apply -f stateless-sandbox-claim.yaml
         




#### Verify sub-second execution

Capture the Agent Sandbox Pod name and verify that the `/workspace` directory is mounted and ready for immediate use:
    
    
    export POD_NAME=$(kubectl get sandboxclaim agent-1-claim -o jsonpath='{.status.sandbox.name}')
    kubectl exec $POD_NAME -- ls -la /workspace
    

#### Terminate the agent session

To end the agent session and release the claimed Sandbox, delete the SandboxClaim resource:
    
    
    kubectl delete sandboxclaim agent-1-claim
    

#### Clean up resources

Delete the Sandbox Warm Pool and the Sandbox template:
    
    
    kubectl delete sandboxwarmpool stateless-warmpool
    kubectl delete sandboxtemplate stateless-sandbox-template
    

### Configure with multi-second startup

To implement an ephemeral workspace that tolerates multi-second latency, use direct Agent Sandbox creation _without_ a Warm Pool.

#### Define a stateless Agent Sandbox

  1. Save the following manifest as `sandbox-direct-stateless.yaml`:
         
         apiVersion: agents.x-k8s.io/v1alpha1
         kind: Sandbox
         metadata:
           name: sandbox-direct-stateless
           namespace: default
         spec:
           replicas: 1
           podTemplate:
             spec:
               runtimeClassName: gvisor
               automountServiceAccountToken: false
               securityContext:
                 runAsNonRoot: true
                 runAsUser: 1000
                 fsGroup: 1000 # Grant group access to the volume
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule"
               containers:
               - name: agent
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 volumeMounts:
                 - name: ephemeral-disk
                   mountPath: /workspace
                 resources:
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               restartPolicy: OnFailure
           volumeClaimTemplates:
           - metadata:
               name: ephemeral-disk
             spec:
               accessModes: ["ReadWriteOnce"]
               storageClassName: dynamic-rwo
               resources:
                 requests:
                   storage: 10Gi
         




#### Deploy the Agent Sandbox

To dynamically provision the disk and attach it to the scheduled node, apply the manifest:
    
    
    kubectl apply -f sandbox-direct-stateless.yaml
    

#### Verify startup latency and execution

Monitor the Pod status to observe the attachment delay before the Pod transitions to the `Running` state:
    
    
    kubectl get pods -w
    

After the Pod is running, capture the Pod name and verify that the `/workspace` directory is available:
    
    
    POD_NAME=sandbox-direct-stateless
    kubectl exec $POD_NAME -- ls -la /workspace
    

#### Terminate agent session

Delete the Sandbox resource to automatically terminate the Pod and destroy its ephemeral storage:
    
    
    kubectl delete sandbox sandbox-direct-stateless
    

## What's next

  * [Learn more about Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).
  * [Learn more about isolating AI code execution with Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox).
  * Learn how to [Save and restore Agent Sandbox on GKE environments with Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
