---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer/
title: Create a backend service-based external load balancer \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:26.239689+00:00
---

# Create a backend service-based external load balancer  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Create a backend service-based external load balancer Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to deploy an external LoadBalancer Service that builds a backend service-based regional external passthrough Network Load Balancer. Before reading this page, ensure that you're familiar with the following:

  * [About LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer)
  * [GKE LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters)



To learn more about regional external passthrough Network Load Balancers in general, see [Backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Requirements

  * This tutorial uses `spec.loadBalancerClass` to create a backend service-based regional external passthrough Network Load Balancer with `GCE_VM_IP` NEG backends. This tutorial requires GKE version 1.33.1-gke.1779000 or later because `spec.loadBalancerClass` requires GKE version 1.33.1-gke.1779000 or later. Version 1.33.1-gke.1779000 or later also exceeds minimum GKE version requirements for NEG backends or the weighted load balancer feature.

  * If your cluster is on a version earlier than 1.36, the `HttpLoadBalancing` add-on must be enabled in your cluster. This add-on is enabled by default. For more information see [HttpLoadBalancing prerequisite](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#prerequisite-httpaddon).

  * To enable Cloud Logging for an external LoadBalancer Service, your GKE cluster must use version 1.36.0-gke.2459000 or later.




## Choose a cluster

You can create a new cluster or choose an existing cluster that meets the requirements.

### Create a new cluster

**Autopilot**

To create a new Autopilot cluster:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --release-channel=RELEASE_CHANNEL \
        --cluster-version=VERSION \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `RELEASE_CHANNEL`: the name of the GKE [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) for the cluster.
  * `VERSION`: the GKE version for the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster.



To disable automatic VPC firewall rule creation for LoadBalancer Services, include the `--disable-l4-lb-firewall-reconciliation` flag. For more information, see [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules).

**Standard**

To create a new Standard cluster:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --release-channel=RELEASE_CHANNEL \
        --cluster-version=VERSION \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `RELEASE_CHANNEL`: the name of the GKE [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) for the cluster.
  * `VERSION`: the GKE version for the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster.



To disable automatic VPC firewall rule creation for LoadBalancer Services, include the `--disable-l4-lb-firewall-reconciliation` flag. For more information, see [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules).

### Upgrade an existing cluster

Use the gcloud CLI to update an existing cluster:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
        --cluster-version=VERSION \
        --master \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the existing cluster.
  * `VERSION`: the specific GKE version to which you want to upgrade your cluster. For more information, see [Manually upgrading the control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp).
  * `COMPUTE_LOCATION`: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster.



To disable automatic VPC firewall rule creation for LoadBalancer Services, include the `--disable-l4-lb-firewall-reconciliation` flag. For more information, see [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules).

## Deploy a sample workload

Deploy the following sample workload which provides the serving Pods for the external LoadBalancer Service.

  1. Save the following sample Deployment as `store-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: store
         spec:
           replicas: 20
           selector:
             matchLabels:
               app: store
           template:
             metadata:
               labels:
                 app: store
             spec:
               containers:
               - image: registry.k8s.io/echoserver:1.10
                 imagePullPolicy: Always
                 name: echoserver
                 ports:
                   - name: http
                     containerPort: 8080
                 readinessProbe:
                   httpGet:
                     path: /healthz
                     port: 8080
                     scheme: HTTP
         

  2. Apply the manifest to the cluster:
         
         kubectl apply -f store-deployment.yaml
         

  3. Verify that there are 20 serving Pods for the Deployment:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                     READY   STATUS    RESTARTS   AGE
         store-cdb9bb4d6-s25vw      1/1     Running   0          10s
         store-cdb9bb4d6-vck6s      1/1     Running   0          10s
         ....
         




## Create the external LoadBalancer Service

  1. Expose the sample workload by creating an external LoadBalancer Service.

     1. Save the following Service manifest as `store-v1-lb-svc.yaml`:
            
            apiVersion: v1
            kind: Service
            metadata:
              name: store-v1-lb-svc
            spec:
              type: LoadBalancer
              **loadBalancerClass : networking.gke.io/l4-regional-external**
              selector:
                app: store
              ports:
              - name: tcp-port
                protocol: TCP
                port: 8080
                targetPort: 8080
            

     2. Apply the manifest to the cluster:
            
            kubectl apply -f store-v1-lb-svc.yaml
            

Note the following points about this sample manifest:

     * If your cluster runs GKE 1.33.1-gke.1779000 to 1.36, you must set the `spec.loadBalancerClass` field to the `networking.gke.io/l4-regional-external` value at the time the manifest is first applied to the cluster. This field instructs GKE to create a backend service-based regional external passthrough Network Load Balancer. In GKE 1.37 and later, this configuration is the default behavior and the field is not required. Backend service-based regional external passthrough Network Load Balancers are _required_ to support features like IPv6 and weighted load balancing.

     * GKE uses either `GCE_VM_IP` NEG backends or unmanaged instance group backends, depending on the cluster's version. In clusters with version 1.32.2-gke.1652000, the backend service-based regional external passthrough Network Load Balancer uses `GCE_VM_IP` NEGs. In previous versions, the backend service-based regional external passthrough Network Load Balancer uses unmanaged instance groups.

     * This `spec.loadBalancerClass` field is immutable and must be set when you create the Service. Because this field is immutable, you can't add or modify it on the manifest of an _existing_ LoadBalancer Service. Any attempt to do so will result in an error and the Service update will fail.




### Enable weighted load balancing

To distribute new connections proportionally to nodes based on how many serving, ready, and non-terminating Pods are present on each node, enable weighted load balancing by adding the `networking.gke.io/weighted-load-balancing: "pods-per-node"` annotation to the Service manifest.

  1. Add the `networking.gke.io/weighted-load-balancing: "pods-per-node"` annotation to the `store-v1-lb-svc.yaml` Service manifest, and ensure that you also set the `externalTrafficPolicy: Local` value so that it looks like this:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: store-v1-lb-svc
           **annotations :**
             **networking.gke.io/weighted-load-balancing : "pods-per-node"**
         spec:
           type: LoadBalancer
           **loadBalancerClass : networking.gke.io/l4-regional-external**
           **externalTrafficPolicy : Local**
           selector:
             app: store
           ports:
           - name: tcp-port
             protocol: TCP
             port: 8080
             targetPort: 8080
         

  2. Apply the manifest to the cluster:
         
         kubectl apply -f store-v1-lb-svc.yaml
         




Note the following about this example on weighted load balancing:

  * The Service manifest uses `externalTrafficPolicy: Local`. If you _don't_ need to enable weighted load balancing, you can also use `externalTrafficPolicy: Cluster`. For details about how the `externalTrafficPolicy` defines node grouping, which nodes pass their load balancer health checks, and how packets are processed, see [LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).

  * If you enable weighted load balancing, GKE doesn't prevent you from using `externalTrafficPolicy: Cluster`, but `externalTrafficPolicy: Cluster` effectively disables weighted load balancing because the packet might be routed, after the load balancer, to a different node.




You can also enable weighted load balancing on an existing external LoadBalancer Service by using `kubectl edit svc service-name`. The `kubectl edit` command opens the existing load balancer's Service manifest in your configured text editor, where you can modify the manifest and save changes. When you edit an existing external LoadBalancer Service, note the following points:

  * The existing external LoadBalancer Service must have resulted in the creation of a backend service-based regional external passthrough Network Load Balancers. For clusters running GKE versions earlier than 1.37, this requirement means the existing external LoadBalancer Service _must_ have the `spec.loadBalancerClass` field set to `networking.gke.io/l4-regional-external` when the manifest was first applied to the cluster.

Adding the `networking.gke.io/weighted-load-balancing: "pods-per-node"` annotation to an existing external LoadBalancer Service that uses a target pool-based regional external passthrough Network Load Balancer has no effect.

  * When updating the existing external LoadBalancer Service manifest, make sure to set the `externalTrafficPolicy: Local` value. Using `externalTrafficPolicy: Cluster` effectively disables weighted load balancing because the packet might be routed, after the load balancer, to a different node.




#### Disable weighted load balancing

To distribute new connections to nodes regardless of how many serving Pods are present on each node, disable weighted load balancing by removing the `networking.gke.io/weighted-load-balancing: "pods-per-node"` annotation from the Service manifest.

**Note:** Enabling or disabling weighted load balancing clears the load balancer's connection tracking table. Existing connections might be routed to different nodes, resulting in those nodes sending TCP reset packets. As a best practice, enable or disable weighted load balancing when a brief period of connection interruptions can be tolerated.

### Enable logging for backend services

You can enable, disable, and view logs for a backend service-based regional external passthrough Network Load Balancer.

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
         

  3. Add the `networking.gke.io/l4lb-config` annotation to the `store-v1-lb-svc.yaml` Service manifest:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: store-v1-lb-svc
           annotations:
             cloud.google.com/l4-rbs: "enabled"
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
         
         kubectl apply -f store-v1-lb-svc.yaml
         




## Verify the external LoadBalancer Service and its components

  1. Verify that your Service is running:
         
         kubectl get svc store-v1-lb-svc
         

The output is similar to the following:
         
         NAME               TYPE           CLUSTER-IP        EXTERNAL-IP     PORT(S)          AGE
         store-v1-lb-svc   LoadBalancer   10.44.196.160     35.193.28.231   8080:32466/TCP   11m
         

GKE assigned an `EXTERNAL_IP` for the regional external passthrough Network Load Balancer.

**Note:** It might take a few minutes for GKE to allocate an external IP address before the load balancer is ready to serve your application.
  2. Test connecting to the load balancer:
         
         curl EXTERNAL_IP:PORT
         

Replace the following:

     * `EXTERNAL_IP`: the allocated IP address for the regional external passthrough Network Load Balancer.
     * `PORT`: the allocated port number for the regional external passthrough Network Load Balancer.

The output is similar to the following:
    
    Hostname: store-v1-lb-svc-cdb9bb4d6-hflxd
    
    Pod Information:
      -no pod information available-
    
    Server values:
      server_version=nginx: 1.13.3 - lua: 10008
    
    Request Information:
      client_address=10.128.0.50
      method=GET
      real path=/
      query=
      request_version=1.1
      request_scheme=http
      request_uri=EXTERNAL_IP
    
    Request Headers:
      accept=*/*
      host=EXTERNAL_IP
      user-agent=curl/7.81.0
    
    Request Body:
      -no body in request-
    
    

  3. Check your LoadBalancer Service and its set of annotations describing its Google Cloud resources:
         
         kubectl describe svc store-v1-lb-svc
         

The output is similar to the following:
         
         Name:                     store-v1-lb-svc
         Namespace:                default
         Labels:                   <none>
         Annotations:              cloud.google.com/neg-status: {"network_endpoint_groups":{"0":"k8s2-qvveq1d8-default-my-service-ext-5s55db85"},"zones":["us-central1-c"]} #This annotation appears in the output only if the service uses NEG backends.
                                   networking.gke.io/weighted-load-balancing: pods-per-node #This annotation appears in the output only if weighted load balancing is enabled.
                                   service.kubernetes.io/backend-service: k8s2-qvveq1d8-default-my-service-ext-5s55db85
                                   service.kubernetes.io/firewall-rule: k8s2-qvveq1d8-default-my-service-ext-5s55db85
                                   service.kubernetes.io/firewall-rule-for-hc: k8s2-qvveq1d8-default-my-service-ext-5s55db85-fw
                                   service.kubernetes.io/healthcheck: k8s2-qvveq1d8-default-my-service-ext-5s55db85
                                   service.kubernetes.io/tcp-forwarding-rule: a808124abf8ce406ca51ab3d4e7d0b7d
         Selector:                 app=store
         Type:                     LoadBalancer
         IP Family Policy:         SingleStack
         IP Families:              IPv4
         IP:                       10.18.102.23
         IPs:                      10.18.102.23
         LoadBalancer Ingress:     35.184.160.229
         Port:                     tcp-port  8080/TCP
         TargetPort:               8080/TCP
         NodePort:                 tcp-port  31864/TCP
         Endpoints:                10.20.1.28:8080,10.20.1.29:8080
         Session Affinity:         None
         External Traffic Policy:  Local
         HealthCheck NodePort:     30394
         
         Events:
           Type    Reason                Age                    From                     Message
           ----    ------                ----                   ----                     -------
           Normal  ADD                   4m55s                  loadbalancer-controller  default/my-service-ext
         

There are several fields that indicate that a backend service-based regional external passthrough Network Load Balancer and its Google Cloud resources were successfully created:

     * `Events` field. This field is empty when the LoadBalancer Service and its resources were created successfully. If an error has occurred, it is listed here.
     * List of `Annotations` enabled: GKE adds the following list of read-only annotations to the Service manifest. Each annotation whose name begins with `service.kubernetes.io/` is used to indicate the name of a Google Cloud resource created as part of or to support the load balancer.

       * The `networking.gke.io/weighted-load-balancing: pods-per-node` annotation indicates that weighted load balancing was applied and the load balancer distributes traffic to backend Pods based on the number of Pods running on each node.
       * The `service.kubernetes.io/backend-service` annotation indicates the name of the load balancer's backend service.
       * The `service.kubernetes.io/healthcheck` annotation indicates the name of the load balancer health check used by the backend service.
       * The `service.kubernetes.io/tcp-forwarding-rule` or `service.kubernetes.io/udp-forwarding-rule` annotation indicates the name of the load balancer's forwarding rule.
       * The `service.kubernetes.io/firewall-rule` annotation indicates the name of the firewall rule created to permit traffic to the cluster nodes. Source ranges for this firewall rule are customizable using `spec.loadBalancerSourceRanges[]`. For additional detail about firewall rules for LoadBalancer Services, see [Firewall rules and source IP address allowlist](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#fw_ip_address).
       * The `service.kubernetes.io/firewall-rule-for-hc` annotation indicates the name of the firewall rule required for load balancer health checks.
       * The `cloud.google.com/neg-status` annotation indicates both the NEGs that are used by the load balancer and their zones. This annotation is only present when both of the following are true:

         * The cluster was running GKE version 1.32.2-gke.1652000 or later when the manifest was applied to the cluster.
         * The `spec.loadBalancerClass` field that was set to the `networking.gke.io/l4-regional-external` value was present in the Service manifest when it was applied to the cluster.
  4. Verify that load balancer resources and firewall rules have been created for the external LoadBalancer Service:

     * To see the forwarding rule, run the following command:
           
           gcloud compute forwarding-rules describe FWD_RULE_NAME \
               --region=REGION_NAME
           

Replace the following:

       * `FWD_RULE_NAME`: the forwarding rule name provided by either the `service.kubernetes.io/tcp-forwarding-rule` or `service.kubernetes.io/udp-forwarding-rule` read-only annotations. To check these annotations, run `kubectl describe svc SERVICE_NAME`.
       * `REGION_NAME`: the Google Cloud region containing the cluster. For zonal clusters, the region contains the zone used by the cluster.
     * To see the backend service, run the following command:
           
           gcloud compute backend-services describe BACKEND_SERVICE_NAME \
             --region=REGION_NAME
           

Replace the following:

       * `BACKEND_SERVICE_NAME`: the name of the backend service provided by the `service.kubernetes.io/backend-service` read-only annotation. To check this read-only annotation, run `kubectl describe svc SERVICE_NAME`.
       * `REGION_NAME`: the Google Cloud region containing the cluster. For zonal clusters, the region contains the zone used by the cluster.
     * To see the load balancer health check, run the following command:
           
           gcloud compute health-checks describe HEALTH_CHECK_NAME \
             --region=REGION_NAME
           

Replace the following:

       * `HEALTH_CHECK_NAME`: the load balancer's health check name. The name of the health check is provided by the `service.kubernetes.io/healthcheck` read-only annotation. To check this read-only annotation, run `kubectl describe svc SERVICE_NAME`.
       * `REGION_NAME`: the Google Cloud region containing the cluster. For zonal clusters, the region contains the zone used by the cluster.
     * To see the firewall rules, run the following commands:
           
           gcloud compute firewall-rules describe FIREWALL_RULE_NAME
           
           
           gcloud compute firewall-rules describe HEALTH_CHECK_FIREWALL_RULE_NAME
           

Replace the following:

       * `FIREWALL_RULE_NAME`: the name of the firewall rule that permits traffic to the load balancer. The name of this firewall rule is provided by the `service.kubernetes.io/firewall-rule` read-only annotation. To check this read-only annotation, run `kubectl describe svc SERVICE_NAME`.
       * `HEALTH_CHECK_FIREWALL_RULE_NAME`: the name of the firewall rule that permits health checks of the load balancer's backends (the cluster's nodes). The name of this firewall rule is provided by the `service.kubernetes.io/firewall-rule-for-hc` read-only annotation. To check this read-only annotation, run `kubectl describe svc SERVICE_NAME`.
     * To see the load balancer NEGs, run the following command:
           
           gcloud compute network-endpoint-groups describe NEG_NAME \
             --zone=ZONE_NAME
           

Replace the following:

       * `NEG_NAME`: the load balancer's NEG name. The name of the NEG is provided by the `cloud.google.com/neg-status` read-only annotation. To check this read-only annotation, run the `kubectl describe svc SERVICE_NAME` command. The annotation contains structured data with information about the NEG names and zones that are used by the load balancer. For zonal clusters, this annotation contains information about one NEG. For regional clusters, this annotation contains information about a NEG in each zone that the cluster is located in.
       * `ZONE_NAME`: the Google Cloud zone that contains the NEG.
  5. Verify that Cloud Logging has been enabled for the backend service:
         
         kubectl get svc SERVICE_NAME --output yaml
         

Replace the following:

     * `SERVICE_NAME`: the name of the backend service.

In the output, ensure that the `Status.Conditions` field has `Type: LoggingConfigManaged` and `Reason: Reconciled`.




## Delete the external LoadBalancer Service

To delete the sample `store-v1-lb-svc` external LoadBalancer Service, use the following command:
    
    
    kubectl delete service store-v1-lb-svc
    

GKE automatically removes all load balancer resources that it created for the external LoadBalancer Service.

## Migrate to `GCE_VM_IP` NEG backends

External LoadBalancer Services create backend service-based regional external passthrough Network Load Balancers if they are created in GKE 1.37 or later, specify the `networking.gke.io/l4-regional-external` value for the `spec.loadBalancerClass` field, or include the `cloud.google.com/l4-rbs: "enabled"` annotation. Depending on the GKE version of the cluster, GKE uses either `GCE_VM_IP` network endpoint groups or unmanaged instance groups as backends:

  * If the Service manifest was applied to a cluster running GKE version 1.32.2-gke.1652000 or later, the resulting regional external passthrough Network Load Balancer uses `GCE_VM_IP` network endpoint group (NEG) backends.

  * If the Service manifest was applied to a cluster running an earlier GKE version, the resulting regional external passthrough Network Load Balancer uses unmanaged instance group backends.




For more information, see [Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping) in About LoadBalancer Services.

You can create a new external LoadBalancer Service powered by a backend service-based regional external passthrough Network Load Balancer that uses `GCE_VM_IP` NEG backends if your existing Service uses one of the following load balancers:

  * A backend service-based regional external passthrough Network Load Balancer with instance group backends
  * A target pool-based regional external passthrough Network Load Balancer

**Note:** Switching to a backend service-based regional external passthrough Network Load Balancer using `GCE_VM_IP` NEG backends requires a few minutes of downtime to replace the Service.

To switch to a backend service-based regional external passthrough Network Load Balancer using `GCE_VM_IP` NEG backends:

  1. If you haven't already, upgrade your cluster to GKE version 1.32.2-gke.1652000 or later.

  2. Identify the external LoadBalancer Service that you want to switch to a backend service-based regional external passthrough Network Load Balancer using `GCE_VM_IP` NEG backends. Describe the Service using the following command:
         
         kubectl describe svc SERVICE_NAME -n SERVICE_NAMESPACE
         

Replace the following:

     * `SERVICE_NAME`: the name of the existing external LoadBalancer Service.

     * `SERVICE_NAMESPACE`: the namespace of the existing external LoadBalancer Service.

In the command output, note the load balancer's external IPv4 address listed after `LoadBalancer Ingress`.

  3. Retrieve the Service manifest for the existing LoadBalancer Service:

     * It's best if you have the original Service manifest that you applied to the cluster in the past. For example, you might have this in a source control repository.

     * If you don't have the original Service manifest:

       * Run the following command to get a YAML copy of the Service manifest that represents the load balancer current implementation:
             
             kubectl get svc SERVICE_NAME -n SERVICE_NAMESPACE -o yaml
             

       * Copy the manifest YAML to a text editor. Remove the `status` attribute and the following `metadata` attributes:

         * All of the following annotations: 
           * The `kubectl.kubernetes.io/last-applied-configuration` annotation
           * All annotations that start with `service.kubernetes.io`
         * `creationTimestamp`
         * `finalizers`
         * `resourceVersion`
         * `uid`
     * Ensure that the manifest includes the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value. If you're migrating from target pool-based regional external passthrough Network Load Balancer the field needs to be added.

Save the manifest file and note where you've saved it. The rest of this procedure refers to the path where you've saved the manifest as MANIFEST_FILE_PATH.

  4. Configure a static external IPv4 address resource to hold the external IPv4 address used by the existing load balancer:
         
         gcloud compute addresses create IP_ADDRESS_NAME --region=CLUSTER_REGION --addresses LB_EXTERNAL_IP
         

Replace the following:

     * `IP_ADDRESS_NAME`: the name of the static external IP address. The name must adhere to [name conventions for Compute Engine resources](https://docs.cloud.google.com/compute/docs/naming-resources).

     * `CLUSTER_REGION`: the region that contains the cluster. For zonal clusters, this is the region that contains the cluster's zone.

     * `LB_EXTERNAL_IP`: the external IPv4 address used by the current load balancer, determined in the second step of this procedure.

  5. Verify that the static external IPv4 address resource was created:
         
         gcloud compute addresses describe IP_ADDRESS_NAME --region=CLUSTER_REGION
         

Replace the variables as inidicated in the previous step.

  6. Delete the existing Service:
         
         kubectl delete svc SERVICE_NAME -n SERVICE_NAMESPACE
         

  7. Add the following annotation to the `MANIFEST_FILE_PATH` Service manifest file:
         
         networking.gke.io/load-balancer-ip-addresses: IP_ADDRESS_NAME
         

For more information about this annotation, see [Static IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#spd-static-ip) in LoadBalancer Service parameters.

  8. Apply the updated Service manifest to the cluster:
         
         kubectl apply -f MANIFEST_FILE_PATH
         

  9. (Optional) Release the static IPv4 address resource.
         
         gcloud compute addresses delete IP_ADDRESS_NAME --region=CLUSTER_REGION
         




## Troubleshoot

This section describes an issue that you might encounter when you configure weighted load balancing.

### Wrong external traffic policy for weighted load balancing

If you don't set the `externalTrafficPolicy: Local` value when you enable weighted load balancing, you might get a warning event when you describe the Service using the following command:
    
    
    kubectl describe svc store-v1-lb-svc`
    
    
    
    Events:
      Type     Reason                   Age      From                     Message
      ----     ------                   ----     ----                     -------
      **Warning  UnsupportedConfiguration 4m55s    loadbalancer-controller  Weighted load balancing by pods-per-node has no effect with External Traffic Policy: Cluster.**
    

To effectively enable weighted load balancing, you must set the `externalTrafficPolicy: Local` value.

## What's next

  * For a general overview of Load Balancer Services, see [LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).
  * For a description of Load Balancer Services parameters, see [LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters).
  * [Troubleshoot load balancing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
