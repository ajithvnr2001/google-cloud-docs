---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles/
title: Apply multiple Policy Controller bundles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:49.336226+00:00
---

# Apply multiple Policy Controller bundles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Apply multiple Policy Controller bundles Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enable Policy Controller bundles.

For more detailed information about applying and using policy bundles, read the instructions for the bundle that you want to apply using the left navigation menu. For more information about policy bundles, see the [Policy Controller bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles) overview.

If you installed Policy Controller using the Google Cloud console, the [policy essentials bundle](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-policy-essentials-v2022) is installed by default, but you can enable more bundles.

## Before you begin

  * [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller).



## Apply policy bundles

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

### Console

To apply one or more policy bundles on a cluster using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.

  3. In the **Add/Edit policy bundles** menu, ensure the template library is toggled on.

  4. To enable all policy bundles, toggle **Add all policy bundles** on _check_circle_.

  5. To enable individual policy bundles, toggle on each policy bundle that you want to enable.

  6. Optional: To exempt a namespace from enforcement, expand the **Show advanced settings** menu. In the **Exempt namespaces** field, provide a list of valid namespaces.

**Best practice** : 

Exempt system namespaces to avoid errors in your environment. You can find the instructions to exempt namespaces and a list of common namespaces created by Google Cloud services on the [Exclude namespaces page](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces).

  7. Select **Save changes**.




You can view additional information about your policy coverage and violations using the [Policy Controller dashboard](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status).

### gcloud

To apply a policy bundle, complete the following steps:

  1. If any of the bundles that you're applying use referential constraints, you must enable support for referential constraints:
         
         gcloud container fleet policycontroller update --referential-rules
         

You can check whether a bundle requires support for referential constraints on the [Policy bundles overview](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).

  2. For each bundle that you want to install, run the following command:
         
         gcloud container fleet policycontroller content bundles set BUNDLE_NAME
         

Replace `BUNDLE_NAME` with the name of the bundle that you want to install. The name is the bundle prefix, for example `cis-k8s-v1.5.1`. You can find a list of names on the [Policy bundles overview](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).

  3. Optional: To exempt a namespace from enforcement, run the following command:
         
         gcloud container fleet policycontroller content bundles set BUNDLE_NAME \
           --exempted-namespaces=NAMESPACES
         

Replace `NAMESPACES` with a comma-separated list of namespaces that you don't want enforced, for example `kube-system,gatekeeper-system`.

For more information about how to add exemptable namespaces, see [Exclude namespaces from Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces).

  4. To remove a bundle, run the following command:
         
         gcloud container fleet policycontroller content bundles remove BUNDLE_NAME
         




## Troubleshooting

You can't modify policy bundles that are installed directly by using the instructions on this page. If you're having issues with a policy bundle and need to make edits, install the bundle by using one of the methods on the individual policy bundle's page. These methods pull the policy bundle from a Git repository, which lets you make changes. For example, if you want to edit the CIS Kubernetes Benchmark 1.5, follow the instructions on [Use CIS Kubernetes Benchmark v1.5.1 policy constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-benchmark) instead of this page.

**Caution:** If you're switching from applying policy bundles directly to using a manual install method, ensure that you first remove the policy bundle with either the Google Cloud console or Google Cloud CLI steps on this page before you manually install the bundle.

## What's next

  * Learn more about [applying individual constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).
  * Take a tutorial on [using policy bundles in your CI/CD pipeline to shift left](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
