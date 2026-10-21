---
url: https://docs.cloud.google.com/service-health/docs/script-enable-api/
title: Enable Personalized Service Health for all projects in an organization or folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:06.968630+00:00
---

# Enable Personalized Service Health for all projects in an organization or folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/script-enable-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Enable Personalized Service Health for all projects in an organization or folder Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a script that enables each project in an organization or folder for service health events processing. It grants the [Identity and Access Management (IAM) principal](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works) specified the Service Health Viewer role, which lets you view events and enable the Service Health API.

## Before you begin

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Ensure that you have the following permissions to run the script:

  * Permission to list projects under the parent: `resourcemanager.projects.list`.
  * Permission to add IAM (Service Health Viewer role) for the specified IAM principal: `resourcemanager.projects.setIamPolicy`.
  * Permission to enable Google Cloud services: `serviceusage.services.enable`.



One way to gain these permissions is to ask an administrator to grant you an appropriate role. Search for the permissions in the [Predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) section of the IAM basic and predefined roles reference page. The roles that have the permissions appear.

## Run the script

The script accepts the following parameters:

  * `PARENT_ID`: ID of the parent to projects. The ID can be for an organization or a folder. All projects under the parent will have Personalized Service Health enabled.
  * (optional) `IAM_PRINCIPAL`: An identifier for the principal, or member, which will be granted the Service Health Viewer role. It usually has the following form: `PRINCIPAL_TYPE:ID`. Example:`user:my-user@example.com`.

For the full list of supported values, see the [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) section of the Manage access to projects, folders, and organizations page.




To run the script:

  1. Decide on the API VERSION: `v1` or `v1beta`.
  2. Paste the following script to a file:
         
         #!/bin/bash
         
         PARENT_ID="$1" PRINCIPAL="$2"
         
         FAILED_PROJECTS=()
         
         for project in $(gcloud projects list --filter="parent.id: ${PARENT_ID}" --format="value(projectId)")
         do
             echo "Enabling PSH API for project $project"
             gcloud services enable servicehealth.googleapis.com --project="${project}"
             echo "Finished enabling PSH API for project $project"
         
             if [[ -n "$PRINCIPAL" ]]; then
                 echo "Adding $PRINCIPAL as service health viewer to project $project"
                 gcloud projects add-iam-policy-binding "${project}" --member "${PRINCIPAL}" --role roles/servicehealth.viewer
                 echo "Finished adding $PRINCIPAL as service health viewer to project $project"
                 sleep 5
             else echo "PRINCIPAL not provided, will not grant service health viewer role. Please provide a PRINCIPAL value in order to view events."
             fi
         
             echo "Attempt to list events from Personalized Service Health for project $project"
             RESPONSE="$(curl -w "%{http_code}" -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://servicehealth.googleapis.com/API VERSION/projects/"${project}"/locations/global/events)" HTTP_CODE=$(tail -n1 <<< "$RESPONSE")
         
             if [[ "$HTTP_CODE" -ne 200 ]] ; then
                 echo "Failed to list events for project $project"
                 echo "Response: $RESPONSE"
                 FAILED_PROJECTS+=($project)
             else
                 echo "Successfully listed events for project $project"
             fi
         done
         
         if [[ "${#FAILED_PROJECTS[@]}" -ne 0 ]]; then
             echo "Listing projects that failed to activate"
             for project in "${FAILED_PROJECTS[@]}"
             do
                 echo "$project"
             done
         fi
         

  3. Run the script. The following examples assume the script is in a file named `activateProjects.sh`:

     * To activate all projects in organization ID `345678901` and grant user`user:test-user@gmail.com` the role of`roles/servicehealth.viewer`, run:
           
           bash activateProjects.sh 345678901 "user:test-user@gmail.com"
           

     * To activate all projects in organization ID `345678901` and grant service account `serviceAccount:test-proj1@example.domain.com` the role of`roles/servicehealth.viewer`, run:
           
           bash activateProjects.sh 345678901 "serviceAccount:test-proj1@example.domain.com"
           




Personalized Service Health will take up to 24 hours to start processing service health events.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
