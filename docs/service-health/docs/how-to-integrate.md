---
url: https://docs.cloud.google.com/service-health/docs/how-to-integrate/
title: Integrate with Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:02.930579+00:00
---

# Integrate with Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/how-to-integrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Integrate with Personalized Service Health Stay organized with collections  Save and categorize content based on your preferences. 

Though service disruptions are inevitable, transparent and early communication is essential to evaluate what is happening, keep your stakeholders informed, and execute actions to minimize impact to your business.

Operating a reliable cloud application is a shared responsibility between Google Cloud and application developers. When a service disruption happens, Google Cloud aims to communicate the incident quickly and provide an impact assessment. You must evaluate how to receive notifications, act on emerging incidents, and manage the impact to your application.

Personalized Service Health can help with this process. You can integrate with it in various ways to learn of emerging incidents, evaluate the impact to your applications, and receive updates from Google Cloud. This document provides an overview of how to receive signals of service disruptions from Google Cloud, including recommendations on integrating with them.

## Decide where to integrate

Personalized Service Health provides a personalized view of Google Cloud products used by your projects or across your organization. We recommend integrating with Personalized Service Health to give you the most coverage and range of integration options.

**Integration point** | **Use case** | **Benefits** | **Dependencies**  
---|---|---|---  
Console dashboard (Personalized Service Health)  | View active disruptions  | Personalized to your projects, available by default  | Identity and Access Management (IAM)  
Google Cloud console   
Alerts (Personalized Service Health)  | Proactive notifications  | Personalized to your projects, convenient, and proactive  | IAM  
Cloud Logging  
Cloud Monitoring   
API (Personalized Service Health)  | Integrate with another system or tool  | Personalized to your projects or organization  | IAM   
  
## Choose method of interaction with Personalized Service Health

You must consider Personalized Service Health in the context of your intended operations, monitoring, and incident response model. By evaluating how your teams use signals during and leading up to incidents, you can decide how you want to use Personalized Service Health.

The following table shows how you might interact with Personalized Service Health, depending on how it's set up.

**Example scenario in your organization** | **Integration with Personalized Service Health** | **Example tools you may be integrating with**  
---|---|---  
Developers who are oncall for a few applications  | Individual project alerts Console dashboard | [Google Cloud Observability](https://cloud.google.com/products/operations/), PagerDuty   
Centralized incident response across an organization  | API integration with existing system using the OrganizationEvents API ([v1](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationEvents), [v1beta](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/organizations.locations.organizationEvents))  | PagerDuty, custom dashboards   
Internal platform to manage cloud resources and operations  | Service Health API   
Individual project alerts   
Service Health API integration with an internal developer platform  | Backstage, Terraform   
Many programmatically configured and managed projects (Example: 1,000+)  | Service Health API  
Automated API-based notifications  | Backstage, Terraform, PagerDuty   
  
## Use Personalized Service Health during an incident

Once you've integrated with Personalized Service Health and start getting alert notifications, Personalized Service Health provides information about Google Cloud disruptions that can help you manage their impact.

### Detect and scope out the incident

Questions you might ask at this stage include:

  * Is it a real problem?
  * Can you validate the impact?
  * What are the symptoms?
  * Which users, products, or portions of the business are affected? What geographies?



Personalized Service Health helps you understand if the issue originates from your project or Google, so you can implement the appropriate incident response. It lets you find and view event information so you can monitor the event, impacted products, and locations that affect your project.

Here are steps you might take:

  1. Review the alert, if you have it set up. 
     * What caused this alert to fire?
     * How do these alerts fit in with all your other potentially product-specific alerts?
  2. Access the Service Health dashboard for your project or organization. You can view events, impacted products, and locations at a glance, and answer the following questions: 
     * Which of your projects are affected?
     * Which products your project depends on are affected?
     * Is the event affecting specific resources within those locations?
  3. Review the events and understand their scope, impact, and relevance to your project.
  4. Identify an event that looks connected to the issue you're seeing.
  5. Find verification steps, mitigation (if available), and expected resolution time for the event.



Personalized Service Health helps you review the current state and impact of incidents affecting your project or organization, so you can efficiently manage and respond to them. For example, you can prioritize effectively by accurately identifying the highest priority incident.

### Mitigate, resolve, or escalate the incident

Questions you might ask at this stage include:

  * How can you work around the incident?
  * Can you fix it directly?
  * Should you initiate a failover now, or wait longer?
  * Who should you notify to get it fixed?



Personalized Service Health helps you understand an incident's impact on your projects and resources, be informed of available workarounds, and receive updates on the estimated resolution time.

#### Monitor progress toward incident resolution

The event overview in the Service Health dashboard identifies key information such as symptoms and workarounds, which are necessary for mitigation and shows when the state changes. These details let you:

  * Monitor a running summary of potential impact as the situation evolves.
  * Stay updated on any new developments and the expected time of the next communication or update.
  * See when a symptom is published.
  * See when a workaround is identified.
  * See when the state changes to **Resolved**.



You can take the following actions while you monitor progress:

  * Review workarounds, if available.
  * Implement the incident response appropriate for your project or organization.
  * Continue to monitor the event until it is mitigated or resolved.



#### When to contact Support

Google is aware of events that appear in the Service Health dashboard. To know what Google is doing about an event, select it to see the details.

If an issue doesn't appear to be represented in any of the events in the dashboard, contact Support.

### Use Personalized Service Health with other sources of incident information

Regardless of your company setup, use Personalized Service Health as an additional signal when evaluating the impact of incidents. Make sure you can review multiple sources of incident information so you can decide on next steps based on data and evidence.

Reasons to use multiple sources of incident information include:

  * A Google Cloud product might be undergoing an incident in some location, but your projects may not be affected because they are in a different location.
  * If your serving system has two complete replicas in separate zones and a critical Google Cloud product in one zone fails, Personalized Service Health will inform you of that failure. However, your users may not actually be affected and you may not need to take immediate action.
  * If your project depends on many Google Cloud products within a location, Personalized Service Health won't know: 
    * If your project requires all of the products to be functional.
    * If your project will continue to work in case one product fails.
    * If your entire application is affected if one or more of the products fail.
  * Personalized Service Health itself can also be degraded or undergo failure. To verify, you can [check its status](https://docs.cloud.google.com/service-health/docs/service-health-disruption).



You will need to interpret signals from Personalized Service Health as appropriate to your setup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
