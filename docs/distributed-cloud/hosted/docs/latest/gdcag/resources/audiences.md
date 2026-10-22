---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences/
title: Documentation audiences for Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:48.326645+00:00
---

# Documentation audiences for Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Documentation audiences for Google Distributed Cloud air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the audiences for Google Distributed Cloud (GDC) air-gapped documentation to help you find information relevant to your role.

This page details key audience groups such as the infrastructure operator group, platform administrator group, and application operator group. You'll find information about the level of the [GDC resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy) they operate within, along with a list of example responsibilities for teams in each audience group within the context of Distributed Cloud.

**Important** : Every organization defines its roles and responsibilities differently. Some tasks and responsibilities might be shared by multiple roles. The examples listed are typical and don't represent a full list.

## Understand the intended audience for GDC documentation

The Google Distributed Cloud air-gapped documentation supports different audience groups and is structured to address their unique information needs. You'll see references to the following audience groups in the documentation:

  * Infrastructure operator group: Teams within the infrastructure operator group are responsible for delivering and supporting GDC services. They can oversee the full lifecycle of GDC, from hardware setup and management to infrastructure deployment and ongoing operations of the infrastructure in support of end users, such as Platform Administrator or Application Operator.
  * Platform administrator group: Teams within the platform administrator group manage the GDC environment after deployment. They define, create, and oversee policies to manage access and resources to enable effective application and service development.
  * Application operator group: Teams within the application operator group are responsible for the full lifecycle of services and applications deployed within GDC environments. They develop, manage, and monitor applications and services to support an organization's internal and external users.



## Infrastructure operator group

Teams within infrastructure operator groups support the delivery, configuration, and operation of GDC at the **universe level** , providing support for core systems that make up the GDC infrastructure. For more information about the GDC universe level, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview#deployment-hierarchy-overview). They are responsible for the entire infrastructure operation lifecycle of Google Distributed Cloud air-gapped, which includes pre-deployment hardware testing, infrastructure deployment, and ongoing infrastructure management. The scope of infrastructure operator group typically covers the following tasks:

  * Gathering requirements for the business' operational needs and limitations
  * Designing the solution architecture
  * Implementing the underlying infrastructure for GDC 
    * Setting up the hardware stack
    * Deploying the initial zones
    * Configuring deployment pipelines and tools
    * Setting up and configuring networking infrastructure and services, storage services, and compute
    * Troubleshooting infrastructure issues, updating the infrastructure, and responding to incidents
  * Onboarding the organization to the GDC environment
  * Providing customer support to the platform administrator group
  * Providing centralized support for the infrastructure 
    * Providing technical assistance
    * Documenting common issues and work arounds
  * Maintaining the GDC air-gapped environment 
    * Monitoring security alerts and logs
    * Escalating support to data center operating teams
    * Performing system upgrades and regular system patching, updates, and vulnerability remediation
  * Setting up and maintaining billing for the organization



## Platform administrator group

Teams within the platform administrator group manage the GDC environment after deployment at both the **organizational level** and **project level.** They're responsible for overseeing resources to enable effective application and service deployment within the GDC environment. They plan and define the resource hierarchy to reflect the organization's structure and manage resource allocation through policies, quotas, and access control across multiple zones. The scope of the platform administrator group typically covers the following tasks:

  * Considering the requirements for the business' operational needs and limitations
  * Planning and defining the resource hierarchy
  * Managing user identities and access control to resources
  * Configuring and managing secure networks
  * Viewing logs and monitoring
  * Implementing security measures within the air-gapped environment
  * Establishing automated build, test, and deployment processes
  * Provisioning and configuring compute, networking, storage to support applications
  * Monitoring performance, reliability, and security



The following audiences are commonly a part of the platform administrator group:

  * IT administrators
  * Billing ops
  * Database administrators
  * Security engineer
  * Network administrator
  * Compliance auditor



### IT administrator

IT administrators maintain, configure, and operate an organization's IT infrastructure, with the goal of ensuring its security, efficiency, and performance by keeping computer systems and servers up-to-date. Common tasks include the following examples::

  * Configuring, monitoring, and managing the organization's IT infrastructure
  * Maintaining backup and performing recovery procedures
  * User provisioning
  * Defining the resource hierarchy
  * Monitoring for performance, reliability, and security issues
  * Responding to audits



### Billing operator

Billing operators set up, process, and manage the billing cycle for the organization, with the goal of ensuring accurate invoicing, timely payments, and billing transparency. Common tasks include the following examples:

  * Reviewing invoices and usage data
  * Maintaining accurate records
  * Managing payments



### Database administrator

Database administrators maintain physical databases for the entire organization, with the goal of maintaining consistent performance, robust security, continuous data availability, and ensuring data sovereignty. Common tasks include:

  * Designing and implementing databases
  * Plan maintenance windows
  * Optimizing databases
  * Evaluating and planning for future capacity



### Security engineer

Security engineers design, implement, and manage the entire organization's security infrastructure, with the goal of ensuring robust protection. Common tasks include the following examples:

  * Identifying compliance requirements for the organization
  * Designing the overall security infrastructure
  * Configuring security systems based on industry and compliance requirements
  * Managing security systems and tools across the organization
  * Conducting vulnerability assessments
  * Resolving security and vulnerability issues



### Network administrator

Network administrators install, configure, maintain, and troubleshoot the organization's network infrastructure. Their goal is to ensure that the network runs efficiently and securely to enable reliable access to projects and resources within the GDC environment. Common tasks include the following examples:

  * Setting up the network, including VPNs and load balancers.
  * Managing network performance
  * Troubleshooting network issues and managing outbound traffic
  * Configuring network policies
  * Overseeing network security



### Compliance auditor

Compliance auditors evaluate an organization's adherence to policies, regulatory requirements, and industry standards, with the goal of ensuring that an organization operates within legal and ethical boundaries while maintaining transparency. Common tasks include the following examples:

  * Auditing processes and verifying compliance
  * Reviewing documentation and records
  * Identifying instances of non-compliance
  * Developing recommendations and preventative actions.



## Application operator group

Teams within the application operator group manage workload, application, and project life cycles at the **project level**. Their goal is to support a project's internal and external users by ensuring efficient and reliable delivery of services and applications running within GDC environments. The scope of application operations typically covers the following tasks:

  * Developing and testing applications in air-gapped environments
  * Deploying services and applications that meet organizational requirements
  * Monitoring services and application to minimize disruptions
  * Optimizing services and applications running within GDC
  * Troubleshooting issues affecting applications



The following audiences are commonly a part of the application administrator group:

  * Application developer
  * Developer operations (DevOps)
  * Data scientist
  * Machine learning (ML) engineer



### Application developer

Developers design, test, and maintain applications and services that run within air-gapped environments. They translate organizational requirements and specifications into functional applications for internal and external users. Common tasks include the following examples:

  * Gathering design specifications for applications and services
  * Designing applications and services
  * Building applications and services
  * Reviewing code
  * Deploying and maintaining applications
  * Debugging and troubleshooting application issues



### Developer operations (DevOps)

DevOps focus on tasks that bridge software development and IT operations, optimizing the efficiency, security, and reliability of deployment pipelines supporting the development cycle. Common tasks include the following examples:

  * Setting development pipelines and infrastructure
  * Maintaining the development infrastructure
  * Automating deployments
  * Monitoring the reliability of development environments
  * Evaluating the scalability of the deployment pipeline
  * Troubleshooting deployment issues



### Data scientists

Data scientists analyze complex data and identify meaningful trends and insights to inform organizational decisions and solve challenges. Their goal is to collaborate with other teams to inform decisions. Common tasks include the following examples:

  * Gathering and analyzing complex datasets
  * Informing machine learning models
  * Collaborating with other teams to inform how to optimize systems
  * Evaluating the performance of existing models and systems
  * Communicating insights, trends, and findings



### ML engineer

ML engineers design, build, and prepare ML models for deployment, converting theoretical models into operational solutions for the organization. Their goal is to implement consistent methodologies that standardize ML development and operations, ensuring solutions are reliable, efficient, and scalable. Common tasks include the following examples:

  * Setting up the ML development environment
  * Deploying machine learning models
  * Improving the accuracy and efficiency of machine learning models
  * Setting up data storage and resources required for ML
  * Maintaining ML implementations



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
