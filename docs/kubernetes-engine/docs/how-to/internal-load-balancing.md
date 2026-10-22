---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing/
title: Create an internal load balancer \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:56.247713+00:00
---

# Create an internal load balancer  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Create an internal load balancer Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to deploy an internal LoadBalancer Service that builds an internal passthrough Network Load Balancer. Before reading this page, ensure that you're familiar with the following:

  * [About LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer)
  * [GKE LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters)



To learn more about internal passthrough Network Load Balancers in general, see [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## Requirements

  * This tutorial uses `spec.loadBalancerClass` to create an internal passthrough Network Load Balancer with `GCE_VM_IP` NEG backends. This tutorial requires GKE version 1.33.1-gke.1779000 or later because `spec.loadBalancerClass` requires GKE version 1.33.1-gke.1779000 or later.

  * Zonal affinity requires GKE version 1.33.3-gke.1392000 and later.

  * Your cluster must have GKE subsetting enabled:

    * GKE subsetting is enabled by default in clusters that run version 1.36 and later. For these versions, subsetting is active regardless of the cluster's subsetting flag value.

    * In supported GKE versions before version 1.36, you must enable GKE subsetting explicitly. You can enable GKE subsetting when you create a new cluster or by updating an existing cluster. Once enabled, GKE subsetting cannot be disabled. For more information, see Verify and enable GKE subsetting.

  * If your cluster is on a version earlier than 1.36, the `HttpLoadBalancing` add-on must be enabled in your cluster. This add-on is enabled by default.

  * To enable Cloud Logging for an internal LoadBalancer Service, your GKE cluster must use version 1.36.0-gke.2459000 or later.




## Verify and enable GKE subsetting

Ensure that GKE subsetting is enabled:

  * GKE subsetting is always enabled in GKE version 1.36 and later.

  * You can enable GKE subsetting manually in new and existing Standard and Autopilot clusters that run GKE version 1.18.19-gke.1400 and later, but before GKE version 1.36. You cannot disable GKE subsetting after you have enabled it.




For information about why GKE subsetting is important, see [Special considerations for internal LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#internal-lb).

To determine whether GKE subsetting is enabled, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --format="get(currentMasterVersion, networkConfig.enableL4ilbSubsetting)"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION `: the zone or region of the cluster.



The output of the command shows the cluster's control plane version followed by `True` or `False` for the `networkConfig.enableL4ilbSubsetting` attribute. Interpret the output in the following way:

  * If the control plane version is 1.36 or later, GKE subsetting is enabled regardless of whether the `networkConfig.enableL4ilbSubsetting` attribute is `True` or `False`.
  * If the control plane version is before 1.36: 
    * `True` means GKE subsetting is enabled.
    * `False` means GKE subsetting is disabled.



To enable GKE subsetting in a cluster that runs GKE version 1.18.19-gke.1400 and later, but before GKE version 1.36, use the gcloud CLI or the Google Cloud console.

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[ Go to Google Kubernetes Engine ](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Networking** , next to the **Subsetting for L4 Internal Load Balancers** field, click _edit_ **Enable subsetting for L4 internal load balancers**.

  4. Select the **Enable subsetting for L4 internal load balancers** checkbox.

  5. Click **Save Changes**.




### gcloud
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION
        --enable-l4-ilb-subsetting
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION `: the zone or region of the cluster.



Enabling GKE subsetting—by using gcloud CLI, the Google Cloud console, or by upgrading your cluster to version 1.36 or later—does not modify existing internal LoadBalancer Services. If you want to migrate an existing internal LoadBalancer Service to use `GCE_VM_IP` NEG backends, you must deploy a replacement Service manifest.

**Caution:** Don't remove or modify finalizer tags on Service resources. GKE depends on these tags to distinguish between non-subsetting and subsetting load balancers. If you use external resource managers or GitOps tools, configure these tools to preserve the finalizer tags. Removing or updating these tags can prevent new load balancers from being successfully provisioned.

## Deploy a workload

The following manifest describes a Deployment that runs a sample web application container image.

  1. Save the manifest as `ilb-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: ilb-deployment
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: ilb-deployment
           template:
             metadata:
               labels:
                 app: ilb-deployment
             spec:
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f ilb-deployment.yaml
         




## Create an internal LoadBalancer Service

  1. (Optional) Disable automatic VPC firewall rules creation:

While GKE automatically creates VPC firewall rules to allow traffic to your internal load balancer, you have the option to disable the automatic VPC firewall rules creation and manage firewall rules on your own. You can disable VPC firewall rules only if you have enabled GKE subsetting for your internal LoadBalancer Service. However, managing VPC firewall rules is optional and you can rely on the automatic rules.

Before you disable automatic VPC firewall rules creation, ensure that you define allow rules that permit traffic to reach your load balancer and application Pods.

For more information on managing VPC firewall rules, see [manage automatic firewall rule creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#manage-firewall-rule-creation) and how to disable automatic firewall rule creation, see [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules).

  2. The following example creates an internal LoadBalancer Service using TCP port `80`. GKE deploys an internal passthrough Network Load Balancer whose forwarding rule uses port `80`, but then forwards traffic to backend Pods on port `8080`:

     1. Save the manifest as `ilb-svc.yaml`:
            
            apiVersion: v1
            kind: Service
            metadata:
              name: ilb-svc
            spec:
              type: LoadBalancer
              # Request an internal load balancer.
              loadBalancerClass: networking.gke.io/l4-regional-internal
              # Evenly route external traffic to all endpoints.
              externalTrafficPolicy: Cluster
              # Prioritize routing traffic to endpoints that are in the same zone.
              trafficDistribution: PreferSameZone
              selector:
                app: ilb-deployment
              # Forward traffic from TCP port 80 to port 8080 in backend Pods.
              ports:
              - name: tcp-port
                protocol: TCP
                port: 80
                targetPort: 8080
            

Your manifest must contain the following:

        * A `name` for the internal LoadBalancer Service, in this case `ilb-svc`.
        * The `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-internal` value to specify an internal LoadBalancer Service, as shown in the example manifest.
        * The `type: LoadBalancer`.
        * A `spec: selector` field to specify the Pods the Service should target, for example, `app: hello`.
        * Port information: 
          * The `port` represents the destination port on which the forwarding rule of the internal passthrough Network Load Balancer receives packets.
          * The `targetPort` must match a `containerPort` defined on each serving Pod.
          * The `port` and `targetPort` values don't need to be the same. Nodes always perform destination NAT, changing the destination load balancer forwarding rule IP address and `port` to a destination Pod IP address and `targetPort`. For more details, see [Destination Network Address Translation on nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#pp-step2) in the LoadBalancer Service concepts documentation.

Your manifest can contain the following:

        * `spec.ipFamilyPolicy` and `ipFamilies` to define how GKE allocates IP addresses to the Service. GKE supports either single-stack (IPv4 only or IPv6 only), or dual-stack IP LoadBalancer Services. A dual-stack LoadBalancer Service is implemented with two separate internal passthrough Network Load Balancer forwarding rules: one for IPv4 traffic and one for IPv6 traffic. The GKE dual-stack LoadBalancer Service is available in version 1.29 or later. To learn more, see [IPv4/IPv6 dual-stack Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#service_parameters).
        * `spec.trafficDistribution` to define how GKE routes incoming traffic. To enable zonal affinity, set the value of this field to `PreferSameZone`. Zonal affinity means that GKE prioritizes routing traffic that originates from a zone to nodes and Pods within that same zone. If no healthy Pods are available in that zone, traffic is routed to another zone. For cluster versions earlier than 1.35.0-gke.1811000, use `PreferClose` as the value instead. Zonal affinity requires GKE subsetting to be enabled.

**Note:** You can also enable or disable zonal affinity on an existing internal LoadBalancer Service by using the `kubectl edit svc service-name` command. The `kubectl edit` command opens the existing load balancer's Service manifest in your configured text editor, where you can add or remove the `spec.trafficDistribution` parameter and save changes. Traffic might be briefly interrupted when you modify this parameter.

For important considerations and a workaround for scaling workloads with zonal affinity, see Scale workloads with zonal affinity.

For more information, see [LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#service_parameters).

     2. Apply the manifest to your cluster:
            
            kubectl apply -f ilb-svc.yaml
            

  3. Get detailed information about the Service:
         
         kubectl get service ilb-svc --output yaml
         

The output is similar to the following:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             cloud.google.com/neg: '{"ingress":true}'
             cloud.google.com/neg-status: '{"network_endpoint_groups":{"0":"k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r"},"zones":["ZONE_NAME","ZONE_NAME","ZONE_NAME"]}'
             kubectl.kubernetes.io/last-applied-configuration: |
               {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{"networking.gke.io/load-balancer-type":"Internal"},"name":"ilb-svc","namespace":"default"},"spec":{"externalTrafficPolicy":"Cluster","ports":[{"name":"tcp-port","port":80,"protocol":"TCP","targetPort":8080}],"selector":{"app":"ilb-deployment"},"type":"LoadBalancer"}}
             networking.gke.io/load-balancer-type: Internal
             service.kubernetes.io/backend-service: k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r
             service.kubernetes.io/firewall-rule: k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r
             service.kubernetes.io/firewall-rule-for-hc: k8s2-pn2h9n5f-l4-shared-hc-fw
             service.kubernetes.io/healthcheck: k8s2-pn2h9n5f-l4-shared-hc
             service.kubernetes.io/tcp-forwarding-rule: k8s2-tcp-pn2h9n5f-default-ilb-svc-3bei4n1r
           creationTimestamp: "2022-07-22T17:26:04Z"
           finalizers:
           - gke.networking.io/l4-ilb-v2
           - service.kubernetes.io/load-balancer-cleanup
           name: ilb-svc
           namespace: default
           resourceVersion: "51666"
           uid: d7a1a865-7972-44e1-aa9e-db5be23d6567
         spec:
           allocateLoadBalancerNodePorts: true
           clusterIP: 10.88.2.141
           clusterIPs:
           - 10.88.2.141
           externalTrafficPolicy: Cluster
           internalTrafficPolicy: Cluster
           ipFamilies:
           - IPv4
           ipFamilyPolicy: SingleStack
           ports:
           - name: tcp-port
             # Kubernetes automatically allocates a port on the node during the
             # process of implementing a Service of type LoadBalancer.
             nodePort: 30521
             port: 80
             protocol: TCP
             targetPort: 8080
           selector:
             app: ilb-deployment
           sessionAffinity: None
           trafficDistribution: PreferSameZone
           type: LoadBalancer
         **status :
           # IP address of the load balancer forwarding rule.
           loadBalancer:
             ingress:
             - ip: 10.128.15.245**
         

The output has the following attributes:

     * The IP address of the internal passthrough Network Load Balancer's forwarding rule is included in `status.loadBalancer.ingress`. This IP address is different from the value of `clusterIP`. In this example, the load balancer's forwarding rule IP address is `10.128.15.245`.
     * Any Pod that has the label `app: ilb-deployment` is a serving Pod for this Service. These are the Pods that receive packets routed by the internal passthrough Network Load Balancer.
     * Clients call the Service by using this `loadBalancer` IP address and the TCP destination port specified in the `port` field of the Service manifest. For complete details about how packets are routed once received by a node, see [Packet processing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#node-packet-processing).
     * GKE assigned a `nodePort` to the Service; in this example, port `30521` is assigned. The `nodePort` is not relevant to the internal passthrough Network Load Balancer.
  4. Inspect the Service network endpoint group:
         
         kubectl get svc ilb-svc -o=jsonpath="{.metadata.annotations.cloud\.google\.com/neg-status}"
         

The output is similar to the following:
         
         {"network_endpoint_groups":{"0":"k8s2-knlc4c77-default-ilb-svc-ua5ugas0"},"zones":["ZONE_NAME"]}
         

The response indicates that GKE has created a network endpoint group named `k8s2-knlc4c77-default-ilb-svc-ua5ugas0`. This annotation is present in services of type `LoadBalancer` that use GKE subsetting and is not present in Services that don't use GKE subsetting.




### Enable logging for backend services

You can enable, disable, and view logs for an Internal passthrough Network Load Balancer. To enable logging for your backend services, you must have GKE subsetting enabled.

You configure Cloud Logging by creating an L4LBConfig custom resource that specifies your logging settings. The L4LBConfig resource is linked to a Kubernetes Service in the Service manifest. After you apply the manifest, the GKE controller configures logging for the backend service. If you don't link an L4LBConfig resource to the Service, the controller stops managing the logging configuration and leaves the backend service in its last known state. For more information, see [Understand coast behavior](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing#understand_coast_behavior).

You can configure the following fields:

  * `enabled`: if set to `true`, enables logging for this Service and logs are available in Cloud Logging. Otherwise, logging is disabled for this Service.
  * `sampleRate`: specifies a value from `0` through `1,000,000` (default), where `0` means no packets are logged and `1,000,000` means 100% of packets are logged. The `sampleRate` field is optional, and is relevant only if the value of the `enable` field is set to `true`.
  * `optionalMode`: controls which optional metadata fields are included in the generated logs for the load balancer. The field accepts one of the following string values: 
    * `EXCLUDE_ALL_OPTIONAL`: default setting if `optionalMode` is not specified. When set, no optional fields are included in the logs, providing the most concise log format.
    * `INCLUDE_ALL_OPTIONAL`: enables logging for all available optional fields, providing the most detailed log entries.
    * `CUSTOM`: specifies a custom list of optional fields which are included in the logs. With the `CUSTOM` mode, you must also use the `optionalFields` parameter to provide a comma-separated list of the fields that you want.
  * `optionalFields`: comma-separated string of field names. Defines the exact optional metadata fields that you want to include in the generated logs. This field is used only when `optionalMode` is set to `CUSTOM`, otherwise any values are ignored.



To configure Cloud Logging, create the L4LBConfig resource in the same namespace as your Service resource. The following example L4LBConfig manifest enables Cloud Logging and sets the sample rate to 50% of the requests for a given load balancer Service.

  1. Save the following manifest as `svc-l4lb-config.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: L4LBConfig
         metadata:
           name: svc-l4lb-config
           namespace: default
         spec:
           logging:
             enabled: true # must be included
             sampleRate: 500000
             optionalMode: "INCLUDE_ALL_OPTIONAL"
         

  2. Apply the L4LBConfig manifest to your cluster:
         
         kubectl apply -f svc-l4lb-config.yaml
         

  3. Add the `networking.gke.io/l4lb-config` annotation to the `ilb-svc.yaml` Service manifest:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: ilb-svc
           annotations:
             networking.gke.io/load-balancer-type: "Internal"
             **networking.gke.io/l4lb-config : "svc-l4lb-config"**
         spec:
           type: LoadBalancer
           selector:
             app: store
           ports:
             - name: tcp-port
               protocol: TCP
               port: 8080
               targetPort: 8080
         

  4. Apply the Service manifest to your cluster:
         
         kubectl apply -f ilb-svc.yaml
         




## Scale workloads with zonal affinity

Because the HorizontalPodAutoscaler (HPA) scales Pods based on aggregate cluster metrics rather than per-zone load, decouple your workloads by zone to prevent zonal overload. Instead of a single cluster-wide Deployment and HPA, create a separate Deployment and HPA for each zone your cluster operates in. A single internal LoadBalancer Service can route traffic to all of these independent zonal workloads simultaneously.

### Architecture overview

  * **One workload per zone:** create separate Deployments for each zone (for example, `zone-a`, `zone-b`).
  * **Node selectors:** bind each Deployment to its specific zone using the `topology.kubernetes.io/zone` node selector.
  * **One HPA per zone:** attach an HPA to each specific Deployment so that its Pods scale independently based on localized metrics.
  * **One shared Service:** expose all of these Deployments behind a single internal LoadBalancer Service configured with zonal affinity (using the same selector).



### Configure independent zonal workloads

The following example demonstrates how to implement this architecture across two zones.

  1. Create a separate Deployment for each zone. The Deployments share the same `app` label but have a strict `nodeSelector` tying them to a specific zone.

Save the following manifest as `zonal-deployments.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-app-zone-a
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: my-app
               zone: zone-a
           template:
             metadata:
               labels:
                 app: my-app
                 zone: zone-a
             spec:
               nodeSelector:
                 topology.kubernetes.io/zone: "COMPUTE_ZONE_A"
               containers:
               - name: echoserver
                 image: gcr.io/google_containers/echoserver:1.10
                 ports:
                 - containerPort: 8080
                 resources:
                   requests:
                     cpu: "100m"
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-app-zone-b
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: my-app
               zone: zone-b
           template:
             metadata:
               labels:
                 app: my-app
                 zone: zone-b
             spec:
               nodeSelector:
                 topology.kubernetes.io/zone: "COMPUTE_ZONE_B"
               containers:
               - name: echoserver
                 image: gcr.io/google_containers/echoserver:1.10
                 ports:
                 - containerPort: 8080
                 resources:
                   requests:
                     cpu: "100m"
         

Replace `COMPUTE_ZONE_A` and `COMPUTE_ZONE_B` with your actual zones (for example, `us-central1-a` and `us-central1-b`).

  2. Apply the manifest:
         
         kubectl apply -f zonal-deployments.yaml
         

  3. Create an independent HPA for each zonal deployment.

Save the following manifest as `zonal-hpas.yaml`:
         
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: hpa-zone-a
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: my-app-zone-a
           minReplicas: 2
           maxReplicas: 10
           metrics:
           - type: Resource
             resource:
               name: cpu
               target:
                 type: Utilization
                 averageUtilization: 70
         ---
         apiVersion: autoscaling/v2
         kind: HorizontalPodAutoscaler
         metadata:
           name: hpa-zone-b
         spec:
           scaleTargetRef:
             apiVersion: apps/v1
             kind: Deployment
             name: my-app-zone-b
           minReplicas: 2
           maxReplicas: 10
           metrics:
           - type: Resource
             resource:
               name: cpu
               target:
                 type: Utilization
                 averageUtilization: 70
         

  4. Apply the manifest:
         
         kubectl apply -f zonal-hpas.yaml
         

  5. Ensure your Service targets the shared label (`app: my-app`) and has zonal affinity enabled.

Save the following manifest as `zonal-service.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: my-app-service-internal
         spec:
           type: LoadBalancer
           loadBalancerClass: networking.gke.io/l4-regional-internal
           trafficDistribution: PreferSameZone
           selector:
             app: my-app
           ports:
           - name: tcp-port
             protocol: TCP
             port: 8080
             targetPort: 8080
         

  6. Apply the manifest:
         
         kubectl apply -f zonal-service.yaml
         




## Verify internal passthrough Network Load Balancer components

This section shows you how to verify the key components of your internal passthrough Network Load Balancer.

  * Verify that your Service is running:
        
        kubectl get service SERVICE_NAME --output yaml
        

Replace `SERVICE_NAME` with the name of the Service manifest.

If you enabled zonal affinity, the output includes the parameter `spec.trafficDistribution`. The value of this field is set to `PreferSameZone`, or `PreferClose` if the cluster version is earlier than 1.35.0-gke.1811000.

  * Verify the internal passthrough Network Load Balancer's forwarding rule IP address. The internal passthrough Network Load Balancer's forwarding rule IP address is `10.128.15.245` in the example included in the Create an internal LoadBalancer Service section. Verify that this forwarding rule is included in the list of forwarding rules in the cluster's project by using the Google Cloud CLI:
        
        gcloud compute forwarding-rules list --filter="loadBalancingScheme=INTERNAL"
        

The output includes the relevant internal passthrough Network Load Balancer forwarding rule, its IP address, and the backend service referenced by the forwarding rule (`k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r` in this example).
        
        NAME                          ... IP_ADDRESS  ... TARGET
        ...
        k8s2-tcp-pn2h9n5f-default-ilb-svc-3bei4n1r   10.128.15.245   ZONE_NAME/backendServices/k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r
        

  * Describe the load balancer's backend service by using the Google Cloud CLI:
        
        gcloud compute backend-services describe k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r --region=COMPUTE_REGION
        

Replace `COMPUTE_REGION` with the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the backend service.

If you enabled zonal affinity:

    * The `networkPassThroughLbTrafficPolicy.zonalAffinity.spillover` field should be set to the `ZONAL_AFFINITY_SPILL_CROSS_ZONE` value.
    * The `networkPassThroughLbTrafficPolicy.zonalAffinity.spilloverRatio` field should be set to `0` or not be included.

The output includes the backend `GCE_VM_IP` NEG or NEGs for the Service (`k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r` in this example).
    
    backends:
    - balancingMode: CONNECTION
      group: .../ZONE_NAME/networkEndpointGroups/k8s2-pn2h9n5f-default-ilb-svc-3bei4n1r
    ...
    kind: compute#backendService
    loadBalancingScheme: INTERNAL
    name: aae3e263abe0911e9b32a42010a80008
    networkPassThroughLbTrafficPolicy:
      zonalAffinity:
        spillover: ZONAL_AFFINITY_SPILL_CROSS_ZONE
    protocol: TCP
    ...
    

If you disabled zonal affinity, the `networkPassThroughLbTrafficPolicy.zonalAffinity.spillover` field should be set to `ZONAL_AFFINITY_DISABLED` or not be included. Note that zonal affinity is automatically disabled if your cluster is on a version earlier than 1.33.3-gke.1392000.

  * Determine the list of nodes in a subset for a service:
        
        gcloud compute network-endpoint-groups list-network-endpoints NEG_NAME \
            --zone=COMPUTE_ZONE
        

Replace the following:

    * `NEG_NAME`: the name of the network endpoint group created by the GKE controller.
    * `COMPUTE_ZONE`: the [compute zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the network endpoint group to operate on.
  * Determine the list of healthy nodes for an internal passthrough Network Load Balancer:
        
        gcloud compute backend-services get-health SERVICE_NAME \
            --region=COMPUTE_REGION
        

Replace the following:

    * `SERVICE_NAME`: the name of the backend service. This value is the same as the name of the network endpoint group created by the GKE controller.
    * `COMPUTE_REGION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the backend service to operate on.
  * Verify that Cloud Logging has been enabled for the Service:
        
        kubectl get svc SERVICE_NAME --output yaml
        

Replace the following:

    * `SERVICE_NAME`: the name of the Service.

In the output, ensure that the `Status.Conditions` field has `Type: LoggingConfigManaged` and `Reason: Reconciled`.




## Test connectivity to the internal passthrough Network Load Balancer

The internal passthrough Network Load Balancer is only accessible within the same VPC network ([or a connected network](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks)). By default, the load balancer's forwarding rule has global access disabled, so client VMs, Cloud VPN tunnels, or Cloud Interconnect attachments (VLANs) must be located in the same region as the internal passthrough Network Load Balancer. To support clients in all regions, you can enable global access on the load balancer's forwarding rule by including the [global access](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#global_access_internal_lb) annotation in the Service manifest.

Run the following command in the same region as the cluster:
    
    
    curl LOAD_BALANCER_IP:80
    

Replace `LOAD_BALANCER_IP` with the load balancer's forwarding rule IP address.

The response shows the output of `ilb-deployment`:
    
    
    Hello, world!
    Version: 1.0.0
    Hostname: ilb-deployment-77b45987f7-pw54n
    

## Delete the internal LoadBalancer Service and load balancer resources

You can delete the Deployment and Service using `kubectl delete` or the Google Cloud console.

### kubectl

#### Delete the Deployment

To delete the Deployment, run the following command:
    
    
    kubectl delete deployment ilb-deployment
    

#### Delete the Service

To delete the Service, run the following command:
    
    
    kubectl delete service ilb-svc
    

### Console

#### Delete the Deployment

To delete the Deployment, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Select the Deployment you want to delete, then click _delete_ **Delete**.

  3. When prompted to confirm, select the **Delete HorizontalPodAutoscaler associated with selected Deployment** checkbox, then click **Delete**.




#### Delete the Service

To delete the Service, perform the following steps:

  1. Go to the **Services & Ingress** page in the Google Cloud console.

[Go to Services & Ingress](https://console.cloud.google.com/kubernetes/discovery)

  2. Select the Service you want to delete, then click _delete_ **Delete**.

  3. When prompted to confirm, click **Delete**.




## Shared IP

The internal passthrough Network Load Balancer allows the [sharing of a Virtual IP address amongst multiple forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip). This is useful for expanding the number of simultaneous ports on the same IP or for accepting UDP and TCP traffic on the same IP. It allows up to a maximum of 50 exposed ports per IP address. Shared IPs are supported natively on GKE clusters with internal LoadBalancer Services. When deploying, the Service's `loadBalancerIP` field is used to indicate which IP should be shared across Services.

### Limitations

A shared IP for multiple load balancers has the following limitations and capabilities:

  * Each forwarding rule can have up to five ports (contiguous or non-contiguous), or it can be configured to match and forward traffic on all ports. If an Internal LoadBalancer Service defines more than five ports, the forwarding rule will automatically be set to match all ports.
  * A maximum of ten Services (forwarding rules) can share an IP address. This results in a maximum of 50 ports per shared IP.
  * Each forwarding rule that shares the same IP address must use a unique combination of protocols and ports. Therefore, every internal LoadBalancer Service must use a unique set of protocols and ports.
  * A combination of TCP-only and UDP-only Services is supported on the same shared IP, however you cannot expose both TCP and UDP ports in the same Service.



### Enabling Shared IP

To enable an internal LoadBalancer Services to share a common IP, follow these steps:

  1. Create a static internal IP with `--purpose SHARED_LOADBALANCER_VIP`. An IP address must be created with this purpose to enable its ability to be shared. If you create the static internal IP address in a Shared VPC, you must create the IP address in the same service project as the instance that will use the IP address, even though the value of the IP address will come from the range of available IPs in a selected shared subnet of the Shared VPC network. Refer to [reserving a static internal IP](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#reserve_internal_ip) on the _Provisioning Shared VPC_ page for more information.

  2. Deploy up to ten internal LoadBalancer Services using this static IP in the `loadBalancerIP` field. The internal passthrough Network Load Balancers are reconciled by the GKE service controller and deploy using the same frontend IP.




The following example demonstrates how this is done to support multiple TCP and UDP ports against the same internal load balancer IP.

  1. Create a static IP in the same region as your GKE cluster. The subnet must be the same subnet that the load balancer uses, which by default is the same subnet that is used by the GKE cluster node IPs.

If your cluster and the VPC network are in the same project:
         
         gcloud compute addresses create IP_ADDR_NAME \
             --project=PROJECT_ID \
             --subnet=SUBNET \
             --addresses=IP_ADDRESS \
             --region=COMPUTE_REGION \
             --purpose=SHARED_LOADBALANCER_VIP
         

If your cluster is in a Shared VPC service project but uses a Shared VPC network in a host project:
         
         gcloud compute addresses create IP_ADDR_NAME \
             --project=SERVICE_PROJECT_ID \
             --subnet=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/SUBNET \
             --addresses=IP_ADDRESS \
             --region=COMPUTE_REGION \
             --purpose=SHARED_LOADBALANCER_VIP
         

Replace the following:

     * `IP_ADDR_NAME`: a name for the IP address object.
     * `SERVICE_PROJECT_ID`: the ID of the service project.
     * `PROJECT_ID`: the ID of your project (single project).
     * `HOST_PROJECT_ID`: the ID of the Shared VPC host project.
     * `COMPUTE_REGION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) containing the shared subnet.
     * `IP_ADDRESS`: an unused internal IP address from the selected subnet's primary IP address range. If you omit specifying an IP address, Google Cloud selects an unused internal IP address from the selected subnet's primary IP address range. To determine an automatically selected address, you'll need to run [`gcloud compute addresses describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe).
     * `SUBNET`: the name of the shared subnet.
  2. Save the following TCP Service configuration to a file named `tcp-service.yaml` and then deploy to your cluster. Replace `IP_ADDRESS` with the IP address you chose in the previous step.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: tcp-service
           namespace: default
         spec:
           type: LoadBalancer
           # Request an internal load balancer.
           loadBalancerClass: networking.gke.io/l4-regional-internal
           # Use an IP address that you create.
           loadBalancerIP: IP_ADDRESS
           selector:
             app: myapp
           ports:
           - name: 8001-to-8001
             protocol: TCP
             port: 8001
             targetPort: 8001
           - name: 8002-to-8002
             protocol: TCP
             port: 8002
             targetPort: 8002
           - name: 8003-to-8003
             protocol: TCP
             port: 8003
             targetPort: 8003
           - name: 8004-to-8004
             protocol: TCP
             port: 8004
             targetPort: 8004
           - name: 8005-to-8005
             protocol: TCP
             port: 8005
             targetPort: 8005
         

  3. Apply this Service definition against your cluster:
         
         kubectl apply -f tcp-service.yaml
         

  4. Save the following UDP Service configuration to a file named `udp-service.yaml` and then deploy it. It also uses the `IP_ADDRESS` that you specified in the previous step.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: udp-service
           namespace: default
         spec:
           type: LoadBalancer
           # Request an internal load balancer.
           loadBalancerClass: networking.gke.io/l4-regional-internal
           # Use the same IP address that you used for the TCP Service.
           loadBalancerIP: IP_ADDRESS
           selector:
             app: my-udp-app
           ports:
           - name: 9001-to-9001
             protocol: UDP
             port: 9001
             targetPort: 9001
           - name: 9002-to-9002
             protocol: UDP
             port: 9002
             targetPort: 9002
         

  5. Apply this file against your cluster:
         
         kubectl apply -f udp-service.yaml
         

  6. Validate that the VIP is shared amongst load balancer forwarding rules by listing them out and filtering for the static IP. This shows that there is a UDP and a TCP forwarding rule both listening across seven different ports on the shared `IP_ADDRESS`, which in this example is `10.128.2.98`.
         
         gcloud compute forwarding-rules list | grep 10.128.2.98
         ab4d8205d655f4353a5cff5b224a0dde                         us-west1   10.128.2.98     UDP          us-west1/backendServices/ab4d8205d655f4353a5cff5b224a0dde
         acd6eeaa00a35419c9530caeb6540435                         us-west1   10.128.2.98     TCP          us-west1/backendServices/acd6eeaa00a35419c9530caeb6540435
         




## Known issues

### Error creating load balancer in Standard tier

When you create an internal passthrough Network Load Balancer in a project with the [project default network tier](https://docs.cloud.google.com/network-tiers/docs/set-network-tier#setting_the_tier_for_all_resources_in_a_project) set to Standard, the following error message appears:
    
    
    Error syncing load balancer: failed to ensure load balancer: googleapi: Error 400: STANDARD network tier (the project's default network tier) is not supported: Network tier other than PREMIUM is not supported for loadBalancingScheme=INTERNAL., badRequest
    

To resolve this issue in GKE versions earlier than 1.23.3-gke.900, configure the project default network tier to Premium.

This issue is resolved in GKE versions 1.23.3-gke.900 and later when [GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) is enabled.

The GKE controller creates internal passthrough Network Load Balancers in the Premium network tier even if the project default network tier is set to Standard.

## What's next

  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * [Learn more about Compute Engine load balancers](https://docs.cloud.google.com/compute/docs/load-balancing).
  * [Learn how to create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * [Troubleshoot load balancing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing).
  * [Learn about IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).
  * [Learn about configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
