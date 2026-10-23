---
url: https://docs.cloud.google.com/secure-source-manager/docs/configure-service-perimeter/
title: Configure Secure Source Manager in a VPC Service Controls perimeter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:30.085245+00:00
---

# Configure Secure Source Manager in a VPC Service Controls perimeter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/configure-service-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Configure Secure Source Manager in a VPC Service Controls perimeter Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to use a Private Service Connect Secure Source Manager in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter to guard against data exfiltration.

This guide is intended for network administrators, security architects, and cloud operations professionals who want to mitigate the risk of sensitive data loss.

## Before you begin

  1. [Create a Private Service Connect Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-private-service-connect-instance).
  2. [Create a VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).



### Required roles

To get the permissions that you need to configure Secure Source Manager in a VPC Service Controls perimeter, ask your administrator to grant you the following IAM roles on the organization: 

  * [Access Context Manager Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)
  * [Project Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`)



## Follow best practices

Careless enablement of VPC Service Controls can cause problems with existing applications and could potentially cause an outage. We recommend that you plan enablement carefully and allow ample time to gather data, conduct tests, and analyze violation logs. Make sure that stakeholders from your VPC Service Controls operations team and your applications team are available for the task.

For more information on best practices, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable)

## Add your project to the perimeter

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, select the perimeter you want to use to protect your project.

  3. On the **VPC Service Control enforced config detail** page, click **Edit** in the **resources to protect** section.

  4. Click **Resources to protect** and add your project ID.

  5. Click **Save**.




## Add Secure Source Manager as a restricted service

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, select the perimeter you added your project to.

  3. On the **VPC Service Control enforced config detail** page, click **Edit** in the **Restricted services** section.

  4. Click **Add services**.

  5. In the **Specify services to restrict** dialog, select the checkbox next to Secure Source Manager. You can use the filter query to locate Secure Source Manager in the list.

  6. Click **Save**.




After you update a service perimeter, it can take up to 30 minutes for the changes to propagate and take effect. During this time, the perimeter might block requests with the following error message:
    
    
    Error 403: Request is prohibited by organization's policy.
    

## What's next

  * Learn more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * Learn more about [Connecting to VMs without external IP addresses](https://cloud.google.com/solutions/connecting-securely#external).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
