---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/data-collection-with-data-residency/
title: Configure hybrid to use the new data pipeline \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:18:40.977914+00:00
---

# Configure hybrid to use the new data pipeline  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/data-collection-with-data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure hybrid to use the new data pipeline Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/data-collection-with-data-residency.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/data-collection-with-data-residency.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/data-collection-with-data-residency.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/data-collection-with-data-residency.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/data-collection-with-data-residency.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/data-collection-with-data-residency.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/data-collection-with-data-residency.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/data-collection-with-data-residency.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/data-collection-with-data-residency.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/data-collection-with-data-residency.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/data-collection-with-data-residency.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/data-collection-with-data-residency.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/data-collection-with-data-residency.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/data-collection-with-data-residency.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/data-collection-with-data-residency.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/data-collection-with-data-residency.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/data-collection-with-data-residency.html)



## Overview

Starting with version 1.13.1, Apigee hybrid orgs with data residency enabled can use a new data pipeline that allows the runtime components to write data directly to the control plane. Previously, this was done via the UDCA component which generated signed urls to write to Google Cloud Services. The new pipeline eliminates the need for UDCA and other related components responsible for processing data uploaded to Google Cloud Services. 

**Note:** The new data pipeline is required for hybrid orgs on v1.13.1 or higher with data residency enabled. **Tip:** Starting with version 1.14.0, the new data pipeline is supported on all organizations with or without data residency enabled. See [Apigee hybrid version 1.14.0](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1140). 

## Configuration

You can configure hybrid to use the new data pipeline for individual components using the following instructions.

### Setting Authorization Flow

Set permissions for the runtime service account to interact with new pipeline to push data to the control plane. This step is required to allow Debug sessions and Analytics to operate with the new pipeline:
    
    
    curl -X  PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      "https://apigee.googleapis.com/v1/organizations/ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
      -d '{ "analytics_publisher_identities": ["serviceAccount:apigee-runtime@ORG_NAME.iam.gserviceaccount.com"]}'

The response should look like the following:
    
    
    {
      "name": "organizations/newpipeline-hybrid-org/operations/8316aa78-c137-4733-92ec-cc0d2d92fd29",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/newpipeline-hybrid-org/controlPlaneAccess",
        "state": "IN_PROGRESS"
      }
    }
    

Verify state of the operation using the name parameter from the update response: 
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
      -H "Content-Type:application/json"  \
      "https://apigee.googleapis.com/v1/organizations/ORG_NAME/operations/8316aa78-c137-4733-92ec-cc0d2d92fd29"

The response should look like the following:
    
    
    {
      "name": "organizations/newpipeline-hybrid-org/operations/8316aa78-c137-4733-92ec-cc0d2d92fd29",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/newpipeline-hybrid-org/controlPlaneAccess",
        "state": "FINISHED"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.ControlPlaneAccess",
        "name": "organizations/newpipeline-hybrid-org/controlPlaneAccess"
      }
    }
    

Verify the organization's ControlPlaneAccess configuration:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/controlPlaneAccess" \
    -H "Authorization: Bearer $(gcloud auth print-access-token)"

The response should look like the following:
    
    
    {
      "synchronizerIdentities": [
        "serviceAccount:apigee-synchronizer@newpipeline-hybrid-org.iam.gserviceaccount.com"
      ],
      "analyticsPublisherIdentities": [
        "serviceAccount:apigee-runtime@newpipeline-hybrid-org.iam.gserviceaccount.com"
      ]
    }
    

## Switching between new and old pipelines for debug and Analytics data residency

Once the right authorization has been provided to the service accounts, users can switch their Apigee instance to use the new pipeline.

To switch to the new pipeline, set `newDataPipeline.debugSession: true` and `newDataPipeline.analytics: true` in your `overrides.yaml` file. 

To stop using the new pipeline, set `newDataPipeline.debugSession: false` and `newDataPipeline.analytics: false` in your `overrides.yaml` file. 

For example:
    
    
    ... rest of the overrides.yaml ...
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION  # Specifies the analytics region for the hybrid org. This attribute is
                                   # the regional endpoint used to push analytics and debug data to the
                                   # control plane. For example: us-central1
    
    newDataPipeline:
      **debugSession: true**  # this flag enables debug session to use the new data pipeline
      **analytics: true**     # this flag enables analytics to use the new data pipeline
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster. For example, us-west1
    org: ORG_NAME
    
    ... rest of the overrides.yaml ...
    

Apply these changes with the `helm upgrade` command. Upgrade one environment at a time. Specify the environment with `--set env=`ENV_NAME.
    
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      -f OVERRIDES_FILE
    

  * ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart.
  * ENV_NAME is the name of the environment you are upgrading.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
