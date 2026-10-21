---
url: https://docs.cloud.google.com/looker/docs/updating-your-looker-instance/
title: Preparing your Looker deployment for updates \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:41:20.232336+00:00
---

# Preparing your Looker deployment for updates  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/updating-your-looker-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Preparing your Looker deployment for updates Stay organized with collections  Save and categorize content based on your preferences. 

Looker releases a new product version every month — with rare exceptions — that is full of new features, updates, and changes. Most Looker customers are able to take advantage of these updates as soon as they are available, because [Looker hosts, manages, and updates their Looker deployments](https://docs.cloud.google.com/looker/docs/looker-hosted-installation-steps). However, if you [self-host](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps) your Looker deployment or are holding off on updating because of [feature deprecations](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#migrating_away_from_legacy_features), you can fall behind and miss the latest and greatest Looker has to offer.

## Why should you update your Looker deployment?

In addition to the fact that Looker is constantly releasing new functionality to improve user experience, there are important reasons to stay current:

  * Looker provides product support coverage for Looker instances on the latest stable version and the two previous versions, as well as the [extended support release (ESR)](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview). Because a new Looker version is released every month — with rare exceptions — going three months without updating puts you outside the stable window. The latest version provides all new features and updates, along with the latest bug fixes.
  * Looker takes [security](https://looker.com/product/security) very seriously and updates the product to address any new web vulnerabilities. While Looker keeps supported releases as safe as possible, you can do your part by staying current with Looker to ensure that your Looker instance has access to the latest security patches.



## Steps and considerations when updating

The following steps can help you prepare your Looker deployment for updates:

  1. Address any concerns about updating.
  2. Review the release notes.
  3. Prepare for LookML parameter and feature deprecations.
  4. Create a backup of your instance — and restore to any staging environments.
  5. Update your staging instances and test.
  6. Update your production environment.



These steps may or may not apply to your deployment, depending on whether or not you have staging environments.

### Address any concerns about updating

Sometimes you may want to prevent updates for a specific functional reason. This could be a significant change in functionality for which you need more time to train your users, or it could be a feature, tool, or LookML parameter that was deprecated in a new release that is operationally critical for your business, such as an API endpoint that is used by a script or separate application.

If the reason is a feature or LookML parameter deprecation, be sure to review the release notes and prepare for the deprecation.

### Review the release notes

Looker's release notes describe what is new in each release so that you can stay abreast of new features that your users should take advantage of and any breaking changes that may affect rollout of a new version. See the [Looker releases](https://docs.cloud.google.com/looker/docs/looker-releases) page for links to the release notes and changelog for the latest release:

  * See the release highlights to read about the most exciting new features, and make sure to review the **Potentially breaking changes** section to identify breaking changes that you may need to prepare for.

  * See the changelog for more granular details about feature updates and bug fixes.




### Prepare for LookML parameter and feature deprecations

Enhancements to LookML can include parameter deprecations. Update your LookML to keep everything working in the new version. Check the [legacy feature schedule](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) for deprecated LookML parameters that have been completely removed, in or prior to the version to which you are updating.

To prepare for feature deprecations, follow the steps suggested in the [Migrating away from legacy features](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#migrating_away_from_legacy_features) section of the **Legacy features** documentation page.

> It's best practice to update your LookML to remove ALL deprecated LookML, as those parameters will be removed in a future release.

### Create a backup of your instance — and restore to any staging environments

[Creating regular backups](https://docs.cloud.google.com/looker/docs/creating-backups) is strongly recommended and should be completed before each update. Additionally, while this is not required, if you are updating several versions it's a good idea to set up a staging server where you can test the updated version before rolling it out to your entire company.

There are different steps for creating backups depending on whether your Looker deployment is self-hosted or is hosted by Looker.

#### Creating backups for customer-hosted Looker

If you host your own Looker instance, you can follow the guide for [creating backups](https://docs.cloud.google.com/looker/docs/creating-backups) and use the guide for [restoring backups](https://docs.cloud.google.com/looker/docs/restoring-backups) to a new staging environment.

### Update your staging instances and test

If you have a staging instance, you can deploy and test the update prior to updating your production instance. There are different steps for updating your Looker instance depending on whether your Looker deployment is self-hosted or hosted by Looker.

#### Updating a staging instance for customer-hosted Looker deployments

If you host your own Looker instance, download the latest [release JAR](https://docs.cloud.google.com/looker/docs/downloading-looker-jar-files) and follow the instructions on the [Updating a Looker instance](https://docs.cloud.google.com/looker/docs/updating-looker-instance) documentation page to update your staging instance to the latest Looker version. Be sure to check the [Deployment specifications](https://docs.cloud.google.com/looker/docs/installing-looker-application#server_specifications) section on the **Installing the Looker application** documentation page for the latest server requirements — particularly for the Java version.

#### Updating a staging instance for Looker-hosted Looker deployments

If your instance is hosted by Looker, reach out to your Looker contact or [Looker Support](http://console.cloud.google.com/support/cases) to have our team update your staging instance for you.

Once your staging instance is up to date, log in and test the new features and updates. Make sure your important dashboards and Looks run without errors and that there are no (new) LookML errors when you validate your LookML models.

### Update your production environment

If all tests are successful on your staging instance, you can go ahead and update your production instance to the latest version of Looker, following the same process you used for staging. _Before updating your production instance, be sure you have performed a recent backup in case you need to restore for any reason._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
