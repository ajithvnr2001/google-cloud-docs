---
url: https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind/
title: Use Filestore agent volumes with GKE Agent Sandbox dynamic storage late-binding \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:36.917513+00:00
---

# Use Filestore agent volumes with GKE Agent Sandbox dynamic storage late-binding  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Use Filestore agent volumes with GKE Agent Sandbox dynamic storage late-binding Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

Dynamic storage late-binding lets you inject Filestore agent volumes directly into running, pre-warmed Google Kubernetes Engine (GKE) Agent Sandbox pods upon claim. By bypassing the standard Kubernetes volume attachment lifecycle, dynamic late-binding achieves under 100 ms storage attachment latency without requiring pod restarts.

This architecture enables high-density, low-latency agent platforms to:

  * Eliminate pod cold-start and container initialization delays.
  * Dynamically attach and detach persistent workspaces on demand.
  * Pause or hibernate idle agent sessions and resume them on any available pre-warmed sandbox pod while preserving file system state.



## Before you begin

  1. Complete the initial setup in [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).
  2. Verify that your GKE cluster runs version `1.36.0-gke.3302001` or higher. This version supports the `force-shared` annotation required for gVisor `emptyDir` mount propagation.
  3. Verify that your `volume-pool-sc` `StorageClass` specifies `volumeBindingMode: Immediate` and `reclaimPolicy: Delete`.



## Architecture overview

The late-binding architecture consists of four components:

  * **Platform orchestrator or custom controller:** A control-plane service or Kubernetes controller that manages session lifecycles. It watches for `SandboxClaim` events, resolves tenant volume metadata, calls the storage node daemon API to bind or unbind storage, and manages deletion finalizers.
  * **Storage node daemon:** A privileged `DaemonSet` running on each gVisor node that exposes a mount API.
  * **`SandboxTemplate` with `force-shared`:** A [gVisor sandbox pod](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) template which lets the host mounts propagate dynamically into the gVisor sandbox container.
  * **`SandboxWarmPool`:** A pool of pre-warmed running sandbox pods ready to receive mount requests instantly upon claim.

**Note:** To make the underlying mechanics transparent, the procedural steps in this document use manual CLI commands (`kubectl exec` and `kubectl patch`) to simulate orchestrator actions. In a production environment, you must build a custom controller or orchestrator to automate these workflows. For architectural guidance, see Production considerations and custom controller design.

## Deploy the storage node daemon

Create a manifest named `storage-node-daemon.yaml` containing the privileged `DaemonSet`:

Click to view the `storage-node-daemon.yaml` manifest
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: storage-node-daemon
      namespace: default
    spec:
      selector:
        matchLabels:
          app: storage-node-daemon
      template:
        metadata:
          labels:
            app: storage-node-daemon
        spec:
          hostPID: true
          nodeSelector:
            sandbox.gke.io/runtime: gvisor
          tolerations:
            - key: "sandbox.gke.io/runtime"
              operator: "Equal"
              value: "gvisor"
              effect: "NoSchedule"
          initContainers:
            - name: install-nfs
              image: debian:stable-slim
              securityContext:
                privileged: true
              volumeMounts:
                - name: host-root
                  mountPath: /host-root
                  mountPropagation: Bidirectional
              command: ["/bin/sh", "-c"]
              args:
                - |
                  nsenter -t 1 -m -u -i -n -- apt-get update && \
                  nsenter -t 1 -m -u -i -n -- apt-get install -y nfs-common || true
          containers:
            - name: daemon
              image: python:3.11-slim
              securityContext:
                privileged: true
              volumeMounts:
                - name: host-root
                  mountPath: /host-root
                  mountPropagation: Bidirectional
              command: ["python3", "-u", "-c"]
              args:
                - |
                  import os, json, subprocess, traceback
                  from http.server import BaseHTTPRequestHandler, HTTPServer
    
                  def safe_join(base, *parts):
                      base = os.path.abspath(base)
                      path = os.path.abspath(os.path.join(base, *parts))
                      if os.path.commonpath([base, path]) != base:
                          raise ValueError("Path escapes base directory")
                      return path
    
                  class Handler(BaseHTTPRequestHandler):
                      def do_POST(self):
                          try:
                              length = int(self.headers.get('Content-Length', 0))
                              data = json.loads(self.rfile.read(length))
                              pod_uid = data['pod_uid']
                              action = data['action']
                              volume_name = data['volume_name']
                              sub_dir = data['sub_dir']
    
                              parent = safe_join("/host-root/var/lib/kubelet/pods",
                                                 pod_uid, "volumes/kubernetes.io~empty-dir", volume_name)
                              target = safe_join(parent, sub_dir)
                              host_target = safe_join("/var/lib/kubelet/pods", pod_uid,
                                                      "volumes/kubernetes.io~empty-dir", volume_name, sub_dir)
    
                              if action == "bind_nfs":
                                  source = f"{data['nfs_server']}:{data['nfs_path']}"
                                  os.makedirs(target, exist_ok=True)
                                  subprocess.run(["nsenter", "-t", "1", "-m", "--",
                                                  "mount", "-t", "nfs", "-o", "nolock", source, host_target], check=True)
                                  subprocess.run(["nsenter", "-t", "1", "-m", "--",
                                                  "chown", "-R", "1000:1000", host_target], check=True)
                                  with open(f"{parent}/.ready", "w") as f:
                                      f.write("ready")
                                  msg = f"Bound {source} to {host_target}"
                              elif action == "unbind":
                                  subprocess.run(["nsenter", "-t", "1", "-m", "--",
                                                  "umount", "-l", host_target], check=True)
                                  msg = f"Unbound {host_target}"
    
                              self.send_response(200)
                              self.end_headers()
                              self.wfile.write(msg.encode())
                          except Exception:
                              err = traceback.format_exc()
                              self.send_response(500)
                              self.end_headers()
                              self.wfile.write(err.encode())
    
                  HTTPServer(('localhost', 9090), Handler).serve_forever()
          volumes:
            - name: host-root
              hostPath:
                path: /
    

Apply the manifest:
    
    
    kubectl apply -f storage-node-daemon.yaml
    

## Deploy the `SandboxTemplate` and `SandboxWarmPool`

Create a manifest named `sandbox-latebind.yaml` containing the template and warm pool:

Click to view the `sandbox-latebind.yaml` manifest
    
    
    apiVersion: extensions.agents.x-k8s.io/v1alpha1
    kind: SandboxTemplate
    metadata:
      name: late-bind-template
      namespace: default
    spec:
      networkPolicyManagement: Unmanaged
      podTemplate:
        metadata:
          annotations:
            dev.gvisor.empty-dir.workspace-volume.force-shared: "true"
        spec:
          runtimeClassName: gvisor
          automountServiceAccountToken: false
          nodeSelector:
            sandbox.gke.io/runtime: gvisor
          tolerations:
            - key: "sandbox.gke.io/runtime"
              value: "gvisor"
              effect: "NoSchedule"
          securityContext:
            runAsNonRoot: true
            runAsUser: 1000
            runAsGroup: 1000
            fsGroup: 1000
          containers:
            - name: agent
              image: busybox:latest
              securityContext:
                capabilities:
                  drop: ["ALL"]
                allowPrivilegeEscalation: false
              volumeMounts:
                - name: workspace-volume
                  mountPath: /workspace
                  mountPropagation: HostToContainer
              env:
                - name: MOUNT_PATH
                  value: "/workspace"
                - name: SUB_DIR
                  value: "user_data"
              command: ["/bin/sh", "-c"]
              args:
                - |
                  echo "Waiting for late-bind signal..."
                  while [ ! -f $MOUNT_PATH/.ready ]; do sleep 0.05; done
                  echo "Filestore volume mounted successfully!"
                  ls -la $MOUNT_PATH/$SUB_DIR
                  date >> $MOUNT_PATH/$SUB_DIR/session.txt
                  sleep infinity
          volumes:
            - name: workspace-volume
              emptyDir: {}
    ---
    apiVersion: extensions.agents.x-k8s.io/v1alpha1
    kind: SandboxWarmPool
    metadata:
      name: late-bind-warmpool
      namespace: default
    spec:
      replicas: 2
      sandboxTemplateRef:
        name: late-bind-template
    

Apply the manifest:
    
    
    kubectl apply -f sandbox-latebind.yaml
    

## Claim a sandbox and dynamically bind storage

  1. Create a claim manifest named `late-bind-claim.yaml` that includes a deletion finalizer (`agent.sandbox/storage-cleanup`):
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxClaim
         metadata:
           name: late-bind-session-1
           namespace: default
           finalizers:
             - agent.sandbox/storage-cleanup
         spec:
           sandboxTemplateRef:
             name: late-bind-template
         

Apply the claim:
         
         kubectl apply -f late-bind-claim.yaml
         

  2. Dynamically provision a volume using a PVC manifest named `agent-volume-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: session-1-pvc
           namespace: default
         spec:
           accessModes: [ReadWriteMany]
           storageClassName: volume-pool-sc
           resources:
             requests:
               storage: 1Gi
         

Apply the PVC:
         
         kubectl apply -f agent-volume-pvc.yaml
         

  3. Retrieve the assigned pod UID, node, and backing PV export details:
         
         POD_NAME=$(kubectl get pods \
           -l extensions.agents.x-k8s.io/claimed-by=late-bind-session-1 \
           -o jsonpath='{.items[0].metadata.name}')
         POD_UID=$(kubectl get pod "${POD_NAME}" -o jsonpath='{.metadata.uid}')
         NODE_NAME=$(kubectl get pod "${POD_NAME}" -o jsonpath='{.spec.nodeName}')
         PV_NAME=$(kubectl get pvc session-1-pvc -o jsonpath='{.spec.volumeName}')
         NFS_IP=$(kubectl get pv "${PV_NAME}" \
           -o jsonpath='{.spec.csi.volumeAttributes.ip}')
         NFS_PATH="/$(kubectl get pv "${PV_NAME}" \
           -o jsonpath='{.spec.csi.volumeAttributes.volume}')"
         

  4. Send the mount signal to the node daemon on the pod host:
         
         DAEMON_POD=$(kubectl get pods -l app=storage-node-daemon \
           --field-selector spec.nodeName="${NODE_NAME}" \
           -o jsonpath='{.items[0].metadata.name}')
         kubectl exec "${DAEMON_POD}" -c daemon -- python3 -c "
         import urllib.request, json
         payload = json.dumps({
             'action': 'bind_nfs',
             'pod_uid': '${POD_UID}',
             'volume_name': 'workspace-volume',
             'sub_dir': 'user_data',
             'nfs_server': '${NFS_IP}',
             'nfs_path': '${NFS_PATH}'
         }).encode()
         req = urllib.request.Request(
             'http://localhost:9090',
             data=payload,
             headers={'Content-Type': 'application/json'})
         print(urllib.request.urlopen(req).read().decode())
         "
         

  5. Apply a deletion finalizer to the claimed pod to prevent premature cleanup while the host mount is active:
         
         kubectl patch pod "${POD_NAME}" --type=merge \
           -p '{"metadata":{"finalizers":["agent.sandbox/storage-cleanup"]}}'
         

**Caution:** Because host-level mounts bypass standard Kubelet volume tracking, deleting a pod before unmounting its storage causes Kubelet cleanup to fail with a `Device or resource busy` error. Applying finalizers to both the `SandboxClaim` and the `Pod` ensures that your orchestrator can safely unmount storage before Kubernetes deletes the pod.
  6. Verify the volume mount inside the running pod:
         
         kubectl logs "${POD_NAME}" -c agent
         

The output confirms that the volume was mounted successfully:
         
         Waiting for late-bind signal...
         Filestore volume mounted successfully!
         drwxr-xr-x    2 1000     1000          4096 ... user_data
         




## Pause and resume a session

When an agent session concludes or enters hibernation, your orchestrator must unmount the host storage before allowing Kubernetes to terminate or recycle the pod.

  1. Initiate deletion of the `SandboxClaim` in the background. Because of the finalizer, Kubernetes marks the claim for deletion but pauses pod termination:
         
         kubectl delete sandboxclaim late-bind-session-1 --wait=false
         

  2. Unmount the NFS share on the host node:
         
         kubectl exec "${DAEMON_POD}" -c daemon -- python3 -c "
         import urllib.request, json
         payload = json.dumps({
             'action': 'unbind',
             'pod_uid': '${POD_UID}',
             'volume_name': 'workspace-volume',
             'sub_dir': 'user_data'
         }).encode()
         req = urllib.request.Request(
             'http://localhost:9090',
             data=payload,
             headers={'Content-Type': 'application/json'})
         print(urllib.request.urlopen(req).read().decode())
         "
         

  3. Remove the finalizers from both the `SandboxClaim` and the pod to complete termination:
         
         kubectl patch sandboxclaim late-bind-session-1 --type=merge \
           -p '{"metadata":{"finalizers":[]}}'
         kubectl patch pod "${POD_NAME}" --type=merge \
           -p '{"metadata":{"finalizers":[]}}'
         




To resume the session later, claim a new pre-warmed pod and send the bind request using the existing PVC (`session-1-pvc`). The new sandbox pod immediately gains access to the preserved workspace state.

## Production considerations and custom controller design

The manual commands in this document demonstrate the low-level mechanics of dynamic late-binding. To run this architecture reliably in production, you must develop a custom Kubernetes controller or platform orchestrator tailored to your application's session lifecycle.

When designing your production controller and node daemon, implement the following architectural patterns:

### Automate the reconciliation and finalizer lifecycle

Because the storage node daemon performs host-level mounts outside of standard Kubernetes Container Storage Interface (CSI) lifecycle management, Kubelet is unaware of active mounts inside the pod's `emptyDir`. If a pod is deleted while the mount is active, Kubelet fails to remove the `emptyDir` directory and raises a `Device or resource busy` error, leaving the pod stuck in a `Terminating` state.

Your custom controller must automate a strict state machine using finalizers (such as `agent.sandbox/storage-cleanup`):

  1. **Claim creation and binding:**
     * Attach a static finalizer to every `SandboxClaim` upon creation.
     * Watch the Kubernetes API for `SandboxClaim` status updates. When a claim binds to a warm pool pod, extract the assigned `pod_uid`, `nodeName`, and backing Filestore volume attributes.
     * Send an authenticated `bind` request to the storage node daemon running on the target node.
     * Immediately patch the running `Pod` object to add the dynamic finalizer. Because `SandboxTemplate` specifications don't support static pod finalizers, patching the pod dynamically is required to protect the pod during node drains or rescheduling events where the pod is evicted but the `SandboxClaim` remains active.
  2. **Graceful termination and eviction handling:**
     * Watch for `deletionTimestamp` on both `SandboxClaim` and `Pod` resources.
     * When a deletion or eviction is detected, call the node daemon's `unbind` endpoint to cleanly unmount the host directory (`umount -l`).
     * Verify that the unmount succeeded and that all pending writes have flushed before patching the `Pod` and `SandboxClaim` to remove their finalizers. This can help you achieve clean teardown across graceful claim deletions, GKE node upgrades, Spot VM preemptions, and out-of-memory (OOM) kills.



### Secure and harden the storage node daemon

  * **Replace`kubectl exec` with authenticated APIs:** In production, don't use `kubectl exec` or bind the daemon to `localhost`. Configure the storage node daemon to expose a dedicated gRPC or HTTPS endpoint over the cluster network secured with mutual TLS (mTLS) or Kubernetes `ServiceAccount` token authentication.
  * **Isolate daemon namespaces and network access:** Deploy the privileged `storage-node-daemon` `DaemonSet` in a restricted administrative namespace (for example, `sandbox-storage-system`) rather than the `default` or tenant namespaces. Apply Kubernetes `NetworkPolicy` rules that permit ingress to the daemon API exclusively from your custom controller pods and block all traffic from sandboxed agent pods.
  * **Use pre-baked container images:** Avoid installing packages like `nfs-common` at runtime in an `initContainer`. Use a prebuilt, immutable container image with all required mount utilities pre-installed to eliminate node startup delays and external repository dependencies.



### Enforce storage quotas and multi-tenant isolation

  * **Monitor per-agent storage usage:** When you dynamically bind-mount a subdirectory from a shared `ReadWriteMany` (RWX) Filestore volume into an `emptyDir`, standard Kubernetes `emptyDir.sizeLimit` settings can't enforce per-agent storage quotas on the mounted NFS path. To prevent a single runaway agent from exhausting the shared volume and causing a denial of service (DoS), implement directory quota monitoring in your orchestrator or provision dedicated volumes using [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).
  * **Adapt mount payloads for different workspace access modes:** Your controller can support multiple agent storage topologies by varying the parameters sent to the node daemon: 
    * **Private isolated workspaces:** Bind a unique tenant subdirectory or dedicated PVC to a single sandbox pod with read-write permissions.
    * **Collaborative workspaces:** Concurrently bind the same shared RWX subdirectory across multiple coordinating agent pods for real-time file sharing.
    * **Exploration branching workspaces:** Mount a base template directory as read-only (`ro`) so agents can read shared assets without modifying the golden copy, while routing new writes to a separate writable scratch path or copy-on-restore directory.



### Coordinate point-in-time snapshots and cleanup

  * **Achieve write quiescence before snapshots:** To capture consistent point-in-time workspace snapshots without data corruption, your orchestrator should pause active writes by initiating the unbind workflow (or flushing file system buffers) before archiving the workspace directory or triggering a Filestore snapshot.
  * **Automate tenant deprovisioning:** When a user session or workspace expires permanently, ensure your controller first unbinds any active mounts across all nodes before executing asynchronous background tasks to delete the tenant's persistent directories from the backing volume.



For a complete reference implementation showing dynamic finalizer management, multi-tenant isolation, and snapshot restoration workflows, see the [GKE Sandbox late-binding storage example](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/latebind-storage-gke-sandbox) on GitHub.

## What's next

  * Explore static [Agent Sandbox integration](https://docs.cloud.google.com/filestore/docs/agent-sandbox).
  * Deploy self-managed [GKE workloads](https://docs.cloud.google.com/filestore/docs/self-managed-gke).
  * Learn how to create and manage [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
