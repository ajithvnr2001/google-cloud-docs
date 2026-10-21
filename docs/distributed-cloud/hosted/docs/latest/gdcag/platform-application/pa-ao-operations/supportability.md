---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/supportability/
title: Supportability \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:37:13.830743+00:00
---

# Supportability  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/supportability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Supportability Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to manage your platform's health, engage with your Support team, and understand errors so you can effectively troubleshoot information to resolve issues. You must set up a resilient support process for your Google Distributed Cloud (GDC) air-gapped organization to streamline issue resolution.

The following information is for IT administrators within the platform administrator group and developer operations members (DevOps) within the application operator group, who are responsible for managing the operations of the GDC air-gapped platform for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Access software notifications

Check the following tools for notifications of when an issue appears in the software components of your platform:

  * **The common software dashboard:** For notifications about system health information, such as GKE Enterprise components, clusters, services, and VMs.
  * **Your mailbox:** For email notifications that include basic information about the problem, such as error codes.



Click a notification to view the problematic component page and access the relevant logs.

## Configure notifications recipients

Configure the following communication channels to receive alerts, even if they are disconnected from the dashboard:

  * SMS messages
  * Email notifications
  * PagerDuty



Organize the type of notification and recipient role, such as billing, software, and hardware.

## Understand software errors

Follow these practices to access relevant information about errors on software components, resolve the issue, and engage with Support effectively:

  * Find the error code of each error.
  * Use error codes to search the local and online documentation.
  * The user interface provides snippets of information regarding particular errors. Hold the pointer over an error code to view the snippets.



## Sanitize software troubleshooting information from sensitive data

Sanitize troubleshooting information for the software components, including configurations, logs, status, and metrics of all sensitive data, and comply with sovereignty requirements.

Google Distributed Cloud (GDC) air-gapped provides a list of default sensitive keywords to obfuscate and remove. Follow these steps to sanitize troubleshooting information:

  1. Customize the default list by adding and removing custom keywords.
  2. Receive a report of all the obfuscated occurrences.
  3. Receive warnings of potential remaining sensitive information.



Critical items to obfuscate include:

  * Fully Qualified Domain Names (FQDNs)
  * IP addresses
  * Usernames
  * Hostnames
  * Workload names
  * Hashes
  * Certificates
  * Customer names



## Create a software system snapshot

Create a snapshot of your software components to pack all the information necessary to troubleshoot the issue and engage with Support effectively:

  1. Select the components to include.
  2. Generate a tar file with all the required configurations, logs, status, and metrics.
  3. Specify the component to debug.
  4. Specify how to sanitize the data.



## Share information with Support

Google provides level 1 (L1) and level 2 (L2) support for GDC. For more information on how you can share information with your Support teams and infrastructure operator group, see [Request support](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/request-support).

## Enforce policies on snapshot sharing

Follow these practices to ensure that the snapshot data you share with Support is secure, protected, and subject to data retention policies you control:

  * Define and enforce access control policies to the snapshot.
  * Define and enforce data retention policies for the snapshot.
  * Set up a secure channel to upload the snapshot to the Support portal.



## Access hardware notifications

Check notifications of when an issue appears in the hardware components of your platform. Notifications appear in System Manager with system health information of hardware components such as racks, servers, switches, and storage.

You can receive email notifications too. They include basic information about the problem, such as error codes. Click the notification to view the problematic component page and access the relevant logs.

## Request capacity upgrades

Monitor, forecast, and request additional hardware capacity to ensure the health and scalability of your workloads.

## Process the system snapshot

Before you process the system snapshot, ensure you have the following requirements:

  * The snapshot tool has a connection to a running cluster.
  * You have the following necessary permissions to read the configuration and logs on the cluster: 
    * Application Operators have administrative capabilities.
    * Platform Administrators have access permissions restricted to assigned information.



To process the system snapshot, select the components of the system to snapshot. The tool connects to your cluster to pull information for each selected component. Following the data retrieval, the data goes through post-processing to filter sensitive data. The tool then bundles the information into a zip file.

Optionally, you can inspect the zip file and its content to ensure that you are not capturing any sensitive data before sharing it with Support.

## Access Support documentation

Access the following documentation and playbooks to help troubleshoot the customer problem at hand:

  * Support playbooks
  * Public documentation, best practices, FAQs, and the knowledge base
  * The user community



A partner might provide L1 and L2 support, so these artifacts must be publicly available.

## Escalate a software problem to L3

Follow these steps to escalate a software problem to Google for level 3 (L3) or advanced support:

  1. Request permission to share snapshot data with Google.
  2. Open a support ticket with Google.
  3. Provide Google with access to your snapshot.
  4. Monitor and provide visibility into the operations that Google performs on the snapshot.



## Escalate a hardware problem to L3

Follow these steps to escalate a problem to Google that a hardware failure caused:

  1. Extract and sanitize the minimal information to troubleshoot the hardware components: 
     * Logs
     * Status and configurations
     * Metrics
     * Physical information such as a rack number, component type, serial number, and physical location.
  2. Request permission to share snapshot data with Google.
  3. Open a support ticket with Google.
  4. Provide Google with access to your snapshot.
  5. Monitor and provide visibility into the operations that Google performs on the snapshot.



## Open a hardware support case

Google has access to the same troubleshooting tools to diagnose the customer's snapshot. Open a support case with the hardware-as-a-service (HWaaS) partner to get hardware support through the shared ticketing system.

Support tickets have the following priority levels with the corresponding service-level agreements (SLA):

  * Critical
  * High
  * Medium



## Share customer data with the HWaaS partner

Follow these steps to share system hardware data with the hardware partner and enable hardware troubleshooting:

  1. Request permission to share snapshot data with an HWaaS partner.
  2. Ensure you comply with sovereignty requirements: nationality and location of the Support agent.
  3. Grant the HWaaS partner secure access to the customer hardware snapshot, including the serial number, physical location, logs, metrics, and configuration files.
  4. Notify to who you have granted access.
  5. Enforce automatic expiration of access privileges.
  6. Log all activities and share them with all involved parties.



## Notify Google of troubleshooting results and fix the timeline

Report back to Google on the root cause of the issue and offer a gradual fix so that Google can notify the end customer and partner. Use a ticketing system to provide details of the required fix task and provide an estimated timeline for it to complete.

## Coordinate data center access

Coordinate logistics and permissions for secure access to the data center and perform the necessary hardware fix.

The HWaaS partner ensures compliance with sovereignty requirements, such as the nationality of the Support agent. They need the following information:

  * The details of the point of contact of the data center and location.
  * The exact location of the problem rack and component in the data center.
  * A process to get clearance and authorization to access the data center at an agreed-upon time.
  * A process to schedule on-site intervention at a data center.



## Obtain hardware support for SLO and SLA

Google provides support through a hardware original equipment manufacturer (OEM) partner. The process is as follows:

  1. Google negotiates hardware support for service-level objectives (SLO) and service-level agreements (SLA) with an HWaaS partner.
  2. SLO and SLA vary based on incident criticality, which can be critical, high, or medium.
  3. The HWaaS partner updates the ticket with the status and estimated time to fix it.
  4. The HWaaS partner confirms when the issue is resolved.



## Upgrade capacity

To respond to a request for a capacity increase, use built-in extra capacity if available. Go onsite and upgrade physical capacity if no additional capacity is available on the racks.

## Schedule recurring reviews with Google

Set up periodic reviews with the HWaaS partner to check the current status of deployments and plan scheduled interventions.

Go through the following actions during recurring reviews:

  * Check required scheduled updates to the operating system, hardware and firmware.
  * Review the status of existing deployments.
  * Plan new deployments.



## Communicate scheduled maintenance and upgrades

Communicate with existing customers on upcoming scheduled maintenance plans. Go through the following actions with them:

  * Select the resources to upgrade.
  * Specify why the upgrades will perform in their current state.
  * Determine who will perform the upgrades and when, where, and how.
  * Plan for the possible impact and downtimes.



## Set scheduled maintenance

Schedule regular preventive maintenance and ensure that the system is up to date and performs well. The HWaaS reports back on the completion of maintenance. It needs the following processes:

  * A process to gain clearance to access the data center.
  * A process to schedule on-site intervention at the data center.



## What's next

  * [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings)
  * [Monitoring and logging overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-overview)
  * [Feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
