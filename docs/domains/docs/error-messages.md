---
url: https://docs.cloud.google.com/domains/docs/error-messages/
title: Cloud Domains error messages \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:01:13.857505+00:00
---

# Cloud Domains error messages  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Cloud Domains error messages Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page provides explanations and recommended resolutions for error messages that you might receive when you're doing any of the following:

  * Using Cloud Domains in the Google Cloud console



## Privacy protection is off or partially off

A help_outline next to **Off** or **Limited** in the **Privacy protection** column indicates that your privacy protection is turned off, and your information is fully or partially available to the public.

To learn more about privacy protection, see [Privacy protection](https://docs.cloud.google.com/domains/docs/overview#privacy-protection).

To turn on privacy protection for your domain, see [Edit registration settings for a domain](https://docs.cloud.google.com/domains/docs/edit-registration-settings#editing_privacy_settings).

## Status indicators

The following table lists status indicators that you might see next to the domain name during registration and how to resolve the issues.

Sign | Status | Description  
---|---|---  
check_circle | **Success** | Your registration is active without any errors.  
warning | **Warning** | There are some issues with the domain—for example, the registrant email was not verified, or the domain is suspended. For information about how to resolve this, see [Domain suspension](https://docs.cloud.google.com/domains/docs/troubleshooting#domain-suspension).  
fiber_manual_record | **Inactive** | The domain is exported.  
error | **Error** | Your registration or transfer has failed. For details about how to fix this issue, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting#during_registration_a_registration_resource_ends_up_in_state_registration_failed).  
![](https://docs.cloud.google.com/static/domains/images/progress_activity_black_24dp.svg) | **In progress** | Your registration or transfer is pending. If this persists, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting#during_registration_a_registration_resource_seems_to_be_stuck_in_state_registration_pending).  
  
## Errors during domain registration

The following table describes errors that you might encounter during the domain registration process when using the gcloud CLI or the API. You can find these errors in one of the following ways:

  * As output when you run the [`gcloud domains registrations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/describe).
  * When you hold the pointer over the status of a domain in the **Status** column in the Google Cloud console. You can also click the status to see the error.

Error message | Description  
---|---  
DOMAIN_NOT_AVAILABLE | The domain is not available for registration. Try registering a different domain.  
INVALID_CONTACTS | The provided contact information was not accepted. Ensure that the contact information is valid and try again.  
REGISTER_FAILURE_REASON_UNKNOWN | Registration failed for an unknown reason.  
  
## What's next

  * To find API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
