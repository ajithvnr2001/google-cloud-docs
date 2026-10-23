---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/ingress-tls/
title: Configuring TLS and mTLS on the ingress gateway \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:39.390911+00:00
---

# Configuring TLS and mTLS on the ingress gateway  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/ingress-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring TLS and mTLS on the ingress gateway Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/ingress-tls.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/ingress-tls.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/ingress-tls.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/ingress-tls.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/ingress-tls.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/ingress-tls.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/ingress-tls.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/ingress-tls.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/ingress-tls.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/ingress-tls.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/ingress-tls.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/ingress-tls.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/ingress-tls.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/ingress-tls.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/ingress-tls.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/ingress-tls.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/ingress-tls.html)



This topic explains how to enable one-way TLS and mTLS on the ingressgateway. 

##  Configuring one-way TLS 

Use one-way TLS to secure API proxy endpoints on the ingress gateway. To enable one-way TLS, you configure the ingress with TLS cert/key pairs or with a Kubernetes Secret, as explained in the following options.

### Option 1: key/cert pair

Provide SSL cert and key files in the `virtualhosts` property in your overrides file: 
    
    
    virtualhosts:
      - name: $ENVIRONMENT_GROUP_NAME
        sslCertPath: "$CERT_FILE"
        sslKeyPath: "$KEY_FILE"

**Note:** See 
* [`virtualhosts.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-name)
* [`virtualhosts.sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-sslcertpath)
* [`virtualhosts.sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-sslkeypath)

Where $ENVIRONMENT_GROUP_NAME is the name of an environment group with corresponding host aliases, and $CERT_FILE and $KEY_FILE are TLS key and certificate files. See [Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates). 

**Tip:** For security purposes, it is best practice to have a separate TLS cert/key pair for each virtual host. If you are using a Subject Alternative Name (SAN ) certificate, this TLS cert/key pair should be used on one virtual host that is shared across the domain. 

### Option 2: Kubernetes Secret

Create a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) and add it to your overrides file.

  1. Create the Secret in the `**apigee**` namespace: 
         
         kubectl create -n APIGEE_NAMESPACE secret generic $SECRET_NAME  \
           --from-file=key=$KEY_FILE \
           --from-file=cert=$CERT_FILE

  2. Configure the `virtualhosts` property in your overrides file: 
         
         virtualhosts:
           - name: $ENVIRONMENT_GROUP_NAME
             tlsMode: SIMPLE  # Note: SIMPLE is the default, so it is optional.
             sslSecret: $SECRET_NAME

**Note:** See 
     * [`virtualhosts.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-name)
     * [`virtualhosts.tlsMode`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-tlsmode)
     * [`virtualhosts.sslSecret`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-sslsecret)

##  Configuring mTLS 

Instead of one-way TLS, you can configure [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication) on the ingress gateway. There are two options for configuring mTLS, as explained below. 

### Option 1: key/cert pair and CA file

Provide TLS certificate data containing Certificate Authority certificates: 
    
    virtualhosts:
      - name: $ENVIRONMENT_GROUP_NAME
        tlsMode: MUTUAL
        caCertPath: "$CA_FILE"
        sslCertPath: "$CERT_FILE"
        sslKeyPath: "$KEY_FILE"

**Note:** See 
     * [`virtualhosts.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-name)
     * [`virtualhosts.tlsMode`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-tlsmode)
     * [`virtualhosts.caCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-cacertpath)
     * [`virtualhosts.sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-sslcertpath)
     * [`virtualhosts.sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-sslkeypath)

Where $ENVIRONMENT_GROUP_NAME is the name of an environment group with corresponding host aliases, $CA_FILE specifies TLS certificate data (CA bundle file) containing Certificate Authority certificates, and $CERT_FILE and $KEY_FILE are TLS key and certificate files. See [Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates). 

### Option 2: Kubernetes Secrets

Create two Kubernetes Secrets. The first secret is for the SSL cert/key pair and the second is for the CA. Then, add them to your overrides file. 

     1. Create two Kubernetes secrets the `**apigee**` namespace: 
            
            kubectl create -n APIGEE_NAMESPACE secret generic $SECRET_NAME  \
              --from-file=key=$KEY_FILE \
              --from-file=cert=$CERT_FILE

     2. Create a secret for the CA: 
            
            kubectl create -n APIGEE_NAMESPACE secret generic $SECRET_NAME-cacert  \
              --from-file=cacert=$CA_FILE

     3. Configure the `virtualhosts` property in your overrides file: 
            
            virtualhosts:
              - name: $ENVIRONMENT_GROUP_NAME
                tlsMode: MUTUAL  # Note: Be sure to specify MUTUAL
                sslSecret: $SECRET_NAME

**Note:** See 
        * [`virtualhosts.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-name)
        * [`virtualhosts.tlsMode`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-tlsmode)
        * [`virtualhosts.sslSecret`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-sslsecret)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
