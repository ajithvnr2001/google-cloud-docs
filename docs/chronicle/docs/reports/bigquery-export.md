---
url: https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export/
title: Stream data with advanced BigQuery export \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:21.114110+00:00
---

# Stream data with advanced BigQuery export  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stream data with advanced BigQuery export

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document describes how to access and use your Google SecOps data in BigQuery with the **Advanced BigQuery Export** feature. As an Enterprise Plus customer, you can use the feature to access your security data in near-real-time through a fully managed, streaming data pipeline. This capability can help address the critical challenge of data latency in security operations and lead to more timely and effective threat detection and response.

## Before you begin

Review the following points that define eligibility requirements and necessary actions:

  * **Enterprise Plus customers only** : This feature is available for Google SecOps Enterprise Plus customers only. For all other customers, see [Export to a self-managed BigQuery project](https://docs.cloud.google.com/chronicle/docs/preview/cloud-integration/export-to-customer-managed-project).
  * **Feature activation required** : This feature is enabled on request and may require initial configuration in your organization's Google SecOps instance. Contact your Google SecOps representative to confirm feature enablement, if necessary.
  * **Data migration** : When you activate this feature, your data begins to export to a new BigQuery tenant project for your Google SecOps instance in addition to your existing exports to your Google-managed BigQuery project as described in [Export to a Google-managed BigQuery project](https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery). This dual operation supports your move to the new feature without disruption. You are notified before the old export pipeline is disabled for your account.
  * **VPC Service Controls** : Advanced BigQuery Export can work in a VPC Service Controls perimeter. For more information, see [Configure VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops).
  * **Customer-Managed Encryption Keys (CMEK)** : Advanced BigQuery Export is available for customers who have enabled CMEK on their Google SecOps instance. For more information, see [CMEK for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops). If you use CMEK with VPC Service Controls, refer to [Configure VPC Service Controls for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) for recommendations and instructions. 



## Feature overview

Advanced BigQuery Export automatically provisions and manages essential Google SecOps datasets, including [Unified Data Model (UDM) events](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview), rule detections, entity graphs, and Indicator of Compromise (IoC) matches—in a secure, Google-managed BigQuery project. You gain secure, read-only access to this data through a BigQuery linked dataset, which appears directly in your own Google Cloud project. This functionality lets you query your security data as if it were stored locally, but without the overhead of managing the data pipeline or storage.

Google SecOps exports the following categories of security data to BigQuery:

  * **UDM event records** : UDM records created from log data ingested by customers. These records are enriched with aliasing information.
  * **Rule matches (detections)** : Instances where a rule matches one or more events.
  * **IoC matches** : Artifacts (for example, domains or IP addresses) from events that match IoC feeds. This includes matches to and from global feeds and customer-specific feeds.
  * **Ingestion metrics** : Statistics, such as the number of log lines ingested, the number of events produced from logs, and the number of log errors indicating that logs couldn't be parsed.
  * **Entity graph and entity relationships** : The description of entities and their relationships with other entities.



### Core benefits

The core benefits of Advanced BigQuery Export include the following:

  * **Near-real-time data freshness** : A streaming architecture makes your security data available for querying within minutes of ingestion. UDM events, rule detections, and IoC matches are available with an expected latency of 5-10 minutes.
  * **Simplified and predictable cost model** : Google SecOps covers all data ingestion and storage costs within the managed BigQuery project. Your organization is responsible only for the BigQuery analysis costs incurred when you run queries.
  * **Zero-maintenance data access** : The underlying infrastructure is fully managed by Google, which lets your team focus on data analysis rather than data engineering.
  * **Data integrity and deduplication** : Security data is frequently updated or _re-enriched_ after initial ingestion. The feature uses fine-grained Data Manipulation Language (DML) merges to update records in place. You receive clean, deduplicated data without writing complex SQL deduplication routines.
  * **Seamless MSSP support (hub-and-spoke)** : Managed Security Service Providers (MSSPs) can efficiently manage analytics across multiple customer tenants by programmatically subscribing to their customers' linked datasets from a single, centralized _hub_ project.
  * **Built-in compliance** : The feature natively supports [VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops), [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops), and data residency (DRZ). Customer-facing audit logs (Access Transparency) are delivered directly to your Cloud Logging workspace using the Federated Resource Identification Service (FRIS).



### Common use cases

Advanced BigQuery Export is designed for security analysts, threat hunters, data scientists, and security engineers who require direct, high-performance access to fresh security data for ad hoc investigations, custom analytics, and integration with business intelligence tools.

Common use cases for Advanced BigQuery Export include the following:

  * Run ad hoc queries directly in BigQuery.
  * Use your own business intelligence tools, such as Microsoft Power BI, to create dashboards, reports, and analytics.
  * Join Google SecOps data with third-party datasets.



### Architecture

The Advanced BigQuery Export architecture uses a continuous streaming pipeline. Data from your Google SecOps instance is pushed to a secure, Google-managed tenant project using the high-throughput BigQuery Storage Write API (gRPC). 

Google SecOps uses BigQuery sharing to create a secure [data listing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings) and provide you with access. In your BigQuery **Explorer** pane, your Google Cloud project is automatically subscribed to this listing, which is displayed as the `secops_linked_datalake` [linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets).

This model supports strong data isolation while giving you seamless, read-only query access.

### Key terminology

The following are some key terms and concepts for Advanced BigQuery Export:

  * **[Tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant)** : A Google Cloud project that is owned and managed by Google SecOps. This project is where your exported security data is physically stored and managed. You don't have direct access to this project.
  * **[BYOP (Bring Your Own Project)](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project)** : The Google Cloud project that your organization owns and links to your Google SecOps instance. This is the project where the linked dataset appears and where you run your queries and incur analysis costs. 
  * **[Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin)** : The globally unique identifier for your Google Cloud project linked to your Google SecOps instance.
  * **[Linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets)** : A read-only BigQuery dataset that serves as a symbolic link or pointer to a shared dataset in another project. It lets you query data without copying it, providing secure access while the data provider manages the physical storage.
  * **[Fine-grained DML (FGDML)](https://docs.cloud.google.com/bigquery/docs/data-manipulation-language#fine-grained_dml)** : The automated backend process that Advanced BigQuery Export uses to perform upserts (updates and inserts). If an event arrives late or is re-enriched, the system updates the existing row in place, based on its unique identifier (for example, `metadata.id`) rather than creating a duplicate.
  * **[Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview)** : Google's extensible, standard schema for parsing and normalizing security telemetry data from hundreds of vendor products into a consistent format.
  * **[Managed Security Service Providers (MSSP)](https://cloud.google.com/security/partners/mssp?e=48754805)** : Google Cloud certified MSSPs offer a comprehensive suite of tools and expertise to fortify your defenses against ever-evolving cybersecurity threats.



## Set up your system

To use Advanced BigQuery Export, you must first set up your system. Depending on your environment and requirements, follow the instructions in one of the following sections.

### Default setup

Follow these steps to set up your system to use Advanced BigQuery Export and begin querying your data:

  1. **Confirm your license** : Make sure that your organization has a Google SecOps Enterprise Plus license.
  2. **Identify your project** : Sign in to the Google Cloud console and select the Google Cloud project that is linked to your Google SecOps instance.
  3. **Locate the linked dataset** : In the BigQuery console, use the **Explorer** pane to navigate to your project's resources. You see a linked dataset named `secops_linked_datalake`. This dataset is a read-only pointer to the live security data managed by Google SecOps.
  4. **Verify Identity and Access Management (IAM) permissions** : To query the data, your user or service account must have the following IAM roles granted on your project:

     * `roles/bigquery.dataViewer`: Required for end users or BI tools in your organization to run SQL queries against the linked dataset views.
     * `roles/bigquery.jobUser`: Required for end users or BI tools in your organization to run SQL queries against the linked dataset views.
     * `Chronicle API Admin`: Required within Google SecOps to execute the Dataplane APIs (for example, `ProvisionPartnerSubscription`) to manage MSSP subscriptions.

These roles allow users (such as security analysts and data consumers) to query data in the linked dataset and run BigQuery jobs within their project.

  5. **Run a test query** : Open the BigQuery SQL workspace and run a basic query to verify that your access is configured correctly. You can use the following code snippet:
         
         SELECT *
         FROM `PROJECT_ID.secops_linked_datalake.events`
         LIMIT 10;
         

Replace PROJECT_ID with your actual Google Cloud Project ID.




### Set up Advanced BigQuery Export within a VPC Service Controls perimeter

To set up Advanced BigQuery Export within your VPC Service Controls perimeter, you need to configure a specific ingress rule. This rule allows the necessary Google SecOps service accounts to interact with BigQuery and related services on the projects protected by the perimeter. For detailed instructions and more information, see [Configure VPC Service Controls for Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops).

  * To set up Advanced BigQuery Export within your VPC Service Controls perimeter, configure the following ingress rule:
        
        - ingressFrom:
            identities:
            - serviceAccount:malachite-advanced-bq-exporter@system.gserviceaccount.com
            - serviceAccount:malachite-data-export-service@system.gserviceaccount.com
            sources:
            - accessLevel: "*"
          ingressTo:
            operations:
            - serviceName: analyticshub.googleapis.com
              methodSelectors:
              - method: "*"
            - serviceName: bigquery.googleapis.com
              methodSelectors:
              - method: "*"
            resources:
            - projects/PROJECT_NUMBER
        

Replace `PROJECT_NUMBER` with your Google SecOps-linked Google Cloud project number.




### For MSSPs — Set up centralized access to BigQuery data of your sub-tenants

If you are provisioned as an MSSP, you can leverage Google SecOps dataplane APIs to programmatically create BigQuery linked datasets in your central "hub" project. These linked datasets point to the BigQuery data of your customers (spokes), enabling you to query across multiple tenants from a single pane of glass. This process requires your customer to grant your MSSP instance access.

The key benefits include:

  * **Centralized visibility:** Analyze security data across all your customers in one place.
  * **Efficient workflows:** Streamline threat hunting and reporting across your client base.
  * **Programmatic management:** Automate the setup and teardown of data access.



#### Prerequisites

  * **MSSP**

    * A Google Cloud project to serve as your central "hub."
    * A Google SecOps instance.
    * Appropriate IAM permissions to manage BigQuery datasets in your hub project.
  * **Customer (Sub-tenant)**

    * A Google SecOps Enterprise Plus license.
    * A Google Cloud project (BYOP) linked to your Google SecOps instance.
    * Appropriate IAM permissions to manage Google SecOps API access.
    * `gcloud` CLI installed and authenticated.



#### Step 1: Customer grants MSSP access

The customer can call the ProvisionPartnerSubscription API to grant permissions to their MSSP's Google SecOps instance. Google SecOps automatically provisions a BigQuery linked dataset, named in the format of `secops_linked_datalake_<customer_id>` within the MSSP's Google Cloud Project linked to the MSSP's Google SecOps instance. This dataset links to the customer's Google SecOps data.

##### API endpoint:
    
    
    POST
    https://chronicle.googleapis.com/v1alpha/projects/CUSTOMER_PROJECT/locations/REGION/instances/CUSTOMER_INSTANCE_ID/bigQueryExport:provisionPartnerSubscription
    

##### Method

`POST`

##### Request body

Empty JSON object.
    
    
    {}
    

**Example CURL command (to be run by the customer):**
    
    
    curl -X POST \
      -H "Authorization: Bearer ${OAUTH_TOKEN}" \
      -H "Content-Type: application/json" \
      -d '{}' \
      "https://chronicle.googleapis.com/v1alpha/projects/CUSTOMER_PROJECT/locations/REGION/instances/CUSTOMER_INSTANCE_ID/bigQueryExport:provisionPartnerSubscription"
    

Replace the following placeholders:

  * CUSTOMER_PROJECT: The customer's Google Cloud Project ID or Project Number. See [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
  * REGION: The Google Cloud region where the customer's Google SecOps instance resides (for example, us, europe-west2). See the list of [regions](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint).
  * CUSTOMER_INSTANCE_ID: The customer's Google SecOps Instance ID.



##### Response body

Returns `ProvisionPartnerSubscriptionResponse` containing the subscription details.
    
    
    {
      "subscriptionDetails": {
        "subscription": "projects/SUBSCRIBER_PROJECT_ID/locations/SUBSCRIBER_REGION/subscriptions/SUBSCRIPTION_ID",
        "linkedDataset": "string"
      }
    }
    

  * SUBSCRIBER_PROJECT_ID: The subscriber MSSP's Google Cloud Project ID.
  * SUBSCRIBER_REGION: The region where the subscriber's Google Cloud Project is located.
  * SUBSCRIPTION_ID: A unique identifier for the existing subscription.



#### Step 2: MSSP queries data across tenants

Once the linked datasets from multiple customers are provisioned in your (MSSP's) Google Cloud Project, you can use standard BigQuery SQL queries to analyze the data. To query across multiple customers, use the UNION ALL operator.

**Example query (to be run by the MSSP in their hub project):**
    
    
    SELECT event_type, timestamp
    FROM `PARTNER_PROJECT_ID.secops_linked_datalake_CUSTOMER_ID_1.events`
    WHERE <your_conditions>
    
    UNION ALL
    
    SELECT event_type, timestamp
    FROM `PARTNER_PROJECT_ID.secops_linked_datalake_CUSTOMER_ID_2.events`
    WHERE <your_conditions>
    
    -- Add more UNION ALL clauses for other customers
    

#### Step 3: Customer audits access

The customer can call the `fetchSubscriptions` API to see all active subscriptions and MSSP instances accessing their data.

##### API endpoint
    
    
    GET https://chronicle.googleapis.com/v1alpha/projects/CUSTOMER_PROJECT/locations/REGION/instances/CUSTOMER_INSTANCE_ID/bigQueryExport:fetchSubscriptions
    

##### Method

`GET`

**Example CURL command (to be run by the customer):**
    
    
    curl -X GET \
      -H "Authorization: Bearer ${OAUTH_TOKEN}" \
      "https://chronicle.googleapis.com/v1alpha/projects/CUSTOMER_PROJECT/locations/REGION/instances/CUSTOMER_INSTANCE_ID/bigQueryExport:fetchSubscriptions"
    

Replace the following placeholders:

  * CUSTOMER_PROJECT: The customer's Google Cloud Project ID or Project Number. See [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
  * REGION: The Google Cloud region where the customer's Google SecOps instance resides (e.g., us, europe-west2). See the list of [regions](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint).
  * CUSTOMER_INSTANCE_ID: The customer's Google SecOps Instance ID.



##### Response body

Returns FetchSubscriptionsResponse with a list of active subscriptions.
    
    
    {
      "subscriptions": [
        {
          "subscription": "projects/SUBSCRIBER_PROJECT_ID/locations/SUBSCRIBER_REGION/subscriptions/SUBSCRIPTION_ID",
          "linkedDataset": "string"
        }
      ]
    }
    

  * SUBSCRIBER_PROJECT_ID: The subscriber's Google Cloud Project ID. The subscriber can refer to either the customer or an MSSP.
  * SUBSCRIBER_REGION: The region where the subscriber's Google Cloud Project is located.
  * SUBSCRIPTION_ID: A unique identifier for the existing subscription.



#### Step 4: Customer revokes access (if needed)

If a customer needs to revoke an MSSP's access, they can use the revokePartnerSubscription API. This action immediately revokes the permission to query the linked dataset using the MSSP's hub project. The revoked subscription's ID becomes inactive.

**Note:** Existing subscriptions are not automatically revoked if a customer's instance is unlinked from an MSSP instance. Revocation must be manually executed.

##### API endpoint
    
    
    POST https://chronicle.googleapis.com/v1alpha/projects/CUSTOMER_PROJECT/locations/REGION/instances/CUSTOMER_INSTANCE_ID/bigQueryExport:revokePartnerSubscription
    

##### Method

`POST`

##### Request body

Requires the URI of the subscription to revoke, which was obtained from the `fetchSubscriptions` API call.
    
    
    {
      "subscriptionUri": "projects/SUBSCRIBER_PROJECT_ID/locations/SUBSCRIBER_REGION/subscriptions/SUBSCRIPTION_ID"
    }
    

**Example CURL command (to be run by the customer):**
    
    
    # Set subscription details obtained from Fetch Subscriptions
    export SUBSCRIBER_PROJECT_ID="partner-byop-project-id"
    export SUBSCRIBER_REGION="subscription-location"
    export SUBSCRIPTION_ID="subscription-id"
    
    curl -X POST \
      -H "Authorization: Bearer ${OAUTH_TOKEN}" \
      -H "Content-Type: application/json" \
      -d '{
        "subscriptionUri": "projects/SUBSCRIBER_PROJECT_ID/locations/SUBSCRIBER_REGION/subscriptions/SUBSCRIPTION_ID"
      }' \
      "https://chronicle.googleapis.com/v1alpha/projects/CUSTOMER_PROJECT/locations/REGION/instances/CUSTOMER_INSTANCE_ID/bigQueryExport:revokePartnerSubscription"
    

Replace the following placeholders:

  * SUBSCRIBER_PROJECT_ID: The subscriber's Google Cloud Project ID.
  * SUBSCRIBER_REGION: The region where the subscriber's Google Cloud Project is located.
  * SUBSCRIPTION_ID: A unique identifier for the existing subscription.
  * CUSTOMER_PROJECT: The customer's Google Cloud Project ID or Project Number.
  * REGION: The Google Cloud region where the customer's Google SecOps instance resides.
  * CUSTOMER_INSTANCE_ID: The customer's Google SecOps Instance ID.



##### Response body

Empty JSON object.
    
    
    {}
    

**Note:** Hub-and-spoke MSSP subscriptions are supported only within the same region. Cross-region federation (for example, US to Europe) isn't supported.

## Query your BigQuery data

You can run queries directly in BigQuery or connect your own business intelligence tool, such as Microsoft Power BI, to BigQuery.

See the following for more information about queries:

  * For information about accessing and running queries in BigQuery, open [Run a query](https://docs.cloud.google.com/bigquery/docs/running-queries) and learn how to [run an interactive query](https://docs.cloud.google.com/bigquery/docs/running-queries#queries) and [run a batch query](https://docs.cloud.google.com/bigquery/docs/running-queries#batch).
  * For information about how to query partitioned tables, see [Query partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables).



### Data retention period in your BigQuery tenant project

The retention period for your data in BigQuery is identical to the data retention period configured for your Google SecOps tenant. There is no separate, configurable setting to customize your retention policy for data in BigQuery. Data is automatically purged from the BigQuery tables as it ages past your tenant's retention window.

### Linked datasets

Linked datasets contain tables corresponding to different types of security data.

**Note:** A linked dataset is strictly read-only. This is a critical security measure to ensure the integrity and accuracy of the data, which is managed exclusively by the Google SecOps platform pipeline.

The following table provides a summary of the available datasets, their target data freshness, and the unique identifiers used for ensuring data integrity:

**Note:** Certain records, such as late-arriving or re-enriched events, are updated using fine-grained Data Manipulation Language (DML) merges. Consequently, there can be a delay of up to 12 hours for these records to appear in your BigQuery dataset.Dataset name | Description | Best expected freshness | Unique identifiers for deduplication  
---|---|---|---  
`events` | Normalized security events in the UDM schema. For information about the schema, see [Google SecOps events schema](https://docs.cloud.google.com/chronicle/docs/reports/events-schema-overview). | < 5 minutes | `id` (String representation)  
`rule_detections` | Detections generated by Google SecOps detection engine rules. | < 5 minutes | detection.id  
`ioc_matches` | Indicator of compromise (IOC) matches found against UDM events. | < 5 minutes | Composite key of day_bucket_seconds, feed_log_type, ioc_type, ioc_value  
`entity_graph` | Contextual data about entities (users, assets) and their relationships. | ~4 hours (batch) | Composite key of partition_day, metadata.product_entity_id, metadata.event_metadata.id  
`ingestion_metrics` | Statistics on log ingestion volume and data sources. | ~5 minutes | None (append-only time-series)  
`entity_enum_value_to_name_mapping` | Maps numerical values to string values for entity graph enumerated types. | N/A | None  
`udm_enum_value_to_name_mapping` | Maps numerical values to string values for UDM event enumerated types. | N/A | None  
**Important:** Until Advanced BigQuery Export is made Generally Available, data for ingestion_metrics will continue to be exported only to your existing [Google-managed BigQuery project](https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery).

### Sample queries

The following examples demonstrate how to query the datasets for common security use cases.

#### Example — Find all network connections from a specific IP address in the last 24 hours

This query searches the events table for recent network activity from a suspicious IP address.
    
    
    SELECT
      metadata.product_event_type,
      principal.ip,
      target.ip,
      network.application_protocol
    FROM
      `PROJECT_ID.secops_linked_datalake.events`
    WHERE
      principal.ip = '192.0.2.1'
      AND metadata.event_timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR);
    

  * Replace PROJECT_ID with your Google Cloud Project ID.



#### Example — Count the top 10 most frequent rule detections

This query on the rule_detections table helps identify the most common threats or policy violations that are detected in your environment.
    
    
    SELECT
      rule_name,
      COUNT(*) AS detection_count
    FROM
      `PROJECT_ID.secops_linked_datalake.rule_detections`
    WHERE
      detection.id IS NOT NULL
    GROUP BY
      1
    ORDER BY
      2 DESC
    LIMIT
      10;
    

  * Replace PROJECT_ID with your Google Cloud Project ID.



## Best practices

The following are some best practices for querying with Advanced BigQuery Export:

  * **Optimize query costs:** Even though storage is free, compute costs are billed to your project, so do the following:

    * Avoid SELECT *. In your query, specify only the columns you need to reduce the amount of data scanned and lower query costs.
    * Make sure that your queries take advantage of BigQuery partitioning (using the hour_time_bucket partition time column) and clustering (hour_time_bucket, log_type, event_type, id) to scan less data and significantly reduce your query costs.
  * **Use partition filters:** The events table is partitioned by the hour_time_bucket column. Always include a WHERE clause filter on this column to limit queries to the smallest possible time window, which significantly improves performance and reduces cost.

  * **Write efficient queries:** The UDM schema is wide and sparse. To efficiently filter for specific event types, use WHERE... IS NOT NULL on relevant fields. For example, to find only DNS queries, filter WHERE network.dns.questions.name IS NOT NULL.

  * **Validate queries:** Use the query validator in the BigQuery UI before you run a query. The query validator provides an estimate of the data processed, helping you avoid unexpectedly large and costly queries.

  * **Use enum mapping tables:** Advanced BigQuery Export includes entity_enum_value_to_name_mapping and udm_enum_value_to_name_mapping tables. Use these to join against your events to translate numerical enum values into human-readable strings without writing manual translation logic in your queries.

  * **Audit logging integration:** Advanced BigQuery Export integrates with the Federated Resource Identification Service (FRIS). Customer-facing audit logs, which use the Google Access Transparency feature, are delivered natively inside your BYOP Cloud Logging workspace if Google personnel access the managed tenant project.




## Known limitations

The following are known limitations of the Advanced BigQuery Export feature:

  * **Entity-graph latency:** The entity_graph dataset is exported using a batch process and has a data freshness of approximately four hours.
  * **UDM schema-column limits:** BigQuery has a soft limit of 10,000 columns per table. The UDM schema contains over 27,000 fields and is sparsely populated. The export pipeline intelligently includes only populated columns for a given event, keeping most customers well under the limit. Google SecOps monitors column usage and proactively requests a limit increase for your tenant project if it approaches this threshold.
  * **Retention period is non-configurable:** The data retention period for all security data exported to BigQuery is automatically synchronized with the data retention period of your Google SecOps project, and isn't configurable separately.
  * **SOAR data isn't supported:** Data from Google Security Operations SOAR (search_everything_db) isn't supported in Advanced BigQuery Export.
  * **Cross-region federation isn't supported:** Hub-and-spoke MSSP subscriptions are supported within the same region. Cross-region federation (for example, US to Europe) isn't supported.
  * **Duplicate events are possible (less than 1% probability):** Although the system uses DML merges to handle deduplication automatically, due to the nature of distributed streaming, there is a remote possibility (< 1%) of duplicate events appearing during edge-case ingestion windows before the background merge completes.
  * **Historical data is accessible but requires specific methods:** Data export begins from the moment that Advanced BigQuery Export is enabled, and older data remains accessible in your existing project. To query data exported prior to the activation of Advanced BigQuery Export, you need either to use a single query that joins data across both projects, or run two separate queries on the respective projects (one for the older dataset and one for the new dataset).



## Troubleshooting and support

The following table provides solutions for common problems that you may encounter:

Observed symptom | Possible cause | Recommended action  
---|---|---  
Queries fail with `Access Denied: User does not have permission.` | The user or service account lacks the necessary BigQuery IAM roles on the Google Cloud project that is linked to your Google SecOps instance. | Grant the **BigQuery Data Viewer** and **BigQuery Job User** roles to the principal. Verify this using `gcloud projects get-iam-policy YOUR_PROJECT_ID --flatten="bindings.members" --format='table(bindings.role)' --filter="bindings.members:user:your-user@example.com"`  
The `secops_linked_datalake` dataset is not visible in my BigQuery project. | 1\. You are not in the correct Google Cloud project.  
2\. Your organization is not on the Enterprise Plus tier.  
3\. Your organization is on the Enterprise Plus tier, but Advanced BigQuery Export is not enabled in your Google SecOps instance. | 1\. In the Google Cloud console, verify you have selected the project linked to your Google SecOps instance.  
2\. Contact your Google representative to confirm your Google SecOps license tier.  
3\. Contact your Google SecOps representative and ask them to enable Advanced BigQuery Export in your Google SecOps instance.  
API call fails with a permission error for `ProvisionPartnerSubscription` or `FetchSubscriptions` | The calling identity lacks the required permissions. | Ensure that the service account or user making the call has the Chronicle API Administrator IAM role, which includes permissions on the hub instance resource.  
Missing custom columns or a schema mismatch | A brand-new log type or deeply nested UDM field was ingested. | Advanced BigQuery Export uses dynamic schema updates. When new UDM fields are populated, the system automatically detects the schema mismatch, pauses briefly, updates the BigQuery schema, and retries the insertion. No action is needed.  
  
## Frequently asked questions

The following sections are some frequently asked questions.

### Do I need to modify my existing, legacy BigQuery SQL queries to use Advanced Google SecOps Export?

No. To maintain 100% backward compatibility, Google SecOps exposes views (for example, events, ioc_matches) in the linked dataset that perfectly match the schema of the tables from the legacy Google SecOps export feature.

### Can I adjust the data retention period for my Advanced BigQuery Export?

No. The data retention period in Advanced BigQuery Export directly mirrors your Google SecOps data retention policy. When data expires in Google SecOps, it automatically expires and is deleted from the BigQuery tenant project.

### Will I be charged for the backend DML updates and deduplication?

No. All backend storage, streaming insert operations, and fine-grained DML compute costs are absorbed by Google SecOps. You only pay for the queries you explicitly run in your BYOP.

### Is this feature available for Google SecOps Standard or Enterprise tiers?

No. Advanced BigQuery Export (managed storage and streaming) is a premium feature exclusive to the Google SecOps Enterprise Plus tier. Standard and Enterprise customers can use the Bring Your Own BigQuery (BYOBQ) model, where they provide the BigQuery project and cover both storage and compute costs.

### Why might I see temporary differences in counts between data in Advanced BigQuery Export and statistics shown in the Google Security Operations UI?

Temporary discrepancies can occur due to the near real-time, streaming nature of the Advanced BigQuery Export pipeline. Here are the key reasons:

  * **Late-arriving data:** The export pipeline is designed for high throughput. Most data appears in BigQuery within 5 to 10 minutes. However, events can sometimes arrive late to the processing pipeline due to network delays or source system issues. While the system aims to merge these late events, there can be a brief window where live UI statistics, which reflect the absolute latest state, differ from the BigQuery data that is undergoing continuous updates.

  * **Data re-enrichment:** Google SecOps continuously enriches event data with the latest threat intelligence and contextual information. The Advanced BigQuery Export exports events based on their state at the time of initial enrichment. If an event is re-enriched with new information after it has been streamed to BigQuery, this updated version might not be immediately reflected in BigQuery. This can lead to differences when comparing against UI elements that always show the fully re-enriched data.

  * **DML merge latency:** To keep the data in BigQuery up-to-date and handle things like late-arriving data or potential duplicates, the pipeline uses Data Manipulation Language (DML) `MERGE` operations in the background. These operations, while efficient, are not instantaneous. There is an inherent latency as these merges are processed, especially for fine-grained updates. During this merge interval, queries against BigQuery might not capture the very latest micro-updates that are already visible in the Google Security Operations UI.




Due to the factors mentioned (late data, re-enrichment handling, and merge latencies), a perfect 1:1 match between BigQuery and live UI statistics at any precise second might not always occur. The Advanced BigQuery Export provides near real-time data, optimized for use cases like threat hunting, custom analytics, and dashboarding where data freshness within minutes is crucial. For audit purposes requiring absolute point-in-time consistency, consider the potential for minor, transient differences.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
