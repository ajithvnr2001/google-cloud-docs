---
url: https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc/
title: Integrate with Assured OSS for code security \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:35.063895+00:00
---

# Integrate with Assured OSS for code security  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Integrate with Assured OSS for code security Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The [Assured Open Source Software (Assured OSS) premium tier](https://docs.cloud.google.com/assured-open-source-software/docs/overview) lets you enhance your code security by using the OSS packages that Google uses for its own developer workflows. When you use Assured OSS, your developers can take advantage of the security expertise and experience that Google applies to securing its own open source dependencies.

When you integrate Assured OSS with Security Command Center, you can do the following:

  * Choose from thousands of [curated and most popular Java, Python, Go, and JavaScript (NPM) packages](https://docs.cloud.google.com/security-command-center/docs/aoss-supported-packages-premium), including common machine learning and artificial intelligence projects like TensorFlow, Pandas, and Scikit-learn.
  * Configure a secure proxy to download all Java, Python, Go, and JavaScript packages with attestations from Assured OSS, making Google a known and trusted supplier.
  * Use the SBOMs and VEX in Assured OSS that are provided in industry-standard formats like SPDX and CycloneDX to know more about your ingredients.
  * Increase confidence in the integrity of the packages that you are using through signed, tamper-evident provenance from Google.
  * Reduce security risk as Google is actively scanning, finding, and fixing new vulnerabilities in curated packages.



## Before you begin

Complete these tasks before you complete the remaining tasks on this page.

### Activate Security Command Center Enterprise or Premium tier

Verify that the [Security Command Center Premium tier](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier) or [Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) is activated at the organization level.

### Set up permissions at the organization level

You must set up permissions at the organization level and the project level.

Make sure that you have the following role or roles on the organization: Security Center Admin, Organization Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



### Set up permissions at the project level

Make sure that you have the following role or roles on the project: Service Usage Admin, Service Account Admin, Project IAM Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



### Set up Google Cloud CLI

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

## Set up Assured OSS

###  Console 

These steps apply to Security Command Center Enterprise tier only.

  1. In the Google Cloud console, go to the Security Command Center **Setup guide**.

[Go to Setup guide](https://console.cloud.google.com/projectselector2/security/command-center/setup-guide?supportedpurview=organizationId)

  2. Verify that you are viewing the organization that you activated the Security Command Center Enterprise tier on.

  3. Expand the **Review security capabilities summary** panel.

  4. Click **Code security > Set up**.

  5. In the **Set up code security** panel, click **AOSS Setup**.

  6. Select a new service account or select the existing service accounts that you want to add the Assured Open Source Software permissions to.

  7. Select the Google Cloud project where you want to locate the Assured OSS resources.

  8. Click **Set up Assured OSS**.

The setup process automatically completes the following:

     * If selected, creates the new service account `assuredoss@PROJECT_ID.gservicesaccount.com`.
     * Assigns the Assured OSS User role to the designated service account to use with Assured OSS.
     * Assigns the Assured OSS Admin role to the logged in user account so that the account can configure the service.
     * Enables the Assured Open Source Software API and, if it isn't enabled already, the [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) API.
     * Sets up the Assured OSS proxy service in an Artifact Registry instance in the project that you selected. A repository is provisioned for each language (Java, Python, Go, and JavaScript (NPM)). These repositories can automatically pull packages from the curated portfolio. If a package isn't available as part of the curated portfolio, the repositories redirect the request to the canonical repositories. The proxy service supports the US region only. For more information, see [Assured OSS repository options](https://docs.cloud.google.com/assured-open-source-software/docs/overview#aoss-repository-options).
     * Grants you and the service account permissions to access package metadata and notifications from Google owned projects.
  9. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console) for each designated Assured OSS service account and download the key in JSON format.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  10. In the command line on your local machine, run the following command on the downloaded key file to get the base64-encoded string:
         
         base64 KEY_FILENAME.json
         

Replace `KEY_FILENAME.json` with the name of the service account key that you downloaded.

You need the base64-encoded string when you set up a remote repository for Assured OSS.

  11. To download the packages, use the endpoints that Assured OSS provisions for each language. Make a note of these endpoints for later use.

     * Java: 
           
           https://us-maven.pkg.dev/PROJECT_ID/assuredoss-java

     * Python: 
           
           https://us-python.pkg.dev/PROJECT_ID/assuredoss-python

     * JavaScript (NPM): 
           
           https://us-npm.pkg.dev/PROJECT_ID/assuredoss-javascript

     * Go: 
           
           https://us-go.pkg.dev/PROJECT_ID/assuredoss-go

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured OSS.

  12. Click **Next**. [Configure Assured OSS](https://docs.cloud.google.com/security-command-center/docs/aoss-remote-repository-access) with your organization's artifact repository manager such as JFrog Artifactory or Sonatype Nexus.




###  gcloud 

These steps apply to Security Command Center Premium and Enterprise.

  1. Authenticate to Google Cloud with a user account that you want to use to enable Assured OSS:
         
         gcloud auth revoke
         gcloud auth application-default revoke
         gcloud auth login
         

  2. Search for the project where you want to locate the Assured OSS resources:
         
         gcloud alpha projects search --query="displayName=PROJECT_NAME"
         

Replace `PROJECT_NAME` with the project name.

  3. Set the project where you want to locate the Assured OSS resources:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the project identifier.

  4. Grant roles to the user account to set up Assured OSS:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=user:email@domain.com \
           --role=roles/assuredoss.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=user:email@domain.com \
           --role=roles/serviceusage.serviceUsageAdmin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=user:email@domain.com \
           --role=roles/iam.serviceAccountAdmin
         

Where `email@domain.com` is the email address for your user account.

  5. Enable Assured OSS in the project. Enabling Assured OSS also enables the Artifact Registry API.
         
         gcloud services enable assuredoss.googleapis.com
         

  6. To create a new service account for Assured OSS instead of using existing service accounts, complete the following:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
           --description="Service account for using Assured OSS"
           --display-name="Assured OSS service account"
         

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account (for example, `assuredoss`).

  7. Configure the service accounts for Assured OSS:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
           --role roles/assuredoss.user
         

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name of the service account (for example, `assuredoss`).
     * `PROJECT_ID`: the project identifier.
  8. To access the security metadata repository after setting up Assured OSS premium using gcloud, send an email to [customer-support-aoss@google.com](mailto:customer-support-aoss@google.com) with the service accounts that you enabled for Assured OSS.
  9. Set up the Assured OSS proxy service in an Artifact Registry instance by creating Assured OSS repositories. You must create repositories for all languages. The Assured OSS proxy service that provisions the repositories supports the US region only.
         
         alias gcurlj='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -X'
         
         gcurlj POST https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories\?repositoryId\=assuredoss-java   -d '{"format": "MAVEN", "mode": "AOSS_REPOSITORY"}'
         
         gcurlj POST https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories\?repositoryId\=assuredoss-javascript   -d '{"format": "NPM", "mode": "AOSS_REPOSITORY"}'
         
         gcurlj POST https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories\?repositoryId\=assuredoss-python   -d '{"format": "PYTHON", "mode": "AOSS_REPOSITORY"}'
         
         gcurlj POST https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories\?repositoryId\=assuredoss-go   -d '{"format": "GO", "mode": "AOSS_REPOSITORY"}'
         

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured OSS.

These repositories can automatically pull packages from the curated portfolio. If a package isn't available as part of the curated portfolio, the repositories redirect the request to the canonical repositories.

  10. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console) for each Assured OSS service account and download the key in JSON format.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  11. In the command line, run the following command on the downloaded key file to get the base64-encoded string:
         
         base64 KEY_FILENAME.json
         

Replace `KEY_FILENAME.json` with the name of the service account key that you downloaded.

You need the base64-encoded string when you set up a remote repository for Assured OSS.

  12. To download the packages, use the endpoints provisioned by Assured OSS for each language. Make a note of these endpoints:

     * Java: 
           
           https://us-maven.pkg.dev/PROJECT_ID/assuredoss-java

     * Python: 
           
           https://us-python.pkg.dev/PROJECT_ID/assuredoss-python

     * JavaScript (NPM): 
           
           https://us-npm.pkg.dev/PROJECT_ID/assuredoss-javascript

     * Go: 
           
           https://us-go.pkg.dev/PROJECT_ID/assuredoss-go

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured OSS.

  13. [Configure Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/remote-repository-access) to download packages with your organization's artifact repository manager such as JFrog Artifactory or Sonatype Nexus.

  14. Optionally, view the available Java, Python, Go, and JavaScript packages:
         
         gcloud auth revoke
         gcloud auth application-default revoke
         gcloud auth login --cred-file=KEY_FILENAME.json
         

Replace `KEY_FILENAME.json` with the name of the service account key that you downloaded.
         
         export GOOGLE_APPLICATION_CREDENTIALS=KEY_FILENAME.json
         

Replace `KEY_FILENAME.json` with the name of the service account key that you downloaded.
         
         gcurlj GET "https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-java/packages"
         gcurlj GET "https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-python/packages"
         gcurlj GET "https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-javascript/packages"
         gcurlj GET "https://artifactregistry.googleapis.com/v1/projects/PROJECT_ID/locations/us/repositories/assuredoss-go/packages"
         

Replace `PROJECT_ID` with the ID of the project that you selected when you set up Assured OSS.




## What's next

  * [Configure support for VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc)
  * [Download Go packages](https://docs.cloud.google.com/security-command-center/docs/aoss-download-go-packages)
  * [Download Java packages](https://docs.cloud.google.com/security-command-center/docs/aoss-download-java-packages)
  * [Download NPM packages](https://docs.cloud.google.com/security-command-center/docs/aoss-download-npm-packages)
  * [Download Python packages](https://docs.cloud.google.com/security-command-center/docs/aoss-download-python-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
