---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication/
title: Sign in to Docker and Helm \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:19.286092+00:00
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

This document describes how to sign in to Docker or Helm using CLI secrets.

Harbor registry instances in Google Distributed Cloud (GDC) air-gapped appliance use Identity-Aware Proxy (IAP) for authentication. After you sign in to the Harbor web interface using IAP for the first time, you can retrieve a static CLI secret from your Harbor user profile and use it as your password when signing in from the Docker or Helm CLI. This method is only available with the Harbor UI.

## Before you begin

### Required IAM roles

To configure authentication for Harbor registry instances, contact your Project IAM Admin to request the **Harbor Instance Viewer** (`harbor-instance-viewer`) role, which lets you get, list, and watch Harbor instances in the project namespace. This role includes the required permissions to view the details of existing Harbor instances so you can retrieve the registry URLs for authentication.

## Sign in with CLI secrets

To sign in to Docker or Helm with CLI secrets, follow these steps:

  1. Sign in to Harbor with an IAP user account.
  2. Click your username and select **User Profile**.
  3. To copy the CLI secret associated with your account, click content_copy **Copy**.
  4. Optional: To display buttons for automatically generating or manually creating a new CLI secret, click more_horiz **More** in your user profile.

**Note:** You can have only one CLI secret. When a new secret is generated or created, the old secret becomes invalid.
  5. If you generated a new CLI secret, click content_copy **Copy** to copy it.

  6. Use your CLI secret as the password when signing in to Harbor from the Docker or Helm CLI:
         
         docker login -u USERNAME -p CLI_SECRET HARBOR_INSTANCE_URL
         

Replace the following:

     * `USERNAME`: the Harbor account username.
     * `CLI_SECRET`: the generated CLI secret.
     * `HARBOR_INSTANCE_URL`: the URL of the Harbor instance.
**Note:** The CLI secret doesn't expire unless you manually rotate it. The CLI secret isn't associated with your user identity token. Signing out from Harbor or the GDC console doesn't revoke the CLI secret.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
