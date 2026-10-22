---
url: https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices/
title: Migrate to Google Cloud: Best practices for validating a migration plan \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:35.175589+00:00
---

# Migrate to Google Cloud: Best practices for validating a migration plan  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Best practices for validating a migration plan Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-05 UTC

This document describes the best practices for validating the plan to migrate your workloads to Google Cloud. This document doesn't list all of the possible best practices for validating a migration plan, and it doesn't give you guarantees of success. Instead, it helps you to stimulate discussions about potential changes and improvements to your migration plan.

This document is useful if you're planning a migration from an on-premises environment, from a private hosting environment, or from another cloud provider to Google Cloud. The document is also useful if you're evaluating the opportunity to migrate and want to explore what it might look like.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads)
  * [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)
  * [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment)
  * Migrate to Google Cloud: Best practices for validating a migration plan (this document)
  * [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs)



## Assessment

Performing a complete [assessment of your workloads and environments](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads) helps to ensure that you develop a deep understanding of your workloads and environments. Developing this understanding helps you to minimize the risks of issues happening during and after your migration to Google Cloud.

### Make a complete assessment

Before you proceed with the [steps that follow the assessment phase](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path), complete the [assessment of your workloads and environments](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads). To make a complete assessment, consider the following items, which are often overlooked:

  * **Inventory:** Ensure that the [inventory of the workloads to migrate](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads#build_an_inventory_of_your_workloads) is up to date and that you completed the assessment. For example, consider how fresh and reliable the source data is for your assessment, and what gaps might exist in the data.
  * **Downtimes:** Identify the workloads that can handle downtimes. Determine when these downtimes can occur and for how long they can last to minimize disruption, such as during late evenings or weekends. Migrating workloads while experiencing zero or nearly zero downtimes is harder than migrating workloads that can afford downtimes. To complete a zero-downtime migration, you need to design for and implement redundancy for each workload to migrate. You also need to coordinate these redundant instances.

When you assess how much downtime a workload can tolerate, assess whether the business benefit of a zero-downtime migration is greater than the added migration complexity. Where possible, avoid creating a zero-downtime requirement for a workload.

  * **Clustering and redundancy:** Assess which workloads support clustering and redundancy. If a workload supports clustering and redundancy, you can deploy multiple instances of that workload, even across different environments, such as the source environment and the target environment. Clustered and redundant deployments might simplify the migration because those workloads coordinate with each other with limited intervention.

  * **Configuration updates:** Assess how you update the configuration of your workloads. For example, consider how you deliver updates to the configuration of each workload that you want to migrate. This consideration is critical for the success of your migration because you might have to update the configuration of your workloads while you migrate them to the target environment.

  * **Generate multiple assessment reports:** During the assessment phase, it might be useful to generate more than one assessment report to account for different scenarios. For example, you can generate reports to take into account different load profiles for your workloads, such as at- and off-peak times.




### Assess the failure modes that your workloads support

Knowing how your workloads behave under exceptional circumstances helps you to ensure that you don't expose them to conditions from which they can't recover. As part of the assessment, gather information about the [failure modes and their effects](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) that your workloads support and can automatically recover from, and which failure modes need your intervention. For example, you can start by considering questions about possible failure modes, such as the following:

  * What happens if a workload loses connectivity to the network?
  * Is a workload able to resume its work from where it left off after being stopped?
  * What happens if the performance of a workload or its dependencies is inadequate?
  * What happens if there are two workloads that have the same identifier in the architecture?
  * What happens if a scheduled task doesn't run?
  * What happens if two workloads process the same message?



Another source for unsupported failure modes might be the migration plan itself. Determine whether your migration plan includes steps that depend on the success of a particular condition and whether it includes contingencies if the condition is not met. A plan that includes these types of conditions can indicate that the plan itself might fail or that individual components might fail during migration.

After you assess those failure modes and their effects, validate your findings in a non-critical environment by simulating failures and injecting faults that emulate those failure modes. For example, if a workload is designed to automatically recover after a network connectivity loss, validate the automatic recovery by forcibly interrupting its connectivity and then restoring it.

### Assess your data processing pipelines

Your workload assessment should be able to answer the following questions:

  * Are resources correctly sized for the migration?
  * How much time is required to migrate the data that your workloads need?
  * Can the target environment accommodate the full volume of data?
  * How do your workloads behave when they have to accommodate spikes in demand or spikes in the amount of data that they produce in a given time window?
  * If there are spikes in demand or spikes in the amount of data that your workloads produce, is there any adverse effect, such as increased latency or delays in responses?
  * After your workloads start, do they need time to ramp up to the expected levels of performance?



The results of this assessment are often models of the demand that your workloads satisfy and the data that the workloads produce in a given time window. When you gather data points to produce such models, consider that those data points might vary significantly between peak and non-peak time windows. For more information about how and what to monitor, see [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) in the Site Reliability Engineering book.

### Ensure that you can update and deploy each workload to migrate

During the migration, you might need to update some of the workloads that you're migrating. For example, you might need to deploy a fix for an issue, or roll back a recent change that is causing an issue. For each workload that you're migrating, ensure that you can apply and deploy changes. For example, if you're migrating a workload for which you have the source code, ensure that you can access that source code, and that you can build, package, and deploy the source code as needed.

Your migration might include workloads that you can't apply and deploy changes to, such as pre-existing and ready-made software. In that scenario, refactor your migration plan to consider additional effort to mitigate the issues that might occur after you migrate those workloads.

### Assess your network infrastructure

A functional network infrastructure is fundamental for the migration. You can use the network infrastructure as part of your migration tooling. For example, you can use load balancers and DNS servers to direct traffic according to your migration plan.

To avoid issues during the migration, it's important to assess your network infrastructure and evaluate to what extent it can support your migration. For example, you can start by considering questions about your load-balancing infrastructure, such as the following:

  * What happens when you reconfigure your load balancers?
  * How long does it take for the updated configuration to be in effect?
  * When migrating with zero downtime, what happens if you get a spike of traffic before the updated configuration is in place?



After you consider questions about your load-balancing infrastructure, next consider questions about your DNS infrastructure, such as the following:

  * Which DNS records should you update to point them to the target environment, and when should you update them?
  * Which clients are using those DNS records?
  * How is the time to live (TTL) configured for the DNS records that you plan to update?
  * Can you set the DNS record TTL to its minimum value in seconds before you perform the migration?
  * Do your DNS clients and intermediaries respect the TTL of the DNS records that you plan to update? For example, do your applications have client-side DNS caching that ignores the TTL that you've configured for the migration? Remember that DNS resolution involves multiple layers of caching. Consider using [Google Public DNS](https://developers.google.com/speed/public-dns) to avoid ISP DNS issues.
  * Do your DNS clients respect the TTL of the DNS records to update? For example, do your applications have client-side DNS caching that ignores the TTL that you've configured for the migration?
  * Do you detect traffic directed at your source environment even after you completed the migration?



### Consider creating a proof of concept

A proof of concept (POC) is a small, preliminary implementation of a planned migration project. It validates the feasibility, functionality, and potential benefits of that project before you commit to a full implementation. A POC helps you to determine whether the migration workloads function correctly in the target environment.

Start by defining the scope and the specific success criteria for the POC. Your success criteria could include metrics like full target workload compatibility, minimal migration downtime, and specific performance demands.

After you identify your success criteria, test and validate your POC. In your migration plan documentation, capture your findings, the challenges that you encountered, and any potential solutions to those challenges.

Consider creating a POC when you want to investigate the following areas of interest:

  * **Validate migration feasibility:** Verify that your applications, workloads, and data function as expected in Google Cloud.
  * **Estimate downtime and plan for rollback:** Measure the downtime that's required to migrate your workloads and to transfer data. Validate your rollback scenarios.
  * **Refine the migration plan:** Use the following considerations to refine your plan before you commit to a full-scale migration: 
    * Identify the best migration approach.
    * Identify your modernization or workload refactoring needs.
    * Identify the potential risks or issues with your migration.
    * Test the migration.
  * **Perform security and compliance validation:** Ensure that the security policies, the Identity and Access Management (IAM) roles, and the compliance requirements for your migration align with your organization's needs.
  * **Build confidence and stakeholder buy-in:** Help ensure stakeholder satisfaction. A successful POC builds stakeholder confidence in the migration plan by demonstrating tangible benefits to your leadership and technical teams.
  * **Estimate costs and optimization possibilities:** Estimate the costs that are associated with the migration. Explore optimization possibilities, such as testing different target environment sizes and migration tools.



Iterate through several POCs. Adjust the target workloads and the migration plan until you create a POC that fulfills your success criteria.

## Migration planning

Thoroughly planning your migration helps you to avoid issues during and after the migration. Planning also helps you to avoid effort to deal with unanticipated tasks.

### Develop a rollback strategy for each step of the migration plan

During the migration, any step of the migration plan that you execute might result in unanticipated issues. To ensure that you're able to recover from those issues, prepare a rollback strategy for each step of the migration plan. To avoid losing time during an outage, do the following:

  * Ensure that your rollback strategies work by periodically reviewing and testing each rollback strategy.
  * Set a maximum-allowed execution time for each migration step. After this allowed execution time expires, your teams start rolling back the migration step.



Even if you have rollback strategies ready for each step of the migration plan, some of those steps might still be potentially disruptive. A potentially disruptive step might cause some kind of loss even if you roll it back, such as a data loss. Assess which steps of the migration plan are potentially disruptive.

If you automated any step of the migration plan, ensure that you have a preplanned procedure for each automated step if there is a failure in the automation. As with rollback strategies, periodically review and test each preplanned procedure.

If you set up communication channels as part of the migration, to ensure that you aren't locked out from your environment, provision backup channels that you can use to recover from a failure. For example, if you're setting up [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview), during the migration you can also set up a backup access through the public internet in case you experience any issues during provisioning and configuration.

### Plan to modernize and adapt your workloads

When planning your migration to Google Cloud, remember that migrating and integrating your workloads takes time and might present challenges. Consider creating an overview document that describes the general architecture of your workloads, including information about the following topics:

  * Dependencies on external systems and on third-party middleware, such as storage, messaging, and hosting.
  * Mechanisms to authenticate and authorize workloads.
  * Processes to integrate with IAM.
  * Requirements for the runtime environment.
  * Interactions with storage layer options, like [Cloud Storage](https://cloud.google.com/storage) and [Google Cloud databases](https://cloud.google.com/products/databases).
  * Requirements for your data transfer volume and bandwidth.
  * Changes in your application code that you might make during your migration.
  * Options for integrating with [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs).



Modernizing your workloads might be necessary, such as integrating Google Cloud libraries for authentication, authorization, storage, and observability. Modernizing legacy libraries can require effort. Plan for enough time to thoroughly test your workloads.

### Plan for gradual rollouts and deployments

To reduce the scope of issues and problems that might occur during the migration, avoid big-scale changes, and design your migration plan to gradually deploy changes. For example, plan for gradual deployments and configuration changes.

If you plan for gradual rollouts, to lower the risk of unanticipated issues caused by the application of the changes, minimize the number and the size of those changes. After you identify and resolve issues in your first small rollout, you can make the subsequent rollouts for similar changes at larger scales.

### Alert development and operations teams

To reduce the impact of issues that might occur during a migration, alert the teams that are responsible for any workload to migrate. Also alert the teams that are responsible for the infrastructure of both the source and target environments.

If your teams work in different time zones and you practice the [follow-the-sun](https://en.wikipedia.org/wiki/Follow-the-sun) operating model, ensure the following:

  * Your teams properly cover those time zones and they cover multiple consecutive shifts, because they might be unable to resolve issues during a single shift.
  * Your teams are prepared to collect detailed information about the issues that they might face. This collection provides the engineers on the next shift a complete understanding of what the previous shift did, and why.
  * Specific people in your teams are responsible for any given shift.



### Remove proof-of-concept resources from the target production environment

As part of the assessment, you might have used the target environment to host experiments and proofs of concept. Before the migration, remove any resources that you created during those experiments and proofs of concept from the production area of the target environment.

You can keep resources in a non-production area of the target environment while the migration is in progress because they might help you to gather information about any issue that might arise during the migration. For example, to diagnose issues that affect your production workloads after the migration, you can compare the configuration and data logs of the production workload against the configuration and data logs of the proofs of concept and experiments.

After you complete the migration and you validate that the target environment works as expected, you can delete the resources in the non-production area of the target environment.

### Define criteria to safely retire the source environment

To avoid the cost of running two environments indefinitely, define what conditions must be met for you to safely retire the source environment, such as the following:

  * All workloads, including their backups and high availability and disaster recovery mechanisms, are successfully migrated to the target environment.
  * The data migrated to the target environment is consistent, accessible, and usable.
  * The accuracy and completeness of the migrated data fulfill the defined standard.
  * Resources that remain in the source environment aren't dependencies for workloads that are out of the migration scope.
  * The performance of your workloads on the target environment fulfill your SLA targets.
  * Your monitoring systems report that there isn't any network traffic to the source environment that should be directed to the target environment.
  * After the workloads are running without issue in the target environment for a period that you define, you are confident that you no longer need the ability to fall back to the source environment.



### Plan to update all documents and dashboards

After you complete the migration, plan to comprehensively update your production operation runbooks, your support documents, and your monitoring dashboards. The changes that you need to make to your documentation might include the following items:

  * **Architectural diagrams:** Update your architectural diagrams to reflect the Google Cloud architecture, especially if you modernize and refactor your workloads.
  * **Connection and authentication:** Update your documentation on authentication methods, such as IAM, and network configurations, to reflect the Google Cloud architecture.
  * **Security:** Update your documentation that discusses Google Cloud security features, including encryption at rest and in transit, and IAM-based access controls.
  * **Maintenance and scaling:** Update your production operation runbooks on managed services maintenance windows, vertical and horizontal scaling procedures, and best practices for performance optimization.
  * **High Availability and failover:** Update your documentation for high availability configurations, regional and zonal synchronization considerations, and failover mechanisms.
  * **Backup and recovery:** Update your backup and recovery processes to align with the processes that Google Cloud and the [Backup and Disaster Recovery (DR) Service](https://cloud.google.com/backup-disaster-recovery) support. These processes include automated backups, point-in-time recovery possibilities, and export and import procedures.
  * **Disaster recovery:** Update your DR plan and procedures to align with the DR capabilities of Google Cloud and then test the updated procedures.
  * **Monitoring and logging:** Integrate Google Cloud Observability into your monitoring dashboards and alerting systems. Update your documentation on [Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview) and specify how to interpret logs, metrics and alerts.



## Operations

To efficiently manage the source environment and the target environment during the migration, you need to engineer your operational processes as well.

### Monitor your environments

To observe how your source and target environments are behaving and to help you diagnose issues as they occur, set up the following:

  * A monitoring system to gather metrics that are useful to your scenario.
  * A logging system to observe the flow of operations that is performed by your workloads and other components of your environments.
  * An alerting system that warns you before a problematic event occurs.



[Google Cloud Observability](https://cloud.google.com/products/operations) supports integrated monitoring, logging, and alerting for your Google Cloud environment.

Because a workload and its dependencies span multiple environments, you might need to consider using multiple monitoring and alerting tools for different environments. Consider the timing of when you migrate the monitoring and alerting policies that support the workloads. For example, if your source environment is configured to alert when a particular server is down, the alert triggers when you intentionally turn down that server. The alert trigger is expected, but it's unhelpful behavior. As part of the migration, you need to continuously adjust the alerts for the source environment and reconfigure them for the target environment.

### Manage the migration

To manage the migration, you review the performance of the migration to gather information that you can use as a retrospective after the migration is complete. After you gather information, you use it to analyze the migration performance and to prepare data points about potential improvements to your environments.

For example, to start planning to manage the migration, consider the following questions:

  * How long did each step of the migration plan take?
  * Were there any steps of the migration plan that took more time to complete than anticipated?
  * Were there any missing steps or checks?
  * Did any adverse events occur during the migration?



## What's next

  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Other contributor: [Alex Cârciu](https://www.linkedin.com/in/alex-carciu) | Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-05 UTC."],[],[]] 
