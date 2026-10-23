---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks/
title: Common GKE user roles and tasks \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:14.206319+00:00
---

# Common GKE user roles and tasks  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Common GKE user roles and tasks Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In the GKE documentation, each document is often written for a specific need or to help solve a business problem that you might have. These needs are often the responsibility of various teams and roles in your organization. This document lists some of the common user roles, responsibilities, and tasks that are referenced in our content.

You don't need to read the entire document to understand our content. However, mapping your unique role and responsibilities to the examples described in this document can help you better identify documentation that applies to you.

This list of example user roles isn't exhaustive, as each organization is different. Your role, responsibilities, and tasks might not align exactly with the following common examples. And, the names used in your organization might differ from the names used in this document. This document helps you find the roles or responsibilities that most closely resemble your own.

## Common role archetypes

The following high-level areas of common user roles are often referenced in our content:

  * Admins and architects
  * Operators
  * Developers
  * Security specialists
  * Networking specialists
  * Data and AI specialists
  * Storage specialists



## Admins and architects

Admins and architects administer and architect cloud platforms and products. The following common user roles are part of the high-level Admins and architects area:

  * Cloud architects
  * IT administrators
  * Identity and account admins



This section explains the common user roles that are part of the Admins and architects area.

### Cloud architects

Cloud architects are responsible for determining the appropriate combination of IaaS, PaaS, SaaS, and on-premises components necessary to serve product and business objectives. They consider efficiency, cost, security, and governance constraints in architecting solutions.

Common tasks of Cloud architects include the following examples:

  * Define IT solutions and system architecture in accordance with company strategy in coordination with key stakeholders.
  * Optimize systems architecture and resources to ensure the lowest total cost of ownership for their company or business unit.
  * Re-architect their current architecture to ensure they can migrate seamlessly with their existing integrations and third-party services.
  * Define strategy and system architecture for migration to cloud, including applications and databases.



### IT administrators

IT administrators are responsible for the upkeep, configuration, and reliable operation of an organization's computer systems, servers, and data security systems. They ensure that the organization's IT infrastructure is secure, efficient, and up to date.

Common tasks of IT administrators include the following examples:

  * Set up, monitor, and manage cloud infrastructure, including backup infrastructure.
  * Define and enforce organization-level backup policies.
  * Set up alerting and monitor IT systems for performance and vulnerabilities.
  * Manage organization policies, user and group provisioning, and set resource hierarchy, quota policies.
  * Receive and respond to compliance issues and audits across platform.
  * Evaluate backup solutions and collaborate with IT and infrastructure owners on choosing a solution.
  * Ensure all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to enforce compliance, such as backup policies.



### Identity and account admins

Identity and account admins administer organization policies, user policies, and user access. They manage the identity environment at their company, such as Active Directory, and provision users and groups to access platforms, tools, and resources based on their role and function policies.

Common tasks of Identity and account admins include the following examples:

  * Create user accounts and manage integration into IT tools such as Google Cloud and organizational apps.
  * Build and deploy integrations between applications and identity tools.
  * Manage and administer identity infrastructure tools.
  * Troubleshoot, diagnose, and remediate issues or outages associated with IAM tools.
  * Manually provision access for critical or high-risk applications.
  * Manage processes related to identity and access provisioning.
  * Manage job-based user groups and group settings.
  * Define and create custom user roles if needed.
  * Create and manage policies related to user permissions.



## Operators

Operators manage and optimize the deployment and operation of applications. The following common user roles are part of the high-level Operators area:

  * Platform admins and operators
  * App operators and site reliability engineering (SRE)
  * DevOps



This section explains the common user roles that are part of the Operators area.

### Platform admins and operators

Platform admins and operators are responsible for provisioning and creating resources for application teams, and managing the central infrastructure for their organization.

Common tasks of Platform admins and operators include the following examples:

  * System administration.
  * Lifecycle management of the underlying tech infrastructure.
  * Implementation of GitOps.



### App operators and SRE

App operators and site reliability engineering (SRE) are responsible for ensuring that software systems are reliable, scalable, and performant. They use software and automation to manage and monitor systems, and they work closely with developers to ensure that changes to code don't impact reliability.

Common tasks of App operators and SRE include the following examples:

  * Set-up 
    * Publish and manage APIs for their application or service.
    * Plan capacity and infrastructure needs.
    * Create alerting policies.
  * Monitor 
    * Monitor the health of deployed applications or services, such as for service level objective (SLO) compliance, and sometimes also maintain their underlying infrastructure.
    * Monitor the health of ongoing releases.
    * Respond to alerts and pages when SLOs or applications fail.
    * Debug to find root cause.
  * Deploy 
    * Deploy apps and services to production.
    * Grant permission to deploy applications or services to production.
  * Test and deploy new service instances, versions, bug fixes, or security patches.
  * Build and use release pipeline and continuous integration / continuous development (CI/CD) stack.



### DevOps

The role of DevOps combines development and operations to improve the speed, security, and efficiency of software development and delivery. They are responsible for ensuring the reliability and performance of cloud applications, such as establishing service-level objectives (SLO), assessing service-level indicators (SLI), and identifying and resolving issues that may compromise SLO targets.

Common tasks of DevOps include the following examples:

  * Set up DevOps pipelines and infrastructure.
  * Maintain and modernize DevOps pipelines.
  * Automate deployments.
  * Templating of declarative configuration.
  * Ongoing monitoring of deployments.



## Developers

Developers write code to build applications and platform infrastructure. The following common user roles are part of the high-level Developers area:

  * Application developers
  * Platform engineers



This section explains the common user roles that are part of the Developers area.

### Application developers

Application developers write the code for applications that eventually run on a cloud platform like Google Cloud. Organizations rely on developers to add features to their digital platforms and add value for their end users.

Common tasks of Application developers include the following examples:

  * Write application and test code.
  * Debug and troubleshoot code.
  * Review other developers' code.
  * Add new features to the application and commit them to version control.
  * Create and present design documents to engineering and product colleagues.
  * Learn and evaluate new technologies.



Depending on the size and maturity of the organization, they might also be responsible for the following tasks:

  * Manage DevOps pipelines and processes.
  * Manage application security.
  * Provision and configure cloud resources.
  * Perform data management for the application, such as taking snapshots or backup and restoring an application in case of a failure.
  * Research and evaluate new technologies.
  * Find and fix problems in production.
  * Respond to system health alerts, such as on-call duties.
  * Define and maintain schemas of databases for data storage and retrieval.
  * Query the database to be used in applications and services.



### Platform engineers

Platform engineers are responsible for building centralized platforms of services and tools to help make the development process more efficient, reliable, secure, and compliant with regulations.

Common tasks of Platform engineers include the following examples:

  * Evaluate new technologies for the organization.
  * Oversee cloud, application, or platform architecture of their organization.
  * Create reusable pipelines, processes, dashboards, and tools for application teams.
  * Manage which technologies can and cannot be used by application teams to develop applications and services.
  * Test and rollout new versions of platform and infrastructure.
  * Capacity management and cost optimizations.
  * Determine what infrastructure services the organization will provide for application teams.
  * Provision new database resources and configure them to ensure availability, performance, compliance, and manage costs.
  * Establish and maintain connections between databases and the applications and services that need the data.



## Security specialists

Security specialists define, govern and implement policies and procedures to protect an organization's data from unauthorized access. The following common user roles are part of the high-level Security specialists area:

  * Security engineers



This section explains the common user roles that are part of the Security specialists area.

### Security engineers

Security engineers collaborate with other user roles to identify compliance requirements based on industry and regional regulations. They manage multiple security functions and are responsible for implementing configurations of systems to meet defined requirements.

Common tasks of Security engineers include the following examples:

  * Define how systems are configured to ensure compliance with regulations and requirements.
  * Implement changes and updates to systems.
  * Develop and maintain security policies.
  * Support the resolution of security issues or vulnerabilities which need strategic assistance, such as incidents and issues escalated from support.
  * Run scans and manage ongoing security monitoring.
  * Manage multiple security functions and tools.



## Networking specialists

Networking specialists define, implement and maintain the network architecture. The following common user roles are part of high-level Networking specialists area:

  * Network architects
  * Network administrators
  * Network engineers



This section explains the common user roles that are part of the Networking specialists area.

### Network architects

Network architects are technical professionals who design, build, and maintain cloud-based networks. They are responsible for ensuring that cloud networks are reliable, secure, scalable, and performant. Network architects typically have a deep understanding of cloud networking technologies, services, and best practices.

Common tasks of Network architects include the following examples:

  * Design and architect the network for their organization.
  * Develop network specifications.
  * Plan network security.
  * Network maintenance.



### Network administrators

Network administrators are responsible for the installation, configuration, maintenance, and troubleshooting of computer networks. They play a crucial role in ensuring that an organization's network is running smoothly and efficiently, allowing employees to access the resources they need to do their jobs.

Common tasks of Network administrators include the following examples:

  * Design and architect the network for their organization.
  * Monitor network performance.
  * Set up new networks.
  * Manage network security.
  * Troubleshoot and resolve network issues.



### Network engineers

Network engineers are in charge of network implementation, including building infrastructure and networks, replacing equipment, adding new equipment, and working on new requirements and services.

Common tasks of Network engineers include the following examples:

  * Install, configure, and support network equipment.
  * Establish networking environment by designing system configuration and directing system installation.
  * Implement data security systems such as firewalls.
  * Perform network maintenance.
  * Analyze and resolve network performance issues.



## Data and AI specialists

Data and AI specialists collect, organize, and analyze data to inform business decisions and to develop competitive AI solutions. The following common user roles are part of the high-level Data and AI specialists area:

  * Data engineers
  * Data administrators
  * Data scientists
  * Machine learning (ML) engineers



This section explains the common user roles that are part of the Data and AI specialists area.

### Data engineers

Data engineers bring data from data sources and make it available to the right people. They might also be responsible for building self-service tools for others to get the data that they need on their own.

Common tasks of Data engineers include the following examples:

  * Set up and operate data infrastructure.
  * Build, maintain, and monitor data pipelines.
  * Write data in and out of enterprise data warehouses (EDWs) and databases.
  * Orchestrate different data workloads.
  * Develop and implement data models and perform data transformations.
  * Build tools and processes that enable data consumers to access data they need independently.
  * Deploy workloads that are ready for production, such as machine learning (ML), business intelligence (BI), or ETL (extract, transform, load) and ELT (extract, load, transform).



### Data administrators

Data administrators ensure that their company's data solutions are productive, efficient, and cost effective.

Common tasks of Data administrators include the following examples:

  * Configure data environments.
  * Manage data backup and recovery.
  * Optimize systems for capacity and efficiency.
  * Monitor performance metrics and troubleshoot.
  * Manage and optimize cost.
  * Run audits.
  * Manage metadata and other data assets.
  * Manage and implement data policies.
  * Manage access and permissions.
  * Apply security tags to relevant data.



### Data scientists

Data scientists range in skill level from shallow ML (XGBoost, Scikit), to deep ML with PyTorch and TensorFlow. Their aim is to build the most optimal model to solve a business problem. They value velocity and collaboration, and work closely with data science peers and business experts.

Common tasks of Data scientists include the following examples:

  * Analyze data, create statistical and ML models.
  * Create, train, and improve ML algorithms and models.
  * Evaluate third-party ML APIs for price and quality.
  * Clean data sets for use in statistical models.
  * Consult on defining business goals and objectives through use of ML.



### Machine learning (ML) engineers

Machine learning (ML) engineers are core MLOps users, with expertise in code, ML, and deployment. Their goal is to standardize ML practice and operationalize models for deployment.

Common tasks of Machine learning (ML) engineers include the following examples:

  * Environment setup
  * Deployment
  * Post-production
  * Governance



## Storage specialists

Storage specialists provision and manage storage in the cloud and backup infrastructure. The following common user roles are part of the high-level Storage specialists area:

  * Storage administrators
  * Backup and disaster recovery (DR) administrators
  * On-site ops



This section explains the common user roles that are part of the Storage specialists area.

### Storage administrators

Storage administrators provision and manage the storage infrastructure to ensure data security and compliance, while also monitoring performance, usage, and spend. As part of these responsibilities they manage storage-related org policies, permissions, and quotas.

Common tasks of Storage administrators include the following examples:

  * Create and allocate storage.
  * Configure and manage data security, protection, and access and permissions.
  * Configure and manage lifecycle policies and quotas.
  * Monitor storage performance, usage, and spend.
  * Connect or help connect storage with other services, such as Google Cloud.



### Backup and disaster recovery (DR) administrators

Backup and disaster recovery (DR) administrators define, implement, monitor, and troubleshoot baseline data protection policies for all resources within their projects.

Common tasks of Backup and disaster recovery (DR) administrators include the following examples:

  * Ensure backups are secure and protected according to organizational and legal policies.
  * Define and create backup plans for all applications and databases.
  * Manage and perform backup and recoveries across the organization.
  * Enable application teams to perform backups and recoveries, within certain guardrails.
  * Control who can do what when it comes to backup and recovery, in collaboration with Identity and account admins.
  * Monitor and troubleshoot failed backups.
  * Design and execute disaster recovery plans for applications.
  * Organize and participate in DR tests and exercises.
  * Create reports to document compliance in coordination with a centralized governance team.
  * Create playbooks and guidelines for applications teams to provision and protect their resources.
  * Ensure data is sufficiently protected against disasters and accidental deletion.



### On-site ops

On-site ops set up data appliances in data centers or server rooms to facilitate the successful transfer of data. This role also helps with appliance maintenance so that engineers can move and deploy apps and models successfully.

Common tasks of On-site ops include the following examples:

  * Receive device when it arrives at the customer site and verify the hardware and software integrity to make sure they haven't been tampered with.
  * Power up, connect, and set up the devices or appliances on site so that teams can move data successfully.
  * Monitor device or appliance status on site and help with hardware maintenance and troubleshooting.
  * Prepare and return the device to Google after data migration is complete, or at the end of the device lifecycle.



## What's next?

[Explore Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/learn#gke)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
