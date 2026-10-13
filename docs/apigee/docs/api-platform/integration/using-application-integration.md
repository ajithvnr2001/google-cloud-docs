---
url: https://docs.cloud.google.com/apigee/docs/api-platform/integration/using-application-integration/
title: Use Application Integration \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:11.441828+00:00
---

# Use Application Integration  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/integration/using-application-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Use Application Integration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information intended for existing Apigee customers who want to use Application Integration with the same Google Cloud project. 

## Overview

All Apigee subscription users who had enabled the _Apigee Integrations_ add-on, will now be redirected to Application Integration at no additional cost. Application Integration is set up for you, and all your existing integrations in Apigee were automatically synchronized and available to use. This means that you can continue to use your existing Google Cloud project for Application Integration without any additional configurations. 

To learn more about Application Integration, see [Application Integration overview](https://docs.cloud.google.com/application-integration/docs/overview). 

**Note:** Existing integrations configured in the `US multi-region(us)` location are not available in Application Integration. 

From the Apigee UI, go to the **Application Integration** page.

[Go to Application Integration](https://console.cloud.google.com/integrations)

![Redirect from Apigee to Application Integration](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/application_integration.png)![Redirect from Apigee to Application Integration](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/application_integration.png)

**Tip:** We recommend using the Application Integration [API reference](https://docs.cloud.google.com/application-integration/docs/apis) and [IAM permissions](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions) once you start using Application Integration. 

## What has changed?

The following table provides a summary of the expected differences or changes in your Google Cloud project: 

Apigee resource/feature  | Changes   
---|---  
**IAM permissions** | Integrations now use the predefined Application Integration IAM roles. See IAM permission changes.  
**Service account** | A new default service account is created that is used for all integrations. See Service account changes.  
**REST APIs** | Use Application Integration REST API. See REST API changes.  
**Send Email task and Approval task** | The sender email address is changed for all outgoing emails. See Integration task changes.  
  
### IAM permission changes

All existing user accounts or principals are granted with equivalent [Predefined Application Integration](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions) IAM permissions. 

Application Integration IAM permissions have the following format: 

### Format
    
    
    integrations.integrationRESOURCE.ACTION
    

### Example
    
    
    integrations.integrationVersions.get
    

#### Custom IAM role limitations

The following limitations apply if you have defined [custom IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) in your Google Cloud project:

  * Apigee proxies using a service account with custom IAM roles containing Apigee Integration permissions might fail. We recommend that you update your custom IAM roles with the Application Integration [IAM permissions](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions). 



For information about IAM roles and permissions, see [Access control overview](https://docs.cloud.google.com/application-integration/docs/access-control).

### Service account changes

A new default service account with the [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) `(roles/integrations.serviceAgent)` IAM role is created in your Google Cloud project. 

The new Application Integration default service account is used for the following integration operations: 

  * To run an integration.
  * To invoke a Cloud Function using the [Cloud Function task](https://docs.cloud.google.com/application-integration/docs/configure-cloud-function-task).
  * To call an Integration Connector using the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).
  * To create service account tokens for [Service account type](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#service-account) authentication profiles.
  * To encrypt and decrypt Cloud KMS keys for authentication profiles. 



Application Integration default service account has the following email address:

### Format
    
    
      service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com
    

### Example
    
    
      service-46733320069@gcp-sa-integrations.iam.gserviceaccount.com
    

For information about service accounts, see [Access control overview](https://docs.cloud.google.com/application-integration/docs/access-control#sa).

**Notes:** Apigee will continue to use the existing default Apigee service account—`service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com`—for other Apigee resources and operations. 

### REST API changes

In general, most of the Apigee Integration APIs have their respective Application Integration API equivalents. 

The following table describes the key change in the REST APIs of Application Integration when compared to Application Integration: 

| Apigee Integration (including Apigee proxy)  | Application Integration   
---|---|---  
**REST Resource** | `projects/PROJECT_ID/locations/REGION/products/apigee/integration/INTEGRATION_NAME` | `projects/PROJECT_ID/locations/REGION/integration/INTEGRATION_NAME`  
**Note:** Your existing resource paths will continue to work in Application Integration. 

For information about Application Integration APIs, see [Application Integration REST API](https://docs.cloud.google.com/application-integration/docs/apis).

### Integration task changes

The [Send Email](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task) task and the [Approval](https://docs.cloud.google.com/application-integration/docs/configure-approval-task) task will use `noreply-application-integration@google.com` to send email notifications. In addition, all the approval request emails sent using the [Approval task](https://docs.cloud.google.com/application-integration/docs/configure-approval-task) will link to Application Integration. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
