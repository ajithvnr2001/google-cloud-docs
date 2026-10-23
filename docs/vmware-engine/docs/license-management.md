---
url: https://docs.cloud.google.com/vmware-engine/docs/license-management/
title: License management \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:00.713777+00:00
---

# License management  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/license-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# License management

This document describes how to register and manage Bring Your Own License (BYOL) license keys for Google Cloud VMware Engine.

BYOL license management in the Google Cloud console lets you apply VMware Cloud Foundation (VCF) portable licenses—acquired directly from Broadcom or an authorized reseller—to Google Cloud. Registering license keys tracks node CPU core capacity in entitlement usage reports.

You manage licenses at the Cloud Billing account level rather than per project. Entitlements cover node CPU core capacity across all projects linked to that Cloud Billing account.

For node options and pricing, see [VMware Engine pricing](https://docs.cloud.google.com/vmware-engine/pricing).

## License lifecycle operations

You can perform the following lifecycle operations on license keys:

  * **Add license key** : Register a license key by providing the product type, key string, core quantity, effective start and end dates, and Broadcom Site ID.
  * **Update license key** : Adjust core counts or extend expiration dates by re-entering the existing key string with updated parameters. The new entry supersedes the existing record.
  * **Sunset license key** : Permanently mark an active key as retired so that VMware Engine excludes it from future usage calculations.
  * **View dashboard** : View a list of registered keys, their statuses (Active, Sunsetted, or Expired), and active core capacity across the billing account.

**Note:** You can't specify past expiration dates in the console. To retire a key before its expiration date, use the sunset process. Key sunsetting is permanent and can't be undone. To restore a sunsetted key, you must add the key string again as a new entry.

## How BYOL licenses apply to usage

Ported BYOL entitlements apply to node CPU core capacity across all projects associated with the Cloud Billing account. VMware Engine aggregates active core counts across linked projects to calculate total core usage.

BYOL licenses don't apply to the following:

  * Underlying Google Cloud infrastructure spend
  * Storage and backups
  * IP addresses and network outbound data transfer
  * Third-party add-ons outside supported VCF components



## Register BYOL license keys

You register license keys at the Cloud Billing account level. When a Broadcom license expires, you must renew it directly with Broadcom.

**Caution:** Registering a license key requires compliance attestation. You must confirm that registered keys comply with your agreement with Broadcom.

### Before you begin

Before you register license keys, verify that you have the following license key attributes from your Broadcom portal:

  * Product type
  * License key string
  * Core quantity
  * Effective start and end dates
  * Broadcom Site ID



In addition, ensure that you have the required Identity and Access Management (IAM) permissions and have enabled the Enterprise Purchasing API.

#### Required IAM permissions

To manage or view license keys, ensure that you have one of the following IAM roles on the project:

  * `roles/enterprisepurchasing.admin`: Add, update, or sunset license keys.
  * `roles/enterprisepurchasing.viewer`: View license keys.



#### Custom role permissions

If you use custom roles instead of predefined roles, ensure that your custom roles include the following permissions on the project:

  * `enterprisepurchasing.googleapis.com/licenseKeys.create`
  * `enterprisepurchasing.googleapis.com/licenseKeys.delete`
  * `enterprisepurchasing.googleapis.com/licenseKeys.get`
  * `enterprisepurchasing.googleapis.com/licenseKeys.list`



For more information about roles, see [VMware Engine IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam).

#### Enable the Enterprise Purchasing API

Before managing or viewing license keys, go to the **API Library** in the Google Cloud console and enable the Enterprise Purchasing API (`enterprisepurchasing.googleapis.com`):

[Enable the API](https://console.cloud.google.com/apis/library/enterprisepurchasing.googleapis.com)

To enable the API, ensure that you have the required permissions on the project:

  * **Project owners and administrators** : If you have the Project Owner (`roles/owner`) or Project Editor (`roles/editor`) role, you have the required permissions by default and can enable the service without additional role assignments.
  * **Standard project contributors** : If you have a basic viewer or resource-level role, you can't enable services by default. To grant the minimum privileges required to enable the service, an administrator must grant you the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).



### Register a license key

You register license keys by using the Google Cloud console. After you register a key, VMware Engine updates available core capacity across all projects linked to the billing account.

**Note:** The console verifies syntax and input formatting, but doesn't perform real-time backend API validation against Broadcom systems during key registration.

To register a new BYOL license key, do the following:

  1. In the Google Cloud console, go to the **License Management** page.

[Go to License Management](https://console.cloud.google.com/vmwareengine/licenses)

  2. Click **Add License Key**.

  3. In the **License Key String** field, enter the license key string.

  4. In the **Product Name** list, select your Broadcom product.

  5. In the **Quantity (Cores)** field, specify the number of cores allocated to this license key.

  6. In the **Start Date** and **End Date** fields, select the effective dates matching your Broadcom agreement.

  7. In the **Site ID** field, enter your Broadcom Site ID.

  8. Select the compliance attestation checkbox.

  9. Click **Submit**.




The registered license capacity takes effect immediately for all project quota requests.

## Troubleshooting

The following table describes common issues and how to resolve them:

Issue | Resolution  
---|---  
A license key was sunsetted by mistake. |  Sunsetting is permanent and can't be undone. To restore the key, re-enter the license key string by using the **Add License Key** flow.   
Unable to view or manage BYOL license keys in the Google Cloud console.  |  Verify that the Enterprise Purchasing API is enabled on the project and that you have the `roles/enterprisepurchasing.admin` or `roles/enterprisepurchasing.viewer` role (or equivalent custom permissions) on the project.   
  
## Support

If you need support or have questions regarding your Broadcom licensing agreement, contact Broadcom or your licensing reseller. If you need support with VMware Engine, [contact Customer Care](https://docs.cloud.google.com/support).

## What's next

  * Learn about [VMware Engine committed use discounts](https://docs.cloud.google.com/vmware-engine/docs/cud).
  * Learn about [VMware Engine node quotas and limits](https://docs.cloud.google.com/vmware-engine/quotas).
  * Learn about [VMware Engine pricing](https://docs.cloud.google.com/vmware-engine/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
