---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways/
title: Deploying Gateways \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:06.940616+00:00
---

# Deploying Gateways  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploying Gateways Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Deploy Kubernetes Gateway resources to manage how external traffic reaches applications within a single Google Kubernetes Engine (GKE) cluster. Configuring GKE Gateway provides flexible and powerful control over ingress traffic, improving the scalability and reliability of your applications. For example, GKE Gateway offers optimized routing and autoscaling capabilities. These capabilities are essential for low-latency online serving, ensuring a responsive user experience while helping control costs.

To deploy Gateways across multiple clusters or a fleet, see [Deploying Multi-Cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways). For specific Gateway configurations like cross-namespace routing and HTTP traffic splitting, refer to [Gateway API user guides](https://gateway-api.sigs.k8s.io/guides/).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).

  * Ensure that your user account has the Certificate Manager Editor (`roles/certificatemanager.editor`) role so you can create the necessary certificate maps.




### GKE Gateway controller requirements

  * Gateway API is supported on [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) clusters only.
  * If you are using the regional or cross-region GatewayClasses, you must enable a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  * Your cluster must have the `HttpLoadBalancing` add-on enabled.
  * If you are using Istio, you must upgrade Istio to one of the following versions: 
    * 1.15.2 or later
    * 1.14.5 or later
    * 1.13.9 or later.
  * If you are using Shared VPC, then in the host project, you need to assign the `Compute Network User` role to the GKE Service account for the service project. 



### Restrictions and limitations

When using GKE Gateway, understand the following limitations and restrictions:

  * GKE GatewayClasses support different capabilities depending on the load balancer they use. To learn more about the different features supported with each GatewayClass, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

**Best practice** : 

For optimal performance, limit the number of Gateways to a maximum of 100. Exceeding this limit can affect performance or result in increased latency.

  * GKE Gateway only supports the [Gateway API Standard release channel](https://gateway-api.sigs.k8s.io/docs/concepts/versioning/).

  * GKE Gateway is always enabled on Autopilot clusters. You can't install Gateway API Experimental release channel CRDs on Autopilot clusters.

  * You cannot use a [FrontendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_frontendconfig_parameters) or a [BackendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_backendconfig_parameters) to configure a Gateway. You must use a [Policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).

  * GKE Gateway behaves differently than Ingress, in that Gateway does not infer health check parameters. If your Service does not return 200 for requests to `GET /`, or you have other tuned pod readiness checks, you need to [configure a HealthCheckPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check) for your service.

  * You cannot specify a port number directly in the hostname (for example, web.example.com:80) for traffic routing.

  * You can view the load balancer resources that GKE creates for Gateways in the Google Cloud console, but these resources don't reference the Gateway or GKE cluster they are attached to.

  * You can't automatically generate a Google-managed SSL certificate with Gateways but you can manually create and reference a Google-managed SSL certificate. For more information, see [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).

  * HTTPRoute is the only Route type supported. TCPRoutes, UDPRoutes, and TLSRoutes are not supported. To see a list of fields the GKE Gateway controller supports, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

  * Custom request and response headers with Gateway or path redirects and URL rewrites with Gateway is only available on GKE version 1.27 or later.

  * For custom request and response headers with Gateway and path redirects and URL rewrites with Gateway, the GatewayClass `gke-l7-gxlb` is not supported.

  * When configuring HTTPRoute custom request headers, the [Google Cloud variable](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global#variables) `origin_request_header` is not supported. To configure CORS, you can use the `CORS` filter type.

  * Google Cloud classic Application Load Balancer limitations apply to the GKE Gateway. In addition, you can't configure a custom Host response header in the backend service.

  * Path redirects and URL rewrites are mutually exclusive, you can't use both filters at the same time in the same rules.

  * Redirecting traffic to a different port is not supported with Cloud Load Balancing. To see the list of fields the GKE Gateway controller supports, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

  * GKE Gateway does not support [Wildcards, regular expressions, and dynamic URLs](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#wildcards-regx-dynamic).

  * If you specify a Gateway with a regional external gateway class, the controller provisions an internal IP address instead of the external address. To learn how to use a named address with the regional external Application Load Balancer, see deploy a regional external Gateway.

  * Gateway utilizes [Standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#standalone_negs) for provisioning Network Endpoint Groups. To help ensure that the Gateway controller properly reconciles the load balancer configuration, you cannot modify the `cloud.google.com/neg` annotation for a Service that is part of the Gateway.

  * GKE Gateway does not support referencing a Service that is also referenced by a GKE Ingress.

  * When a Gateway is configured to provision an IP address, changing the `Gateway.spec.gatewayClass` is not supported. To help ensure that the Gateway controller properly reconciles the load balancer, delete the existing Gateway and re-deploy the manifest with the updated `gatewayClass` value.

  * The `networking.gke.io/app-protocols` annotation is not supported. Use the [`appProtocol` field](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#load-balancer-tls) instead to achieve the same result.

  * If you use GKE Gateway with [`external-dns`](https://github.com/kubernetes-sigs/external-dns) and the health state of the Gateway is unhealthy, by default, all DNS records associated with the Gateway are deleted from your DNS zones.

**Best practice** : 

When running `external-dns`, set the `policy=upsert-only` flag. This configuration helps to prevent the deletion of existing DNS records.

  * If a port is removed from a Service that GKE Gateway references through a route, the [Standalone NEG annotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg) on the Service you must also update the Standalone NEG controller on the Service to remove that port. If you don't, the NEG controller eventually stops syncing Pod endpoints for this Service. For details, see [NEG Controller stops managing endpoints when port removed from Service](https://docs.cloud.google.com/kubernetes-engine/networking/docs/known-issues#service-remove-port-neg-controller).

  * Deployments using Multi-Cluster Gateways (MCG) that use _zonal_ clusters are susceptible to service disruptions during cluster upgrades. This issue occurs because a legacy Network Endpoint Group (NEG) discovery mechanism might incorrectly report zero backends when the zonal cluster's control plane is temporarily unavailable. A long-term fix is in progress. To avoid this single point of failure, use **regional** GKE clusters with MCG.




## Enable Gateway API in your cluster

Before using Gateway resources in GKE, your cluster must have Gateway API enabled.

Before you update an existing GKE cluster to enable Gateway API, make sure that the minimum requirements are met before proceeding with the update.

To enable Gateway API on an existing GKE cluster (Autopilot or Standard), use the following command. This operation might take up to 45 minutes for the cluster to reconcile and install the CustomResourceDefinition.
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CLUSTER_LOCATION\
        --gateway-api=standard
    

Replace the following:

  * `CLUSTER_NAME`: the name of the existing cluster.

  * `CLUSTER_LOCATION`: the [Compute Engine region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster.




The `--gateway-api=standard` flag instructs GKE to install the CRDs of the Gateway API Standard Channel with the cluster.

## Verify your cluster

After creating or upgrading your cluster, the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) automatically installs GatewayClasses. It might take a few minutes for the controller to recognize the CRDs and install the GatewayClasses.

  1. Confirm Gateway API is enabled in the GKE control plane:
         
         gcloud container clusters describe CLUSTER_NAME \
           --location=CLUSTER_LOCATION \
           --format json
         

The output is similar to the following. If this output is empty, re-run the cluster update command.
         
         "networkConfig": {
           ...
           "gatewayApiConfig": {
             "channel": "CHANNEL_STANDARD"
           },
           ...
         },
         

  2. Confirm the GatewayClasses are installed in your cluster:
         
         kubectl get gatewayclass
         

The output is similar to the following:
         
         NAME                             CONTROLLER                  ACCEPTED   AGE
         gke-l7-global-external-managed   networking.gke.io/gateway   True       16h
         gke-l7-regional-external-managed networking.gke.io/gateway   True       16h
         gke-l7-gxlb                      networking.gke.io/gateway   True       16h
         gke-l7-rilb                      networking.gke.io/gateway   True       16h
         




To understand the capabilities of each GatewayClass, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

Only single-cluster GatewayClasses are installed automatically. To install and use the multi-cluster GatewayClasses for internal and external multi-cluster load balancing, see [Enabling multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways).

## Deploy an internal Gateway

An internal Gateway exposes applications that are only reachable from within the VPC or networks connected to the VPC.

### Deploy a regional internal Gateway

The following example shows you how to deploy a regional internal Gateway that enables efficient and secure communication between services within a specific geographic region.

#### Configure a proxy-only subnet

You must [configure a proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#proxy_only_subnet_create) before you create a Gateway that uses an internal Application Load Balancer. Each region of a VPC in which you use internal Application Load Balancers must have a proxy-only subnet. This subnet provides internal IP addresses to the load balancer proxies.

  1. Create a proxy-only subnet:
         
         gcloud compute networks subnets create SUBNET_NAME \
             --purpose=REGIONAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=COMPUTE_REGION \
             --network=VPC_NETWORK_NAME \
             --range=CIDR_RANGE
         

Replace the following:

     * `SUBNET_NAME`: the name of the proxy-only subnet.
     * `COMPUTE_REGION`: the region of the proxy-only subnet.
     * `VPC_NETWORK_NAME`: the name of the VPC network in which you create this proxy-only subnet. Ensure this is the same VPC network where your GKE cluster resides and where you deploy the Gateway. This is important for seamless communication between the load balancer and your backend services.
     * `CIDR_RANGE`: the primary IP address range of the subnet. You must use a subnet mask no longer than `/26` so that at least 64 IP addresses are available for proxies in the region. The recommended subnet mask is `/23`.
  2. Verify your proxy-only subnet:
         
         gcloud compute networks subnets describe SUBNET_NAME \
             --region=COMPUTE_REGION
         

The output is similar to the following:
         
         ...
         gatewayAddress: 10.1.1.1
         ipCidrRange: 10.1.1.0/24
         kind: compute#subnetwork
         name: proxy-subnet
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/networks/default
         privateIpGoogleAccess: false
         privateIpv6GoogleAccess: DISABLE_GOOGLE_ACCESS
         purpose: REGIONAL_MANAGED_PROXY
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/REGION
         role: ACTIVE
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/REGION/subnetworks/proxy-subnet
         state: READY
         




#### Create a Gateway

A Gateway resource represents a data plane that routes traffic in Kubernetes. A Gateway can represent many different kinds of load balancing and routing depending on the GatewayClass it is derived from. To learn more about the Gateway resource, see the [Gateway resource](https://gateway-api.sigs.k8s.io/api-types/gateway/) description or the [API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.Gateway).

In this case, the administrator of the GKE cluster wants to create a Gateway that can be used by different teams to expose their applications internally. The administrator deploys the Gateway, and application teams deploy their Routes independently and attach them to this Gateway.

  1. Save the following Gateway manifest to a file named `gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
            name: internal-http
         spec:
           # Specify an existing GatewayClass.
           gatewayClassName: gke-l7-rilb
           listeners:
           # Listen for HTTP traffic on port 80.
           - name: http
             protocol: HTTP
             port: 80
         

This manifest includes the following fields:

     * `gatewayClassName: gke-l7-rilb`: specifies the GatewayClass that this Gateway is derived from. `gke-l7-rilb` corresponds to the internal Application Load Balancer.
     * `port: 80`: specifies that the Gateway exposes only port 80 for listening for HTTP traffic.

This Gateway is configured to handle HTTP traffic only on port 80. It doesn't support HTTPS (port 443) by default, and if you attempt to connect over HTTPS, the request might fail.

  2. Deploy the Gateway in your cluster:
         
         kubectl apply -f gateway.yaml
         

  3. Validate that the Gateway has deployed correctly. It might take a few minutes for it to deploy all of its resources.
         
         kubectl describe gateways.gateway.networking.k8s.io internal-http
         

The output is similar to the following:
         
         Name:         internal-http
         Namespace:    default
         Spec:
           Gateway Class Name:  gke-l7-rilb
           Listeners:
             Allowed Routes:
               Kinds:
                 Group:  gateway.networking.k8s.io
                 Kind:   HTTPRoute
               Namespaces:
                 From:  Same
             Name:      http
             Port:      80
             Protocol:  HTTP
          Status:
            Addresses:
              Type:   IPAddress
              Value:  192.168.1.14
            Conditions:
              Last Transition Time:  2025-03-19T19:53:46Z
              Message:               The OSS Gateway API has deprecated this condition, do not depend on it.
              Observed Generation:   1
              Reason:                Scheduled
              Status:                True
              Type:                  Scheduled
              Last Transition Time:  2025-03-19T19:53:46Z
              Message:
              Observed Generation:   1
              Reason:                Accepted
              Status:                True
              Type:                  Accepted
              **Last Transition Time:  2025-03-19T19:53:46Z
              Message:
              Observed Generation:   1
              Reason:                Programmed
              Status:                True # Indicates that the Gateway is ready.
              Type:                  Programmed**
              Last Transition Time:  2025-03-19T19:53:46Z
              Message:               The OSS Gateway API has altered the "Ready" condition semantics and reserved it for future use.  GKE Gateway will stop emitting it in a future update, use "Programmed" instead.
              Observed Generation:   1
              Reason:                Ready
              Status:                True
              Type:                  Ready
              Last Transition Time:  2025-03-19T19:53:46Z
              Message:
              Observed Generation:   1
              Reason:                Healthy
              Status:                True
              Type:                  networking.gke.io/GatewayHealthy
         Events:
           Type    Reason  Age                From                       Message
           ----    ------  ----               ----                       -------
           Normal  ADD     92s                networking.gke.io/gateway  test/internal-http
           Normal  UPDATE  45s (x3 over 91s)  networking.gke.io/gateway  test/internal-http
           Normal  SYNC    45s                networking.gke.io/gateway  SYNC on test/internal-http was a success
         

In this output, the status of `True` for the `Programmed` condition indicates that the Gateway is ready.

At this point, there is a Gateway deployed in your cluster that has provisioned a load balancer and an IP address. The Gateway has no Routes, however, and so it doesn't know how it should send traffic to backends. Without Routes, all traffic goes to a default backend, which returns an HTTP 404. Next, you deploy an application and Routes, which tell the Gateway how to get to application backends.




#### Deploy the demo applications

Application teams can deploy their applications and Routes independently from the deployment of Gateways. In some cases the application team might want to own the Gateway as well and deploy it themselves as a resource dedicated to their applications. See [Route binding](https://gateway-api.sigs.k8s.io/concepts/api-overview/#route-binding) for different ownership models of Gateways and Routes. In this example however, the store team deploys their application and an accompanying HTTPRoute to expose their app through the `internal-http` Gateway created in the previous section.

The HTTPRoute resource has many configurable fields for traffic matching. For an explanation of HTTPRoute's fields, see the [API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.HTTPRoute).

  1. Deploy the store application (store-v1, store-v2, and store-german deployments) to your cluster:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/main/gateway/gke-gateway-controller/app/store.yaml
         

This creates three Deployments and three Services which are named store-v1, store-v2, and store-german.

  2. Validate that the application has deployed successfully:
         
         kubectl get pod
         

The output is similar to the following after the application is running:
         
         NAME                        READY   STATUS    RESTARTS   AGE
         store-german-66dcb75977-5gr2n   1/1     Running   0          38s
         store-v1-65b47557df-jkjbm       1/1     Running   0          14m
         store-v2-6856f59f7f-sq889       1/1     Running   0          14m
         

  3. Validate that the Services have been deployed:
         
         kubectl get service
         

The output shows a Service for each store Deployment:
         
         NAME           TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
         store-german   ClusterIP   10.48.3.183   <none>        8080/TCP   4s
         store-v1       ClusterIP   10.48.2.224   <none>        8080/TCP   5s
         store-v2       ClusterIP   10.48.4.48    <none>        8080/TCP   5s
         




#### Deploy the HTTPRoute

Route resources define protocol-specific rules for mapping traffic from a Gateway to Kubernetes backends. The [HTTPRoute resource](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#httproute) does HTTP and HTTPS traffic matching and filtering and is supported by all of the `gke-l7` GatewayClasses.

In this section, you deploy an HTTPRoute, which programs the Gateway with the routing rules needed to reach your store application.

  1. Save the following HTTPRoute manifest to a file named `store-route.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store
         spec:
           # Attach the HTTPRoute to a Gateway.
           parentRefs:
           - kind: Gateway
             name: internal-http
           # Route requests that have `store.example.com` in the Host header.
           hostnames:
           - "store.example.com"
           rules:
           # Send requests with the `env: canary` header to the `store-v2` Service.
           - matches:
             - headers:
               - name: env
                 value: canary
             backendRefs:
             - name: store-v2
               port: 8080
           # Send requests with `/de` in the path to the `store-german` Service.
           - matches:
             - path:
                 value: /de
             backendRefs:
             - name: store-german
               port: 8080
           # Send unmatched requests to the store-v1 Service.
           - backendRefs:
             - name: store-v1
               port: 8080
         

  2. Deploy the HTTProute in your cluster:
         
         kubectl apply -f store-route.yaml
         

The `store` HTTPRoute is bound to the `internal-http` Gateway by using the `parentRefs` property. These routing rules are configured on the underlying load balancer as in this diagram:

![The routing rules configured by the store HTTPRoute](https://docs.cloud.google.com/static/kubernetes-engine/images/httproute-store.svg)

These routing rules process HTTP traffic in the following manner:

     * Traffic to `store.example.com/de` goes to the Service `store-german`.
     * Traffic to `store.example.com` with the HTTP header `"env: canary"` goes to the Service `store-v2`.
     * The remaining traffic to `store.example.com` goes to the Service `store-v1`.
  3. Verify that the HTTPRoute has been deployed:
         
         kubectl describe httproute store
         

The output is similar to the following:
         
         Name:         store
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  gateway.networking.k8s.io/v1
         Kind:         HTTPRoute
         # Multiple lines are omitted here.
         Spec:
           Hostnames:
             store.example.com
           Parent Refs:
             Group:  gateway.networking.k8s.io
             Kind:   Gateway
             Name:   internal-http
           Rules:
             Backend Refs:
               Group:
               Kind:    Service
               Name:    store-v1
               Port:    8080
               Weight:  1
             Matches:
               Path:
                 Type:   PathPrefix
                 Value:  /
             Backend Refs:
               Group:
               Kind:    Service
               Name:    store-v2
               Port:    8080
               Weight:  1
             Matches:
               Headers:
                 Name:   env
                 Type:   Exact
                 Value:  canary
               Path:
                 Type:   PathPrefix
                 Value:  /
             Backend Refs:
               Group:
               Kind:    Service
               Name:    store-german
               Port:    8080
               Weight:  1
             Matches:
               Path:
                 Type:   PathPrefix
                 Value:  /de
         Status:
           Parents:
             Conditions:
               Last Transition Time:  2022-11-01T04:18:52Z
               Message:
               Reason:                Accepted
               Status:                True
               Type:                  Accepted
               Last Transition Time:  2022-11-01T04:18:52Z
               Message:
               Reason:                ReconciliationSucceeded
               Status:                True
               Type:                  Reconciled
             Controller Name:         networking.gke.io/gateway
             Parent Ref:
               Group:  gateway.networking.k8s.io
               Kind:   Gateway
               Name:   internal-http
         Events:
           Type    Reason  Age                From                   Message
           ----    ------  ----               ----                   -------
           Normal  ADD     24m                sc-gateway-controller  default/store
           Normal  SYNC    16m (x4 over 23m)  sc-gateway-controller  Bind of HTTPRoute "default/store" to ParentRef {Group:       gateway.networking.k8s.io",
           # Multiple lines are omitted here.
         

  4. Verify that the HTTPRoute is bound to the Gateway:
         
         kubectl describe gateway
         

The output is similar to the following:
         
         Name:         internal-http
         Namespace:    default
         Labels:       <none>
         <...>
         Status:
           Addresses:
             Type:   IPAddress
             Value:  10.128.15.203
           Conditions:
             Last Transition Time:  2022-11-01T03:47:01Z
             Message:
             Reason:                Scheduled
             Status:                True
             Type:                  Scheduled
             Last Transition Time:  2022-11-01T03:47:01Z
             Message:
             Reason:                Ready
             Status:                True
             Type:                  Ready
           Listeners:
         **Attached Routes:  1**
             Conditions:
               Last Transition Time:  2022-11-01T03:47:01Z
               Message:
               Reason:                Ready
               Status:                True
               Type:                  Ready
             Name:                    http
             Supported Kinds:
               Group:  gateway.networking.k8s.io
               Kind:   HTTPRoute
               <...>
         




#### Send traffic to your application

Now that your Gateway, Route, and application are deployed in your cluster, you can pass traffic to your application. The Gateway is configured to serve HTTP traffic only on port 80. Requests made with HTTPS might fail unless TLS has been separately configured.

  1. Retrieve the IP address from the Gateway so that you can send traffic to your application:
         
         kubectl get gateways.gateway.networking.k8s.io internal-http -o=jsonpath="{.status.addresses[0].value}"
         

The output is an IP address.

  2. Send traffic to this IP address from a virtual machine (VM) instance with connectivity to the cluster. This is necessary because the Gateway has an internal IP address and is only accessible from within your VPC network. Because the `internal-http` is a regional load balancer, the client VM must be within the same region as the GKE cluster.

Create a test VM in the same VPC network and region:
         
         gcloud compute instances create test-vm \
             --zone=COMPUTE_ZONE \
             --network=VPC_NETWORK_NAME
         

Connect to the VM by using SSH:
         
         gcloud compute ssh test-vm --zone=COMPUTE_ZONE
         

From within the VM's shell, make a request to `store.example.com`:
         
         curl http://store.example.com --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
         

Replace `GATEWAY_IP_ADDRESS` with the IP address from the previous step.

The output from the demo app shows information about the location where the app is running:
         
         {
           "cluster_name": "gke1",
           "host_header": "store.example.com",
           "metadata": "store-v1",
           "node_name": "gke-gke1-pool-2-bd121936-5pfc.c.gateway-demo-243723.internal",
           "pod_name": "store-v1-84b47c7f58-pmgmk",
           "pod_name_emoji": "💇🏼‍♀️",
           "project_id": "gateway-demo-243723",
           "timestamp": "2022-10-25T13:31:17",
           "zone": "ZONE_NAME"
         }
         

  3. Test the path match by going to the German version of the store service at `store.example.com/de`:
         
         curl http://store.example.com/de --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
         

The output confirms that the request was served by a `store-german` Pod:
         
         {
           "cluster_name": "gke1",
           "host_header": "store.example.com",
           **"metadata" : "Gutentag!", **
           "node_name": "gke-gke1-pool-2-bd121936-n3xn.c.gateway-demo-243723.internal",
           **"pod_name" : "store-german-5cb6474c55-lq5pl", **
           "pod_name_emoji": "🧞‍♀",
           "project_id": "gateway-demo-243723",
           "timestamp": "2022-10-25T13:35:37",
           "zone": "ZONE_NAME"
         }
         

  4. Finally, use the `env: canary` HTTP header to send traffic to the canary version of the store Service:
         
         curl -H "env: canary" http://store.example.com --resolve store.example.com:80:GATEWAY_IP_ADDRESS -v
         

The output confirms that the request was served by a `store-v2` Pod:
         
         {
           "cluster_name": "gke1",
           "host_header": "store.example.com",
           **"metadata" : "store-v2", **
           "node_name": "gke-gke1-pool-2-bd121936-5pfc.c.gateway-demo-243723.internal",
           **"pod_name" : "store-v2-5788476cbd-s9thb", **
           "pod_name_emoji": "🦰",
           "project_id": "gateway-demo-243723",
           "timestamp": "2022-10-25T13:38:26",
           "zone": "ZONE_NAME"
         }
         




## Deploy an external Gateway

An external Gateway exposes applications that are reachable from the internet or networks outside of your VPC network. The deployment is similar to an internal Gateway deployment except you must secure your applications because the Gateway is accessible to the public internet.

You have two options to create an external Gateway: a global external Gateway or a regional external Gateway.

  * **Regional external Gateway:** This Gateway uses a regional IP address as the frontend of the Gateway. The behavior of this Gateway depends on the Network Service Tier you select: 
    * If you choose the Standard Network Service Tier (default), the regional IP address is advertised only in the local Google Cloud Compute region where the regional external Gateway is deployed. Clients sending traffic to this IP address are routed by their local ISP and over the public internet before reaching the Google region where the IP address is advertised.
    * If you choose the Premium Network Service Tier, the regional IP address is advertised across Google's global network. This means client traffic enters Google's high-quality global backbone at a Google edge peering point as close as possible to the client, even if the destination is a regional IP address. This location significantly reduces latency and improves performance by minimizing the distance traffic travels over the public internet.
  * **Global external Gateway:** This Gateway uses a global IP address (or Anycast IP address) as the frontend of the Gateway. This IP address is advertised in all Google Cloud Compute regions. Clients sending traffic to this Anycast IP address are routed to the closest Google location where the IP address is advertised. The global external Gateway is only available in the [Premium Network Service Tier](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier).



### Deploy a regional external Gateway

The following example shows you how to expose a store application with multiple certificates attached to the regional external Gateway using self-managed certificates and an HTTPRoute.

#### Create a proxy subnet for your regional Gateway

You must configure a proxy-only subnet before you create a Gateway that uses a regional external Application Load Balancer. Each region of a VPC in which you use regional external Application Load Balancer must have an `external_managed_proxy` subnet. This subnet provides internal IP addresses to the load balancer proxies.

#### Create a certificate to secure your client traffic

You can use a certificate issued and validated by your certificate authority (CA) or create a self-signed certificate. For more information on how to create a certificate, see [Store a certificate in a Kubernetes Secret](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#store-certificate-secret).

To secure traffic between your clients and your regional Gateway, you can use the following methods:

  * Google-managed or self-managed Certificate Manager certificates
  * Self-managed regional SSL certificates
  * Kubernetes Secrets



`CertificateMap` or Google-managed SSL certificates aren't supported with regional Gateways.

For more information, see [Certificates and Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary).

#### Create a regional external HTTP(S) Gateway

  1. Create a regional static IP address for the external load balancer.
         
         gcloud compute addresses create IP_ADDRESS_NAME \
           --region=COMPUTE_REGION \
           --network-tier=STANDARD
         

Replace the following:

     * `IP_ADDRESS_NAME`: the name of the new static IP address.
     * `COMPUTE_REGION`: The Compute Engine region where your cluster is running.
  2. Create a regional external Application Load Balancer Gateway using a self-managed certificate as follows and save the manifest as `regional-gateway.yaml`:
         
         kind: Gateway
           apiVersion: gateway.networking.k8s.io/v1
           metadata:
             name: external-regional-http
           spec:
             # Name of an existing GatewayClass.
             gatewayClassName: gke-l7-regional-external-managed
             # Listen for HTTPS traffic on port 443
             listeners:
             - name: https
               protocol: HTTPS
               port: 443
               tls:
                 # Terminate the TLS session with the client at the Gateway.
                 mode: Terminate
                 # Certificates for the Gateway to use to create a new TLS session.
                 certificateRefs:
                 - name: store-example-com
             # The name of the static IP address of the external load balancer.
             # You can also use the `IPAddress` type to specify the actual IP address.
             addresses:
             - type: NamedAddress
               value: IP_ADDRESS_NAME
         

  3. Apply the `regional-gateway` manifest:
         
         kubectl apply -f regional-gateway.yaml
         

  4. Verify your configuration.
         
         kubectl get gateway
         

The output is similar to the following:
         
         NAME            CLASS                              ADDRESS         READY   AGE
         external-http   gke-l7-regional-external-managed   35.118.32.224   True    49s
         

To get more details, use a describe command:
         
         kubectl describe gateway
         

The output is similar to the following:
         
         Name:         external-regional-http
         Namespace:    default
         Labels:       <none>
         ...
         Spec:
           Gateway Class Name:  gke-l7-regional-external-managed
           Listeners:
             Allowed Routes:
               Namespaces:
                 From:  Same
             Name:      https
             Port:      443
             Protocol:  HTTPS
             Tls:
               Certificate Refs:
                 Group:
                 Kind:   Secret
                 Name:   store-example-com
               Mode:     Terminate
           ...
         




#### Deploy the demo applications

Application teams can deploy their applications and Routes independently from the deployment of Gateways. In some cases the application team might want to own the Gateway as well and deploy it themselves as a resource dedicated to their applications. See [Route binding](https://gateway-api.sigs.k8s.io/concepts/security-model/#1-route-binding) for different ownership models of Gateways and Routes. In this example, the store team deploys their application and an accompanying HTTPRoute to expose their app through the `external-http` Gateway created in the previous section.

For more information about HTTPRoute fields, see the [API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.HTTPRoute).

  1. Deploy the sample application to your cluster:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/main/gateway/gke-gateway-controller/app/store.yaml
         

This sample application creates three Deployments and three Services which are named `store-v1`, `store-v2`, and `store-german`.

  2. Verify that the application has deployed successfully:
         
         kubectl get pod
         

The output is similar to the following:
         
         NAME                            READY   STATUS    RESTARTS   AGE
         store-german-66dcb75977-5gr2n   1/1     Running   0          38s
         store-v1-65b47557df-jkjbm       1/1     Running   0          14m
         store-v2-6856f59f7f-sq889       1/1     Running   0          14m
         

  3. Verify that the Services have deployed successfully:
         
         kubectl get service
         

The output is similar to the following:
         
         NAME           TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
         store-german   ClusterIP   10.48.3.183   <none>        8080/TCP   4s
         store-v1       ClusterIP   10.48.2.224   <none>        8080/TCP   5s
         store-v2       ClusterIP   10.48.4.48    <none>        8080/TCP   5s
         




#### Create an HTTPRoute

Route resources define protocol-specific rules for mapping traffic from a Gateway to Kubernetes backends. The [HTTPRoute resource](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#httproute) does HTTP and HTTPS traffic matching and filtering and is supported by all of the `gke-l7-*` GatewayClasses.

In this section, you deploy an HTTPRoute, which configures the Gateway with routing rules required to reach the sample application.

  1. Save the following manifest to a file named `store-route-external.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-external
         spec:
           parentRefs:
           # Bind the route to the 'external-http' Gateway.
           - kind: Gateway
             name: external-http
           hostnames:
           - "store.example.com"
           rules:
           # Default rule for store.example.com that sends traffic to the store-v1 service.
           - backendRefs:
             - name: store-v1
               port: 8080
           # Match requests with the "env: canary" header and send them to the store-v2 service.
           - matches:
             - headers:
               - name: env
                 value: canary
             backendRefs:
             - name: store-v2
               port: 8080
           # Match requests with the path "/de" and sends them to the store-german service.
           - matches:
             - path:
                 value: /de
             backendRefs:
             - name: store-german
               port: 8080
         

This manifest describes an HTTPRoute that references the `external-http` Gateway.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f store-route-external.yaml
         

The `store` HTTPRoute is bound to the `external-http` Gateway by using the `parentRefs` property. These following diagram shows the routing rules configured on the underlying load balancer:

![The routing rules configured by the store HTTPRoute](https://docs.cloud.google.com/static/kubernetes-engine/images/httproute-store-external.svg)

The routing rules process HTTP traffic as follows:

     * Traffic to `store.example.com/de` routes to Service `store-german`.
     * Traffic to `store.example.com` with the HTTP header `"env: canary"` routes to Service `store-v2`.
     * The remaining traffic to `store.example.com` routes to Service `store-v1`.
  3. Verify that the HTTPRoute has been deployed:
         
         kubectl describe httproute store-external
         

The output is similar to the following:
         
         Name:         store-external
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  gateway.networking.k8s.io/v1
         Kind:         HTTPRoute
         # Multiple lines are omitted here.
         Spec:
           Hostnames:
             store.example.com
           Parent Refs:
             Group:  gateway.networking.k8s.io
             Kind:   Gateway
             Name:   external-http
           Rules:
             Backend Refs:
               Group:
               Kind:    Service
               Name:    store-v1
               Port:    8080
               Weight:  1
             Matches:
               Path:
                 Type:   PathPrefix
                 Value:  /
             Backend Refs:
               Group:
               Kind:    Service
               Name:    store-v2
               Port:    8080
               Weight:  1
             Matches:
               Headers:
                 Name:   env
                 Type:   Exact
                 Value:  canary
               Path:
                 Type:   PathPrefix
                 Value:  /
             Backend Refs:
               Group:
               Kind:    Service
               Name:    store-german
               Port:    8080
               Weight:  1
             Matches:
               Path:
                 Type:   PathPrefix
                 Value:  /de
         Status:
           Parents:
             # This section shows the status of this route in relation to each Gateway attached.
             Conditions:
               Last Transition Time:  2022-11-01T05:42:31Z
               Message:
               Reason:                Accepted
               Status:                True # Means that the Gateway has validated and accepted this route's configuration.
               Type:                  Accepted
               Last Transition Time:  2022-11-01T05:43:18Z
               Message:
               Reason:                ReconciliationSucceeded
               Status:                True
               Type:                  Reconciled
             Controller Name:         networking.gke.io/gateway
             Parent Ref:
               Group:  gateway.networking.k8s.io
               Kind:   Gateway
               Name:   external-http
         Events:
           Type     Reason  Age    From                   Message
           ----     ------  ----   ----                   -------
           Normal   ADD     2m48s  sc-gateway-controller  default/store-external
           Normal  SYNC  61s (x3 over 2m27s)  sc-gateway-controller  Bind of HTTPRoute "default/store-external" to ParentRef Group:       "gateway.networking.k8s.io",
           ...
         

  4. Verify that the HTTPRoute is bound to the Gateway:
         
         kubectl describe gateway external-http
         

The output is similar to the following:
         
         Name:         external-http
         Namespace:    default
         Labels:       <none>
         # Multiple lines are omitted here.
         Status:
           Addresses:
             Type:   IPAddress
             Value:  34.149.207.45
           Conditions:
             Last Transition Time:  2022-11-01T05:37:21Z
             Message:
             Reason:                Scheduled
             Status:                True
             Type:                  Scheduled
             Last Transition Time:  2022-11-01T05:43:18Z
             Message:
             Reason:                Ready
             Status:                True
             Type:                  Ready
           Listeners:
         **Attached Routes:  1**
             Conditions:
               Last Transition Time:  2022-11-01T05:43:18Z
               Message:
               Reason:                Ready
               Status:                True
               Type:                  Ready
             Name:                    https
             Supported Kinds:
               Group:  gateway.networking.k8s.io
               Kind:   HTTPRoute
               # Multiple lines are omitted here.
         




#### Send traffic to your application

Now that your Gateway, Route, and application are deployed in your cluster, you can pass traffic to your application.

  1. Get the IP address of the Gateway:
         
         kubectl get gateways.gateway.networking.k8s.io external-http -o=jsonpath="{.status.addresses[0].value}"
         

The output is an IP address.

  2. Create a VM:
         
         gcloud cloud-shell ssh
         

  3. Send traffic to the Gateway IP address from the VM. You must set the host header manually because you don't own the `example.com` hostname.
         
         curl https://store.example.com --resolve store.example.com:443:GATEWAY_IP_ADDRESS --cacert cacert.pem -v
         

Replace `GATEWAY_IP_ADDRESS` with the IP address of the Gateway from the previous step.

cacert.pem: the certificate file that you generated. You must save this file on the machine that you use to connect to the Gateway.

The output shows information from the demo app about the location where the app is running:
         
         {
           "cluster_name": "gke1",
           "host_header": "store.example.com",
           "metadata": "store-v1",
           "node_name": "gke-gke1-pool-2-bd121936-5pfc.c.gateway-demo-243723.internal",
           "pod_name": "store-v1-84b47c7f58-pmgmk",
           "pod_name_emoji": "💇🏼‍♀️",
           "project_id": "gateway-demo-243723",
           "timestamp": "2022-09-25T13:31:17",
           "zone": "us-central1-a"
         }
         

  4. Test the path match by going to the German version of the `store` service at `store.example.com/de`:
         
         curl https://store.example.com/de --resolve store.example.com:443:GATEWAY_IP_ADDRESS --cacert cacert.pem -v
         

The output confirms that the request was served by a `store-german` Pod:
         
         {
           "cluster_name": "gke1",
           "host_header": "store.example.com",
           "metadata": "Gutentag!",
           "node_name": "gke-gke1-pool-2-bd121936-n3xn.c.gateway-demo-243723.internal",
           "pod_name": "store-german-5cb6474c55-lq5pl",
           "pod_name_emoji": "🧞‍♀",
           "project_id": "gateway-demo-243723",
           "timestamp": "2022-09-25T13:35:37",
           "zone": "us-central1-a"
         }
         

  5. Send traffic to the canary version of the `store` Service using the `env: canary` HTTP header:
         
         curl -H "env: canary" https://store.example.com --resolve store.example.com:443:GATEWAY_IP_ADDRESS --cacert cacert.pem -v
         

The output confirms that the request was served by a `store-v2` Pod:
         
         {
           "cluster_name": "gke1",
           "host_header": "store.example.com",
           "metadata": "store-v2",
           "node_name": "gke-gke1-pool-2-bd121936-5pfc.c.gateway-demo-243723.internal",
           "pod_name": "store-v2-5788476cbd-s9thb",
           "pod_name_emoji": "👩🏿",
           "project_id": "gateway-demo-243723",
           "timestamp": "2022-09-25T13:38:26",
           "zone": "us-central1-a"
         }
         




### Deploy a global external Gateway

The following example shows you how to expose a store application with multiple certificates attached to the global external Gateway and grouped in a certificate map using Certificate Manager and an HTTPRoute.

#### Create a certificate map

Google recommends that you use [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) to manage certificates when you need 15 or more certificates per Gateway or you need to use wildcard certificates.

You can also secure your external Gateway using Kubernetes Secrets or Google-managed SSL certificates. For more information, see [Gateway security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security).

In this section, you create certificates using Certificate Manager to secure the applications running on the cluster.

  1. Enable the Certificate Manager API:
         
         gcloud services enable certificatemanager.googleapis.com
         

  2. Create a certificate map:
         
         gcloud beta certificate-manager maps create store-example-com-map
         

  3. Load your Google-managed certificate and keys into a Certificate:
         
         gcloud beta certificate-manager certificates create store-example-com-cert \
             --certificate-file="CERTIFICATE_FILE" \
             --private-key-file="PRIVATE_KEY_FILE"
         

Replace the following:

     * `CERTIFICATE_FILE`: the name of your certificate file. The file must have the `.pem` extension. For example, `cert.pem`.
     * `PRIVATE_KEY_FILE`: the name of your private key file.

For more information, see [Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).

  4. Create a `CertificateMapEntry` which assigns the certificate to the certificate map:
         
         gcloud beta certificate-manager maps entries create store-example-com-map-entry \
             --map=store-example-com-map \
             --hostname=store.example.com \
             --certificates=store-example-com-cert
         




To learn how to secure a Gateway using other sources for certificates, such as Kubernetes Secrets or SSL certificates, see [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).

#### Create a Gateway

A Gateway resource represents a data plane that routes traffic in Kubernetes. A Gateway can represent many different kinds of load balancing and routing depending on the GatewayClass it uses.

To learn more about the Gateway resource, see the [Gateway resource](https://gateway-api.sigs.k8s.io/api-types/gateway/) description or the [API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.Gateway).

In this section, you create a Gateway. Application teams can use the Gateway to expose their applications to the internet by deploying Routes independently and attaching them securely to the Gateway.

  1. Save the following manifest to a file named `gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
           annotations:
             networking.gke.io/certmap: store-example-com-map
         spec:
           # This GatewayClass uses a global external Application Load Balancer.
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
         
         

This manifest describes a Gateway with the following fields:

     * `gatewayClassName: gke-l7-global-external-managed`: specifies the GatewayClass for this Gateway. This gateway class uses a global external Application Load Balancer.
     * `protocol: HTTPS` and `port: 443`: specify that the Gateway exposes port 443 for HTTPS traffic. These fields enables TLS.
     * `networking.gke.io/certmap: store-example-com-map`: specifies the name of the certificate map in Certificate Manager.

There is no TLS section because TLS is configured with Certificate Manager using the annotation `networking.gke.io/certmap`.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f gateway.yaml
         

It might take a few minutes for GKE to deploy the resources.

  3. Verify that the Gateway has deployed successfully:
         
         kubectl describe gateway
         

The output is similar to the following:
         
         Name:         external-http
         Namespace:    default
         Labels:       <none>
         ...
         Spec:
           Gateway Class Name:  gke-l7-global-external-managed
           Listeners:
             Allowed Routes:
               Namespaces:
                 From:  Same
             Name:      https
             Port:      443
             Protocol:  HTTPS
             Tls:
               Certificate Refs:
                 Group:
                 Kind:   Secret
                 Name:   store-example-com
               Mode:     Terminate
          ...
         

This output shows that the Gateway deployed in your cluster has a load balancer and a public IP address. The Gateway has no Routes, which means it can't send traffic to backends. Without Routes, all traffic goes to a default backend, which returns an HTTP 404 response. In the next section, you deploy Routes, which instruct the Gateway to send traffic to backends.




#### Deploy the demo application

You can deploy your applications and routes independently from the deployment of Gateways.

For more information on how to deploy the demo applications, see Deploy the demo applications.

#### Create an HTTPRoute

You must create an HTTPRoute to do HTTP and HTTPS traffic matching and filtering.

#### Send Traffic to your application

After you have deployed your application and created HTTPRoutes, you can pass traffic to your application.

For more information on how to send traffic to your application, see Send traffic to your application.

### Deploy a regional external Gateway

The following example shows you how to expose a store application with multiple certificates attached to the regional external Gateway using self-managed certificates and an HTTPRoute.

#### Create a proxy subnet for your regional Gateway

You must configure a proxy-only subnet before you create a Gateway that uses a regional external Application Load Balancer. Each region of a VPC in which you use regional external Application Load Balancer must have an `external_managed_proxy` subnet. This subnet provides internal IP addresses to the load balancer proxies.

#### Create a certificate to secure your client traffic

You can use a certificate issued and validated by your certificate authority (CA) or create a self-signed certificate. For more information on how to create a certificate, see [Store a certificate in a Kubernetes Secret](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#store-certificate-secret).

To secure traffic between your clients and your regional Gateway, you can use the following methods:

  * Google-managed or self-managed Certificate Manager certificates
  * Self-managed regional SSL certificates
  * Kubernetes Secrets



CertificateMap or Google-managed SSL certificates aren't supported with regional Gateways.

For more information, see [Certificates and Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary)

#### Create a regional external HTTP(S) Gateway

  1. Create a regional static IP address for the external load balancer.
         
         gcloud compute addresses create IP_ADDRESS_NAME \
           --region=COMPUTE_REGION \
           --network-tier=STANDARD
         

Replace the following:

     * `IP_ADDRESS_NAME`: the name of the new static IP address.
     * `COMPUTE_REGION`: The Compute Engine region where your cluster is running.
  2. Create a regional external Application Load Balancer Gateway using a self-managed certificate as follows and save the manifest as `regional-gateway.yaml`:
         
         kind: Gateway
           apiVersion: gateway.networking.k8s.io/v1
           metadata:
             name: external-regional-http
           spec:
             # Name of an existing GatewayClass.
             gatewayClassName: gke-l7-regional-external-managed
             # Listen for HTTPS traffic on port 443
             listeners:
             - name: https
               protocol: HTTPS
               port: 443
               tls:
                 # Terminate the TLS session with the client at the Gateway.
                 mode: Terminate
                 # Certificates for the Gateway to use to create a new TLS session.
                 certificateRefs:
                 - name: store-example-com
             # The name of the static IP address of the external load balancer.
             # You can also use the `IPAddress` type to specify the actual IP address.
             addresses:
             - type: NamedAddress
               value: IP_ADDRESS_NAME
         

  3. Apply the `regional-gateway` manifest:
         
         kubectl apply -f regional-gateway.yaml
         

  4. Verify your configuration.
         
         kubectl get gateway
         

The output is similar to the following:
         
         NAME            CLASS                              ADDRESS         READY   AGE
         external-http   gke-l7-regional-external-managed   35.118.32.224   True    49s
         

To get more details, use a describe command:
         
         kubectl describe gateway
         

The output is similar to the following:
         
         Name:         external-regional-http
         Namespace:    default
         Labels:       <none>
         ...
         Spec:
           Gateway Class Name:  gke-l7-regional-external-managed
           Listeners:
             Allowed Routes:
               Namespaces:
                 From:  Same
             Name:      https
             Port:      443
             Protocol:  HTTPS
             Tls:
               Certificate Refs:
                 Group:
                 Kind:   Secret
                 Name:   store-example-com
               Mode:     Terminate
           ...
         




#### Deploy the demo application

You can deploy your applications and routes independently from the deployment of Gateways.

For more information on how to deploy the demo applications, see Deploy the demo applications.

#### Create an HTTPRoute

You must create an HTTPRoute to do HTTP and HTTPS traffic matching and filtering.

#### Send Traffic to your application

After you have deployed your application and created HTTPRoutes, you can pass traffic to your application.

For more information on how to send traffic to your application, see Send traffic to your application.

## Use shared Gateways

Gateway API uses separate resources, Gateways and Route resources, to deploy load balancers and routing rules. This differs from Ingress, which combines everything in one resource. By splitting responsibility among resources, Gateway enables the load balancer and its routing rules to be deployed separately and to be deployed by different users or teams. This enables Gateways to become shared Gateways that attach with many different Routes that can be fully owned and managed by independent teams, even across different namespaces.

### Deploy routes against a shared Gateway

This example builds on the `internal-http` Gateway deployed in Deploy an internal Gateway.

In this example, the site team deploys their application, Services, and an HTTPRoute to match traffic from the Gateway to those Services.

  1. Deploy the example application:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/gke-networking-recipes/main/gateway/gke-gateway-controller/app/site.yaml
         

  2. Save the following manifest to a file named `site-route-internal.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: site-internal
         spec:
           # Attach the HTTPRoute to the `internal-http` Gateway.
           parentRefs:
           - kind: Gateway
             name: internal-http
           # Route requests that have `site.example.com` in the Host header.
           hostnames:
           - "site.example.com"
           # Send all requests to the `site-v1` Service.
           rules:
           - backendRefs:
             - name: site-v1
               port: 8080
         

This manifest describes an HTTPRoute that matches all traffic for `site.example.com` and routes it to the `site-v1` Service.

  3. Apply the manifest to your cluster:
         
         kubectl apply -f site-route-internal.yaml
         

  4. Verify that the HTTPRoute is attached to the Gateway:
         
         kubectl describe httproute.gateway.networking.k8s.io site-internal
         

The output is similar to the following:
         
         Status:
           Parents:
             Conditions:
               Last Transition Time:  2023-01-09T15:05:43Z
               Message:
               Reason:                Accepted
               Status:                True
               Type:                  Accepted
               Last Transition Time:  2023-01-09T15:05:43Z
               Message:
               Reason:                ReconciliationSucceeded
               Status:                True
               Type:                  Reconciled
             Controller Name:         networking.gke.io/gateway
             Parent Ref:
               Group:  gateway.networking.k8s.io
               Kind:   Gateway
               Name:   internal-http
               ...
         

If the `Accepted` condition for the Gateway is `True`, the HTTPRoute has successfully bound to the Gateway. To learn more about the Status field, see route status.

  5. Verify that traffic to the Gateway is routed correctly:
         
         curl -H "host: site.example.com" GATEWAY_IP_ADDRESS
         curl -H "host: store.example.com" GATEWAY_IP_ADDRESS
         

Replace `GATEWAY_IP_ADDRESS` with the IP address of the internal Gateway.

You must use a virtual machine (VM) in the same VPC as the Gateway.

The output is similar to the following:
         
         {
           "cluster_name": "CLUSTER_NAME",
           "host_header": "site.example.com",
           "metadata": "site-v1",
           "pod_name": "site-v1-5d64fc4d7d-fz6f6",
           "pod_name_emoji": "👩🏼‍🍳",
           "project_id": "PROJECT_ID",
           "timestamp": "2022-11-02T19:07:01",
           "zone": "ZONE_NAME"
         }
         ...
         {
           "cluster_name": "CLUSTER_NAME",
           "host_header": "store.example.com",
           "metadata": "store-v1",
           "pod_name": "store-v1-6d8d58d78-vz8pn",
           "pod_name_emoji": "🧝🏻‍♂️",
           "project_id": "PROJECT_ID",
           "timestamp": "2022-11-02T19:07:01",
           "zone": "ZONE_NAME"
         }
         

This output indicates that requests with the `site.example.com` Host header reach the `site-v1` Service, while requests with the `store.example.com` Host header reach the `store-v1` Service.




## Configure network tier

You can specify the network tier for a regional external Application Load Balancer's listener address by using the `type` field within the `addresses[]` array in the Gateway definition. If you don't specify a network tier, the Gateway defaults to using a Standard Tier ephemeral IP address.

Use the following values for the `type` field:

  * `networking.gke.io/premium-ephemeral-ipv4-address`: assigns a Premium Tier IP address.
  * `networking.gke.io/standard-ephemeral-ipv4-address`: assigns a Standard Tier IP address.



To assign IP addresses from both network tiers, specify both types in the `addresses` field.

The following example shows you how to make Google Cloud assign a Premium Tier IP address to a Gateway. To provision a Standard Tier IP address, use `networking.gke.io/standard-ephemeral-ipv4-address`.

  1. Save the following sample manifest as `external-regional-http.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-regional-http
         spec:
           # Name of an existing GatewayClass.
           gatewayClassName: gke-l7-regional-external-managed
           # Listen for HTTPS traffic on port 443.
           listeners:
           - name: https
             protocol: HTTPS
             port: 443
             tls:
               # Terminate the TLS session with the client at the Gateway.
               mode: Terminate
               # Certificates for the Gateway to use to create a new TLS session.
               certificateRefs:
               - name: store-example-com
             addresses:
             # Request a Premium Tier ephemeral IPv4 address for the Gateway.
             - type: networking.gke.io/premium-ephemeral-ipv4-address
         

**Note:** to provision a Standard Tier IP address, use `networking.gke.io/standard-ephemeral-ipv4-address`.
  2. Apply the sample manifest:
         
         kubectl apply -f external-regional-http.yaml
         


**Note:** If you create a regional external Application Load Balancer Gateway that uses the `gke-l7-regional-external-managed` GatewayClass without specifying a network tier address, the Gateway defaults to using a Standard Tier ephemeral IP address. Modifying the Gateway manifest later to specify an explicit address type, such as `networking.gke.io/standard-ephemeral-ipv4-address` or `networking.gke.io/premium-ephemeral-ipv4-address`, results in an IP address change, which might disrupt services. To prevent service interruptions, define your address configuration when you create the Gateway.

## Configure the Gateway default backend

All of the `gke-l7-*` GatewayClasses return HTTP 404 to unmatched traffic. You can configure the default backend using an explicit default Route that sends unmatched traffic to a user-provided Service.

Gateways are configured to handle error codes like 404 (Not Found) and 500 (Server Error), even without explicit backend definitions. The default behavior may vary between Gateway implementations. For greater control over error handling, consider configuring custom backends.

The following HTTPRoute is an example of how to customize the default backend. If you apply an HTTPRoute similar to the following, it takes precedence over the implicit default backend:
    
    
    kind: HTTPRoute
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: custom-default-backend
    spec:
      parentRefs:
      - kind: Gateway
        name: my-internal-gateway
      # Omit the `hostnames` field to route all unmatched traffic from the
      # attached Gateway.
      rules:
      - backendRefs:
        - name: my-custom-default-backend-service
          port: 8080
    

This HTTPRoute matches all traffic from a particular Gateway. You can only have one such rule for each Gateway or else the rules conflict and precedence ordering applies.

You can use a default backend to prevent someone from creating a default route Backend that routes all Gateway traffic. An explicit HTTPRoute always takes precedence over new HTTPRoutes with conflicting routing rules.

## Configure a static IP address for a Gateway

Every Gateway has an IP address it uses to listen for traffic. If you don't specify an IP address on the Gateway, then the Gateway controller automatically provides an IP address. You can also create a static IP address so that the IP address exists independent of the Gateway lifecycle.

After a Gateway is deployed, its IP address shows in the status field:
    
    
    kind: Gateway
    ...
    status:
      addresses:
        - value: 10.15.32.3
    

Depending on the GatewayClass, the IP address is allocated from the following subnets: 

**GatewayClasses** | **Default IP Address Pool**  
---|---  
* gke-l7-rilb
* gke-l7-rilb-mc
| Regional private IP addresses from the primary node IPv4/IPv6 address range  
* gke-l7-regional-external-managed
* gke-l7-regional-external-managed-mc
| Regional public IP addresses from [Google's regional external IPv4/IPv6 ranges](https://docs.cloud.google.com/vpc/docs/ip-addresses)  
* gke-l7-global-external-managed
* gke-l7-global-external-managed-mc
* gke-l7-gxlb
* gke-l7-gxlb-mc
| Global public IP addresses from [Google's global external IPv4/IPv6 ranges](https://docs.cloud.google.com/vpc/docs/ip-addresses)  
  
The field `addresses.NamedAddress` lets you specify an IP address independently of the Gateway. You can create a static IP address resource prior to Gateway deployment and the resource is referenced by the `NamedAddress`. You can reuse the static IP address even if the Gateway is deleted.

### Use a named IP address

You can configure an IPv4 or IPv6 address by specifying a `NamedAddress`. You must provision a static IP address before you create a Gateway.

  1. Create a static IP address resource:
         
         gcloud compute addresses create IP_ADDRESS_NAME \
             --purpose=SHARED_LOADBALANCER_VIP \
             --region=COMPUTE_REGION \
             --subnet=SUBNET \
             --project=PROJECT_ID
         

Replace the following:

     * `IP_ADDRESS_NAME`: the name of the new static IP address
     * `COMPUTE_REGION`: for regional Gateways, the Compute Engine region where your cluster is running. This flag is not needed for global, external Gateways.
     * `SUBNET`: the subnet for the IP address. This flag is not needed for global, external Gateways.
     * `PROJECT_ID`: the project where your GKE cluster is running.
  2. Save the following manifest to a file named `named-ip-gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: internal-http
         spec:
           gatewayClassName: gke-l7-rilb
           listeners:
           - name: http
             protocol: HTTP
             port: 80
           addresses:
           - type: NamedAddress
             value: IP_ADDRESS_NAME
         

This manifest describes a Gateway that references the named IP address.

  3. Apply the manifest to your cluster:
         
         kubectl apply -f named-ip-gateway.yaml
         

  4. Verify your Gateway IP address:
         
         kubectl describe gateway internal-http
         

The output is similar to the following:
         
         Name:         internal-http
         Namespace:    default
         Labels:       <none>
         ...
         Spec:
           Addresses:
             Type:              NamedAddress
             Value:             IP_ADDRESS_NAME
           Gateway Class Name:  gke-l7-rilb
           Listeners:
             Allowed Routes:
               Namespaces:
                 From:  Same
             Name:      http
             Port:      80
             Protocol:  HTTP
         Status:
           Addresses:
             Type:   IPAddress
             Value:  10.15.32.103
         




## Configure HTTP-to-HTTPS redirects

Cloud Load Balancing offers HTTP to HTTPS redirect functionality. An external Application Load Balancer redirects unencrypted HTTP requests to an HTTPS load balancer that uses the same IP address. When you create a Gateway with HTTP-to-HTTPS redirects enabled, both of these load balancers are created automatically. Requests to the external IP address of the Gateway on port 80 are automatically redirected to the same external IP address on port 443.

By default, HTTP to HTTPS redirects are not defined on the Gateway.

To redirect HTTP traffic to HTTPS, configure a Gateway to handle both HTTP and HTTPS traffic. If you disable either HTTP or HTTPS, the Gateway does not redirect traffic.

The following example shows you how you can use HTTP-to-HTTPS redirect as a means to help ensure that traffic from your clients going to your web applications is always being redirected to a secure page.

HTTP-to-HTTPS redirects are not supported with the `gke-l7-gxlb` and `gke-l7-gxlb-mc` GatewayClasses. To learn more about the different features supported with each GatewayClass, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

Note that the `hostnames` section in an HTTPRoute is optional. You can create a catch-all redirect for all hostnames on a specific HTTP port by omitting the `hostnames` section. Additionally, you can use a wildcard redirect, for example:
    
    
    ...
    hostnames:
    - "*.example.com" # Matches all subdomains of example.com
    ...
    

### Redirect HTTP traffic from an infrastructure namespace

In some cases, there isn't a clear distinction between the infrastructure or platform admin team and the application teams and preventing misuse of the Gateway can become a challenge.

The following example further restricts the use of the HTTP listener to prevent unintentional use of non-secure protocol from the application teams. This example configures the Gateway to allow an HTTPRoute to use the HTTP listener only if the route is in a namespace that has the `otherInfra: httpToHttps` label. However, the Gateway allows HTTPRoutes in any namespace to use the HTTPS listener. You can restrict the http-redirect namespace using Kubernetes RBAC so that application teams cannot create an HTTPRoute in this namespace by mistake.

  1. Create the namespace of a Gateway. Save the manifest as `gateway-namespace.yaml`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: gateway-infra
         

  2. Apply the manifest:
         
         kubectl apply -f gateway-namespace.yaml
         

  3. Create the namespace of a Gateway and save the manifest as `redirect-namespace.yaml`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: http-redirect
           labels:
             otherInfra: httpToHttps
         

This `http-redirect` namespace has the `otherInfra: httpToHttps` label.

  4. Apply the manifest:
         
         kubectl apply -f redirect-namespace.yaml
         

  5. To restrict the http listener usage, create a Gateway using the following manifest. Save the manifest as `external-gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: external-http
           namespace: gateway-infra
         spec:
           # Name of an existing GatewayClass.
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: http
             protocol: HTTP
             port: 80
             #  Allow only HTTPRoutes from namespaces that have the
             # `otherInfra: httpToHttps` label to use this listener.
             allowedRoutes:
               kinds:
               - kind: HTTPRoute
               namespaces:
                 from: Selector
                 selector:
                   matchLabels:
                     otherInfra: httpToHttps
           - name: https
             protocol: HTTPS
             port: 443
             # Allow HTTPRoutes from any namespace to use this listener.
             allowedRoutes:
               kinds:
               - kind: HTTPRoute
               namespaces:
                 from: All
             tls:
               mode: Terminate
               options:
                 networking.gke.io/pre-shared-certs: store-example-com
         

     * The `namespace` field specifies that the Gateway is created in the `gateway-infra` namespace.

     * The `namespaces` field in the `allowedRoutes` section restricts the http listener to the namespace matching the label `otherInfra: httpToHttps`.

  6. Apply the manifest:
         
         kubectl apply -f external-gateway.yaml
         

  7. To force the HTTPS redirect, create a default HTTPRoute using the following manifest. Save the manifest as `http-redirect.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: redirect
           # Create the HTTPRoute in the `http-redirect` namespace.
           namespace: http-redirect
         spec:
           # Attach the HTTPRoute to the `http` listener in the `external-http`
           # Gateway.
           parentRefs:
           - namespace: gateway-infra
             name: external-http
             sectionName: http
           rules:
           # Respond to the request with an HTTPS redirection.
           - filters:
             - type: RequestRedirect
               requestRedirect:
                 scheme: https
         

     * The `sectionName` field instructs the Gateway to match only on the http listener. The `RequestRedirect` filter forces the redirection to the https listener.
  8. Apply the manifest:
         
         kubectl apply -f http-redirect.yaml
         

  9. Create a Service for an application using the following manifest. Save the manifest as `service-deployment.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: store-v1
         spec:
           selector:
             app: store
             version: v1
           ports:
           - port: 8080
             targetPort: 8080
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: store-v1
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: store
               version: v1
           template:
             metadata:
               labels:
                 app: store
                 version: v1
             spec:
               containers:
               - name: whereami
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                 - containerPort: 8080
                 env:
                 - name: METADATA
                   value: "store-v1"
         

  10. Apply the manifest:
         
         kubectl apply -f service-deployment.yaml
         

  11. Create an HTTPRoute for an application that only allows HTTPS using the following manifest. Save the manifest as `http-route.yaml`:
         
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-external
           labels:
             gateway: external-http
         spec:
           # Attach the HTTPRoute to the HTTPS listener in the `external-http`
           # Gateway.
           parentRefs:
           - name: external-http
             namespace: gateway-infra
             sectionName: https
           # Match requests that have the `store.example.com` Host header.
           hostnames:
           - "store.example.com"
           # Route requests to the `store-v1` Service.
           rules:
           - backendRefs:
             - name: store-v1
               port: 8080
         

  12. Apply the manifest:
         
         kubectl apply -f http-route.yaml
         




## Configure path redirects and URL rewrites

[Path redirects](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/#redirects) involve redirecting an incoming request from one URL path to another. Path redirects let you change the structure of the URL when you need to handle outdated or deprecated URLs.

[URL rewrites](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/#rewrites) help modify the incoming URL before processing it on the server. It lets you change the structure or format of the URL without actually changing the underlying content or file structure. URL rewriting is beneficial for creating user-friendly and SEO-friendly URLs that are easy to remember and understand. By default, path redirects and URL rewrites are not configured, you need to explicitly configure those redirects or rewrites using a filter in your HTTPRoute.

GKE Gateway supports path redirects and URL rewrites. For more information, see [HTTP path redirects and rewrites](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/).

### Configure path redirects

You can configure path redirects to either replace the entire path or only a prefix in the URL.

#### Replace entire path

  1. To replace an entire path, configure a filter in an HTTPRoute that replaces any URL that contains the prefix `/any-path` in the URL path by the strict value `/new-path`.

  2. Create an HTTPRoute manifest as follows and name it as `store.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
           kind: HTTPRoute
           metadata:
             name: store
           spec:
             parentRefs:
             - kind: Gateway
               name: external-http
             hostnames:
             - store.example.com
             rules:
             - matches:
               - path:
                   # Match requests by a prefix, like `/any-path` and `/any-path/home`.
                   type: PathPrefix
                   value: /any-path
               filters:
               - type: RequestRedirect
                 requestRedirect:
                   path:
                     # Replace the full path with `/new-path`. For example, both
                     # `/any-path/home` and `/any-path` become `/new-path`.
                     type: ReplaceFullPath
                     replaceFullPath: /new-path
                   statusCode: 302
         

For example, this manifest sets a routing rule for an HTTPRoute as follows: Any route to the URL `https://store.example.com/any-path/...` should be redirected to a new location, `https://store.example.com/new-path/` (strict).

  3. Apply the manifest:
         
         kubectl apply -f store.yaml
         




This routing rule follows a strict redirection rule, which means that the browser does not attempt to cache the redirect, instead, redirects to the latest version.

#### Replace a prefix only

  1. To replace a prefix only, configure a filter in an HTTPRoute that replaces any URL that contains the prefix `/any-prefix` in the URL path by the strict value `/new-prefix`.

  2. Create an HTTPRoute manifest as follows and name it as `store.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: store
         spec:
           parentRefs:
             - kind: Gateway
               name: external-http
           hostnames:
           - store.example.com
           rules:
           - matches:
               - path:
                   # Match requests by prefix, like `/any-prefix` and
                   # `/any-prefix/home`.
                   type: PathPrefix
                   value: /any-prefix
             filters:
             - type: RequestRedirect
               requestRedirect:
                 path:
                   # Replace the matched prefix with `/new-prefix`. For example,
                   # `/any-prefix` becomes `/new-prefix` and `/any-prefix/home`
                   # becomes `/new-prefix/home`.
                   type: ReplacePrefixMatch
                   replacePrefixMatch: /new-prefix
                 statusCode: 302
         

For example, this manifest sets a routing rule for an HTTPRoute as follows: Any route to the URL `https://store.example.com/any-path/v1/...` should be redirected to a new location, `https://store.example.com/new-path/v1/...` (only).

  3. Apply the manifest:
         
         kubectl apply -f store.yaml
         




This routing rule follows the only redirection rule, which helps ensure that the browser always redirects you to the same intended page.

### Configure URL rewrites

Set URL rewrites to change the way a URL appears to users. You can use URL rewrites to make URLs more user-friendly, to improve SEO, or to redirect users to a new page.

#### Rewrite the entire hostname

To rewrite the entire hostname:

  1. Configure a filter in an HTTPRoute that instructs the Gateway to replace the `Host` information in the request header from `www.example.com` to `store.example.com` before forwarding the request to the backend service.

  2. Create an HTTPRoute manifest as follows and name it as `www.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
           kind: HTTPRoute
           metadata:
             name: www
           spec:
             parentRefs:
               - kind: Gateway
                 name: external-http
             hostnames:
             - www.example.com
             rules:
             - filters:
               - type: URLRewrite
                 # Replace the hostname in the URL with `store.example.com`.
                 urlRewrite:
                   hostname: store.example.com
               backendRefs:
               - name: store-v1
                 port: 8080
         

For example, with the above configuration, any request to `https://www.example.com` is forwarded to the backend service with the `Host: store.example.com` header, instead of `Host: www.example.com`.

  3. Apply the manifest:
         
         kubectl apply -f www.yaml
         




#### Rewrite using path modifiers

You can combine rewrites with path modifiers to provide advanced URL and path modifications before relaying the request to the backend service.

To rewrite using path modifiers:

  1. Configure a filter in an HTTPRoute that instructs the Gateway to replace the 'Host' information in the request header from www.example.com`to store.example.com` and replace the value `/store` by `/` before forwarding the request to the backend service.

  2. Create an HTTPRoute manifest as follows and name it as `www.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
           kind: HTTPRoute
           metadata:
             name: www
           spec:
             parentRefs:
               - kind: Gateway
                 name: external-http
             hostnames:
             - www.example.com
             rules:
             - matches:
               - path:
                   type: PathPrefix
                   value: /store
               filters:
               - type: URLRewrite
                 # For URLs that have `/store` in the path, replace the hostname with
                 # store.example.com and replace the `/store` prefix with `/de`.
                 urlRewrite:
                   hostname: store.example.com
                   path:
                     type: ReplacePrefixMatch
                     replacePrefixMatch: /de
               backendRefs:
               - name: store-german
                 port: 8080
         

For example, with the above configuration, any request to `https://www.example.com/store/...` is forwarded to the backend service with `Host: store.example.com` in the request header (instead of `Host: www.example.com`) and the `/store` is rewritten to `/de`.

  3. Apply the manifest:
         
         kubectl apply -f www.yaml
         




### Verify your configuration

To verify that the filter was applied after creating your HTTPRoute with URL rewrite or path redirects filters, do the following:
    
    
    kubectl get httproute www -o yaml
    

The output is similar to the following:
    
    
      apiVersion: gateway.networking.k8s.io/v1
      kind: HTTPRoute
      metadata:
        annotations:
          kubectl.kubernetes.io/last-applied-configuration: |
            {"apiVersion":"gateway.networking.k8s.io/v1","kind":"HTTPRoute","metadata":{"annotations":{},"name":"www","namespace":"default"},"spec":{"hostnames":["www.example.com"],"parentRefs":[{"kind":"Gateway","name":"external-http"}],"rules":[{"backendRefs":[{"name":"store-german","port":8080}],"filters":[{"type":"URLRewrite","urlRewrite":{"hostname":"store.example.com","path":{"replacePrefixMatch":"/de","type":"ReplacePrefixMatch"}}}],"matches":[{"path":{"type":"PathPrefix","value":"/store"}}]}]}}
        creationTimestamp: "2023-06-22T01:00:42Z"
        generation: 3
        name: www
        namespace: default
        resourceVersion: "51268631"
        uid: e516493e-806d-44d6-ae0d-1c9ff25682cf
      spec:
        hostnames:
        - www.example.com
        parentRefs:
        - group: gateway.networking.k8s.io
          kind: Gateway
          name: external-http
        rules:
        - backendRefs:
          - group: ""
            kind: Service
            name: store-german
            port: 8080
            weight: 1
          filters:
          - type: URLRewrite
            urlRewrite:
              hostname: store.example.com
              path:
                replacePrefixMatch: /de
                type: ReplacePrefixMatch
          matches:
          - path:
              type: PathPrefix
              value: /store
      status:
        parents:
        - conditions:
          - lastTransitionTime: "2023-06-22T01:11:26Z"
            message: ""
            observedGeneration: 2
            reason: Accepted
            status: "True"
            type: Accepted
          - lastTransitionTime: "2023-06-22T01:11:26Z"
            message: ""
            observedGeneration: 2
            reason: ReconciliationSucceeded
            status: "True"
            type: Reconciled
          controllerName: networking.gke.io/gateway
          parentRef:
            group: gateway.networking.k8s.io
            kind: Gateway
            name: external-http
    
    

To get more details, use the describe command:
    
    
    kubectl describe httproute
    

## Configure Cross-Origin Resource Sharing (CORS)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cross-Origin Resource Sharing (CORS) is a security mechanism that helps web applications running at one origin (domain) securely access resources hosted on a different origin.

You can configure CORS policies directly within HTTPRoute resources using the `CORS` filter. This approach allows the load balancer to inject the appropriate CORS response headers and handle CORS preflight (`OPTIONS`) requests, offloading this responsibility from your backend services.

### Configure a CORS policy

The following example shows an HTTPRoute configured with a `CORS` filter that allows cross-origin requests from `https://www.example.com` for specific methods and headers:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: route-with-cors
      namespace: default
    spec:
      parentRefs:
      - name: my-gateway
      rules:
      - matches:
        - path:
            type: PathPrefix
            value: /api
        backendRefs:
        - name: my-backend
          port: 8080
        filters:
        - type: CORS
          cors:
            allowOrigins:
            - "https://www.example.com"
            allowMethods:
            - GET
            - POST
            - DELETE
            allowHeaders:
            - "x-request-header-1"
            - "x-request-header-2"
            exposeHeaders:
            - "x-response-header-a"
            - "x-response-header-b"
            allowCredentials: true
            maxAge: 3600
    

The `cors` configuration block supports the following fields:

  * **`allowOrigins`** : a list of allowed origins. The `http` and `https` protocols are supported. You can specify these origins in any of the following formats: 
    * Explicit origins (for example, `https://www.example.com`).
    * A single catch-all wildcard (`*`) to allow all origins. If this wildcard is used, no other origins can be specified. For security reasons, we strongly discourage combining the catch-all wildcard with the `allowCredentials` setting (for more information, see the following field definition).
    * Wildcard patterns (for example, `https://*.domain.com`). The `*` wildcard must appear immediately after the scheme (`http://` or `https://`) and must be followed by a dot (for example, `http://*.domain.com`), a port (for example, `https://*:4433`), or be the last character (for example, `http://*`).
  * **`allowMethods`** : the HTTP methods permitted for CORS requests. Supports the wildcard (`*`) to allow all methods. If the wildcard is used, no other methods can be specified.
  * **`allowHeaders`** : the HTTP headers that clients are allowed to send. Supports the wildcard (`*`) to allow all headers. If the wildcard is used, no other headers can be specified.
  * **`exposeHeaders`** : the HTTP headers that are safe to expose to the client script. Supports the wildcard (`*`) to expose all headers.
  * **`allowCredentials`** : controls whether the browser can share the server response for requests sent in credentialed mode, such as requests that contain cookies or HTTP authentication. The default is `false`. When you configure this setting, consider the following security aspects: 
    * If you specify the `*` wildcard as the value for any of `allowMethods`, `allowHeaders`, or `exposeHeaders` fields, the browser blocks a response to a credentialed mode request. This block occurs even if the value of the `allowCredentials` field is set to `true` for security reasons.
    * When `allowOrigins` contains the `*` wildcard, the GKE Gateway controller does not literally copy the `*` wildcard from the `allowOrigins` field to response headers. As a result, the browser will _not_ block such a response to a credentialed mode request, allowing any potentially malicious site to access user data. For this reason, we strongly discourage a configuration with the following settings: `allowCredentials: true` and `allowOrigins` with the wildcard `*`.
  * **`maxAge`** : specifies how long (in seconds) the browser can cache the preflight response. The default is `5` seconds. The value must be `1` or greater.



### Limitations

  * **Single-cluster gateways only** : CORS is not supported for multi-cluster gateways.
  * **Incompatibility with`RequestRedirect`**: you cannot use a `CORS` filter and a `RequestRedirect` filter in the same route rule.
  * **Regular expression limits** : the GKE Gateway controller internally represents wildcard patterns in the value of the `allowOrigins` field as regular expressions. There are [limits](https://docs.cloud.google.com/load-balancing/docs/quotas#url_maps) on the usage of regular expressions, which affect GatewayClasses as follows: 
    * For the `gke-l7-global-external-managed` GatewayClass, you can use only a single regular expression per Gateway listener (shared with other features). This limitation is subject to double counting rules, which means combining a wildcard pattern with a `PathPrefix` match is unsupported.
    * For `gke-l7-regional-external-managed` and `gke-l7-rilb` GatewayClasses, you can use up to five regular expressions per hostname (shared with other features).
    * The catch-all wildcard (`*`) does not count towards these limits.
    * A single wildcard pattern in a CORS filter can count multiple times towards the regular expression limit. The GKE Gateway controller multiplies a CORS filter in an HTTPRoute rule by the number of matches in that rule. Additionally, a match of type `PathPrefix` counts twice unless the path is `/`.



For more information about the standard CORS behavior in Gateway API, see the upstream [CORS User Guide](https://gateway-api.sigs.k8s.io/guides/user-guides/http-cors/).

## Configure custom request and response headers

Custom request and response headers let you specify additional headers to HTTP(S) requests and responses. Depending on the information detected by the load balancer, these headers can include the following information:

  * Latency to the client
  * Geographic location of the client's IP address
  * Parameters of the TLS connection



By default, there are no custom headers added to the request sent/received to/from your backend services, you need to explicitly configure custom headers using a filter in your HTTPRoute.

You can configure custom headers by adding a filter section in your HTTPRoute's rules as follows:

### Configure custom request headers

Create a HTTPRoute manifest with a RequestHeaderModifier filter and save it as `http-route-request.yaml:`
    
    
      apiVersion: gateway.networking.k8s.io/v1
      kind: HTTPRoute
      metadata:
        name: store
      spec:
        <...>
        rules:
            filters:
              - type: RequestHeaderModifier
                requestHeaderModifier:
                  <...>
    

Apply the manifest:
    
    
      kubectl apply -f http-route-request.yaml
    

### Configure custom response headers

Create a HTTPRoute manifest with a ResponseHeaderModifier filter and save it as `http-route-response.yaml:`
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: store
    spec:
      <...>
      rules:
          filters:
            - type: ResponseHeaderModifier
              responseHeaderModifier:
                <...>
    

Apply the manifest:
    
    
      kubectl apply -f http-route-response.yaml
    

**Note:** GKE Gateway controller implements custom headers in the URL map and not in the backend service.

You can add, set, and remove headers as described in the [Gateway API implementation](https://gateway-api.sigs.k8s.io/guides/http-header-modifier/). You can configure your HTTPRoute with a custom header using [Google Cloud supported variables](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global#variables).

**Example 1:**

To configure an HTTPRoute that adds client location information to the HTTP request before sending it to the backend service, create a HTTPRoute manifest and name it as `external-http-request.yaml`:
    
    
      apiVersion: gateway.networking.k8s.io/v1
      kind: HTTPRoute
      metadata:
        name: store
      spec:
        parentRefs:
          - kind: Gateway
            name: external-http
        hostnames:
        - store.example.com
        rules:
          - matches:
            - path:
                type: PathPrefix
                value: /fr
            filters:
              # Add custom headers to requests that have `/fr` in the path.
              - type: RequestHeaderModifier
                requestHeaderModifier:
                  add:
                    - name: X-Client-Geo-Location
                      value: "{client_region},{client_city}"
            backendRefs:
              - name: store-french
                port: 8080
    

For example, for clients located in Strasbourg, France, the Gateway adds a header as `X-Client-Geo-Location:FR,Strasbourg`.

**Example 2:**

To configure an HTTPRoute that adds a custom response header to support HTTP Strict Transport Security, create a HTTPRoute manifest and name it as `external-http-response.yaml`:
    
    
      apiVersion: gateway.networking.k8s.io/v1
      kind: HTTPRoute
      metadata:
        name: store
      spec:
        parentRefs:
          - kind: Gateway
            name: external-http
        hostnames:
        - store.example.com
        rules:
          - matches:
            - path:
                type: PathPrefix
                value: /de
            filters:
              # Add custom headers to responses to requests that have `/de` in the
              # path.
              - type: ResponseHeaderModifier
                responseHeaderModifier:
                  add:
                    - name: Strict-Transport-Security
                      value: max-age=63072000
            backendRefs:
              - name: store-german
                port: 8080
    

### Verify your configuration

  1. To verify your configuration after configuring custom request and response headers, do the following:
         
         kubectl get httproute
         

The output is similar to the following:
         
         NAME    HOSTNAMES               AGE
           store   ["store.example.com"]   4d23h
         

  2. To get more details, use the describe command:
         
         kubectl describe httproute
         

The output is similar to the following:
         
         Name:         store
           Namespace:    default
           Labels:       <none>
           Annotations:  <none>
           API Version:  gateway.networking.k8s.io/v1
           Kind:         HTTPRoute
           Metadata:
             Creation Timestamp:  2023-05-27T00:51:01Z
             Generation:          5
             Resource Version:    25418887
             UID:                 2e07a1b8-420b-41b4-acd1-cecbfcd39f42
           Spec:
             Hostnames:
               store.example.com
             Parent Refs:
               Group:  gateway.networking.k8s.io
               Kind:   Gateway
               Name:   external-http
             Rules:
               Backend Refs:
                 Group:
                 Kind:    Service
                 Name:    store-v1
                 Port:    8080
                 Weight:  1
               Matches:
                 Path:
                   Type:   PathPrefix
                   Value:  /
               Backend Refs:
                 Group:
                 Kind:    Service
                 Name:    store-v2
                 Port:    8080
                 Weight:  1
               Matches:
                 Headers:
                   Name:   env
                   Type:   Exact
                   Value:  canary
                 Path:
                   Type:   PathPrefix
                   Value:  /
               Backend Refs:
                 Group:
                 Kind:    Service
                 Name:    store-german
                 Port:    8080
                 Weight:  1
               Filters:
                 Request Header Modifier:
                   Add:
                     Name:   X-Client-Geo-Location
                     Value:  {client_region},{client_city}
                 Type:       RequestHeaderModifier
               Matches:
                 Path:
                   Type:   PathPrefix
                   Value:  /de
           Status:
             <...>
         




## Configure regular expression matching

GKE Gateway supports regular expression matching for HTTPRoute paths, query parameters, and headers. You can use regular expressions to define flexible routing rules.

Regular expression matching is supported on the following Envoy-based GatewayClasses:

  * `gke-l7-regional-external-managed`
  * `gke-l7-regional-external-managed-mc`
  * `gke-l7-rilb`
  * `gke-l7-rilb-mc`
  * `gke-l7-cross-regional-internal-managed-mc`



### Limitations

  * **RE2 syntax** : only [RE2 syntax](https://github.com/google/re2/wiki/Syntax) is supported. RE2 does not support lookahead, lookbehind, or backreferences.
  * **Quotas and limits** : 
    * **Maximum regular expression matches** : you can configure up to five regular expression matches per path matcher (HTTPRoute).
    * **Maximum length** : the maximum length of a regular expression is 250 characters.
  * **Performance impact** : regular expression matching is computationally expensive. Using regular expression matchers can increase request latency: 
    * **One regular expression matcher** : latency increase of about 100 microseconds per request.
    * **Five regular expression matchers** : latency increase of about 200 microseconds per request.



### Configure path regular expression matching

To configure path matching by using a regular expression, in the `path` match rule, set the value of the `type` field to `RegularExpression`.

The following example routes requests, where the path matches the `/videos/hd.*` regular expression (for example, `/videos/hd-123` or `/videos/hd-promo.mp4`), to the `store-videos-hd` service:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: store-path-regex
    spec:
      parentRefs:
      - kind: Gateway
        name: internal-http
      hostnames:
      - "store.example.com"
      rules:
      - matches:
        - path:
            type: RegularExpression
            value: /videos/hd.*
        backendRefs:
        - name: store-videos-hd
          port: 8080
    

### Configure query parameter regular expression matching

To match query parameters by using a regular expression, in the `queryParams` match rule, set the value of the `type` field to `RegularExpression`.

The following example routes requests, where the `param1` query parameter matches the `.*param_value.*-hd` regular expression, to the `android-hd` service:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: store-query-regex
    spec:
      parentRefs:
      - kind: Gateway
        name: internal-http
      hostnames:
      - "store.example.com"
      rules:
      - matches:
        - queryParams:
          - name: param1
            type: RegularExpression
            value: .*param_value.*-hd
        backendRefs:
        - name: android-hd
          port: 8080
    

### Configure header regular expression matching

To match HTTP headers by using a regular expression, in the `headers` match rule, set the value of the `type` field to `RegularExpression`.

The following example routes requests, where the `User-Agent` header matches the `.*Android.*-hd` regular expression, to the `android-hd` service:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: store-header-regex
    spec:
      parentRefs:
      - kind: Gateway
        name: internal-http
      hostnames:
      - "store.example.com"
      rules:
      - matches:
        - headers:
          - name: User-Agent
            type: RegularExpression
            value: .*Android.*-hd
        backendRefs:
        - name: android-hd
          port: 8080
    

## Configure frontend mTLS

To enable client certificate authentication, Google Application Load Balancer provides frontend mTLS. For GKE Gateways, frontend mTLS lets you configure and apply client certificate validation to all supported GatewayClass resources, whether global or regional. For more information, see [Configure frontend mTLS for a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-frontend-mtls).

## Configure backend TLS

Backend authenticated TLS is a security feature that enables the GKE Gateway load balancer to verify the identity of the backends it connects to. For GKE Gateways, this functionality lets you configure and apply backend certificate validation to supported GatewayClasses, such as global or regional external managed load balancers and regional internal load balancers.

For more information, see [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-tls).

To require the Gateway to also authenticate its own identity to your backends (mutual TLS), you should use a client certificate on the Gateway resource. For instructions, see [Configure backend mutual TLS (mTLS) for a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-mtls).

## Route status

HTTPRoute resources emit conditions and events to help users understand if a HTTPRoute has successfully bound with one or more Gateways or if it was rejected.

### HTTPRoute conditions

HTTPRoute conditions indicate the status of the Route and the Gateways it is bound to. Because a Route can be bound to multiple Gateways, this is a list of Gateways and the individual conditions between the Route and each Gateway.

  * `Accepted=True` indicates that the HTTPRoute is successfully bound to a Gateway.
  * `Accepted=False` indicates that the HTTPRoute has been rejected from binding with this Gateway.



If there are no Gateways listed under the `Gateway bindings` heading, then your HTTPRoute labels and Gateway label selectors might not match. This can occur if your Route is not being selected by any Gateways.

### HTTPRoute events

HTTPRoute events provide details about the status of the HTTPRoute. Events are grouped by the following reasons:

  * `ADD` events are triggered by a resource being added.
  * `UPDATE` events are triggered by a resource being updated.
  * `SYNC` events are triggered by periodic reconciliation.



## Route merging, precedence, and validation

### Route precedence

Gateway API defines strict [precedence rules](https://gateway-api.sigs.k8s.io/reference/spec/#httproute) for how traffic is matched by Routes that have overlapping routing rules. The precedence between two overlapping HTTPRoutes is as follows:

  1. **Hostname merge** : The longest/most specific hostname match.
  2. **Path merge** : The longest/most specific path match.
  3. **Header merge** : The largest number of HTTP headers that match.
  4. **Conflict** : If the previous three rules don't establish precedence, then precedence goes to the HTTPRoute resource with the oldest timestamp.



### Route merging

For `gke-l7` GatewayClasses, all HTTPRoutes for a given Gateway are merged into the same [URL map resource](https://docs.cloud.google.com/load-balancing/docs/url-map). How the HTTPRoutes are merged together depends on the type of overlap between HTTPRoutes. The HTTPRoute from the earlier example can be split into three separate HTTPRoutes to illustrate route merging and precedence:

  1. Route merge: All three HTTPRoutes attach with the same `internal-http` Gateway, so they are merged together.
  2. Hostname merge: All three Routes match for `store.example.com`, so their hostname rules are merged.
  3. Path merge: store-german-route has a more specific path `/de`, so this is not merged further. store-v1-route and store-v2-route both match on the same `/*` path as well, so they are merged on the path.
  4. Header merge: store-v2-route has a more specific set of HTTP header matches than store-v1-route, so they are not merged further.
  5. Conflict: Because the Routes are able to be merged on hostname, path, and headers, there are no conflicts, and all of the routing rules are applied to traffic.



The single HTTPRoute used in the earlier example are equivalent to these three separate routes:
    
    
    kind: HTTPRoute
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: store-v1-route
    spec:
      parentRefs:
      - kind: Gateway
        name: internal-http
      hostnames:
      - "store.example.com"
      rules:
      - backendRefs:
        - kind: Service
          name: store-v1
          port: 8080
    ---
    kind: HTTPRoute
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: store-v2-route
    spec:
      parentRefs:
      - kind: Gateway
        name: internal-http
      hostnames:
      - "store.example.com"
      rules:
      - matches:
        - headers:
          - type: Exact
            name: env
            value: canary
        backendRefs:
        - kind: Service
          name: store-v2
          port: 8080
    ---
    kind: HTTPRoute
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: store-german-route
    spec:
      parentRefs:
      - kind: Gateway
        name: internal-http
      hostnames:
      - "store.example.com"
      rules:
      - matches:
        - path:
            type: PathPrefix
            value: /de
        backendRefs:
        - kind: Service
          name: store-german
          port: 8080
    

## Kubernetes Gateways and Istio Gateways

Note that the Kubernetes Gateway API and the Istio API both have a resource named Gateway. While they perform similar functions, they are not the same resource. If you are using Istio and Gateway API in the same Kubernetes cluster, these names overlap when using kubectl on the command line. `kubectl get gateway` might return the Kubernetes Gateway resources and not the Istio Gateway resources or vice versa.
    
    
    $ kubectl api-resources
    NAME       SHORTNAMES   APIGROUP                       NAMESPACED   KIND
    gateways   gw           networking.istio.io/v1beta1    true         Gateway
    gateways   gtw          networking.k8s.io/v1beta1      true         Gateway
    

If you are using Istio and upgrade to GKE 1.20 and later it is recommended to start using the Gateway resource shortname or specify the API group. The shortname for a Kubernetes Gateway is `gtw` and the shortname for an Istio Gateway is `gw`. The following commands return the Kubernetes Gateway and Istio Gateway resources respectively.
    
    
    # Kubernetes Gateway
    $ kubectl get gtw
    NAME                        CLASS
    multi-cluster-gateway       gke-l7-global-external-managed-mc
    
    $ kubectl get gateway.networking.x-k8s.io
    NAME                        CLASS
    multi-cluster-gateway       gke-l7-global-external-managed-mc
    
    # Istio Gateway
    $ kubectl get gw
    NAME               AGE
    bookinfo-gateway   64m
    
    $ kubectl get gateway.networking.istio.io
    NAME               AGE
    bookinfo-gateway   64m
    

## Troubleshooting

### Proxy-only subnet missing in the region

**Symptom:**

The following issue might occur when you create a regional Gateway (internal or external):
    
    
    generic::invalid_argument: error ensuring load balancer: Insert: Invalid value for field 'resource.target': 'regions/[REGION_NAME]/targetHttpProxies/gkegw-x5vt-default-internal-http-[ID]'. A reserved managed proxy subnetwork with purpose REGIONAL_MANAGED_PROXY is required.
    

**Reason:**

This error message indicates that no proxy-only subnet exists in the region for your Gateway.

**Workaround:**

To resolve this issue, configure a proxy-only subnet.

### Proxy-only subnet already exists in the region with the wrong purpose

**Symptom:**

The following issue might occur when you create a proxy-only subnet for your regional Gateway (internal or external):
    
    
    ERROR: (gcloud.compute.networks.subnets.create) Could not fetch resource:
     - The resource 'projects/[PROJECT_NAME]/regions/[REGION_NAME]/subnetworks/[PROXY_ONLY_SUBNET_NAME]' already exists
    

**Reason:**

This error message indicates that you attempted to create a regional proxy-only subnet in a region that already has a proxy-only subnet.

**Workaround:**

To resolve this issue, use the following steps:

  1. Check that a proxy-only subnet already exists in the region and verify that it has the correct purpose:

     1. List your subnets to find which one is the proxy-only subnet in the region:
            
            gcloud compute networks subnets list --regions=COMPUTE_REGION
            

Replace `COMPUTE_REGION` with the Compute Engine region where you want to create your regional Gateway.

     2. Describe your proxy-only subnet in the region to find its purpose:
            
            gcloud compute networks subnets describe PROXY_ONLY_SUBNET \
                --region COMPUTE_REGION | grep -E 'name|purpose'
            

Replace `PROXY_ONLY_SUBNET` with the proxy-only subnet.

GKE Gateway only supports `REGIONAL_MANAGED_PROXY` proxy-only subnets for regional Gateways (internal or regional).

  2. If the existing proxy-only subnet in the region was created with an `INTERNAL_HTTPS_LOAD_BALANCER` purpose, [migrate its purpose to `REGIONAL_MANAGED_PROXY`](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#migrate-purpose).




### No healthy upstream

**Symptom:**

The following issue might occur when you create a Gateway but cannot access the backend services (503 response code):
    
    
    no healthy upstream
    

**Reason:**

This error message indicates that the health check prober cannot find healthy backend services. It is possible that your backend services are healthy but you might need to customize the health checks.

**Workaround:**

To resolve this issue, [customize your health check](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check) based on your application's requirements (for example, `/health`) using a HealthCheckPolicy.

### Orphaned Gateway resources after cluster deletion

**Symptom:**

When attempting to re-create the Gateway, GKE-managed load balancer resources still remain visible in the Google Cloud console but cannot be deleted using the UI, which shows a message similar to the following:
    
    
    This load balancing service is read-only. It is managed by GKE and can be modified only by GKE.
    

**Reason:**

This issue occurs when the Gateway controller fails to clean up the stale underlying Google Cloud resources during cluster or gateway deletion and re-creation.

**Workaround:**

To resolve this issue, delete the orphaned load-balancing resources by using Google Cloud CLI commands as follows:
    
    
    gcloud compute forwarding-rules delete FORWARDING_RULE_NAME
    
    # For HTTP proxies
    gcloud compute target-http-proxies delete PROXY_NAME
    
    # For HTTPS proxies
    gcloud compute target-https-proxies delete PROXY_NAME
    
    gcloud compute url-maps delete URL_MAP_NAME
    
    # For global backend services
    gcloud compute backend-services delete BACKEND_SERVICE_NAME --global
    
    # For regional backend services
    gcloud compute backend-services delete BACKEND_SERVICE_NAME --region=REGION
    
    gcloud compute health-checks delete HEALTH_CHECK_NAME
    
    gcloud compute network-endpoint-groups delete NEG_NAME --zone=ZONE
    
    

Replace the following:

  * `FORWARDING_RULE_NAME`: the name of the forwarding rule.
  * `PROXY_NAME`: the name of the target proxy.
  * `URL_MAP_NAME`: the name of the URL map.
  * `BACKEND_SERVICE_NAME`: the name of the backend service.
  * `HEALTH_CHECK_NAME`: the name of the health check.
  * `NEG_NAME`: the name of the network endpoint group.
  * `REGION`: the region of the regional backend service.
  * `ZONE`: the zone of the network endpoint group.



## What's next

  * Learn more about the [Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn how to [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).
  * Learn about other Gateway configurations in the [Gateway API](https://gateway-api.sigs.k8s.io/guides/) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
