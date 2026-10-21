---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication/
title: Sign in to Docker and Helm \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:13.516550+00:00
---

# Sign in to Docker and Helm  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Sign in to Docker and Helm Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to sign in to Docker or Helm using the Managed Harbor Service (MHS) credential helper or CLI secrets.

To provide flexibility, Google Distributed Cloud (GDC) air-gapped appliance provides two methods to authenticate with Docker and Helm from your Harbor registry instance. The first method is using the Managed Harbor Service (MHS) credential helper and your GDC identity to sign in to the Docker or Helm CLI. After authenticating with GDC, you can sign in to the Docker client and perform Docker operations, without having to create or manage separate CLI secrets in Harbor.

The second method is using CLI secrets. After you authenticate using Identity-Aware Proxy (IAP) and sign in to the Harbor interface for the first time, use the Docker or Helm CLI to access Harbor. The Docker and Helm CLIs cannot handle redirection for IAP, so Harbor provides a CLI secret to use when signing in from Docker or Helm. This method is only available when Harbor uses IAP authentication.

## Before you begin

To configure Docker and Helm authentication for Harbor registry instances, you must have the MHS credential helper (`docker-credential-mhs`) installed in your environment. The credential helper is included by default in the gdcloud CLI bundle. For more information, see [gdcloud CLI overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview).

### Required IAM roles

To configure authentication for Harbor registry instances, contact your Project IAM Admin to request the **Harbor Instance Viewer** (`harbor-instance-viewer`) role, which lets you get, list, and watch Harbor instances in the project namespace. This role includes the required permissions to view the details of existing Harbor instances so you can retrieve the registry URLs for authentication.

## Sign in to Docker or Helm with CLI secrets

To sign in to Docker or Helm with CLI secrets, follow these steps:

  1. Sign in to Harbor with an IAP user account.
  2. Click your username and select **User Profile**.
  3. To copy the CLI secret associated with your account, click content_copy **Copy**.
  4. Optional: To display buttons for automatically generating or manually creating a new CLI secret, click the more_horiz ellipses in your user profile.

**Note:** A user can only have one CLI secret. When a new secret is generated or created, the old secret becomes invalid.
  5. If you generated a new CLI secret, click content_copy **Copy** to copy it.

  6. You can now use your CLI secret as the password when signing in to Harbor from the Docker or Helm CLI:



    
    
        docker login -u USERNAME -p CLI_SECRET HARBOR_INSTANCE_URL
    

Replace the following:

  * `USERNAME`: the Harbor account username
  * `CLI_SECRET`: the generated CLI secret.
  * `HARBOR_INSTANCE_URL`: the URL of the Harbor instance.

**Note:** The CLI secret does not expire, unless you manually rotate it. The CLI secret is not associated with the user identity token. Signing out from Harbor or the GDC console does not revoke the CLI secret.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
