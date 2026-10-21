---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/gateway-tls-termination/
title: Set up TLS termination in ingress gateway \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:32.166008+00:00
---

# Set up TLS termination in ingress gateway  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/gateway-tls-termination/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up TLS termination in ingress gateway

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

## Overview

This page demonstrates how to set up a TLS termination in ingress gateway in Cloud Service Mesh to manage external HTTPS traffic to your services. You will learn how to configure the gateway for secure communication using TLS, enabling encrypted access to your applications. This process leverages Cloud Service Mesh capabilities to expose services like securely.

## Before you begin 

To complete the steps in this document you need the following resources:

  * A Kubernetes cluster with Cloud Service Mesh installed.



## Set up your environment

Run the following commands from a workstation that can access the cluster you intend to use. Make sure that the `kubectl` tool is configured to use the cluster context specific to your cluster.

  1. Set the environment variables.
         
         export ASM_INGRESSGATEWAY_NAMESPACE=asm-ingressgateway
         export ASM_INGRESSGATEWAY_DEPLOYMENT_NAME=asm-ingressgateway
         export ASM_INGRESSGATEWAY_SERVICE_NAME=asm-ingressgateway
         

  2. The foo application deployed in your cluster. Install it with:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: foo
           namespace: foo
         spec:
           selector:
             app: test-backend
           ports:
           - port: 8080
             targetPort: 8080
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: foo
           namespace: foo
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: test-backend
           template:
             metadata:
               labels:
                 app: test-backend
             spec:
               containers:
               - name: whereami
                 image: gcr.io/google-samples/whereami:v1.2.23
                 ports:
                 - containerPort: 8080
         EOF
         

  3. Generate certificates and keys




To secure your ingress gateway, you will need TLS certificates and keys. You can use any certificate generation tool or follow these steps using openssl to create the necessary credentials.

  * Create a root CA certificate and key
        
        mkdir example_certs
        openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=Example Corp/CN=example.com' \
          -keyout example.com.key -out example.com.crt
        

  * Generate a certificate and key for ingress
        
        openssl req -out foo.example.com.csr -newkey rsa:2048 -nodes \
          -keyout foo.example.com.key -subj "/CN=foo.example.com/O=Foo Org"
        
        openssl x509 -req -sha256 -days 365 -CA example.com.crt \
          -CAkey example.com.key -set_serial 0 \
          -in foo.example.com.csr -out foo.example.com.crt
        




## Set up a TLS ingress gateway

Before you complete the instructions in this section, you'll need to determine your control plane implementation. Use the instructions in [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-managed#identify_control_plane_implementation) to do this.

  1. Create the namespace. This namespace is used to deploy the ingress gateway.
         
         kubectl create namespace ${ASM_INGRESSGATEWAY_NAMESPACE}
         

  2. Apply the default injection label to the namespace:
         
         kubectl label namespace ${ASM_INGRESSGATEWAY_NAMESPACE} \
             istio.io/rev- istio-injection=enabled --overwrite
         

  3. Apply the [ingress gateway manifest file](https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples/blob/main/docs/ingress-gateway-external-lb/ingress-gateway.yaml).
         
         kubectl --namespace ${ASM_INGRESSGATEWAY_NAMESPACE} apply --filename https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-service-mesh-samples/main/docs/ingress-gateway-external-lb/ingress-gateway.yaml
         

Expected output:
         
         serviceaccount/asm-ingressgateway created
         role.rbac.authorization.k8s.io/asm-ingressgateway created
         rolebinding.rbac.authorization.k8s.io/asm-ingressgateway created
         deployment.apps/asm-ingressgateway created
         service/asm-ingressgateway created
         poddisruptionbudget.policy/asm-ingressgateway created
         horizontalpodautoscaler.autoscaling/asm-ingressgateway created
         

  4. Store the TLS credentials in a Kubernetes secret:
         
         kubectl create -n ${ASM_INGRESSGATEWAY_NAMESPACE} secret tls foo-credential \
           --key=example_certs/foo.example.com.key \
           --cert=example_certs/foo.example.com.crt
         

  5. Define the ingress gateway: Create a Gateway resource to handle HTTPS traffic on port 443:
         
         cat <<EOF | kubectl apply -f -
         apiVersion: networking.istio.io/v1
         kind: Gateway
         metadata:
           name: secure-gateway
           namespace: ${ASM_INGRESSGATEWAY_NAMESPACE}
         spec:
           selector:
             app: asm-ingressgateway
             istio: ingressgateway
           servers:
           - port:
               number: 443
               name: https
               protocol: HTTPS
             tls:
               mode: SIMPLE
               credentialName: foo-credential
             hosts:
             - "foo.example.com"
         EOF
         

  6. Route traffic to the foo service: Define a VirtualService to direct traffic to the foo deployment:
         
         cat <<EOF | kubectl apply -f -
         apiVersion: networking.istio.io/v1
         kind: VirtualService
         metadata:
           name: foo-routing
           namespace: ${ASM_INGRESSGATEWAY_NAMESPACE}
         spec:
           hosts:
           - "foo.example.com"
           gateways:
           - secure-gateway
           http:
           - match:
             - uri:
                 prefix: /status
             - uri:
                 prefix: /delay
             route:
             - destination:
                 host: foo
                 port:
                   number: 8080
         EOF
         

  7. [Set up the external load balancer](https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/external-lb-gateway#in-cluster) to connect with the ingress gateway from the cluster

  8. Test the secure connection: Use curl to verify the setup:
         
         export EXTERNAL_LB_IP_ADDRESS=EXTERNAL_LB_IP_ADDRESS
         curl -v -H "Host: foo.example.com" --resolve "foo.example.com:443:$EXTERNAL_LB_IP_ADDRESS" \
           --cacert example_certs/example.com.crt "https://foo.example.com:443/ping"
         




Replace `EXTERNAL_LB_IP_ADDRESS` with ip of external load balancer.

The output is similar to the following:
    
    
        {
          "cluster_name": "gke-us",
          "host_header": "34.120.175.141",
          "pod_name": "whereami-deployment-954cbf78-mtlpf",
          "pod_name_emoji": "😎",
          "project_id": "my-project",
          "timestamp": "2021-11-29T17:01:59",
          "zone": "us-central1-b"
        }
    

## What's next

  * Read more about [Installing and upgrading gateways](https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/gateways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
