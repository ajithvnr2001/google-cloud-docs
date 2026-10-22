---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-architecture/
title: Layer 7 load balancing reference architecture \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:12.808999+00:00
---

# Layer 7 load balancing reference architecture  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Layer 7 load balancing reference architecture Stay organized with collections  Save and categorize content based on your preferences. 

This reference architecture provides a customer-managed Layer 7 load balancing solution in Google Distributed Cloud (GDC) air-gapped. By deploying popular open-source controllers like HAProxy Kubernetes Ingress or NGINX Gateway Fabric on a GDC standard cluster, customers can seamlessly route L7 traffic to hybrid environments. This architecture uses TLS Termination (`Ingress` / `HTTPRoute`) to route traffic based on [Server Name Indication](https://www.cloudflare.com/en-gb/learning/ssl/what-is-sni/) (SNI) to both built-in containerized pods and applications hosted on external virtual machines.

### Features and capabilities

  * **Advanced Layer 7 Routing:** Supports host-based routing, path-based routing, and advanced traffic management such as header-based matching and traffic weighting.
  * **Centralized TLS Management:** Provides centralized TLS management and termination.
  * **Hybrid Environment Support:** Seamlessly routes L7 traffic to both built-in containerized pods and applications hosted on external virtual machines.
  * **Flexible Controller Options:** Offers a choice between modern [NGINX Gateway Fabric](https://docs.nginx.com/nginx-gateway-fabric/) (using Gateway API) or the well-established [HAProxy Ingress Controller](https://www.haproxy.com/documentation/kubernetes-ingress/).
  * **Air-Gapped Readiness:** Integrated with Harbor Registry to store and serve proxy and application images within private, disconnected environments.
  * **Complex Traffic Splitting:** Enables advanced traffic distribution strategies for modern application delivery.



### Architectural principles

  * **Two-Tier Load Balancing Pattern:** This architecture combines GDC's built-in L4 Load Balancer (as the entry point) with a customer-managed L7 Gateway deployed within Kubernetes.
  * **Role-Oriented Separation:** It follows a design that separates responsibilities between infrastructure providers, cluster operators, and developers through specific resources (like `GatewayClass`, `Gateway`, and `HTTPRoute`, or `Ingress`).
  * **Transition to Modern Standards:** The architecture prioritizes the Gateway API for modern routing capabilities while maintaining support for the legacy Ingress API where stability for specific controllers is required.
  * **Customer-Managed Flexibility:** By deploying self-managed controllers, customers gain control over L7 features and configuration that are not natively provided by the GDC managed L4 balancer.
  * **Abstraction of Workload Location:** The architecture treats containerized and VM-based workloads consistently through Kubernetes Service abstractions (standard or headless).



## Conceptual architecture

![Conceptual architecture diagram for Layer 7 load balancing on GDC air-gapped.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/l7-lb-diagram.png)

### Logical architecture

The logical architecture consists of several functional components working in concert to route external traffic to internal or external backends:

  1. **Ingress/Gateway Entry Point:** A **Client** initiates HTTPS requests which first hit the GDC L4 Load Balancer. This built-in balancer serves as the entry point and distributes TCP/443 traffic to the L7 Load Balancer.
  2. **Control Plane:** Ingress or Gateway Controllers (HAProxy or NGINX operators) monitor Kubernetes resources such as `Ingress`, `Gateway`, and `HTTPRoute`
  3. **Data Plane:** Based on the observed resources, the controllers dynamically update the underlying Proxies which perform the actual traffic routing based on SNI-based host routing rules and TLS Termination.
  4. **Backend Services:**
     * **Containerized Pods:** Managed as standard Deployments and exposed with regular Kubernetes Services.
     * **External VMs:** Integrated into the cluster with a headless Kubernetes Service and a custom endpoint (or `EndpointSlice`) containing the VM's direct IP
  5. **Artifact Management:** All images for the proxies and applications are served from a local Harbor Registry to ensure functionality in an air-gapped environment



### Core concepts and technologies

The architecture uses a two-tier load balancing pattern, combining GDC's built-in L4 Load Balancer with a customer-managed L7 Gateway deployed in Kubernetes. The key components include the following:

  * **Client:** An entity initiating HTTPS requests to interact with the applications.
  * **GDC Standard Cluster:** GDC provides a built-in way to create Kubernetes Vanilla Clusters. In this solution, the cluster will host the L7 LB and its controllers, along with the workloads and healess service for external VMs
  * **GDC L4 Load Balancer:** The built-in L4 load balancer serving as the entry point, distributing TCP/443 traffic directly to the Kubernetes Pods running the Ingress or Gateway controllers.
  * **Ingress and Gateway Controllers:** HAProxy or NGINX operators running in the Standard Cluster. For Nginx, they monitor Gateway API resources (like `Gateway` and `HTTPRoute`) and dynamically update the underlying proxies. For HAProxy, they monitor the `Ingress` resources and dynamically update the underlying proxies. 
    * [HAProxy Ingress Controller](https://www.haproxy.com/documentation/kubernetes-ingress/): An Ingress controller for Kubernetes that utilizes HAProxy as a reverse proxy and Layer 7 load balancer, also handling TLS termination.
    * [Nginx Gateway Fabric](https://github.com/nginx/nginx-gateway-fabric): An implementation of the Gateway API using NGINX as the data plane.
  * **Ingress and Gateway (with HTTPRoute):** Standardized Kubernetes resources defining the physical listening port (443) and the SNI-based host routing rules with TLS Termination.
  * **Containerized Workload (Pods):** A standard Kubernetes Deployment exposed internally using a regular Kubernetes `Service`.
  * **VM-based Workload (External):** A workload hosted on an external VM on the project network, exposed to the proxy with a headless Kubernetes `Service` and a custom endpoint containing the VM's direct IP.
  * **Harbor Registry:** A private container registry used to store and serve the proxy and application images in the air-gapped environment.



### Ingress versus Gateway APIs

The Kubernetes networking landscape is transitioning from the legacy _Ingress API_ to the modern _Gateway API_. Understanding the differences between these two is critical for selecting the right architecture for your workloads.

  * **Ingress API:** Historically, Ingress has been the standard for managing external access to HTTP services. It provides host-based and path-based routing, but its design is relatively basic and lacks built-in support for advanced traffic management (for example, header-based matching or traffic weighting) without relying on vendor-specific annotations. Importantly, the Ingress API is now considered **feature-frozen** by the Kubernetes community ([Ingress limitations](https://gateway-api.sigs.k8s.io/concepts/why-gateway-api/#ingress-vs-gateway-api) and [evolution of Kubernetes networking](https://kubernetes.io/blog/2021/04/22/evolving-kubernetes-networking-with-gateway-api/)).

  * **Gateway API:** Often referred to as the _V2_ of Ingress, the Gateway API is a collection of Custom Resource Definitions (CRDs) that provide a more robust and extensible model for service networking. It is designed to be **role-oriented** , separating responsibilities between infrastructure providers (`GatewayClass`), cluster operators (`Gateway`), and developers (`HTTPRoute`/`TLSRoute`) ([Gateway API in GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api?content_ref=is+composed+of+api+resources+that+correspond+to+the+organizational+roles+of+cluster+operator+developer+and+infrastructure+provider)). This separation allows for more granular control and better multi-tenancy support.




In this GDC air-gapped solution, we have purposefully chosen different APIs for the two featured controllers:

  * **NGINX (Gateway API):** For the NGINX implementation, we utilize **NGINX Gateway Fabric** , which is a mature and built-in implementation of the Gateway API. Leveraging the Gateway API for NGINX allows customers to benefit from the modern standards and advanced routing capabilities (like `HTTPRoute`) that are built in to the API.
  * **HAProxy (Ingress API):** Although the Gateway API is the strategic direction, we have selected the **Ingress API** for HAProxy in this guide. This is because _HAProxy's Gateway API integration isn't considered mature_. By using the well-established HAProxy Ingress Controller, we ensure a stable and reliable L7 solution for customers who prefer HAProxy, while still providing a path toward modern L7 capabilities.



## Assumptions and constraints

### Assumptions

  * **Infrastructure Readiness:** The deployment assumes the availability of GDC air-gapped 1.15.x Standard Clusters.
  * **Local Registry:** It is assumed that a local Harbor Registry is correctly configured to store and serve proxy and application images in the air-gapped environment.
  * **Native Entry Point:** Traffic is assumed to first hit the built-in GDC L4 Load Balancer, which then distributes traffic to the L7 proxies.



### Constraints

  * **Customer-Managed Solution:** There is no managed, SLA-backed L7 service in GDC; this implementation is entirely self-managed by the customer.
  * **Standard Clusters Only:** Shared User Clusters are out of scope due to the high privileges required for Ingress and Gateway Controller deployment.
  * **API Maturity:** While NGINX uses the modern Gateway API, HAProxy is constrained to the Ingress API because its Gateway API integration is not yet considered mature.
  * **Air-gapped Maintenance:** All container images must be manually promoted and managed within the local Harbor registry.
  * **Community Editions:** The architecture is designed for open-source community editions of Nginx and HAProxy. Enterprise Editions may work but have not been explicitly tested.
  * **Operational Ownership:** Customers must manage their own scaling, high availability, and patching for the third-party controllers.
  * **Support Boundary:** Google support covers only the underlying GDC infrastructure; issues with HAProxy or NGINX software itself are the customer's or vendor's responsibility.
  * **API Obsolescence:** The Ingress API (used for HAProxy) is feature-frozen by the Kubernetes community, which may limit future routing capabilities.



### Licensing

  * **Community Editions:** The architecture is designed for open-source community editions (typically Apache 2.0 or similar), which are free to use but customer-managed.
  * **Enterprise Procurement:** Procurement and management of commercial licenses, such as NGINX Plus or HAProxy Enterprise, are the sole responsibility of the customer.



## Additional materials

  * [Nginx Layer 7 Load Balancing on GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-nginx-impl)
  * [HAProxy Layer 7 Load Balancing on GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-haproxy-impl)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
