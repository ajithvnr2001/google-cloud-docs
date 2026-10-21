---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds/
title: Safeguard builds \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:06.696833+00:00
---

# Safeguard builds  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Safeguard builds Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for protecting your builds. Building code can refer to different types of operations, such as:

  * Optimizing or obfuscating code: For example, the Google open source tool [Closure Compiler](https://developers.google.com/closure/compiler/) parses and analyzes JavaScript, removes dead code, and rewrites and minimizes what's left. It also checks the code for common JavaScript pitfalls.
  * Compiling code into intermediate code: For example, you can compile Java code into a Java class file (`.class`), or C++ code into an object file (`.obj`).
  * Compiling code and linking, creating a library or executable file: For example, compiling C++ code into a Shared Library (`.so`) or a Windows executable file (`.exe`).
  * Packaging code into a distributable or deployable format: Examples include creating Java WAR (`.war`) files from Java class files, creating a Docker image, or creating a Python built distribution (`.whl`).



Depending on the programming language you use and the environment you deploy to, your build might contain different combinations of these operations. For example, a build might package Python code into a built distribution and upload it to an artifact store like [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) or [PyPI](https://pypi.org/) so that you can use it as a dependency in Cloud Run functions. You could also containerize the Python code and deploy the container image to Cloud Run or Google Kubernetes Engine.

The practices in this document focus on building code for packaging or deployment to runtime environments rather than compiling code.

## Use automated builds

An _automated build_ or _scripted build_ defines all build steps in build script or build configuration, including steps to retrieve source code and steps to build the code. The only manual command, if any, is the command to run the build.

For example, a build script can be:

  * A Cloud Build `cloudbuild.yaml`.
  * A Makefile that you run with the `make` tool.
  * A GitHub Actions workflow file in YAML format stored in your `.github/workflows/` directory.



Automated builds provide consistency in the build steps. However, it's also important to run builds in a consistent, trusted environment.

Although local builds can be useful for debugging purposes, releasing software from local builds can introduce a lot of security concerns, inconsistencies and inefficiencies into the build process.

  * Allowing local builds provides a way for an attacker with malicious intent to modify the build process.
  * Inconsistencies in developer local environments and developer practices make it difficult to reproduce builds and diagnose build issues.



Manual builds make the process inefficient by leveraging more infrastructure resources such as compute, storage and networks. In the [requirements](https://slsa.dev/spec/v0.1/requirements) for the [SLSA](https://slsa.dev) framework, automated builds are a requirement for SLSA level 1, and using a build service instead of developer environments for builds is a requirement for SLSA level 2.

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) is the managed build service on Google Cloud. It uses a [build config](https://docs.cloud.google.com/build/docs/build-config) file to provide build steps to Cloud Build. You can configure builds to fetch dependencies, run unit tests, static analyses, and integration tests, and create artifacts with build tools such as Docker, Gradle, Maven, Go, and Python. Cloud Build is fully integrated with other CI/CD services on Google Cloud such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) and [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview), as well as runtime environments such as [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) It also provides integration with major source code management systems such as GitHub and Bitbucket.

## Generate build provenance

[Build provenance](https://slsa.dev/provenance/v0.1) is a collection of verifiable data about a build.

Provenance metadata includes details such as the digests of the built images, the input source locations, the build toolchain, and the build duration.

Generating build provenance helps you to:

  * Verify that a built artifact was created from a trusted source location and by a trusted build system.
  * Identify code injected from an untrusted source location or build system.



You can use alerting and policy mechanisms to proactively use build provenance data. For example, you can create policies that only allow deployments of code built from verified sources.

For SLSA level 1, build provenance must be available to consumers of the built artifacts. For SLSA level 2, the build provenance data must also be:

  * Generated by the build service or readable directly from the build service.
  * Verifiable by a consumer for authenticity and integrity. This should be done with a digital signature generated by the service that creates the build provenance data.



For SLSA level 3, the provenance content must also include:

  * The entry point of the build definition.
  * All build parameters under a user's control.



[Cloud Build](https://docs.cloud.google.com/build/docs/overview) can generate build provenance for container images that provide SLSA level 3 build assurance. For more information, see [Viewing build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance).

## Use an ephemeral build environment

Ephemeral environments are temporary environments that are meant to last for a single build invocation. After the build, the environment is wiped or deleted. Ephemeral builds ensure that the build service and build steps run in an ephemeral environment, such as a container or VM. Instead of reusing an existing build environment, the build service provisions a new environment for each build and then destroys it after the build process is complete.

Ephemeral environments ensure clean builds since there are no residual files or environment settings from previous builds that can interfere with the build process. A non-ephemeral environment provides an opportunity for attackers to inject malicious files and content. An ephemeral environment also reduces maintenance overhead and reduces inconsistencies in the build environment.

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) sets up a new virtual machine environment for every build and destroys it after the build.

## Restrict access to the build service

Follow the security principle of least privilege by granting the minimum required permissions to the build service and build resources. You should also use a non-human identity to run builds and interact with other services on behalf of the build.

If you use Cloud Build:

  * Grant the minimum required [permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions) to members of your organization.
  * Customize the permissions for the service account that acts on behalf of Cloud Build so that it only has permissions necessary for your usage. Edit the permissions of the default [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account), or consider using a [custom service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) instead.
  * Use the Cloud Build [Allowed integrations](https://docs.cloud.google.com/build/docs/securing-builds/limit-builds-external-services) organization policy to control the external services that are allowed to invoke build triggers.
  * Place Cloud Build in a service perimeter using [VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls). The perimeter allows free communication between Google Cloud services within the perimeter, but limits communication across the perimeter based on rules that you specify. The perimeter also mitigates the risk of data exfiltration.

Cloud Build only supports VPC Service Controls for builds that you run in a [private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).




## Protect credentials

Builds often include connections to other systems such as version control, artifact stores, and deployment environments. Protecting credentials that you use in your builds helps to prevent unauthorized access to systems in your software supply chain and exfiltration of data.

Avoid storing hard coded credentials directly in version control or in your build configuration. Instead, store credentials in a secure keystore.

In Google Cloud, [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) securely stores API keys, passwords, and other sensitive data. You can configure Cloud Build to [use secrets stored in Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets).

## Manage your dependencies

The integrity of your applications relies on the integrity of both the code you develop and any dependencies you use. You also need to consider where you publish your dependencies, who has access to read and write to your artifact repositories, and policies for trusted sources of build artifacts that you deploy into your runtime environments.

To learn more about dependency management, see [Manage dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).

In Cloud Build, you use [cloud builders](https://docs.cloud.google.com/build/docs/cloud-builders) to run commands. Builders are container images with common languages and tools installed in them. You can use public container images from public registries such as Docker Hub, builders provided by Cloud Build, community-contributed builders, and custom builders that you create. You can also use [buildpacks](https://buildpacks.io/) as builders, including [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview).

Review the builders that you use in your Cloud Build builds, find out who provides them, and decide if you trust them in your software supply chain. To maintain more control over the code in a builder, you can [create custom builders](https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders#creating_a_custom_builder) instead of using builders from a public source.

## Reduce opportunities to alter the build

There are a variety of other factors that can influence a build, including:

  * Builds that run concurrently and are able to influence each other, or a build that persists and impacts a subsequent build.
  * Builds that accept user parameters other than the build entry point and the top-level source location.
  * Builds that specify dependencies with ranges or dependencies that are mutable, (for example using an image with the `latest` tag). These approaches create risk for builds to use bad or unwanted versions of dependencies.



The following practices help to mitigate these risks:

  * Run each build in an ephemeral environment.
  * Avoid running builds with additional parameters so that users cannot influence variables defined in the build scripts.
  * Restrict access to the build service and build resources.
  * Reference immutable versions of dependencies instead of identifiers such as tags that can point to a different version of the artifact in the future. For more information about dependencies, see [Dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).



## Software supply chain security

Google Cloud provides a set of modular capabilities and tools that you can use to improve the security posture of your software supply chains. It [displays security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/build-view-security-insights) for built applications built by Cloud Build. This includes:

  * The SLSA level, which identifies the maturity level of your software supply chain security.
  * Vulnerabilities, software bill of materials (SBOM), and Vulnerability Exploitability eXchange (VEX) statements for build artifacts.
  * Build provenance, which is a collection of verifiable metadata about a build. It includes details such as the digests of the built images, the input source locations, the build toolchain, build steps, and the build duration.



For instructions on viewing security insights for built applications, see [Build an application and view security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/build-view-security-insights).

## What's next

  * Learn the [best practices to safeguard source code](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-source).
  * Learn the [best practices to safeguard dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).
  * Learn the [best practices to safeguard deployments](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-deploys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
