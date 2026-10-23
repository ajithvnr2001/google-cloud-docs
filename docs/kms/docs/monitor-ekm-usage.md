---
url: https://docs.cloud.google.com/kms/docs/monitor-ekm-usage/
title: Monitor EKM usage \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:19.749047+00:00
---

# Monitor EKM usage  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/monitor-ekm-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Monitor EKM usage Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use Cloud Monitoring to monitor your external key manager (EKM) connection. The following metrics can help you understand your EKM usage:

  * `cloudkms.googleapis.com/ekm/external/request_latencies`
  * `cloudkms.googleapis.com/ekm/external/request_count`



This page shows you how to create a dashboard to track metrics related to your Cloud EKM keys and external key manager connection, such as request counts and latencies. For more information about these metrics, see [cloudkms metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudkms). For more information about the dashboard creation process described in the following sections, see [Managing dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

## Before you begin

The steps on this page assume the following:

  * You already have Cloud EKM set up in a project, including an [EKM connection](https://docs.cloud.google.com/kms/docs/create-ekm-connection) and one or more [external keys](https://docs.cloud.google.com/kms/docs/create-external-key).



### Required roles

To get the permissions that you need to create dashboards using the gcloud CLI, ask your administrator to grant you the following IAM roles on your project: 

  * [Monitoring Dashboard Configuration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.dashboardEditor) (`roles/monitoring.dashboardEditor`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create dashboards using the gcloud CLI. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create dashboards using the gcloud CLI:

  * `monitoring.dashboards.create`
  * `monitoring.dashboards.delete`
  * `monitoring.dashboards.update`
  * `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a dashboard to monitor your EKM

To monitor the status of your EKM, create a dashboard that monitors your request count and latencies:

  1. Download the dashboard configuration: [`ekm-dashboard.json`](https://docs.cloud.google.com/static/kms/static/ekm-dashboard.json).

  2. Create a custom dashboard with the configuration file by running the following command:
         
         gcloud monitoring dashboards create \
         --config-from-file=ekm-dashboard.json




## View your EKM dashboard

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Resources > Dashboards** and view the dashboard named **Cloud KMS EKM**.




## Create an alert policy for EKM metrics

Complete the following steps using the gcloud CLI:

  1. Select a notification channel to receive EKM metrics alerts.

     * To use an existing notification channel, first view your channels:
           
           gcloud beta monitoring channels list
           

Choose a channel from the list. Make note of the notification channel ID; you need it later.

     * To use a new notification channel, create the channel using an email address:
           
           gcloud beta monitoring channels create \
           --display-name="Notification channel for EKM latency alert" \
           --description="This notification channel receives EKM latency metric alerts" \
           --type=email \
           --channel-labels=email_address=NOTIFICATION_EMAIL
           

If successful, this command returns the name of the new channel. Make note of the notification channel ID; you need it later. The output is similar to the following:
           
           Created notification channel [projects/PROJECT_ID/notificationChannels/NOTIFICATION_CHANNEL_ID]
           

  2. Create an alerting policy using the [`monitoring policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/create) command:
         
         gcloud monitoring policies create \
                 --notification-channels=NOTIFICATION_CHANNEL_ID \
                 --aggregation=' {"alignmentPeriod": "60s","perSeriesAligner": "ALIGN_PERCENTILE_99"}' \
                 --condition-display-name="EKM Request Latency > 150ms" \
                 --condition-filter='resource.type="cloudkms.googleapis.com/Project"
                                     metric.type="cloudkms.googleapis.com/ekm/external/request_latencies"
                                     metric.labels.ekm_service_region="LOCATION"
                                     metric.labels.method="LABEL_METHOD"' \
                 --duration="0s" \
                 --if="> 150" \
                 --display-name="EKM metric latency alert" \
                 --trigger-count=1 \
                 --combiner='AND'
         

Replace the following:

     * NOTIFICATION_CHANNEL_ID: the ID of the notification channel.
     * LOCATION: the region for which you want to alert on this metric. If you want to alert regardless of region, omit `metric.labels.ekm_service_region`.
     * LABEL_METHOD: the `method` label that you want to alert on—for example, `wrap`, `unwrap`, `asymmetricSign`, `checkCryptoSpacePermissions`, `createKey`, `getInfo`, or `getPublicKey`. You can use **Metrics Explorer** to explore metric labels.



## What's next

  * [Explore your data across various metric dimensions using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * Optional: Create [alerting policies](https://docs.cloud.google.com/monitoring/alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
