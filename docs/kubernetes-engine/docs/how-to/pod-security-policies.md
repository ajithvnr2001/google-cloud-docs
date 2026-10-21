---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies/
title: PodSecurityPolicy deprecation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:27.358404+00:00
---

# PodSecurityPolicy deprecation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  PodSecurityPolicy deprecation Stay organized with collections  Save and categorize content based on your preferences. 

PodSecurityPolicy (beta) is deprecated in Kubernetes version 1.21 and removed in version 1.25. To learn more, refer to the [PodSecurityPolicy deprecation blog post](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/). For Google Kubernetes Engine (GKE) clusters running version 1.25 or later, you can no longer use PodSecurityPolicy, and you must disable the feature before upgrading to versions 1.25 or later. For instructions, refer to [Migrate from PodSecurityPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-podsecuritypolicy#disable-psp).

## Alternatives to PodSecurityPolicy

If you want to continue using Pod-level security controls in GKE, we recommend one of the following solutions:

  * **Use the`PodSecurity` admission controller**: You can use the [`PodSecurity` admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission) to apply Pod Security Standards to Pods running on your GKE Standard and Autopilot clusters. Pod Security Standards are predefined security policies that meet the high-level needs of Pod security in Kubernetes. These policies are cumulative, and range from being highly permissive to being highly restrictive.

To migrate your existing PodSecurityPolicy configuration to `PodSecurity`, refer to [Migrate from PodSecurityPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-podsecuritypolicy).

  * **Use Policy Controller with the Pod Security Policy bundle** : Policy Controller lets you apply and enforce security policies in your GKE clusters. Policy Controller [_bundles_](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles), like the Pod Security Policy bundle, let you enforce the same validations as PodSecurityPolicy with capabilities such as dry-run and fine-grained control over resource coverage.

For more information, refer to [Use Policy Controller's Pod Security Policy bundle](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-constraints-to-enforce-pod-security).

  * **Use Gatekeeper** : GKE Standard clusters allow you to apply security policies using Gatekeeper. You can use Gatekeeper to enforce the same capabilities as PodSecurityPolicy, as well as take advantage of other functionality such as dry-run, gradual rollouts, and auditing.

For more information, refer to [Apply custom Pod-level security policies using Gatekeeper](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper).

  * **Use GKE Autopilot clusters** : GKE Autopilot clusters implement many of the recommended security policies by default.

For more information, refer to the [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).




## View deprecation insights and recommendations

You can check which clusters use this deprecated feature by using [deprecation insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations#view-deprecation-insights-recs). Deprecation insights for this feature are supported for clusters running any GKE version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
