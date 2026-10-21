---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/assess/
title: Assess your security posture \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:13.313655+00:00
---

# Assess your security posture  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/assess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Assess your security posture Stay organized with collections  Save and categorize content based on your preferences. 

_Security posture_ is an organization's ability to detect, respond to, and remediate threats. It includes the readiness of an organization's people, hardware, software, policies and processes across the entire software lifecycle.

There are a number of frameworks and tools that you can use to assess your security posture and identify ways to mitigate threats.

## Software delivery practices

A strong security posture requires a strong foundation in software delivery best practices, and these practices go beyond implementing tools and technical controls. For example, if the change approval process is unclear, then it is easier for unwanted changes to enter your software supply chain. If teams are discouraged from raising issues, they might hesitate to report security concerns.

[DevOps Research and Assessment](https://dora.dev/) (DORA) performs independent research into practices and capabilities of high performance technology teams. To assess your team's performance and learn about ways to improve, use the following DORA resources:

  * Take the [DORA DevOps Quick Check](https://dora.dev/quickcheck/) to get some quick feedback on how your organization compares with others.
  * Read about the technical, process, measurement, and cultural DevOps [capabilities](https://dora.dev/devops-capabilities/) identified by DORA.



## Frameworks for security posture

The [NIST Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final) (SSDF) and [Cybersecurity Assessment Framework](https://www.ncsc.gov.uk/collection/caf/cyber-assessment-framework) (CAF) are frameworks developed by governments to help organizations assess their security posture and mitigate supply chain threats. These frameworks take into consideration the software development lifecycle as well as other aspects related to software security such as incident response plans. The complexity and scope of these frameworks can require a substantial investment in time and resources.

[Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) is a framework that aims to make assessment and mitigation implementation more approachable and incremental. It explains supply chain threats and associated mitigations and provides examples of tools to implement mitigations. It also groups requirements for strengthening your security posture in levels, so that you can prioritize and incrementally implement changes. SLSA is primarily focused on the software delivery pipeline, so you should use it together with other assessment tools like the SSDF and CAF.

SLSA is inspired by Google's internal [Binary Authorization for Borg](https://docs.cloud.google.com/docs/security/binary-authorization-for-borg) a mandatory enforcement check for all of Google's production workloads.

Google Cloud provides a modular set of capabilities and tools that incorporate best practices in SLSA. You can view insights about your security posture, including the SLSA level of your builds.

## Artifact and dependency management

Visibility into vulnerabilities in your software lets you proactively respond and remediate potential threats before you release your applications to your customers. You can use the following tools to get more visibility into vulnerabilities.

Vulnerability scanning
    Vulnerability scanning services such as [Artifact Analysis](https://docs.cloud.google.com/container-analysis/docs/container-analysis) help you to identify known vulnerabilities in your software.
Dependency management
    

Open Source Insights is a centralized source for information about dependency graphs, known vulnerabilities, and licenses associated with open source software. Use the site to learn about your dependencies.

The Open Source Insights project also makes this data available as an [Google Cloud Dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-data/deps-dev). You can use [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) to explore and analyze the data.

Source control policy
    

[Scorecards](https://github.com/ossf/scorecard) is an automated tool that identifies risky software supply chain practices in your GitHub projects.

    

[Allstar](https://github.com/ossf/allstar) is a GitHub App that continuously monitors GitHub organizations or repositories for adherence to configured policies. For example, you can apply a policy to your GitHub organization that checks for collaborators outside the organization who have administrator or push access.

To learn more about managing your dependencies, see [Dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies)

## Team awareness about cybersecurity

If your teams have an understanding of software supply chain threats and best practices, they can design and develop more secure applications.

In the [State of Cybersecurity 2021, Part 2](https://www.isaca.org/state-of-cybersecurity-2021), a survey of information security professionals, survey respondants reported that cybersecurity training and awareness programs had some positive impact (46%) or strong positive impact (32%) on employee awareness.

The following resources can help you learn more about supply chain security and security on Google Cloud:

  * [Google Cloud enterprise foundation blueprint](https://docs.cloud.google.com/architecture/security-foundations) describes setting up organization structure, authentication and authorization, resource hierarchy, networking, logging, detective controls, and more. It is one of the guides in the [Google Cloud security best practices center](https://docs.cloud.google.com/security/best-practices).
  * [Developing Secure Software](https://training.linuxfoundation.org/training/developing-secure-software-lfd121/) teaches foundational software development practices in the context of software supply chain security. The course focuses on best practices for designing, developing, and testing code, but also covers topics such as handling vulnerability disclosures, assurance cases, and considerations for software distribution and deployment. The [Open Source Security Foundation](https://openssf.org/) (OpenSSF) created the training.



## Preparing for change

After you have identified changes you want to make, you need to plan for the changes.

  * Identify best practices and mitigations to improve the reliability and security of your supply chain.
  * Develop guidelines and policies to ensure that teams implement changes and measure compliance consistently. For example, your company policies might include criteria for deployment that you implement with [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview). The following resources can help you:

    * [Minimum Viable Secure Product](https://mvsp.dev), a security checklist of controls to establish a baseline security posture for a product. You can use the checklist to establish your minimum security control requirements and to evaluate software by third-party vendors.
    * NIST [Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) publication (SP 800-53).
  * Plan for incremental changes to reduce the size, complexity, and impact of each change. It also helps the people on your teams to adjust to each change, provide feedback, and apply lessons you've learned to the future changes.




The following resources can help you with planning and implementing change.

  * [ROI of DevOps Transformation](https://docs.cloud.google.com/resources/roi-of-devops-transformation-whitepaper) is a white paper that describes how to forecast the value of and justify investment in DevOps transformation.

  * The Google [Cloud Application Modernization Program](https://docs.cloud.google.com/camp) provides holistic, guided assessment, measuring key outcomes (speed and stability and burnout) and identifying the technical, process, and cultural capabilities that improve those outcomes for your organization. See the [CAMP announcement blog post](https://cloud.google.com/blog/products/application-development/google-camp-shows-you-how-to-operate-at-scale) for more information about the program.

  * [How to transform](https://dora.dev/devops-capabilities/cultural/devops-culture-transform/) provides guidance to help you plan for and implement changes. Fostering a culture that supports incremental, ongoing change leads to more successful change outcomes.

  * The [NIST Secure Software Delivery Framework](https://csrc.nist.gov/Projects/ssdf) describes software security practices based on established practices from organizations such as [The Software Alliance](https://www.bsa.org/), [Open Web Application Security Project](https://owasp.org/), and [SAFECode](https://safecode.org/). It includes a set of practices to prepare your organization as well as practices for implementing changes and responding to vulnerabilities.




## What's next

  * Learn about [best practices](https://docs.cloud.google.com/software-supply-chain-security/docs/practices) to protect your software supply chain.
  * Learn about [software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview) and the Google Cloudproducts and features that help you to protect your software supply chain.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
