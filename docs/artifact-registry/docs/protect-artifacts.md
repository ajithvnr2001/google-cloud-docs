---
url: https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts/
title: Control access and protect artifacts \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:55.327898+00:00
---

# Control access and protect artifacts  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Control access and protect artifacts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Google Cloud services and features that help you to safeguard your artifacts.

## Encryption at rest

By default, Google Cloud automatically [encrypts data when it is at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can create repositories encrypted with [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK).

## Access control

By default, all repositories are private. Follow the security principle of least privilege and only grant the minimum [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) that are required by users and service accounts.

## Restrict artifact downloads

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can [restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads). Download rules let you allow or deny artifact downloads from your repositories and packages. You can also set conditions so the rule applies to specific tags or versions.

For each repository in your project, you can have one download rule at the repository level and one download rule per package. When a client attempts a download, Artifact Registry first checks for a download rule on the artifact's package. If a rule doesn't exist, or the rule's conditions don't apply to the artifact, Artifact Registry checks for a rule on the repository.

For example, you can create a rule for your repository to deny all downloads, and then create a rule for a package to allow downloads from that particular package. The package-level rule takes precedence and only artifacts belonging to that package can be downloaded from the repository.

Download rules are available on all repository modes and for the following repository formats:

  * Apt
  * Docker
  * Go
  * Maven
  * npm
  * Python

**Note:** Download rules apply only to client-based artifact download requests such as Docker pulls, Maven downloads or npm installs. Download rules don't apply to manual Google Cloud CLI pulls and API-based downloads such as the [download file](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files) command. Container pushes and metadata listings are separate operations, and can't be evaluated in the CEL schema.

## Prevent data exfiltration

To prevent data exfiltration, you can use [VPC Service Controls](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc) to place Artifact Registry and other Google Cloud services in a network security perimeter.

## Vulnerability scanning

[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs) can scan container images for security vulnerabilities in [publicly monitored packages](https://docs.cloud.google.com/artifact-analysis/docs/vulnerability-scanning#sources).

The following options are available:

[Automatic vulnerability scanning](https://docs.cloud.google.com/artifact-analysis/docs/vulnerability-scanning)
    When enabled, this feature identifies package vulnerabilities in your container images. Images are scanned when they are uploaded to Artifact Registry and the data is continuously monitored to find new vulnerabilities for up to 30 days after pushing the image.
[On-Demand Scanning API](https://docs.cloud.google.com/artifact-analysis/docs/on-demand-scanning)
    When enabled, you can manually scan local images or images stored in Artifact Registry. This feature helps you to detect and address vulnerabilities early in your build pipeline. For example, you can use Cloud Build to scan an image after it is built and then [block upload to Artifact Registry](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild) if the scan detects vulnerabilities at a specified severity level. If you also enabled automatic vulnerability scanning, Artifact Analysis also scans images you upload to the registry.

## Deployment policy

You can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) to configure a policy that the service enforces when an attempt is made to deploy a container image to one of the [supported Google Cloud environments](https://docs.cloud.google.com/binary-authorization/docs/overview#supported_platforms).

For example, you can configure Binary Authorization to only allows deployments if an image is signed for compliance with a vulnerability scan policy.

## Removing unused images

Remove unused container images to reduce storage costs and mitigate the risks of using old software.

## Shifting left on security

Integrating information security objectives into daily work can help increase software delivery performance and build more secure systems. This idea is also known as _shifting left_ , because concerns, including security concerns, are addressed earlier in the software development lifecycle (that is, left in a left-to-right schedule diagram). Shifting left on security is one of the DevOps capabilities identified in the [DORA State of DevOps research program](https://dora.dev/).

To learn more:

  * Read about the [Shifting left on security](https://dora.dev/devops-capabilities/technical/shifting-left-on-security/) capability. 
  * Read the whitepaper [Shifting left on security](https://docs.cloud.google.com/solutions/shifting-left-on-security), which describes responsibilities, practices, processes, tools, and techniques that increase confidence in the software development lifecycle (SDLC) and reduce security-risk concerns. 



## Considerations for public repositories

Carefully consider the following cases:

  * Usage of artifacts from public sources
  * Making your own Artifact Registry repositories public



### Using artifacts from public sources

The following public sources of artifacts provide tools you might use or dependencies for your builds and deployments:

  * [GitHub](http://github.com/)
  * [Docker Hub](https://hub.docker.com/)
  * [PyPI](https://pypi.org)
  * [npm public registry](https://registry.npmjs.org)



However, your organization might have constraints that impact your use of public artifacts. For example:

  * You want to control the content of your software supply chain.
  * You don't want to depend on an external repository.
  * You want to strictly control vulnerabilities in your production environment.
  * You want the same base operating system in every image.



Consider the following approaches secure your software supply chain:

  * Set up automatic builds so that your artifacts have consistent, known content. You can use Cloud Build [build triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds) or other continuous integration tools.


  * Use standardized base images. Google provides some [base images](https://github.com/GoogleContainerTools/base-images-docker) that you can use.


  * Address vulnerabilities in your artifacts. You can use [On-Demand Scanning API](https://docs.cloud.google.com/artifact-analysis/docs/on-demand-scanning) to scan container images for vulnerabilities before storing them in Artifact Registry. [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs) can also scan containers that you push to Artifact Registry.


  * Enforce your internal standards on image deployments. [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) provides enforcement for container image deployments to [supported Google Cloud environments](https://docs.cloud.google.com/binary-authorization/docs/overview#supported_platforms).



### Public Artifact Registry repositories

You can make an Artifact Registry repository public by granting the Artifact Registry Reader role to the `allUsers` identity.

If all your users have Google Cloud accounts, you can limit access to authenticated users with the `allAuthenticatedUsers` identity instead.

Consider the following guidelines before making an Artifact Registry repository public:

  * Verify that all artifacts you store in the repository are sharable publicly and do not expose credentials, personal data, or confidential data.
  * By default, projects have unlimited per-user [quotas](https://docs.cloud.google.com/artifact-registry/quotas). To prevent abuse, [cap](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage) per-user quotas within your project.

\- You are charged for [network data transfer](https://docs.cloud.google.com/artifact-registry/pricing#data-transfer) when users download artifacts. If you expect a lot of internet download traffic, consider the associated costs. 

## Guidance for web applications

  * The [OWASP Top 10](https://owasp.org/www-project-top-ten/) lists the top web application security risks according to the Open Web Application Security Project (OSWAP).



## Guidance for containers

  * [Docker best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) includes recommendations for building images.


  * The Center for Internet Security (CIS) has a [Docker Benchmark](https://www.cisecurity.org/benchmark/docker/) for evaluating the security of a Docker container.

Docker provides an open source script called [Docker Bench for Security](https://github.com/docker/docker-bench-security). You can use the script to validate a running Docker container against the CIS Docker Benchmark.

Docker Bench For Security can help you verify many items in the CIS Docker Benchmark, but not all items are verifiable with the script. For example, the script cannot verify if the host for the container is hardened or if the container image includes personal data. Review all items in the benchmark and identify those that might need additional verification.




## What's next

[Learn more about dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
