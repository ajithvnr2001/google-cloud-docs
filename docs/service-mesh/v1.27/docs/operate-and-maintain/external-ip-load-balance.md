---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/external-ip-load-balance/
title: Configure external IP addresses for Google Distributed Cloud (software only) for VMware with F5 BIG-IP load balancers \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:37.804797+00:00
---

# Configure external IP addresses for Google Distributed Cloud (software only) for VMware with F5 BIG-IP load balancers  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/external-ip-load-balance/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure external IP addresses for Google Distributed Cloud (software only) for VMware with F5 BIG-IP load balancers

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).**Note:** This feature is not supported on managed Cloud Service Mesh

The default Cloud Service Mesh installation on Google Distributed Cloud (software only) for VMware assumes that external IP addresses are automatically allocated for `LoadBalancer` services. This is not true for Google Distributed Cloud (software only) for VMware with F5 BIG-IP load balancers. Because of this, you need to allocate one or more external IP addresses, depending on your service mesh configuration:

  * One external IP address for the Cloud Service Mesh ingress Gateway resource, for example the gateway that your customers use to access your workloads from across the internet.
  * Another external IP address for your clusters to communicate with each other if they exist on different networks within your service mesh. This is referred to as the east-west gateway.



## Configuring the ingress gateway IP address

To configure an external IP address for the ingress gateway, follow the instructions in one of these sections, depending on your [Google Distributed Cloud (software only) for VMware load balancing mode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/setup-load-balance):

### Integrated mode

  1. Patch the `istio-ingressgateway` Service's configuration with the external IP address for the ingress gateway: 
         
         kubectl patch svc istio-ingressgateway -n istio-system --type='json' -p '[{"op": "add", "path": "/spec/loadBalancerIP", "value": "INGRESS_GATEWAY_IP"}]'

### Manual mode

  2. View the `istio-ingressgateway` service's configuration in your shell: 
         
         kubectl get svc -n istio-system istio-ingressgateway -o yaml

Each of the ports for Cloud Service Mesh's gateways are displayed. The command output is like the following: 
         
         ...
           ports:
           - name: status-port
             nodePort: 30391
             port: 15020
             protocol: TCP
             targetPort: 15020
           - name: http2
             nodePort: 31380
             port: 80
             protocol: TCP
             targetPort: 80
           - name: https
             nodePort: 31390
             port: 443
             protocol: TCP
             targetPort: 443
           - name: tcp
             nodePort: 31400
             port: 31400
             protocol: TCP
             targetPort: 31400
           - name: https-kiali
             nodePort: 31073
             port: 15029
             protocol: TCP
             targetPort: 15029
           - name: https-prometheus
             nodePort: 30253
             port: 15030
             protocol: TCP
             targetPort: 15030
           - name: https-grafana
             nodePort: 30050
             port: 15031
             protocol: TCP
             targetPort: 15031
           - name: https-tracing
             nodePort: 31204
             port: 15032
             protocol: TCP
             targetPort: 15032
           - name: tls
             nodePort: 30158
             port: 15443
             protocol: TCP
             targetPort: 15443
           ...

  3. Expose these ports through your load balancer.   
  
For example, the service port named `http2` has `port` 80 and `nodePort` 31380\. Suppose the node addresses for your user cluster are `192.168.0.10`, `192.168.0.11`, and `192.168.0.12`, and your load balancer's VIP is `203.0.113.1`.   
  
Configure your load balancer so that traffic sent to `203.0.113.1:80` is forwarded to `192.168.0.10:31380`, `192.168.0.11:31380`, or `192.168.0.12:31380`. You can select the service ports that you want to expose on this given VIP. 




Confirm that the ingress gateway was assigned an external IP address. There might be a slight delay that requires you to repeat this command until you see the expected result:
    
    
    kubectl --context="${CTX_CLUSTER1}" get svc istio-ingressgateway -n istio-system
    

The expected output is:
    
    
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)   AGE
    istio-ingressgateway   LoadBalancer   10.80.6.124   34.75.71.237   ...       51s

## Configuring the east-west gateway IP address

To configure an external IP address for the east-west gateway, follow the instructions in one of these sections, depending on your [Google Distributed Cloud (software only) for VMware load balancing mode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/setup-load-balance):

### Integrated mode

  1. Patch the `istio-eastwestgateway` Service's configuration with the external IP address for the east-west gateway: 
         
         kubectl patch svc istio-eastwestgateway -n istio-system --type='json' -p '[{"op": "add", "path": "/spec/loadBalancerIP", "value": "EAST_WEST_GATEWAY_IP"}]'

### Manual mode

  2. View the `istio-eastwestgateway` service's configuration in your shell: 
         
         kubectl get svc -n istio-system istio-eastwestgateway -o yaml

Each of the ports for Cloud Service Mesh's gateways are displayed. The command output is like the following: 
         
         ports:
           - name: status-port
             nodePort: 31781
             port: 15021
             protocol: TCP
             targetPort: 15021
           - name: tls
             nodePort: 30498
             port: 15443
             protocol: TCP
             targetPort: 15443
           - name: tls-istiod
             nodePort: 30879
             port: 15012
             protocol: TCP
             targetPort: 15012
           - name: tls-webhook
             nodePort: 30336
             port: 15017
             protocol: TCP
             targetPort: 15017
           ...

  3. Expose these ports through your load balancer.   
  
For example, the service port named `http2` has `port` 80 and `nodePort` 31380\. Suppose the node addresses for your user cluster are `192.168.0.10`, `192.168.0.11`, and `192.168.0.12`, and your load balancer's VIP is `203.0.113.1`.   
  
Configure your load balancer so that traffic sent to `203.0.113.1:80` is forwarded to `192.168.0.10:31380`, `192.168.0.11:31380`, or `192.168.0.12:31380`. You can select the service ports that you want to expose on this given VIP. 




Confirm that the east-west gateway was assigned an external IP address. There might be a slight delay that requires you to run repeat this command until you see the expected result:
    
    
    kubectl --context="${CTX_CLUSTER1}" get svc istio-eastwestgateway -n istio-system
    

The expected output is:
    
    
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)   AGE
    istio-eastwestgateway   LoadBalancer   10.80.6.124   34.75.71.237   ...       51s

## What's next?

  * [Deploy the Online Boutique sample sample application](https://docs.cloud.google.com/service-mesh/v1.27/docs/onlineboutique-install-kpt)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
