---
url: https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar/
title: Transfer a registered domain to another registrar \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:59.672755+00:00
---

# Transfer a registered domain to another registrar  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Transfer a registered domain to another registrar Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page describes how to transfer a registered domain from Cloud Domains to a third-party domain registrar.

By default, domains that support transfer locks are locked to prevent unauthorized transfers. To prepare a domain for transfer, you must do the following:

  * Unlock the domain to make it eligible for a transfer. Some domain registrars don't support transfer locks due to registry restrictions. These domains typically remain unlocked—for example, `.co.nz`, `.de`, `.fr`, `.jp`, `.nl`, and `.pw`.
  * Get an authorization code to provide to your new domain registrar. Some domains don't support authorization codes—for example, `.uk` and `.co.uk`.
  * Verify that your contact details in the WHOIS database are correct.



## Unlock a domain for transfer

To unlock a domain for transfer, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.registrations.configureManagement`



**Roles**

  * `roles/domains.admin`



###  Console 

  1. In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

  2. Click the domain name that you want to transfer.

  3. To unlock the domain, click **Unlock**.

  4. On the confirmation dialog, click **Unlock**.

A message at the bottom of the page confirms that the unlocking is successful.




###  gcloud 

Use the [`gcloud domains registrations configure management` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management):
    
    
    gcloud domains registrations configure management DOMAIN_NAME
    

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.com`.

Your output looks similar to the following:
    
    
    Your current Transfer Lock state is: LOCKED
    Specify new transfer lock state
     [1] locked
     [2] unlocked
     [3] cancel
    Please enter your numeric choice (3):  2
    
    Waiting for 'operation-1596736789522-5ac394123aa03-f2d2f2c3-948ac1a3' to complete...done.
    Updated registration [example.com].
    

###  API 

Use the [`registrations.configureManagementSettings` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureManagementSettings):
    
    
    POST https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations/DOMAIN_NAME:configureManagementSettings
    
    {
      "managementSettings": {
        "transferLockState": "UNLOCKED"
      },
      "updateMask": "transferLockState"
    }
    

Replace the following:

  * `PROJECT_ID`: the name of your project
  * `DOMAIN_NAME`: the domain that you want to transfer



## Get the authorization code

To get the authorization code for a transfer, see [Get or reset an authorization code](https://docs.cloud.google.com/domains/docs/reset-authorization-code).

Some domains, such as `.uk` or `.co.uk`, don't support authorization codes. For instructions about how to transfer a `.uk` or `.co.uk` domain to another registrar, see the next section.

## Transfer a `.uk` or a `.co.uk` domain

To transfer a `.uk` or `.co.uk` domain to another registrar, initiate a push transfer.

The transfer might happen instantly, or it might take some time to complete. Contact your new registrar if the transfer doesn't complete within a few days.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.registrations.configureManagement`



**Roles**

  * `roles/domains.admin`



### gcloud

Use the [`gcloud domains registrations initiate-push-transfer` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/initiate-push-transfer):
    
    
    gcloud domains registrations initiate-push-transfer DOMAIN_NAME \
        --tag=NEW_REGISTRY_TAG
    

Replace the following:

  * `DOMAIN_NAME`: the name of the registered domain that you want to renew—for example, `example.app`.
  * `NEW_REGISTRY_TAG`: the tag of the new registrar as documented in [List of registrars](https://nominet.uk/registrar-list/).



### API

Use the [`registrations.initiatePushTransfer` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/initiatePushTransfer):
    
    
    POST https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations/DOMAIN_NAME:initiatePushTransfer
      {
        "tag" : "NEW_REGISTRY_TAG"
      }
    

Replace the following:

  * `PROJECT_ID`: the name of your project
  * `DOMAIN_NAME`: the name of the domain that you want to renew
  * `NEW_REGISTRY_TAG`: the tag of the new registrar. To get the tag of your new registrar, see [List of registrars](https://nominet.uk/registrar-list/).



## Verify contact details

To ensure that your new registrar can confirm your intent to transfer, verify that your contact details for the domain registration are correct. Some registrars might require you to make your contact information public before you transfer a domain.

For instructions about how to change your contact and privacy settings, see [Edit contact and privacy settings](https://docs.cloud.google.com/domains/docs/edit-registration-settings#edit-contact-and-privacy-settings).

## What's next

  * To edit registration settings by using Cloud Domains, see [Edit registration settings](https://docs.cloud.google.com/domains/docs/edit-registration-settings).
  * To access API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
