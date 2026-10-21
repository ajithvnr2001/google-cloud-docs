---
url: https://docs.cloud.google.com/vpc-service-controls/docs/enable/
title: Best practices for enabling VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:48.181621+00:00
---

# Best practices for enabling VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Best practices for enabling VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the recommended process to configure and enforce VPC Service Controls protection in your Google Cloud organization.

Careless enablement of VPC Service Controls can cause problems with existing applications and could potentially cause an outage. We recommend that you plan enablement carefully and allow ample time to gather data, conduct tests, and analyze violation logs. Make sure that stakeholders from your VPC Service Controls operation team and your applications team are available for the task.

For each workload or application that you onboard to VPC Service Controls, you should repeat the enablement process.

## Coordinate communication

Often, the network security or cloud enablement team leads the VPC Service Controls enablement effort. We recommend that you have a dedicated person who creates and tracks cross-functional meetings and documents action items. Your teams collaborate about the following:

  * Google Cloud APIs access patterns
  * Identification of service perimeter violations
  * Permitting access to the perimeter



Much like with conventional network firewalls, the intent is to identify and permit the flows necessary for the efficient functioning of legitimate business workloads.

## Document access patterns and use cases

To begin the enablement process, identify and clearly document all valid access patterns. Access patterns are repeatable types of interactions between elements outside and inside the perimeter. The following are some common access patterns:

  * **Data access patterns** : Services outside the perimeter store or retrieve data that resides in the perimeter.
  * **Resource access patterns** : 
    * Users access projects in the perimeter through the Google Cloud console.
    * Third-party tools or services manage and access resources inside the perimeter.
    * Services or resources within the perimeter access Google APIs.
  * **Endpoint access patterns** : 
    * Users access resources within the perimeter from a device that your organization manages.
    * On-premises resources communicate to resources within the perimeter.



After you identify the access patterns for a workload, identify your use cases and categorize them under one of the access patterns in the preceding list. The following are some common use cases:

  * Cloud administrators manage projects that are part of a perimeter.
  * Automation services like Terraform, Jenkins, and Microsoft Azure DevOps that reside outside of the perimeter manage resource deployment inside the perimeter.
  * Configuration management services like Ansible, Chef, or Puppet that reside outside of the perimeter manage deployment and configuration of software on resources that are inside the perimeter.
  * Security monitoring and enforcing services like Forseti or SIEM that reside outside of the perimeter consume data or enforce the security policies on a resource that is inside the perimeter.



For every use case, document the following:

  * The access pattern
  * The actors that can trigger the use case
  * Conditions that trigger the use case
  * Whether the use case is a valid access pattern and should be allowed
  * Any assumptions that pertain to the use case



For a sample access pattern and use case tracker, see [VPC Service Controls onboarding template - use cases (PDF)](https://docs.cloud.google.com/static/solutions/vpc-service-controls-enterprise-best-practices-use-cases-template.pdf).

## Conduct interviews

Conduct interviews with your workload teams to discuss the access patterns and use cases that you collect from the preceding communications templates. The following are examples of questions that you might ask during these interviews:

  * Are your use cases a first priority to be considered for VPC Service Controls enablement? We recommend that you only consider first priority workloads for the initial enablement, and onboard other, less critical workloads after protecting business-critical resources.

  * Can you complete a comprehensive execution of all use cases? You do this to trigger all possible perimeter scenarios so that you can fully analyze and confirm that the application will function correctly after you enforce the perimeter.

  * How long does it take to run through the use case execution?

  * Are you planning any major changes for this workload that might conflict with VPC Service Controls enablement? Workload features need to be in a stable state before you enable VPC Service Controls.




## Prepare a dry run

The [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) reduces the complexity of testing VPC Service Controls enforcement by identifying violations without interruption to the applications. You configure a dry run as a separate perimeter that logs all violations but doesn't perform any blocking. You can execute workloads while they are in the dry run perimeter and generate violation logs to be analyzed.

To prepare the dry-run environment, do the following:

  1. Identify all projects that are qualified to be part of the perimeter, and complete the use case and interview process for those projects.
  2. [Create a dry-run perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) and add all the projects.
  3. In the VPC Service Controls [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#creating_a_service_perimeter), under **Restricted Services > Services to protect**, add all supported services.
  4. Create an [aggregated logging sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that sends all logs to BigQuery, or create a [log sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) for each project that sends the dry-run logs to a common BigQuery dataset. To query these log messages and identify VPC Service Controls violations, you can use a SQL query.

To create a log sink that includes all relevant VPC Service Controls log messages, use the following filter:
         
         logName="projects/$PROJECT/logs/cloudaudit.googleapis.com%2Fpolicy"
         

  5. For maximum security, disallow access to unsupported services. Configure your perimeter such that only restricted services function in the perimeter. To do this, [configure the accessible services list to `RESTRICTED-SERVICES`](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#enable_vpc_accessible_services).

  6. If you already have a list of allowed public IPs, identities, trusted devices, projects, or VPC networks, add them to an ingress rule or access level as applicable in the dry-run perimeter. Permitting known legitimate flows helps reduce the number of violation logs and lets reviewers focus on actionable events.

  7. Verify that none of the VPCs in the projects have an egress path to the internet or the private VIP.

  8. Verify that all VPCs have the [`*.googleapis.com` DNS pointing to `restricted.googleapis.com`](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-dns).

![In Zone details, DNS name *.googleapis.com has restricted.googleapis.com in the Data field](https://docs.cloud.google.com/static/vpc-service-controls/images/vpc-service-controls-enterprise-best-practices-restricted-dns.png)




## Execute use cases

At an agreed time, have your application team execute their workload on the project in the dry run perimeter. Make sure that you have full coverage of all code that might call Google APIs. When the dry run is complete, your designated review team can perform the violation log analysis.

## Analyze violations

Dry-run violation logs contain most of the information that you need to determine if an application violation requires any action, such as adding identities or IP addresses to the perimeter allowlist. The violation data is stored in the BigQuery table `cloudaudit_googleapis_com_policy`. The following are the primary elements to analyze the violation:

  * The protected service and API method being called.
  * The project inside the perimeter that would have blocked the request.
  * The email of the identity that is calling the protected API.
  * The IP address of the caller.
  * The type of violation.



The following example is a BigQuery query that returns all violation details:
    
    
    SELECT
    receiveTimestamp, #time of violation
    Resource.labels.service, #protected Google Cloud service being blocked
    protopayload_auditlog.methodName, #method name being called
    resource.labels.project_id as PROJECT, #protected project blocking the call
    protopayload_auditlog.authenticationInfo.principalEmail, #caller identity
    protopayload_auditlog.requestMetadata.callerIp, #caller IP
    JSON_EXTRACT(protopayload_auditlog.metadataJson, '$.dryRun') as DRYRUN, #dry-run indicator
    JSON_EXTRACT(protopayload_auditlog.metadataJson, '$.violationReason') as REASON, #reason for violation
    protopayload_auditlog.metadataJson, #raw violation entry
    FROM `BQ_DATASOURCE_NAME.cloudaudit_googleapis_com_policy_*`
    where JSON_EXTRACT(protopayload_auditlog.metadataJson, '$.dryRun') = "true" #ensure these are dry-run logs
    

### Query relevant violations

The following strategies can help you to identify the relevant violations:

  * Add a timestamp qualifier for the time window when each unique application executed their use case:
        
        WHERE receiveTimestamp >'2020-07-23 19:53:48.241317 UTC'
        

  * Add a filter for the naming convention of workload identities or projects:
        
        WHERE where resource.labels.project_id like '%APPLICATION_NAME%'
        




### Review violation logs

When you review violation logs, determine if the following are true:

  * Is the identity (email) expected to invoke the protected APIs?
  * Should the caller be allowed to invoke the API from outside the perimeter?



Based on the preceding criteria, determine if you need to allow the identity, device, IP address, CIDR range, project, or network to access the perimeter from outside.

Some entries might have an IP address of `private`. This indicates that the call came from the Google network, either by Google's own services or by a VPC in a project that is outside the perimeter. For Google services such as [log sink writers](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks#creating_an_aggregated_sink), you need to add the Google service account to an allowlist.

Entries without emails are due to [Cloud Audit Logs redaction](https://docs.cloud.google.com/logging/docs/audit#user-id) for read-only operations that were denied due to lack of IAM permissions. In such cases, you can use IP address and resource names to understand the origin of the access attempt. This kind of access attempt might be an accidental access by a user from outside your organization. For example, a user who mistypes a similarly named bucket.

If you see a violation type of `SERVICE_NOT_ALLOWED_FROM_VPC`, the workload might be using a service that is supported by VPC Service Controls but wasn't added to the list of protected APIs. For example, if IAM caused such a violation, the administrator should add IAM to the list of accessible services by running the following Google Cloud CLI command:
    
    
    gcloud access-context-manager perimeters update perimeter_test \
     --add-vpc-allowed-services=RESTRICTED-SERVICES,IAM.googleapis.com \
     --policy=1234567890
    

You can create a Data Studio dashboard to review violations. For more information, see [Monitor VPC Service Controls violations on your Google Cloud organization with Data Studio](https://medium.com/google-cloud/create-a-data-studio-dashboard-to-monitor-vpc-sc-violations-on-your-google-cloud-organization-bf8f3bead691). Data Studio was previously known as Data Studio.

## What's next

  * Learn more about [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
  * Learn how to [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
