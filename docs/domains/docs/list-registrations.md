---
url: https://docs.cloud.google.com/domains/docs/list-registrations/
title: List registered domains \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:55.083528+00:00
---

# List registered domains  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/list-registrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  List registered domains Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

If you have one or more domains registered with Cloud Domains, you can view a list of your registered domains. This is helpful when you have multiple domain registrations in a project. You can also view the following details for each of your domain registrations:

  * Name
  * DNS provider or name servers
  * Renewal status
  * Renewal date
  * Privacy protection status of your domain



You can apply filters to customize the list that you want to see.

To list and view registration details for your domains, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.registrations.get` to view details of a single registration resource
  * `domains.registrations.list` to list registration resources



**Roles**

  * `roles/domains.viewer`
or 
  * `roles/domains.admin`



###  Console 

In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

The **Registrations** page lists your registrations.

You can view the details of a domain or view a domain in Cloud Domains when it is in the `Active` or `Suspended` state. To view domain registration details, click the domain name.

###  gcloud 

  * To list all domain registrations in a project, use the [`gcloud domains registrations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/list):
        
        gcloud domains registrations list
        

By default, registrations are listed in a table format.

  * To view registration details for a specific domain, use the [`gcloud domains registrations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/describe):
        
        gcloud domains registrations describe DOMAIN_NAME
        

Replace `DOMAIN_NAME` with the name of the domain that you want to view details for—for example, `example.app`.




###  API 

  * To list all registrations in a project, use the [`registrations.list` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/list) with an empty body:
        
        GET https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations
        

You can also use filters to restrict the listed registrations:
        
        GET https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations?filter=FILTER_STRING
        

Replace the following:

    * `PROJECT_ID`: the name of your project
    * `FILTER_STRING`: the [filter](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/list#query-parameters) string that you want to use

Before URL encoding, an example filter string is `domainName:"example.com"`.

After URL encoding, the filter string is `domainName%3D%22example.com%22` and in context looks like the following: 
    
    GET https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations?filter=domainName%3D%22example.com%22
    

  * To view registration details for a specific domain, use the [`registrations.get` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/get) with an empty body:
        
        GET https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations/DOMAIN_NAME
        

Replace the following:

    * `PROJECT_ID`: the name of your project
    * `DOMAIN_NAME`: the name of the domain that you want to get details for



## What's next

  * To edit registration settings for a domain in Cloud Domains, see [Edit registration settings](https://docs.cloud.google.com/domains/docs/edit-registration-settings).
  * To delete a domain, see [Delete a registered domain](https://docs.cloud.google.com/domains/docs/delete-domain).
  * To access API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
