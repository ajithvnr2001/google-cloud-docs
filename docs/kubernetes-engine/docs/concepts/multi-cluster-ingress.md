---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress/
title: Multi Cluster Ingress \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:58.406491+00:00
---

# Multi Cluster Ingress  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Multi Cluster Ingress Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Multi Cluster Ingress is a cloud-hosted controller for Google Kubernetes Engine (GKE) clusters. It's a Google-hosted service that supports deploying shared load balancing resources across clusters and across regions. To deploy Multi Cluster Ingress across multiple clusters, complete [Setting up Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup) then see [Deploying Ingress across multiple clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress).

For a detailed comparison between Multi Cluster Ingress (MCI), Multi-cluster Gateway (MCG), and load balancer with Standalone Network Endpoint Groups (LB and Standalone NEGs), see [Choose your multi-cluster load balancing API for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).

## Multi-cluster networking

Many factors drive multi-cluster topologies, including close user proximity for apps, cluster and regional high availability, security and organizational separation, cluster migration, and data locality. These use cases are rarely isolated. As the reasons for multiple clusters grow, the need for a formal and productized multi-cluster platform becomes more urgent.

Multi Cluster Ingress is designed to meet the load balancing needs of multi-cluster, multi-regional environments. It's a controller for the external HTTP(S) load balancer to provide ingress for traffic coming from the internet across one or more clusters.

Multi Cluster Ingress's multi-cluster support satisfies many use cases including:

  * A single, consistent virtual IP (VIP) for an app, independent of where the app is deployed globally.
  * Multi-regional, multi-cluster availability through health checking and traffic failover.
  * Proximity-based routing through public Anycast VIPs for low client latency.
  * Transparent cluster migration for upgrades or cluster rebuilds.



## Default quotas

Multi Cluster Ingress has the following default quotas:

  * For details about member limits for fleets, see [fleet management quotas](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quotas#allocation_quotas). for how many members are supported in a fleet.
  * 100 `MultiClusterIngress` resources and 100 `MultiClusterService` resources per project. You can create up to 100 `MultiClusterIngress` and 100 `MultiClusterService` resources in a config cluster for any number of backend clusters up to the per-project cluster maximum.



## Pricing and trials

To learn about Multi Cluster Ingress pricing, see [Multi Cluster Ingress pricing](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-gateway-and-multi-cluster-ingress).

## How Multi Cluster Ingress works

Multi Cluster Ingress builds on the architecture of the [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https). The global external Application Load Balancer is a globally distributed load balancer with proxies deployed at 100+ Google points of presence (PoPs) around the world. These proxies, called [Google Front Ends (GFEs)](https://cloud.google.com/security/infrastructure/design#google-frontend-service), sit at the edge of Google's network, positioned close to clients. Multi Cluster Ingress creates external Application Load Balancers in the [Premium Tier](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier). These load balancers use global external IP addresses advertised using [anycast](https://en.wikipedia.org/wiki/Anycast). Requests are served by GFEs and the cluster that is closest to the client. Internet traffic goes to the closest Google PoP and uses the Google backbone to get to a GKE cluster. This load balancing configuration results in [lower latency](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency#options_for_load_balancing) from the client to the GFE. You can also reduce latency between serving GKE clusters and GFEs by running your GKE clusters in regions that are closest to your clients.

Terminating HTTP and HTTPS connections at the edge allows the Google load balancer to decide where to route traffic by determining backend availability before traffic enters a data center or region. This gives traffic the most efficient path from the client to the backend while considering the backends' health and capacity.

Multi Cluster Ingress is an Ingress controller that programs the external HTTP(S) load balancer using [network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs) (NEGs). When you create a `MultiClusterIngress` resource, GKE deploys Compute Engine load balancer resources and configures the appropriate Pods across clusters as backends. The NEGs are used to track Pod endpoints dynamically so the Google load balancer has the right set of healthy backends.

![Multi Cluster Ingress traffic flow](https://docs.cloud.google.com/static/kubernetes-engine/images/anthos-ingress-traffic-flow.svg)

As you deploy applications across clusters in GKE, Multi Cluster Ingress ensures that the load balancer is in sync with events that occur in the cluster:

  * A Deployment is created with the right matching labels.
  * A Pod's process dies and fails its health check.
  * A cluster is removed from the pool of backends.



Multi Cluster Ingress updates the load balancer, keeping it consistent with the environment and desired state of Kubernetes resources.

## Multi Cluster Ingress architecture

Multi Cluster Ingress uses a centralized Kubernetes API server to deploy Ingress across multiple clusters. This centralized API server is called the config cluster. Any GKE cluster can act as the config cluster. The config cluster uses two custom resource types: `MultiClusterIngress` and `MultiClusterService`. By deploying these resources on the config cluster, the Multi Cluster Ingress controller deploys load balancers across multiple clusters.

The following concepts and components make up Multi Cluster Ingress:

  * Multi Cluster Ingress controller - This is a globally distributed control plane that runs as a service outside of your clusters. This allows the lifecycle and operations of the controller to be independent of GKE clusters.

  * Config cluster - This is a chosen GKE cluster running on Google Cloud where the `MultiClusterIngress` and `MultiClusterService` resources are deployed. This is a centralized point of control for these multi-cluster resources. These multi-cluster resources exist in and are accessible from a single logical API to retain consistency across all clusters. The Ingress controller watches the config cluster and reconciles the load balancing infrastructure.

  * A [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) lets you logically group and normalize GKE clusters, making administration of infrastructure easier and enabling the use of multi-cluster features such as Multi Cluster Ingress. You can learn more about the benefits of fleets and how to create them in the [fleet management documentation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). A cluster can only be a member of a single fleet.

  * Member cluster - Clusters registered to a fleet are called [member clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership). Member clusters in the fleet comprise the full scope of backends that Multi Cluster Ingress is aware of. The [Google Kubernetes Engine cluster management view](https://console.cloud.google.com/kubernetes/list/overview) provides a secure console to view the state of all your registered [clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards#kubernetes_clusters).




![Multi Cluster Ingress arch](https://docs.cloud.google.com/static/kubernetes-engine/images/anthos-ingress-arch.svg)

### Deployment workflow

The following steps illustrate a high-level workflow for using Multi Cluster Ingress across multiple clusters.

  1. Register GKE clusters to a fleet in your chosen project.

  2. Configure a GKE cluster as the central config cluster. This cluster can be a dedicated control plane, or it can run other workloads.

  3. Deploy applications to the GKE clusters where they need to run.

  4. Deploy one or more `MultiClusterService` resources in the config cluster with label and cluster matches to select clusters, namespace, and Pods that are considered backends for a given Service. This creates NEGs in Compute Engine, which begins to register and manage service endpoints.

  5. Deploy a `MultiClusterIngress` resource in the config cluster that references one or more `MultiClusterService` resources as backends for the load balancer. This deploys the Compute Engine external load balancer resources and exposes the endpoints across clusters through a single load balancer VIP.




## Ingress concepts

Multi Cluster Ingress uses a centralized Kubernetes API server to deploy Ingress across multiple clusters. The following sections describe the Multi Cluster Ingress resource model, how to deploy Ingress, and concepts important for managing this highly available network control plane.

### MultiClusterService resources

A `MultiClusterService` is a custom resource used by Multi Cluster Ingress to represent sharing services across clusters. A `MultiClusterService` resource selects Pods, similar to the Service resource, but a `MultiClusterService` can also select labels and clusters. The pool of clusters that a `MultiClusterService` selects across are called _member clusters_. All of the clusters registered to the fleet are member clusters.

A `MultiClusterService` only exists in the config cluster and does not route anything like a ClusterIP, LoadBalancer, or NodePort Service does. Instead, it lets the Multi Cluster Ingress controller refer to a singular distributed resource.

The following sample manifest describes a `MultiClusterService` for an application named `foo`:
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterService
    metadata:
      name: foo
      namespace: blue
    spec:
      template:
        spec:
          selector:
            app: foo
          ports:
          - name: web
            protocol: TCP
            port: 80
            targetPort: 80
    

This manifest deploys a Service in all member clusters with the selector `app: foo`. If `app: foo` Pods exist in that cluster, then those Pod IP addresses are added as backends for the `MultiClusterIngress`.

The following `mci-zone1-svc-j726y6p1lilewtu7` is a derived Service generated in one of the target clusters. This Service creates a NEG which tracks Pod endpoints for all pods that match the specified label selector in this cluster. A derived Service and NEG will exist in every target cluster for every `MultiClusterService` (unless using cluster selectors). If no matching Pods exist in a target cluster then the Service and NEG will be empty. The derived Services are managed fully by the `MultiClusterService` and are not managed by users directly.
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        cloud.google.com/neg: '{"exposed_ports":{"8080":{}}}'
        cloud.google.com/neg-status: '{"network_endpoint_groups":{"8080":"k8s1-a6b112b6-default-mci-zone1-svc-j726y6p1lilewt-808-e86163b5"},"zones":["us-central1-a"]}'
        networking.gke.io/multiclusterservice-parent: '{"Namespace":"default","Name":"zone1"}'
      name: mci-zone1-svc-j726y6p1lilewtu7
      namespace: blue
    spec:
      selector:
        app: foo
      ports:
      - name: web
        protocol: TCP
        port: 80
        targetPort: 80
    

A few notes about the derived Service:

  * Its function is as a logical grouping of endpoints as backends for Multi Cluster Ingress.
  * It manages the lifecycle of the NEG for a given cluster and application.
  * It's created as a headless Service. Note that only the `Selector` and `Ports` fields are carried over from the `MultiClusterService` to the derived service.
  * The Ingress controller manages its lifecycle.



### MultiClusterIngress resource

A `MultiClusterIngress` resource behaves identically in many ways to the core Ingress resource. Both have the same specification for defining hosts, paths, protocol termination and backends.

The following manifest describes a `MultiClusterIngress` that routes traffic to the `foo` and `bar` backends depending on the HTTP host headers:
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterIngress
    metadata:
      name: foobar-ingress
      namespace: blue
    spec:
      template:
        spec:
          backend:
            serviceName: default-backend
            servicePort: 80
          rules:
          - host: foo.example.com
            backend:
              serviceName: foo
              servicePort: 80
          - host: bar.example.com
            backend:
              serviceName: bar
              servicePort: 80
    

This `MultiClusterIngress` resource matches traffic to the virtual IP address on `foo.example.com` and `bar.example.com` by sending this traffic to the `MultiClusterService` resources named `foo` and `bar`. This `MultiClusterIngress` has a default backend that matches on all other traffic and sends that traffic to the default-backend `MultiClusterService`.

The following diagram shows how traffic flows from an Ingress to a cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/ingress-host-match.svg)

In the diagram, there are two clusters, `gke-us` and `gke-eu`. Traffic flows from `foo.example.com` to the Pods that have the label `app:foo` across both clusters. From `bar.example.com`, traffic flows to the Pods that have the label `app:bar` across both clusters.

### Ingress resources across clusters

The config cluster is the only cluster that can have `MultiClusterIngress` and `MultiClusterService` resources. Each target cluster which has Pods that match the `MultiClusterService` label selectors also have a corresponding derived Service scheduled on them. If a cluster is explicitly not selected by a `MultiClusterService`, then a corresponding derived Service is not created in that cluster.

![](https://docs.cloud.google.com/static/kubernetes-engine/images/ifa-resource-model.svg)

### Namespace sameness

Namespace sameness is a property of Kubernetes clusters in which a namespace extends across clusters and is considered the same namespace.

In the following diagram, namespace `blue` exists across the `gke-cfg`, `gke-eu` and `gke-us` GKE clusters. Namespace sameness considers the namespace `blue` to be the same across all clusters. This means that a user has the same privileges to resources in the `blue` namespace in every cluster. Namespace sameness also means that Service resources with the same name across multiple clusters in namespace `blue` are considered to be the same Service.

![](https://docs.cloud.google.com/static/kubernetes-engine/images/namespace-sameness.png)

The Gateway treats the Service as a single pool of endpoints across the three clusters. Because Routes and `MultiClusterIngress` resources can only route to Services within the same namespace, this provides consistent multi-tenancy for config across all clusters in the fleet. Fleets provide a high degree of portability since resources can be deployed or moved across clusters without any changes to their config. Deployment into the same fleet namespace provides consistency across clusters.

Consider the following design principles for Namespace sameness:

  * Namespaces for different purposes should not have the same name across clusters.
  * Namespaces should be reserved either explicitly, by allocating a namespace, or implicitly, through out-of-band policies, for teams and clusters within a fleet.
  * Namespaces for the same purpose across clusters should share the same name.
  * User permission to Namespaces across clusters should be tightly controlled to prevent unauthorized access.
  * You should not use the default Namespace or generic Namespaces like "prod" or "dev" for normal application deployment. It is too easy for users to deploy resources to the default Namespace accidentally and violate the segmentation principles of Namespaces.
  * The same Namespace should be created across clusters wherever a given team or group of users must deploy resources.



### Config cluster design

The Multi Cluster Ingress config cluster is a single GKE cluster which hosts the `MultiClusterIngress` and `MultiClusterService` resources and acts as the single control point for Ingress across the fleet of target GKE clusters. You choose the config cluster when you enable Multi Cluster Ingress. You can choose any GKE cluster as the config cluster and change the config cluster at any time.

#### Config cluster availability

Because the config cluster is a single point of control, Multi Cluster Ingress resources cannot be created or updated if the config cluster API is unavailable. Load balancers and traffic being served by them will not be affected by a config cluster outage but changes to `MultiClusterIngress` and `MultiClusterService` resources will not be reconciled by the controller until it is available again.

Consider the following design principles for config clusters:

  * The config cluster should be chosen such that it is highly available. Regional clusters are preferred over zonal clusters.
  * To enable Multi Cluster Ingress, the config cluster does not have to be a dedicated cluster. The config cluster may host administrative or even application workloads, though you should ensure that hosted applications do not impact the availability of the config cluster API server. The config cluster can be a target cluster that hosts backends for `MultiClusterService` resources, though if extra precautions are needed the config cluster can also be excluded as a backend through cluster selection.
  * Config clusters should have all the Namespaces that are used by target cluster backends. A `MultiClusterService` resource can only reference Pods in the same Namespace across clusters so that Namespace must be present in the config cluster.
  * Users that deploy Ingress across multiple clusters must have access to the config cluster to deploy `MultiClusterIngress` and `MultiClusterService` resources. However, users should only have access to Namespaces they have permission to use.



#### Selecting and migrating the config cluster

You must choose the config cluster when you enable Multi Cluster Ingress. Any member cluster of a fleet can be selected as the config cluster. You can update the config cluster at any time but must take care to ensure that it does not cause disruption. The Ingress controller will reconcile whatever resources exist in the config cluster. When migrating the config cluster from the current one to the next one, `MultiClusterIngress` and `MultiClusterService` resources must be identical. If the resources are not identical, the Compute Engine Load Balancers may be updated or destroyed after the config cluster update.

The following diagram shows how a centralized CI/CD system applies `MultiClusterIngress` and `MultiClusterService` resources to the GKE API server for the config cluster (`gke-us`) and a backup cluster (`gke-eu`) at all times so that the resources are identical across the two clusters. You can change the config cluster for emergencies or planned downtime at any time without any impact because the `MultiClusterIngress` and `MultiClusterService` resources are identical.

![](https://docs.cloud.google.com/static/kubernetes-engine/images/ingress-for-anthos-3.png)

### Cluster selection

`MultiClusterService` resources can select across clusters. By default, the controller schedules a derived Service on every target cluster. If you do not want a derived Service on every target cluster, you can define a list of clusters using the `spec.clusters` field in the `MultiClusterService` manifest.

You might want to define a list of clusters if you need to:

  * Isolate the config cluster to prevent `MultiClusterService` resources from selecting across the config cluster.
  * Control traffic between clusters for application migration.
  * Route to application backends that only exist in a subset of clusters.
  * Use a single HTTP(S) virtual IP address for routing to backends that live on different clusters.



You must ensure that member clusters within the same fleet and region have unique names to prevent naming collisions.

To learn how to configure cluster selection, see [Setting up Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup#specifying_a_config_cluster).

The following manifest describes a `MultiClusterService` that has a `clusters` field that references `europe-west1-c/gke-eu` and `asia-northeast1-a/gke-asia`:
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterService
    metadata:
      name: foo
      namespace: blue
    spec:
      template:
        spec:
          selector:
            app: foo
          ports:
          - name: web
            protocol: TCP
            port: 80
            targetPort: 80
      clusters:
      - link: "europe-west1-c/gke-eu"
      - link: "asia-northeast1-a/gke-asia-1"
    

This manifest specifies that Pods with the matching labels in the `gke-asia` and `gke-eu` clusters can be included as backends for the `MultiClusterIngress`. Any other clusters are excluded even if they have Pods with the `app: foo` label.

The following diagram shows an example `MultiClusterService` configuration using the preceding manifest:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/ingress-for-anthos-4.png)

In the diagram, there are three clusters: `gke-eu`, `gke-asia-1`, and `gke-asia-2`. The `gke-asia-2` cluster is not included as a backend, even though there are Pods with matching labels, because the cluster is not included in the manifest `spec.clusters` list. The cluster does not receive traffic for maintenance or other operations.

## What's next

  * Learn how to [Setup Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup).
  * Learn about [Deploying multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways).
  * Learn about [Deploying Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress).
  * Implement [Multi Cluster Ingress for external load balancing](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/multi-cluster/mci-basic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
