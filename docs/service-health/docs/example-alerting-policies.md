---
url: https://docs.cloud.google.com/service-health/docs/example-alerting-policies/
title: Example alerting policies \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:16.218723+00:00
---

# Example alerting policies  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/example-alerting-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Example alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

This document shows examples of alerting policies that customize the content of alert notifications.

## Before you begin

Be familiar with [setting up alerts for Personalized Service Health](https://docs.cloud.google.com/service-health/docs/configure-alerts-cloud-logging).

See the [Service Health log schema reference](https://docs.cloud.google.com/service-health/docs/reference/event-logs/rpc/google.cloud.servicehealth.logging.v1) for the fields you can set in the alert notifications and conditions.

## Example alert conditions

The following sections show examples of fine-grained alert conditions that you can use for Cloud Logging or Terraform.

**Note:** Set the version of the Service Health logs in your alert condition. The current version is `type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog. `

### Alert on a new incident for a specific Google Cloud product

Set `ALERT_CONDITION` to the following:
    
    
    labels."servicehealth.googleapis.com/new_event"=true AND jsonPayload.detailedCategory = \"CONFIRMED_INCIDENT\" AND jsonPayload.impactedProductIds =~ \"hV87iK5DcEXKgWU2kDri\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\"
    

The product name is in the common Google Cloud format. See [Google Cloud Service Health](https://status.cloud.google.com) for an example of the format.

### Alert on a new incident for a specific region

Set `ALERT_CONDITION` to the following:
    
    
    labels."servicehealth.googleapis.com/new_event"=true AND jsonPayload.detailedCategory = \"CONFIRMED_INCIDENT\" AND jsonPayload.impactedLocations =~ \"us-central1\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\"
    

The location name is in the common Google Cloud format. See [Google Cloud Service Health](https://status.cloud.google.com) for an example of the format.

### Alert on a new emerging incident for a specific product

Set `ALERT_CONDITION` to the following:
    
    
    labels."servicehealth.googleapis.com/new_event"=true AND jsonPayload.detailedCategory = \"EMERGING_INCIDENT\" AND jsonPayload.impactedProductIds =~ \"ix7u9beT8ivBdjApTif3\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\"
    

### Alert on any update or change to an incident

Set `ALERT_CONDITION` to the following:
    
    
    jsonPayload.detailedCategory = \"CONFIRMED_INCIDENT\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\"
    

### Alert on any update on confirmed incidents

Set `ALERT_CONDITION` to the following:
    
    
    jsonPayload.state =~ \"ACTIVE\" AND jsonPayload.detailedCategory = \"CONFIRMED_INCIDENT\" AND jsonPayload.detailedState != \"EMERGING\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\"
    

### Alert on state or relevance updates

Set `ALERT_CONDITION` to the following:
    
    
    jsonPayload.detailedCategory = \"CONFIRMED_INCIDENT\" AND "labels.servicehealth.googleapis.com/updated_fields" =~ \"'state'\" OR labels."servicehealth.googleapis.com/updated_fields" =~ \"'relevance'\" AND jsonPayload.@type = \"type.googleapis.com/google.cloud.servicehealth.logging.v1.EventLog\"
    

## Alert notification with full incident details

The following alert notification provides full incident details.
    
    
    {
      "displayName": "ALERT_NAME",
      "combiner": "OR",
      "conditions": [ {
        "displayName": "Log match condition",
        "conditionMatchedLog": {
          "filter": "ALERT_CONDITION",
          "labelExtractors": {
            "description": "EXTRACT(jsonPayload.description)",
            "impactedLocations": "EXTRACT(jsonPayload.impactedLocations)",
            "impactedProducts": "EXTRACT(jsonPayload.impactedProducts)",
            "startTime": "EXTRACT(jsonPayload.startTime)",
            "state": "EXTRACT(jsonPayload.state)",
            "detailedState": "EXTRACT(jsonPayload.detailedState)"
          } } } ],
      "documentation": {
      "content": "# View details at [Service Health dashboard](https://console.cloud.google.com/servicehealth/incidentDetails/projects%2F${resource.labels.resource_container}%2Flocations%2F${resource.labels.location}%2Fevents%2F${resource.labels.event_id}?project=${resource.labels.resource_container}) \n## Description \n${log.extracted_label.description} \n## Impacted locations \n${log.extracted_label.impactedLocations} \n## Impacted products \n${log.extracted_label.impactedProducts} \n## Incident start time \n${log.extracted_label.startTime} \n## Event state \n${log.extracted_label.state} \n## Event detailed state \n ${log.extracted_label.detailedState}",
        "mimeType": "text/markdown"
      },
      "notificationChannels": [ "NOTIFICATION_CHANNEL" ],
      "enabled": true,
      "alertStrategy": { "notificationRateLimit": { "period": "300s" }, "autoClose": "1800s" }
    }
    

The `labelExtractors` and `content` fields in the example include all information available for the incident.

## Alert notification with a link to the Service Health dashboard

The following example provides a link to the Service Health dashboard.
    
    
    {
      "displayName": "ALERT_NAME",
      "combiner": "OR",
      "conditions": [ {
        "displayName": "Log match condition",
        "conditionMatchedLog": {
          "filter": "ALERT_CONDITION",
          "labelExtractors": {
            "description": "EXTRACT(jsonPayload.description)",
            "impactedLocations": "EXTRACT(jsonPayload.impactedLocations)",
            "impactedProducts": "EXTRACT(jsonPayload.impactedProducts)",
            "startTime": "EXTRACT(jsonPayload.startTime)",
            "state": "EXTRACT(jsonPayload.state)",
            "detailedState": "EXTRACT(jsonPayload.detailedState)"
          } } } ],
      "documentation": {
      "content": "# View details at [Service Health dashboard](https://console.cloud.google.com/servicehealth/eventDetails/projects%2F${resource.labels.resource_container}%2Flocations%2F${resource.labels.location}%2Fevents%2F${resource.labels.event_id})",
        "mimeType": "text/markdown"
      },
      "notificationChannels": [ "NOTIFICATION_CHANNEL" ],
      "enabled": true,
      "alertStrategy": { "notificationRateLimit": { "period": "300s" }, "autoClose": "1800s" }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
