---
url: https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts/
title: Essential Contacts overview \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:35:00.889953+00:00
---

# Essential Contacts overview  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Essential Contacts overview Stay organized with collections  Save and categorize content based on your preferences. 

You can use Essential Contacts to establish a custom directory of contacts to address critical Google Cloud notifications to the appropriate teams across your projects, folders, and organization resources. This document outlines Essential Contacts capabilities to help you design your contact-notification strategy. To configure or modify contacts, see [Manage Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts).

Essential Contacts provides contact information that other services can access to send their specific notifications. However, the Essential Contacts service doesn't send or manage those emails itself.

With Essential Contacts, you can define a directory of custom contacts for the following specific notification categories:

  * Billing
  * Legal
  * Product updates
  * Security
  * Suspension
  * Technical



You can also define contacts to receive notifications from all of these categories at the same time.

## Notify the right people

By default, Identity and Access Management (IAM) roles manage permissions and access controls for Google Cloud resources. However, individuals assigned to these roles might not always be the best contacts for all operational notifications, especially when organizations have specialized teams for areas such as billing, legal, or security. Additionally, due to personnel and role changes, relying solely on default IAM principals for all notifications can lead to overlooking crucial alerts about your projects or folders.

Essential Contacts lets you designate custom groups or teams as points of contact for specific notification categories. We recommend configuring Essential Contacts to make sure important information about your Google Cloud resources reaches the correct teams promptly.

Essential Contacts isn't a tool for you to manually send internal emails to your teams or to configure service-specific notification integrations for individual Google Cloud products.

Individual Google Cloud products govern their own notification integrations. However, Essential Contacts serves as a central, primary contact directory that helps your teams improve responsiveness and accountability across diverse operational functions. If you don't establish and maintain Essential Contacts, you might miss critical notifications within those designated categories.

The following are some key benefits of configuring Essential Contacts:

  * **Receive targeted notifications** : Make sure that designated teams or groups receive specific messages directly, such as security alerts or billing updates.
  * **Improve reliability and prevent missed notifications** : Reduce the risk of missed notifications because of incorrect contact information.
  * **Maintain operational awareness and compliance** : Establish clear notification channels for operational, security, and compliance issues to support business continuity.
  * **Facilitate proactive management** : Control who gets notified to help you manage your organization effectively, respond to issues promptly, and plan for product changes based on critical updates.



## Notification and delivery capabilities

Essential Contacts serves solely as a central directory for your custom contacts in notification categories. If you don't configure custom contacts for a specific category, Essential Contacts provides IAM principals as fallback contacts for Google Cloud notifications. For more information about recommended contacts per category, see Notification categories. For details about default fallback contacts and routing considerations, see [Fallback contacts](https://docs.cloud.google.com/resource-manager/docs/essential-contacts-fallback-contacts).

Even when you configure custom contacts in Essential Contacts for a specific category, individual services that access this contact information might also send notifications to other principals with relevant IAM roles, depending on their communication requirements.

Essential Contacts only provides contact information that other Google Cloud services can use, but it doesn't send or manage notification emails itself. Individual services retrieve contact details for their purposes and have their independent permission mechanisms. For example, [Advisory Notifications](https://docs.cloud.google.com/advisory-notifications/docs/overview) retrieves details from Essential Contacts to display sensitive data from critical notifications within the Google Cloud console, including security and privacy information. However, you require additional roles to access Advisory Notifications.

Each Google Cloud service determines its own notification needs and specifics, including message content, sender email addresses, and delivery frequency. Not all Google Cloud products use Essential Contacts to send notifications. Individual offerings manage their own notification channels and might require service-specific opt-ins or dedicated roles. For detailed information about notifications from specific offerings, consult the documentation for each product.

To help you anticipate who to expect Google Cloud notification emails from, sender email addresses end with the `@google.com` address domain. Some notifications for Essential Contacts might include a footer similar to the following to help you identify why you received the message:

_"You are receiving this message because your administrator has designated you as an essential contact for the CATEGORY_NAME category."_

## Best practices for Essential Contacts

Follow these best practices to configure and manage your Essential Contacts effectively:

  * **Use group aliases, mailing lists, or shared email addresses** : Configure distribution lists or group email addresses like `security-team@yourcompany.com` or `gcp-billing@yourcompany.com` instead of individual email addresses to receive notifications.

This practice significantly reduces the risk of missed notifications because of personnel changes and simplifies ongoing management.

  * **Assign custom contacts for every relevant category** : Verify that proper contacts are assigned for each notification category that is important to your organization to achieve comprehensive coverage.

  * **Keep contacts up to date and verify details** : Regularly review and update contact information. Periodic review and updates help contacts remain current.

For example, you can use the Google Cloud console to validate your contacts annually. The Google Cloud console might prompt you to verify your contacts if you haven't verified them in the past year. An unvalidated contact continues to receive notifications unless their email address is invalid or they are removed from the Essential Contacts list. However, we recommend that you establish your own regular review cycle.

Google Cloud cannot automatically detect whether an individual contact's email address remains valid or monitored when personnel changes occur, because email addresses can belong to any domain. Establishing an annual or quarterly review cycle helps ensure that critical notifications continue reaching active staff and reduces email delivery bounces.

  * **Choose the right resource hierarchy level based on inheritance preferences** : You can assign contacts at the project, folder, or organization level. Contacts are inherited through the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

As a result, organization-level contacts receive notifications for the organization and all its folders and projects, while folder-level contacts receive notifications for that folder and its nested items. Where you assign contacts depends on your organization's structure.

Generally, we recommend the following structure based on organizational practices, especially for sensitive categories like Billing, Legal, and Security:

**Recommended level** | **Notification category**  
---|---  
Organization level |  The level for security contacts depends on your organization's specific security practices. Assign these at the project level if project owners manage their own project security or at the organization level if a central group manages security for all projects. However, as a general guide, we recommend the following notification categories at the organization level: 
    * Billing
    * Legal
    * Security  
Folder or project level |  Technical contacts might receive a large number of notifications. Assign these at the folder or project level to help manage the flow. As a general guide, we recommend the following notification categories at the folder or project level: 
    * Product updates
    * Security
    * Suspension
    * Technical
    * All  



## Notification categories

You can assign custom contacts to several notification categories. If you don't add a specific contact to a category, notifications in that category typically go to the _fallback contact_ , selected based on their IAM role. For a complete list of fallback contacts and default routing considerations, see [Fallback contacts](https://docs.cloud.google.com/resource-manager/docs/essential-contacts-fallback-contacts). We recommend adding custom contacts for all relevant categories.

You can add individuals as custom contacts, but we recommend using groups or teams instead. For information on best practices, see Best practices for Essential Contacts.

Review the following table to learn about notification categories, examples of notifications you might receive, and recommended recipients.

Individual Google Cloud products govern their own notification integrations. Some Google Cloud products require service-specific opt-ins for their specific notification features or integrations. These products might not use Essential Contacts for the following general notification categories or the examples provided. For more information, see the documentation for the specific product.

**Category** | **Description and importance** | **Examples of notifications** | **Recommended custom contact**  
---|---|---|---  
**Billing** | Critical billing and payment notifications regarding your Google Cloud account and services. | 

  * Price updates for services you use
  * Payment method errors or expiration warnings
  * Budget threshold alerts
  * Changes to billing accounts, invoices, and payment instruments
  * Overdue payment notifications
  * Catalog approvals

| Finance department staff. Contacts might include:  


  * Budget owners
  * Accounts payable and procurement planners
  * Other individuals who manage your financial relationship with Google Cloud

  
**Legal** | Official legal and compliance notifications. | 

  * Enforcement actions related to your services
  * Regulatory compliance updates and audits
  * Government notices or legal requests concerning your account
  * Changes to Terms of Service or other legal agreements

| 

  * Legal counsel
  * Compliance officers
  * Government relations specialists
  * Other relevant legal team members from your organization

  
**Product updates** | Information about changes to Google Cloud products, runtime platforms, and APIs. | 

  * Feature announcements and general availability updates
  * Version deprecations
  * Product terms updates
  * Deprecation notices and lifecycle transitions
  * Service migrations and architectural requirement changes

| 

  * Product managers
  * Solution architects
  * Lead engineers
  * Technical teams who need to plan for or adapt to product changes

  
**Security** | Urgent notifications regarding security and privacy issues affecting your resources or account. | 

  * Security bulletins and high-severity vulnerability advisories
  * Vulnerability alerts, including details on detected critical vulnerabilities affecting your resources
  * Data breach incidents and privacy notifications
  * Information on detected malicious attacks originating from or targeting your resources
  * Advisories on widespread threats that might require user attention
  * Abuse, cryptomining, and security incident notifications
  * Terms of Service violations
  * Notifications related to project deletion

| 

  * IT security teams
  * Security Operations Center (SOC)
  * Operations security personnel
  * Incident response teams
  * Chief Information Security Officer (CISO)

  
**Suspension** | Notifications about potential or actual account and project suspensions because of policy violations or other issues. | 

  * Apigee evaluation compliance issues or expiration
  * Copyright infringements
  * Critical abuse alerts that might lead to suspension
  * General notifications because of non-payment or Terms of Service violations

| Operations leads and other individuals or teams immediately responsible for IT infrastructure and business application uptime.  
**Technical** | Operational issues, technical events, and important updates relevant to the stability and functioning of your services. Receiving notifications for specific infrastructure or host-level errors depends on the originating Google Cloud services and might require enrollment in their product-specific premium support programs. | 

  * Logging configuration errors
  * Data loss prevention updates
  * Upcoming maintenance and zone disruptions
  * Service disruptions, outages, or degradations
  * Updates regarding SLO breaches
  * Actions on Google status
  * Abuse notifications

| 

  * IT operations staff
  * Site Reliability Engineers (SREs)
  * System administrators
  * On-call engineers
  * Technical support teams

  
**All** | All notifications from each of the categories listed earlier.  
  
_(It is a superset.)_ | Contacts in this category receive notifications from all of the following categories:  


  * Billing
  * Legal
  * Product updates
  * Security
  * Suspension
  * Technical

| Automated systems, such as ticketing or logging, and central operations teams.  
  
For example, you can use it for comprehensive logging or routing by automated systems for a potentially large number of notifications.   
  
## Supported languages

In Essential Contacts, each contact has a preferred language setting. Notification creators can reference this setting when sending notifications.

When you add a contact in the Google Cloud console, the Google Cloud console automatically configures the contact's preferred language based on the contact creator's [preferred language settings](https://console.cloud.google.com/user-preferences/languages).

When you add a contact using the API, you manually configure the contact's preferred language using a language code. This language code can refer to any of the languages that Essential Contacts supports.

If a notification isn't available in the contact's preferred language, the system sends it in English.

####  Supported languages 

Language | Language code  
---|---  
Afrikaans | af  
Albanian | sq  
Amharic | am  
Arabic | ar  
Arabic (Egyptian) | ar-EG  
Armenian | hy  
Azerbaijani | az  
Basque | eu  
Belarusian | be  
Bengali | bn  
Bosnian | bs  
Bulgarian | bg  
Burmese | my  
Catalan | ca  
Chinese | zh  
Chinese (Hong Kong) | zh-HK  
Chinese (Taiwan) | zh-TW  
Croatian | hr  
Czech | cs  
Danish | da  
Dutch | nl  
English | en  
English (Australia) | en-AU  
English (UK) | en-GB  
English (US) | en-US  
Estonian | et  
Filipino | fil  
Finnish | fi  
French | fr  
French (Canada) | fr-CA  
Galician | gl  
German | de  
Gerogian | ka  
Greek | el  
Gujarati | gu  
Hebrew | iw  
Hindi | hi  
Hungarian | hu  
Icelandic | is  
Indonesian | id  
Irish | ga  
Italian | it  
Japanese | ja  
Javanese | jv  
Kannada | kn  
Kazakh | kk  
Khmer | km  
Korean | ko  
Kyrgyz | ky  
Lao | lo  
Latvian | lv  
Lithuanian | lt  
Macedonian | mk  
Malay | ms  
Malayalam | ml  
Marathi | mr  
Mongolian | mn  
Nepali | ne  
Norwegian | no  
Pashto | ps  
Persian | fa  
Polish | pl  
Portuguese | pt  
Portuguese (Brazil) | pt-BR  
Portuguese (Portugal) | pt-PT  
Punjabi | pa  
Romanian | ro  
Russian | ru  
Serbian | sr  
Sindhi | sd  
Sinhala | si  
Slovak | sk  
Slovenian | sl  
Somali | so  
Spanish | es  
Spanish (Latin America) | es-419  
Swahili | sw  
Swedish | sv  
Tamil | ta  
Telugu | te  
Thai | th  
Turkish | tr  
Turkmen | tk  
Ukranian | uk  
Urdu | ur  
Uzbek | uz  
Vietnamese | vi  
Welsh | cy  
Zulu | zu  
  
## Service limitations

The following limitations apply when configuring Essential Contacts:

  * **Email delivery:** Essential Contacts serves as a contact directory and doesn't send or manage emails itself. You can't use it to manually send internal emails to your teams.
  * **Product integration:** Not all Google Cloud products use Essential Contacts to send notifications. Some products govern their own integrations and might require service-specific opt-ins.
  * **Language support:** If a notification isn't available in a contact's preferred language, the system sends it in English.
  * **Email address limits:** The following email length limits apply: 
    * **Total length:** A maximum of 254 characters applies to both the Google Cloud console and API.
    * **Domain and subdomains:** A maximum of 63 characters for any subdomain and label, excluding the `@` and `.` characters, applies to both the Google Cloud console and API.
    * **Local part in the Google Cloud console:** A maximum of 64 characters. If you exceed this, you receive a `Please enter a valid email address` error.
    * **Local part in the API:** When using the API, such as with the Google Cloud CLI or REST API, the local part can be up to the 254-character limit. If you exceed the API limit, you receive a `400 / INVALID_ARGUMENT: Request contains an invalid argument.` error.



## What's next

  * [Manage Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts).
  * [Review the fallback contacts reference](https://docs.cloud.google.com/resource-manager/docs/essential-contacts-fallback-contacts).
  * [Create custom constraints for Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/essentialcontacts-custom-org-policies).
  * Learn how to [associate a domain with a project](https://docs.cloud.google.com/resource-manager/docs/managing-notifications#associate-domain) for verification purposes.
  * Understand how to [manage notification preferences](https://docs.cloud.google.com/resource-manager/docs/managing-notifications#manage-preferences).
  * Learn about [Advisory Notifications](https://docs.cloud.google.com/advisory-notifications/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
