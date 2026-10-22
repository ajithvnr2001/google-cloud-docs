---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview/
title: Architectural overview of Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:43.517057+00:00
---

# Architectural overview of Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Architectural overview of Knative serving Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an architectural overview of Knative serving and covers the changes that occur when you enable Knative serving in your Google Kubernetes Engine cluster. 

This information is useful for the following types of users:

  * Users getting started with Knative serving.
  * Operators with experience in running GKE clusters.
  * Application developers who need to know more about how Knative serving integrates with Kubernetes clusters to design better applications or configure their Knative serving application.



## Components in the default installation

Install [Knative serving](https://knative.dev/docs) into your cluster to connect and manage your stateless workloads. Knative components are created in the `knative-serving` namespace.

Knative serving uses Cloud Service Mesh to route traffic. By default, Cloud Service Mesh installs components in the `istio-system` namespace.

Here's a list of the components installed by Knative serving and Cloud Service Mesh:

  * Components installed by Knative serving in the `knative-serving` namespace:

    * **Activator** : When [pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/) are scaled in to zero or become overloaded with requests sent to the revision, Activator temporarily queues the requests and sends metrics to Autoscaler to spin up more pods. Once Autoscaler scales the revision based on the reported metrics and available pods, Activator forwards queued requests to the revision. Activator is a data plane component; data plane components manage all functions and processes forwarding user traffic.
    * **Autoscaler** : Aggregates and processes metrics from Activator and the queue proxy sidecar container, a component in the data plane that enforces request concurrency limits. Autoscaler then calculates the observed concurrency for the revision and adjusts the size of the deployment based on the desired pod count. When pods are available in the revision, Autoscaler is a control plane component; otherwise, when pods are scaled in to zero, Autoscaler is a data plane component.
    * **Controller** : Creates and updates the child resources of Autoscaler and the Service objects. Controller is a control plane component; control plane components manage all functions and processes establishing the request path of user traffic.
    * **Metrics Collector** : Collects metrics from Knative serving components then forwards them to Cloud Monitoring.
    * **Webhook** : Sets default values, rejects inconsistent and invalid objects, and [validates](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook) and [mutates](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook) Kubernetes API calls against Knative serving resources. Webhook is a control plane component.
  * Components installed by Cloud Service Mesh running in the `istio-system` namespace:

    * **Cluster Local Gateway** : Load balancer in the data plane responsible for handling internal traffic that arrives from one Knative serving service to another. The Cluster Local Gateway can only be accessed from within your GKE cluster and does not register an external domain to prevent accidental exposure of private information or internal processes.
    * **Istio Ingress Gateway** : Load balancer in the data plane that is responsible for receiving and handling incoming traffic from outside the cluster, including traffic from either external or internal networks.
    * **Istiod** : Configures the Cluster Local Gateway and the Istio Ingress Gateway to handle HTTP requests at the correct endpoints. Istiod is a control plane component. For more information, see [Istiod](https://istio.io/latest/docs/ops/deployment/architecture/#istiod).



Knative serving components are updated automatically with any GKE control plane cluster updates. For more information, see [Available GKE versions](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/cluster-versions).

### Cluster resource usage

The initial installation for Knative serving approximately requires 1.5 virtual CPU and 1 GB of memory for your cluster. The number of nodes in your cluster do not affect the space and memory requirements for a Knative serving installation.

An Activator can consume requests at a maximum of 1000 milliCPU and 600 MiB RAM. When an existing Activator can't support the number of incoming requests, an additional Activator spins up, which requires a reservation of 300 milliCPU and 60 MiB RAM.

Every pod created by the Knative serving service creates a queue proxy sidecar that enforces request concurrency limits. The queue proxy reserves 25 milliCPU and has no memory reservation. The queue proxy's consumption depends on how many requests are getting queued and the size of the requests; there are no limits on the CPU and memory resources it can consume.

## Creating a Service

[ ![Diagram showing Knative serving service architecture](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/CRfAGCP-service-architecture.svg)](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/CRfAGCP-service-architecture.svg) Knative serving Service architecture (click to enlarge)

Knative serving extends Kubernetes by defining a set of [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources): Service, Revision, Configuration, and Route. These CRDs define and control how your applications behave on the cluster:

  * _Knative serving Service_ is the top level custom resource defined by Knative serving. It is a single application that manages the whole lifecycle of your workload. Your service ensures your app has a _route_ , a _configuration_ , and a new _revision_ for each update of the service.
  * _Revision_ is a point-in-time, immutable snapshot of the code and configuration.
  * _Configuration_ maintains the current settings for your latest revision and records a history of all past revisions. Modifying a configuration creates a new revision.
  * _Route_ defines an HTTP endpoint and associates the endpoint with one or more revisions to which requests are forwarded.



When a user creates a Knative serving Service, the following happen:

  1. The Knative serving Service object defines:

     1. A configuration for how to serve your revisions.
     2. An immutable revision for this version of your service.
     3. A route to manage specified traffic allocation to your revision.
  2. The route object creates VirtualService. The VirtualService object configures Ingress Gateway and Cluster Local Gateway to route gateway traffic to the correct revision.

  3. The revision object creates the following control plane components: a Kubernetes Service object and a Deployment object.

  4. Network configuration connects Activator, Autoscaler, and load balancers for your app.




## Request handling

The following diagram shows a high level overview of a possible request path for user traffic through the Knative serving data plane components on a sample Google Kubernetes Engine cluster:

[ ![Diagram showing Knative serving cluster architecture](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/CRfAGCP-cluster-architecture.svg)](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/CRfAGCP-cluster-architecture.svg) Knative serving cluster architecture (click to enlarge)

The next diagram expands from the diagram above to give an in depth view into the user traffic's request path, also described in detail below: [ ![Diagram showing Knative serving request path](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/CRfAGCP-request-handling.svg)](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/CRfAGCP-request-handling.svg) Knative serving request path (click to enlarge)

For a Knative serving request path:

  1. Traffic arrives through:

     * The Ingress Gateway for traffic from outside of clusters
     * The Cluster Local Gateway for traffic within clusters
  2. The VirtualService component, which specifies traffic routing rules, configures the gateways so that user traffic is routed to the correct revision.

  3. Kubernetes Service, a control plane component, determines the next step in the request path dependent on the availability of pods to handle the traffic:

     * If there are no pods in the revision:

       1. Activator temporarily queues the request received and pushes a metric to Autoscaler to scale more pods.
       2. Autoscaler scales to desired state of pods in Deployment.
       3. Deployment creates more pods to receive additional requests.
       4. Activator retries requests to the queue proxy sidecar.
     * If the service is scaled out (pods are available), the Kubernetes Service sends the request to the queue proxy sidecar.

  4. The queue proxy sidecar enforces request queue parameters, single or multi-threaded requests, that the container can handle at a time.

  5. If the queue proxy sidecar has more requests than it can handle, Autoscaler creates more pods to handle additional requests.

  6. The queue proxy sidecar sends traffic to the user container.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
