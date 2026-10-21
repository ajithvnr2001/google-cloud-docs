---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/tolerations/
title: Using Kubernetes Tolerations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:16:06.455535+00:00
---

# Using Kubernetes Tolerations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/tolerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using Kubernetes Tolerations Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/tolerations.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/tolerations.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/tolerations.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/tolerations.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/tolerations.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/tolerations.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/tolerations.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/tolerations.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/tolerations.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/tolerations.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/tolerations.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/tolerations.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/tolerations.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/tolerations.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/tolerations.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/tolerations.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/tolerations.html)



**Note:** Apigee hybrid only supports Tolerations when you are using Helm charts to manage your hybrid installation. 

To use the [ Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/), you must define the `tolerations` override property for each Apigee hybrid component. The following components support defining tolerations: 

  * `ao`
  * `apigeeIngressGateway`
  * `cassandra`
  * `cassandraSchemaSetup`
  * `cassandraSchemaValidation`
  * `cassandraUserSetup`
  * `connectAgent`
  * `istiod`
  * `logger`
  * `mart`
  * `metrics`
  * `mintTaskScheduler`
  * `redis`
  * `runtime`
  * `synchronizer`
  * `udca`
  * `Watcher`



See the [ Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref) for more information about these components. 

Apply Tolerations to individual components by adding the `tolerations:` configuration properties in your overrides file and then upgrading the Helm chart for the component. 

See the [Apigee Helm charts reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-reference) for a list of which Helm charts manage each hybrid component. 

For example, to apply the tolerations to the Apigee operator deployment 

  1. Add the `tolerations:` properties to `ao:` in your overrides file: 
         
         ao:
           tolerations:
           - key: "key1"
             operator: "Equal"
             value: "value1"
             effect: "NoExecute"
             tolerationSeconds: 3600

  2. Apply the change to the `apigee-operator` chart: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           --atomic \
           -f overrides.yaml
         




To apply the tolerations to the Cassandra StatefulSet: 

  1. Add the `tolerations:` properties to `cassandra:` in your overrides file: 
         
         cassandra:
           tolerations:
           - key: "key1"
             operator: "Equal"
             value: "value1"
             effect: "NoExecute"
             tolerationSeconds: 3600

  2. Apply the change to the `apigee-datastore` chart: 
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --create-namespace \
           --namespace  \
           --atomic \
           -f overrides.yaml
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
