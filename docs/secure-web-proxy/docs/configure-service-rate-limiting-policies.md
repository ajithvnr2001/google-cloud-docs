---
url: https://docs.cloud.google.com/secure-web-proxy/docs/configure-service-rate-limiting-policies/
title: Configure service rate limiting policies \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:37.029236+00:00
---

# Configure service rate limiting policies  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/configure-service-rate-limiting-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Configure service rate limiting policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure [service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#rate-limiting-policies) for Secure Web Proxy to protect your systems from traffic overloads and manage the costs of outbound web traffic.

## Before you begin

  * Review the [Secure Web Proxy overview](https://docs.cloud.google.com/secure-web-proxy/docs/overview) and [Service rate limiting policies overview](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#rate-limiting-policies) pages.

  * [Enable the following APIs](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#enable-apis):

    * Network Security API (`networksecurity.googleapis.com`)
    * Network Services API (`networkservices.googleapis.com`)

To enable the APIs, run the following command:
    
    gcloud services enable \
        networksecurity.googleapis.com \
        networkservices.googleapis.com
    

  * Make sure that your user account has the required administrative [roles and permissions](https://docs.cloud.google.com/secure-web-proxy/docs/roles-permissions) to configure Secure Web Proxy resources.

  * A Secure Web Proxy instance must be active before you can create a policy. For more information, see [Deploy a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).

  * Optional: To create a rate limiting policy based on client certificate identities (such as `CLIENT_CERT_COMMON_NAME`), make sure that you [configure frontend mutual TLS (mTLS)](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp).




## Set up a service rate limiting policy

To create a service rate limiting policy, define your configuration in a YAML file and then import that file into Secure Web Proxy.

  1. Create the `my-rate-limit-policy.yaml` file, and then specify the policy parameters.

The following example limits the number of requests sent to a large language model (LLM) provider (`foo.com`) to 100 requests per minute for each agent on a Secure Web Proxy gateway for outbound traffic. Each agent is identified by the common name in its client certificate.
         
         name: "projects/ PROJECT_ID /locations/ LOCATION /rateLimitPolicies/test-policy"
           description: "Simple agent for LLM rate limiting."
           httpRules:
           # Match on the provider host name.
           - to:
               destination:
                 hosts:
                 - exact: "foo.com"
         
             # default RPM bucket
             rateLimitActions:
             - rateLimitBucket: "rl_default_rpm_limit"
         
           rateLimitBuckets:
           - name: "rl_default_rpm_limit"
             # Identify client by its client cert name
             keys:
             - keyType: PRINCIPAL
               principalType: CLIENT_CERT_COMMON_NAME
             defaultLimit:
               countLimit:
                 count: 100
                 interval: 1
                 intervalUnit: MINUTES
         
           targets:
           - resource: "projects/ PROJECT_ID /locations/ LOCATION /gateways/ GATEWAY_NAME "
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `LOCATION`: region of your Secure Web Proxy instance; for example, `us-central1`
     * `GATEWAY_NAME`: name of your Secure Web Proxy gateway instance
  2. Import the rate limit policy YAML file by using the following command:
         
         gcloud alpha network-security rate-limit-policies import test-policy \
           --source=my-rate-limit-policy.yaml \
           --location=LOCATION
         

Replace `LOCATION` with the region of your Secure Web Proxy instance.




## What's next

  * [Understand a service rate limiting policy log entry](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs#srl-logs)
  * [Configure log alerts for throttled traffic](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs#alert-for-throttled-traffic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
