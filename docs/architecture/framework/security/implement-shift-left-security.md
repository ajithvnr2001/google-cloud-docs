---
url: https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security/
title: Implement shift-left security \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:45.368195+00:00
---

# Implement shift-left security  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Implement shift-left security Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-05 UTC

This principle in the security pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) helps you identify practical controls that you can implement early in the software development lifecycle to improve your security posture. It provides recommendations that help you implement preventive security guardrails and post-deployment security controls.

## Principle overview

_Shift-left security_ means adopting security practices early in the software development lifecycle. This principle has the following goals:

  * Avoid security defects before system changes are made. Implement preventive security guardrails and adopt practices such as infrastructure as code (IaC), policy as code, and security checks in the CI/CD pipeline. You can also use other platform-specific capabilities like [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) and [hardened GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) in Google Cloud.
  * Detect and fix security bugs early, fast, and reliably after any system changes are committed. Adopt practices like code reviews, post-deployment vulnerability scanning, and security testing.



The [Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design) and shift-left security principles are related but they differ in scope. The security-by-design principle helps you to avoid fundamental design flaws that would require re-architecting the entire system. For example, a threat-modeling exercise reveals that the current design doesn't include an authorization policy, and all users would have the same level of access without it. Shift-left security helps you to avoid implementation defects (bugs and misconfigurations) before changes are applied, and it enables fast, reliable fixes after deployment.

## Recommendations

To implement the shift-left security principle for your cloud workloads, consider the recommendations in the following sections:

  * Adopt preventive security controls
  * Automate provisioning and management of cloud resources
  * Automate secure application releases
  * Ensure that application deployments follow approved processes
  * Scan for known vulnerabilities before application deployment
  * Monitor your application code for known vulnerabilities



### Adopt preventive security controls

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Identity and access management
  * Cloud governance, risk, and compliance



Preventive security controls are crucial for maintaining a strong security posture in the cloud. These controls help you proactively mitigate risks. You can prevent misconfigurations and unauthorized access to resources, enable developers to work efficiently, and help ensure compliance with industry standards and internal policies.

Preventive security controls are more effective when they're implemented by using infrastructure as code (IaC). With IaC, preventive security controls can include more customized checks on the infrastructure code before changes are deployed. When combined with automation, preventive security controls can run as part of your CI/CD pipeline's automatic checks.

The following products and Google Cloud capabilities can help you implement preventive controls in your environment:

  * [Organization Policy Service constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview): configure predefined and custom constraints with centralized control.
  * [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls): create perimeters around your Google Cloud services.
  * Identity and Access Management (IAM), [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview), and [principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies): restrict access to resources.
  * [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) and [Open Policy Agent (OPA)](https://www.openpolicyagent.org/): enforce IaC constraints in your CI/CD pipeline and avoid cloud misconfigurations.



IAM lets you authorize _who_ can act on specific resources based on permissions. For more information, see [Access control for organization resources with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).

Organization Policy Service lets you set restrictions on resources to specify how they can be configured. For example, you can use an organization policy to do the following:

  * [Limit resource sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) based on domain.
  * [Limit the use of service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts).
  * [Restrict the physical location](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) of newly created resources.



In addition to using organizational policies, you can restrict access to resources by using the following methods:

  * [Tags with IAM](https://docs.cloud.google.com/iam/docs/tags-access-control): assign a tag to a set of resources and then set the access definition for the tag itself, rather than defining the access permissions on each resource.
  * [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview): define conditional, attribute-based access control for resources.
  * Defense in depth: use VPC Service Controls to further restrict access to resources.



For more information about resource management, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

### Automate provisioning and management of cloud resources

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Application security
  * Cloud governance, risk, and compliance



Automating the provisioning and management of cloud resources and workloads is more effective when you also adopt declarative IaC, as opposed to imperative scripting. IaC isn't a security tool or practice on its own, but it helps you to improve the security of your platform. Adopting IaC lets you create repeatable infrastructure and provides your operations team with a known good state. IaC also improves the efficiency of rollbacks, audit changes, and troubleshooting.

When combined with CI/CD pipelines and automation, IaC also gives you the ability to adopt practices such as _policy as code_ with tools like OPA. You can audit infrastructure changes over time and run automatic checks on the infrastructure code before changes are deployed.

To automate the infrastructure deployment, you can use tools like [Config Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-controller/docs/overview), Terraform, Jenkins, and [Cloud Build](https://docs.cloud.google.com/build). To help you build a secure application environment using IaC and automation, Google Cloud provides the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). This blueprint is Google's opinionated design that follows all of our recommended practices and configurations. The blueprint provides step-by-step instructions to configure and deploy your Google Cloud topology by using Terraform and Cloud Build.

You can modify the scripts of the enterprise foundations blueprint to configure an environment that follows Google recommendations and meets your own security requirements. You can further build on the blueprint with additional blueprints or design your own automation. The Google Cloud Architecture Center provides other blueprints that can be implemented on top of the enterprise foundations blueprint. The following are a few examples of these blueprints:

  * [Deploy an enterprise developer platform on Google Cloud](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint)
  * [Deploy a secured serverless architecture using Cloud Run](https://docs.cloud.google.com/architecture/blueprints/serverless-blueprint)
  * [Build and deploy generative AI and machine learning models in an enterprise](https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint)
  * [Import data from Google Cloud into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint)



### Automate secure application releases

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Application security.

Without automated tools, it can be difficult to deploy, update, and patch complex application environments to meet consistent security requirements. We recommend that you build automated CI/CD pipelines for your software development lifecycle (SDLC). Automated CI/CD pipelines help you to remove manual errors, provide standardized development feedback loops, and enable efficient product iterations. Continuous delivery is one of the best practices that the [DORA framework](https://dora.dev/research/?view=detail) recommends.

Automating application releases by using CI/CD pipelines helps to improve your ability to detect and fix security bugs early, fast, and reliably. For example, you can scan for security vulnerabilities automatically when artifacts are created, narrow the scope of security reviews, and roll back to a known and safe version. You can also define policies for different environments (such as development, test, or production environments) so that only verified artifacts are deployed.

To help you automate application releases and embed security checks in your CI/CD pipeline, Google Cloud provides multiple tools including [Cloud Build](https://docs.cloud.google.com/build), [Cloud Deploy](https://docs.cloud.google.com/deploy/docs), [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), and [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs).

To establish a process that verifies multiple security requirements in your SDLC, use the [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev) framework, which has been defined by Google. SLSA requires security checks for source code, build process, and code provenance. Many of these requirements can be included in an automated CI/CD pipeline. To understand how Google applies these practices internally, see [Google Cloud's approach to change](https://docs.cloud.google.com/docs/cloud-approach-to-change).

### Ensure that application deployments follow approved processes

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Application security.

If an attacker compromises your CI/CD pipeline, your entire application stack can be affected. To help secure the pipeline, you should enforce an established approval process before you deploy the code into production.

If you use Google Kubernetes Engine (GKE) or Cloud Run, you can establish an approval process by using [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview). Binary Authorization attaches configurable signatures to container images. These signatures (also called _attestations_) help to validate the image. At deployment time, Binary Authorization uses these attestations to determine whether a process was completed. For example, you can use Binary Authorization to do the following:

  * Verify that a specific build system or CI pipeline created a container image.
  * Validate that a container image is compliant with a vulnerability signing policy.
  * Verify that a container image passes the criteria for promotion to the next deployment environment, such as from development to QA.



By using Binary Authorization, you can enforce that only trusted code runs on your target platforms.

### Scan for known vulnerabilities before application deployment

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Application security.

We recommend that you use automated tools that can continuously perform vulnerability scans on application artifacts before they're deployed to production.

For containerized applications, use [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs) to automatically run vulnerability scans for container images. Artifact Analysis scans new images when they're uploaded to [Artifact Registry](https://docs.cloud.google.com/artifact-registry). The scan extracts information about the system packages in the container. After the initial scan, Artifact Analysis continuously monitors the metadata of scanned images in Artifact Registry for new vulnerabilities. When Artifact Analysis receives new and updated vulnerability information from [vulnerability sources](https://docs.cloud.google.com/artifact-analysis/docs/vulnerability-scanning#sources), it does the following:

  * Updates the metadata of the scanned images to keep them up to date.
  * Creates new vulnerability occurrences for new notes.
  * Deletes vulnerability occurrences that are no longer valid.



### Monitor your application code for known vulnerabilities

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Application security.

Use automated tools to constantly monitor your application code for known vulnerabilities such as the [OWASP Top 10](https://owasp.org/www-project-top-ten/). For more information about Google Cloud products and features that support OWASP Top 10 mitigation techniques, see [Mitigate OWASP Top 10:2025 on Google Cloud](https://docs.cloud.google.com/docs/security/owasp-top-ten-mitigation).

Use [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) to help identify security vulnerabilities in your App Engine, Compute Engine, and GKE web applications. The scanner crawls your application, follows all of the links within the scope of your starting URLs, and attempts to exercise as many user inputs and event handlers as possible. It can automatically scan for and detect common vulnerabilities, including [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting), [code injection](https://en.wikipedia.org/wiki/Code_injection), [mixed content](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content), and outdated or insecure libraries. Web Security Scanner provides early identification of these types of vulnerabilities without distracting you with false positives.

In addition, if you use GKE to manage fleets of Kubernetes clusters, the security posture dashboard shows opinionated, actionable recommendations to help improve your fleet's security posture.

[ Previous arrow_back  Implement zero trust  ](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust)

[ Next Implement preemptive cyber defense  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/security/implement-preemptive-cyber-defense)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-05 UTC."],[],[]] 
