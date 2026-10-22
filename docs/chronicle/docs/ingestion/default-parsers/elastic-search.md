---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-search/
title: Collect Elasticsearch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:55.806630+00:00
---

# Collect Elasticsearch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Elasticsearch logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Elasticsearch logs to Google Security Operations using Amazon S3. The parser transforms raw JSON formatted logs into a unified data model (UDM). It extracts fields from nested JSON structures, maps them to UDM fields, and enriches the data with security-relevant context like severity levels and user roles.

## Before you begin

  * A Google SecOps instance
  * Privileged access to **Elasticsearch** cluster administration
  * Privileged access to **AWS** (S3, IAM, EC2)
  * EC2 instance or persistent host to run Logstash



## Get Elasticsearch prerequisites

  1. Sign in to your **Elasticsearch cluster** as an administrator.
  2. Verify that your Elasticsearch subscription includes **Security features** (required for audit logging).
  3. Note your Elasticsearch cluster name and version for reference.
  4. Identify the path where audit logs will be written (default: `$ES_HOME/logs/<clustername>_audit.json`).



## Enable Elasticsearch audit logging

  1. On each Elasticsearch node, edit the **elasticsearch.yml** configuration file.
  2. Add the following setting:
         
         xpack.security.audit.enabled: true
         

  3. Perform a **rolling restart** of the cluster to apply changes:

     * Disable shard allocation: `PUT _cluster/settings {"persistent": {"cluster.routing.allocation.enable": "primaries"}}`
     * Stop and restart each node one at a time.
     * Re-enable shard allocation: `PUT _cluster/settings {"persistent": {"cluster.routing.allocation.enable": null}}`
  4. Verify audit logs are being generated at `<clustername>_audit.json` in the logs directory.




## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `elastic-search-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add a description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure Logstash to ship audit logs to S3

  1. Install **Logstash** on an EC2 instance or persistent host that can access the Elasticsearch audit log files.
  2. Install the S3 output plugin if not already present:
         
         bin/logstash-plugin install logstash-output-s3
         

  3. Create a Logstash configuration file (`elastic-to-s3.conf`):
         
         input {
           file {
             path => "/path/to/elasticsearch/logs/*_audit.json"
             start_position => "beginning"
             codec => "json"              # audit file: 1 JSON object per line
             sincedb_path => "/var/lib/logstash/sincedb_elastic_search"
             exclude => ["*.gz"]
           }
         }
         
         filter {
           # Intentionally minimal: do NOT reshape audit JSON the ELASTIC_SEARCH parser expects.
           # If you must add metadata for ops, put it under [@metadata] so it won't be written.
           # ruby { code => "event.set('[@metadata][ingested_at]', Time.now.utc.iso8601)" }
         }
         
         output {
           s3 {
             access_key_id => "YOUR_AWS_ACCESS_KEY"
             secret_access_key => "YOUR_AWS_SECRET_KEY"
             region => "us-east-1"
             bucket => "elastic-search-logs"
             prefix => "logs/%{+YYYY}/%{+MM}/%{+dd}/"
         
             codec => "json_lines"        # NDJSON output (1 JSON object per line)
             encoding => "gzip"           # compress objects
         
             server_side_encryption => true
             # Optionally for KMS:
             # server_side_encryption_kms_key_id => "arn:aws:kms:REGION:ACCT:key/KEY_ID"
         
             size_file => 104857600       # 100MB rotation
             time_file => 300             # 5 min rotation
           }
         }
         

  4. Start Logstash with the configuration:
         
         bin/logstash -f elastic-to-s3.conf
         




## Optional: Create read-only IAM user for Google SecOps

  1. Go to **AWS Console > IAM > Users > Add users**.
  2. Click **Add users**.
  3. Provide the following configuration details: 
     * **User** : Enter `secops-reader`.
     * **Access type** : Select **Access key – Programmatic access**.
  4. Click **Create user**.
  5. Attach minimal read policy (custom): **Users > secops-reader > Permissions > Add permissions > Attach policies directly > Create policy**.
  6. In the JSON editor, enter the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::elastic-search-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::elastic-search-logs"
             }
           ]
         }
         

  7. Set the name to `secops-reader-policy`.

  8. Go to **Create policy > search/select > Next > Add permissions**.

  9. Go to **Security credentials > Access keys > Create access key**.

  10. Download the **CSV** (these values are entered into the feed).




## Configure a feed in Google SecOps to ingest Elasticsearch logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Elasticsearch Logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Elastic Search** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://elastic-search-logs/logs/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
Level | security_result.severity | The logic checks the value of the "Level" field and maps it to the corresponding UDM severity level:   
\- "INFO", "ALL", "OFF", "TRACE", "DEBUG" are mapped to "INFORMATIONAL".   
\- "WARN" is mapped to "LOW".   
\- "ERROR" is mapped to "ERROR".   
\- "FATAL" is mapped to "CRITICAL".  
message.@timestamp | timestamp | The timestamp is parsed from the "@timestamp" field within the "message" field of the raw log, using the format "yyyy-MM-ddTHH:mm:ss.SSS".  
message.action | security_result.action_details | Value is taken from the "action" field within the "message" field of the raw log.  
message.event.action | security_result.summary | Value is taken from the "event.action" field within the "message" field of the raw log.  
message.event.type | metadata.product_event_type | Value is taken from the "event.type" field within the "message" field of the raw log.  
message.host.ip | target.ip | Value is taken from the "host.ip" field within the "message" field of the raw log.  
message.host.name | target.hostname | Value is taken from the "host.name" field within the "message" field of the raw log.  
message.indices | target.labels.value | Value is taken from the "indices" field within the "message" field of the raw log.  
message.mrId | target.hostname | Value is taken from the "mrId" field within the "message" field of the raw log.  
message.node.id | principal.asset.product_object_id | Value is taken from the "node.id" field within the "message" field of the raw log.  
message.node.name | target.asset.hostname | Value is taken from the "node.name" field within the "message" field of the raw log.  
message.origin.address | principal.ip | The IP address is extracted from the "origin.address" field within the "message" field of the raw log, by removing the port number.  
message.origin.type | principal.resource.resource_subtype | Value is taken from the "origin.type" field within the "message" field of the raw log.  
message.properties.host_group | principal.hostname | Value is taken from the "properties.host_group" field within the "message" field of the raw log.  
message.properties.host_group | target.group.group_display_name | Value is taken from the "properties.host_group" field within the "message" field of the raw log.  
message.request.id | target.resource.product_object_id | Value is taken from the "request.id" field within the "message" field of the raw log.  
message.request.name | target.resource.name | Value is taken from the "request.name" field within the "message" field of the raw log.  
message.user.name | principal.user.userid | Value is taken from the "user.name" field within the "message" field of the raw log.  
message.user.realm | principal.user.attribute.permissions.name | Value is taken from the "user.realm" field within the "message" field of the raw log.  
message.user.roles | about.user.attribute.roles.name | Value is taken from the "user.roles" field within the "message" field of the raw log.  
| metadata.event_type | Hardcoded value: "USER_RESOURCE_ACCESS"  
| metadata.log_type | Hardcoded value: "ELASTIC_SEARCH"  
| metadata.product_name | Hardcoded value: "ELASTICSEARCH"  
| metadata.vendor_name | Hardcoded value: "ELASTIC"  
| principal.port | The port number is extracted from the "origin.address" field within the "message" field of the raw log.  
| target.labels.key | Hardcoded value: "Indice"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-search-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
