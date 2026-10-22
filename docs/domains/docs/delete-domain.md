---
url: https://docs.cloud.google.com/domains/docs/delete-domain/
title: Delete a registered domain \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:14.629550+00:00
---

# Delete a registered domain  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/delete-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Delete a registered domain Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page describes how to delete a registered domain in Cloud Domains.

Before you delete a project with active domain registrations, transfer your registered domains from Cloud Domains to another registrar to avoid losing access.

**Caution:** You can't [delete a domain registration resource](https://docs.cloud.google.com/domains/docs/delete-domain) in Cloud Domains until it has expired or transferred out. However, you can [turn off automatic renewal for a domain name](https://docs.cloud.google.com/domains/docs/edit-registration-settings#turn-off-renew) or [transfer a registered domain to another registrar](https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar) and then delete the domain registration resource in Cloud Domains. 

To delete a registered domain, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.registrations.delete`



**Roles**

  * `roles/domains.admin`



### Console

  1. In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

  2. On the **Registrations** page, select the domain name that you want to delete.

  3. Next to the domain name that you want to delete, click more_vert**More**.

  4. To remove the domain, click delete**Delete**.




### gcloud

Use the [`gcloud domains registrations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/delete):
    
    
    gcloud domains registrations delete DOMAIN_NAME
    

Replace `DOMAIN_NAME` with the name of the registered domain that you want to delete—for example, `example.app`.

### API

Use the [`registrations.delete` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/delete) with an empty request body:
    
    
    DELETE https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations/DOMAIN_NAME
    

Replace the following:

  * `PROJECT_ID`: the name of your project
  * `DOMAIN_NAME`: the name of the domain that you want to delete



## What's next

  * To view a list of your registered domains, see [List registered domains](https://docs.cloud.google.com/domains/docs/list-registrations).
  * To edit registration settings for a domain in Cloud Domains, see [Edit registration settings](https://docs.cloud.google.com/domains/docs/edit-registration-settings).
  * To access API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
