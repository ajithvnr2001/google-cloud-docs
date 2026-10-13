---
url: https://docs.cloud.google.com/deploy/docs/alerts/
title: Create Cloud Deploy alerts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:48.316005+00:00
---

# Create Cloud Deploy alerts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Create Cloud Deploy alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud Deploy and [Google Cloud Observability](https://cloud.google.com/products/operations) to set up alerting policies so you are notified for specific events and conditions in Cloud Deploy.

Alerts for Cloud Deploy are generated using [platform logs](https://docs.cloud.google.com/deploy/docs/platform-logs) stored by Cloud Logging. Google Cloud Observability supports alerts generated using time-series data from Cloud Monitoring, but Cloud Deploy alerts are [based on logs only](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

Cloud Deploy alert policies are per delivery pipeline.

**Note:** In addition to the alerts described in this article, you can [subscribe to Cloud Deploy service notifications](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications) using Pub/Sub topics.

## What are alerts?

Alerts are notifications from Google Cloud Observability under certains conditions. You specify those conditions in an alerting policy. The [Google Cloud Observability documentation](https://docs.cloud.google.com/monitoring/alerts) describes alerting and alerting policies in more detail. This document describes the specific Cloud Deploy activities for which you can set up alerting policies.

## Available alerts

You can set up alerting policies for the following circumstances, specific to Cloud Deploy:

  * The [render](https://docs.cloud.google.com/deploy/docs/terminology#render) operation, for a given release, has failed.

For every release, all manifests, service definitions, and any other configs that must be rendered, are rendered for all targets before anything is deployed. This alert notifies you if a release's render operation fails.

  * A rollout has failed.

This alert notifies you when a rollout within this delivery pipeline fails. You can then take action, as described in the article [Manage rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).

  * A rollout requires [approval](https://docs.cloud.google.com/deploy/docs/promote-release#manage_approvals_for_a_delivery_pipeline).

One of your targets is configured to require approval, and the release is now being promoted to that target, but approval is pending.

  * A rollout with a [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) requires [phase advancement](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#advance_rollout).

When using a canary deployment strategy, each canary increment is a phase in the rollout for that release and target. Advancing those stages can be done manually or automatically. If there's a rollout waiting for a stage to be advanced, this alert lets you know.




## What permissions do you need?

The person using the Google Cloud console to set up alerting policies must have the [permissions that Google Cloud Observability requires](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#before_you_begin).

## Configure Cloud Deploy alerts

To create an alert for a delivery pipeline:

  1. Open the **Delivery pipeline details** page for the pipeline for which you want to create an alert policy.

![delivery pipeline details in Google Cloud console, showing alerts button](https://docs.cloud.google.com/static/deploy/images/alerts-delivery-pipeline-details-page.png)

  2. Click the **Recommended alerts** button.

The **Alert policy templates** dialog is displayed, showing the alert-policy templates that are available for Cloud Deploy.

  3. Select each policy template you want to use for this delivery pipeline.

You can also click **Show options** to set options for the template, and to see current log messages related to that policy template.

  4. Under **Configure notifications** , select the notification channel or channels the notifications will be sent to.

If you don't already have notification channels configured, you can click **Manage notification channels**.




By default, a maximum of 1 alert per policy is sent every 5 minutes. You can configure this in the **Show options** sections of each alert policy template.

For more information about setting up alerting policies and notification channels, see the [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

### Other ways to set up alerts

Besides creating alert policies using the Google Cloud console, you can [use the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api) or [the Google Cloud Observability Terraform provider](https://docs.cloud.google.com/monitoring/alerts/terraform).

## What's next

  * [Learn more about Google Cloud Observability](https://docs.cloud.google.com/monitoring/alerts) alerts.

  * [Read about Cloud Deploy platform logs](https://docs.cloud.google.com/deploy/docs/platform-logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
