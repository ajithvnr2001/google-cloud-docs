---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/base-path-routing/
title: Configure virtual hosts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:18.079130+00:00
---

# Configure virtual hosts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/base-path-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure virtual hosts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/base-path-routing.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/base-path-routing.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/base-path-routing.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/base-path-routing.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/base-path-routing.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/base-path-routing.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/base-path-routing.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/base-path-routing.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/base-path-routing.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/base-path-routing.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/base-path-routing.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/base-path-routing.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/base-path-routing.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/base-path-routing.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/base-path-routing.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/base-path-routing.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/base-path-routing.html)



This topic discusses the [virtualhosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts) configuration property. Virtual hosts allow Apigee hybrid to handle API requests to hostaliases associated with an environment group. For more information, see [Routing and base paths](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#routing) in the [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) topic. 
    
    
    ...
    virtualhosts:
      - name: my-env-group
        sslCertPath: ./certs/fullchain.pem
        sslKeyPath: ./certs/privkey.key
    ...

When an API proxy call comes, it is routed to the host alias(es) of the environment group where the API proxy is deployed. 

For instructions on how to apply `virtualhosts` to the cluster, see Applying virtualhosts changes. For information about configuring TLS, see [Configuring TLS and mTLS on the Istio ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/ingress-tls). 

##  Adding multiple virtual hosts 

The [`virtualhosts[]`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts) property is an array, and therefore you can create more than one. 
    
    
    ...
    virtualhosts:
      - name: my-env-group-1
        sslCertPath: ./certs/fullchain1.pem
        sslKeyPath: ./certs/privkey1.key
    
      - name: my-env-group-2
        sslCertPath: ./certs/fullchain2.pem
        sslKeyPath: ./certs/privkey2.key
    ...

**Tip:** For security purposes, it is best practice to have a separate TLS cert/key pair for each virtual host. If you are using a Subject Alternative Name (SAN ) certificate, this TLS cert/key pair should be used on one virtual host that is shared across the domain. 

For information about configuring TLS, see [Configuring TLS and mTLS on the Istio ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/ingress-tls).

##  Applying `virtualhosts` changes 

If you only add or change the `virtualhosts` property, apply the changes with the `apigee-virtualhost` chart and the name of the environment group to which you are applying the changes: 
    
    
    helm upgrade $ENV_GROUP apigee-virtualhost/ \
      --namespace apigee \
      --atomic \
      --set envgroup=$ENV_GROUP \
      -f OVERRIDES_FILE.yaml
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ENV_GROUP_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

If, for example, you change `virtualhosts` and `env`, then you must apply the change with `helm upgrade` without using the `ENV_GROUP apigee-virtualhost/`flag to update the cluster. For example:

Run helm upgrade for each environment you want to update.
    
    
    helm upgrade $ENV_NAME apigee-env/ \
      --namespace apigee \
      --atomic \
      --set env=$ENV_NAME \
      -f OVERRIDES_FILE.yaml
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ENV_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

## TLS keys and certificates

The `virtualhost` property requires a TLS key and certificate. The key/cert are used to provide secure communication with the ingress gateway and must be compatible with the host aliases used in the specified environment group.

It is up to you how you generate proper TLS certificate/key pairs for your hybrid configuration. The following topics are provided as samples only, intended primarily for trying out or testing a new hybrid installation if it isn't feasible to obtain TLS credentials in another way: 

  * See [Obtain TLS credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/lets-encrypt) for a set of sample steps for creating an authorized TLS certificate/key pair.
  * You can use a self-signed certificate/key pair(s) for testing purposes only. See [Generate self-signed TLS credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/environment-self-signed-tls). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
