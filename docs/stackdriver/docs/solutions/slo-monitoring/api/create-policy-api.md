---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/create-policy-api/
title: Creating an alerting policy \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:31.223800+00:00
---

# Creating an alerting policy  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/create-policy-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Creating an alerting policy Stay organized with collections  Save and categorize content based on your preferences. 

Alerting policies for the burn rate of your error budget are based on the time-series selector `select_slo_burn_rate`, described in [Retrieving SLO data](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors). There are other time-series selectors, and you can use some of them as the basis for alerting policies. For a discussion of SLO-based alerting policies, see [Alerting on your burn rate](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate).

You create alerting policies by using the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) method. The general use of this method is documented in [Managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).

Alerting policies for SLOs are similar to other metric-threshold alerting policies, but they differ in one specific way: the `filter` in the [`MetricThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold) specification of the condition uses a time-series selector instead of a pair of metric and monitored-resource types.

## Conditions for SLO-based alerting policies

An alerting policy must have at least one condition. For a SLO-based condition, use a [`MetricThreshold`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold)-type condition.

A metric-threshold condition can contain two pairs of time-series configurations: `filter` and `aggregations`. Because SLO data is retrieved differently than other time-series data, the only field used in a condition for an SLO is the `filter` field.

A condition for an SLO does set the `comparison`, `thresholdValue`, `duration`, and `trigger` fields.

This example creates a condition that is violated when the burn rate exceeds 2 times the normal rate. The structure looks like this: 
    
    
      "conditions": [
        {
          "displayName":"SLO burn rate alert for ${SLO_ID} exceeds 2",
          "conditionThreshold": {
            "filter": DATA_RETRIEVAL_FILTER_FOR_SLO,
            "comparison":"COMPARISON_GT",
            "thresholdValue": 2,
            "duration": {
              "seconds":"0",
            },
          },
        }
      ],
    

To set the `filter` field, you need the resource name of a specific SLO. This value is of the form `projects/${PROJECT}/services/${SERVICE_ID}/serviceLevelObjectives/${SLO_ID}`. For information on finding the SLO ID, see [Listing SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api#slos-list).

To create an alert on burn rate, use the time-series selector `select_slo_burn_rate`. This selector takes two values, the target SLO and the lookback period. For more information, see [`select_slo_burn_rate`](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors#tss-burn-rate).

For example, the following filter gets the burn rate of the target SLO with a 1-hour lookback period:

`"filter":"select_slo_burn_rate(\"projects/${PROJECT}/services/${SERVICE_ID}/serviceLevelObjectives/${SLO_ID}\", \"60m\")"`

## The rest of the alerting policy

To complete the alerting policy, specify values for the remaining fields:

  * `displayName`: A description of the alerting policy.
  * `combiner`: Describes the logic for combining conditions. This policy has only one condition, so either `AND` or `OR` works.
  * `notificationChannels`: An array of existing notification channels to use when the alerting policy is triggered. For information on finding and creating notification channels, see [Notification channels](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#nc).
  * `documentation`: Information that is sent when the condition is violated to help recipients diagnose the problem. For details, see [`Documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation).



## Creating the alerting policy

The following example uses the API to create a burn-rate alerting policy. For information about listing, modifying, and deleting alerting policies, see [Managing alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).

For example, to create the alerting policy by using `curl`, send a `POST` message to the `https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/alertPolicies` endpoint, and provide the alerting policy in the request body. The JSON in the request body describes an alerting policy that uses a threshold condition based on the `select_slo_burn_rate` time-series selector with a one-hour lookback period.

  1. Create a variable to hold the request body:
         
         CREATE_ALERT_POST_BODY=$(cat <<EOF
         {
           "displayName":"SLO burn-rate alert for ${SLO_ID} with a threshold of 2",
           "combiner":"AND",
           "conditions": [
             {
               "displayName":"SLO burn rate alert for ${SLO_ID} exceeds 2",
               "conditionThreshold": {
                 "filter":"select_slo_burn_rate(\"projects/${PROJECT}/services/${SERVICE_ID}/serviceLevelObjectives/${SLO_ID}\", \"60m\")",
                 "comparison":"COMPARISON_GT",
                 "thresholdValue": 2,
                 "duration": {
                   "seconds":"0",
                 },
               },
             }
           ],
           "notificationChannels": ["${NOTIFICATION_CHANNEL}", ],
           "documentation": {
              "content": "SLO burn for the past 60m exceeded twice the acceptable budget burn rate.",
              "mime_type": "text/markdown",
           },
         }
         EOF
         )
         

  2. Post the request to the endpoint:
         
         curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" --header "Content-Type: application/json" -X POST -d "${CREATE_ALERT_POST_BODY}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/alertPolicies
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
