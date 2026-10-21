---
url: https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners/
title: Autopilot partners \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:11.282034+00:00
---

# Autopilot partners  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  Autopilot partners Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page provides information about Google Kubernetes Engine (GKE) Autopilot partner organizations and the specialized workloads that they make available in Autopilot clusters.

## What are Autopilot partner workloads?

Google Kubernetes Engine (GKE) Autopilot clusters don't usually allow workloads that require elevated privileges, such as access to `/var/run`, `privileged: true`, or highly-privileged Linux file capabilities such as `NET_RAW` and `SYS_ADMIN`.

The exceptions to this restriction are Autopilot _partner workloads_. A subset of [Google Cloud Partners](https://cloud.google.com/partners) provide specially-privileged workloads for Autopilot clusters. You can deploy these partner workloads to meet requirements such as collecting node-level metrics without needing to run a sidecar container in every Pod.

### Overview of the allowlisting process

Every partner workload goes through a review process to ensure that they meet baseline requirements for GKE, such as having the least amount of permissions required to run correctly, and fine-grained control over the resources that the workloads can access.

We take measures such as the following to restrict the capabilities of these deployed workloads:

  * Verify that the containers are pulled from the approved location.
  * Reject Pod specs that don't match the approved specification.



If you're a Google Cloud partner with an Autopilot workload that requires elevated privileges and needs to be added to an allowlist, contact your partner manager for information about the Autopilot partner program.

### Run privileged partner workloads in Autopilot

In GKE version 1.32.2-gke.1652000 and later, some partners provide _allowlists_ that correspond to their privileged workloads. These workloads can't run in your clusters unless you install the corresponding allowlist. This method has the following benefits:

  * You have explicit control over whether a partner workload can run in your cluster.
  * GKE automatically synchronizes the allowlists in your cluster with the latest version from a Google-managed repository that stores allowlist files for partner workloads.
  * Partner workloads that don't meet the strict criteria of an installed allowlist are rejected during deployment.



For more information, see [Run privileged workloads from GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads).

Privileged partner workloads that were added between 2021 and 2024 can run on Autopilot mode without an allowlist. Cluster operators who have the corresponding permissions can deploy these workloads in your cluster at any time.

## Pricing

Any resources that partner workloads create in your Autopilot clusters are billed according to the [Autopilot pricing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode). For information about any additional pricing for partner solutions, consult the relevant partner's documentation.

## Autopilot partner workloads

The following sections describe the partner workloads for Autopilot. The partner workloads available for each of your clusters depends on the GKE version of the cluster.

This table only describes the Google Cloud partners that have Autopilot workloads that need elevated privileges. Other Google Cloud partners have products that work with Autopilot without needing elevated privileges. For a full list of Google Cloud partners, refer to the [Partner Directory](https://cloud.google.com/find-a-partner/).

### Partners that support allowlists

The following table describes partners whose workloads are available to install with allowlists. Each entry in this table includes the path to a partner's workload allowlists, which you can use to [configure allowlist installation and synchronization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads#create-allowlistsynchronizer) for your cluster.

Partner | Description  
---|---  
Attribute |  Attribute offers zero-tagging technology that analyzes runtime data with eBPF to reveal costs associated with customers, features, and apps automatically, including across shared and multi-tenant setups. Attribute provides real-time insights for margin optimization, pricing strategy, and cost accountability.  Allowlist path: `Attribute/sensor/*` For more information, refer to [Attribute installation guide for GKE Autopilot (login required)](https://attrb.io/documents/cloud-integrations/cloud-integrations/connect-to-gcp/attribute-sensor-for-gke-autopilot/).  
Checkmk |  Checkmk helps organizations monitor the reliability and availability of their applications, optimize resource usage, and address issues that may arise. Checkmk can automatically discover and collect cluster-wide data, providing visibility into GKE Autopilot performance and health, and visualize the information with dashboards. Allowlist path: `Checkmk/checkmk_kube_agent/*` For more information, refer to [Checkmk installation instructions for GKE Autopilot](https://checkmk.com/blog/monitor-gke-autopilot-checkmk).  
CrowdStrike Falcon |  CrowdStrike Falcon helps secure cloud infrastructure and prevent breaches by leveraging machine learning and human-driven threat intelligence to reduce the attack surface and provide visibility of events in the environment. CrowdStrike Falcon's user space sensor provides visibility and protection for GKE Autopilot using a single agent, protecting both the node and containers running on it. Allowlist path: `CrowdStrike/falcon-sensor/*` For more information, refer to [CrowdStrike Falcon Deployment Guide for GKE (login required)](https://falcon.crowdstrike.com/login/?next=%2Fdocumentation%2Fpage%2Fa69024ee%2Ffalcon-operator---deployment-guide-for-google-kubernetes-engine).  
Dash0 |  Dash0 is an agentic observability platform built on OpenTelemetry that helps you monitor GKE Autopilot workloads with correlated logs, metrics, and traces. By combining unified telemetry with automated analysis, Dash0 helps you detect, understand, and resolve issues faster. Allowlist path: `Dash0/operator/*` For more information, refer to [Installing the Dash0 operator on GKE Autopilot](https://github.com/dash0hq/dash0-operator/tree/main/helm-chart/dash0-operator#notes-on-gke-autopilot).  
Datadog |  Datadog provides visibility into containerized apps running on GKE Autopilot by collecting metrics, logs, and traces, which helps to identify performance issues and provide context for troubleshooting. Allowlist path: `Datadog/datadog/*` For more information, refer to [Monitor GKE Autopilot with Datadog](https://www.datadoghq.com/blog/gke-autopilot-monitoring/).  
Dynatrace |  Dynatrace provides enterprise observability for security platform modernization and cloud adoption with real-time discovery and AI-powered causal context. You can deploy the Dynatrace OneAgent in your Google Cloud environment to get automated insights into the usage and performance of your GKE clusters.  Allowlist paths: 

  * `Dynatrace/csidriver/*`
  * `Dynatrace/csijob/*`
  * `Dynatrace/logmonitoring/*`

For more information, refer to the [ Dynatrace installation instructions for GKE Autopilot](https://www.dynatrace.com/support/help/setup-and-configuration/setup-on-k8s/installation/supported-technologies#gke-autopilot).  
Gremlin |  Gremlin helps enterprises to build more reliable systems by identifying and addressing potential failure points. Its cloud-native platform integrates with Google Cloud, allowing DevOps teams to test reliability and detect risk across cloud infrastructure and applications. Allowlist path: `Gremlin/agent/*` For more information, refer to the [ Installing Gremlin on GKE Autopilot](https://www.gremlin.com/docs/installing-gremlin-on-gke-autopilot).  
Harness |  Harness Chaos Engineering lets you to introduce faults into applications and infrastructure to test the resilience of business services. The platform provides tools to build a scalable resilience testing practice, with features like Experiments, ChaosGuard for governance, and AI-powered recommendations. It also offers enterprise capabilities such as RBAC, SSO, and auditing. Allowlist path: `Harness/allowlists/*` For more information, refer to the [ Harness Chaos Engineering documentation for GKE Autopilot](https://developer.harness.io/docs/chaos-engineering/guides/gke-autopilot).  
Kodem |  Kodem integrates code and runtime analysis to provide security teams with contextual insights. Kodem provides visibility across source code, containers, OS, and memory to help identify exploitable vulnerabilities. This visibility helps security teams to prioritize, determine the root cause, and remediate or mitigate risks. Allowlist paths: 

  * `Kodem-Security/koltan/*`
  * `Kodem-Security/komon/*`

For more information, refer to the [ Kodem Security Runtime sensors for GKE Autopilot (login required)](https://docs.kodemsecurity.com/deployments/deployments-overview/installing-kodem-runtime-sensors-in-gke-autopilot).  
MetalBear mirrord |  MetalBear mirrord lets developers run local processes in the context of their cloud cluster. This tool connects the local process to the cluster's network, environment variables, and files without deploying the process to the cluster. Allowlist path: `mirrord/mirrord-agent/*` For more information, refer to the [mirrord installation instructions for GKE Autopilot](https://metalbear.com/mirrord/docs/getting-started/installing-mirrord/operator#gke-autopilot).  
Odigos |  Odigos automates application observability with eBPF and OpenTelemetry, giving you control over your workload instrumentation and providing end-to-end distributed traces. Allowlist path: `Odigos/Odigos/*` For more information, refer to the [Odigos installation instructions for GKE Autopilot](https://docs.odigos.io/oss/setup/installation-options#gke-installation).  
Orca Sensor |  Orca Sensor is an eBPF-based sensor that can be deployed to GKE Autopilot clusters to provide runtime visibility and protection that's integrated with the Orca Cloud Security Platform. Allowlist path: `Orca-Security/orca-allowlist/*` For more information, refer to the [Orca Sensor installation guide (login required)](https://docs.orcasecurity.io/docs/runtime-protection).  
Palo Alto Networks | 

#### Prisma Cloud

Prisma Cloud DaemonSet Defenders enforce policies for your environment. Prisma Cloud Radar displays a visualization of your nodes and clusters so you can identify risks and investigate incidents. Allowlist path: `Palo-Alto-Networks/prisma-cloud-defender/*` For more information, refer to the [Prisma Cloud Kubernetes installation guide](https://docs.prismacloud.io/en/compute-edition/22-12/admin-guide/install/install-gke-autopilot).

#### Cortex XDR

Cortex XDR provides threat prevention, detection, and response capabilities. The solution uses the Cortex XDR agent (using eBPF) to identify, detect, and help protect against threats, vulnerabilities, misconfigurations, and anomalous behavior. Allowlist path: `Palo-Alto-Networks/cortex-agent/*` For more information, refer to the [Cortex Agent Administrator Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/8.9/Cortex-XDR-Agent-Administrator-Guide/Install-the-Cortex-XDR-Agent-for-Kubernetes-Hosts).  
SentinelOne Cloud Workload Security for Containers |  SentinelOne provides an AI-powered threat protection solution for containerized workloads. This solution lets you monitor, detect, and analyze process, file, and binary-based threats across nodes and containers within GKE Autopilot clusters. Allowlist path: `SentinelOne/s1-agent/*` For more information, refer to the [SentinelOne Kubernetes installation guide (login required)](https://community.sentinelone.com/s/article/000008772).  
Steadybit |  Steadybit is a platform for chaos engineering that helps teams improve the reliability and resilience of their systems by injecting failures and testing how applications respond. It offers automation tools to simulate disruptions in cloud-native environments. Allowlist path: `Steadybit/extension-container/*` For more information, see [Steadybit on GKE Autopilot](https://steadybit.com/blog/chaos-engineering-with-steadybit-on-gke-autopilot/?utm_source=gke_listing).  
Sweet Security |  The Sweet Security platform helps companies implement security practices in their GKE Autopilot clusters. Using an eBPF-based sensor that integrates with existing Kubernetes tooling, Sweet Security provides real-time monitoring, threat detection and prevention, runtime vulnerability management, API security, and AI security. Allowlist path: `Sweet/sensor/*` For more information, refer to [Sweet Security Sensor Deployment for GKE Autopilot (login required)](https://docs.sweet.security/docs/gke-autopilot).  
Sysdig Secure DevOps Platform |  The Sysdig Secure Devops Platform helps you implement container security practices in your GKE Autopilot clusters, including monitoring and securing workloads using the Sysdig agent. The Sysdig agent is a host component that processes syscall, creates capture files, and performs auditing and compliance. Allowlist path: `Sysdig/agent/*` For more information, refer to [Visibility and Security for GKE Autopilot](https://sysdig.com/blog/visibility-security-gke-autopilot/).  
Trend Micro |  Trend Vision One Container Security provides protection for containers from development through deployment and in production. It helps prevent pre-runtime and runtime vulnerabilities, attacks, and misconfigurations in containerized applications. Allowlist path: `Trend-Vision-One/trendmicro-scout/*` For more information, refer to the [Trend Vision One installation guide for Container Security on GKE](https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-connecting-google-gke-clusters).  
Upwind |  Upwind is a Cloud Security Platform that uses runtime context to identify risks, threats, and insights from cloud infrastructure and workloads. Its eBPF-based sensor for GKE Autopilot clusters provides runtime context for posture management, real-time threat detection, and defense measures, to help ensure security. Allowlist path: `Upwind/upwind-agent/*` For more information, refer to the [Upwind GKE Autopilot compatibility update](https://www.upwind.io/feed/proactively-secure-google-cloud-workloads-with-upwinds-gke-autopilot-integration).  
Uptycs |  Uptycs Container Security Platform helps you implement security best practices for GKE Autopilot clusters through its eBPF runtime sensor-based monitoring solution. The platform offers visibility into processes, connections, and Kubernetes RBAC security controls by providing security monitoring, compliance capabilities, and threat detection across containerized workloads and nodes. Allowlist path: `Uptycs/uptycs-runtime-sensor/*` For more information, refer to the [Uptycs GKE Autopilot compatibility update](https://www.uptycs.com/blog/uptycs-gke-security-autopilot-kubernetes-protection).  
Virtana |  Virtana Container Observability provides visibility into Kubernetes, OpenShift, and containerized environments. Built on open-source telemetry, it helps teams detect and resolve issues, optimize resource usage, and maintain performance. Allowlist paths: 

  * `Virtana/cadvisor/*`
  * `Virtana/node-exporter/*`

For more information, refer to [Deploy Virtana on GKE Autopilot clusters](https://docs.virtana.com/en/container-observability/deployment/deploy-virtana-co-south-on-gke-autopilot-clusters.html#deploy-virtana-co-south-on-gke-autopilot-clusters).  
Wiz Runtime Sensor |  The Wiz Runtime Sensor provides detection and response capabilities for cloud workloads. It is an eBPF-based agent that can be deployed to GKE clusters to provide real-time visibility and monitoring of running processes, network connections, file activity, and system calls to detect, investigate, and respond to malicious behavior affecting the workload. Allowlist path: `Wiz/wiz-sensor/*` For more information, refer to the [Wiz Runtime Sensor overview](https://www.wiz.io/blog/wiz-expands-platform-with-the-runtime-sensor-to-provide-unified-cloud-security).  
  
### Partners that don't support allowlists

The following table describes partners whose workloads don't support allowlists. These workloads might have fewer features, such as a lack of support for private image registries. 

Partner | Description  
---|---  
Aqua |  Aqua supports securing and ensuring compliance for the full lifecycle of workloads on GKE Autopilot, and specifically the Kubernetes pods, which run multiple containers with shared sets of storage and networking resources. For more information, refer to [Protecting Cloud Native Workloads on GKE Autopilot](https://blog.aquasec.com/gke-autopilot-security).  
Check Point CloudGuard |  Check Point CloudGuard provides unified, cloud-native security across your applications, workloads, and network. You can use it to manage your security posture across Google Cloud environments. For more information, refer to [Onboarding Kubernetes clusters](https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/Assets/Kubernetes/Kubernetes.htm).  
Elastic Cloud on Kubernetes (ECK) |  Built on the Kubernetes Operator pattern, Elastic Cloud on Kubernetes (ECK) extends the basic Kubernetes orchestration capabilities to support the setup and management of the Elastic Stack on Kubernetes. With Elastic Cloud on Kubernetes you can manage and monitor multiple clusters, scale cluster capacity and storage, and perform safe configuration changes through rolling upgrades. For more information, refer to the [ ECK Quickstart](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-autopilot.html).  
HashiCorp Consul |  HashiCorp Consul is a service networking solution to automate network configurations, discover services, and enable secure connectivity across environments, including GKE Autopilot.  For more information, refer to the [Consul installation instructions for GKE Autopilot](https://developer.hashicorp.com/consul/docs/k8s/installation/install#install-consul-on-gke-autopilot).  
Kubecost |  Kubecost provides real-time cost visibility and insights for teams using GKE, including Autopilot, helping you monitor your Kubernetes costs.  For more information, refer to the [Kubecost installation instructions for GKE Autopilot](https://docs.kubecost.com/install-and-configure/install/provider-installations/gke-autopilot-install).  
Lacework |  Lacework provides visibility and context to defend cloud environments by using machine learning. The Lacework security platform learns normal behavior in your cloud environment to help you spot threats.  For more information, refer to the [Lacework installation instructions for GKE Autopilot](https://docs.lacework.net/onboarding/install-with-gke-autopilot#deploy-agent-using-a-deamonset-manifest).  
New Relic |  The New Relic Kubernetes integration gives you observability into the health and performance of your environment by using the New Relic infrastructure agent, which collects telemetry data from your cluster using several New Relic integrations such as the Kubernetes events integration, the Prometheus Agent, and the New Relic Logs Kubernetes plugin.  For more information, refer to the [New Relic installation instructions for GKE Autopilot](https://docs.newrelic.com/docs/kubernetes-pixie/kubernetes-integration/installation/kubernetes-integration-install-configure/#gke-autopilot).  
Splunk Observability Cloud |  Splunk Observability Cloud provides visibility into the composition, state, and ongoing issues within a cluster. For more information, refer to the [Splunk Kubernetes installation guide](https://help.splunk.com/en/splunk-observability-cloud/manage-data/splunk-distribution-of-the-opentelemetry-collector/get-started-with-the-splunk-distribution-of-the-opentelemetry-collector/collector-for-kubernetes/install-with-helm).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
