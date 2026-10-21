---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/bring-your-own-cert/
title: Using your own TLS certificates \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:26.639847+00:00
---

# Using your own TLS certificates  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/bring-your-own-cert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using your own TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to configure Knative serving to use your own SSL/TLS certificates.

Alternatively, you can use the [managed TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls) feature, which automatically creates and renews TLS certificates through [Let's Encrypt](https://letsencrypt.org/)

To use your own certificates, you store your TLS certificates in a Kubernetes Secret and then configure the ingress gateway of Cloud Service Mesh to use that secret.

## Before you begin

  * These instructions assume that you have already obtained your TLS certificates.
  * You must configure a custom domain. For details, see [Mapping custom domains](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains).
  * You are required to configure each of your Knative serving services that use the [ingress gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview#components_in_the_default_installation) to serve external traffic. If these external facing services are not configured to use your TLS certificates, the services will not be able to verify an HTTPS connection and therefore, never achieve the `ready` state.



## Storing TLS certificates in a Kubernetes Secret

To store the certificates into a Secret:

  1. Open a terminal and navigate to the directory where your TLS certificates are located.

  2. Use the following command to create a secret that stores your certificates:
         
         kubectl create --namespace INGRESS_NAMESPACE secret tls SECRET_NAME \
           --key PRIVATE_KEY.pem \
           --cert FULL_CHAIN.pem

Replace:

     * INGRESS_NAMESPACE with the namespace of your ingress service, `istio-ingressgateway`. Specify the `istio-system` namespace if you installed Cloud Service Mesh using the default configuration.
     * SECRET_NAME with the name that you want use for your Kubernetes Secret.
     * PRIVATE_KEY.pem with the name of the file that holds your certificate private key.
     * FULL_CHAIN.pem with the name of the file that holds your public certificate.



You can now configure the ingress gateway to use the secret you just created for your TLS certificate.

## Configuring the ingress gateway to use your certificates

Modify the ingress gateway of Cloud Service Mesh to use the secret that you created for your TLS certificates:

  1. Open the ingress gateway YAML in edit mode by running the following command:
         
         kubectl edit gateway knative-ingress-gateway --namespace knative-serving

Example of the default ingress gateway configuration:
         
         apiVersion: networking.istio.io/v1beta1
         kind: Gateway
         metadata:
           ...
           # other skipped configuration
           ...
         spec:
           selector:
             istio: ingressgateway
           servers:
           - hosts:
             - '*'
             port:
               name: http
               number: 80
               protocol: HTTP
         

  2. Configure the ingress gateway to use your secret by appending the `hosts`, `port`, and `tls` attributes to the existing YAML.

     * **To configure all services to use the same secret** : Append the following to your YAML configuration and specify `"*"` as the `hosts` attribute value:
           
           ...
           # other skipped configuration
           ...
           - hosts:
             - "*"
             port:
               name: https
               number: 443
               protocol: HTTPS
             tls:
               mode: SIMPLE
               credentialName: SECRET_NAME
           

Replace SECRET_NAME with the name of the secret that you created.

See example.

     * **To individually configure each of your services** : Append the following to your YAML configuration and specify the values for the `hosts` attributes using the service's name and namespace:

For each service, you specify values for the `hosts`, `port`, and `tls` attributes:
           
           ...
           # other skipped configuration
           ...
           - hosts:
             - SERVICE_NAME.SERVICE_NAMESPACE.CUSTOM_DOMAIN
             port:
               number: 443
               name: https-SERVICE_NAME
               protocol: HTTPS
             tls:
               mode: SIMPLE
               credentialName: SECRET_NAME
           

Replace:

       * SERVICE_NAME with the name of the Knative serving service. Every service that uses the ingress gateway to serve external traffic must be individually configured.
       * SERVICE_NAMESPACE with the name of the namespace in which the service is running.
       * CUSTOM_DOMAIN with the custom domain for which you configured the service to use.
       * SECRET_NAME with the name of the secret that you want the service to use. If you created multiple secrets for different sets of TLS certificates, you can specify which secret each service uses.

See example.

  3. Save your changes.




You can now use the HTTPS protocol to access your deployed Knative serving services.

## Examples

Configure all services:
    

This example demonstrates how to configure all services to use the `TLSsecret` secret:
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      ...
      # other skipped configuration
      ...
    spec:
      selector:
        istio: ingressgateway
      servers:
        - hosts:
          - "*"
          port:
            name: http
            number: 80
            protocol: HTTP
        - hosts:
          - "*"
          port:
            name: https
            number: 443
            protocol: HTTPS
          tls:
            mode: SIMPLE
            credentialName: **TLSsecret**
    

Configure individual services:
    

This example demonstrates how to individually configure all three of the services that are serving internet traffic:
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      ...
      # other skipped configuration
      ...
    spec:
      selector:
        istio: ingressgateway
      servers:
      - hosts:
        - "*"
        port:
          name: http
          number: 80
          protocol: HTTP
      - hosts:
        - **prodservice**.**prodnamespace**.my-custom-domain.com
        port:
          number: 443
          name: https-**prodservice**
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: **TLSsecret**
      - hosts:
        - **experiment**.**namespace**.my-custom-domain.com
        port:
          number: 443
          name: https-**experiment**
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: **TLSsecret**
      - hosts:
        - **fallbackservice**.**anothernamespace**.my-custom-domain.com
        port:
          number: 443
          name: https-**fallbackservice**
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: **anotherTLSsecret**
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
