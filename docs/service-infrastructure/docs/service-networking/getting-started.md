---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started/
title: Getting Started with the Service Networking API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:01.904088+00:00
---

# Getting Started with the Service Networking API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Getting Started with the Service Networking API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and start using the Service Networking API. For most operational use cases, Google recommends the `gcloud` [command line interface](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings). If you need to program against the Service Networking API, you can use one of our provided [client libraries](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/libraries).

## Enabling the service

Enable Service Networking in the private services management project. This project handles the private connections with consumer VPC networks. For more information, see [Enabling private services access](https://docs.cloud.google.com/service-infrastructure/docs/enabling-private-services-access).

### console

  1. Select or create a private services management project.

[Go to the manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. Enable the Service Networking API.

[Enable the API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)




### gcloud

Activate the Service Networking API:
    
    
    gcloud services enable servicenetworking.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with the Google Cloud project ID of your private services management project.

Service Networking enables you to offer your [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) on internal IP addresses to service consumers. Service consumers use [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to privately connect to your service. To set up your service for private services access, reach out to your Google representative for more information.

**Note:** When you use private services access as a service producer, you are solely responsible for securing VPC networks and all resources and data available on them. Google is not responsible for how data and resources may be accessed or used by the service consumers that you are connecting with.**Note:** When the Service Networking API is enabled, the service account provisioning will happen just-in-time. This means that unless we do not have a resource (for example: configuration of Private Google Access) configured which calls the API, we won't see the service account getting created. Once the service account gets provisioned, it is visible in the format service-{project number}@service-networking.iam.gserviceaccount.com and is added with roles/servicenetworking.serviceAgent policy binding on the consumer project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
