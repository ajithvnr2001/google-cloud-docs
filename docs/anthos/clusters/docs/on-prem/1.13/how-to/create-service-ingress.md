---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-service-ingress/
title: Create a Service and an Ingress \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:13.354429+00:00
---

# Create a Service and an Ingress  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-service-ingress/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Create a Service and an Ingress Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-service-ingress)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-service-ingress)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create a Kubernetes [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) object in a user cluster for Google Distributed Cloud. An Ingress is associated with one or more [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), each of which is associated with a set of [Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod).

## Before you begin

Get an [SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation:

## Create a Deployment

Here's a manifest for a Deployment:
    
    
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

  * The `env` fields specify that the `hello-app` containers listen on TCP port 50000, and the `node-hello` containers listen on TCP port 8080. For `hello-app`, you can see the effect of the `PORT` environment variable by looking at the [hello-app source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/hello-app/main.go).




Copy the manifest to a file named `hello-deployment.yaml`, and create the Deployment:
    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f hello-deployment.yaml
    

where USER_CLUSTER_KUBECONFIG is the path of the [kubeconfig file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-user-cluster#locate-user-cluster-kubeconfig) for your user cluster.

## Expose your Deployment with a Service

To provide a stable way for clients to send requests to the Pods of your Deployment, create a Service.

Here's a manifest for a Service that exposes your Deployment to clients inside your cluster:
    
    
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
    

Copy the manifest to a file named `hello-service.yaml`, and create the Service:
    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f hello-service.yaml
    

View the Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get service hello-service --output yaml
    

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
    

In the preceding output, the `ports` field is an array of [ServicePort](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#serviceport-v1-core) objects: one named `world-port` and one named `kubernetes-port`.

These are the ways a client can call the Service:

  * **Using`world-port`:** A client running on one of the cluster nodes sends a request to the `clusterIP` on `port`. In this example, 10.96.14.249:60000. The request is forwarded to a member Pod on `targetPort`. In this example, POD_IP_ADDRESS:50000.

  * **Using`kubernetes-port`**: A client running on one of the cluster nodes sends a request to the `clusterIP` on `port`. In this example, 10.96.14.249:60001. The request is forwarded to a member Pod on `targetPort`. In this example, POD_IP_ADDRESS:8080.




## Ingress components

These are some of the cluster components related to ingress:

  * The `istio-ingress` Deployment. This is the _ingress proxy_. The ingress proxy forwards traffic to internal Services according to rules specified in an Ingress object.

  * The `istio-ingress` Service. This Service exposes the `istio-ingress` Deployment.

  * The `istiod` Deployment. This is the _ingress controller_. The ingress controller watches the creation of [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) objects and configures the ingress proxy accordingly.




## Create an Ingress

Here's a manifest for an Ingress:
    
    
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
    

Copy the manifest to a file named `my-ingress.yaml`, and create the Ingress:
    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f my-ingress.yaml
    

When you create a user cluster, you specify a value for `loadbalancer.ingressVip` in the cluster configuration file. This IP address is configured on the cluster load balancer. When you create an Ingress, the Ingress is given this same VIP as its external IP address.

When a client sends a request to your user cluster ingress VIP, the request is routed to your load balancer. The load balancer uses the `istio-ingress` Service to forward the request to the ingress proxy, which runs in your user cluster. The ingress proxy is configured to forward the request to different backends depending on the path in the request URL.

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
    

The ingress Service forwards the request to `clusterIP`: 8080. The request then goes to one of the member Pods of the `hello-service` Service. The container, in that Pod, listening on port 8080 displays a `Hello Kubernetes!` message.

## Test the Ingress

Test the Ingress using the `/greet-the-world` path:
    
    
    curl USER_CLUSTER_INGRESS_VIP/greet-the-world
    

Replace USER_CLUSTER_INGRESS_VIP with the external IP address of the Ingress.

The output shows a `Hello, world!` message:
    
    
    Hello, world!
    Version: 2.0.0
    Hostname: ...
    

Test the Ingress using the `/greet-kubernetes` path:
    
    
    curl USER_CLUSTER_INGRESS_VIP/greet-kubernetes
    

The output shows a `Hello, Kubernetes!` message:
    
    
    Hello Kubernetes!
    

## Set up HTTPS for Ingress

If you want to accept HTTPS requests from your clients, the ingress proxy must have a certificate so it can prove its identity to your clients. This proxy must also have a private key to complete the HTTPS handshake.

The following example uses these entities:

  * Ingress proxy: Participates in the HTTPS handshake, and then forwards packets to member Pods of the `hello-service` Service.

  * Domain for the `hello-service` Service: altostrat.com in Example Org




Follow these steps:

  1. Create a root certificate and private key. This example uses a root certificate authority of `root.ca.example.com` in Root CA Example Org.
         
         openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=Root CA Example Inc./CN=root.ca.example.com' -keyout root-ca.key -out root-ca.crt
         

  2. Create a certificate signing request:
         
         openssl req -out server.csr -newkey rsa:2048 -nodes -keyout server.key -subj "/CN=altostrat.com/O=Example Org"
         

  3. Create a serving certificate for the ingress proxy.
         
         openssl x509 -req -days 365 -CA root-ca.crt -CAkey root-ca.key -set_serial 0 -in server.csr -out server.crt
         

You have now created the following certificates and keys:

     * `root-ca.crt`: Certificate for the root CA
     * `root-ca.key`: Private key for the root CA
     * `server.crt`: Serving certificate for the ingress proxy
     * `server.key`: Private key for the ingress proxy
  4. Create a Kubernetes Secret that holds the serving certificate and key.
         
         kubectl create secret tls example-server-creds --key=server.key --cert=server.crt --namespace gke-system
         

The resulting Secret is named `example-server-creds`.

**Note:** TLS secrets must be defined in the `gke-system` namespace.



### Create a Deployment and Service

If you created a Deployment and a Service in the HTTP portion of this guide, leave those in place. If you did not, create them now, following the steps described for HTTP.

### Create an Ingress

If you previously created an Ingress in the HTTP portion, delete that Ingress before proceeding. 

Delete the Ingress:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete ingress my-ingress
    

To handle traffic for the Service that you created previously, create a new Ingres that has a `tls` section. This will enable HTTPS between clients and the ingress proxy.

Here's a manifest for an Ingress:
    
    
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
    

Save the manifest in a file named `my-ingress-2.yaml`, and create the Ingress:
    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f my-ingress-2.yaml
    

Confirm by testing.

  * Test the /greet-the-world path:
        
        curl -v --resolve altostrat.com:443:USER_CLUSTER_INGRESS_VIP https://altostrat.com/greet-the-world --cacert root-ca.crt
        

Output:
        
        Hello, world!
        Version: 2.0.0
        Hostname: hello-deployment-5ff7f68854-wqzp7
        

  * Test the `/greet-kubernetes` path:
        
        curl -v --resolve altostrat.com:443:USER_CLUSTER_INGRESS_VIP https://altostrat.com/greet-kubernetes --cacert root-ca.crt
        

Output:
        
        Hello Kubernetes!
        




## Cleaning up

Delete your Ingress:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete ingress INGRESS_NAME
    

Replace INGRESS_NAME with the name of the Ingress, such as `my-ingress` or `my-ingress-2`.

Delete your Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete service hello-service
    

Delete your Deployment:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete deployment hello-deployment
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
