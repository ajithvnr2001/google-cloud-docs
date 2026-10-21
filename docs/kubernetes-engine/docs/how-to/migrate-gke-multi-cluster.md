---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-gke-multi-cluster/
title: Migrate to multi-cluster networking \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:51.895165+00:00
---

# Migrate to multi-cluster networking  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-gke-multi-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Migrate to multi-cluster networking Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2022-02-17 UTC

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Multi-cluster networking is a valuable tool that enables use cases like regional high availability, globally distributed proximity to users for lower latency, and organizational isolation between teams. [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) provides built-in capabilities for multi-cluster networking that you can enable and use at scale across a fleet of GKE clusters. This feature also lets you combine, or migrate deployed infrastructure between, GKE Standard and Autopilot to meet the architectural needs of each application.

With GKE [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, Google manages the infrastructure, including the control plane and the nodes. If you want to configure and manage your nodes instead, GKE provides [Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-standard). For more information on the differences between modes, see [Choose a cluster mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

This page demonstrates these features through several deployment topologies. You learn how to take an application deployed in a single GKE cluster and migrate it to a multi-cluster deployment across GKE Standard and Autopilot clusters. You use GKE [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services) for east-west traffic and [multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways) to enable multi-cluster north-south networking.

This page is for cloud architects and operations teams that use, or plan to use, GKE to deploy services across multiple Kubernetes clusters. Before reading this page, ensure that you're familiar with [Kubernetes](https://kubernetes.io/docs/home/).

## Multi-cluster Services and multi-cluster Gateways

Kubernetes can run using a single control plane across disparate cloud zones to provide resiliency and higher availability for your services. GKE takes this one step further and provides GKE [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services) (MCS) that provides a cross-cluster service discovery and invocation mechanism. Services that use this feature are discoverable and accessible across clusters with a virtual IP, which matches the behavior of a `ClusterIP` Service accessible in a cluster. This approach allows for the following benefits:

  * Services can be load-balanced across multiple clusters in the same region or different regions (east-west traffic).
  * Cross-region service high availability options are achievable.
  * Stateful and stateless workloads can be deployed and managed across separate clusters.
  * Shared services are available across clusters.



To learn more about how to deploy MCS, see [Configuring multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).

GKE provides an implementation of the Kubernetes Gateway API that uses the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller). Gateway allows GKE to deploy Google Cloud load balancers to provide inbound (north-south) traffic routing for services deployed on GKE. GKE also provides [multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways) (MCG) which extend the GKE Gateway controller to provision load balancers that route traffic to services deployed on disparate GKE clusters.

The following diagram shows how, when you combine MCS and MCG, you are able to manage the complementary aspects of service deployment and traffic routing from a single control plane:

![Multi-cluster Services facilitates communication between services in a cluster and multi-cluster Gateway deploys load balancers to route traffic across clusters.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-gateway-traffic.png)

For more information, see [Deploying multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).

**Note:** In a multi-cluster scenario where clusters belong to different custom subnets and are registered to the same fleet, you must create a firewall rule to allow cross-cluster traffic. For more information, see [create firewall rule](https://docs.cloud.google.com/service-mesh/docs/unified-install/gke-install-multi-cluster#create_firewall_rule).

## Overview of migration

GKE multi-cluster networking capabilities benefit workloads of various profiles. For example, you might have stateless components with bursty traffic that you wish to move to Autopilot because of its more efficient cost model.

Or, you might want to place your application frontends closer to users. This approach provides lower latency and caching that improves application performance and user experience. At the same time, you might have some stateful components that your application relies on that can only reside in one location. This configuration requires north-south, multi-cluster load balancing to send client traffic to the correct cluster in that location. You also need east-west, multi-cluster load balancing to send traffic between clusters to reach the stateful components.

This page uses the [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) cloud microservices demo application to demonstrate a multi-cluster pattern that can be used to enhance the deployment of the single zone demo. You start with a single-zone version of the application. You then add elements of high availability and resilience by using multi-cluster Services and multi-cluster Gateways, and reduce operational toil by taking advantage of Autopilot.

### Initial single-cluster deployment

In the following diagram, the Online Boutique application is initially deployed to a single GKE Standard mode cluster named _std-west_ , and is exposed by using a `LoadBalancer` Service:

![A single Standard mode GKE cluster that runs all the services exposed using a regular HTTP external LoadBalancer service.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-initial-state.svg)

### Migrate to multi-cluster Services

In the next intermediate step, you create two additional clusters, and the stateless services are deployed in additional regions. You create two GKE Autopilot clusters named _auto-east_ and _auto-central_ in two separate regions distinct from the single _std-west_ GKE Standard cluster, and register the clusters to the [Google Cloud fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).

Fleets are a Google Cloud concept for logically organizing clusters and other resources, and let you use and manage multi-cluster capabilities and apply consistent policies across your systems.

You export the _cartservice_ on the _std-west_ cluster in the _onlineboutique_ namespace to the new fleet clusters by using [ServiceExport](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#registering_a_service_for_export). You deploy Online Boutique's _frontend_ Service on all three clusters and expose it through a [ClusterIP](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_clusterip) service. You then export the service to the fleet using `ServiceExports`. Services such as the middleware layer of the Online Boutique (like _productcatalog_ , _shipping_ , and _adservice_) are also deployed to all three clusters.

A `Pod` that runs in any cluster in the fleet can access an exported `Service` by sending a request to the `ClusterSet` URI for that service. The request routes to an endpoint that backs the service.

The _frontend_ Service is able to consume the middleware services (such as _productcatalogservice_ or _currencyservice_) locally in the same cluster. This architecture helps keep incoming requests local to the regions whose frontend responds to the request, and avoids unnecessary inter-region network traffic charges.

The following diagram illustrates the two multi-cluster Services. The stateless _frontend_ Service is deployed to three clusters, and the stateful backend _cartservice_ is deployed to one cluster. The diagram also shows that in this intermediate step, inbound traffic for the frontend service remains routed to the original GKE Standard cluster in _us-west1_ using a regional external passthrough Network Load Balancer created by the frontend-external `LoadBalancer` Service:

![Multi cluster Services runs across three GKE clusters but
traffic is still directed to a single cluster using a regular HTTP external
LoadBalancer service.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-services.svg)

### Migrate to multi-cluster Gateway

In the final step, you route inbound traffic for the _frontend_ Service from external client requests to services in multiple clusters in the fleet using a multi-cluster Gateway.

A fourth cluster named _config-central_ is added to the fleet to host and manage the configuration for the [Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) and [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/) resources that are created as part of this configuration. The `HTTPRoute` resource maps the _/_ prefix to the frontend [ServiceImport](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#consuming_cross-cluster_services). Traffic for the Online Boutique's frontend is sent to a healthy endpoint in one of the available regions. This approach adds elements of high availability to the Online Boutique application architecture.

In the following diagram, the multi-cluster Gateway deploys a Global Cloud Load Balancer that routes external traffic to the stateless _frontend_ Service deployed on each of the three application clusters in the fleet.

![Multi cluster Services runs across three GKE clusters and traffic is now distributed across frontend services in all clusters using a multi-cluster external Gateway.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-gateway.svg)

In the final state, this opinionated pattern demonstrates loose coupling between the stateful (_cartservice_ and _redis-cart_) and stateless portions of the application (_frontend_ , _emailservice_ , _checkoutservice_ , _recommendationservice_ , _paymentservice_ , _productcatalogservice_ , _currencyservice_ , _shippingservice_ , and _adservice_). While outside the scope of this page, this approach gives you a future opportunity to add resilience and high availability to the stateful services layer.

## Objectives

  * Create and configure GKE Standard and Autopilot clusters.
  * Deploy Online Boutique to a zonal GKE Standard cluster.
  * Export multi-cluster `Services`.
  * Deploy manifests to Standard and Autopilot clusters.
  * Enable and configure multi-cluster Gateways.
  * Test multi-region application behavior.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Compute Engine](https://cloud.google.com/compute/all-pricing) for [GKE worker nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes)
  * [Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#lb)
  * [Multi Cluster Ingress](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-gateway-and-multi-cluster-ingress)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

Before you begin, ensure you have the following requirements met:

  * It is recommended that you use a new project for this guide, as the easiest way to clean up is to delete the project once you are finished.
  * This guide assumes you have the _Owner IAM_ role for your Google Cloud project. For production or real-world settings, it is best practice to scope permissions to least privilege. For more information, see [Using IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely) and [Verify every access attempt explicitly](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust#verify_every_access_attempt_explicitly).
  * Familiarize yourself with the [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) microservices demo application architecture.



## Prepare the environment

In this guide, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/features) to enter commands. Cloud Shell gives you access to the command line in the Google Cloud console and includes Google Cloud SDK and other tools, such as the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). Cloud Shell appears as a window at the bottom of the Google Cloud console. It can take several minutes to initialize, but the window appears immediately.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In Cloud Shell, define environment variables used in this guide. Replace PROJECT_ID with your own project ID:
         
         export PROJECT=PROJECT_ID
         gcloud config set project ${PROJECT}
         

  3. Enable the services required for the steps on this page:
         
         gcloud services enable \
             gkehub.googleapis.com \
             multiclusteringress.googleapis.com \
             dns.googleapis.com \
             trafficdirector.googleapis.com \
             cloudresourcemanager.googleapis.com \
             multiclusterservicediscovery.googleapis.com \
             container.googleapis.com
         
         gcloud container fleet multi-cluster-services enable
         

Multi-cluster Services manages Google Cloud components like Cloud DNS, firewall rules, and Cloud Service Mesh, so these APIs must also be enabled. For more information, see [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview#multi-cluster_kubernetes).

The output is similar to the following example:
         
         Operation "operations/acf.p2-822685001869-ee4ebe78-6dd8-465e-b0fd-3b0e5f964bad"
         finished successfully.
         
         Waiting for Feature Multi-cluster Services to be created...done.
         

  4. Verify that multi-cluster Services shows the _ACTIVE_ state:
         
         gcloud container fleet multi-cluster-services describe
         

The output is similar to the following example:
         
         createTime: '2021-11-30T21:59:25.245190894Z'
         name: projects/PROJECT_ID/locations/global/features/multiclusterservicediscovery
         resourceState:
           state: ACTIVE
         spec: {}
         updateTime: '2021-11-30T21:59:27.459063070Z'
         

If the value of _state_ is not _ACTIVE_ , see the [multi-cluster services troubleshooting details](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#troubleshooting).




## Create and configure GKE clusters

To demonstrate the multi-cluster pattern in this guide, you use three _application clusters_ in three separate cloud regions, and one cluster to _host the configuration_ for Gateway resources. You register all clusters with the fleet associated with your project. A Google Cloud project can only have a single fleet associated with it. This project is known as the fleet host project.

In this document, all the GKE clusters are deployed in the same project. The Shared VPC network is created in this project, which is also the fleet's project.

  1. Create Standard and Autopilot GKE clusters and register the clusters to your project's fleet:
         
         gcloud container clusters create std-west \
             --location us-west1-a \
             --num-nodes=6 \
             --enable-ip-alias \
             --release-channel regular \
             --workload-pool=${PROJECT}.svc.id.goog \
             --gateway-api=standard \
             --enable-fleet \
             --async \
         
         gcloud container clusters create-auto auto-east \
             --location us-east1 \
             --release-channel regular \
             --enable-fleet \
             --async
         
         gcloud container clusters create-auto auto-central \
             --location us-central1 \
             --release-channel regular \
             --enable-fleet \
             --async
         
         gcloud container clusters create config-central \
             --location us-central1 \
             --num-nodes=1 \
             --enable-ip-alias \
             --release-channel regular \
             --workload-pool=${PROJECT}.svc.id.goog \
             --gateway-api=standard \
             --enable-fleet \
             --async
         

Workload Identity Federation for GKE is enabled by default on GKE Autopilot clusters so you don't have to use the `--workload-pool` flag when you create those clusters like you do with the GKE Standard clusters.

  2. Wait for the clusters' _STATUS_ to change from _PROVISIONING_ to _RUNNING_. This process can take up to 10 minutes. You can monitor the progress by using a watch loop:
         
         watch -n 20 --difference=permanent "gcloud container clusters list"
         

The output is similar to the following example:
         
         NAME: auto-central
         LOCATION: us-central1
         MASTER_VERSION: 1.21.5-gke.1802
         MASTER_IP: 107.178.213.138
         MACHINE_TYPE: e2-medium
         NODE_VERSION: 1.21.5-gke.1802
         NUM_NODES: 3
         STATUS: PROVISIONING
         
         NAME: config-central
         LOCATION: us-central1
         MASTER_VERSION: 1.21.5-gke.1802
         MASTER_IP:
         MACHINE_TYPE: e2-medium
         NODE_VERSION: 1.21.5-gke.1802
         NUM_NODES: 9
         STATUS: PROVISIONING
         
         NAME: auto-east
         LOCATION: us-east1
         MASTER_VERSION: 1.21.5-gke.1802
         MASTER_IP: 35.229.88.209
         MACHINE_TYPE: e2-medium
         NODE_VERSION: 1.21.5-gke.1802
         NUM_NODES: 3
         STATUS: PROVISIONING
         
         NAME: std-west
         LOCATION: us-west1-a
         MASTER_VERSION: 1.21.5-gke.1802
         MASTER_IP: 35.197.93.113
         MACHINE_TYPE: e2-medium
         NODE_VERSION: 1.21.5-gke.1802
         NUM_NODES: 6
         STATUS: PROVISIONING
         

  3. After all the clusters are in the _RUNNING_ state, press `CTRL-C` to interrupt the command.

  4. Add an Identity and Access Management (IAM) policy binding granting the fleet host project MCS service account the _Network User_ role for its own project:
         
         gcloud projects add-iam-policy-binding ${PROJECT} \
             --member "serviceAccount:${PROJECT}.svc.id.goog[gke-mcs/gke-mcs-importer]" \
             --role "roles/compute.networkViewer"
         

You use Workload Identity Federation for GKE to grant the MCS service read access to your project VPC network configuration. As a result, the fleet host project's MCS _Importer GKE_ service account needs this role.

The output is similar to the following example:
         
         - members:
           - serviceAccount:PROJECT_ID.svc.id.goog[gke-mcs/gke-mcs-importer]
           role: roles/compute.networkViewer
         [...]
         

  5. Create an IAM binding in the fleet host project that assigns the GKE Service Agent role to the project's GKE fleet service account:
         
         gcloud projects add-iam-policy-binding ${PROJECT} \
             --member "serviceAccount:service-{${PROJECT}}@gcp-sa-gkehub.iam.gserviceaccount.com" \
             --role roles/gkehub.serviceAgent
         

  6. Create an IAM binding in the fleet host project that assigns the MCS Service Agent role to the project's MCS service account.:
         
         gcloud projects add-iam-policy-binding ${PROJECT} \
             --member "serviceAccount:service-{${PROJECT}}@gcp-sa-mcsd.iam.gserviceaccount.com" \
             --role roles/multiclusterservicediscovery.serviceAgent
         

  7. Connect to the clusters and generate kubeconfig entries:
         
         gcloud container clusters get-credentials std-west \
             --location us-west1-a --project $PROJECT
         
         gcloud container clusters get-credentials auto-east \
             --location us-east1 --project $PROJECT
         
         gcloud container clusters get-credentials auto-central \
             --location us-central1 --project $PROJECT
         
         gcloud container clusters get-credentials config-central \
             --location us-central1 --project $PROJECT
         

For each command, the output is similar to the following example:
         
         Fetching cluster endpoint and auth data.
         kubeconfig entry generated for std-west.
         

  8. Rename contexts for clusters so that they are easier to work with in the rest of this page:
         
         kubectl config rename-context \
             gke_${PROJECT}_us-west1-a_std-west \
             std-west
         
         kubectl config rename-context \
             gke_${PROJECT}_us-east1_auto-east \
             auto-east
         
         kubectl config rename-context \
             gke_${PROJECT}_us-central1_auto-central \
             auto-central
         
         kubectl config rename-context \
             gke_${PROJECT}_us-central1_config-central \
             config-central
         

In this guide, the contexts are named based on their location. Although you can provide alternate names, the remaining steps in this guide use the names used in this step.




## Deploy Online Boutique on GKE Standard

In the first step of the demonstration deployment, you deploy the full set of Online Boutique application services to the single GKE Standard cluster _std-west_ in _us-west1_.

  1. Create the namespace _onlineboutique_ on _std-west_ :
         
         kubectl create namespace onlineboutique --context std-west
         

The output is similar to the following example:
         
         namespace/onlineboutique created
         

  2. Clone the Online Boutique GitHub repository and set up a _WORKDIR_ variable:
         
         cd ~
         
         git clone --branch release/v0.4.1 \
             https://github.com/GoogleCloudPlatform/microservices-demo.git
         
         cd microservices-demo/release && export WORKDIR=`pwd`
         

  3. Deploy Online Boutique on _std-west_. This process creates `Deployments` and `Services` for all of Online Boutique's microservices, and includes a [LoadBalancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer) type Service which externally exposes Online Boutique's frontend service:
         
         cd $WORKDIR
         
         kubectl apply -f kubernetes-manifests.yaml \
             -n onlineboutique --context=std-west
         

  4. Wait for the `LoadBalancer` Service to get an external IP:
         
         watch -n 20 --difference=permanent \
              "kubectl get svc frontend-external -n onlineboutique --context=std-west"
         

Initially, the output is similar to the following example:
         
         NAME                TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
         frontend-external   LoadBalancer   10.60.5.62   <pending>     80:30359/TCP   43s
         

When the `Service` is ready the _EXTERNAL-IP_ column displays the public IP address of the load balancer.

  5. After the `Service` is ready, get the external IP address of the load balancer and use curl to verify that the frontend is ready. If this curl command returns an error, wait a few moments before you try again:
         
         curl $(kubectl get svc frontend-external \
               -n onlineboutique --context=std-west \
               -o=jsonpath="{.status.loadBalancer.ingress[0].ip}") | \
                 grep -e Cluster -e Zone -e Pod
         

The successful output of the curl command is similar to the following example:
         
         <b>Cluster: </b>std-west<br/>
         <b>Zone: </b>us-west1-a<br/>
         <b>Pod: </b>frontend-b7bddcc97-wdjsk
         




You now have a single-zone version of Online Boutique running in _us-west1-a_. You can also use a web browser to navigate to the external IP assigned to the _frontend-external_ `LoadBalancer` Service to access the application and observe its behavior. This initial single deployment is shown in the following diagram:

![A single Standard mode GKE cluster that runs all the services exposed with a regular HTTP external LoadBalancer service.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-initial-state.svg)

## Export cartservice as a multi-cluster Service

In this section, you start to add elements of high availability to the application. You export the backend _cartservice_ as a multi-cluster Service to the GKE Autopilot clusters.

  1. Create the namespace _onlineboutique_ on the remaining clusters:
         
         kubectl create namespace onlineboutique --context auto-east
         
         kubectl create namespace onlineboutique --context auto-central
         
         kubectl create namespace onlineboutique --context config-central
         

For each command, the output is similar to the following example:
         
         namespace/onlineboutique created
         

  2. Export _cartservice_ from the _std-west_ cluster to all other clusters in the `ClusterSet`. The `ServiceExport` object registers the _cartservice_ Service, with GKE multi-cluster Services, for export to all clusters in the fleet that have the namespace _onlineboutique_ present. For more details, see [registering a service for export](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#registering_a_service_for_export).
         
         cat <<EOF>> $WORKDIR/cartservice-export.yaml
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
          namespace: onlineboutique
          name: cartservice
         
         EOF
         
         kubectl apply -f $WORKDIR/cartservice-export.yaml \
             -n onlineboutique --context=std-west
         




## Apply application manifests for multi-cluster pattern

In this section you apply two curated manifests to deploy the multi-cluster pattern. These manifests contain selected portions of the _kubernetes-manifests.yaml_ that you previously applied to the _std-west_ cluster:

  * The first manifest is used for the _frontend_ `Deployment`, `Service`, and `ServiceExport`.
  * The second manifest is used to deploy the middleware `Services` (_emailservice_ , _checkoutservice_ , _recommendationservice_ , _paymentservice_ , _productcatalogservice_ , _currencyservice_ , _shippingservice_ , and _adservice_) to all regions that have a _frontend_ running. By keeping a request local to a region for as long as possible, you avoid unnecessary inter-region network traffic charges.



A `Pod` that runs in any cluster in the fleet can access an exported `Service` by sending a request to the `ClusterSet` URI for that service in the format `SERVICE_NAME.NAMESPACE.svc.clusterset.local`. For example, the _frontend_ `Deployments` in all three example clusters are able to consume the _cartservice_ , in the `onlineboutique` namespace, by making a request to _cartservice.onlineboutique.svc.clusterset.local_.

For this reason, in each manifest, the hostname for the _cartservice_ has been updated to its `ClusterSet` URI. This step is critical. If this service hostname is not updated, the _frontend_ Service would ask kube-dns for `cartservice` instead of `cartservice.onlineboutique.svc.clusterset.local`. This behavior would result in `HTTP Status 500` errors on clusters where a local version of _cartservice_ is not available, and cause the _frontend_ pods to be unhealthy.

  1. Set an environment varianble for the GitHub repository that contains the manifests:
         
         export MANIFEST_REPO_PATH=https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/master/gateway/docs/cluster-migration
         

  2. Apply the manifests to deploy the frontend layer to all three workload clusters:
         
         kubectl apply -f ${MANIFEST_REPO_PATH}/onlineboutique-frontend-manifests.yaml \
             -n onlineboutique --context=std-west
         
         kubectl apply -f ${MANIFEST_REPO_PATH}/onlineboutique-frontend-manifests.yaml \
             -n onlineboutique --context=auto-east
         
         kubectl apply -f ${MANIFEST_REPO_PATH}/onlineboutique-frontend-manifests.yaml \
             -n onlineboutique --context=auto-central
         

  3. Apply the manifests to deploy the middleware layer to all three workload clusters:
         
         kubectl apply -f ${MANIFEST_REPO_PATH}/onlineboutique-middleware-manifests.yaml \
             -n onlineboutique --context=std-west
         
         kubectl apply -f ${MANIFEST_REPO_PATH}/onlineboutique-middleware-manifests.yaml \
             -n onlineboutique --context=auto-east
         
         kubectl apply -f ${MANIFEST_REPO_PATH}/onlineboutique-middleware-manifests.yaml \
             -n onlineboutique --context=auto-central
         




You now have the _frontend_ `Deployment`, `Service`, and `ServiceExport` active in clusters _std-west_ , _auto-east_ , and _auto-central_. You also have locally running Online Boutique middleware services in each cluster. However, external traffic is still routed only to the `Service` that runs in the initial cluster in _us-west1_ , as shown in the following diagram:

![Multi cluster Services runs across three GKE clusters but traffic is still directed to a single cluster using a regular HTTP external LoadBalancer service.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-services.svg)

## Enable and configure multi-cluster Gateways

In this section, you route traffic to and load balance external traffic across frontends in all three clusters. To achieve this configuration, you use multi-cluster Gateways (MCG). These steps to set up MCG follow the guidance described in more detail on [Enabling multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways).

In these steps, you use the _config-central_ cluster to host the configuration for Gateway resources.

  1. Confirm that all clusters have successfully registered to the fleet:
         
         gcloud container fleet memberships list --project=$PROJECT
         

The following example output shows that all the clusters are successfully registered:
         
         NAME: auto-central
         EXTERNAL_ID: 21537493-32ea-4a41-990d-02be2c1b319f
         
         NAME: config-central
         EXTERNAL_ID: 4369423e-ea7b-482d-a0eb-93b560e67b98
         
         NAME: std-west
         EXTERNAL_ID: 7fcb048b-c796-476b-9698-001a00f91ab3
         
         NAME: auto-east
         EXTERNAL_ID: aae2d2ff-b861-4a38-bcaf-612f14810012
         

  2. Install the Gateway API _custom resource definition_ on the _config-central_ cluster:
         
         kubectl --context=config-central kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v0.5.0" \
             | kubectl apply -f -
         

This step installs the Gateway API custom resource definitions including the `GatewayClass`, `Gateway`, and `HTTPRoute` resources. The custom resource definitions are maintained by the Kubernetes [Network Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-network). Once installed, you can use the GKE Gateway controller.

  3. Enable Multi Cluster Ingress for your fleet if you haven't done so already. Enabling this feature also enables the multi-cluster Gateway controller.
         
         gcloud container fleet ingress enable \
             --config-membership=config-central \
             --project=$PROJECT
         
         gcloud container fleet ingress describe --project=$PROJECT
         

The output is similar to the following example:
         
         createTime: '2021-12-08T23:10:52.505888854Z'
         name: projects/PROJECT_ID/locations/global/features/multiclusteringress
         resourceState:
           state: ACTIVE
         spec:
           multiclusteringress:
             configMembership: projects/zl-mcs-expf61cbd13/locations/global/memberships/config-central
         state:
           state:
             code: OK
             description: Ready to use
             updateTime: '2021-12-08T23:11:37.994971649Z'
         updateTime: '2021-12-08T23:11:38.098244178Z'
         

If the value of _state_ is not _ACTIVE_ , see [Troubleshooting and operations for Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/troubleshooting-and-ops#config_cluster_migration).

  4. Confirm that `GatewayClasses` are available on the _config-central_ cluster:
         
         kubectl get gatewayclasses --context=config-central
         

The output is similar to the following example:
         
         NAME                                  CONTROLLER                  AGE
         gke-l7-global-external-managed        networking.gke.io/gateway   18s
         gke-l7-global-external-managed-mc     networking.gke.io/gateway   19s
         gke-l7-regional-external-managed      networking.gke.io/gateway   18s
         gke-l7-regional-external-managed-mc   networking.gke.io/gateway   19s
         gke-l7-gxlb                           networking.gke.io/gateway   74s
         gke-l7-gxlb-mc                        networking.gke.io/gateway   16s
         gke-l7-rilb                           networking.gke.io/gateway   74s
         gke-l7-rilb-mc                        networking.gke.io/gateway   16s
         

Different `GatewayClass` resources have different capabilities. For more information on when to use which type, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

  5. Deploy the `external-http` Gateway resource to `config-central`:
         
         cat <<EOF>> $WORKDIR/external-http-gateway.yaml
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
           namespace: onlineboutique
         spec:
           gatewayClassName: gke-l7-global-external-managed-mc
           listeners:
           - protocol: HTTP
             port: 80
             name: http
         EOF
         
         kubectl apply -f external-http-gateway.yaml \
             -n onlineboutique --context=config-central
         

As indicated by the `gatewayClassName` field, this resource is of `GatewayClass` _gke-l7-global-external-managed-mc_ which manages Layer 7 external Cloud Load Balancing and exposes the multi-cluster application

  6. Deploy the `HTTPRoute` named _public-frontend-route_ on _config-central_ :
         
         cat <<EOF>> $WORKDIR/public-frontend-route.yaml
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: public-frontend-route
           namespace: onlineboutique
         spec:
           parentRefs:
           - name: "external-http"
           hostnames:
           - "store.example.com"
           rules:
           - matches:
             - path:
                 type: PathPrefix
                 value: /
             backendRefs:
             - name: frontend
               group: net.gke.io
               kind: ServiceImport
               port: 80
         EOF
         
         kubectl apply -f public-frontend-route.yaml \
             -n onlineboutique --context=config-central
         

When you deploy the `HTTPRoute` resource it creates an external Layer 7 Cloud Load Balancing resource and exposes the frontend `ServiceImport` backed by the frontend services that run in the _std-west_ , _auto-east_ , and _auto-central_ clusters.

**Note:** Alternatively, you can replace `store.example.com` in this manifest with a hostname from a domain you or your team owns, and point the respective DNS record to the external IP address of the load balancer created by this step. Requests destined for that hostname would then be directed to this load balancer.

The following diagram shows how, after the multi-cluster Gateway is deployed, traffic can be routed to any of the frontend multi-cluster Services on any of the three application clusters:

![Multi cluster Services runs across three GKE clusters and traffic is now distributed across frontend services in all clusters using a multi-cluster external Gateway.](https://docs.cloud.google.com/static/kubernetes-engine/images/migrate-gke-multi-cluster-gateway.svg)

  7. Wait for the load balancer to be ready with a provisioned external IP address before proceeding to the next step. It can take up to 10 minutes for the IP address to be assigned. You can monitor progress by using a watch loop. The load balancer has a name in the pattern like _gkemcg-onlineboutique-external-http-k09mfhk74gop_ :
         
         watch -n 20 --difference=permanent \
             "gcloud compute forwarding-rules list \
                 | grep -A 5 NAME..*external-http"
         

The output is similar to the following example:
         
         NAME: gkemcg-onlineboutique-external-http-k09mfhk74gop
         REGION:
         IP_ADDRESS: 34.149.29.176
         IP_PROTOCOL: TCP
         TARGET: gkemcg-onlineboutique-external-http-k09mfhk74gop
         

  8. Once the load balancer is ready, run the following command in Cloud Shell to export the external IP address of the load balancer created through the application of _external-http-gateway.yaml_ and _public-frontend-route.yaml_ manifests:
         
         export EXTERNAL_LB_IP=$(kubectl --context=config-central \
                                     -n onlineboutique get gateway external-http \
                                     -o=jsonpath='{.status.addresses[0].value}')
         

  9. When you send a request to the load balancer with the appropriate headers, it returns the HTML contents served by the frontend service. For example, since you configured the `HTTPRoute` resource to map the `store.example.com` hostname to the _frontend_ `ServiceImport`, you must supply the `HOST` header when you make the HTTP request. If the following curl example returns an error, wait a few minutes and try again:
         
         curl -H 'HOST: store.example.com' $EXTERNAL_LB_IP | \
             grep -e Cluster -e Zone -e Pod
         

The successful output of the curl command is similar to the following example:
         
         <b>Cluster: </b>auto-central<br/>
         <b>Zone: </b>us-central1-f<br/>
         <b>Pod: </b>frontend-7c7d596ddc-jdh8f
         

**Note:** If the matching headers, as configured in the `HTTPRoute`, are not supplied when you make the request, the client receives an `HTTP status 404` error. Any of the three frontend pods that run in the serving path can respond to the HTTP request inbound to the global load balancer. The global load balancer can route requests to healthy backends located closest to where the request originated.



## Test application multi-region routing behavior

One of the powerful features obtained by using multi-cluster Services and multi-cluster Gateways is that external requests are routed to the geographically closest cluster.

To test application multi-region behavior, generate traffic that originates from the various regions where you have clusters deployed. Create three small pods, one in each of the serving clusters (_std-west_ , _auto-east_ , and _auto-central_), that you can use to send HTTP requests to the load balancer endpoint. The results let you see which frontend `Pod` responds.

  1. Create the client pods:
         
         kubectl run --context=std-west \
                     --image=radial/busyboxplus:curl client-west \
                     -- sh -c 'while sleep 3600; do :; done'
         
         kubectl run --context=auto-east \
                     --image=radial/busyboxplus:curl client-east \
                     -- sh -c 'while sleep 3600; do :; done'
         
         kubectl run --context=auto-central \
                     --image=radial/busyboxplus:curl client-central \
                     -- sh -c 'while sleep 3600; do :; done'
         

  2. After the pods are running, use a curl command to send a request to the load balancer endpoint from the client `Pod` in the _std-west_ cluster and review the response:
         
         kubectl exec -it --context=std-west client-west \
             -- curl -H 'HOST: store.example.com' $EXTERNAL_LB_IP | \
                    grep -e Cluster -e Zone -e Pod
         

The successful output of the curl command is similar to the following example:
         
         <b>Cluster: </b>std-west<br/>
         <b>Zone: </b>us-west1-a<br/>
         <b>Pod: </b>frontend-7cf48b79cf-trzc4
         

  3. Run the same curl request from the client `Pod` in the _auto-east_ cluster, and look at the response:
         
         kubectl exec -it --context=auto-east client-east \
             -- curl -H 'HOST: store.example.com' $EXTERNAL_LB_IP | \
                    grep -e Cluster -e Zone -e Pod
         

The successful output of the curl command is similar to the following example:
         
         <b>Cluster: </b>auto-east<br/>
         <b>Zone: </b>us-east1-d<br/>
         <b>Pod: </b>frontend-6784b6df98-scdws
         

As this is an Autopilot cluster, the cluster may need to provision additional resources to schedule the `Pod`. If you see output similar to the following example, wait a moment and try again:
         
         Error from server (BadRequest): pod client-east does not have a host assigned
         

  4. Run the curl from the client `Pod` in the _auto-central_ cluster and check the response:
         
         kubectl exec -it --context=auto-central client-central \
             -- curl -H 'HOST: store.example.com' $EXTERNAL_LB_IP | \
                 grep -e Cluster -e Zone -e Pod
         

The successful output of the curl command is similar to the following example:
         
         <b>Cluster: </b>auto-central<br/>
         <b>Zone: </b>us-central1-b<br/>
         <b>Pod: </b>frontend-6784b6df98-x2fv4
         

These results confirm that traffic routes to the corresponding pods in the locations closest to request origin.




## Test application multi-region resiliency

In addition to efficient traffic routing, running your services in multiple regions provides resiliency in the rare, yet still possible, case of infrastructure failure.

Test the behavior by deleting the _frontend_ `Deployments` in specific clusters and then retry the curl command from the client `Pod` in those regions. Observe that the application is still available, and look at the location of the `Pod` that responds to the request.

  1. Run the curl command from the _client-west_ `Pod` in the _std-west_ cluster, and see that the result comes from the frontend in _us-west1_ :
         
         kubectl exec -it --context=std-west client-west \
             -- curl -H 'HOST: store.example.com' $EXTERNAL_LB_IP  | \
                    grep -e Cluster -e Zone -e Pod
         

The successful output of the curl command is similar to the following example:
         
         <b>Cluster: </b>std-west<br/>
         <b>Zone: </b>us-west1-a<br/>
         <b>Pod: </b>frontend-7cf48b79cf-trzc4
         

  2. Delete the _frontend_ `Deployment` in the _std-west_ cluster:
         
         kubectl delete deploy frontend \
             -n onlineboutique --context=std-west
         

The output is similar to the following example:
         
         deployment.apps "frontend" deleted
         

  3. Send another request from the _client-west_ `Pod` in the _std-west_ cluster. You should see a response from one of the remaining _frontend_ `Deployments` located in the _auto-east_ or _auto-central_ clusters:
         
         kubectl exec -it --context=std-west client-west \
             -- curl -H 'HOST: store.example.com' $EXTERNAL_LB_IP | \
                    grep -e Cluster -e Zone -e Pod
         

Output similar to the following example indicates the location of the healthy `Pod` that responds to this request:
         
         <b>Cluster: </b>auto-central<br/>
         <b>Zone: </b>us-central1-b<br/>
         <b>Pod: </b>frontend-6784b6df98-x2fv4
         

or
         
         <b>Cluster: </b>auto-east<br/>
         <b>Zone: </b>us-east1-d<br/>
         <b>Pod: </b>frontend-6784b6df98-scdws
         

Run the command several times to see alternating results.




With this demonstration deployment, you have added elements of resiliency and geographic distribution to the Online Boutique application using multi-cluster Services and multi-cluster Gateways. Requests are routed to the closest geographical region and even if the frontend or middleware services in a region experience issues, the end user is still able to successfully use the application.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Read more about [Google Cloud fleet and multi-cluster management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).
  * Learn about [how to register a cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation), including GKE clusters, to a Google Cloud fleet.
  * Dive deeper into the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) and the [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2022-02-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-02-17 UTC."],[],[]] 
