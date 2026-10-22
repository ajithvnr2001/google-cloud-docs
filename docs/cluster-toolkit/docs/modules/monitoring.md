---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/monitoring/
title: Create a Cloud Monitoring dashboard \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:17.267419+00:00
---

# Create a Cloud Monitoring dashboard  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Cloud Monitoring dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Optimize your high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads on Google Cloud by creating a [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards) with the dashboard module in Cluster Toolkit.

You can use the module's default layout, add custom widgets, or build a dashboard from scratch to monitor and optimize your HPC environments.

For the complete list of inputs and outputs, see the [`dashboard` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/monitoring/dashboard) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `dashboard` module, see the [`examples/hpc-enterprise-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-enterprise-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `dashboard` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select software or resource** menu and then select **Cloud Monitoring dashboard**.
  * The `dashboard` module does not create a continuous long-running workload or a full cluster. It provisions a [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards) that monitors the performance and health of your cluster.



### Required roles

To get the permissions that you need to create Cloud Monitoring dashboards, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create the default HPC dashboard

By default, the module creates a dashboard that is tailored for HPC workloads. To create this dashboard, add the `dashboard` module to your blueprint.
    
    
    - id: hpc_dash
      source: modules/monitoring/dashboard
    
    

## Create a dashboard with custom widgets

You can add custom widgets to the dashboard by using the `widgets` setting. This setting accepts a list of JSON strings, where each string represents a [widget configuration](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget).

The following example adds a text widget with Markdown content to the default HPC dashboard.
    
    
    - id: hpc_dash
      source: modules/monitoring/dashboard
      settings:
        widgets:
        - |
          {
            "text": {
              "content": "## Cluster Overview\nThis dashboard tracks the core metrics for the production cluster.",
              "format": "MARKDOWN"
            },
            "title": "Welcome"
          }
    
    

## Create an empty dashboard

If you prefer to build a dashboard entirely from scratch (programmatically or manually after deployment), then you can set the `base_dashboard` setting to a value of `Empty`.
    
    
    - id: empty_dash
      source: modules/monitoring/dashboard
      settings:
        base_dashboard: Empty
        title: "My Custom Dashboard"
    
    

## What's next

  * Learn more about [managing dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) in Cloud Monitoring.
  * For a complete list of input fields and output values, see the [`dashboard` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/monitoring/dashboard) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
