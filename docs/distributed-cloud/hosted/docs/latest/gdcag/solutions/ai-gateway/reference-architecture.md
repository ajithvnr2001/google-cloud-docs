---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/reference-architecture/
title: AI Gateway reference architecture on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:14:27.193984+00:00
---

# AI Gateway reference architecture on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/reference-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  AI Gateway reference architecture on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

### Problem Statement

Organizations that run Large Language Models (LLMs) in air-gapped environments quickly accumulate model endpoints: every open weight model served on Google Distributed Cloud (GDC) air-gapped (see the companion guide set Open Weight Models on GDC air-gapped) exposes its own Kubernetes `Service`, its own address, its own credentials and its own operational lifecycle. Application and agent developers end up in architectural silos, hard-coding one endpoint per model and rewriting integrations with every model iteration. This fragmentation creates technical debt and slows down the deployment of mission-critical, multi-step agentic workloads.

Standard networking layers are also "AI-blind": a conventional load balancer treats inference traffic like generic HTTP and can't read the `model` field of a request, prioritize latency-sensitive workloads, account for tokens instead of requests, or steer a request to the model server replica that already holds the relevant KV cache. In high-cost air-gapped GPU clusters this leads to hardware underutilization and a poor return on investment. While [Gemini on GDC](https://cloud.google.com/distributed-cloud-air-gapped) provides managed frontier models, customers who combine them with self-hosted open weight models need an inference layer that offers cloud-like agility without compromising data sovereignty: no request, prompt or model weight may leave the GDC boundary.

### Proposed solution

This document outlines the reference architecture for a self-managed AI gateway on GDC air-gapped: a secure, centralized inference layer that gives applications one OpenAI-compatible endpoint for all models and routes each request to the right backend. The reference implementation builds on the Kubernetes Gateway API: Envoy Gateway is the Gateway API implementation (control plane and Envoy proxy data plane) and Envoy Agent Router (formerly Envoy AI Gateway) extends it with AI-specific request processing: model extraction from the request body, request and response translation, upstream authentication, token accounting and, optionally, token-based rate limiting. The Gateway API Inference Extension adds model-server-aware endpoint selection (`InferencePool` and Endpoint Picker) so that GPU capacity is used efficiently. All artifacts are staged in the Harbor registry of the GDC organization and the whole stack runs in a standard cluster without any external connectivity.

**What is included:** This architecture covers the deployment of Envoy Gateway and Envoy Agent Router in a standard cluster, the Gateway API resources (`GatewayClass`, `Gateway`) and Envoy Agent Router resources (`AIGatewayRoute`, `AIServiceBackend`, `BackendSecurityPolicy`, `GatewayConfig`) that expose a unified OpenAI-compatible endpoint, body-based routing on the `model` field, the Gateway API Inference Extension (`InferencePool`, `InferenceObjective`, Endpoint Picker) for model-aware load balancing, optional token-based rate limiting with Redis, TLS termination at the gateway, network policies (`NetworkPolicy` / `ProjectNetworkPolicy`) and the air-gapped artifact management in Harbor. The model serving backends behind the gateway (Ollama, vLLM) are deployed with the companion guide set Open Weight Models on GDC air-gapped.

**What isn't included:** This architecture doesn't cover a managed AI gateway product, the deployment and tuning of the models themselves (companion guide set), model fine-tuning, non-LLM GenAI modalities, agent-to-tool traffic (`MCPRoute`) or commercially supported gateway distributions. Gemini on GDC is a managed product capability; its provisioning is out of scope and this version of the guide set validates the gateway with self-hosted open weight models.

**Audience:** The primary audience for this document includes Platform Administrators responsible for deploying and operating the gateway in a standard cluster and technical architects designing AI platforms within the air-gapped environment. Application developers who consume the unified endpoint are a secondary audience who benefit from understanding how their requests are routed.

## Architecture

The solution runs entirely in a standard cluster of the GDC air-gapped organization. In the Services layer the Kubernetes Gateway API standardizes the configuration model; the AI gateway control plane (the Envoy Gateway controller and the Envoy Agent Router controller) reads the Gateway API and Envoy Agent Router resources and configures the data plane: an Envoy proxy `Deployment` that is the request entry point (exposed through a `Service` of type `LoadBalancer`) and the Envoy Agent Router external processor that runs as a sidecar in the proxy `Pod` and executes the AI-specific logic. In the Application layer, customer workloads (applications and agents) send an AI request to the proxy (1), the proxy hands the request to the external processor, which extracts the model name, translates the request and records token usage (2), the proxy forwards the balanced traffic to the inference `Pod`s of the selected model (3), and the model runs on the GPU nodes of the Infrastructure layer (4). Model serving backends are attached to the gateway either as an `AIServiceBackend` (any OpenAI-compatible `Service`) or as an `InferencePool` whose Endpoint Picker selects the best replica per request. Container images and Helm charts are pulled from Harbor.

![AI Gateway reference architecture on GDC air-gapped.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/ai-gateway-architecture.png)

## Solution components

The solution uses the following components:

Solution Component | Responsibilities | Data Flow | Interfaces  
---|---|---|---  
**Kubernetes Gateway API** | Standard, role-oriented resource model for ingress and routing: `GatewayClass` (owned by the platform), `Gateway` (listeners, TLS) and route resources (owned by application teams). Successor of the Ingress API without vendor-specific annotations. | Declarative configuration only; the resources are watched by the controllers and carry no request traffic. | Kubernetes API (`gateway.networking.k8s.io/v1`); the CRDs are installed from the Envoy Gateway CRD chart.  
**Envoy Gateway controller (control plane)** | Implements the Gateway API: provisions one Envoy proxy `Deployment` and `LoadBalancer` `Service` per `Gateway`, translates routes and policies (`BackendTrafficPolicy`, `SecurityPolicy`, `EnvoyExtensionPolicy`, `Backend`, `EnvoyProxy`) into xDS configuration, runs the global rate limit service when configured, and calls the Envoy Agent Router extension server through its extension manager so that `InferencePool` backends are added to the translation. | Watches the Kubernetes API and pushes xDS configuration to the proxies; no request traffic. | Kubernetes API (watch), xDS gRPC towards the proxies, gRPC towards the extension server (port 1063).  
**Envoy Agent Router controller (control plane)** | Reconciles the `aigateway.envoyproxy.io/v1beta1` resources, `AIGatewayRoute` (routing rules on the extracted model name), `AIServiceBackend` (a backend with its API schema), `BackendSecurityPolicy` (upstream credentials) and `GatewayConfig` (external processor settings per `Gateway`), into Envoy Gateway resources, injects the external processor sidecar into the Envoy proxy `Pod`s and serves the extension server used by Envoy Gateway. | Configuration only. | Kubernetes API, gRPC extension server (port 1063), mutating admission webhook for the sidecar injection.  
**Envoy proxy (data plane)** | Request entry point: terminates TLS, matches listeners and routes, load-balances across backend endpoints, enforces rate limits and timeouts, retries and falls back to alternative backends, and emits access logs and metrics. | Receives client requests on the `LoadBalancer` VIP (80/443), consults the external processor for every AI request, forwards the request to the selected backend endpoint (a `Service` or the `Pod` chosen by the Endpoint Picker) and streams the response back to the client. | HTTP/HTTPS towards clients (OpenAI-compatible API), ext_proc gRPC towards the sidecar and the Endpoint Picker, HTTP towards the backends, gRPC towards the rate limit service.  
**Envoy Agent Router external processor (ExtProc)** | Parses the OpenAI-compatible request body, extracts the `model` field into the routing header `x-ai-eg-model`, applies model name overrides, translates request and response payloads between the client API schema and the backend API schema, injects the upstream credentials defined by `BackendSecurityPolicy`, and extracts token usage (input, output, total) from the response into dynamic metadata used for token-based rate limiting and metrics. | Sidecar container in the Envoy proxy `Pod`; processes request and response bodies, including streamed responses. | Envoy ext_proc gRPC; Prometheus metrics endpoint.  
**Gateway API Inference Extension (InferencePool + Endpoint Picker)** | `InferencePool` (`inference.networking.k8s.io/v1`) groups the `Pod`s of one model server deployment (label selector, target port, for example 8000) and references its Endpoint Picker (EPP). `InferenceObjective` (`v1alpha2`) assigns a priority per model or objective. The EPP scrapes the model server metrics (request queue depth, KV-cache utilization, loaded LoRA adapters) and selects the endpoint for every request. | The proxy calls the EPP (ext_proc, port 9002) with the request headers; the EPP answers with the endpoint to use; the proxy forwards the request to that `Pod`. | Kubernetes API (CRDs), gRPC ext_proc (9002), Prometheus scrape of the model servers.  
**Redis (optional)** | Backing store of the Envoy rate limit service: shared counters for request-based and token-based limits across all proxy replicas. Only needed when global rate limiting is configured. | The rate limit service reads and increments counters on port 6379 for every limited request. | Redis protocol (6379). Redis 8.10 deployed in the cluster, or an existing Redis instance.  
**Model serving backends (Ollama / vLLM)** | Serve the open weight models behind the gateway; deployed with the companion guide set Open Weight Models on GDC air-gapped. Attached as an `AIServiceBackend` (any OpenAI-compatible `Service`, for example Ollama) or as an `InferencePool` (model servers such as vLLM that expose the metrics the Endpoint Picker scores on). | Receive the routed requests from the proxy, run inference on the GPU nodes (or on CPU for functional evaluation with small models) and return the OpenAI-compatible response. | OpenAI-compatible REST API: vLLM on port 8000, Ollama on port 11434; Prometheus metrics (vLLM) for the Endpoint Picker.  
**Harbor** | Stores the container images (Envoy proxy, Envoy Gateway, Envoy Agent Router controller and external processor, rate limit service, Endpoint Picker, Redis) and the Helm charts (OCI artifacts) of the solution. | Artifacts are copied from the public registries into Harbor with `seed_registry.sh` (`crane`) from a workstation with internet access; the cluster pulls images with a robot account through image pull secrets and the charts are rendered from Harbor with `helm template`. | OCI Distribution API; Harbor UI and robot accounts.  
**Standard cluster and GPU nodes** | Hosts all gateway components (CPU nodes are sufficient) and the inference `Pod`s (GPU nodes with the accelerator resources discovered from the nodes). Provides `LoadBalancer` VIPs, persistent storage for the model weights and the network policy enforcement. | Foundational platform; requests enter through the `LoadBalancer` VIP of the `Gateway` and stay inside the cluster network. | Kubernetes API, GDC networking APIs (`networking.gdc.goog/v1` `ProjectNetworkPolicy`), GDC console and `gdcloud` for the Platform Administrator.  
**Note:** Backends attached as an `AIServiceBackend` (for example Ollama) are load-balanced by the proxy across the endpoints of their `Service`; model-server-aware endpoint selection (queue depth, KV cache, priorities) requires an `InferencePool` whose model servers expose vLLM-compatible metrics.

### Features and capabilities

This reference architecture provides the following core capabilities:

  * **Unified OpenAI-compatible endpoint:** Applications call one address (`/v1/chat/completions`, `/v1/models`, …) for every model served behind the gateway. 
    * _Components:_ `Gateway`, `AIGatewayRoute`, Envoy proxy, external processor.
    * _Responsibilities:_ Exposing a stable virtual IP, terminating TLS, accepting the OpenAI-compatible request format and translating it to the backend schema when needed.
    * _Interfaces:_ HTTPS REST (JSON, including server-sent events for streaming).
  * **Body-based (model-aware) routing:** The gateway reads the `model` field of the request body and routes the request to the matching backend without any client-side endpoint logic. 
    * _Components:_ External processor, `AIGatewayRoute` rules matching on `x-ai-eg-model`, `AIServiceBackend`, `InferencePool`.
    * _Responsibilities:_ Extracting the model name, matching route rules, renaming models (`modelNameOverride`), splitting traffic by weight and falling back to alternative backends by priority.
    * _Interfaces:_ Kubernetes API (`aigateway.envoyproxy.io/v1beta1`).
  * **Model-server-aware load balancing:** Requests to an `InferencePool` are sent to the replica with the shortest queue and the most useful KV cache instead of round robin. 
    * _Components:_ Gateway API Inference Extension (`InferencePool`, `InferenceObjective`, Endpoint Picker).
    * _Responsibilities:_ Scraping model server metrics, scoring endpoints (queue depth, KV-cache utilization, prefix-cache affinity, LoRA adapters), honoring per-objective priorities under load.
    * _Interfaces:_ Kubernetes API (`inference.networking.k8s.io/v1`, `inference.networking.x-k8s.io/v1alpha2`), ext_proc gRPC (9002).
  * **Upstream authentication and security policies:** Credentials for backends that require them are injected by the gateway and never distributed to the applications. 
    * _Components:_ `BackendSecurityPolicy`, Envoy Gateway `SecurityPolicy`, TLS listeners.
    * _Responsibilities:_ Injecting API keys towards the backends, terminating client TLS at the `Gateway`, enforcing client authentication and authorization policies when required.
    * _Interfaces:_ Kubernetes `Secret`s referenced by the policies.
  * **Token-based rate limiting (optional):** Usage is measured in tokens, not only in requests. 
    * _Components:_ External processor (`llmRequestCosts`), Envoy Gateway `BackendTrafficPolicy` (global rate limit), rate limit service, Redis.
    * _Responsibilities:_ Extracting input, output and total tokens from every response, attaching them as request costs, enforcing per-consumer or per-model budgets across all proxy replicas.
    * _Interfaces:_ Kubernetes API, Redis (6379).
  * **Traffic management:** Standard Gateway API capabilities apply to AI traffic. 
    * _Components:_ `Gateway`, `HTTPRoute`, `AIGatewayRoute`, `BackendTrafficPolicy`.
    * _Responsibilities:_ Host-, path- and header-based matching, timeouts suited to long generations, retries, weighted traffic splitting and priority-based fallback between backends.
    * _Interfaces:_ Kubernetes API.
  * **Observability:** Request, latency and token metrics are available for every model. 
    * _Components:_ Envoy proxy access logs and statistics, external processor metrics (token usage, request duration, time to first token), Endpoint Picker metrics.
    * _Responsibilities:_ Exposing Prometheus-format metrics and structured access logs that the GDC observability stack or a customer-managed Prometheus can scrape.
    * _Interfaces:_ Prometheus metrics endpoints, standard output logs.
  * **Air-gapped artifact management:** Every image and chart is staged in Harbor before installation. 
    * _Components:_ Harbor, `seed_registry.sh`, robot accounts, image pull secrets, `EnvoyProxy` resource (proxy image and pull secret).
    * _Responsibilities:_ Seeding images and OCI Helm charts from a connected workstation, pinning versions, rendering charts offline with `helm template`.
    * _Interfaces:_ OCI Distribution API, Kubernetes API.



### Architectural principles

  * **Standards First** : The gateway is configured through the Kubernetes Gateway API and its Inference Extension and speaks the OpenAI-compatible API towards applications, so applications, routes and backends stay portable across gateway implementations.
  * **Security First** : All components and data reside within the GDC air-gapped boundary. TLS terminates at the `Gateway`, backend credentials are injected by the gateway, and network access is restricted with `NetworkPolicy` and `ProjectNetworkPolicy` objects.
  * **Data Sovereignty** : Prompts, responses, model weights and usage data never leave the customer's GDC organization; no external connectivity is required for operation.
  * **Separation of Concerns** : The role-oriented Gateway API lets the Platform Administrator own the `GatewayClass`, `Gateway`, TLS and network policies while application teams own their `AIGatewayRoute`, `AIServiceBackend` and `InferencePool` resources in their own namespaces.
  * **Decoupled Control and Data Plane** : Controllers only translate configuration; the request path consists of the Envoy proxy, its external processor sidecar and the Endpoint Picker, which keep serving traffic if a controller restarts.
  * **Open & Flexible**: The architecture uses open-source software throughout (Envoy Gateway, Envoy Agent Router, Gateway API Inference Extension, Ollama, vLLM) and the same Gateway API resources can be served by alternative implementations.
  * **Scalability & Performance**: The data plane scales horizontally by adding proxy replicas and vertically by adjusting CPU and memory; model-server-aware load balancing keeps the GPUs saturated without overloading individual replicas.
  * **Simplified End User Experience** : One endpoint, one API format and one credential for every model shorten the path from model deployment to consumption.
  * **Resilience** : Kubernetes health checks and replication, Envoy retries and priority-based fallback between backends keep the endpoint available when individual model replicas fail.



## Considerations

  * **Scalability and Performance:**
    * The gateway components are CPU-only workloads; the Envoy proxy `Deployment` of a `Gateway` scales horizontally by increasing its replica count (`EnvoyProxy` resource) and vertically by raising CPU and memory requests. Body inspection by the external processor costs CPU proportional to request and response size; streamed responses are processed incrementally.
    * Model-server-aware load balancing only applies to backends attached as an `InferencePool`; backends attached as an `AIServiceBackend` are load-balanced by the proxy across the endpoints of their `Service`.
    * The gateway doesn't add GPU capacity: throughput and latency are bounded by the model servers. Size the model deployments with the companion guide set (vLLM for high throughput, Ollama for ease of use and CPU-only evaluation).
    * Long generations need longer request and idle timeouts than typical HTTP APIs; configure them on the routes and policies rather than on the clients.
  * **Resource Management:**
    * All gateway components run on CPU nodes and need no accelerator; the following table gives indicative sizing for a functional deployment. The reference implementation sets the exact requests and limits; production values depend on request rate and payload sizes.
    * The port table that follows lists every port the network policies must admit.
    * GPU planning belongs to the model deployments: the accelerator resource names are discovered from the nodes as described in the companion guide set.



**Indicative sizing of the gateway components (CPU only)**

Component | Replicas | CPU (request) | Memory (request) | Notes  
---|---|---|---|---  
Envoy Gateway controller | 1 | 100m–500m | 256Mi–1Gi | Control plane; not in the request path  
Envoy Agent Router controller | 1 | 100m–500m | 256Mi–512Mi | Control plane and extension server  
Envoy proxy `Pod` (proxy + external processor sidecar) | 1–2 per `Gateway` | 500m–2 | 512Mi–2Gi | Scale with request rate and payload size  
Endpoint Picker | 1 per `InferencePool` | 100m–500m | 256Mi–512Mi | Scrapes the model server metrics  
Rate limit service (optional) | 1 | 100m–500m | 256Mi–512Mi | Only with global rate limiting  
Redis (optional) | 1 | 100m–500m | 256Mi–1Gi | Only with global rate limiting  
  
### Network ports

Port | Component | Purpose  
---|---|---  
80 / 443 | Envoy proxy (`Gateway` listeners) | HTTP / HTTPS entry point on the `LoadBalancer` VIP  
1063 | Envoy Agent Router controller (extension server) | gRPC calls from the Envoy Gateway extension manager  
9002 | Endpoint Picker | ext_proc gRPC calls from the Envoy proxy  
6379 | Redis | Rate limit counters  
8000 | vLLM | OpenAI-compatible API and metrics of the model server  
11434 | Ollama | Ollama and OpenAI-compatible API of the model server  
  
  * **Availability and Reliability:**
    * The proxy and the external processor run in the same `Pod`; multiple replicas behind the `LoadBalancer` `Service` mask individual `Pod` failures, and the controllers can restart without interrupting traffic.
    * `AIGatewayRoute` rules can list several backends with priorities so that the gateway falls back to another replica set or model server when a backend is unhealthy.
    * The Endpoint Picker is a per-pool `Deployment`; if it is unavailable, requests to that `InferencePool` fail until it is back. Run it with resource requests and readiness probes and monitor it like a data plane component.
    * Redis holds only rate limit counters; a Redis outage affects rate limiting, not routing.
  * **Operational Complexity:**
    * Version alignment between Envoy Gateway, Envoy Agent Router and the Gateway API Inference Extension: upgrade the three together with the tested combination (Envoy Gateway 1.8.4, Envoy Agent Router 1.1.0, Gateway API Inference Extension 1.5.0).
    * Air-gapped lifecycle: every image and chart is re-seeded into Harbor for each upgrade; the `EnvoyProxy` resource and the chart values pin the registry and the pull secret.
    * Two configuration layers: platform-owned `GatewayClass` / `Gateway` / `EnvoyProxy` and team-owned `AIGatewayRoute` / `AIServiceBackend` / `InferencePool`; onboarding a new model means adding a route rule and a backend, not a new gateway.
    * Monitoring: request rate, latency (including time to first token), token usage per model and per consumer, Endpoint Picker scoring, and GPU utilization of the model servers.
    * `InferenceObjective` is still an alpha API (`v1alpha2`); expect schema changes between releases of the Inference Extension.
  * **Security and Compliance:**
    * The entire solution operates within the GDC air-gapped security perimeter.
    * Network policies are mandatory: a namespace `NetworkPolicy` admits traffic from the proxy to the model server ports (8000, 11434) and to the Endpoint Picker (9002), and a `ProjectNetworkPolicy` admits client traffic to the `LoadBalancer` VIP when consumers reside outside the project.
    * TLS terminates at the `Gateway` with a certificate stored in a Kubernetes `Secret`; clients only ever see the gateway endpoint.
    * Upstream credentials (for example an API key required by a model server) are stored in `Secret`s referenced by a `BackendSecurityPolicy` and injected by the gateway, so applications never hold backend credentials.
    * Token-based rate limiting bounds the consumption of expensive GPU capacity per consumer or per model.
    * Harbor robot accounts and Kubernetes image pull secrets ensure secure access to container images; role-oriented Gateway API RBAC separates platform and application responsibilities.



## Design decisions

The following key design decisions have been made for this reference architecture:

**Decision 1: AI gateway implementation: open-source Envoy Agent Router on Envoy Gateway versus alternative distributions**

Context | Key Decision | Rationale  
---|---|---  
The AI gateway is the primary architectural choice with viable alternatives, from self-managed open-source options to commercially supported offerings: (a) Envoy Agent Router on Envoy Gateway (open source), (b) kgateway and [agentgateway](https://agentgateway.dev/) (open-source Gateway API implementations that also handle LLM provider traffic, MCP tools and agent-to-agent communication in one data plane, optionally with vendor support from solo.io), (c) Solo Enterprise for agentgateway as the commercially supported premium option. | The reference implementation uses the open-source Envoy Agent Router on Envoy Gateway. The alternatives remain valid choices behind the same Gateway API resources; a commercially supported distribution is recommended for production environments that require dedicated vendor support. | Open-source advantages: lightweight and standards-conformant, high-performance L7 routing, no licensing fees, ideal to evaluate the solution before committing to a paid offering; Envoy Agent Router is the option validated in this guide set. Open-source disadvantages: support is best effort by the Solutions team and community-driven, which may not satisfy core production environments. Premium advantages: enterprise support agreements for the gateway lifecycle and, often, advanced agentic capabilities. Premium disadvantages: paid licensing or support agreement and an additional vendor relationship.  
  
**Decision 2: Kubernetes Gateway API with the Inference Extension versus Ingress or a proprietary gateway API**

Context | Key Decision | Rationale  
---|---|---  
Inference endpoints can be exposed with the legacy Ingress API, a gateway-specific configuration format, or the Kubernetes Gateway API. Model-aware load balancing additionally needs a way to describe model server pools and their priorities. | The solution standardizes on the Kubernetes Gateway API (`GatewayClass`, `Gateway`, routes) implemented by Envoy Gateway, and on the Gateway API Inference Extension (`InferencePool`, `InferenceObjective`, Endpoint Picker) for model-aware routing. | The Gateway API is the Kubernetes standard that succeeds Ingress, is role-oriented (platform versus application teams) and portable across implementations. The Inference Extension is the community standard for model-server-aware routing (queue depth, KV cache, priorities) and is supported by Envoy Agent Router out of the box; the alternative gateway distributions implement the same APIs, which keeps Decision 1 reversible.  
  
**Decision 3: Body-based routing on the`model` field of OpenAI-compatible requests as the unified endpoint**

Context | Key Decision | Rationale  
---|---|---  
Applications can address models through one endpoint per model (host- or path-based), through a custom header set by the client, or through the `model` field that every OpenAI-compatible request already carries. | The gateway exposes one OpenAI-compatible endpoint and routes on the `model` field: the external processor extracts it into the `x-ai-eg-model` header and `AIGatewayRoute` rules match on that header. | Existing OpenAI-compatible clients and SDKs work unchanged and switch models by changing one string; endpoints, credentials and model placement can change without touching applications; the same rules can map a model name to several backends for traffic splitting, fallback or model name overrides.  
  
**Decision 4: Air-gapped artifact seeding into Harbor versus on-demand pulls**

Context | Key Decision | Rationale  
---|---|---  
The upstream installation pulls container images from public registries and Helm charts as OCI artifacts on demand, which is impossible in an air-gapped environment. | All container images (Envoy proxy, Envoy Gateway, Envoy Agent Router controller and external processor, rate limit service, Endpoint Picker, Redis) and the Envoy Gateway and Envoy Agent Router Helm charts are seeded into a Harbor project with `seed_registry.sh` (`crane`), charts are rendered offline with `helm template` from Harbor, and the `EnvoyProxy` resource and the chart values pin the Harbor registry and the pull secret. | One repeatable, auditable seeding step per version; the cluster never needs external connectivity; version pinning makes upgrades explicit and reversible.  
  
**Decision 5: Optional token-based rate limiting with Redis versus request-based limits only**

Context | Key Decision | Rationale  
---|---|---  
GPU capacity is consumed per token, not per request; a request-count limit can't protect a shared model from a few very large prompts or long generations. Global rate limiting in Envoy Gateway needs a shared counter store. | Token-based rate limiting is an optional feature of the architecture: the external processor records input, output and total tokens per request (`llmRequestCosts`), a `BackendTrafficPolicy` enforces the budget, and a Redis instance (Redis 8.10, deployed in the cluster or an existing instance) stores the counters. Deployments without rate limiting don't need Redis. | Usage is measured in the unit that reflects cost, budgets are enforced consistently across all proxy replicas, and the dependency is only paid for by customers who need quotas.  
  
**Decision 6: Topology: gateway control and data plane in a dedicated namespace of a standard cluster, models in application namespaces**

Context | Key Decision | Rationale  
---|---|---  
The gateway could run in a dedicated cluster, in every application namespace, or once per standard cluster next to the models it fronts. Open weight models on GDC air-gapped are deployed in standard clusters (companion guide set). | The Envoy Gateway and Envoy Agent Router control plane and the Envoy proxy data plane run in a dedicated namespace of the standard cluster that hosts the models; `AIGatewayRoute`, `AIServiceBackend`, `InferencePool` and the model deployments live in the application namespaces and are referenced across namespaces. | Requests stay inside the cluster network between the proxy and the model `Pod`s (lowest latency, no additional load balancers), the Platform Administrator owns the gateway namespace while application teams own their routes and models, and the Endpoint Picker can scrape the model servers directly. A per-project client gateway that forwards to a central server gateway remains an extension of this topology for multi-project consumption.  
  
## Assumptions and limitations

  * GDC air-gapped 1.16.2-hf1 or later environment is available with a standard cluster that runs Kubernetes v1.32.13-gke.400 or later.
  * Sufficient hardware resources (especially GPUs) are present for the model serving backends; the gateway components themselves run on CPU nodes. Real models need GPUs; small models on Ollama can run on CPU for functional evaluation only.
  * Harbor instance is set up and accessible, and a workstation with internet access and connectivity to the GDC environment (Harbor and Kubernetes API) is available for seeding images and charts.
  * Users have the necessary permissions: project roles Harbor Instance Viewer and Standard Cluster Admin plus a `StandardClusterRoleBinding` to the `cluster-admin` role on the standard cluster for the cluster-scoped installation (CRDs, `GatewayClass`, namespaces), see the reference implementation.
  * The model serving backends expose an OpenAI-compatible API; backends attached as an `InferencePool` also expose the vLLM-compatible metrics the Endpoint Picker relies on.
  * **Limitation:** support for the open-source components (Envoy Gateway, Envoy Agent Router, Gateway API Inference Extension) is best effort by the Solutions team; dedicated vendor support requires a commercially supported distribution (Decision 1).
  * **Limitation:** `InferenceObjective` is an alpha API (`inference.networking.x-k8s.io/v1alpha2`) and may change between releases of the Inference Extension.
  * **Limitation:** a `LoadBalancer` VIP for the `Gateway` and a `ProjectNetworkPolicy` are required for consumers outside the project; inside the project, in-cluster clients or `kubectl port-forward` can reach the gateway `Service` directly.
  * **Limitation:** Gemini on GDC, model fine-tuning, non-LLM GenAI models and multi-node model serving are out of scope for this version of the solution.



### User flow

The following is a comprehensive user flow for the AI gateway on GDC air-gapped: first the request path that an application developer relies on, then the setup path the Platform Administrator follows.

### 1\. Developer request path

An application or agent needs nothing but the gateway endpoint, a client credential if the gateway enforces one, and the model name.

  * **Send the request:** The application calls `POST /v1/chat/completions` on the gateway endpoint with an OpenAI-compatible JSON body that names the model (for example `"model": "gemma"`), exactly as it would call any OpenAI-compatible service.
  * **Enter the gateway:** The request reaches the `LoadBalancer` VIP of the `Gateway`; the Envoy proxy terminates TLS and matches the listener and route.
  * **Process the body:** The proxy hands the request to the Envoy Agent Router external processor, which parses the body, extracts the model name into the `x-ai-eg-model` header and translates the payload to the backend schema if it differs.
  * **Select the backend:** The `AIGatewayRoute` rule that matches the model name selects an `AIServiceBackend` (for example the Ollama `Service`) or an `InferencePool` (for example a vLLM replica set); for an `InferencePool`, the Endpoint Picker chooses the replica with the shortest queue and the best KV-cache match.
  * **Forward and respond:** The proxy injects upstream credentials when a `BackendSecurityPolicy` applies, forwards the request to the chosen `Pod`, streams the response back and lets the external processor record the token usage, which feeds the metrics and, when configured, the token-based rate limit.
  * **Switch models:** To use another model the developer changes the `model` string; no new endpoint, credential or client library is needed.



### 2\. Platform Administrator setup path

  * **Seed artifacts into Harbor:** Create the Harbor robot accounts, then copy the container images and the Envoy Gateway and Envoy Agent Router Helm charts into Harbor with `seed_registry.sh` from a workstation with internet access.
  * **Install Envoy Gateway:** Render the CRD and controller charts from Harbor with `helm template` and apply them in the gateway namespace; create the `EnvoyProxy` resource that pins the proxy image and pull secret and verify the controller with a basic `GatewayClass`, `Gateway` and `HTTPRoute`.
  * **Install Envoy Agent Router:** Install the Envoy Agent Router CRDs and the Gateway API Inference Extension CRDs, deploy the Envoy Agent Router controller, and reconfigure Envoy Gateway to call its extension server (port 1063) and to accept `InferencePool` backends; optionally deploy Redis and enable the global rate limit service.
  * **Expose the gateway:** Create the `GatewayClass` and the `Gateway` with HTTP and HTTPS listeners (TLS certificate `Secret`), wait for the `LoadBalancer` VIP, and apply the `ProjectNetworkPolicy` for consumers outside the project.
  * **Attach models:** Deploy the model serving backends with the companion guide set, then create `AIServiceBackend` resources for OpenAI-compatible `Service`s and `InferencePool` plus Endpoint Picker resources for vLLM-compatible replica sets, together with the namespace `NetworkPolicy` objects.
  * **Publish the route:** Create the `AIGatewayRoute` with one rule per model name (body-based routing) and, where needed, `BackendSecurityPolicy` and `BackendTrafficPolicy` objects for upstream credentials and token budgets.
  * **Validate and operate:** Call `/v1/models` and `/v1/chat/completions` through the VIP (or a `kubectl port-forward` fallback), check the proxy, external processor and Endpoint Picker metrics, and hand the endpoint and model names to the application teams. Scale proxy replicas and model deployments independently; upgrade Envoy Gateway, Envoy Agent Router and the Inference Extension together.



The detailed steps are provided in the [Envoy Agent Router reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/envoy/reference-implementation) and [Body-based routing with Envoy Agent Router user guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/envoy/body-based-routing).

## Additional materials

  * [Envoy Agent Router reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/envoy/reference-implementation)
  * [Body-based routing with Envoy Agent Router user guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/envoy/body-based-routing)
  * [Open-weight LLMs reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-llm-architecture)
  * [Envoy Agent Router documentation](https://aigateway.envoyproxy.io/docs)
  * [Envoy Gateway](https://gateway.envoyproxy.io/)
  * [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/)
  * [Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/)
  * [Google Distributed Cloud air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
