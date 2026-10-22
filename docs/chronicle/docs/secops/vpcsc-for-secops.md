---
url: https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops/
title: Configure VPC Service Controls \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:59.672023+00:00
---

# Configure VPC Service Controls  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VPC Service Controls

Supported in:

Google SecOps 

This guide describes how to configure VPC Service Controls for Google Security Operations.

VPC Service Controls lets you set up a service perimeter to guard against data exfiltration. Configure Google Security Operations with VPC Service Controls so that Google SecOps can access resources and services outside its service perimeter.

To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). You can also see the [Google Security Operations entry](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_secops) in the VPC Service Controls supported products table.

## Before you begin

  * Make sure that you have the [required roles to configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) at the organization level.
  * To use Google SecOps with VPC Service Controls, you can only use VPC Service Controls-compliant features. The following lists VPC Service Controls-compliant features:

    * Google SecOps with VPC Service Controls supports only Google Cloud Identity authentication, third-party identity providers, and Workforce Identity Federation.
    * Google SecOps [feature RBAC](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access) must be enabled to use VPC Service Controls with Google SecOps.
    * Google SecOps with VPC Service Controls supports only the following public-facing APIs:

      * `chronicle.googleapis.com`
      * `chronicleservicemanager.googleapis.com`

To onboard to VPC Service Controls, you must migrate all corresponding endpoints onto the `chronicle.googleapis.com` API.

    * Google SecOps with VPC Service Controls supports export of Google SecOps Unified Data Model (UDM) data only to a [self-managed BigQuery project](https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project) or using [Advanced BigQuery Export](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export).

    * VPC Service Controls supports only Google SecOps [Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards).

    * You can create Cloud Storage feeds only with the [`GOOGLE_CLOUD_STORAGE_V2`](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#gc-storage-v2) source type using v2 connectors.

    * When you create new Pub/Sub subscriptions when Google SecOps is restricted within a VPC Service Controls perimeter, Google SecOps requires that you write logs to Cloud Storage and use [GOOGLE_CLOUD_STORAGE_V2](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#gc-storage-v2) or [GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#gcs-edt) instead of your [CLOUD_PUB_SUB](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#setup-pubsub-push) feeds.

  * For a Google SecOps instance using [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek), Google strongly recommends that you either keep your [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service) project within the same perimeter as your Google SecOps-linked Google Cloud project or keep your keys inside the Google SecOps-linked Google Cloud project itself.

  * For the SOAR side of the platform, if your Google SecOps instance uses [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek), confirm that your [SOAR instance is migrated](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#check-migration) to Google.com.

  * If you're using legacy SOAR data exports to BigQuery, such as for Looker or Managed BigQuery Export, Google recommends that you use the [Bring Your Own BigQuery (BYOBQ)](https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project) feature instead. Because Looker dashboards are a legacy feature, Google also recommends that you use [Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards) instead. If you continue to use legacy SOAR data exports to BigQuery, you must configure a dedicated egress rule in your VPC Service Controls service perimeter. To get the required rule and project information, such as `SOAR_TENANT_PROJECT_ID` and `BQ_TLA_PROJECT_NUMBER`, contact your Customer Engineer (CE) or [open a support case](https://docs.cloud.google.com/chronicle/docs/getting-support).




### Limitations

  * The Google SecOps Chronicle API endpoint `ImportPushLogs` doesn't support VPC Service Controls. However, this limitation doesn't pose a data-exfiltration risk, because the `ImportPushLogs` endpoint is only used for pushing data to a Google SecOps instance, not for accessing data.

  * Google SecOps with VPC Service Controls doesn't support [Looker](https://docs.cloud.google.com/looker/docs) dashboards.

  * Google Cloud Pub/Sub doesn't support creating a new Pub/Sub subscription that uses the Chronicle API endpoints to ingest logs ([Pub/Sub entry](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_pubsub) in the VPC Service Controls supported products table). However, any existing Pub/Sub subscriptions (created before moving Google Cloud project inside the VPC Service Controls perimeter) will continue to ingest logs as expected.

  * Google SecOps with VPC Service Controls doesn't support legacy cloud bucket and third-party API feed connectors.




## Configure the ingress and egress rules

Configure [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) based on the service perimeter configuration. For more information, see [Service perimeter overview](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

**Warning:** After you set up the ingress and egress rules, run Google SecOps with VPC Service Controls in [_dry-run mode_](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) for the first couple of weeks. Audit your Cloud Audit Logs for any violations before moving the setup to enforced mode. Possible causes of violations might be [Content Hub](https://docs.cloud.google.com/chronicle/docs/secops/content_hub) response integrations in your system without the necessary ingress or egress rules.

If you encounter issues with VPC Service Controls, use the VPC Service Controls violation analyzer to debug and analyze the issue. For more information, see [Diagnose an access denial in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).

### Configure the ingress rule for SOAR

This section describes how to configure VPC Service Controls for the SOAR side of the platform.

Configure the following ingress rule for the Google Cloud user account that you specified when you set up Google SecOps:
    
    
      - ingressFrom:
          identityType: ANY_SERVICE_ACCOUNT
          sources:
          - accessLevel: "*"
        ingressTo:
          operations:
          - serviceName: secretmanager.googleapis.com
            methodSelectors:
            - method: "*"
          resources:
          - projects/PROJECT_NUMBER
    

Replace `PROJECT_NUMBER` with your Google SecOps-linked Google Cloud project number.

### Configure the rules for SIEM

This section describes how to configure VPC Service Controls for the SIEM side of the platform.

#### Ingress rule for Advanced BigQuery Export

If you're using the [Advanced BigQuery Export](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export) feature, configure the following rule for the Google Cloud user account that you specified when you set up Google SecOps:
    
    
        - ingressFrom:
          identities:
          - serviceAccount:malachite-bq-export-entity-graph-batch-adv-bq@system.gserviceaccount.com
          - serviceAccount:malachite-customer-monitoring-exporter@system.gserviceaccount.com
          sources:
          - accessLevel: "*"
        ingressTo:
          operations:
          - serviceName: bigquery.googleapis.com
            methodSelectors:
            - method: "*"
          resources:
          - projects/PROJECT_NUMBER
    

Replace `PROJECT_NUMBER` with your Google SecOps-linked Google Cloud project number.

#### Ingress rule for data tables

If you're using [data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables), configure the following rule for the Google Cloud user account that you specified when you set up Google SecOps:
    
    
      - ingressFrom:
          identities:
          - user:malachite-data-plane-api@prod.google.com
          sources:
          - accessLevel: "*"
        ingressTo:
          operations:
          - serviceName: storage.googleapis.com
            methodSelectors:
            - method: "*"
          resources:
          - projects/PROJECT_NUMBER
    

Replace `PROJECT_NUMBER` with your Google SecOps-linked Google Cloud project number.

### Configure the rules for Google SecOps with Security Command Center

This section describes how to configure VPC Service Controls for Google SecOps with Security Command Center.

The service accounts in the following rules are created only during Google SecOps provisioning, therefore, you should configure the Security Command Center rules after the provisioning, but before starting to use Security Command Center.

**Note:** In the Google SecOps platform, the Security Command Center integration is called _Google Security Command Center_. For more information, see [Collect Security Command Center findings](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-security-command-center-findings) and [Security Command Center issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshoot-services-within-perimeter#scc-issues).

Complete the following tasks for the Google Cloud user account that you specified when you set up Google SecOps:

  1. Configure the following ingress rule:
         
         - ingressFrom:
             identities:
             - serviceAccount: service-org-GOOGLE_ORGANIZATION_NUMBER@gcp-sa-chronicle-soar.iam.gserviceaccount.com
             - serviceAccount: service-org-GOOGLE_ORGANIZATION_NUMBER@security-center-api.iam.gserviceaccount.com
             - serviceAccount: service-org-GOOGLE_ORGANIZATION_NUMBER@gcp-sa-csc-hpsa.iam.gserviceaccount.com
             - serviceAccount: service-org-GOOGLE_ORGANIZATION_NUMBER@gcp-sa-asm-hpsa.iam.gserviceaccount.com
             sources:
             - accessLevel: "*"
           ingressTo:
             operations:
             - serviceName: chronicle.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: securitycenter.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: cloudasset.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: monitoring.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: iam.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: orgpolicy.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: serviceusage.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: dns.googleapis.com
               methodSelectors:
               - method: "*"
             resources:
             - projects/PROJECT_NUMBER
         

Replace the following:

     * `GOOGLE_ORGANIZATION_NUMBER`: your Google Cloud organization number
     * `PROJECT_NUMBER`: your Google SecOps-linked Google Cloud project number
  2. Configure the following egress rule:
         
         - egressTo:
             operations:
             - serviceName: pubsub.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: securitycenter.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: cloudasset.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: iam.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: "*"
             resources:
             - "*"
           egressFrom:
             identities:
             - serviceAccount: service-org-GOOGLE_ORGANIZATION_NUMBER@gcp-sa-chronicle-soar.iam.gserviceaccount.com
             - serviceAccount: service-org-GOOGLE_ORGANIZATION_NUMBER@security-center-api.iam.gserviceaccount.com
             sources:
             - resource: projects/PROJECT_NUMBER
         

Replace the following:

     * `GOOGLE_ORGANIZATION_NUMBER`: your Google Cloud organization number
     * `PROJECT_NUMBER`: your Google SecOps-linked Google Cloud project number



### Configure the ingress rule for customer-managed encryption keys (CMEKs)

This section describes how to configure VPC Service Controls for Google SecOps with customer-managed encryption keys ([CMEKs](https://docs.cloud.google.com/kms/docs/cmek)). CMEKs are encryption keys that you own, manage, and store in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service).

Configure the following ingress rule:
    
    
      - ingressFrom:
        identities:
        - serviceAccount: service-SECRET_MANAGER_PROJECT_NUMBER@gcp-sa-secretmanager.iam.gserviceaccount.com
        - serviceAccount: service-GOOGLE_MANAGED_BIGQUERY_PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com
        - serviceAccount: bq-GOOGLE_MANAGED_BIGQUERY_PROJECT_NUMBER@bigquery-encryption.iam.gserviceaccount.com
          sources:
          - accessLevel: "*"
        ingressTo:
          operations:
          - serviceName: secretmanager.googleapis.com
            methodSelectors:
            - method: "*"
          - serviceName: cloudkms.googleapis.com
            methodSelectors:
            - method: "*"
          resources:
          - projects/CMEK_PROJECT_NUMBER
    
    

Replace the following:

  * `SECRET_MANAGER_PROJECT_NUMBER`: the project that Google uses to store secrets for some ingestion features, which you can get from your Google SecOps representative
  * `GOOGLE_MANAGED_BIGQUERY_PROJECT_NUMBER`: the project that Google uses to store BigQuery resources for some export features, which you can get from your Google SecOps representative
  * `CMEK_PROJECT_NUMBER`: the project number storing the CMEKs



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
