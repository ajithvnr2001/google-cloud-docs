---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-trusts/
title: Manage trusts \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:48.841721+00:00
---

# Manage trusts  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-trusts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Manage trusts Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to manage a one-way trust relationship between an on-premises domain and a Managed Microsoft AD domain. It assumes you have already completed the steps in [creating a one-way trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-one-way-trust).

## Validating a trust

To validate the trust, complete the following steps.

###  Console 

  1. Open the Managed Microsoft AD page in the Google Cloud console.   
[Open the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)

  2. Select the domain to validate.

  3. On the domain details page, select the **Trust relationships** tab.

  4. Click **Validate Trust** for trust relationship you want to validate.

  5. The trust state should change to **Validating**. Wait a few minutes for it to change to **Connected** or **Disconnected**.




If the trust state is **Disconnected** , you can obtain more information by describing the domain. For more information, see [Manage domains](https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domains).

###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory domains trusts validate-state domain \
        --target-domain-name=target-domain-name
    

Learn more about the [`validate` command](https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state).

## Monitoring trust health

Managed Microsoft AD periodically verifies the outbound trust state and logs this metric in Cloud Monitoring.

To view the log of the health of the trust, complete the following steps.

  1. Open the Managed Microsoft AD page in the Google Cloud console.   
[Open the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)

  2. In the **Trust relationships** table, in the **Actions** column for your trust, click more_vert.

  3. In the **More** menu, select **Monitoring**.

  4. On the Cloud Monitoring page, you can view a log of the trust's health.




Learn more about [Monitoring](https://docs.cloud.google.com/monitoring/docs).

## Refreshing Name Suffix Routing for an on-premises trust

To refresh the Name Suffix Routing for an on-premises trust, complete the following steps.

  1. Log in to an on-premises domain controller using a Domain or Enterprise administrator account.

  2. Open **Active Directory Domains and Trusts**.

  3. Select the **Trust** tab. It displays outbound and inbound trusts.

  4. Select the trust with the Managed Microsoft AD domain.

  5. Click **Properties**.

  6. Navigate to **Name Suffix Routing**.

  7. Click **Refresh** to add the name suffixes in the Managed Microsoft AD domain.

  8. Click **OK**.




## What's next

  * Learn how to [troubleshoot accessing a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#trust_no_longer_works).
  * Learn how to [troubleshoot creating a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#unable_to_create_trust).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
