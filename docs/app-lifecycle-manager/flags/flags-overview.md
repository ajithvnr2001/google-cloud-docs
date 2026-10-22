---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-overview/
title: App Lifecycle Manager feature flags overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:47.600301+00:00
---

# App Lifecycle Manager feature flags overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-overview/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  App Lifecycle Manager feature flags overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Lifecycle Manager feature flags let you control the availability and behavior of features within your applications, without requiring new code deployments or infrastructure changes.

You can use flags in two primary ways:

  1. **Integrated:** Couple flag management with your application deployments managed by App Lifecycle Manager.
  2. **Standalone:** Use the robust flagging system independently, even if your application infrastructure is managed elsewhere, by modeling your system components as App Lifecycle Manager Units.



Feature flags integrate with App Lifecycle Manager's core concepts like units and rollouts. This lets you manage flag configurations alongside your application infrastructure (integrated approach).

Review the main [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview) if you are not familiar with App Lifecycle Manager Units or Rollouts.

## Why use App Lifecycle Manager feature flags?

When you implement feature flags with App Lifecycle Manager it provides several benefits for your SaaS development and operations lifecycle:

  * **Decouple feature releases from code deployments:** Ship new code to production with features disabled by default. Enable features for specific users or gradually roll them out when ready, reducing the risk associated with large deployments.
  * **Increase safety, speed, and reliability:**
    * Test features in production with a limited audience (canary releases).
    * Perform gradual rollouts using App Lifecycle Manager Rollout capabilities, minimizing the impact of potential issues.
  * **Enable allow listing and tenant customization:** Turn features on or off for units which can represent tenants, services, or environments.
  * **Simplify rollbacks:** When you disable a feature flag, it's often much faster and less disruptive than deploying a previous version of your application. This workflow lets you disable problematic features without rolling back binaries.
  * **Unified management of flag configurations:** Manage feature flag definitions and use them to configure rollouts. This workflow provides operational reliability by letting you change your application's functionality by creating feature flag rollouts.



## How App Lifecycle Manager feature flags work

Using feature flags in App Lifecycle Manager involves two main aspects: the management plane (defining and rolling out flags) and the data plane (accessing flag values within your application).

### Integrated usage with App Lifecycle Manager

If you use App Lifecycle Manager to manage your application deployments (for example, deploying infrastructure using Terraform Blueprints):

  1. **Define flags:** Create feature flag resources within App Lifecycle Manager, specifying a unique `Flag key` (`enable-new-dashboard`, for example) and associating it with a unit kind. Boolean flags are supported.
  2. **Provision flag changes:** Changes to flags (creation or updates) are not live until you initiate an App Lifecycle Manager rollout. This lets you use features like batches, supervision, and safety checks for flag deployments. The rollout updates the flag configuration associated with the targeted units.
  3. **Access flags in application:** Your application code, running within the provisioned unit (for example, in a container on Cloud Run or Google Kubernetes Engine), uses an OpenFeature SDK configured with the `flagd` provider. This provider connects to the `saasconfig.googleapis.com` service endpoint. Using App Lifecycle Manager, inject the necessary unit identifier into your application environment, letting the SDK fetch the correct flag values for that specific unit.



This deep integration lets you manage feature lifecycles alongside infrastructure lifecycles. For a practical example, see the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart).

### Management plane

You interact with the management plane to define and control your flags. You can use Google Cloud console, gcloud CLI, or the App Lifecycle Manager API to:

  * Create or update flags: To define flags, you specify the `Flag key`, associate it with a unit kind, and set its type and default value.
  * Create rollouts: You initiate a rollout to distribute flag changes (creations or updates) to the targeted units belonging to the flag's unit kind. Rollouts ensure changes are applied safely and reliably according to your configured policies.



### Data plane

Your application code interacts with the data plane to consume flag values:

  * **OpenFeature SDK:** Integrate the vendor-neutral [OpenFeature](https://openfeature.dev) SDK into your application.
  * **`flagd` provider:** Configure the OpenFeature SDK to use the `flagd` provider.
  * **Configuration:** Point the `flagd` provider to the App Lifecycle Manager feature flag service endpoint: `saasconfig.googleapis.com:443`.
  * **Targeting:** Provide the `provider_id` to identify the flag configuration. This value typically corresponds to the full resource name of the App Lifecycle Manager unit (`projects/PROJECT_ID/locations/LOCATION/featureFlagsConfigs/UNIT_ID`, for example).
  * **Authentication:** The provider uses Application Default Credentials (ADC) to securely authenticate requests to the Google Cloud service endpoint. The service account used needs the `roles/saasconfig.viewer` Identity and Access Management role.
  * **Flag evaluation:** Use [standard OpenFeature methods (`client.get_boolean_value(...)`)](https://openfeature.dev/docs/reference/concepts/evaluation-api/#basic-evaluation,%20for%20example) in your code to check flag values. The provider handles fetching the latest rolled-out configuration from the service.



App Lifecycle Manager provides reference implementations and examples for integrating with the data plane:

  * [Using feature flags with Python](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart)



## Feature flag value types

App Lifecycle Manager feature flags support more than standard on/off boolean evaluations. You can define flags with `STRING`, `INTEGER`, or `DOUBLE` values to control complex operational variables such as runtime thresholds, theme parameters, or configuration limits.

Unlike with boolean flags, you need to explicitly define non-boolean flags during creation to dictate the universe of possible return types.

**Note:** Percentage-based allocations are not supported for non-boolean flags. You must rely on `defaultTarget` configuration or use standard CEL-based targeting logic to assign specific values. 

### String flags

String flags pass configuration identifiers directly to connected clients.
    
    
    gcloud beta app-lifecycle-manager flags create "feature-mode" \
      --key="feature-mode" \
      --flag-value-type=STRING \
      --location="global" \
      --unit-kind="UNIT_KIND_ID" \
      --variants='[{"id": "standard", "stringValue": "STANDARD"}, {"id": "advanced", "stringValue": "ADVANCED"}]' \
      --evaluation-spec='{"defaultTarget": "standard"}'
    

### Integer flags

Integer flags govern exact numerical limits and payload boundaries.
    
    
    gcloud beta app-lifecycle-manager flags create "max-retry-count" \
      --key="max-retry-count" \
      --flag-value-type=INTEGER \
      --location="global" \
      --unit-kind="UNIT_KIND_ID" \
      --variants='[{"id": "low", "integerValue": 3}, {"id": "high", "integerValue": 10}]' \
      --evaluation-spec='{"defaultTarget": "low"}'
    

### Double flags

Double flags deliver high-precision values used for probability thresholds or float parameters.
    
    
    gcloud beta app-lifecycle-manager flags create "sampling-rate" \
      --key="sampling-rate" \
      --flag-value-type=DOUBLE \
      --location="global" \
      --unit-kind="demo-test-unitkind" \
      --variants='[{"id": "minimal", "doubleValue": 0.01}, {"id": "full", "doubleValue": 1.0}]' \
      --evaluation-spec='{"defaultTarget": "minimal"}'
    

## Provision feature flags using rollouts

App Lifecycle Manager ensures safe changes or updates at scale by using rollouts to provision feature flag updates.

Without staged rollouts, a minor flag configuration change (enabling a feature for 1% of users, for example) propagates instantaneously across all application instances. If this feature introduces a regression, issues can occur simultaneously across your entire infrastructure. This global propagation significantly elevates your risk of widespread service impact.

App Lifecycle Manager rollouts mitigate this risk by enabling gradual, controlled distribution of flag changes, limiting the potential scope of any unforeseen problems.

## Feature flag sets

Feature flag sets group multiple feature flags together and lets you manage them as a single logical resource. This is useful for releasing features that require multiple flags to be coordinated.

[Learn more about flag sets](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-sets).

## Manifests

Manifests let you define and manage feature flags using JSON files. You can push these definitions to the App Lifecycle Manager API, or pull existing configurations to generate type-safe accessors for your application.

[Learn more about manifests](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-manifests).

## Complex targeting

You can use Common Expression Language (CEL) to create sophisticated targeting rules based on user or request attributes for precise control over which users see which features.

[Learn more about complex targeting](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-targeting).

## Multi-tenant architecture

You can use multi-tenant deployments with App Lifecycle Manager if you target flags to specific units or groups of units (using labels, or tenants). You can also implement gradual rollouts across your tenant fleet.

[Learn more about multi-tenant architecture](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-multi-tenant).

## Allocate feature flags

Define _allocations_ (such as _experimental_ or _baseline_) and use traffic splitting to perform tests, or randomized rollouts.

[Learn more about feature flag allocations](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-experimentation).

## What's next

  * Try the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart) to integrate flags with an App Lifecycle Manager-managed deployment.
  * Review the main [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview) if you are new to the platform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
