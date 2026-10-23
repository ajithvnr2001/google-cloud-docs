---
url: https://docs.cloud.google.com/architecture/design-secure-deployment-pipelines-bp/
title: Design secure deployment pipelines \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:31.624734+00:00
---

# Design secure deployment pipelines  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/design-secure-deployment-pipelines-bp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Design secure deployment pipelines Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-29 UTC

A deployment pipeline is an automated process that takes code or prebuilt artifacts and deploys them to a test environment or a production environment. Deployment pipelines are commonly used to deploy applications, configuration, or cloud infrastructure (infrastructure as code), and they can play an important role in the overall security posture of a cloud deployment.

This guide is intended for DevOps and security engineers and describes best practices for designing secure deployment pipelines based on your confidentiality, integrity, and availability requirements.

## Architecture

The following diagram shows the flow of data in a deployment pipeline. It illustrates how you can turn your artifacts into resources.

![Artifact flows into a deployment pipeline and comes out a resource.](https://docs.cloud.google.com/static/architecture/images/design_secure_deployment_pipelines_01.svg)

Deployment pipelines are often part of a larger continuous integration/continuous deployment (CI/CD) workflow and are typically implemented using one of the following models:

  * **Push model:** In this model, you implement the deployment pipeline using a central CI/CD system such as [Jenkins](https://www.jenkins.io/doc/) or [GitLab](https://docs.gitlab.com/ee/ci/). This CI/CD system might run on Google Cloud, on-premises, or on a different cloud environment. Often, the same CI/CD system is used to manage multiple deployment pipelines.

The push model leads to a centralized architecture with a few CI/CD systems that are used for managing a potentially large number of resources or applications. For example, you might use a single Jenkins or GitLab instance to manage your entire production environment, including all its projects and applications.

  * **Pull model:** In this model, the deployment process is implemented by an agent that is deployed alongside the resource–for example, in the same [Kubernetes](https://docs.cloud.google.com/kubernetes-engine) cluster. The agent pulls artifacts or source code from a centralized location, and deploys them locally. Each agent manages one or two resources.

The pull model leads to a more decentralized architecture with a potentially large number of single-purpose agents.




Compared to manual deployments, consistently using deployment pipelines can have the following benefits:

  * Increased efficiency, because no manual work is required.
  * Increased reliability, because the process is fully automated and repeatable.
  * Increased traceability, because you can trace all deployments to changes in code or to input artifacts.



To perform, a deployment pipeline requires access to the resources it manages:

  * A pipeline that deploys infrastructure by using tools like [Terraform](https://www.terraform.io/intro) might need to create, modify, or even delete resources like VM instances, subnets, or Cloud Storage buckets.
  * A pipeline that deploys applications might need to upload new container images to Artifact Registry, and deploy new application versions to [App Engine](https://docs.cloud.google.com/appengine/docs), [Cloud Run](https://docs.cloud.google.com/run/docs), or [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs).
  * A pipeline that manages settings or deploys configuration files might need to modify VM instance metadata, Kubernetes configurations, or modify data in [Cloud Storage](https://docs.cloud.google.com/storage/docs).



If your deployment pipelines aren't properly secured, their access to Google Cloud resources can become a weak spot in your security posture. Weakened security can lead to several kinds of attacks, including the following:

  * **Pipeline poisoning attacks:** Instead of attacking a resource directly, a bad actor might attempt to compromise the deployment pipeline, its configuration, or its underlying infrastructure. Taking advantage of the pipeline's access to Google Cloud, the bad actor could make the pipeline perform malicious actions on Cloud resources, as shown in the following diagram:

![A bad actor can attack an insecure deployment pipeline using code.](https://docs.cloud.google.com/static/architecture/images/design_secure_deployment_pipelines_02.svg)

  * **Supply chain attacks:** Instead of attacking the deployment pipeline, a bad actor might attempt to compromise or replace pipeline input—including source code, libraries, or container images, as shown in the following diagram:

![A bad actor can attack the supply chain that feeds a deployment pipeline.](https://docs.cloud.google.com/static/architecture/images/design_secure_deployment_pipelines_03.svg)




To determine whether your deployment pipelines are appropriately secured, it's insufficient to look only at the allow policies and deny policies of Google Cloud resources in isolation. Instead, you must consider the entire graph of systems that directly or indirectly grant access to a resource. This graph includes the following information:

  * The deployment pipeline, its underlying CI/CD system, and its underlying infrastructure
  * The source code repository, its underlying servers, and its underlying infrastructure
  * Input artifacts, their storage locations, and their underlying infrastructure
  * Systems that produce the input artifacts, and their underlying infrastructure



Complex input graphs make it difficult to identify user access to resources and systemic weaknesses.

The following sections describe best practices for designing deployment pipelines in a way that helps you manage the size of the graph, and reduce the risk of lateral movement and supply chain attacks.

## Assess security objectives

Your resources on Google Cloud are likely to vary in how sensitive they are. Some resources might be highly sensitive because they're business critical or confidential. Other resources might be less sensitive because they're ephemeral or only intended for testing purposes.

To design a secure deployment pipeline, you must first understand the resources the pipeline needs to access, and how sensitive these resources are. The more sensitive your resources, the more you should focus on securing the pipeline.

The resources accessed by deployment pipelines might include:

  * Applications, such as Cloud Run or App Engine
  * Cloud resources, such as VM instances or Cloud Storage buckets
  * Data, such as Cloud Storage objects, BigQuery records, or files



Some of these resources might have dependencies on other resources, for example:

  * Applications might access data, cloud resources, and other applications.
  * Cloud resources, such as VM instances or Cloud Storage buckets, might contain applications or data.

![The dependencies one resource has on another can affect the sensitivity of both.](https://docs.cloud.google.com/static/architecture/images/design_secure_deployment_pipelines_04.svg)




As shown in the preceding diagram, dependencies affect how sensitive a resource is. For example, if you use an application that accesses highly sensitive data, typically you should treat that application as highly sensitive. Similarly, if a cloud resource like a Cloud Storage bucket contains sensitive data, then you typically should treat the bucket as sensitive.

Because of these dependencies, it's best to first assess the sensitivity of your data. Once you've assessed your data, you can examine the dependency chain and assess the sensitivity of your Cloud resources and applications.

### Categorize the sensitivity of your data

To understand the sensitivity of the data in your deployment pipeline, consider the following three objectives:

  * **Confidentiality** : You must protect the data from unauthorized access.
  * **Integrity** : You must protect the data against unauthorized modification or deletion.
  * **Availability** : You must ensure that authorized people and systems can access the data in your deployment pipeline.



For each of these objectives, ask yourself what would happen if your pipeline was breached:

  * **Confidentiality:** How damaging would it be if data was disclosed to a bad actor, or leaked to the public?
  * **Integrity:** How damaging would it be if data was modified or deleted by a bad actor?
  * **Availability:** How damaging would it be if a bad actor disrupted your data access?



To make the results comparable across resources, it's useful to introduce security categories. [Standards for Security Categorization (FIPS-199)](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.199.pdf) suggests using the following four categories:

  * **High:** Damage would be severe or catastrophic
  * **Moderate:** Damage would be serious
  * **Low:** Damage would be limited
  * **Not applicable:** The standard doesn't apply



Depending on your environment and context, a different set of categories could be more appropriate.

The confidentiality and integrity of pipeline data exist on a spectrum, based on the security categories just discussed. The following subsections contain examples of resources with different confidentiality and integrity measurements:

#### Resources with low confidentiality, but low, moderate, and high integrity

The following resource examples all have low confidentiality:

  * **Low integrity:** Test data
  * **Moderate integrity:** Public web server content, policy constraints for your organization
  * **High integrity:** Container images, disk images, application configurations, access policies (allow and deny lists), liens, access-level data



#### Resources with medium confidentiality, but low, moderate, and high integrity

The following resource examples all have medium confidentiality:

  * **Low integrity:** Internal web server content
  * **Moderate integrity:** Audit logs
  * **High integrity:** Application configuration files



#### Resources with high confidentiality, but low, moderate, and high integrity

The following resource examples all have high confidentiality:

  * **Low integrity:** Usage data and personally identifiable information
  * **Moderate integrity:** Secrets
  * **High integrity:** Financial data, KMS keys



### Categorize applications based on the data that they access

When an application accesses sensitive data, the application and the deployment pipeline that manages the application can also become sensitive. To qualify that sensitivity, look at the data that the application and the pipeline need to access.

Once you've identified and categorized all data accessed by an application, you can use the following categories to initially categorize the application before you design a secure deployment pipeline:

  * **Confidentiality** : Highest category of any data accessed
  * **Integrity** : Highest category of any data accessed
  * **Availability** : Highest category of any data accessed



This initial assessment provides guidance, but there might be additional factors to consider—for example:

  * Two sets of data might have low-confidentiality in isolation. But when combined, they could reveal new insights. If an application has access to both sets of data, you might need to categorize it as medium- or high-confidentiality.
  * If an application has access to high-integrity data, then you should typically categorize the application as high-integrity. But if that access is read only, a categorization of high-integrity might be too strict.



For details on a formalized approach to categorize applications, see [Guide for Mapping Types of Information and Information Systems to Security Categories (NIST SP 800-60 Vol. 2 Rev1)](https://csrc.nist.gov/publications/detail/sp/800-60/vol-2-rev-1/final).

### Categorize cloud resources based on the data and applications they host

Any data or application that you deploy on Google Cloud is hosted by a Google Cloud resource:

  * An application might be hosted by an App Engine service, a VM instance, or a GKE cluster.
  * Your data might be hosted by a persistent disk, a Cloud Storage bucket, or a BigQuery dataset.



When a cloud resource hosts sensitive data or applications, the resource and the deployment pipeline that manages the resource can also become sensitive. For example, you should consider a Cloud Run service and its deployment pipeline to be as sensitive as the application that it's hosting.

After categorizing your data and your applications, create an initial security category for the application. To do so, determine a level from the following categories:

  * **Confidentiality** : Highest category of any data or application hosted
  * **Integrity** : Highest category of any data or application hosted
  * **Availability** : Highest category of any data or application hosted



When making your initial assessment, don't be too strict—for example:

  * If you encrypt highly confidential data, treat the encryption key as highly confidential. But, you can use a lower security category for the resource containing the data.
  * If you store redundant copies of data, or run redundant instances of the same applications across multiple resources, you can make the category of the resource lower than the category of the data or application it hosts.



### Constrain the use of deployment pipelines

If your deployment pipeline needs to access sensitive Google Cloud resources, you must consider its security posture. The more sensitive the resources, the better you need to attempt to secure the pipeline. However, you might encounter the following practical limitations:

  * When using existing infrastructure or an existing CI/CD system, that infrastructure might constrain the security level you can realistically achieve. For example, your CI/CD system might only support a limited set of security controls, or it might be running on infrastructure that you consider less secure than some of your production environments.
  * When setting up new infrastructure and systems to run your deployment pipeline, securing all components in a way that meets your most stringent security requirements might not be cost effective.



To deal with these limitations, it can be useful to set constraints on what scenarios should and shouldn't use deployment pipelines and a particular CI/CD system. For example, the most sensitive deployments are often better handled outside of a deployment pipeline. These deployments could be manual, using a privileged session management system or a privileged access management system, or something else, like tool proxies.

To set your constraints, define which access controls you want to enforce based on your resource categories. Consider the guidance offered in the following table:

**Category of resource** | **Access controls**  
---|---  
Low | No approval required  
Moderate | Team lead must approve  
High | Multiple leads must approve and actions must be recorded  
  
Contrast these requirements with the capabilities of your source code management (SCM) and CI/CD systems by asking the following questions and others:

  * Do your SCM or CI/CD systems support necessary access controls and approval mechanisms?
  * Are the controls protected from being subverted if bad actors attack the underlying infrastructure?
  * Is the configuration that defines the controls appropriately secured?



Depending on the capabilities and limitations imposed by your SCM or CI/CD systems, you can then define your data and application constraints for your deployment pipelines. Consider the guidance offered in the following table:

**Category of resource** | **Constraints**  
---|---  
Low | Deployment pipelines can be used, and developers can self-approve deployments.  
Moderate | Deployment pipelines can be used, but a team lead has to approve every commit and deployment.  
High | Don't use deployment pipelines. Instead, administrators have to use a privileged access management system and session recording.  
  
## Maintain resource availability

Using a deployment pipeline to manage resources can impact the availability of those resources and can introduce new risks:

  * **Causing outages:** A deployment pipeline might push faulty code or configuration files, causing a previously working system to break, or data to become unusable.
  * **Prolonging outages:** To fix an outage, you might need to rerun a deployment pipeline. If the deployment pipeline is broken or unavailable for other reasons, that could prolong the outage.



A pipeline that can cause or prolong outages poses a denial of service risk: A bad actor might use the deployment pipeline to intentionally cause an outage.

### Create emergency access procedures

When a deployment pipeline is the only way to deploy or configure an application or resource, pipeline availability can become critical. In extreme cases, where a deployment pipeline is the only way to manage a business-critical application, you might also need to consider the deployment pipeline business-critical.

Because deployment pipelines are often made from multiple systems and tools, maintaining a high level of availability can be difficult or uneconomical.

You can reduce the influence of deployment pipelines on availability by creating emergency access procedures. For example, create an alternative access path that can be used if the deployment pipeline isn't operational.

Creating an emergency access procedure typically requires most of the following processes:

  * Maintain one of more user accounts with privileged access to relevant Google Cloud resources.
  * Store the credentials of emergency-access user accounts in a safe location, or use a privileged access management system to broker access.
  * Establish a procedure that authorized employees can follow to access the credentials.
  * Audit and review the use of emergency-access user accounts.



### Ensure that input artifacts meet your availability demands

Deployment pipelines typically need to download source code from a central source code repository before they can perform a deployment. If the source code repository isn't available, running the deployment pipeline is likely to fail.

Many deployment pipelines also depend on third-party artifacts. Such artifacts might include libraries from sources such as npm, Maven Central, or the NuGet Gallery, as well as container base images, and `.deb`, and `.rpm` packages. If one of the third-party sources is unavailable, running the deployment pipeline might fail.

To maintain a certain level of availability, you must ensure that the input artifacts of your deployment pipeline all meet the same or higher availability requirements. The following list can help you ensure the availability of input artifacts:

  * Limit the number of sources for input artifacts, particularly third-party sources
  * Maintain a cache of input artifacts that deployment pipelines can use if source systems are unavailable



### Treat deployment pipelines and their infrastructure like production systems

Deployment pipelines often serve as the connective tissue between development, staging, and production environments. Depending on the environment, they might implement multiple stages:

  * In the first stage, the deployment pipeline updates a development environment.
  * In the next stage, the deployment pipeline updates a staging environment.
  * In the final stage, the deployment pipeline updates the production environment.



When using a deployment pipeline across multiple environments, ensure that the pipeline meets the availability demands of each environment. Because production environments typically have the highest availability demands, you should treat the deployment pipeline and its underlying infrastructure like a production system. In other words, apply the same access control, security, and quality standards to the infrastructure running your deployment pipelines as you do for your production systems.

### Limit the scope of deployment pipelines

The more resources that a deployment pipeline can access, the more damage it can possibly cause if compromised. A compromised deployment pipeline that has access to multiple projects or even your entire organization could, in the worst case, possibly cause lasting damage to all your data and applications on Google Cloud.

To help avoid this worst-case scenario, limit the scope of your deployment pipelines. Define the scope of each deployment pipeline so it only needs access to a relatively small number of resources on Google Cloud:

  * Instead of granting access on the project level, only grant deployment pipelines access to individual resources.
  * Avoid granting access to resources across multiple Google Cloud projects.
  * Split deployment pipelines into multiple stages if they need access to multiple projects or environments. Then, secure the stages individually.



## Maintain confidentiality

A deployment pipeline must maintain the confidentiality of the data it manages. One of the primary risks related to confidentiality is data exfiltration.

There are multiple ways in which a bad actor might attempt to use a deployment pipeline to exfiltrate data from your Google Cloud resources. These ways include:

  * **Direct:** A bad actor might modify the deployment pipeline or its configuration so that it extracts data from your Google Cloud resources and then copies it elsewhere.
  * **Indirect:** A bad actor might use the deployment pipeline to deploy compromised code, which then steals data from your Google Cloud environment.



You can reduce confidentiality risks by minimizing access to confidential resources. Removing all access to confidential resources might not be practical, however. Therefore, you must design your deployment pipeline to meet the confidentiality demands of the resources it manages. To determine these demands, you can use the following approach:

  1. Determine the data, applications, and resources the deployment pipeline needs to access, and categorize them.
  2. Find the resource with the highest confidentiality category and use it as an initial category for the deployment pipeline.



Similar to the categorization process for applications and cloud resources, this initial assessment isn't always appropriate. For example, you might use a deployment pipeline to create resources that will eventually contain highly confidential information. If you restrict the deployment pipeline so that it can create–but can't read–these resources, then a lower confidentiality category might be sufficient.

To maintain confidentiality, the [Bell–LaPadula model](https://en.wikipedia.org/wiki/Bell%E2%80%93LaPadula_model) suggests that a deployment pipeline must not:

  * Consume input artifacts of higher confidentiality
  * Write data to a resource of lower confidentiality



![The Bell–LaPadula model.](https://docs.cloud.google.com/static/architecture/images/design_secure_deployment_pipelines_05.svg)

According to the Bell–LaPadula model, the preceding diagram shows how data should flow in the pipeline to help ensure data confidentiality.

### Don't let deployment pipelines read data they don't need

Deployment pipelines often don't need access to data, but they might still have it. Such over-granting of access can result from:

  * Granting incorrect access permissions. A deployment pipeline might be granted access to Cloud Storage on the project level, for example. As a result, the deployment pipeline can access all Cloud Storage buckets in the project, although access to a single bucket might be sufficient.
  * Using an overly permissive role. A deployment pipeline might be granted a role that provides full access to Cloud Storage, for example. However, the permission to create new buckets would suffice.



The more data that a pipeline can access, the higher the risk that someone or something can steal your data. To help minimize this risk, avoid granting deployment pipelines access to any data that they don't need. Many deployment pipelines don't need data access at all, because their sole purpose is to manage configuration or software deployments.

### Don't let deployment pipelines write to locations they don't need

To remove data, a bad actor needs access and a way to transfer the data out of your environment. The more storage and network locations a deployment pipeline can send data to, the more likely it is that a bad actor can use one of those locations for exfiltration.

You can help reduce risk by limiting the number of network and storage locations where a pipeline can send data:

  * Revoke write access to resources that the pipeline doesn't need, even if the resources don't contain any confidential data.
  * Block internet access, or restrict connections, to an allow-listed set of network locations.



Restricting outbound access is particularly important for pipelines that you've categorized as moderately confidential or highly confidential because they have access to confidential data or cryptographic key material.

### Use VPC Service Controls to help prevent compromised deployments from stealing data

Instead of letting the deployment pipeline perform data exfiltration, a bad actor might attempt to use the deployment pipeline to deploy compromised code. That compromised code can then steal data from within your Google Cloud environment.

You can help reduce the risk of such data-theft threats by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs). VPC Service Controls let you restrict the set of resources and APIs that can be accessed from within certain Google Cloud projects.

## Maintain integrity

To keep your Google Cloud environment secure, you must protect its integrity. This includes:

  * Preventing unauthorized modification or deletion of data or configuration
  * Preventing untrusted code or configuration from being deployed
  * Ensuring that all changes leave a clear audit trail



Deployment pipelines can help you maintain the integrity of your environment by letting you:

  * Implement approval processes—for example, in the form of code reviews
  * Enforce a consistent process for all configuration or code changes
  * Run automated tests or quick checks before each deployment



To be effective, you must try to ensure that bad actors can't undermine or sidestep these measures. To prevent such activity, you must protect the integrity of:

  * The deployment pipeline and its configuration
  * The underlying infrastructure
  * All inputs consumed by the deployment pipeline



To prevent the deployment pipeline from becoming vulnerable, try to ensure that the integrity standards of the deployment pipeline match or exceed the integrity demands of the resources it manages. To determine these demands, you can use the following approach:

  1. Determine the data, applications, and resources the deployment pipeline needs to access, and categorize them.
  2. Find the resource with the highest integrity category and use it as the category for the deployment pipeline.



To maintain the integrity of the deployment pipeline, the [Biba model](https://en.wikipedia.org/wiki/Biba_Model) suggests that:

  * The deployment pipeline must not consume input artifacts of lower integrity.
  * The deployment pipeline must not write data to a resource of higher integrity.



![The Biba integrity model.](https://docs.cloud.google.com/static/architecture/images/design_secure_deployment_pipelines_06.svg)

According to the Biba model, the preceding diagram shows how data should flow in the pipeline to help ensure data integrity.

### Verify the authenticity of input artifacts

Many deployment pipelines consume artifacts from third-party sources. Such artifacts might include:

  * Docker base images
  * `.rpm` or `.deb`packages
  * Maven, `.npm`, or NuGet libraries



A bad actor might attempt to modify your deployment pipeline so that it uses compromised versions of third-party artifacts by:

  * Compromising the repository that stores the artifacts
  * Modifying the deployment pipeline's configuration to use a different source repository
  * Uploading malicious packages with similar names, or names that contain typos



Many package managers let you verify the authenticity of a package by supporting code-signing. For example, you can use PGP to sign RPM and Maven packages. You can use Authenticode to sign NuGet packages.

You can use code-signing to reduce the risk of falling victim to compromised third-party packages by:

  * Requiring that all third-party artifacts are signed
  * Maintaining a curated list of trusted publisher certificates or public keys
  * Letting the deployment pipeline verify the signature of third-party artifacts against the trusted publishers list



Alternatively, you can verify the hashes of artifacts. You can use this approach for artifacts that don't support code-signing and change infrequently.

### Ensure that underlying infrastructure meets your integrity demands

Instead of compromising the deployment pipeline itself, bad actors might attempt to compromise its infrastructure, including:

  * The CI/CD software that runs the deployment pipeline
  * The tools used by the pipeline—for example, Terraform, kubectl, or Docker
  * The operating system and all its components



Because the infrastructure that underlies deployment pipelines is often complex and might contain components from various vendors or sources, this type of security breach can be difficult to detect.

You can help reduce the risk of compromised infrastructure by:

  * Holding the infrastructure and all its components to the same integrity standards as the deployment pipeline and the Google Cloud resources that it manages
  * Making sure tools come from a trusted source and verifying their authenticity
  * Regularly rebuilding infrastructure from scratch
  * Running the deployment pipeline on [shielded VMs](https://cloud.google.com/security/products/shielded-vm)



### Apply integrity controls in the pipeline

While bad actors are a threat, they aren't the only possible source of software or configuration changes that can impair the integrity of your Google Cloud environment. Such changes can also originate from developers and simply be accidental, due to unawareness, or the result of typos and other mistakes.

You can help reduce the risk of inadvertently applying risky changes by configuring deployment pipelines to apply additional integrity controls. Such controls can include:

  * Performing static analysis of code and configuration
  * Requiring all changes to pass a set of rules (policy as code)
  * Limiting the number of changes that can be done at the same time



## What's next

  * Learn about our best practices for [using service accounts in deployment pipelines](https://docs.cloud.google.com/iam/docs/best-practices-for-using-service-accounts-in-deployment-pipelines).
  * Review our [best practices for securing service accounts](https://docs.cloud.google.com/iam/docs/best-practices-for-securing-service-accounts).
  * Learn more about [Investigating and responding to threats](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-29 UTC."],[],[]] 
