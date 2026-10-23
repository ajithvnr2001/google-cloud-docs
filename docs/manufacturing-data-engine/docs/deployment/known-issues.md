---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/known-issues/
title: Known issues \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:10.596744+00:00
---

# Known issues  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Known issues

This page provides known issues that you might run into while using Manufacturing Data Engine (MDE), and potential workarounds until they are tackled in a future MDE release. Read them carefully as they might affect your MDE deployment.

## Enable GKE cluster filestore driver

**Status** : Active.

**MDE versions affected** : 1.40 and earlier with existing GKE clusters.

**Root cause** : As of 1.4.0, the MDE GKE cluster uses a filestore instance to store JVM heap dumps which enables the engineering team to troubleshoot customer issues more effectively. Due to Terraform restrictions, this add-on might not be enabled for the autopilot clusters of earlier versions.

**Workaround** : If you experience that the pods are not starting up and they are in the `ContainerCreating` state, then you need to enable the CSI driver for the Filestore using the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
       --update-addons=GcpFilestoreCsiDriver=ENABLED --region REGION_NAME
    

## MDE deployment requires Object-level ACLs enabled in Cloud Storage

**Status** : Active. To be fixed in MDE 1.5.3

**Issue 529102892** : Terraform deployment fails with the error
    
    
       The GCP Organizational policy "constraints/storage.uniformBucketLevelAccess" prevented
       to proceed with Manufacturing Data Engine platform deployment with this error "│
       Error: googleapi: Error 412: Request violates constraint
       'constraints/storage.uniformBucketLevelAccess', conditionNotMet"
    

**MDE versions affected:** 1.3.x to 1.5.2

**Root cause** : Newly created Google Cloud orgs enforce `storage.uniformBucketLevelAccess` organization policy constraint, which clashes with the Cloud Storage fine grained access bucket requirements for MDE.

**Workaround** : Ask the org administrator to disable the `storage.uniformBucketLevelAccess` constraint for the MDE project in the [https://console.cloud.google.com/iam-admin/orgpolicies/list](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/organiation%20policies).

## Timeout during import of configuration packages

**Status** : Active. To be fixed in MDE 1.5.3

**Issue 503724179** : When importing >20 types in one MDE configuration package, the process fails. 

**MDE versions affected:** 1.5.x

**Root cause** : Importing a big number of types causes MDE to hit a 3 min timeout.

**Workaround** : Split the configuration package in smaller packages and import them sequentially.

## Grafana module not foundwhen running terraform init

**Status** : Fixed in MDE 1.5.1.

**Issue 435653743** : The terraform grafana module is disabled by default in MDE, however, during MDE deployment or upgrade, `terraform init` will attempt to load it, generating the "Grafana module not found" error.

**MDE versions affected:** 1.3.x to 1.5.0.

**Root cause** : The repository that contained the _helm-grafana_ terraform module has been removed by the owner. We are looking into alternatives for those customers interested in the integration.

**Workaround:** Rename the suffix of the module file with the following command, so `terraform init` doesn't try to load it:
    
    
      mv modules/deployment/helm-grafana.tf modules/deployment/helm-grafana.disabled_tf
    

Alternatively, if you are not planning on using Grafana with MDE, you can remove `helm-grafana.tf` with the following command:
    
    
      rm modules/deployment/helm-grafana.tf
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
