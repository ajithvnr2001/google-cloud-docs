---
url: https://docs.cloud.google.com/docs/security/binary-authorization-for-borg/
title: Binary Authorization for Borg \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:42:38.770086+00:00
---

# Binary Authorization for Borg  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/binary-authorization-for-borg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Binary Authorization for Borg Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in September 2026, and represents the status quo as of the time it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers._

This document describes how we use code reviews, security infrastructure, and an enforcement check called _Binary Authorization for Borg (BAB)_ to help protect Google's software supply chain against insider risk. BAB helps reduce insider risk because it ensures that production software is reviewed and approved before it's deployed, particularly when our code can access sensitive data. BAB applies to all services that are running on [Borg service deployments](https://docs.cloud.google.com/docs/security/infrastructure/design#secure-service). Since the original publication of this document, we have included key concepts of BAB into an open specification called [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/).

This document is part of a series of technical papers that describes some projects that the Google security team has developed to help improve security, including [BeyondProd](https://docs.cloud.google.com/docs/security/beyondprod). For an overview of Google's infrastructure security, see the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).

## Insider risk

Insider risk represents a threat to the security of user data, which can include employment data, financial data, or other proprietary or business data. Insider risk is the potential for an employee to use their organizational knowledge or access to perform malicious acts, or for an external attacker to use the compromised credentials of an employee to do the same.

To minimize insider risk within our software supply chain, we use BAB. BAB is an internal enforcement check that occurs when software is deployed. BAB ensures that code and configuration deployments meet certain minimum standards and support uniformity in our production systems.

We help protect user data within our production systems by limiting unilateral access by our employees. BAB helps ensure that employees, while acting alone, can't directly or indirectly access or otherwise affect user data without proper authorization and justification. BAB and its associated controls help us enforce least privilege, which improves our security posture independently from a specific threat actor. In other words, BAB limits unilateral access regardless of whether the actor has malicious intent, their account has been compromised, or they have unintentionally been granted access.

## Binary Authorization for Borg benefits

Adopting BAB and a containerized deployment model provides many security benefits to Google infrastructure. The benefits include the following:

  * **BAB helps reduce overall insider risk:** BAB requires code to meet certain standards and change management practices before the code can access user data. This requirement reduces the potential for an employee acting alone (or a compromised employee account) from accessing user data programmatically.
  * **BAB supports uniformity of production systems:** Using containerized systems and verifying their BAB requirements before deployment helps ensure that our systems are easier to debug, more reliable, and include well-defined change management processes. BAB requirements provide a common language for production system requirements.
  * **BAB dictates a common language for data protection:** BAB tracks conformance across Google systems. Data about this conformance is published internally and is available to other teams. Publishing BAB data enables teams to use common terms when communicating with each other about their data access protection. This common language reduces the iterative work that is needed when working with data across teams.
  * **BAB allows programmatic tracking of compliance requirements:** BAB simplifies what were previously manual compliance tasks. Certain processes at Google require tighter controls on how we deal with data. For example, our financial reporting systems must comply with the Sarbanes-Oxley Act (SOX). Before BAB, we had a system that helped us manually perform verifications to ensure our compliance. With the introduction of BAB, many of these checks were automated based on the BAB policies for the services. Automating these checks enabled the compliance team to increase both the scope of services covered and the adoption of appropriate controls on these services.



BAB is part of the larger [BeyondProd](https://docs.cloud.google.com/docs/security/beyondprod) framework that we use to mitigate insider risk.

## Google's development and production process

By default, Google's development and production process includes four mandatory steps: code review, verifiable builds, containerized deployment, and service-based identity. The following sections describe these steps in more detail.

### Step 1: Code review

Most of our source code is stored in a [central monolithic repository](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/), and requires review and approval from at least one engineer other than the author. A monolithic codebase allows for the enforcement of a single control point for code reviews.

At a minimum, our code review process requires that the owners of a system must approve code modifications to that system. 

When importing changes from third-party or open source code, we verify that the change is appropriate (for example, the latest version). However, we often don't have the same review controls in place for every change made by external developers to the third-party or open source code we use.

### Step 2: Verifiable builds

Our build system is similar to [Bazel](https://bazel.build/), which builds and compiles source code to create a binary for deployment. Our build system runs in an isolated and locked-down environment that is separated from the employees performing the builds. For each build, the system produces provenance generated by verifiable builds . This provenance is a signed certificate that describes the sources and dependencies that went into the build, the cryptographic hashes of any binaries or other build artifacts, and the full build parameters. This provenance enables the following:

  * The ability to trace a binary to the source code that was used in its creation. By extension, the provenance can also trace the process around the creation and submission of the source code it describes.
  * The ability to verify that the binary wasn't modified as any changes to the file would automatically invalidate its signature.



Because build actions can be arbitrary code, our build system has been hardened for multi-tenancy. In other words, our build system is designed to prevent one build from influencing any other builds. The system prevents builds from making changes that could compromise the integrity of the build provenance or of the system itself. After the build is complete, the change is deployed using Borg.

### Step 3: Containerized deployment

After the build system creates the binary, it's packaged into a container image and deployed as a _Borg job_ on our [cluster orchestration system, Borg](https://research.google.com/pubs/pub43438.html). We run hundreds of thousands of jobs from many different applications, across multiple clusters, each with up to tens of thousands of machines. Despite this scale, our production environment is fairly homogeneous. As a result, the touchpoints for access to user data can be more easily controlled and audited.

Containers provide notable security benefits. Containers are meant to be immutable, with frequent redeployments from a complete image rebuild. Containerization enables us to review a code change in context, and provides a single control point for changes that get deployed into our infrastructure.

A Borg job's configuration specifies the requirements for the job to be deployed: the container images, runtime parameters, arguments, and flags. Borg schedules the job, taking into account the job's constraints, priority, quota, and any other requirements that are listed in the configuration. After the job is deployed, the Borg job can interact with other jobs in production.

### Step 4: Service-based identity

A Borg job runs as a service identity. This identity is used to access datastores or remote procedure call (RPC) methods of other services. Multiple jobs might run as the same identity. Only those employees who are responsible for running the service (typically [Site Reliability Engineers (SREs)](https://sre.google/)) can deploy or modify jobs with a particular identity.

When Borg starts a job, it provisions the job with cryptographic credentials. The job uses these credentials to prove its identity when making requests of other services using [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security). For a service to access certain data or another service, its identity must have the necessary permissions. 

Our policies require BAB protection for service identities that have access to user data and any other sensitive information. Quality assurance and development jobs that don't have access to sensitive data are permitted to run with fewer controls.

## How Binary Authorization for Borg works

BAB integrates with Borg to ensure that only authorized jobs are allowed to run with the identity of each service. BAB also creates an audit trail of the code and configuration used in BAB-enabled jobs to allow for monitoring and incident response.

BAB is designed to ensure that all production software and configuration are properly reviewed, checked in, built verifiably, and authorized, particularly when that code can access user data.

### Service-specific policy

When service owners onboard their service to Borg, they create a BAB policy that defines the security requirements for their service. This policy is called the _service-specific policy_. Defining or modifying a policy is itself a code change that must undergo review.

The service-specific policy defines what code and configuration is allowed to run as the service's identity, as well as the required properties of that code and configuration. All jobs running as the service identity must meet the service-specific policy.

All Borg services at Google are required to configure a service-specific policy. 

By default, this practice enforces the following requirements:

  * **Code must be auditable:** We can trace the container image back to its human-readable sources through provenance generated by verifiable builds. A retention policy keeps the human-readable sources of the code for at least 18 months, even if the code isn't submitted.
  * **Code must be submitted:** The code is built from a specified, defined location in our source repository. Submission generally implies that the code has undergone a code review.
  * **Configurations must be submitted:** Any configurations that are provided during deployment go through the same review and submission process as regular code. Therefore, command-line flag values, arguments, and parameters can't be modified without review.



Services that don't have access to sensitive data — or, in rare circumstances, services that have a valid and approved exception — might have a more permissive policy, such as one that only requires auditability of code, or even one that turns off BAB entirely.

The systems and components that enforce BAB are tightly controlled using strict automated requirements and additional manual controls.

### Enforcement modes

BAB uses two _enforcement modes_ to ensure that jobs comply with the service-specific policy: 

  * Deploy-time enforcement, which blocks non-compliant jobs from deploying.
  * Continuous verification, which monitors and alerts on non-compliant jobs that were deployed.



Additionally, in case of an emergency, emergency response procedures can bypass deploy-time enforcement.

#### Deploy-time enforcement mode

Borg Prime is Borg's centralized controller, which acts as the certificate authority for ALTS. When a new job is submitted, Borg Prime consults BAB to verify that the job meets the service-specific policy requirements before Borg Prime grants the ALTS certificate to the job. This check acts as an admission controller: Borg only starts the job if it satisfies the service-specific policy. This check occurs even when the employee or service making the deployment request is otherwise authorized.

In rare cases, services can opt out of deploy-time enforcement with an adequate justification.

#### Continuous verification mode

After a job is deployed, it's continuously verified for its lifetime, regardless of its enforcement mode at deployment time. A BAB process runs at least once a day to check that jobs that were started (and might still be running) conform to any updates to their policies. For example, continuous verification mode is constantly checking for jobs that are running with outdated policies or were deployed using emergency response procedures. If a job is found that doesn't adhere to the latest policy, BAB notifies the service owners so that they can mitigate the risk.

#### Emergency response procedures

When an incident or outage occurs, our first priority is to restore the affected service as quickly as possible. In an emergency situation, it might be necessary to run code that hasn't been reviewed or verifiably built. As a result, enforcement mode can be overridden using an emergency response flag. Emergency response procedures also act as a backup in case there is a failure of BAB that would otherwise block a deployment. When a developer deploys a job using the emergency response procedure, they must submit a justification as part of their request. 

During an emergency response, BAB logs details about the associated Borg job and sends a notification to both Google's centralized security team and the team that owns the service identity. The log entry includes a reference to a snapshot of the code that was deployed and the user-provided justification. Emergency response procedures are only meant to be used as a last resort.

### BAB in other environments

Originally, BAB only supported protection of Borg jobs and required the software to be developed using Google's traditional source control, build, and packaging pipeline. However, BAB has added support for protecting other software delivery and deployment environments and support for alternative source control, build, and packaging systems. The implementation details for these various environments differ, but the benefits of BAB remain.

There are a few cases that don't lend themselves well to human code reviews before deployment, notably iterative development of machine learning code and high-frequency data analysis. In these cases, we have alternative controls that compensate for human review.

## Connection to SLSA

The [Supply-chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/) is an open-source specification for improving the security of software supply chains. The following BAB concepts align with the SLSA v1.2 framework:

  * **Source history and two-person review (SLSA Source L1–L4):** BAB requires that production code be maintained in a version control system that preserves revision history, enforces branch controls, and requires two-party code review before changes are submitted.
  * **Cryptographic provenance and builder identity (SLSA Build L1–L2):** For each build, the build system generates a cryptographically signed provenance attestation.
  * **Verifiable, hardened builds (SLSA Build L3–L4):** Code is built on an isolated, hardened build platform that is separate from the employees who initiate the build.
  * **Artifact verification (SLSA Verifying artifacts):** SLSA defines how verifiers validate provenance signatures and compare provenance claims against preconfigured expectations. In BAB, service-specific policies define and enforce these expectations for each service identity.



## Adopt similar controls in your organization

This section describes the best practices that we learned as we implemented BAB so that you can adopt similar controls in your organization.

### Create a homogeneous, containerized CI/CD pipeline

The adoption of BAB was made easier because most teams used a single source control system, code review process, build system, and deployment system. Code reviews were already part of our culture, so we were able to make changes without too many significant user-visible changes. To adopt BAB, we focused on code reviews, verifiable builds, containerized deployments, and service-based identities for access control. This approach simplified the adoption of BAB and strengthened the guarantees that a solution like BAB can provide.

Our widespread use of microservices and service-based identities (like service accounts), rather than host-based identities (like IP addresses), let us build fine-grained control over the software that is permitted to run each service.

If your organization is unable to adopt a service identity directly, you could try protecting identity tokens using other measures as an interim step.

### Determine your goals, and define your policies based on your requirements

Build your policy-driven release process one piece at a time. You might need to implement certain changes earlier than others in your CI/CD pipeline. For example, you might need to start conducting formal code reviews before you can enforce them at deployment time.

A great motivator for a policy-driven release process is compliance. If you can encode at least some of your compliance requirements in a policy, it can help automate your tests and ensure that they are reliably in effect. Start with a base set of requirements and codify more advanced requirements as you go.

### Enforce policies at deployment and runtime

It's hard to define comprehensive policies on a piece of software without first knowing where it will run and what data it will access. Therefore, service-specific policy enforcement is done when code is deployed and when it accesses data, not when it's built. A policy is defined in terms of a runtime identity, so the same code might run in different environments and be subject to different policies.

We use BAB in addition to other access mechanisms to limit access to user data. Service owners can further ensure that data is only accessed by a job that meets particular BAB requirements.

### Enlist change agents across teams

When we created a Google-wide mandate for BAB deployment, what most affected our success rate was finding owners to drive the change in each product group. We identified a handful of service owners who saw immediate benefits from enforcement and were willing to provide feedback. We asked these owners to volunteer before making any changes mandatory. After we had their help, we set up a formal change management team to track ongoing changes. We then identified accountable owners in each product team to implement the changes.

### Determine how to manage third-party code

If you must manage third-party code, consider how you will introduce your policy requirements to your third-party codebase. For example, you can initially start by keeping a repository of all third-party code used. You can also regularly vet that code against your security requirements.

For more information on managing third-party code, see [Shared success in building a safer open source community](https://blog.google/technology/safety-security/shared-success-in-building-a-safer-open-source-community/).

## What's next

  * Read about [BeyondProd](https://docs.cloud.google.com/docs/security/beyondprod), which we use to build a secure perimeter around our microservices.
  * To adopt a secure CI/CD pipeline, see [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
