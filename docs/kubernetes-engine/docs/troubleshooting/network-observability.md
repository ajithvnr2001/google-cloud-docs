---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability/
title: Troubleshoot GKE network observability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:57.044420+00:00
---

# Troubleshoot GKE network observability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot GKE network observability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides instructions and diagnostic procedures for diagnosing networking issues in Google Kubernetes Engine (GKE) clusters using GKE Dataplane V2 observability, Hubble, and Cloud Monitoring.

For an architectural overview and conceptual best practices, see [Best practices for network observability](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/network-observability).

## Troubleshooting decision tree and core concepts

Before reviewing the procedures, use the following decision matrix to identify which tier of the GKE networking stack is likely causing your issue, and navigate to the corresponding section.

Symptom or diagnostic question | Suspected tier | Recommended procedure  
---|---|---  
Pods fail to resolve external domains or internal Kubernetes Services (DNS timeouts, `NXDOMAIN`, `SERVFAIL`). | Tier 1: Pod and Service (DNS) | Diagnose DNS resolution failures  
Services cannot communicate; connection timeouts or dropped packets between Pods. | Tier 1: Pod and Service (Policy or packet drops) | Diagnose packet drops and NetworkPolicy blocks  
Workload replicas have uneven traffic load, or Pods log high rates of TCP resets (`RST`). | Tier 1: Pod and Service (Load balancing or transport) | Diagnose traffic imbalance and TCP resets  
General latency, intermittent timeouts, or CNI restarts across nodes. | Tier 2: Node and CNI (Kernel) | Triage for node-level latency and CNI bottlenecks  
Pods cannot reach resources outside GKE (Cloud SQL, external APIs, or other VPCs). | Tier 3: VPC and routing | Isolate GKE versus VPC or external connectivity issues  
Need automated path simulation to verify whether firewall rules, routes, or NetworkPolicies block traffic. | Tier 3: VPC and routing (Simulation) | Diagnose connectivity using Connectivity Tests  
Need to identify which workloads send traffic to the internet and undergo NAT. | Tier 4: External gateway and cost | Identify NAT traffic (egress to internet)  
High inter-zone data transfer costs or need to visualize top talkers without writing SQL queries. | Tier 4: External gateway and cost | Analyze cluster traffic costs and performance using Flow Analyzer  
  
### Core networking concepts

If you are new to Kubernetes or Google Cloud networking, keep these core concepts in mind:

  * **eBPF (Extended Berkeley Packet Filter):** an operating system technology that allows running secure monitoring and routing programs directly inside the Linux kernel. GKE Dataplane V2 uses eBPF to route packets and enforce NetworkPolicies with minimal performance overhead.
  * **IP masquerading (SNAT):** the process of rewriting the source IP address of a packet. When a GKE Pod (which has a private IP address) communicates with the internet or external VPC resources, GKE masquerades (rewrites) the Pod IP address to the node IP address so external systems know how to route the reply.
  * **Connection tracking (Conntrack):** a kernel feature that tracks all active network connections. In GKE Dataplane V2 clusters, this tracking is split between two tables: the standard Linux kernel conntrack (used by the `ip-masq-agent`) and a Cilium and GKE Dataplane V2-managed conntrack table stored in an eBPF map. If a node handles too many concurrent connections, either of these tracking tables can fill up (conntrack exhaustion), causing the node to silently drop new packets.
  * **Hubble:** the observability engine for GKE Dataplane V2. It runs on top of eBPF and provides real-time visibility into traffic flows, packet drops, and NetworkPolicy evaluation.



## Tier 1: Pod and Service (Application) observability

The Pod and Service tier covers network communication between Pods, Services, and cluster DNS. Issues at this tier typically manifest as application connection timeouts, name resolution failures, or uneven load distribution.

### Diagnose DNS resolution failures

Review the diagnostic scope and prerequisites before troubleshooting DNS issues:

  * **Focus area:** communication between Pods and CoreDNS or NodeLocal DNSCache, DNS latency, upstream DNS resolution timeouts, and FQDN NetworkPolicy validation.
  * **Prerequisites:** GKE Dataplane V2 metrics enabled; `kubectl` access.
  * **CNI compatibility:** GKE Dataplane V2 (Advanced Datapath) and standard GKE CNI.
  * **Symptom:** Pods log `dial tcp: lookup <domain>: i/o timeout`, `NXDOMAIN`, or intermittent latency on outbound API calls.
  * **Goal:** determine whether the DNS failure originates inside the cluster (`kube-dns` or NodeLocal DNSCache saturation), a NetworkPolicy blocking UDP or TCP port 53, or upstream network degradation.



#### Step 1: Basic reachability check

Before troubleshooting DNS layers, verify whether the destination is reachable directly by using its IP address from inside the affected Pod:
    
    
    # 1. Test raw IP reachability (bypasses DNS entirely)
    kubectl exec -it my-pod -n default -- curl -v --connect-timeout 5 http://10.240.0.10:8080
    
    # 2. Test domain resolution
    kubectl exec -it my-pod -n default -- curl -v --connect-timeout 5 http://my-service.default.svc.cluster.local:8080
    

  * **If IP connection succeeds but domain fails:** the issue is isolated to the DNS resolution layer. Proceed to Step 2.
  * **If both fail:** the issue is network-level routing or policy enforcement. Proceed to Diagnose packet drops and NetworkPolicy blocks.



##### Check for FQDN NetworkPolicy DNS pre-population

If your cluster uses FQDN-based NetworkPolicies (`FQDNNetworkPolicy`), verify that the domain name is explicitly permitted. If a Pod queries an external domain that is not pre-populated in the GKE Dataplane V2 DNS proxy cache or allowed by policy, GKE Dataplane V2 blocks egress traffic to the resolved IP address:
    
    
    # Verify whether UDP or TCP port 53 egress is permitted in the Pod's namespace
    kubectl get networkpolicy -n default -o yaml | grep -A 5 -B 2 "port: 53"
    

#### Step 2: Check DNS metrics in Cloud Monitoring

GKE exposes built-in DNS metrics in Cloud Monitoring under the `kubernetes.io/networking/dns/` prefix.

**Important:** If your cluster uses Cloud DNS for GKE, DNS queries don't traverse `kube-dns` or NodeLocal DNSCache Pods. These `kube-dns` metrics remain flat. Refer to the Cloud DNS documentation for DNS query troubleshooting in that mode.

To check DNS metrics in Cloud Monitoring, do the following:

  1. In the Google Cloud console, navigate to **Cloud Monitoring > Dashboards**.
  2. Select the predefined **GKE DNS Observability - Cluster View** dashboard (or navigate to **Metrics Explorer** and filter for `kubernetes.io/networking/dns/`).
  3. Evaluate the following primary signals (for NodeLocal DNSCache, replace `kubedns` with `node_local_dns` in the metric path):

Metric name | Warning threshold | Root cause  
---|---|---  
`kubernetes.io/networking/dns/kubedns/max_concurrent_rejected_request_count` | > 0 | Concurrent query limit reached. `kube-dns` or NodeLocal DNSCache is dropping queries.  
`kubernetes.io/networking/dns/kubedns/dns_request_latencies` | p99 > 100ms | High end-to-end DNS resolution latency across `kube-dns` or NodeLocal DNSCache.  
`kubernetes.io/networking/dns/kubedns/forwarding_request_latencies` | p99 > 100ms | Upstream DNS server latency or saturation.  
  
##### DNS performance and timeout triage sequence

Follow this triage sequence to diagnose DNS latency, cache misses, and upstream timeouts:

  1. **Check cache hit ratio:** query `kubernetes.io/networking/dns/kubedns/dns_cache_request_count` (or `node_local_dns/dns_cache_request_count`) grouped by the `cache_status` label. If `cache_status="hit"` is low and `cache_status="miss"` is high, applications might be issuing non-FQDN queries (such as `my-service` instead of `my-service.default.svc.cluster.local`), causing search path traversal across all entries in `/etc/resolv.conf`.
  2. **Evaluate upstream latency:** high `forwarding_request_latencies` indicates issues with the upstream DNS server (for example, corporate on-premises DNS reached over Cloud Interconnect or Cloud VPN, or Cloud DNS limits).
  3. **Audit custom DNS overrides:** inspect custom `kube-dns` ConfigMaps for misconfigured stubs or upstream forwards:
         
         kubectl get configmap kube-dns -n kube-system -o yaml
         




#### Step 3: Stream live DNS traffic with Hubble CLI

Use the Hubble CLI helper alias to inspect live DNS requests and responses streamed from the node kernel:
    
    
    # 1. Ensure the helper alias is set in your terminal session
    alias gke-hubble="kubectl exec -it -n gke-managed-dpv2-observability deployment/hubble-relay -c hubble-cli -- hubble"
    
    # 2. Observe live DNS (Port 53) traffic for a specific Pod
    gke-hubble observe --pod default/my-pod --port 53
    

**Note:** Hubble CLI parses DNS headers at the application layer (OSI Layer 7). In the flow output, look for the `DNS Query` and `DNS Answer` fields. If the query displays `RCODE: NXDOMAIN` or `RCODE: SERVFAIL`, the DNS server is rejecting or unable to resolve the record.

#### Step 4: Validate the fix

If concurrent query rejections occurred, apply NodeLocal DNSCache to absorb high-frequency DNS lookups directly on the node without hitting cluster-wide `kube-dns` limits:
    
    
    # Verify NodeLocal DNSCache DaemonSet is running
    kubectl get daemonset node-local-dns -n kube-system
    

* * *

### Diagnose packet drops and NetworkPolicy blocks

Review the diagnostic scope and prerequisites before investigating packet drops and policy denials:

  * **Focus area:** traffic drops between Pod objects or between Pod and Service objects, NetworkPolicy enforcement, kernel eBPF drop reasons.
  * **Prerequisites:** GKE Dataplane V2 Flow Observability enabled; NetworkPolicy logging configured.
  * **CNI compatibility:** GKE Dataplane V2 only.
  * **Symptom:** application connection attempts fail with `Connection timed out` or `Connection reset by peer`.
  * **Goal:** pinpoint the exact NetworkPolicy or eBPF reason dropping packets without trial-and-error changes to security policies.



#### Step 1: Monitor Hubble drop metrics

When GKE Dataplane V2 drops a packet, it emits the metric `hubble_drop_total` tagged with the drop reason and source and destination metadata. To monitor Hubble drop metrics, do the following:

  1. If not already configured, deploy a Google Cloud Managed Service for Prometheus `PodMonitoring` resource to scrape Hubble metrics:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: hubble-metrics
           namespace: gke-managed-dpv2-observability
         spec:
           selector:
             matchLabels:
               k8s-app: cilium
           endpoints:
           - port: hubble-metrics
             interval: 30s
         

  2. Run the following query in **Cloud Monitoring > Metrics Explorer** to view drops by reason:
         
         sum by (reason) (rate(hubble_drop_total[5m])) > 0
         

  3. Interpret the common `reason` codes:

     * `Policy denied`: a Kubernetes NetworkPolicy is explicitly or implicitly blocking the connection.
     * `CT: Map insertion failed`: the connection tracking (conntrack) table is exhausted.
     * `Unsupported L3 protocol`: non-IPv4 or IPv6 packet or corrupted header.



#### Step 2: Check NetworkPolicy logs in Cloud Logging

NetworkPolicy logging exports structured JSON logs for all policy decisions. To query NetworkPolicy logs in Cloud Logging, do the following:

  1. In the Google Cloud console, navigate to **Cloud Logging > Logs Explorer**.
  2. Run the following query:
         
         resource.type="k8s_node"
         log_name:"projects/PROJECT_ID/logs/events"
         jsonPayload.connection.verdict="DENY"
         jsonPayload.src.pod_name="my-source-pod"
         

  3. Inspect the JSON payload:

     * `jsonPayload.drop_reason`: shows why the packet was dropped.
     * `jsonPayload.policies`: lists which NetworkPolicies were evaluated. If an empty list is returned with a `DENY` verdict, the namespace is operating in default-deny mode and no policy allowed the traffic.



If no NetworkPolicy logs appear, verify that logging is enabled in the cluster's NetworkLogging custom resource. For example, check that the `spec.cluster.deny.log` field is set to `true`:
    
    
    kubectl get networklogging default -o yaml
    

#### Step 3: Trace live drops with Hubble CLI

Stream live drops directly by using Hubble CLI to inspect real-time packets:
    
    
    gke-hubble observe --verdict DROPPED --namespace default --follow
    

Example output:
    
    
    TIMESTAMP             SOURCE               DESTINATION          TYPE     VERDICT
    10:14:22.102          default/frontend     default/backend:80   to-stack DROPPED (Policy denied by NetworkPolicy: backend-deny-all)
    

The output indicates the exact NetworkPolicy blocking traffic (`backend-deny-all`).

#### Step 4: Check for conntrack exhaustion

If the drop reason indicates `CT: Map insertion failed`:

  1. Inspect the GKE Dataplane V2 agent log for conntrack table saturation:
         
         kubectl logs -n kube-system daemonset/anetd -c cilium-agent --tail=100 | grep "Conntrack table full"
         

  2. Check the maximum size of the conntrack table on the affected node:
         
         kubectl exec -it -n kube-system daemonset/anetd -c cilium-agent -- cilium status --all-controllers | grep -i conntrack
         

If the conntrack table is full, scale out your workloads across more nodes or reduce the connection rate from client Pods.




* * *

### Diagnose traffic imbalance and TCP resets

Review the diagnostic scope and prerequisites before troubleshooting traffic imbalance and connection resets:

  * **Focus area:** load balancing unevenness, TCP handshake failures, sudden connection termination.
  * **Prerequisites:** GKE Dataplane V2 metrics enabled.
  * **CNI compatibility:** GKE Dataplane V2.
  * **Symptom:** certain Pod replicas receive excessive traffic while others remain idle; client applications log `connection reset by peer` or `broken pipe`.
  * **Goal:** determine whether traffic imbalance is caused by connection stickiness at the transport layer (OSI Layer 4, TCP) versus the application layer (OSI Layer 7, HTTP/2 or gRPC), and identify the source of TCP RST packets.



#### Step 1: Compare Pod-level traffic flow

To determine whether traffic is distributed evenly across your replicas, do the following:

  1. In Cloud Monitoring, query the ingress flow count across all Pods in a Deployment:
         
         sum by (pod) (rate(pod_flow_ingress_flows_count{destination_workload="my-service"}[5m]))
         

  2. Evaluate the traffic distribution across Pods. If a single Pod receives the majority of traffic, investigate connection reuse or sticky sessions:

     * **gRPC or HTTP/2:** long-lived TCP connections cause all requests to traverse a single TCP stream to one backend Pod. Transport-layer (OSI Layer 4, TCP) Kubernetes Service routing cannot balance requests inside an established HTTP/2 connection.
     * **ClientIP Session Affinity:** verify whether the Service is configured with `sessionAffinity: ClientIP`.
     * **Headless Services:** clients might resolve DNS once and cache the single IP address permanently.



#### Step 2: Analyze TCP reset metrics

TCP resets (`RST`) terminate connections immediately. They are emitted by the operating system kernel when an endpoint receives a packet for an unknown port, or when an application closes a connection with unread data in the buffer.

Run the following MQL query in Cloud Monitoring:
    
    
    fetch prometheus_target
    | metric 'prometheus.googleapis.com/hubble_tcp_flags_total/counter'
    | filter (metric.flag == 'RST')
    | align rate(1m)
    | every 1m
    | group_by [metric.source, metric.destination, metric.traffic_direction], sum(val())
    

Review the results of the query to determine the source of the reset:

  * **Outgoing RST (traffic_direction=`egress`):** the local Pod is generating the reset. Check if the Pod application is crashing, reaching its connection limit, or actively rejecting the connection.
  * **Incoming RST (traffic_direction=`ingress`):** the remote peer (external database, API, or remote Pod) sent the reset. Check destination server health and firewall states.



#### Step 3: Stream TCP resets live

Use Hubble CLI to capture the live reset handshake:
    
    
    gke-hubble observe --type trace --verdict FORWARDED --tcp-flags RST --namespace default
    

#### Step 4: Remediation and actionable fixes

Apply the following remediation steps depending on the cause of your traffic imbalance or TCP resets:

  * **For application-layer (OSI Layer 7) or gRPC connection stickiness:**
    * Deploy Cloud Service Mesh to enable application-layer (OSI Layer 7) request-level load balancing.
    * Configure client-side connection limits or keep-alive timeouts (for example, gRPC `MAX_CONNECTION_AGE` and `MAX_CONNECTION_AGE_GRACE`) to force periodic connection re-establishment.
  * **For Service IP affinity:** remove `service.spec.sessionAffinity` unless application state strictly requires it.
  * **For headless Service DNS caching:** ensure application runtimes (such as JVM `networkaddress.cache.ttl`) don't cache DNS results indefinitely.
  * **For application backlog queue overflow:** when an application listen queue is full, the Linux kernel drops incoming SYN packets or sends a TCP RST. Scale out Pod replicas or increase the application listen backlog (`somaxconn`).



* * *

## Tier 2: Node and CNI (Kernel) observability

The node and CNI tier encompasses the host Linux kernel, eBPF programs, and node network interfaces. Bottlenecks at this tier affect all workloads running on the affected node.

### System integrity check: Detect unauthorized patching of anetd

**Caution:** Manually modifying or restarting the GKE Dataplane V2 networking DaemonSet (`anetd`) can cause cluster-wide networking outages and violate GKE managed service level objectives.

GKE Dataplane V2 runs as a managed DaemonSet (`anetd`) in the `kube-system` namespace. In Cloud Logging, you can query Kubernetes audit logs to detect whether unauthorized users or automated scripts have patched or restarted `anetd`:
    
    
    protoPayload.methodName="io.k8s.core.v1.daemonsets.patch" OR
    protoPayload.methodName="io.k8s.core.v1.daemonsets.update"
    protoPayload.resourceName="namespaces/kube-system/daemonsets/anetd"
    

If unauthorized patching is detected, revert the DaemonSet to the default configuration or trigger a node pool recreation to restore managed state.

* * *

### Triage for node-level latency and CNI bottlenecks

Review the diagnostic scope and prerequisites before diagnosing node-level latency and kernel bottlenecks:

  * **Focus area:** host kernel latency, packet drops at the VM interface, GKE Dataplane V2 eBPF agent saturation, conntrack exhaustion.
  * **Prerequisites:** Compute Engine VM metrics enabled; `kubectl` access.
  * **CNI compatibility:** GKE Dataplane V2 and standard GKE CNI.
  * **Symptom:** cross-node traffic experiences latency spikes or random drops, while intra-node traffic remains healthy.
  * **Goal:** differentiate between host VM network throttling, Linux kernel drops, and CNI-level bottlenecks.



#### Step 1: Differentiate issues outside GKE from issues inside GKE

Run the **Compute Engine VM baseline test** : Deploy a standalone Compute Engine VM in the same VPC subnet as the GKE cluster nodes. Test connectivity from the VM to the target destination.

  * **If the standalone VM experiences the same packet drops or latency:** the issue is located outside GKE (VPC firewalls, Cloud NAT, Cloud Interconnect, or the external server). Proceed to Isolate GKE versus VPC or external connectivity issues.
  * **If the standalone VM communicates normally, but GKE Pods fail:** the issue is inside GKE (node-level eBPF, conntrack, or CNI). Proceed to Step 2.



**Limitations of the VM baseline test:** This test might not catch intermittent or low-rate drops that only manifest under high aggregate traffic volumes. Additionally, if the issue is isolated to the underlying hardware of a single VM host, other VMs might not reproduce the behavior.

#### Step 2: Differentiate application issues from node and CNI tier issues

**Troubleshooting custom ip-masq-agent SNAT port collisions:** Clusters using a custom `ip-masq-agent` configuration with the `--random-fully` flag can experience intermittent egress latency. Under high traffic volumes, iptables `--random-fully` might allocate an ephemeral port that collides with an active NodePort, resulting in connection delays. Upgrade `ip-masq-agent` to version 2.11.1 or higher, or remove `--random-fully` to avoid port collisions.

To determine whether latency originates in the application or at the node and CNI tier, do the following:

  1. **Check application resource saturation:** Verify that the node is not experiencing CPU throttling or memory pressure, which delays packet processing in user space:
         
         kubectl top nodes
         kubectl top pods -n default
         

  2. **Inspect Linux kernel conntrack count:** Check the active conntrack count on the host:
         
         # On a node where you have debugging access
         cat /proc/sys/net/netfilter/nf_conntrack_count
         cat /proc/sys/net/netfilter/nf_conntrack_max
         

If `nf_conntrack_count` approaches `nf_conntrack_max`, the host kernel drops new TCP SYN packets.




#### Step 3: Verify VM-level packet drops using Compute Engine telemetry

Google Cloud Compute Engine exports VM-level network interface metrics to Cloud Monitoring.

In Cloud Monitoring > Metrics Explorer, query:
    
    
    sum by (drop_reason) (rate(compute_googleapis_com:instance_network_dropped_packets_count[5m]))
    

  * `FQ_CODEL_DROP`: packet dropped due to Fair Queuing or CoDel queue saturation (VM egress bandwidth limit exceeded).
  * `FIREWALL_RULE_DROP`: packet dropped by a VPC firewall rule.
  * `RATE_LIMIT_DROP`: packet dropped because the VM exceeded its network interface maximum packets per second (PPS) quota.



#### Step 4: Investigate kernel-level drops using eBPF

If VM-level metrics show zero drops, but GKE Pods still drop packets, inspect the GKE Dataplane V2 agent (`anetd`) for eBPF map drops:
    
    
    kubectl logs -n kube-system daemonset/anetd -c cilium-agent --tail=200 | grep -i "drop"
    

Look for `ct-map-insertion-failed` or `fib-lookup-failed`.

* * *

## Tier 3: VPC and Routing (Cloud Network) observability

The VPC and cloud routing tier connects GKE nodes to other Google Cloud services, on-premises networks, and the internet. Failures here typically stem from VPC firewall rules, custom routes, or gateway configurations.

### Isolate GKE versus VPC or external connectivity issues

Review the diagnostic scope and prerequisites before isolating external network issues from in-cluster failures:

  * **Focus area:** boundary isolation between Kubernetes internal routing and VPC cloud routing.
  * **Prerequisites:** gcloud CLI; permissions to create Connectivity Tests.
  * **CNI compatibility:** all clusters.
  * **Symptom:** Pods fail to connect to an external resource (for example, Cloud SQL, an on-premises API, or a third-party endpoint).
  * **Goal:** rapidly determine whether the drop occurs within the GKE node or inside the Google Cloud VPC or external network.



#### Step 1: The Compute Engine VM baseline test

To deploy a baseline VM and evaluate whether the issue persists outside GKE, do the following:

  1. Deploy a temporary Compute Engine VM instance in the same VPC subnet and zone as your GKE node pool:
         
         gcloud compute instances create gke-baseline-tester \
             --zone=us-central1-a \
             --subnet=gke-subnet \
             --machine-type=e2-micro
         

  2. Connect to the instance using SSH and test connectivity to the destination:
         
         curl -v --connect-timeout 5 https://api.example.com
         

  3. Evaluate the outcome:

     * **If the Compute Engine VM cannot connect:** the problem is in the VPC or external network (firewall rules, routing tables, Cloud NAT IP exhaustion, or external IP whitelisting).
     * **If the Compute Engine VM connects successfully:** the problem is inside GKE (NetworkPolicy blocking egress, non-masqueraded Pod CIDR, or container-level DNS).



#### Step 2: Run an on-demand Connectivity Tests test

Run a Google Cloud Connectivity Tests test from the node VM to the destination:
    
    
    gcloud network-management connectivity-tests create test-node-to-dest \
        --source-instance=projects/PROJECT_ID/zones/us-central1-a/instances/gke-baseline-tester \
        --destination-ip-address=203.0.113.10 \
        --destination-port=443 \
        --protocol=TCP \
        --round-trip
    

[Check the result](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#viewing-tests) in the Google Cloud console to identify whether a VPC firewall rule or route is dropping the traffic.

* * *

### Diagnose connectivity using Connectivity Tests

Connectivity Tests simulates packet paths across GKE and VPC resources without sending live traffic. This simulation evaluates Service ClusterIP-to-Pod DNAT resolution, GKE Dataplane V2 NetworkPolicy ingress and egress rules, and node IP masquerading (SNAT). Review the diagnostic scope and prerequisites before running automated path simulations:

  * **Focus area:** automated static path simulation for GKE Pods, Services, NetworkPolicies, and VPC routes.
  * **Prerequisites:** Network Intelligence Center enabled; Network Management API enabled.
  * **CNI compatibility:** GKE Dataplane V2 (enhanced analysis).
  * **Symptom:** unexplained connectivity drops where all configurations appear valid upon manual inspection.
  * **Goal:** statically simulate and trace the entire packet path from a Pod source to destination, identifying the exact line of policy causing a drop.



#### Scenario A: Verify whether a GKE NetworkPolicy is blocking metrics collection

When scraping metrics from Pods in a secure namespace, Google Cloud Managed Service for Prometheus collectors might be blocked by a default-deny NetworkPolicy:
    
    
    gcloud network-management connectivity-tests create test-gmp-to-pod \
        --source-ip-address=10.0.0.15 \
        --destination-gke-pod=projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/k8s/namespaces/prod/pods/backend-pod \
        --destination-port=8080 \
        --protocol=TCP \
        --round-trip
    

Inspect the test trace in Google Cloud console. If the test terminates at the step `GKE Network Policy evaluation` with `DROP`, an ingress rule must be added to allow traffic from the collector Pods.

#### Scenario B: Verify reachability to a GKE Service

Simulate reachability from a client VM to an internal Kubernetes Service:
    
    
    gcloud network-management connectivity-tests create test-vm-to-service \
        --source-instance=projects/PROJECT_ID/zones/us-central1-a/instances/client-vm \
        --destination-ip-address=10.96.0.100 \
        --destination-port=80 \
        --protocol=TCP \
        --round-trip
    

The simulated trace shows:

  1. VPC route match.
  2. VPC firewall egress and ingress allow.
  3. Arrival at the GKE node.
  4. Service DNAT to backend Pod IP address.
  5. Evaluation of Ingress NetworkPolicy on the backend Pod.



#### Scenario C: Diagnose Pod-to-internet egress issues

When Pods cannot reach an external API on the internet:

  1. Create a test from the Pod to the external public IP address (such as `8.8.8.8`):
         
         gcloud network-management connectivity-tests create test-pod-to-internet \
             --source-gke-pod=projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/k8s/namespaces/prod/pods/app-pod \
             --destination-ip-address=8.8.8.8 \
             --destination-port=53 \
             --protocol=UDP \
             --round-trip
         

  2. Examine the drop point:

     * **Dropped at NetworkPolicy:** the Pod lacks an egress NetworkPolicy permitting traffic to `0.0.0.0/0`.
     * **Dropped at VPC Firewall:** a VPC firewall rule denies outbound traffic from the node subnet.
     * **Dropped at Cloud NAT or Route:** the subnet lacks a default route to the internet gateway or Cloud NAT is not configured for the subnet.



* * *

## Tier 4: External Gateway and Cost (Internet and NAT) observability

The external gateway tier manages outbound traffic to public internet destinations through Cloud NAT or external gateways. Observability at this tier helps identify high-egress workloads and control data transfer costs.

### Identify NAT traffic (egress to internet)

Review the diagnostic scope and prerequisites before analyzing outbound internet and NAT traffic:

  * **Focus area:** outbound internet traffic, Cloud NAT port utilization, external data transfer costs.
  * **Prerequisites:** GKE Dataplane V2 Flow Observability enabled.
  * **CNI compatibility:** GKE Dataplane V2.
  * **Symptom:** Cloud NAT port exhaustion errors or unexpectedly high outbound internet egress costs.
  * **Goal:** identify which specific GKE Pod and Service objects are transmitting traffic to external internet endpoints.



#### Step 1: Understand the "to-stack" and "world" concepts in GKE Dataplane V2

In GKE Dataplane V2:

  * `world`: represents any destination outside the GKE cluster and outside the VPC (the public internet).
  * `to-stack`: represents packets transitioning from the eBPF container veth interface to the host Linux networking stack to undergo IP masquerade (SNAT) before reaching Cloud NAT.



#### Step 2: Stream and filter NAT traffic with Hubble CLI

Stream live outbound internet flows originating from your cluster:
    
    
    # Stream egress flows heading to external internet ("world")
    gke-hubble observe \
        --traffic-direction egress \
        --verdict FORWARDED \
        --to-identity world \
        --follow
    

Example output:
    
    
    TIMESTAMP             SOURCE               DESTINATION          TYPE     VERDICT
    10:25:01.120          default/worker-pod   142.250.190.46:443   to-stack FORWARDED
    

To identify the top outbound talkers, you can also pipe Hubble JSON output to `jq` to count external egress flows by Pod:
    
    
    timeout 60s gke-hubble observe \
        --traffic-direction egress \
        --verdict FORWARDED \
        --to-identity world \
        -o json | jq -r '.flow.source.namespace + "/" + .flow.source.pod_name' | sort | uniq -c | sort -nr | head -n 10
    

#### Step 3: Monitor external traffic using metrics

In Cloud Monitoring, track the volume of external flows:
    
    
    fetch prometheus_target
    | metric 'prometheus.googleapis.com/pod_flow_egress_flows_count/counter'
    | filter (metric.destination_identity == 'world')
    | align rate(1m)
    | every 1m
    | group_by [metric.source_workload, metric.source_namespace], sum(val())
    

* * *

### Analyze cluster traffic costs and performance using Flow Analyzer

Review the diagnostic scope and prerequisites before visualizing traffic flows and cross-zone costs:

  * **Focus area:** cross-zone data transfer costs, top talkers, inter-node traffic visibility without SQL queries.
  * **Prerequisites:** VPC Flow Logs enabled with `INCLUDE_ALL_METADATA`; Intranode Visibility enabled; Observability Analytics enabled on the log bucket.
  * **CNI compatibility:** all clusters.
  * **Symptom:** elevated inter-zone data transfer charges on monthly Google Cloud bills.
  * **Goal:** visually identify which GKE workloads are generating cross-zone traffic and optimize placement without querying raw logs.



#### Prerequisites

To use Flow Analyzer for GKE:

  1. **VPC Flow Logs:** must be enabled on the cluster subnet with `metadata="INCLUDE_ALL_METADATA"`.
  2. **Intranode Visibility:** must be enabled on the cluster so pod-to-pod traffic is exposed to the VPC flow logging pipeline.
  3. **Log Analytics:** the `_Default` bucket in Cloud Logging must be upgraded to use Observability Analytics.



**Note:** Flow logs are written to the project that owns the network. In a Shared VPC setup, this project is the host project, not the service project that runs on your GKE cluster. Run Flow Analyzer in the host project, and use the host project ID for `PROJECT_ID` in the Observability Analytics query.

#### Step 1: Identify GKE top talkers in Flow Analyzer

To view high-volume workloads in Flow Analyzer, do the following:

  1. In the Google Cloud console, go to the **Flow Analyzer** page.
  2. Click **Source bucket** and select the log bucket that holds your flow logs. Unless you've routed them elsewhere, this is the **_Default** bucket.
  3. In **Traffic aggregation** , select **Source - Destination**.
  4. Set the time range for your analysis window.
  5. Under **Organize flows by** , select the GKE Pod or workload fields.
  6. Click **Run new query**. The **Highest data flows** chart shows which workloads move the most data.



#### Step 2: Analyze inter-zone traffic costs

Cross-zone traffic incurs data transfer charges. To locate workloads transmitting across zones:

  1. Under **Organize flows by** , select the source zone and destination zone fields.
  2. Click **Run new query** and read the **All data flows** table. Rows where the source and destination zones differ are your cross-zone traffic. Flow Analyzer filters match on values, so you can't filter for "not equal"; compare the zone pairs in the results instead.
  3. Expand a high-volume zone pair to see the underlying source and destination GKE workloads.



**Remediation:**

  * Implement Kubernetes `topologySpreadConstraints` or `podAffinity` to colocate communicating services within the same availability zone.
  * Enable **Topology Aware Routing** (`service.kubernetes.io/topology-mode: Auto`) on the Service to keep traffic within the originating zone.



#### Step 3: Drill down to Observability Analytics (For advanced SQL queries)

From Flow Analyzer, click **View in Log Analytics** to run SQL queries against the flow data.

The following SQL query calculates top cross-zone Pod talkers:
    
    
    SELECT
      JSON_VALUE(json_payload.src_gke_details.pod.workload.workload_name) AS src_workload,
      JSON_VALUE(json_payload.dest_gke_details.pod.workload.workload_name) AS dest_workload,
      JSON_VALUE(json_payload.src_instance.zone) AS src_zone,
      JSON_VALUE(json_payload.dest_instance.zone) AS dest_zone,
      SUM(CAST(JSON_VALUE(json_payload.bytes_sent) AS INT64)) / 1024 / 1024 / 1024 AS total_gb_sent
    FROM
      `PROJECT_ID.global._Default._AllLogs`
    WHERE
      log_name LIKE '%vpc_flows%'
      AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
      AND JSON_VALUE(json_payload.src_instance.zone) != JSON_VALUE(json_payload.dest_instance.zone)
    GROUP BY
      1, 2, 3, 4
    ORDER BY
      total_gb_sent DESC
    LIMIT 20;
    

* * *

## Hubble CLI reference and query cheat sheet

The Hubble CLI streams and filters live network flow data directly from the GKE Dataplane V2 kernel ring buffer.

### Setup: Create a helper alias

Because Hubble runs inside the cluster control plane, configure a shell alias to execute Hubble commands without deploying local binaries:
    
    
    alias gke-hubble="kubectl exec -it -n gke-managed-dpv2-observability deployment/hubble-relay -c hubble-cli -- hubble"
    

### Common filtering recipes

Troubleshooting goal | Hubble CLI command  
---|---  
Observe all dropped packets in real time across the cluster | `gke-hubble observe --verdict DROPPED --follow`  
Stream all traffic for a specific Pod in any namespace | `gke-hubble observe --pod default/my-pod --follow`  
Filter traffic between two specific namespaces | `gke-hubble observe --from-namespace frontend --to-namespace backend`  
Isolate traffic on a specific port (such as Port 80) | `gke-hubble observe --port 80`  
Inspect live DNS queries and answers | `gke-hubble observe --port 53`  
View live TCP resets (RST packets) | `gke-hubble observe --type trace --verdict FORWARDED --tcp-flags RST`  
Stream all outbound traffic heading to the public internet | `gke-hubble observe --traffic-direction egress --to-identity world`  
Inspect HTTP application-layer (OSI Layer 7) traffic | `gke-hubble observe --protocol http`  
  
### Advanced filtering with negation (`--not`)

You can exclude known high-volume or healthy traffic to focus on anomalies:
    
    
    # Observe drops, but exclude internal kube-system health probes and DNS
    gke-hubble observe \
        --verdict DROPPED \
        --not --namespace kube-system \
        --not --port 53
    

### Output formatting and jq integration

To process flow records programmatically, output in JSON format:
    
    
    # Extract only source, destination, and drop reason from the last 100 flows
    gke-hubble observe --verdict DROPPED -o json --last 100 | \
        jq -r '[.time, .flow.source.pod_name, .flow.destination.pod_name, .flow.drop_reason_desc] | @tsv'
    

### Limitations

When using Hubble CLI for live troubleshooting, keep the following technical limitations in mind:

  * **Ephemeral node-local ring buffer:** Hubble flows are stored in an in-memory ring buffer on each individual node. During high-traffic events, older flow logs are overwritten within seconds. For historical analysis, rely on NetworkPolicy logging and VPC Flow Logs in Cloud Logging.
  * **No built-in logical OR:** Hubble CLI flags evaluate multiple arguments using logical AND. To search for multiple conditions (such as Port 80 OR Port 443), run separate commands or filter the JSON output using `jq`.



## What's next

  * [Best practices for network observability](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/network-observability)
  * [Troubleshoot GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshoot-networking)
  * [Troubleshoot connectivity issues in your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/connectivity-issues-in-cluster)
  * [About GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability)
  * [Troubleshoot data issues in Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/manage-flow-analyzer)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
