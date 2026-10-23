---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-remote-repository-access/
title: Download Assured OSS packages using a remote repository \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:11.027183+00:00
---

# Download Assured OSS packages using a remote repository  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-remote-repository-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Download Assured OSS packages using a remote repository Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how you can set up a remote repository to access and download Assured OSS packages. You have two options for setting up a remote repository: JFrog Artifactory or Sonatype Nexus. For more information about repository options, see [Assured OSS repository options](https://docs.cloud.google.com/assured-open-source-software/docs/overview#aoss-repository-options).

This document applies to the [Assured OSS Premium tier](https://docs.cloud.google.com/assured-open-source-software/docs/overview) only. For other Assured OSS tiers, see [Download Assured OSS packages using a remote repository](https://docs.cloud.google.com/assured-open-source-software/docs/remote-repository-access).

## Before you begin

  1. [Integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).

  2. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Security Command Center for the requested service accounts.




## Set up a remote repository using JFrog Artifactory

  1. Sign in to the JFrog Artifactory repository manager. Ensure that you have the required privileges to create a new remote repository.
  2. Select the option to create a new remote repository in your repository manager.
  3. Select the appropriate repository type (for example, select `Maven` for Java, `PyPi` for Python, `npm` for JavaScript, or `Go` for Go).
  4. Optionally, test the connection to the repository using the following steps:

     1. In the **Repository Key** field, enter a unique name or identifier for the remote repository.
     2. In the **URL** field, enter one of the following:

        * Java: 
              
              https://us-maven.pkg.dev

        * Python: 
              
              https://us-python.pkg.dev

        * JavaScript (NPM): 
              
              https://us-npm.pkg.dev

        * Go: 
              
              https://us-go.pkg.dev

Don't enter the complete domain name because this action might return an HTTP `404` or HTTP `405` status code.

     3. Leave the remaining fields blank.

     4. Click **Test**. The connection is successful when you see the following output:

`Successfully connected to server`

  5. To create a new remote repository, enter the following information:

     1. In the **Repository Key** field, enter a unique name or identifier for the remote repository. For example, `assured-oss-java-repo`.
     2. In the **URL** field, enter one of the following:

        * Java: 
              
              https://us-maven.pkg.dev/PROJECT_ID/assuredoss-java

        * Python: 
              
              https://us-python.pkg.dev/PROJECT_ID/assuredoss-python

        * JavaScript (NPM): 
              
              https://us-npm.pkg.dev/PROJECT_ID/assuredoss-javascript

        * Go: 
              
              https://us-go.pkg.dev/PROJECT_ID/assuredoss-go

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured OSS.

     3. In the **User Name** field, enter `_json_key_base64`.

     4. In the **Password** field, provide the base64-encoded string of the service account JSON key file. Use the entire base64-encoded string in a single line as password. To get the base64-encoded string, run the command `cat key-filename.json | base64 -w 0`.

     5. For Python only, in the **Registry URL** field, enter the following: 
            
            https://us-python.pkg.dev/PROJECT_ID/assuredoss-python

  6. For Go only, in the **Advanced Settings** tab, select **Bypass HEAD Requests**.

  7. Click **Create Remote Repository**.

For Python packages, append the obtained URL with `/simple`. Use the URL as the `index-url` in the `pip install` command to download the required Python packages. For example, if the obtained URL of the repository is `https://a0a87smb7hcda.jfrog.io/artifactory/api/pypi/assured-oss-python-repo`, then the corresponding `index-url` is `https://a0a87smb7hcda.jfrog.io/artifactory/api/pypi/assured-oss-python-repo/simple`.




After the new remote repository is set up, configure your build tools (for example, Apache Maven, Gradle Build Tool, or pip) to use this new remote repository.

### Known issues

Testing the connection using the **Test** button can return an error even if the connection is configured correctly. We recommend that you create the remote repository irrespective of the test button behavior. For another way of confirming a connection, see [Validate your connection](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection).

## Set up a remote repository using Sonatype Nexus

  1. Sign in to your Sonatype Nexus repository manager. Ensure that you have the required privileges to create a new remote repository.
  2. Select the option to create a new repository.
  3. Select the appropriate repository type (for example, select `Maven` for Java, `PyPi` for Python, `npm` for JavaScript, or `Go` for Go).
  4. Enter the following details for the new repository:

     1. In the **Name** field, enter a unique name or identifier for the remote repository.
     2. In the **Remote Storage** field, choose from the following:

        * Java: 
              
              https://us-maven.pkg.dev/PROJECT_ID/assuredoss-java

        * Python: 
              
              https://us-python.pkg.dev/PROJECT_ID/assuredoss-python

        * JavaScript (NPM): 
              
              https://us-npm.pkg.dev/PROJECT_ID/assuredoss-javascript

        * Go: 
              
              https://us-go.pkg.dev/PROJECT_ID/assuredoss-go

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured OSS.

  5. Under **HTTP** , select **Authentication**.

  6. Specify the following:

     1. In the **Authentication type** field, enter `Username`.
     2. In the **Username** field, enter `_json_key_base64`.
     3. In the **Password** field, provide the base64-encoded string of the service account JSON key file. Use the entire base64 encoded-string in a single line as password. To get the base64-encoded string, run the command `cat key-filename.json | base64`.
  7. Click **Create Repository**.




After the new remote repository is set up, point your build tools (for example, Apache Maven, Gradle Build Tool, or pip) to use this new remote repository.

## What's next

  * [Download Go packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-go-packages)
  * [Download Java packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-java-packages)
  * [Download NPM packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-npm-packages)
  * [Download Python packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-python-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
