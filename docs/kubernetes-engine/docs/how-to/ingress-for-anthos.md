---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-for-anthos/
title: Deploying Ingress across clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:24.443811+00:00
---

# Deploying Ingress across clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-for-anthos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploying Ingress across clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to deploy an Ingress that serves an application across multiple GKE clusters. To learn more about Multi Cluster Ingress, see [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress).

For a detailed comparison between Multi Cluster Ingress (MCI), Multi-cluster Gateway (MCG), and load balancer with Standalone Network Endpoint Groups (LB and Standalone NEGs), see [Choose your multi-cluster load balancing API for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).

## Before you begin

This document assumes that you created clusters in a fleet and set the `gke-us` cluster as the config cluster for Multi Cluster Ingress, as described in [Setting up Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup). To verify this cluster configuration, follow these steps:

  1. Confirm that your project has two clusters that are members of a fleet:
         
         gcloud container clusters list \
             --format="table(name, location, fleet.project:label=FLEET, status)" \
             --project=FLEET_HOST_PROJECT
         

Replace `FLEET_HOST_PROJECT` with the project ID of the fleet host project.

The output is similar to the following:
         
         NAME      LOCATION          FLEET                                   STATUS
         gke-eu    europe-west1      FLEET_NAME   RUNNING
         gke-us    us-central1       FLEET_NAME   RUNNING
         

In this output, `FLEET_NAME` is the name of the fleet.

  2. Connect to the `gke-us` config cluster:
         
         gcloud container clusters get-credentials gke-us \
             --location=us-central1 \
             --project=CLUSTER_PROJECT
         

Replace `CLUSTER_PROJECT` with the project ID of the project that contains the `gke-us` cluster.

  3. Verify that the Kubernetes CustomResourceDefinitions for Multi Cluster Ingress are installed in the `gke-us` cluster:
         
         kubectl get crds | grep multicluster
         

The output is similar to the following:
         
         multiclusteringresses.networking.gke.io       2026-05-12T16:39:52Z
         multiclusterservices.networking.gke.io        2026-05-12T16:39:53Z
         

If the output is empty, disable and enable Multi Cluster Ingress for the fleet:

     1. Disable Multi Cluster Ingress:
            
            gcloud container fleet ingress disable \
                --project=FLEET_HOST_PROJECT
            

     2. Enable Multi Cluster Ingress for the fleet and specify the `gke-us` cluster as the config cluster:
            
            gcloud container fleet ingress enable \
                --config-membership=gke-us \
                --location=us-central1 \
                --project=CLUSTER_PROJECT
            

After you enable Multi Cluster Ingress, verify that the CustomResourceDefinitions are installed in the `gke-us` cluster by running the `kubectl get crds` command.




## Deployment tutorial

In the following tasks, you will deploy a fictional app named `whereami` and a `MultiClusterIngress` in two clusters. The Ingress provides a shared virtual IP (VIP) address for the app deployments.

### Creating the Namespace

Because fleets have the property of [namespace sameness](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#namespace_sameness), we recommend that you coordinate Namespace creation and management across clusters so identical Namespaces are owned and managed by the same group. You can create Namespaces per team, per environment, per application, or per application component. Namespaces can be as granular as necessary, as long as a Namespace `ns1` in one cluster has the same meaning and usage as `ns1` in another cluster.

In this example, you create a `whereami` Namespace for each application in each cluster.

  1. Create a file named `namespace.yaml` that has the following content:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: whereami
         

**Note:** You can use `kubectl config use-context` to switch between clusters when deploying resources. Use `kubectl config get-contexts` to see which ones are available. You can use `kubectl config rename-context` to rename contexts to more human-friendly names.
  2. Switch to the gke-us context:
         
         kubectl config use-context gke-us
         

  3. Create the Namespace:
         
         kubectl apply -f namespace.yaml
         

  4. Switch to the gke-eu context:
         
         kubectl config use-context gke-eu
         

  5. Create the Namespace:
         
         kubectl apply -f namespace.yaml
         

The output is similar to the following:
         
         namespace/whereami created
         




### Deploying the app

  1. Create a file named `deploy.yaml` that has the following content:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: whereami-deployment
           namespace: whereami
           labels:
             app: whereami
         spec:
           selector:
             matchLabels:
               app: whereami
           template:
             metadata:
               labels:
                 app: whereami
             spec:
               containers:
               - name: frontend
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                 - containerPort: 8080
         

  2. Switch to the gke-us context:
         
         kubectl config use-context gke-us
         

  3. Deploy the `whereami` app:
         
         kubectl apply -f deploy.yaml
         

  4. Switch to the gke-eu context:
         
         kubectl config use-context gke-eu
         

  5. Deploy the `whereami` app:
         
         kubectl apply -f deploy.yaml
         

  6. Verify that the `whereami` app has successfully deployed in each cluster:
         
         kubectl get deployment --namespace whereami
         

The output should be similar to the following in both clusters:
         
         NAME           READY   UP-TO-DATE   AVAILABLE   AGE
         whereami-deployment   1/1     1            1           12m
         




### Deploying through the config cluster

Now that the application is deployed across `gke-us` and `gke-eu`, you will deploy a load balancer by deploying `MultiClusterIngress` and `MultiClusterService` resources in the config cluster. These are the multi-cluster equivalents of Ingress and Service resources.

In the [setup guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup#specifying_a_config_cluster), you configured the `gke-us` cluster as the config cluster. The config cluster is used to deploy and configure Ingress across all clusters.

  1. Set the context to the config cluster.
         
         kubectl config use-context gke-us
         

**Note:** Only one cluster can be the active config cluster at any time. You can deploy `MultiClusterIngress` and `MultiClusterService` resources to other clusters, but they won't be seen or processed by the Multi Cluster Ingress controller.



#### MultiClusterService

  1. Create a file named `mcs.yaml` that has the following content:
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterService
         metadata:
           name: whereami-mcs
           namespace: whereami
         spec:
           template:
             spec:
               selector:
                 app: whereami
               ports:
               - name: web
                 protocol: TCP
                 port: 8080
                 targetPort: 8080
         

  2. Deploy the `MultiClusterService` resource that matches the `whereami` app:
         
         kubectl apply -f mcs.yaml
         

  3. Verify that the `whereami-mcs` resource has successfully deployed in the config cluster:
         
         kubectl get mcs -n whereami
         

The output is similar to the following:
         
         NAME       AGE
         whereami-mcs   9m26s
         

This `MultiClusterService` creates a derived headless Service in every cluster that matches Pods with `app: whereami`. You can see that one exists in the `gke-us` cluster `kubectl get service -n whereami`.

The output is similar to the following:
         
         NAME                                TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
         mci-whereami-mcs-svc-lgq966x5mxwwvvum   ClusterIP   None          <none>        8080/TCP         4m59s
         




A similar headless Service will also exist in `gke-eu`. These local Services are used to dynamically select Pod endpoints to program the global Ingress load balancer with backends.

#### MultiClusterIngress

  1. Create a file named `mci.yaml` that has the following content:
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterIngress
         metadata:
           name: whereami-ingress
           namespace: whereami
         spec:
           template:
             spec:
               backend:
                 serviceName: whereami-mcs
                 servicePort: 8080
         

Note that this configuration routes all traffic to the `MultiClusterService` named `whereami-mcs` that exists in the `whereami` namespace.

  2. Deploy the `MultiClusterIngress` resource that references `whereami-mcs` as a backend:
         
         kubectl apply -f mci.yaml
         

The output is similar to the following:
         
         multiclusteringress.networking.gke.io/whereami-ingress created
         

Note that `MultiClusterIngress` has the same schema as the Kubernetes Ingress. The Ingress resource semantics are also the same with the exception of the `backend.serviceName` field.




The `backend.serviceName` field in a `MultiClusterIngress` references a `MultiClusterService` in the fleet API rather than a Service in a Kubernetes cluster. This means that any of the settings for Ingress, such as TLS termination, settings can be configured in the same way.

## Validating a successful deployment status

Google Cloud Load Balancer deployment might take several minutes to deploy for new load balancers. Updating existing load balancers completes faster because new resources don't need to be deployed. The `MultiClusterIngress` resource details the underlying Compute Engine resources that have been created on behalf of the `MultiClusterIngress`.

  1. Verify that deployment has succeeded:
         
         kubectl describe mci whereami-ingress -n whereami
         

The output is similar to the following:
         
         Name:         whereami-ingress
         Namespace:    whereami
         Labels:       <none>
         Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                         {"apiVersion":"networking.gke.io/v1","kind":"MultiClusterIngress","metadata":{"annotations":{},"name":"whereami-ingress","namespace":"whe...
         API Version:  networking.gke.io/v1
         Kind:         MultiClusterIngress
         Metadata:
           Creation Timestamp:  2020-04-10T23:35:10Z
           Finalizers:
             mci.finalizer.networking.gke.io
           Generation:        2
           Resource Version:  26458887
           Self Link:         /apis/networking.gke.io/v1/namespaces/whereami/multiclusteringresses/whereami-ingress
           UID:               62bec0a4-8a08-4cd8-86b2-d60bc2bda63d
         Spec:
           Template:
             Spec:
               Backend:
                 Service Name:  whereami-mcs
                 Service Port:  8080
         Status:
           Cloud Resources:
             Backend Services:
               mci-8se3df-8080-whereami-whereami-mcs
             Firewalls:
               mci-8se3df-default-l7
             Forwarding Rules:
               mci-8se3df-fw-whereami-whereami-ingress
             Health Checks:
               mci-8se3df-8080-whereami-whereami-mcs
             Network Endpoint Groups:
               zones/europe-west1-b/networkEndpointGroups/k8s1-e4adffe6-whereami-mci-whereami-mcs-svc-lgq966x5m-808-88670678
               zones/us-central1-b/networkEndpointGroups/k8s1-a6b112b6-whereami-mci-whereami-mcs-svc-lgq966x5m-808-609ab6c6
             Target Proxies:
               mci-8se3df-whereami-whereami-ingress
             URL Map:  mci-8se3df-whereami-whereami-ingress
           VIP:        34.98.102.37
         Events:
           Type    Reason  Age                    From                              Message
           ----    ------  ----                   ----                              -------
           Normal  ADD     3m35s                  multi-cluster-ingress-controller  whereami/whereami-ingress
           Normal  UPDATE  3m10s (x2 over 3m34s)  multi-cluster-ingress-controller  whereami/whereami-ingress
         

There are several fields that indicate the status of this Ingress deployment:

     * `Events` is the first place to look. If an error has occurred it will be listed here.

     * `Cloud Resource`lists the Compute Engine resources like forwarding rules, backend services, and firewall rules that have been created by the Multi Cluster Ingress controller. If these are not listed it means that they have not been created yet. You can inspect individual Compute Engine resources with the Console or `gcloud` command to get its status.

     * `VIP` lists an IP address when one has been allocated. Note that the load balancer may not yet be processing traffic even though the VIP exists. If you don't see a VIP after a couple minutes, or if the load balancer is not serving a 200 response within 10 minutes, see [Troubleshooting and operations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/troubleshooting-and-ops).

If the output events are `Normal`, then the `MultiClusterIngress` deployment is likely successful, but the only way to determine that the full traffic path is functional is to test it.

  2. Validate that the application is serving on the VIP with the `/ping` endpoint:
         
         curl INGRESS_VIP/ping
         

Replace `INGRESS_VIP` with the virtual IP (VIP) address.

The output is similar to the following:
         
         {
         "cluster_name": "gke-us",
         "host_header": "34.120.175.141",
         "pod_name": "whereami-deployment-954cbf78-mtlpf",
         "pod_name_emoji": "😎",
         "project_id": "my-project",
         "timestamp": "2021-11-29T17:01:59",
         "zone": "us-central1-b"
         }
         

The output should indicate the region and backend of the application.

  3. You can also go to the `http://INGRESS_VIP` URL in your browser to see a graphical version of the application that shows the region that it's being served from.

The cluster that the traffic is forwarded to depends on your location. The GCLB is designed to forward client traffic to the closest available backend with capacity.




## Resource specs

### MultiClusterService spec

The `MultiClusterService` definition consists of two pieces:

  1. A `template` section that defines the Service to be created in the Kubernetes clusters. Note that while the `template` section contains fields supported in a typical Service, there are only two fields that are supported in a `MultiClusterService`: `selector` and `ports`. The other fields are ignored.

  2. An optional `clusters` section that defines which clusters receive traffic and the load balancing properties for each cluster. If no `clusters` section is specified or if no clusters are listed, all clusters are used by default.




The following manifest describes a standard `MultiClusterService`:
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterService
    metadata:
      name: NAME
      namespace: NAMESPACE
    spec:
      template:
        spec:
          selector:
            app: POD_LABEL
          ports:
          - name: web
            protocol: TCP
            port: PORT
            targetPort: TARGET_PORT
    

Replace the following:

  * `NAME`: the name of the `MultiClusterService`. This name is referenced by the `serviceName` field in the `MultiClusterIngress` resources.
  * `NAMESPACE`: the Kubernetes Namespace that the `MultiClusterService` is deployed in. It must match be in the same Namespace as the `MultiClusterIngress` and the Pods across all clusters in the fleet.
  * `POD_LABEL`: the label that determines which pods are selected as backends for this `MultiClusterService` across all clusters in the fleet.
  * `PORT`: must match with the port referenced by the `MultiClusterIngress` that references this `MultiClusterService`.
  * `TARGET_PORT`: the port that is used to send traffic to the Pod from the GCLB. A NEG is created in each cluster with this port as its serving port.



### MultiClusterIngress spec

The following `mci.yaml` describes the load balancer frontend:
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterIngress
    metadata:
      name: NAME
      namespace: NAMESPACE
    spec:
      template:
        spec:
          backend:
           serviceName: DEFAULT_SERVICE
           servicePort: PORT
          rules:
            - host: HOST_HEADER
              http:
                paths:
                - path: PATH
                  backend:
                    serviceName: SERVICE
                    servicePort: PORT
    

Replace the following:

  * `NAME`: the name of the `MultiClusterIngress` resource.
  * `NAMESPACE`: the Kubernetes Namespace that the `MultiClusterIngress` is deployed in. It must be in the same Namespace as the `MultiClusterService` and the Pods across all clusters in the fleet.
  * `DEFAULT_SERVICE`: acts as the default backend for all traffic that does not match any host or path rules. This is a required field and a default backend must be specified in the `MultiClusterIngress` even if there are other host or path matches configured.
  * `PORT`: any valid port number. This must match with the `port` field of the `MultiClusterService` resources.
  * `HOST_HEADER`: matches traffic by the HTTP host header field. The `host` field is optional.
  * `PATH`: matches traffic by the path of the HTTP URL. The `path` field is optional.
  * `SERVICE`: the name of a `MultiClusterService` that is deployed in the same Namespace and config cluster as this `MultiClusterIngress`.



## Multi Cluster Ingress features

This section shows you how to configure additional Multi Cluster Ingress features.

### Cluster selection

By default, Services derived from Multi Cluster Ingress are scheduled on every member cluster. However, you may want to apply ingress rules to specific clusters. Some use-cases include:

  * Applying Multi Cluster Ingress to all clusters but the config cluster for isolation of the config cluster.
  * Migrating workloads between clusters in a blue-green fashion.
  * Routing to application backends that only exist in a subset of clusters.
  * Using a single L7 VIP for host or path routing to backends that live on different clusters.



Cluster selection lets you select clusters by region or name in the `MultiClusterService` object. This controls which clusters your `MultiClusterIngress` is pointing to and where the derived Services are scheduled. Clusters within the same fleet and region shouldn't have the same name so that clusters can be referenced uniquely.

  1. Open `mcs.yaml`
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterService
         metadata:
           name: whereami-mcs
           namespace: whereami
         spec:
           template:
             spec:
               selector:
                 app: whereami
               ports:
               - name: web
                 protocol: TCP
                 port: 8080
                 targetPort: 8080
         

This specification creates Derived Services in all clusters, the default behavior.

  2. Append the following lines in the clusters section:
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterService
         metadata:
           name: whereami-mcs
           namespace: whereami
         spec:
           template:
             spec:
               selector:
                 app: whereami
               ports:
               - name: web
                 protocol: TCP
                 port: 8080
                 targetPort: 8080
           clusters:
           - link: "us-central1-b/gke-us"
           - link: "europe-west1-b/gke-eu"
         

This example creates Derived Service resources only in gke-us and gke-eu clusters. You must select clusters to selectively apply ingress rules. If the "clusters" section of the `MultiClusterService` is not specified or if no clusters are listed, it is interpreted as the default "all" clusters.




### HTTPS support

The Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) supports HTTPS. Before enabling HTTPS support, you must create a static IP address. This static IP allows HTTP and HTTPS to share the same IP address. For more information, see Creating a static IP.

Once you have created a static IP address, you can create a Secret.

**Note:** The public key certificate must be .PEM encoded and match the given private key.

  1. Create a Secret:
         
         kubectl -n whereami create secret tls SECRET_NAME --key PATH_TO_KEYFILE --cert PATH_TO_CERTFILE
         

Replace the following:

     * `SECRET_NAME` with the name of your Secret.
     * `PATH_TO_KEYFILE` with the path to the TLS key file.
     * `PATH_TO_CERTFILE` with the path to the TLS certificate file.
  2. Update the `mci.yaml` file with the Secret name:
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterIngress
         metadata:
           name: whereami-ingress
           namespace: whereami
           annotations:
             networking.gke.io/static-ip: STATIC_IP_ADDRESS
         spec:
           template:
             spec:
               backend:
                 serviceName: whereami-mcs
                 servicePort: 8080
               tls:
               - secretName: SECRET_NAME
         

Replace the `SECRET_NAME` with the name of your Secret. The `STATIC_IP_ADDRESS` is the IP address or the complete URL of the address you allocated in the Creating a static IP section.

  3. Redeploy the `MultiClusterIngress` resource:
         
         kubectl apply -f mci.yaml
         

The output is similar to the following:
         
         multiclusteringress.networking.gke.io/whereami-ingress configured
         




### BackendConfig support

The following BackendConfig CRD lets you customize settings on the Compute Engine BackendService resource:
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: whereami-health-check-cfg
      namespace: whereami
    spec:
      healthCheck:
        checkIntervalSec: [int]
        timeoutSec: [int]
        healthyThreshold: [int]
        unhealthyThreshold: [int]
        type: [HTTP | HTTPS | HTTP2 | TCP]
        port: [int]
        requestPath: [string]
      timeoutSec: [int]
      connectionDraining:
        drainingTimeoutSec: [int]
      sessionAffinity:
        affinityType: [CLIENT_IP | CLIENT_IP_PORT_PROTO | CLIENT_IP_PROTO | GENERATED_COOKIE | HEADER_FIELD | HTTP_COOKIE | NONE]
        affinityCookieTtlSec: [int]
      cdn:
        enabled: [bool]
        cachePolicy:
          includeHost: [bool]
          includeQueryString: [bool]
          includeProtocol: [bool]
          queryStringBlacklist: [string list]
          queryStringWhitelist: [string list]
      securityPolicy:
        name: ca-how-to-security-policy
      logging:
        enable: [bool]
        sampleRate: [float]
      iap:
        enabled: [bool]
        oauthclientCredentials:
          secretName: [string]
    

To use BackendConfig, attach it on your `MultiClusterService` resource using an annotation:
    
    
    apiVersion: networking.gke.io/v1
    kind: MultiClusterService
    metadata:
      name: whereami-mcs
      namespace: whereami
      annotations:
        cloud.google.com/backend-config: '{"ports": {"8080":"whereami-health-check-cfg"}}'
    spec:
     template:
       spec:
         selector:
           app: whereami
         ports:
         - name: web
           protocol: TCP
           port: 8080
           targetPort: 8080
    

For more information about BackendConfig semantics, see [Associating a service port with a BackendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/backendconfig#associating_a_service_port_with_a_backendconfig).

### gRPC support

Configuring gRPC applications on Multi Cluster Ingress requires very specific setup. Here are some tips to make sure your load balancer is configured properly:

  1. Make sure that the traffic from the load balancer to your application is HTTP/2. Use application protocols to configure this.
  2. Make sure that your application is properly configured for SSL since this is a [requirement](https://docs.cloud.google.com/load-balancing/docs/https#protocol_to_the_backends) of HTTP/2. Note that using self-signed certs is acceptable.
  3. You must turn off mTLS on your application because mTLS is [not supported](https://docs.cloud.google.com/load-balancing/docs/https#client_communications_with_the_load_balancer) for L7 external load balancers.



## Resource lifecycle

### Configuration changes

`MultiClusterIngress` and `MultiClusterService` resources behave as standard Kubernetes objects, so changes to the objects are asynchronously reflected in the system. Any changes that result in an invalid configuration cause associated Google Cloud objects to remain unchanged and raise an error in the object event stream. Errors associated with the configuration will be reported as events.

### Managing Kubernetes resources

Deleting the Ingress object tears down the HTTP(S) load balancer so traffic is no longer forwarded to any defined `MultiClusterService`.

Deleting the `MultiClusterService` removes the associated derived services in each of the clusters.

### Managing clusters

The set of clusters targeted by the load balancer can be changed by adding or removing clusters from the fleet.

For example, to remove the `gke-eu` cluster as a backend for an ingress, run:
    
    
    gcloud container fleet memberships unregister CLUSTER_NAME \
      --gke-uri=URI
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `URI`: the URI of the GKE cluster.



To add a cluster in Europe, run:
    
    
    gcloud container fleet memberships register europe-cluster \
      --context=europe-cluster --enable-workload-identity
    

You can find out more about cluster registration options in [Register a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).

Note that registering or unregistering a cluster changes its status as a backend for all Ingresses. Unregistering the `gke-eu` cluster removes it as an available backend for all Ingresses you create. The reverse is true for registering a new cluster.

**Note:** If you want to delete a fleet member cluster, ensure you unregister the cluster before you delete it. Failure to do so could result in unexpected behavior.

### Disabling Multi Cluster Ingress

Before disabling Multi Cluster Ingress you must ensure that you first delete your `MultiClusterIngress` and `MultiClusterService` resources and verify any associated networking resources are deleted.

Then, to disable Multi Cluster Ingress, use the following command:
    
    
    gcloud container fleet ingress disable
    

If you don't delete `MultiClusterIngress` and `MultiClusterService` resources before disabling Multi Cluster Ingress, you might encounter an error similar to the following:
    
    
    Feature has associated resources that should be cleaned up before deletion.
    

If you want to force disable Multi Cluster Ingress, use the following command:
    
    
    gcloud container fleet ingress disable --force
    

**Note:** Force disabling might result in unexpected behavior. It is not recommended to force disable for production environments.

## Annotations

The following annotations are supported on `MultiClusterIngress` and `MultiClusterService` resources.

#### MultiClusterIngress Annotations

**Annotation** | **Description**  
---|---  
networking.gke.io/frontend-config | References a [FrontendConfig resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_frontendconfig_parameters) in the same Namespace as the MultiClusterIngress resource.  
networking.gke.io/static-ip | Refers to the literal IP address of a global static IP.  
networking.gke.io/pre-shared-certs | Refers to a global SSLCertificate resource.  
  
#### MultiClusterService Annotations

**Annotation** | **Description**  
---|---  
networking.gke.io/app-protocols | Use this annotation to set the protocol for communication between the load balancer and the application. Possible protocols are HTTP, HTTPS, and HTTP/2. See [HTTPS between load balancer and your application](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#https_tls_between_load_balancer_and_your_application) and [HTTP/2 for load balancing with Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-http2).  
cloud.google.com/backend-config | Use this annotation to configure the backend service associated with a servicePort. For more information, see [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).  
  
### SSL Policies and HTTPS Redirects

You can use the FrontendConfig resource to configure SSL policies and HTTPS redirects. SSL policies allow you to specify which cipher suites and TLS versions are accepted by the load balancer. HTTPS redirects allow you to enforce the redirection from HTTP or port 80 to HTTPS or port 443. The following steps configure an SSL policy and HTTPS redirect together. Note that they can also be configured independently.

  1. Create an [SSL policy](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#creating_an_ssl_policy_with_a_google-managed_profile) that will reject requests using a version lower than TLS v1.2.
         
         gcloud compute ssl-policies create tls-12-policy \
          --profile MODERN \
          --min-tls-version 1.2 \
          --project=PROJECT_ID
         

Replace `PROJECT_ID` with the project ID where your GKE clusters are running.

  2. View your policy to ensure it has been created.
         
         gcloud compute ssl-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         NAME           PROFILE  MIN_TLS_VERSION
         tls-12-policy  MODERN   TLS_1_2
         

  3. Create a certificate for `foo.example.com` as in [the example](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#creating_and_storing_a_tls_certificate). Once you have the `key.pem` and `cert.pem`, store these credentials as a Secret that will be referenced by the MultiClusterIngress resource.
         
         kubectl -n whereami create secret tls SECRET_NAME --key key.pem --cert cert.pem
         

  4. Save the following FrontendConfig resource as `frontendconfig.yaml`. See [Configuring FrontendConfig resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_frontendconfig_parameters) for more information on the supported fields within a FrontendConfig.
         
         apiVersion: networking.gke.io/v1beta1
         kind: FrontendConfig
         metadata:
           name: frontend-redirect-tls-policy
           namespace: whereami
         spec:
           sslPolicy: tls-12-policy
           redirectToHttps:
             enabled: true
         

This FrontendConfig will enable HTTPS redirects and an SSL policy that enforces a minimum TLS version of 1.2.

  5. Deploy `frontendconfig.yaml` into your config cluster.
         
         kubectl apply -f frontendconfig.yaml --context MCI_CONFIG_CLUSTER
         

Replace the `MCI_CONFIG_CLUSTER` with the name of your [config cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup#specifying_a_config_cluster).

  6. Save the following MultiClusterIngress as `mci-frontendconfig.yaml`.
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterIngress
         metadata:
           name: foo-ingress
           namespace: whereami
           annotations:
             networking.gke.io/frontend-config: frontend-redirect-tls-policy
             networking.gke.io/static-ip: STATIC_IP_ADDRESS
         spec:
           template:
             spec:
               backend:
                 serviceName: default-backend
                 servicePort: 8080
               rules:
               - host: foo.example.com
                 http:
                   paths:
                     - backend:
                         serviceName: whereami-mcs
                         servicePort: 8080
               tls:
               - secretName: SECRET_NAME
         

     * Replace `STATIC_IP_ADDRESS` with a static global IP address that you have already provisioned.
     * Replace `SECRET_NAME` with the Secret where your `foo.example.com` certificate is stored.

There are two requirements when enabling HTTPS redirects:

     * TLS must be enabled, either through the `spec.tls` field or through the pre-shared certificate annotation `networking.gke.io/pre-shared-certs`. The MultiClusterIngress won't deploy if HTTPS redirects is enabled but HTTPS is not.
     * A static IP must be referenced through the `networking.gke.io/static-ip` annotation. Static IPs are required when enabling HTTPS on a MultiClusterIngress.
**Note:** Deployment of the application or MultiClusterService is not shown in this example, but they must also be created for this to fully work.
  7. Deploy the MultiClusterIngress to your config cluster.
         
         kubectl apply -f mci-frontendconfig.yaml --context MCI_CONFIG_CLUSTER
         

  8. Wait a minute or two and inspect `foo-ingress`.
         
         kubectl describe mci foo-ingress --context MCI_CONFIG_CLUSTER
         

A successful output resembles the following:

     * The `Cloud Resources` status is populated with resource names
     * The `VIP` field is populated with the load balancer IP address
    
    Name:         foobar-ingress
    Namespace:    whereami
    
    ...
    
    Status:
      Cloud Resources:
        Backend Services:
          mci-otn9zt-8080-whereami-bar
          mci-otn9zt-8080-whereami-default-backend
          mci-otn9zt-8080-whereami-foo
        Firewalls:
          mci-otn9zt-default-l7
        Forwarding Rules:
          mci-otn9zt-fw-whereami-foobar-ingress
          mci-otn9zt-fws-whereami-foobar-ingress
        Health Checks:
          mci-otn9zt-8080-whereami-bar
          mci-otn9zt-8080-whereami-default-backend
          mci-otn9zt-8080-whereami-foo
        Network Endpoint Groups:
          zones/europe-west1-b/networkEndpointGroups/k8s1-1869d397-multi-cluste-mci-default-backend-svc--80-9e362e3d
          zones/europe-west1-b/networkEndpointGroups/k8s1-1869d397-multi-cluster--mci-bar-svc-067a3lzs8-808-89846515
          zones/europe-west1-b/networkEndpointGroups/k8s1-1869d397-multi-cluster--mci-foo-svc-820zw3izx-808-8bbcb1de
          zones/us-central1-b/networkEndpointGroups/k8s1-a63e24a6-multi-cluste-mci-default-backend-svc--80-a528cc75
          zones/us-central1-b/networkEndpointGroups/k8s1-a63e24a6-multi-cluster--mci-bar-svc-067a3lzs8-808-36281739
          zones/us-central1-b/networkEndpointGroups/k8s1-a63e24a6-multi-cluster--mci-foo-svc-820zw3izx-808-ac733579
        Target Proxies:
          mci-otn9zt-whereami-foobar-ingress
          mci-otn9zt-whereami-foobar-ingress
        URL Map:  mci-otn9zt-rm-whereami-foobar-ingress
      VIP:        34.149.29.76
    Events:
      Type     Reason  Age                From                              Message
      ----     ------  ----               ----                              -------
      Normal   UPDATE  38m (x5 over 62m)  multi-cluster-ingress-controller  whereami/foobar-ingress
    

  9. Verify that HTTPS redirects function correctly by sending an HTTP request through `curl`.
         
         curl VIP
         

Replace `VIP` with the MultiClusterIngress IP address.

The output should show that the request was redirected to the HTTPS port which indicates that redirects are functioning correctly.

  10. Verify that the TLS policy functions correctly by sending an HTTPS request using TLS version 1.1. Because DNS is not configured for this domain, use the `--resolve` option to tell `curl` to resolve the IP address directly.
         
         curl https://foo.example.com --resolve foo.example.com:443:VIP --cacert CERT_FILE -v
         

This step requires the certificate PEM file used to secure the MultiClusterIngress. A successful output will look similar to the following:
         
         ...
         * SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
         * ALPN, server accepted to use h2
         * Server certificate:
         *  subject: O=example; CN=foo.example.com
         *  start date: Sep  1 10:32:03 2021 GMT
         *  expire date: Aug 27 10:32:03 2022 GMT
         *  common name: foo.example.com (matched)
         *  issuer: O=example; CN=foo.example.com
         *  SSL certificate verify ok.
         * Using HTTP2, server supports multi-use
         * Connection state changed (HTTP/2 confirmed)
         * Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
         * Using Stream ID: 1 (easy handle 0x7fa10f00e400)
         > GET / HTTP/2
         > Host: foo.example.com
         > User-Agent: curl/7.64.1
         > Accept: */*
         >
         * Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
         < HTTP/2 200
         < content-type: application/json
         < content-length: 308
         < access-control-allow-origin: *
         < server: Werkzeug/1.0.1 Python/3.8.6
         < date: Wed, 01 Sep 2021 11:39:06 GMT
         < via: 1.1 google
         < alt-svc: clear
         <
         {"cluster_name":"gke-us","host_header":"foo.example.com","metadata":"foo","node_name":"gke-gke-us-default-pool-22cb07b1-r5r0.c.mark-church-project.internal","pod_name":"foo-75ccd9c96d-dkg8t","pod_name_emoji":"👞","project_id":"mark-church-project","timestamp":"2021-09-01T11:39:06","zone":"us-central1-b"}
         * Connection #0 to host foo.example.com left intact
         * Closing connection 0
         

The response code is 200 and TLSv1.2 is being used which indicates that everything is functioning properly.

Next you can verify that the SSL policy enforces the correct TLS version by attempting to connect with TLS 1.1. Your SSL policy must be configured for a minimum version of 1.2 for this step to work.

  11. Send the same request from the previous step, but enforce a TLS version of 1.1.
         
         curl https://foo.example.com --resolve foo.example.com:443:VIP -v \
           --cacert CERT_FILE \
           --tls-max 1.1
         

A successful output will look similar to the following:
         
         * Added foo.example.com:443:34.149.29.76 to DNS cache
         * Hostname foo.example.com was found in DNS cache
         *   Trying 34.149.29.76...
         * TCP_NODELAY set
         * Connected to foo.example.com (34.149.29.76) port 443 (#0)
         * ALPN, offering h2
         * ALPN, offering http/1.1
         * successfully set certificate verify locations:
         *   CAfile: cert.pem
           CApath: none
         * TLSv1.1 (OUT), TLS handshake, Client hello (1):
         * TLSv1.1 (IN), TLS alert, protocol version (582):
         * error:1400442E:SSL routines:CONNECT_CR_SRVR_HELLO:tlsv1 alert protocol version
         * Closing connection 0
         curl: (35) error:1400442E:SSL routines:CONNECT_CR_SRVR_HELLO:tlsv1 alert protocol version
         

The failure to complete the TLS handshake indicates that the SSL policy has blocked TLS 1.1 successfully.




### Creating a static IP

  1. Allocate a static IP:
         
         gcloud compute addresses create ADDRESS_NAME --global
         

Replace `ADDRESS_NAME` with the name of the static IP to allocate.

The output contains the complete URL of the address you created, similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses/ADDRESS_NAME].
         

  2. View the IP address you just created:
         
         gcloud compute addresses list
         

The output is similar to the following:
         
         NAME          ADDRESS/RANGE  TYPE      STATUS
         ADDRESS_NAME  STATIC_IP_ADDRESS  EXTERNAL  RESERVED
         

This output includes:

     * The `ADDRESS_NAME` you defined.
     * The `STATIC_IP_ADDRESS` allocated.
  3. Update the `mci.yaml` file with the static IP:
         
         apiVersion: networking.gke.io/v1
         kind: MultiClusterIngress
         metadata:
           name: whereami-ingress
           namespace: whereami
           annotations:
             networking.gke.io/static-ip: STATIC_IP_ADDRESS
         spec:
           template:
             spec:
               backend:
                 serviceName: whereami-mcs
                 servicePort: 8080
         

Replace the `STATIC_IP_ADDRESS` with either:

     * The allocated IP address, similar to: `34.102.201.47`
     * The complete URL of the address you created, similar to: `"https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses/ADDRESS_NAME"`

The `STATIC_IP_ADDRESS` is not the resource name (`ADDRESS_NAME`).

  4. Redeploy the `MultiClusterIngress` resource:
         
         kubectl apply -f mci.yaml
         

The output is similar to the following:
         
         multiclusteringress.networking.gke.io/whereami-ingress configured
         

  5. Follow the steps in Validating a successful deployment status to verify that the deployment is serving on the `STATIC_IP_ADDRESS`.




### Pre-shared certificates

[Pre-shared certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl#using_pre-shared_certificates) are certificates uploaded to Google Cloud that can be used by the load balancer for TLS termination instead of certificates stored in Kubernetes Secrets. These certificates are uploaded out of band from GKE to Google Cloud and referenced by a `MultiClusterIngress` resource. Multiple certificates, either through pre-shared certs or Kubernetes secrets, are also supported.

Using the certificates in Multi Cluster Ingress requires the `networking.gke.io/pre-shared-certs` annotation and the names of the certs. When multiple certificates are specified for a given `MultiClusterIngress`, a predetermined order governs which cert is presented to the client.

You can list the available SSL certificates by running:
    
    
    gcloud compute ssl-certificates list
    

The following example describes client traffic to one of the specified hosts that matches the Common Name of the pre-shared certs so the respective certificate that matches the domain name will be presented.
    
    
    kind: MultiClusterIngress
    metadata:
      name: shopping-service
      namespace: whereami
      annotations:
        networking.gke.io/pre-shared-certs: "domain1-cert, domain2-cert"
    spec:
      template:
        spec:
          rules:
          - host: my-domain1.gcp.com
            http:
              paths:
              - backend:
                  serviceName: domain1-svc
                  servicePort: 443
          - host: my-domain2.gcp.com
            http:
              paths:
              - backend:
                  serviceName: domain2-svc
                  servicePort: 443
    

### Google-managed Certificates

[Google-managed Certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) are supported on `MultiClusterIngress` resources through the `networking.gke.io/pre-shared-certs` annotation. Multi Cluster Ingress supports the attachment of Google-managed certificates to a `MultiClusterIngress` resource, however unlike single-cluster Ingress, the [declarative generation of a Kubernetes `ManagedCertificate` resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs#setting_up_the_managed_certificate) is not supported on `MultiClusterIngress` resources. The original creation of the Google-managed certificate must be done directly through the `compute ssl-certificates create` API before you can attach it to a `MultiClusterIngress`. That can be done following these steps:

  1. Create a Google-managed Certificate as [in step 1 here.](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#create-ssl) Don't move to step 2 as Multi Cluster Ingress will attach this certificate for you.
         
         gcloud compute ssl-certificates create my-google-managed-cert \
             --domains=my-domain.gcp.com \
             --global
         

  2. Reference the name of the certificate in your `MultiClusterIngress` using the `networking.gke.io/pre-shared-certs` annotation.
         
         kind: MultiClusterIngress
         metadata:
         name: shopping-service
         namespace: whereami
         annotations:
           networking.gke.io/pre-shared-certs: "my-google-managed-cert"
         spec:
         template:
           spec:
             rules:
             - host: my-domain.gcp.com
               http:
                 paths:
                 - backend:
                     serviceName: my-domain-svc
                     servicePort: 8080
         




The preceding manifest attaches the certificate to your `MultiClusterIngress` so that it can terminate traffic for your backend GKE clusters. Google Cloud will [automatically renew your certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#renewal) prior to certificate expiry. Renewals occur transparently and does not require any updates to Multi Cluster Ingress.

### Application protocols

The connection from the load balancer proxy to your application uses HTTP by default. Using `networking.gke.io/app-protocols` annotation, you can configure the load balancer to use HTTPS or HTTP/2 when it forwards requests to your application. In the `annotation` field of the following example, `http2` refers to the `MultiClusterService` port name and `HTTP2` refers to the protocol that the load balancer uses.
    
    
    kind: MultiClusterService
    metadata:
      name: shopping-service
      namespace: whereami
      annotations:
        networking.gke.io/app-protocols: '{"http2":"HTTP2"}'
    spec:
      template:
        spec:
          ports:
          - port: 443
            name: http2
    

### BackendConfig

Refer to the section above on how to configure the annotation.

## What's next

  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * Learn more about [setting up HTTP Load Balancing with Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer).
  * Implement [Multi Cluster Ingress with end to end HTTPS](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/multi-cluster/mci-https-e2e).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
