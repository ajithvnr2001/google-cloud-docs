---
url: https://docs.cloud.google.com/build/docs/view-build-security-insights/
title: View build security insights \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:07.970562+00:00
---

# View build security insights  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/view-build-security-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  View build security insights Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view security information about your Cloud Build builds using the **Security insights** side panel in the Google Cloud console.

The **Security insights** side panel provides a high-level overview of multiple security metrics. You can use the side panel to identify and mitigate risks in your build process.

![Security insights panel](https://docs.cloud.google.com/build/images/build-sds-panel.png)

This panel displays the following information:

  * **Supply-chain Levels for Software Artifacts (SLSA) Level** : Identifies the maturity level of your software build process in accordance with the [SLSA specification](https://slsa.dev/spec/v1.0/levels). For example, this build has achieved SLSA Level 3.
  * **Vulnerabilities** : An overview of any vulnerabilities found in your artifacts, and the name of the image that [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) has scanned. You can click the image name to view vulnerability details. For example, in the screenshot, you can click **java-guestbook-backend**.
  * [**Vulnerability Exploitability eXchange (VEX) status**](https://docs.cloud.google.com/artifact-analysis/docs/upload-vex) for the built artifacts.
  * [**Software bill of materials (SBOM)**](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview) for the build artifacts.
  * **Build details** : Details of the build such as the builder and the link to view logs.



To learn how you can use Cloud Build with other Google Cloud products and features to improve the security posture of your software supply chain, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## Enable vulnerability scanning

The **Security insights** panel displays data from Cloud Build and from [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis). Artifact Analysis is a service that scans for vulnerabilities in OS, Java (Maven) and Go packages when you upload build artifacts to Artifact Registry.

You must enable vulnerability scanning to receive the complete set of **Security insights** results.

  1. Enable the Container Scanning API to turn on vulnerability scanning.

[Enable the Container Scanning API](https://console.cloud.google.com/apis/enableflow?apiid=containerscanning.googleapis.com)

  2. Execute a build and [store your build artifact in Artifact Registry](https://docs.cloud.google.com/build/docs/building/store-artifacts-in-artifact-registry). Artifact Analysis automatically scans the build artifacts.




Vulnerability scanning may take a few minutes, depending on the size of your build.

For more information on vulnerability scanning, see [Automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

There is a cost for scanning. See the [Pricing page](https://cloud.google.com/artifact-analysis/pricing) for pricing information.

## Grant permissions to view insights

To view **Security insights** in Google Cloud console, you must have the following [IAM roles](https://docs.cloud.google.com/iam/docs/overview), or a role with equivalent permissions. If Artifact Registry and Artifact Analysis are running in different projects, you must add the Container Analysis Occurrences Viewer role or equivalent permissions in the project where Artifact Analysis is running.

  * [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`): View insights for a build.
  * [Container Analysis Occurrences Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`): View vulnerabilities and other dependency information.



## View the Security insights side panel

To view the **Security insights** panel:

  1. Open the **Build History** page in the Google Cloud console:

[Open the Build History page](https://console.cloud.google.com/cloud-build/builds)

  2. Select your project and click **Open**.

  3. In the **Region** drop-down menu, select the region in which you ran your build.

  4. In the table with the builds, locate the row with the build for which you want to view security insights.

  5. Under the **Security insights** column click **View**.

This opens the **Security insights** side panel.

  6. (Optional) If your build produces multiple artifacts, select the artifact for which you want to view security insights from the **Artifact** drop-down box.

![Security insights panel for multi-container builds](https://docs.cloud.google.com/build/images/multi-container-sds-panel.png)

This displays the **Security insights** panel for the selected artifact.




### SLSA level

The [SLSA level](https://slsa.dev/spec/v1.0/levels) rates your build's current level of security assurance based on a collection of [guidelines](https://slsa.dev/spec/v1.0/).

### Vulnerabilities

The **Vulnerabilities** card displays the vulnerability occurrences, available fixes, and VEX status for the build artifacts.

[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) supports scanning for container images pushed to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview). The scans detect vulnerabilities in operating system packages, and in application packages created in Java (Maven) or Go.

Scanning results are organized by [severity level](https://docs.cloud.google.com/artifact-analysis/docs/os-scanning-automatically#severity_levels_for_vulnerabilities). The severity level is a qualitative assessment based on exploitability, scope, impact, and maturity of the vulnerability.

Click the image name to see the artifacts that have been scanned for vulnerabilities.

For every container image pushed to Artifact Registry, Artifact Analysis can store an associated VEX statement. VEX is a type of security advisory that indicates whether a product is affected by a known vulnerability.

Each VEX statement provides:

  * The publisher of the VEX Statement
  * The artifact for which the statement is written
  * The vulnerability assessment (VEX status) for any known vulnerabilities



## Dependencies

The **Dependencies** card shows a list of SBOMs with a list of dependencies.

When you build a container image using Cloud Build and push it to Artifact Registry, Artifact Analysis can generate SBOM records for the pushed images.

An SBOM is a full inventory of an application, identifying the packages your software relies on. The contents can include third-party software from vendors, internal artifacts, and open source libraries.

### Build

The Build card includes the following information:

  * **Logs** \- links to your build log information
  * **Builder** \- builder name
  * **Completed** \- time elapsed since the build completed
  * **Provenance** \- verifiable metadata about a build



Provenance metadata includes details such as the digests of the built images, the input source locations, the build toolchain, build steps, and the build duration. You can also [validate build provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#validate-provenance) at any time.

To ensure that your future builds include provenance information, configure Cloud Build to [require that your images have provenance metadata](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#require-provenance-metadata-for-your-build).

## What's next

  * Learn about [software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).
  * Learn [software supply chain security best practices](https://docs.cloud.google.com/software-supply-chain-security/docs/practices).
  * Learn how to [store and view build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
