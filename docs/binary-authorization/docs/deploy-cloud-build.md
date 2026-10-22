---
url: https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build/
title: Deploy only images built by Cloud Build \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:46.357351+00:00
---

# Deploy only images built by Cloud Build  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Deploy only images built by Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to secure your software supply chain by configuring Binary Authorization to allow only container images built by Cloud Build to be deployed.

You configure this deployment control by requiring the `built-by-cloud-build` attestor in your Binary Authorization policy. Cloud Build automatically creates the `built-by-cloud-build` attestor in your project when you run a build that generates images. After images are successfully built, Cloud Build automatically signs and creates attestations for them. At deploy time, Binary Authorization verifies the attestations with the `built-by-cloud-build` attestor. Verified images are allowed to be deployed. Images that fail verification are disallowed from being deployed, and the failure is logged to Cloud Audit Logs.

For end-to-end guide that describes how to use Cloud Build-recorded metadata and Binary Authorization, see [Using signed provenance and Binary Authorization](https://docs.cloud.google.com/build/docs/securing-builds/signed-provenance-with-binauthz).

## Before you begin

To use this feature you must first do the following:

  * [Set up Binary Authorization for your platform](https://docs.cloud.google.com/binary-authorization/docs/set-up-platform).
  * [Set up Cloud Build](https://docs.cloud.google.com/build/docs/set-up) and build an image.

**Note:** If your build specifies a [location](https://docs.cloud.google.com/build/docs/locations), an attestation is created only if you explicitly set [`requestedVerifyOption`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#verifyoption) to `VERIFIED`.



## Configure the policy

In this section you configure the Binary Authorization policy to require the `built-by-cloud-build` attestor.

To allow only images built by Cloud Build to be deployed, perform the following steps:

### Console

  1. Go to the **Binary Authorization** page in the Google Cloud console:

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization)

  2. In the **Policy** tab, click **Edit Policy**.

  3. In the **Edit Policy** dialog, select **Allow only images that have been approved by all of the following attestors**.

  4. Click **Add Attestors**.

  5. In the **Add attestors** dialog box, do the following:

     1. Select **Add by project and attestor name** and perform the following steps: 
        1. In the **Project name** field, enter the project where you run Cloud Build.
        2. Click the **Attestor name** field and note that the `built-by-cloud-build` attestor is available.
        3. Click `built-by-cloud-build`.
     2. Alternatively, select **Add by attestor resource ID**. In **Attestor resource ID** , enter
            
            projects/PROJECT_ID/attestors/built-by-cloud-build
            

Replacing `PROJECT_ID` with the project where you run Cloud Build.

  6. Click **Add 1 attestor**.

  7. Click **Save Policy**.




### gcloud

  1. Export your existing policy to a file using the following command:
         
         gcloud container binauthz policy export > /tmp/policy.yaml
         

  2. Edit your policy file.

  3. Edit one of the following rules:

     * `defaultAdmissionRule`
     * `clusterAdmissionRules`
     * `istioServiceIdentityAdmissionRules`
     * `kubernetesServiceAccountAdmissionRules`
  4. Add a `requireAttestationsBy` block to the rule if there isn't one there already.

  5. In the `requireAttestationsBy` block, add
         
         projects/PROJECT_ID/attestors/built-by-cloud-build
         

Replacing `PROJECT_ID` with the project where you run Cloud Build.

  6. Save the policy file.

  7. Import the policy file.
         
         gcloud container binauthz policy import /tmp/policy.yaml
         

The following is an example policy file that contains the reference to the `built-by-cloud-build-attestor`:
         
         defaultAdmissionRule:
           evaluationMode: REQUIRE_ATTESTATION
           enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
           requireAttestationsBy:
             - projects/PROJECT_ID/attestors/built-by-cloud-build
         name: projects/PROJECT_ID/policy
         

Replace `PROJECT_ID` with the project ID where you run Cloud Build.




## What's next

  * Instead of disallowing images from deploying, you can [use dry-run mode](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run) to log policy violations.
  * View audit log events for disallowed images on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#blocked-deployments) or [Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run#blocked-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
