---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/crd-with-invalid-caBundle/
title: Troubleshoot CRDs with an invalid CA bundle \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:29.629805+00:00
---

# Troubleshoot CRDs with an invalid CA bundle  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/crd-with-invalid-caBundle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Troubleshoot CRDs with an invalid CA bundle Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) are powerful tools for [extending Kubernetes capabilities](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/). However, if a CRD contains an invalid or malformed Certificate Authority (CA) bundle within its conversion webhook configuration `spec.conversion.webhook.clientConfig.caBundle`, it can disrupt cluster operations. This issue can manifest as errors during resource creation, updates, or deletions, affecting the stability and performance of your cluster.

To prevent this issue, Google Kubernetes Engine (GKE) automatically detects CRDs with invalid CA bundles and generates a [recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders). Use this document to find the recommendation, identify your misconfigured CRDs, and update them.

This information is important for [Platform admins and operators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-platform-admin) and other users who manage CRDs and custom resources in GKE.

## Identify impacted clusters

To get insights identifying clusters that are affected by CRDs with invalid CA bundles, follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) for subtype `K8S_CRD_WITH_INVALID_CA_BUNDLE`. You can get insights in the following ways:

  * Use the Google Cloud console.
  * Use the Google Cloud CLI, or the Recommender API, filtering with the subtype `K8S_CRD_WITH_INVALID_CA_BUNDLE`.



After you identify the CRDs using the insights, follow the instructions to troubleshoot the misconfigured CA bundle.

## When GKE detects misconfigured CRDs

GKE generates an insight and recommendation with the `K8S_CRD_WITH_INVALID_CA_BUNDLE` subtype if the GKE cluster has one or more CRDs reporting a misconfigured `caBundle` for the webhook client configuration in `spec.conversion.webhook.clientConfig`.

Follow the instructions to check CRDs with misconfigured CA bundle.

## Troubleshoot the detected CRDs

The following sections have instructions for you to troubleshoot the CRDs that GKE detected as potentially misconfigured.

After you implement the instructions and the CRDs are correctly configured, the recommendation is resolved within 24 hours and no longer appears in the console. If it has been less than 24 hours since you've implemented the guidance of the recommendation, you can [mark the recommendation as resolved](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#resolve-recommendation). If you don't want to implement the recommendation, you can [dismiss it](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#dismiss-recommendation).

### Identify affected CRDs in a cluster

  1. [View insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) for subtype `K8S_CRD_WITH_INVALID_CA_BUNDLE`, choosing one insight at a time to troubleshoot. GKE generates one insight per cluster which has a broken CRD.

  2. Run the following command to describe the Service to find CRDs with potentially problematic CA bundles:
         
         kubectl get crd -o custom-columns=NAME:.metadata.name,CABUNDLE:.spec.conversion.webhook.clientConfig.caBundle
         

The output includes the following:

     * **Name** : The name of the CRD.
     * **CaBundle** : The CA bundle associated with the CRD's conversion webhook, if present. Examine the output. If the caBundle column is empty for a CRD that you know utilizes a conversion webhook, this signals a potential issue with the caBundle.



### Recreate the CRD

To resolve this error, recreate the affected CRD with a valid CA bundle:

  1. Back up existing custom resources associated with this problematic CRD, if you have any. Run the following command to export the existing resources:
         
         kubectl get <crd-name> -o yaml > backup.yaml
         

  2. Delete the existing CRD:
         
         kubectl delete crd <crd-name>
         

  3. Ensure that the `caBundle` field of the CRD contains a well-formed, base-64-encoded PEM certificate. You can do this either by editing the CRD directly or by reaching out to its authors.

  4. Modify the CRD YAML definition, updating the `spec.conversion.webhook.clientConfig.caBundle` field with the valid CA bundle data. The result should look something like the following:
         
         spec:
               conversion:
                 webhook:
                   clientConfig:
                     caBundle: <base64-encoded-ca-bundle>
         

  5. Apply the corrected CRD:
         
         kubectl apply -f <corrected-crd-file.yaml>
         

  6. Restore your custom resources:
         
         kubectl apply -f backup.yaml
         




## What's next

  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders)
  * [Troubleshooting common issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
