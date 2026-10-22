---
url: https://docs.cloud.google.com/domains/docs/troubleshooting/
title: Troubleshoot Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:43.466814+00:00
---

# Troubleshoot Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Troubleshoot Cloud Domains Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page describes common issues that you might encounter while using Cloud Domains and how to resolve them.

## Domain registration issues

This section lists some issues that you might encounter when registering your domain.

#### The `searchDomains` API call shows a domain name as available, but `retrieveRegisterParameters` shows it is not

The `searchDomains` call checks a large space of possible domain names to provide suggestions. It relies on an availability cache that might be incomplete or out of date. The `retrieveRegisterParameters` call, on the other hand, deals with only one domain name at a time and provides up-to-date domain name availability information.

#### You cannot use preferred contact privacy mode with the domain you are trying to register

The available contact privacy modes depend on the ending of the domain name that you choose. Domain endings are administered by many different partner registries, and some of these have unique behavior and requirements. For example, some domain endings don't allow contact privacy at all, and others redact certain parts of your contact information from the public WHOIS registry. Prior to registration, refer to the `supportedPrivacy` field in the output of `retrieveRegisterParameters` to determine which contact privacy modes are supported for a given domain name. After registration, the supported contact privacy modes are listed in the `supportedPrivacy` field of the registration resource.

#### During registration, a `registration` resource seems to be stuck in `state: REGISTRATION_PENDING`

The `REGISTRATION_PENDING` state should be short-lived, in the order of a few minutes in most cases, before transitioning to `ACTIVE`. If a registration is pending for more than a few hours, contact [Google Cloud support](https://docs.cloud.google.com/support).

#### During registration, a registration resource ends up in `state: REGISTRATION_FAILED`

When a domain registration fails, you can call `retrieveRegisterParameters` again to check whether the domain is still available. If it is, you can delete your registration and try to register again.

There are also a number of common data-quality issues that can cause your domain registration to fail. For example, if you are setting custom name servers when registering the domain, they might not be recognized as registered name servers by the controlling [registry](https://docs.cloud.google.com/domains/docs/key-terms#terms-registry). To complete your registration, you can temporarily set your DNS provider to Cloud DNS and change it after registration.

For details about the errors that you might receive during domain registration, see [Errors during domain registration](https://docs.cloud.google.com/domains/docs/error-messages#errors_during_domain_registration).

If the problem persists, contact [Google Cloud support](https://docs.cloud.google.com/support).

#### You are getting a `Quota exceeded` error while trying to register a domain

You might have exceeded the quota for the number of registered domains. For detailed information about quotas, see the [Quotas](https://docs.cloud.google.com/domains/quotas) page.

## Registrant email verification issues

This section lists some issues that you might encounter when verifying your email address after registering a domain.

#### After registering a domain, you don't get a verification email

If you used the same registrant email address before with another domain name, you might not need to verify the address again. You can check your verification status directly on the registration resource, which shows `UNVERIFIED_EMAIL` in the `issue` field if your verification is pending. You can trigger a resend of the verification email on the Cloud Domains **Registration details** page.

#### Why must you verify your email address after registering a domain?

When you register a domain, Google requires you to verify your email address. You receive an email with instructions to complete the verification. If you fail to verify your email address within 15 days of registration, your domain is suspended.

#### You no longer have access to your verified email address

If the registrant email address is inaccessible by the named registratant, or if you don't have access to the registrant email address, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

#### Your domain got suspended due to lack of email verification

If your domain is suspended due to lack of email verification, your registration resource will be in `state: SUSPENDED`, and the issue field will contain `UNVERIFIED_EMAIL`. In this case, trigger a resend of the verification email on the Cloud Domains **Registration details** page, and then follow the instructions in that email to complete email verification. After verification is completed, your domain's suspension is automatically lifted.

## Contact configuration issues

This section lists some issues that you might encounter when configuring your contact information.

#### Changes to your contact configuration are not taking effect

Due to Internet Corporation for Assigned Names and Numbers (ICANN) requirements, many types of contact changes require confirmation from both the previous registrant and the new registrant. While changes that you made are awaiting such confirmation, they are temporarily listed in the `pendingContactSettings` field of the registration resource. To confirm pending changes, the earlier and new registrants must follow the confirmation instructions that they receive.

To resend change confirmations that might have been lost, trigger a resend of the verification email on the Cloud Domains **Registration details** page.

#### You are listed as the registrant contact, but have lost access to your domain

Registrants are considered to be the rightful owners of a domain registration. If you are listed as the registrant contact but have lost access to the domain, contact [Customer Care](https://docs.cloud.google.com/support).

#### You deleted a project and lost access to your domain

If you delete the project that contains your `Registration` resource, you lose access to the domain. You have a few recovery options. If you deleted the project recently, you can [restore the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project), and then you can [transfer a registered domain to another registrar](https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar).

If you cannot restore your project, the registrant contact can reach out to [Google Cloud support](https://docs.cloud.google.com/support) to gain access to the domain.

#### Contact details while registering or transferring a domain for a company

When registering a domain that is owned by a company, the registrant must provide the company's contact details such as email address and phone number. If the registrant provides their personal contact details, the company might lose access to the domain when the registrant leaves.

## DNS configuration issues

This section lists some issues that you might encounter when configuring DNS settings.

#### You made changes to your DNS configuration but the changes are not taking effect

Due to the nature of DNS as a distributed system, changes to DNS configurations often take a while to propagate to the entire internet. This is because DNS resolvers anywhere in the world can cache your earlier configuration for a length of time equal to the TTL of that record. Thus, it might take the full duration of the previously configured TTL for your new configuration to become fully visible. For Cloud Domains, changes to the DNS provider or name servers and changes related to [DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec) can often take up to a day to become fully visible across the internet.

#### You published DS records and now your domain is not resolving

Publishing DS records is the last step in enabling DNSSEC for your domain. To ensure that your domain continues to resolve, DS records should generally be removed a day or two before changing your name servers or DNS provider. Similarly, new DS records should be published no sooner than a day or two after completing a name server or DNS provider change.

If problems resolving your domain coincide with changes to DS records, it means that your DNS domain provider has not properly signed your domain's DNS configuration. You can remove the DS records to see if that fixes the problem. However, like any other DNS change, removing the DS records can take some time (up to the TTL of the removed records) to take effect.

#### You chose Google Domains as your DNS provider, but cannot see your zone in Cloud DNS

**Caution:** Google Domains as your Domain Name System (DNS) provider for your domains in Cloud Domains is retired, and some DNS functionality from Cloud Domains is no longer supported. For more information, see [Cloud Domains feature deprecation](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations). 

Choosing Google Domains as your free DNS provider means that you must manage your DNS configuration by using the Google Domains website. These DNS configurations are not visible in the Cloud DNS product and don't provide API access for configuration. If you require API access, create a zone in Cloud DNS and configure your domain to use that zone.

**Note:** You are billed separately for the Cloud DNS service.

## Billing issues

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

For detailed domain pricing information, see [Cloud Domains pricing](https://cloud.google.com/domains/pricing). For common billing questions, see [Billing questions](https://docs.cloud.google.com/domains/docs/billing-questions).

#### You want to disable automatic renewals for your domain

By default, all domains in Cloud Domains renew automatically. To turn off automatic renewal of your domain, see [Turn off automatic renewal for a domain name](https://docs.cloud.google.com/domains/docs/edit-registration-settings#turn-off-renew). You can manage the domain in Cloud Domains until its current registration period expires and you are billed for the full registration year.

#### You want to delete your domain and return it to the pool of available domains

To delete your domain before your registration expires, contact [Customer Care](https://docs.cloud.google.com/support).

## Domain transfer issues to and from other registrars

**Caution:** Transferring a registered domain from a third-party domain registrar to Cloud Domains is deprecated and removed. For more information, see [Google Domains feature deprecation](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations). 

This section lists some issues that you might encounter when transferring your domain to other registrars.

#### You want to transfer your domain from Cloud Domains to another registrar but can't access your transfer authorization code

Cloud Domains does not allow transfers to other registrars within the first 60 days of registration. To request an exception, contact [Customer Care](https://docs.cloud.google.com/support).

If your registration has crossed the 60-day limit, see [Get or reset an authorization code](https://docs.cloud.google.com/domains/docs/reset-authorization-code).

#### You want to transfer a `.uk` or a `.co.uk` domain from Cloud Domains to another registrar but these domains don't support authorization codes

Some domains, such as `.uk` or `.co.uk`, don't support authorization codes. For more information, see [Transfer a `.uk` or a `.co.uk` domain](https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar#initiate-push-transfer).

## Domain suspension issues

This section lists some issues that you might encounter if you haven't yet verified your domain.

#### Your domain stopped working and has `state: SUSPENDED`

When your registration resource is in `state: SUSPENDED`, you can generally find more information in the `issues` field. The most common cause of suspension is `issues: UNVERIFIED_EMAIL`. For details, see the Registrant email verification section.

There are many other possible causes of domain suspension. If you see `issues: CONTACT_SUPPORT` on your registration resource, contact the [Google Cloud support](https://docs.cloud.google.com/support) team to learn more about the domain suspension.

## What's next

  * To resolve errors, see [Error messages](https://docs.cloud.google.com/domains/docs/error-messages).
  * To find API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
