---
url: https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate/
title: About GKE Agent Substrate \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:18:52.740963+00:00
---

# About GKE Agent Substrate  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About GKE Agent Substrate Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** Agent Substrate is available to all Google Cloud customers for evaluation and non-production use. Production support is offered on an allowlist basis under a private GA program. To request production support for your workloads, submit the [Agent Substrate Production Support Signup form](https://docs.google.com/forms/d/e/1FAIpQLSeVdndsPwD_D9RCLNvRzVbx0a8gYzIHLOTA6db-N1UFP7w1zw/viewform?usp=preview). Our team will follow up within 48 hours.

Agent Substrate runs agentic workloads at scale on Kubernetes clusters. It addresses a common resource inefficiency: interactive agents (such as personal assistants and coding agents) often spend most of their time waiting for user input or external triggers. Keeping these inactive agents continuously running uses CPU and memory that could otherwise be allocated to active workloads.

Agent Substrate solves this problem by suspending idle agents and taking a snapshot of the agent's active memory (RAM) and local files. When the suspended agent needs to act again, the system restores the agent's state onto an available sandbox in under a second.

Agent Substrate builds on the capabilities of [Agent Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox), and improves on Agent Sandbox by bypassing the bottlenecks of the standard Kubernetes control plane. As a result, it runs significantly more concurrent agents per machine and drastically reduces agent startup times.

Standard Kubernetes deployments (including Agent Sandbox) associate each agent workload with a dedicated Pod. Although Kubernetes is highly scalable, it's constrained by the scheduling throughput and startup latency of Pods. In addition, Kubernetes doesn't support hibernating Pods, and keeping millions of idle agents in a cluster would exhaust Pod limits and control plane memory. To avoid paying for idle compute, you have to shut down the Pods and manage agent state in external storage. Agent Substrate solves these scaling constraints by decoupling agent state from underlying Pods: it stores millions of suspended agent snapshots in storage and restores them on demand onto a shared pool of warm Workers.

Agent Substrate is an open source system that you deploy directly onto your own GKE Standard clusters. Although the core project is developed in the open source [Agent Substrate repository](https://github.com/agent-substrate/substrate), Google provides GKE-optimized deployment tooling and scripts in the [substrate-gke repository](https://github.com/ai-on-gke/substrate-gke), for eligible Google Cloud customers.

## Benefits of Agent Substrate

You can use Agent Substrate to achieve the following goals:

  * **Run untrusted code safely** : Agent Substrate enforces kernel and network isolation so that you can execute AI-generated code without risking your broader infrastructure.
  * **Build long-running, stateful agents** : an agent's working memory and files are preserved across sessions. The agent resumes from the exact point it paused.
  * **Respond to requests in real time** : when a new request triggers a suspended agent, the system restores the agent's state in a fraction of a second.
  * **Reduce compute costs** : you can run more agents on fewer machines by sharing a pool of Worker sandboxes across all your agents. Because idle agents are suspended and not using CPU and memory, you pay for compute only when agents are actively processing tasks.



## Use cases

Agent Substrate is designed to run agents at any scale, from tens to millions of concurrent agents. Here are three example workloads:

  * **Productivity agents** : long-term background assistants that maintain context over weeks. Because these assistants spend the majority of time waiting for triggers, suspending the workloads when not in use reduces compute costs.
  * **Ephemeral sandboxes** : on-demand, isolated environments for executing untrusted LLM-generated code, running tool calls, or analyzing data. Because sandboxes restore in under a second, the system can provide disposable environments for short-lived tasks and release resources when execution finishes.
  * **Coding agents** : AI assistants that hold real-time conversations with developers to write, build, and test code. The agent runs terminal commands and modifies files inside a sandbox. When the agent is idle, the system suspends it until the developer sends another prompt.



## How Agent Substrate works

Agent Substrate is built on Kubernetes, but you don't need to understand Kubernetes to use it. The core concepts of Agent Substrate are the following:

  * **Actor** : a single running instance of an agent.
  * **ActorTemplate** : a configuration blueprint (defining container images, environment variables, and compute resources) that's used to instantiate Actors.
  * **Worker** : a secure sandbox where an active Actor runs.
  * **WorkerPool** : a group of pre-started, idle Workers that are kept ready to receive an Actor.



Because an Actor isn't tied to a specific Worker, the system can suspend idle agents and reuse the freed compute. This architecture lets the system run millions of agents on a limited number of machines.

A typical agent lifecycle follows these steps:

  1. **Routing** : each incoming API request from your application specifies its target Actor. For example, when a user types a new prompt into a chat interface, your application sends a request directed at the specific Actor managing the user's session.
  2. **Resuming** : if the request is for a suspended Actor, the system claims a warm Worker from the WorkerPool and restores the Actor's snapshot onto that Worker.
  3. **Executing** : the system routes the request to this newly active Worker, and the Actor processes the task.
  4. **Suspending** : when the Actor finishes its work and becomes idle, the system takes a fresh snapshot of the Actor's memory and files, saves the snapshot to storage, and releases the empty Worker back to the pool.



## Workload isolation and GKE Sandbox

Agent Substrate uses [gVisor](https://gvisor.dev/) or [Cloud Hypervisor](https://www.cloudhypervisor.org/) to run each workload in a sandbox that isolates the application code from the host kernel. The Agent Substrate installation includes a gVisor runtime for Workers, so that you don't need to configure [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) on the underlying GKE nodes.

## Limitations and requirements

Agent Substrate has the following limitations and requirements:

  * **Cluster version and beta APIs** : Agent Substrate is supported on GKE Standard clusters running version 1.36 (with beta flags enabled) or version 1.37 or later. Versions earlier than 1.36 are unsupported. In addition, GKE requires beta APIs (`podcertificaterequests` and `clustertrustbundles`). If you enable these APIs on an existing cluster that runs version 1.36, you must also replace the existing nodes so that Pod certificate projection is enabled on them. On version 1.37 or later, existing nodes don't need to be replaced.
  * **Workload Identity Federation for GKE** : GKE clusters must have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) enabled. Agent Substrate uses Workload Identity Federation for GKE to authenticate to Google Cloud APIs, such as Cloud Storage for saving agent snapshots.
  * **VM families** : 
    * **Mixed CPU architectures** : Agent Substrate doesn't support general-purpose machine series that run on mixed CPU architectures (such as E2 machine types) because of a known issue with gVisor.
    * **Uniform VM types per Actor template** : mixing VM types within a single `ActorTemplate` (the configuration blueprint used to create Actors) isn't supported. For example, if your cluster has two node pools using C4 and N2 VMs, an `ActorTemplate` must include a node selector that specifies a single VM type (such as C4) to prevent Actors for that template from being split across different machine types.
  * **GPU support** : GPU device passthrough into Actor containers isn't supported. Specifying `nvidia.com/gpu` only places Pods on GPU-enabled nodes, but doesn't pass the GPU device into the Actor container. In addition, gVisor can't snapshot live CUDA contexts.
  * **Networking** : 
    * **Egress policies** : `EgressPolicy` rules (network controls by hostname and IP address) aren't supported, including the following capabilities: 
      * Default deny rules
      * Hostname-based rules
      * Credential injection
    * **Open connections** : open network connections (such as database sessions or connections to MCP servers) aren't preserved when an agent suspends. Your agent code must handle reconnecting to external services when the agent resumes.
  * **Observability and Managed OpenTelemetry** : [Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke) has the following limitations: 
    * Managed OpenTelemetry for GKE is in Preview.
    * Collector connectors aren't supported, which requires using an external proxy meter for telemetry benchmarking.
    * Collector deployments incur memory cache overhead that scales linearly with the number of Pods in large clusters.
    * TLS isn't supported in Managed OpenTelemetry for GKE.
  * **Storage** : the system requires [Cloud Storage](https://docs.cloud.google.com/storage) to save the snapshots of your agents.
  * **Installation environment** : you can't install Agent Substrate in [Cloud Shell](https://docs.cloud.google.com/shell). Cloud Shell has a 5 GB persistent disk storage limit which doesn't provide enough disk space for the installation. You must install Agent Substrate from a local workstation or a virtual machine (VM) with sufficient disk space.



## What's next

  * Learn how to [install Agent Substrate on your GKE cluster](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate).

  * Explore the code that installs Agent Substrate on GKE in the [substrate-gke GitHub repository](https://github.com/ai-on-gke/substrate-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
