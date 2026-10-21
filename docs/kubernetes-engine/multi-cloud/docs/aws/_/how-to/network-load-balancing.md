---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/network-load-balancing/
title: Create a network load balancer \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:41:27.758885+00:00
---

# Create a network load balancer  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/network-load-balancing/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Create a network load balancer Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up an [L4 load balancer](https://en.wikipedia.org/wiki/Transport_layer) with an AWS Elastic Load Balancer (ELB) or a Network Load Balancer (NLB) endpoint.

For more information on the other types of load balancers that you can use with GKE on AWS, see [Load balancer overview](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancers).

This page is for Networking specialists who want to install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

  * [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster) and configure `kubectl` to connect to it.
  * [Tag your service load balancer subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets#tag_your_subnets_for_their_intended_use). This is required for subnet auto-discovery.
  * Decide whether you need a [Classic](https://aws.amazon.com/elasticloadbalancing/features/) or a [Network](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) ELB.
  * Decide whether you need an internet-facing or internal load balancer.



### Choose a load balancer type

GKE on AWS creates a Service load balancer as either an AWS Classic Elastic Load Balancer (Classic ELB) or NLB. By default, GKE on AWS creates a Classic ELB. To create an NLB, set the `service.beta.kubernetes.io/aws-load-balancer-type` annotation to `nlb`. For more information on the differences between load balancer types, see [Load balancer types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html) in the AWS documentation.

**Note:** You cannot apply the NLB annotation to an existing Service. To change type, you must delete and recreate the existing LoadBalancer.

### Choose an internet-facing or internal load balancer

Service load balancers can be either internet-facing (with a publicly resolvable DNS name) or internal (only accessible within your VPC).

By default, new load balancers are internet-facing. To create an internal load balancer, set the `service.beta.kubernetes.io/aws-load-balancer-internal` annotation to `"true"` in your manifest.

You cannot apply the `aws-load-balancer-internal` annotation to an existing Service. To change between internet-facing and internal configurations, you must delete and recreate the existing LoadBalancer.

### Choose your subnets

When creating load balancers, AWS needs to know what subnets to place them in. By default, these subnets are automatically discovered from among the subnets in the VPC. This requires that subnets have specific tags. For details of subnet auto-discovery and tagging, see [Load Balancer Subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets).

Alternately, you can specify load balancer subnets with an annotation, by adding the `service.beta.kubernetes.io/aws-load-balancer-subnets` annotation to the Service. The value for this annotation is a comma-separated list of subnet IDs or subnet names— for example `subnet-012345678abcdef,subnet-abcdef123456789,subnet-123456789abcdef`.

## Create an example load balancer

You create a Service of type LoadBalancer by creating a deployment and exposing that deployment with a Service. In the following example, you create a sample load balancer.

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
         

  4. Create a Service of type `LoadBalancer` for your deployment.

  5. Decide what type of load balancer you need:

     * An internet-facing Classic ELB
     * An internet-facing NLB
     * An internal Classic ELB
     * An internal NLB

Choose the tab that matches your requirements and copy the manifest within it to a file named `my-lb-service.yaml`.

### Internet-facing Classic
    
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
    

### Internet-facing NLB

You create an NLB by setting the annotation `service.beta.kubernetes.io/aws-load-balancer-type` to `nlb`. The following YAML includes this annotation.
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-lb-service
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-type: nlb
    spec:
      type: LoadBalancer
      selector:
        app: products
        department: sales
      ports:
      - protocol: TCP
        port: 60000
        targetPort: 50001
    

### Internal Classic

You create an internal LoadBalancer by setting the annotation `service.beta.kubernetes.io/aws-load-balancer-internal` to `"true"`. The following YAML includes this annotation.
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-lb-service
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-internal: "true"
    spec:
      type: LoadBalancer
      selector:
        app: products
        department: sales
      ports:
      - protocol: TCP
        port: 60000
        targetPort: 50001
    

### Internal NLB

You create an internal NLB by setting the annotations:

     * `service.beta.kubernetes.io/aws-load-balancer-internal` to `"true"`
     * `service.beta.kubernetes.io/aws-load-balancer-type` to `nlb`

The following YAML includes both annotations.
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-lb-service
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-internal: "true"
        service.beta.kubernetes.io/aws-load-balancer-type: nlb
    spec:
      type: LoadBalancer
      selector:
        app: products
        department: sales
      ports:
      - protocol: TCP
        port: 60000
        targetPort: 50001
    

  6. Create the Service with `kubectl apply`:
         
         kubectl apply -f my-lb-service.yaml
         

**Note:** Configuring the load balancer and IP address takes several minutes.
  7. View the Service's address with `kubectl get service`.
         
         kubectl get service my-lb-service
         

The output will include a column `EXTERNAL-IP` with an address of the load balancer (either public or private depending how the load balancer was created).

  8. If you have created an internet-facing load balancer you can connect to the load balancer with `curl` using the following command:
         
         curl http://EXTERNAL_IP:60000
         

Replace `EXTERNAL_IP` with the address from the EXTERNAL-IP column in the previous step.




The output resembles the following:
    
    
    ```none
    Hello, world!
    Version: 2.0.0
    Hostname: my-deployment-50001-84b6dc5555-zmk7q
    ```
    

### Cleaning up

To remove the Service and Deployment, use the `kubectl delete` command:
    
    
    kubectl delete -f my-lb-service.yaml
    kubectl delete -f my-deployment-50001.yaml
    

## Next steps

  * [Set up an HTTP Load Balancer](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/http-load-balancing).

  * Learn more about GKE on Google Cloud documentation on [Exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).

  * See the complete list of [supported annotations](https://github.com/kubernetes/cloud-provider-aws/blob/a43d818415c2fbd62a61c2ee613ae4d770426ea5/pkg/providers/v1/aws.go#L101-L243).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
