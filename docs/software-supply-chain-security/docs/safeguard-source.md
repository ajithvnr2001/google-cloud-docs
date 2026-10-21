---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-source/
title: Safeguard source \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:12.629315+00:00
---

# Safeguard source  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Safeguard source Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for managing software source code.

A fundamental step software teams take to manage their source is adopting a version control system (VCS). Version control systems provide history and auditability for changes. Hosted version control systems such as GitHub provide additional benefits such as availability, stability, security controls, integrated code review tools, and integration with other cloud services.

While most teams are using version control today, there are many ways to configure a version control system and its integrations with other parts of the CI/CD pipeline.

This document explores software supply chain security considerations for configuring a version control system. It describes best practices from [Supply-chain Levels for Software Artifacts](https://slsa.dev), a framework for safeguarding your software supply chain. The framework includes requirements at several levels to help you implement changes incrementally, including [source requirements](https://slsa.dev/spec/v0.1/requirements#source-requirements).

A version control system with change history and immutable revisions is a SLSA level 2 requirement. We recommend alignment with SLSA level 2 as a starting baseline level for your software supply chain.

At SLSA level 3, source and build platforms adhere to stronger security requirements, including verified source history and source retention policy. SLSA level 4 adds two-person reviews to source requirements.

## Use version control for more than your application source

Storing application source in version control is a well-established practice when historical reviews and audit are necessary. However there are other types of source that also benefit from version control, including configuration, policy, and data. This includes any files that:

  * Impact your compute infrastructure's availability and security
  * Require collaboration to finalize
  * Require a repeatable approval process
  * Require a change history



Some examples are:

  * **Infrastructure-as-code** : Organizations that want to manage their infrastructure in a scalable and secure way use infrastructure-as-code as a key methodology. For example, you can store Terraform modules in version control that [create Artifact Registry repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#terraform).
  * **Configuration management** : Configuration management is similar to infrastructure-as-code, but focuses on managing application configuration with tools such as Ansible, Puppet, and Chef. You store and manage application configuration files in your version control system.
  * **Database configurations and migration scripts** : Store the configuration and scripts for both your product databases and analytics or logging databases.
  * **Jupyter notebooks** : There are a variety of ways to work with notebooks stored in GitHub, including the [extension for JupyterLab](https://github.com/jupyterlab/jupyterlab-git), [Colaboratory](https://research.google.com/colaboratory/), and [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/save-to-github)
  * **Security policies** : Store policy files for automated policy enforcement. For example, you can store Gatekeeper policies that [permit or deny deployment behavior in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper) or [Sentinel policies](https://docs.hashicorp.com/sentinel) that prevent Terraform from provisioning infrastructure that is in violation of policy.



Version control is one of the [technical capabilities](https://dora.dev/devops-capabilities/technical/version-control/) identified by [DORA DevOps research](https://dora.dev/) that drives higher software delivery and organizational performance. Storing your scripts, source code, and configuration files in version control helps you to reproduce and recover environments, trace and audit changes, and respond to defects quickly.

## Repository configuration

Repositories are the fundamental logical unit for organizing code and related roles, permissions, integrations and approvals.

Problems that can occur with repository configuration include:

  * Repository configuration is not standardized, so it becomes difficult to ensure that repository security is appropriate to the application it represents, particularly in the common scenario when an organization has hundreds or thousands of repositories.
  * Whoever creates the repository becomes an owner with full administrative permissions, including the ability to perform merges with no other reviewers.
  * Integrating repositories with code analysis, build servers, issue trackers, notification services, and other parts of CI/CD infrastructure can be considerable work. Having a standard way to create and set up repositories saves repetitive work and supports best practices.



To address these problems, best practices include

  * Set up repositories with an automated, repeatable, security-conscious process. For example, you can set up Terraform modules that incorporate the security requirements of the application the repository is for. High-security applications require more and different merge approvers than lower-security apps.
  * Create a way for repository administrators to select from a set of repository configuration templates that drive new repository setup rather than configuring each repository from scratch. These templates should reflect the different security levels of your applications, and be synchronized with the user identities that are required for each security level. In practice this usually means using a hierarchical [identity and access control (IAM) system](https://en.wikipedia.org/wiki/Identity_management) that reflects the applications and infrastructure in your organization and the users who are responsible for them.
  * Require centralized identity management with multi-factor authentication for repository users. 
    * Centralized identity management ensures that when users leave the organization or move to new teams you maintain least privilege around source management.
    * Multi-factor authentication significantly reduces the risk of phishing and other types of attacks on your source. Two-factor authentication is one of the SLSA level 4 requirements for code approvers.
  * Limit repository owners to a small number of trusted employees. This might require integrating version control with an identity management system and moving the ability to set policies higher in the organization. If possible, remove the ability for repository owners to perform merges without a second reviewer.



## Code review

Code review is the primary way that organizations maintain the quality and security of their software. Code review tries to address various failure modes such as:

  * Introduction of code with software defects or an inflexible design.
  * Poorly defined APIs
  * Introduction of security issues due to insecure code written by the developer
  * Introduction of security issues due to adding third-party libraries that are insecure or could become insecure.



Some ways to mitigate risk include:

  * Implement [test automation](https://dora.dev/devops-capabilities/technical/test-automation/) throughout the software lifecycle. Automated testing that triggers when you commit source to the version control system is a way for developers to quickly get feedback on issues found by the tests.
  * Make the number and identity of reviewers appropriate to the application's security level. For instance, an intranet app with low usage will have lower security requirements than a publicly facing business critical application.
  * Assign reviewers based on both technical expertise and the trust level required for the change in the commit. The reviewer should be an expert in the language being reviewed, the systems the code interacts with, and the security risks in this class of application. The technical expertise requirement has many dimensions. For example: 
    * Is the code readable?
    * Is it secure?
    * Is it using appropriate third-party libraries?
    * Is a process of securing third-party libraries in place?
    * Is the code composable?
    * Is the API design following best practices?
  * Reviews should not be a bureaucratic step, but a continuing conversation around best practices. Create checklists, style guides, and design standards around each part of your technology stack, along with educational programs for new developers. Some IDEs such as VS Code and IntelliJ provide linters that can automatically flag programmatic or stylistic errors. Linters help developers create more consistent code and let code reviewers focus more on issues that are not easy to identify with automated checks.

[Developing Secure Software](https://training.linuxfoundation.org/training/developing-secure-software-lfd121/) is a free online course created by [Open Source Security Foundation](https://openssf.org/) (OpenSSF). It describes foundational software development practices in the context of software supply chain security.

  * Perform code reviews with feature branch pull requests as soon as an individual developer is ready. Don't wait until right before a new release is placed into test to do security checks and code review.

  * Integrating vulnerability scanning, including scanning for third party libraries, into pull requests and IDEs helps identify problems as soon as possible. [On-Demand Scanning API](https://docs.cloud.google.com/container-analysis/docs/on-demand-scanning-howto) in Google Cloud lets you scan containers locally for vulnerabilities.

  * Integrate pre-merge automated tests so that developers can identify and fix changes that will break the application. [Learn more about test automation](https://dora.dev/devops-capabilities/technical/test-automation/).




## Merge approvals

In continuously integrated CI/CD pipelines, merging code into a production branch may result in downstream changes including automated build and rollout. For this reason, securing who can merge is a critical part of securing software deployments. Considerations include:

  * Set up protected branch owners on your production branches. The number and identity of those allowed to merge should be appropriate to the security requirements of the application. SLSA level 4 requires two strongly authenticated approvers, but the number of approvers should be appropriate to the content of the repository.
  * Tightly control identities of repository owners since in most version control systems, they can perform merges by themselves.
  * Separate deployment and merge approval processes for multi-repository and multi-artifact rollouts.



## Tools to secure development

Google Cloud provides a set of modular capabilities and tools that you can use to improve the security posture of your software supply chain. The following components help protect software source code:

  * **Cloud Workstations (Preview)**

Cloud Workstations provides fully-managed development environments on Google Cloud. It enables IT and security administrators to easily provision, scale, manage and secure their development environments and allows developers to access development environments with consistent configurations and customizable tooling.

Cloud Workstations helps with shifting security left by enhancing the security posture of your application development environments. It has security features such as VPC Service Controls, private ingress or egress, forced image update and Identity and Access Management access policies. For more information, see the [Cloud Workstations documentation](https://docs.cloud.google.com/workstations/docs/concepts).

  * **Cloud Code source protect (Preview)**

[Cloud Code](https://docs.cloud.google.com/code/docs) provides IDE support to create, deploy and integrate applications with Google Cloud. It enables developers to create and customize a new application from sample templates and run the finished application. Cloud Code source protect gives developers real-time security feedback, such as identification of vulnerable dependencies and license reporting, as they work in their IDEs. It provides quick and actionable feedback that allows developers to make corrections to their code at the beginning of the software development process.

**Feature availability** : Cloud Code source protect is not available for public access. To get access to this feature, see the [access request page](https://docs.google.com/forms/d/e/1FAIpQLSeBUSpLmXsvGhnKfYx7g-Cmd-oth9yXbUTZNFIL87cdGIu2RQ/viewform?resourcekey=0-tR1FN8wQtdR43sJixQL3jw).




## What's next

  * Learn the [best practices to safeguard builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds).
  * Learn the [best practices to safeguard dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).
  * Learn the [best practices to safeguard deployments](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-deploys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
