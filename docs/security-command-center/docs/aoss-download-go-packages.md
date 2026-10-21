---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-download-go-packages/
title: Download Go packages using direct repository access \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:54.286312+00:00
---

# Download Go packages using direct repository access  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-download-go-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Download Go packages using direct repository access Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

After you [integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc), Assured Open Source Software packages are hosted in an Artifact Registry repository that is created in a project that you control.

This document explains how you can connect to the Artifact Registry repository for Assured OSS to directly access and download the Go packages.

This document applies to the Assured OSS premium tier only. For the free tier, see [Download Go packages using direct repository access for the free tier](https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages).

## Before you begin

  1. To get the permissions that you need to get the base64-encoded string of the service account key, ask your administrator to grant you the [Service Account Key Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. [Integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).

  3. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Security Command Center for the requested service accounts.

  4. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  5. If you've installed the Google Cloud CLI previously, check that you have the latest version by running this command:
         
         gcloud components update




## Set up authentication

To set up authentication, see [Set up authentication for Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication).

## Download Go packages

  1. In gcloud CLI, install [Go 1.15](https://go.dev/doc/install) or later.

  2. Install the gcloud CLI add-on for Go:
         
         gcloud components install package-go-module
         

  3. Instruct Go to download modules from the Assured OSS repository:
         
         export GOPROXY=https://us-go.pkg.dev/PROJECT_ID/assuredoss-go
         

Replace PROJECT_ID with the ID of the project that you selected when you set up Assured OSS.

  4. Exclude the module that you're developing from being checked using the public checksum database:
         
         export GONOSUMDB=MODULE_PATH_REGEX
         

  5. Add your Artifact Registry credentials to your `netrc` file with the Go credential helper:
         
         GOPROXY=proxy.golang.org \
           go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.1.0 \
           add-locations --locations=us \
           --json_key=KEY_FILENAME.json
         




## What's next

  * [Access security metadata and verify packages in the premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata).
  * Review the [list of supported Go packages](https://docs.cloud.google.com/security-command-center/docs/aoss-supported-packages-go-premium).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
