---
url: https://docs.cloud.google.com/resource-manager/docs/essential-contacts-fallback-contacts/
title: Fallback contacts \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:59.572589+00:00
---

# Fallback contacts  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/essential-contacts-fallback-contacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Fallback contacts Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a reference of default fallback contacts for each notification category in Essential Contacts. When you don't configure a custom contact for a notification category, Google Cloud automatically routes notifications to fallback contacts based on their IAM roles.

To learn how to add, modify, or remove custom contacts, see [Manage Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts). To learn more about general Essential Contacts capabilities and recommended recipients, see [Essential Contacts overview](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## How fallback contacts work

Essential Contacts provides a central directory for custom notification contacts. When an event triggers a notification, such as a billing invoice alert, security vulnerability advisory, or scheduled maintenance notice, Google Cloud resolves recipients through the following process:

  1. **Direct contact assignment** : Google Cloud checks whether custom contacts are configured for that specific [notification category](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) on the target resource, such as a project.
  2. **Hierarchy inheritance** : If no custom contact exists at the resource level, the system evaluates parent folders and the organization resource for inherited contacts.
  3. **Role-based fallback** : If no custom contacts are configured anywhere in the resource hierarchy for that category, Google Cloud identifies principals holding designated IAM roles on the resource and sends the notification to them as _fallback contacts_.



Even when custom contacts are configured, individual Google Cloud services might also send direct notifications to specific IAM role holders based on their independent service requirements. For more information, see the documentation for each specific service.

## Fallback contacts by category

The following table lists the default fallback contact role and examples of notifications sent for each Essential Contacts notification category.

**Category** | **Default fallback contact** | **Examples of notifications**  
---|---|---  
**Billing** | Billing Account Administrator (`roles/billing.admin`) | 

  * Price updates for services you use
  * Payment method errors or expiration warnings
  * Budget threshold alerts
  * Changes to billing accounts, invoices, and payment instruments
  * Overdue payment notifications
  * Catalog approvals

  
**Legal** | Billing Account Administrator (`roles/billing.admin`) | 

  * Enforcement actions related to your services
  * Regulatory compliance updates and audits
  * Government notices or legal requests concerning your account
  * Changes to Terms of Service or other legal agreements

  
**Product updates** | Project Owner (`roles/owner`) | 

  * Feature announcements and general availability updates
  * Version deprecations
  * Product terms updates
  * Deprecation notices and lifecycle transitions
  * Service migrations and architectural requirement changes

  
**Security** | Organization Administrator (`roles/resourcemanager.organizationAdmin`) | 

  * Security bulletins and high-severity vulnerability advisories
  * Vulnerability alerts, including details on detected critical vulnerabilities affecting your resources
  * Data breach incidents and privacy notifications
  * Information on detected malicious attacks originating from or targeting your resources
  * Advisories on widespread threats that might require user attention
  * Abuse, cryptomining, and security incident notifications
  * Terms of Service violations
  * Notifications related to project deletion

  
**Suspension** | Project Owner (`roles/owner`) | 

  * Apigee evaluation compliance issues or expiration
  * Copyright infringements
  * Critical abuse alerts that might lead to suspension
  * General notifications because of nonpayment or Terms of Service violations

  
**Technical** | Project Owner (`roles/owner`) | 

  * Logging configuration errors
  * Data loss prevention updates
  * Upcoming maintenance and zone disruptions
  * Service disruptions, outages, or degradations
  * Updates regarding SLO breaches
  * Actions on Google status
  * Abuse notifications

  
**All** | Not applicable.  
  
This category acts as a superset and doesn't have a dedicated fallback contact. If you don't assign a contact to the **All** category, Google Cloud evaluates fallback contacts on a per-category basis. | Contacts in this category receive notifications from all of the following categories:  


  * Billing
  * Legal
  * Product updates
  * Security
  * Suspension
  * Technical

  
  
## Recommendations for fallback management

Follow these recommended practices to manage fallback contacts:

  * **Configure group aliases** : Use email distribution lists, such as `gcp-security@example.com` or `gcp-billing@example.com`, instead of individual email addresses. This practice ensures notifications reach the entire responsible team even when personnel changes occur.
  * **Assign contacts at higher resource levels** : Assigning contacts at the organization or folder level lets child projects inherit contacts automatically, preventing unconfigured projects from defaulting to fallback contacts.
  * **Establish a verification schedule** : Periodically review and validate contact lists in the Google Cloud console to verify that designated email addresses remain active and monitored.
  * **Prepare fallback recipients** : If you don't configure custom contacts and rely on default fallback contacts for your notification categories, make sure that fallback recipients are prepared to handle notifications as necessary. For example, the Billing Account Administrator must be aware that they will receive legal notifications as a fallback.



For more details on contact configuration and inheritance, see [Best practices for Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#best-practices).

## What's next

  * Learn how to [Manage Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts).
  * Review the [Essential Contacts overview](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
