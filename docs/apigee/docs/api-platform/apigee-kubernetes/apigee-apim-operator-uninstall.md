---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-uninstall/
title: Uninstall the Apigee Operator for Kubernetes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:25.666499+00:00
---

# Uninstall the Apigee Operator for Kubernetes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-uninstall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Uninstall the Apigee Operator for Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to uninstall the Apigee Operator for Kubernetes from a GKE cluster. The following sections outline the steps required to complete this task: 

  * Remove the API management policies.
  * Uninstall the Apigee Operator for Kubernetes.
  * Uninstall the Apigee CRDs.



## Required roles

If you assigned the required roles to your service account as described in [ Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#required-roles), no additional IAM roles or permissions are required to complete these tasks.

You can choose to authorize actions on resources in your Google Kubernetes Engine cluster using the built-in role-based access control (RBAC) mechanism in Kubernetes. For more information, see [ Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

## Remove the API management policies

To remove the API management policies, remove all `yaml` Kubernetes resources applied to the GKE cluster in reverse order. For example, if you followed the steps in [Create an `APIMExtensionPolicy`](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension) and [Add policies to the GKE Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies), you would remove the resources corresponding to the files in this order: 

  * `apigee-gateway-policy-withSA.yaml`
  * `new-admin-template.yaml`
  * `template-rule.yaml`
  * `apigee-policies.yaml`
  * `apim-policies.yaml`
  * `api-product.yaml`
  * `global-ext-lb1-apim-policy.yaml`



Remove each resource using the following command: 
    
    
    kubectl delete -f FILENAME

where FILENAME is the name of the file corresponding to the resource you want to remove. 

## Uninstall the Apigee Operator for Kubernetes

To uninstall the Apigee Operator for Kubernetes use the following commands:
    
    
    helm uninstall apigee-apim-operator -n apim
    helm repo remove apigee-apim-operator

These commands remove the Apigee Operator for Kubernetes and the Apigee CRD Helm charts from your cluster.

## Uninstall the CRDs

To uninstall the Apigee CRDs, use the following command: 
    
    
    helm uninstall apigee-apim-crds -n apim

## Troubleshoot

If you encounter issues when uninstalling the Apigee Operator for Kubernetes, see [Troubleshoot the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot) for solutions to common errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
