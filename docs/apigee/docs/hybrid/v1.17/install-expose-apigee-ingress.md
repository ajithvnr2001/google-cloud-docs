---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress/
title: Step 1: Expose Apigee ingress gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:20.397610+00:00
---

# Step 1: Expose Apigee ingress gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 1: Expose Apigee ingress gateway Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-expose-apigee-ingress.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-expose-apigee-ingress.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-expose-apigee-ingress.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-expose-apigee-ingress.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-expose-apigee-ingress.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-expose-apigee-ingress.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-expose-apigee-ingress.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-expose-apigee-ingress.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-expose-apigee-ingress.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-expose-apigee-ingress.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-expose-apigee-ingress.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-expose-apigee-ingress.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-expose-apigee-ingress.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-expose-apigee-ingress.html)



This step explains how to set up the Kubernetes service for your Apigee ingress gateway. The Kubernetes service is needed for each ingress deployment to obtain an IP address that can be exposed. Client calls to proxies will invoke a hostname that will resolve to this IP address. 

##  Options for Kubernetes services for your Apigee ingress gateway 

There are two options for providing a kubernetes service to assign the IP address ... 

  * Create a custom Kubernetes service for each Apigee ingress gateway (recommended).
  * Use the default Kubernetes service. 



###  Create your own Kubernetes service 

For production environments, Apigee recommends you create a custom Kubernetes service for each ingress gateway. 

  * Apigee deletes default service, but does not delete the custom kubernetes service upon cleanup. Hence, the IP address won't be released upon reinstallation of Apigee hybrid.
  * For platforms not on Google Cloud, like EKS, AKS, and OpenShift, you need to customize the Kubernetes service to work with the cloud provider. Therefore it is better to create a custom Kubernetes service than to use the default service, because apigee does not support all customizations to the default Kubernetes service.



Use the following steps to set up and route traffic to the new ingress gateway. 

  1. Create a Kubernetes service with the required pod selector labels, `app`, `ingress_name`, and `org`. These labels are already present in Apigee ingress gateway pods. 

Create a service file using the following template: 
         
         apiVersion: v1
         kind: Service
         metadata:
           name: SERVICE_NAME
           namespace: APIGEE_NAMESPACE
         spec:
           ports:
           - name: status-port
             port: 15021
             protocol: TCP
             targetPort: 15021
           - name: https
             port: 443
             protocol: TCP
             targetPort: 8443
           selector:
             app: apigee-ingressgateway #required
             ingress_name: INGRESS_NAME
             org: ORG_NAME
           type: LoadBalancer
           loadBalancerIP: LOAD_BALANCER_IP

     * SERVICE_NAME is a name used to identify this service. For example, `apigee-prod-1`. **Note:** To more easily identify your services, use the ingress name as part of the service name. 
     * INGRESS_NAME is the name of this Apigee ingress gateway. It must match the name you provided for `ingressGateways.name` in your `overrides.yaml` file. For more information see [`ingressGateways` in the Configuration properties reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways).
     * ORG_NAME is the name of the Apigee organization. It must match the name you provided for `org` in your `overrides.yaml` file. For more information see [`org` in the Configuration properties reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#org).
     * LOAD_BALANCER_IP is the IP address for the load balancer. 

If you have an IP address reserved for your load balancer, enter that. 

If you do not have an IP address already reserved, you can use the one returned by the default Apigee ingress service. Use the `EXTERNAL-IP` returned by the following command: 
           
           kubectl get svc -n APIGEE_NAMESPACE -l app=apigee-ingressgateway

**Caution:** Because of a [limitation](https://docs.cloud.google.com/load-balancing/docs/l7-internal#limitations) on Google Cloud internal Application Load Balancer, this Apigee routing option does not support HTTP 1.0 requests. Incoming client requests that specify the HTTP 1.0 protocol will fail. Later HTTP versions are supported.

Apigee ingress gateway exposes the following ports: 

Port | Description  
---|---  
**443** | Runtime traffic.  
**15021** | Health check. `status-port` exposes a `/healthz/ready` endpoint that can be used with GKE Ingress health checks.  
  2. Create the service by applying the `SERVICE_FILENAME.yaml`: 
         
         kubectl apply -f SERVICE_FILENAME.yaml

  3. Find the external IP of Apigee ingress gateway with the following command: 
         
         kubectl get svc -n APIGEE_NAMESPACE SERVICE_NAME

Your output should look something like: 
         
         NAME                                        TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)                                      AGE
         apigee-ingressgateway-prod-hybrid-37a39bd   LoadBalancer   192.0.2.123   **233.252.0.123**   15021:32049/TCP,80:31624/TCP,443:30723/TCP   16h

  4. Disable the loadbalancer for the default Apigee ingress gateway service: 
     1. Update the [`ingressGateways[].svcType`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-svctype) property to `ClusterIP` in your overrides file: 
            
            ingressGateways:
              svcType: ClusterIP

     2. Upgrade the `apigee-org` chart to apply the changes: 
            
            helm upgrade ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

See [Disable the loadbalancer for the default Apigee ingress gateway service](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/managing-ingress#disable-loadbalancer) for more information.

  5. Test the ingress gateway by making a healthcheck call. 
         
         curl -H 'User-Agent: GoogleHC' https://DOMAIN/healthz/ingress -k \
           --resolve "DOMAIN:443:INGRESS_IP_ADDRESS"

Where

     * DOMAIN is the domain you provided as the hostname for the environment group you created in [Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment).
     * INGRESS_IP_ADDRESS is the ingress IP address, for example `233.252.0.123`.

On success the command returns: 
    
    Apigee Ingress is healthy

  6. Use this IP address to update your DNS record (usually an `A` or `CNAME` record) at your registrar or DNS provider.



###  Use the default Kubernetes service 

For non-production environments or to test initial traffic through the Apigee ingress gateway, Apigee hybrid provides default Kubernetes service for each ingress deployment. 

You can make limited configuration changes to the default service in your `overrides.yaml` file. For the available configuration options, see [Managing Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/managing-ingress). For example, you can add annotations. **Note:** This service will be deleted when the ingress deployment is deleted (when the ingress gateway is removed from the overrides file). 

For production environments, it is recommended you provide a Kubernetes service for ingress. Follow the steps in Create your own Kubernetes service. 

  1. Find the external IP of the default Apigee ingress service with the following command: 
         
         kubectl get svc -n APIGEE_NAMESPACE -l app=apigee-ingressgateway

Your output should look something like: 
         
         NAME                                        TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)                                      AGE
         apigee-ingressgateway-prod-hybrid-37a39bd   LoadBalancer   192.0.2.123   **233.252.0.123**   15021:32049/TCP,80:31624/TCP,443:30723/TCP   16h

  2. Test the ingress gateway by making a healthcheck call. 
         
         curl -H 'User-Agent: GoogleHC' https://DOMAIN/healthz/ingress -k \
           --resolve "DOMAIN:443:INGRESS_IP_ADDRESS"

Where

     * DOMAIN is the domain you provided as the hostname for the environment group you created in [Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment).
     * INGRESS_IP_ADDRESS is the ingress IP address, for example `233.252.0.123`.

On success the command returns: 
    
    Apigee Ingress is healthy

  3. Use this IP address to update your DNS record (usually an `A` or `CNAME` record) at your registrar or DNS provider.

**Congratulations!**

You've successfully set up the Apigee ingress gateway. Now it's time to download a proxy and test your ingress gateway.

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress) [(NEXT) Step 2: Deploy a proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
