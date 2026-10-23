---
url: https://docs.cloud.google.com/service-health/docs/configure-alerts-terraform/
title: Configure alerts in Terraform \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:27.174965+00:00
---

# Configure alerts in Terraform  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/configure-alerts-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Configure alerts in Terraform Stay organized with collections  Save and categorize content based on your preferences. 

If you're using Terraform, you can set up alerts for service health events that appear in Personalized Service Health. This document explains how.

## Before you begin

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for the project that you want to create alerts for.
  2. Have a notification channel defined in your Terraform configuration. For more information, see the documentation for the [`google_monitoring_notification_channel`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_notification_channel) resource.



## Example configuration

The following example Terraform configuration enables Personalized Service Health and alerts for all new incidents and all updates.
    
    
    provider "google" {
      project = "PROJECT_ID"
    }
    
    resource "google_project_service" "project" {
      service = "servicehealth.googleapis.com"
    }
    
    resource "google_monitoring_alert_policy" "alert_policy_all" {
      display_name = "All incidents, all updates"
      combiner     = "OR"
      enabled      = "true"
      conditions {
        display_name = "test condition"
        condition_matched_log {
          filter     = "resource.type = \"servicehealth.googleapis.com/Event\" AND jsonPayload.category = \"INCIDENT\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\""
          label_extractors = {
              state = "EXTRACT(jsonPayload.state)"
              description = "EXTRACT(jsonPayload.description)"
              impactedProducts = "EXTRACT(jsonPayload.impactedProducts)"
              startTime = "EXTRACT(jsonPayload.startTime)"
              title = "EXTRACT(jsonPayload.title)"
              impactedLocations = "EXTRACT(jsonPayload.impactedLocations)"
          }
        }
      }
    
      documentation {
        content = "### $${log.extracted_label.title}\nCheck out [Personalized Service Health dashboard](https://console.cloud.google.com/servicehealth/incidentDetails/projects%2F${resource.labels.resource_container}%2Flocations%2F${resource.labels.location}%2Fevents%2F${resource.labels.event_id}?project=${resource.labels.resource_container}) for more details.<br><br>  Description: $${log.extracted_label.description}<br><br>  Impacted products: $${log.extracted_label.impactedProducts}<br><br> Impacted locations: $${log.extracted_label.impactedLocations}<br><br>  Incident start time: $${log.extracted_label.startTime}<br><br>  State: $${log.extracted_label.state}"
        mime_type = "text/markdown"
      }
      alert_strategy {
        notification_rate_limit {
          period = "300s"
        }
      }
    
      notification_channels =  ["projects/PROJECT_ID/notificationChannels/NOTIFICATION_CHANNEL"]
    
      user_labels = {  # Add any extra labels that might be helpful
        scope = "all"
      }
    }
    

The service `servicehealth.googleapis.com` refers to Personalized Service Health, and the filter pulls all events. See the [Service Health API reference](https://docs.cloud.google.com/service-health/docs/reference) for the fields you can set.

The previous configuration is equivalent to choosing the **All incidents, all updates** option in [setting up an alert within the Service Health dashboard](https://docs.cloud.google.com/service-health/docs/configure-alerts-dashboard).

See the following pages for more information on the fields you can set in the alert policy:

  * Documentation for the [`google_monitoring_alert_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy) resource.

  * [Example alert conditions](https://docs.cloud.google.com/service-health/docs/example-alerting-policies#example_alert_conditions) that you can add to the `filter` field of your Terraform configuration and define when the alert triggers.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
