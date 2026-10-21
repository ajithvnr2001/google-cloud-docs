---
url: https://docs.cloud.google.com/service-infrastructure/docs/checking-status/
title: Checking Status \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:08.433468+00:00
---

# Checking Status  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/checking-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Checking Status Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Service Infrastructure for checking status on [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed), [service producers](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer), [service consumers](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer), and API keys.

When a service producer offers a service to its service consumers, it needs to ensure that various preconditions are met, such as whether:

  * A service consumer has been deleted.
  * The service consumer has [enabled](https://docs.cloud.google.com/service-infrastructure/docs/glossary#enabled) the service.
  * An API key is valid.



The Service Control API provides a simple [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) method to check such preconditions. A managed service should call this method on a regular basis to ensure the preconditions are met. The activity between the service producer and the service consumer is represented by an [`Operation`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation). The `services.check` method performs the following checks on the operation:

  * The service producer project is live and in a healthy state.
  * The service consumer project is live and in a healthy state.
  * The managed service is enabled on the service consumer project.
  * The API key is valid.
  * The use of the API key satisfies restrictions associated with the API key, such as IP or HTTP referrer restrictions.



The `services.check` method is typically called from the servers that actually implement the service. For security and privacy purposes, the Service Control API uses [Identity and Access Management](https://docs.cloud.google.com/iam) to verify the caller has the proper permission to call the method. For details, see [Service Control API Access Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/access-control).

## Checking status

After you [roll out](https://docs.cloud.google.com/service-infrastructure/docs/glossary#rollout) a managed service, you can call the `services.check` method on the service without additional configuration. See the [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) reference for details.

To quickly experiment with the method, you can use the `gcurl` command to call the `services.check` method. See [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started) for the initial setup steps.
    
    
    gcurl -d '{
      "operation": {
        "operationId": "123e4567-e89b-12d3-a456-426655440000",
        "consumerId": "project:endpointsapis-consumer",
        "startTime":"2016-07-31T05:20:00Z",
        "operationName":"google.example.hello.v1.HelloService.GetHello"
      }
    }' https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:check
    {
      "operationId": "123e4567-e89b-12d3-a456-426655440000"
    }
    

The response from the check method indicates whether all checks succeeded or some checks failed. Success is indicated by the absence of [`checkErrors`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#CheckError) field. Otherwise, the `checkErrors` field lists the failed checks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
