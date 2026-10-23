---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cert-manager-custom-namespace/
title: Running cert-manager in a custom namespace \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:54.888026+00:00
---

# Running cert-manager in a custom namespace  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cert-manager-custom-namespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Running cert-manager in a custom namespace Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cert-manager-custom-namespace.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cert-manager-custom-namespace.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cert-manager-custom-namespace.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cert-manager-custom-namespace.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cert-manager-custom-namespace.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cert-manager-custom-namespace.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cert-manager-custom-namespace.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cert-manager-custom-namespace.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cert-manager-custom-namespace.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cert-manager-custom-namespace.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cert-manager-custom-namespace.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cert-manager-custom-namespace.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cert-manager-custom-namespace.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cert-manager-custom-namespace.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cert-manager-custom-namespace.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cert-manager-custom-namespace.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cert-manager-custom-namespace.html)



This topic explains how to specify a custom Kubernetes namespace for [cert-manager](https://cert-manager.io/).

In most cases, cert-manager runs in the `cert-manager` namespace. Some users may have company policies restricting the creation of new Kubernetes namespaces or have policies requiring cert-manager to be run in a different namespace, for example `kube-system`.

## Specify a custom namespace for cert-manager

  1. Create the namespace if needed: 
         
         kubectl create namespace new-cert-manager-namespace

  2. Install cert-manager following the instructions in [Installation: Introduction](https://cert-manager.io/v1.10-docs/installation/) in the cert-manager documentation. **Note:** You will have to edit the installation manifests to install cert-manager in a custom namespace.
  3. Add a [`certManager`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#certmanager) stanza to your overrides file. 
         
         certManager:
           namespace: new-cert-manager-namespace
             

  4. Apply the namespace change: 

Test with a dry run first:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml \
           --dry-run=server
         

Apply the change:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml
         

  5. Verify that cert-manager installed correctly in the new namespace with the `kubectl get pods` command: 
         
         kubectl get pods -n new-cert-manager-namespace
         
         NAME                                      READY   STATUS    RESTARTS   AGE
         cert-manager-1234567-abcde                1/1     Running   0          21s
         cert-manager-cainjector-23456789a-bcdef   1/1     Running   0          22s
         cert-manager-webhook-3456789ab-cdef0      1/1     Running   0          20s

  6. If cert manager had previoiusly been running, delete the `cert-manager` instance in the `cert-manager` namespace by following the instructions in [Uninstall in the cert-manager documentation](https://cert-manager.io/docs/installation/kubectl/#uninstalling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
