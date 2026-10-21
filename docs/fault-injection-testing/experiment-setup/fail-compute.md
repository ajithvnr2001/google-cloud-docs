---
url: https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/
title: Set up an experiment for Fail Compute \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:02:11.531105+00:00
---

# Set up an experiment for Fail Compute  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Set up an experiment for Fail Compute Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to set up a new experiment template for Fail Compute fault. This fault lets you fail compute resources for individual VMs or entire Managed Instance Groups (MIGs) of VMs.

Before proceeding, you must have the following:

  * The `roles/faulttesting.operator` role.



To create a new experiment template, do the following:

  1. Open the [Google Cloud console](https://console.cloud.google.com/).
  2. Navigate to the Fault Injection Testing **Overview** page.
  3. Select **Create experiment template**. 
     * Alternatively, from the Fault Injection Testing **Overview** page, click **Experiment templates** on the left navigation bar, and click **Create Template**.
  4. In the Fault Type section, select **Fail Compute** , then the `GCE` option.
  5. In the Target section: 
     1. Choose a target type. 
        * **Individual VMs**. Isolates specified [virtual machine instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances). Individually specified VMs cannot be part of a Managed Instance Group (MIG).
        * **All VMs with a given secure tag**. Targets VMs based on a specified [secure tag](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues) and region. 
          * You must apply the tag outside of the Fault Injection Testing interface before the experiment is created.
          * Tagged VMs cannot be part of a MIG, and any tagged VMs outside of the experiment's region will be excluded from the test.
          * Ensure that the [Cloud Asset API](https://docs.cloud.google.com/asset-inventory/docs/reference/rest) is enabled. Fault Injection Testing uses this API to discover tagged VMs.
          * The [firewall policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies) used to block traffic won't reference this tag directly. Targeted VMs will be bound to a new, experiment-specific tag for the duration of the experiment.
        * **All VMs in a zonal MIG**. Targets VMs within a specified [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups) MIG. Autoscaling and autohealing for the MIG will be disabled for the duration of the test.
        * **All VMs in a regional MIG**. Targets VMs within a specified [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroups) MIG. Autoscaling and autohealing for the MIG will be disabled for the duration of the test.
        * **All VMs in a zone.** Targets all non-MIG VMs and zonal MIGs in the specified zone. 
          * Regional MIGs won't be included, even if they have components in that zone.
          * Affected zonal MIGs will have autoscaling and autohealing disabled for the duration of the test.
          * Ensure that the Cloud Asset API is enabled because Fault Injection Testing uses the API to discover MIGs and VMs in the specified zone.
        * **All VMs in a region.** Targets all non-MIG VMs and all MIGs (both zonal and regional) within the selected region. 
          * Autoscaling and autohealing will be disabled for all affected MIGs for the duration of the test.
          * Ensure that the CAIS API is enabled because Fault Injection Testing uses the API to discover MIGs and VMs in the specified region.
  6. Set the **Duration** to how long the experiment should run.
  7. In the **Template name** section, provide a clear and descriptive name for the template. Optionally provide details in the description.
  8. In the **Verify** section: 
     1. See a recap of the settings you selected.
     2. Wait for the automated dry run to finish.
     3. After the dry run is complete, the list of resources that will receive the fault injection appears. If there are errors with the targeted resources, they will also appear here.
  9. **Create** the experiment template. A confirmation message indicating that the template has been created appears, and the new template shows up in the list of templates.



For details on how the Fail Compute fault behaves, see the [Fail Compute fault reference](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute).

## What's next

[Run an experiment](https://docs.cloud.google.com/fault-injection-testing/run-experiment) using the experiment template you created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
