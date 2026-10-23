---
url: https://docs.cloud.google.com/service-infrastructure/docs/manage-consumer-quota/
title: Managing Consumer Quota \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:14.512468+00:00
---

# Managing Consumer Quota  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/manage-consumer-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Managing Consumer Quota Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Service Consumer Management API to view and override the quota limits enforced on individual consumers of your service.

Be sure to familiarize yourself with the [service quota model](https://docs.cloud.google.com/docs/quota) to better understand the terminology used in this tutorial.

**Note:** Service Consumer Management only displays information about a project's quota _limits_ , not its quota _usage_. To get quota usage data, use the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/docs/apis) instead.

To program against the Service Infrastructure API, we recommend that you use one of our provided [client libraries](https://docs.cloud.google.com/service-usage/docs/libraries). To experiment with the API, you can follow the instructions in this guide and use the `curl` command to test the API without setting up a full application development environment.

## Display service quota

To display service quota metrics and limits, follow these steps:

  1. To use `gcurl`, run the following `alias` command with authentication token:
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         

  2. To see all quota limits on all metrics that apply to a particular consumer, use the following method:
         
         gcurl https://serviceconsumermanagement.googleapis.com/v1beta1/services/SERVICE_NAME/projects/PROJECT_ID/consumerQuotaMetrics
         

Replace the following:

     * `SERVICE_NAME`: the name of your service.
     * `PROJECT_ID`: the ID of the consumer project of interest.

This call responds with a list of metrics defined by the service, each with the list of limits on those metrics that apply to this consumer, the values for those limits, and any overrides. Here's an example response:
    
    {
      "metrics": [
        {
          "name": "services/myservice.appspot.com/projects/consumer-project-id/consumerQuotaMetrics/airport_requests",
          "metric": "airport_requests",
          "displayName": "Airport Requests",
          "consumerQuotaLimits": [
            {
              "name": "services/myservice.appspot.com/projects/consumer-project-id/consumerQuotaMetrics/airport_requests/limits/%2Fmin%2Fproject",
              "metric": "airport_requests",
              "unit": "1/min/{project}",
              "quotaBuckets": [
                {
                  "effectiveLimit": "5",
                  "defaultLimit": "5",
                }
              ]
            }
          ],
        }
      ]
    }
    

  3. Each metric in the response has a name field. To inspect quota settings for just that metric, rather than for all metrics, use its name in the URL:
         
         gcurl https://serviceconsumermanagement.googleapis.com/v1beta1/METRIC_NAME
         

Replace `METRIC_NAME` with the fully qualified name of the metric. For example:

`services/myservice.appspot.com/projects/consumer-project-id/consumerQuotaMetrics/airport_requests`

  4. Each limit within a metric has a name field. To inspect quota settings for just that limit on that metric, rather than for all limits on a metric or all metrics, use its name in the URL:
         
         gcurl https://serviceconsumermanagement.googleapis.com/v1beta1/LIMIT_NAME
         

Replace `LIMIT_NAME` with the fully qualified name of the limit. For example:

`services/myservice.appspot.com/projects/consumer-project-id/consumerQuotaMetrics/airport_requests/limits/%2Fmin%2Fproject`




## Apply a producer override

The owner or administrator of a service can apply a producer override to a specific limit for a specific consumer, granting a quota increase on that limit.

  1. To identify a limit, first use one of the preceding methods to find the quota limit of interest, and use its name field to apply a producer override to it:
         
         gcurl https://serviceconsumermanagement.googleapis.com/v1beta1/LIMIT_NAME/producerOverrides -d '{"override": {"override_value": "12345"} }'
         

This call can be used to apply a new override or update an existing override to a new value. To grant unlimited quota on a limit, use "-1" as the override value.

If the call succeeds, it returns an operation identifier, which represents ongoing work on the server, as the quota change propagates to backend systems:
         
         {
           "name": "operations/quf.92accba3-6530-4fc1-9a95-c1280d48a6b7"
         }
         

  2. To check the progress of the operation, use its name:
         
         gcurl https://serviceconsumermanagement.googleapis.com/v1/OPERATION_NAME
         

When this call responds with a message that includes "done":true, then the operation is finished. If the operation fails, the message includes error details.

You can also check whether a change has been applied by repeating the original get call on the specific limit. The limit must now have an additional `producerOverride` field.




### Force large quota changes

If an override would cause the enforced quota to decrease by more than 10%, the call is rejected, as a safety measure to avoid accidentally decreasing quota too quickly. To disregard this restriction, use the force flag:
    
    
    gcurl https://serviceconsumermanagement.googleapis.com/v1beta1/LIMIT_NAME/producerOverrides -d '{"override": {"override_value": "0"}, "force": true}'

### Apply regional or zonal quota overrides

Some quota limits are enforced on a per-region or per-zone basis; this is indicated by the presence of /{region} or /{zone} in the limit unit.

Applying an override to such a limit changes the base quota on every region or zone. To change the quota for only a specific region or zone, use the location field:
    
    
    gcurl https://serviceconsumermanagement.googleapis.com/v1beta1/LIMIT_NAME/producerOverrides -d '{"override": {"override_value": "135", "dimensions": {"region": "asia-south1"} } }'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
