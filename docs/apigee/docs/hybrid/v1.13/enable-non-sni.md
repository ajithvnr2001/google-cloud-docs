---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-non-sni/
title: Enable non-SNI clients \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:55:26.798268+00:00
---

# Enable non-SNI clients  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-non-sni/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enable non-SNI clients Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-non-sni.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-non-sni.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/enable-non-sni.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-non-sni.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-non-sni.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/enable-non-sni.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-non-sni.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-non-sni.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/enable-non-sni.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/enable-non-sni.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/enable-non-sni.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/enable-non-sni.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enable-non-sni.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/enable-non-sni.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/enable-non-sni.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/enable-non-sni.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/enable-non-sni.html)



This topic explains how to enable non-SNI clients for use with Apigee hybrid. 

##  How to configure a non-SNI client

This section explains how to enable support for non-SNI ([Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication)) clients in Apigee hybrid. A non-SNI client uses port 443 and is required if you want to integrate hybrid runtime instances with Google [Cloud Load Balancing](https://cloud.google.com/load-balancing/docs) or for clients that do not support SNI. 

  1. Create an ApigeeRoute custom resource definition (CRD). Be sure that `enableNonSniClient` is set to `true`: 
         
         apiVersion: apigee.cloud.google.com/v1alpha1
         kind: ApigeeRoute
         metadata:
           name: ROUTE_NAME
           namespace: APIGEE_NAMESPACE
         spec:
           hostnames:
           - "*"
           ports:
           - number: 443
             protocol: HTTPS
             tls:
               credentialName: CREDENTIAL_NAME
               mode: SIMPLE
               #optional
               minProtocolVersion: TLS_AUTO
           selector:
             app: apigee-ingressgateway
           **enableNonSniClient: true**

Where: 

     * ROUTE_NAME is the name you give to the custom resource (CR).
     * CREDENTIAL_NAME is the name of a Kubernetes Secret deployed to the cluster that contains TLS credentials for your virtualhost. You can find the credential name with the following `kubectl` Command: 
           
           kubectl -n APIGEE_NAMESPACE get ApigeeRoutes -o=yaml | grep credentialName

     * `hostnames` must be set to the wildcard "*". **Note:** Do not create two ApigeeRoute objects with a wildcard "*" hostname.
  2. Open your overrides file and make the change described in the next step.
  3. For each environment group, add the ApigeeRoute name to the `additionalGateways` property. For example: 
         
         virtualhosts:
           - name: default
             sslCertPath: ./certs/fullchain.pem
             sslKeyPath: ./certs/privkey.pem
             additionalGateways: ["ROUTE_NAME"]

  4. Save the CRD file. For example: `ApigeeRoute.yaml`
  5. Apply the CRD to the cluster: 
         
         kubectl apply -f ApigeeRoute.yaml -n APIGEE_NAMESPACE

  6. Apply the change to `virtualhosts`. If you have set the $ENV_GROUP environment variable in your shell, you can use that in the following commands: 
         
         helm upgrade $ENV_GROUP apigee-virtualhost/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set envgroup=$ENV_GROUP \
           -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ENV_GROUP_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.



##  Usage notes 

  * **What happens if the cluster has more than one org?**

Since the ingress is at the cluster level for a given port (443), and there can only be one key/cert pair for the ApigeeRoute CRD, all orgs must share the same key/cert pair.

  * **What happens if the cluster has more than one environment group? Will it work if the virtual hosts share the same key/cert pair?**

All hostnames across all environment groups must use the same key/cert pair. 

  * **Why are we creating an ApigeeRoute instead of Gateway?**

ApigeeRoutes can be validated by Apigee; however, [Gateway](https://istio.io/latest/docs/reference/config/networking/gateway/) (the Istio CRD) cannot be. Technically, even Gateway can work, but we can prevent potential configuration mistakes (through a validation webhook). 

  * **How can I configure non-SNI clients for Apigee?**

If your Apigee instance is exposed through a Google Load Balancer, then the Load Balancer supports non-SNI clients as explained [in the Load Balancing documentation.](https://cloud.google.com/load-balancing/docs/ssl-certificates#multiplessl-selection) Otherwise, if you have exposed an Apigee instance through an internal PSC endpoint or VPC, by default the Apigee instance supports non-SNI clients. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
