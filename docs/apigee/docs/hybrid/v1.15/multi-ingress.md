---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-ingress/
title: Adding multiple ingress gateways to customer-installed Cloud Service Mesh \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:58:20.751676+00:00
---

# Adding multiple ingress gateways to customer-installed Cloud Service Mesh  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Adding multiple ingress gateways to customer-installed Cloud Service Mesh Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/multi-ingress.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-ingress.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-ingress.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/multi-ingress.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-ingress.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/multi-ingress.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/multi-ingress.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/multi-ingress.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-ingress.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/multi-ingress.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/multi-ingress.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/multi-ingress.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/multi-ingress.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/multi-ingress.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/multi-ingress.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/multi-ingress.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/multi-ingress.html)



This procedure describes adding additional Cloud Service Mesh gateways to your Apigee hybrid installation. 

**Note:** Starting with Apigee hybrid version 1.8, Apigee hybrid uses Apigee ingress gateway to provide an ingress gateway for your hybrid installation. To configure multiple Apigee ingress gateways, see [Managing Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/managing-ingress#installing-additional-apigee-ingress-gateway-gateways). 

## Installing additional Cloud Service Mesh gateways

In the Cloud Service Mesh `overlay.yaml` file you can add more ingress gateways by following a similar pattern as the one below. Note that the `spec.components[].label` and `spec.components[].k8s.service.selector` elements allow you to associate a named ingress gateway with a specific virtual host, as explained in Targeting an ingress to a virtual host. 
    
    
      apiVersion: install.istio.io/v1alpha1
      kind: IstioOperator
      spec:
        profile: asm-gcp
        # hub: gcr.io/gke-release/asm # {"$ref":"#/definitions/io.k8s.cli.setters.anthos.servicemesh.hub"}
        components:
          ingressGateways:
          - name: istio-ingressgateway-dairy
            enabled: true
            **label:
              app: istio-ingressgateway
              ingress_name: dairy**
            k8s:
              service:
                **selector:
                  app: istio-ingressgateway
                  ingress_name: dairy**
                type: LoadBalancer
                ports:
                - name: status-port
                  port: 15021
                - name: http2
                  port: 80
                  targetPort: 8080
                - name: https
                  port: 443
                  targetPort: 8443
              hpaSpec:
                minReplicas: 1
                maxReplicas: 10
          - name: istio-ingressgateway-vegetables
            enabled: true
            **label:
              app: istio-ingressgateway
              ingress_name: vegetables**
            k8s:
              service:
                **selector:
                  app: istio-ingressgateway
                  ingress_name: vegetables**
                ports:
                - name: http2
                  port: 80
                  targetPort: 8080
                - name: status-port
                  port: 15020
                - name: https
                  port: 443
                  targetPort: 8443
              hpaSpec:
                minReplicas: 1
                maxReplicas: 10
              resources:
                requests:
                  cpu: 300m
                  memory: 128Mi
      

Follow the Cloud Service Mesh documentation for your platform to apply the changes. 

## Targeting an Cloud Service Mesh/istio ingress to a virtual host

You can target a labeled Cloud Service Mesh/istio ingress gateway to a specific virtual host in your overrides file. This configuration specifies the ingress gateway where Apigee will apply the virtual host's configuration. In the following example, traffic to virtual host `milk-vh` is directed through the ingress labeled `dairy` and traffic to the other two virtual hosts goes through the `vegetables` ingress. The ingresses must be properly labeled, as explained in Installing additional Apigee ingress gateway gateways. 
    
    
    virtualhosts:
      - name: milk-vh
        sslCertPath: cert-milk.crt
        sslKeyPath: cert-milk.key
        **selector:
          app: istio-ingressgateway
          ingress_name: dairy**
    
      - name: carrots-vh
        sslCertPath: cert-carrots.crt
        sslKeyPath: cert-carrots.key
        **selector:
          app: istio-ingressgateway
          ingress_name: vegetables**
    
      - name: ginger-vh
        sslCertPath: cert-ginger.crt
        sslKeyPath: cert-ginger.key
        **selector:
          app: apigee-ingressgateway
          ingress_name: vegetables**
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
