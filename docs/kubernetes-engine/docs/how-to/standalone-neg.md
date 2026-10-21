---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg/
title: Container-native load balancing through standalone zonal NEGs \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:04:21.169071+00:00
---

# Container-native load balancing through standalone zonal NEGs  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Container-native load balancing through standalone zonal NEGs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to create a Kubernetes Service that is backed by a [zonal `GCE_VM_IP_PORT` network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs#zonal-neg) in a Google Kubernetes Engine (GKE) [VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).

For information on the benefits, requirements, and limitations of container-native load balancing, see [Container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing).

## Overview

A [NEG](https://docs.cloud.google.com/load-balancing/docs/negs) represents a group of endpoints. GKE supports standalone NEGs of the `GCE_VM_IP_PORT` type. `GCE_VM_IP_PORT` NEGs support endpoints using either the VM's primary internal IP address or an IP address from one of its alias IP ranges.

In the context of a GKE VPC-native cluster using standalone NEGs, each endpoint is a Pod IP address and target port. Pod IP addresses are sourced from the node's alias IP range for Pods, which comes from the cluster's [subnet secondary IP address range for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_pods).

GKE provides a _NEG controller_ to manage the membership of `GCE_VM_IP_PORT` NEGs. You can add the NEGs it creates as backends to the backend services for load balancers that you configure outside of the GKE API.

The following diagram describes how Kubernetes API objects correspond to Compute Engine objects.

![Kubernetes Services correspond to Compute Engine network endpoint groups,
while Kubernetes Pods correspond to Compute Engine network endpoints. The NEG
controller component of the control plane manages this.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg1.svg)

### Ingress with NEGs

When [NEGs are used with GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing), the Ingress controller facilitates the creation of all aspects of the load balancer. This includes creating the virtual IP address, forwarding rules, health checks, firewall rules, and more.

Ingress is the recommended way to use container-native load balancing as it has many features that simplify the management of NEGs. Standalone NEGs are an option if NEGs managed by Ingress don't serve your use case.

### Standalone NEGs

When NEGs are deployed with load balancers provisioned by anything other than Ingress, they are considered standalone NEGs. Standalone NEGs are deployed and managed through the NEG controller, but the forwarding rules, health checks, and other load balancing objects are deployed manually.

Standalone NEGs don't conflict with Ingress enabled container-native load balancing.

The following illustration shows the differences in how the load balancing objects are deployed in each scenario:

![With standalone NEGs and Ingress managed NEGs, the NEG controller on the
GKE control plane manages the NEG and Network endpoints objects. With standalone NEGs, every other component is
managed by the user as described in the previous paragraphs.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg2.svg)

By default, the GKE NEG controller creates standalone NEGs only in the zones where the cluster has nodes. To simplify load balancer setup, you can also pre-provision empty NEGs in specific zones (or all zones within a region) immediately after creating your Service, without waiting for workloads to be deployed. Support for pre-provisioning NEGs is in the [Preview](https://cloud.google.com/products#product-launch-stages) stage.

#### Preventing leaked NEGs

With standalone NEGs, you are responsible for managing the lifecycles of NEGs and the resources that make up the load balancer. You could leak NEGs in these ways:

  * When a GKE service is deleted, the associated NEG won't be garbage collected if the NEG is still referenced by a backend service. Dereference the NEG from the backend service to allow NEG deletion.
  * When a cluster is deleted, standalone NEGs won't be deleted in the following scenarios:

    * The NEG is still referenced by a backend service.
    * The cluster deletion process shuts down the NEG controller before the controller can delete the NEG.

To prevent leaked NEGs, dereference the NEG from the backend service and delete all NEGs before you delete the cluster.




If you have leaked NEGs after deleting the cluster or service, you can [delete the NEGs](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/delete) by using the Google Cloud CLI.

## Use cases of standalone NEGs

Standalone NEGs have several critical uses. Standalone NEGs are very flexible. This is in contrast to Ingress (used with or without NEGs) which defines a specific set of load balancing objects that were chosen in an opinionated way to make them straightforward to use.

Use cases for standalone NEGs include:

### Heterogeneous services of containers and VMs

NEGs can contain both VM and container IP addresses. This means a single virtual IP address can point to a backend that consists of both Kubernetes and non-Kubernetes workloads. This can also be used to migrate existing workloads to a GKE cluster.

Standalone NEGs can point to VM IPs which makes it possible to manually configure load balancers to point at backends that are comprised of both VMs and containers for the same service VIP.

### Customized Ingress controllers

You can use a customized Ingress controller (or no Ingress controller) to configure load balancers that target standalone NEGs.

### Use Cloud Service Mesh with GKE

You can use [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh) with GKE. Cloud Service Mesh uses standalone NEGs to provide container-native load balancing for the managed service mesh.

### Use external proxy Network Load Balancers with GKE

You can use standalone NEGs to load balance directly to containers with the [external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) which is not supported natively by Kubernetes/GKE.

## Pod readiness

[Readiness gates](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate) are an extensibility feature of Kubernetes that allow the injection of extra feedback or signals into the PodStatus to allow the Pod to transition to the Ready state. The NEG controller manages a custom readiness gate to help ensure that the full network path from Compute Engine load balancer to pod is functional. Pod readiness gates in GKE are explained in [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing#pod_readiness).

Ingress with NEGs deploys and manages Compute Engine health checks on behalf of the load balancer. However, standalone NEGs make no assumptions about Compute Engine health checks because they are expected to be deployed and managed separately. Compute Engine health checks should always be configured along with the load balancer to prevent traffic from being sent to backends which are not ready to receive. If there is no health check status associated with the NEG (usually because no health check is configured), then the NEG controller will mark the Pod's readiness gate value to True when its corresponding endpoint is programmed in NEG.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing VPC-native cluster. Your cluster must have the `HttpLoadBalancing` add-on enabled. New GKE clusters have the `HttpLoadBalancing` add-on enabled by default.

To create a new Standard cluster, see [Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). Autopilot clusters are VPC-native by default.




## Using standalone NEGs

The following instructions show you how to use standalone NEGs with an external HTTP load balancer on GKE.

You must create the following objects:

  * A [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) that creates and manages Pods.
  * A [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) that creates a NEG.
  * A load balancer created with the Compute Engine API. This differs from using NEGs with Ingress, in which case Ingress creates and configures a load balancer for you. With standalone NEGs you are responsible for associating the NEG and the backend service to connect the Pods to the load balancer. The load balancer consists of several components, shown in the following diagram:



![The components of a load balancer are a forwarding rule, target HTTP proxy,
URL map, health check, and backend service. This directs traffic to a NEG that
contains Pod IP addresses.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg3.svg)

### Create a Deployment

The following example manifests specify Deployments that run three instances of a containerized HTTP server. The HTTP server responds to requests with the hostname of the application server, the name of the Pod the server is running on.

We recommend you use workloads that use Pod readiness feedback.

### Using Pod readiness feedback
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: neg-demo-app # Label for the Deployment
      name: neg-demo-app # Name of Deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          run: neg-demo-app
      template: # Pod template
        metadata:
          labels:
            run: neg-demo-app # Labels Pods from this Deployment
        spec: # Pod specification; each Pod created by this Deployment has this specification
          containers:
          - image: registry.k8s.io/e2e-test-images/agnhost:2.40 # Application to run in Deployment's Pods
            name: hostname
            args:
            - serve-hostname
            - --port=9376
      

### Using hardcoded delay
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: neg-demo-app # Label for the Deployment
      name: neg-demo-app # Name of Deployment
    spec:
      minReadySeconds: 60 # Number of seconds to wait after a Pod is created and its status is Ready
      replicas: 3
      selector:
        matchLabels:
          run: neg-demo-app
      template: # Pod template
        metadata:
          labels:
            run: neg-demo-app # Labels Pods from this Deployment
        spec: # Pod specification; each Pod created by this Deployment has this specification
          containers:
          - image: registry.k8s.io/e2e-test-images/agnhost:2.40 # Application to run in Deployment's Pods
            name: hostname
            args:
            - serve-hostname
            - --port=9376
      

Save this manifest as `neg-demo-app.yaml`, then create the Deployment by running the following command:
    
    
    kubectl apply -f neg-demo-app.yaml
    

### Create a Service

The following manifest specifies a Service where:

  * Any Pod with the label `run: neg-demo-app` is a member of this Service.
  * The Service has one [ServicePort](https://v1-25.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#serviceport-v1-core) field with port 80.
  * The `cloud.google.com/neg` annotation specifies that port 80 will be associated with a NEG. The optional `name` field specifies that the NEG will be named `NEG_NAME`. If the `name` field is omitted, a unique name will be automatically generated. See naming NEGs for details.
  * Each member Pod must have a container that is listening on TCP port 9376.


    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: neg-demo-svc
      annotations:
        cloud.google.com/neg: '{"exposed_ports": {"80":{"name": "NEG_NAME"}}}'
    spec:
      type: ClusterIP
      selector:
        run: neg-demo-app # Selects Pods labelled run: neg-demo-app
      ports:
      - port: 80
        protocol: TCP
        targetPort: 9376
    

Replace `NEG_NAME` with the name for the NEG. The NEG name must be unique in its region.

Save this manifest as `neg-demo-svc.yaml`, then create the Service by running the following command:
    
    
    kubectl apply -f neg-demo-svc.yaml
    

A NEG is created within a few minutes of Service creation.

#### Service types

While this example uses a `ClusterIP` service, all five [types of Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#types_of_services) support standalone NEGs. We recommend the default type, `ClusterIP`.

#### Naming NEGs

In GKE versions 1.18.18-gke.1200 and later, you can specify a custom name for NEGs, or GKE can generate a name automatically. Previous versions of GKE only support automatically generated NEG names.

GKE creates one NEG in each zone used by the cluster. The NEGs all use the same name.

##### Specifying a name

Specifying a custom NEG name simplifies configuring the load balancer because you know the name and zone(s) of the NEG(s) in advance. Custom NEG names must meet the following requirements:

  * Be unique to the cluster's zone for zonal clusters, or unique to the region for regional clusters.

  * Must not match the name of any existing NEG that was not created by the GKE NEG controller.

  * Must not contain underscores.


**Note:** When there's a name conflict, NEG creation or syncing fails. For troubleshooting steps, see NEG is not synced with Service.

Use the `name` field in the `cloud.google.com/neg` annotation of the Service to specify a NEG name:
    
    
    cloud.google.com/neg: '{"exposed_ports": {"80":{"name": "NEG_NAME"}}}'
    

Replace `NEG_NAME` with the name for the NEG. The NEG name must be unique in its region.

##### Using an automatically generated name

Automatically generated NEG names are guaranteed to be unique. To use an automatically generated name, omit the `name` field:
    
    
    cloud.google.com/neg: '{"exposed_ports": {"80":{}}}'
    

The automatically generated name has the following format:

`k8s1-CLUSTER_UID-NAMESPACE-SERVICE-PORT-RANDOM_HASH`

#### Mapping ports to multiple NEGs

A Service can listen on more than one port. By definition, NEGs have only a single IP address and port. This means that if you specify a Service with multiple ports, it will create a NEG for each port.

The format of the `cloud.google.com/neg` annotation is:
    
    
    cloud.google.com/neg: '{
       "exposed_ports":{
          "SERVICE_PORT_1":{},
          "SERVICE_PORT_2":{},
          "SERVICE_PORT_3":{},
          ...
       }
     }'
    

In this example, each instance of `SERVICE_PORT_N` is a distinct port number that refers to existing service ports of the Service. For each service port listed, the NEG controller creates one NEG in each zone the cluster occupies.

#### Pre-provisioning empty NEGs

By default, the GKE NEG controller creates a standalone NEG only in the zones where the cluster has nodes. If a cluster scales up and adds nodes in a new zone, the controller automatically creates the corresponding NEGs. To attach empty NEGs to a backend service immediately after setting up a Kubernetes Service—without waiting for nodes to scale into those zones—pre-provision empty NEGs (Preview). Pre-provisioning NEGs simplifies load balancer configuration since traffic routing begins automatically when workloads eventually scale into those new zones.

To enable pre-provisioning, extend the `cloud.google.com/neg` annotation on your Kubernetes Service with the optional `zones` field, for example:
    
    
    cloud.google.com/neg: '{"exposed_ports": {"80":{}}, "zones":["us-central1-a", "us-central1-b"]}'
    

If you specify multiple ports under `exposed_ports`, the configured zones setting applies to the NEGs created for all of those ports.

The `zones` field accepts a list of string values. You can configure the `zones` field in the following ways:

  * **Omitted or empty list:** if the `zones` field is missing or set to `[]`, the controller uses the default behavior:

    * NEGs are created only in zones where the cluster has nodes.
    * Any unused NEGs are marked as `INACTIVE`.
  * **Wildcard`["*"]`:** this option creates empty NEGs across **all zones within the region** where the GKE cluster is located. This behavior applies to both regional and zonal clusters (for a zonal cluster, GKE creates empty NEGs in all other zones of the region).

  * **Explicit list of zones:** this option creates NEGs in the specified zones (for example, `["us-central1-a", "us-central1-b"]`), as well as any other zones where the cluster has nodes.




##### Requirements and limitations

  * Your cluster must use GKE version 1.36.2-gke.3104000 or later.
  * Any zones listed in the `zones` field must reside within the same region as your cluster.
  * If you configure the `zones` field with an incorrect format, the controller falls back to standard behavior and raises a `Warning` event on the Service object.
  * Empty NEGs count against your regional project quotas. Using wildcard configurations across multiple services might exhaust your limits.
  * When you use the wildcard (`["*"]`) option to configure the `zones` field, newly created zones in a region might take significant time to propagate for NEG pre-provisioning. If your workloads depend on new zones, specify those zones explicitly in the annotation.



#### Retrieve NEG statuses

Use the following command to retrieve the statuses of the cluster's Services:
    
    
    kubectl get service neg-demo-svc -o yaml
    

The output is similar to the following:
    
    
    cloud.google.com/neg-status: '{
       "network-endpoint-groups":{
          "SERVICE_PORT_1": "NEG_NAME_1",
          "SERVICE_PORT_2": "NEG_NAME_2",
          ...
       },
       "zones":["ZONE_1", "ZONE_2", ...]
    }
    

In this output, each element in the `network-endpoint-groups` mapping is a service port (like `SERVICE_PORT_1`) and the name of the corresponding managed NEGs (like `NEG_NAME_1`). The `zones` list contains every zone (like `ZONE_1`) that has a NEG in it.

The output is similar to the following:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        cloud.google.com/neg: '{"exposed_ports": {"80":{}}}'
        cloud.google.com/neg-status: '{"network_endpoint_groups":{"80":"k8s1-cca197ad-default-neg-demo-app-80-4db81e02"},"zones":["ZONE_1", "ZONE_2"]}'
      labels:
        run: neg-demo-app
      name: neg-demo-app
      namespace: default
      selfLink: /api/v1/namespaces/default/services/neg-demo-app
      ...
    spec:
      clusterIP: 10.0.14.252
      ports:
      - port: 80
        protocol: TCP
        targetPort: 9376
      selector:
        run: neg-demo-app
      sessionAffinity: None
    status:
      loadBalancer: {}
    

In this example, the annotation shows that service port 80 is exposed to NEGs named `k8s1-cca197ad-default-neg-demo-app-80-4db81e02`.

#### Validate NEG creation

A NEG is created within a few minutes of Service creation. If there are Pods that match the label specified in the Service manifest, then upon creation the NEG will contain the IPs of the Pods.

There are two ways to verify that the NEG is created and is correctly configured. In GKE 1.18.6-gke.6400 and later, a custom resource `ServiceNetworkEndpointGroup` stores status information about NEGs created by the Service controller. In previous versions, you must inspect the NEGs directly.

##### The `ServiceNetworkEndpointGroup` resource

List the NEGs in a cluster by getting all of the `ServiceNetworkEndpointGroup` resources:
    
    
    kubectl get svcneg
    

Observe the status of a NEG by checking the status of the `ServiceNetworkEndpointGroup` resource:
    
    
    kubectl get svcneg NEG_NAME -o yaml
    

Replace `NEG_NAME` with the name of the individual NEG you want to inspect.

The output of this command includes a status section that might contain error messages. If you have pre-provisioned NEGs, the output displays these NEGs in states of `ACTIVE` even if there are no Pods running in those zones yet.

Some errors are reported as a Service event. You can find further details by querying the Service object:
    
    
    kubectl describe service SERVICE_NAME
    

Replace `SERVICE_NAME` with the name of the relevant Service.

To verify that the NEG controller is successfully syncing the NEG, check the status field of the `ServiceNetworkEndpointGroup` resource for a condition with `type:Synced`. The time of the most recent sync is in the `status.lastSyncTime` field.

`ServiceNetworkEndpointGroup` resources only exist in GKE version 1.18 and later.

##### Inspecting NEGs directly

Verify that the NEG exists by listing the NEGs in your Google Cloud project and checking for a NEG that matches the Service you created. The NEG's name has the following format:

`k8s1-CLUSTER_UID-NAMESPACE-SERVICE-PORT-RANDOM_HASH`

Use the following command to list NEGs:
    
    
    gcloud compute network-endpoint-groups list
    

The output is similar to the following:
    
    
    NAME                                          LOCATION       ENDPOINT_TYPE   SIZE
    k8s1-70aa83a6-default-my-service-80-c9710a6f  ZONE_NAME      GCE_VM_IP_PORT  3
    

This output shows that the `SIZE` of the NEG is 3, meaning that it has three endpoints which correspond to the three Pods in the Deployment.

Identify the individual endpoints with the following command:
    
    
    gcloud compute network-endpoint-groups list-network-endpoints NEG_NAME
    

Replace `NEG_NAME` with the name of the NEG for which you want to display the individual endpoints.

The output shows three endpoints, each of which has a Pod's IP address and port:
    
    
    INSTANCE                                           IP_ADDRESS  PORT
    gke-cluster-3-default-pool-4cc71a15-qlpf  10.12.1.43  9376
    gke-cluster-3-default-pool-4cc71a15-qlpf  10.12.1.44  9376
    gke-cluster-3-default-pool-4cc71a15-w9nk  10.12.2.26  9376
    

## Attaching an external Application Load Balancer to standalone NEGs

You can use NEGs as a backend for an external Application Load Balancer using the Compute Engine API.

  1. Create a firewall rule. Load balancers need to access cluster endpoints to perform health checks. This command creates a firewall rule to allow access:
         
         gcloud compute firewall-rules create fw-allow-health-check-and-proxy \
            --network=NETWORK_NAME \
            --action=allow \
            --direction=ingress \
            --target-tags=GKE_NODE_NETWORK_TAGS \
            --source-ranges=130.211.0.0/22,35.191.0.0/16 \
            --rules=tcp:9376
         

Replace the following:

     * `NETWORK_NAME`: the network where the cluster runs.
     * `GKE_NODE_NETWORK_TAGS`: the [networking tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) on the GKE nodes.

If you did not create custom network tags for your nodes, GKE automatically generates tags for you. You can look up these generated tags by running the following command:
    
    gcloud compute instances describe INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of the host Compute Engine VM instance running the GKE node. For example, the output in the previous section displays the instance names in the `INSTANCE` column for the GKE nodes.

For Standard clusters, you can also run `gcloud compute instances list` to list all instances in your project.

  2. Create a global virtual IP address for the load balancer:
         
         gcloud compute addresses create hostname-server-vip \
             --ip-version=IPV4 \
             --global
         

  3. Create a health check. This is used by the load balancer to detect the liveness of individual endpoints within the NEG.
         
         gcloud compute health-checks create http http-basic-check \
             --use-serving-port
         

  4. Create a [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) that specifies that this is a global external Application Load Balancer:
         
         gcloud compute backend-services create my-bes \
             --protocol HTTP \
             --health-checks http-basic-check \
             --global
         

  5. Create a [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) and [target proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies) for the load balancer. This example is very straightforward because the `serve_hostname` app used for this guide has a single endpoint and does not feature URLs.
         
         gcloud compute url-maps create web-map \
             --default-service my-bes
         
         
         gcloud compute target-http-proxies create http-lb-proxy \
             --url-map web-map
         

  6. Create a [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). This is what creates the load balancer.
         
         gcloud compute forwarding-rules create http-forwarding-rule \
             --address=HOSTNAME_SERVER_VIP \
             --global \
             --target-http-proxy=http-lb-proxy \
             --ports=80
         

Replace `HOSTNAME_SERVER_VIP` with the IP address to use for the load balancer. If you omit `--address`, GKE automatically assigns an ephemeral IP address.

You can also [reserve a new static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).




### Checkpoint

These are the resources you have created so far:

  * An external virtual IP address
  * The forwarding rules
  * The firewall rules
  * The target HTTP proxy
  * The URL map the Compute Engine health check
  * The backend service
  * The Compute Engine health check



The relationship between these resources is shown in the following diagram:

![Relationship between the resources you've created.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg7.svg)

These resources together are a load balancer. In the next step you will add backends to the load balancer.

One of the benefits of standalone NEGs demonstrated here is that the lifecycles of the load balancer and backend can be completely independent. The load balancer can continue running after the application, its services, or the GKE cluster is deleted. You can add and remove new NEGs or multiple NEGs from the load balancer without changing any of the frontend load balancer objects.

### Add backends to the load balancer

Use [`gcloud compute backend-services add-backend`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) to connect the NEG to the load balancer by adding it as a backend of the `my-bes` backend service:
    
    
    gcloud compute backend-services add-backend my-bes \
        --global \
        --network-endpoint-group=NEG_NAME \
        --network-endpoint-group-zone=NEG_ZONE \
        --balancing-mode RATE --max-rate-per-endpoint 5
    

Replace the following:

  * `NEG_NAME`: the name of your network endpoint group. The name is either the name you specified when creating the NEG or an autogenerated name. If you did not specify a name for the NEG, see the following instructions to find the autogenerated name.
  * `NEG_ZONE`: the zone your network endpoint group is in. See the following instructions to find this value.



Use this command to get the name and location of the NEG:
    
    
    gcloud compute network-endpoint-groups list
    

The output is similar to the following:
    
    
    NAME                                          LOCATION       ENDPOINT_TYPE   SIZE
    k8s1-70aa83a6-default-my-service-80-c9710a6f  ZONE_NAME      GCE_VM_IP_PORT  3
    

In this example output, the name of the NEG is `k8s1-70aa83a6-default-my-service-80-c9710a6f`.

Multiple NEGs can be added to the same backend service. Global backend services like `my-bes` can have NEG backends in different regions, while regional backend services must have backends in a single region.

### Validate that the load balancer works

**Note:** It may take a few minutes for the load balancer to provision and stabilize.

There are two ways to validate that the load balancer you set up is working:

  * Verify that the health check is correctly configured and reporting healthy.
  * Access the application and verify its response.



### Verify health checks

Check that the backend service is associated with the health check and network endpoint groups, and that the individual endpoints are healthy.

Use this command to check that the backend service is associated with your health check and your network endpoint group:
    
    
    gcloud compute backend-services describe my-bes --global
    

The output is similar to the following:
    
    
    backends:
    - balancingMode: RATE
      capacityScaler: 1.0
      group: ... /networkEndpointGroups/k8s1-70aa83a6-default-my-service-80-c9710a6f
    ...
    healthChecks:
    - ... /healthChecks/http-basic-check
    ...
    name: my-bes
    ...
    

Next, check the health of the individual endpoints:
    
    
    gcloud compute backend-services get-health my-bes --global
    

The `status:` section of the output is similar to the following:
    
    
    status:
      healthStatus:
      - healthState: HEALTHY
        instance: ... gke-cluster-3-default-pool-4cc71a15-qlpf
        ipAddress: 10.12.1.43
        port: 50000
      - healthState: HEALTHY
        instance: ... gke-cluster-3-default-pool-4cc71a15-qlpf
        ipAddress: 10.12.1.44
        port: 50000
      - healthState: HEALTHY
        instance: ... gke-cluster-3-default-pool-4cc71a15-w9nk
        ipAddress: 10.12.2.26
        port: 50000
    

### Access the application

Access the application through the load balancer's IP address to confirm that everything is working.

**Note:** It takes a few minutes for the load balancer to be fully programmed.

First, get the virtual IP address of the load balancer:
    
    
    gcloud compute addresses describe hostname-server-vip --global | grep "address:"
    

The output will include an IP address. Next, send a request to that IP address (`34.98.102.37` in this example):
    
    
    curl 34.98.102.37
    

The response from the `serve_hostname` app should be `neg-demo-app`.

## Attaching an internal Application Load Balancer to standalone NEGs

You can use NEGs to configure an internal Application Load Balancer for your services running in standalone GKE Pods.

### Configuring the proxy-only subnet

The [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) is for all regional internal Application Load Balancers in the load balancer's region.

**Important:** Don't try to assign addresses from the proxy-only subnet to your load balancer's forwarding rule or backends. You assign the forwarding rule's IP address and the backend instance IP addresses from a different subnet range (or ranges) from the proxy-only subnet. Google Cloud reserves the subnet range for Google Cloud-managed proxies.

###  Console 

If you're using the Google Cloud console, you can wait and create the proxy-only subnet later.

###  gcloud 

Create the proxy-only subnet with the [gcloud compute networks subnets create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command.
    
    
    gcloud compute networks subnets create proxy-only-subnet \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=COMPUTE_REGION \
        --network=lb-network \
        --range=10.129.0.0/23
    

Replace `COMPUTE_REGION` with the [Compute Engine](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the subnet.

###  API 

Create the proxy-only subnet with the [`subnetworks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert) method.
    
    
    POST https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/COMPUTE_REGION/subnetworks
    
    
    
    {
      "name": "proxy-only-subnet",
      "ipCidrRange": "10.129.0.0/23",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "region": "projects/PROJECT_ID/regions/COMPUTE_REGION",
      "purpose": "REGIONAL_MANAGED_PROXY",
      "role": "ACTIVE"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `COMPUTE_REGION`: the [Compute Engine](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the subnet.



### Configuring firewall rules

This example uses the following firewall rules:

  * `fw-allow-ssh`: An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port 22 from any address. You can choose a more restrictive source IP range for this rule. For example, you can specify just the IP ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which the firewall rule applies.

  * `fw-allow-health-check`: An ingress rule, applicable to the instances being load balanced, that allows all TCP traffic from the Google Cloud health checking systems (in `130.211.0.0/22` and `35.191.0.0/16`). This example uses the target tag `load-balanced-backend` to identify the instances to which it should apply.

  * `fw-allow-proxies`: An ingress rule, applicable to the instances being load balanced, that allows TCP traffic on port `9376` from the internal HTTP(S) load balancer's managed proxies. This example uses the target tag `load-balanced-backend` to identify the instances to which it should apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

###  Console 

  1. Go to the **Firewall policies** page in the Google Cloud console.

[Go to **Firewall policies**](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** add_box to create the rule to allow incoming SSH connections:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-ssh`
     * **Source filter** : `IPv4 ranges`
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : 
       * Select **Specified protocols and ports**.
       * Select the `tcp` checkbox and specify port `22`.
  3. Click **Create**.

  4. Click **Create firewall rule** add_box again to create the rule to allow Google Cloud health checks:

     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : `IPv4 ranges`
     * **Source IPv4 ranges** : `130.211.0.0/22` and `35.191.0.0/16`
     * **Protocols and ports** : 
       * Select **Specified protocols and ports**
       * Select the `tcp` checkbox and specify port `80`. As a best practice, limit this rule to just the protocols and ports that match those used by your health check. If you use `tcp:80` for the protocol and port, Google Cloud can contact your VMs using HTTP on port 80, but it cannot contact them using HTTPS on port 443.
  5. Click **Create**.

  6. Click **Create firewall rule** add_box again to create the rule to allow the load balancer's proxy servers to connect the backends:

     * **Name** : `fw-allow-proxies`
     * **Network** : `lb-network`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : `IPv4 ranges`
     * **Source IPv4 ranges** : `10.129.0.0/23`
     * **Protocols and ports** : 
       * Select **Specified protocols and ports**.
       * Select the `tcp` checkbox and specify port `9376`.
  7. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  2. Create the `fw-allow-health-check` rule to allow Google Cloud health checks. This example allows all TCP traffic from health check probers; however, you can configure a narrower set of ports to meet your needs.
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=130.211.0.0/22,35.191.0.0/16 \
             --target-tags=load-balanced-backend \
             --rules=tcp
         

  3. Create the `fw-allow-proxies` rule to allow the internal HTTP(S) load balancer's proxies to connect to your backends.
         
         gcloud compute firewall-rules create fw-allow-proxies \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.129.0.0/23 \
             --target-tags=load-balanced-backend \
             --rules=tcp:9376
         




###  API 

Create the `fw-allow-ssh` firewall rule by making a `POST` request to the [`firewalls.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    
    
    {
      "name": "fw-allow-ssh",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "sourceRanges": [
        "0.0.0.0/0"
      ],
      "targetTags": [
        "allow-ssh"
      ],
      "allowed": [
       {
         "IPProtocol": "tcp",
         "ports": [
           "22"
         ]
       }
      ],
     "direction": "INGRESS"
    }
    

Replace `PROJECT_ID` with your project ID.

Create the `fw-allow-health-check` firewall rule by making a `POST` request to the [`firewalls.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    
    
    {
      "name": "fw-allow-health-check",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "sourceRanges": [
        "130.211.0.0/22",
        "35.191.0.0/16"
      ],
      "targetTags": [
        "load-balanced-backend"
      ],
      "allowed": [
        {
          "IPProtocol": "tcp"
        }
      ],
      "direction": "INGRESS"
    }
    

Create the `fw-allow-proxies` firewall rule to allow TCP traffic within the proxy subnet the [`firewalls.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    
    
    {
      "name": "fw-allow-proxies",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "sourceRanges": [
        "10.129.0.0/23"
      ],
      "targetTags": [
        "load-balanced-backend"
      ],
      "allowed": [
        {
          "IPProtocol": "tcp",
          "ports": [
            "9376"
          ]
        }
      ],
      "direction": "INGRESS"
    }
    

Replace `PROJECT_ID` with your project ID.

### Configuring the load balancer

For the forwarding rule's IP address, use a backend subnet. If you try to use the proxy-only subnet, forwarding rule creation fails.

###  Console 

### Select a load balancer type

  1. Go to the **Create a load balancer** page in the Google Cloud console. [Go to **Create a load balancer**](https://console.cloud.google.com/networking/loadbalancing/add)
  2. Under **HTTP(S) Load Balancing** , click **Start configuration**.
  3. Select _Only between my VMs_. This setting means that the load balancer is internal.
  4. Click **Continue**.



### Prepare the load balancer

  1. For the **Name** of the load balancer, enter `l7-ilb-gke-map`.
  2. For the **Region** , select the region where you created the subnet.
  3. For the **Network** , select `lb-network`.



### Reserve a proxy-only subnet

**Note:** If you've already reserved a proxy-only subnet, as instructed, the **Reserve a Subnet** button isn't displayed, so you skip this section and continue with the steps in Configure the backend service.

Reserve a proxy-only subnet:

  1. Click **Reserve a Subnet**.
  2. For the **Name** , enter `proxy-only-subnet`.
  3. For the **IP address range** , enter `10.129.0.0/23`.
  4. Click **Add**.



### Configure the backend service

  1. Click **Backend configuration**.
  2. From the **Create or select backend services** menu, select **Create a backend service**.
  3. Set the **Name** of the backend service to `l7-ilb-gke-backend-service`.
  4. For **Backend type** , select **Network endpoint groups**.
  5. In the **New backend** card of the **Backends** section: 
     1. Set the **Network endpoint group** to the NEG was created by GKE. To get the NEG name, see Validate NEG creation.
     2. For **Maximum RPS** , specify a maximum rate of `5` RPS per endpoint. Google Cloud will exceed this maximum if necessary.
     3. Click **Done**.
  6. From the **Health check** drop-down list, select **Create a health check** and then specify the following parameters: 
     1. **Name** : `l7-ilb-gke-basic-check`
     2. **Protocol** : HTTP
     3. **Port specification** : _Serving port_
     4. Click **Save and Continue**.
  7. Click **Create**.



### Configure the URL map

  1. Click **Routing rules**. Ensure that the _l7-ilb-gke-backend-service_ is the only backend service for any unmatched host and any unmatched path.



### Configure the frontend

Click **Frontend configuration** and perform the following steps:

**For HTTP:**

  1. Click **Frontend configuration**.
  2. Click **Add frontend IP and port**.
  3. Set the **Name** to _l7-ilb-gke-forwarding-rule_.
  4. Set the **Protocol** to _HTTP_.
  5. Set the **Subnetwork** the name of your cluster's subnet.
  6. Under **Internal IP** , select _Reserve a static internal IP address_.
  7. In the panel that appears provide the following details: 
     1. **Name** : `l7-ilb-gke-ip`
     2. In the **Static IP address** section, select _Let me choose_.
     3. In the **Custom IP address** section, enter `10.1.2.199`.
     4. Click **Reserve**.
  8. Set the **Port** to `80`.
  9. Click **Done**.



**For HTTPS:**

If you are using HTTPS between the client and the load balancer, you need one or more SSL certificate resources to configure the proxy. See [SSL Certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) for information on how to create SSL certificate resources. Google-managed certificates aren't supported with internal HTTP(S) load balancers.

  1. Click **Frontend configuration**.
  2. Click **Add frontend IP and port**.
  3. In the **Name** field, enter `l7-ilb-gke-forwarding-rule`.
  4. In the **Protocol** field, select `HTTPS (includes HTTP/2)`.
  5. Set the **Subnet** the name of your cluster's subnet.
  6. Under **Internal IP** , select _Reserve a static internal IP address_.
  7. In the panel that appears provide the following details: 
     1. **Name** : `l7-ilb-gke-ip`
     2. In the **Static IP address** section, select _Let me choose_.
     3. In the **Custom IP address** section, enter `10.1.2.199`.
     4. Click **Reserve**.
  8. Ensure that the **Port** is set to `443`, to allow HTTPS traffic.
  9. Click the **Certificate** drop-down list. 
     1. If you already have a [self-managed SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types) you want to use as the primary SSL certificate, select it from the drop-down menu.
     2. Otherwise, select **Create a new certificate**. 
        1. Fill in a **Name** of `l7-ilb-cert`.
        2. In the appropriate fields upload your PEM-formatted files: 
           * **Public key certificate**
           * **Certificate chain**
           * **Private key**
        3. Click **Create**.
  10. To add certificate resources in addition to the primary SSL certificate resource: 
     1. Click **Add certificate**.
     2. Select a certificate from the **Certificates** list or click **Create a new certificate** and follow the instructions.
  11. Click **Done**.



### Complete the configuration

Click **Create**.

###  gcloud 

  1. Define the HTTP health check with the [gcloud compute health-checks create http](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http) command.
         
         gcloud compute health-checks create http l7-ilb-gke-basic-check \
             --region=COMPUTE_REGION \
             --use-serving-port
         

  2. Define the backend service with the [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) command.
         
         gcloud compute backend-services create l7-ilb-gke-backend-service \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=HTTP \
             --health-checks=l7-ilb-gke-basic-check \
             --health-checks-region=COMPUTE_REGION \
             --region=COMPUTE_REGION
         

  3. Set the `DEPLOYMENT_NAME` variable:
         
         export DEPLOYMENT_NAME=NEG_NAME
         

Replace `NEG_NAME` with the name of the NEG.

  4. Add NEG backends to the backend service with the [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) command.
         
         gcloud compute backend-services add-backend l7-ilb-gke-backend-service \
             --network-endpoint-group=$DEPLOYMENT_NAME \
             --network-endpoint-group-zone=COMPUTE_ZONE-b \
             --region=COMPUTE_REGION \
             --balancing-mode=RATE \
             --max-rate-per-endpoint=5
         

  5. Create the URL map with the [gcloud compute url-maps create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create) command.
         
         gcloud compute url-maps create l7-ilb-gke-map \
             --default-service=l7-ilb-gke-backend-service \
             --region=COMPUTE_REGION
         

  6. Create the target proxy.

**For HTTP:**

Use the [gcloud compute target-http-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create) command.
         
         gcloud compute target-http-proxies create l7-ilb-gke-proxy \
             --url-map=l7-ilb-gke-map \
             --url-map-region=COMPUTE_REGION \
             --region=COMPUTE_REGION
         

**For HTTPS:**

See [SSL Certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) for information on how to create SSL certificate resources. Google-managed certificates aren't supported with internal HTTP(S) load balancers.

Assign your filepaths to variable names.
         
         export LB_CERT=PATH_TO_PEM_FORMATTED_FILE
         
         
         export LB_PRIVATE_KEY=PATH_TO_PEM_FORMATTED_FILE
         

Create a regional SSL certificate using the [gcloud compute ssl-certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command.

[gcloud compute ssl-certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create)
         
         gcloud compute ssl-certificates create l7-ilb-cert \
             --certificate=$LB_CERT \
             --private-key=$LB_PRIVATE_KEY \
             --region=COMPUTE_REGION
         

Use the regional SSL certificate to create a target proxy with the [gcloud compute target-https-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create) command.
         
         gcloud compute target-https-proxies create l7-ilb-gke-proxy \
             --url-map=l7-ilb-gke-map \
             --region=COMPUTE_REGION \
             --ssl-certificates=l7-ilb-cert
         

  7. Create the forwarding rule.

For custom networks, you must reference the subnet in the forwarding rule. Note that this is the VM subnet, not the proxy subnet.

**For HTTP:**

Use the [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command with the correct flags.
         
         gcloud compute forwarding-rules create l7-ilb-gke-forwarding-rule \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=SUBNET_NAME \
             --address=10.1.2.199 \
             --ports=80 \
             --region=COMPUTE_REGION \
             --target-http-proxy=l7-ilb-gke-proxy \
             --target-http-proxy-region=COMPUTE_REGION
         

**For HTTPS:**

Use the [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command with the correct flags.
         
         gcloud compute forwarding-rules create l7-ilb-gke-forwarding-rule \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=SUBNET_NAME  \
             --address=10.1.2.199 \
             --ports=443 \
             --region=COMPUTE_REGION \
             --target-https-proxy=l7-ilb-gke-proxy \
             --target-https-proxy-region=COMPUTE_REGION
         

Replace `SUBNET_NAME` with the name of your cluster's subnet.




###  API 

Create the health check by making a `POST` request to the [`regionHealthChecks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/COMPUTE_REGION/healthChecks
    
    
    
    {
       "name": "l7-ilb-gke-basic-check",
       "type": "HTTP",
       "httpHealthCheck": {
         "portSpecification": "USE_SERVING_PORT"
       }
    }
    

Replace `PROJECT_ID` with the project ID.

Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/COMPUTE_REGION/backendServices
    
    
    
    {
      "name": "l7-ilb-gke-backend-service",
      "backends": [
        {
          "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/COMPUTE_ZONE/networkEndpointGroups/NEG_NAME",
          "balancingMode": "RATE",
          "maxRatePerEndpoint": 5
        }
      ],
      "healthChecks": [
        "projects/PROJECT_ID/regions/COMPUTE_REGION/healthChecks/l7-ilb-gke-basic-check"
      ],
      "loadBalancingScheme": "INTERNAL_MANAGED"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `NEG_NAME`: the name of the NEG.



Create the URL map by making a `POST` request to the [`regionUrlMaps.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/COMPUTE_REGION/urlMaps
    
    
    
    {
      "name": "l7-ilb-gke-map",
      "defaultService": "projects/PROJECT_ID/regions/COMPUTE_REGION/backendServices/l7-ilb-gke-backend-service"
    }
    

Replace `PROJECT_ID` with the project ID.

Create the target HTTP proxy by making a `POST` request to the [`regionTargetHttpProxies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpProxies/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/COMPUTE_REGION/targetHttpProxy
    
    
    
    {
      "name": "l7-ilb-gke-proxy",
      "urlMap": "projects/PROJECT_ID/global/urlMaps/l7-ilb-gke-map",
      "region": "COMPUTE_REGION"
    }
    

Replace `PROJECT_ID` with the project ID.

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/COMPUTE_REGION/forwardingRules
    
    
    
    {
      "name": "l7-ilb-gke-forwarding-rule",
      "IPAddress": "10.1.2.199",
      "IPProtocol": "TCP",
      "portRange": "80-80",
      "target": "projects/PROJECT_ID/regions/COMPUTE_REGION/targetHttpProxies/l7-ilb-gke-proxy",
      "loadBalancingScheme": "INTERNAL_MANAGED",
      "subnetwork": "projects/PROJECT_ID/regions/COMPUTE_REGION/subnetworks/SUBNET_NAME",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "networkTier": "PREMIUM",
    }
    

Replace `PROJECT_ID` with the project ID.

### Testing

Create a VM instance in the zone to test connectivity:
    
    
    gcloud compute instances create l7-ilb-client \
        --image-family=debian-9 \
        --image-project=debian-cloud \
        --zone=COMPUTE_ZONE \
        --network=lb-network \
        --subnet=SUBNET_NAME \
        --tags=l7-ilb-client,allow-ssh
    

Sign in to the client instance to check that HTTP(S) services on the backends are reachable using the internal Application Load Balancer's forwarding rule IP address, and traffic is being load balanced among endpoints in the NEG.

Connect to each client instance using SSH:
    
    
    gcloud compute ssh l7-ilb-client \
        --zone=COMPUTE_ZONE-b
    

Verify that the IP is serving its hostname:
    
    
    curl 10.1.2.199
    

For HTTPS testing, run the following command:
    
    
    curl -k -s 'https://test.example.com:443' --connect-to test.example.com:443:10.1.2.199:443
    

The `-k` flag causes `curl` to skip certificate validation.

Run 100 requests and confirm that they are load balanced.

**For HTTP:**
    
    
    {
    RESULTS=
    for i in {1..100}
    do
        RESULTS="$RESULTS:$(curl --silent 10.1.2.199)"
    done
    echo "***"
    echo "*** Results of load-balancing to 10.1.2.199: "
    echo "***"
    echo "$RESULTS" | tr ':' '\n' | grep -Ev "^$" | sort | uniq -c
    echo
    }
    

**For HTTPS:**
    
    
    {
    RESULTS=
    for i in {1..100}
    do
        RESULTS="$RESULTS:$(curl -k -s 'https://test.example.com:443' --connect-to test.example.com:443:10.1.2.199:443
    )"
    done
    echo "***"
    echo "*** Results of load-balancing to 10.1.2.199: "
    echo "***"
    echo "$RESULTS" | tr ':' '\n' | grep -Ev "^$" | sort | uniq -c
    echo
    }
    

## Attach an external proxy Network Load Balancer to standalone NEGs

You can use standalone NEGs to load balance directly to containers with the [external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) which is not supported natively by Kubernetes or GKE. Proxy Network Load Balancers are intended for TCP traffic only, with or without SSL. For HTTP(S) traffic, we recommend that you use an Application Load Balancer instead.

  1. Create a firewall rule to allow health checks.

Load balancers need to access cluster endpoints to perform health checks. The following command creates a firewall rule to allow access:
         
         gcloud compute firewall-rules create allow-tcp-lb-and-health \
            --network=NETWORK_NAME \
            --target-tags=GKE_NODE_NETWORK_TAGS \
            --source-ranges=130.211.0.0/22,35.191.0.0/16 \
            --allow tcp:9376
         

Replace the following:

     * `NETWORK_NAME`: the network where the cluster runs.
     * `GKE_NODE_NETWORK_TAGS`: the [networking tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) on the GKE nodes.

If you didn't create custom network tags for your nodes, GKE automatically generates tags for you. You can look up these generated tags by running the following command:
    
    gcloud compute instances describe INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of the host Compute Engine VM instance running the GKE node. For example, the output in the Inspect NEGs directly section displays the instance names in the `INSTANCE` column for the GKE nodes.

For Standard clusters, you can also run the `gcloud compute instances list` to list all instances in your project.

For Autopilot clusters, target the cluster service account instead of network tags.

Replace the `--target-tags=GKE_NODE_NETWORK_TAGS` flag with `--target-service-accounts=SERVICE_ACCOUNT_EMAIL`. We recommended that you use a custom [minimally-privileged](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#minimum_permissions) service account for the cluster.

  2. Create a global virtual IP address for the load balancer:
         
         gcloud compute addresses create tcp-lb-static-ipv4 \
            --ip-version=IPV4 \
            --global
         

  3. Define a health check for backend endpoints.

The load balancer uses health checks to detect the liveness of individual endpoints within the NEG.
         
         gcloud compute health-checks create tcp my-tcp-health-check \
            --use-serving-port
         

  4. Create a backend service with session affinity.

This [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) specifies that this is a external proxy Network Load Balancer with [`CLIENT_IP`](https://docs.cloud.google.com/load-balancing/docs/backend-service#client_ip_affinity) session affinity:
         
         gcloud compute backend-services create my-tcp-lb \
            --load-balancing-scheme EXTERNAL_MANAGED \
            --global-health-checks \
            --global \
            --protocol TCP \
            --health-checks my-tcp-health-check \
            --timeout 5m \
            --session-affinity=CLIENT_IP
         

  5. Create a [target TCP proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies) for the load balancer.

If you want to turn on the [proxy header](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-tcp#proxy-protocol), set it to `PROXY_V1` instead of `NONE`.
         
         gcloud compute target-tcp-proxies create my-tcp-lb-target-proxy \
             --backend-service my-tcp-lb \
             --proxy-header NONE
         

  6. Create a [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) to route traffic.

This forwarding rule creates the load balancer.
         
         gcloud compute forwarding-rules create my-tcp-lb-ipv4-forwarding-rule \
             --load-balancing-scheme EXTERNAL_MANAGED \
             --global \
             --target-tcp-proxy my-tcp-lb-target-proxy \
             --address tcp-lb-static-ipv4 \
             --ports 80
         




### Verify load balancer resources creation

You have created the following resources:

  * An external virtual IP address
  * The forwarding rule
  * The firewall rule
  * The target proxy
  * The backend service
  * The Compute Engine health check



The external virtual IP address is connected to the forwarding rule, which directs traffic that is allowed by the firewall rule to the target proxy. The target proxy then communicates with the backend service, which is periodically checked by the health check. The relationship between these resources is shown in the following diagram:

![Relationship between the resources you've created.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg8.svg)

These resources together are a load balancer. In the next step, you will add backends to the load balancer.

One of the benefits of the standalone NEGs demonstrated here is that the lifecycles of the load balancer and backend can be completely independent. The load balancer can continue running after the application, its services, or the GKE cluster is deleted. You can add and remove new NEGs or multiple NEGs from the load balancer without changing any of the frontend load balancer objects.

### Add standalone NEGs as backends to the load balancer

Use [`gcloud compute backend-services add-backend`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) to connect the NEG to the load balancer by adding as a backend of the `my-tcp-lb` backend service:
    
    
    gcloud compute backend-services add-backend my-tcp-lb \
        --global \
        --network-endpoint-group=NEG_NAME \
        --network-endpoint-group-zone=NEG_ZONE \
        --balancing-mode CONNECTION \
        --max-connections 100
    

Replace the following:

  * `NEG_NAME`: the name of your network endpoint group. The name is either the name you specified when creating the NEG or an autogenerated name. If you did not specify a name for the NEG, see the following instructions to find the autogenerated name.
  * `NEG_ZONE`: the zone your network endpoint group is in. See the following instructions to find this value.



To get the name and location of the NEGs, use this command:
    
    
    gcloud compute network-endpoint-groups list
    

The output is similar to the following:
    
    
    NAME: k8s1-65a95e90-default-neg-demo-svc-80-663a85e4
    LOCATION: us-central1-a
    ENDPOINT_TYPE: GCE_VM_IP_PORT
    SIZE: 3
    

In this example output, the name of the NEG is `kk8s1-65a95e90-default-neg-demo-svc-80-663a85e4` and zone is `us-central1-a`.

Multiple NEGs can be added to the same backend service. Global backend services like `my-tcp-lb` can have NEG backends in different regions, while regional backend services must have backends in a single region.

### Verify the load balancer configuration and connectivity

**Note:** It might take a few minutes for the load balancer to provision and stabilize.

There are two ways to validate that the load balancer you set up is working:

  * Verify that the health check is correctly configured and is reporting as healthy.
  * Access the application and verify its response.



### Verify health checks

Check that the backend service is associated with the health check and network endpoint groups, and that the individual endpoints are healthy.

To check that the backend service is associated with your health check and your network endpoint group, use this command:
    
    
    gcloud compute backend-services describe my-tcp-lb --global
    

The output is similar to the following:
    
    
    backends:
    - balancingMode: CONNECTION
      group: ... /networkEndpointGroups/k8s1-65a95e90-default-neg-demo-svc-80-663a85e4
      maxConnections: 100
    ...
    healthChecks:
    - ... /healthChecks/my-tcp-health-check
    ...
    name: my-tcp-lb
    ...
    

Next, check the health of the individual endpoints:
    
    
    gcloud compute backend-services get-health my-tcp-lb --global
    

The `status:` section of the output is similar to the following:
    
    
    status:
      healthStatus:
      - healthState: HEALTHY
        instance: ... gke-cluster-3-default-pool-4cc71a15-qlpf
        ipAddress: 10.12.1.43
        port: 50000
      - healthState: HEALTHY
        instance: ... gke-cluster-3-default-pool-4cc71a15-qlpf
        ipAddress: 10.12.1.44
        port: 50000
      - healthState: HEALTHY
        instance: ... gke-cluster-3-default-pool-4cc71a15-w9nk
        ipAddress: 10.12.2.26
        port: 50000
    

### Verify application connectivity

To verify that the load balancer is functioning correctly, access the application through the external IP address of the load balancer.

**Note:** Allow several minutes for the load balancer to be fully programmed.

  1. **Get the external IP address of the load balancer:**

To retrieve the external IP address that you reserved for the load balancer, use the following command:
         
         gcloud compute addresses describe tcp-lb-static-ipv4 --global | grep "address:"
         

This command outputs the IP address.

  2. **Send a request to the IP address:**

Use the `curl` command to send a request to the external IP address.
         
         curl EXTERNAL_IP_ADDRESS
         

Replace `EXTERNAL_IP_ADDRESS` with the IP address that you obtained in the previous step:

The response from the `serve_hostname` application should begin with `neg-demo-app`.




## Implementing heterogeneous services (VMs and containers)

Load balancers can be frontends to mixed Kubernetes and non-Kubernetes workloads. This could be part of a migration from VMs to containers or a permanent architecture that benefits from a shared load balancer. This can be achieved by creating load balancers that target different kinds of backends including standalone NEGs.

### VMs and containers in the same backend service

This example shows how to create a NEG that points at an existing VM running a workload, and how to add this NEG as another backend of an existing `backendService`. This way a single load balancer balances between VMs and GKE containers.

This examples extends the previous example that uses an external HTTP load balancer.

Because all endpoints are grouped by the same `backendService`, the VM and container endpoints are considered the **same service**. This means the host or path matching will treat all backends identically based on the URL map rules.

![The described architecture. The load balancer created earlier points to two NEGs, the NEG for containers created earlier and a new NEG containing a VM's IP address.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg4.svg)

When you use a NEG as a backend for a backend service, all other backends in that backend service must also be NEGs. You can't use instance groups and NEGs as backends in the same backend service. Additionally, containers and VMs cannot exist as endpoints within the same NEG, so they must always be configured with separate NEGs.

  1. Deploy a VM to Compute Engine with this command:
         
         gcloud compute instances create vm1 \
             --zone=COMPUTE_ZONE \
             --network=NETWORK \
             --subnet=SUBNET \
             --image-project=cos-cloud \
             --image-family=cos-stable --tags=vm-neg-tag
         

Replace the following:

     * `COMPUTE_ZONE`: the name of the zone.
     * `NETWORK`: the name of the network.
     * `SUBNET`: the name of the subnet associated with the network.
  2. Deploy an application to the VM:
         
         gcloud compute ssh vm1 \
             --zone=COMPUTE_ZONE \
             --command="docker run -d --rm --network=host registry.k8s.io/e2e-test-images/agnhost:2.40 serve-hostname --port=9376 && sudo iptables -P INPUT ACCEPT"
         

This command deploys to the VM the same example application used in the earlier example. For simplicity, the application is run as a Docker container but this is not essential. The `iptables` command is required to allow firewall access to the running container.

  3. Validate that the application is serving on port 9376 and reporting that it is running on vm1:
         
         gcloud compute ssh vm1 \
             --zone=COMPUTE_ZONE \
             --command="curl -s localhost:9376"
         

The server should respond with `vm1`.

  4. Create a NEG to use with the VM endpoint. Containers and VMs can both be NEG endpoints, but a single NEG can't have both VM and container endpoints.
         
         gcloud compute network-endpoint-groups create vm-neg \
             --subnet=SUBNET \
             --zone=COMPUTE_ZONE
         

  5. Attach the VM endpoint to the NEG:
         
         gcloud compute network-endpoint-groups update vm-neg \
             --zone=COMPUTE_ZONE \
             --add-endpoint="instance=vm1,ip=VM_PRIMARY_IP,port=9376"
         

Replace `VM_PRIMARY_IP` with the VM's primary IP address.

  6. Confirm that the NEG has the VM endpoint:
         
         gcloud compute network-endpoint-groups list-network-endpoints vm-neg \
             --zone COMPUTE_ZONE
         

  7. Attach the NEG to the backend service using the same command that you used to add a container backend:
         
         gcloud compute backend-services add-backend my-bes
             --global \
             --network-endpoint-group vm-neg \
             --network-endpoint-group-zone COMPUTE_ZONE \
             --balancing-mode RATE --max-rate-per-endpoint 10
         

  8. Open firewall to allow the VM's health check:
         
         gcloud compute firewall-rules create fw-allow-health-check-to-vm1 \
             --network=NETWORK \
             --action=allow \
             --direction=ingress \
             --target-tags=vm-neg-tag \
             --source-ranges=130.211.0.0/22,35.191.0.0/16 \
             --rules=tcp:9376
         

  9. Validate that the load balancer is forwarding traffic to both the new vm1 backend and the existing container backend by sending test traffic:
         
         for i in `seq 1 100`; do curl ${VIP};echo; done
         

You should see responses from both the container (`neg-demo-app`) and VM (`vm1`) endpoints.




### VMs and containers for different backend services

This example shows how to create a NEG that points at an existing VM running a workload, and how to add this NEG as the backend to a new `backendService`. This is useful for the case where the containers and VMs are different services but need to share the same L7 load balancer, such as if the services share the same IP address or domain name.

This examples extends the previous example that has a VM backend in the same backend service as the container backend. This example reuses that VM.

Because the container and VM endpoints are grouped in separate backend services, they are considered **different services**. This means that the URL map will match backends and direct traffic to the VM or container based on the hostname.

The following diagram shows how a single virtual IP address corresponds to two host names, which in turn correspond to a container-based backend service and a VM-based backend service.

![A single virtual IP address mapping to two hostnames, one hostname for a container-based backend and one for a VM-based backend.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg5.svg)

The following diagram shows the architecture described in the previous section:

![The architecture has two NEGs, one for the service implemented with containers
and another for the service implemented with VMs. There is a backend service
object for each NEG. The URL Map object directs traffic to the correct backend
service based on the requested URL.](https://docs.cloud.google.com/static/kubernetes-engine/images/sneg6.svg)

  1. Create a new backend service for the VM:
         
         gcloud compute backend-services create my-vm-bes \
            --protocol HTTP \
            --health-checks http-basic-check \
            --global
         

  2. Attach the NEG for the VM, `vm-neg`, to the backend-service:
         
         gcloud compute backend-services add-backend my-vm-bes \
             --global \
             --network-endpoint-group vm-neg \
             --network-endpoint-group-zone COMPUTE_ZONE \
             --balancing-mode RATE --max-rate-per-endpoint 10
         

  3. Add a host rule to the [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) to direct requests for `container.example.com` host to the container backend service:
         
         gcloud compute url-maps add-path-matcher web-map \
             --path-matcher-name=container-path --default-service=my-bes \
             --new-hosts=container.example.com --global
         

  4. Add another host rule the URL map to direct requests for `vm.example.com` host to the VM backend service:
         
         gcloud compute url-maps add-path-matcher web-map \
             --path-matcher-name=vm-path --default-service=my-vm-bes \
             --new-hosts=vm.example.com --global
         

**Note:** It takes a few minutes for the load balancer to be fully programmed.
  5. Validate that the load balancer sends traffic to the VM backend based on the requested path:
         
         curl -H "HOST:vm.example.com" VIRTUAL_IP
         

Replace `VIRTUAL_IP` with the virtual IP address.




## Limitations of standalone NEGs

  * Annotation validation errors are exposed to the user through Kubernetes events.
  * The [limitations of NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing#limitations) also apply to standalone NEGs.
  * Standalone NEGs don't work with [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).
  * Standalone NEGs can only be used with compatible network services including [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh) and the [compatible load balancer types](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts).



## Pricing

Refer to the [load balancing section](https://docs.cloud.google.com/vpc/network-pricing#lb-pricing) of the pricing page for details on pricing of the load balancer. There is no additional charge for NEGs.

## Troubleshooting

This section provides troubleshooting steps for common issues that you might encounter with the standalone NEGs.

### No standalone NEG configured

**Symptom:** No NEG is created.

**Potential Resolution:**

  * Check the events associated with the Service and look for error messages.
  * Verify the standalone NEG annotation is well-formed JSON, and that the exposed ports match existing Ports in the Service spec.
  * Verify the NEG status annotation and see if expected service ports has corresponding NEGs.
  * Verify that the NEGs have been created in the expected zones, with the command `gcloud compute network-endpoint-groups list`.
  * If using GKE version 1.18 or later, check if the `svcneg` resource for the Service exists. If it does, check the `Initialized` condition for any error information.
  * If you are using custom NEG names, ensure that each NEG name in is unique in its region.



### Traffic does not reach the endpoints

**Symptom:** 502 errors or rejected connections.

**Potential Resolution:**

  * After the service is configured new endpoints will generally become reachable after attaching them to NEG, provided they respond to health checks.
  * If after this time traffic still can't reach the endpoints resulting in 502 error code for HTTP(S) or connections being rejected for TCP/SSL load balancers, check the following: 
    * Verify that firewall rules allow incoming TCP traffic to your endpoints from following ranges: `130.211.0.0/22` and `35.191.0.0/16`.
    * Verify that your endpoints are healthy using the Google Cloud CLI or by calling `getHealth` API on the `backendService` or the listEndpoints API on the NEG with the showHealth parameter set to `SHOW`.



### Stalled rollout

**Symptom:** Rolling out an updated Deployment stalls, and the number of up-to-date replicas does not match the chosen number of replicas.

**Potential Resolution:**

The deployment's health checks are failing. The container image might be bad or the health check might be misconfigured. The rolling replacement of Pods waits until the newly started Pod passes its Pod Readiness gate. This only occurs if the Pod is responding to load balancer health checks. If the Pod does not respond, or if the health check is misconfigured, the readiness gate conditions can't be met and the rollout can't continue.

  * If you're using kubectl 1.13 or higher, you can check the status of a Pod's readiness gates with the following command:
        
        kubectl get my-Pod -o wide
        

Check the **READINESS GATES** column.

This column doesn't exist in kubectl 1.12 and lower. A Pod that is marked as being in the READY state may have a failed readiness gate. To verify this, use the following command:
        
        kubectl get my-pod -o yaml
        

The readiness gates and their status are listed in the output.

  * Verify that the container image in your Deployment's Pod specification is functioning correctly and is able to respond to health checks.

  * Verify that the health checks are correctly configured.




### NEG is not garbage collected

**Symptom:** A NEG that should have been deleted still exists.

**Potential Resolution:**

  * The NEG is not garbage collected if the NEG is referenced by a backend service. See Preventing leaked NEGs for details.
  * If using 1.18 or later, you can check for events in the `ServiceNetworkEndpointGroup` resource using the service neg procedure.
  * Check to see if the NEG is still needed by a service. Check the `svcneg` resource for the service that corresponds to the NEG and check if a Service annotation exists.



### NEG is not synced with Service

**Symptom:** Expected (Pod IP) endpoints don't exist in the NEG, the NEG is not synchronized, or the error `Failed to sync NEG_NAME (will not retry): neg name NEG_NAME is already in use, found a custom named neg with an empty description`

**Potential Resolution:**

If you are using GKE 1.18 or later, check the `svcneg` resource for information:

  * Check the `status.lastSyncTime` value to verify if the NEG has synced recently.
  * Check the `Synced` condition for any errors that occurred in the most recent sync.



If you are using GKE 1.19.9 or later, check whether there exists a NEG whose name and zone match the name and zone of the NEG that the GKE NEG controller needs to create. For example, a NEG with the name that the NEG controller needs to use might have been created using gcloud CLI or the Google Cloud console in the cluster's zone (or one of the cluster's zones). In this case, you must delete the existing NEG before the NEG controller can synchronize its endpoints. Standalone NEG creation and membership are designed to be managed by the NEG controller.

## What's next

  * [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)
  * [Backend Services](https://docs.cloud.google.com/load-balancing/docs/backend-service)
  * [Creating Health Checks](https://docs.cloud.google.com/load-balancing/docs/health-checks)
  * [Using Target Proxies](https://docs.cloud.google.com/load-balancing/docs/target-proxies)
  * [Using Forwarding Rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
