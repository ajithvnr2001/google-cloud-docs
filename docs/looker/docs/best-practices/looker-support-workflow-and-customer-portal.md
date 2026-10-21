---
url: https://docs.cloud.google.com/looker/docs/best-practices/looker-support-workflow-and-customer-portal/
title: The legacy Looker customer portal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:08:00.768086+00:00
---

# The legacy Looker customer portal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/looker-support-workflow-and-customer-portal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  The legacy Looker customer portal Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Starting on October 26, 2023, case creation in the Looker customer portal will be available only for customers using Legacy Looker support. (Historical cases will still be available in view-only mode on the **Requests** page.)

Use the [Google Cloud console](https://console.cloud.google.com/) to create new support requests.

The customer portal is a feature of the [Legacy Help Center](https://help.looker.com), which allows customers to track support requests that are filed with Looker Support in one central location. Access the portal by clicking **Sign in** on the Legacy Help Center main page and then clicking **Support requests** under the user profile menu: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-dcl-workflow-2210.png)

From the portal, customers can search for tickets and view chat transcripts, ticket responses, and ticket details. The **My requests** page displays a search bar and links to support requests in a table with the following information: 

  * **Subject** — Displays each support request with a link to the issue 
  * **Id** — Displays the unique Id of the support request 
  * **Created** — Displays the days since the support request was created 
  * **Last Activity** — Displays the days since the last activity 
  * **Status** — Displays the status of the support request 



![](https://docs.cloud.google.com/static/looker/docs/images/hc-dcl-workflow-2-2210.png)

> While all customers can view their own support requests and tickets that they are copied on, _only[Looker technical contacts](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#technical_contacts) who have requested org-level access can view tickets for their entire organization._ Open a [support request](https://help.looker.com) or reach out to your success team to request this access. 

Looker users with the [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role can also request org-level access to the portal by opening a [support request](https://help.looker.com/hc/en-us/requests/new?ticket_form_id=34884). The request must include approval from a technical contact at their organization. 

## Looker Support workflow

The following sections provide more information about Looker Support's ticket process and workflow, including status labels, priority, and the implications of both. 

### Priority

Looker Support prioritizes tickets according to the following classifications: 

  * **S1-Urgent** — A complete loss of application functionality has occurred, causing a critical impact on business operations. 
  * **S2-High** — Looker services are operational but degraded, causing a significant impact on business operations. 
  * **S3-Tolerable** — Looker services are usable, the affected functions or components are non-critical, and most operations are unaffected. 
  * **S4-Question** — This includes general questions, requests for documentation, or other non-critical, system-related issues. Operations are not affected. 



Priority is subject to reclassification based on the evolution of an issue, as well as its impact. Ticket priority is updated in accordance with the **current** state of impact. 

The [Looker Technical Support Services Guidelines](https://cloud.google.com/terms/looker/support) provide more information on priority classifications and corresponding service level agreements (SLAs). 

### Status labels

Looker Support uses status labels to track the team or individual who is responsible for the next steps. The statuses and their business impacts are as follows: 

  * **Open** — The initial request has either just been opened or is still ongoing (if received through chat), or the requester has recently responded to the ticket and Looker Support is actively investigating or responding. 
  * **Awaiting your reply** — Looker Support has reached out to or responded to the requester and is waiting for a response before proceeding with next steps. 
  * **On hold** — Progression of the ticket is contingent on an internal team or process. Examples include: 
    * Looker Support is attempting to reproduce a reported bug or investigate a workaround. 
    * Looker Support is liaising with an Engineering team with regard to a bug. 
    * Looker Support has determined that the request is best served by the Account team and is waiting for the Account team to make contact with the requester before closing the ticket. 

> _**On hold** does not imply that an issue is not being investigated; it means that Looker Support is holding for completion of an action on their side._

  * **Solved** — Ideally, this occurs when the requester and support agent agree that the issue is resolved. However, there are several additional circumstances in which a ticket may be marked as **Solved** : 
    * Looker Support has reported a bug to the Looker Engineering team, and the requester and support agent have communicated and aligned on the priority and estimated resolution timeline. 
    * The ticket has been "merged" into another support request. When this occurs, Looker Support determines that two or more tickets span the same issue with the same customer or represent one chat that may have been disrupted and split into multiple support tickets. Although Looker Support merges the impacted tickets into one, the tickets remain separate on the customer portal; the merged tickets will be labeled **Solved**. 
    * The requester has not responded to the ticket for a period of time and has received at least one additional alert from the support agent (the period of time and the number of alerts from the agent may vary, depending on the severity of the issue). Although the ticket is marked **Solved** , the issue can be reopened by the requester as needed. See the next section for more information about reopening closed Looker Support support requests. 



## Reopening support requests

If a requester believes that an issue that was marked **Solved** was left unresolved or was not sufficiently resolved, or if a requester was unable to engage with the support agent during the troubleshooting process and was unresponsive, the issue can be reopened. A response on the ticket thread, either through the customer portal or email, will automatically reopen a closed support request. Customers can also initiate a new chat session to reopen a support request. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
