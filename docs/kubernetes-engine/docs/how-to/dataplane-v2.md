---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2/
title: Using GKE Dataplane V2 \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:59.765883+00:00
---

# Using GKE Dataplane V2  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Using GKE Dataplane V2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to enable and troubleshoot [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) for Google Kubernetes Engine (GKE) clusters.

GKE Dataplane V2 is always enabled in new Autopilot clusters. If you're experiencing issues with using GKE Dataplane V2, skip to [Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#troubleshooting).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

To get the permissions that you need to create a GKE cluster, ask your administrator to grant you the Kubernetes Engine Cluster Admin (`container.clusterAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Creating a GKE cluster with GKE Dataplane V2

You can enable GKE Dataplane V2 only when you create a new GKE cluster. You can't modify this setting for an existing cluster.

**Note:** GKE Dataplane V2 include built-in support for [Kubernetes NetworkPolicy enforcement](https://kubernetes.io/docs/concepts/services-networking/network-policies/). If you try to [enable or disable network policy enforcement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy#enabling_network_policy_enforcement) in a cluster that uses GKE Dataplane V2, then the request fails and GKE returns the error message `Enabling NetworkPolicy for clusters with DatapathProvider=ADVANCED_DATAPATH is not allowed`.

To create a Standard cluster that uses GKE Dataplane V2, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the navigation menu, click **Networking**.

  3. Expand the **Container Network Interface (CNI)** section.

  4. Select the **Dataplane V2** checkbox.

  5. Click **Create**.




### gcloud

Run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-dataplane-v2
    

Replace the following:

  * `CLUSTER_NAME`: a name for your new cluster.
  * `CONTROL_PLANE_LOCATION`: a [location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster's control plane.



### API

To create a new cluster with GKE Dataplane V2, specify the [`datapathProvider` field](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#datapathprovider) in the [`networkConfig` object](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#networkconfig) in your cluster [`create` request](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/create).

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your project ID.
  * `CONTROL_PLANE_LOCATION`: a [location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster's control plane.
  * `CLUSTER_NAME`: a name for your new cluster.



HTTP method and URL: 
    
    
    POST https://container.googleapis.com/v1/projects/PROJECT_ID/locations/CONTROL_PLANE_LOCATION/clusters

Request JSON body: 
    
    
    {
      "cluster":{
        "name": "CLUSTER_NAME",
        "location": "CONTROL_PLANE_LOCATION",
        "initialNodeCount": 1,
        "networkConfig":{
          "datapathProvider":"ADVANCED_DATAPATH"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://container.googleapis.com/v1/projects/PROJECT_ID/locations/CONTROL_PLANE_LOCATION/clusters"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://container.googleapis.com/v1/projects/PROJECT_ID/locations/CONTROL_PLANE_LOCATION/clusters" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "operation-1234567890",
      "zone": "us-central1-b",
      "operationType": "CREATE_CLUSTER",
      "status": "RUNNING",
      "selfLink": "https://container.googleapis.com/v1/projects/1234567890/zones/us-central1-b/operations/operation-1234567890",
      "targetLink": "https://container.googleapis.com/v1/projects/1234567890/zones/us-central1-b/clusters/example-cluster",
      "startTime": "2026-09-21T14:42:56.222681067Z"
    }
    

## Troubleshooting issues with GKE Dataplane V2

This section shows you how to investigate and resolve issues with GKE Dataplane V2.

  1. Confirm that GKE Dataplane V2 is enabled:
         
         kubectl -n kube-system get pods -l k8s-app=cilium -o wide
         

If GKE Dataplane V2 is running, the output includes Pods with the prefix `anetd-`. anetd is the networking controller for GKE Dataplane V2.

  2. If the issue is with services or network policy enforcement, check the `anetd` Pod logs. Use the following log selectors in Cloud Logging:
         
         resource.type="k8s_container"
         labels."k8s-pod/k8s-app"="cilium"
         resource.labels.cluster_name="CLUSTER_NAME"
         

  3. If Pod creation is failing, check the kubelet logs for clues. Use the following log selectors in Cloud Logging:
         
         resource.type="k8s_node"
         log_name=~".*/logs/kubelet"
         resource.labels.cluster_name="CLUSTER_NAME"
         

Replace `CLUSTER_NAME` with the name of the cluster, or remove it entirely to see logs for all clusters.

  4. If the `anetd` Pods are not running, examine the cilium-config ConfigMap for any modifications. Avoid altering existing fields within this ConfigMap, because such changes can destabilize the cluster and disrupt `anetd`. The ConfigMap gets patched back to the default state only if new fields are added to it. Any changes to existing fields are not patched back, and we recommend not changing or customizing the ConfigMap.




## Known issues

When you use GKE Dataplane V2, you might encounter the following known issues.

### Health check probes originate from `169.254.4.6` in GKE 1.35 and later

In GKE Dataplane V2 clusters running GKE version 1.35.1-gke.1516000 and later, the CNI configuration uses a unified `cilium-cni` plugin instead of chaining `ptp` and `cilium-cni`. With this configuration, Cilium sets the Pod default gateway to the node-local `cilium_host` interface IP address (`169.254.4.6`) rather than the `.1` address of the node's Pod CIDR range (for example, `10.x.x.1`).

By setting the Pod default gateway to the node-local `cilium_host` interface, node-local `kubelet` liveness, readiness, and startup probes (`kube-probe`) and `NodeLocal DNSCache` traffic originate from `169.254.4.6`. Standard Kubernetes `NetworkPolicy` resources automatically permit node-local health probes (`reserved:host`), so you don't need to apply any changes to the `NetworkPolicy` configuration. However, if your applications enforce application-level IP allowlists or web server ACLs on health check endpoints, update those allowlists to permit the `169.254.4.6/32` (or `169.254.0.0/16`) IP address.

### Connection timeouts for not-ready Pods

When a Pod is not ready, connections to the associated Service can time out. This is the expected behavior for GKE Dataplane V2, and it differs from kube-proxy, which can return a faster `connection refused` error.

### Identity-Relevant Label filtering for Cilium Identity doesn't take effect and Pods are stuck in ContainerCreating state

_Affected versions: 1.34, 1.35_

In GKE Dataplane V2 clusters, emergency use of Identity-Relevant Label filtering via `kube-system/cilium-config-emergency-override` ConfigMap is not correctly applied at the affected versions.

This approach limits which Pod labels are used for Cilium Identity generation.

When other mechanisms of preventing/removing high cardinality label key/values from Pods is not available (such as when labels are applied by a tool or framework), Identity-Relevant Label filtering can be used to exclude the label keys from Cilium Identity calculation. For more information about configuring these rules, see [Identity-Relevant Labels](https://docs.cilium.io/en/stable/operations/performance/scalability/identity-relevant-labels/) in the Cilium documentation.

For the affected GKE versions, Cilium identities created by the operator continue to include the excluded labels.

**Symptoms**

  * Pods with labels that should be filtered for Cilium Identity generation might fail to start and get stuck in the `ContainerCreating` state. Pod events might show timeout errors:
        
        {"level":"warning", "msg":"Error changing endpoint identity", "error":"unable to resolve identity: timed out waiting for cilium-operator to allocate CiliumIdentity for key ...;, error: exponential backoff cancelled via context: context canceled", "k8sPodName":"...", "subsys":"endpoint"}
        

  * Instead of sharing identities based on filtered labels, Pods with unique label values continue to generate unique Cilium Identities. This can lead to a sharp increase of identities, potentially exhausting available Cilium Identities (up to a limit of 65,536) and causing scalability issues.




**Fixed versions**

To fix this issue, [upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_manually) to one of the following GKE versions:

  * 1.34.6-gke.1307000 or later
  * 1.35.2-gke.1962000 or later



**Workaround**

As a workaround, apply the label filtering rules to the `data.labels` field in the main `cilium-config` ConfigMap and remove them from `cilium-config-emergency-override`. This situation persists through control plane operations, such as upgrades, because GKE preserves user modifications to fields it does not manage within the `cilium-config` ConfigMap.

  1. Remove the `labels` key from the `data` section of the `cilium-config-emergency-override` ConfigMap if it exists.
  2. Edit the `cilium-config` ConfigMap by adding or modifying the `labels` key in the `data` section. For example, to prevent labels named `uuid` from being used for identity generation:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: cilium-config
           namespace: kube-system
         data:
           # ... other existing keys
           labels: "!uuid"
           # ... other existing keys
         

  3. Restart the `anet-operator` on the control plane by upgrading the control plane to the _same_ version it is running. This forces the operator to restart and reload its configuration:
         
         gcloud container clusters upgrade CLUSTER_NAME \
             --location CLUSTER_LOCATION \
             --project PROJECT_ID \
             --cluster-version $(gcloud container clusters describe CLUSTER_NAME --location CLUSTER_LOCATION --project PROJECT_ID --format="value(currentMasterVersion)") \
             --master
         

  4. After the control plane restarts, restart the `anetd` DaemonSet to ensure node agents also pick up any required changes:
         
         kubectl rollout restart daemonset anetd -n kube-system
         




### Intermittent connectivity issues related to `NodePort` range conflicts in GKE Dataplane V2 clusters

In GKE Dataplane V2 clusters, intermittent connectivity problems can occur for masqueraded traffic or with ephemeral port usage. These problems are due to the potential port conflicts with the reserved `NodePort` range and typically happen in the following scenarios:

  * **Custom`ip-masq-agent`:** If you use a custom `ip-masq-agent` (version 2.10 or later), where the cluster has `NodePort` or Load Balancer services, you might observe intermittent connectivity issues due to their conflict with the `NodePort` range. Since version 2.10 and later, `ip-masq-agent` has the `--random-fully` argument implemented internally by default. To mitigate this, explicitly set `--random-fully=false` (applicable since version 2.11) under arguments in your `ip-masq-agent` configuration. For configuration details, see [Configuring an IP masquerade agent in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

  * **Ephemeral port range overlap:** If the ephemeral port range that's defined by `net.ipv4.ip_local_port_range` on your GKE nodes overlaps with the `NodePort` range (30000-32767), it can also trigger connectivity issues. To prevent this problem, ensure that these two ranges don't overlap.




Review your `ip-masq-agent` configuration and ephemeral port range settings to ensure they don't conflict with the `NodePort` range. If you encounter intermittent connectivity issues, consider these potential causes and adjust your configuration accordingly.

### Connectivity issues with `hostPort` in GKE Dataplane V2 clusters

_Affected GKE versions:_ All available versions

In clusters that use GKE Dataplane V2, you might encounter connectivity failures when traffic targets a node's IP:Port where port is the `hostPort` defined on the Pod. These issues arise in two primary scenarios:

  * **Nodes with`hostPort` behind a passthrough Network Load Balancer:**

`hostPort` ties a Pod to a specific node's port, and a passthrough Network Load Balancer distributes traffic across all nodes. When you expose Pods to the internet using `hostPort` and a passthrough Network Load Balancer, the load balancer might send traffic to a node where the Pod isn't running, causing connection failures. This is due to a known limitation in GKE Dataplane V2 where passthrough Network Load Balancer traffic is not consistently forwarded to `hostPort` Pods.

**Workaround:** When exposing `hostPort`s of a Pod on the node with a passthrough Network Load Balancer, specify the internal or external IP address of the Network Load Balancer in the Pod's `hostIP` field.
        
        ports:
        - containerPort: 62000
          hostPort: 62000
          protocol: TCP
          hostIP: 35.232.62.64
        - containerPort: 60000
          hostPort: 60000
          protocol: TCP
          hostIP: 35.232.62.64
          # Assuming 35.232.62.64 is the external IP address of a passthrough Network Load Balancer.
        

  * **`hostPort` conflict with reserved `NodePort` range:**

If a Pod's `hostPort` conflicts with the reserved `NodePort` range (30000-32767), Cilium might fail to forward traffic to the Pod. This behavior occurs because Cilium manages `hostPort` capabilities, replacing the previous Portmap method. This is an expected behavior for Cilium and is mentioned in their public documentation.




We don't plan to fix these limitations in later versions. The root cause of these issues is related to Cilium's behavior and outside the direct control of GKE.

**Recommendation:** We recommend that you migrate to `NodePort` Services instead of `hostPort` for improved reliability. `NodePort` Services provide similar capabilities.

### Port ranges for network policies don't take effect

_Affected GKE versions:_ earlier than 1.32

If you specify the `endPort` field in a `NetworkPolicy` object on a cluster that has GKE Dataplane V2 enabled and runs a GKE version earlier than 1.32, Kubernetes ignores the field.

The [Kubernetes `NetworkPolicy` API](https://kubernetes.io/docs/concepts/services-networking/network-policies/) lets you specify a range of ports where Kubernetes enforces the network policy. This API is supported in clusters with Calico Network Policy, and in clusters with GKE Dataplane V2 that run GKE version 1.32 or later. The API isn't supported in GKE Dataplane V2 clusters that run versions earlier than 1.32.

To verify the behavior of your `NetworkPolicy` objects, read them back after writing them to the API server. If the object still contains the `endPort` field, Kubernetes enforces the feature. If the `endPort` field is missing, Kubernetes doesn't enforce the feature. The object stored in the API server is the source of truth for the network policy.

For more information, see [KEP-2079: Network Policy to support Port Ranges](https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/2079-network-policy-port-range).

#### Fixed versions

To resolve this issue, [upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) to GKE version 1.32 or later.

### Nodes in `NodeNotReady` state due to missing `containerID` error

When clusters are upgraded to GKE version 1.35.1-gke.1616000 and later, nodes might immediately enter a `NodeNotReady` state if both GKE Dataplane V2 and Cloud Service Mesh are enabled.

**Note:** If you use the in-cluster control plane in Cloud Service Mesh, you must manually upgrade the CNI component to version 1.23 (compatible with CNI spec v1.1.0) before upgrading to GKE version 1.35.

#### Cause

Starting with GKE version 1.35.1-gke.1616000, GKE Dataplane V2 clusters use CNI version 1.1.0 in their CNI configuration files. This change requires downstream CNI plugins, such as Google Managed Istio, to also support CNI version 1.1.0. Because of a delay in the Managed Istio rollout, some clusters have not yet received the compatible version (1.23), leading to the initialization failure.

#### Symptoms

Affected nodes immediately show as `NodeNotReady`. The following error message appears in the containerd logs:
    
    
    NetworkPluginNotReady message:Network plugin returns error: missing containerID
    

#### Workaround

To mitigate the issue, downgrade the impacted cluster to a GKE version earlier than 1.35.1-gke.1616000.

### Custom eBPF programs interference

GKE uses eBPF programs to manage networking for GKE Dataplane V2. If you deploy custom eBPF programs on GKE-managed node network interfaces, these programs can interfere with GKE-managed eBPF programs and cause networking issues.

GKE doesn't support custom eBPF programs attached to the following network interfaces:

  * `eth*`
  * `ens4`
  * `lo`
  * `cilium*`
  * `gke*`
  * `veth*`



The presence of custom eBPF programs on these interfaces can interfere with the GKE Dataplane V2 `anetd` agent-installed programs, which can disrupt cluster networking. We recommend that you remove any custom eBPF programs or workloads that inject such programs from your cluster.

#### Discover custom eBPF programs

To discover custom eBPF programs running on cluster nodes, you can create a DaemonSet configured with the `hostNetwork: true` setting, that uses [bpftool](https://github.com/libbpf/bpftool) to query such eBPF programs:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: bpftool-logger
      labels:
        app: bpftool-logger
    spec:
      selector:
        matchLabels:
          app: bpftool-logger
      template:
        metadata:
          labels:
            app: bpftool-logger
        spec:
          hostPID: true
          hostNetwork: true
          containers:
          - name: bpftool
            image: ubuntu:22.04
            securityContext:
              privileged: true
            env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            command:
            - /bin/bash
            - -c
            - |
              echo "Installing dependencies..."
              apt-get update -y > /dev/null 2>&1
              apt-get install -y curl tar > /dev/null 2>&1
    
              echo "Downloading and setting up bpftool..."
              curl -sL https://github.com/libbpf/bpftool/releases/download/v7.7.0/bpftool-v7.7.0-amd64.tar.gz | tar xz
              chmod +x bpftool
              mv bpftool /usr/local/bin/
    
              echo "========== $(date) | Node: ${NODE_NAME} =========="
              bpftool net | grep -E '^(eth|ens4|lo|cilium|gke|veth)' | grep -v ' cil_'
              sleep infinity
    

  1. Save the manifest as `ebpf-discovery.yaml` and apply the DaemonSet:
         
         kubectl apply -f ebpf-discovery.yaml
         

  2. Wait for the Pods to be running:
         
         kubectl rollout status ds/bpftool-logger
         

  3. Check the logs from the Pods to discover eBPF programs:
         
         kubectl logs -l app=bpftool-logger
         

  4. When you have finished, delete the DaemonSet:
         
         kubectl delete -f ebpf-discovery.yaml
         




## What's next

  * Learn how to [use network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging).
  * Learn how to [control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).
  * Learn more about [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).
  * Learn more about [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).
  * Learn how to [configure GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
