---
url: https://docs.cloud.google.com/application-design-center/docs/enforce-security-policies/
title: Enforce security policies \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:10.326320+00:00
---

# Enforce security policies  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/enforce-security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Enforce security policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To help you both establish authoritative policy requirements and verify that your application infrastructure aligns with organizational security policies before deployment, App Design Center integrates with [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview). An administrator can [deploy frameworks in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#deploy-framework), which you then attach to application templates in App Design Center.

During the application design phase, application developers can [run an assessment](https://docs.cloud.google.com/application-design-center/docs/manage-applications#security-compliance) to analyze the application infrastructure and view compliance findings for each framework directly on the design canvas:

  * Review the assessment scorecard to adjust the design and fix misconfigurations before proceeding with the deployment.
  * Applications inherit the frameworks that are attached to associated application templates. Validation continues post-deployment, where [Security Command Center monitors runtime resources](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) to detect configuration drift.
  * Because App Design Center manages the application lifecycle, you can trace any runtime issues detected by Security Command Center to the specific template revision that introduced them.



This document describes how to attach Security Command Center frameworks to application templates to run assessments and enforce security policies.

## Before you begin

To attach frameworks to your application templates and perform security assessments in App Design Center, you must have [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/service-tiers) active for your organization. The assessment features available to you depend on your service tier:

  * **Standard tier** : Your application templates and instances are validated against the Google Cloud [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) framework.
  * **Premium or Enterprise tier** : In addition to the Security Essentials framework, you can [create additional frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) in Security Command Center and attach them directly to your templates to enforce custom or regulatory compliance.



After [setting up your application management boundary](https://docs.cloud.google.com/application-design-center/docs/setup#choose_your_setup_model), you can view and attach security frameworks in the App Design Center canvas. For more information, see [App Hub as a detection service in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration).

### Required roles

To get the permissions that you need to attach frameworks to templates and run assessments, ask your administrator to grant you the following IAM roles on the management project: 

  * Manage frameworks: [Application Design Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.admin) (`roles/designcenter.admin`) 
  * Attach frameworks to templates and run assessments: [Application Design Center User ](https://docs.cloud.google.com/iam/docs/roles-permissions/designcenter#designcenter.user) (`roles/designcenter.user`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Attach frameworks to your application template

To enforce consistent security policies on deployed applications, attach [Security Command Center frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) directly to your application templates. This applies a consistent set of policies to any application deployed from that template.

To attach frameworks to your application template, do the following:

###  gcloud CLI 

  1. Find available frameworks to attach:
         
         gcloud alpha design-center locations fetch-frameworks LOCATION \
             --project=PROJECT
         

  2. Create a policy to attach the framework to your application template:
         
         gcloud alpha design-center spaces application-templates policies create POLICY \
             --application-template=APPLICATION_TEMPLATE \
             --project=PROJECT \
             --location=LOCATION \
             --space=SPACE \
             --policy-type=compliance-framework \
             --policy-uri=POLICY_URI
         

Replace the following:

     * `POLICY`: A name for the policy attachment, for example, `my-security-policy`.
     * `APPLICATION_TEMPLATE`: The template ID for the application template.
     * `PROJECT`: Your management project ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.
     * `POLICY_URI`: The URI of the Security Command Center framework you want to attach, for example, `organizations/12345/locations/global/frameworks/my-framework`.



## Run an assessment

Before you share a template with application developers, perform a template security assessment. This helps you identify and fix any security issues before application developers deploy an application based on the template:

###  gcloud CLI 
    
    
    gcloud alpha design-center spaces application-templates generate-assessment-report APPLICATION_TEMPLATE \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE
    

Replace the following:

  * `APPLICATION_TEMPLATE`: The template ID for the application template that you want to assess.
  * `PROJECT`: Your management project ID.
  * `LOCATION`: The application template region.
  * `SPACE`: Your space ID.



The output displays an assessment report for your application template based on attached frameworks.

## What's next

  * [Create an application](https://docs.cloud.google.com/application-design-center/docs/manage-applications)
  * [Monitor applications](https://docs.cloud.google.com/application-design-center/docs/monitor-applications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
