---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/manage-feature-gates/
title: Manage feature gates \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:58.011125+00:00
---

# Manage feature gates  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/manage-feature-gates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage feature gates Stay organized with collections  Save and categorize content based on your preferences. 

## What is a feature gate and why do we have it?

Some Google Distributed Cloud (GDC) air-gapped appliance customers must complete an accreditation process to satisfy a set of compliance requirements. These customers might have specific features that must go through accreditation review by a third party before they can be enabled for production workloads.

Certain features might require multiple releases to get finalized and shouldn't be exposed to all customers until stable and ready. However, other customers might want to work with Google to do _proof of concept_ testing with the unreleased feature.

GDC introduces several concepts to hold features before they are ready:

  * **Deployment feature level threshold (deployment threshold)** : defines the minimum level to use for the device. This is set at bootstrap time.

  * **`FeatureGate` resource**: defines the top-level configuration tracking the default maturity level per feature. The resource also keeps track of any feature overrides the operator has added.

  * **Feature level** : tracks what level of maturity to which a given feature is set. A feature is enabled when it's greater than or equal to the deployment threshold.




Possible feature level values in ascending order are: `DEV`, `TEST`, `PREVIEW`, `PRODUCTION`, and `ACCREDITED`.

For example, if the deployment threshold is set to `PRODUCTION`, features set with feature level `ACCREDITED` or `PRODUCTION` are enabled. If the deployment threshold is set to `ACCREDITED`, only features with level `ACCREDITED` are enabled.

Feature gates or levels are not the same as A/B testing that you might see in consumer products. Feature gates are either on or off for the entire GDC device. Feature gates are designed to be turned on after accreditation review is completed and stay on.

Deployments with accreditation requirements must have their own `FeatureGate` configuration, which must match what has been accredited for that or previous versions.

## Feature level usage

There are three custom resource definitions related to configuring feature gates and levels:

  * `Stage`: defines the deployment threshold for a cluster. Stores the deployment minimum stage threshold, which is what to compare against feature gates to determine feature enablement.
  * `FeatureGate`: stores the default stage of each feature and keeps track of any overrides.
  * `SubcomponentOverride`: used by the feature gate system to override the default stage of a feature to enable it. Appears elsewhere in other contexts.



Stage value is the deployment minimum threshold stored in each cluster. This must only be set during bootstrapping and never changed after bootstrap. All features with an equal or greater feature stage value are enabled. To override the default stage of a feature gate, see [OOPS-P0072](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/operations-manual/relops/processes/oops-p0072).

Feature gates are similar to an upgrade. No images or versions change, but it is effectively the final step of an upgrade to enable the features that were added in a previous upgrade. This feature enablement might occur weeks or months after the initial upgrade, depending on how long accreditation takes. Continue performing upgrades regularly to pull in fixes and patches while accreditation is ongoing.

When features are overridden, GDC triggers a reconciler to restart all pods that depend on the feature. This must be done during a maintenance window, as some changes might require downtime.

Some features have an accompanying service manual runbook that describes when it must be enabled, and what to look for after the override has been applied. This might be for cases that requires more than a pod restart, or must be performed after other features are enabled.

You can find these feature runbooks in the service manual attached to the relevant operable component.

The list of active feature gates is available in the [Features stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/feature-stages) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
