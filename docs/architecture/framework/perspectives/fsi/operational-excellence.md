---
url: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/operational-excellence/
title: Financial services perspective: Operational excellence \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:23.655596+00:00
---

# Financial services perspective: Operational excellence  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/operational-excellence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Financial services perspective: Operational excellence Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-28 UTC

This document in the [Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi) provides an overview of the principles and recommendations to build, deploy, and operate robust FS workloads in Google Cloud. These recommendations help you set up foundational elements like observability, automation, and scalability. The recommendations in this document align with the [operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence) of the Well-Architected Framework.

Operational excellence is critical for FS workloads in Google Cloud due to the highly regulated and sensitive nature of such workloads. Operational excellence ensures that cloud solutions can adapt to evolving needs _and_ meet your requirements for value, performance, security, and reliability. Failures in these areas could result in significant financial losses, regulatory penalties, and reputational damage.

Operational excellence provides the following benefits for FS workloads:

  * **Maintain trust and reputation** : Financial institutions rely heavily on their customers' trust. Operational disruptions or security breaches can severely erode this trust and cause customer attrition. Operational excellence helps to minimize these risks.
  * **Meet stringent regulatory compliance requirements** : Financial services are subject to numerous and complex regulations, such as the following:

    * [EU General Data Protection Regulation (GDPR)](https://gdpr-info.eu/art-1-gdpr/)
    * [EU Digital Operational Resilience Act (DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)
    * [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa)
    * Industry-specific regulations

Robust operational processes, monitoring, and incident management are essential for demonstrating compliance with regulations and avoiding penalties.

  * **Ensure business continuity and resilience** : Financial markets and services often operate continuously. Therefore, high availability and effective disaster recovery are paramount. Operational excellence principles guide the design and implementation of resilient systems. The [reliability pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability) provides more guidance in this area.

  * **Protect sensitive data** : Financial institutions handle vast amounts of highly sensitive customer and financial data. Strong operational controls, security monitoring, and rapid incident response are crucial in order to prevent data breaches and maintain privacy. The [security pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security) provides more guidance in this area.

  * **Optimize performance for critical applications** : Many financial applications, such as trading platforms and real-time analytics, demand high performance and low latency. To meet these performance requirements, you need highly optimized compute, networking, and storage design. The [performance optimization pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/performance-optimization) provides more guidance in this area.

  * **Manage costs effectively** : In addition to security and reliability, financial institutions are also concerned with cost efficiency. Operational excellence includes practices for optimizing resource utilization and managing cloud spending. The [cost optimization pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization) provides more guidance in this area.




The operational excellence recommendations in this document are mapped to the following core principles:

  * Define SLAs and corresponding SLOs and SLIs
  * Define and test incident management processes
  * Continuously improve and innovate



## Define SLAs and corresponding SLOs and SLIs

Across many FS organizations, the availability of applications is typically classified based on [recovery time objective (RTO) and recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) metrics. For business-critical applications that serve external customers, a service level agreement (SLA) might also be defined.

SLAs need a framework of metrics that represents the behavior of the system from the user-satisfaction perspective. [Site reliability engineering (SRE)](https://sre.google/sre-book/table-of-contents/) practices offer a way to achieve the level of system reliability that you want. Creating a framework of metrics involves defining and monitoring key numerical indicators to understand system health from the user's perspective. For example, metrics like latency and error rates quantify how well a service is performing. These metrics are called service level indicators (SLIs). Developing effective SLIs is crucial, because they provide the raw data that's necessary to objectively assess reliability.

To define meaningful SLAs, SLIs, and SLOs, consider the following recommendations:

  * Develop and define SLIs for each critical service. Set target values that define the acceptable performance levels.
  * Develop and define the service level objectives (SLO) that correspond to the SLIs. For example, an SLO might state that 99.9% of requests must have a latency that's less than 200 milliseconds.
  * Identify the internal remedial actions that must be taken if a service doesn't meet the SLOs. For example, to improve the resilience of the platform, you might need to focus development resources on fixing issues.
  * Validate the SLA requirement for each service and recognize the SLA as the formal contract with the service users.



### Examples of service levels

The following table provides examples of SLIs, SLOs, and SLAs for a payment platform:

**Business metric** | **SLI** | **SLO** | **SLA**  
---|---|---|---  
Payment transaction success | A quantitative measure of the percentage of all initiated payment transactions that are successfully processed and confirmed. **Example** : (number of successful transactions ÷ total number of valid transactions) × 100, measured over a rolling 5-minute window. | An internal target to maintain a high percentage of successful payment transactions over a specific period. **Example** : Maintain a 99.98% payment transaction success rate over a rolling 30-day window, excluding invalid requests and planned maintenance. | A contractual guarantee for the success rate and speed of payment transaction processing. **Example** : The service provider guarantees that 99.0% of payment transactions initiated by the client will be successfully processed and confirmed within one second.  
Payment processing latency | The average time taken for a payment transaction to be processed from initiation by the client to final confirmation. **Example** : Average response time in milliseconds for transaction confirmation, measured over a rolling 5-minute window. | An internal target for the speed at which payment transactions are processed. **Example** : Ensure that 99.5% of payment transactions are processed within 400 milliseconds over a rolling 30-day window. | A contractual commitment to resolve critical payment processing issues within a specified timeframe. **Example** : For critical payment processing issues (defined as an outage that affects more than 1% of transactions), the service provider commits to a resolution time of within two hours from the time when the issue is reported or detected.  
Platform availability | The percentage of time when the core payment processing API and user interface are operational and accessible to clients. **Example** : (total operational time − downtime) ÷ total operational time × 100, measured per minute. | An internal target for the uptime of the core payment platform. **Example** : Achieve 99.995% platform availability per calendar month, excluding scheduled maintenance windows. | A formal, legally binding commitment to clients regarding the minimum uptime of the payment platform, including consequences for failure to meet. **Example** : The platform will maintain a minimum of 99.9% availability per calendar month, excluding scheduled maintenance windows. If the availability falls below the minimum level, the client will receive a service credit of 5% of the monthly service fee for each 0.1% drop.  
  
Use SLI data to monitor whether systems are within the defined SLOs and to ensure that the SLAs are met. By using a set of well-defined SLIs, engineers and developers can monitor FS applications at the following levels:

  * Directly within the service that the applications are deployed on, such as GKE or Cloud Run.
  * By using logs that are provided by infrastructure components, such as the load balancer.



[OpenTelemetry](https://cloud.google.com/learn/what-is-opentelemetry) provides an open source standard and a set of technologies to capture all types of telemetry including metrics, traces, and logs. [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) provides a fully-managed, highly scalable backend for metrics and operation of Prometheus at scale.

For more information about SLI, SLO, and error budgets, see the [SRE handbook](https://sre.google/sre-book/service-level-objectives).

To develop effective alerting and monitoring dashboards and mechanisms, use [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) tools together with [Google Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). For information about security-specific monitoring and detection capabilities, see the [security pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security).

## Define and test incident management processes

Well-defined and regularly tested incident management processes contribute directly to the value, performance, security, and reliability of the FS workloads in Google Cloud. These processes help financial institutions meet their stringent regulatory requirements, protect sensitive data, maintain business continuity, and uphold customer trust.

Regular testing of incident management processes provides the following benefits:

  * **Maintain performance under peak loads** : Regular performance and load testing help financial institutions ensure that their cloud-based applications and infrastructure can handle peak transaction volumes, market volatility, and other high-demand scenarios without performance degradation. This capability is crucial for maintaining a seamless user experience and meeting the demands of financial markets.
  * **Identify potential bottlenecks and limitations** : Stress testing pushes systems to their limits, and it enables financial institutions to identify potential bottlenecks and performance limitations before they affect critical operations. This proactive approach enables financial institutions to adjust their infrastructure and applications for optimal performance and scalability.
  * **Validate reliability and resilience** : Regular testing, including [chaos engineering](https://cloud.google.com/blog/products/databases/chaos-testing-spanner-improves-reiliability?e=48754805) or simulated failures, helps to validate the reliability and resilience of financial systems. This testing ensures that the systems can recover gracefully from failures and maintain high availability, which is essential for business continuity.
  * **Perform[effective capacity planning](https://static.googleusercontent.com/media/sre.google/en//static/pdf/login_winter20_10_torres.pdf)**: Performance testing provides valuable data on resource utilization under different load conditions, which is crucial for accurate capacity planning. Financial institutions can use this data to proactively anticipate future capacity needs and to avoid performance issues due to resource constraints.
  * **Deploy new features and code changes successfully** : Integrating automated testing into CI/CD pipelines helps to ensure that changes and new deployments are thoroughly validated before they're released into production environments. This approach significantly reduces the risk of errors and regressions that could lead to operational disruptions.
  * **Meet regulatory requirements for system stability** : Financial regulations often require institutions to have robust testing practices to ensure the stability and reliability of their critical systems. Regular testing helps to demonstrate compliance with these requirements.



To define and test your incident management processes, consider the following recommendations.

### Establish clear incident response procedures

A well-established set of [incident response procedures](https://sre.google/resources/practices-and-processes/incident-management-guide/) involves the following elements:

  * Roles and responsibilities that are defined for incident commanders, investigators, communicators, and technical experts to ensure effective and coordinated response.
  * Communication protocols and escalation paths that are defined to ensure that information is shared promptly and effectively during incidents.
  * Procedures that are documented in a runbook or playbook that outlines the steps for communication, triage, investigation, and resolution.
  * Regular training and preparation that equips teams with the knowledge and skills to respond effectively.



### Implement performance and load testing regularly

Regular [performance and load testing](https://sre.google/sre-book/testing-reliability/) helps to ensure that cloud-based applications and infrastructure can handle peak loads and maintain optimal performance. Load testing simulates realistic traffic patterns. Stress testing exercises the system to its limits to identify potential bottlenecks and performance limitations. You can use products like [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) and load testing services to simulate real-world traffic. Based on the test results, you can adjust your cloud infrastructure and applications for optimal performance and scalability. For example, you can adjust resource allocation or tune application configurations.

### Automate testing within CI/CD pipelines

Incorporating automated testing into your CI/CD pipelines helps to ensure the quality and reliability of cloud applications by validating changes before deployment. This approach significantly reduces the risk of errors and regressions and it helps you to build a more stable and robust software system. You can incorporate different types of testing in your CI/CD pipelines, including unit testing, integration testing, and end-to-end testing. Use products like [Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) to create and manage your CI/CD pipelines.

## Continuously improve and innovate

For financial services workloads in the cloud, migrating to the cloud is merely the initial step. Ongoing enhancement and innovation are essential for the following reasons:

  * **Accelerate innovation** : Take advantage of new technologies like AI to improve your services.
  * **Reduce costs** : Eliminate inefficiencies and optimize resource use.
  * **Enhance agility** : Adapt to market and regulatory changes quickly.
  * **Improve decision making** : Use data analytics products like BigQuery and Looker to make informed choices.



To ensure continuous improvement and innovation, consider the following recommendations.

### Conduct regular retrospectives

[Retrospectives](https://sre.google/sre-book/postmortem-culture/) are vital for continuously improving incident response procedures, and for optimizing testing strategies based on the outcomes of regular performance and load testing. To ensure that retrospectives are effective, do the following:

  * Give teams an opportunity to reflect on their experiences, identify what went well, and pinpoint areas for improvement.
  * Hold retrospectives after project milestones, major incidents, or significant testing cycles. Teams can learn from both successes and failures and continuously refine their processes and practices.
  * Use a structured approach like the [start-stop-continue](https://docs.cloud.google.com/architecture/framework/operational-excellence/continuously-improve-and-innovate#conduct_regular_retrospectives) model to ensure that the retrospective sessions are productive and lead to actionable steps.
  * Use retrospectives to identify areas where automation of change management can be further enhanced to improve reliability and reduce risks.



### Foster a culture of learning

A culture of learning facilitates safe exploration of new technologies in Google Cloud, such as AI and ML capabilities to enhance services like fraud detection and personalized financial advice. To promote a culture of learning, do the following:

  * Encourage teams to experiment, share knowledge, and learn continuously.
  * Adopt a blameless culture, where failures are viewed as opportunities for growth and improvement.
  * Create a psychologically safe environment that lets teams take risks and consider innovative solutions. Teams learn from both successes and failures, which leads to a more resilient and adaptable organization.
  * Develop a culture that facilitates sharing of knowledge gained from incident management processes and testing exercises.



### Stay up-to-date with cloud technologies

Continuous learning is essential for understanding and implementing new security measures, leveraging advanced data analytics for better insights, and adopting innovative solutions that are relevant to financial services.

  * Maximize the potential of Google Cloud services by staying informed about the latest advancements, features, and best practices.
  * When new Google Cloud features and services are introduced, identify opportunities to further automate processes, enhance security, and improve the performance and scalability of your applications.
  * Participate in relevant conferences, webinars, and training sessions to expand your knowledge and understand new capabilities.
  * Encourage team members to obtain [Google Cloud certifications](https://cloud.google.com/learn/certification) to help ensure that the organization has the necessary skills for success in the cloud.



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)

[ Next Security  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
