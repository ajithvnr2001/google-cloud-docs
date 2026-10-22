---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:23.135344+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The PagerDuty connector for Gemini Enterprise lets you perform insert, delete, update, and read operations on PagerDuty datasets.

## Supported actions

When the PagerDuty connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create incident | Create an incident synchronously without a corresponding event from a monitoring service.  
Update incident | Acknowledge, resolve, escalate, or reassign an incident.  
Add note to incident | Add a note to an incident's timeline.  
Create service | Create a new service.  
Update service | Update an existing service.  
Create user | Create a new user account in PagerDuty.  
Update user | Update an existing user's details.  
Create on-call override | Create an override for a specific user covering a specified time range on a schedule.  
Search | Search for incidents, services, users, schedules, and escalation policies.  
List on-call entries | List the on-call entries during a given time range.  
List log entries | Get the full timeline of an incident.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search using the PagerDuty data store, you need to enable the following scopes:

Scope | Purpose  
---|---  
read | Grants read access to PagerDuty resources like incidents, services, and users.  
write | Grants write access to PagerDuty resources, allowing creation and modification of incidents, services, and users.  
  
For information on how to configure these scopes, see [Set redirect URL and scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty/pagerduty-configuration#set-redirect-url-and-scopes).

## Limitations

This section outlines known issues and limitations that can affect your use of the PagerDuty data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing PagerDuty data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The PagerDuty data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a connector with PagerDuty, see [Set up a PagerDuty data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
