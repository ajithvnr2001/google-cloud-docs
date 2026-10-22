---
url: https://docs.cloud.google.com/kubernetes-engine/networking/docs/known-issues/
title: GKE networking known issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:37.168828+00:00
---

# GKE networking known issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/networking/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  GKE networking known issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page lists known issues for GKE networking. This page is for Admins and architects who manage the lifecycle of the underlying technology infrastructure, and respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail.

To filter the known issues by a product version, select your filters from the following drop-down menus.

Select your GKE version:

1.351.341.331.321.311.301.291.281.27

Or, search for your issue:

Identified version(s) | Fixed version(s) | Issue and workaround  
---|---|---  
1.36 | Fix in progress | 

### Connectivity failures and crash-looping system Pods on Windows nodes that use Layer 4 load balancers

GKE clusters with Windows Server node pools running version 1.36 might experience either of the following: 

  * Outbound network connectivity failures for workloads.
  * Critical system Pods (such as `pdcsi-node-windows` and `gke-metrics-agent-windows`) continuously restarting in a `CrashLoopBackOff` state.

This issue occurs when clusters use Layer 4 internal load balancers without [GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#subsetting), or external passthrough Network Load Balancer using older target pools or instance groups. In GKE 1.36, the Compute Engine Guest Agent enables `CorePlugin` by default on Windows Server and dynamically binds load balancer virtual IP (VIP) addresses directly to the host network adapter (`vEthernet (Ethernet)`) as secondary `/32` addresses. Outbound traffic to the VIP loops back into the host and is dropped, and outbound connections to the GKE control plane (Kubernetes API server) or Google Cloud metadata server (`169.254.169.254`) intermittently select the secondary VIP as the source IP address, causing connection timeouts.  **Workaround:** To mitigate this issue, use one of the following methods:

  * **Enable L4 subsetting (recommended for internal load balancers):** Add the `gke.googleapis.com/subsetting: "true"` annotation to your internal LoadBalancer Service spec, and re-create or perform a rolling restart of the Windows nodes to clear existing secondary IP addresses: 
        
        apiVersion: v1
        kind: Service
        metadata:
          name: SERVICE_NAME
          annotations:
            cloud.google.com/load-balancer-type: "Internal"
            gke.googleapis.com/subsetting: "true"
        spec:
          type: LoadBalancer
                

  * **Use backend service-based external load balancers:** For external load balancing, migrate older target-pool-based services to [backend service-based external load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer). 
  * **Disable Guest Agent IP address forwarding by using a node startup script:** Use a custom node startup script that adds the `ip_forwarding = false` key-value pair under the `[NetworkInterfaces]` section in the `C:\Program Files\Google\Compute Engine\instance_configs.cfg` file, and then restarts the `GCEGuestAgent` service: 
        
        $configFile = "C:\Program Files\Google\Compute Engine\instance_configs.cfg"
        if (Test-Path $configFile) {
            Add-Content -Path $configFile -Value "`r`n[NetworkInterfaces]`r`nip_forwarding = false"
            Restart-Service -Name GCEGuestAgent -Force
        }
                

  * **Postpone Windows node pool upgrades:** Keep Windows node pools on GKE 1.34 or 1.35 until the fixed Windows node image is available. 

  
InferencePool Helm chart v1.1.0 |  | 

### InferencePool targetPortNumber flag ignored

In version `v1.1.0` of the `InferencePool` Helm chart, the `--set inferencePool.targetPortNumber` flag might be ignored, and the target port number defaults to `8000`. This default port number causes routing issues if your model server listens on a different port, such as `30000` for SGLang.   
**Workaround:** Verify the port after installation:
    
    
    kubectl get inferencepool POOL_NAME -o jsonpath='{.spec.targetPorts}' \
        --context=CLUSTER_CONTEXT
        

If the port is incorrect, patch the `InferencePool` custom resource before you export it:
    
    
    kubectl patch inferencepool POOL_NAME --type=merge \
        -p '{"spec":{"targetPorts":[{"number":TARGET_PORT}]}}' \
        --context=CLUSTER_CONTEXT
          
  
1.33, 1.34, 1.35 | 

  * 1.33.11-gke.1137000 or later
  * 1.34.6-gke.1154000 or later
  * 1.35.0-gke.3047000 or later

| 

### Intermittent Pod connectivity or DNS failures due to `CiliumEndpoint` deletion

Clusters with GKE Dataplane V2 enabled might experience intermittent connectivity failures or DNS resolution issues for running Pods. This issue is caused by a race condition during the `cilium-agent` (`anetd`) startup process. When the `cilium-agent` is temporarily unavailable, the `cilium-cni` plugin might queue endpoint deletion requests for existing Pods. If the agent processes these stale deletion events after it successfully initializes or re-creates the Pod's endpoint, the agent incorrectly deletes the active `CiliumEndpoint`. Consequently, the affected Pod loses its network identity and routing configuration, causing its traffic to be dropped. This issue often manifests as DNS failures because the eBPF `ipcache` incorrectly identifies the destination as unmanaged. Affected Pods might enter a `CrashLoopBackOff` state.   
**Workaround:** To mitigate this issue, manually delete the affected Pod or restart the `anetd` Pod on the node where the issue occurs. Doing so forces the re-creation of the missing `CiliumEndpoint` and restores connectivity. **Resolution:** The fix is included in `advanceddatapath` component version `33.7.36` or later. To resolve this issue, upgrade your cluster to one of the versions listed in the **Fixed version(s)** column.  
1.29, 1.30, 1.31, 1.32, 1.33 | 1.34 | 

### The `cilium-agent` container within the anetd Pod crash after deleting a FQDN network policy

Clusters with GKE Dataplane V2 enabled might experience a momentary `cilium-agent` containers crash, leading to longer reconciliation time for events that must be programmed in the data plane. This issue is caused by a nil pointer dereference upon FQDN Network Policy deletion. The issue is triggered by the deletion of a FQDN network policy. When the issue occurs, the Cilium-agent container within the anetd Pods return an error message similar to the following: `panic: runtime error: invalid memory address or nil pointer dereference [signal SIGSEGV: segmentation violation code=0x1 addr=0x20 pc=0x33e237d]`   
**Workaround:** To mitigate this issue, instead of deleting a FQDN policy, you can patch it to not have any effect by making sure no Pods are subject to it:
    
    
          kubectl patch fqdnnetpol -n namespace policy-name --patch '
          spec:
            podSelector:
              matchLabels:
                miss: me
          '
        

**Resolution** Upgrade the cluster version to the 1.34 version  
1.28, 1.29, 1.30, 1.31, 1.32, 1.33 |  | 

### Pod IP address leak on nodes with GKE Dataplane V2

Clusters with GKE Dataplane V2 enabled might experience Pod IP address exhaustion on nodes. This issue is caused by a container runtime bug that can leak allocated IP addresses when Pods hit transient CNI errors during creation. The issue is triggered when the GKE cluster node is upgraded to or created with one of the following GKE versions: 

  * 1.33 and later
  * 1.32 and later
  * 1.31.2-gke.1115000 or later
  * 1.30.8-gke.1051001 or later
  * 1.29.10-gke.1059000 or later
  * 1.28.15-gke.1024000 or later

When this issue occurs, new Pods that are scheduled on the affected node fail to start and return an error message similar to the following: `failed to assign an IP address to container`.   
**Workaround:** To mitigate this issue, you can apply the mitigation DaemonSet to the cluster to clean up the leaked IP resources:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: cleanup-ipam-dir
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          name: cleanup-ipam
      template:
        metadata:
          labels:
            name: cleanup-ipam
        spec:
          hostNetwork: true
          securityContext:
            runAsUser: 0
            runAsGroup: 0
            seccompProfile:
              type: RuntimeDefault
          automountServiceAccountToken: false
          containers:
          - name: cleanup-ipam
            image: gcr.io/gke-networking-test-images/ubuntu-test:2022@sha256:6cfbdf42ccaa85ec93146263b6e4c60ebae78951bd732469bca303e7ebddd85e
            command:
            - /bin/bash
            - -c
            - |
              while true; do
              for hash in $(find /hostipam -iregex '/hostipam/[0-9].*' -mmin +10 -exec head -n1 {} \; ); do
              hash="${hash%%[[:space:]]}"
              if [ -z $(ctr -n k8s.io c ls | grep $hash | awk '{print $1}') ]; then
              grep -ilr $hash /hostipam
              fi
              done | xargs -r rm
              echo "Done cleaning up /var/lib/cni/networks/gke-pod-network at $(date)"
              sleep 120s
              done
            volumeMounts:
            - name: host-ipam
              mountPath: /hostipam
            - name: host-ctr
              mountPath: /run/containerd
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop:
                - ALL
          volumes:
          - name: host-ipam
            hostPath:
              path: /var/lib/cni/networks/gke-pod-network
          - name: host-ctr
            hostPath:
              path: /run/containerd  
  
1.31, 1.32, 1.33 | 

  * 1.33.1-gke.1107000 and later
  * 1.32.8-gke.1108000 and later

| 

### Ingress and Service load balancers outages on clusters with a legacy network

An incompatibility with [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) causes the backends of a GKE-managed load balancer deployed using Ingress or Service to be detached. This results in the load balancer having no active backends, which in turn leads to all incoming requests to those load balancers getting dropped.  The issue impacts GKE clusters which use a legacy network and are on version 1.31 or later.  To identify GKE clusters with a legacy network, run the following command: 
    
    
        gcloud container clusters describe CLUSTER_NAME --location=LOCATION --format="value(subnetwork)"
      

A cluster with a legacy network will get an empty output for this command.  **Workaround:** As legacy networks have been deprecated for some time, the preferred solution is to migrate your legacy network to a VPC network. You can do this by [converting a legacy network that contains GKE clusters](https://docs.cloud.google.com/vpc/docs/using-legacy#convert-network-gke). If you are unable to perform this migration at this time, reach out to Cloud Customer Care.   
1.30, 1.31, 1.32 | 

  * 1.30.10-gke.1070000 and later
  * 1.31.5-gke.1068000 and later
  * 1.32.1-gke.1002000 and later

| 

### Newly created nodes are not added to the layer 4 internal load balancers

Google Cloud load balancers that are created for internal LoadBalancer Services might miss newly created nodes in the backend instance group.  The issue will be most visible on a cluster that was scaled to zero nodes and then scaled back to one or more nodes.  **Workarounds:**

  * [Turn on GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#subsetting) and recreate the Service. **Note** : GKE subsetting can't be turned off after it is turned on.
  * Create another internal LoadBalancing Service. When it syncs, the instance group will also be fixed for the affected Service. The new Service can be removed after the sync. 
  * Add and then remove the [node.kubernetes.io/exclude-from-external-load-balancers](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-exclude-from-external-load-balancers) label from one of the nodes. 
  * Add a node to the cluster. You can remove the node after the Service starts functioning. 

  
1.31,1.32 | 

  * 1.31.7-gke.1158000 and later
  * 1.32.3-gke.1499000 and later

| 

### Gateway API issues due to storedVersions removed from CRD status

The Kube-Addon-Manager in GKE incorrectly removes the `v1alpha2` `storedVersion` from the status of Gateway API CRDs like `gateway`, `httpRoute`, `gatewayClass`, and `referenceGrant`. This problem occurs even when the cluster still has instances of those CRDs stored in the `v1alpha2` format. If the GKE cluster version is upgraded without the `storedVersions`, the Gateway API calls fail. The failed calls might also break controllers that implement Gateway API.  Your cluster may be at risk if it meets all of the following conditions: 

  * The Gateway API is enabled on your cluster.
  * You have, at any point in the past, installed a `v1alpha2` version of a Gateway API CRD.
  * Your cluster has been running on an affected GKE version.

**Workaround:** The recommended workaround is to delay cluster upgrades until the issue is resolved.  Alternatively, if you need to upgrade the cluster version, you must update the storage version for all affected Gateway API CRDs to `v1beta1`. The following example updates the `gatewayClass` CRD: 

  1. Check for the presence the of `v1alpha2` storage version: 
         
         kubectl get crd gatewayclasses.gateway.networking.k8s.io -ojsonpath="{.status.storedVersions}"

  2. Adjust the storage version to `v1beta1` by running the following on all GatewayClass resources present on the cluster: 
         
         kubectl annotate gatewayclass gateway-class-name bump-storage-version="yes"

  3. Remove the `v1alpha2` storage version and set the storage version to `v1beta1`: 
         
         kubectl patch customresourcedefinitions gatewayclasses.gateway.networking.k8s.io --subresource='status' --type='merge' -p '{"status":{"storedVersions":["v1beta1"]}}'

  4. Perform the upgrade as usual. 

  
1.32 | 

  * 1.32.3-gke.1170000 and later

| 

### New Pods failing to initialize stuck on ContainerCreating

New Pods fail to be created and are stuck in the `ContainerCreating` state. When this issue happens, the service container logs the following: 
    
    
    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "[sandbox-ID]": plugin type="cilium-cni" failed (add): unable to create endpoint: Cilium API client timeout exceeded

The issue impacts GKE clusters in versions between 1.32 and before 1.32.3-gke.1170000, that were created at GKE versions 1.31 or 1.32. The root cause is that an in-memory data structure that maintained a collection of allocated Cilium identities was not correctly synchronized with the Kubernetes API server state.  To confirm the GKE version that was used to create the cluster, you can query the `initialClusterVersion` resource by using the following command: 
    
    
      gcloud container clusters describe [cluster_name] --location [location] --format='value(initialClusterVersion)'
      

If the GKE cluster has logging enabled, the `cilium-agent` container logs the `unable to resolve identity: timed out waiting for cilium-operator to allocate CiliumIdentity for key` message in Logs Explorer by using the following query: 
    
    
       resource.type="k8s_container"
       resource.labels.container_name="cilium-agent"
      

**Workaround:** A temporary mitigation is to restart the control plane. This can be achieved by upgrading the control plane to the same version it is already running: 
    
    
      gcloud container clusters upgrade [cluster_name] --location [location] --cluster-version=[version] --master
        
  
1.27,1.28,1.29,1.30,1.31 |  | 

### NEG Controller stops managing endpoints when port removed from Service

When the NEG controller is configured to create a [Standalone NEG](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg) for a Service and one of the configured ports is later removed from the Service, the NEG controller will eventually stop managing endpoints for the NEG. In addition to Services where the user creates a Standalone NEG annotation, this also affects Services which are referenced by GKE Gateway, MCI, and GKE Multi Cluster Gateway.  **Workaround:** When removing a port from a Service with a Standalone NEG annotation, the annotation needs to also be updated to remove the port in question.   
1.28 |  | 

### Gateway TLS configuration error

We've identified an issue with configuring TLS for Gateways in clusters running GKE version 1.28.4-gke.1083000. This affects TLS configurations using either an [SSLCertificate](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-ssl-certificate) or a [CertificateMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager). If you're upgrading a cluster with existing Gateways, updates made to the Gateway will fail. For new Gateways, the load balancers won't be provisioned. This issue will be fixed in an upcoming GKE 1.28 patch version.   
1.27,1.28,1.29 | 

  * 1.26.13-gke.1052000 and later
  * 1.27.10-gke.1055000 and later
  * 1.28.6-gke.1095000 and later
  * 1.29.1-gke.1016000 and later

| 

### Intermittent connection establishment failures

Clusters on control plane versions 1.26.6-gke.1900 and later might encounter intermittent connection establishment failures.  The chances of failures are low and it doesn't affect all clusters. The failures should stop completely after a few days since the symptom onset.   
1.27,1.28,1.29 | 

  * 1.27.11-gke.1118000 or later
  * 1.28.7-gke.1100000 or later
  * 1.29.2-gke.1217000 or later

| 

### DNS resolution issues with Container-Optimized OS

Workloads running on GKE clusters with Container-Optimized OS-based nodes might experience DNS resolution issues.   
1.28 | 1.28.3-gke.1090000 or later | 

### Network Policy drops a connection due to incorrect connection tracking lookup

For clusters with GKE Dataplane V2 enabled, when a client Pod connects to itself using a Service or the virtual IP address of an internal passthrough Network Load Balancer, the reply packet is not identified as a part of an existing connection due to incorrect conntrack lookup in the dataplane. This means that a Network Policy that restricts ingress traffic for the Pod is incorrectly enforced on the packet.  The impact of this issue depends on the number of configured Pods for the Service. For example, if the Service has 1 backend Pod, the connection always fails. If the Service has 2 backend Pods, the connection fails 50% of the time.  **Workaround:** You can mitigate this issue by configuring the `port` and `containerPort` in the Service manifest to be the same value.   
1.27,1.28 | 

  * 1.28.3-gke.1090000 or later
  * 1.27.11-gke.1097000 or later

| 

### Packet drops for hairpin connection flows

For clusters with GKE Dataplane V2 enabled, when a Pod creates a TCP connection to itself using a Service, such that the Pod is both the source and destination of the connection, GKE Dataplane V2 eBPF connection tracking incorrectly tracks the connection states, leading to leaked conntrack entries.  When a connection tuple (protocol, source/destination IP, and source/destination port) has been leaked, new connections using the same connection tuple might result in return packets being dropped.  **Workaround:** Use one of the following workarounds:

  * Enable TCP reuse (keep-alives) for an application running in a Pod that might communicate with itself using a Service. This prevents the TCP FIN flag from being issued and avoids leaking the conntrack entry. 
  * When using short-lived connections, expose the Pod using a proxy load balancer, such as Gateway, to expose the Service. This results in the destination of the connection request being set to the load balancer IP address, preventing GKE Dataplane V2 from performing SNAT to the loopback IP address. 

  
Earlier than 1.31.0-gke.1506000 | 1.31.0-gke.1506000 and later | 

### Device typed network in GKE multi-network fails with long network names

Cluster creation fails with the following error: `error starting very-long-string-that-exceeds-character-limit-gpu-nic0 device plugin endpoint: listen unix /var/lib/kubelet/plugins_registry/networking.gke.io.networks_very-long-string-that-exceeds-character-limit-gpu-nic0.sock: bind: invalid argument` **Workaround:** Limit the length of device-typed network object names to 41 characters or less. The full path of each UNIX domain socket is composed, including the corresponding network name. Linux has a limitation on socket path lengths (under 107 bytes). After accounting for the directory, filename prefix, and the `.sock` extension, the network name is limited to a maximum of 41 characters.  
1.27, 1.28, 1.29, 1.30 | 

  * 1.30.4-gke.1282000 or later
  * 1.29.8-gke.1157000 or later
  * 1.28.13-gke.1078000 or later
  * 1.27.16-gke.1342000 or later

| 

### Connectivity issues for `hostPort` Pods after control plane upgrade

Clusters with [network policy enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) might experience connectivity issues with [hostPort](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#container-v1-core) Pods. Additionally, newly created Pods might take an additional 30 to 60 seconds to be ready.  The issue is triggered when the GKE control plane of a cluster is upgraded to one of the following GKE versions 

  * 1.30 to 1.30.4-gke.1281999
  * 1.29.1-gke.1545000 to 1.29.8-gke.1156999
  * 1.28.7-gke.1042000 to 1.28.13-gke.1077999
  * 1.27.12-gke.1107000 to 1.27.16-gke.1341999

**Workaround:** Upgrade or recreate nodes immediately after the GKE control plane upgrade.  
1.31, 1.32 | 

  * 1.32.1-gke.1729000 or later
  * 1.31.6-gke.1020000 or later

| 

### Broken UDP traffic between Pods that run on the same node

Clusters with [intra-node visibility enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) might experience broken UDP traffic between Pods that run on the same node.  The issue is triggered when the GKE cluster node is upgraded to or created with one of the following GKE versions: 

  * 1.32.1-gke.1729000 or later
  * 1.31.6-gke.1020000 or later

The impacted path is Pod-to-Pod UDP traffic on the same node through Hostport or Service. **Resolution** Upgrade the cluster to one of the following fixed versions:

  * 1.32.3-gke.1927000 or later
  * 1.31.7-gke.1390000 or later

  
1.28, 1.29, 1.30, 1.31 |  | 

### Calico Pods not healthy on clusters with less than 3 total nodes and insufficient vCPU

Calico-typha and calico-node Pods can't be scheduled on clusters meeting all of the following conditions: fewer than 3 nodes total, each node having 1 or fewer allocatable vCPUs, and [network policy enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) enabled. This is due to insufficient CPU resources.  **Workarounds:**

  * Scale to a minimum of 3 node pools with 1 node using 1 allocatable vCPU.
  * Resize a single node pool to a minimum of 3 nodes with 1 allocatable vCPU.
  * Use a machine-type with at least 2 allocatable vCPU on a node pool with a single node.

  
|  | 

### Multi-Cluster Gateway (MCG) outages on zonal clusters during control plane upgrades

Deployments using Multi-Cluster Gateway (MCG) on GKE zonal clusters may experience outages with `503` errors during events that cause a control plane restart, such as a cluster upgrade. This occurs because MCG relies on a legacy mechanism for Network Endpoint Group (NEG) discovery that incorrectly reports zero backends when nodes in a zonal cluster become temporarily unavailable during the control plane restart. This causes the load balancer to remove all backends, resulting in traffic loss.  **Workarounds:**

  * The recommended solution is to migrate from zonal GKE cluster to regional GKE cluster. Regional clusters have a highly available control plane, which eliminates the single point of failure that triggers this issue during upgrades or restarts.

  
|  | 

### NEG readiness gate race condition

Under certain conditions the readiness gates may return a ready state "false positive", before the ingress health check reports a healthy state, generating error events like the following on the Ingress object: `NEG is not attached to any BackendService with health checking. Marking condition "cloud.google.com/load-balancer-neg-ready" to True.` This issue causes the Load Balancer to report a `503` error (`failed_to_pick_backend`) to traffic while GKE is performing the rolling update on the deployment workload. Having a relatively small number of Pods (for example, 2) compared to the number of NEGs will increase the risk of this race condition. NEGs are created for each region, with one NEG per zone, which typically results in three NEGs. If there is a relatively larger number of Pods, such that each NEG always has multiple Pods before the rolling update starts, this race condition is very unlikely to be triggered. **Workaround:** The best way to prevent this race condition is to have more backends in the Network Endpoint Group. Ensure that the rolling update strategy is configured to ensure that at least 1 Pod is always running. For example if only 2 Pods run normally, an example configuration could look like this:
    
    
    strategy:
       type: RollingUpdate
       rollingUpdate:
         maxUnavailable: 0
         maxSurge: 1
        

The previous example is a suggestion. You must update the strategy based on several factors, such as the number of replicas.  
|  | 

### Incomplete garbage collection of container-native load balancers

GKE garbage collects container-native load balancers every two minutes. If a cluster is deleted before load balancers are fully removed, you need to manually delete the load balancer's NEGs. **Workaround:** View the NEGs in your project by running the following command:
    
    
    gcloud compute network-endpoint-groups list

In the command output, look for the relevant NEGs. To delete a NEG, run the following command, replacing `<var>NEG_NAME</var>` with the name of the NEG:
    
    
    gcloud compute network-endpoint-groups delete <var>NEG_NAME</var>  
  
|  | 

### Align workload rollouts with endpoint propagation

This issue does not occur in clusters that use Pod readiness feedback to manage workload rollouts. When you deploy a workload to your cluster, or when you update an existing workload, the container-native load balancer can take longer to propagate new endpoints than it takes to finish the workload rollout.   
**Workaround:** Configure your workloads' `minReadySeconds` and `terminationGracePeriodSeconds` values to be 60 seconds or higher to ensure that the service is not disrupted due to workload rollouts.

  * `terminationGracePeriodSeconds` allows the Pod to shut down gracefully by waiting for connections to terminate after a Pod is scheduled for deletion.
  * `minReadySeconds` adds a latency period after a Pod is created.

  
|  | 

### initialDelaySeconds in Pod readinessProbe not respected

You might expect the `initialDelaySeconds` configuration in the Pod's `readinessProbe` to be respected by the container-native load balancer; however, `readinessProbe` is implemented by kubelet, and the `initialDelaySeconds` configuration controls the kubelet health check, not the container-native load balancer. Container-native load balancing has its own load balancing health check.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
