---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress/
title: Configure Ingress for external Application Load Balancers \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:27.117701+00:00
---

# Configure Ingress for external Application Load Balancers  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure Ingress for external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to configure an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) by creating a Kubernetes Ingress object.

Before reading this page, ensure that you're familiar with [GKE networking concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



### Enable the `HttpLoadBalancing` add-on

Your cluster must have the `HttpLoadBalancing` add-on enabled. This add-on is enabled by default. In Autopilot clusters, you can't disable this add-on.

You can enable the `HttpLoadBalancing` add-on using the Google Cloud console or the Google Cloud CLI.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. Under **Networking** , in the **HTTP Load Balancing** field, click _edit_ **Edit HTTP Load Balancing**.

  4. Select the **Enable HTTP load balancing** checkbox.

  5. Click **Save Changes**.




### gcloud
    
    
    gcloud container clusters update CLUSTER_NAME --update-addons=HttpLoadBalancing=ENABLED
    

Replace `CLUSTER_NAME` with the name of your cluster.

### Create a static IP address

An external Application Load Balancer provides one stable IP address that you can use to route requests to one or more Services. If you want a permanent IP address, you must reserve a [global static external IP address](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#static_ip_addresses_for_https_load_balancers) before you create an Ingress.

If you modify an existing Ingress to use a static IP address instead of an ephemeral IP address, GKE might change the IP address of the load balancer when GKE re-creates the forwarding rule of the load balancer.

## Create an external Application Load Balancer

In this exercise, you configure an external Application Load Balancer to route requests to different Services depending on the URL path.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/welcome?walkthrough_id=load-balancing--ext-https-load-balancer-ingress)

* * *

### Create Deployments and Services

Create two Deployments with Services named `hello-world-1` and `hello-world-2`:

  1. Save the following manifest as `hello-world-deployment-1.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: hello-world-deployment-1
         spec:
           selector:
             matchLabels:
               greeting: hello
               version: one
           replicas: 3
           template:
             metadata:
               labels:
                 greeting: hello
                 version: one
             spec:
               containers:
               - name: hello-app-1
                 image: "us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0"
                 env:
                 - name: "PORT"
                   value: "50000"
         

This manifest describes a sample Deployment with three replicas.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f hello-world-deployment-1.yaml
         

  3. Save the following manifest as `hello-world-service-1.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: hello-world-1
         spec:
           type: NodePort
           selector:
             greeting: hello
             version: one
           ports:
           - protocol: TCP
             port: 60000
             targetPort: 50000
         

This manifest describes a Service with the following properties:

     * Any Pod that has both the `greeting: hello` label and the `version: one` label is a member of the Service.
     * GKE forwards requests sent to the Service on TCP port 60000 to one of the member Pods on TCP port 50000.
     * The Service type is `NodePort`, which is required unless you're using [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native-load-balancing). If using container-native load balancing, there is no restriction on type of service, but we recommend that you use a Service of `type ClusterIP` unless you explicitly need the nodePort provided by a NodePort Service. LoadBalancer Services are not supported as Ingress backends.
  4. Apply the manifest to the cluster:
         
         kubectl apply -f hello-world-service-1.yaml
         

  5. Save the following manifest as `hello-world-deployment-2.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: hello-world-deployment-2
         spec:
           selector:
             matchLabels:
               greeting: hello
               version: two
           replicas: 3
           template:
             metadata:
               labels:
                 greeting: hello
                 version: two
             spec:
               containers:
               - name: hello-app-2
                 image: "us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0"
                 env:
                 - name: "PORT"
                   value: "8080"
         

This manifest describes a sample Deployment with three replicas.

  6. Apply the manifest to the cluster:
         
         kubectl apply -f hello-world-deployment-2.yaml
         

  7. Save the following manifest as `hello-world-service-2.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: hello-world-2
         spec:
           type: NodePort
           selector:
             greeting: hello
             version: two
           ports:
           - protocol: TCP
             port: 80
             targetPort: 8080
         

This manifest describes a Service with the following properties:

     * Any Pod that has both the `greeting: hello` label and the `version: two` label is a member of the Service.
     * GKE forwards requests sent to the Service on TCP port 80 to one of the member Pods on TCP port 8080.
  8. Apply the manifest to the cluster:
         
         kubectl apply -f hello-world-service-2.yaml
         




### Create an Ingress

Create an Ingress that specifies rules for routing requests depending on the URL path in the request. When you create the Ingress, the GKE Ingress controller creates and configures an external Application Load Balancer.

  1. Save the following manifest as `my-ingress.yaml`:
         
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: my-ingress
           annotations:
             # If the class annotation is not specified it defaults to "gce".
             kubernetes.io/ingress.class: "gce"
         spec:
           rules:
           - http:
               paths:
               - path: /*
                 pathType: ImplementationSpecific
                 backend:
                   service:
                     name: hello-world-1
                     port:
                       number: 60000
               - path: /v2
                 pathType: ImplementationSpecific
                 backend:
                   service:
                     name: hello-world-2
                     port:
                       number: 80
         

This manifest describes an Ingress with the following properties:

     * There are two GKE Ingress classes. To specify an Ingress class, you must use the `kubernetes.io/ingress.class` annotation. You cannot specify a GKE Ingress using `spec.ingressClassName`.

     * The `gce` class deploys an [external Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb).

     * The `gce-internal` class deploys an [internal Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb).

     * When you deploy an Ingress resource without the annotations `spec.ingressClassName` and `kubernetes.io/ingress.class`, GKE creates an external Application Load Balancer. This is the same behavior that occurs if you specify the `kubernetes.io/ingress.class: gce` annotation. For more information, see [GKE Ingress controller behavior](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#controller_summary).

     * GKE creates a [Google Cloud backend Service](https://docs.cloud.google.com/load-balancing/docs/backend-service) for each `backend.service`. Each of the backend services corresponds to a Kubernetes Service, and each backend service must reference a [Google Cloud health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts). This health check is _different_ from a Kubernetes liveness or readiness probe because the health check is implemented outside of the cluster. To learn more, see [Health checks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#health_checks)

     * When a client sends a request to the load balancer with URL path `/`, GKE forwards the request to the `hello-world-1` Service on port 60000. When a client sends a request to the load balancer using URL path `/v2`, GKE forwards the request to the `hello-world-2` Service on port 80. For more information about the `path` and `pathType` properties, see URL Paths.

     * If you want to reserve a [global static external IP address](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-routing-security#static_ip_addresses_for_https_load_balancers), include a `kubernetes.io/ingress.global-static-ip-name` annotation in the Ingress object as shown here:
    
    apiVersion: networking.k8s.io/v1
     kind: Ingress
     metadata:
       name: my-ingress
       annotations:
         **kubernetes.io/ingress.global-static-ip-name : my-static-address**
     ```
    

  2. Apply the manifest to the cluster:
         
         kubectl apply -f my-ingress.yaml
         




### Test the external Application Load Balancer

Wait about five minutes for the load balancer to be configured, then test the external Application Load Balancer:

  1. View the Ingress:
         
         kubectl get ingress my-ingress --output yaml
         

The output shows the IP address of the external Application Load Balancer:
         
         status:
           loadBalancer:
             ingress:
             - ip: 203.0.113.1
         

  2. Test the `/` path:
         
         curl LOAD_BALANCER_IP_ADDRESS/
         

Replace `LOAD_BALANCER_IP_ADDRESS` with the external IP address of the load balancer.

The output is similar to the following:
         
         Hello, world!
         Version: 1.0.0
         Hostname: ...
         

If the output includes a 404 error, wait a few minutes.

  3. Test the `/v2` path:
         
         curl load-balancer-ip/v2
         

The output is similar to the following:
         
         Hello, world!
         Version: 2.0.0
         Hostname: ...
         




## How Ingress for external load balancing works

This section describes the components and configurations that enable external load balancing for your GKE applications, including URL path matching, network endpoint groups, and Shared VPC integration.

### URL Paths

The only supported wildcard character for the `path` field of an Ingress is the `*` character. The `*` character must follow a forward slash (`/`) and must be the last character in the pattern. For example, `/*`, `/foo/*`, and `/foo/bar/*` are valid patterns, but `*`, `/foo/bar*`, and `/foo/*/bar` are not.

A more specific pattern takes precedence over a less specific pattern. If you have both `/foo/*` and `/foo/bar/*`, then `/foo/bar/bat` is taken to match `/foo/bar/*`. For more information about path limitations and pattern matching, see the [URL Maps documentation](https://docs.cloud.google.com/load-balancing/docs/url-map).

For GKE clusters running versions earlier than 1.21.3-gke.1600, the only supported value for the `pathType` field is `ImplementationSpecific`. For clusters running version 1.21.3-gke.1600 or later, `Prefix` and `Exact` values are also supported for `pathType`.

### Network endpoint groups

If your cluster supports [Container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native-load-balancing), we recommend that you use network endpoint groups (NEGs). When you create the Ingress, GKE creates an Application Load Balancer in the project, and NEGs are created in each zone where the cluster runs. The endpoints in the NEG and the endpoints of the Service are kept in sync. For GKE clusters 1.17 and later, container-native load balancing is default and does not require an explicit `cloud.google.com/neg: '{"ingress": true}'` Service annotation, under certain conditions. For clusters where NEGs are not the default, we still strongly recommend that you use container-native load balancing, but it must be enabled explicitly on a per-Service basis. The annotation should be applied to Services in the following manner:
    
    
    kind: Service
    ...
      annotations:
        cloud.google.com/neg: '{"ingress": true}'
    ...
    

When you add this annotation, a new BackendService is created for the existing Service. This can result in a temporary outage for your Service.

**Caution:** Don't remove or modify the `cloud.google.com/neg: '{"ingress": true}'` annotation after you apply it to a Service. For clusters where container-native load balancing is the default, GKE automatically adds this annotation to new Services. If you use third-party controllers or GitOps tools, configure these tools to ignore this annotation because removing or updating this annotation can cause service outages.

### Shared VPC

If the GKE cluster in which you are deploying the Ingress resources is in a service project, and you want the GKE control plane to manage the firewall resources in your host project, then the service project's GKE service account must be granted the appropriate IAM permissions in the host project as per [Managing firewall resources for clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#managing_firewall_resources). This lets the Ingress controller create firewall rules to allow both ingress traffic and traffic for Google Cloud health checks.

The following is an example of an event that might be present in the Ingress resource logs. This error occurs when the Ingress controller is unable to create a firewall rule to allow ingress traffic for Google Cloud health checks if the permissions are not configured correctly.
    
    
    Firewall change required by security admin: `gcloud compute firewall-rules update <RULE_NAME> --description "GCE L7 firewall rule" --allow tcp:<PORT> --source-ranges 130.211.0.0/22,35.191.0.0/16 --target-tags <TARGET_TAG> --project <HOST_PROJECT>
    

If you prefer to [manually provision firewall rules from the host project](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-routing-security#manually_provision_firewall_rules), then you can mute the `firewallXPNError` events by adding the `networking.gke.io/suppress-firewall-xpn-error: "true"` annotation to the Ingress resource.

## Summary of external Ingress annotations

You can use the following annotations to configure the behavior of your external Ingress resources and the associated Kubernetes Service objects.

### Ingress annotations

**Annotation** | **Description**  
---|---  
kubernetes.io/ingress.allow-http | Specifies whether to allow HTTP traffic between the client and the HTTP(S) load balancer. Possible values are "true" and "false". Default is "true". See [Disabling HTTP](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#disabling_http).  
ingress.gcp.kubernetes.io/pre-shared-cert |  Use this annotation to attach certificate resources to GKE Ingress resources. For more information, see [Using multiple SSL certificates with external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl).  
kubernetes.io/ingress.global-static-ip-name | Use this annotation to specify that the load balancer should use a static external IP address that you previously created. See [Static IP addresses for HTTP(S) load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#static_ip_addresses_for_https_load_balancers).  
networking.gke.io/v1beta1.FrontendConfig | Use this annotation to customize the client-facing configuration of the load balancer. For more information, see [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).  
networking.gke.io/suppress-firewall-xpn-error | For Ingress Load Balancers, if Kubernetes can't change the firewall rules due to insufficient permission, a `firewallXPNError` event is created every several minutes. In [GLBC 1.4](https://github.com/kubernetes/ingress-gce) and later, you can mute the `firewallXPNError` event by adding `networking.gke.io/suppress-firewall-xpn-error: "true"` annotation to the ingress resource. You can remove this annotation to unmute. Possible values are `true` and `false`. The default value is `false`.  
  
### Service annotations related to Ingress

**Annotation** | **Description**  
---|---  
cloud.google.com/app-protocols | Use this annotation to set the protocol for communication between the load balancer and the application. Possible protocols are HTTP, HTTPS, and HTTP2.  
cloud.google.com/backend-config | Use this annotation to configure the backend service associated with a Service. For more information, see [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).  
cloud.google.com/neg | Use this annotation to specify that the load balancer should use network endpoint groups. See [Using Container-native Load Balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).  
  
## What's next

  * Read a conceptual overview of [Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) in GKE.

  * Perform the tutorial on [Setting up an external Application Load Balancer with Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer).

  * Read a conceptual overview of [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) in GKE.

  * Implement a [basic external Ingress](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-external-basic).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
