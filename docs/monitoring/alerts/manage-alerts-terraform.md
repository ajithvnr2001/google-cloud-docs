---
url: https://docs.cloud.google.com/monitoring/alerts/manage-alerts-terraform/
title: Manage alerting policies with Terraform \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:27.642395+00:00
---

# Manage alerting policies with Terraform  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/manage-alerts-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage alerting policies with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud Terraform Provider lets you edit, delete, and export alerting policies in your Google Cloud project. You configure alerting policies and notification channels by using the [`google_monitoring_alert_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy) and [`google_monitoring_notification_channel`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_notification_channel) resources.

[Terraform](https://www.terraform.io/) uses configuration files to build, change, and version the components needed to run a single application or your entire infrastructure. For more information about using Terraform, see the [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform#docs), the [Google Cloud Terraform Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) reference, and [Get Started - Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started).

## Before you begin

To get the permissions that you need to modify alerting policies by using Terraform, ask your administrator to grant you the following IAM roles on your project: 

  * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)
  * Create and use log-based alerting policies: [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The Monitoring Editor role also lets you perform activities like creating dashboards and viewing alerts. If you only need to configure alerting policies with Terraform, then you can use the Monitoring AlertPolicy Editor (`roles/monitoring.alertPolicyEditor`) role instead.

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## Edit or delete alerting policies

To edit or delete an alerting policy in your Google Cloud project, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for you project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  2. In the Cloud Shell, go to the directory that contains your Terraform configuration.

  3. Edit the configuration file, locate the `google_monitoring_alert_policy` resource for your alerting policy, and then either modify or delete that resource.

  4. In the Cloud Shell, enter `terraform apply`.




## Export an alerting policy configuration to a Terraform configuration

You can export an alerting policy configuration from Google Cloud to a Terraform definition in your Terraform configuration. This process is helpful if you created an alerting policy in Google Cloud after you created your Terraform configuration.

To export your alerting policy, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for you project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  2. In the Cloud Shell, go to the directory that contains your Terraform configuration.

  3. Add an [`import`](https://developer.hashicorp.com/terraform/language/import) block to a file in your Terraform configuration. The import block has the following arguments:

     * `to`: The resource address as specified by your Terraform configuration. This field has the format of `google_monitoring_alert_policy.RESOURCE_NAME`, where RESOURCE_NAME is a value you choose. We recommend choosing a resource name that clearly describes your alerting policy.

     * `id`: The name of the alerting policy. This field has the format of `project/PROJECT_ID/alertPolicies/ALERT_POLICY_ID`.

For example, you want to export an alerting policy that monitors CPU usage, so you set RESOURCE_NAME to `cpu_usage_threshold`. You then set `id` as the alerting policy name:
    
    import {
    to = google_monitoring_alert_policy.cpu_usage_threshold
    id = "projects/my-alerting-project/alertPolicies/7160801095019277297"
    }
    

  4. In the Cloud Shell, run the following command:
         
         terraform plan -generate-config-out=generated.tf
         

The previous command creates a file named `generated.tf`, which lets you review your alerting policy definition before you add it to your Terraform configuration. You can edit the definition, move it to a different file, or leave it unchanged.

  5. In the Cloud Shell, enter `terraform apply` to import your alerting policy definition to your Terraform configuration.




For more information about generating definitions for resources that aren't part of your Terraform configuration, see [Generating configuration](https://developer.hashicorp.com/terraform/language/import/generating-configuration).

## What's next

  * Learn more about [Terraform](https://www.terraform.io/).
  * Try out code samples that use the Google Cloud Terraform Provider with Cloud Monitoring.
  * View the Google Cloud Terraform Provider [repository on GitHub](https://github.com/hashicorp/terraform-provider-google).
  * [File a GitHub issue](https://github.com/hashicorp/terraform-provider-google/issues) to report a bug or ask a question about Terraform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
