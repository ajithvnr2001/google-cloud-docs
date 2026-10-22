---
url: https://docs.cloud.google.com/looker/docs/looker-core-vpcsc/
title: VPC Service Controls support for Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:48.251883+00:00
---

# VPC Service Controls support for Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  VPC Service Controls support for Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls can improve your ability to mitigate the risk of data exfiltration from Google Cloud services. You can use VPC Service Controls to create service perimeters that help protect the resources and data of services that you explicitly specify.

To add the Looker (Google Cloud core) service to a VPC Service Controls service perimeter, follow the instructions about how to create a service perimeter on the [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#create-perimeter) documentation page, and select **Looker (Google Cloud core) API** in the **Specify services to restrict** dialog. To learn more about using VPC Service Controls, visit the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) documentation page.

VPC Service Controls supports Looker (Google Cloud core) instances that meet two criteria:

  * [Instance editions](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#create_edition) must be **Enterprise** or **Embed**
  * [Instance network configurations](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#set_the_network_connection) must use private connections

**Note:** If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), ensure that you either include the Looker (Google Cloud core) service project in the same service perimeter as the Shared VPC host project or create a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters) between the two projects. If the Looker (Google Cloud core) service project and the Shared VPC host project are not in same perimeter or cannot communicate through a perimeter bridge, instance creation could fail or the Looker (Google Cloud core) instance may not function properly.

## Required roles

To understand the required IAM roles for setting up VPC Service Controls, visit the [Access control with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) page of the VPC Service Controls documentation.

## Removing the default route

When a Looker (Google Cloud core) instance is created inside a Google Cloud project that is within a VPC Service Controls perimeter, or is inside a project that gets added to a VPC Service Controls perimeter, you must remove the default route to the internet. Removing the default route restricts outgoing traffic to only [VPC Service Controls compliant services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). For example, if the default route is removed, sending email fails because the API used to send email isn't VPC Service Controls compliant.

**Note:** The `gcloud services vpc-peerings` command and the `services.enableVpcServiceControls` REST method are supported only for Looker (Google Cloud core) instances that use [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa). For instances that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview), the `gcloud services vpc-peerings` command isn't supported and fails with a `PRODUCER_TENANT_PROJECT_NOT_FOUND` error. Instead, you control the default route for Private Service Connect instances by using your VPC network's [routes](https://docs.cloud.google.com/vpc/docs/routes) and [firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

To remove the default route to the internet for a private services access instance, select one of the following options:

### gcloud
    
    
    gcloud services vpc-peerings enable-vpc-service-controls --network=NETWORK --service=servicenetworking.googleapis.com
    

Replace `NETWORK` with your Looker (Google Cloud core) instance's VPC network.

For more information, visit the [gcloud services vpc-peerings enable-vpc-service-controls](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls) documentation page.

### REST

HTTP method and URL:
    
    
    PATCH https://servicenetworking.googleapis.com/v1/{parent=services/*}:enableVpcServiceControls
    

Request JSON body:
    
    
    {
    "consumerNetwork": NETWORK
    }
    

Replace `NETWORK` with your Looker (Google Cloud core) instance's VPC network.

For more information, visit the [Method: services.enableVpcServiceControls](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/enableVpcServiceControls) documentation page.

## Connecting to resources or services outside the VPC Service Controls perimeter

To connect to another Google Cloud resource or service, you may need to set up [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) if the project that the resource is in is located outside the VPC Service Controls perimeter.

For information about accessing other external resources, follow the instructions for the type of resource that you want to connect to on either the [Access external services using private services access](https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config) or the [Looker (Google Cloud core) southbound access to external services using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) documentation page (depending on whether your instance uses private services access or Private Service Connect).

**Note:** If you are creating a Looker (Google Cloud core) instance inside a Shared VPC, and the Shared VPC host project and the Looker (Google Cloud core) service project are in different VPC Service Controls perimeters, you must create a [VPC Service Controls perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges) between the two perimeters to allow instance creation.

## Adding CMEK keys to a perimeter

Sometimes, a Looker (Google Cloud core) instance that is [enabled with customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) has the Cloud KMS key hosted in a different Google Cloud project. For this scenario, when you enable VPC Service Controls, you must add the KMS key hosting project to the security perimeter.

## What's next?

  * [Connect Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Set up the Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
