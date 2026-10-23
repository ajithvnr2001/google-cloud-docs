---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/practices/
title: Protect your software supply chain \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:09.228932+00:00
---

# Protect your software supply chain  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Protect your software supply chain Stay organized with collections  Save and categorize content based on your preferences. 

This documentation focuses primarily on best practices that support protecting your software across processes and systems in your software supply chain. It also includes information about how to implement some of the practices on Google Cloud.

  * [Safeguarding source integrity](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-source)
  * [Safeguarding build integrity](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds)
  * [Managing dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies)
  * [Safeguarding deployments](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-deploys)



There are additional considerations for protecting your software that span the software lifecycle or are foundational development practices that support software supply chain security. For example:

  * Controlling physical and remote access to systems.
  * Implementing audit, monitoring, and feedback mechanisms so that you are able to quickly identify and respond to threats and non-compliance with policy.
  * Foundational coding practices including design, input validation, output to untrusted systems, data processing, code analysis, and cryptography.
  * Foundational DevOps practices beyond ones mentioned in this documentation, including technical approaches, team process, and organizational culture.
  * Adherence to software licenses terms, including open source licenses for direct and transitive dependencies.

Some open source licenses have restrictive license terms that are problematic for commercial software. In particular, some licenses require you to release your source code under the same license as the open source software that you are reusing. If you want to keep your source code private, it's important to know the licenses terms of open source software you use.

  * Increasing awareness about cybersecurity by providing training to employees. According the [State of Cybersecurity 2021, Part 2](https://www.isaca.org/state-of-cybersecurity-2021), a survey of information security professionals, social engineering was the most frequent type of attack. Survey respondants also reported that cybersecurity training and awareness programs had some positive impact (46%) or strong positive impact (32%) on employee awareness.




Use the resources in the following sections to learn more about these topics.

## Security on Google Cloud

Learn about setting up organization structure, authentication and authorization, resource hierarchy, networking, logging, detective controls, and more in the [Google Cloud enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations), one of the guides in the [Google Cloud security best practices center](https://docs.cloud.google.com/security/best-practices).

You can view centralized information about vulnerabilities and possible risks using these Google Cloud services:

  * View information about vulnerabilities and threats across your Google Cloud organization with [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).
  * Get information about your service usage with [Recommender](https://docs.cloud.google.com/recommender/docs/overview), including recommendations that can help you to reduce risk. For example, you can identify IAM principals with excess permissions or unattended Google Cloud projects.



To learn more about security on Google Cloud, see the [Security section of the Google Cloud web site](https://docs.cloud.google.com/security).

## DevOps and software development practices

See the [DevOps capabilities](https://dora.dev/devops-capabilities/) documentation to learn more about DevOps practices that contribute to faster software delivery and more reliable and secure software.

There are also foundational practices for designing, developing, and testing code that apply to all programming languages. You also need to evaluate how you distribute software and the terms of software licenses in all of your dependencies. The Linux Foundation offers free online training on these topics:

  * [Developing Secure Software](https://training.linuxfoundation.org/training/developing-secure-software-lfd121/): Foundational software development practices in the context of software supply chain security. The course focuses on best practices for designing, developing, and testing code, but also covers topics such as handling vulnerability disclosures, assurance cases, and considerations for software distribution and deployment. The [Open Source Security Foundation](https://openssf.org/) (OpenSSF) created the training.
  * [Open Source Licensing Basics for Developers](https://training.linuxfoundation.org/training/open-source-licensing-basics-for-software-developers/) Learn about licenses and copyright for open source projects.
  * [Introduction to Open Source License Compliance Management](https://training.linuxfoundation.org/training/introduction-to-open-source-license-compliance-management-lfc193/) Learn about building an open source compliance program for your organization.



## Developing your policies

As you incrementally implement best practices, document the policies for your organization and incorporate validation of policies into your development, build, and deployment processes. For example, your company policies might include criteria for deployment that you implement with [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).

  * [Minimum Viable Secure Product](https://mvsp.dev), a security checklist of controls to establish a baseline security posture for a product. You can use the checklist to establish your minimum security control requirements and to evaluate software by third-party vendors.
  * NIST [Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) publication (SP 800-53).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
