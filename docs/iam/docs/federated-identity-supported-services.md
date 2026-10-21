---
url: https://docs.cloud.google.com/iam/docs/federated-identity-supported-services/
title: Identity federation: products and limitations \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:27.010866+00:00
---

# Identity federation: products and limitations  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/federated-identity-supported-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Identity federation: products and limitations Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This page provides details of limitations and the level of support for each Google Cloud product that can use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) or [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), collectively _identity federation_.

### Workforce Identity Federation

Workforce Identity Federation lets your workforce—employees, vendors, partners, and other users—access Google Cloud products by using an identity provider (IdP). Your workforce can access Google Cloud through the Google Cloud Workforce Identity Federation console, also known as the console (federated), the Google Cloud CLI, or a Google Cloud API.

Workforce Identity Federation limitations for the console (federated), the Google Cloud CLI, and Google Cloud API are listed in UI and API entries for each product.

### Workload Identity Federation

Workload Identity Federation lets your workloads programmatically access Google Cloud products by using workload-provided identities such as IAM roles for AWS workloads, Kubernetes service accounts for GKE workloads, or GitHub identities for your deployment pipelines.

Workload Identity Federation limitations for the Google Cloud CLI and Google Cloud APIs, collectively _API limitations_ , are listed in `Google Cloud API limitations` entries for each product, later in this document.

## Google Cloud products and limitations

The table in this section lists products, their level of support for identity federation, limitations, and other information.

### Organization

The limitations table is organized in the following way:

  * **Product:** The product name.
  * **Identity federation launch stage:** Refers to the [launch stage](https://cloud.google.com/products/#product-launch-stages) of the product's support for identity federation. Launch stage doesn't refer to the launch stage of the product itself.
  * **Columns that describe supported products:**
    * **Google Cloud API:** The product's identity federation-related limitations that are associated with API methods and the gcloud CLI commands that access those methods.
    * **Console (federated):** The product's Workforce Identity Federation-related console (federated) UI limitations.
    * **Other:** The product's identity federation-related limitations that aren't Google Cloud API or console (federated) limitations.
  * **Columns that describe unsupported products:**
    * **Alternatives:** For products that don't support identity federation, this column describes alternative products that support identity federation and provide similar features. 



## List of products and limitations

**Launch stage** GAPreviewUnsupported Product  |  [Identity federation launch stage](https://cloud.google.com/products/#product-launch-stages) |  Limitations   
---|---|---  
  
### [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  [`v1alpha` APIs](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1alpha) aren't available for federated identities.   
Other:  |  No known limitations   
  
### [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Agent Assist](https://docs.cloud.google.com/agent-assist/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  In order to use [Virtual Agent Handoff](https://docs.cloud.google.com/agent-assist/docs/basics#virtual_agents) with a Dialogflow ES agent, API callers cannot use Workforce Identity Federation for logging in.   
---|---  
Google Cloud API:  |  [Agent Assist import of conversation transcripts to conversation datasets](https://docs.cloud.google.com/agent-assist/docs/smart-reply#import_conversation_transcripts_to_your_conversation_dataset) does not support Workforce Identity Federation.   
Other:  |  No known limitations   
  
### [Agent Registry](https://docs.cloud.google.com/agent-registry/overview)

|  [Preview](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  During Preview, certain Agent Platform Governance and Agent Gateway console pages have limited support for Workforce Identity Federation sessions.   
---|---  
Google Cloud API:  |  During Preview, certain API and CLI operations, such as importing Agent Gateway resources, return internal errors when called with Workforce Identity Federation credentials. Use a standard Google Account (Cloud Identity or Google Workspace) instead.   
Other:  |  No known limitations   
  
### [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  The following fleet health features aren't supported while using Workforce Identity Federation: 

  * Performance and Backups summary cards
  * Data in the clusters table, such as CPU percentage and Memory Available

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Anti Money Laundering AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [API Gateway](https://docs.cloud.google.com/api-gateway/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Apigee](https://docs.cloud.google.com/apigee/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * Features in [Preview](https://docs.cloud.google.com/products#product-launch-stages) aren't supported for Workforce Identity Federation users. This includes the following features: 
    * **Data Studio integration**
    * **Risk assessment**
    * **Shadow API discovery**
  * [ Local development with Apigee in Cloud Code ](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview) isn't supported for Workforce Identity Federation users. 

  
---|---  
Google Cloud API:  | 

  * [API Management APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest) don't support Workforce Identity Federation users. 
  * [Apigee Connect APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/apigee-connect) don't support Workforce Identity Federation users. 

  
Other:  |  No known limitations   
  
### [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [APIs and Services](https://docs.cloud.google.com/apis/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * [OAuth client management](https://developers.google.com/identity/protocols/oauth2) isn't supported.
  * [OAuth brand management](https://developers.google.com/identity/protocols/oauth2/production-readiness/brand-verification) isn't supported.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [App Engine](https://docs.cloud.google.com/appengine/docs)

|  Unsupported  |  |  Alternatives:  |  Google recommends that you use Cloud Run as an alternative.   
---|---  
  
### [App Hub](https://docs.cloud.google.com/app-hub/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Application Integration](https://docs.cloud.google.com/application-integration/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * Container Registry doesn't support identity federation. There is an information banner in the settings page in **Container Registry transition**.

  
  
### [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Batch](https://docs.cloud.google.com/batch/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [BigQuery](https://docs.cloud.google.com/bigquery/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Saving queries isn't supported.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * The following features don't support Workforce Identity Federation with BigQuery: 
    * [Connected Sheets](https://docs.cloud.google.com/bigquery/docs/connected-sheets)
    * [Google Drive](https://docs.cloud.google.com/bigquery/docs/external-data-drive)
    * [Recommendations](https://docs.cloud.google.com/bigquery/docs/recommendation-overview)
    * [Slot estimator](https://docs.cloud.google.com/bigquery/docs/slot-estimator)
    * [SQL generation with Gemini](https://docs.cloud.google.com/bigquery/docs/write-sql-gemini#generate_a_sql_query)
    * [Python code generation with Gemini](https://docs.cloud.google.com/bigquery/docs/write-sql-gemini#generate_python_code)
  * The following operations don't support Workforce Identity Federation: 
    * Loading data from [Amazon S3](https://docs.cloud.google.com/bigquery/docs/omni-aws-create-connection), [Apache Spark](https://docs.cloud.google.com/bigquery/docs/connect-to-spark), or [Azure Blob Storage](https://docs.cloud.google.com/bigquery/docs/omni-azure-create-connection) through the [Connection API](https://docs.cloud.google.com/bigquery/docs/connections-api-intro)
    * Loading data from [Google Drive](https://docs.cloud.google.com/bigquery/docs/external-data-drive)

  
  
### [Bigtable](https://docs.cloud.google.com/bigtable/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Blockchain Analytics](https://docs.cloud.google.com/blockchain-analytics/docs/overview)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Blockchain Node Engine](https://docs.cloud.google.com/blockchain-node-engine/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Carbon Footprint](https://docs.cloud.google.com/carbon-footprint/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Channel Services](https://docs.cloud.google.com/channel/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  In the **IAM policy** tab, the **Analyze Full Access** button is unavailable for Workforce Identity Federation users.   
---|---  
Google Cloud API:  |  [`analyzeMove`](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove) isn't supported by identity federation.   
Other:  |  No known limitations   
  
### [Cloud Billing](https://docs.cloud.google.com/billing/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * Workforce Identity Federation users must manage billing using the [console (federated)](https://console.cloud.google/) Billing pages or [Google Payments center (federated)](https://payments.cloud.google/). 

  
  
### [Cloud Build](https://docs.cloud.google.com/build/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud CDN](https://docs.cloud.google.com/cdn/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Code](https://docs.cloud.google.com/code/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * Email messages sent from Airflow only include the Airflow UI link that is accessible by Google accounts. To access Airflow UI as a Workforce Identity Federation user, the link must be manually updated (changed to the [URL for Workforce Identity Federation](https://docs.cloud.google.com/composer/docs/composer-2/access-environments-with-workforce-identity-federation#access-airflow-ui)).
  * Third-party identifiers in VPC Service Controls ingress and egress rules aren't supported.

  
  
### [Cloud Console](https://cloud.google.com/cloud-console)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Workforce Identity Federation users can only access the [Google Cloud Workforce Identity Federation console, also known as the console (federated)](https://console.cloud.google/) . They can't access the Google Cloud console. The console (federated) provides limited access to only those Google Cloud products that support Workforce Identity Federation. For more information, see [About the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-learn-more) . The console (federated) has the following limitations: 

  * Language preference is selected at sign-in and can't be updated within the console (federated).
  * Product notifications, updates, and offers can't be enabled on the [communication preferences](https://docs.cloud.google.com/resource-manager/docs/managing-notifications#manage-preferences) page.
  * Personalization based on your Google Cloud console activity isn't supported.
  * The [Transparency and Control Center](https://docs.cloud.google.com/recommender/docs/opting-out) page isn't available.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  Workforce Identity Federation users aren't eligible for the Google Cloud Free Trial.   
  
### [Cloud Customer Care](https://docs.cloud.google.com/support/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * When creating **billing support** cases, users might be required to re-verify their email address. Contact details (for example, email addresses) cannot be changed for Workforce Identity Federation users after interaction with the support team has started.
  * The Premium Support Event Management Service is unavailable to Workforce Identity Federation users.

  
---|---  
Google Cloud API:  |  Cloud Support API doesn't support identity federation.   
Other:  |  No known limitations   
  
### [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Deploy](https://docs.cloud.google.com/deploy/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Cloud Storage buckets must have [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled to view Cloud Deploy artifacts.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  Cloud Storage buckets created through Cloud Deploy have [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.   
  
### [Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Cloud DNS](https://docs.cloud.google.com/dns/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  Cloud DNS has a limitation on the number of name server shards. To learn more, see [Name server limits](https://docs.cloud.google.com/dns/quotas#name-server-limits) . Before allocating the final name server shard, Cloud DNS verifies ownership of the domain, which cannot be performed by federated identities.   
Other:  |  No known limitations   
  
### [Cloud Domains](https://docs.cloud.google.com/domains/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Cloud Fleet Routing](https://cloud.google.com/ai)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Intrusion Detection System](https://docs.cloud.google.com/intrusion-detection-system/docs/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Logging](https://docs.cloud.google.com/logging/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Mobile App](https://cloud.google.com/app)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  [The legacy Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring) doesn't support sending metrics with identity federation. Instead, Workforce Identity Federation users can install the [Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent) .   
  
### [Cloud NAT](https://docs.cloud.google.com/nat/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler/)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Cloud Run](https://docs.cloud.google.com/run/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  [Setting up continuous deployment with Cloud Build](https://docs.cloud.google.com/run/docs/continuous-deployment) from the Cloud Run console is disabled for Workforce Identity Federation. You must set up continuous deployment in Cloud Build.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * The IAM permission `run.routes.invoke`, which can manage access to Cloud Run service endpoints, doesn't support Workforce Identity Federation. Enable [Identity-Aware Proxy for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) to use it.
  * Cloud Run doesn't support Workload Identity Federation direct resource access. To allow access, use [service account impersonation](https://docs.cloud.google.com/iam/docs/workload-identity-federation#impersonation).

  
  
### [Cloud Run functions](https://docs.cloud.google.com/functions/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  [Setting up continuous deployment with Cloud Build](https://docs.cloud.google.com/run/docs/continuous-deployment) from the Cloud Run console is disabled for Workforce Identity Federation. You must set up continuous deployment in Cloud Build.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * The IAM permission `run.routes.invoke`, which manages access to Cloud Run service endpoints, doesn't support Workforce Identity Federation. Enable [Identity-Aware Proxy for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) to use it.
  * Cloud Run doesn't support Workload Identity Federation. To allow access, use [service account impersonation](https://docs.cloud.google.com/iam/docs/workload-identity-federation#impersonation).

  
  
### [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * The App Engine Cron Jobs tab isn't available for Workforce Identity Federation users.
  * The App Engine option in the target type configuration isn't available for Workforce Identity Federation users.

  
---|---  
Google Cloud API:  |  The Cloud Scheduler API doesn't support identity federation for jobs that have their `target` attribute set to [`appEngineHttpTarget`](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#appenginehttptarget) . To send a job to an App Engine target using identity federation, create your job with the `target` type set to [`httpTarget`](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#HttpTarget) and the `uri` field set to the full URI path of your App Engine target.   
Other:  |  No known limitations   
  
### [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  [In-cluster control plane](https://docs.cloud.google.com/service-mesh/docs/supported-features) doesn't support identity federation.   
Other:  |  No known limitations   
  
### [Cloud Shell](https://docs.cloud.google.com/shell/docs)

|  Unsupported  |  |  Alternatives:  |  Google recommends that you use Cloud Workstations as an alternative.   
---|---  
  
### [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Cloud SQL](https://docs.cloud.google.com/sql/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Query Insights isn't supported.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  | 

  * The Help Assistant isn't supported.
  * Query Insights isn't supported.

  
  
### [Cloud Storage](https://docs.cloud.google.com/storage/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * Viewing object details requires [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) to be enabled for the bucket.
  * Process with Cloud Run functions isn't supported.
  * Scan with Cloud Data Loss Prevention isn't supported.

  
---|---  
Google Cloud API:  | 

  * Identity federation with all Cloud Storage APIs is supported only for [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) buckets. Identity federation access to buckets with fine-grained [access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) is rejected.
  * Although all users and workloads can use existing [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls), identity federation users and workloads cannot generate signed URLs.

  
Other:  |  [Google Cloud access tokens that are based on Workforce Identity Federation credentials](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#exchange_external_credentials_for_a_access_token) cannot be downscoped with [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials) .   
  
### [Cloud Talent Solution](https://docs.cloud.google.com/talent-solution/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Tasks](https://docs.cloud.google.com/tasks/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  The App Engine routing override option isn't available for Workforce Identity Federation users.   
---|---  
Google Cloud API:  |  The Cloud Tasks API doesn't support identity federation for tasks that have App Engine targets—for example: 

  * **App Engine queues:** Since App Engine queues (queues that are created using a `queue.yaml` or `queue.xml` file) contain only tasks with App Engine targets, tasks in these queues aren't supported. 
  * **Regular queues:** For regular Cloud Tasks queues, tasks with HTTP targets are supported. Tasks with App Engine targets aren't supported (even though the queue isn't an App Engine queue). 

  
Other:  |  No known limitations   
  
### [Cloud Trace](https://docs.cloud.google.com/trace/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Translation](https://docs.cloud.google.com/translate/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Vision API](https://docs.cloud.google.com/vision/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cloud Workstations](https://docs.cloud.google.com/workstations/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Cluster Director](https://docs.cloud.google.com/cluster-director/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  To connect to the nodes in your cluster by using the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) , you must [grant access to users outside of your organization](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#external-user) .   
  
### [Compute Engine](https://docs.cloud.google.com/compute/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  To use [SSH-in-browser](https://docs.cloud.google.com/compute/docs/ssh-in-browser) , you must set up [`google.posix_username` attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) .   
---|---  
Google Cloud API:  | 

  * Importing and exporting images and disks with a Cloud Storage bucket requires [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) to be enabled for the bucket. To work around this limitation, use one of the following options: 
    * If you don't need fine-grained object access control lists (ACLs), [enable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access) on the affected Cloud Storage bucket:   
`gcloud storage buckets update gs://BUCKET_NAME --uniform-bucket-level-access`
    * Use [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation) to import and export images and disks with buckets that don't have uniform bucket-level access enabled. Google service accounts are first-party credentials and aren't subject to identity federation limitations. To impersonate a service account, run the following command:   
`gcloud config set auth/impersonate_service_account SERVICE_ACCOUNT_EMAIL`
  * [Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs) isn't supported.

  
Other:  |  No known limitations   
  
### [Confidential Space](https://docs.cloud.google.com/confidential-computing/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Context-Aware Access](https://docs.cloud.google.com/beyondcorp-enterprise/docs)

|  [Preview](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * In **Add principals to the Google Cloud console & APIs**, the **Group ID** text field doesn't support autocomplete or provide validation for Workforce Identity Federation users.
  * Workforce Identity Federation groups are identified by their IDs rather than their names.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Customer Experience Insights](https://docs.cloud.google.com/contact-center/insights/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Data Catalog](https://docs.cloud.google.com/data-catalog/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  In the edit [steward](https://docs.cloud.google.com/data-catalog/docs/concepts/metadata#types_of_business_metadata) dialog on the entry details page, contact suggestions aren't shown.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Database Migration Service](https://docs.cloud.google.com/database-migration/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Dataflow](https://docs.cloud.google.com/dataflow/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Dataform](https://docs.cloud.google.com/dataform/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * [Dataplex Explore workbench](https://docs.cloud.google.com/dataplex/docs/explore-data) doesn't support Workforce Identity Federation.
  * [Scheduled scripts and notebooks through explore workbench](https://docs.cloud.google.com/dataplex/docs/schedule-queries-notebooks) don't support Workforce Identity Federation.
  * [Secure view](https://docs.cloud.google.com/dataplex/docs/lake-security#secure-view) doesn't support Workforce Identity Federation.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * Workforce Identity Federation users can perform create, view, update, and delete operations in Cluster, Jobs, and Batches list pages. Workflows, Autoscaling policies, and component exchange aren't available to Workforce Identity Federation.
  * Cluster create functionality is available, except for Managed Service for Apache Spark on GKE cluster creation, Managed Service for Apache Spark Compute Engine cluster with personal authentication, or with Component Gateway enabled.
  * The **Output**section in the Batch and Job detail page isn't available for Workforce Identity Federation users.****
  * The **Recommend Alert** section in the Cluster and Job list page isn't available for Workforce Identity Federation users.

  
---|---  
Google Cloud API:  |  The following methods don't support identity federation: 

  * [Dataproc on GKE](https://docs.cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke-overview)
  * [Managed Service for Apache Spark Personal Cluster Authentication](https://docs.cloud.google.com/dataproc/docs/concepts/iam/personal-auth)
  * [Managed Service for Apache Spark Service Account based Secure Multi-tenancy](https://docs.cloud.google.com/dataproc/docs/concepts/iam/sa-multi-tenancy)

  
Other:  |  No known limitations   
  
### [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Datastore](https://docs.cloud.google.com/datastore/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Datastream](https://docs.cloud.google.com/datastream/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Dialogflow](https://docs.cloud.google.com/dialogflow/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Dialogflow ES is not supported in the Google Cloud console for Workforce Identity Federation users.   
---|---  
Google Cloud API:  |  Workforce Identity Federation is supported only on Dialogflow CX APIs.   
Other:  |  No known limitations   
  
### [Document AI](https://docs.cloud.google.com/document-ai/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Enterprise Knowledge Graph](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Error Reporting](https://docs.cloud.google.com/error-reporting/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Eventarc](https://docs.cloud.google.com/eventarc/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  [Third-party event publishing](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview) using a `ChannelConnection` resource isn't supported for identity federation.   
Other:  |  No known limitations   
  
### [Filestore](https://docs.cloud.google.com/filestore/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Firestore](https://docs.cloud.google.com/firestore/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  [Security Rules](https://docs.cloud.google.com/firestore/docs/security/get-started) don't support Workforce Identity Federation.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Gemini](https://docs.cloud.google.com/duet-ai/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  Gemini for Google Cloud [license management](https://docs.cloud.google.com/gemini/docs/manage-licenses) doesn't support Workforce Identity Federation.   
  
###  [ Google Antigravity ](https://antigravity.google/docs/enterprise)

|  Unsupported  |  |  Alternatives:  |  Google Antigravity doesn't support Workforce Identity Federation. As an alternative, authenticate the Antigravity CLI using a Google Workspace or Cloud Identity account, or use short-lived credentials through service account impersonation with Application Default Credentials (ADC).   
---|---  
  
### [Google Cloud Armor](https://docs.cloud.google.com/armor/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Google Cloud Contact Center as a Service](https://docs.cloud.google.com/contact-center/ccai-platform/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Google Cloud CCaaS cannot be set up by a Workforce Identity Federation user through the Google Cloud CCaaS console.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  To set up Google Cloud CCaaS through the gcloud CLI, [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) users must contact Customer Care.   
  
### [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) is supported for authentication to the [open source Apache Kafka APIs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka) . However, it is not supported for clients using [Fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) . As an alternative, [link Kubernetes ServiceAccounts to IAM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) .   
  
### [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * Cloud Marketplace contains links to Google domains that might not support Workforce Identity Federation.
  * The **Launch** button is disabled for all VM products that use Deployment Manager because Deployment Manager doesn't support Workforce Identity Federation.
  * SaaS sign-up and SSO login don't support Workforce Identity Federation.
  * Producer Portal doesn't support Workforce Identity Federation.
  * [Request Procurement](https://docs.cloud.google.com/marketplace/docs/governance/requesting-procurement) doesn't support Workforce Identity Federation.
  * Service Catalog doesn't support Workforce Identity Federation.

  
---|---  
Google Cloud API:  |  [Partner API](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference) doesn't support Workforce Identity Federation.   
Other:  |  Customers don't receive notifications if no email address is provided by Billing Account Admins or Product Owners.   
  
### [Google Cloud Migration Center](https://docs.cloud.google.com/migration-center/docs)

|  [Preview](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * [Exporting Total Cost of Ownership Reports (TCO Reports)](https://docs.cloud.google.com/migration-center/docs/generate-tco-report#export_your_tco_report) isn't supported for Workforce Identity Federation users.
  * [Exporting assets](https://docs.cloud.google.com/migration-center/docs/view-assets#export_assets_data) isn't supported for Workforce Identity Federation users.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Google Distributed Cloud air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  When you log in to any attached Google Distributed Cloud connected cluster, the option **Use your Google identity** isn't available for Workforce Identity Federation.   
---|---  
Google Cloud API:  |  If you use Workload Identity Federation to programmatically run `kubectl` commands against different clusters from a Pod, you must use service account impersonation, as described in [ Alternative: link Kubernetes ServiceAccounts to IAM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) . This limitation doesn't apply if you use your own workload identity pool with Workload Identity Federation.   
Other:  |  No known limitations   
  
### [Google Distributed Cloud software only](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  When you log in to any attached Google Distributed Cloud software-only for bare metal cluster, the option **Use your Google identity** isn't available for Workforce Identity Federation.   
---|---  
Google Cloud API:  |  If you use Workload Identity Federation to programmatically run `kubectl` commands against different clusters from a Pod, you must use service account impersonation, as described in [ Alternative: link Kubernetes ServiceAccounts to IAM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) . This limitation doesn't apply if you use your own workload identity pool with Workload Identity Federation.   
Other:  |  `gkectl` and `bmctl` don't support Workforce Identity Federation.   
  
### [Google Earth Engine](https://cloud.google.com/earth-engine)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Earth Engine Code Editor doesn't support Workforce Identity Federation.   
---|---  
Google Cloud API:  | 

  * Exporting data to Google Drive from Earth Engine APIs isn't supported for Workforce Identity Federation.
  * Legacy Earth Engine assets that aren't managed by Google Cloud projects aren't supported for Workforce Identity Federation users.

  
Other:  |  The BigQuery function [`ST_REGIONSTATS`](https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions#st_regionstats) for raster data doesn't support Workforce Identity Federation.   
  
### [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * When you log in to any attached cluster, GKE on AWS cluster, or GKE on Azure cluster, the option **Use your Google identity** isn't available for Workforce Identity Federation.
  * When you create or attach any attached cluster, GKE on AWS cluster, or GKE on Azure cluster, you won't automatically be added as an administrator for Workforce Identity Federation.

  
---|---  
Google Cloud API:  |  If you use Workload Identity Federation for GKE to programmatically run `kubectl` commands against a different GKE cluster from a Pod, you must use service account impersonation, as described in [Alternative: link Kubernetes ServiceAccounts to IAM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) . This limitation doesn't apply if you use your own workload identity pool with Workload Identity Federation.   
Other:  |  `gkeadm` , `gkectl` and `bmctl` don't support Workforce Identity Federation.   
  
### [Google Security Operations](https://docs.cloud.google.com/chronicle)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Hybrid Connectivity](https://docs.cloud.google.com/hybrid-connectivity)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Identity and Access Management](https://docs.cloud.google.com/iam/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * The **Name** column within the IAM table doesn't show display names for Google identities.
  * When adding new principals to allow policies, the **Add principals** text field supports only autocompletion for service accounts.
  * The **Add exempted principal** text field in the **Audit Logs** page supports only autocompletion for service accounts.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * In the Applications tab, the **Method** column is disabled, and users cannot use external identities for authorization.
  * In the Applications tab, App Engine resources cannot be listed.
  * The **Go to OAuth configuration** item in the _more_vert_ action menu isn't available.
  * In the **Applications** tab, on-premises connectors cannot be added or listed.

  
---|---  
Google Cloud API:  |  The IAP API doesn't support TCP forwarding for Workforce Identity Federation users. You must instead use console (federated) or the gcloud CLI for TCP forwarding.   
Other:  |  No known limitations   
  
### [Identity Platform](https://docs.cloud.google.com/identity-platform/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Enabling Identity Platform through the Google Cloud Workforce Identity Federation console is not supported. Workforce Identity Federation administrators must enable Identity Platform either through the Firebase Authentication console or by logging into the Google Cloud console using a Cloud Identity or Workspace account before Workforce Identity Federation users can access Identity Platform through the console (federated).   
---|---  
Google Cloud API:  |  [`InitializeIdentityPlatform`](https://docs.cloud.google.com/identity-platform/docs/reference/rpc/google.cloud.identitytoolkit.admin.v2#google.cloud.identitytoolkit.admin.v2.ProjectConfigService.InitializeIdentityPlatform) doesn't support identity federation.   
Other:  |  No known limitations   
  
### [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Knative serving](https://docs.cloud.google.com/anthos/run/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * [Continuous deployment with Cloud Build](https://docs.cloud.google.com/anthos/run/docs/continuous-deployment-with-cloud-build) doesn't support Workforce Identity Federation.
  * [Registering a domain with Cloud Domains](https://docs.cloud.google.com/anthos/run/docs/mapping-custom-domains#register-domain) doesn't support Workforce Identity Federation.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  When using Workforce Identity Federation, Knative serving requires a cluster with managed Cloud Service Mesh.   
  
### [Live Stream API](https://docs.cloud.google.com/livestream/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Data Studio](https://docs.cloud.google.com/looker/docs/studio)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  Workforce Identity Federation users can't use [IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview) to access the [Active Directory management VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/part-1-deploy-active-directory#creating_a_management_vm) .   
  
### [Media CDN](https://docs.cloud.google.com/media-cdn/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  The following APIs support identity federation: 

  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis)
  * [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [Memorystore for Memcached](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey)

  
Other:  |  No known limitations   
  
### [Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Multi-party Compute](https://docs.cloud.google.com/multi-party-compute)

|  [Preview](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Firewall Insights cannot be exported to JSON or CSV.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Parallelstore](https://docs.cloud.google.com/parallelstore/docs/overview/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Personalized Service Health](https://docs.cloud.google.com/service-health/docs/overview/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Policy Intelligence](https://docs.cloud.google.com/policy-intelligence/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  The following Policy Intelligence features have limitations for Workforce Identity Federation users who use the Google Cloud Workforce Identity Federation console: 

  * [Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access): Workforce Identity Federation users can't troubleshoot access in the console (federated). 
  * [Policy Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview): Workforce Identity Federation users can't analyze access in the console (federated). 
  * [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview): Workforce Identity Federation users can't simulate changes to an allow policy within the console (federated). 
  * [IAM Recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview): Workforce Identity Federation users can't view recommendations in the console (federated). 

  
---|---  
Google Cloud API:  |  The following Policy Intelligence features have API limitations for federated identities: 

  * [Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access): Federated identities can't check the membership of Google groups in allow and deny policies, or the membership of Cloud Identity accounts (domains) in deny policies. When federated identities call the `iam.troubleshoot` method, role bindings and deny rules that contain groups or domains have an access result of **Unknown** , unless the role binding or deny rule also explicitly includes the principal. 
  * [Policy Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview): When calling the [`analyzeIamPolicy`](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy) or the [`analyzeIamPolicyLongrunning`](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning) method, federated identities might receive incomplete analysis results because of the following: 
    * Federated identities can't check the membership of Google groups in allow policies. As a result, when federated identities analyze access for a principal, the query results don't include permissions and roles that the principal has due to their membership in a group. 
    * When analyzing access, federated identities can't enable the `expand-groups` option. 
Federated identities can't use the following API methods: 
    * [`analyzeMove`](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove)
  * [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview): Federated identities can't use the Policy Simulator API (`policysimulator.googleapis.com`). 
  * [Activity Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication): Federated identities can't use the Policy Analyzer API (`policyanalyzer.googleapis.com`). 
  * [IAM Recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview): Federated identities can't use the Recommender API (`recommender.googleapis.com`). 

  
Other:  |  No known limitations   
  
### [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  When publishing a service, DNS configuration is not available.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  In the **Entitlements** section, when you type requester and approver principals, only service account names are autocompleted.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  Automated [email notifications](https://docs.cloud.google.com/iam/docs/pam-overview#email-notifications) aren't sent for entitlement and grant changes. For notifications to be sent, administrators or requesters can explicitly configure email addresses.   
  
### [Pub/Sub](https://docs.cloud.google.com/pubsub/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  [Pub/Sub Lite API](https://docs.cloud.google.com/pubsub/lite/docs) doesn't have endpoints that support identity federation.   
Other:  |  No known limitations   
  
### [reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * Multi-factor authentication through email cannot be configured by Workforce Identity Federation users. For assistance, [contact sales](https://go.chronicle.security/recaptchaupgrade).
  * The demonstration website in Cloud Shell isn't supported for Workforce Identity Federation users.

  
---|---  
Google Cloud API:  |  [`MigrateKey`](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.MigrateKey) isn't supported for federated identities.   
Other:  |  No known limitations   
  
### [Recommender](https://docs.cloud.google.com/recommender/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  [Exporting recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq) isn't supported by Workforce Identity Federation.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Resource Manager](https://docs.cloud.google.com/resource-manager/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Workforce Identity Federation users can only view and operate on the organization for which Workforce Identity Federation was configured. Other organizations to which the users are added are not displayed in the Google Cloud console.   
---|---  
Google Cloud API:  |  The [Organizations API](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations) doesn't support identity federation.   
Other:  |  No known limitations   
  
### [AI Commerce Search API](https://docs.cloud.google.com/retail/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * [User events information](https://docs.cloud.google.com/retail/docs/user-events) is hidden for Workforce Identity Federation users.
  * [Merchant Center accounts](https://docs.cloud.google.com/retail/docs/upload-catalog#mc-ret) are not supported for workforce federation users.
  * [Serving configs](https://docs.cloud.google.com/retail/docs/configs) analytics and usage count are hidden for Workforce Identity Federation users.
  * [Model data requirements](https://docs.cloud.google.com/retail/docs/create-models#import-reqs) are hidden for Workforce Identity Federation users.

  
---|---  
Google Cloud API:  |  The following methods don't support identity federation: 

  * [UpdateCatalog](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CatalogService.UpdateCatalog)
  * [ImportCompletionData](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.CompletionService.ImportCompletionData)
  * [TuneModel](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ModelService.TuneModel)
  * [ImportProducts](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.ImportProducts)
  * [PurgeProducts](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.ProductService.PurgeProducts)
  * [ImportUserEvents](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.ImportUserEvents)
  * [PurgeUserEvents](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.PurgeUserEvents)
  * [RejoinUserEvents](https://docs.cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2alpha#google.cloud.retail.v2alpha.UserEventService.RejoinUserEvents)

  
Other:  |  No known limitations   
  
### [Secret Manager](https://docs.cloud.google.com/secret-manager/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  | 

  * Identity federation users must sign in through the Secure Source Manager instance [web interface](https://docs.cloud.google.com/secure-source-manager/docs/create-instance-federated-identities#access-instance) before running any of the following commands: 
    * Git CLI commands
    * API calls to [data plane endpoints](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest#service-endpoint)
  * Identity federation users must sign in through the Secure Source Manager instance [web interface](https://docs.cloud.google.com/secure-source-manager/docs/create-instance-federated-identities#access-instance) after every session expiry to continue using Git SSH CLI commands with user SSH keys.

  
Other:  | 

  * A new Secure Source Manager instance must be created to use Workforce Identity Federation. Existing instances can't be updated.
  * Workforce identity pool providers used for Secure Source Manager must provide `google.subject` and `google.email` attribute mappings.
  * You can only use your federated identity to log in to a Secure Source Manager instance that is configured to use Workforce Identity Federation.
  * Email notifications from Secure Source Manager are not supported for Workforce Identity Federation configured instances.

  
  
### [Security Command Center](https://docs.cloud.google.com/security-command-center/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  The following features are unavailable for Workforce Identity Federation users: 

  * The Security posture service cannot be managed using Google Cloud console.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Sensitive Data Protection](https://docs.cloud.google.com/dlp/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Service Directory](https://docs.cloud.google.com/service-directory/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs)

|  [Preview](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Managing quota in [Cloud Endpoints](https://docs.cloud.google.com/endpoints) is not supported.   
---|---  
Google Cloud API:  |  [Service Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started) : Creating a managed service doesn't support identity federation. To verify domain ownership and create a managed service, do the following: 

  1. [Add a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) to domain owners using [Site Verification API](https://developers.google.com/site-verification).
  2. [Impersonate this service account](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) to create a managed service.

  
Other:  |  No known limitations   
  
### [Spanner](https://docs.cloud.google.com/spanner/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Only the v2 UI pages support Workforce Identity Federation.   
---|---  
Google Cloud API:  |  Only the v2 API supports identity federation.   
Other:  |  No known limitations   
  
### [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Transcoder API](https://docs.cloud.google.com/transcoder/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview/)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Translation Hub](https://docs.cloud.google.com/translation-hub/docs)

|  Unsupported  |  |  Alternatives:  |  No alternatives available   
---|---  
  
### [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * When Workforce Identity Federation users create a new model monitoring job, Agent Platform doesn't prefill the alert email input with their email address.
  * Vertex AI Pipelines doesn't support Workforce Identity Federation in the console (federated). Instead, use the Vertex AI SDK for Python or the Vertex AI API.

  
---|---  
Google Cloud API:  |  Agent Platform doesn't send email messages to Workforce Identity Federation users.   
Other:  |  Colab Enterprise doesn't support Workforce Identity Federation.   
  
### [Vertex AI Agent Builder](https://docs.cloud.google.com/agent-builder/overview)

|  [Preview](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  | 

  * [Vertex AI agents](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#agent) creation and preview aren't supported.
  * [Google Drive data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#google-drive) creation isn't supported.

  
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Gemini Enterprise](https://cloud.google.com/gemini-enterprise)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  Workspace connectors are not supported for Workforce Identity Federation users.   
  
### [Vertex AI Vision](https://docs.cloud.google.com/vision-ai/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Video stream playback doesn't work for Workforce Identity Federation users.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/notebook-solution)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  | 

  * [Vertex AI Workbench managed notebooks](https://docs.cloud.google.com/vertex-ai/docs/workbench/managed/introduction) ([Deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations)) doesn't support Workforce Identity Federation.
  * [Vertex AI Workbench user-managed notebooks](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/introduction) ([Deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations)) doesn't support Workforce Identity Federation.

  
Other:  |  No known limitations   
  
### [Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Video Stitcher API](https://docs.cloud.google.com/video-stitcher/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  Identity federation is not supported for LiveConfig and Slate resources when Google Ad Manager (GAM) fields are set.   
Other:  |  No known limitations   
  
### [Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  Autocomplete suggestions aren't supported when adding user identities in the following fields: 

  * [Access policies](https://docs.cloud.google.com/access-context-manager/docs/overview#access-policies)
  * [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) in service perimeters

  
---|---  
Google Cloud API:  | 

  * [`v1alpha` APIs](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1alpha) aren't available to federated identities.
  * VPC Service Controls supports only specific [Workforce Identity Federation and Workload Identity Federation principal identifiers](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities). You can use these principal identifiers to [configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

  
Other:  |  No known limitations   
  
### [Web Risk](https://docs.cloud.google.com/web-risk/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Workflows](https://docs.cloud.google.com/workflows/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  The automated grant feature, which grants the Workforce Identity Federation user the Service Account User ( `roles/iam.serviceAccountUser` ) role on the project, is inactive. To grant the role to Workforce Identity Federation users, you must go to the IAM page and specify a Workforce Identity Federation [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers) or contact the project owner to do so.   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
### [Workload Manager](https://docs.cloud.google.com/workload-manager/docs)

|  [GA](https://cloud.google.com/products/#product-launch-stages) |  |  Console (federated):  |  No known limitations   
---|---  
Google Cloud API:  |  No known limitations   
Other:  |  No known limitations   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
