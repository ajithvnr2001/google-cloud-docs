---
url: https://docs.cloud.google.com/iam/docs/key-rotation/
title: Service account key rotation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:45.733829+00:00
---

# Service account key rotation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/key-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Service account key rotation Stay organized with collections  Save and categorize content based on your preferences. 

[Service account keys](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types) are private keys that let you authenticate as a service account. Key rotation is the process of replacing your existing keys with new keys and then invalidating the replaced keys. We recommend that you routinely rotate all keys that you manage, including your service account keys.

Rotating service account keys can help reduce the risk posed by leaked or stolen keys. If a key is leaked, it might take bad actors days or weeks to discover the key. If you regularly rotate your service account keys, there's a higher chance that the leaked keys will be invalid by the time a bad actor gets them.

Having an established process for rotating service account keys also helps you act quickly if you suspect that a service account key has been compromised.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

## How often to rotate keys

We recommend rotating your keys at least every 90 days to reduce the risk posed by leaked keys.

If you believe that a service account key has been compromised, we recommend that you rotate it immediately.

## Key rotation process

To rotate service account keys, do the following:

  1. Identify the service account keys that need to be rotated.
  2. Create new keys for the same service accounts.
  3. Replace the existing keys with the new keys across all applications.
  4. Disable the replaced keys and monitor the applications to confirm that they work as expected.
  5. Delete the service account keys that were replaced.



You can complete these steps by using a centralized secret management service, or by using a custom notification system.

### Centralized secret management service

Many centralized secret management services, like [HashiCorp Vault](https://www.vaultproject.io), provide automatic secret rotation. You can use these services to store and rotate your service account keys.

We don't recommend using Google Cloud's Secret Manager to store and rotate service account keys. This is because, to access Secret Manager secrets, your application needs an identity that Google Cloud can recognize. If your application already has an identity that Google Cloud can recognize, then your application can use that identity to authenticate to Google Cloud instead of using a service account key. 

The same concept applies for other cloud-based secret management services, like Azure KeyVault and AWS Secret Manager. If an application already has an identity that these cloud providers can recognize, your application would be able to use that identity to authenticate to Google Cloud instead of using a service account key.

### Custom notification system

Another approach to service account key rotation is to create a system that sends notifications when keys need to be rotated. For example, you could create a system that sends alerts when it detects keys that were created more than 90 days ago.

First, you need to identify the keys that need to be rotated. To identify these keys, we recommend using Cloud Asset Inventory to search for all service account keys that were created before a certain time.

For example, the following command lists all service account keys that were created before `2023-03-10 00:00:00 UTC` in the organization with the ID `123456789012`:
    
    
    gcloud asset search-all-resources \
        --scope="organizations/123456789012" \
        --query="createTime < 2023-03-10" \
        --asset-types="iam.googleapis.com/ServiceAccountKey" \
        --order-by="createTime"
    

To learn more about searching resources in Cloud Asset Inventory, see [Searching resources](https://docs.cloud.google.com/asset-inventory/docs/searching-resources). After identifying the keys that need to be rotated, you can send out notifications to the appropriate teams.

Additionally, to help the appropriate teams receive critical alerts in the Security category, such as notifications about compromised keys, configure custom contacts using [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

When someone is notified to rotate a key, they should do the following:

  1. [Create a new key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) for the same service account.
  2. Replace the existing key with the new key across all applications.
  3. [Disable the key](https://docs.cloud.google.com/iam/docs/keys-disable-enable#disabling) that they replaced and monitor the applications to confirm that they work as expected.
  4. After they confirm that the applications are working as expected, [delete the replaced key](https://docs.cloud.google.com/iam/docs/keys-create-delete#deleting).



## Expiring service account keys

We don't recommend using expiring service account keys for key rotation. This is because expiring keys can cause outages if they aren't rotated properly. For more information about the use cases for expiring service account keys, see [expiry times for user-managed keys](https://docs.cloud.google.com/iam/docs/service-account-creds#key-expiry).

## What's next

  * Use Cloud Asset Inventory to [search for resources](https://docs.cloud.google.com/asset-inventory/docs/searching-resources), including service account keys, by creation time. 
  * [Create](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating), [disable](https://docs.cloud.google.com/iam/docs/keys-disable-enable#disabling), and [delete](https://docs.cloud.google.com/iam/docs/keys-create-delete#deleting) service account keys.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
