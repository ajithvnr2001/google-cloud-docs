---
url: https://docs.cloud.google.com/managed-lustre/docs/vpc-sc/
title: Secure instances with VPC Service Controls \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:58.935438+00:00
---

# Secure instances with VPC Service Controls  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Secure instances with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to protect your Managed Lustre instances with a service perimeter using VPC Service Controls.

VPC Service Controls protect against data exfiltration and provide an extra layer of security for your instances. For more information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Once the Managed Lustre API is protected by a service perimeter, Managed Lustre API requests coming from clients outside of the perimeter must have the proper access level rules.

## Securing your Google Cloud Managed Lustre instances using VPC Service Controls

  1. [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  2. Add the Managed Lustre API to your service perimeter. For instructions on adding a service to your service perimeter, see [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).




## Use VPC Service Controls with customer-managed encryption keys (CMEK)

When creating a CMEK-protected Managed Lustre instance within a VPC Service Controls perimeter, your Cloud KMS key must be either:

  * Within the same VPC Service Controls perimeter; or
  * Accessible through an egress rule.



When the CMEK-protected instance and the Cloud KMS keys are in the same perimeter, no further configuration is required.

If the Cloud KMS keys are outside of the perimeter, [add the following rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) to your VPC Service Controls perimeter:
    
    
    {
      "egressFrom": {
        "identityType": "ANY_SERVICE_ACCOUNT",
        "sourceRestriction": "SOURCE_RESTRICTION_ENABLED",
        "sources": [
          {
            "resource": "projects/CONSUMER_PROJECT_NUMBER"
          }
        ]
      },
      "egressTo": {
        "operations": [
          {
            "methodSelectors": [{"method": "*"}],
            "serviceName": "cloudkms.googleapis.com"
          }
        ],
        "resources": [
          "projects/KMS_PROJECT_NUMBER"
        ]
      }
    }
    

Replace the placeholders as follows:

  * CONSUMER_PROJECT_NUMBER is the project number of the project that will contain your CMEK-protected Managed Lustre instance.
  * KMS_PROJECT_NUMBER is the project number of the project containing your Cloud Key Management Service keys.



Learn how to [find a project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Limitations of VPC Service Controls for Managed Lustre instances

The following limitation applies when using VPC Service Controls with Managed Lustre:

  * If you use both Shared VPC and VPC Service Controls, the host project that contains the network and the service project that contains the Managed Lustre instance must both be inside the same perimeter. Separating the host project and service project with a perimeter can cause existing instances to become unavailable and can prevent creation of new instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
