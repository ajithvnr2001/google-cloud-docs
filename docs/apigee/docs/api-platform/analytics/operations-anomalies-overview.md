---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/operations-anomalies-overview/
title: Operations anomalies overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:59.283892+00:00
---

# Operations anomalies overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/operations-anomalies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Operations anomalies overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Operations anomalies identifies unusual or unexpected data patterns with your APIs. Operations anomalies continually monitors and performs statistical analysis to find anomalies.

Operations anomalies automatically detects these anomaly types:

  * Increase in all HTTP 4xx or 5xx errors at the organization, environment, and region level
  * Increase in the total response latency for the 90th percentile (p90) at the organization, environment, and region level



For example, in this graph of API error rate, the rate suddenly spikes at around 7 AM. Compared to the data leading up to that time, this increase is unusual enough to be classified as an anomaly.

![Graph of an error-rate anomaly.](https://docs.cloud.google.com/static/apigee/docs/images/error-rate-anomaly.png)

Operations anomalies can also discern variations that are less likely to indicate anomalies. For example, you can see some minor variations in error rate leading up to the anomaly, but these are not significant enough to be categorized as an anomaly.

![Anomaly versus random data variation.](https://docs.cloud.google.com/static/apigee/docs/images/anomaly-versus-random.png)

Operations anomalies enables you to:

  * [ View and investigate anomalies](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/investigate-anomalies): Operations anomalies reports unusual API events (anomalies). You can drill down to find out where and when the incident occurred, and what triggered it, so you can quickly remedy the situation.
  * [Create anomaly alerts](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-operations-anomalies-alerts) and set up notifications to have Apigee send you a message when an incident occurs.



## Prerequisites for using operations anomalies

To use operations anomalies: 

  * The AAPI Ops add-on must be enabled for your organization. See Enable AAPI Ops in an organization.
  * Users of operations anomalies must have the following roles: 
    * `roles/apigee.readOnlyAdmin`
    * `roles/logging.viewer`
    * `roles/monitoring.viewer`
  * Users who [investigate anomalies in the dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/investigate-anomalies) also need the `roles/logging.viewer` role.



## Enable AAPI Ops in an organization

To use AAPI Ops, you must enable it in your organization. Before doing so, first [obtain an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). You can then enable AAPI Ops using an API call that passes the access token.

### View the current add-ons configuration

Before enabling AAPI Ops, check to see whether is already enabled by making the following API call:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/YOUR_ORG" \
      -X GET \
      -H "Content-type: application/json" \
      -H "Authorization: Bearer $TOKEN"

where YOUR_ORG is the name of your organization and `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). This returns basic information about your organization, which includes a section for Apigee add-ons that begins with the line:
    
    
    "addonsConfig": {

Check to see whether this section contains an entry that begins with `"advancedApiOpsConfig"`, like the following example:
    
    
    "advancedApiOpsConfig": {
              "enabled": "true"
          }

If this entry is present, AAPI Ops is already enabled in the organization. If not, you need to enable it as described next.

### Enable AAPI Ops

To enable AAPI Ops in the organization with the default configuration, issue a `POST` request like the one shown below.

**Caution:** This API call overwrites the current add-ons configuration. You must include the current configurations for all add-ons in the above request to prevent them from being overwritten.**Note:** The API call below starts a long running operation that may take a while to complete.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG:setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "addonsConfig": {
          "advancedApiOpsConfig": {
              "enabled": "true"
          }
          <Current add-ons configuration>
        }
      }'

where `<Current add-ons configuration>` is the current add-ons configuration. You can find the current add-ons configuration in the response to the call to view the current add-ons configuration. For example, if the current add-ons configuration is
    
    
    "addonsConfig": {
        "integrationConfig": {
            "enabled":"true"
         },
        "monetizationConfig": {
            "enabled":"true"
         }
      },

the command to enable AAPI Ops would be 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/YOUR_ORG:setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "addonsConfig": {
          "advancedApiOpsConfig": {
              "enabled": "true"
          },
        "integrationConfig": {
              "enabled": "true"
          },
        "monetizationConfig": {
              "enabled": "true"
          }
        }
      }'

After you send the request, you will see a response like the following:
    
    
    {
      "name": "organizations/apigee-docs-d/operations/0718a945-76e0-4393-a456-f9929603b32c",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/apigee-docs-d",
        "state": "IN_PROGRESS"
      }
    }

##  Disable AAPI Ops in your organization 

If for some reason you need to disable AAPI Ops in your organization, you can do so by issuing a `POST` request, passing the add-ons configuration in your request body, as shown below.

**Caution:** The add-ons configuration that you pass in the request body will **overwrite** the current add-ons configuration. [View the current add-ons configuration](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) in the Apigee organization profile and be sure to include it in the request payload. **Note:** The API call below starts a long running operation that may take a while to complete.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** :setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        **"addonsConfig": {
          "advancedApiOpsConfig": {
              "enabled": "false"
          } <_Include current add-ons configuration_ >**
        }
      }'

The following provides an example of the response showing that the operation is in progress: 
    
    
    {
      "name": "organizations/**$ORG** /operations/06274ffb-8940-41da-836d-781cba190437",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/**$ORG** ",
        "state": "IN_PROGRESS"
      }
    }

For more information, see the [Configure organization add-ons API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons). 

## How anomaly detection works

Anomaly detection involves the following stages:

  * Train models
  * Log anomaly events



### Train models

Operations anomalies works by training a model of the behavior of your API proxies from historical time-series data. There is no action required on your part to train the model. Apigee automatically creates and trains models for you from the previous six hours of API data. Therefore, Apigee requires a minimum of six hours of data on an API proxy to train the model before it can log an anomaly.

The goal of training is to improve the accuracy of the model, which can then be tested on historical data. The simplest way to test a model's accuracy is to calculate its _error rate_ —the sum of false positives and false negatives, divided by the total number of predicted events. 

### Log anomaly events

At runtime, operations anomalies compares the current behavior of your API proxies with the behavior predicted by the model. Operations anomalies can then determine, with a specific confidence level, when an operational metric is exceeding the predicted value. For example, when the rate of 5xx errors exceeds the rate predicted by the model.

When Apigee detects an anomaly, it automatically logs the event in the [operations anomalies dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/investigate-anomalies). The list of events displayed in the dashboard includes all detected anomalies, as well as triggered alerts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
