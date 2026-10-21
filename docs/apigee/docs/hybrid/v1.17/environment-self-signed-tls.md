---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-self-signed-tls/
title: Generate self-signed TLS credentials \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:08:50.494553+00:00
---

# Generate self-signed TLS credentials  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-self-signed-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Generate self-signed TLS credentials Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-self-signed-tls.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/environment-self-signed-tls.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/environment-self-signed-tls.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/environment-self-signed-tls.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environment-self-signed-tls.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/environment-self-signed-tls.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/environment-self-signed-tls.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/environment-self-signed-tls.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/environment-self-signed-tls.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/environment-self-signed-tls.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/environment-self-signed-tls.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/environment-self-signed-tls.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/environment-self-signed-tls.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/environment-self-signed-tls.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/environment-self-signed-tls.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/environment-self-signed-tls.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/environment-self-signed-tls.html)



This topic explains how to create self-signed TLS certificates for use in an environment configuration. This information is intended for trial or testing purposes only. 

**Warning:** Self-signed certificates are not recommended for production. Only consider using them for development, trial, or testing purposes.

The runtime ingress gateway (the gateway that handles API proxy traffic) requires a TLS certificate/key pair. For this quickstart installation, you can use self-signed credentials. In the following steps, [openssl](https://www.openssl.org/) is used to generate the credentials. 

  1. Navigate to your `HELM_CHARTS_HOME/apigee-virtualhost/` chart directory and execute the following command to create the certificate and key files. The certificate files will most likely have `.crt` or `.pem` extensions and the key file will most likely have `.key`. **Note:** We recommend storing the certificate and key files in your `HELM_CHARTS_HOME/apigee-virtualhost/` chart directory.
         
         openssl req  -nodes -new -x509 -keyout ./certs/keystore.key -out \
             ./certs/keystore.pem -subj '/CN=mydomain.net' -days 3650

This command creates a self-signed certificate/key pair that you can use for the quickstart installation. The CN `mydomain.net` can be any value you wish for the self-signed credentials. 

  2. Check to make sure the files are in the `./certs` directory: 
         
         ls ./certs
           keystore.pem
           keystore.key

Where `keystore.pem` is the self-signed TLS certificate file and `keystore.key` is the key file. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
