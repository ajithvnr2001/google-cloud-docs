---
url: https://docs.cloud.google.com/saas-runtime/docs/update-saas-offering/
title: Rollout a release \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:02:11.933553+00:00
---

# Rollout a release  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/update-saas-offering/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Rollout a release Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to roll out a release using App Lifecycle Manager.

App Lifecycle Manager enables updates across multiple provisioned units using rollouts. Rollouts target units based on their `UnitKind` and can optionally apply filters (`unit_filter`) to target a specific subset of units using the Google Cloud CLI . This allows for managed updates across your deployed base. A _rollback_ can be performed by upgrading units to a previous release.

For operations on a single, specific unit, use the controls available on the **Unit details** page.

**Note:** You cannot apply filters with App Lifecycle Manager using Google Cloud console.

## Before you begin

Before you update your App offering, you should:

  * Ensure you have [Enabled App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/enable-service).
  * Ensure you have the IAM permissions needed to create an App offering.
  * [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).
  * [Create a UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).
  * [Create and provision a Unit](https://docs.cloud.google.com/app-lifecycle-manager/provision-saas-offering).
  * Prepare a new or modified Terraform blueprint.



## Create a release

Before you can update your App offering, you must create a _release_. A release represents a specific version of your SaaS application that is defined by a blueprint package and its associated configurations. Essentially, a release _contains the update_ to your units.

### Console

  1. Go to App Lifecycle Manager.

[Go to App Lifecycle Manager](https://console.cloud.google.com/saas)

  2. Click **Releases**.

  3. On the **Releases** page, click **Create**.

  4. On the **Create Release** page:

     1. In the **Release name** box, enter a unique name for your release.
     2. In the **Unit kind** box, select the unit kind this release is associated with.
     3. In the **Only upgradeable from (optional)** section, you can optionally select releases that units can be upgraded from to this release. This lets you control upgrade paths.
     4. In the **Create Blueprint** and **Store Blueprint** steps, select or create your blueprint. Refer to [Blueprints documentation](https://docs.cloud.google.com/app-lifecycle-manager/blueprints) for detailed information on blueprints creation options.
     5. In the **Variables (optional)** section, you can optionally set input variables for this release. Refer to [Variables documentation](https://docs.cloud.google.com/app-lifecycle-manager/variables) for more information on setting variables.

**Note:** Rollouts reuse variables that were previously used during provisioning. For example, if you specified a `tenant_project_id` variable during provisioning, this variable will be reused when you create a rollout for this release. However, if you add a variable during new release creation all previously set values of `tenant_project_id` will be overridden.
  5. Click **Create**.

  6. You have created a release. You can view the release details on the **Release details** page. You will be able to reference this release when creating a rollout.




### gcloud

To create a release using Google Cloud console:
    
    
    gcloud beta app-lifecycle-manager releases create RELEASE_NAME --blueprint-package=BLUEPRINT_PACKAGE_URI --unit-kind=UNIT_KIND [--location=LOCATION] [--labels=[KEY=VALUE,...]] [--upgradeable-from-releases=[RELEASE_NAME,...]] [--input-variable-defaults=[variable=VARIABLE,value=VALUE,type=TYPE,...]]
    

Replace:

  * `RELEASE_NAME`: The ID of the release you want to create. This will be part of the full resource name for the release.
  * `BLUEPRINT_PACKAGE_URI`: The URI of the blueprint package to use for this release. Blueprints are OCI images hosted in Artifact Registry, or another OCI registry. 
    * The blueprint package contains the artifacts required for you to provision a unit, and includes metadata about the engine used (Terraform), as well as the version.
    * If you omit the hostname in the URI, it defaults to the regional Artifact Registry path (`us-east1-docker.pkg.dev`, for example).
    * See [Blueprints documentation](https://docs.cloud.google.com/app-lifecycle-manager/blueprints) for more information on creating blueprints.
  * `UNIT_KIND`: The ID or fully qualified identifier for the unit kind this release corresponds to. UNIT_KIND is immutable after you create a release.
  * `LOCATION`: The location where you want to create the release. This flag provides a fallback value for the release location if the full URI path is not provided. Defaults to the location configured in your Google Cloud CLI environment.
  * `LABELS`: (Optional) Labels to apply to the release for categorization. Labels are key-value pairs. 
    * Keys must start with a lowercase character and contain only hyphens, underscores, lowercase characters, and numbers.
    * Values must contain only hyphens, underscores, lowercase characters, and numbers.
    * For example: `--labels=environment=staging,team=app-lifecycle-manager`
  * `UPGRADEABLE_FROM_RELEASES`: (Optional) A comma-separated list of release names that specifies which existing releases can be updated with the new release you create. 
    * If you leave this flag empty, there are no constraints on which releases can be updated to this release.
    * When provided, unit update requests to this release will enforce this constraint.
  * `INPUT_VARIABLE_DEFAULTS`: (Optional) Default values for input variables required by the blueprint. 
    * You can specify variable defaults inline or by referencing a YAML or JSON file.
    * Variables defined here can be overridden during rollout creation.

**Note:** Rollouts reuse variables that were previously used during provisioning. For example, if you specify a `tenant_project_id` variable during provisioning, this variable will be reused when you create a rollout for this release unless explicitly overridden.

For more information on setting variables, see [Variables documentation](https://docs.cloud.google.com/app-lifecycle-manager/variables). For more information about releases, see [`Release`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/releases/create) Google Cloud CLI reference.

## Create a rollout kind

Before you can create a _rollout_ , you need to create a _rollout kind_ that serves as a template for how your release is deployed to your units.

### Console

  1. Go to App Lifecycle Manager.

[Go to App Lifecycle Manager](https://console.cloud.google.com/saas)

  2. Click **Rollout kinds**.

  3. On the **Rollout Kinds** page, click **Create**.

  4. On the **Create a rollout kind** page:

     1. In the **Rollout kind name** box, enter a name for your rollout kind.
     2. In the **Unit kind** box, select the unit kind detailing the type of unit you want the release to rollout.
     3. In the **Rollout strategy** drop-down, select the strategy you would like to use to deploy the release to your units:

        * **One location at a time (simple)** : Updates one location at a time (without soak times). Updates up to 5% of units concurrently.
        * **All at once (simple)** : All locations begin rolling out simultaneously (ideal for development environments and emergency scenarios).
        * **Progressive (gradual)** : Gradually rolls out updates in percentage batches exponentially across multiple locations (with soak times).
        * **Progressive (single location)** : Updates units in percentage batches with extended soak times to detect issues within a single location.

For more information about rollout strategies, see [Rollout strategies](https://docs.cloud.google.com/app-lifecycle-manager/overview#rollout_strategies).

  5. Click **Create**.

  6. You have created a rollout kind. On the **Rollout Kind details** page, you can view and edit the parameters for your rollout kind.




### gcloud

To create a rollout kind using Google Cloud console:
    
    
      gcloud beta app-lifecycle-manager rollout-kinds create ROLLOUT_KIND_NAME --unit-kind=UNIT_KIND --location=LOCATION --rollout_strategy=ROLLOUT_STRATEGY --error_budget=ERROR_BUDGET --unit_filter=UNIT_FILTER --update_unit_kind_default=UPDATE_UNIT_KIND_DEFAULT
    

Replace:

  * `ROLLOUT_KIND_NAME`: The name of rollout kind.
  * `UNIT_KIND`: Defines which units you want to apply releases to. Releases are applied to all units of the selected unit kind.
  * `LOCATION`: The location where you want to create your rollout kind.
  * `ROLLOUT_STRATEGY`: Defines the rollout strategy for your rollout kind. Possible values include:

    * `Google.Cloud.Simple.OneLocationAtATime`: Updates one location at a time (without soak times). Updates up to 5% of units concurrently.
    * `Google.Cloud.Simple.AllAtOnce`: All locations begin rolling out simultaneously (ideal for development environments and emergency scenarios).
    * `Google.Cloud.Progressive.Gradual.v1`: Gradually rolls out updates in percentage batches exponentially across multiple locations (with soak times).
    * `Google.Cloud.Progressive.SingleLocation.v1`: Updates units in percentage batches with extended soak times to detect issues within a single location.

For more information about rollout strategies, see [Rollout strategies](https://docs.cloud.google.com/app-lifecycle-manager/overview#rollout_strategies).

  * `ERROR_BUDGET`: The configuration for error budget. If the number of failed units exceeds your `error_budget` max (defined by `allowed_count`, `allowed_ratio` * `total_units`), the rollout will be paused. If `error_budget` isn't set, App Lifecycle Manager will attempt to update all units regardless of the number of failures encountered.

  * `UNIT_FILTER`: [CEL](https://github.com/google/cel-spec) formatted filter string used against units. The filter will be applied to determine the eligible unit population. This filter can only reduce the scope of the rollout. It cannot expand the rollout's scope.

  * `UPDATE_UNIT_KIND_DEFAULT`: The configuration for updating the unit kind. By default, the unit kind will be updated on the rollout start. Possible values include:

    * `UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED`: Unit kind update strategy is unspecified.
    * `UPDATE_UNIT_KIND_STRATEGY_ON_START`: Update the unit kind strategy on the rollout start.
    * `UPDATE_UNIT_KIND_STRATEGY_NEVER`: Never update the unit kind strategy.



For more information, see [`RolloutKind`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollout-kinds/create) Google Cloud CLI reference.

### Error budget feature

App Lifecycle Manager includes an error budget feature (`ErrorBudget` in `RolloutKind`) as a safeguard. This can automatically pause a rollout if the number or percentage of unit update failures (during infrastructure application, for example) exceeds a configured threshold, helping to limit the impact of potential issues during an update.

## Create a rollout

After you've created a rollout kind, you can create a rollout that specifies the release you want to update your units with.

Once the rollout is created, App Lifecycle Manager updates your units according to the strategy defined in the unit kind.

### Console

  1. Go to App Lifecycle Manager.

[Go to App Lifecycle Manager](https://console.cloud.google.com/saas)

  2. Click **Rollouts.**

  3. On the **Rollout List** page, click **Create**.

  4. On the **Create a rollout** page:

     1. In the **Rollout Kind** box, select the rollout kind detailing how to rollout your release to the specified units.
     2. In the **Release** box, specify the release to update the units with.
     3. In the **Rollout Name** box, enter a name for your rollout.
  5. Click **Create**.

  6. Your rollout has been created.

On the **Global Rollout Detail** page, you can monitor rollout details including the rollout state, rollout progress (by unit count), and rollout failures.




### gcloud

To create a rollout using Google Cloud console:
    
    
      gcloud beta app-lifecycle-manager rollouts create ROLLOUT_NAME --rollout-kind=ROLLOUT_KIND_NAME --release=RELEASE_NAME --location=LOCATION
    

Replace:

  * `ROLLOUT_NAME`: The name of the rollout.
  * `ROLLOUT_KIND_NAME`: Defines which rollout kind you want to use to apply releases to your units. Releases are applied to all units of the unit kind defined in the rollout kind.
  * `RELEASE_NAME`: Defines the release binary you want to deploy to your units.
  * `LOCATION`: The location where you want to create your rollout.



For more information, see [`Rollout`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create) Google Cloud CLI reference.

## What's next

  * To understand more about App Lifecycle Manager, see [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * To get try a tutorial see [Deploy a MySQL instance with App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql).
  * To understand how service accounts are used and how to grant granular permissions for these accounts, see [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#actuation-sa).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
