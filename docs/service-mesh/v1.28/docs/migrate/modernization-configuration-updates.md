---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/migrate/modernization-configuration-updates/
title: Configuration updates for modernization \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:34.088739+00:00
---

# Configuration updates for modernization  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/migrate/modernization-configuration-updates/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuration updates for modernization

This document describes configuration updates you may need to make to your managed Cloud Service Mesh before modernizing your mesh to the `TRAFFIC_DIRECTOR` control plane from the `ISTIOD` control plane.

The following are a list of possible configuration updates necessary to prepare your cluster for modernization. See each section for update instructions:

  * Multi-cluster
  * Enable Workload Identity Federation for GKE
  * Enable managed CNI
  * Non-Standard Binary Usage in Sidecar
  * Migrate to the Istio Ingress Gateway
  * Modernize EnvoyFilter compressor configurations
  * Enable Internet Network Endpoint Groups



For more information on the modernization workflow, see the [Managed control plane modernization](https://docs.cloud.google.com/service-mesh/v1.28/docs/modernization) page.

## Migrate from Istio secrets to multicluster_mode

Multi-cluster secrets are not supported when a cluster is using the `TRAFFIC_DIRECTOR` control plane. This document describes how you can modernize from using Istio multi-cluster secrets to using `multicluster_mode`.

### Istio secrets versus declarative API overview

[Open source istio multi-cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#how_works) endpoint discovery works by using `istioctl` or other tools to create a [Kubernetes Secret](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#before_you_begin) in a cluster. This secret allows a cluster to load balance traffic to another cluster in the mesh. The `ISTIOD` control plane then reads this secret and begins routing traffic to that other cluster.

Cloud Service Mesh has a [declarative API](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/multi-cluster#endpoint-discovery-declarative-api) to control multi-cluster traffic instead of directly creating Istio secrets. This API treats Istio secrets as an implementation detail and is more reliable than creating Istio secrets manually. Future Cloud Service Mesh features will depend on the declarative API, and you won't be able to use those new features with Istio secrets directly. The declarative API is the only supported path forward.

If you are using Istio Secrets, migrate to using the declarative API as soon as possible. Note that the `multicluster_mode` setting directs each cluster to direct traffic to every other cluster in the mesh. Using secrets allows a more flexible configuration, letting you configure for each cluster which other cluster it should direct traffic to in the mesh. For a full list of the differences between the supported features of the declarative API and Istio secrets, see [Supported features using Istio APIs](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-managed#multi-cluster_deployment).

**Important:** With the declarative API, an entire cluster is opted into endpoint discovery at a time. This means that every cluster with `multicluster_mode=connected` will discover endpoints for every other cluster in the fleet that also has `multicluster_mode=connected`. 

### Migrate from Istio secrets to declarative API

If you provisioned Cloud Service Mesh using automatic management with the [fleet feature API](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/provision-control-plane), you don't need to follow these instructions. These steps only apply if you onboarded using `asmcli --managed`.

Note, this process changes secrets that point to a cluster. During this process, the endpoints are removed and then re-added. In between the endpoints being removed and added, the traffic will briefly revert to routing locally instead of load balancing to other clusters. For more information, see the [GitHub issue](https://github.com/istio/istio/issues/36365).

To move from using Istio secrets to the declarative API, follow these steps. Execute these steps at the same time or in close succession:

  1. Enable the declarative API for each cluster in the fleet where you want to enable multi cluster endpoint discovery by setting `multicluster_mode=connected`. Note that you need to explicitly set `multicluster_mode=disconnected` if you don't want the cluster to be discoverable.

Use the following command to opt in a cluster for multi cluster endpoint discovery:
         
         kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"connected"}}'
         

Use the following command to opt a cluster out of endpoint discovery:
         
         kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"disconnected"}}'
         

  2. Delete old secrets.

After setting `multicluster_mode=connected` on your clusters, each cluster will have a new secret generated for every other cluster that also has `multicluster_mode=connected` set. The secret is placed in the istio-system namespace and have the following format:
         
         istio-remote-secret-projects-PROJECT_NAME-locations-LOCATION-memberships-MEMBERSHIPS
         

Each secret will also have the label `istio.io/owned-by: mesh.googleapis.com` applied.

Once the new secrets are created, you can delete any secrets manually created with `istioctl create-remote-secret`:
         
         kubectl delete secret SECRET_NAME -n istio-system
         




Once migrated, check your request metrics to make sure they're routed as expected.

## Enable Workload Identity Federation for GKE

Workload Identity Federation is the recommended secure method for Google Kubernetes Engine workloads. This allows access to Google Cloud services such as Compute Engine, BigQuery, and Machine Learning APIs. Workload Identity Federation doesn't require manual configuration or less secure methods like service account key files because it uses IAM policies. For more details on Workload Identity Federation, see [How Workload Identity Federation for GKE works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#how_works).

The following section describe how to enable Workload Identity Federation.

### Enable Workload Identity Federation on clusters

  1. Check Workload Identity Federation is enabled for your cluster. To do that, ensure the GKE cluster has a Workload Identity Federation pool set configured, which is essential for IAM credential validation.

Use the following command, to check the workload identity pool set for a cluster:
         
         gcloud container clusters describe CLUSTER_NAME \
           --format="value(workloadIdentityConfig.workloadPool)"
         

Replace `CLUSTER_NAME` with the name of your GKE cluster. If you haven't already specified [a default zone or region for gcloud](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#before_you_begin), you might also need to specify a `--region` or `--zone` flag when running this command.

  2. If the output is empty, follow the instructions in [Update an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable-existing-cluster) to enable workload identity on existing GKE clusters.




### Enable Workload Identity Federation on node pools

After Workload Identity Federation is enabled on a cluster, [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) must be configured to use the [GKE metadata server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#metadata_server).

  1. List all the node pools of a Standard cluster. Run the [gcloud container node-pools list](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list) command:
         
         gcloud container node-pools list --cluster CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your GKE cluster. If you haven't already specified [a default zone or region for gcloud](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#before_you_begin), you might also need to specify a `--region` or `--zone` flag when running this command.

  2. Verify that each node pool is using the GKE metadata server:
         
         gcloud container node-pools describe NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --format="value(config.workloadMetadataConfig.mode)"
         

Replace the following:

     * `NODEPOOL_NAME` with the name of your nodepool.
     * `CLUSTER_NAME` with the name of your GKE cluster.
  3. If the output doesn't contain `GKE_METADATA`, update the node pool using the [Update an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#option_2_node_pool_modification) guide.




## Enable managed container network interface (CNI)

This section guides you through enabling managed CNI for Cloud Service Mesh on Google Kubernetes Engine.

### Managed CNI overview

Managed container network interface (CNI) is a Google-managed implementation of the Istio CNI. The [CNI plugin](https://github.com/containernetworking/cni#cni---the-container-network-interface) streamlines pod networking by configuring iptables rules. This enables traffic redirection between applications and Envoy proxies, eliminating the need for privileged permissions for the init-container required to manage `iptables`.

The [Istio CNI plugin](https://istio.io/latest/docs/setup/additional-setup/cni/) replaces the `istio-init` container. The `istio-init` container was previously responsible for setting up the pod's network environment to enable traffic interception for the Istio sidecar. The CNI plugin performs the same network redirect function, but with the added benefit of reducing the need for elevated privileges, thereby enhancing security.

Therefore, for enhanced security and reliability, and to simplify management and troubleshooting, managed CNI is required across all Managed Cloud Service Mesh deployments.

### Impact on init containers

Init containers are specialized containers that run before application containers for setup tasks. Setup tasks can include tasks such as downloading configuration files, communicating with external services, or performing pre-application initialization. Init containers that rely on network access might encounter issues when managed CNI is enabled in the cluster.

The pod setup process with managed CNI is as follows:

  1. The CNI plugin sets up pod network interfaces, assigns pod IPs and redirects traffic to the Istio sidecar proxy which hasn't started yet.
  2. All init containers execute and complete.
  3. The Istio sidecar proxy starts alongside the application containers.



Therefore, if an init container attempts to make outbound network connections or connect to services within the mesh, the network requests from the init containers may be dropped or misrouted. This is because the Istio sidecar proxy, which manages network traffic for the pod, is not running when the requests are made. For more details, refer [Istio CNI documentation](https://istio.io/latest/docs/setup/additional-setup/cni/#how-sidecar-traffic-redirection-works).

### Enable managed CNI for your cluster

Follow the steps in this section to enable managed CNI on your cluster.

  1. Remove network dependencies from your init container. Consider the following alternatives:

     * **Modify application logic or containers:** You can modify your services to remove the dependency on init containers that require network requests or perform network operations within your application containers, after the sidecar proxy has started.
     * **Use Kubernetes ConfigMaps or secrets:** Store configuration data fetched by the network request in Kubernetes ConfigMaps or secrets and mount them into your application containers. For alternative solutions, refer to the [Istio documentation](https://istio.io/latest/docs/setup/additional-setup/cni/#compatibility-with-application-init-containers).
  2. Enable managed CNI on your cluster:

     1. Make the following configuration changes:

        1. Run the following command to locate the `controlPlaneRevision`.
               
               kubectl get controlplanerevision -n istio-system
               

        2. In your `ControlPlaneRevision` (CPR) custom resource (CR), set the annotation `mesh.cloud.google.com/managed-cni-enabled` to `true`.
               
               kubectl annotate controlplanerevision CPR_NAME \
                   -n istio-system mesh.cloud.google.com/managed-cni-enabled=true \
                   --overwrite
               

Replace `CPR_NAME` with the value under the NAME column from the output of the previous step.

        3. In the asm-options ConfigMap, set the `ASM_OPTS` value to `CNI=on`.
               
               kubectl patch configmap asm-options -n istio-system \
                   -p '{"data":{"ASM_OPTS":"CNI=on"}}'
               

        4. In your `ControlPlaneRevision` (CPR) custom resource (CR), set the label `mesh.cloud.google.com/force-reprovision` to `true`. This action triggers control plane restart.

**Note:** This method is not the recommended method for restarting the control plane, and should only be used for Cloud Service Mesh modernization efforts.
               
               kubectl label controlplanerevision CPR_NAME \
                   -n istio-system mesh.cloud.google.com/force-reprovision=true \
                   --overwrite
               

     2. Check the feature state. Retrieve the feature state using the following command:
            
            gcloud container fleet mesh describe --project FLEET_PROJECT_ID
            

Replace `FLEET_PROJECT_ID` with the ID of your Fleet Host project. Generally, the `FLEET_PROJECT_ID` has the same name as the project.

        * Verify that the `MANAGED_CNI_NOT_ENABLED` condition is removed from `servicemesh.conditions`.
        * Note, it may take up to 15-20 minutes for the state to update. Try waiting a few minutes and re-run the command.
     3. Once the `controlPlaneManagement.state` is `Active` in the cluster's feature state, **restart the pods**.




## Move away from Non-Standard Binary Usage in Sidecar

This section suggest ways to make your deployments compatible with the distroless envoy proxy image.

### Distroless envoy proxy sidecar images

Cloud Service Mesh uses two types of Envoy proxy sidecar images based on your [control plane configuration](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-managed#identify_control_plane_implementation), Ubuntu-based image containing various binaries and Distroless image. Distroless base images are minimal container images that prioritize security and resource optimization by only including essential components. The attack surface is reduced to help prevent vulnerabilities. For more information, refer to the documentation on [Distroless proxy image](https://docs.cloud.google.com/service-mesh/v1.28/docs/enable-optional-features-managed#distroless_proxy_image).

### Binary compatibility

As a best practice, you should restrict the contents of a container runtime to only the necessary packages. This approach improves security and the signal-to-noise ratio of Common Vulnerabilities and Exposures (CVE) scanners. Distroless Sidecar image has a minimal set of dependencies, stripped of all non-essential executables, libraries, and debugging tools. It is therefore not possible to execute a shell command or use curl, ping, or other debug utilities like `kubectl exec` inside the container.

### Make clusters compatible with distroless images

  * Remove references to any unsupported binaries (like bash or curl) from your configuration. Particularly inside Readiness, Startup, and Liveness [probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/), and Lifecycle PostStart and PreStop [hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) within the istio-proxy, istio-init, or istio-validation containers.
  * Consider alternatives like [holdApplicationUntilProxyStarts](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-pod-startup-time#global_mesh_configuration_holdapplicationuntilproxystarts) for certain use cases.
  * For debugging, you can use [ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) to attach to a running workload Pod. You can then inspect it and run custom commands. For an example, see [Collecting {service_mesh_name} logs](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-collect-logs#configure_envoy_proxy).



If you can't find a solution for your specific use case, contact Google Cloud Support at [Getting support](https://docs.cloud.google.com/service-mesh/v1.28/docs/getting-support).

## Migrate to the Istio Ingress Gateway

This section shows you how to migrate to the Istio Ingress Gateway. There are two methods for migrating to the Istio Ingress Gateway:

  1. Phased Migration with Traffic Splitting

This method prioritizes minimizing disruption in which you'll incrementally send traffic to the new Istio gateway, allowing you to monitor its performance on a small percentage of requests and quickly revert if necessary. Keep in mind that configuring Layer 7 traffic splitting can be challenging for some applications, so you need to manage both gateway systems concurrently during the transition. See Phased Migration with traffic splitting for the steps.

  2. Direct Migration

This method involves simultaneously rerouting all traffic to the new Istio gateway once you have thoroughly conducted testing. The advantage of this approach is complete separation from the old gateway's infrastructure, allowing adaptable configuration of the new gateway without the constraints of the existing setup. However, there is an increased risk of downtime in case unexpected problems arise with the new gateway during the transition. See Direct Migration for the steps.




The following migration examples assume you have an HTTP service ([httpbin](https://raw.githubusercontent.com/istio/istio/release-1.25/samples/httpbin/httpbin.yaml)) running in the application namespace (default) and exposed externally using Kubernetes Gateway API. The relevant configurations are:

  * Gateway: `k8-api-gateway` (in `istio-ingress` namespace) - configured to listen for HTTP traffic on port 80 for any hostname ending with `.example.com`.
  * HTTPRoute: `httpbin-route` (in `default` namespace) - directs any HTTP request with the hostname `httpbin.example.com` and a path starting with `/get` to the `httpbin` service within the `default` namespace.
  * The httpbin application is accessible using the external IP 34.57.246.68.



![Basic gateway diagram](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/gateway-basic-setup.svg)

### Phased Migration with traffic splitting

#### Provision a new Istio Ingress Gateway

  1. Deploy a new Ingress Gateway following the steps in the [Deploy sample gateway section](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/gateways#deploy_sample_gateway) and customize the sample configurations to your requirements. The samples in the [anthos-service-mesh](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/main/samples/gateways/istio-ingressgateway) repository are meant for deploying a `istio-ingressgateway` loadBalancer service and the corresponding `ingress-gateway` pods.

Example Gateway Resource (istio-ingressgateway.yaml)
         
         apiVersion: networking.istio.io/v1beta1
          kind: Gateway
          metadata:
            name: istio-api-gateway
            namespace: GATEWAY_NAMESPACE
          spec:
            selector:
              istio: ingressgateway  # The selector should match the ingress-gateway pod labels.
            servers:
            - port:
                number: 80
                name: http
                protocol: HTTP
              hosts:   # or specific hostnames if needed
              - "httpbin.example.com"
         

  2. Apply the [Gateway](https://istio.io/v1.24/docs/reference/config/networking/gateway/#Gateway) configuration to manage traffic:
         
         kubectl apply -f istio-ingressgateway.yaml -n GATEWAY_NAMESPACE
         

Ensure the 'spec.selector' in your Gateway resource matches the labels of your `ingress-gateway` pods. For example, if the `ingress-gateway` pods have the label `istio=ingressgateway`, your Gateway configuration must also select this the `istio=ingressgateway` label.




#### Configure initial routing for the new Gateway

  1. Define the initial routing rules for your application using an Istio [VirtualService](https://istio.io/latest/docs/reference/config/networking/virtual-service/).

Example VirtualService (my-app-vs-new.yaml):
         
         apiVersion: networking.istio.io/v1beta1
         kind: VirtualService
         metadata:
           name: httpbin-vs
           namespace: APPLICATION_NAMESPACE
         spec:
             gateways:
             - istio-ingress/istio-api-gateway  # Replace with <gateway-namespace/gateway-name>
             hosts:
             - httpbin.example.com
             http:
             - match:
               - uri:
                   prefix: /get
               route:
               - destination:
                   host: httpbin
                   port:
                     number: 8000
         

  2. Apply the VirtualService:
         
         kubectl apply -f my-app-vs-new.yaml -n MY_APP_NAMESPACE
         




#### Access the backend (httpbin) service through the newly deployed Istio Ingress Gateway

  1. Set the Ingress Host environment variable to the external IP address associated with the recently deployed `istio-ingressgateway` load balancer:
         
         export INGRESS_HOST=$(kubectl -n GATEWAY_NAMESPACE get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
         

  2. Verify the application (httpbin) is accessible using the new gateway:
         
         curl -s -I -HHost:httpbin.example.com "http://$INGRESS_HOST/get"
         

The output is similar to:
         
         HTTP/1.1 200 OK
         




![Request flow with the new istio ingress gateway](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/istio-api-gateway.svg)

#### Modify existing Ingress for traffic splitting

After confirming the successful setup of the new gateway (ex. istio-api-gateway), you can begin routing a portion of your traffic through it. To do this, update your current [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/) to direct a small percentage of traffic to the new gateway, while the larger portion continues to use the existing gateway (k8-api-gateway).

  1. Open the httproute for editing:
         
         kubectl edit httproute httpbin-route -n MY_APP_NAMESPACE
         

  2. Add a new backend reference pointing to the new Ingress Gateway's loadbalancer service with an initial weight of 10% and update the weight for the old gateway's backend.
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: httpbin-route
           namespace: MY_APP_NAMESPACE  # your application's namespace
         spec:
           parentRefs:
           - name: k8-api-gateway
             namespace: istio-ingress
           hostnames: ["httpbin.example.com"]
           rules:
           - matches:
             - path:
                 type: PathPrefix
                 value: /get
             backendRefs:
             - name: httpbin
               port: 8000
               weight: 90
             - name: istio-ingressgateway # Newly deployed load balancer service
               namespace: GATEWAY_NAMESPACE
               port: 80
               weight: 10
         

  3. Grant Permission for Cross-Namespace Referencing with reference grant.

To allow your `HTTPRoute` in the application namespace (default) to access `loadbalancer` service in gateway namespace (istio-ingress), you may need to create a [reference grant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/). This resource serves as a security control, explicitly defining which cross-namespace references are permitted.

The following `istio-ingress-grant.yaml` describes an example reference grant:
         
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: ReferenceGrant
         metadata:
           name: istio-ingressgateway-grant
           namespace: istio-ingress # Namespace of the referenced resource
         spec:
           from:
           - group: gateway.networking.k8s.io
             kind: HTTPRoute
             namespace: MY_APP_NAMESPACE # Namespace of the referencing resource
           to:
           - group: ""               # Core Kubernetes API group for Services
             kind: Service
             name: istio-ingressgateway # Loadbalancer Service of the new ingress gateway
         

  4. Apply the reference grant:
         
         kubectl apply -f istio-ingress-grant.yaml -n GATEWAY_NAMESPACE
         

  5. Verify requests to existing external IP address (ex. 34.57.246.68)are not failing. The following `check-traffic-flow.sh` describes a script to check request failures:
         
         # Update the following values based on your application setup
         external_ip="34.57.246.68" # Replace with existing external IP
         url="http://$external_ip/get"
         host_name="httpbin.example.com"
         
         # Counter for successful requests
         success_count=0
         
         # Loop 50 times
         for i in {1..50}; do
           # Perform the curl request and capture the status code
           status_code=$(curl -s -HHost:"$host_name" -o /dev/null -w "%{http_code}" "$url")
           # Check if the request was successful (status code 200)
           if [ "$status_code" -eq 200 ]; then
             ((success_count++))  # Increment the success counter
           else
             echo "Request $i: Failed with status code $status_code"
           fi
         done
         
         # After the loop, check if all requests were successful
         if [ "$success_count" -eq 50 ]; then
           echo "All 50 requests were successful!"
         else
           echo "Some requests failed.  Successful requests: $success_count"
         fi
         

  6. Execute the script to confirm that no requests fail, regardless of the traffic route:
         
         chmod +x check-traffic-flow.sh
         ./check-traffic-flow.sh
         




![Request flow with traffic split between existing gateway and new istio ingress gateway](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/istio-api-gateway-split.svg)

#### Slowly increase traffic percentage

If no request failures are seen for the existing external IP address (for example, `34.57.246.68`), gradually shift more traffic to the new Istio Ingress Gateway by adjusting the backend weights in your `HTTPRoute`. Increase the weight for the `istio-ingressgateway` and decrease the weight for the old gateway in small increments such as 10%, 20%, and on.

**Important:** Continuously observe key metrics such as request success rate, latency, error rates, and the resource utilization of your application pods to ensure stability at each increment.

Use the following command to update your existing `HTTPRoute`:
    
    
    kubectl edit httproute httpbin-route -n MY_APP_NAMESPACE
    

#### Full traffic migration and removing the old gateway

  1. When the new Istio Ingress Gateway demonstrates stable performance and successful request handling, shift all traffic to it. Update your `HTTPRoute` to set the old gateway's backend weight to `0` and the new gateway's to `100`.

  2. Once traffic is fully routed to the new gateway, update your external DNS records for your application's hostname (for example, `httpbin.example.com`) to point to the external IP address of the load balancer service created in Provision a new Istio Ingress Gateway.

  3. Finally, delete the old gateway and its associated resources:
         
         kubectl delete gateway OLD_GATEWAY -n GATEWAY_NAMESPACE
         kubectl delete service OLD_GATEWAY_SERVICE -n GATEWAY_NAMESPACE
         




### Direct Migration

#### Provision a new Istio Ingress Gateway

  1. Deploy a new Ingress Gateway following the steps in the [Deploy sample gateway section](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/gateways#deploy_sample_gateway) and customize the sample configurations to your requirements. The samples in the [anthos-service-mesh](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/main/samples/gateways/istio-ingressgateway) repository are meant for deploying a `istio-ingressgateway` loadBalancer service and the corresponding `ingress-gateway` pods.

Example Gateway Resource (istio-ingressgateway.yaml)
         
         apiVersion: networking.istio.io/v1beta1
          kind: Gateway
          metadata:
            name: istio-api-gateway
            namespace: GATEWAY_NAMESPACE
          spec:
            selector:
              istio: ingressgateway  # The selector should match the ingress-gateway pod labels.
            servers:
            - port:
                number: 80
                name: http
                protocol: HTTP
              hosts:   # or specific hostnames if needed
              - "httpbin.example.com"
         

  2. Apply the [Gateway](https://istio.io/v1.24/docs/reference/config/networking/gateway/#Gateway) configuration to manage traffic:
         
         kubectl apply -f istio-ingressgateway.yaml -n GATEWAY_NAMESPACE
         

Ensure the 'spec.selector' in your Gateway resource matches the labels of your `ingress-gateway` pods. For example, if the `ingress-gateway` pods have the label `istio=ingressgateway`, your Gateway configuration must also select this the `istio=ingressgateway` label.




#### Configure initial routing for the new Gateway

  1. Define the initial routing rules for your application using an Istio [VirtualService](https://istio.io/latest/docs/reference/config/networking/virtual-service/).

Example VirtualService (my-app-vs-new.yaml):
         
         apiVersion: networking.istio.io/v1beta1
         kind: VirtualService
         metadata:
           name: httpbin-vs
           namespace: APPLICATION_NAMESPACE
         spec:
             gateways:
             - istio-ingress/istio-api-gateway  # Replace with <gateway-namespace/gateway-name>
             hosts:
             - httpbin.example.com
             http:
             - match:
               - uri:
                   prefix: /get
               route:
               - destination:
                   host: httpbin
                   port:
                     number: 8000
         

  2. Apply the VirtualService:
         
         kubectl apply -f my-app-vs-new.yaml -n MY_APP_NAMESPACE
         




#### Access the backend (httpbin) service through the newly deployed Istio Ingress Gateway

  1. Set the Ingress Host environment variable to the external IP address associated with the recently deployed `istio-ingressgateway` load balancer:
         
         export INGRESS_HOST=$(kubectl -n GATEWAY_NAMESPACE get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
         

  2. Verify the application (httpbin) is accessible using the new gateway:
         
         curl -s -I -HHost:httpbin.example.com "http://$INGRESS_HOST/get"
         

The output is similar to:
         
         HTTP/1.1 200 OK
         




![Request flow with the new istio ingress gateway](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/istio-api-gateway.svg)

#### Test and Monitor new gateway

  1. Test all routing rules, validate TLS configuration, security policies, and other features. Perform load testing to verify the new gateway can handle expected traffic.

  2. Once the new gateway is fully tested, update your external DNS records for your application's hostname (for example, `httpbin.example.com`) to point to the external IP address of the load balancer service created in Provision a new Istio Ingress Gateway.

  3. Monitor key metrics such as request success rate, latency, error rates, and the resource utilization of your application pods to verify stability with the new Istio Ingress Gateway. Once stable, you can delete the old gateway and its associated resources
         
         kubectl delete gateway OLD_GATEWAY -n GATEWAY_NAMESPACE
         kubectl delete service OLD_GATEWAY_SERVICE -n GATEWAY_NAMESPACE
         




Important Considerations: Ensure TLS certificates and configurations are correctly set up on the new Istio Ingress Gateway if your application requires HTTPS. See [Set up TLS termination in ingress gateway](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/gateway-tls-termination) for more details.

## Fix multiple control planes

Cloud Service Mesh previously supported [onboarding using `asmcli` (deprecated)](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#August_22_2024) which did not block provisioning multiple control planes. Cloud Service Mesh now enforces the best practice of deploying only one channel per cluster that matches the cluster channel and does not support using multiple deployed channels in the same cluster.

If you want canary deployments on new versions of mesh in rapid before they become available in stable or regular, you need to use two different clusters where each has a separate channel. Note that channels are controlled by the GKE Cluster Channel, and Mesh does not have a separate channel associated with it.

You can check if you have multiple channels by looking for the `UNSUPPORTED_MULTIPLE_CONTROL_PLANES` status condition on your membership. If this warning does not appear, then you are not impacted and may skip reading this section.

  1. Run the following command to check if your cluster has multiple control plane channels:
         
         gcloud container fleet mesh describe
         

The output is similar to:
         
         ...
         projects/.../locations/global/memberships/my-membership:
             servicemesh:
               conditions:
               - code: **UNSUPPORTED_MULTIPLE_CONTROL_PLANES**
                 details: 'Using multiple control planes is not supported. Please remove a control plane from your cluster.'
                 documentationLink: https://cloud.google.com/service-mesh/v1.28/docs/migrate/modernization-configuration-updates#multiple_control_planes
                 severity: WARNING
               controlPlaneManagement:
                 details:
                 - code: REVISION_READY
                   details: 'Ready: asm-managed-stable'
                 implementation: ISTIOD
                 state: ACTIVE
         ...
         

  2. If the `UNSUPPORTED_MULTIPLE_CONTROL_PLANES` condition appeared, determine which channels exist for your cluster:
         
         kubectl get controlplanerevisions -n istio-system
         

The output is similar to:
         
         NAME                 RECONCILED   STALLED   AGE
         asm-managed-stable   True         False     97d
         asm-managed          True         False     97d
         asm-managed-rapid    True         False     97d
         

In this example, all three channels were provisioned:

     * asm-managed-stable -> STABLE
     * asm-managed -> REGULAR
     * asm-managed-rapid -> RAPID

If only 1 result appears, then only one channel is provisioned on your cluster, and you can skip the rest of these steps.

If 2 or more results appear, then follow the rest of these steps to remove the surplus channels.




### Consolidate workloads to one channel

Before you can remove additional channels, you must ensure your workloads are only using a single channel.

  1. Find all the labels you are using in your cluster:
         
         kubectl get namespaces -l istio.io/rev=RELEASE_CHANNEL
         

Depending on the output from the previous command, replace RELEASE_CHANNEL with `asm-managed-stable`, `asm-managed`, or `asm-managed-rapid`. Repeat this step for each provisioned channel.

The output is similar to:
         
         NAME      STATUS   AGE
         default   Active   110d
         

Note that in this example, the default namespace is being injected with the regular channel.

If all of your workloads are already using the same channel, you can skip to step Remove the extra channels. Otherwise, continue in this section.

  2. Change the labels so that only one channel is being used:

**Caution:** Consider the following before changing labels.
     * Pods can also be injected directly in some cases with the `sidecar.istio.io/inject` label. Make sure to check those for that usage as well.
     * You can ignore `istio-injection=enabled` labels for this step. Namespaces with that label will automatically change to match whichever channel is left in the cluster.
     * When selecting a channel to keep, try to select the channel that is the same as your GKE Cluster Channel. If this channel does not exist, then select any one of the active channels.
     * The actual channel you select does not matter. The GKE Cluster Channel determines which version of mesh you get, not the Mesh channel.
     * Check your meshconfig configuration between any active channels that are in use to make sure there are no differences between them. Each channel uses a separate configmap for configuration, so consolidating two channels down to one should ensure consistent behavior between the two channels. `kubectl get configmap istio-asm-managed{-rapid | -stable} -n istio-system -o yaml`
    
    kubectl label namespace NAMESPACE istio.io/rev- istio-injection=enabled --overwrite
    

Replace NAMESPACE with the name of your namespace.

The best practice is to use `istio-injection=enabled`. However, if you don't want to use that label, then you can also use `istio.io/rev=RELEASE_CHANNEL`.

Once you have changed the label for a namespace / pod, you must restart all workloads so that they are injected by the correct control plane.




### Remove the extra channels

Once you have verified that all of your workloads are running on a single channel, you can remove the unused, extra channels. If all three release channels were provisioned, remember to run the following commands for each channel.

  1. Delete the extra `ControlPlaneRevision` resource:
         
         kubectl delete controlplanerevision RELEASE_CHANNEL -n istio-system
         

Replace RELEASE_CHANNEL with `asm-managed-stable`, `asm-managed`, or `asm-managed-rapid`.

  2. Delete the `MutatingWebhookConfiguration`:
         
         kubectl delete mutatingwebhookconfiguration istiod-RELEASE_CHANNEL
         

  3. Delete the `meshconfig` configmap:
         
         kubectl delete configmap istio-RELEASE_CHANNEL
         




### Enable automatic management

**Caution:** Enabling automatic control plane management automatically enables multi-cluster and managed data plane on that cluster.

  1. Run the following command to enable automatic management:
         
         gcloud container fleet mesh update \
             --management automatic \
             --memberships MEMBERSHIP_NAME \
             --project PROJECT_ID \
             --location MEMBERSHIP_LOCATION
         

Replace the following:

     * MEMBERSHIP_NAME is the membership name listed when you verified that your cluster was registered to the fleet.
     * PROJECT_ID is the project ID of your project.
     * MEMBERSHIP_LOCATION is the location of your membership (either a region, or `global`). You can check your membership's location with `gcloud container fleet memberships list --project PROJECT_ID`.
  2. Verify that automatic management is enabled:
         
         gcloud container fleet mesh describe
         

The output is similar to:
         
         ...
         membershipSpecs:
           projects/.../locations/us-central1/memberships/my-member:
             mesh:
               management: **MANAGEMENT_AUTOMATIC**
         membershipStates:
           projects/.../locations/us-central1/memberships/my-member:
             servicemesh:
               conditions:
               - code: VPCSC_GA_SUPPORTED
                 details: This control plane supports VPC-SC GA.
                 documentationLink: http://cloud.google.com/service-mesh/docs/managed/vpc-sc
                 severity: INFO
               controlPlaneManagement:
                 details:
                 - code: REVISION_READY
                   details: 'Ready: asm-managed'
                 implementation: TRAFFIC_DIRECTOR
                 state: ACTIVE
               dataPlaneManagement:
                 details:
                 - code: OK
                   details: Service is running.
                 state: ACTIVE
             state:
               code: OK
               description: |-
                 Revision ready for use: asm-managed.
                 All Canonical Services have been reconciled successfully.
         ...
         




## Modernize EnvoyFilter compressor configurations

If you are using the `envoy.extensions.filters.http.compressor.v3.Compressor` filter, several top-level fields have been deprecated in Envoy and moved to `response_direction_config.common_config` and `request_direction_config.common_config`.

To learn how to update your `EnvoyFilter` resources to the modern and supported format, see the [Modernize EnvoyFilter compressor configurations](https://docs.cloud.google.com/service-mesh/v1.28/docs/migrate/modernize-envoyfilter-compressor) guide.

## Enabling a Required Organization Policy

Cloud Service Mesh requires specific policies to be enabled in order to operate successfully.

### Required Policies

#### compute.disableInternetNetworkEndpointGroup

Cloud Service Mesh requires the ability to create Internet [Network Endpoint Groups](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/provision-control-plane#negs-in-csm) (NEGs). These NEGs are essential components for routing traffic to services outside of Google Cloud.

The `constraints/compute.disableInternetNetworkEndpointGroup` constraint can prevent the creation of these necessary Internet NEGs.

If this organization policy is enforced on your project, folder, or organization, it will block Cloud Service Mesh from functioning correctly with the Traffic Director control plane. This will prevent migration to or successful operation of this Cloud Service Mesh configuration.

If `Enforced` is set to `true`, the creation of Internet NEGs is disabled.

### How do I know if I am impacted?

You can check the effective policy for your project using the Google Cloud console or Google Cloud CLI. Instructions for viewing organization policies can be found in the [Viewing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/using-constraints#viewing_organization_policies) section of the official documentation.

For example, you can use this Google Cloud CLI command:
    
    
    gcloud resource-manager org-policies describe constraints/compute.disableInternetNetworkEndpointGroup --project YOUR_PROJECT_ID --effective
    

If the policy shows the `enforced: true` value, then you are impacted.
    
    
    constraint: constraints/compute.disableInternetNetworkEndpointGroup
    booleanPolicy:
      enforced: true
    

If the policy shows a different value or is empty, then you are not impacted.
    
    
    constraint: constraints/compute.disableInternetNetworkEndpointGroup
    booleanPolicy: {}
    

### Resolving the Issue

If the policy is enforced, you will need to disable this constraint (set to `false`) at the organization, folder, or project level.

Detailed instructions on how to modify organization policies, including boolean constraints like this one, can be found in the [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) guide. You will typically need the `roles/orgpolicy.policyAdmin` role to make these changes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
