---
url: https://docs.cloud.google.com/monitoring/alerts/notification-terraform/
title: Create and manage notification channels with Terraform \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:20.858293+00:00
---

# Create and manage notification channels with Terraform  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/notification-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create and manage notification channels with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Google Cloud Terraform Provider to create notification channels in your Google Cloud project. The Google Cloud Terraform Provider offers the following resources for alerting policies and notification channels:

  * [google_monitoring_alert_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy)
  * [google_monitoring_notification_channel](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_notification_channel)



[Terraform](https://www.terraform.io/) is a tool for building, changing, and versioning infrastructure. It uses configuration files to describe the components needed to run a single application or your entire infrastructure. For more information about using Terraform, see the following:

  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform#docs)
  * [Google Cloud Terraform Provider ](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Get Started - Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)



## Before you begin

To get the permissions that you need to create and modify notification channels by using Terraform, ask your administrator to grant you the [Notification Channel Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelEditor) (`roles/monitoring.notificationChannelEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## Create a notification channel

To create a notification channel in your Google Cloud project, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform).

  2. In the Cloud Shell, go to the directory that contains your Terraform configuration.

  3. Edit the configuration file and add your notification channel.

For example, the following configuration of the [google_monitoring_notification_channel](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_notification_channel) resource defines an email notification channel:
         
         resource "google_monitoring_notification_channel" "email" {
          display_name = "Tier 1 Support Email"
            type = "email"
            labels = {
              email_address = "USER_EMAIL"
            }
          }
         

  4. In the Cloud Shell, enter `terraform apply`.




## Edit or delete notification channels

To edit or delete a notification channel in your Google Cloud project, do the following:

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform).

  2. In the Cloud Shell, go to the directory that contains your Terraform configuration.

  3. Edit your configuration file, find the `google_monitoring_notification_channel` resource for your notification channel, and then modify or delete that resource.

  4. In the Cloud Shell, enter `terraform apply`.




## What's next

  * [Create alerting policies with Terraform](https://docs.cloud.google.com/monitoring/alerts/terraform).
  * Learn more about [Terraform](https://www.terraform.io/).
  * Try out code samples that use the Google Cloud Terraform Provider with Cloud Monitoring.
  * View the Google Cloud Terraform Provider [repository on GitHub](https://github.com/hashicorp/terraform-provider-google).
  * [File a GitHub issue](https://github.com/hashicorp/terraform-provider-google/issues) to report a bug or ask a question about Terraform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
