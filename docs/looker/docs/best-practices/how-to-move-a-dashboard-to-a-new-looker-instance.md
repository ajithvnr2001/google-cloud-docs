---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-move-a-dashboard-to-a-new-looker-instance/
title: Moving a dashboard to another Looker instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:18.871817+00:00
---

# Moving a dashboard to another Looker instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-move-a-dashboard-to-a-new-looker-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Moving a dashboard to another Looker instance Stay organized with collections  Save and categorize content based on your preferences. 

There are two methods for moving dashboards from one Looker instance to another:

  * By using a Git repository



This method involves converting a user-defined dashboard (UDD) to a LookML dashboard, and then migrating the dashboard to a new instance by using a Git repository. This method is supported by Looker.

  * By using Gazer



This method involves using an open-source command line tool to migrate a UDD to a new instance. This method is _not_ supported by Looker.

## Using a Git repository to migrate dashboards

If you have multiple Looker instances in your development lifecycle, you may want to move dashboards across those instances. To do this, save your dashboards as [LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards) and migrate them by using your Git repository. The process is as follows:

  1. If your dashboard is not already a LookML dashboard, [create a LookML copy](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#creating_a_lookml_copy_of_a_user-defined_dashboard) of your user-defined dashboard.
  2. [Deploy your data model to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production) on the first instance, and follow your chosen process for deploying that model to the next instance in your deployment lifecycle. (The [Git Workflow Using One Repository Across Multiple Instances — Development, Staging, and Production](https://discuss.google.dev/t/git-workflow-using-one-repository-across-multiple-instances-development-staging-and-production/119304) Community post describes one option for setting that up.)
  3. On your second instance, you will see your dashboard saved in the [LookML dashboards folder](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#lookml_dashboards_folder).
  4. Optionally, you can [convert the LookML dashboard back to a user-defined dashboard](https://docs.cloud.google.com/looker/docs/converting-lookml-to-user-defined-dashboard) on the second instance.



## Using Gazer to migrate dashboards

**Important:** Because Gazer is an open-source tool that's maintained outside of the standard Looker Support scope, you should report any Gazer-specific persistent issues to the [Gazer GitHub Issues page](https://github.com/looker-open-source/gzr/issues/new).

You can also use Gazer to migrate dashboards between Looker instances. To use Gazer, [see the Gazer Readme on GitHub](https://github.com/looker-open-source/gzr).

### Troubleshooting unsupported layout errors for Gazer

If you encounter an error regarding unsupported dashboard layouts while using Gazer, you can resolve the error by taking the following actions:

  * **Update Gazer** : Earlier versions of Gazer may return an [`Unsupported Layout` error](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-unsupported-dashboard-layout) when you attempt to import [dashboards with tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards). Confirm that you're using the latest version of Gazer to include the fix for supporting the "New Layout" structure.

  * **Verify data models** : Confirm that all of the underlying LookML models are fully deployed on the target instance before importing a dashboard. Inconsistencies in model availability can cause dashboard import failures.

  * **Manually update the dashboard** : If an automated import fails, you can follow the steps outlined in the first section on this page, convert the dashboard from a [LookML dashboard to a UDD](https://docs.cloud.google.com/looker/docs/converting-lookml-to-user-defined-dashboard), and then manually update the tab settings and values as described on the [Troubleshooting unsupported layout errors for dashboards](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-unsupported-dashboard-layout) Best Practices page.




Learn more about [adding tabs to dashboards](https://docs.cloud.google.com/looker/docs/tabbed-dashboards).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
