---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/universal-data-collection-agent-pod-error/
title: UDCA pod error \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:32.617184+00:00
---

# UDCA pod error  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/universal-data-collection-agent-pod-error/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  UDCA pod error Stay organized with collections  Save and categorize content based on your preferences. 

## Symptom

After upgrading Apigee hybrid, your Universal Data Collection Agent (UDCA) and Connect Agent pods throw a permission issue error.

## Error messages

Your UDCA pod throws this error in the logs: 
    
    
    Permission 'apigee.runtimeconfigs.get' denied on resource 
    'organizations/org-example/runtimeConfig' (or it may not 
    exist)\\\",\\n  \\\"status\\\": \\\"PERMISSION_DENIED\\
    

In addition, your Management API for Runtime (MART) pod throws this error regarding the Connect Agent:
    
    
    Permission 'apigeeconnect.endpoints.connect' denied on resource 
    '//apigeeconnect.googleapis.com/projects/org-example/endpoints/APIGEE_MART' 
    (or it may not exist).
    

## Common diagnosis steps

Collect the [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather) script from your cluster and the `overrides.yaml` file for the cluster.

## Possible causes

Cause | Description  
---|---  
Incorrect credentials | You might have entered the wrong credentials in the `overrides.yaml` file.  
SA files located in wrong directory | Your Service Account (SA) files might be residing outside the `$APIGEE_HELM_CHARTS_HOME` directory.  
  
### Cause 1: Incorrect credentials

The `serviceAccountPath` or `serviceAccountRef` used in your `overrides.yaml` file for UDCA, MART, and Connect Agent pods are incorrect. This may be because the `overrides.yaml` file was generated through automation or custom scripts, such as by using Terraform. 

#### Diagnosis

  1. Verify the IAM roles and permissions assigned to the service accounts you use.
         
         gcloud iam service-accounts get-iam-policy SERVICE_ACCOUNT_EMAIL
         gcloud projects get-iam-policy PROJECT_ID
         

Where:

     * SERVICE_ACCOUNT_EMAIL is the email address of the service account.
     * PROJECT_ID is the Google Cloud project associated with the service account.
  2. Review your `overrides.yaml` file to make sure the referenced service account matches the one used in the project IAM policy and roles. 



#### Example

An example of a working IAM policy for the service account for a non-prod setup:
    
    
    gcloud iam service-accounts get-iam-policy apigee-non-prod@org-example.iam.gserviceaccount.com
    

Sample output:
    
    
    bindings:
    - members:
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-cassandra-backup-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-cassandra-default]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-cassandra-guardrails-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-connect-agent-org-example-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-mart-org-example-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-metrics-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-runtime-org-example-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-synchronizer-org-example-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-udca-org-example-sa]
      - serviceAccount:org-example.svc.id.goog[apigee/apigee-watcher-org-example-sa]
      role: roles/iam.workloadIdentityUser
    etag: BwYw33-1N8s=
    version: 1
    

An example of validating roles:
    
    
    gcloud projects get-iam-policy org-example
    

Sample output:
    
    
    bindings:
    - members:
      - serviceAccount:apigee-non-prod@org-example.iam.gserviceaccount.com
      role: roles/apigee.analyticsAgent
    - members:
      - serviceAccount:apigee-non-prod@org-example.iam.gserviceaccount.com
      role: roles/apigee.runtimeAgent
    - members:
      - serviceAccount:apigee-non-prod@org-example.iam.gserviceaccount.com
      role: roles/apigee.synchronizerManager
    - members:
      - serviceAccount:apigee-non-prod@org-example.iam.gserviceaccount.com
      role: roles/apigeeconnect.Agent
    - members:
      - serviceAccount:apigee-non-prod@org-example.iam.gserviceaccount.com
      role: roles/storage.objectAdmin
    

For production, run the same commands against the production service account for `apigee-udca` and check for the IAM roles that matches the [installation](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-service-accounts) section.

#### Resolution

If the service account file used in your `overrides.yaml` does not match the correct service account in the project IAM binding and roles, you should delete and recreate the service account, and correct the service account file used in the `overrides.yaml`. 

### Cause 2: SA files located in wrong directory

This issue occurs when setting up the helm charts and creating the [service account](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-service-accounts). 

#### Diagnosis

Check the location of your service account credential file to ensure that it resides in the correct helm chart directory. The service account JSON file should reside under the following directories:

  * `$APIGEE_HELM_CHARTS_HOME/apigee-datastore`
  * `$APIGEE_HELM_CHARTS_HOME/apigee-telemetry`
  * `$APIGEE_HELM_CHARTS_HOME/apigee-org`
  * `$APIGEE_HELM_CHARTS_HOME/apigee-env`



#### Example

For example, check the helm chart directories by listing the `apigee-datastore` directory, and do the same for `apigee-org`, `apigee-env`, and `apigee-telemetry` directories.

Sample Command:

Make sure you are in the correct directory:
    
    
    pwd

Sample output:
    
    
    /usr/local/home/example/Hybrid/helm-charts
    
    
    ├── apigee-datastore
    │   ├── org-example-apigee-non-prod.json
    │   └── templates
    ├── apigee-env
    │   ├── org-example-apigee-non-prod.json
    │   └── templates
    ├── apigee-ingress-manager
    │   └── templates
    ├── apigee-operator
    │   ├── etc
    │   │   ├── crds
    │   │   │   ├── crd
    │   │   │   │   ├── bases
    │   │   │   │   └── patches
    │   │   │   └── default
    │   │   ├── examples
    │   │   │   └── helmfiles
    │   │   └── tools
    │   │       └── service-accounts
    │   │           ├── org-example-apigee-cassandra.json
    │   │           ├── org-example-apigee-logger.json
    │   │           ├── org-example-apigee-mart.json
    │   │           ├── org-example-apigee-metrics.json
    │   │           ├── org-example-apigee-runtime.json
    │   │           ├── org-example-apigee-synchronizer.json
    │   │           ├── org-example-apigee-udca.json
    │   │           └── org-example-apigee-watcher.json
    │   └── templates
    ├── apigee-org
    │   ├── org-example-apigee-non-prod.json
    │   └── templates
    ├── apigee-redis
    │   └── templates
    ├── apigee-telemetry
    │   ├── org-example-apigee-non-prod.json
    │   └── templates
    ├── apigee-virtualhost
    │   ├── certs
    │   └── templates
    └── cluster-check
    29 directories, 12 files
    

#### Resolution

Copy the Service Account file into the four directories (`apigee-datastore`, `apigee-telemetry`, `apigee-org`, and `apigee-env`) as per the example tree location above, then rerun the helm charts.

## Related documents (optional) 

[Service account setup](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-service-accounts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
