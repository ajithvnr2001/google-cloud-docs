---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/attack-vectors/
title: Software supply chain threats \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:13.044557+00:00
---

# Software supply chain threats  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/attack-vectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Software supply chain threats Stay organized with collections  Save and categorize content based on your preferences. 

_Attack vectors_ for [software supply chains](https://docs.cloud.google.com/software-supply-chain-security/docs/overview) are the various ways in which someone can intentionally or accidentally compromise your software.

Risks of vulnerable software include leaking credentials or confidential data, corruption of data, installation of malware, and application outages. These problems result in lost time, money, and customer trust.

The entry points for threats span the entire software lifecycle and can originate inside or outside of your organization.

![Entry points for software supply chain attacks](https://docs.cloud.google.com/software-supply-chain-security/images/attack-vectors.svg)

The diagram legend includes two sets of threats:

  * Letters **A** to **H** indicate attack vectors in the software supply chain that are described as [threats](https://slsa.dev/spec/v0.1/threats) in the [Supply-chain Levels for Software Artifacts](https://slsa.dev) (SLSA) framework.
  * Numbers **1** to **4** indicate additional attack vectors that the SLSA framework does not directly describe.



Google Cloud provides a modular set of capabilities and tools that incorporate best practices for mitigating both sets of threats.

The subsections in this document describe the threats in the context of source, builds, deployment, and dependencies.

  * Source threats
  * Build threats
  * Deployment and runtime threats
  * Dependency threats



## Source threats

These threats impact the integrity of your source code.

  * **1** : Write insecure code. A lack of secure coding practices can lead to writing code that unintentionally includes vulnerabilities. Insecure developer workstations can also introduce malicious or insecure code. Mitigations include:

    * Setting policies for developer workstations. [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) provides fully-managed, preconfigured workstations that you can customize to align with your requirements.
    * Local scanning of code. Cloud Code source protect (private preview) provides real-time security feedback, including vulnerability and license information for dependencies. Developers can also use the [On-Demand Scanning API](https://docs.cloud.google.com/container-analysis/docs/enable-ods) to scan container images for OS and language package vulnerabilities.
    * Education about [practices to make code more secure](https://docs.cloud.google.com/software-supply-chain-security/docs/practices#devops_and_software_development_practices).
  * **A** : Submit bad code to the source repository. This not only includes malicious code, but also code that unintentionally introduces vulnerabilities to an attack such as [cross-site scripting](https://owasp.org/www-community/attacks/xss/). Mitigations include:

    * Requiring human review for changes to source code.
    * Using code scanning and linting tools that integrate with IDEs and source control systems.
  * **B** : Compromise the source control system. Restricting access to the source control system and other systems in your build pipeline, and using multi-factor authentication helps to mitigate this risk.




When evaluating your source integrity, also examine supporting scripts and configurations that you use to build and deploy your software. Include them in your source control system and code review processes, so that you can reduce the risk from vulnerabilities in these files.

See [Safeguard source](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-source) to learn more about protecting your source.

## Build threats

These threats compromise your software when you build or package it, or trick consumers of your software into using a bad version.

  * **C** : Build with source that is not from the trusted source control system. Mitigations that help to reduce this risk include: 
    * Using build services, such as [Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance), that generate provenance information so that you can validate that your builds use trusted source.
    * Placing your CI/CD infrastructure in a network perimeter to prevent exfiltration of data from your builds. For Google Cloud services, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
    * Storing and using trusted copies of open source dependencies you need in a private artifact store such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).
  * **D** : Compromise the build system. Mitigations that help to reduce this risk include: 
    * Follow the principle of least privilege by restricting direct access to the build system to individuals who require it. In Google Cloud you can grant appropriate [predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) or create [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).
    * Use managed build services such [Cloud Build](https://docs.cloud.google.com/build/docs). Cloud Build runs [ephemeral builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds#ephemeral) by setting up a VM environment for each build and destroying it after the build.
    * Place your CI/CD infrastructure in a network perimeter to prevent. exfiltration of data from your builds. For Google Cloud services, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * **F** : Package and publish software that was built outside of the official process. Build systems that generate and sign build provenance enable you to validate that your software was built by a trusted build system.
  * **G** : Compromise the repository where you store your software for your internal or external users. Mitigations that help to reduce this risk include: 
    * Storing and using trusted copies of open source dependencies you need in private artifact stores such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).
    * Validating build and source provenance.
    * Restricting upload permissions to dedicated non-human accounts and repository administrators. On Google Cloud, [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) act on behalf of services and applications.



## Deployment and runtime threats

  * **H** : Resolving dependencies by specifying a version range or a tag that isn't permanently attached to a specific build version can lead to several issues:

    * Builds are not reproducible because dependencies that a build uses the first time can be different from dependencies that the build uses for future executions of the same build.
    * A dependency might resolve to a compromised version, or a version with changes that break your software. Bad actors can take advantage of this uncertainty to cause your build to choose their version of a package instead of the version you intended to use. A number of [best practices for dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies) can help to mitigate _dependency confusion_ risks.
  * **2** : Compromise the deployment process. If you use a continuous deployment process, compromising that process can introduce unwanted changes to the software that you deliver to your users. You can mitigate risk by restricting access to your deployment service and testing changes in pre-production environments. [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) can help you manage the continuous delivery process and promotion between between environments.

  * **3** : Deploy compromised or noncompliant software. Enforcing deployment policies can help mitigate this risk. You can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) to validate that container images are compliant with policy criteria and block deployment of container images from untrusted sources.

  * **4** : Vulnerabilities and misconfiguration in running software.

    * New vulnerabilities are discovered regularly, which means that new findings can change the security risk level for your applications in production.
    * Some configurations increase risk of unauthorized access, such as running as the root user or allowing privilege escalation on execution of a a container.

The [GKE security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) shows information about [vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-posture-vulnerability-scanning) and [configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning) in your running workloads.

In Cloud Run, you can also view [security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/deploy-run-view-security-insights) about your deployed revisions, including known vulnerabilities in container images you deployed.




See [Safeguard builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds) to learn more about protecting your source, and [Safeguard deployments](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-deploys) to learn about protecting deployments.

## Dependency threats

Dependencies include direct dependencies in your builds as well all _transitive dependencies_ , the recursive tree of dependencies that are downstream from your direct dependencies.

In the diagram, **E** indicates using a bad dependency in your build. A bad dependency can include:

  * Any software that your application depends on, including components you develop internally, commercial third-party software, open source software.
  * Vulnerabilities originating from any of the other attack vectors. For example: 
    * An attacker gains access to your source control system and modifies the version of a dependency that your project uses.
    * Your build includes a component developed by another team in your organization. They build and publish the component directly from their local development environments and accidentally introduce a vulnerability in a library that they only use locally for testing and debugging.
  * Intentional removal of an open source dependency from a public repository. The removal can cause consuming pipelines to break if they retrieve the dependency directly from the public repository.



See [best practices for dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies) to learn about ways to to mitigate risks.

## Mitigating threats

The overall integrity of your supply chain is only as strong as its most vulnerable part. Neglecting an attack vector increases risk of attack in that part of your supply chain.

At the same time, you don't need to change everything at once. The _cumulative act effect_ , more popularly known as the [swiss cheese model](https://en.wikipedia.org/wiki/Swiss_cheese_model), applies to software supply chain security. Each mitigation that you implement reduces your risk, and when you combine mitigations across your supply chain, you increase protection against different types of attacks.

  * [Assess your security posture](https://docs.cloud.google.com/software-supply-chain-security/docs/assess) using frameworks and tools that help you evaluate your organization's ability to detect, respond to, and remediate threats.
  * [Learn about best practices](https://docs.cloud.google.com/software-supply-chain-security/docs/practices) to protect your software supply chain, and Google Cloud products designed to support those practices.
  * Incorporate Google Cloud security features into your development, build, and deployment processes to improve the security posture of your software software supply chain. You can implement services gradually, based on your priorities and existing infrastructure.



## What's next

  * [Assess your security posture](https://docs.cloud.google.com/software-supply-chain-security/docs/assess).
  * [Learn about best practices](https://docs.cloud.google.com/software-supply-chain-security/docs/practices) to protect your software supply chain.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
