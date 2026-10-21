---
url: https://docs.cloud.google.com/binary-authorization/docs/using-cv/
title: Use legacy continuous validation \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:14.187123+00:00
---

# Use legacy continuous validation  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/using-cv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Use legacy continuous validation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Caution:** Legacy continuous validation (legacy CV) with project-singleton policies is [deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy). As of April 15, 2024, you can no longer enable legacy CV with project-singleton policies on new projects, and support for existing projects will be removed on May 1, 2025. Instead, use [continuous validation (CV) with check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv). Existing legacy CV users can migrate project-singleton policies to platform policies. To learn how, see [Migration](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy#migration). 

This page is intended for users of legacy continuous validation (legacy CV) ([deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy)).

Legacy continuous validation is a feature of Binary Authorization that periodically checks container images associated with running Pods for continued compliance with your Binary Authorization project-singleton policy. Legacy CV logs findings to [Cloud Logging](https://docs.cloud.google.com/logging/docs).

Legacy CV does not terminate running Pods.

## Limitations

Legacy CV has the following limitations:

  * Legacy CV only supports Pods deployed on Google Kubernetes Engine (GKE).
  * Legacy CV does not support Binary Authorization policies that specify [specific rules](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-specific-rules-asm) for Cloud Service Mesh service identities, Kubernetes service accounts, or Kubernetes namespaces.



## Before you begin

  1. Ensure that you have set up [Binary Authorization for Google Kubernetes Engine](https://docs.cloud.google.com/binary-authorization/docs/setting-up) in a project. legacy CV logs policy conformance events from Pods in all clusters in the project.

  2. Ensure that the gcloud CLI is updated to the latest version




## Required permissions

Identity and Access Management (IAM) roles include permissions and can be assigned to users, groups, and service accounts. The following roles include the listed permissions for CV:

Role name | Legacy CV permissions | Description  
---|---|---  
`roles/binaryauthorization.policyEditor` | `binaryauthorization.continuousValidationConfig.update` | Enable and disable CV.  
**Note:** We recommend that you grant `binaryauthorization.continuousValidationConfig.update` to users who also have permission to configure a policy.

To set the required IAM permissions, run the following commands:
    
    
    PROJECT_NUMBER=$(gcloud projects list \
      --filter="projectId:ATTESTATION_PROJECT_ID" \
      --format="value(PROJECT_NUMBER)")
    SERVICE_ACCOUNT="service-$PROJECT_NUMBER@gcp-sa-binaryauthorization.iam.gserviceaccount.com"
    
    
    
    gcloud projects add-iam-policy-binding ATTESTATION_PROJECT_ID \
        --member="serviceAccount:$SERVICE_ACCOUNT" \
        --role='roles/containeranalysis.occurrences.viewer'
    

## Enable legacy CV

###  Console 

To enable legacy CV by using the Google Cloud console, do the following:

  1. In the **Google Cloud console** , go to the **Binary Authorization** **Policy** page.

[Go to Binary Authorization Policy](https://console.cloud.google.com/security/binary-authorization/)

  2. Click the **Policy** tab.

  3. Click **Edit Policy**.

  4. Expand the **Additional settings for GKE and Anthos deployments** section.

  5. Select the **Enable Continuous Validation** checkbox.

  6. Click **Save Policy**.




###  REST API 

To enable legacy CV using the REST API, do the following:

  1. Store your project ID:
         
         DEPLOYER_PROJECT_ID=DEPLOYER_PROJECT_ID
         

Replace `DEPLOYER_PROJECT_ID` with the ID of the project where you run GKE.

  2. Get the OAuth token for Google Cloud.
         
         BEARER_TOKEN=$(gcloud auth print-access-token)
         

The token is only valid for a short time.

  3. Enable legacy CV:
         
         curl "https://binaryauthorization.googleapis.com/v1alpha2/projects/${DEPLOYER_PROJECT_ID}/continuousValidationConfig" -X PUT -H "authorization: Bearer $BEARER_TOKEN" -H "Content-Type: application/json" --data '{"enforcementPolicyConfig": {"enabled": "true"}}'
         




Legacy CV is now configured to log events.

**Note:** Legacy CV checks for policy violations at least every 24 hours, so it can take up to 24 hours for legacy CV events to appear in Logging after legacy CV is enabled or a Pod is deployed. Violations continue to be logged for non-conformant Pods until the Pod terminates. Pods that are running before legacy CV is enabled are not guaranteed to be checked.

The Logging log entry is similar to the following example:
    
    
    {
    "insertId": "6054e143-0000-2562-aa64-883d24f57e70",
    "jsonPayload": {
      "@type": "type.googleapis.com/google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent",
      "podEvent": {
        "images": [
          {
            "description": "Image <var>IMAGE_NAME@IMAGE_DIGEST</var> denied by
            attestor projects/<var>ATTESTOR_PROJECT_ID</var>/attestors/<var>ATTESTOR_NAME</var>:
            No attestations found that were valid and signed by a key trusted by
            the attestor",
            "image": "<var>IMAGE_NAME@IMAGE_DIGEST</var>",
            "result": "DENY"
          }
        ],
        "verdict": "VIOLATES_POLICY",
        "deployTime": "2021-03-19T17:00:08Z",
        "pod": "<var>POD_NAME</var>"
      }
    },
    "resource": {
      "type": "k8s_cluster",
      "labels": {
        "cluster_name": "<var>CLUSTER_NAME</var>",
        "location": "<var>CLUSTER_LOCATION</var>",
        "project_id": "<var>DEPLOYER_PROJECT_ID</var>"
      }
    },
    "timestamp": "2021-03-19T17:15:43.872702342Z",
    "severity": "WARNING",
    "logName": "projects/<var>DEPLOYER_PROJECY_ID</var>/logs/binaryauthorization.googleapis.com%2Fcontinuous_validation",
    "receiveTimestamp": "2021-03-19T17:57:00.432116179Z"
    }
    

To learn how to query for legacy CV events, see View legacy CV events on Cloud Logging.

## Troubleshooting

Legacy CV uses other Google Cloud services, like Cloud Asset Inventory and Pub/Sub. In cases where legacy CV fails, you can [check for Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes#using) errors in Cloud Logging.

Additionally, legacy CV creates a feed resource called `binauthz-cv-cai-feed`. Deleting or modifying the feed could cause legacy CV to fail. Legacy CV automatically restores missing or altered feeds, but it can fail to log findings until it does so.

## Disable CV

###  Console 

To disable legacy CV by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Binary Authorization** page:

[Go to Binary Authorization Policy](https://console.cloud.google.com/security/binary-authorization/)

  2. Click the **Policy** tab.

  3. Click **Edit Policy**.

  4. Clear the **Enable Continuous Validation** checkbox.

  5. Click **Save Policy**.




###  REST API 

To disable legacy CV using the REST API, do the following:

  1. Store your project ID:
         
         DEPLOYER_PROJECT_ID=DEPLOYER_PROJECT_ID
         

Replace `DEPLOYER_PROJECT_ID` with the ID of the project where you run GKE.

  2. Get the OAuth token for Google Cloud.
         
         BEARER_TOKEN=$(gcloud auth print-access-token)
         

The token is only valid for a short time.

  3. Disable legacy CV using the following command:
         
         curl "https://binaryauthorization.googleapis.com/v1alpha2/projects/${DEPLOYER_PROJECT_ID}/continuousValidationConfig" -X PUT -H "authorization: Bearer $BEARER_TOKEN" -H "Content-Type: application/json" --data '{"enforcementPolicyConfig": {"enabled": "false"}}'
         




## View legacy CV events in Cloud Logging

After you enable CV, it regularly logs all Pods that violate the Binary Authorization policy to Cloud Logging.

These log entries contain the following log name:

`logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation"`

**Note:** It can take up to 24 hours for legacy CV events to appear in Cloud Logging.

###  Logs Explorer 

To view legacy CV events in Cloud Logging using Logs Explorer, do the following:

  1. [Go to Logs Explorer](https://console.cloud.google.com/logs/query).

  2. Select the project ID where you enabled Google Cloud Observability.

  3. Enter the following query in the _search-query_ box:
         
         logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation"
         

  4. Select the time range in the _time-range selector_.




###  Legacy Logs Viewer 

To view legacy CV events in Cloud Logging using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), do the following:

  1. [Go to Logs Explorer](https://console.cloud.google.com/logs/query).

  2. Select **Go back to the Legacy Logs Viewer** from the **Options** drop-down menu.

  3. Choose the Google Cloud project for in which you set up Google Cloud Observability.

  4. Enter the following query into the _search-query box_ :
         
         logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation"
         

  5. Select the time range in the _time-range selector_.




###  gcloud 

To view legacy CV events from the past week in Cloud Logging using `gcloud`, execute the following command:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation"'
    

## What's next

  * [Use breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass) to deploy a Pod and [view breakglass events](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#view_breakglass_events).
  * [Enable dry run](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run), deploy a container image, and [view dry-run events](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#dry_run_events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
