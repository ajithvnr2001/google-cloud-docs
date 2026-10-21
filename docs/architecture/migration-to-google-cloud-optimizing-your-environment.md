---
url: https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment/
title: Migrate to Google Cloud: Optimize your environment \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:11.930060+00:00
---

# Migrate to Google Cloud: Optimize your environment  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Optimize your environment Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-07 UTC

This document helps you plan and design the optimization phase of your migration to Google Cloud. After you've deployed your workloads in Google Cloud, you can start optimizing your environment.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads)
  * [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)
  * Migrate to Google Cloud: Optimize your environment (this document)
  * [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
  * [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs)



The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

In the optimization phase, you refine your environment to make it more efficient than your initial deployment.

This document is useful if you're planning to optimize an existing environment after migrating to Google Cloud, or if you're evaluating the opportunity to optimize and want to explore what it might look like.

The structure of the optimization phase follows the migration framework described in this series: assess, plan, deploy, and optimize. You can use this versatile framework to plan your entire migration and to break down independent actions in each phase. When you've completed the last step of the optimization phase, you can start this phase over and find new targets for optimization. The optimization phase is defined as an _optimization loop_. An execution of the loop is defined as an _optimization iteration_.

Optimization is an ongoing and continuous task. You constantly optimize your environment as it evolves. To avoid uncontrolled and duplicative efforts, you can set measurable optimization goals and stop when you meet these goals. After that, you can always set new and more ambitious goals, but consider that optimization has a cost, in terms of resources, time, effort, and skills.

The following diagram shows the optimization loop.

![Optimization decision tree.](https://docs.cloud.google.com/static/architecture/images/migration-to-google-cloud-optimizing-your-environment.svg) For a larger image of this diagram, see [Optimization decision tree](https://docs.cloud.google.com/static/architecture/migration-to-google-cloud-optimizing-your-environment.pdf).

In this document, you perform the following repeatable steps of the optimization loop:

  1. Assess your environment, teams, and the optimization loop that you're following.
  2. Establish optimization requirements and goals.
  3. Optimize your environment and train your teams.
  4. Tune the optimization loop.



This document discusses some of the [site reliability engineering (SRE)](https://landing.google.com/sre/) principles and concepts. Google developed the SRE discipline to efficiently and reliably run a global infrastructure serving billions of users. Adopting the complete SRE discipline in your organization might be impractical if you need to modify many of your business and collaboration processes. It might be simpler to apply a subset of the SRE discipline that best suits your organization.

## Assess your environment, teams, and optimization loop

Before starting any optimization task, you need to evaluate your environment. You also need to assess your teams's skills because optimizing your environment might require skills that your teams might lack. Finally, you need to assess the optimization loop. The loop is a resource that you can optimize like any other resource.

### Assess your environment

You need a deep understanding of your environment. For any successful optimization, you need to understand how your environment works and you need to identify potential areas of improvement. This assessment establishes a baseline so that you can compare your assessment against the optimization phase and the next optimization iterations.

[Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads) contains extensive guidance about assessing your workloads and assessing your environments. If you recently completed a migration to Google Cloud, you already have detailed information on how your environment is configured, managed, and maintained. Otherwise, you use that guidance to assess your environment.

### Assess your teams

When you have a clear understanding of your environment, assess your teams to understand their skills. You start by listing all skills, the level of expertise for each skill, and which team members are the most knowledgeable for each skill. Use this assessment in the next phase to discover any missing skills that you need to meet your optimization goals. For example, if you start using a managed service, you need the skills to provision, configure, and interact with that service. If you want to add a caching layer to an application in your environment by using [Memorystore](https://docs.cloud.google.com/memorystore), you need expertise to use that service.

Take into account that optimizing your environment might impact your business and collaboration processes. For example, if you start using a fully managed service instead of a self-managed one, you can give your operators more time to [eliminate toil](https://landing.google.com/sre/sre-book/chapters/eliminating-toil/).

### Assess your optimization loop

The optimization loop is a resource that you can optimize too. Use the data gathered in this assessment to gain clear insights into how your teams performed during the last optimization iteration. For example, if you aim to shorten the iteration duration, you need data about your last iteration, including its complexity and the goals you were pursuing. You also need information about all blockers that you encountered during the last iteration to ensure that you have a mitigation strategy if those blockers reoccur.

If this optimization iteration is the first one, you might not have enough data to establish a baseline to compare your performance. Draft a set of hypotheses about how you expect your teams to perform during the first iteration. After the first optimization iteration, evaluate the loop and your teams' performance and compare it against the hypotheses.

## Establish your optimization requirements and goals

Before starting any optimization task, draft a set of clearly measurable goals for the iteration.

In this step, you perform the following activities:

  1. Define your optimization requirements.
  2. Set measurable optimization goals according to your optimization requirements.



### Define your optimization requirements

You list your requirements for the optimization phase. A requirement expresses a need for improvement and doesn't necessarily have to be measurable.

Starting from a set of quality characteristics for your workloads, your environment, and your own optimization loop, you can draft a questionnaire to guide you in setting your requirements. The questionnaire covers the characteristics that you find valuable for your environment, processes, and workloads.

There are many sources to guide you in defining the quality characteristics. For example, the [ISO/IEC 25010](https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:ed-1:v1:en) standard defines the quality characteristics for a software product, or you can review the [Google Cloud setup checklist](https://docs.cloud.google.com/docs/enterprise/onboarding-checklist).

For example, the questionnaire can ask the following questions:

  * Can your infrastructure and its components scale vertically or horizontally?
  * Does your infrastructure support rolling back changes without manual intervention?
  * Do you already have a monitoring system that covers your infrastructure and your workloads?
  * Do you have an incident management system for your infrastructure?
  * How much time and effort does it take to implement the planned optimizations?
  * Were you able to meet all goals in your past iterations?



Starting from the answers to the questionnaire, you draft the list of requirements for this optimization iteration. For example, your requirements might be the following:

  * Increase the performance of an application.
  * Increase the availability of a component of your environment.
  * Increase the reliability of a component of your environment.
  * Reduce the operational costs of your environment.
  * Shorten the duration of the optimization iteration to reduce the inherent risks.
  * Increase development velocity and reduce time-to-market.



When you have the list of improvement areas, evaluate the requirements in the list. In this evaluation, you analyze your optimization requirements, look for conflicts, and prioritize the requirements in the list. For example, increasing the performance of an application might conflict with operational cost reduction.

### Set measurable goals

After you finalize the list of requirements, define measurable goals for each requirement. A goal might contribute to more than one requirement. If you have any area of uncertainty or if you're not able to define all goals that you need to cover your requirements, go back to the assessment phase of this iteration to gather any missing information, and then refine your requirements.

For help defining these goals, you can follow one of the SRE disciplines, the [definition of service level indicators (SLIs) and service level objectives (SLOs)](https://landing.google.com/sre/sre-book/chapters/service-level-objectives/):

  * SLIs are quantitative measures of the level of service that you provide. For example, a key SLI might be the average request latency, error rate, or system throughput.
  * SLOs are target values or ranges of values for a service level that is measured by an SLI. For example, an SLO might be that the average request latency is lower than 100 milliseconds.



After defining SLIs and SLOs, you might realize that you're not gathering all metrics that you need to measure your SLIs. This metrics collection is the first optimization goal that you can tackle. You set the goals related to extending your monitoring system to gather all metrics that you need for your SLIs.

## Optimize your environment and your teams

After assessing your environment, teams, and optimization loop, as well as establishing requirements and goals for this iteration, you're ready to perform the optimization step.

In this step, you perform the following activities:

  1. Measure your environment, teams, and optimization loop.
  2. Analyze the data coming from these measurements.
  3. Perform the optimization activities.
  4. Measure and analyze again.



### Measure your environment, teams, and optimization loop

You extend your monitoring system to gather data about the behavior of your environment, teams, and the optimization loop to establish a baseline against which you can compare after optimizing.

This activity builds on and extends what you did in the assessment phase. After you establish your requirements and goals, you know which metrics to gather for your measurements to be relevant to your optimization goals. For example, if you defined SLOs and the corresponding SLIs to reduce the response latency for one of the workloads in your environment, you need to gather data to measure that metric.

Understanding these metrics also applies to your teams and to the optimization loop. You can extend your monitoring system to gather data so that you measure the metrics relevant to your teams and the optimization loop. For example, if you have SLOs and SLIs to reduce the duration of the optimization iteration, you need to gather data to measure that metric.

When you design the metrics that you need to extend the monitoring system, take into account that gathering data might affect the performance of your environment and your processes. Evaluate the metrics that you need to implement for your measurements, and their sample intervals, to understand if they might affect performance. For example, a metric with a high sample frequency might degrade performance, so you need to optimize further.

On Google Cloud, you can use [Cloud Monitoring](https://docs.cloud.google.com/monitoring) to implement the metrics that you need to gather data. To implement custom metrics in your workloads directly, you can use [Cloud Client Libraries for Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/reference/libraries), or [OpenTelemetry](https://opentelemetry.io/). If you're using Google Kubernetes Engine (GKE), you can use [GKE usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) to gather information about resource usage, such as CPU, GPU, and TPU usage, and then divide resource usage by [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) or [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

Finally, you can use the [Cloud Architecture Center](https://docs.cloud.google.com/architecture) and [Google Cloud Whitepapers](https://cloud.google.com/whitepapers) as starting points to find new skills that your teams might require to optimize your environment.

### Analyze data

After gathering your data, you analyze and evaluate it to understand how your environment, teams, and optimization loop are performing against your optimization requirements and goals.

In particular, you evaluate your environment against the following:

  * SLOs.
  * Industry best practices.
  * An environment without any technical debt.



The SLOs that you established according to your optimization goals can help you understand if you're meeting your expectations. If you're not meeting your SLOs, you need to enhance your teams or the optimization loop. For example, if you established an SLO for the response latency for a workload to be in a given percentile and that workload isn't meeting that mark, that is a signal that you need to optimize that part of the workload.

Additionally, you can compare your situation against a set of recognized best practices in the industry. For example, the [Google Cloud setup checklist](https://docs.cloud.google.com/docs/enterprise/onboarding-checklist) helps you configure a production-ready environment for enterprise workloads.

After collecting data, you can consider how to optimize your environment to make it more cost efficient. You can [export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) and [analyze data with Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio) to understand how many resources you're using, and extract any spending pattern from it.

Finally, you compare your environment to one where you don't have any [technical debt](https://en.wikipedia.org/wiki/Technical_debt), to see whether you're meeting your long-term goals and to see if the technical debt is increasing. For example, you might establish an SLO for how many resources in your environment you're monitoring versus how many resources you have provisioned since the last iteration. If you didn't extend the monitoring system to cover those new resources, your technical debt increased. When analyzing the changes in your technical debt, also consider the factors that led to those changes. For example, a business need might require an increment in technical debt, or it might be unexpected. Knowing the factors that caused a change in your technical debt gives you insights for future optimization targets.

To monitor your environment on Google Cloud, you can use Monitoring to design [charts](https://docs.cloud.google.com/monitoring/charts), [dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards), and [alerts](https://docs.cloud.google.com/monitoring/alerts). You can then [route Cloud Logging data](https://docs.cloud.google.com/logging/docs/routing/overview) for a more in-depth analysis and extended retention period. For example, you can [create aggregated sinks and use Cloud Storage, Pub/Sub, or BigQuery as destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks). If you export data to BigQuery, you can then [use Data Studio to visualize data](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio) so that you can identify trends and make predictions. You can also use evaluation tools such as [Recommender](https://docs.cloud.google.com/recommender) and [Security Command Center](https://docs.cloud.google.com/security-command-center) to automatically analyze your environment and processes, looking for optimization targets.

After you analyze all of the measurement data, you need to answer two questions:

  1. Are you meeting your optimization goals?

If you answered _yes_ , then this optimization iteration is completed, and you can start a new one. If you answered _no_ , you can move to the second question.

  2. Given the resources that you budgeted, can you achieve the optimization goals that you set for this iteration?




To answer this question, consider all resources that you need, such as time, money, and expertise. If you answered _yes_ , you can move to the next section; otherwise, refine your optimization goals, considering the resources you can use for this iteration. For example, if you're constrained by a fixed schedule, you might need to schedule some optimization goals for the next iteration.

### Optimize your teams

Optimizing the environment is a continuous challenge and can require skills that your teams might lack, which you discovered during the assessment and the analysis. For this reason, optimizing your teams by acquiring new skills and making your processes more efficient is crucial to the success of your optimization activities.

To optimize your teams, you need to do the following:

  * Design and implement a training program.
  * Optimize your team structure and culture.



For your teams to acquire the skills that they are missing, you need to design and implement a training program or choose one that professional Google Cloud trainers prepared. For more information, see [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads#educating_your_organization_about_gcp).

While optimizing your teams, you might find that there is room to improve structure and culture. It's difficult to prescribe an ideal situation upfront, because every company has its own history and idiosyncrasies that contributed to the evolution of your teams' structure and culture.

[Transformational leadership](https://dora.dev/devops-capabilities/cultural/transformational-leadership/) is a good starting point to learn general frameworks for executing and measuring organizational changes aimed at adopting [DevOps](https://cloud.google.com/devops/) practices. For practical guidance on how to implement an effective DevOps culture in your organization, refer to [Site Reliability Engineering](https://landing.google.com/sre/sre-book/toc/index.html), a comprehensive description of the SRE methodology. The [Site Reliability Workbook](https://landing.google.com/sre/workbook/toc/), the companion to the book, uses concrete examples to show you how to put SRE principles and practices to work.

### Optimize your environment

After measuring and analyzing metrics data, you know which areas you need to optimize.

This section covers general optimization techniques for your Google Cloud environment. You can also perform any optimization activity that's specific to your infrastructure and to the services that you're using.

#### Codify everything

One of the biggest advantages of adopting a public cloud environment like Google Cloud, is that you can use well-defined interfaces such as [Cloud APIs](https://docs.cloud.google.com/apis) to provision, configure, and manage resources. You can use your own choice of tools to define your Infrastructure as Code (IaC) process, and your own choice of [version control systems](https://en.wikipedia.org/wiki/Version_control).

You can use tools such as [Terraform](https://www.terraform.io/) to provision your Google Cloud resources, and then tools such as [Ansible](https://www.ansible.com/), [Chef](https://www.chef.io/), or [Puppet](https://puppet.com/) to [configure your these resources](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads). An IaC process helps you implement an effective rollback strategy for your optimization tasks. You can revert any change that you applied to the code that describes your infrastructure. Also, you can avoid unexpected failures while updating your infrastructure by testing your changes.

Furthermore, you can apply similar processes to codify other aspects of your environment, like policies as code, using tools such as [Open Policy Agent](https://www.openpolicyagent.org/), and operations as code, such as [GitOps](https://docs.cloud.google.com/architecture/managing-infrastructure-as-code).

Therefore, if you [adopt an IaC process](https://cloud.google.com/blog/products/devops-sre/want-repeatable-scale-adopt-infrastructure-as-code-on-gcp) in the early optimization iterations, you can define further optimization activities as code. You can also adopt the process gradually, so you can evaluate if it's suitable to your environment.

#### Automate everything

To completely optimize your entire environment, you need to use resources efficiently. This means that you need to eliminate toil to save resources and to reinvest in more important tasks that produce value, like optimization activities.

Per the SRE recommendation, the way to eliminate toil is by increasing automation. Not all automation tasks require highly specialized software engineerings skills or great efforts. Sometimes a short executable script executed periodically can save several hours per day. Google Cloud provides tools such as [Google Cloud CLI](https://docs.cloud.google.com/sdk) and managed services such as Cloud APIs, [Cloud Scheduler](https://docs.cloud.google.com/scheduler), [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer), and [Cloud Run](https://docs.cloud.google.com/run) that your teams can use to automate repetitive tasks.

#### Monitor everything

If you can't gather detailed measures about your environment, you can't improve it, because you lack data to back up your assumptions. This means that you don't know what to do to meet your optimization goals.

A comprehensive monitoring system is a necessary component for your environment. The system monitors all essential metrics that you need to evaluate for your optimization goals. When you design your monitoring system, plan to monitor the [four golden signals](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/#xref_monitoring_golden-signals) at minimum.

You can use managed services such as Monitoring and Logging to monitor your environment without having to set up a complicated monitoring solution.

You might need to implement a monitoring system that can [monitor hybrid and multicloud environments](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns) to satisfy data restriction policies that force you to store data only in certain physical locations, or services that use multiple cloud environments simultaneously.

#### Adopt a cloud-ready approach

Cloud-ready is a paradigm that describes an [efficient way for designing and running an application on the cloud](https://cloud.google.com/blog/products/application-development/5-principles-for-cloud-native-architecture-what-it-is-and-how-to-master-it). The [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/) defines a [cloud-native application](https://github.com/cncf/toc/blob/master/DEFINITION.md) as an application that is scalable, resilient, manageable, and observable by technologies such as containers, service meshes, microservices, immutable infrastructure, and declarative APIs. Google Cloud provides managed services such as GKE, Cloud Run, [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh), Logging, and Monitoring to empower users to design and run cloud-ready applications.

Learn more about cloud-ready technologies from [CNCF Trail Map](https://github.com/cncf/landscape/blob/master/README.md#trail-map) and [CNCF Cloud Native Interactive Landscape](https://landscape.cncf.io/).

#### Cost management

Because of their different billing and cost models, optimizing costs of a public cloud environment like Google Cloud is different than optimizing an on-premises environment.

For more information, see [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs).

### Measure and analyze again

When you complete the optimization activities for this iteration, you repeat the measurements and the analysis to check if you reached your goals. Answer the following question:

  * Did you meet your optimization goals?

If you answered _yes_ , you can move to the next section.

If you answered _no_ , go back to the beginning of the Optimize your environment and your teams phase.




## Tune the optimization loop

In this section, you update and modify the optimization loop that you followed in this iteration to better fit your team structure and environment.

#### Codify the optimization loop

To optimize the optimization loop efficiently, you need to document and define the loop in a form that is standardized, straightforward, and manageable, allowing room for changes. You can use a fully managed service such as [Managed Airflow](https://docs.cloud.google.com/composer) to create, schedule, monitor, and manage your workflows. You can also first represent your processes with a language such as the [business process model and notation (BPMN)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation). After that, you can codify these processes with a standardized language such as the [business process execution language (BPEL)](https://en.wikipedia.org/wiki/Business_Process_Execution_Language). After adopting IaC, describing your processes with code lets you manage them as you do the rest of your environment.

#### Automate the optimization loop

After you codify the optimization loop, you can automate repetitive tasks to eliminate toil, save time, and make the optimization loop more efficient. You can start automating all tasks where a human decision is not required, such as measuring data and producing aggregate reports for your teams to analyze. For example, you can automate data analysis with Cloud Monitoring to check if your environment meets the SLOs that you defined. Given that optimization is a never-ending task and that you iterate on the optimization loop, even small automations can significantly increase efficiency.

#### Monitor the optimization loop

As you did for all the resources in your environment, you need to monitor the optimization loop to verify that it's working as expected and also look for bottlenecks and future optimization goals. You can start monitoring it by tracking how much time and how many resources your teams spent on each optimization step. For example, you can use an issue tracking system and a project management tool to monitor your processes and extract relevant statistics about metrics like issue resolution time and time to completion.

## What's next

  * Read about [Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices).
  * Read the [SRE books](https://landing.google.com/sre/books/) to learn about other concepts and techniques to prepare for optimization.
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-07 UTC."],[],[]] 
