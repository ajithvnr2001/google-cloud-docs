---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies/
title: Dependency management \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:06.859306+00:00
---

# Dependency management  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Dependency management Stay organized with collections  Save and categorize content based on your preferences. 

This document describes application dependencies and best practices for managing them, including vulnerability monitoring, artifact verification, reducing your dependency footprint, and supporting reproducible builds.

A software dependency is a piece of software that your application requires to function such as a software library or a plugin. Resolving dependencies can happen when you are compiling code, building, running, downloading, or installing your software.

Dependencies can include both components that you create, proprietary third-party software, and open source software. The approach you take to managing dependencies can impact the security and reliability of your applications.

Specifics for implementing best practices can vary by artifact format and the tools you use, but the general principles still apply.

## Direct and transitive dependencies

Your applications can include both direct and transitive dependencies:

Direct dependencies
    Software components that an application references directly.
Transitive dependencies
    Software components that an application's direct dependencies functionally require. Each dependency can have its own direct and indirect dependencies, creating a recursive tree of transitive dependencies that all impact the application.

Different programming languages offer different levels of visibility into dependencies and their relationships. In addition, some languages use package managers to resolve the dependency tree when installing or deploying a package.

In the Node.js ecosystem, the npm and yarn package managers use lock files to identify dependency versions for building a module and the dependency versions that a package manager downloads for a specific installation of the module. In other language ecosystems like Java, there is more limited support for dependency introspection. In addition, build systems must use specific dependency managers to systematically manage dependencies.

As an example, consider the npm module `glob` version 8.0.2. You declare direct dependencies for npm modules in the file `package.json`. In the [package.json file for glob](https://github.com/isaacs/node-glob/blob/v8.0.2/package.json), the `dependencies` section lists direct dependencies for the published package. The `devDepdencies` section lists dependencies for local development and testing by maintainers and contributors of `glob`

  * On the npm website, the [glob page](https://www.npmjs.com/package/glob/v/8.0.2) lists the direct dependencies and development dependencies, but does not indicate if these modules have their own dependencies too.

  * You can find additional dependency information about `glob` on the Open Source Insights site. The [dependency list for glob](https://deps.dev/npm/glob/8.0.2/dependencies) includes both direct dependencies and indirect (transitive) dependencies.

A transitive dependency can be multiple layers deep in the dependency tree. For example:

    1. `glob` 8.0.2 has a direct dependency on `minimatch` 5.0.1.
    2. `minimatch` 5.0.1 has has a direct dependency `brace-expression` 2.0.1.
    3. `brace-expression` 2.0.1 has a direct dependency on `balanced-match` 1.0.2.



Without visibility into indirect dependencies, it is very difficult to identify and respond to vulnerabilities and other issues that originate from a component that your code does not reference directly.

When you install the `glob` package, npm resolves the entire dependency tree and saves the list of specific downloaded versions in the file [package.lock.json](https://docs.npmjs.com/cli/v8/configuring-npm/package-lock-json) so that you have a record of all the dependencies. Subsequent installations in the same environment will retrieve the same versions.

## Tools for dependency insights

You can use the following tools to help you understand your open source dependencies and evaluate the security posture of your projects. These tools provide information across package formats.

Security insights in the Google Cloud console
    Google Cloud provides security insights for your artifacts in Cloud Build, Cloud Run, and GKE, including vulnerabilities, dependency information, software bill of materials (SBOM), and build provenance. Other Google Cloud services also provide features that improve your security posture across the software development lifecycle. To learn more, see the [software supply chain security overview](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).
Open source tools
    

A number of open source tools are available, including:

  * [Open Source Insights](https://deps.dev/): A website that provides information about known direct and indirect dependencies, known vulnerabilities, and license information for open source software. The Open Source Insights project also makes this data available as a [Google Cloud Dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-data/deps-dev). You can use [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) to explore and analyze the data.

  * [Open Source Vulnerabilities database](https://osv.dev/): A searchable vulnerability database that aggregates vulnerabilities from other databases into one location.

  * [Scorecards](https://github.com/ossf/scorecard): An automated tool that you can use to identify risky software supply chain practices in your GitHub projects. It performs checks against repositories and gives each check a score from 0 to 10. You can then use the scores to evaluate the security posture of your project.

  * [Allstar](https://github.com/ossf/allstar): A GitHub App that continuously monitors GitHub organizations or repositories for adherence to configured policies. For example, you can apply a policy to your GitHub organization that checks for collaborators outside the organization who have administrator or push access.




## Approaches to including dependencies

There are several common methods for including dependencies with your application:

Install directly from public sources
    Install open source dependencies directly from public repositories, such as Docker Hub, npm, PyPI, or Maven Central. This approach is convenient because you don't need to maintain your external dependencies. However, since you don't control these external dependencies, your software supply chain is more prone to open-source supply chain attacks.
Store copies of dependencies in your source repository
    This approach is also known as _vendoring_. Instead of installing an external dependency from a public repository during your builds, you download it and copy it into your project source tree. You have more control over the vendored dependencies that you use, but there are several disadvantages: 

  * Vendored dependencies increase the size of your source repository and introduce more churn.
  * You must vendor the same dependencies into each separate application. If your source repository or build process does not support reusable source modules, you might need to maintain multiple copies of your dependencies.
  * Upgrading vendored dependencies can be more difficult.


Store dependencies in a private registry
    

A private registry, such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview), provides the convenience of installation from a public repository as well as control over your dependencies. With Artifact Registry, you can:

  * Centralize your build artifacts and dependencies for all your applications.
  * Configure your Docker and language package clients to interact with private repositories in Artifact Registry the same way that they do with public repositories.
  * Have greater control over your dependencies in private repositories:

    * Restrict access to each repository with Identity and Access Management.
    * Use [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) to cache dependencies from upstream public sources and scan them for vulnerabilities (private preview).
    * Use [virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) to group remote and private repositories behind a single endpoint. Set a priority on each repository to control search order when downloading or installing an artifact (private preview).
  * Use Artifact Registry with other Google Cloud services, including Cloud Build, Cloud Run, and Google Kubernetes Engine. Use automatic vulnerability scanning across the software development lifecycle, generate build provenance, control deployments, and view insights about your security posture.




When possible, use a private registry for your dependencies. In situations where you cannot use a private registry, consider vendoring your dependencies so that you have control over the content in your software supply chain.

## Version pinning

Version pinning means restricting an application dependency to a specific version or version range. Ideally, you pin a single version of a dependency.

Pinning the version of a dependency helps to ensure that your application builds are reproducible. However, it also means that your builds do not include updates to the dependency, including security fixes, bug fixes, or improvements.

You can mitigate this issue using automated dependency management tools that monitor dependencies in your source repositories for new releases. These tools make updates to your requirements files to upgrade dependencies as necessary, often including changelog information or additional details.

Version pinning only applies to direct dependencies, not transitive dependencies. For example, if you pin the version of the package `my-library` the pin restricts the version of `my-library` but does not restrict the versions of software that `my-library` has a dependency. You can restrict the dependency tree for a package in some languages using a lock file.

## Signature and hash verification

There are a number of methods you can use to verify the authenticity of an artifact that you are using as a dependency.

Hash verification
    

A hash is a generated value for a file that acts as a unique identifier. You can compare the hash of an artifact with the hash value calculated by the provider of the artifact to confirm the integrity of the file. Hash verification helps you to identify replacement, tampering, or corruption of dependencies, through a man-in-the-middle attack or a compromise of the artifact repository.

Using hash verification requires trusting that the hash you receive from the artifact repository is not compromised.

Signature verification
    

Signature verification adds additional security to the verification process. The artifact repository, maintainers of the software, or both can sign artifacts.

Services such as [sigstore](https://sigstore.dev/) provide a way for maintainers to sign software artifacts and for consumers to verify those signatures.

[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) can verify that container images deployed to Google Cloud runtime environments are signed with attestations for a variety of criteria.

## Lock files and compiled dependencies

Lock files are fully resolved requirements files, specifying exactly what version of every dependency should be installed for an application. Usually produced automatically by installation tools, lock files combine version pinning and signature or hash verification with a full dependency tree for your application.

Installation tools create dependency trees by fully resolving all downstream transitive dependencies of your top-level dependencies, and then include the dependency tree in your lock file. As a result, only these dependencies can be installed, making builds more reproducible and consistent.

## Mixing private and public dependencies

Modern cloud-native applications often depend on both open source, third-party code, as well as closed-source, internal libraries. Artifact Registry lets you share your business logic across multiple applications, and reuse the same tooling to install both external and internal libraries.

However, when mixing private and public dependencies, your software supply chain is more vulnerable to a _dependency confusion_ attack. By publishing projects with the same name as your internal project to open-source repositories, attackers might be able to take advantage of misconfigured installers to install their malicious code instead of your internal dependency.

To avoid a dependency confusion attack, you can take a number of steps:

  * Verify the signature or hashes of your dependencies by including them in a lock file.
  * Separate the installation of third-party dependencies and internal dependencies into two distinct steps.
  * Explicitly mirror the third-party dependencies you need into your private repository, either manually or with a pull-through proxy. Artifact Registry [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) are pull-through proxies for upstream public repositories.
  * Use [virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) to consolidate remote and standard Artifact Registry repositories behind a single endpoint. You can configure priorities for upstream repositories so that your private artifacts versions are always prioritized over public artifacts with the same name.
  * Use trusted sources for public packages and base images. 
    * Use [Assured Open Source Software](https://docs.cloud.google.com/assured-open-source-software/docs) to access popular Java and Python images that Google has tested and verified.
    * Use Google-provided [base images](https://docs.cloud.google.com/software-supply-chain-security/docs/base-images) or a [secure image pipeline](https://docs.cloud.google.com/software-supply-chain-security/docs/create-secure-image-pipeline) for generating your own base images.



## Removing unused dependencies

As your needs change and your application evolves, you might change or stop using some of your dependencies. Continuing to install unused dependencies with your application increases your dependency footprint and increases the risk for you to be compromised by a vulnerability in those dependencies.

Once you have application working locally, a common practice is to copy every dependency you installed during the development process into the requirements file for your application. You then deploy the application with all those dependencies. This approach helps to ensure that the deployed application works, but it's also likely to introduce dependencies you don't need in production.

Use caution when adding new dependencies to your application. Each one has the potential to introduce more code that you don't have complete control over. As a part of your regular linting and testing pipeline, integrate tools that audit your requirements files to determine if you actually use or import your dependencies.

Some languages have tools to help you manage your dependencies. For example you can use the [Maven Dependency Plugin](https://maven.apache.org/plugins/maven-dependency-plugin/) to analyze and manage Java dependencies.

## Vulnerability scanning

Responding quickly to vulnerabilities in your dependencies helps you to protect your software supply chain.

Vulnerability scanning allows you to automatically and consistently assess whether your dependencies are introducing vulnerabilities into your application. Vulnerability scanning tools consume lock files to determine exactly what artifacts you depend on, and notify you when new vulnerabilities surface, sometimes even with suggested upgrade paths.

For example, [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-analysis) identifies [OS package](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) vulnerabilities in container images. It can scan images when they are uploaded to Artifact Registry and continuously monitors them to find new vulnerabilities for up to 30 days after pushing the image.

You can also use [On-Demand Scanning](https://docs.cloud.google.com/artifact-analysis/docs/on-demand-scanning-howto) to scan container images locally for [OS](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview), [Go](https://docs.cloud.google.com/artifact-analysis/docs/go-overview), and [Java](https://docs.cloud.google.com/artifact-analysis/docs/java-overview) vulnerabilities. This lets you identify vulnerabilities early so that you can address them before storing them in Artifact Registry.

## What's next

  * Learn about [software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview) components and how Google Cloud services help you to protect your software.
  * Learn about [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).
  * Learn about [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-analysis) and [types of scanning](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
