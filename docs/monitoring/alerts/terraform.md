---
url: https://docs.cloud.google.com/monitoring/alerts/terraform/
title: Create alerting policies with Terraform \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:43.579975+00:00
---

# Create alerting policies with Terraform  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create alerting policies with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Google Cloud Terraform Provider to create alerting policies in your Google Cloud project. The Google Cloud Terraform Provider provides the following resources for alerting policies and notification channels:

  * [google_monitoring_alert_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy)
  * [google_monitoring_notification_channel](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_notification_channel)



[Terraform](https://www.terraform.io/) is a tool for building, changing, and versioning infrastructure. It uses configuration files to describe the components needed to run a single application or your entire infrastructure. For more information about using Terraform, see the following documents:

  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform#docs)
  * [Google Cloud Terraform Provider ](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Get Started - Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)



## Before you begin

To get the permissions that you need to create alerting policies by using Terraform, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## Create an alerting policy

To create an alerting policy in your Google Cloud project, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform).

  2. In the Cloud Shell, go to the directory that contains your Terraform configuration.

  3. Edit the configuration file and add your alerting policy.

For example, the following configuration defines an alerting policy that sends a notification when the CPU utilization of a VM instance is greater than 50% for over one minute, with [repeated notifications](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#send-repeated-notifications) sent every 30 minutes.
         
         resource "google_monitoring_alert_policy" "alert_policy" {
           display_name = "CPU Utilization > 50%"
           documentation {
             content = "The $${metric.display_name} of the $${resource.type} $${resource.label.instance_id} in $${resource.project} has exceeded 50% for over 1 minute."
           }
           combiner     = "OR"
           conditions {
             display_name = "Condition 1"
             condition_threshold {
                 comparison = "COMPARISON_GT"
                 duration = "60s"
                 filter = "resource.type = \"gce_instance\" AND metric.type = \"compute.googleapis.com/instance/cpu/utilization\""
                 threshold_value = "50"
                 trigger {
                   count = "1"
                 }
             }
           }
         
           alert_strategy {
             notification_channel_strategy {
                 renotify_interval = "1800s"
                 notification_channel_names = [google_monitoring_notification_channel.email.name]
             }
           }
         
           notification_channels = [google_monitoring_notification_channel.email.name]
         
           user_labels = {
             severity = "warning"
           }
         }
         

In the preceding sample, the `notification_channels` field defines the notification channel for the alerting policy. The `notification_channel_names` field configures that notification channel to send repeated notifications. Both fields reference a notification channel with a `display_name` of `email`, which is defined elsewhere in the Terraform configuration. For more information, see [Create and manage notification channels with Terraform](https://docs.cloud.google.com/monitoring/alerts/notification-terraform).

You can use labels to associate an alerting policy with an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application. For more information, see [How to associate an alerting policy with an App Hub application](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#app-labels).

  4. In the Cloud Shell, enter `terraform apply`.




To modify your alerting policy, make your edits and then re-apply the Terraform configuration. For more information, see [Manage alerting policies with Terraform](https://docs.cloud.google.com/monitoring/alerts/manage-alerts-terraform).

## What's next

  * Learn more about [Terraform](https://www.terraform.io/).
  * Try out code samples that use the Google Cloud Terraform Provider with Cloud Monitoring.
  * View the Google Cloud Terraform Provider [repository on GitHub](https://github.com/hashicorp/terraform-provider-google).
  * [File a GitHub issue](https://github.com/hashicorp/terraform-provider-google/issues) to report a bug or ask a question about Terraform.


  * Use tags to [control access to alerting policies](https://docs.cloud.google.com/monitoring/access-control#monitoring-tags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
