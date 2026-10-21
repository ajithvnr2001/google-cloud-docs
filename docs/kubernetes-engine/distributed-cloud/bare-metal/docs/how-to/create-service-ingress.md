---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress/
title: Create a Service and an Ingress \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:51.814180+00:00
---

# Create a Service and an Ingress  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create a Service and an Ingress Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create a Kubernetes [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) object in a user, hybrid, or standalone cluster for Google Distributed Cloud. An Ingress is associated with one or more [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), each of which is associated with a set of [Pods](https://kubernetes.io/docs/concepts/workloads/pods).

## Create a Deployment

Use the following steps to create a Deployment:

  1. Create a Deployment manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: hello-deployment
         spec:
           selector:
             matchLabels:
               greeting: hello
           replicas: 3
           template:
             metadata:
               labels:
                 greeting: hello
             spec:
               containers:
               - name: hello-world
                 image: "gcr.io/google-samples/hello-app:2.0"
                 env:
                 - name: "PORT"
                   value: "50000"
               - name: hello-kubernetes
                 image: "gcr.io/google-samples/node-hello:1.0"
                 env:
                 - name: "PORT"
                   value: "8080"
         

For the purpose of this exercise, these are the important points to understand about the Deployment manifest:

     * Each Pod that belongs to the Deployment has the `greeting: hello` label.

     * Each Pod has two containers.

     * The `env` fields specify that the `hello-app` containers listen on TCP port 50000, and the `node-hello` containers listen on TCP port 8080. For `hello-app`, you can see the effect of the `PORT` environment variable by looking at the [source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/master/quickstarts/hello-app/main.go).

  2. Copy the manifest to a file named `hello-deployment.yaml`.

  3. Create the Deployment:
         
         kubectl apply --kubeconfig CLUSTER_KUBECONFIG -f hello-deployment.yaml
         

Replace `CLUSTER_KUBECONFIG` with the name of the kubeconfig file for your cluster.




## Expose your Deployment with a Service

To provide a stable way for clients to send requests to the Pods of your Deployment, create a Service:

  1. Create a Service manifest that exposes your Deployment to clients inside your cluster:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: hello-service
         spec:
           type: ClusterIP
           selector:
             greeting: hello
           ports:
           - name: world-port
             protocol: TCP
             port: 60000
             targetPort: 50000
           - name: kubernetes-port
             protocol: TCP
             port: 60001
             targetPort: 8080
         

  2. Copy the manifest to a file named `hello-service.yaml`.

  3. Create the Service:
         
         kubectl apply --kubeconfig CLUSTER_KUBECONFIG -f hello-service.yaml
         

Replace `CLUSTER_KUBECONFIG` with the name of the kubeconfig file for your cluster.

  4. View the Service:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get service hello-service --output yaml
         

The output shows the value of `clusterIP` that has been given to the Service. For example:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             ...
         spec:
           clusterIP: 10.96.14.249
           clusterIPs:
           - 10.96.14.249
           ipFamilies:
           - IPv4
           ipFamilyPolicy: SingleStack
           ports:
           - name: world-port
             port: 60000
             protocol: TCP
             targetPort: 50000
           - name: kubernetes-port
             port: 60001
             protocol: TCP
             targetPort: 8080
           selector:
             greeting: hello
           sessionAffinity: None
           type: ClusterIP
         status:
           loadBalancer: {}
         

In the preceding output, the `ports` field is an array of `ServicePort` objects: one named `world-port` and one named `kubernetes-port`. For more information about the Service fields, see [ServiceSpec](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceSpec) in the Kubernetes documentation.

These are the ways a client can call the Service:

     * **Using`world-port`:** A client running on one of the cluster nodes sends a request to the `clusterIP` on `port` (such as `10.96.14.249:60000`). The ingress controller forwards the request to a member Pod on `targetPort` (such as `POD_IP_ADDRESS:50000`, where `POD_IP_ADDRESS` is the IP address of a member Pod).

     * **Using`kubernetes-port`**: A client running on one of the cluster nodes sends a request to the `clusterIP` on `port` (`10.96.14.249:60001`). The ingress controller forwards the request to a member Pod on `targetPort` (`POD_IP_ADDRESS:8080`).




## Ingress components

These are some of the cluster components related to ingress:

**Note:** The Istio components that are preinstalled on Google Distributed Cloud support ingress only. These components are not intended to provide general service mesh capabilities. For information on setting up a fully functional service mesh, see [Setup](https://istio.io/latest/docs/setup/) in the Istio documentation or [Set up a multi-cluster mesh outside Google Cloud](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup) in the Cloud Service Mesh documentation.

  * The `istio-ingress` Deployment. This is the _ingress proxy_. The ingress proxy forwards traffic to internal Services according to rules specified in an Ingress object.

  * The `istio-ingress` Service. This Service exposes the `istio-ingress` Deployment.

  * The `istiod` Deployment. This is the _ingress controller_. The ingress controller watches the creation of [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) objects and configures the ingress proxy accordingly.




All of these Istio in-cluster components are installed in the `gke-system` namespace. This namespace doesn't conflict with a full Istio/Cloud Service Mesh installation.

## Create an Ingress

Use the following steps to create an Ingress:

  1. Create an Ingress manifest:
         
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: my-ingress
         spec:
           rules:
           - http:
               paths:
               - path: /greet-the-world
                 pathType: Exact
                 backend:
                   service:
                     name: hello-service
                     port:
                       number: 60000
               - path: /greet-kubernetes
                 pathType: Exact
                 backend:
                   service:
                     name: hello-service
                     port:
                       number: 60001
         

  2. Copy the manifest to a file named `my-ingress.yaml`.

  3. Create the Ingress:
         
         kubectl apply --kubeconfig CLUSTER_KUBECONFIG -f my-ingress.yaml
         




When you create a user cluster, you specify a value for `loadbalancer.ingressVIP` in the cluster configuration file. This IP address is configured on the cluster load balancer. When you create an Ingress, the Ingress is given this same VIP as its external IP address.

When a client sends a request to your user cluster ingress VIP, the request is routed to your load balancer. The load balancer uses the `istio-ingress` Service to forward the request to the ingress proxy, which runs in your user cluster. The ingress proxy forwards the request to different backends depending on the path in the request URL.

### The `/greet-the-world` path

In your Ingress manifest, you can see a rule that says the path `/greet-the-world` is associated with `serviceName: hello-service` and `servicePort: 60000`. Recall that 60000 is the `port` value in the `world-port` section of your `hello-service` Service.
    
    
    - name: world-port
        port: 60000
        protocol: TCP
        targetPort: 50000
    

The ingress Service forwards the request to `clusterIP`:50000. The request then goes to one of the member Pods of the `hello-service` Service. The container, in that Pod, listening on port 50000 displays a `Hello World!` message.

### The `/greet-kubernetes` path

In your Ingress manifest, you can see a rule that says the path `/greet-kubernetes` is associated with `serviceName: hello-service` and `servicePort: 60001`. Recall that 60001 is the `port` value in the `kubernetes-port` section of your `hello-service` Service.
    
    
    - name: kubernetes-port
        port: 60001
        protocol: TCP
        targetPort: 8080
    

The ingress Service forwards the request to `clusterIP`: 8080. The request then goes to one of the member Pods of the `hello-service` Service. The container in that Pod, listening on port `8080`, displays a `Hello Kubernetes!` message.

## Test the Ingress

  1. Test the Ingress using the `/greet-the-world` path:
         
         curl CLUSTER_INGRESS_VIP/greet-the-world
         

Replace `CLUSTER_INGRESS_VIP` with the external IP address of the Ingress.

The output shows a `Hello, world!` message:
         
         Hello, world!
         Version: 2.0.0
         Hostname: ...
         

  2. Test the Ingress using the `/greet-kubernetes` path:
         
         curl CLUSTER_INGRESS_VIP/greet-kubernetes
         

The output shows a `Hello, Kubernetes!` message:
         
         Hello Kubernetes!
         




## Disable bundled Ingress

The Ingress capability bundled with Google Distributed Cloud supports ingress capabilities only. You may choose to integrate with [Istio](https://istio.io/latest/docs/setup/) or [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup). These products offer additional benefits of a fully functional service mesh, such as mutual Transport Layer Security (mTLS), ability to manage authentication between services, and workload observability. If you integrate with Istio or Cloud Service Mesh, we recommend that you disable the bundled Ingress capability.

You can enable or disable bundled Ingress with the `spec.clusterNetwork.bundledIngress` field in your cluster configuration file. This field is available to version 1.13.0 clusters and higher only. The `bundledIngress` field defaults to `true` and isn't present in the generated cluster configuration file. This field is mutable and can be changed when you create or update a version 1.13.0 or higher cluster.

  * To disable the bundled Ingress capability, add the `bundledIngress` field to the `clusterNetwork` section of your cluster configuration file and set its value to false, as shown in the following example:
        
        apiVersion: v1
        kind: Namespace
        metadata:
          name: cluster-hybrid-basic
        ---
        apiVersion: baremetal.cluster.gke.io/v1
        kind: Cluster
        metadata:
          name: hybrid-basic
          namespace: cluster-hybrid-basic
        spec:
          type: hybrid
          profile: default**  anthosBareMetalVersion: 1.13.0**
          gkeConnect:
            projectID: project-fleet
          controlPlane:
            nodePoolSpec:
              nodes:
              - address: 10.200.0.2
          clusterNetwork:**    bundledIngress: false**
            pods:
              cidrBlocks:
              - 192.168.0.0/16
            services:
              cidrBlocks:
              - 10.96.0.0/20
        ...
        




## Set up HTTPS for Ingress

If you want to accept HTTPS requests from your clients, the ingress proxy must have a certificate so it can prove its identity to your clients. This proxy must also have a private key to complete the HTTPS handshake.

The following example uses these entities:

  * Ingress proxy: Participates in the HTTPS handshake, and then forwards packets to member Pods of the `hello-service` Service.

  * Domain for the `hello-service` Service: altostrat.com in Example Org




Follow these steps:

  1. Create a root certificate and private key. This example uses a root certificate authority of `root.ca.example.com` in Root CA Example Org.
         
         openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj \
             '/O=Root CA Example Inc./CN=root.ca.example.com' -keyout root-ca.key \
             -out root-ca.crt
         

  2. Create a certificate signing request:
         
         openssl req -out server.csr -newkey rsa:2048 -nodes -keyout server.key -subj \
              "/CN=altostrat.com/O=Example Org"
         

  3. Create a serving certificate for the ingress proxy.
         
         openssl x509 -req -days 365 -CA root-ca.crt -CAkey root-ca.key -set_serial 0 \
             -in server.csr -out server.crt
         

You have now created the following certificates and keys:

     * `root-ca.crt`: Certificate for the root CA
     * `root-ca.key`: Private key for the root CA
     * `server.crt`: Serving certificate for the ingress proxy
     * `server.key`: Private key for the ingress proxy
  4. Create a Kubernetes Secret that holds the serving certificate and key.
         
         kubectl create secret tls example-server-creds --key=server.key --cert=server.crt \
             --namespace gke-system
         

The resulting Secret is named `example-server-creds`.

**Note:** TLS secrets must be defined in the `gke-system` namespace.



### Create a Deployment and Service

If you created a Deployment and a Service in the HTTP portion of this guide, leave those in place. If you did not, create them now, following the steps described for HTTP.

### Create an Ingress

Creating an Ingress for HTTPS is similar to creating an Ingress for HTTP, but the Ingress spec for HTTPS includes a `tls` section that specifies the host and a Secret. The `hosts` in the `tls` section need to explicitly match the `host` in the `rules` section.

**Warning:** Don't create multiple Ingresses for the same host. When you use the bundled ingress components, you're limited to a single Ingress custom resource for a given host.

If your backend Service is in a separate namespace, then you need to create a [Service of type ExternalName](https://kubernetes.io/docs/concepts/services-networking/service/#externalname) in the same namespace as the Ingress to route traffic to the backend Service.

The overall steps for creating an Ingress for HTTPS or HTTP are the same, except for what you configure in the manifest file:

  1. If you previously created an Ingress in the HTTP portion of this document, delete that Ingress before proceeding.
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG delete ingress my-ingress
         

  2. To handle traffic for the Service that you created previously, create a new Ingress manifest that has a `tls` section:

The `tls` configuration enables HTTPS between clients and the ingress proxy.
         
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: my-ingress-2
         spec:
           tls:
           - hosts:
             - altostrat.com
             secretName: example-server-creds
           rules:
           - host: altostrat.com
             http:
               paths:
               - path: /greet-the-world
                 pathType: Exact
                 backend:
                   service:
                     name: hello-service
                     port:
                       number: 60000
               - path: /greet-kubernetes
                 pathType: Exact
                 backend:
                   service:
                     name: hello-service
                     port:
                       number: 60001
         

  3. Save the manifest in a file named `my-ingress-2.yaml`, and create the Ingress:
         
         kubectl apply --kubeconfig CLUSTER_KUBECONFIG -f my-ingress-2.yaml
         

  4. Confirm that the Ingress was created and is working properly by testing:

     * Test the `/greet-the-world` path:
           
           curl -v --resolve altostrat.com:443:CLUSTER_INGRESS_VIP \
               https://altostrat.com/greet-the-world \
               --cacert root-ca.crt
           

Output:
           
           Hello, world!
           Version: 2.0.0
           Hostname: hello-deployment-5ff7f68854-wqzp7
           

     * Test the `/greet-kubernetes` path:
           
           curl -v --resolve altostrat.com:443:CLUSTER_INGRESS_VIP \
               https://altostrat.com/greet-kubernetes --cacert root-ca.crt
           

Output:
           
           Hello Kubernetes!
           




## Create a LoadBalancer Service

A Service of type `LoadBalancer` is another way to expose your workloads outside of your cluster. For instructions and an example for creating a service of type `LoadBalancer`, see [Create a Service of type `LoadBalancer` in Deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/deploy-app#lb_svc).

## Cleaning up

  1. Delete your Ingress:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG delete ingress INGRESS_NAME
         

Replace `INGRESS_NAME` with the name of the Ingress, such as `my-ingress` or `my-ingress-2`.

  2. Delete your Service:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG delete service hello-service
         

  3. Delete your Deployment:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG delete deployment hello-deployment
         

  4. Delete your LoadBalancer Service:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG delete service service-does-not-use-nodeports
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
