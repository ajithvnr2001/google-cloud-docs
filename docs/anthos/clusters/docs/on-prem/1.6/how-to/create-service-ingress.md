---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-service-ingress/
title: Creating a Service and an Ingress \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:28.578433+00:00
---

# Creating a Service and an Ingress  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-service-ingress/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Creating a Service and an Ingress Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create a Kubernetes [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) object in an Google Distributed Cloud user cluster. An Ingress object must be associated with one or more [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) objects, each of which is associated with a set of [Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod).

## SSH into your admin workstation

SSH into your admin workstation:
    
    
    ssh -i ~/.ssh/vsphere_workstation ubuntu@[IP_ADDRESS]
    

where [IP_ADDRESS] is the IP address of your admin workstation.

Do all of the remaining steps in this topic on your admin workstation.

## Creating a Deployment

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

  * The `env` fields specify that the `hello-app` containers listen on TCP port 50000, and the `node-hello` containers listen on TCP port 8080. For `hello-app`, you can see the effect of the `PORT` environment variable by looking at the [source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/hello-app/main.go).




Copy the manifest to a file named `hello-deployment.yaml`, and create the Deployment:
    
    
    kubectl apply --kubeconfig [USER_CLUSTER_KUBECONFIG] -f hello-deployment.yaml
    

where [USER_CLUSTER_KUBECONFIG] is the kubeconfig file for your user cluster.

## Exposing your Deployment with a Service

To provide a stable way for clients to send requests to the Pods of your Deployment, create a Service.

Here's a manifest for a Service that exposes your Deployment to clients inside and outside of your cluster:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: hello-service
    spec:
      type: NodePort
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
    
    
    kubectl apply --kubeconfig [USER_CLUSTER_KUBECONFIG] -f hello-service.yaml
    

View the Service:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get service hello-service --output yaml
    

The output shows the `nodePort` values that have been assigned to the Service:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      ...
      name: hello-service
      namespace: default
      ...
    spec:
      clusterIP: 10.105.252.237
      externalTrafficPolicy: Cluster
      ports:
      - name: world-port
        nodePort: 31807
        port: 60000
        protocol: TCP
        targetPort: 50000
      - name: kubernetes-port
        nodePort: 30734
        port: 60001
        protocol: TCP
        targetPort: 8080
      selector:
        greeting: hello
      sessionAffinity: None
      type: NodePort
    status:
      loadBalancer:
        ingress:
        - {}
    

In the preceding output, the `ports` field is an array of [ServicePort](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#serviceport-v1-core) objects: one named `world-port` and one named `kubernetes-port`.

These are the ways a client can call the Service using `world-port`:

  * A client running on one of the cluster nodes can send a request to the `clusterIP` on `port`. In this example, 10.105.252.237:60000. The request is forwarded to a member Pod on `targetPort`. In this example, [POD_IP_ADDRESS]:50000.

  * A client can send a request to the IP address of any cluster node on `nodePort`. In this example, [NODE_IP_ADDRESS]:31807. The request is forwarded to a member Pod on `targetPort`. In this example, [POD_IP_ADDRESS]:50000.




These are the ways a client can call the Service using `kubernetes-port`:

  * A client running on one of the cluster nodes can send a request to the `clusterIP` on `port`. In this example, 10.105.252.237:60001. The request is forwarded to a member Pod on `targetPort`. In this example, [POD_IP_ADDRESS]:8080.

  * A client can send a request to the IP address of any cluster node on `nodePort`. In this example, [NODE_IP_ADDRESS]:30734. The request is forwarded to a member Pod on `targetPort`. In this example, [POD_IP_ADDRESS]:8080.




## Creating an Ingress

Here's a manifest for an Ingress:
    
    
    apiVersion: networking.k8s.io/v1beta1
    kind: Ingress
    metadata:
      name: my-ingress
    spec:
      rules:
      - http:
          paths:
          - path: /greet-the-world
            backend:
              serviceName: hello-service
              servicePort: 60000
          - path: /greet-kubernetes
            backend:
              serviceName: hello-service
              servicePort: 60001
    

Copy the manifest to a file named `my-ingress.yaml`, and create the Ingress:
    
    
    kubectl apply --kubeconfig [USER_CLUSTER_KUBECONFIG] -f my-ingress.yaml
    

As part of creating your user cluster, you specified a virtual IP address (VIP) for ingress by providing a value for `usercluster.vips.ingressvip` in your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/user-cluster-configuration-file).

When a client sends a request to your user cluster ingress VIP, the request is routed to your F5 BIG-IP load balancer. The load balancer forwards the request to an ingress Service running in your user cluster. The ingress Service is configured to forward the request to different backends depending on the path in the request URL.

It is important to understand that there are two different Services related to the steps in this topic:

  * Your Service named `hello-service`. This is a Service that you created to expose the Pods of your `hello-deployment` Deployment.

  * The _ingress Service_ that runs in the `gke-system` namespace of your user cluster. This Service is part of your cluster infrastructure.




### The `/greet-the-world` path

In your Ingress manifest, you can see a rule that says the path `/greet-the-world` is associated with `serviceName: hello-service` and `servicePort: 60000`. Recall that 60000 is the `port` value in the `world-port` field of your `hello-service` Service.
    
    
    - name: world-port
        nodePort: 31807
        port: 60000
        protocol: TCP
        targetPort: 50000
    

The ingress Service chooses a cluster node and forwards the request to the node on `nodePort`. In this example, [NODE_IP_ADDRESS]:31807. The iptables rules on the node forward the request to a member Pod on port 50000. The container listening on port 50000 displays a `Hello World!` message.

### The `/greet-kubernetes` path

In your Ingress manifest, you can see a rule that says the path `/greet-kubernetes` is associated with `serviceName: hello-service` and `servicePort: 60001`. Recall that 60001 is the `port` value in the `kubernetes-port` field of your `hello-service` Service.
    
    
    - name: kubernetes-port
        nodePort: 30734
        port: 60001
        protocol: TCP
        targetPort: 8080
    

The ingress Service chooses a cluster node and forwards the request to the node on `nodePort`. In this example, [NODE_IP_ADDRESS]:30734. The iptables rules on the node forward the request to a member Pod on port 8080. The container listening on port 8080 displays a `Hello Kubernetes!` message.

## Test the Ingress:

Test the Ingress using the `/greet-the-world` path:
    
    
    curl [USER_CLUSTER_INGRESS_VIP]/greet-the-world
    

The output shows a `Hello, world!` message:
    
    
    Hello, world!
    Version: 2.0.0
    Hostname: ...
    

Test the Ingress using the `/greet-kubernetes` path:
    
    
    curl [USER_CLUSTER_INGRESS_VIP]/greet-kubernetes
    

The output shows a `Hello, Kubernetes!` message:
    
    
    Hello Kubernetes!
    

## Cleaning up

Delete your Ingress:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] delete ingress my-ingress
    

Delete your Service:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] delete service hello-service
    

Delete your Deployment:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] delete deployment hello-deployment
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
