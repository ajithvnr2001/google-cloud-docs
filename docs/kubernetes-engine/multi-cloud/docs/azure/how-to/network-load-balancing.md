---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/network-load-balancing/
title: Network load balancing \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:39.109094+00:00
---

# Network load balancing  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/network-load-balancing/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network load balancing

This topic shows you how to set up an L4 load balancer backed by an Azure Standard Load Balancer using GKE on Azure .

When you create a Service of type `LoadBalancer`, a GKE on Azure controller configures an [Azure Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview).

## Before you begin

  * You must [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster) and configure `kubectl` to access the cluster.



## Selecting a public or private load balancer

Service load balancers can be either public — having public frontend IPs — or internal— only accessible through private IPs.

By default, a new Service is public. To create an internal load balancer, you set the `service.beta.kubernetes.io/azure-load-balancer-internal` annotation to `"true"` in your manifest.

## Choosing subnet for internal load balancers

When creating an internal load balancer, GKE on Azure needs to pick the subnet to place the load balancer in. This default service load balancer subnet is chosen from the cluster's creation parameters as follows:

  1. If specified and non-empty, `cluster.networking.serviceLoadBalancerSubnetId`
  2. Otherwise, `cluster.controlPlane.subnetId`



Alternately, you can specify the subnet to use for a given load balancer by adding the `service.beta.kubernetes.io/azure-load-balancer-internal-subnet` annotation to the Service. The value for this annotation is the subnet's name.

## Creating an example LoadBalancer

You create a load balancer by creating a deployment and exposing that deployment with a service.

  1. Create your deployment. Containers in this Deployment listen on port 50001. Save the following YAML to a file named `my-deployment-50001.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-deployment-50001
         spec:
           selector:
             matchLabels:
               app: products
               department: sales
           replicas: 3
           template:
             metadata:
               labels:
                 app: products
                 department: sales
             spec:
               containers:
               - name: hello
                 image: "gcr.io/google-samples/hello-app:2.0"
                 env:
                 - name: "PORT"
                   value: "50001"
         

  2. Create the Deployment with `kubectl apply`:
         
         kubectl apply -f my-deployment-50001.yaml
         

  3. Verify that three Pods are running:
         
         kubectl get pods --selector=app=products
         

  4. Create a Service of type `LoadBalancer` for your deployment. You can create an Azure Standard Load Balancer that is either public, or internal. Choose from one of the following options.

Copy one of the following manifests to a file named `my-lb-service.yaml`.

### Public
         
         apiVersion: v1
         kind: Service
         metadata:
           name: my-lb-service
         spec:
           type: LoadBalancer
           selector:
             app: products
             department: sales
           ports:
           - protocol: TCP
             port: 60000
             targetPort: 50001
         

### Internal

You create an internal LoadBalancer by setting the annotation `service.beta.kubernetes.io/azure-load-balancer-internal` to `"true"`. The following YAML includes this annotation. `yaml apiVersion: v1 kind: Service metadata: name: my-lb-service annotations: service.beta.kubernetes.io/azure-load-balancer-internal: "true" spec: type: LoadBalancer selector: app: products department: sales ports: - protocol: TCP port: 60000 targetPort: 50001`

  5. Create the Service with `kubectl apply`:
         
         kubectl apply -f my-lb-service.yaml
         

**Note:** Configuring the load balancer and IP address takes several minutes.
  6. View the Service's address with `kubectl get service`.
         
         kubectl get service my-lb-service
         

The output will include a column `EXTERNAL-IP` with an address of the load balancer (either public or private depending how the load balancer was created).

  7. If you have created a public load balancer you can connect to the load balancer with `curl`. Replace external-ip with the address from the output of `kubectl get service` from the previous step.
         
         curl http://external-ip:60000
         

The output resembles the following:
         
         Hello, world!
         Version: 2.0.0
         Hostname: my-deployment-50001-84b6dc5555-zmk7q
         




### Cleaning up

To remove the Service and Deployment, use `kubectl delete`.
    
    
    kubectl delete -f my-lb-service.yaml
    kubectl delete -f my-deployment-50001.yaml
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
