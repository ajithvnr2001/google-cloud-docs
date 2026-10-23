---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress/
title: Configuring Ingress for internal Application Load Balancers \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:19.989110+00:00
---

# Configuring Ingress for internal Application Load Balancers  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configuring Ingress for internal Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to set up and use Ingress for internal Application Load Balancers in Google Kubernetes Engine (GKE). Ingress provides built-in support for internal load balancing through the GKE Ingress controller.

To learn more about which features are supported for Ingress for internal Application Load Balancers, see [Ingress features](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration). You can also learn more about how Ingress for internal Application Load Balancers works in [Ingress for internal Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

Ingress for internal Application Load Balancers has the following requirements:

  * Your cluster must use a GKE version later than 1.16.5-gke.10.
  * Your cluster must be [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).
  * Your cluster must have the `HttpLoadBalancing` add-on enabled. This add-on is enabled by default. You must not disable it.
  * You must use [Network Endpoint Groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs) as backends for your Service.
  * You can't enable global access for your internal Application Load Balancer. If you need global access, we recommend that you [deploy an internal Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#internal-gateway).



## Deploying Ingress for internal Application Load Balancers

The following exercises show you how to deploy Ingress for internal Application Load Balancers:

  1. Prepare your environment.
  2. Create a cluster.
  3. Deploy an application.
  4. Deploy a Service.
  5. Deploy Ingress.
  6. Validate the deployment.
  7. Delete Ingress resources.



### Prepare your environment

Before you can deploy load balancer resources through the Kubernetes Ingress API, you must prepare your [networking environment](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb#required_networking_environment) so that the load balancer proxies can be deployed in a given region.

Create a proxy-only subnet:
    
    
    gcloud compute networks subnets create proxy-only-subnet \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=COMPUTE_REGION \
        --network=NETWORK_NAME \
        --range=10.129.0.0/23
    

Replace the following:

  * `COMPUTE_REGION`: a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).
  * `NETWORK_NAME`: the name of the network for the subnet.



For more information, see [configuring the proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configuring_the_proxy-only_subnet).

### Create a firewall rule

The Ingress controller does not create a firewall rule to allow connections from the load balancer proxies in the proxy-subnet. You must create this firewall rule manually. However, the Ingress controller does create firewall rules to allow ingress for Google Cloud health-checks.

Create a firewall rule to allow connections from the load balancer proxies in the proxy-only subnet to the pod listening port:

**Note:** Shared VPC environments require additional preparation. For more information, see [Shared VPC Ingress preparation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#shared_vpc).
    
    
    gcloud compute firewall-rules create allow-proxy-connection \
        --allow=TCP:CONTAINER_PORT \
        --source-ranges=10.129.0.0/23 \
        --network=NETWORK_NAME
    

Replace `CONTAINER_PORT` with the value of the port that the Pod is listening to, such as `9376`.

### Creating a cluster

In this section, you create a VPC-native cluster that you can use with Ingress for internal Application Load Balancers. You can create this cluster using the Google Cloud CLI or the Google Cloud console.

### gcloud

Create a cluster in the same network as the proxy-only subnet:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --network=NETWORK_NAME
    

Replace the following:

  * `CLUSTER_NAME`: a name for your cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster. You must use the same location as the proxy-subnet that you created in the previous section.



### Console

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. In the **Cluster basics** section, complete the following: 
     1. Enter the **Name** for your cluster.
     2. For the **Location type** , select a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster. You must use the same region as the proxy-subnet that you created in the previous section.
  3. In the navigation pane, click **Networking**.
  4. In the **Network** list, select the network that you want the cluster to be created in. This network must be in the same VPC network as the proxy-subnet.
  5. In the **Node subnet** list, select the proxy-subnet that you created
  6. Click **Create**.



### Deploying a web application

In this section, you create a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

To create a Deployment:

  1. Save the following sample manifest as `web-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app: hostname
           name: hostname-server
         spec:
           selector:
             matchLabels:
               app: hostname
           minReadySeconds: 60
           replicas: 3
           template:
             metadata:
               labels:
                 app: hostname
             spec:
               containers:
               - image: registry.k8s.io/serve_hostname:v1.4
                 name: hostname-server
                 ports:
                 - containerPort: 9376
                   protocol: TCP
               terminationGracePeriodSeconds: 90
         

This manifest describes a Deployment that listens on an HTTPS server on port 9376. This Deployment also manages Pods for your application. Each Pod runs one application container with an HTTPS server that returns the hostname of the application server as the response. The default hostname of a Pod is the name of the Pod. The container also handles graceful termination.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f web-deployment.yaml
         




### Deploying a Service as a Network Endpoint Group (NEG)

In this section, you create a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) resource. The Service selects the backend containers by their labels so that the Ingress controller can program them as backend endpoints. Ingress for internal Application Load Balancers requires you to use [NEGs](https://docs.cloud.google.com/load-balancing/docs/negs) as backends. The feature does not support Instance Groups as backends. Because NEG backends are required, the following NEG annotation is required when you deploy Services that are exposed through Ingress:
    
    
    annotations:
      cloud.google.com/neg: '{"ingress": true}'
    

Your Service is automatically annotated with `cloud.google.com/neg: '{"ingress": true}'` when all of the following conditions are true:

  * You are using VPC-native clusters.
  * You are not using a Shared VPC.
  * You are not using [GKE Network Policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).



The annotation is automatically added using a `MutatingWebhookConfiguration` with name `neg-annotation.config.common-webhooks.networking.gke.io`. You can check if the `MutatingWebhookConfiguration` is present with the following command:
    
    
    kubectl get mutatingwebhookconfigurations
    

The usage of NEGs allows the Ingress controller to perform [container native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native_load_balancing). Traffic is load balanced from the Ingress proxy directly to the Pod IP as opposed to traversing the node IP or kube-proxy networking. In addition, [Pod readiness gates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing#pod_readiness) are implemented to determine the health of Pods from the perspective of the load balancer and not only the Kubernetes readiness and liveness checks. Pod readiness gates ensure that traffic is not dropped during lifecycle events such as Pod startup, Pod loss, or node loss.

If you do not include a NEG annotation, you receive a warning on the Ingress object that prevents you from configuring the internal Application Load Balancer. A Kubernetes event is also generated on the Ingress if the NEG annotation is not included. The following message is an example of the event message:
    
    
    Message
    -------
    error while evaluating the ingress spec: could not find port "8080" in service "default/no-neg-svc"
    

An NEG is not created until an Ingress references the Service. The NEG does not appear in Compute Engine until the Ingress and its referenced Service both exist. NEGs are a zonal resource and for multi-zonal clusters, one is created per Service per zone.

To create a Service:

  1. Save the following sample manifest as `web-service.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: hostname
           namespace: default
           annotations:
             cloud.google.com/neg: '{"ingress": true}'
         spec:
           ports:
           - name: host1
             port: 80
             protocol: TCP
             targetPort: 9376
           selector:
             app: hostname
           type: ClusterIP
         

  2. Apply the manifest to the cluster:
         
         kubectl apply -f web-service.yaml
         




### Deploying Ingress

In this section, you create an Ingress resource that triggers the deployment of a Compute Engine load balancer through the Ingress controller. Ingress for internal Application Load Balancers requires the following annotation:
    
    
    annotations:
        kubernetes.io/ingress.class: "gce-internal"
    

You cannot use the `ingressClassName` field to specify a GKE Ingress. You must use the `kubernetes.io/ingress.class` annotation. For more information, see [GKE Ingress controller behavior](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#controller_summary).

**Caution:** Any Ingress resource deployed on GKE without the `kubernetes.io/ingress.class` annotation is interpreted as an external Ingress resource which deploys an external load balancer for the Service. To prevent users from exposing applications publicly by accidentally omitting the correct annotation, implement an [Identity and Access Management (IAM) policy](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions) that enforces limits on public load balancer creation. This policy blocks public load balancer deployment cluster-wide while still allowing internal load balancer creation through Ingress and Service resources.

To create an Ingress:

  1. Save the following sample manifest as `internal-ingress.yaml`:
         
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: ilb-demo-ingress
           namespace: default
           annotations:
             kubernetes.io/ingress.class: "gce-internal"
         spec:
           defaultBackend:
             service:
               name: hostname
               port:
                 number: 80
         

  2. Apply the manifest to the cluster:
         
         kubectl apply -f internal-ingress.yaml
         




### Validating a successful Ingress deployment

In this section, you validate if your deployment was successful.

It can take several minutes for the Ingress resource to become fully provisioned. During this time, the Ingress controller creates items such as forwarding rules, backend services, URL maps, and NEGs.

To retrieve the status of your Ingress resource that you created in the previous section, run the following command:
    
    
    kubectl get ingress ilb-demo-ingress
    

The output is similar to the following:
    
    
    NAME               HOSTS    ADDRESS            PORTS     AGE
    ilb-demo-ingress   *        10.128.0.58        80        59s
    

When the `ADDRESS` field is populated, the Ingress is ready. The use of an RFC 1918 address in this field indicates an internal IP within the VPC.

Since the internal Application Load Balancer is a regional load balancer, the virtual IP (VIP) is only accessible from a client within the same region and VPC. After retrieving the load balancer VIP, you can use tools (for example, `curl`) to issue `HTTP GET` calls against the VIP from inside the VPC.

To issue a `HTTP GET` call, complete the following steps:

  1. To reach your Ingress VIP from inside the VPC, deploy a VM within the same region and network as the cluster:
         
         gcloud compute instances create l7-ilb-client \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --network=NETWORK_NAME \
             --subnet=SUBNET_NAME \
             --zone=COMPUTE_ZONE \
             --tags=allow-ssh
         

Replace the following:

     * `SUBNET_NAME`: the name of a subnet in the network.
     * `COMPUTE_ZONE`: a [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) in the region.

To learn more about creating instances, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  2. To access the internal VIP from inside the VM, use `curl`:

     1. SSH in to the VM that you created in the previous step:
            
            gcloud compute ssh l7-ilb-client \
                --zone=COMPUTE_ZONE
            

     2. Use `curl` to access the internal application VIP:
            
            curl 10.128.0.58
            hostname-server-6696cf5fc8-z4788
            

The successful HTTP response and hostname of one of the backend containers indicates that the full load balancing path is functioning correctly.




### Deleting Ingress resources

Removing Ingress and Service resources also removes the Compute Engine load balancer resources associated with them. To prevent resource leaking, ensure that Ingress resources are torn down when you no longer need them. You must also delete Ingress and Service resources before you delete clusters or else the Compute Engine load balancing resources are orphaned.

To remove an Ingress, complete the following steps:

  1. Delete the Ingress. For example, to delete the Ingress you created in this page, run the following command:
         
         kubectl delete ingress ilb-demo-ingress
         

Deleting the Ingress removes the forwarding rules, backend services, and URL maps associated with this Ingress resource.

  2. Delete the Service. For example, to delete the Service you created in this page, run the following command:
         
         kubectl delete service hostname
         

Deleting the Service removes the NEG associated with the Service.




To deploy an application on GKE and expose the application with a private load balanced IP address, see [Basic Internal Ingress](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-internal-basic).

## Static IP addressing

Internal Ingress resources support both static and ephemeral IP addressing. If an IP address is not specified, an available IP address is automatically allocated from the GKE node subnet. However, the Ingress resource does not provision IP addresses from the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure-a-network) as that subnet is only used for internal proxy consumption. These ephemeral IP addresses are allocated to the Ingress only for the lifecycle of the internal Ingress resource. If you delete your Ingress and create a new Ingress from the same manifest file, you are not guaranteed to get the same external IP address.

If you want a permanent IP address that's independent from the lifecycle of the internal Ingress resource, you must reserve a regional static internal IP address. You can then specify a static IP address by using the `kubernetes.io/ingress.regional-static-ip-name` annotation on your Ingress resource.

The following example shows you how to add this annotation:
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-ingress
      annotations:
        kubernetes.io/ingress.regional-static-ip-name: STATIC_IP_NAME
        kubernetes.io/ingress.class: "gce-internal"
    

Replace `STATIC_IP_NAME` with a static IP name that meets the following criteria:

  * Create the static IP address before you deploy the Ingress. A load balancer does not deploy until the static IP exists, and referencing a non-existent IP address resource does not create a static IP. If you modify an existing Ingress to use a static IP address instead of an ephemeral IP address, GKE might change the IP address of the load balancer when GKE re-creates the forwarding rule of the load balancer.
  * The static IP is [reserved in the service project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#reserve_internal_ip) for an Ingress deployed in the service project of a Shared VPC.
  * Reference the Google Cloud IP address resource by its name, rather than its IP address.
  * The IP address must be from a subnet in the same region as the GKE cluster. You can use any available private subnet within the region (with the exception of the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure-a-network)). Different Ingress resources can also have addresses from different subnets.



## HTTPS between client and load balancer

Ingress for internal load balancing supports the serving of TLS certificates to clients. You can serve TLS certificates through Kubernetes Secrets or through pre-shared regional SSL certificates in Google Cloud. You can also specify multiple certificates per Ingress resource. Use of both HTTPS and HTTP simultaneously is supported for GKE 1.25+. To enable this feature, you need to create a static IP address with PURPOSE=SHARED_LOADBALANCER_VIP, and configure it on the ingress. If a static IP address is not provided, only HTTPS traffic is allowed, and you need to follow the documentation for [Disabling HTTP](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#disabling_http).

**Note:** Ingress for internal load balancing does not support pre-shared global SSL certificates or Google-managed certificates.

The following steps detail how to create a certificate in Google Cloud and then serve it through Ingress to internal clients for both HTTPS and HTTP traffic:

  1. Create the regional certificate:
         
         gcloud compute ssl-certificates create CERT_NAME \
             --certificate CERT_FILE_PATH \
             --private-key KEY_FILE_PATH \
             --region COMPUTE_REGION
         

Replace the following:

     * `CERT_NAME`: a name for your certificate that you choose.
     * `CERT_FILE_PATH`: the path to your local certificate file to create a self-managed certificate. The certificate must be in PEM format.
     * `KEY_FILE_PATH`: the path to a local private key file. The private key must be in PEM format and must use RSA or ECDSA encryption.
     * `COMPUTE_REGION`: a Compute Engine region for your certificate.
  2. Reserve and apply a static IP address following Static IP addressing.

  3. Save the following sample manifest as `ingress-pre-shared-cert.yaml`:
         
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: ilb-demo-ing
           namespace: default
           annotations:
             ingress.gcp.kubernetes.io/pre-shared-cert: "CERT_NAME"
             kubernetes.io/ingress.regional-static-ip-name: STATIC_IP_NAME
             kubernetes.io/ingress.class: "gce-internal"
         spec:
           rules:
           - host: DOMAIN
             http:
               paths:
               - pathType: ImplementationSpecific
                 backend:
                   service:
                     name: SERVICE_NAME
                     port:
                       number: 80
         

Replace the following:

     * `DOMAIN`: your domain.
     * `CERT_NAME`: the name of the certificate you created in the previous section.
     * `SERVICE_NAME`: the name of your Service.
  4. Apply the manifest to the cluster:
         
         kubectl apply -f ingress-pre-shared-cert.yaml
         




## HTTPS between load balancer and application

If your application runs in a GKE Pod and can receive HTTPS requests, you can configure the load balancer to use HTTPS when it forwards requests to your application. For more information, see [HTTPS (TLS) between load balancer and your application](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb#https_tls_between_load_balancer_and_your_application).

## Shared VPC

### Manually add the NEG annotation

If the GKE in which you are deploying the Ingress resources is in a Shared VPC service project, the services are not automatically annotated with the annotation `cloud.google.com/neg: '{"ingress": true}'` because the `MutatingWebhookConfiguration` responsible for injecting the annotation to the services is not installed.

You must add the NEG annotation to the manifest of the Services that are exposed through Ingress for internal Application Load Balancers.

### VPC firewall rules

If the GKE cluster in which you are deploying the Ingress resources is in a Shared VPC service project, and you want the GKE control plane to manage the firewall resources in your host project, then the service project's GKE service account must be granted the appropriate IAM permissions in the host project as per [Managing firewall resources for clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#managing_firewall_resources). This lets the Ingress controller create firewall rules to allow ingress traffic for Google Cloud health checks.

The following is an example of an event that might be present in the Ingress resource logs. This error occurs when the Ingress controller is unable to create a firewall rule to allow ingress traffic for Google Cloud health checks if the permissions are not configured correctly.
    
    
    Firewall change required by security admin: `gcloud compute firewall-rules update <RULE_NAME> --description "GCE L7 firewall rule" --allow tcp:<PORT> --source-ranges 130.211.0.0/22,35.191.0.0/16 --target-tags <TARGET_TAG> --project <HOST_PROJECT>
    

If you prefer to [manually provision firewall rules from the host project](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#manually_provision_firewall_rules_from_the_host_project), then you can mute the `firewallXPNError` events by adding the `networking.gke.io/suppress-firewall-xpn-error: "true"` annotation to the Ingress resource.

## Summary of internal Ingress annotations

The following tables show you the annotations that you can add when you are creating Ingress and Service resources for Ingress for internal Application Load Balancers.

### Ingress annotations

**Annotation** | **Description**  
---|---  
`kubernetes.io/ingress.class` | You can set as `"gce-internal"` for internal Ingress. If the class is not specified, an Ingress resource is interpreted by default as an external Ingress. For more information, see [ GKE Ingress controller behavior.](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#controller_summary)  
`kubernetes.io/ingress.allow-http` | You can allow HTTP traffic between the client and the HTTP(S) load balancer. Possible values are `true` and `false`. The default value is `true`. For more information, see [Disabling HTTP](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#disabling_http).  
`ingress.gcp.kubernetes.io/pre-shared-cert` | You can upload certificates and keys to your Google Cloud project. Use this annotation to reference the certificates and keys. For more information, see [Using multiple SSL certificates with external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl).  
`networking.gke.io/suppress-firewall-xpn-error` |  In [GLBC 1.4](https://github.com/kubernetes/ingress-gce) and later, you can mute the `firewallXPNError` event. For Ingress Load Balancers, if Kubernetes can't change the firewall rules due to insufficient permission, a `firewallXPNError` event is created every several minutes.  Add `networking.gke.io/suppress-firewall-xpn-error: "true"` annotation to the ingress resource. The default value is `false`. You can remove this annotation to unmute.   
`kubernetes.io/ingress.regional-static-ip-name` | You can specify a static IP address to provision your internal Ingress resource. For more information, see [Static IP addressing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress#static_ip_addressing).  
  
### Service annotations related to Ingress

**Annotation** | **Description**  
---|---  
`cloud.google.com/backend-config` | Use this annotation to configure the backend service associated with a servicePort. For more information, see [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).  
`cloud.google.com/neg` | Use this annotation to specify that the load balancer should use network endpoint groups. For more information, see [Using Container-native Load Balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).  
  
## Troubleshooting

Understanding and observing the state of Ingress typically involves inspecting the associated resources. The types of issues encountered often include load balancing resources not being created properly, traffic not reaching backends, or backends not appearing healthy.

Some common troubleshooting steps include:

  * Verifying that client traffic is originating from within the same region and VPC as the load balancer.
  * Verifying that the Pods and backends are healthy.
  * Validating the traffic path to the VIP and for Compute Engine health checks to ensure it is not blocked by firewall rules.
  * Checking the Ingress resource events for errors.
  * Describing the Ingress resource to see the mapping to Compute Engine resources.
  * Validating that the Compute Engine load balancing resources exist, have the correct configurations, and do not have errors reported.



### Filtering for Ingress events

The following query filters for errors across all Ingress events in your cluster:
    
    
    kubectl get events --all-namespaces --field-selector involvedObject.kind=Ingress
    

You can also filter by objects or object names:
    
    
    kubectl get events --field-selector involvedObject.kind=Ingress,involvedObject.name=hostname-internal-ingress
    

In the following error, you can see that the Service referenced by the Ingress does not exist:
    
    
    LAST SEEN   TYPE      REASON      OBJECT                              MESSAGE
    0s          Warning   Translate   ingress/hostname-internal-ingress   error while evaluating the ingress spec: could not find service "default/hostname-invalid"
    

### Inspecting Compute Engine load balancer resources

The following command displays the full output for the Ingress resource so that you can see the mappings to the Compute Engine resources that are created by the Ingress controller:
    
    
    kubectl get ing INGRESS_FILENAME -o yaml
    

Replace `INGRESS_FILENAME` with your Ingress resource's filename.

The output is similar to the following:
    
    
    apiVersion: v1
    items:
    - apiVersion: networking.k8s.io/v1
      kind: Ingress
      metadata:
        annotations:
          **ingress.kubernetes.io/backends: '{"k8s1-241a2b5c-default-hostname-80-29269aa5":"HEALTHY"}'
          ingress.kubernetes.io/forwarding-rule: k8s-fw-default-ilb-demo-ingress--241a2b5c94b353ec
          ingress.kubernetes.io/target-proxy: k8s-tp-default-ilb-demo-ingress--241a2b5c94b353ec
          ingress.kubernetes.io/url-map: k8s-um-default-ilb-demo-ingress--241a2b5c94b353ec**
          kubectl.kubernetes.io/last-applied-configuration: |
           {"apiVersion":"networking.k8s.io/v1","kind":"Ingress","metadata":{"annotations":{"kubernetes.io/ingress.class":"gce-internal"},"name":"ilb-demo-ingress","namespace":"default"},"spec":{"defaultBackend":{"service":{"name":"hostname"},"port":{"number":80}}}}
          kubernetes.io/ingress.class: gce-internal
        creationTimestamp: "2019-10-15T02:16:18Z"
        finalizers:
        - networking.gke.io/ingress-finalizer
        generation: 1
        name: ilb-demo-ingress
        namespace: default
        resourceVersion: "1538072"
        selfLink: /apis/networking.k8s.io/v1/namespaces/default/ingresses/ilb-demo-ingress
        uid: 0ef024fe-6aea-4ee0-85f6-c2578f554975
      spec:
        defaultBackend:
          service:
            name: hostname
            port:
              number: 80
      status:
        loadBalancer:
          ingress:
          - ip: 10.128.0.127
    kind: List
    metadata:
      resourceVersion: ""
      selfLink: ""
    

The `ingress.kubernetes.io/backends` annotations list the backends and their status. Make sure that your backends are listed as `HEALTHY`.

The Compute Engine resources created by the Ingress can be queried directly to understand their status and configuration. Running these queries can also be helpful when troubleshooting.

To list all Compute Engine forwarding rules:
    
    
    gcloud compute forwarding-rules list
    

The output is similar to the following:
    
    
    NAME                                                        REGION       IP_ADDRESS      IP_PROTOCOL  TARGET
    k8s-fw-default-hostname-internal-ingress--42084f6a534c335b  REGION_NAME  10.128.15.225   TCP          REGION_NAME/targetHttpProxies/k8s-tp-default-hostname-internal-ingress--42084f6a534c335b
    

To list the health of a backend service, first list the backend services, and make a copy of the name of the backend service you want to inspect:
    
    
    gcloud compute backend-services list
    

The output is similar to the following:
    
    
    NAME                                         BACKENDS                                                                       PROTOCOL
    k8s1-42084f6a-default-hostname-80-98cbc1c1   REGION_NAME/networkEndpointGroups/k8s1-42084f6a-default-hostname-80-98cbc1c1 HTTP
    

You can now use the backend service name to query its health:
    
    
    gcloud compute backend-services get-health k8s1-42084f6a-default-hostname-80-98cbc1c1 \
        --region COMPUTE_REGION
    

Replace `COMPUTE_REGION` with the Compute Engine region of the backend service.

The output is similar to the following:
    
    
    backend: https://www.googleapis.com/compute/v1/projects/user1-243723/zones/ZONE_NAME/networkEndpointGroups/k8s1-42084f6a-default-hostname-80-98cbc1c1
    status:
      healthStatus:
      - healthState: HEALTHY
    

## What's next

  * Learn about [GKE Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress).

  * Read a conceptual overview of [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) in GKE.

  * Learn how to create an [internal passthrough Network Load Balancer on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).

  * Implement a [basic internal Ingress](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-internal-basic).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
