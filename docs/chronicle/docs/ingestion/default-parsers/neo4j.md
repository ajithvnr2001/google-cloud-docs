---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/neo4j/
title: Collect Neo4j Aura logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:38.325730+00:00
---

# Collect Neo4j Aura logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/neo4j/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Neo4j Aura logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Neo4j Aura logs to Google Security Operations using Google Cloud Storage V2.

Neo4j Aura is a fully managed cloud graph database service. It provides security logs and query logs that can be forwarded to Google Cloud Logging for AuraDB Business Critical, AuraDB Virtual Dedicated Cloud, and AuraDS Enterprise tiers.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Logging sinks
  * Neo4j Aura instance running on Google Cloud Platform
  * Neo4j Aura Project Admin role
  * Neo4j Aura tier that supports log forwarding (AuraDB Business Critical, AuraDB Virtual Dedicated Cloud, or AuraDS Enterprise)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `neo4j-aura-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure Neo4j Aura log forwarding to Google Cloud Logging

Neo4j Aura forwards logs to Google Cloud Logging in your GCP project. This configuration is done in the Neo4j Aura Console.

  1. Navigate to the [Neo4j Aura Console](https://console.neo4j.io/).
  2. Sign in with your Neo4j account.
  3. In the sidebar, go to **Settings > Log forwarding**.
  4. Click **Configure log forwarding**.
  5. Select the scope for log forwarding: 
     * **AuraDB Business Critical** : Select a specific instance to forward its logs.
     * **AuraDB Virtual Dedicated Cloud** : Select a region to forward logs from all instances in that region.
     * **AuraDS Enterprise** : Select a region to forward logs from all instances in that region.
  6. Select the type of logs to forward:

     * **Security logs** : Authentication events, authorization events, and security-related activities.
     * **Query logs** : Cypher queries executed on the database.
**Note:** You can create separate log forwarding configurations for security logs and query logs.
  7. If you selected **Query logs** , expand the **Filter** section to configure optional filters:

     * **Remove start entries** : Enable to forward only query end entries (reduces volume by approximately 50%).
     * **Include** : Select **All queries** , **Successful queries only** , or **Failed queries only**.
  8. Follow the instructions in the wizard specific to Google Cloud Platform.

**Note:** The wizard provides detailed steps for configuring the GCP project ID and granting necessary permissions. The exact fields depend on your Neo4j Aura version, but typically include your GCP Project ID.
  9. Complete the wizard and click **Create** or **Save**.

  10. Wait for the status to change from **setting up** to **forwarding**.

**Note:** It may take a few minutes for log forwarding to become active.



## Create Cloud Logging sink to export logs to GCS

After Neo4j Aura forwards logs to Google Cloud Logging, create a log sink to export those logs to your GCS bucket.

  1. In the **GCP Console** , go to **Logging > Log Router**.
  2. Click **Create sink**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Sink name** | Enter a name (for example, `neo4j-aura-to-gcs`)  
**Sink description** | Enter a description (for example, `Export Neo4j Aura logs to GCS for Chronicle`)  
  4. Click **Next**.

  5. In the **Select sink service** section, select **Cloud Storage bucket**.

  6. In the **Select Cloud Storage bucket** dropdown, select the bucket you created (for example, `neo4j-aura-logs`).

  7. Click **Next**.

  8. In the **Choose logs to include in sink** section, build an inclusion filter to select Neo4j Aura logs.

For Neo4j Aura logs forwarded from the log forwarding feature, use the following filter:
         
         resource.type="generic_node"
         resource.labels.namespace="neo4j-aura"
         

**Note:** The exact filter may vary depending on how Neo4j Aura labels the logs. You can use the **Logs Explorer** to preview logs and refine the filter. Go to **Logging > Logs Explorer** and search for Neo4j-related logs to identify the correct resource type and labels.
  9. Click **Next**.

  10. Review the sink configuration.

  11. Click **Create sink**.




## Verify log export to GCS

  1. Wait 2-3 hours for the first log entries to appear in the GCS bucket.
  2. In the **GCP Console** , go to **Cloud Storage > Buckets**.
  3. Click on your bucket name (for example, `neo4j-aura-logs`).
  4. Verify that log files are being created in the bucket.

Cloud Logging organizes logs in directory hierarchies by log type and date. The directory structure will be similar to:
         
         neo4j-aura-logs/
         ├── security.log/
         │   └── YYYY/
         │       └── MM/
         │           └── DD/
         │               └── HH:MM:SS_HH:MM:SS_S0.json
         └── query.log/
             └── YYYY/
                 └── MM/
                     └── DD/
                         └── HH:MM:SS_HH:MM:SS_S0.json
         




## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Neo4j Aura Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **NEO4J** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email is displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://neo4j-aura-logs/
           

Replace `neo4j-aura-logs` with your actual bucket name.

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `neo4j-aura-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:

     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.
  6. Click **Save**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
id2 | about.resource.attribute.labels | Labels for the resource attributes  
id3 | about.resource.attribute.labels |   
timestamp_msg | metadata.event_timestamp | Event timestamp  
event_type | metadata.event_type | Event type  
recordDate | principal.asset.creation_time | Asset creation time  
namespace | principal.domain.tech.product_object_id | Product object ID in the domain  
properties.host_group | principal.hostname | Source hostname  
msg | principal.process.command_line | Command line of the process  
user_id | principal.user.userid | User ID of the principal  
role | roles.name | Name of the role  
security_result | security_result | Security result details  
levelx | security_result.severity | Severity level  
levelx | security_result.severity_details | Detailed severity information  
properties.source | src.resource.name | Source resource name  
properties.cluster_node | target.hostname | Destination hostname  
database | target.resource.name | Target resource name  
roles | target.user.attribute.roles | Roles associated with the target user  
user_dest | target.user.userid | User ID of the target  
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/neo4j-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
