---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-connect/
title: Apigee Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:40.684996+00:00
---

# Apigee Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Connect Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-connect.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-connect.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/apigee-connect.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/apigee-connect.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/apigee-connect.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/apigee-connect.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-connect.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-connect.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/apigee-connect.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/apigee-connect.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/apigee-connect.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/apigee-connect.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/apigee-connect.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/apigee-connect.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/apigee-connect.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/apigee-connect.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/apigee-connect.html)



This section describes using Apigee Connect for communication between the hybrid management plane and the MART service in the runtime plane.

## Introduction

Apigee Connect allows the Apigee hybrid management plane to connect securely to the MART service in the runtime plane without requiring you to expose the MART endpoint on the internet. If you use Apigee Connect, you do not need to configure the MART ingress gateway with a host alias and an authorized DNS certificate.

![Primary services that execute on the hybrid runtime plane showing Apigee Connect](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.17/images/arch-runtime-apigee-connect.png)

## Configuring Apigee connect

Configure Apigee connect in your overrides with the [`connectAgent`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent) configuration property. 

### Service account

Apigee connect uses the [`apigee-mart`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/mart-service-account) service account. This service account requires the Apigee Connect Agent `roles/apigeeconnect.Agent` role. See [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about#recommended-sas). 

Use the [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent-serviceaccountpath) or [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent-serviceaccountref) configuration properties to specify the `apigee-mart` service account key. Alternatively you can [store the service account key in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault). 

### API

Apigee Connect requires the **Apigee Connect API** in the [Google Cloud API Library](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cloud.google.com/endpoints/docs/openapi/enable-api). For instructions on enabling APIs in the Google Cloud console, see [Step 3: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-enableapi). 

### Applying Apigee connect configuration

Apply changes to the Apigee connect configuration with the `apigee-org` chart with the following command: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ORG_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

### Image

Apigee connect uses the `gcr.io/apigee-release/hybrid/apigee-connect-agent:1.17.1` image. If you want to use a private image repository, see [Use a private image repository with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/container-images). 

## Checking Apigee connect logs

Check the Apigee Connect Agent log. 
    
    
    kubectl logs -n namespace apigee-connect-agent-pod-name

  
The Apigee Connect Agent reports the following log categories:  
Audit logs category | Operations  
---|---  
DATA_READ | `ConnectionService.ListConnections`  
DATA_WRITE | `Tether.Egress`  
For help on viewing audit logs in Apigee hybrid see [ Audit logging information](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/audit-logging-info). 

You can set the level of logging with the [`connectAgent.logLevel`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent-loglevel) configuration property.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
