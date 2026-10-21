---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-reference/
title: Apigee hybrid Helm reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:00:39.922053+00:00
---

# Apigee hybrid Helm reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee hybrid Helm reference Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-reference.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-reference.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/helm-reference.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-reference.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/helm-reference.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-reference.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-reference.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/helm-reference.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/helm-reference.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/helm-reference.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/helm-reference.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/helm-reference.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/helm-reference.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/helm-reference.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/helm-reference.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/helm-reference.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/helm-reference.html)



## Helm supported version

Apigee hybrid supports Helm v3.14.2+. 

## Helm charts for Apigee hybrid components

The hybrid components are installed and managed by the following Helm charts. The table is arranged in the order you will typically install them in during a fresh installation. 

Scope| Components| Helm chart  
---|---|---  
**Apigee operator** | Apigee operator | `apigee-operator`  
**Storage** | Cassandra | `apigee-datastore`  
**In‑memory storage** | Redis | `apigee-redis`  
**Reporting** | Logger  
Metrics | `apigee-telemetry`  
**Ingress** | Apigee Ingress gateway | `apigee-ingress-manager`  
**Organization** | Apigee Connect Agent  
MART  
UDCA  
Watcher | `apigee-org`  
**Environment** | Runtime  
Synchronizer | `apigee-env`  
**Environment group** | virtualhost | `apigee-virtualhost`  
**Note:** The hybrid Helm charts depend on the Apigee hybrid Custom Resource Definitions (CRDs) being installed. See [Install the Apigee hybrid CRDs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-crds) in the Installation guide.

## `apigeectl` / Helm command cross reference

The following table lists the Helm equivalents for common `apigeectl` commands: 

`apigeectl` command | Helm command  
---|---  
`apigeectl init` | The following commands mimic `apigeectl init`: 

  * `kubectl apply -k apigee-operator/etc/crds/default/`
  * `helm install operator apigee-operator/` or  
`helm upgrade operator apigee-operator/`
  * `helm install ingress-manager apigee-ingress-manager/` or  
`helm upgrade ingress-manager apigee-ingress-manager/`

For example:
    
    
    kubectl apply -k  apigee-operator/etc/crds/default/
    helm install operator apigee-operator/
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml
    helm install ingress-manager apigee-ingress-manager/
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml
      
  
`apigeectl init` when used to install or apply changes to istiod. | 

  * `helm install ingress-manager apigee-ingress-manager/`
  * `helm upgrade ingress-manager apigee-ingress-manager/`

For example:
    
    
    helm upgrade ingress-manager apigee-ingress-manager/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml
      
  
`apigeectl apply` | There is no single command to manage all hybrid components. Because each component has a specific chart, you must install or upgrade each chart individually.  
`apigeectl apply --datastore` | 

  * `helm install datastore apigee-datastore/`
  * `helm upgrade datastore apigee-datastore/`

For example:
    
    
    helm upgrade datastore apigee-datastore/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml
      
  
`apigeectl apply --redis` | 

  * `helm install redis apigee-redis/`
  * `helm upgrade redis apigee-redis/`

For example:
    
    
    helm upgrade redis apigee-redis/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml
      
  
`apigeectl apply --org` | 

  * `helm install ORG_NAME apigee-org/`
  * `helm upgrade ORG_NAME apigee-org/`

For example:
    
    
    helm upgrade $ORG_NAME apigee-org/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml
      
  
`apigeectl apply --env ENV_NAME` | 

  * `helm install ENV_NAME apigee-env/`
  * `helm upgrade ENV_NAME apigee-env/`

For example:
    
    
    helm upgrade $ENV_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
    	--atomic \
      -f overrides.yaml
      
  
`apigeectl apply --all-envs` | There is no single command to manage all environments at once. You must install or upgrade each environment individually.  
`apigeectl apply --settings virtualhosts` | 

  * `helm install ENV_GROUP apigee-virtualhosts/`
  * `helm upgrade ENV_GROUP apigee-virtualhosts/`

For example:
    
    
    helm upgrade $ENV_GROUP apigee-virtualhosts/ \
      --install \
      --namespace APIGEE_NAMESPACE \
    	--set envgroup=$ENV_GROUP \
      --atomic \
      -f overrides.yaml
    

**Note:** You must install or upgrade each environment group individually.  
`apigeectl delete COMPONENT` | 

  * `helm delete RELEASE_NAME`

For example:
    
    
    helm delete datastore -n APIGEE_NAMESPACE  
  
`apigeectl delete` or  
`apigeectl delete --all` | There is no single Helm command to delete all components at once. You must delete each component individually.  
`apigeectl COMMAND --dry-run=client` | 

  * `helm COMMAND --dry-run`

For example:
    
    
    helm upgrade datastore apigee-datastore/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f overrides.yaml \
      --dry-run=server  
  
`apigeectl check-ready` | There is no equivalent Helm command.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
