---
url: https://docs.cloud.google.com/lakehouse/docs/vpc-sc-config-sap-bdc/
title: VPC Service Controls configuration for SAP BDC \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:36.087540+00:00
---

# VPC Service Controls configuration for SAP BDC  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/vpc-sc-config-sap-bdc/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  VPC Service Controls configuration for SAP BDC Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure VPC Service Controls (VPC SC) egress and ingress rules for SAP Business Data Cloud (BDC). 

Depending on your integration, you must configure rules for the following data flows:

  * **Querying SAP data (SAP to BDC):** To query SAP tables from Google Cloud, you must configure an **egress rule**.
  * **Publishing data to SAP (BDC to SAP):** To publish data to SAP, you must configure an **ingress rule**.



## Egress rules for querying SAP

You might see this error when querying SAP tables:

`VPC Service Controls: Request is prohibited by organization's policy. File: gs://example-bucket/path/to/file`

This occurs because BigQuery must read Cloud Storage external buckets that host the table data. If your perimeter restricts `storage.googleapis.com`, you might receive a `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` error because the external bucket is outside your perimeter. To resolve this, configure an egress rule. For more information, see [Resources not in the same perimeter](https://cloud.google.com/vpc-service-controls/docs/troubleshooting#resources-not-in-same-perimeter).

### Configure egress rules

This configuration applies if your SAP landscape is deployed on Google Cloud.

If your project uses VPC Service Controls and the perimeter restricts `storage.googleapis.com`, you must configure an egress rule to allow BigQuery to read SAP Cloud Storage buckets for table queries.

  1. Check the current perimeter.
         
         PERIMETER_NAME=accessPolicies/ACCESS_POLICY/servicePerimeters/PERIMETER
         gcloud access-context-manager perimeters describe ${PERIMETER_NAME}
         

Replace the following:

     * `ACCESS_POLICY`: your access policy.
     * `PERIMETER`: your service perimeter.

Your perimeter restricts Cloud Storage bucket reads if the response includes:
    
    resources:
    - projects/PROJECT_ID
    ...
    restrictedServices:
    - storage.googleapis.com
    

  2. Export the current egress rules and append a rule to allow Cloud Storage bucket reads.
         
         PERIMETER_NAME=accessPolicies/ACCESS_POLICY/servicePerimeters/PERIMETER
         gcloud access-context-manager perimeters describe ${PERIMETER_NAME} \
             --format="yaml(status.egressPolicies)" | sed '1,2d; s/^  //' > egress-policies.yaml
         

Replace the following:

     * `ACCESS_POLICY`: your access policy.
     * `PERIMETER`: your service perimeter.

Append this rule to `egress-policies.yaml` to allow you to read Cloud Storage buckets outside the perimeter:
    
    - egressFrom:
        identityType: ANY_IDENTITY
      egressTo:
        operations:
        - methodSelectors:
          - method: google.storage.buckets.get
          - method: google.storage.objects.get
          - method: google.storage.objects.list
          serviceName: storage.googleapis.com
        resources:
        - '*'
    

  3. Update the service perimeter:
         
         gcloud access-context-manager perimeters update ${PERIMETER_NAME} \
             --set-egress-policies=egress-policies.yaml
         

Verify the updated egress policies:
         
         gcloud access-context-manager perimeters describe ${PERIMETER_NAME}
         




## Ingress rules for publishing data to SAP

SAP needs to query the Lakehouse API to read Apache Iceberg tables managed by Lakehouse. Your VPC SC rules might block this if the project's perimeter restricts the `biglake.googleapis.com` service.

If your project has VPC Service Controls enforced, and the perimeter applied on the project restricts the `biglake.googleapis.com` service, you must configure an ingress rule to allow SAP federated principals to access Lakehouse APIs.

### Configure ingress rules

  1. Check the current perimeter.
         
         PERIMETER_NAME=accessPolicies/ACCESS_POLICY/servicePerimeters/PERIMETER
         gcloud access-context-manager perimeters describe ${PERIMETER_NAME}
         

Replace the following:

     * `ACCESS_POLICY`: your access policy.
     * `PERIMETER`: your service perimeter.

Your service perimeter can restrict the Lakehouse API if the response contains:
    
    resources:
    - projects/PROJECT_ID
    ...
    restrictedServices:
    - biglake.googleapis.com
    

  2. Export the current ingress rules and append a rule to allow SAP federated principals to call Lakehouse APIs.
         
         PERIMETER_NAME=accessPolicies/ACCESS_POLICY/servicePerimeters/PERIMETER
         gcloud access-context-manager perimeters describe ${PERIMETER_NAME} \
             --format="yaml(status.ingressPolicies)" | sed '1,2d; s/^  //' > ingress-policies.yaml
         

Replace the following:

     * `ACCESS_POLICY`: your access policy.
     * `PERIMETER`: your service perimeter.
**Note:** The preceding command might create an empty file if the perimeter doesn't have any existing ingress rules.

Append a rule for the SAP federated principal:
    
    - ingressFrom:
        identities:
        - principal://iam.googleapis.com/projects/PROJECT_ID/locations/global/workloadIdentityPools/POOL_NAME/subject/SUBJECT
        sources:
        - accessLevel: '*'
      ingressTo:
        operations:
        - methodSelectors:
          - method: '*'
          serviceName: biglake.googleapis.com
        resources:
        - '*'
    

Replace the following:

     * `PROJECT_ID`: the project ID containing the workload identity pool.
     * `POOL_NAME`: the name of the workload identity pool.
     * `SUBJECT`: the UUID issued by the SAP-side issuer for the workload.
  3. Update the service perimeter:
         
         gcloud access-context-manager perimeters update ${PERIMETER_NAME} \
             --set-ingress-policies=ingress-policies.yaml
         

Verify the updated policies:
         
         gcloud access-context-manager perimeters describe ${PERIMETER_NAME}
         




## What's next

  * [Set up cross-cloud connection for SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).
  * [Query SAP data](https://docs.cloud.google.com/lakehouse/docs/query-sap-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
