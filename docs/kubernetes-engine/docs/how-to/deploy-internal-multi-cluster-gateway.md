---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-internal-multi-cluster-gateway/
title: Deploy an internal multi-cluster Gateway \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:11.367697+00:00
---

# Deploy an internal multi-cluster Gateway  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-internal-multi-cluster-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploy an internal multi-cluster Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document guides you through a practical example to deploy an internal multi-cluster Gateway to route traffic within your VPC network to an application that runs in two different GKE clusters.

Multi-cluster Gateways provide a powerful way to manage traffic for services deployed across multiple GKE clusters. By using Google's global load-balancing infrastructure, you can create a single entry point for your applications, which simplifies management and improves reliability. 

In this tutorial, you use a sample `store` application to simulate a real-world scenario where an online shopping service is owned and operated by separate teams and deployed across a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) of shared GKE clusters.

This example shows you how to set up path-based routing to direct traffic to different clusters. 

## Before you begin

Multi-cluster Gateways require some environmental preparation before they can be deployed. Before you proceed, follow the steps in [Prepare your environment for multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-environment-multi-cluster-gateways):

  1. [Deploy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-environment-multi-cluster-gateways#deploy-clusters) GKE clusters.

  2. [Register](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster_on) your clusters to a fleet (if they aren't already).

  3. [Enable](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-environment-multi-cluster-gateways#enable_multi-cluster_services_in_the_fleet) the multi-cluster Service and multi-cluster Gateway controllers.




Finally, review the GKE Gateway controller [limitations and known issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#limitations) before you use the controller in your environment.

## Deploy an internal multi-cluster Gateway across regions

You can deploy multi-cluster Gateways that provide internal Layer 7 load balancing across GKE clusters in multiple regions. These Gateways use the `gke-l7-cross-regional-internal-managed-mc` GatewayClass. This GatewayClass provisions a cross-region internal Application Load Balancer that's managed by Google Cloud and that enables internal VIPs that clients within your VPC network can access. These Gateways can be exposed by frontends in the regions of your choice, simply by using the Gateway to request addresses in those regions. The internal VIP can be a single IP address, or they can be IP addresses in multiple regions, with one IP address per region that's specified in the Gateway. Traffic is directed to the closest healthy backend GKE cluster that can serve the request.

### Prerequisites

  1. Set up your project and shell by configuring your `gcloud` environment with your project ID:
         
         export PROJECT_ID="YOUR_PROJECT_ID"
         gcloud config set project ${PROJECT_ID}
         

  2. Create GKE clusters in different regions.

This example uses two clusters, `gke-west-1` in `us-west1` and `gke-east-1` in `us-east1`. Ensure the Gateway API is enabled (`--gateway-api=standard`) and clusters are registered to a fleet.
         
         gcloud container clusters create gke-west-1 \
             --location=us-west1-a \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --project=${PROJECT_ID} \
             --enable-fleet \
             --gateway-api=standard
         
         gcloud container clusters create gke-east-1 \
             --location=us-east1-c \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --project=${PROJECT_ID} \
             --enable-fleet \
             --gateway-api=standard
         

Rename contexts for easier access:
         
         gcloud container clusters get-credentials gke-west-1 \
           --location=us-west1-a \
           --project=${PROJECT_ID}
         
         gcloud container clusters get-credentials gke-east-1 \
           --location=us-east1-c \
           --project=${PROJECT_ID}
         kubectl config rename-context gke_${PROJECT_ID}_us-west1-a_gke-west-1 gke-west1
         kubectl config rename-context gke_${PROJECT_ID}_us-east1-c_gke-east-1 gke-east1
         

  3. Enable Multi-Cluster Services (MCS) and Multi-Cluster Ingress (MCI/Gateway):
         
         gcloud container fleet multi-cluster-services enable --project=${PROJECT_ID}
         
         # Set the config membership to one of your clusters (e.g., gke-west-1)
         # This cluster will be the source of truth for multi-cluster Gateway and Route resources.
         gcloud container fleet ingress enable \
             --config-membership=projects/${PROJECT_ID}/locations/us-west1/memberships/gke-west-1 \
             --project=${PROJECT_ID}
         

  4. Configure proxy-only subnets. A proxy-only subnet is required in each region where your GKE clusters are located and where the load balancer will operate. Cross-region internal Application Load Balancers require the purpose of this subnet to be set to `GLOBAL_MANAGED_PROXY`.
         
         # Proxy-only subnet for us-west1
         gcloud compute networks subnets create us-west1-proxy-only-subnet \
             --purpose=GLOBAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=us-west1 \
             --network=default \
             --range=10.129.0.0/23 # Choose an appropriate unused CIDR range
         
         # Proxy-only subnet for us-east1
         gcloud compute networks subnets create us-east1-proxy-only-subnet \
             --purpose=GLOBAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=us-east1 \
             --network=default \
             --range=10.130.0.0/23 # Choose an appropriate unused CIDR range
         

If you're not using the default network, replace `default` with the name of your VPC network. Ensure that the CIDR ranges are unique and don't overlap.

  5. Deploy your demo applications, such as `store`, to both clusters. The example `store.yaml` file from `gke-networking-recipes` creates a `store` namespace and a deployment.
         
         kubectl apply --context gke-west1 -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/main/gateway/gke-gateway-controller/multi-cluster-gateway/store.yaml
         kubectl apply --context gke-east1 -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/main/gateway/gke-gateway-controller/multi-cluster-gateway/store.yaml
         

  6. Export Services from each cluster by creating Kubernetes Service resources and ServiceExport resources in each cluster, which makes the services discoverable across the fleet. The following example exports a generic `store` service and region-specific services (`store-west-1`, `store-east-1`) from each cluster, all within the `store` namespace.

Apply to `gke-west1`:
         
         cat << EOF | kubectl apply --context gke-west1 -f -
         apiVersion: v1
         kind: Service
         metadata:
           name: store
           namespace: store
         spec:
           selector:
             app: store
           ports:
           - port: 8080
             targetPort: 8080
         ---
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
           name: store
           namespace: store
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: store-west-1 # Specific to this cluster
           namespace: store
         spec:
           selector:
             app: store
           ports:
           - port: 8080
             targetPort: 8080
         ---
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
           name: store-west-1 # Exporting the region-specific service
           namespace: store
         EOF
         

Apply to `gke-east1`:
         
         cat << EOF | kubectl apply --context gke-east1 -f -
         apiVersion: v1
         kind: Service
         metadata:
           name: store
           namespace: store
         spec:
           selector:
             app: store
           ports:
           - port: 8080
             targetPort: 8080
         ---
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
           name: store
           namespace: store
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: store-east-1 # Specific to this cluster
           namespace: store
         spec:
           selector:
             app: store
           ports:
           - port: 8080
             targetPort: 8080
         ---
         kind: ServiceExport
         apiVersion: net.gke.io/v1
         metadata:
           name: store-east-1 # Exporting the region-specific service
           namespace: store
         EOF
         

  7. Check ServiceImports: Verify that ServiceImport resources are created in each cluster within the `store` namespace. It might take a few minutes for them to be created. `bash kubectl get serviceimports --context gke-west1 -n store kubectl get serviceimports --context gke-east1 -n store` You should see `store`, `store-west-1`, and `store-east-1` listed (or relevant entries based on propagation).




### Configure an internal multi-region Gateway

Define a `Gateway` resource that references the `gke-l7-cross-regional-internal-managed-mc` GatewayClass. You apply this manifest to your designated config cluster, such as `gke-west-1`.

The `spec.addresses` field lets you request ephemeral IP addresses in specific regions or use pre-allocated static IP addresses.

  1. To use ephemeral IP addresses, save the following `Gateway` manifest as `cross-regional-gateway.yaml`:
         
         # cross-regional-gateway.yaml
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: internal-cross-region-gateway
           namespace: store # Namespace for the Gateway resource
         spec:
           gatewayClassName: gke-l7-cross-regional-internal-managed-mc
           addresses:
           # Addresses across regions. Address value is allowed to be empty or matching
           # the region name.
           - type: networking.gke.io/ephemeral-ipv4-address/us-west1
             value: "us-west1"
           - type: networking.gke.io/ephemeral-ipv4-address/us-east1
             value: "us-east1"
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               kinds:
               - kind: HTTPRoute # Only allow HTTPRoute to attach
         

The following list defines some of the fields in the previous YAML file:

     * **`metadata.namespace`** : the namespace where the Gateway resource is created, for example, `store`.
     * **`spec.gatewayClassName`** : the name of the GatewayClass. Must be `gke-l7-cross-regional-internal-managed-mc`.
     * **`spec.listeners.allowedRoutes.kinds`** : the kinds of Route objects that can be attached, for example, `HTTPRoute`.
     * **`spec.addresses`** : 
       * **`type: networking.gke.io/ephemeral-ipv4-address/ REGION`**: requests an ephemeral IP address.
       * **`value`** : specifies the region for the address, for example, `"us-west1"` or `"us-east1"`.
  2. Apply the manifest to your config cluster, for example, `gke-west1`:
         
         kubectl apply --context gke-west1 -f cross-regional-gateway.yaml
         




### Attach HTTPRoutes to the Gateway

Define `HTTPRoute` resources to manage traffic routing and apply them to your config cluster.

  1. Save the following `HTTPRoute` manifest as `store-route.yaml`:
         
         # store-route.yaml
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-route
           namespace: store
           labels:
             gateway: cross-regional-internal
         spec:
           parentRefs:
           - name: internal-cross-region-gateway
             namespace: store # Namespace where the Gateway is deployed
           hostnames:
           - "store.example.internal" # Hostname clients will use
           rules:
           - matches: # Rule for traffic to /west
             - path:
                 type: PathPrefix
                 value: /west
             backendRefs:
             - group: net.gke.io # Indicates a multi-cluster ServiceImport
               kind: ServiceImport
               name: store-west-1 # Targets the ServiceImport for the west cluster
               port: 8080
           - matches: # Rule for traffic to /east
             - path:
                 type: PathPrefix
                 value: /east
             backendRefs:
             - group: net.gke.io
               kind: ServiceImport
               name: store-east-1 # Targets the ServiceImport for the east cluster
               port: 8080
           - backendRefs: # Default rule for other paths (e.g., /)
             - group: net.gke.io
               kind: ServiceImport
               name: store # Targets the generic 'store' ServiceImport (any region)
               port: 8080
         

The following list defines some of the fields in the previous YAML file:

     * **`spec.parentRefs`** : attaches this route to `internal-cross-region-gateway` in the `store` namespace.
     * **`spec.hostnames`** : represents the hostname that clients use to access the service.
     * **`spec.rules`** : defines routing logic. This example uses path-based routing: 
       * `/west` traffic goes to `store-west-1` ServiceImport.
       * `/east` traffic goes to `store-east-1` ServiceImport.
       * All other traffic, such as `/`, goes to the generic `store` ServiceImport.
     * **`backendRefs`** : 
       * `group: net.gke.io` and `kind: ServiceImport` target multi-cluster services.
  2. Apply the `HTTPRoute` manifest to your config cluster:
         
         kubectl apply --context gke-west1 -f store-route.yaml
         




### Verify the status of the Gateway and Route

  1. Check the Gateway status:
         
         kubectl get gateway internal-cross-region-gateway -n store -o yaml --context gke-west1
         

Look for a condition with `type:`Programmed`and`status: "True"`. You should see IP addresses assigned in the`status.addresses`field, corresponding to the regions you specified (e.g., one for`us-west1`and one for`us-east1`).

  2. Check the HTTPRoute status:
         
         kubectl get httproute store-route -n store -o yaml --context gke-west1
         

Look for a condition in `status.parents[].conditions` with `type: Accepted` (or `ResolvedRefs`) and `status: "True"`.




### Confirm traffic

After you assign the IP addresses to the Gateway, you can test traffic from a client VM that's within your VPC network and in one of the regions, or in a region that can connect to the Gateway IP address.

  1. Retrieve the Gateway IP addresses.

The following command attempts to parse the JSON output. You might need to adjust the `jsonpath` based on the exact structure.
         
         kubectl get gateway cross-region-gateway -n store --context gke-west1 -o=jsonpath="{.status.addresses[*].value}".
         

The output of this command should include the VIPs, such as `VIP1_WEST`, or `VIP2_EAST`.

  2. Send test requests: From a client VM in your VPC:
         
         # Assuming VIP_WEST is an IP in us-west1 and VIP_EAST is an IP in us-east1
         # Traffic to /west should ideally be served by gke-west-1
         curl -H "host: store.example.internal" http://VIP_WEST/west
         curl -H "host: store.example.internal" http://VIP_EAST/west # Still targets store-west-1 due to path
         
         # Traffic to /east should ideally be served by gke-east-1
         curl -H "host: store.example.internal" http://VIP_WEST/east # Still targets store-east-1 due to path
         curl -H "host: store.example.internal" http://VIP_EAST/east
         
         # Traffic to / (default) could be served by either cluster
         curl -H "host: store.example.internal" http://VIP_WEST/
         curl -H "host: store.example.internal" http://VIP_EAST/
         

The response should include details from the `store` application that indicate which backend pod served the request, such as `cluster_name` or `zone`.




### Use static IP Addresses

Instead of ephemeral IP addresses, you can use pre-allocated static internal IP addresses.

  1. Create static IP addresses in the regions that you want to use:
         
         gcloud compute addresses create cross-region-gw-ip-west --region us-west1 --subnet default --project=${PROJECT_ID}
         gcloud compute addresses create cross-region-gw-ip-east --region us-east1 --subnet default --project=${PROJECT_ID}
         

If you're not using the default subnet, replace `default` with the name of the subnet that has the IP address you want to allocate. These subnets are regular subnets, _not_ the proxy-only subnets.

  2. Update the Gateway manifest by modifying the `spec.addresses` section in your `cross-regional-gateway.yaml` file:
         
         # cross-regional-gateway-static-ip.yaml
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: internal-cross-region-gateway # Or a new name if deploying alongside
           namespace: store
         spec:
           gatewayClassName: gke-l7-cross-regional-internal-managed-mc
           addresses:
           - type: networking.gke.io/named-address-with-region # Use for named static IP
             value: "regions/us-west1/addresses/cross-region-gw-ip-west"
           - type: networking.gke.io/named-address-with-region
             value: "regions/us-east1/addresses/cross-region-gw-ip-east"
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             allowedRoutes:
               kinds:
               - kind: HTTPRoute
         

  3. Apply the updated Gateway manifest.
         
         kubectl apply --context gke-west1 -f cross-regional-gateway.yaml
         




### Special considerations for non-default subnets

Be aware of the following considerations when you use non-default subnets:

  * **Same VPC network:** all user-created resources—such as static IP addresses, proxy-only subnets, and GKE clusters—must reside within the same VPC network.

  * **Address subnet:** when you create static IP addresses for the Gateway, they are allocated from regular subnets in the specified regions.

  * **Cluster subnet naming:** Each region must have a subnet that has the same name as the subnet that the MCG config cluster resides in.

    * For example, if your `gke-west-1` config cluster is in `projects/YOUR_PROJECT/regions/us-west1/subnetworks/my-custom-subnet`, then the regions you are requesting addresses for must also have the `my-custom-subnet` subnet. If you request addresses in the `us-east1` and `us-centra1` regions, then a subnet named `my-custom-subnet` must also exist in those regions.



## Clean up

After completing the exercises on this document, follow these steps to remove resources and prevent unwanted charges incurring on your account:

  1. [Delete the clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).

  2. [Unregister the clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister) from the fleet if they don't need to be registered for another purpose.

  3. Disable the `multiclusterservicediscovery` feature:
         
         gcloud container fleet multi-cluster-services disable
         

  4. Disable Multi Cluster Ingress:
         
         gcloud container fleet ingress disable
         

  5. Disable the APIs:
         
         gcloud services disable \
             multiclusterservicediscovery.googleapis.com \
             multiclusteringress.googleapis.com \
             trafficdirector.googleapis.com \
             --project=PROJECT_ID
         




## Troubleshooting

### Proxy-only subnet for internal Gateway does not exist

If the following event appears on your internal Gateway, a proxy-only subnet does not exist for that region. To resolve this issue, deploy a proxy-only subnet.
    
    
    generic::invalid_argument: error ensuring load balancer: Insert: Invalid value for field 'resource.target': 'regions/us-west1/targetHttpProxies/gkegw-x5vt-default-internal-http-2jzr7e3xclhj'. A reserved and active subnetwork is required in the same region and VPC as the forwarding rule.
    

### No healthy upstream

**Symptom:**

The following issue might occur when you create a Gateway but cannot access the backend services (503 response code):
    
    
    no healthy upstream
    

**Reason:**

This error message indicates that the health check prober cannot find healthy backend services. It is possible that your backend services are healthy but you might need to customize the health checks.

**Workaround:**

To resolve this issue, [customize your health check](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check) based on your application's requirements (for example, `/health`) using a `HealthCheckPolicy`.

## What's next

  * Learn more about the [Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * To configure backend authenticated TLS for your multi-cluster Gateway, see [Configure backend TLS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-tls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
