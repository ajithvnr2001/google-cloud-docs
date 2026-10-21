---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configure-target-timeout-limit/
title: Configure Target Timeout Limit in Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:16:28.670518+00:00
---

# Configure Target Timeout Limit in Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configure-target-timeout-limit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure Target Timeout Limit in Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configure-target-timeout-limit)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-target-timeout-limit)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/configure-target-timeout-limit)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configure-target-timeout-limit)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/configure-target-timeout-limit)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/configure-target-timeout-limit)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/configure-target-timeout-limit)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-target-timeout-limit)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/configure-target-timeout-limit)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/configure-target-timeout-limit)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/configure-target-timeout-limit)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/configure-target-timeout-limit)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/configure-target-timeout-limit)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/configure-target-timeout-limit)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/configure-target-timeout-limit)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/configure-target-timeout-limit)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/configure-target-timeout-limit)



## Overview

Starting in version 1.14.2, Apigee hybrid supports Target Timeout Limit up to 10 minutes. 

Apigee hybrid supports target `io.timeout.millis` up to 55000 milliseconds as default. See [Target Endpoint Transport Specification](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#targetendpointtransportpropertyspecification). 

To enable environments in your hybrid installation to increase target timeout limit for multiple slow target endpoints, make the following changes to your runtime configuration: 

  * Configure the `virtualhosts[].requestTimeout` between Istio and Message Processor(MP). See [virtualhosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/config-prop-ref#virtualhost)
  * Configure the `conf_http_HTTPTransport.io.timeout.millis` between MP and Targets

**Note:** For this change to be effective, you need to set both the timeouts in the runtime configuration. **Caution:** Apigee supports target io.timeout.millis up to 10 minutes. 

You can configure these settings for individual environments or for all environments in your installation.

## Configure virtualhost to change the request timeout limit

The requestTimeout is the maximum time (in seconds) set on a virtual host for a request to be processed by the MP. 

To configure the request timeout limit, you can use the `virtualhosts[].requestTimeout` properties. Make the following changes to your `overrides.yaml` file: 

  1. Add the following stanza to your `overrides.yaml` file: 
         
         virtualhosts:
         - name: ENV_GROUP_NAME
           requestTimeout: 600   # Increase requestTimeout to 600 seconds
         

  2. You must upgrade one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each environment group mentioned in the overrides.yaml file: 

Dry run:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set envgroup=ENV_GROUP_NAME \
           -f OVERRIDES_FILE \
           --dry-run=server
         

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. It is usually ENV_GROUP_NAME.

Upgrade the chart:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set envgroup=ENV_GROUP_NAME \
           -f OVERRIDES_FILE
         

**Note:** ENV_GROUP_RELEASE_NAME must be unique within the `apigee` namespace. 

For example, if you have an _environment_ named `prod` and an _environment group_ named `prod`, set the value of ENV_GROUP_RELEASE_NAME to something unique, like `prod-envgroup`. 

  3. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls environment group-related details from the control plane. Therefore, check that the corresponding AR's state is running: 
         
         kubectl -n APIGEE_NAMESPACE get arc
         
         
         NAME                                STATE   AGE
         apigee-org1-dev-egroup                       2d
         
         
         kubectl -n APIGEE_NAMESPACE get ar
         
         
         NAME                                        STATE     AGE
         apigee-org1-dev-egroup-cb9a8a              running   2d
         




## Configure individual environments to change target timeout limit

If the proxies having slow target endpoints are in only one or a few environments in your installation, you can configure the environments individually to change the target timeout limit. This avoids adding impact to other environments. 

To configure individual environments to change target timeout limit, you can use the `envs[].components.runtime` properties. Make the following changes to your `overrides.yaml` file: 

  1. Add the following stanza to your `overrides.yaml` file: 
         
         envs:
         - name: ENV_NAME
           components.
             runtime:
               cwcAppend:
                 conf_http_HTTPTransport.io.timeout.millis: 600000   # Increase io.timeout.millis to 600000 milliseconds
         

  2. You must upgrade one environment at a time. Upgrade the `apigee-env` chart for each environment you are updating: 

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run=server
         

     * ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts class="external"](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.
     * ENV_NAME is the name of the environment you are upgrading.
     * OVERRIDES_FILE is your edited `overrides.yaml` file.
  3. Upgrade the chart: 
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE
         

  4. Verify it is up and running by checking the state of the respective env:
         
         kubectl -n APIGEE_NAMESPACE get apigeeenv
         
         
         NAME                          STATE       AGE   GATEWAYTYPE
         my-org-my-env-123abc            running     2d
         

**Note** : If the upgrade command fails with the error `Forbidden: state: releasing`, the existing components are still in releasing status. You can wait for the current update to complete and then retry. Check release status with the following command: 
    
    kubectl get env -n APIGEE_NAMESPACE




## Configure all environments to change target timeout limit

Changes to your `runtime` stanza will change target timeout limit for all environments in your installation. You can override these settings for individual environments with the `runtime` properties. 

  1. Add the following stanza to your `overrides.yaml` file: 
         
         runtime:
           cwcAppend:
             conf_http_HTTPTransport.io.timeout.millis: 600000   # Increase io.timeout.millis to 600000 milliseconds
         

  2. Upgrade the `apigee-env` chart for each environment in your installation: 

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
