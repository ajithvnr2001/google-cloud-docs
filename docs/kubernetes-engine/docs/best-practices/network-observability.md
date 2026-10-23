---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/network-observability/
title: Best practices for GKE network observability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:03.733358+00:00
---

# Best practices for GKE network observability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/network-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Best practices for GKE network observability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Managing network connectivity and security policies in dynamic Kubernetes environments presents significant operational challenges. GKE Dataplane V2 observability provides platform administrators with kernel-level visibility into cluster network traffic, which can help enable rapid troubleshooting, continuous compliance auditing, and proactive path validation.

This document outlines conceptual architecture and best practices for Google Kubernetes Engine (GKE) network observability, including the telemetry stack, a mental model for triage, proactive alerting rules, Terraform automation, and cost optimization techniques.

For step-by-step troubleshooting instructions and diagnostic procedures, see [Troubleshoot network observability](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability).

## GKE network observability benefits

Implementing an observability strategy in GKE provides the following key advantages:

  * **Accelerated Mean Time to Resolution (MTTR):** by leveraging eBPF-powered metrics and Hubble flow logs, you can immediately isolate network anomalies. This visibility lets you distinguish between application-level failures, Kubernetes NetworkPolicy blocks, and VPC firewall drops, reducing debugging cycles from hours to minutes.
  * **Kernel-level instrumentation without sidecars:** GKE Dataplane V2 executes observability logic directly within the host Linux kernel using eBPF. This eliminates the need for resource-intensive sidecar proxies or application-level code modifications, ensuring minimal overhead and preserving application performance.
  * **Continuous security compliance auditing:** NetworkPolicy logging generates detailed audit logs for every connection attempt (verdicts of `ALLOW` or `DENY`). These logs provide a tamper-proof record of cluster traffic, essential for satisfying regulatory compliance frameworks (such as PCI-DSS, SOC 2, and HIPAA).
  * **Proactive path validation:** integration with Connectivity Tests lets you simulate network paths and evaluate GKE NetworkPolicies statically before workloads are deployed, preventing configuration drift and deployment-phase connectivity issues.
  * **Resource and cost optimization:** detailed flow tracking exposes inefficiencies such as excessive Cloud NAT port utilization, inter-zone data transfer spikes, and un-cached DNS resolution patterns, enabling informed capacity planning and cost management.



## GKE network observability architecture

GKE Dataplane V2 offers a multi-layered observability stack designed for different operational phases. The following table outlines the core components and their recommended use cases:

Observability component | Primary use case | Availability | Data retention | Performance overhead | Key telemetry signals  
---|---|---|---|---|---  
GKE Dataplane V2 metrics | System-wide health monitoring, trend analysis, and alerting. | GKE Dataplane V2 only | Historical telemetry retention (Cloud Monitoring and Google Cloud Managed Service for Prometheus stores 30 or more days of metrics and logs) | Negligible (kernel-level aggregation) | Packet and byte counters, TCP reset counts, and connection drop rates (`pod_flow_drop_count`).  
NetworkPolicy logs | Security policy auditing, historical connection analysis, and compliance. | GKE Dataplane V2 only (for `NetworkLogging` custom resource configuration) | Configurable (Cloud Logging) | Low (buffered log export) | Connection metadata (source and destination labels, IP addresses, ports) and policy verdicts (`ALLOW` or `DENY`).  
Hubble CLI and UI | Live, interactive traffic analysis and real-time packet-level debugging. | GKE Dataplane V2 only | Ephemeral (node-local ring buffer) | Low (enable dynamically) | Real-time flow traces, detailed drop reasons (such as policy denied or conntrack table saturation).  
GKE DNS metrics | Monitoring DNS resolution performance, cache efficiency, and upstream latency. | All clusters | Long-term (Cloud Monitoring) | Negligible | DNS request count, cache hit and miss ratio, upstream forwarding latency, and concurrent limit rejections.  
Connectivity Tests | Pre-deployment path validation and static configuration auditing. | All clusters | Not applicable (on-demand simulation) | None (statically simulated) | Simulated packet routing path, including simulated NetworkPolicy evaluation.  
VPC Flow Logs | Inter-node and external traffic auditing, security forensics, and cost analysis. | All clusters | Configurable (Cloud Logging or BigQuery) | None (configurable sampling rate) | 5-tuple connection details, bytes and packets sent, GKE metadata (namespace, workload, service), and RTT (for TCP).  
Flow Analyzer | Visual analysis of VPC traffic, identifying top talkers, and analyzing cross-zone costs without writing SQL queries. | All clusters | Depends on Observability Analytics bucket retention | None (analytical UI) | Aggregated traffic volume and latency grouped by GKE workload or service.  
  
In the preceding table, a performance overhead of _Negligible_ means that components remain strictly within a minimal resource footprint (typically <0.1 vCPU and minimal memory) regardless of traffic volume or system scale. _Low_ components maintain a minimal footprint under standard conditions but scale dynamically with traffic density. Under high-throughput scenarios, resource usage can scale up to 2 vCPU and several hundred megabytes of memory.

## GKE observability mental model and triage loop

To troubleshoot network anomalies effectively, you need to select the appropriate telemetry signal for your operational scope and follow a consistent triage methodology.

### Choose the right telemetry source

With multiple telemetry sources available, choose the tool that fits your current operational task:

Telemetry source | Answers | Ideal for | Google Cloud destination  
---|---|---|---  
GKE Dataplane V2 metrics | What is happening and at what scale? | Dashboards, alerting, and capacity planning. | Cloud Monitoring (`prometheus.googleapis.com`)  
NetworkPolicy logs | Why was a connection blocked inside GKE? | Security audits and security policy root-cause analysis. | Cloud Logging (`policy-action` log)  
VPC Flow Logs | What happened to this traffic after leaving the Pod? | Historical traffic analysis between workloads, inter-zone data transfer costs, and VPC-level drop attribution. | Cloud Logging and Observability Analytics (`vpc_flows` log)  
Hubble CLI and UI | What is passing through the node right now? | Live debugging, tcpdump alternative, and active incidents. | Ephemeral ring buffer (Hubble CLI)  
Connectivity Tests | Can traffic travel successfully? | Active dataplane probing and path analysis: verify reachability and identify exact drop points across VPC firewalls, routes, and GKE nodes. | Network Intelligence Center (simulation)  
  
### Standardized troubleshooting loop

Use this repeatable workflow to triage any GKE networking incident:

  1. **Detect anomaly:** identify the issue through Cloud Monitoring alerts (for example, spikes in TCP resets, DNS concurrent limit rejections, or packet drops).
  2. **Isolate the tier:** run the GCE VM baseline test (see [Triage for node-level latency and CNI bottlenecks](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#triage-node-latency)) to determine whether the block is inside the GKE cluster (CNI, NetworkPolicy, IP masquerade) or outside in the VPC (firewall rules, routing, Cloud NAT).
  3. **Investigate root cause:** perform a detailed analysis of the flow: 
     * For live incidents: use Hubble CLI (`hubble observe`) to stream real-time flows and identify drop reasons.
     * For historical or intermittent issues: query NetworkPolicy logs or VPC Flow Logs in Cloud Logging.
  4. **Validate remediation:** run a simulated [Connectivity Tests test](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#diagnose-connectivity-tests) to verify that the path is statically allowed, and then check the metrics dashboard to confirm that the drop rate has returned to zero.



## Proactive network monitoring and alerting

To maintain high availability, platform administrators should establish alerting policies in Cloud Monitoring to identify network degradation before it impacts workloads.

### Alert on packet drop spikes

An anomalous increase in dropped network flows typically indicates a misconfigured security policy or node-level connection tracking (conntrack) exhaustion.

  * **Prometheus Query (PromQL):**
        
        sum(rate(pod_flow_egress_flows_count{verdict="DROPPED"}[5m])) by (source) > 10
        

  * **Recommended action:** refer to [Diagnose packet drops and NetworkPolicy blocks](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#diagnose-packet-drops) to isolate the specific GKE NetworkPolicy or eBPF drop reason causing packet loss.




### Alert on DNS saturation

When CoreDNS or NodeLocal DNSCache reaches its concurrent query limit, subsequent DNS lookups are rejected, leading to intermittent application timeouts.

  * **Prometheus Query (PromQL):**
        
        sum by (cluster_name) (rate(kubernetes_io_networking_dns_kubedns_max_concurrent_rejected_request_count[5m])) > 0
        

  * **Recommended action:** scale the `kube-dns` replica count or implement NodeLocal DNSCache to distribute the resolution load. For detailed steps, see [Diagnose DNS resolution failures](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#diagnose-dns-failures).




### Alert on TCP reset spikes

A spike in TCP reset packets often indicates that a backend service is rejecting connections, potentially due to application crash loops or socket queue saturation.

**Note:** This alert requires the Hubble metrics scraping configuration (`PodMonitoring`) described in [Diagnose packet drops and NetworkPolicy blocks](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#diagnose-packet-drops) to be active.

  * **Monitoring Query Language (MQL):**
        
        fetch prometheus_target
        | metric 'prometheus.googleapis.com/hubble_tcp_flags_total/counter'
        | filter (metric.flag == 'RST')
        | align rate(1m)
        | every 1m
        | group_by [metric.source, metric.destination], sum(val())
        | condition val() > 50
        

  * **Recommended action:** refer to [Diagnose traffic imbalance and TCP resets](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#diagnose-traffic-imbalance) to investigate connection stickiness or application queue saturation.




### Automated path validation in CI/CD

Integrate Connectivity Tests into deployment pipelines to validate network paths statically before routing production traffic. Use the gcloud CLI to verify that newly deployed workloads can reach external dependencies (such as databases and APIs) without policy blockages.

  * **Example command:**
        
        gcloud network-management connectivity-tests create test-prod-db-egress \
            --source-gke-pod=projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/k8s/namespaces/prod/pods/my-app-pod \
            --destination-ip-address=10.240.0.100 \
            --protocol=TCP \
            --destination-port=5432 \
            --round-trip
        




### Enable Observability Analytics for visual flow analysis

To enable visual, SQL-free analysis of VPC traffic flows, upgrade the GKE log bucket (typically the `_Default` bucket) to use Observability Analytics. This lets platform administrators leverage Flow Analyzer to investigate traffic distribution and data transfer costs. For more information, see [Analyze cluster traffic costs and performance using Flow Analyzer](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability#analyze-traffic-costs).

## Terraform automation: Observability-as-Code

To implement this observability architecture consistently and avoid manual setup errors, deploy the telemetry pipeline using the following Terraform configuration (requires the `google-beta` provider):
    
    
    # Configure the VPC Subnet with VPC Flow Logs enabled and all metadata included
    resource "google_compute_subnetwork" "gke_subnet" {
      name          = "gke-subnet"
      ip_cidr_range = "10.0.0.0/20"
      region        = "us-central1"
      network       = google_compute_network.custom.id
    
      # Enable VPC Flow Logs. flow_sampling is the secondary sampling rate, which
      # applies to flow log entries after they are generated. The primary packet
      # sampling rate is dynamic and isn't configurable.
      log_config {
        aggregation_interval = "INTERVAL_5_SEC"
        flow_sampling        = 0.5 # Default rate; satisfies the LIGHT org policy tier
        metadata             = "INCLUDE_ALL_METADATA"
      }
    }
    
    # Configure GKE Cluster with Dataplane V2, Intranode Visibility, and Hubble
    resource "google_container_cluster" "primary" {
      provider   = google-beta
      name       = "gke-observability-cluster"
      location   = "us-central1"
      network    = google_compute_network.custom.id
      subnetwork = google_compute_subnetwork.gke_subnet.id
    
      # Enable Dataplane V2 (Required for all advanced telemetry)
      datapath_provider = "ADVANCED_DATAPATH"
    
      # Enable Intranode Visibility (ensures local node pod-to-pod traffic hits the VPC)
      enable_intranode_visibility = true
    
      # Enable Managed Service for Prometheus (GMP)
      monitoring_config {
        enable_components = ["SYSTEM_COMPONENTS"]
        managed_prometheus {
          enabled = true
        }
    
        # Enable Dataplane V2 Flow Observability (Hubble Relay and metric exposure)
        advanced_datapath_observability_config {
          enable_metrics = true
          enable_relay   = true
        }
      }
    }
    
    # Upgrade the Default log bucket to use Log Analytics (required for Flow Analyzer)
    resource "google_logging_project_bucket_config" "default_analytics" {
      project          = var.project_id
      location         = "global"
      bucket_id        = "_Default"
      enable_analytics = true
    }
    
    # Define a baseline static path validation test (Pod to external internet gateway)
    resource "google_network_management_connectivity_test" "pod_to_internet" {
      name = "pod-to-internet-egress"
      source {
        gke_pod = "projects/${var.project_id}/locations/us-central1/clusters/${google_container_cluster.primary.name}/k8s/namespaces/prod/pods/my-app-pod"
      }
      destination {
        ip_address = "8.8.8.8"
        port       = 443
      }
      protocol = "TCP"
    }
    

## Cost optimization and noise reduction

Network telemetry (metrics and logs) can generate substantial data volumes, leading to high ingestion and storage costs. Use the following strategies to optimize telemetry collection without losing visibility into critical traffic:

### Disable allowed connection logs

By default, NetworkPolicy logging captures both allowed and denied connections. Allowed connections dominate log volume (often 99% or more of traffic). You can update the cluster's `NetworkLogging` configuration to capture only denied connections (drops), which dramatically reduces logging costs:

  1. Save the following manifest as `network-logging-config.yaml`:
         
         apiVersion: networking.gke.io/v1alpha1
         kind: NetworkLogging
         metadata:
           name: default
         spec:
           cluster:
             allow:
               log: false # Disable logging for allowed traffic
               delegate: false
             deny:
               log: true  # Keep logging for blocked traffic (critical for security/triage)
               delegate: false
         

  2. Apply the configuration:
         
         kubectl apply -f network-logging-config.yaml
         




### Delegate logging through annotations

For fine-grained cost control, delegate logging to annotations by setting `delegate: true` in the `NetworkLogging` custom resource. This configuration ensures the following:

  * Allowed traffic is logged only if the matching NetworkPolicy has the annotation `policy.network.gke.io/enable-logging: "true"`.
  * Denied traffic is logged only for Pod objects in namespaces annotated with `policy.network.gke.io/enable-deny-logging: "true"`.



This configuration lets you enable logging only for highly critical workloads (such as payment gateways) while ignoring noisy, low-risk services.

### Tune VPC Flow Logs sampling rate

**Caution:** VPC Flow Logs on high-traffic clusters can incur significant Cloud Logging ingestion charges. To reduce volume, filter logs and metadata before lowering the secondary sampling rate. Keep the default `0.5` rate—which satisfies the `LIGHT` tier of the `constraints/compute.requireVpcFlowLogs` organization policy—on subnets backing clusters that you actively troubleshoot. Because Pods are short-lived, lower rates frequently miss critical flows.

In your Terraform configuration (or Google Cloud console), lower the secondary sampling rate only on subnets where you need traffic volume and cost aggregates rather than individual flow records. Because VPC Flow Logs estimates total traffic from sampled packets, byte and packet counts remain usable for cost analysis at lower rates. Don't set the `flow_sampling` rate lower than `0.1`, the minimum rate that satisfies the `ESSENTIAL` tier of the `constraints/compute.requireVpcFlowLogs` organization policy:
    
    
    resource "google_compute_subnetwork" "gke_subnet" {
      # ... other subnet configs ...
      log_config {
        aggregation_interval = "INTERVAL_5_SEC"
        flow_sampling        = 0.1 # ESSENTIAL tier: volume and cost analysis, not per-flow troubleshooting
        metadata             = "INCLUDE_ALL_METADATA"
      }
    }
    

The following table summarizes the secondary sampling rates and the corresponding tiers of the `constraints/compute.requireVpcFlowLogs` organization policy:

Secondary sampling rate | Organization policy tier | When to use it  
---|---|---  
`1.0` | `COMPREHENSIVE` | Clusters with a standing requirement for per-flow forensics or security auditing. Choose this rate when you configure the subnet, because raising the rate after an incident doesn't recover flows that were never captured.  
`0.5` (default) | `LIGHT` | Subnets that back clusters you troubleshoot. This is the default rate and the recommended baseline.  
`0.1` | `ESSENTIAL` | Subnets where you need traffic volume and cost aggregates rather than individual flows.  
  
### Apply Cloud Logging exclusions

Exclude noisy or irrelevant logs (such as `kube-system` internal traffic) directly at the Cloud Logging sink level. Add an exclusion filter to your `_Default` sink to drop internal metadata or system Pod logs:
    
    
    resource.type="gce_subnetwork" AND
    log_name:"projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows" AND
    jsonPayload.src_gke_details.pod.pod_namespace="kube-system"
    

## Best practices and operational tips

Consider the following operational guidelines when deploying and maintaining your cluster telemetry pipeline:

  * **Enable GKE Dataplane V2 flow observability on demand:** flow observability (`hubble-relay`) can introduce slight overhead. For production clusters, you can enable it during debugging sessions and [disable](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability#disable-observability) it afterwards to minimize resource consumption on nodes:
        
        gcloud container clusters update CLUSTER_NAME \
            --enable-dataplane-v2-flow-observability \
            --location=LOCATION
        

  * **Enable Intranode Visibility:** by default, traffic between two Pod objects on the same node doesn't leave the node, making it invisible to VPC Flow Logs. Intranode Visibility is enabled by default in Autopilot clusters and disabled by default on Standard clusters, including Standard clusters that use GKE Dataplane V2. [Enabling Intranode Visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) hairpins this traffic through the VPC, and helps ensure that VPC firewall rules and flow logs apply consistently.

  * **Understand Service VIP resolution behavior:** after a Kubernetes Service Virtual IP (VIP) is resolved to a backend Pod IP address, transport-layer (OSI Layer 4) metrics count it as pod-to-pod traffic. To trace which Service VIP was originally targeted, rely on Hubble CLI live flows during the connection handshake.

  * **Align metric and log timestamps:** when investigating an incident, correlate the spike in Cloud Monitoring metrics with the exact time window when querying logs in Cloud Logging or Hubble CLI to ensure that you are analyzing the same event.




## What's next

  * [Troubleshoot network observability](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-observability)
  * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
  * [About GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability)
  * [Observe your traffic using GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
