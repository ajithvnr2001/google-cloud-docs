---
url: https://docs.cloud.google.com/support/docs/best-practices/
title: Best practices for working with Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:03.726597+00:00
---

# Best practices for working with Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/best-practices/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Best practices for working with Customer Care Stay organized with collections  Save and categorize content based on your preferences. 

Following support case best practices helps you resolve technical issues faster when working with Customer Care. By including clear timestamps, project identifiers, and diagnostic details, you give support engineers the context needed to investigate your case right away.

## Creating a support case

Before you create a support case, [review known issues](https://docs.cloud.google.com/support/docs/customer-care-procedures#view_known_issues) to see if a case has already been filed.

To avoid confusion and so that we can track your request in a single point, create one support case per issue. Any duplicate cases that are created are closed.

## Describing your issue

Writing a detailed support case makes it easier for the Customer Care team to respond to you quickly and efficiently. When your support case is missing critical details, we need to ask for more information, which takes additional time.

The best support cases are both detailed and specific. They tell us what happened and what you expected to happen. When you describe your issue in your support case, include the following details:

  * **Time:** The specific timestamp when the issue began.
  * **Product:** The products and features associated with the issue.
  * **Location:** The zones where you're seeing the issue.
  * **Identifiers:** The project ID or the application ID and other concrete identifiers that help us research the issue.
  * **Useful artifacts:** Any details you can provide to help us diagnose the issue.
  * **Problem type:** Is the problem intermittent, transient, or consistent.



The following sections describe these concepts in greater detail.

### Time

Using the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format for the date and timestamp, tell us when you first noticed this issue and how long it lasted.

Examples:

  * Starting at 2017-09-08T15:13:06+00:00 and ending 5 minutes later, we observed...
  * Observed intermittently, starting no earlier than 2017-09-10 and observed 2-5 times...
  * Ongoing since 2017-09-08T15:13:06+00:00...
  * From 2017-09-08T15:13:06+00:00 to 2017-09-08T15:18:16+00:00...



The Customer Care specialist resolving the issue is very likely not in your time zone, so relative statements like the following make the problem harder to diagnose:

  * "This started sometime yesterday..." (Forces us to infer the implied date.)
  * "We noticed the issue on 9/8..." (Ambiguous, as some might interpret this date as September 8, and others might interpret it as August 9.)



### Product

Although the basic case form asks you to specify a product name, we need specific information about which _feature_ in that product is having the issue. Ideally, your report will refer to specific APIs or Google Cloud console URLs (or screenshots). For APIs, you can link to the documentation page, which contains the product name in the URL.

Also tell us about the mechanism that you're using to initiate the request (for example, REST API, Google Cloud CLI, Google Cloud console, or perhaps a tool like Cloud Deployment Manager. If multiple products are involved, give us each name specifically.

Examples:

  * "Compute Engine REST API returned the following errors..."
  * "The BigQuery query interface in console.cloud.google.com is hanging..."



The following statements are not specific enough to know where to look when diagnosing the issue:

  * "Can't create instances..." (We need to know the method you are using to create instances.)
  * "The `gcloud compute create instances` command is giving an error..."(The command syntax is incorrect, so we can't run it ourselves to reproduce the error. Also, we don't know which error you actually saw.)



### Location

We need to know your data center region and zone because we often deploy changes to one region or zone at a time. The region and zone are a proxy for the version number of the underlying software. This information helps us to know if breaking changes in a particular version of our software are affecting your systems.

Examples:

  * "In us-east1-b ..."
  * "I tried regions us-east1 and us-central1..."



### Identifiers

Specific identifiers help us identify which of your Cloud projects is experiencing the issue. We always need to know the alphanumeric project or application ID. _Project names are not helpful._ If the issue is affecting multiple projects, include every affected ID.

In addition to project or application IDs, several other identifiers help us diagnose your case:

  * Instance IDs.
  * BigQuery job IDs or table names.
  * IP addresses.



When specifying an IP address, also tell us the context in which it is used. For example, specify if the IP is connected to a Compute instance, a load balancer, a custom route, or an API endpoint. Also tell us if the IP address is not related to Google's systems (for example, if the IP address is for your home internet, a VPN endpoint, or an external monitoring system).

Examples:

  * "In project robot-name-165473 or my-project-id..."
  * "Across multiple projects (including my-project-id)..."
  * "Connecting to Google Cloud external IP 218.239.8.9 from our corporate gateway 56.56.56.56..."



General statements like the following are too general to help diagnose the issue:

  * "One of our instances is unreachable..."
  * "We can't connect from the internet..."



### Useful artifacts

Providing us with artifacts related to the issue will speed up troubleshooting by helping us see exactly what you are seeing.

For example:

  * Use a screenshot to show exactly what you see.
  * For web-based interfaces, provide any relevant [browser trace information](https://docs.cloud.google.com/support/docs/capture-browser-trace).
  * Attach tcpdump output, logs snippets, example stack traces.

**Note:** We recommend uploading file attachments in formats that are widely supported and non-proprietary, such as PNG, TXT, or PDF.

### Problem type

  * **Intermittent** : Intermittent problems occur randomly with no regular patterns of failure. Intermittent problems are difficult to troubleshoot because their irregularity makes it hard to gather data during the failure. In this case, you should try to identify bottlenecks in architecture and check whether your resources are hitting their maximum threshold usages. You can also run frequent checks in a scheduled job using automation, and if the check fails, collect debug information during the failure. Examples of this type of failure are DNS resolution failures and packet loss.

  * **Transient** : Transient problems are momentary or exist only for a short period of time. If you have problems that happen only for a second or a few microseconds, you can check for micro bursts of traffic or resource peak utilizations. In most cases, transient problems can be ignored if they don't recur often and if your service is designed to be tolerant of transient failures. Examples of this type of failure are network latency spikes that occur only for a few microseconds, and small packet losses that cause timeouts. The Transmission Control Protocol (TCP) is designed for failures such as small packet loss and latency spikes, and it can handle these problems effectively, unless your application is sensitive to latency.

  * **Consistent** : Consistent problems are problems that fail completely, such as when your website is down. Consistent problems are relatively straightforward to troubleshoot because they can be reproduced. In this case, tell us the steps to reproduce the problem so that our Customer Care specialists can replicate the environment and troubleshoot the problem for you.




### Example descriptions

The following examples provide detailed descriptions for support cases.

#### Example one
    
    
    JobName:
    
    A_ATL_BIG1toBQ_big_04)201704202
    
    00045_491
    
    Source:
    
    S3_avl-transfer
    
    Destination:
    
    CloudStorage: avl-transfer
    
    Start time (ISO 8601 format): 2017-04-20 20:14:43 PDT
    
    End time (ISO 8601 format): 2017-04-21 at 10:03:44 PDT
    
    I started a file transfer at 2017-04-20 at 20:14:43 PDT using the transfer API.
    This job normally takes 10 minutes to complete, but in this case the job was
    still running when I canceled it the next day (2017-04-21 at 10:03:44 PDT). This
    is not an isolated event; several other jobs involving the transfer API had
    intermittent, significant delays.
    
    Please investigate the cause of the delays and advise of any best practices that
    we can implement to prevent these issues in the future.
    

#### Example two
    
    
    Start time (ISO 8601 format): 2017-05-12 at 11:03:43
    
    End time (ISO 8601 format): The issue is still happening as of the time of this
    report.
    
    Issue summary:
    
    `/cron/payments-service/sync-v2-batch` cron using the App Engine Task Queue API
    has stopped running since 2017-05-12 at 11:03:43. We rely on this job to handle
    payments correctly.
    
    We saw datastore and queue errors and then the cron stopped running. We
    attempted unsuccessfully to fix the issue by re-uploading cron.xml. Here is the
    error trace:
    
    `[error trace]`
    
    Please advise if the issue is with the API or our implementation and let us
    know next steps.
    

## Setting the priority and escalating

Priority helps us understand the impact this issue is having on your business, and affects how quickly we respond to resolve the issue. Priorities are defined in the following table. You can find more information at [Support case priority](https://docs.cloud.google.com/support/docs/customer-care-procedures#support_case_priority).

Priority Definition | Example Situation  
---|---  
**P1: Critical Impact—Service Unusable in Production** | The application or infrastructure is unusable in production, having a significant rate of user-facing errors. Business impact is critical (revenue loss, potential data integrity issue, etc.).  
**P2: High Impact—Service Use Severely Impaired** | The infrastructure is degraded in production, having a noticeable rate of user-facing errors or difficulties in spinning up a new production system. Business impact is moderate (danger of revenue loss, productivity decrease, etc.).  
**P3: Medium Impact—Service Use Partially Impaired** | The issue is limited in scope and/or severity. The issue has no user-visible impact. Business impact is low (for example, inconvenience, or minor business processes affected).  
**P4: Low Impact—Service Fully Usable** | Little to no business or technical impact. Recommended for consultative tickets where in-depth analysis, troubleshooting or consultancy are preferred to more frequent communications.  
  
### When to set the highest priority

If you have an issue that is affecting business critical services and needs immediate attention from Google, choose "P1" as the priority. Explain to us in detail why you selected P1. Include a brief description of the impact this issue is having on your business. For example, you might consider a problem with a dev version to be P1, even if no end users are directly impacted, if it is blocking a critical security fix.

When a case is set as P1, an expert is immediately alerted to exclusively work on the issue. You receive a quick initial response to join a live troubleshooting call through Google Meet. If your organization can't use Google Meet, include a link to your video conferencing software of choice for the expert to join. After that, you receive regular updates through the case.

We appreciate detailed comments supporting the chosen prioritization level because it helps us respond appropriately.

### What to expect from support on P1 cases

  * **New P1 case**

    * A support expert will engage with you through Google Meet or any other bridge that you provide. We expect that you join the call within 15-30 minutes. Inform the support expert if you can't join the call for any reason.
    * The case "follows the sun" by default. This means that the support experts engage 24 hours a day until the case is mitigated or deprioritized. If case mitigation is best pursued in a specific region, that case can be locked to a certain time zone. You can tell us your preference to this effect.
  * **P1 priority increase**

    * If the issue has started impacting your production environment, or is about to, you may increase the priority of an existing P2 - P4 case to P1.
    * When you increase the priority of an existing case to P1, the support case may be reassigned to allow an available support expert to provide immediate attention.
  * **Non-production impact**

To ensure that appropriate resources are allocated where needed, support may engage with you to reevaluate cases marked as P1 that are not impacting production or causing high business impact.




### Response times

Issue priority levels have predefined response times defined in the [Google Cloud Platform Technical Support Services Guidelines](https://cloud.google.com/terms/tssg/). If you need a response by a specific time, let us know in your report description. If a P1 issue needs to be handled around the clock, you can [request follow-the-sun service](https://docs.cloud.google.com/support/docs/customer-care-procedures#request_follow-the-sun_service). These cases are re-assigned several times per day to an active Customer Care specialist. While we troubleshoot your P1 case, we recommend that you remain engaged to answer questions until resolution to facilitate efficient communication. If you become unresponsive for more than 3 hours, we might reduce the priority of the case to a P2 until you re-engage.

### Escalating

When circumstances change, you might need to escalate an issue. Good reasons for escalation are:

  * Increase in business impact.
  * Breakdown of the resolution process. For example, you haven't received an update in the agreed upon amount of time or your issue is "stuck" without progress after exchanging several messages.



When you're experiencing a high-impact issue, the best solution is to set the case to the appropriate priority for an adequate amount of time, rather than escalating. Escalating doesn't necessarily resolve the case any faster and escalating shortly after priority change might even cause the case resolution to be slower. You can find a more detailed explanation in the [When should you escalate](https://youtu.be/tUBHqx7F2U0) video.

For more information, see [Escalate a case](https://docs.cloud.google.com/support/docs/customer-care-procedures#escalate_case).

## Route cases to the required time zone

Because of the factors on which [Customer Care availability](https://docs.cloud.google.com/support/docs/language-working-hours#availability) is based, your support case might be assigned to a Customer Care specialist who works outside your hours of operation. It's also possible that you would want to engage with Customer Care during the business days of a specific time zone. In such cases, we recommend that you request Customer Care to route your support case to a time zone that is convenient for your case. You can add this request in your case description or response. For example, `Please route this case to the Pacific time zone (GMT-8)`. P1 cases are handed down to the next region Customer Care because it [follows the sun](https://docs.cloud.google.com/support/docs/customer-care-procedures#request_follow-the-sun_service) while other cases would stay with the current case owner to continue working on the case the next day.

## Provide feedback with CES survey

When a case is resolved, a Customer Effort Score (CES) survey regarding your opinion on how the process went would be sent over email. We would really appreciate it if you can take a few minutes to fill it out, so we would know what we did well and what were the challenges in order to improve these aspects.

Every feedback form is manually reviewed by the Customer Experience team and results in corresponding actions to improve your future experience. The score will be out of 5. A score of 3 or lower would be considered difficult from the customer side. On the other side, a score 4 or more means the interaction was not difficult for the customer and considered as a positive experience.

For more information, watch the [How to Submit Google Cloud Services Feedback with CES](https://www.youtube.com/watch?v=t5lI-vlgbeQ&t=2s) video.

## Long-running or difficult issues

Issues that take a long time to resolve can become confusing and stale. The best way to prevent this is to collect information using our [Long-running issue template](https://services.google.com/fh/files/misc/long_running_issue_template.pdf) with the latest state summarized at the top.

To use the template, open the preceding link and make a copy. Include links to all relevant cases and internal tracking bugs. Share this document with your account team's group and ask them to share it with specific Customer Care specialists.

This document includes:

  * A summary of the current state summarized at the top.
  * A list of the hypotheses that are potentially true.
  * The tests or tools that you intend to use to test each hypothesis.



Try to keep each case focused on a single issue, and avoid reopening a case to bring up a new issue.

## Reporting a production outage

If the issue has caused your application to stop serving traffic to users, or has similar business-critical impact, this might be a production outage. We want to know as soon as possible. Issues that block a small number of developers, by contrast, are not what we think of as production outages.

When we get a report of a production outage, we quickly triage the situation by:

  * Immediately checking for known issues affecting Google Cloud infrastructure.
  * Confirming the nature of the issue.
  * Establishing communication channels.



You can expect a response with a brief message, which contains:

  * Any related known issues affecting multiple customers.
  * An acknowledgement that we can observe the issue you've reported, or a request for more details.
  * How we intend to communicate.



Therefore, it's important to quickly create a case including time, product, identifiers, and location, and then start deeper troubleshooting. Your organization might have a defined incident management process and this step should be executed very near the beginning of it.

Google's incident management process defines a key role: the incident commander. This person gets the right people involved, continually collects the latest status, and periodically summarizes the state of the issue. They delegate to others to troubleshoot and apply changes. This delegation allows us to investigate multiple hypotheses in parallel. We recommend that you establish a similar process within your organization. The person who opened the case is usually the best choice to be the incident commander because they have the most context.

## Reporting a networking issue

The size and complexity of Google's network can make it difficult to identify which team owns the problem. To diagnose networking issues, we need to identify very specific root causes. Because networking error messages are often general (like, "Can't connect to server"), we need to gather detailed diagnostic information to narrow down the possible hypotheses.

Packet flow diagrams provide an excellent structure for the issue report. These diagrams describe the important hops that a packet takes along a path from source to destination, along with any significant transformations along the way.

Start by identifying the affected network endpoints by Internet IP address or by [RFC 1918](https://tools.ietf.org/html/rfc1918) private address plus an identifier for the network. For example, 2.3.4.5 or 10.2.3.4 on the Compute Engine project's default network.

Note anything meaningful about the endpoints, such as:

  * Who controls them.
  * Whether they are associated with a DNS hostname.
  * Any intermediate encapsulation or indirection, or both such as VPN tunneling, proxies, and NAT gateways.
  * Any intermediate filtering, like firewalls or CDN or WAF.



Many problems that manifest as high latency or intermittent packet loss will require a path analysis or a packet capture, or both for diagnosis.

  * **Path analysis** is a list of all hops that packets traverse and is familiar as "traceroute". We often use [MTR](https://en.wikipedia.org/wiki/MTR_\(software\)) or tcptraceroute, or both because they have better diagnostic power. We recommend becoming familiar with these tools.
  * **Packet capture** (also known as "pcap," from the name of the library "libpcap") is an observation of real network traffic. It's important to take a packet capture for both endpoints, at the same time, which can be tricky. It's a good idea to practice with the necessary tools (for example, [tcpdump](https://en.wikipedia.org/wiki/Tcpdump) or [Wireshark](https://en.wikipedia.org/wiki/Wireshark)) and make sure they are installed before you need them.



## Reporting a Google Cloud console issue

When reporting an issue with the web-based Google Cloud console, in addition to the preceding guidance, provide the following information to help us narrow down potential issue causes:

  * URLs of impacted console pages
  * IDs of impacted projects
  * Number of impacted users
  * Whether the issue occurs across different machines
  * Impacted browsers
  * Any browser extensions or firewall systems in use



Additionally, including any relevant [browser trace information](https://docs.cloud.google.com/support/docs/capture-browser-trace) helps us understand and investigate your issue.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
