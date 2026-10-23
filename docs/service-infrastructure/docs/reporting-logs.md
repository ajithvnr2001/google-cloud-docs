---
url: https://docs.cloud.google.com/service-infrastructure/docs/reporting-logs/
title: Reporting Logs \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:22.678682+00:00
---

# Reporting Logs  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/reporting-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Reporting Logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Service Infrastructure to enable [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) to send logs to both [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) and [service consumer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer) projects.

The Service Control API accepts structured or unstructured log data, which it batches and forwards to [Cloud Logging](https://docs.cloud.google.com/logging). Both you and users of your managed services can use Google Cloud console and Google API Console to view the log data, or use the Cloud Logging API to access the data programmatically.

Whereas Logging alone allows a managed service to generate logs for use by you as the developer of the managed service, the Service Control API also lets you generate logs that are intended for your users. This makes it possible for your users to understand and diagnose their use of your managed service.

## Configuring logs

Before you send logs to the Service Control API, you need to specify three different bits of information in your [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service):

  * **Log names** : You can have one or more distinct logs. Each log is identified by a unique name. Individual logs make it possible for you to isolate distinct types of data if it makes the data easier to visualize or use.

  * **Monitored resources** : A [monitored resource](https://docs.cloud.google.com/logging/docs/api/v2#monitored-resources) represents a cloud entity that produces some logging data. To define a monitored resource in the service configuration, see [monitored_resource.proto](https://github.com/googleapis/googleapis/blob/master/google/api/monitored_resource.proto) for the technical specification. We strongly recommend you to use the same monitored resource for both [monitoring](https://docs.cloud.google.com/service-infrastructure/docs/reporting-metrics) and logging.

  * **Log configuration** : Lets you specify the monitored resource associated with any log stream and the service producer or service consumer project where each log should be sent. To configure the log association, see [logging.proto](https://github.com/googleapis/googleapis/blob/master/google/api/logging.proto) for the technical specification.




In the following example of [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config), the log `activity_log` is configured to be sent to the service consumer.
    
    
    # The definition of the monitored resource to be used.
    monitored_resources:
    - type: library.appspot.com/Branch
      description: A library branch
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
    
    # The log name to be used.
    logs:
    - name: activity_log
    
    # The logging configuration.
    logging:
      consumer_destinations:
      - monitored_resource: library.appspot.com/Branch
        logs:
        - activity_log
    

After you have authored such configuration, you will need to follow [Managing Service Configurations](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) and [Managing Service Rollouts](https://docs.cloud.google.com/service-infrastructure/docs/rollout) to push the service configuration to the Service Management API, which will configure the monitored resource in [Cloud Logging](https://docs.cloud.google.com/logging).

## Reporting logs

After the service configuration push finishes, you can call the Service Control API to report log entries. The following example uses the `gcurl` command to demonstrate the call. To learn how to set this up, see [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).
    
    
    gcurl -d "{
      'operations': [ {
        'operationId': 'e8bf36ef-f9b5-4274-b4f9-079a3731e6e5',
        'operationName': 'New book arrived',
        'consumerId': 'projects/library-consumer',
        'startTime': '`date +%FT%T%:z`',
        'endTime': '`date +%FT%T%:z`',
        'labels': {
          'location': 'us-east1',
          'branch_id': 'my-test-library-branch'
        },
        'logEntries': [ {
          'severity': 'INFO',
          'textPayload': 'new book arrived',
          'name': 'activity_log'
        } ]
      } ]
    }" https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:report
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
