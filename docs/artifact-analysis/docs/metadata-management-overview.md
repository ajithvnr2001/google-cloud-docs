---
url: https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview/
title: Metadata management overview \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:27.101428+00:00
---

# Metadata management overview  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Metadata management overview Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces key concepts for metadata management and its importance in a secure software delivery chain.

One of the aspects of a secure supply chain is keeping track of the lifespan of a software artifact. For compliance purposes, this tracking information might need to be available even well after the artifact is retired. This can be achieved by generating and storing metadata that describes important events about an artifact or a software resource: a container image, a virtual machine, or a software package.

Artifact Analysis lets you store metadata information associated with a resource, this metadata can be later retrieved to audit your software supply chain.

## How Artifact Analysis stores metadata

Artifact Analysis is built on top of [Grafeas](https://grafeas.io), an open source component metadata API that can work as a centralized source of truth for tracking and enforcing policies. Build, auditing, and compliance tools can use Grafeas to store, query and retrieve comprehensive metadata about software components.

Because Grafeas is open source, you are not locked in to a particular vendor. Grafeas associates metadata using a unique software identifier. It decouples the artifact storage, so you can store metadata about components from many different repositories. The same principles apply to Artifact Analysis, you can use it as a centralized universal metadata store for software components in Artifact Registry or any other location.

The Grafeas model involves two entities:

  * A **provider** that creates metadata stored in **notes**.
  * A **customer** that identifies if the metadata stored in a note applies to their artifacts. If that's the case, the metadata is represented as an **occurrence** of a note.



### Note

A [note](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes) describes a high-level piece of metadata. For example, you can create a note about [build provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance) so that customers see that an artifact was built using a specific, trusted build system. You can also use a note to store information about the builder of a build process. Providers that perform the analysis typically own and create notes. Customers that want to use the metadata can then identify occurrences of notes within their projects.

We recommend that you store notes and occurrences in separate projects, allowing for more fine-grained access control.

Notes must be editable only by the note owner, and read-only for customers who have access to occurrences referencing them.

**Important:** As of September 2025, Artifact Analysis no longer supports storing 3rd-party vulnerabilities in notes. Artifact Analysis now only supports note storage for vulnerabilities generated from Google Cloud scans.

### Occurrence

An [occurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences) represents when a note was found on a software artifact; it can be thought of as an instantiation of a note. For example, an occurrence of a note about a vulnerability would describe the package that the vulnerability was found in and specific remediation steps. Alternatively, an occurrence of a note about build details would describe the container images that resulted from a build.

Typically, occurrences are stored in separate projects than those where notes are created. Write access to occurrences should only be granted to users who have access to link a note to the occurrence. Any user can have read access to occurrences.

## Supported metadata types

The following table lists the [metadata types](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/NoteKind) that Artifact Analysis supports. Third-party metadata providers can store and retrieve all of the following metadata types for their customers' images.

Metadata type | Usage in Google Cloud services  
---|---  
**Vulnerability** provides vulnerability information for audited files. | Artifact Analysis generates vulnerability occurrences based on [external databases](https://docs.cloud.google.com/artifact-analysis/docs/on-demand-scanning#vulnerability_sources) of publicly disclosed security issues.  
**Build** provides information on build provenance. | Cloud Build generates this metadata and Artifact Analysis stores the information if you use Cloud Build to build the image.  
**Package** contains information about the packages installed in your image. |   
**Discovery** contains information about the initial scan of images. | Artifact Analysis provides this information only for vulnerability scans.  
**Attestation** contains image [certification information](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). | Yes. [Binary Authorization](https://docs.cloud.google.com/binary-authorization) reads this information and can use it to [gate deployments](https://docs.cloud.google.com/build/docs/securing-builds/secure-deployments-to-run-gke).  
**Vulnerability assessment** stores an uploaded VEX statement in the Grafeas [VulnerabilityAssessment note](https://github.com/grafeas/grafeas/blob/master/proto/v1/vex.proto#L28) format. |   
**SBOM reference** provides additional metadata to help you locate and verify SBOMs. |   
  
## What's next

  * [Provide metadata](https://docs.cloud.google.com/artifact-analysis/docs/store-retrieve-metadata) for your images.
  * Grant granular control over your metadata by [configuring access control](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
