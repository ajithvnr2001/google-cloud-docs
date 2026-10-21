---
url: https://docs.cloud.google.com/service-infrastructure/docs/reporting-metrics/
title: Reporting Monitoring Metrics \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:31.633457+00:00
---

# Reporting Monitoring Metrics  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/reporting-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Reporting Monitoring Metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Service Infrastructure to enable [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) to generate monitoring data to send to [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) and [service consumer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer) projects. Monitoring provides visibility into the performance, uptime, and overall health of individual managed services.

The Service Control API accepts metrics, which it batches and forwards to [Cloud Monitoring](https://docs.cloud.google.com/monitoring). Monitoring ingests these metrics and generates insights via dashboards, charts, and alerts.

Whereas Monitoring alone allows a managed service to generate monitoring data for use by you as a developer of the managed service, the Service Control API also lets you generate monitoring data which is intended for your users. This makes it possible for your users to understand and diagnose use of your managed service.

Note, this guide is for monitoring metrics defined by [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed). Monitoring Custom Metrics cannot be reported via Service Control API. To report Custom Metrics, you need to follow the Monitoring [guide](https://docs.cloud.google.com/monitoring/custom-metrics).

## Configuring monitoring

Before you send monitoring data to the Service Control API, you need to specify three different bits of information in your [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service):

  * **Monitored resources** : A [monitored resource](https://docs.cloud.google.com/monitoring/api/v3/metrics#intro-resources) represents a cloud entity that produces some monitoring data. To define a monitored resource in the service configuration, see [monitored_resource.proto](https://github.com/googleapis/googleapis/blob/master/google/api/monitored_resource.proto) for the technical specification. We strongly recommend you to use the same monitored resource for both monitoring and [logging](https://docs.cloud.google.com/service-infrastructure/docs/report-logs).

  * **Metrics** : You can report one or more metrics. Each metric represents a single piece of state whose value is tracked over time. See [metric.proto](https://github.com/googleapis/googleapis/blob/master/google/api/metric.proto) for the technical specification to define a metric.

  * **Monitoring configuration** : Lets you specify the metrics associated with individual monitored resources and the service producer or service consumer project where each metric should be sent. See [monitoring.proto](https://github.com/googleapis/googleapis/blob/master/google/api/monitoring.proto) for details.




The following example of service configuration defines a monitored resource and a metric.
    
    
    # The definition of the monitored resource to be used.
    monitored_resources:
    - type: library.appspot.com/Branch
      description: A library branch.
      display_name: Library Branch
      launch_stage: ALPHA
      labels:
      - key: resource_container
        description: The Google Cloud resource container (ie. project id) for
        the branch.
      - key: location
        description: The Google Cloud region the branch is located.
      - key: branch_id
        description: The ID of the branch.
    
    # The definition of the metrics to be used.
    metrics:
    - name: library.appspot.com/book/num_overdue
      display_name: Books Overdue
      description: The current number of overdue books.
      launch_stage: ALPHA
      metric_kind: GAUGE
      value_type: INT64
      unit: 1
    - name: library.googleapis.com/book/returned_count
      display_name: Books Returned
      description: The count of books that have been returned.
      launch_stage: ALPHA
      metric_kind: DELTA
      value_type: INT64
      unit: 1
    
    # The monitoring configuration.
    monitoring:
      producer_destinations:
      - monitored_resource: library.appspot.com/Branch
        metrics:
        - library.googleapis.com/book/returned_count
      consumer_destinations:
      - monitored_resource: library.appspot.com/Branch
        metrics:
        - library.appspot.com/book/num_overdue
    

After you have authored such configuration, you will need to follow [Managing Service Configurations](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) and [Managing Service Rollouts](https://docs.cloud.google.com/service-infrastructure/docs/rollout) to push the service configuration to Service Management API, which will configure the monitored resource and metric definitions in [Cloud Monitoring](https://docs.cloud.google.com/monitoring).

## Reporting metrics

After the service configuration push finishes, you can call the Service Control API to report metrics. The following example uses the `gcurl` command to demonstrate the call. For information on how to set this up, see [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).
    
    
    gcurl -d "{
      'operations': [ {
        'operationId': '8356d3c5-f9b5-4274-b4f9-079a3731e6e5',
        'operationName': 'Return books',
        'consumerId': 'projects/library-consumer',
        'startTime': '`date +%FT%T%:z`',
        'endTime': '`date +%FT%T%:z --date="5 seconds"`',
        'labels': {
          'location': 'us-east1',
          'branch_id': 'my-test-library-branch'
        },
        'metricValueSets': [ {
          'metricName': 'library.googleapis.com/book/returned_count',
          'metricValues': [ { 'int64Value': '23' } ]
        } ]
      } ]
    }" https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:report
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
