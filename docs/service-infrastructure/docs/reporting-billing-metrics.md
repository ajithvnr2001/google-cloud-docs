---
url: https://docs.cloud.google.com/service-infrastructure/docs/reporting-billing-metrics/
title: Reporting Billing Metrics \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:07.664322+00:00
---

# Reporting Billing Metrics  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/reporting-billing-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Reporting Billing Metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Service Infrastructure to enable [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) to send billing usage data so that Cloud Billing can charge against [service consumers](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer). For example, you can define a metric called `library.appspot.com/books/borrowed` to measure the number of books borrowed by a customer and define a stock keeping unit (SKU) and price for it.

The Service Control API accepts metrics, which it batches, aggregates, and forwards to [Cloud Billing](https://docs.cloud.google.com/billing). Cloud Billing ingests these metrics and generates bills based on the predefined price model. If there is no predefined price model, [Cloud Billing](https://docs.cloud.google.com/billing) simply disregards the billing metrics. To define the price model, please contact your Google Cloud partner account manager.

## Configuring billing

Before you send billing data to the Service Control API, you need to specify three different bits of information in your [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service):

  * **Monitored resources** : You can collect billing usage for each resource. The monitored resources need at least one label key `cloud.googleapis.com/location` to indicate the location of the billing usage.

  * **Metrics** : You can report one or more metrics. Each metric measures the usage of a given type of resource. Only DELTA metrics with INT64 values are supported for billing.

  * **Billing configuration** : Lets you specify the metrics to be sent to Cloud Billing.




The following example service configuration defines one metric that measures the number of books borrowed by a customer. A client can invoke the `services.report` method to report values on the metric. See [billing.proto](https://github.com/googleapis/googleapis/blob/master/google/api/billing.proto) for details on billing configuration.
    
    
    # library
    monitored_resources:
     - type: library.appspot.com/branch
       labels:
       - key: cloud.googleapis.com/location
         description: The cloud location.
       - key: library.appspot.com/city
         description: The city where the library branch is located in.
    
    # The metrics to be used.
    metrics:
    - name: library.appspot.com/books/borrowed
      metric_kind: DELTA
      value_type: INT64
      unit: '1'
    
    # The billing configuration.
    billing:
      consumer_destinations:
      - monitored_resource: library.appspot.com/branch
        metrics:
        - library.appspot.com/books/borrowed
    

## Reporting billing metrics

Once you have configured monitoring in the [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service) and pushed the service configuration using the Service Management API, you can call the Service Control API to report metrics. The following example uses the `gcurl` command to demonstrate the call. For information on how to set this up, see [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).
    
    
    $ gcurl -d "{
      'operations': [ {
        'operationId': '8356d3c5-f9b5-4274-b4f9-079a3731e6e5',
        'consumerId': 'project:library-consumer',
        'startTime': '`date +%FT%T%:z`',
        'endTime': '`date +%FT%T%:z`',
        'labels': {
          'cloud.googleapis.com/location': 'us-west1',
          'library.appspot.com/city': 'Kirkland',
        },
        'metricValueSets': [ {
          'metricName': 'library.appspot.com/books/borrowed',
          'metricValues': [ { 'int64Value': '10' } ]
        } ]
      } ]
    }" https://servicecontrol.googleapis.com/v1/services/library.appspot.com:report
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
