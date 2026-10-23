---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-download-npm-packages/
title: Download NPM packages using direct repository access \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:04.668553+00:00
---

# Download NPM packages using direct repository access  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-download-npm-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Download NPM packages using direct repository access Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

After you [integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc), Assured Open Source Software packages are hosted in an Artifact Registry repository that is created in a project that you control.

This document explains how you can connect to the Artifact Registry repository for Assured OSS to directly access and download JavaScript (NPM) packages.

This document applies to the Assured OSS premium tier only.

## Before you begin

  1. To get the permissions that you need to get the base64-encoded string of the service account key, ask your administrator to grant you the [Service Account Key Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. [Integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).

  3. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Security Command Center for the requested service accounts.

  4. [Install Node.js and `npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) on your local machine.

  5. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  6. If you've installed the Google Cloud CLI previously, check that you have the latest version by running this command:
         
         gcloud components update




## Set up authentication

To set up authentication for Node.js (NPM), configure `.npmrc` to authenticate with Artifact Registry using service account credentials or Google Cloud user credentials.

**Note:** If you are using the credential helper to authenticate with an access token, obtain a new token.

For more information, see [Set up authentication for Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication).

## Download NPM packages

  1. In your `.npmrc` file, set the registry URL for your JavaScript (NPM) packages:
         
         registry=https://us-npm.pkg.dev/PROJECT_ID/assuredoss-javascript/
         

Replace PROJECT_ID with the ID of the project that you selected when you set up Assured OSS.

  2. Install the required NPM packages by using `npm` or `yarn`:

     * `npm`:
           
           npm install package-name
           

     * `yarn`:
           
           yarn add package-name
           

Replace `package-name` with your package name or scoped package name (for example, `express` or `@scope/package-name`).




## What's next

  * [Access security metadata and verify packages in the premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata)
  * Review the [list of supported NPM packages](https://docs.cloud.google.com/security-command-center/docs/aoss-supported-packages-npm-premium)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
