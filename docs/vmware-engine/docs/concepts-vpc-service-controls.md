---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls/
title: VPC Service Controls with VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:07.290313+00:00
---

# VPC Service Controls with VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VPC Service Controls with VMware Engine

To further protect your Google Cloud VMware Engine resources, you can protect them using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

VPC Service Controls lets you define a security perimeter for your VMware Engine resources. The service perimeter limits exporting and importing of resources and their associated data to within the defined perimeter. Google recommends creating your service perimeter and adding VMware Engine to the Restricted Services before creating your first Private Cloud.

When you create a service perimeter, you select one or more projects to be protected by the perimeter. Requests between projects within the same perimeter remain unaffected. All existing APIs continue to function as long as the resources involved are within the same service perimeter. Note the IAM roles and policies still apply within a service perimeter.

When a service is protected by a perimeter, requests cannot be made by the service _inside_ the perimeter to any resource _outside_ the perimeter. This includes exporting resources from inside to outside the perimeter. For more information, see [Overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) in the VPC Service Controls documentation.

In order to ensure VPC Service Controls works for VMware Engine, you must add the VMware Engine service to the Restricted Services within VPC Service Controls.

## Limitations

  * When adding existing VMware Engine, Private Clouds, Network Policies, and VPC Peering to a VPC Service Perimeter, Google does not check previously created resources to see if they still comply with the perimeter's policies.



## Expected behaviors

  * Creating VPC Peering to a VPC outside of the perimeter will be blocked.
  * Use of VMware Engine workload internet access service will be blocked.
  * Use of External IP address service will be blocked.
  * Only the restricted Google APIs IPs will be available - `199.36.153.4/30`.



## Add VMware Engine to allowed VPC Service Controls

To add the VMware Engine service to the allowed VPC Service Controls, you can follow these steps in the [Google Cloud console](https://console.cloud.google.com/):

  1. Go to the [VPC Service Controls](https://docs.cloud.google.com/console/security/service-perimeter) page.
  2. Click the name of the perimeter that you want to modify.
  3. On the **Edit VPC Service Perimeter page** , click the **Restricted Services** tab.
  4. Click **Add Services**.
  5. In the **Specify services to restrict** section, check the field for VMware Engine. If not already selected, check the fields for **Compute Engine API** and **Cloud DNS API**.
  6. Click **Add Services**.
  7. Click **Save**.



## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Learn about services supported by [restricted virtual IPs](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services).
  * Read more about [service perimeter configuration steps](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#stages). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
