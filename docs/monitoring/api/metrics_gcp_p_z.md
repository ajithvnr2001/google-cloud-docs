---
url: https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z/
title: Google Cloud metrics: P through Z \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:29.771363+00:00
---

# Google Cloud metrics: P through Z  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Google Cloud metrics: P through Z Stay organized with collections  Save and categorize content based on your preferences. 

These tables list the Google Cloud metric types whose service domain name begins with the letters `p` through `z`, such as `storage.googleapis.com`. For information about other metric types, see [Google Cloud metrics overview](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



**Cloud Endpoints** : APIs managed by Cloud Endpoints write [ `serviceruntime`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) metrics against the [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api) monitored-resource type.

**Note:** To monitor the availability of a service, create an uptime check. These checks create [`monitoring.googleapis.com/uptime_check/check_passed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed) metric data. Don't configure an alerting policy to track a metric type such as `compute.googleapis.com/instance/uptime` if your goal is to monitor the availability of a service. For information about why such alerting policies might not function as you expect, see [Uptime policy doesn't create expected alerts](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#use-uptime-check). For information about how to create an uptime check, see [Managing uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks).

## Google Cloud metrics

Metrics from [Google Cloud](https://docs.cloud.google.com/docs).

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### parallelstore

Metrics from [Parallelstore](https://docs.cloud.google.com/parallelstore/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `parallelstore.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`instance/available_capacity_bytes` BETA ** _(project)_**   
Available capacity in bytes   
`GAUGE`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Available storage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/export_data_bytes_count` BETA ** _(project)_**   
Export Data Bytes Count   
`DELTA`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Number of bytes exported._  
`instance/export_data_objects_count` BETA ** _(project)_**   
Export Data Objects Count   
`DELTA`, `INT64`, `1`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Number of objects exported._  
`instance/import_data_bytes_count` BETA ** _(project)_**   
Import Data Bytes Count   
`DELTA`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Number of bytes imported._  
`instance/import_data_objects_count` BETA ** _(project)_**   
Import Data Objects Count   
`DELTA`, `INT64`, `1`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Number of objects imported._  
`instance/instance_failure` BETA ** _(project)_**   
Parallelstore Instance failure   
`GAUGE`, `BOOL`, ``   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _When an instance is in a FAILED state, this metric will report True, otherwise False. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`instance/read_bytes_count` BETA ** _(project)_**   
Read byte count   
`DELTA`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Number of bytes read. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/read_ops_count` BETA ** _(project)_**   
Read operation count   
`DELTA`, `INT64`, `{operation}`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _The number of read/fetch RPC processed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/total_capacity_bytes` BETA ** _(project)_**   
Total capacity (bytes)   
`GAUGE`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _The total amount of usable storage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/transferred_byte_count` BETA ** _(project)_**   
(Deprecated) Transferred byte count   
`DELTA`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _(Deprecated) Number of bytes read or written. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operation_type`: Operation type, one of [fetch, update].   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/used_capacity_bytes` BETA ** _(project)_**   
Used capacity in bytes   
`GAUGE`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Used storage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/write_bytes_count` BETA ** _(project)_**   
Write byte count   
`DELTA`, `INT64`, `By`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _Number of bytes written. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
`instance/write_ops_count` BETA ** _(project)_**   
Write operation count   
`DELTA`, `INT64`, `{operation}`   
**[parallelstore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_parallelstore.googleapis.com/Instance)** |  _The number of write/update RPC processed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`rank`: Server ID within the System.   
`target`: The ID of the DAOS target on the server.   
  
### privateca

Metrics from [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `privateca.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`ca/cert/ca_cert_creation` GA ** _(project)_**   
CA certificate creation count   
`DELTA`, `INT64`, `1`   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _The number of certificates issued by a CA with CA:TRUE. Sampled every 60 seconds._  
`ca/cert/create_count` GA ** _(project)_**   
Certificate creation count   
`DELTA`, `INT64`, `1`   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _The number of certificates issued by a CA. Sampled every 60 seconds._  
`ca/cert/create_failure_count` GA ** _(project)_**   
Certificate creation CA policy error count   
`DELTA`, `INT64`, `1`   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _The number of certificate creation failures. Sampled every 60 seconds._   
`reason`: The failure reason, such as VALIDATION or POLICY.   
`error_detail`: The detailed reason that caused the failure.   
`ca/cert/create_request_count` GA ** _(project)_**   
Certificate creation request count   
`DELTA`, `INT64`, `1`   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _The number of certificate creation requests per CA. Sampled every 60 seconds._  
`ca/cert_chain_expiration` GA ** _(project)_**   
CA certificate chain expiration   
`GAUGE`, `INT64`, `s`   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _Time (in seconds) until each CA certificate parent expires. Sampled every 3600 seconds._   
`cert_subject_key_id`: Subject key ID (SKID) of the CA certificate.   
`ca/cert_expiration` GA ** _(project)_**   
CA certificate expiration   
`GAUGE`, `INT64`, `s`   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _Time (in seconds) until the CA certificate expires. Sampled every 3600 seconds._  
`ca/cert_revoked` GA ** _(project)_**   
CA revocation status   
`GAUGE`, `BOOL`, ``   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _The CA certificate has been revoked. Value is true when revoked. Sampled every 3600 seconds._   
`status`: REVOKED when the value is true. When false, possible values are NOT_REVOKED, or REVOCATION_STATUS_UNKNOWN if the CRL is inaccessible.   
`ca/resource_state` GA ** _(project)_**   
CA resource state   
`GAUGE`, `BOOL`, ``   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _State of the certificate authority. Value is true when enabled, false otherwise. Sampled every 3600 seconds._   
`state`: State of CA, such as "ENABLED" or "DISABLED".   
`gcs/bucket_issue` GA ** _(project)_**   
Cloud Storage bucket issue   
`GAUGE`, `BOOL`, ``   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _Errors for Cloud Storage buckets. Value is false when OK, true when there are issues. Sampled every 3600 seconds._   
`status`: Status of the Storage bucket, such as "OK", "PERMISSION_DENIED" or "DELETED".   
`kms/key_issue` GA ** _(project)_**   
Cloud KMS key issue   
`GAUGE`, `BOOL`, ``   
**[privateca.googleapis.com/CertificateAuthority](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority)** |  _Errors for Cloud KMS signing keys. Value is false when OK, true when there are issues. Sampled every 3600 seconds._   
`status`: Status of the KMS key, such as "OK", "PERMISSION_DENIED" or "DESTROYED".   
  
### pubsub

Metrics from [Pub/Sub](https://docs.cloud.google.com/pubsub/docs). For more information, see [Pub/Sub monitoring](https://docs.cloud.google.com/pubsub/docs/monitoring). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `pubsub.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`snapshot/backlog_bytes` GA ** _(project)_**   
Snapshot backlog bytes   
`GAUGE`, `INT64`, `By`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Total byte size of the messages retained in a snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`snapshot/backlog_bytes_by_region` GA ** _(project)_**   
Snapshot backlog bytes by region   
`GAUGE`, `INT64`, `By`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Total byte size of the messages retained in a snapshot, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`snapshot/config_updates_count` GA ** _(project)_**   
Snapshot configuration operations   
`DELTA`, `INT64`, `1`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Cumulative count of configuration operations, grouped by operation type and result. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`operation_type`: Type of operation performed.   
`snapshot/num_messages` GA ** _(project)_**   
Snapshot messages   
`GAUGE`, `INT64`, `1`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Number of messages retained in a snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`snapshot/num_messages_by_region` GA ** _(project)_**   
Snapshot messages by region   
`GAUGE`, `INT64`, `1`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Number of messages retained in a snapshot, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`snapshot/oldest_message_age` GA ** _(project)_**   
Oldest snapshot message age   
`GAUGE`, `INT64`, `s`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Age (in seconds) of the oldest message retained in a snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`snapshot/oldest_message_age_by_region` GA ** _(project)_**   
Oldest snapshot message age by region   
`GAUGE`, `INT64`, `s`   
**[pubsub_snapshot](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_snapshot)** |  _Age (in seconds) of the oldest message retained in a snapshot, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`subscription/ack_latencies` GA ** _(project)_**   
Ack latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Distribution of ack latencies in milliseconds. The ack latency is the time between when Cloud Pub/Sub sends a message to a subscriber client and when Cloud Pub/Sub receives an Acknowledge request for that message. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`delivery_type`: Delivery mechanism: push, pull or streaming pull.   
`subscription/ack_message_count` GA ** _(project)_**   
Ack message count   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of messages acknowledged by Acknowledge requests, grouped by delivery type. Dead-lettered messages may show up as pull acks. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`delivery_type`: Delivery mechanism: push, pull, streaming pull, or filter.   
`subscription/backlog_bytes` GA ** _(project)_**   
Backlog size   
`GAUGE`, `INT64`, `By`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Total byte size of the unacknowledged messages (a.k.a. backlog messages) in a subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/billable_bytes_by_region` GA ** _(project)_**   
Billable bytes by region   
`GAUGE`, `INT64`, `By`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Total byte size of the billable messages in a subscription, broken down by Cloud region and type. Please refer to https://cloud.google.com/pubsub/pricing#storage_costs to understand the pricing for retaining unacknowledged messages in subscriptions for more than 24 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`type`: The type of billable backlog (unacked messages or retained acked messages).   
`subscription/byte_cost` GA ** _(project)_**   
Subscription byte cost   
`DELTA`, `INT64`, `By`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative cost of operations, measured in bytes. This is used to measure quota utilization. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`operation_type`: Type of operation performed.   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/config_updates_count` GA ** _(project)_**   
Subscription configuration operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of configuration operations for each subscription, grouped by operation type and result. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`operation_type`: Type of operation performed.   
`subscription/dead_letter_message_count` GA ** _(project)_**   
Dead letter message count   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of messages published to dead letter topic, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/delivery_latency_health_score` GA ** _(project)_**   
Delivery latency health score   
`GAUGE`, `BOOL`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _A score that measures the health of a subscription over a 10 minute rolling window. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`criteria`: Criteria of the health score. Possible values are ack_latency, expired_ack_deadlines, nack_requests, seek_requests, and utilization.   
`subscription/exactly_once_warning_count` GA ** _(project)_**   
Exactly once delivery warning   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Count of instances (acks and modacks that may have failed) that may lead to message redeliveries. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`delivery_type`: Delivery mechanism: push, pull or streaming pull.   
`reason`: Cause of the possible redelivery.   
`operation_type`: Type of operation performed. One of [ack, modack].   
`subscription/expired_ack_deadlines_count` GA ** _(project)_**   
Expired ack deadlines count   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of messages whose ack deadline expired while the message was outstanding to a subscriber client. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`delivery_type`: Delivery mechanism: push, pull or streaming pull.   
`subscription/export_push_subscription_details` GA ** _(project)_**   
Export push subscription details   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Type and state of the export push subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`subscription_state`: State of the export push subscription.   
`subscription_type`: Export push subscription type.   
`subscription/message_transform_latencies` GA ** _(project)_**   
Subscription message transform latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Distribution of subscription message transform latencies in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: String representation of a status code such as 'ok', 'invalid_argument', or 'unavailable'.   
`filtered`: (BOOL) Whether or not the message transform resulted in a filtered message.   
`subscription/mod_ack_deadline_message_count` GA ** _(project)_**   
Mod ack deadline message count   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of messages whose deadline was updated by ModifyAckDeadline requests, grouped by delivery type. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`delivery_type`: Delivery mechanism: push, pull or streaming pull.   
`subscription/mod_ack_deadline_message_operation_count` DEPRECATED ** _(project)_**   
ModifyAckDeadline message operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of ModifyAckDeadline message operations, grouped by result. This metric is deprecated. Use subscription/mod_ack_deadline_request_count instead. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/mod_ack_deadline_request_count` GA ** _(project)_**   
ModifyAckDeadline requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of ModifyAckDeadline requests, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/mod_ack_latencies` GA ** _(project)_**   
ModAck latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Distribution of ModAck latencies. For each message delivery attempt, the ModAck latency is the duration between when the CPS service delivers the message to a subscriber client and when the CPS service receives a ModAck request for that message (note that this means this metric may be recorded multiple times per delivery attempt). If this metric is growing, it indicates that the subscriber is repeatedly extending the acknowledgement deadline for a message (i.e., it is holding on to that message). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`delivery_type`: Delivery mechanism, one of [push, pull, streaming pull].   
`subscription/nack_requests` GA ** _(project)_**   
Nack requests   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of messages that were nacked. One message nacked multiple times will be counted multiple times. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`delivery_type`: Delivery mechanism: push, pull or streaming pull.   
`subscription/num_outstanding_messages` GA ** _(project)_**   
Outstanding push messages   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Number of messages delivered to a subscription's push endpoint, but not yet acknowledged. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`subscription/num_retained_acked_messages` GA ** _(project)_**   
Retained acked messages   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Number of acknowledged messages retained in a subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/num_retained_acked_messages_by_region` GA ** _(project)_**   
Retained acked messages by region   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Number of acknowledged messages retained in a subscription, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`subscription/num_unacked_messages_by_region` GA ** _(project)_**   
Unacked messages by region   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Number of unacknowledged messages in a subscription, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`subscription/num_undelivered_messages` GA ** _(project)_**   
Unacked messages   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Number of unacknowledged messages (a.k.a. backlog messages) in a subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/oldest_retained_acked_message_age` GA ** _(project)_**   
Oldest retained acked message age   
`GAUGE`, `INT64`, `s`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Age (in seconds) of the oldest acknowledged message retained in a subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/oldest_retained_acked_message_age_by_region` GA ** _(project)_**   
Oldest retained acked message age by region   
`GAUGE`, `INT64`, `s`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Age (in seconds) of the oldest acknowledged message retained in a subscription, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`subscription/oldest_unacked_message_age` GA ** _(project)_**   
Oldest unacked message age   
`GAUGE`, `INT64`, `s`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Age (in seconds) of the oldest unacknowledged message (a.k.a. backlog message) in a subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/oldest_unacked_message_age_by_region` GA ** _(project)_**   
Oldest unacked message age by region   
`GAUGE`, `INT64`, `s`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Age (in seconds) of the oldest unacknowledged message in a subscription, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`subscription/open_streaming_pulls` GA ** _(project)_**   
Number of open streaming pulls   
`GAUGE`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Number of open StreamingPull streams per subscription, grouped by status. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Status of the stream. For example, 'ok', 'suspended_subscriber_quota_exceeded' when subscriber throughput quota limits are exceeded, 'suspended_client_flow_controlled' when flow control is initiated by the client, 'suspended_max_outstanding_bytes_exceeded' when the maximum number of outstanding bytes is exceeded, or 'suspended_max_outstanding_messages_exceeded' when the maximum number of outstanding messages is exceeded.   
`subscription/pull_ack_message_operation_count` DEPRECATED ** _(project)_**   
Acknowledge message operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of acknowledge message operations, grouped by result. This metric is deprecated. Use subscription/pull_ack_request_count instead. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/pull_ack_request_count` GA ** _(project)_**   
Acknowledge requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of acknowledge requests, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/pull_message_operation_count` DEPRECATED ** _(project)_**   
Pull operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of pull message operations, grouped by result. This metric is deprecated. Use subscription/pull_request_count instead. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/pull_request_count` GA ** _(project)_**   
Pull requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of pull requests, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/push_request_count` GA ** _(project)_**   
Push requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of push attempts, grouped by result. Unlike pulls, the push server implementation does not batch user messages. So each request only contains one user message. The push server retries on errors, so a given user message can appear multiple times. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_class`: A classification group for the response code. It can be one of ['ack', 'deadline_exceeded', 'internal', 'invalid', 'remote_server_4xx', 'remote_server_5xx', 'unreachable'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`delivery_type`: Push delivery mechanism.   
`subscription/push_request_latencies` GA ** _(project)_**   
Push latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Distribution of push request latencies (in microseconds), grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`delivery_type`: Push delivery mechanism.   
`subscription/retained_acked_bytes` GA ** _(project)_**   
Retained acked bytes   
`GAUGE`, `INT64`, `By`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Total byte size of the acknowledged messages retained in a subscription. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/retained_acked_bytes_by_region` GA ** _(project)_**   
Retained acked bytes by region   
`GAUGE`, `INT64`, `By`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Total byte size of the acknowledged messages retained in a subscription, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`subscription/seek_request_count` GA ** _(project)_**   
Seek requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of seek attempts, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`subscription/sent_message_count` GA ** _(project)_**   
Sent message count   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of messages sent by Cloud Pub/Sub to subscriber clients, grouped by delivery type. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`delivery_type`: Delivery mechanism: push, pull or streaming pull.   
`subscription/streaming_pull_ack_message_operation_count` DEPRECATED ** _(project)_**   
StreamingPull Acknowledge message operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of StreamingPull acknowledge message operations, grouped by result. This metric is deprecated. Use subscription/streaming_pull_ack_request_count instead. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'unavailable').   
`subscription/streaming_pull_ack_request_count` GA ** _(project)_**   
StreamingPull Acknowledge requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of streaming pull requests with non-empty acknowledge ids, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'unavailable').   
`subscription/streaming_pull_message_operation_count` DEPRECATED ** _(project)_**   
StreamingPull message operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of streaming pull message operations, grouped by result. This metric is deprecated. Use subscription/streaming_pull_response_count instead. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'unavailable').   
`subscription/streaming_pull_mod_ack_deadline_message_operation_count` DEPRECATED ** _(project)_**   
StreamingPull ModifyAckDeadline message operations   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of StreamingPull ModifyAckDeadline operations, grouped by result. This metric is deprecated. Use subscription/streaming_pull_mod_ack_deadline_request_count instead. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'unavailable').   
`subscription/streaming_pull_mod_ack_deadline_request_count` GA ** _(project)_**   
StreamingPull ModifyAckDeadline requests   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of streaming pull requests with non-empty ModifyAckDeadline fields, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'unavailable').   
`subscription/streaming_pull_response_count` GA ** _(project)_**   
StreamingPull responses   
`DELTA`, `INT64`, `1`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Cumulative count of streaming pull responses, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'unavailable').   
`subscription/unacked_bytes_by_region` GA ** _(project)_**   
Unacked bytes by region   
`GAUGE`, `INT64`, `By`   
**[pubsub_subscription](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_subscription)** |  _Total byte size of the unacknowledged messages in a subscription, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`topic/byte_cost` GA ** _(project)_**   
Topic byte cost   
`DELTA`, `INT64`, `By`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Cost of operations, measured in bytes. This is used to measure utilization for quotas. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`operation_type`: Type of operation performed.   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`topic/config_updates_count` GA ** _(project)_**   
Topic configuration operations   
`DELTA`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Cumulative count of configuration operations, grouped by operation type and result. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`operation_type`: Type of operation performed.   
`topic/ingestion_byte_count` GA ** _(project)_**   
Ingestion byte count   
`DELTA`, `INT64`, `By`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Byte count of ingested messages per ingestion source type and import partition (e.g. AWS Kinesis shard id). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`source_type`: Ingestion data source type.   
`source_name`: Ingestion data source name.   
`import_partition`: Import partition of the ingestion source, if applicable.   
`topic/ingestion_data_source_state` GA ** _(project)_**   
Ingestion data source state   
`GAUGE`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _State of the ingestion data source per ingestion source type. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`source_type`: Ingestion data source type.   
`source_name`: Ingestion data source name.   
`state`: State of the ingestion source.   
`topic/ingestion_failure_count` GA ** _(project)_**   
Ingestion failure count   
`DELTA`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Number of errors encountered when ingesting data per ingestion source type, source name, import partition, and reason for error. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`source_type`: Ingestion data source type.   
`source_name`: Ingestion data source name.   
`import_partition`: Import partition of the ingestion source, if applicable.   
`reason`: Reason for ingestion failure.   
`topic/ingestion_message_count` GA ** _(project)_**   
Ingestion message count   
`DELTA`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Number of ingested messages per ingestion source type and import partition (e.g. AWS Kinesis shard id). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`source_type`: Ingestion data source type.   
`source_name`: Ingestion data source name.   
`import_partition`: Import partition of the ingestion source, if applicable.   
`topic/message_sizes` GA ** _(project)_**   
Publish message size   
`DELTA`, `DISTRIBUTION`, `By`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Distribution of publish message sizes (in bytes). Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._  
`topic/message_transform_latencies` GA ** _(project)_**   
Topic message transform latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Distribution of topic message transform latencies in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: String representation of a status code such as 'ok', 'invalid_argument', or 'unavailable'.   
`filtered`: (BOOL) Whether or not the message transform resulted in a filtered message.   
`topic/num_retained_acked_messages_by_region` GA ** _(project)_**   
Retained acked messages by region   
`GAUGE`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Number of acknowledged messages retained across all subscriptions and snapshots attached to the topic, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`topic/num_retained_messages` GA ** _(project)_**   
Retained messages   
`GAUGE`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Number of messages retained in a topic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/num_unacked_messages_by_region` GA ** _(project)_**   
Unacked messages by region   
`GAUGE`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Number of unacknowledged messages across all subscriptions and snapshots attached to a topic, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`topic/oldest_retained_acked_message_age_by_region` GA ** _(project)_**   
Oldest retained acked message age by region   
`GAUGE`, `INT64`, `s`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Age (in seconds) of the oldest acknowledged message retained across all subscriptions and snapshots attached to a topic, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`topic/oldest_retained_message_age` GA ** _(project)_**   
Oldest retained message age   
`GAUGE`, `INT64`, `s`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Age (in seconds) of the oldest message retained in a topic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/oldest_unacked_message_age_by_region` GA ** _(project)_**   
Oldest unacked message age by region   
`GAUGE`, `INT64`, `s`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Age (in seconds) of the oldest unacknowledged message across all subscriptions and snapshots attached to a topic, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`topic/retained_acked_bytes_by_region` GA ** _(project)_**   
Retained acked bytes by region   
`GAUGE`, `INT64`, `By`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Total byte size of the acknowledged messages retained across all subscriptions and snapshots attached to a topic, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
`topic/retained_bytes` GA ** _(project)_**   
Retained bytes   
`GAUGE`, `INT64`, `By`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Total byte size of the messages retained in a topic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/schema_validation_latencies` GA ** _(project)_**   
Schema validation latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Distribution of schema validation latencies in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`schema_name_with_revision_id`: The schema name with revision id such as 'my-schema@0a0b0c0d' - on success, or 'my-schema@unknown' - on failure).   
`status`: String representation of a status code such as 'ok', 'invalid_argument', or 'unavailable'.   
`topic/send_message_operation_count` DEPRECATED ** _(project)_**   
Publish message operations   
`DELTA`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Cumulative count of publish message operations, grouped by result. This metric is deprecated. Apply a count aggregator on topic/message_sizes instead. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`topic/send_request_count` GA ** _(project)_**   
Publish requests   
`DELTA`, `INT64`, `1`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Cumulative count of publish requests, grouped by result. Sampled every 60 seconds. After sampling, data is not visible for up to 181 seconds._   
`response_class`: A classification group for the response code. It can be one of ['success', 'invalid', 'internal'].   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'success', 'not_found', 'unavailable').   
`topic/send_request_latencies` GA ** _(project)_**   
Publish request latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Distribution of publish request latencies in microseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code, for example, 'success', 'not_found', 'unavailable').   
`has_ordering`: (BOOL) Whether or not the publish contained ordering keys.   
`schema_type`: The schema type associated with the topic, one of ['proto','avro', none]   
`topic/unacked_bytes_by_region` GA ** _(project)_**   
Unacked bytes by region   
`GAUGE`, `INT64`, `By`   
**[pubsub_topic](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsub_topic)** |  _Total byte size of the unacknowledged messages across all subscriptions and snapshots attached to the topic, broken down by Cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The Cloud region in which messages are persisted.   
  
### pubsublite

Metrics from [Pub/Sub Lite](https://docs.cloud.google.com/pubsub/lite/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `pubsublite.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`reservation/throughput_capacity/limit` BETA ** _(project)_**   
Reservation throughput capacity limit   
`GAUGE`, `INT64`, `1`   
**[pubsublite_reservation](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_reservation)** |  _The current configured throughput capacity of this reservation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`reservation/throughput_capacity/usage` BETA ** _(project)_**   
Reservation throughput capacity usage   
`DELTA`, `DOUBLE`, `1`   
**[pubsublite_reservation](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_reservation)** |  _Usage of reservation throughput capacity by kind of usage. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`kind`: Usage kind, one of ["ZONAL_PUBLISH" - publishing to zonal topics; "ZONAL_SUBSCRIBE" - subscribing to zonal topics].   
`reservation/throughput_capacity/utilization` BETA ** _(project)_**   
Reservation throughput capacity utilization ratio   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[pubsublite_reservation](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_reservation)** |  _The ratio of the rate of throughput capacity usage to available throughput capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`kind`: Usage kind, one of ["ZONAL_PUBLISH" - publishing to zonal topics; "ZONAL_SUBSCRIBE" - subscribing to zonal topics].   
`subscription/backlog_message_count` GA ** _(project)_**   
Backlog message count   
`GAUGE`, `INT64`, `1`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Total number of the unacknowledged messages (a.k.a. backlog messages) for a subscription in a given topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/backlog_quota_bytes` GA ** _(project)_**   
Backlog quota bytes   
`GAUGE`, `INT64`, `By`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Total quota byte size of the unacknowledged messages (a.k.a. backlog messages) for a subscription in a given topic partition.. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/export_status` BETA ** _(project)_**   
Subscription export status   
`GAUGE`, `BOOL`, ``   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _The status of an export subscription in a given topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Status of the export, such as "ACTIVE", "PAUSED", "NOT_FOUND" or "PERMISSION_DENIED".   
`subscription/flow_control_status` BETA ** _(project)_**   
Subscription flow control   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Fraction of time spent in each flow control state. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`state`: Flow control state, one of ["NO_CLIENT_TOKENS" - indicates that the per-partition limit of outstanding bytes or messages has been reached; "NO_PARTITION_CAPACITY" - indicates that the per-partition subscribe throughput limit has been reached; "NO_RESERVATION_CAPACITY" - indicates that the per-reservation throughput limit has been reached; "NOT_FLOW_CONTROLLED" - indicates that the subscriber is not flow-controlled].   
`subscription/oldest_unacked_message_age` GA ** _(project)_**   
Oldest unacked message age   
`GAUGE`, `INT64`, `s`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Age (in seconds) of the oldest unacknowledged message retained for a subscription in a given topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`subscription/sent_message_count` GA ** _(project)_**   
Subscription sent message count   
`DELTA`, `INT64`, `1`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Count of messages sent to subscribers for a subscription in a given topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`subscription/sent_quota_bytes` GA ** _(project)_**   
Subscription sent quota bytes   
`DELTA`, `INT64`, `By`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Quota byte size of messages sent to subscribers for a subscription in a given topic partition. See https://cloud.google.com/pubsub/lite/quotas#resource_quotas for quota byte calculation. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`subscription/sent_raw_bytes` GA ** _(project)_**   
Subscription sent raw bytes   
`DELTA`, `INT64`, `By`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Byte size of messages sent to subscribers for a subscription in a given topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`subscription/unexportable_message_count` BETA ** _(project)_**   
Subscription unexportable message count   
`DELTA`, `INT64`, `1`   
**[pubsublite_subscription_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_subscription_partition)** |  _Count of messages that cannot be exported to the destination for an export subscription in a given topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`reason`: Reason why a message is unexportable, one of ["INCOMPATIBLE" - violates constraints of the export destination; "OVERSIZED" - exceeds size limits for the export destination].   
`topic/flow_control_status` BETA ** _(project)_**   
Topic publish flow control   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Fraction of time spent in each flow control state. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`state`: Flow control state, one of ["NO_PARTITION_CAPACITY" - indicates that the per-partition subscribe throughput limit has been reached; "NO_RESERVATION_CAPACITY" - indicates that the per-reservation throughput limit has been reached; "NOT_FLOW_CONTROLLED" - indicates that the subscriber is not flow-controlled].   
`topic/oldest_retained_message_age` GA ** _(project)_**   
Oldest retained message age   
`GAUGE`, `INT64`, `s`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Age (in seconds) of the oldest message retained in a topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/publish_message_count` GA ** _(project)_**   
Publish message count   
`DELTA`, `INT64`, `1`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Count of messages published to a topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`topic/publish_quota_byte_limit` GA ** _(project)_**   
Publish quota byte limit   
`GAUGE`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The maximum number of message bytes that can be published per second per topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/publish_quota_bytes` GA ** _(project)_**   
Publish quota bytes   
`DELTA`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Quota byte size of messages published to a topic partition. See https://cloud.google.com/pubsub/lite/quotas#resource_quotas for quota byte calculation. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`topic/publish_quota_utilization` GA ** _(project)_**   
Publish quota utilization ratio   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The ratio of the rate of message quota bytes that are being published to a partition to the rate that can be published per topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`topic/publish_raw_bytes` GA ** _(project)_**   
Publish raw bytes   
`DELTA`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Byte size of messages published to a topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`topic/publish_request_count` GA ** _(project)_**   
Publish request count   
`DELTA`, `INT64`, `1`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Count of publish requests sent to a topic partition, broken down by response code. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: Operation response code string, derived as a string representation of a status code (e.g., 'OK', 'NOT_FOUND', 'UNAVAILABLE').   
`topic/sent_quota_bytes` GA ** _(project)_**   
Topic sent quota bytes   
`DELTA`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _Quota byte size of messages sent to subscribers for a topic partition. See https://cloud.google.com/pubsub/lite/quotas#resource_quotas for quota byte calculation. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`topic/storage_quota_byte_limit` GA ** _(project)_**   
Storage quota byte limit   
`GAUGE`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The quota byte limit for message storage in a topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/storage_quota_bytes` GA ** _(project)_**   
Storage quota bytes   
`GAUGE`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The current quota bytes of messages stored in a topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/storage_quota_utilization` GA ** _(project)_**   
Storage quota utilization ratio   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The ratio of the number of message quota bytes that are stored in a partition to the provisioned bytes that can be stored per topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/subscribe_quota_byte_limit` GA ** _(project)_**   
Subscribe quota byte limit   
`GAUGE`, `INT64`, `By`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The maximum number of message bytes that can be received by subscribers per second per topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic/subscribe_quota_utilization` GA ** _(project)_**   
Subscribe quota utilization ratio   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[pubsublite_topic_partition](https://docs.cloud.google.com/monitoring/api/resources#tag_pubsublite_topic_partition)** |  _The ratio of the rate of message quota bytes that are sent to subscribers for a partition to the rate that can be received per topic partition. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
  
### recaptchaenterprise

Metrics from [reCAPTCHA](https://docs.cloud.google.com/recaptcha-enterprise/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `recaptchaenterprise.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`account_defender_assessment_count` GA ** _(project)_**   
Account Defender assessments   
`DELTA`, `INT64`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Count of Account Defender assessments. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`label`: The Account Defender label returned in the assessment, one of ["profile_match"; "suspicious_login_activity"; "suspicious_account_creation"; "related_accounts_number_high"; "" - empty string when no label is returned in the assessment].   
`assessment_count` GA ** _(project)_**   
Token assessments   
`DELTA`, `INT64`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Total count of token assessments. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`token_status`: Token assessment outcome. "valid" for valid token assessments, otherwise an InvalidReason will be given. One of [valid, invalid_reason_unspecified, unknown_invalid_reason, malformed, expired, dupe, missing, browser_error, unexpected_action, key_mismatch, domain_mismatch].   
`assessments` GA ** _(project)_**   
Assessment request scores   
`DELTA`, `DISTRIBUTION`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Distribution of real-time assessment request scores for valid tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`action`: Action name provided at token generation.   
`platform`: Client platform: "web", "android", or "ios".   
`challenge`: For CHECKBOX or INVISIBLE keys, "challenge" or "nocaptcha".   
`executes` GA ** _(project)_**   
Execute request scores   
`DELTA`, `DISTRIBUTION`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Distribution of execute request scores. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`action`: Action name provided at token generation.   
`platform`: Client platform. Examples include: "firefox", "ios".   
`express_assessments` GA ** _(project)_**   
Express Assessment request scores   
`DELTA`, `DISTRIBUTION`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Distribution of real-time express assessment request scores. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`sms_toll_fraud_risks` GA ** _(project)_**   
SMS toll fraud risks   
`DELTA`, `DISTRIBUTION`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Distribution of SMS toll fraud risks. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`country_calling_code`: The ITU E.164 country calling code for the phone number.   
`solution_count` GA ** _(project)_**   
Captcha solution results   
`DELTA`, `INT64`, `1`   
**[recaptchaenterprise.googleapis.com/Key](https://docs.cloud.google.com/monitoring/api/resources#tag_recaptchaenterprise.googleapis.com/Key)** |  _Counts of captcha solutions. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`challenge`: Challenge result: "pass", "fail", or "nocaptcha".   
`platform`: Client platform. Examples include: "firefox", "ios".   
  
### recommendationengine

Metrics from [Recommendations](https://docs.cloud.google.com/retail/docs). Launch stages of these metrics: EARLY_ACCESS

The "metric type" strings in this table must be prefixed with `recommendationengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`event_store/processed_event_count` EARLY_ACCESS ** _(project)_**   
Recommendation Processed Event Count   
`DELTA`, `INT64`, `1`   
**[recommendationengine.googleapis.com/EventStore](https://docs.cloud.google.com/monitoring/api/resources#tag_recommendationengine.googleapis.com/EventStore)** |  _The count of processed user event in given event store. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`event_type`: Event type, see https://cloud.google.com/recommendations-ai/docs/user-events#user_event_types.   
`status`: Status of event, should be joined or unjoined.   
  
### redis

Metrics from [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `redis.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`clients/blocked` GA ** _(project)_**   
Blocked Clients   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of blocked clients. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`clients/connected` GA ** _(project)_**   
Connected Clients   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of client connections. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`cluster/backup/last_backup_duration` GA ** _(project)_**   
Last backup duration   
`GAUGE`, `INT64`, `ms`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The duration of the last backup operation as milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`cluster/backup/last_backup_size` GA ** _(project)_**   
Last backup size   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The size of the last backup in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`cluster/backup/last_backup_start_time` GA ** _(project)_**   
Last backup start time   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The start time of the last backup operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`cluster/backup/last_backup_status` GA ** _(project)_**   
Last backup status   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The status of the last backup operation as 1/0 (success/failure). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`cluster/clients/average_connected_clients` GA ** _(project)_**   
Client connections - average   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean current number of client connections across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/clients/maximum_connected_clients` GA ** _(project)_**   
Client connections - maximum   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum current number of client connections across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/clients/total_connected_clients` GA ** _(project)_**   
Client connections - total   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Current number of client connections to the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/commandstats/failed_calls_count` BETA ** _(project)_**   
Failed commands count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of failed Redis commands. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`cluster/commandstats/total_calls_count` GA ** _(project)_**   
Commands count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of Redis commands. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`cluster/commandstats/total_usec_count` GA ** _(project)_**   
Commands time   
`DELTA`, `INT64`, `us`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The total time consumed per command. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`cluster/cpu/average_utilization` GA ** _(project)_**   
CPU utilization - average   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean CPU utilization across the cluster from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/cpu/maximum_utilization` GA ** _(project)_**   
CPU utilization - maximum   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum CPU utilization across the cluster from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/cross_cluster_replication/secondary_average_replication_offset_diff` GA ** _(project)_**   
Cross cluster replication average offset diff   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Average replication offset difference between primary shards and secondary shards. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`secondary_cluster_project_number`: Secondary cluster project number.   
`secondary_cluster_location`: Secondary cluster location.   
`secondary_cluster_id`: Secondary cluster Id.   
`secondary_cluster_uid`: Secondary cluster uid.   
`cluster/cross_cluster_replication/secondary_maximum_replication_offset_diff` GA ** _(project)_**   
Cross cluster replication maximum offset diff   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum replication offset difference between primary shards and secondary shards. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`secondary_cluster_project_number`: Secondary cluster project number.   
`secondary_cluster_location`: Secondary cluster location.   
`secondary_cluster_id`: Secondary cluster Id.   
`secondary_cluster_uid`: Secondary cluster uid.   
`cluster/cross_cluster_replication/secondary_replication_links` GA ** _(project)_**   
Cross cluster replication links   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Number of replication links between a primary cluster and a secondary cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`secondary_cluster_project_number`: Secondary cluster project number.   
`secondary_cluster_location`: Secondary cluster location.   
`secondary_cluster_id`: Secondary cluster Id.   
`secondary_cluster_uid`: Secondary cluster uid.   
`cluster/import/last_import_duration` GA ** _(project)_**   
Last import duration   
`GAUGE`, `INT64`, `ms`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The duration of the last import operation as milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`import_type`: The type of the import, one of [CREATE_IMPORT, LIVE_IMPORT].   
`import_source`: The source of the import, one of [MANAGED_BACKUP, GCS_SOURCE].   
`cluster/import/last_import_start_time` GA ** _(project)_**   
Last import start time   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The start time of the last import operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`import_type`: The type of the import, one of [CREATE_IMPORT, LIVE_IMPORT].   
`import_source`: The source of the import, one of [MANAGED_BACKUP, GCS_SOURCE].   
`cluster/keyspace/total_keys` GA ** _(project)_**   
Total keys   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Number of keys stored in the cluster instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/memory/average_utilization` GA ** _(project)_**   
Memory utilization - average   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean memory utilization across the cluster from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/memory/maximum_utilization` GA ** _(project)_**   
Memory utilization - maximum   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum memory utilization across the cluster from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/memory/size` GA ** _(project)_**   
Memory size   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Memory size of the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/memory/total_used_memory` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Total memory usage of the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/node/clients/blocked_clients` GA ** _(project)_**   
Blocked connections   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of client connections blocked by the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/clients/connected_clients` GA ** _(project)_**   
Client connections   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of clients connected to the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/clients/maxclients` BETA ** _(project)_**   
Max Clients Configuration   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Max clients configuration from redis conf. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/clients/recent_max_input_buffer` BETA ** _(project)_**   
Max input buffer   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Max input buffer in bytes among current client connections. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/clients/recent_max_output_buffer` BETA ** _(project)_**   
Max output buffer   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Max output buffer in bytes among current client connections. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/clients/tracking_clients` BETA ** _(project)_**   
Tracking clients   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of clients that are being tracked by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/commandstats/calls_count` GA ** _(project)_**   
Commands count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of calls for this command on the cluster node in one minute. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`cluster/node/commandstats/failed_calls_count` BETA ** _(project)_**   
Failed command calls   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of failed calls for this command. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: Command of the call.   
`cluster/node/commandstats/rejected_calls_count` BETA ** _(project)_**   
Rejected command calls   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of rejected calls for this command. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: Command of the call.   
`cluster/node/commandstats/usec_count` GA ** _(project)_**   
Commands time   
`DELTA`, `INT64`, `us`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The total time consumed per command in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`cluster/node/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _CPU utilization for the cluster node from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`state`: CPU usage state, one of [sys, sys_children, sys_main_thread, user, user_children, user_main_thread]   
`cluster/node/cross_cluster_replication/follower_replication_offset_diff` GA ** _(project)_**   
Cross cluster replication follower offset diff   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Replication offset diff in bytes between a replicator node and its follower node, reported by the replicator node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`secondary_cluster_project_number`: Secondary cluster project number.   
`secondary_cluster_location`: Secondary cluster Id.   
`secondary_cluster_id`: Secondary cluster Id.   
`secondary_cluster_uid`: Secondary cluster uid.   
`follower_node_id`: Follower node Id.   
`cluster/node/cross_cluster_replication/role` GA ** _(project)_**   
Cross cluster replication role   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Cross cluster replication role of the node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`ccr_role`: Cross cluster replication role, one of [replicator, follower].   
`cluster/node/errorstats/errors_count` BETA ** _(project)_**   
Errors count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Different error counters for errors occurred within the engine. The engine field name is errorstat_XXX, XXX can be MOVED, ERR, OOM etc.. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`error_type`: The error type, e.g. NO_ERR, ERR, MOVED, ASK, OOM etc..   
`cluster/node/json/documents_count` GA ** _(project)_**   
JSON documents count   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of JSON documents in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/json/used_memory` GA ** _(project)_**   
JSON memory usage   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Memory consumed by JSON documents in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/keyspace/keys_with_expiration` BETA ** _(project)_**   
keys with an expiration   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of keys with an expiration. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/keyspace/total_keys` GA ** _(project)_**   
Total keys   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of keys stored in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/dataset_usage` BETA ** _(project)_**   
Memory used by dataset   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Actual dataset memory usage. The engine field name is used_memory_dataset. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/lua_usage` BETA ** _(project)_**   
Memory used by Lua engine   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of bytes used by the Lua engine. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/maxmemory` BETA ** _(project)_**   
Max memory   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Maximum amount of memory redis can consume, 0 means ram capping is disabled. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/maxmemory_policy` BETA ** _(project)_**   
Maxmemory policy   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The maxmemory policy configuration on the node level. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`maxmemory_policy`: The maxmemory policy configuration on the node level.   
`cluster/node/memory/mem_not_counted_for_evict` BETA ** _(project)_**   
Memory not counted for eviction   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Used memory that's not counted for key eviction. This is basically a transient replica and AOF buffers. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/normal_clients_usage` BETA ** _(project)_**   
Memory Usage by normal clients   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of bytes used by normal clients. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/number_of_cached_scripts` BETA ** _(project)_**   
Number of cached scripts   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The number of EVAL scripts cached by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/number_of_functions` BETA ** _(project)_**   
Number of functions   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The number of functions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/peak_usage` BETA ** _(project)_**   
Peak memory usage   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Peak memory consumed by Redis ever (in bytes). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/replica_clients_usage` BETA ** _(project)_**   
Memory Usage by replica clients   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of bytes used by replica clients. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/rss_usage` BETA ** _(project)_**   
Usage rss   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of bytes that Redis allocated as seen by the operating system (a.k.a resident set size). This is the number reported by tools such as top(1) and ps(1). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/scripts_usage` BETA ** _(project)_**   
Memory used by scripts   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of bytes overhead by the EVAL scripts and Function scripts (part of used memory). The engine field name is used_memory_scripts. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total memory usage of the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/memory/utilization` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Memory utilization within the cluster node from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_enabled` BETA ** _(project)_**   
AOF enabled   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Flag indicating if AOF is enabled. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_fsync_errors_count` GA ** _(project)_**   
AOF fsync errors count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of AOF fsync errors on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_fsync_lag` GA ** _(project)_**   
AOF fsync lag   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _AOF lag between memory and persistent store on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_last_bgrewrite_status` GA ** _(project)_**   
AOF last bgrewrite success   
`GAUGE`, `BOOL`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Indicates the success of the last AOF bgrewrite operation on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_string`: Status code description.   
`cluster/node/persistence/aof_last_cow_size` BETA ** _(project)_**   
Last AOF COW size   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The size in bytes of the copy-on-write memory during the last AOF rewrite operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_last_rewrite_time_sec` BETA ** _(project)_**   
Last AOF rewrite duration   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Duration of the last AOF rewrite operation in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_last_write_status` GA ** _(project)_**   
AOF last write success   
`GAUGE`, `BOOL`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Indicates the success of the last AOF write operation on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_string`: Status code description.   
`cluster/node/persistence/aof_rewrite_in_progress` BETA ** _(project)_**   
AOF rewrite in progress   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Flag indicating if an AOF rewrite is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/aof_rewrites_count` GA ** _(project)_**   
AOF rewrites count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _AOF rewrites count on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_code`: (INT64) gRPC error code (e.g. 0=OK, 8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`cluster/node/persistence/async_loading` BETA ** _(project)_**   
Async loading   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Flag indicating if async loading is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/auto_restore_count` GA ** _(project)_**   
Auto restore count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of restores from dumpfile on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_code`: (INT64) gRPC error code (e.g. 0=OK, 13=INTERNAL)   
`status_string`: Status code description.   
`persistence_mode`: "AOF" or "RDB".   
`cluster/node/persistence/current_cow_peak` BETA ** _(project)_**   
Current COW peak   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Peak size in bytes of the copy-on-write memory during the current fork operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/current_cow_size` BETA ** _(project)_**   
Current COW size   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The size in bytes of the copy-on-write memory during the current fork operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/current_fork_percentage` BETA ** _(project)_**   
Current fork percentage   
`GAUGE`, `DOUBLE`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The percentage of the current fork operation progress (0-100). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/current_save_keys_total` GA ** _(project)_**   
Keys in current save   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of keys at the beginning of the current save operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/loading` BETA ** _(project)_**   
Loading   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Flag indicating if loading is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/rdb_bgsave_in_progress` GA ** _(project)_**   
RDB BGSAVE in progress   
`GAUGE`, `BOOL`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Indicates if a RDB BGSAVE is currently in progress on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/rdb_last_bgsave_status` GA ** _(project)_**   
RDB last BGSAVE success   
`GAUGE`, `BOOL`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Indicates the success of the last BGSAVE on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_string`: Status code description.   
`cluster/node/persistence/rdb_last_bgsave_time_sec` BETA ** _(project)_**   
Last BGSAVE duration   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Duration of the last RDB save operation in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/rdb_last_cow_size` BETA ** _(project)_**   
Last RDB COW size   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The size in bytes of the copy-on-write memory during the last RDB save operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/rdb_last_save_age` GA ** _(project)_**   
RDB last save age   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Measures the time in seconds, since the last successful snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/rdb_next_save_time_until` GA ** _(project)_**   
Time until next RDB snapshot   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Measures the time in seconds, remaining until the next snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/persistence/rdb_saves_count` GA ** _(project)_**   
RDB saves count.   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of RDB saves in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_code`: (INT64) gRPC error code (e.g. 0=OK, 8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`cluster/node/replication/offset` GA ** _(project)_**   
Replication offset   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Measures the replication offset bytes of the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/replication/primary_sync_in_progress` BETA ** _(project)_**   
Primary sync in progress   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Flag indicating if a primary syncing to replica is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/replication/sync_full_count` BETA ** _(project)_**   
Full Resync Count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The total number of full resyncs with replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/replication/sync_partial_err_count` BETA ** _(project)_**   
Partial sync Error count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The number of denied partial resync requests. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/replication/sync_partial_ok_count` BETA ** _(project)_**   
Partial sync OK count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The number of accepted partial resync requests. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/server/healthy` GA ** _(project)_**   
Cluster node is healthy   
`GAUGE`, `BOOL`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Indicates if Cluster Node is healthy and available. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/server/uptime` GA ** _(project)_**   
Node uptime   
`GAUGE`, `INT64`, `s`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Measures the uptime of the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/acl_access_denied_auths_count` BETA ** _(project)_**   
ACL access denied authentications   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of ACL access denied authentication failures. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/acl_access_denied_channels_count` BETA ** _(project)_**   
ACL access denied channels count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of failed attempts by users to access channels they do not have permission to access. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/acl_access_denied_commands_count` BETA ** _(project)_**   
ACL access denied commands count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of failed attempts by users to run commands they don’t have permission to call. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/acl_access_denied_keys_count` BETA ** _(project)_**   
ACL access denied keys count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of failed attempts by users to access keys they don’t have permission to access. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/connections_received_count` GA ** _(project)_**   
Client connections - received   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of total client connections created in the last one minute on the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/evicted_clients_count` BETA ** _(project)_**   
Evicted client connections   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of client connections evicted due to client memory over eviction limit. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/evicted_keys_count` GA ** _(project)_**   
Evicted keys   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of evicted keys by the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/expire_cycle_cpu_millisecond_count` BETA ** _(project)_**   
Expire cycle cpu milliseconds   
`DELTA`, `INT64`, `ms`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The total cumulative amount of time spent on active expiry cycles. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/expired_keys_count` GA ** _(project)_**   
Expired keys   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of key expiration events in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/expired_keys_percentage` BETA ** _(project)_**   
Expired stale key percentage   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The percentage of keys probably expired. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/expired_time_cap_reached_count` BETA ** _(project)_**   
Expired time cap reached count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _The total count of times that active expiry cycles have stopped early. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/keyspace_hits_count` GA ** _(project)_**   
Keyspace hits   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of successful lookup of keys in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/keyspace_misses_count` GA ** _(project)_**   
Keyspace misses   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of failed lookup of keys in the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/latest_fork_usec` BETA ** _(project)_**   
Latest fork operation   
`GAUGE`, `INT64`, `us`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Duration of the latest fork operation in microseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/net_input_bytes_count` GA ** _(project)_**   
Network bytes - incoming   
`DELTA`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of incoming network bytes received by the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/net_output_bytes_count` GA ** _(project)_**   
Network bytes - outgoing   
`DELTA`, `INT64`, `By`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Count of outgoing network bytes sent from the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/pubsub_channels` BETA ** _(project)_**   
Pub/Sub channels   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Global number of pub/sub channels with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/pubsub_patterns` BETA ** _(project)_**   
Pub/Sub patterns   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Global number of pub/sub patterns with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/pubsubshard_channels` BETA ** _(project)_**   
Pub/Sub shard channels   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Global number of pub/sub shard channels with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/rejected_connections_count` GA ** _(project)_**   
Client connections - rejected   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of connections rejected because of maxclients limit by the cluster node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/total_fork_count` BETA ** _(project)_**   
Total fork count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Total number of forks since server start. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/tracking_total_items` BETA ** _(project)_**   
Tracking total items   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of items (Sum of clients per key) being tracked by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/tracking_total_keys` BETA ** _(project)_**   
Tracking total keys   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of keys being tracked by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/stats/tracking_total_prefixes` BETA ** _(project)_**   
Tracking total prefixes   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _Number of tracked prefixes in server prefix table. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/node/vm/memory/utilization` BETA ** _(project)_**   
VM memory utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[redis.googleapis.com/ClusterNode](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/ClusterNode)** |  _VM memory utilization for the cluster node from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/persistence/aof_fsync_lags` GA ** _(project)_**   
AOF fsync lags.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Distribution of AOF lag between memory and persistent store across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/persistence/aof_rewrite_count` GA ** _(project)_**   
AOF rewrite count.   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of AOF rewrites across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_code`: (INT64) gRPC error code (e.g. 0=OK,8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`cluster/persistence/rdb_last_success_ages` GA ** _(project)_**   
RDB snapshot ages.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Age of RDB snapshots across cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/persistence/rdb_saves_count` GA ** _(project)_**   
RDB saves count.   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of RDB saves across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_code`: (INT64) gRPC error code (e.g. 0=OK,8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`cluster/replication/average_ack_lag` GA ** _(project)_**   
Replication acknowledge lag - average   
`GAUGE`, `DOUBLE`, `s`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean replication acknowledge lag (in seconds) of replica across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/replication/average_offset_diff` GA ** _(project)_**   
Replication offset diff - average   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean replication offset diff (in bytes) across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/replication/maximum_ack_lag` GA ** _(project)_**   
Replication acknowledge lag - maximum   
`GAUGE`, `DOUBLE`, `s`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum replication acknowledge lag (in seconds) of replica across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/replication/maximum_offset_diff` GA ** _(project)_**   
Replication offset diff - maximum   
`GAUGE`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum replication offset diff (in bytes) across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/attributes` GA ** _(project)_**   
Vector search attributes   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The number of attributes across all indexes for vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/average_used_memory_bytes` GA ** _(project)_**   
Vector search average used memory   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The average per-node used memory for all search functionality, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/background_indexing_in_progress` GA ** _(project)_**   
Vector search background indexing in progress   
`GAUGE`, `BOOL`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Indicates if the background indexing is in progress across any index. When the metric value is true, background indexing is in progress in at least one index. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/indexed_keys` GA ** _(project)_**   
Vector search indexed keys   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The number of keys indexed across all indexes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/indexes` GA ** _(project)_**   
Vector search indexes   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The number of indexes created for searching for vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/maximum_used_memory_bytes` GA ** _(project)_**   
Vector search maximum used memory   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The maximum per-node used memory for all search functionality, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/search/query_requests_count` GA ** _(project)_**   
Vector search query request count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The number of query requests across all indexes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status`: Success or failure of the query request. Possible values: "success", "failure".   
`role`: The replication role, one of [primary, replica].   
`cluster/search/total_used_memory_bytes` GA ** _(project)_**   
Vector search total used memory   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _The total used memory in bytes for all search functionality in all nodes, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/security/rotate_tls_cert_count` BETA ** _(project)_**   
TLS certificate rotation count   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of TLS certificate rotations on the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`status`: The status of the TLS certificate rotation.   
`failure_reason`: The failure reason of the TLS certificate rotation.   
`rotation_trigger_source`: The trigger source of the TLS certificate rotation.   
`cluster/stats/average_evicted_keys` GA ** _(project)_**   
Evicted keys - average   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean number of evicted keys due to memory capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/stats/average_expired_keys` GA ** _(project)_**   
Expired keys - average   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/stats/average_keyspace_hits` GA ** _(project)_**   
Keyspace hits - average   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean number of successful lookup of keys across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/average_keyspace_misses` GA ** _(project)_**   
Keyspace misses - average   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Mean number of failed lookup of keys across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/maximum_evicted_keys` GA ** _(project)_**   
Evicted keys - maximum   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum number of evicted keys due to memory capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/stats/maximum_expired_keys` GA ** _(project)_**   
Expired keys - maximum   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/stats/maximum_keyspace_hits` GA ** _(project)_**   
Keyspace hits - maximum   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum number of successful lookup of keys across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/maximum_keyspace_misses` GA ** _(project)_**   
Keyspace misses - maximum   
`GAUGE`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Maximum number of failed lookup of keys across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/total_connections_received_count` GA ** _(project)_**   
Client connections - received   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of client connections created in the last one minute. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/total_evicted_keys_count` GA ** _(project)_**   
Evicted keys - total   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Total number of evicted keys due to memory capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/stats/total_expired_keys_count` GA ** _(project)_**   
Expired keys - total   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Total number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/stats/total_keyspace_hits_count` GA ** _(project)_**   
Keyspace Hits - total   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Total number of successful lookup of keys across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/total_keyspace_misses_count` GA ** _(project)_**   
Keyspace misses - total   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Total number of failed lookup of keys across the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/total_net_input_bytes_count` GA ** _(project)_**   
Network bytes - incoming total   
`DELTA`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of incoming network bytes received by the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/total_net_output_bytes_count` GA ** _(project)_**   
Network bytes - outgoing total   
`DELTA`, `INT64`, `By`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of outgoing network bytes sent from the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`cluster/stats/total_rejected_connections_count` GA ** _(project)_**   
Client connections - rejected   
`DELTA`, `INT64`, `1`   
**[redis.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_redis.googleapis.com/Cluster)** |  _Count of client connections rejected because of maxclients limit. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`commands/calls` GA ** _(project)_**   
Calls   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Total number of calls for this command in one minute. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`cmd`: The command executed.   
`commands/total_time` GA ** _(project)_**   
Total Time of Calls   
`DELTA`, `INT64`, `us`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _The amount of time in microseconds that this command took in the last second. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`cmd`: The command executed.   
`commands/usec_per_call` GA ** _(project)_**   
Time per Call   
`GAUGE`, `DOUBLE`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Average time per call over 1 minute by command. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`cmd`: The command executed.   
`keyspace/avg_ttl` GA ** _(project)_**   
Average TTL   
`GAUGE`, `DOUBLE`, `ms`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Average TTL for keys in this database. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`db`: The index of the database, default of 0.   
`keyspace/keys` GA ** _(project)_**   
Keys   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of keys stored in this database. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`db`: The index of the database, default of 0.   
`keyspace/keys_with_expiration` GA ** _(project)_**   
Expirable Keys   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of keys with an expiration in this database. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`db`: The index of the database, default of 0.   
`persistence/rdb/bgsave_in_progress` GA ** _(project)_**   
Persisting RDB   
`GAUGE`, `BOOL`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Flag indicating a RDB save is on-going. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/enabled` GA ** _(project)_**   
Snapshot RDB mode enabled   
`GAUGE`, `BOOL`, ``   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates if the snapshot is in RDB mode. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/attempts_since_last_success` GA ** _(project)_**   
RDB recovery attempts   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates number of recovery attempts since the last successful recovery attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/elapsed_time` GA ** _(project)_**   
RDB recovery elapsed time   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates increasing time elapsed for an in-progress recovery from an RDB snapshot. 0 means the recovery is idle or completed. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/estimated_recovery_time` GA ** _(project)_**   
RDB recovery estimated time   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the expected recovery time when using the last successful snapshot for recovery. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/estimated_remaining_time` GA ** _(project)_**   
RDB recovery remaining time   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates remaining time to finish recovery from an RDB snapshot. 0 means the recovery is idle or completed. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/in_progress` GA ** _(project)_**   
RDB recovery in progress   
`GAUGE`, `BOOL`, ``   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates if recovery from an RDB snapshot is in progress. When the metric value is true, then a recovery is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/last_duration` GA ** _(project)_**   
RDB recovery last duration   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates time it took to restore the last snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/last_status` GA ** _(project)_**   
RDB recovery last status   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates status of the most recent recovery. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`message`: The message from the status of the last recovery.   
`rdb/recovery/loaded_bytes_count` GA ** _(project)_**   
RDB loaded size   
`DELTA`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _During a recovery, indicates how many bytes have loaded. 0 if the recovery is not active. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/recovery/total_bytes_count` GA ** _(project)_**   
RDB snapshot size   
`DELTA`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the size in bytes of the snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/snapshot/attempt_count` GA ** _(project)_**   
RDB snapshot attempts count   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates number of snapshot attempts every minute. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/snapshot/elapsed_time` GA ** _(project)_**   
RDB snapshot elapsed time   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates increasing time elapsed while creating the current snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/snapshot/in_progress` GA ** _(project)_**   
RDB snapshot in progress   
`GAUGE`, `BOOL`, ``   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates if RDB snapshot is in progress. When the metric value is true, then an RDB snapshot is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/snapshot/last_status` GA ** _(project)_**   
RDB snapshot last status   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates status of the most recent snapshot attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`message`: The message from the status of the last snapshot.   
`rdb/snapshot/last_success_age` GA ** _(project)_**   
RDB snapshot last success age   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates time elapsed since the start of the last successful snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/snapshot/last_success_duration` GA ** _(project)_**   
RDB snapshot last success duration   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the total time required to write the last successful snapshot, not including failed attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`rdb/snapshot/time_until_next_run` GA ** _(project)_**   
Next snapshot time   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Seconds until the next scheduled snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`replication/master/slaves/lag` GA ** _(project)_**   
Seconds lagging   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _The number of seconds that replica is lagging behind primary. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`slave`: The index of slave on a particular master.   
`replication/master/slaves/offset` GA ** _(project)_**   
Replication byte offset (Replica)   
`GAUGE`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _The number of bytes that have been acknowledged by replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`slave`: The index of slave on a particular master.   
`replication/master_repl_offset` GA ** _(project)_**   
Replication byte offset (Master)   
`GAUGE`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _The number of bytes that master has produced and sent to replicas. To be compared with replication byte offset of replica. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`replication/offset_diff` GA ** _(project)_**   
Bytes pending replication   
`GAUGE`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _The largest number of bytes that have not been replicated across all replicas. This is the biggest difference between replication byte offset (master) and replication byte offset (replica) of all replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`replication/role` GA ** _(project)_**   
Node Role   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Returns a value indicating the node role. 1 indicates primary and 0 indicates replica. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`search/attributes` GA ** _(project)_**   
Vector search attributes   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the number of attributes in vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`search/background_indexing_in_progress` GA ** _(project)_**   
Vector search background indexing in progress   
`GAUGE`, `BOOL`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates if the background indexing is in progress. When the metric value is true, then the background indexing is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`search/indexed_hash_keys` GA ** _(project)_**   
Vector search indexed hash keys   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the number of indexed hash keys in vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`search/indexes` GA ** _(project)_**   
Vector search indexes   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the number of indexes in vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`search/query_requests_count` GA ** _(project)_**   
Vector search query requests count   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the number of query requests count. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`status_string`: Status code description.   
`search/used_memory_bytes` GA ** _(project)_**   
Vector search used memory in bytes   
`GAUGE`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Indicates the used memory in bytes in vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`server/uptime` GA ** _(project)_**   
Uptime   
`GAUGE`, `INT64`, `s`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Uptime in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/cache_hit_ratio` GA ** _(project)_**   
Cache Hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Cache Hit ratio as a fraction. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/connections/total` GA ** _(project)_**   
Total Connections Received   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Total number of connections accepted by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/cpu_utilization` GA ** _(project)_**   
CPU seconds   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _CPU-seconds consumed by the Redis server, broken down by system/user space and parent/child relationship. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role (one of [primary, replica]).   
`space`: The space ("system" or "user") in which CPU resources were consumed.   
`relationship`: The parent/child relationship of the process using CPU resources.   
`stats/cpu_utilization_main_thread` GA ** _(project)_**   
Main Thread CPU seconds   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _CPU-seconds consumed by the Redis server main thread, broken down by system/user space and parent/child relationship. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role (one of [primary, replica]).   
`space`: The space ("system" or "user") in which CPU resources were consumed.   
`relationship`: The parent/child relationship of the process using CPU resources.   
`stats/evicted_keys` GA ** _(project)_**   
Evicted Keys   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of evicted keys due to maxmemory limit. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/expired_keys` GA ** _(project)_**   
Expired Keys   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Total number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/keyspace_hits` GA ** _(project)_**   
Hits   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of successful lookup of keys in the main dictionary. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/keyspace_misses` GA ** _(project)_**   
Misses   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of failed lookup of keys in the main dictionary. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/memory/maxmemory` GA ** _(project)_**   
Maximum Memory   
`GAUGE`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Maximum amount of memory Redis can consume. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/memory/system_memory_overload_duration` GA ** _(project)_**   
Time in system memory overload   
`DELTA`, `INT64`, `us`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _The amount of time in microseconds the instance is in system memory overload mode. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/memory/system_memory_usage_ratio` GA ** _(project)_**   
System Memory Usage Ratio   
`GAUGE`, `DOUBLE`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Memory usage as a ratio of maximum system memory. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/memory/usage` GA ** _(project)_**   
Used Memory   
`GAUGE`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Total number of bytes allocated by Redis. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/memory/usage_ratio` GA ** _(project)_**   
Memory Usage Ratio   
`GAUGE`, `DOUBLE`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Memory usage as a ratio of maximum memory. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/network_traffic` GA ** _(project)_**   
Total traffic to Redis   
`DELTA`, `INT64`, `By`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Total number of bytes sent to/from redis (includes bytes from commands themselves, payload data, and delimiters). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`direction`: The direction of the traffic, inbound or outbound.   
`stats/pubsub/channels` GA ** _(project)_**   
Pubsub Channels   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Global number of pub/sub channels with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/pubsub/patterns` GA ** _(project)_**   
Pubsub Patterns   
`GAUGE`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Global number of pub/sub pattern with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
`stats/reject_connections_count` GA ** _(project)_**   
Rejected Connections   
`DELTA`, `INT64`, `1`   
**[redis_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_redis_instance)** |  _Number of connections rejected because of maxclients limit. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`role`: The node role, one of [primary, replica].   
  
### retail

Metrics from [AI Commerce Search API](https://docs.cloud.google.com/retail/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `retail.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`catalog/processed_user_events` GA ** _(project)_**   
Number of user events processed   
`GAUGE`, `INT64`, `1`   
**[retail.googleapis.com/Catalog](https://docs.cloud.google.com/monitoring/api/resources#tag_retail.googleapis.com/Catalog)** |  _The number of user events that have been processed for a catalog. Only the user events that are recorded in real time are included. Historical user events, which are bulk imported, are not included. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`event_type`: Event type, see https://cloud.google.com/retail/docs/user-events.   
`status`: Status of event, should be joined or unjoined.   
  
### router

Metrics from [Cloud Router](https://docs.cloud.google.com/compute/docs/cloudrouter). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `router.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`best_received_routes_count` GA ** _(project)_**   
Received routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of best routes received by router. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`bfd/control/receive_intervals` GA ** _(project)_**   
BFD control packets receive intervals   
`GAUGE`, `INT64`, `ms`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _BFD control packets receive intervals. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/received_packets_count` GA ** _(project)_**   
Control packets received   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of control packets received from this BFD session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/rejected_packets_count` GA ** _(project)_**   
Control packets rejected   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of control packets rejected, from this BFD session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/transmit_intervals` GA ** _(project)_**   
BFD control packets transmit intervals   
`GAUGE`, `INT64`, `ms`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _BFD control packets transmit intervals. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/control/transmitted_packets_count` GA ** _(project)_**   
Control packets transmitted   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of control packets transmitted from this BFD session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bfd/session_flap_events_count` GA ** _(project)_**   
BFD session flap   
`DELTA`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of each BFD flap event from this BFD session. A session flap event refers to the transition from Up state. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`event_type`: The reason for the BFD flap such as "AdminDown" or "ControlDetectionTimeExpired".   
`bfd/session_up` GA ** _(project)_**   
BFD session status   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Indicator for successful BFD session establishment. 1 indicates the session is up. 0 indicates the session is down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`peer_ip`: The peer IP of the BFD session.   
`bgp/received_routes_count` GA ** _(project)_**   
BGP received routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of routes received on a bgp session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`bgp_peer_name`: The name of the bgp session.   
`bgp/sent_routes_count` GA ** _(project)_**   
BGP sent routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of routes sent on a bgp session. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`bgp_peer_name`: The name of the bgp session.   
`bgp/session_up` GA ** _(project)_**   
BGP session status   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Indicator for successful bgp session establishment. 1 indicates the session is up. 0 indicates the session is down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`bgp_peer_name`: The name of the bgp session.   
`bgp_sessions_down_count` GA ** _(project)_**   
BGP sessions down count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of BGP sessions on the router that are down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`bgp_sessions_up_count` GA ** _(project)_**   
BGP sessions up count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of BGP sessions on the router that are up. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`dynamic_routes/learned_routes/any_dropped_unique_destinations` BETA ** _(project)_**   
Any unique destinations dropped   
`GAUGE`, `BOOL`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _A boolean metric of whether there are any unique destinations dropped in a network region due to exceeding quota. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`dynamic_routes/learned_routes/dropped_unique_destinations` BETA ** _(project)_**   
Unique destinations dropped   
`GAUGE`, `INT64`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _The number of unique destinations dropped in a network region due to exceeding quota. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`dynamic_routes/learned_routes/unique_destinations_limit` BETA ** _(project)_**   
Unique destinations limit   
`GAUGE`, `INT64`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _The maximum number of unique destinations allowed by route quota for this network region. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`dynamic_routes/learned_routes/used_unique_destinations` BETA ** _(project)_**   
Unique destinations used   
`GAUGE`, `INT64`, `1`   
**[gce_network_region](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network_region)** |  _Number of unique destinations used by learned routes for this network region. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`routing_mode`: Routing mode of the route, one of ["global" - learned from remote regions; "regional" - learned from local regions].   
`nat/allocated_ports` GA ** _(project)_**   
Allocated ports   
`GAUGE`, `INT64`, `{port}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Number of ports allocated to all VMs by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`nat_ip`: NAT IP of the ports.   
`nat/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of connections closed over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of received packets dropped by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of sent packets dropped by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`reason`: The reason for the packet drop. Possible values are OUT_OF_RESOURCES, ENDPOINT_INDEPENDENCE_CONFLICT.   
`nat/nat_allocation_failed` GA ** _(project)_**   
NAT allocation failed   
`GAUGE`, `BOOL`, ``   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Indicates if there is a failure in allocating NAT IPs to any VM in the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`nat/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of new connections created over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Number of connections currently open on the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/port_usage` GA ** _(project)_**   
Port usage   
`GAUGE`, `INT64`, `{port}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Maximum number of connections from VM to a single internet endpoint (IP:port). Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of bytes received (destination - > VMs) via the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of packets received (destination - > VMs) via the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/rule/nat_allocation_failed` GA ** _(project)_**   
NAT allocation failed per rule   
`GAUGE`, `BOOL`, ``   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Indicates if there is a failure in allocating NAT IPs to any VM in the NAT gateway for a specific NAT rule._   
`nat_rule_priority`: The priority number of the NAT rule associated with the error.   
`nat/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of bytes sent (VMs - > destination) over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[nat_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_nat_gateway)** |  _Count of packets sent (VMs - > destination) over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 225 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`router_up` GA ** _(project)_**   
Router tasks up   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Number of router software tasks that are running successfully. A value greater than or equal to 1 indicates that the router is up, although not all software tasks may be running. Compare the returned number to the expected number of software tasks for the router. A value of 0 indicates that the router is down. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`sent_routes_count` GA ** _(project)_**   
Sent routes count   
`GAUGE`, `INT64`, `1`   
**[gce_router](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_router)** |  _Current number of routes sent by router. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
### run

Metrics from managed [Cloud Run](https://docs.cloud.google.com/run/docs). (For Knative serving metrics, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) and [Knative metrics](https://docs.cloud.google.com/monitoring/api/metrics_knative).) Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `run.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`container/billable_instance_time` GA ** _(project)_**   
Billable Instance Time   
`DELTA`, `DOUBLE`, `s`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Billable time aggregated across all container instances. For a given container instance, billable time occurs when the container instance is starting or at least one request is being processed. Billable time is rounded up to the nearest 100 milliseconds. Examples: If a revision with 2 container instances has been continuously serving traffic in the last minute, the value is 2s/s with the default "rate" aligner. If a single request lasting 30ms was received by a revision in the past minute, it is rounded up to 100ms and averaged to 1.7ms/s over the minute with the default "rate" aligner. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/completed_probe_attempt_count` GA ** _(project)_**   
Completed Health Check Probe Attempt Count   
`DELTA`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Number of completed health check probe attempts and their results. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`probe_action`: Mechanism used to perform the probing.   
`is_healthy`: (BOOL) Result of the health check probe.   
`container_name`: Name of the probed container.   
`is_default`: (BOOL) Whether this probe is injected by google infrastructure.   
`probe_type`: Type of the probe.   
`container/completed_probe_count` GA ** _(project)_**   
Completed Health Check Probe Count   
`DELTA`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Number of completed health check probes and their results. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`probe_action`: Mechanism used to perform the probing.   
`is_healthy`: (BOOL) Result of the health check probe.   
`container_name`: Name of the probed container.   
`is_default`: (BOOL) Whether this probe is injected by google infrastructure.   
`probe_type`: Type of the probe.   
`container/containers` GA ** _(project)_**   
Multi-container instance counts   
`GAUGE`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Number of container instances that exist, broken down by state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`state`: Whether a container is "active" or "idle".   
`container/cpu/allocation_time` GA ** _(project)_**   
Container CPU Allocation   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container CPU allocation in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/cpu/usage` GA ** _(project)_**   
Multi-container CPU Usage   
`GAUGE`, `DISTRIBUTION`, `s{CPU}`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Actual container cpu usage in cpu seconds broken down by the metric field, container name. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`container/cpu/utilizations` GA ** _(project)_**   
Container CPU Utilization   
`DELTA`, `DISTRIBUTION`, `10^2.%`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container CPU utilization distribution across all container instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/gpu/memory_usages` GA ** _(project)_**   
GPU Memory Usage   
`GAUGE`, `DISTRIBUTION`, `By`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container GPU memory usage distribution across all container instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`gpu_number`: (INT64) Matches the CUDA device index (e.g. "0", "1").   
`container/gpu/memory_utilizations` GA ** _(project)_**   
GPU Memory Utilization   
`GAUGE`, `DISTRIBUTION`, `10^2.%`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container GPU memory utilization distribution across all container instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`gpu_number`: (INT64) Matches the CUDA device index (e.g. "0", "1").   
`container/gpu/utilizations` GA ** _(project)_**   
GPU Utilization   
`GAUGE`, `DISTRIBUTION`, `10^2.%`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container GPU utilization distribution across all container instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`gpu_number`: (INT64) Matches the CUDA device index (e.g. "0", "1").   
`container/instance_count` GA ** _(project)_**   
Instance Count   
`GAUGE`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Number of container instances that exist, broken down by state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: Whether a container is "active" or "idle".   
`container/instance_count_with_readiness` BETA ** _(project)_**   
Instance Count with Readiness   
`GAUGE`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _The number of instances broken down by readiness probe status. The readiness status can be one of "UNKNOWN", "HEALTHY" and "UNHEALTHY". Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`readiness_status`: The readiness status can be one of "UNKNOWN", "HEALTHY" and "UNHEALTHY".   
`container/max_request_concurrencies` GA ** _(project)_**   
Max Concurrent Requests   
`DELTA`, `DISTRIBUTION`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of the maximum number of concurrent requests being served by each container instance over a minute. Filter by 'state' = 'active' only get the concurrency of active container instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: Whether a container is "active" or "idle".   
`container/memory/allocation_time` GA ** _(project)_**   
Container Memory Allocation   
`DELTA`, `DOUBLE`, `GiBy.s`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container memory allocation in Gibibyte-seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/memory/tmpfs_usage` GA ** _(project)_**   
Multi-container Tmpfs Usage   
`GAUGE`, `DISTRIBUTION`, `byte`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Actual container tmpfs usage in bytes broken down by the metric field, container name. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`container/memory/usage` GA ** _(project)_**   
Multi-container Memory Usage   
`GAUGE`, `DISTRIBUTION`, `byte`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Actual container memory usage in bytes broken down by the metric field, container name. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`container_name`: Container name.   
`container/memory/utilizations` GA ** _(project)_**   
Container Memory Utilization   
`DELTA`, `DISTRIBUTION`, `10^2.%`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Container memory utilization distribution across all container instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/network/received_bytes_count` GA ** _(project)_**   
Received Bytes   
`DELTA`, `INT64`, `By`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Incoming socket and HTTP request traffic, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`kind`: Type of network from where traffic is received, one of [internet, private, google]   
`container/network/sent_bytes_count` GA ** _(project)_**   
Sent Bytes   
`DELTA`, `INT64`, `By`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Outgoing socket and HTTP response traffic, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`kind`: Type of network where traffic is sent, one of [internet, private, google]. Response traffic is classified as [google] for responses returned through Google Cloud load balancers and [internet] for the rest.   
`container/network/throttled_inbound_bytes_count` BETA ** _(project)_**   
Inbound bytes throttled   
`DELTA`, `INT64`, `By`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Inbound bytes dropped due to network throttling. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`network`: Network layer (L3) protocol used, one of [ipv4, ipv6].   
`transport`: Transport used, one of [tcp, udp, icmp].   
`type`: Type of network from where traffic is received, one of [public, private, googleapis]   
`container/network/throttled_inbound_packets_count` BETA ** _(project)_**   
Inbound packets throttled   
`DELTA`, `INT64`, `{packet}`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Inbound packets dropped due to network throttling. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`network`: Network layer (L3) protocol used, one of [ipv4, ipv6].   
`transport`: Transport used, one of [tcp, udp, icmp].   
`type`: Type of network from where traffic is received, one of [public, private, googleapis]   
`container/network/throttled_outbound_bytes_count` BETA ** _(project)_**   
Outbound bytes throttled   
`DELTA`, `INT64`, `By`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Outbound bytes dropped due to network throttling. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`network`: Network layer (L3) protocol used, one of [ipv4, ipv6].   
`transport`: Transport used, one of [tcp, udp, icmp].   
`type`: Type of network from where traffic is received, one of [public, private, googleapis]   
`container/network/throttled_outbound_packets_count` BETA ** _(project)_**   
Outbound packets throttled   
`DELTA`, `INT64`, `{packet}`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Outbound packets dropped due to network throttling. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`network`: Network layer (L3) protocol used, one of [ipv4, ipv6].   
`transport`: Transport used, one of [tcp, udp, icmp].   
`type`: Type of network from where traffic is received, one of [public, private, googleapis]   
`container/probe_attempt_latencies` GA ** _(project)_**   
Health Check Probe Attempt Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Distribution of time spent running a single probe attempt before success or failure in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`probe_action`: Mechanism used to perform the probing.   
`is_healthy`: (BOOL) Result of the health check probe.   
`container_name`: Name of the probed container.   
`is_default`: (BOOL) Whether this probe is injected by google infrastructure.   
`probe_type`: Type of the probe.   
`container/probe_latencies` GA ** _(project)_**   
Health Check Probe Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Distribution of time spent running a probe before success or failure in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`probe_action`: Mechanism used to perform the probing.   
`is_healthy`: (BOOL) Result of the health check probe.   
`container_name`: Name of the probed container.   
`is_default`: (BOOL) Whether this probe is injected by google infrastructure.   
`probe_type`: Type of the probe.   
`container/startup_latencies` BETA ** _(project)_**   
Container startup latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Distribution of time spent starting a new container instance in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/connection_latencies` GA ** _(project)_**   
CloudSQL connection latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of latency in microseconds for connections originating from Cloud Run to CloudSQL. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/connection_refused_count` GA ** _(project)_**   
CloudSQL connection refused count   
`DELTA`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Total number of connections refused originating from Cloud Run to CloudSQL. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/connection_request_count` GA ** _(project)_**   
CloudSQL connection request count   
`DELTA`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Total number of connection requests originating from Cloud Run to CloudSQL. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/received_bytes_count` GA ** _(project)_**   
CloudSQL bytes received   
`DELTA`, `INT64`, `By`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Number of bytes received by Cloud Run from CloudSQL over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`infrastructure/cloudsql/sent_bytes_count` GA ** _(project)_**   
CloudSQL bytes sent   
`DELTA`, `INT64`, `By`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Number of bytes sent by Cloud Run to CloudSQL over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/disk/allocation_time` BETA ** _(project)_**   
Instance Disk Allocation   
`DELTA`, `DOUBLE`, `GiBy.s`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Instance disk allocation in GiB seconds, broken down by the metric fields, volume name and volume type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`volume_name`: Name of the volume.   
`volume_type`: Type of the volume.   
`instance/disk/usage` BETA ** _(project)_**   
Instance Disk Usage   
`GAUGE`, `DISTRIBUTION`, `byte`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Instance disk usage in bytes broken down by the metric fields, volume name and volume type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`volume_name`: Name of the volume.   
`volume_type`: Type of the volume.   
`instance/disk/utilizations` BETA ** _(project)_**   
Instance Disk Utilization   
`DELTA`, `DISTRIBUTION`, `10^2.%`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[cloud_run_worker_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_worker_pool)** |  _Instance disk utilization as a percentage, broken down by the metric fields, volume name and volume type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`volume_name`: Name of the volume.   
`volume_type`: Type of the volume.   
`job/completed_execution_count` GA ** _(project)_**   
Completed Executions   
`DELTA`, `INT64`, `1`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)** |  _Number of completed job executions and their result. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`result`: Execution result.   
`job/completed_task_attempt_count` GA ** _(project)_**   
Completed exit result and task attempts   
`DELTA`, `INT64`, `1`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)** |  _Number of completed task attempts and its corresponding exit result. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`result`: Job task result.   
`attempt`: (INT64) The number of retries for a job task.   
`job/running_executions` GA ** _(project)_**   
Running Executions   
`GAUGE`, `INT64`, `1`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)** |  _Number of running job executions. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`job/running_task_attempts` GA ** _(project)_**   
Running task attempts   
`GAUGE`, `INT64`, `1`   
**[cloud_run_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_job)** |  _Number of running task attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`attempt`: (INT64) The number of retries for a job task.   
`pending_queue/pending_requests` ALPHA ** _(project)_**   
Pending Requests   
`GAUGE`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Number of pending requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`request_count` GA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Number of requests reaching the revision. Excludes requests that are not reaching your container instances (for example, unauthorized requests or when maximum number of instances is reached). Captured at the end of the request lifecycle. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`route`: Always empty.   
`request_latencies` GA ** _(project)_**   
Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of request latency in milliseconds reaching the revision. Latency is measured from when the request reaches the running container to when it exits. Notably, it does not include container startup latency. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`route`: Always empty.   
`request_latency/e2e_latencies` BETA ** _(project)_**   
End to End Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of request latencies in milliseconds measured from when the request enters Google Cloud's network to when Cloud Run sends the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`request_latency/ingress_to_region` BETA ** _(project)_**   
Ingress to Region Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of request latencies in milliseconds measured from when the request enters Google Cloud's network to when the request reaches the cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`request_latency/pending` BETA ** _(project)_**   
Pending Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of request latencies in milliseconds measured from when the request reaches Cloud Run to when the request is sent to an instance. Includes time spent waiting for a slot on an existing instance, or for a new instance to start (startup latency). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`request_latency/response_egress` BETA ** _(project)_**   
Response Egress Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of response latencies in milliseconds measured from when the container finished processing the request to when Cloud Run sends the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`request_latency/routing` BETA ** _(project)_**   
Routing Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of request latencies in milliseconds measured from when the request reaches the cloud region to when the request reaches Cloud Run. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`request_latency/user_execution` BETA ** _(project)_**   
User Execution Request Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Distribution of request latencies in milliseconds measured from when the request reaches a running instance to when it exits. Only includes time spent in user container. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: Response code of a request.   
`response_code_class`: Response code class of a request.   
`scaling/recommended_instances` GA ** _(project)_**   
Recommended Instances   
`GAUGE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _Recommended number of instances per scaling driver. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`scaling_driver`: Factor that determined the recommended instance count, e.g. CPU utilization.   
`service_health_count` BETA ** _(project)_**   
Service Health Count   
`GAUGE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)** |  _The number of services in each Service Health status, based on their readiness probe results. The service health status can be one of "UNKNOWN", "HEALTHY" and "UNHEALTHY". Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`service_health`: The service health status can be one of "UNKNOWN", "HEALTHY" and "UNHEALTHY".   
  
### saasservicemgmt

Metrics from [App Lifecycle Manager](https://docs.cloud.google.com/saas-runtime/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `saasservicemgmt.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`rollout/state` BETA ** _(project)_**   
Rollout State   
`GAUGE`, `BOOL`, ``   
**[saasservicemgmt.googleapis.com/Rollout](https://docs.cloud.google.com/monitoring/api/resources#tag_saasservicemgmt.googleapis.com/Rollout)** |  _Indicates the current state of a specific rollout._   
`state_name`: The human-readable name of the rollout state, one of ['UNSPECIFIED', 'RUNNING', 'PAUSED', 'SUCCEEDED', 'FAILED', 'CANCELLED', 'WAITING', 'CANCELLING', 'RESUMING', 'PAUSING'].   
`root_rollout_id`: The root_rollout associated with this local rollout. If this rollout is the root_rollout itself then the rollout_id of the monitored resource will be equal to the root_rollout_id.   
`saas_id`: The SaaS ID associated with this rollout.   
`unit_kind_id`: The Unit Kind ID associated with this rollout.   
`release_id`: The Release ID associated with this rollout.   
`reason`: Indicates the reason for the current state of the rollout.   
`unit/count` GA ** _(project)_**   
Unit Count   
`GAUGE`, `INT64`, `1`   
**[saasservicemgmt.googleapis.com/UnitKind](https://docs.cloud.google.com/monitoring/api/resources#tag_saasservicemgmt.googleapis.com/UnitKind)** |  _The total number of units._   
`release_id`: The release name of the unit.   
`unit_state`: The state of the unit at time of collection.   
`saas_id`: Unique identifier for saas instance.   
`tenant_id`: Unique identifier for tenant.   
`unit/unit_operation_completion_time` GA ** _(project)_**   
The time to complete a unit operation   
`GAUGE`, `INT64`, `ms`   
**[saasservicemgmt.googleapis.com/Unit](https://docs.cloud.google.com/monitoring/api/resources#tag_saasservicemgmt.googleapis.com/Unit)** |  _The time from unit operation creation to the time the unit operation completes._   
`unit_kind_id`: Identifier for a unit kind.   
`unit_operation_type`: The type of unit operation e.g. provision and upgrade.   
`saas_id`: Unique identifier for saas instance.   
`tenant_id`: Unique identifier for tenant.   
`unit/unit_operations_by_state` GA ** _(project)_**   
Unit Operation counts by state   
`GAUGE`, `INT64`, `1`   
**[saasservicemgmt.googleapis.com/Unit](https://docs.cloud.google.com/monitoring/api/resources#tag_saasservicemgmt.googleapis.com/Unit)** |  _Indicates the number of unit operation in a terminal state._   
`rollout_id`: Identifier for a rollout.   
`unit_kind_id`: Identifier for a unit kind.   
`unit_operation_type`: The type of unit operation e.g. provision and upgrade.   
`unit_operation_state`: The current state of unit operation e.g. succeed and failed.   
`status`: The canonical code for this unit operation.   
`saas_id`: Unique identifier for saas instance.   
`tenant_id`: Unique identifier for tenant.   
  
### serviceruntime

Metrics available to be collected by any [ Google Cloud API](https://console.cloud.google.com/apis/library) (resource type [`consumed_api`](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)) and by APIs you created by using [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs) (resource type [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api)). Note that not all Google Cloud APIs collect `serviceruntime` metrics. 

The resources listed for the metrics are at launch stage GA, except for `api`, which is at launch stage BETA. 

The "metric type" strings in this table must be prefixed with `serviceruntime.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _The count of completed requests. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._   
`protocol`: The protocol of the request, e.g. "http", "grpc".   
`response_code`: The HTTP response code for HTTP requests, or HTTP equivalent code for gRPC requests. See code mapping in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`response_code_class`: The response code class for HTTP requests, or HTTP equivalent class for gRPC requests, e.g. "2xx", "4xx".   
`grpc_status_code`: The numeric gRPC response code for gRPC requests, or gRPC equivalent code for HTTP requests. See code mapping in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`api/request_latencies` GA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of latencies in seconds for non-streaming requests. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/request_latencies_backend` GA ** _(project)_**   
Request backend latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of backend latencies in seconds for non-streaming requests. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/request_latencies_overhead` GA ** _(project)_**   
Request overhead latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of request latencies in seconds for non-streaming requests excluding the backend. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/request_sizes` GA ** _(project)_**   
Request sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of request sizes in bytes recorded at request completion. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/response_sizes` GA ** _(project)_**   
Response sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of response sizes in bytes recorded at request completion. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`mcp/request_count` GA ** _(project)_**   
MCP Request Count   
`DELTA`, `INT64`, `1`   
**[consumed_mcp_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_mcp_api)** |  _The count of MCP requests._   
`response_code`: The HTTP response code for HTTP requests, or HTTP equivalent code for MCP requests.   
`response_code_class`: The response code class for HTTP requests, or HTTP equivalent class for gRPC requests, e.g. '2xx', '4xx'.   
`mcp/request_durations` GA ** _(project)_**   
MCP Request Duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[consumed_mcp_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_mcp_api)** |  _The duration of the MCP request from the time it was sent until the response or ack is received._  
`quota/allocation/usage` GA ** _(project, folder, organization)_**   
Allocation quota usage   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The total consumed allocation quota. Values reported more than 1/min are dropped. If no changes are received in quota usage, the last value is repeated at least every 24 hours. Sampled every 60 seconds._   
`quota_metric`: The name of quota metric or quota group.   
`quota/concurrent/exceeded` ALPHA ** _(project, folder, organization)_**   
Concurrent Quota Exceeded   
`DELTA`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)** |  _The number of times exceeding the concurrent quota was attempted. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`time_window`: The window size for concurrent operation limits.   
`quota/concurrent/limit` ALPHA ** _(project, folder, organization)_**   
Concurrent Quota limit   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The concurrent limit for the quota. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`time_window`: The window size for concurrent operation limits.   
`quota/concurrent/usage` ALPHA ** _(project, folder, organization)_**   
Concurrent Quota usage   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`time_window`: The window size for concurrent operation limits.   
`quota/exceeded` GA ** _(project, folder, organization)_**   
Quota exceeded error   
`GAUGE`, `BOOL`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)** |  _The error happened when the quota limit was exceeded. Sampled every 60 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`quota/limit` GA ** _(project, folder, organization)_**   
Quota limit   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The limit for the quota. Sampled every 86400 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`quota/rate/net_usage` GA ** _(project, folder, organization)_**   
Rate quota usage   
`DELTA`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The total consumed rate quota. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`method`: The API method name, such as "disks.list".   
`quota_metric`: The name of quota metric or quota group.   
`quota/ratev2/exceeded` BETA ** _(project, folder, organization)_**   
Windowed Rate Quota Exceeded   
`DELTA`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)** |  _The number of times exceeding the windowed rate quota was attempted. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`window_size`: The window size for rate operation limits.   
`quota/ratev2/limit` BETA ** _(project, folder, organization)_**   
Windowed Rate Quota limit   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The windowed rate limit for the quota. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`window_size`: The window size for rate operation limits.   
`quota/ratev2/net_usage` BETA ** _(project, folder, organization)_**   
Windowed Rate Quota usage   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The windowed rate usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`method`: The API method name, such as "disks.list".   
`limit_name`: The quota limit name, such as "RequestsPerDay" or "InUseIpAddresses".   
`quota_metric`: The name of quota metric or quota group.   
`window_size`: The window size for rate operation limits.   
`window_start_time`: The start time of the window.   
  
### spanner

Metrics from [Spanner](https://docs.cloud.google.com/spanner/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `spanner.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/adapter_request_count` GA ** _(project)_**   
Adapter API requests   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner Adapter API requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`method`: Cloud Spanner Adapter API method.   
`protocol`: Adapter protocol.   
`message_type`: Adapter protocol message type.   
`adapter_status`: Adapter protocol request result.   
`op_type`: Operation type.   
`api/adapter_request_latencies` GA ** _(project)_**   
Adapter request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies for a database. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner Adapter API method.   
`protocol`: Adapter protocol.   
`message_type`: Adapter protocol message type.   
`op_type`: Operation type.   
`api/api_request_count` GA ** _(project)_**   
API requests   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner API requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`method`: Cloud Spanner API method.   
`api/mcp_request_count` GA ** _(project)_**   
MCP request rate   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Rate of Cloud Spanner MCP requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Request call result, ok=success.   
`tool`: The name of the MCP tool.   
`database`: Target database.   
`api/mcp_request_latencies` GA ** _(project)_**   
MCP request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of MCP request latencies. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`tool`: The name of the MCP tool.   
`database`: Target database.   
`api/read_request_count_by_serving_location` BETA ** _(project)_**   
Read API request by serving location   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner Read API requests by serving location, whether it is a directed read query, and whether it is a change stream query. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`is_change_stream`: (BOOL) TRUE if it is a change stream query.   
`is_directed_read`: (BOOL) TRUE if it is a directed read query.   
`status`: Request call result, OK=success.   
`serving_location`: The location of serving replicas.   
`api/read_request_latencies_by_change_stream` GA ** _(project)_**   
Read request latencies by change stream   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of read request latencies by whether it is a change stream query. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`is_change_stream`: (BOOL) TRUE if it is a change stream query.   
`api/read_request_latencies_by_serving_location` BETA ** _(project)_**   
Read API request latencies by serving location   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of read request latencies by serving location, whether it is a directed read query, and whether it is a change stream query. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. This is a superset of spanner.googleapis.com/api/read_request_latencies_by_change_stream. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`is_change_stream`: (BOOL) TRUE if it is a change stream query.   
`is_directed_read`: (BOOL) TRUE if it is a directed read query.   
`serving_location`: The location of serving replicas.   
`api/received_bytes_count` GA ** _(project)_**   
Bytes received by Cloud Spanner   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Uncompressed request bytes received by Cloud Spanner. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`api/request_count` GA ** _(project)_**   
API request rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Rate of Cloud Spanner API requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`method`: Cloud Spanner API method.   
`api/request_count_per_protocol` GA ** _(project)_**   
API request rate per protocol   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Rate of Cloud Spanner API requests per protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Request call result, ok=success.   
`region`: The region where the request was served.   
`protocol`: Protocl used for this request.   
`method`: Cloud Spanner API method.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`op_type`: Operation type.   
`database`: Target database.   
`api/request_count_per_transaction_options` GA ** _(project)_**   
API requests by transaction options   
`GAUGE`, `DOUBLE`, `1/s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner API request rate by transaction options. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`status`: Request call result, ok=success.   
`op_type`: Operation type ("read", "write" or "other").   
`response_code`: HTTP response code received, such as 200 or 500.   
`lock_mode`: The read lock mode used if within a read-write transaction ("PESSIMISTIC" or "OPTIMISTIC").   
`isolation_level`: The isolation level used if within a read-write transaction ("SERIALIZABLE" or "REPEATABLE_READ").   
`region`: The region where the request was served.   
`transaction_type`: Transaction type ("READ_ONLY", "READ_WRITE", "PARTITIONED_DML" or "NONE").   
`api/request_latencies` GA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies for a database. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`api/request_latencies_by_transaction_type` GA ** _(project)_**   
Request latencies by transaction type   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies by transaction types. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`transaction_type`: Transaction type ("READ_ONLY" or "READ_WRITE").   
`is_leader_involved`: (BOOL) TRUE if the leader roundtrip call is issued.   
`api/request_latencies_per_protocol` GA ** _(project)_**   
Request latencies per protocol   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies for a database per protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The region where the request was served.   
`protocol`: Protocl used for this request.   
`method`: Cloud Spanner API method.   
`op_type`: Operation type.   
`database`: Target database.   
`api/request_latencies_per_transaction_options` GA ** _(project)_**   
Request latencies by transaction options   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies by transaction options for a database. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`op_type`: Operation type ("read", "write" or "other").   
`lock_mode`: The read lock mode used if within a read-write transaction ("PESSIMISTIC" or "OPTIMISTIC").   
`isolation_level`: The isolation level used if within a read-write transaction ("SERIALIZABLE" or "REPEATABLE_READ").   
`is_leader_involved`: (BOOL) TRUE if the leader roundtrip call is issued.   
`region`: The region where the request was served.   
`transaction_type`: Transaction type ("READ_ONLY", "READ_WRITE", "PARTITIONED_DML" or "NONE").   
`api/sent_bytes_count` GA ** _(project)_**   
Bytes sent by Cloud Spanner   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Uncompressed response bytes sent by Cloud Spanner. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`client/afe_connectivity_error_count` GA ** _(project)_**   
AFE Connectivity Error Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of requests that failed to reach the Spanner API Frontend. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/afe_latencies` GA ** _(project)_**   
AFE Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency between Spanner API Frontend receiving an RPC and starting to write back the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/attempt_count` GA ** _(project)_**   
Attempt Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The total number of RPC attempt performed by the Spanner client. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner attempt status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/attempt_latencies` GA ** _(project)_**   
Attempt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of the total end-to-end latency across a RPC attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner attempt status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/gfe_connectivity_error_count` GA ** _(project)_**   
GFE Connectivity Error Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of requests that failed to reach the Google network. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/gfe_latencies` GA ** _(project)_**   
GFE Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency between Google network(GFE) receiving an RPC and reading back the first byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/operation_count` GA ** _(project)_**   
Operation Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The total number of operations performed by the Spanner client. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/operation_latencies` GA ** _(project)_**   
Operation Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of the total end-to-end latency across all RPC attempts associated with a Spanner operation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`graph_algorithm_stat/total/execution_count` GA ** _(project)_**   
Graph algorithm execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total graph algorithm requests received by Cloud Spanner during the time interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`algorithm`: Graph algorithm executed.   
`graph_algorithm_stat/total/execution_durations` GA ** _(project)_**   
Graph algorithm durations   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of graph algorithm execution times (in seconds) within the database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`algorithm`: Graph algorithm executed.   
`graph_algorithm_stat/total/failed_execution_count` GA ** _(project)_**   
Graph algorithm failed count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total failed graph algorithm requests in Cloud Spanner during the time interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`algorithm`: Graph algorithm executed.   
`status`: failed status, one of [cancelled, timeout, error].   
`graph_query_stat/total/bytes_returned_count` GA ** _(project)_**   
Graph query bytes returned count   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of data bytes that the graph queries returned, excluding transmission encoding overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/execution_count` GA ** _(project)_**   
Graph query execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times Cloud Spanner saw graph queries during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/failed_execution_count` GA ** _(project)_**   
Graph query failures   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times graph queries failed during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`status`: failed status, one of [cancelled, timeout, error].   
`graph_query_stat/total/query_latencies` GA ** _(project)_**   
Graph query latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total length of time, in seconds, for graph query executions within the database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/returned_rows_count` GA ** _(project)_**   
Graph query rows returned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the graph queries returned. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/scanned_rows_count` GA ** _(project)_**   
Graph query rows scanned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the graph queries scanned excluding deleted values. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`instance/autoscaling/high_priority_cpu_utilization_target` GA ** _(project)_**   
Autoscaling high priority cpu utilization target   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _High priority CPU utilization target used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/max_node_count` GA ** _(project)_**   
Autoscaling max nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of nodes autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/max_processing_units` GA ** _(project)_**   
Autoscaling max processing units   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of processing units autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/min_node_count` GA ** _(project)_**   
Autoscaling min nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of nodes autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/min_processing_units` GA ** _(project)_**   
Autoscaling min processing units   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of processing units autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/storage_utilization_target` GA ** _(project)_**   
Autoscaling storage utilization target   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage utilization target used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/total_cpu_utilization_target` GA ** _(project)_**   
Autoscaling total cpu utilization target   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total CPU utilization target used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/backup/used_bytes` GA ** _(project)_**   
Backup storage used   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Backup storage used in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`backup`: Target backup.   
`instance/cpu/smoothed_utilization` GA ** _(project)_**   
Smoothed CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _24-hour smoothed utilization of provisioned CPU. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`instance/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of provisioned CPU. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/cpu/utilization_by_operation_type` GA ** _(project)_**   
CPU utilization by operation type   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of provisioned CPU, by operation type. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Currently, it does not include CPU utilization for system tasks. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`is_system`: (BOOL) TRUE if the number is system CPU utilization.   
`priority`: Task priority ("high" or "medium" or "low").   
`category`: Operation type ("read_readonly", "beginorcommit" etc).   
`instance/cpu/utilization_by_priority` GA ** _(project)_**   
CPU utilization by priority   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of provisioned CPU, by priority. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`is_system`: (BOOL) TRUE if the number is system CPU utilization.   
`priority`: Task priority ("high", "medium", or "low").   
`instance/cross_region_replicated_bytes_count` GA ** _(project)_**   
Cross region replicated bytes   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of bytes replicated from preferred leader to replicas across regions. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`source_region`: Preferred leader region.   
`destination_region`: Cloud Spanner region the data is replicated to.   
`tag`: Type of transaction contributing to replication.   
`instance/data_boost/processing_unit_second_count` GA ** _(project)_**   
Processing unit second   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total processing units used for DataBoost operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`credential_id`: The IAM credential ID.   
`instance/disk_load` GA ** _(project)_**   
Disk load   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of HDD disk load in an instance. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/dual_region_quorum_availability` GA ** _(project)_**   
Dual Region Quorum Availability   
`GAUGE`, `BOOL`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Quorum availability signal for dual region instance configs. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`quorum_availability`: Quorum availability level.   
`instance/edition/feature_usage` GA ** _(project)_**   
Feature usage   
`GAUGE`, `BOOL`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Indicates if an edition feature is being used by the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`feature`: Edition feature.   
`database`: Database using the feature, if any.   
`used_in_query_path`: (BOOL) Used in query path, or not.   
`instance/leader_percentage_by_region` GA ** _(project)_**   
Leader percentage by region   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percentage of leaders by cloud region. Values are typically numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`region`: Cloud region containing the leaders.   
`instance/node_count` GA ** _(project)_**   
Nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total number of nodes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/peak_split_cpu_usage_score` GA ** _(project)_**   
Peak split cpu usage score   
`GAUGE`, `DOUBLE`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum cpu usage score observed in a database across all splits. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/placement_row_limit` GA ** _(project)_**   
Placement row limit   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Upper limit for placement rows. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/placement_row_limit_per_processing_unit` GA ** _(project)_**   
Placement row limit per processing unit   
`GAUGE`, `DOUBLE`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Upper limit for placement rows per processing unit. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/placement_rows` GA ** _(project)_**   
Placement row count by database   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of placement rows in a database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/processing_units` GA ** _(project)_**   
Processing units   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total number of processing units. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/replica/autoscaling/high_priority_cpu_utilization_target` GA ** _(project)_**   
Autoscaling high priority cpu utilization target for replica   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _High priority CPU utilization target used for autoscaling replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/max_node_count` GA ** _(project)_**   
Autoscaling max nodes for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of nodes autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/max_processing_units` GA ** _(project)_**   
Autoscaling max processing units for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of processing units autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/min_node_count` GA ** _(project)_**   
Autoscaling min nodes for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of nodes autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/min_processing_units` GA ** _(project)_**   
Autoscaling min processing units for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of processing units autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/total_cpu_utilization_target` GA ** _(project)_**   
Autoscaling total cpu utilization target for replica   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total CPU utilization target used for autoscaling replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/cmek/total_keys` BETA ** _(project)_**   
CMEK keys   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of CMEK keys identified by database and key revocation status. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`is_key_revoked`: (BOOL) True if the CloudKMS key is revoked.   
`instance/replica/node_count` GA ** _(project)_**   
Replica nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of nodes allocated to each replica identified by location and replica type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/processing_units` GA ** _(project)_**   
Replica processing units.   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of processing units allocated to each replica identified by location and replica type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/schema_object_count_limit` GA ** _(project)_**   
Schema objects count limit   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The schema object count limit for the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/schema_objects` GA ** _(project)_**   
Schema object count   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The total count of schema objects in the database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/session_count` GA ** _(project)_**   
Sessions   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of sessions in use. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`instance/storage/columnar_used_bytes` BETA ** _(project)_**   
Storage used (logical) for columnar storage   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used (logical) in bytes for columnar storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`storage_class`: Storage type.   
`instance/storage/columnar_used_bytes_by_region` BETA ** _(project)_**   
Storage used (logical) for columnar storage by region   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used (logical) in bytes for columnar storage by cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`storage_class`: Storage type.   
`instance/storage/combined/limit_bytes` GA ** _(project)_**   
Storage limit (combined)   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit (combined) for instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/storage/combined/limit_bytes_per_processing_unit` GA ** _(project)_**   
Storage limit (combined) per processing unit   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit (combined) per processing unit in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/storage/combined/utilization` GA ** _(project)_**   
Storage utilization (combined)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used (combined) as a fraction of storage limit (combined). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/storage/limit_bytes` GA ** _(project)_**   
Storage limit   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit for instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_class`: Storage type.   
`instance/storage/limit_bytes_per_processing_unit` GA ** _(project)_**   
Storage limit per processing unit   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit per processing unit in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_class`: Storage type.   
`instance/storage/used_bytes` GA ** _(project)_**   
Storage used   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`storage_class`: Storage type.   
`instance/storage/utilization` GA ** _(project)_**   
Storage utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used as a fraction of storage limit. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_class`: Storage type.   
`lock_stat/total/lock_wait_time` GA ** _(project)_**   
Lock wait time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total lock wait time for lock conflicts recorded for the entire database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`pending_restore_count` GA ** _(project)_**   
Pending restore count   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Limits number of pending restores per instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`query_count` GA ** _(project)_**   
Count of queries   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of queries by database name, status, query type, and used optimizer version. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`query_type`: Type of query.   
`optimizer_version`: (INT64) Optimizer version used by the query.   
`query_stat/total/bytes_returned_count` GA ** _(project)_**   
Bytes returned count   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of data bytes that the queries returned, excluding transmission encoding overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/cpu_time` GA ** _(project)_**   
Query cpu time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds of CPU time Cloud Spanner spent on operations to execute the queries. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/execution_count` GA ** _(project)_**   
Query execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times Cloud Spanner saw queries during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/failed_execution_count` GA ** _(project)_**   
Query failures   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times queries failed during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`status`: failed status, one of [cancelled, timeout, error].   
`query_stat/total/query_latencies` GA ** _(project)_**   
Query latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total length of time, in seconds, for query executions within the database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/remote_service_calls_count` GA ** _(project)_**   
Remote service calls count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of remote service calls. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/remote_service_calls_latencies` GA ** _(project)_**   
Remote service calls latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency of remote service calls. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/remote_service_network_bytes_sizes` GA ** _(project)_**   
Remote service network bytes   
`DELTA`, `DISTRIBUTION`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Network bytes exchanged with remote service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`direction`: Direction of traffic: sent or received.   
`query_stat/total/remote_service_processed_rows_count` GA ** _(project)_**   
Remote service rows count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of rows processed by a remote service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/remote_service_processed_rows_latencies` GA ** _(project)_**   
Remote service rows latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency of rows processed by a remote service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/returned_rows_count` GA ** _(project)_**   
Rows returned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the queries returned. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/scanned_rows_count` GA ** _(project)_**   
Rows scanned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the queries scanned excluding deleted values. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`queue/active_receive_tvf_queries` BETA ** _(project)_**   
Active receive Table-Valued Function (TVF) queries   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of active receive table-valued function (TVF) queries in the queue. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/buffered_in_flight_messages` BETA ** _(project)_**   
Buffered in-flight messages   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of in-flight messages in the queue that are currently leased and buffered in memory. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/buffered_ready_messages` BETA ** _(project)_**   
Buffered ready messages   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of ready messages in the queue that are buffered in memory and available for delivery. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/lease_expiration_count` BETA ** _(project)_**   
Lease expirations   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of expired message leases. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/message_ack_count` BETA ** _(project)_**   
Messages acknowledged   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of messages acknowledged. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/message_payload_sizes` BETA ** _(project)_**   
Message payload sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of message payload sizes in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/message_send_count` BETA ** _(project)_**   
Messages sent   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of messages sent. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/oldest_unacked_message_age` BETA ** _(project)_**   
Oldest unacked message age   
`GAUGE`, `INT64`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Age of the oldest unacknowledged message in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`quota/internal/instance_admin_update_instance_requests/exceeded` ALPHA ** _(project)_**   
Instance update requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Number of attempts to exceed the limit on quota metric spanner.googleapis.com/internal/instance_admin_update_instance_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal/instance_admin_update_instance_requests/limit` ALPHA ** _(project)_**   
Instance update requests quota limit   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current limit on quota metric spanner.googleapis.com/internal/instance_admin_update_instance_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal/instance_admin_update_instance_requests/usage` ALPHA ** _(project)_**   
Instance update requests quota usage   
`DELTA`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current usage on quota metric spanner.googleapis.com/internal/instance_admin_update_instance_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/pending_restore_count/exceeded` GA ** _(project)_**   
Pending restore count quota exceeded error   
`DELTA`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Number of attempts to exceed the limit on quota metric spanner.googleapis.com/pending_restore_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/pending_restore_count/limit` GA ** _(project)_**   
Pending restore count quota limit   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current limit on quota metric spanner.googleapis.com/pending_restore_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/pending_restore_count/usage` GA ** _(project)_**   
Pending restore count quota usage   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current usage on quota metric spanner.googleapis.com/pending_restore_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`read_stat/total/bytes_returned_count` GA ** _(project)_**   
Bytes returned count   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total number of data bytes that the reads returned excluding transmission encoding overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/client_wait_time` GA ** _(project)_**   
Client wait time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds spent waiting due to throttling. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/cpu_time` GA ** _(project)_**   
Read cpu time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds of CPU time Cloud Spanner spent execute the reads excluding prefetch CPU and other overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/execution_count` GA ** _(project)_**   
Read execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times Cloud Spanner executed the read shapesduring the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/leader_refresh_delay` GA ** _(project)_**   
Leader refresh delay   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds spent coordinating reads across instances in multi-regionconfigurations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/locking_delays` GA ** _(project)_**   
Locking delays   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total time in seconds spent waiting due to locking. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/returned_rows_count` GA ** _(project)_**   
Rows returned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the reads returned. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`row_deletion_policy/deleted_rows_count` GA ** _(project)_**   
Rows deleted   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of rows deleted by the policy since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`row_deletion_policy/processed_watermark_age` GA ** _(project)_**   
Processed watermark age   
`GAUGE`, `INT64`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Time between now and the read timestamp of the last successful execution. An execution happens as the background task deletes eligible data in batches and is successful even when there are rows that cannot be deleted. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`row_deletion_policy/undeletable_rows` GA ** _(project)_**   
Total number of undeletable rows   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows in all tables in the database that can't be deleted. A row can't be deleted if, for example, it has so many child rows that a delete would exceed the transaction limit. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`transaction_stat/total/bytes_written_count` GA ** _(project)_**   
Bytes written   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of bytes written by transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`transaction_stat/total/commit_attempt_count` GA ** _(project)_**   
Transaction commit attempts   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of commit attempts for transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`status`: Commit status ("success", "abort", or "precondition_failure")   
`transaction_stat/total/commit_retry_count` GA ** _(project)_**   
Transaction commit retries   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of commit attempts that are retries from previously aborted transaction attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`transaction_stat/total/participants` GA ** _(project)_**   
Transaction participants   
`DELTA`, `DISTRIBUTION`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total number of participants in each commit attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`transaction_stat/total/transaction_latencies` GA ** _(project)_**   
Transaction latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total seconds takenfrom the first operation of the transaction to commit or abort. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
  
### storage

Metrics from [Cloud Storage](https://docs.cloud.google.com/storage/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `storage.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`anywhere_cache/ingested_bytes_count` BETA ** _(project)_**   
Ingested Raw Bytes   
`DELTA`, `INT64`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta number of raw bytes (successfully) ingested into the cache, broken down by zone. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`cache_zone`: The zone of the cache being accessed.   
`anywhere_cache_zone`: The zone of the Anywhere Cache used to serve the request.   
`anywhere_cache/request_count` BETA ** _(project)_**   
Request Count for Anywhere Cache   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of API calls, grouped by the API method name, response code, cache zone, and cache hit. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: The response code of the requests.   
`anywhere_cache_zone`: The zone of the Anywhere Cache used to serve the request.   
`anywhere_cache_hit`: (BOOL) Whether the request was served from Anywhere Cache.   
`method`: The name of the API method called.   
`anywhere_cache/sent_bytes_count` BETA ** _(project)_**   
Sent Bytes For Anywhere Cache   
`DELTA`, `INT64`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of bytes sent over the network, grouped by the API method name, response code, cache zone, and cache hit status. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: The response code of the requests.   
`anywhere_cache_zone`: The zone of the Anywhere Cache used to serve the request.   
`anywhere_cache_hit`: (BOOL) Whether the request was served from Anywhere Cache.   
`method`: The name of the API method called.   
`anywhere_cache_metering/cache_storage_bytes_count` GA ** _(project)_**   
Bytes in Cache   
`GAUGE`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Number of bytes in cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`anywhere_cache_metering/cache_storage_kbsec_count` GA ** _(project)_**   
Bytes in Anywhere Cache over time in Kibibyte-secs.   
`DELTA`, `INT64`, `KiBy.s`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _The delta of Anywhere Cache Storage in Kibibyte-secs broken down by Anywhere Cache zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`anywhere_cache_metering/eviction_byte_count` GA ** _(project)_**   
Evicted Bytes   
`DELTA`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Delta number of bytes evicted from cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`anywhere_cache_metering/ingested_billable_bytes_count` GA ** _(project)_**   
Ingested Billable Bytes   
`DELTA`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Delta number of billable bytes (successfully) ingested into the cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`api/lro_count` GA ** _(project)_**   
Operation count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Count of completed long-running operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`type`: Operation type, such as "bulk-restore-objects" or "rename-folder".   
`canonical_code`: Canonical code of the operation.error field, such as "OK" or "CANCELLED".   
`api/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of API calls, grouped by the API method name and response code. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: The response code of the requests.   
`method`: The name of the API method called.   
`authn/authentication_count` GA ** _(project)_**   
Authentication count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Count of HMAC/RSA signed requests grouped by authentication method and access id. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`authentication_method`: The authentication method (HMAC/RSA) used for the request.   
`response_code`: The response code of the requests.   
`method`: The name of the API method called.   
`access_id`: The access id of the authentication key.   
`authz/acl_based_object_access_count` GA ** _(project)_**   
Object-ACL based access count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of requests that result in an object being granted access solely due to object ACLs. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`authz/acl_operations_count` GA ** _(project)_**   
ACLs usage   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Usage of ACL operations broken down by type. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`acl_operation`: Type of ACL operation.   
`authz/object_specific_acl_mutation_count` GA ** _(project)_**   
Object ACL changes   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of changes made to object specific ACLs. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`auto_annotate/operations/model_count` BETA ** _(project)_**   
Executed Models Count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of models executed in the bucket during the time window, grouped by model_name, model_version, and status. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`status`: Enrichment processing status, e.g. "SUCCESS", "FAILURE".   
`model_version`: The version of the model used.   
`model_name`: The name of the model used for enrichment.   
`auto_annotate/operations/pending_objects` BETA ** _(project)_**   
Pending Objects Count   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of objects pending enrichment in the bucket. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`auto_annotate/operations/processed_object_count` BETA ** _(project)_**   
Processed Objects Count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of objects processed by object enrichments during the time window. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`auto_annotate/operations/request_count` BETA ** _(project)_**   
Executed API Requests Count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of API calls made during the time window, grouped by method and response_code. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`method`: The name of the API method called.   
`response_code`: The response code of the requests.   
`auto_annotate/storage/annotated_objects` BETA ** _(project)_**   
Objects Enriched Snapshot   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Current snapshot of all objects stored in the bucket that have any model enrichments, grouped by type and data_locations._   
`type`: The type of the object. For example, 'live-object'.   
`data_locations`: A comma-separated list of locations where the data is stored. For example, 'US-CENTRAL1-A'.   
`auto_annotate/storage/model_outputs` BETA ** _(project)_**   
Models Enriched Snapshot   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of model outputs stored in the bucket, grouped by model_name, model_version, status, type, and data_locations._   
`status`: Model processing status, e.g. "SUCCESS", "FAILURE".   
`model_version`: The version of the model used.   
`model_name`: The name of the model used for enrichment.   
`type`: The type of the object. For example, 'live-object'.   
`data_locations`: A comma-separated list of locations where the data is stored. For example, 'US-CENTRAL1-A'.   
`autoclass/transition_operation_count` GA ** _(project)_**   
Autoclass transition count   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of storage class transition operations initiated by Autoclass. Sampled every 300 seconds. After sampling, data is not visible for up to 1200 seconds._   
`source_storage_class`: The source storage class of the transition.   
`destination_storage_class`: The destination storage class of the transition.   
`autoclass/transitioned_bytes_count` GA ** _(project)_**   
Autoclass transitioned bytes count   
`DELTA`, `INT64`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total bytes transitioned by Autoclass. Sampled every 300 seconds. After sampling, data is not visible for up to 1200 seconds._   
`source_storage_class`: The source storage class of the transition.   
`destination_storage_class`: The destination storage class of the transition.   
`client/grpc/client/attempt/duration` DEPRECATED ** _(project)_**   
End-to-end time taken to complete an RPC attempt   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[storage.googleapis.com/Client](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Client)** |  _End-to-end time taken to complete an RPC attempt including the time it takes to pick a subchannel._   
`grpc_lb_locality`: The locality to which the traffic is being sent. This will be set to the resolver attribute passed down from the weighted_target policy, or the empty string if the resolver attribute is unset.   
`grpc_status`: gRPC server status code received, e.g. "OK", "CANCELLED", "DEADLINE_EXCEEDED".   
`grpc_method`: Full gRPC method name, including package, service and method.   
`grpc_target`: Canonicalized target URI used when creating gRPC Channel.   
`client/grpc/client/attempt/rcvd_total_compressed_message_size` DEPRECATED ** _(project)_**   
Total bytes (compressed but not encrypted) received across all response messages (metadata excluded) per RPC attempt   
`CUMULATIVE`, `DISTRIBUTION`, `By`   
**[storage.googleapis.com/Client](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Client)** |  _Total bytes (compressed but not encrypted) received across all response messages (metadata excluded) per RPC attempt; does not include grpc or transport framing bytes._   
`grpc_lb_locality`: The locality to which the traffic is being sent. This will be set to the resolver attribute passed down from the weighted_target policy, or the empty string if the resolver attribute is unset.   
`grpc_status`: gRPC server status code received, e.g. "OK", "CANCELLED", "DEADLINE_EXCEEDED".   
`grpc_method`: Full gRPC method name, including package, service and method.   
`grpc_target`: Canonicalized target URI used when creating gRPC Channel.   
`client/grpc/client/attempt/sent_total_compressed_message_size` DEPRECATED ** _(project)_**   
Total bytes (compressed but not encrypted) sent across all request messages (metadata excluded) per RPC attempt   
`CUMULATIVE`, `DISTRIBUTION`, `By`   
**[storage.googleapis.com/Client](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Client)** |  _Total bytes (compressed but not encrypted) sent across all request messages (metadata excluded) per RPC attempt; does not include grpc or transport framing bytes._   
`grpc_lb_locality`: The locality to which the traffic is being sent. This will be set to the resolver attribute passed down from the weighted_target policy, or the empty string if the resolver attribute is unset.   
`grpc_status`: gRPC server status code received, e.g. "OK", "CANCELLED", "DEADLINE_EXCEEDED".   
`grpc_method`: Full gRPC method name, including package, service and method.   
`grpc_target`: Canonicalized target URI used when creating gRPC Channel.   
`client/grpc/client/attempt/started` DEPRECATED ** _(project)_**   
The total number of RPC attempts started   
`CUMULATIVE`, `INT64`, `{attempt}`   
**[storage.googleapis.com/Client](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Client)** |  _The total number of RPC attempts started, including those that have not completed._   
`grpc_method`: Full gRPC method name, including package, service and method.   
`grpc_target`: Canonicalized target URI used when creating gRPC Channel.   
`client/grpc/client/call/duration` DEPRECATED ** _(project)_**   
End-to-end time the gRPC library takes to complete an RPC from the application’s perspective.   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[storage.googleapis.com/Client](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Client)** |  _This metric aims to measure the end-to-end time the gRPC library takes to complete an RPC from the application’s perspective._   
`grpc_status`: gRPC server status code received, e.g. "OK", "CANCELLED", "DEADLINE_EXCEEDED".   
`grpc_method`: Full gRPC method name, including package, service and method.   
`grpc_target`: Canonicalized target URI used when creating gRPC Channel.   
`network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of bytes received over the network, grouped by the API method name and response code. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: The response code of the requests.   
`method`: The name of the API method called.   
`network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of bytes sent over the network, grouped by the API method name and response code. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: The response code of the requests.   
`method`: The name of the API method called.   
`quota/anywhere_cache_storage_size/exceeded` GA ** _(project)_**   
Anywhere Cache Storage Size quota exceeded error   
`DELTA`, `INT64`, `1`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Number of attempts to exceed the limit on quota metric storage.googleapis.com/anywhere_cache_storage_size. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`anywhere_cache_id`: The ID of the cache.   
`quota/anywhere_cache_storage_size/limit` GA ** _(project)_**   
Anywhere Cache Storage Size quota limit   
`GAUGE`, `INT64`, `KiBy`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Current limit on quota metric storage.googleapis.com/anywhere_cache_storage_size. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`anywhere_cache_id`: The ID of the cache.   
`quota/anywhere_cache_storage_size/usage` GA ** _(project)_**   
Anywhere Cache Storage Size quota usage   
`GAUGE`, `INT64`, `KiBy`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Current usage on quota metric storage.googleapis.com/anywhere_cache_storage_size. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`anywhere_cache_id`: The ID of the cache.   
`quota/dualregion_anywhere_cache_egress_bandwidth/limit` GA ** _(project)_**   
Dualregion Anywhere Cache Egress Bandwidth quota limit   
`GAUGE`, `INT64`, `bit`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current limit on quota metric storage.googleapis.com/dualregion_anywhere_cache_egress_bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`dualregion_location`: The dualregion location of the GCS bucket.   
`quota/dualregion_anywhere_cache_egress_bandwidth/usage` GA ** _(project)_**   
Dualregion Anywhere Cache Egress Bandwidth quota usage   
`DELTA`, `INT64`, `bit`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current usage on quota metric storage.googleapis.com/dualregion_anywhere_cache_egress_bandwidth. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`dualregion_location`: The dualregion location of the GCS bucket.   
`quota/dualregion_google_egress_bandwidth/limit` GA ** _(project)_**   
Dualregion Google Egress Bandwidth quota limit   
`GAUGE`, `INT64`, `bit`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current limit on quota metric storage.googleapis.com/dualregion_google_egress_bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`dualregion_location`: The dualregion location of the GCS bucket.   
`quota/dualregion_google_egress_bandwidth/usage` GA ** _(project)_**   
Dualregion Google Egress Bandwidth quota usage   
`DELTA`, `INT64`, `bit`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current usage on quota metric storage.googleapis.com/dualregion_google_egress_bandwidth. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`dualregion_location`: The dualregion location of the GCS bucket.   
`quota/dualregion_internet_egress_bandwidth/limit` GA ** _(project)_**   
Dualregion Internet Egress Bandwidth quota limit   
`GAUGE`, `INT64`, `bit`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current limit on quota metric storage.googleapis.com/dualregion_internet_egress_bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`dualregion_location`: The dualregion location of the GCS bucket.   
`quota/dualregion_internet_egress_bandwidth/usage` GA ** _(project)_**   
Dualregion Internet Egress Bandwidth quota usage   
`DELTA`, `INT64`, `bit`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current usage on quota metric storage.googleapis.com/dualregion_internet_egress_bandwidth. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`dualregion_location`: The dualregion location of the GCS bucket.   
`quota/rapid_cache_storage_size/exceeded` GA ** _(project)_**   
Quota Limit Exceeded   
`DELTA`, `INT64`, `1`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Number of attempts to exceed the limit on quota metric storage.googleapis.com/rapid_cache_storage_size._   
`anywhere_cache_id`: The ID of the cache.   
`limit_name`: The name of the quota limit.   
`quota/rapid_cache_storage_size/limit` GA ** _(project)_**   
Quota Limit   
`GAUGE`, `INT64`, `1`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Current limit on quota metric storage.googleapis.com/rapid_cache_storage_size._   
`anywhere_cache_id`: The ID of the cache.   
`limit_name`: The name of the quota limit.   
`quota/rapid_cache_storage_size/usage` GA ** _(project)_**   
Quota Usage   
`GAUGE`, `INT64`, `1`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Current usage on quota metric storage.googleapis.com/rapid_cache_storage_size._   
`anywhere_cache_id`: The ID of the cache.   
`limit_name`: The name of the quota limit.   
`quota/total_core_bytes/exceeded` ALPHA ** _(project)_**   
Total Storage Size for Core Buckets (GiB) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Number of attempts to exceed the limit on quota metric storage.googleapis.com/total_core_bytes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`bucket_location`: The location of the bucket.   
`quota/total_core_bytes/limit` ALPHA ** _(project)_**   
Total Storage Size for Core Buckets (GiB) quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current limit on quota metric storage.googleapis.com/total_core_bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`bucket_location`: The location of the bucket.   
`quota/total_core_bytes/usage` ALPHA ** _(project)_**   
Total Storage Size for Core Buckets (GiB) quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[storage.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Project)** |  _Current usage on quota metric storage.googleapis.com/total_core_bytes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`bucket_location`: The location of the bucket.   
`rapid_cache_metering/cache_storage_bytes_count` GA ** _(project)_**   
Bytes in Cache   
`GAUGE`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Number of bytes in cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_metering/cache_storage_kbsec_count` GA ** _(project)_**   
Bytes in Rapid Cache over time in Kibibyte-secs.   
`DELTA`, `INT64`, `KiBy.s`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _The delta of Rapid Cache Storage in Kibibyte-secs broken down by Rapid Cache zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_metering/eviction_byte_count` GA ** _(project)_**   
Evicted Bytes   
`DELTA`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Delta number of bytes evicted from cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_metering/ingested_billable_bytes_count` GA ** _(project)_**   
Ingested Billable Bytes   
`DELTA`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Delta number of billable bytes (successfully) ingested into the cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_ultra_metering/cache_storage_bytes_count` BETA ** _(project)_**   
Bytes in Cache   
`GAUGE`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Number of bytes in cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_ultra_metering/cache_storage_kbsec_count` BETA ** _(project)_**   
Bytes in Rapid Cache Ultra over time in Kibibyte-secs.   
`DELTA`, `INT64`, `KiBy.s`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _The delta of Rapid Cache Ultra Storage in Kibibyte-secs broken down by Rapid Cache Ultra zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_ultra_metering/eviction_byte_count` BETA ** _(project)_**   
Evicted Bytes   
`DELTA`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Delta number of bytes evicted from cache, broken down by zone. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`rapid_cache_ultra_metering/ingested_billable_bytes_count` BETA ** _(project)_**   
Ingested Billable Bytes   
`DELTA`, `INT64`, `By`   
**[storage.googleapis.com/Storage](https://docs.cloud.google.com/monitoring/api/resources#tag_storage.googleapis.com/Storage)** |  _Delta number of billable bytes (successfully) ingested into the cache, broken down by zone and ingestion source. Sampled every 3600 seconds. After sampling, data is not visible for up to 28800 seconds._   
`cache_zone`: Cache zone.   
`ingestion_source`: Ingestion source.   
`replication/meeting_rpo` GA ** _(project)_**   
Meeting RPO   
`GAUGE`, `BOOL`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _A boolean value of whether objects are meeting RPO or not. For ASYNC_TURBO, RPO is 15 minutes; For DEFAULT, RPO is 12 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`rpo`: Recovery Point Objective of the bucket, one of [ASYNC_TURBO - turbo replication, DEFAULT - default replication].   
`replication/missing_rpo_minutes_last_30d` GA ** _(project)_**   
Minutes missing Recovery Point Objective (RPO) in last 30d   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of minutes where the Recovery Point Objective (RPO) was missed, as measured over the most recent 30 days. The metric is delayed by storage.googleapis.com/replication/v2/time_since_metrics_updated. Sampled every 60 seconds. After sampling, data is not visible for up to 3720 seconds._   
`rpo`: Recovery Point Objective of the bucket, one of [ASYNC_TURBO - turbo replication, DEFAULT - default replication].   
`replication/object_replications_last_30d` DEPRECATED ** _(project)_**   
Object replications in last 30d   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of object replications, as measured over the most recent 30 days. The metric can be broken down by whether each object replication was meeting or missing Recovery Point Objective (RPO). The metric is delayed by storage.googleapis.com/replication/time_since_metrics_updated. Sampled every 60 seconds. After sampling, data is not visible for up to 3720 seconds._   
`rpo`: Recovery Point Objective of the bucket, one of [ASYNC_TURBO - turbo replication, DEFAULT - default replication].   
`meeting_rpo`: (BOOL) Whether the object replication was meeting Recovery Point Objective (RPO).   
`replication/time_since_metrics_updated` DEPRECATED ** _(project)_**   
Time since replication metrics were updated   
`GAUGE`, `INT64`, `s`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Seconds since the last time when storage.googleapis.com/replication/* metrics were calculated. Sampled every 60 seconds. After sampling, data is not visible for up to 3720 seconds._   
`rpo`: Recovery Point Objective of the bucket, one of [ASYNC_TURBO - turbo replication, DEFAULT - default replication].   
`replication/turbo_max_delay` GA ** _(project)_**   
Maximum delay in Turbo replication   
`GAUGE`, `INT64`, `s`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delay represents the age in seconds of the oldest object that has not been replicated. Objects uploaded before this time have been replicated. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`replication/v2/object_replications_last_30d` GA ** _(project)_**   
Object replications in last 30d   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of object replications, as measured over the most recent 30 days. The metric can be broken down by whether each object replication was meeting or missing the design target. The metric is delayed by storage.googleapis.com/replication/v2/time_since_metrics_updated. Sampled every 60 seconds. After sampling, data is not visible for up to 3720 seconds._   
`rpo`: Recovery Point Objective of the bucket, one of [ASYNC_TURBO - turbo replication, DEFAULT - default replication].   
`target`: Replication design target. ASYNC_TURBO has two design targets - 5 min RPO and 15 min RPO. DEFAULT has two design targets - 99.9% of newly written objects within 1 hr, and 12 hour RPO.   
`meeting_target`: (BOOL) Whether the object replication was meeting the design target.   
`replication/v2/time_since_metrics_updated` GA ** _(project)_**   
Time since replication metrics were updated   
`GAUGE`, `INT64`, `s`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Seconds since the last time when metric storage.googleapis.com/replication/missing_rpo_minutes_last_30dand /replication/v2/object_replications_last_30d were calculated. Sampled every 60 seconds. After sampling, data is not visible for up to 3720 seconds._   
`rpo`: Recovery Point Objective of the bucket, one of [ASYNC_TURBO - turbo replication, DEFAULT - default replication].   
`target`: Replication design target. ASYNC_TURBO has two design targets - 5 min RPO and 15 min RPO. DEFAULT has two design targets - 99.9% of newly written objects within 1 hr, and 12 hour RPO.   
`storage/object_count` GA ** _(project)_**   
Object count   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of objects per bucket, grouped by storage class. Soft-deleted objects are not included in the total; use the updated v2 metric for a breakdown of total usage including soft-deleted objects. This value is measured once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the day. Buckets with no objects in them are not tracked by this metric. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 690 seconds._   
`storage_class`: Storage class of the data.   
`storage/total_byte_seconds` GA ** _(project)_**   
Total byte seconds   
`GAUGE`, `DOUBLE`, `By.s`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total daily storage in byte*seconds used by the bucket, grouped by storage class. Soft-deleted objects are not included in the total; use the updated v2 metric for a breakdown of total usage including soft-deleted objects. This value is measured once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the day. Buckets with no objects in them are not tracked by this metric. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 690 seconds._   
`storage_class`: Storage class of the data.   
`storage/total_bytes` GA ** _(project)_**   
Total bytes   
`GAUGE`, `DOUBLE`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total size of all objects in the bucket, grouped by storage class. Soft-deleted objects are not included in the total; use the updated v2 metric for a breakdown of total usage including soft-deleted objects. This value is measured once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the day. Buckets with no objects in them are not tracked by this metric. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 690 seconds._   
`storage_class`: Storage class of the data.   
`storage/v2/deleted_bytes` GA ** _(project)_**   
Deleted Bytes (v2)   
`DELTA`, `INT64`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Delta count of deleted bytes per bucket, grouped by storage class. This value is measured and reported once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. On days with no deletes, no datapoint is exported for this metric. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._   
`storage_class`: Storage class of the data.   
`storage/v2/total_byte_seconds` GA ** _(project)_**   
Total byte seconds (v2)   
`GAUGE`, `DOUBLE`, `By.s`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total daily storage in byte*seconds used by the bucket, grouped by storage class and type where type can be live-object, noncurrent-object, soft-deleted-object and multipart-upload. This value is measured once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the day. Buckets with no objects in them are not tracked by this metric. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 690 seconds._   
`storage_class`: Storage class of the data.   
`type`: Type of the data.   
`storage/v2/total_bytes` GA ** _(project)_**   
Total bytes (v2)   
`GAUGE`, `DOUBLE`, `By`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total size of all objects and multipart-uploads in the bucket, grouped by storage class and type where type can be live-object, noncurrent-object, soft-deleted-object and multipart-upload. This value is measured once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the day. Buckets with no objects in them are not tracked by this metric. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 690 seconds._   
`storage_class`: Storage class of the data.   
`type`: Type of the data.   
`storage/v2/total_count` GA ** _(project)_**   
Total count (v2)   
`GAUGE`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _Total number of objects and multipart-uploads per bucket, grouped by storage class and type where type can be live-object, noncurrent-object, soft-deleted-object and multipart-upload. This value is measured once per day, and there might be a delay after measuring before the value becomes available in Cloud Monitoring. Once available, the value is repeated at each sampling interval throughout the day. Buckets with no objects in them are not tracked by this metric. For this metric, the sampling period is a reporting period, not a measurement period. Sampled every 300 seconds. After sampling, data is not visible for up to 690 seconds._   
`storage_class`: Storage class of the data.   
`type`: Type of the data.   
  
### storagebatchoperations

Metrics from [Cloud Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). Launch stages of these metrics: ALPHA

The "metric type" strings in this table must be prefixed with `storagebatchoperations.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/concurrent/bucket_operations/exceeded` ALPHA ** _(project)_**   
Bucket Operations concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _Concurrent exceeded on quota metric storagebatchoperations.googleapis.com/bucket_operations. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`job_id`: The unique name of the batch operation job.   
`quota/concurrent/bucket_operations/limit` ALPHA ** _(project)_**   
Bucket Operations concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _Concurrent limit on quota metric storagebatchoperations.googleapis.com/bucket_operations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`job_id`: The unique name of the batch operation job.   
`quota/concurrent/bucket_operations/usage` ALPHA ** _(project)_**   
bucket_operations usage   
`GAUGE`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`time_window`: The window size for concurrent operation limits.   
`job_id`: The number of job_id items.   
`quota/concurrent/single_bucket_dry_run_jobs/exceeded` ALPHA ** _(project)_**   
Single Bucket Dry Run Jobs concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _Concurrent exceeded on quota metric storagebatchoperations.googleapis.com/single_bucket_dry_run_jobs. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/single_bucket_dry_run_jobs/limit` ALPHA ** _(project)_**   
Single Bucket Dry Run Jobs concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _Concurrent limit on quota metric storagebatchoperations.googleapis.com/single_bucket_dry_run_jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/single_bucket_dry_run_jobs/usage` ALPHA ** _(project)_**   
single_bucket_dry_run_jobs usage   
`GAUGE`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`time_window`: The window size for concurrent operation limits.   
`quota/concurrent/single_bucket_jobs/exceeded` ALPHA ** _(project)_**   
Single Bucket Jobs concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _Concurrent exceeded on quota metric storagebatchoperations.googleapis.com/single_bucket_jobs. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/single_bucket_jobs/limit` ALPHA ** _(project)_**   
Single Bucket Jobs concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _Concurrent limit on quota metric storagebatchoperations.googleapis.com/single_bucket_jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/single_bucket_jobs/usage` ALPHA ** _(project)_**   
single_bucket_jobs usage   
`GAUGE`, `INT64`, `1`   
**[storagebatchoperations.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_storagebatchoperations.googleapis.com/Location)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`time_window`: The window size for concurrent operation limits.   
  
### storagetransfer

Metrics from [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `storagetransfer.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`agent/connected` BETA ** _(project)_**   
Agent connected status   
`GAUGE`, `BOOL`, ``   
**[transfer_service_agent](https://docs.cloud.google.com/monitoring/api/resources#tag_transfer_service_agent)** |  _Indicates whether or not a Transfer Service agent is connected. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`agent/transferred_bytes_count` BETA ** _(project)_**   
Agent transfer delta   
`DELTA`, `INT64`, `By`   
**[transfer_service_agent](https://docs.cloud.google.com/monitoring/api/resources#tag_transfer_service_agent)** |  _Delta of bytes transferred by a Transfer Service agent. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`transferjob/copied_bytes_count` BETA ** _(project)_**   
Copied bytes count   
`DELTA`, `INT64`, `By`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of bytes copied to the data sink. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status of copying the bytes; can be 'succeeded', 'skipped' due to sync, or 'failed'.   
`transferjob/copied_objects_count` BETA ** _(project)_**   
Copied objects count   
`DELTA`, `INT64`, `1`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of objects copied to the data sink. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status of copying the objects; can be 'succeeded', 'skipped' due to sync, or 'failed'.   
`transferjob/deleted_bytes_count` BETA ** _(project)_**   
Deleted bytes count   
`DELTA`, `INT64`, `By`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of bytes deleted from the data source or sink. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status of deleting the bytes; can be 'succeeded' or 'failed'.   
`origin`: The location where the bytes are deleted; can be 'source' or 'sink'.   
`transferjob/deleted_objects_count` BETA ** _(project)_**   
Deleted objects count   
`DELTA`, `INT64`, `1`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of objects deleted from the data source or sink. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status of deleting the objects; can be 'succeeded' or 'failed'.   
`origin`: The location where the objects are deleted; can be 'source' or 'sink'.   
`transferjob/error_count` BETA ** _(project)_**   
Error count   
`DELTA`, `INT64`, `1`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of errors encountered during the transfer, grouped by canonical error code. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`code`: The canonical error code of the error, such as 'NOT_FOUND' or 'PERMISSION_DENIED'.   
`transferjob/found_bytes_count` BETA ** _(project)_**   
Found bytes count   
`DELTA`, `INT64`, `By`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of bytes found that are scheduled to be transferred or deleted, excluding any that are filtered based on object conditions or skipped due to sync. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`origin`: The location where the bytes are found; can be 'source' or 'sink'.   
`transferjob/found_objects_count` BETA ** _(project)_**   
Found objects count   
`DELTA`, `INT64`, `1`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Number of objects found that are scheduled to be transferred or deleted, excluding any that are filtered based on object conditions or skipped due to sync. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`origin`: The location where the objects are found; can be 'source' or 'sink'.   
`transferjob/object_replication_count` BETA ** _(project)_**   
Replicated objects count   
`DELTA`, `INT64`, `1`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _The number of objects replicated via Cross-bucket replication. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status of the object replication can be 'succeeded' or 'failed'.   
`source_bucket`: The name of the source bucket.   
`destination_bucket`: The name of the destination bucket.   
`transferjob/replication_latency` BETA ** _(project)_**   
Replication latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[storage_transfer_job](https://docs.cloud.google.com/monitoring/api/resources#tag_storage_transfer_job)** |  _Completion latency for the object to be replicated via Cross-bucket replication. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`source_bucket`: The name of the source bucket.   
`destination_bucket`: The name of the destination bucket.   
  
### telcoautomation

Metrics from [Telecom Network Automation](https://docs.cloud.google.com/telecom-network-automation). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `telcoautomation.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`deployment/update_count` BETA ** _(project)_**   
Deployment Updates   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Total count of the 'updates' to the NFDeployment, with specific status codes._   
`source`: The source of the status could be deployment creation, deletion or an EdgeEvent.   
`status`: Status of the update.   
`deployment/update_failures` BETA ** _(project)_**   
Deployment Update Failures   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Total count of the 'updates' failed to be written._  
`edgecontainer/request_count` BETA ** _(project)_**   
Edgecontainer Requests   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Requests to EdgeContainer API._   
`resource_type`: The type of resource (EdgeCluster, EdgeMahcine etc.) that request is based upon.   
`operation_type`: The operation type (create, delete etc.) of the request.   
`status`: Status of the request.   
`edgecontainer/update_count` BETA ** _(project)_**   
Edgecontainer Updates   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Total count of the 'updates' to the EdgeContainer CRs, with specific status code._   
`resource_type`: The type of resource: EdgeCluster, EdgeMahcine etc.   
`status`: Status of the update.   
`edgecontainer/update_failures` BETA ** _(project)_**   
Edgecontainer Update Failures   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Total count of the 'updates' failed to be written._  
`edgenetwork/request_count` BETA ** _(project)_**   
Edgenetwork Requests   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Requests to EdgeNetwork API._   
`resource_type`: The type of resource (EdgeRouter, EdgeSubnet etc.) that request is based upon.   
`operation_type`: The operation type (create, delete etc.) of the request.   
`status`: Status of the request.   
`edgenetwork/update_count` BETA ** _(project)_**   
Edgenetwork Updates   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Total count of the 'updates' to the EdgeNetwork CRs, with specific status code._   
`resource_type`: The type of resource: EdgeRouter, EdgeSubnet etc.   
`status`: Status of the update.   
`edgenetwork/update_failures` BETA ** _(project)_**   
Edgenetwork Update Failures   
`CUMULATIVE`, `INT64`, `1`   
**[telcoautomation.googleapis.com/OrchestrationCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_telcoautomation.googleapis.com/OrchestrationCluster)** |  _Total count of the 'updates' failed to be written._  
  
### tpu

Metrics from [Cloud TPU](https://docs.cloud.google.com/tpu/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `tpu.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`accelerator/duty_cycle` GA ** _(project)_**   
Accelerator Duty Cycle   
`GAUGE`, `DOUBLE`, `%`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Percentage of time over the sample period during which the accelerator was actively processing. Values are in the range of [0,100]._   
`accelerator_id`: Device Id of Accelerator.   
`accelerator/memory_bandwidth_utilization` GA ** _(project)_**   
Accelerator Memory Bandwidth Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Current percentage of the accelerator memory bandwidth that is being used. Computed by dividing the memory bandwidth used over a sample period by the maximum supported bandwidth over the same sample period._   
`accelerator_id`: Device Id of Accelerator.   
`accelerator/memory_total` GA ** _(project)_**   
Accelerator Total Memory   
`GAUGE`, `INT64`, `By`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Total accelerator memory currently allocated in bytes._   
`accelerator_id`: Device Id of Accelerator.   
`accelerator/memory_used` GA ** _(project)_**   
Accelerator Memory Used   
`GAUGE`, `INT64`, `By`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Total accelerator memory currently used in bytes._   
`accelerator_id`: Device Id of Accelerator.   
`accelerator/tensorcore_utilization` GA ** _(project)_**   
Accelerator TensorCore Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Current percentage of the Tensorcore that is utilized. Computed by dividing the Tensorcore operations that were performed over a sample period by the supported number of Tensorcore operations over the same sample period._   
`accelerator_id`: Device Id of Accelerator.   
`container/cpu/utilization` BETA ** _(project)_**   
Container CPU utilization   
`GAUGE`, `DOUBLE`, `%`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Current CPU utilization of the docker container on the TPU worker. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`container_name`: The docker container name.   
`container/memory/usage` BETA ** _(project)_**   
Container memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Current memory usage of the docker container on the TPU worker. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`container_name`: The docker container name.   
`cpu/utilization` BETA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `%`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Current CPU utilization on the TPU worker, represented as a percentage. Values are typically numbers between 0.0 and 100.0, but might exceed 100.0. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`core`: The CPU core in use.   
`instance/interruption_count` BETA ** _(project)_**   
Interruption Count   
`GAUGE`, `INT64`, `1`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Interruptions are system evictions of infrastructure while the customer is in control of that infrastructure. This metric is the current count of interruptions by type and reason. The stream is often undefined when the count is zero. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`instance_name`: The name of the VM instance.   
`interruption_type`: The top-level interruption type.   
`interruption_reason`: The reason for the interruption.   
`instance/uptime_total` GA ** _(project)_**   
Uptime Total   
`GAUGE`, `INT64`, `s`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Elapsed time since the VM was started, in seconds. After sampling, data is not visible for up to 120 seconds. When VM is Stopped the time is not calculated. On starting the VM again, the timer will reset to 0 for that VM. Sampled every 60 seconds. After sampling, data is not visible for up to 125 seconds._  
`memory/usage` BETA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Memory usage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`multislice/accelerator/device_to_host_transfer_latencies` GA ** _(project)_**   
Device to Host Transfer Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Cumulative distribution of device to host transfer latency for each chunk of data. A latency starts when the request for data to be transferred to the host is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`buffer_size`: Size of the buffer.   
`multislice/accelerator/host_to_device_transfer_latencies` GA ** _(project)_**   
Host to Device Transfer Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Cumulative distribution of host to device transfer latency for each chunk of data of multislice traffic. A latency starts when the request for data to be transferred to the device is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`buffer_size`: Size of the buffer.   
`multislice/network/collective_end_to_end_latencies` GA ** _(project)_**   
Collective End to End Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Cumulative distribution of end to end collective latency for multislice traffic. A latency starts when the request for the collective is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`input_size`: Size of the buffer.   
`collective_type`: Collective operation type.   
`multislice/network/dcn_transfer_latencies` GA ** _(project)_**   
DCN Transfer Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[tpu.googleapis.com/GceTpuWorker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu.googleapis.com/GceTpuWorker)** |  _Cumulative distribution of network-transfer latencies for multislice traffic. A latency starts when the request for data to be transferred over the DCN is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`buffer_size`: Size of the buffer.   
`type`: Protocol type.   
`network/received_bytes_count` BETA ** _(project)_**   
Network bytes received   
`DELTA`, `INT64`, `By`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Cumulative bytes of data this server has received over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/sent_bytes_count` BETA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Cumulative bytes of data this server has sent over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`tpu/mxu/utilization` BETA ** _(project)_**   
MXU utilization   
`GAUGE`, `DOUBLE`, `%`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _Current MXU utilization on the TPU worker, represented as a percentage. Values are typically numbers between 0.0 and 100.0. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`tpu/tensorcore/idle_duration` BETA ** _(project)_**   
Tensorcore idle duration   
`GAUGE`, `INT64`, `s`   
**[tpu_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_tpu_worker)** |  _The number of seconds tensorcore has been idle for. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`chip`: The chip ID.   
  
### trafficdirector

Metrics from [Cloud Service Mesh](https://docs.cloud.google.com/traffic-director/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `trafficdirector.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`xds/server/connected_clients` GA ** _(project)_**   
Connected clients   
`GAUGE`, `INT64`, `1`   
**[gateway_scope](https://docs.cloud.google.com/monitoring/api/resources#tag_gateway_scope)**   
**[gce_network](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_network)**   
**[mesh](https://docs.cloud.google.com/monitoring/api/resources#tag_mesh)** |  _The number of clients connected to Traffic Director. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`client_type`: Type of xDS_client connected to Traffic Director, one of [ENVOY, GRPC_JAVA, GRPC_CPP GRPC_PYTHON, GRPC_GO, GRPC_RUBY, GRPC_PHP, GRPC_NODE, GRPC_CSHARP, UNKNOWN].   
`api_version`: The xDS API version used by xDS clients to connect to Traffic Director, one of [V2, V3].   
`client_zone`: The Google Cloud zone where xDS clients are running.   
`xds/server/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of requests served by a backend service. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`source_region`: The Google Cloud region which is the source of the request.   
`destination_region`: The Google Cloud region which is the destination of the request.   
`status`: The status of the request, one of [ISSUED, SUCCESS, ERROR].   
`xds/server/request_count_by_zone` GA ** _(project)_**   
Request count by zone   
`DELTA`, `INT64`, `1`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of requests served by a backend service grouped by zone. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`source_zone`: The Google Cloud zone which is the source of the request.   
`destination_zone`: The Google Cloud zone which is the destination of the request.   
`status`: The status of the request, one of [issued, success, error].   
  
### transferappliance

Metrics from [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs). Launch stages of these metrics: ALPHA BETA

The "metric type" strings in this table must be prefixed with `transferappliance.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`appliance/cpu/load_average` ALPHA ** _(project)_**   
Average CPU load   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _CPU load average over the past sample period. Sampled every 60 seconds._   
`sample_period`: Sample collection interval to calculate CPU load, one of ["1min", "5mins", "15mins"].   
`appliance/disk/health` ALPHA ** _(project)_**   
Disk health   
`GAUGE`, `BOOL`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports the health status of each disk. Sampled every 3600 seconds._   
`id`: ID of the disk.   
`type`: Disk health evaluation standards, for example, "vendor_reported".   
`appliance/disk/partition/total_bytes` ALPHA ** _(project)_**   
Disk partition total space   
`GAUGE`, `INT64`, `By`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _The total space of each disk partition. Sampled every 60 seconds._   
`type`: The type of the disk partition, for example, "root", "metadata", "srv", "data", etc.   
`appliance/disk/partition/used_bytes` ALPHA ** _(project)_**   
Disk partiton used space   
`GAUGE`, `INT64`, `By`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _The used space of each disk partition. Sampled every 60 seconds._   
`type`: The type of the disk partition, for example, "root", "metadata", "srv", "data", etc.   
`appliance/hardware/health` ALPHA ** _(project)_**   
Hardware component health   
`GAUGE`, `BOOL`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports if the specific hardware component works properly. Sampled every 3600 seconds._   
`type`: The type of the hardware component, for example, "power_supply", "fan", "cache_vault", etc.   
`appliance/network/bytes_received` ALPHA ** _(project)_**   
Network bytes received per interface   
`GAUGE`, `INT64`, `By`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports the amount of bytes received per interface. Sampled every 60 seconds._   
`interface`: Name of the interface, for example, eno1, eno2, enp26s0f1, ens26, etc.   
`appliance/network/bytes_sent` ALPHA ** _(project)_**   
Network bytes sent per interface   
`GAUGE`, `INT64`, `By`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports the amount of bytes sent per interface. Sampled every 60 seconds._   
`interface`: Name of the interface, for example, eno1, eno2, enp26s0f1, ens26, etc.   
`appliance/network/connectivity` ALPHA ** _(project)_**   
Interface network connectivity   
`GAUGE`, `BOOL`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports if the interface network is reachable. Sampled every 60 seconds._   
`interface`: Name of the interface, for example, eno1, eno2, enp26s0f1, ens26, etc.   
`appliance/network/dns_health` ALPHA ** _(project)_**   
DNS health   
`GAUGE`, `BOOL`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports if the DNS configuration works well. Sampled every 60 seconds._  
`appliance/network/packets_received` ALPHA ** _(project)_**   
Network packets received per interface   
`GAUGE`, `INT64`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports the amount of packets received per interface. Sampled every 60 seconds._   
`interface`: Name of the interface, for example, eno1, eno2, enp26s0f1, ens26, etc.   
`status`: Status of the packet transmission, one of ["success" - healthy packets; "dropped" - discarded packets; "error" - packets errors].   
`appliance/network/packets_sent` ALPHA ** _(project)_**   
Network packets sent per interface   
`GAUGE`, `INT64`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports the amount of packets sent per interface. Sampled every 60 seconds._   
`interface`: Name of the interface, for example, eno1, eno2, enp26s0f1, ens26, etc.   
`status`: Status of the packet transmission, one of ["success" - healthy packets; "dropped" - discarded packets; "error" - packets errors].   
`appliance/service/state` ALPHA ** _(project)_**   
Service state   
`GAUGE`, `BOOL`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Reports the running status of the service. Sampled every 60 seconds._   
`name`: Name of the service.   
`appliance/storage/stored_bytes` BETA ** _(project)_**   
Stored bytes   
`GAUGE`, `INT64`, `By`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _The current number of bytes stored in the storage buffer of the appliance. Sampled every 60 seconds._  
`appliance/transfer/health` BETA ** _(project)_**   
Transfer health   
`GAUGE`, `BOOL`, `1`   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Is on-prem transfer software currently running?. Sampled every 60 seconds._  
`appliance/version` ALPHA ** _(project)_**   
Appliance component version   
`GAUGE`, `BOOL`, ``   
**[transferappliance.googleapis.com/Appliance](https://docs.cloud.google.com/monitoring/api/resources#tag_transferappliance.googleapis.com/Appliance)** |  _Current version of the specific appliance component. Sampled every 300 seconds._   
`type`: Component type, for example, os, ta, samba, containerd_server, containerd_client, kubelet, etc.   
`version`: The version of the appliance component.   
  
### translationhub

Metrics from [Translation Hub](https://docs.cloud.google.com/translation-hub/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `translationhub.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/document_pages/exceeded` BETA ** _(project)_**   
Translation Hub document pages quota exceeded error   
`DELTA`, `INT64`, `1`   
**[translationhub.googleapis.com/Portal](https://docs.cloud.google.com/monitoring/api/resources#tag_translationhub.googleapis.com/Portal)** |  _Number of attempts to exceed the limit on quota metric translationhub.googleapis.com/document_pages. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`portal`: Translation Hub Portal.   
`quota/document_pages/limit` BETA ** _(project)_**   
Translation Hub document pages quota limit   
`GAUGE`, `INT64`, `d`   
**[translationhub.googleapis.com/Portal](https://docs.cloud.google.com/monitoring/api/resources#tag_translationhub.googleapis.com/Portal)** |  _Current limit on quota metric translationhub.googleapis.com/document_pages. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`portal`: Translation Hub Portal.   
`quota/document_pages/usage` BETA ** _(project)_**   
Translation Hub document pages quota usage   
`DELTA`, `INT64`, `d`   
**[translationhub.googleapis.com/Portal](https://docs.cloud.google.com/monitoring/api/resources#tag_translationhub.googleapis.com/Portal)** |  _Current usage on quota metric translationhub.googleapis.com/document_pages. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`portal`: Translation Hub Portal.   
  
### vectorsearch

Metrics from [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `vectorsearch.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`aggregate/latencies` BETA ** _(project)_**   
Aggregate Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Distribution of aggregate response latencies._   
`response_code`: The response code.   
`aggregate_method`: The aggregation method used in the request.   
`aggregate/request_bytes_count` BETA ** _(project)_**   
Aggregate Request Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in aggregate requests._   
`response_code`: The response code.   
`aggregate_method`: The aggregation method used in the request.   
`aggregate/request_count` BETA ** _(project)_**   
Aggregate Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of aggregate requests._   
`response_code`: The response code.   
`aggregate_method`: The aggregation method used in the request.   
`aggregate/response_bytes_count` BETA ** _(project)_**   
Aggregate Response Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in aggregate responses._   
`response_code`: The response code.   
`aggregate_method`: The aggregation method used in the request.   
`batch_search/latencies` BETA ** _(project)_**   
Batch Search Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Distribution of batch search response latencies._   
`response_code`: The response code.   
`combine_options`: The combine options used in the batch search request.   
`batch_search/request_bytes_count` BETA ** _(project)_**   
Batch Search Request Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in batch search requests._   
`response_code`: The response code.   
`combine_options`: The combine options used in the batch search request.   
`batch_search/request_count` BETA ** _(project)_**   
Batch Search Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of batch search requests._   
`response_code`: The response code.   
`combine_options`: The combine options used in the batch search request.   
`batch_search/response_bytes_count` BETA ** _(project)_**   
Batch Search Response Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in batch search responses._   
`response_code`: The response code.   
`combine_options`: The combine options used in the batch search request.   
`collection/latencies` BETA ** _(project)_**   
Collection Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Latency distribution for collection management requests._   
`api_method`: The API method.   
`collection/lro_count` BETA ** _(project)_**   
Collection LRO Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of completed long-running operations on collections._   
`api_method`: The API method.   
`response_code`: The response code.   
`collection/lro_durations` BETA ** _(project)_**   
Collection LRO Durations   
`DELTA`, `DISTRIBUTION`, `s`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Distribution of durations for completed long-running operations on collections._   
`api_method`: The API method.   
`response_code`: The response code.   
`collection/request_count` BETA ** _(project)_**   
Collection Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of collection management requests._   
`api_method`: The API method.   
`response_code`: The response code.   
`data_object/latencies` BETA ** _(project)_**   
DataObject Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Latency distribution for data object management requests._   
`api_method`: The API method.   
`response_code`: The response code.   
`data_object/objects` BETA ** _(project)_**   
DataObject Objects   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current number of data objects. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`data_object/objects_per_request` BETA ** _(project)_**   
DataObject Objects Per Request   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Total number of data objects touched per data object management request, summed across requests. Always 1 for single-object methods (Create/Get/Update/Delete); equals the batch size for Batch* methods._   
`api_method`: The API method.   
`response_code`: The response code.   
`data_object/request_bytes_count` BETA ** _(project)_**   
DataObject Request Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in data object management requests._   
`api_method`: The API method.   
`response_code`: The response code.   
`data_object/request_count` BETA ** _(project)_**   
DataObject Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of data object management requests._   
`api_method`: The API method.   
`response_code`: The response code.   
`data_object/response_bytes_count` BETA ** _(project)_**   
DataObject Response Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in data object management responses._   
`api_method`: The API method.   
`response_code`: The response code.   
`data_object/storage_bytes` BETA ** _(project)_**   
DataObject Storage Bytes   
`GAUGE`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current storage used by data objects in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`index/data_object_count` BETA ** _(project)_**   
Index Data Object Count   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Number of data objects currently materialized in the index. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`index/latencies` BETA ** _(project)_**   
Index Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Latency distribution for index management requests._   
`api_method`: The API method.   
`index/lro_count` BETA ** _(project)_**   
Index LRO Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Number of completed long-running operations on indexes._   
`api_method`: The API method.   
`response_code`: The response code.   
`index/lro_durations` BETA ** _(project)_**   
Index LRO Durations   
`DELTA`, `DISTRIBUTION`, `s`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Distribution of durations for completed long-running operations on indexes._   
`api_method`: The API method.   
`response_code`: The response code.   
`index/replicas` BETA ** _(project)_**   
Current Replicas   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Number of active replicas used by the Index. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`index/request_count` BETA ** _(project)_**   
Index Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Number of index management requests._   
`api_method`: The API method.   
`response_code`: The response code.   
`index/state` BETA ** _(project)_**   
Index State   
`GAUGE`, `BOOL`, `1`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _The state of an index. True if the index is in the specified state._   
`state`: The index state.   
`index/storage_bytes` BETA ** _(project)_**   
Index Storage Bytes   
`GAUGE`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Index](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Index)** |  _Storage footprint of the raw, per-data-object payload stored for the index, in bytes (includes restricts overhead). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`query/latencies` BETA ** _(project)_**   
Query Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Distribution of query response latencies._   
`response_code`: The response code.   
`query/request_bytes_count` BETA ** _(project)_**   
Query Request Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in query requests._   
`response_code`: The response code.   
`query/request_count` BETA ** _(project)_**   
Query Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of query requests._   
`response_code`: The response code.   
`query/response_bytes_count` BETA ** _(project)_**   
Query Response Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in query responses._   
`response_code`: The response code.   
`quota/batch_search_requests/exceeded` BETA ** _(project)_**   
Batch Search requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/batch_search_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/batch_search_requests/limit` BETA ** _(project)_**   
Batch Search requests quota limit   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/batch_search_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/batch_search_requests/usage` BETA ** _(project)_**   
Batch Search requests quota usage   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/batch_search_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/data_object_reads/exceeded` BETA ** _(project)_**   
Data Object read requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/data_object_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/data_object_reads/limit` BETA ** _(project)_**   
Data Object read requests quota limit   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/data_object_reads. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/data_object_reads/usage` BETA ** _(project)_**   
Data Object read requests quota usage   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/data_object_reads. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/data_object_write_bytes/exceeded` BETA ** _(project)_**   
Data Object write bytes quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/data_object_write_bytes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/data_object_write_bytes/limit` BETA ** _(project)_**   
Data Object write bytes quota limit   
`GAUGE`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/data_object_write_bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/data_object_write_bytes/usage` BETA ** _(project)_**   
Data Object write bytes quota usage   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/data_object_write_bytes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/data_object_writes/exceeded` BETA ** _(project)_**   
Data Object write requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/data_object_writes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/data_object_writes/limit` BETA ** _(project)_**   
Data Object write requests quota limit   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/data_object_writes. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/data_object_writes/usage` BETA ** _(project)_**   
Data Object write requests quota usage   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/data_object_writes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/knn_search_requests/exceeded` BETA ** _(project)_**   
KNN Search requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/knn_search_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/knn_search_requests/limit` BETA ** _(project)_**   
KNN Search requests quota limit   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/knn_search_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/knn_search_requests/usage` BETA ** _(project)_**   
KNN Search requests quota usage   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/knn_search_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/query_requests/exceeded` BETA ** _(project)_**   
Query requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/query_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/query_requests/limit` BETA ** _(project)_**   
Query requests quota limit   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/query_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/query_requests/usage` BETA ** _(project)_**   
Query requests quota usage   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/query_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/search_requests/exceeded` BETA ** _(project)_**   
Search requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of attempts to exceed the limit on quota metric vectorsearch.googleapis.com/search_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/search_requests/limit` BETA ** _(project)_**   
Search requests quota limit   
`GAUGE`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current limit on quota metric vectorsearch.googleapis.com/search_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/search_requests/usage` BETA ** _(project)_**   
Search requests quota usage   
`DELTA`, `INT64`, `1`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Current usage on quota metric vectorsearch.googleapis.com/search_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`search/latencies` BETA ** _(project)_**   
Search Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Distribution of search response latencies._   
`search_type`: The type of search: vector_search, semantic_search, text_search, unknown.   
`index_id`: The index ID used in the request.   
`response_code`: The response code.   
`search_kind`: Single/Batch search.   
`search/request_bytes_count` BETA ** _(project)_**   
Search Request Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in search requests._   
`search_type`: The type of search: vector_search, semantic_search, text_search, unknown.   
`index_id`: The index ID used in the request.   
`response_code`: The response code.   
`search_kind`: Single/Batch search.   
`search/request_count` BETA ** _(project)_**   
Search Request Count   
`DELTA`, `INT64`, `1{request}`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of search requests._   
`search_type`: The type of search: vector_search, semantic_search, text_search, unknown.   
`index_id`: The index ID used in the request.   
`response_code`: The response code.   
`search_kind`: Single/Batch search.   
`search/response_bytes_count` BETA ** _(project)_**   
Search Response Bytes   
`DELTA`, `INT64`, `By`   
**[vectorsearch.googleapis.com/Collection](https://docs.cloud.google.com/monitoring/api/resources#tag_vectorsearch.googleapis.com/Collection)** |  _Number of bytes in search responses._   
`search_type`: The type of search: vector_search, semantic_search, text_search, unknown.   
`index_id`: The index ID used in the request.   
`response_code`: The response code.   
`search_kind`: Single/Batch search.   
  
### videostitcher

Metrics from [Video Stitcher API](https://docs.cloud.google.com/video-stitcher/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `videostitcher.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`project/live_ad_insertion_count` BETA ** _(project)_**   
Live ad insertion count   
`DELTA`, `INT64`, `1`   
**[videostitcher.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_videostitcher.googleapis.com/Project)** |  _The number of ad insertions for live sessions including success and failure._   
`failed_reason`: Failure reason if the ad was not inserted successfully.   
`state`: Whether the ad insertion succeeded or failed.   
`liveconfig_id`: The ID of the liveconfig.   
`project/live_slate_insertion_count` BETA ** _(project)_**   
Live slate insertion count   
`DELTA`, `INT64`, `1`   
**[videostitcher.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_videostitcher.googleapis.com/Project)** |  _The number of slate insertions for live sessions including success and failure._   
`failed_reason`: Failure reason if the slate was not inserted successfully.   
`state`: Whether the slate insertion succeeded or failed.   
`stream_id`: The ID of the video stream.   
`project/vod_ad_insertion_count` BETA ** _(project)_**   
VOD ad insertion count   
`DELTA`, `INT64`, `1`   
**[videostitcher.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_videostitcher.googleapis.com/Project)** |  _The number of ad insertions for VOD sessions including success and failure._   
`failed_reason`: Failure reason if the ad was not inserted successfully.   
`state`: Whether the ad insertion succeeded or failed.   
`asset_id`: The ID of the video asset.   
  
### visionai

Metrics from [Vision AI](https://docs.cloud.google.com/vision-ai/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `visionai.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`platform/connected_service/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[visionai.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Instance)** |  _The number of requests sent from Vertex AI Vision App Platform to other connected GCP services._   
`service_name`: The name of the service that Vertex AI Vision App Platform connected to.   
`response_code`: The response code that Vertex AI Vision App Platform received from the service.   
`processing_type`: The type of processing for which Vertex AI Vision App Platform connected to this service.   
`node_id`: The Vertex AI Vision App Platform application node from which this connection originated.   
`platform/connected_service/request_latencies` BETA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[visionai.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Instance)** |  _The total client-side request latencies from Vertex AI Vision to other connected GCP services. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`service_name`: The name of the service that Vertex AI Vision App Platform connected to.   
`response_code`: The response code that Vertex AI Vision App Platform received from the service.   
`processing_type`: The type of processing for which Vertex AI Vision App Platform connected to this service.   
`node_id`: The Vertex AI Vision App Platform application node from which this connection originated.   
`platform/custom_model/predict_count` BETA ** _(project)_**   
Prediction count   
`DELTA`, `INT64`, `1`   
**[visionai.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Instance)** |  _The number of predictions from Vertex AI Vision App Platform._   
`response_code`: The response code that Vertex AI Vision App Platform received for the prediction.   
`node_id`: The Vertex AI Vision App Platform application node from which this prediction originated.   
`platform/custom_model/predict_latencies` BETA ** _(project)_**   
Prediction latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[visionai.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Instance)** |  _The total client-side prediction latencies from Vertex AI Vision App Platform. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: The response code that Vertex AI Vision App Platform received for the prediction.   
`node_id`: The Vertex AI Vision App Platform application node from which this prediction originated.   
`platform/instance/uptime` BETA ** _(project)_**   
Uptime   
`GAUGE`, `DOUBLE`, `ms`   
**[visionai.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Instance)** |  _The uptime of a Vertex AI Vision App Platform application instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`stream/network/received_bytes_count` BETA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[visionai.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Stream)** |  _The number of bytes received by a Vertex AI Vision stream._   
`event_id`: The event corresponding to the bytes being received.   
`stream/network/received_packets_count` BETA ** _(project)_**   
Received packets   
`DELTA`, `INT64`, `1`   
**[visionai.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Stream)** |  _The number of packets received by a Vertex AI Vision stream._   
`event_id`: The event corresponding to the packets being received.   
`stream/network/sent_bytes_count` BETA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[visionai.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Stream)** |  _The number of bytes sent by a Vertex AI Vision stream._   
`event_id`: The event corresponding to the bytes being sent.   
`stream/network/sent_packets_count` BETA ** _(project)_**   
Sent packets   
`DELTA`, `INT64`, `1`   
**[visionai.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_visionai.googleapis.com/Stream)** |  _The number of packets sent by a Vertex AI Vision stream._   
`event_id`: The event corresponding to the packets being sent.   
  
### vmwareengine

Metrics from [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `vmwareengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`network/max_utilization_percentage` BETA ** _(project)_**   
Max percentage of network usage   
`GAUGE`, `DOUBLE`, `1`   
**[vmwareengine.googleapis.com/VmwareEngineNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_vmwareengine.googleapis.com/VmwareEngineNetwork)** |  _Maximum percentage network usage for a vmware engine network across all network paths._   
`datacenter_zone`: Zone of the private clouds for this network path.   
`private_connection_name`: Private connection name if the Vmware Engine Network is legacy.   
`network/utilization` BETA ** _(project)_**   
Network usage in Mbps   
`GAUGE`, `DOUBLE`, `1`   
**[vmwareengine.googleapis.com/VmwareEngineNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_vmwareengine.googleapis.com/VmwareEngineNetwork)** |  _Total network usage for a vmware engine network across all network paths in Mbps._   
`datacenter_zone`: Zone of the private clouds for this network path.   
`private_connection_name`: Private connection name if the Vmware Engine Network is legacy.   
  
### vpcaccess

Metrics from [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `vpcaccess.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connector/cpu/utilizations` BETA ** _(project)_**   
CPU Utilizations   
`GAUGE`, `DISTRIBUTION`, `10^2.%`   
**[vpc_access_connector](https://docs.cloud.google.com/monitoring/api/resources#tag_vpc_access_connector)** |  _Distribution of CPU utilizations for instances underlying a VPC Access Connector. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`connector/instances` BETA ** _(project)_**   
Active instances   
`GAUGE`, `INT64`, `1`   
**[vpc_access_connector](https://docs.cloud.google.com/monitoring/api/resources#tag_vpc_access_connector)** |  _Total number of active instances underlying a VPC Access connector. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`connector/received_bytes_count` BETA ** _(project)_**   
Bytes received delta   
`DELTA`, `INT64`, `By`   
**[vpc_access_connector](https://docs.cloud.google.com/monitoring/api/resources#tag_vpc_access_connector)** |  _Delta of bytes transferred by a VPC Access Connector. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`connector/received_packets_count` BETA ** _(project)_**   
Packets received delta   
`DELTA`, `INT64`, `{packet}`   
**[vpc_access_connector](https://docs.cloud.google.com/monitoring/api/resources#tag_vpc_access_connector)** |  _Delta of packets received by a VPC Access Connector. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`connector/sent_bytes_count` BETA ** _(project)_**   
Bytes sent delta   
`DELTA`, `INT64`, `By`   
**[vpc_access_connector](https://docs.cloud.google.com/monitoring/api/resources#tag_vpc_access_connector)** |  _Delta of bytes transferred by a VPC Access Connector. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`connector/sent_packets_count` BETA ** _(project)_**   
Packets sent delta   
`DELTA`, `INT64`, `{packet}`   
**[vpc_access_connector](https://docs.cloud.google.com/monitoring/api/resources#tag_vpc_access_connector)** |  _Delta of packets sent by a VPC Access Connector. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
  
### vpn

Metrics from [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `vpn.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`gateway/connections` GA ** _(project)_**   
Number of connections   
`GAUGE`, `INT64`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Indicates the number of HA connections per VPN gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`configured_for_sla`: (BOOL) Whether the HA connection is fully configured for SLA.   
`gcp_service_health`: (BOOL) Whether the Google Cloud side of the HA connection is fully functional.   
`end_to_end_health`: (BOOL) Whether the HA connection is functional end-to-end.   
`network/dropped_received_packets_count` GA ** _(project)_**   
Incoming packets dropped   
`DELTA`, `INT64`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Ingress (received from peer VPN) packets dropped for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/dropped_sent_packets_count` GA ** _(project)_**   
Outgoing packets dropped   
`DELTA`, `INT64`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Egress (directed to peer VPN) packets dropped for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Ingress (received from peer VPN) bytes for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/received_packets_count` GA ** _(project)_**   
Received packets   
`DELTA`, `INT64`, `{packets}`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Ingress (received from peer VPN) packets for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: Delivery status, for example, [successful, exceeds_mtu, throttled].   
`tunnel_name`: The name of the tunnel.   
`network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Egress (directed to peer VPN) bytes for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/sent_packets_count` GA ** _(project)_**   
Sent packets   
`DELTA`, `INT64`, `{packets}`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Egress (directed to peer VPN) packets for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: Delivery status, for example, [successful, exceeds_mtu, throttled].   
`tunnel_name`: The name of the tunnel.   
`tunnel_established` GA ** _(project)_**   
Tunnel established   
`GAUGE`, `DOUBLE`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Indicates successful tunnel establishment if > 0\. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`vpn_tunnel/gateway_ip_version` GA ** _(project)_**   
Gateway IP version   
`GAUGE`, `BOOL`, ``   
**[vpn_tunnel](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_tunnel)** |  _The IP version of the HA VPN gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`gateway_ip_version`: The IP version of the HA VPN gateway.   
  
### workflows

Metrics from [Workflows](https://docs.cloud.google.com/workflows/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `workflows.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`await_callback_step_count` GA ** _(project)_**   
Await Callback Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps that wait for a callback. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`callback_requests_count` GA ** _(project)_**   
Callback Requests Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of requests made to trigger a callback. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`callback_timeout_count` GA ** _(project)_**   
Callback Timeout Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of callbacks that timed out. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`cmek_protected_workflow_count` GA ** _(project)_**   
CMEK Protected Workflow Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of workflows deployed with CMEK protection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`compute_slice_count` GA ** _(project)_**   
Compute Slice Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of compute slices executed. Steps are executed in slices of work, which depends on the of type steps being executed (e.g. HTTP requests will run separately from “assign” steps). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`type`: The type of compute slice, such as "IO_REQUEST" or "WAKEUP".   
`has_parallel`: (BOOL) Whether the workflow uses parallel steps.   
`compute_slice_latencies` GA ** _(project)_**   
Compute Slice Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies from the time a compute slice was scheduled to the time it was executed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`type`: The type of compute slice, such as "IO_REQUEST" or "WAKEUP".   
`has_parallel`: (BOOL) Whether the workflow uses parallel steps.   
`compute_step_count` GA ** _(project)_**   
Compute Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of compute steps executed (e.g. "assign" and "for" steps). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`compute_step_latencies` GA ** _(project)_**   
Compute Step Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of executed compute steps. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`create_callback_step_count` GA ** _(project)_**   
Create Callback Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps that create a callback. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`method`: The method type of the created callback, such as "POST".   
`deployment_attempt_count` GA ** _(project)_**   
Deployment Attempt Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of workflow deployment attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`result`: The status of the deployment attempts.   
`deployment_latencies` GA ** _(project)_**   
Deployment Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of workflow deployment attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`duplicate_event_count` GA ** _(project)_**   
Duplicate Event Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of duplicate event triggers received. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`event_type`: The type of the event.   
`event_time_to_ack_latencies` GA ** _(project)_**   
Event Time To Ack Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies from the time an event starts to the time the workflows service acks it. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`event_type`: The type of the event.   
`event_trigger_count` GA ** _(project)_**   
Event Trigger Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of event triggers received. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`event_type`: The type of the event.   
`result`: The result of the event trigger.   
`execution_backlog_size` GA ** _(project)_**   
Execution Backlog Size   
`GAUGE`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executions that have not started yet. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`execution_times` GA ** _(project)_**   
Execution times   
`DELTA`, `DISTRIBUTION`, `s`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Distribution of workflow execution times. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`external_step_count` GA ** _(project)_**   
External step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of executed external steps for the workflow. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._  
`finished_execution_count` GA ** _(project)_**   
Finished execution count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of finished executions for the workflow. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The execution status of the workflow.   
`revision_id`: The revision ID of the executed workflow.   
`internal_execution_error_count` GA ** _(project)_**   
Internal Execution Error Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executions that failed with an internal error. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`internal_step_count` GA ** _(project)_**   
Internal step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of executed internal steps for the workflow. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._  
`io_internal_request_count` GA ** _(project)_**   
IO Internal Request Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of I/O requests made by a Workflow to Google services. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`service_domain`: The domain of the Google service being called, such as "bigquery.googleapis.com".   
`io_step_count` GA ** _(project)_**   
IO Step Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of I/O steps executed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`io_result`: The I/O step result.   
`io_step_type`: The I/O step type.   
`destination_type`: The I/O step destination type.   
`had_system_error`: (BOOL) Whether the I/O step had a system error.   
`io_step_latencies` GA ** _(project)_**   
IO Step Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of I/O steps executed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`io_result`: The I/O step result.   
`io_step_type`: The I/O step type.   
`had_system_error`: (BOOL) Whether the I/O step had a system error.   
`kms_decrypt_latencies` GA ** _(project)_**   
KMS Decrypt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of decrypt requests to KMS by workflows for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the decrypt requests.   
`attempts`: (INT64) The attempts count of the decrypt requests.   
`kms_decrypt_request_count` GA ** _(project)_**   
KMS Decrypt Request Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of KMS decrypt requests made by the service for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the decrypt requests.   
`kms_encrypt_latencies` GA ** _(project)_**   
KMS Encrypt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Latencies of encrypt requests to KMS by workflows for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the encrypt requests.   
`attempts`: (INT64) The attempts count of the encrypt requests.   
`kms_encrypt_request_count` GA ** _(project)_**   
KMS Encrypt Request Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of KMS encrypt requests made by the service for CMEK. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`status`: The status of the encrypt requests.   
`parallel_branch_step_count` GA ** _(project)_**   
Parallel branch step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps using parallel branches. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_branch_substep_count` GA ** _(project)_**   
Parallel branch substep count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps within parallel branches. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_iteration_step_count` GA ** _(project)_**   
Parallel iteration step count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps using parallel iterations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_iteration_substep_count` GA ** _(project)_**   
Parallel iteration substep count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of executed steps within parallel iterations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`parallel_unhandled_exceptions_limit_count` GA ** _(project)_**   
Parallel unhandled exceptions limit count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of times the unhandled parallel exception limit was reached. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`pending_io_requests` GA ** _(project)_**   
Pending IO Requests   
`GAUGE`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of in-flight I/O requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`sent_bytes_count` GA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of outgoing HTTP bytes (URL, headers and body) sent by the workflow. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`started_execution_count` GA ** _(project)_**   
Started execution count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Count of started executions for the workflow. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`started_vpcsc_executions_count` GA ** _(project)_**   
Started VPC-SC Executions Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of VPC-SC restricted executions started. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
`vpcsc_protected_io_count` GA ** _(project)_**   
VPC-SC Protected IO Count   
`DELTA`, `INT64`, `1`   
**[workflows.googleapis.com/Workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_workflows.googleapis.com/Workflow)** |  _Number of I/O requests made using VPC-SC. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`revision_id`: The revision ID of the executed workflow.   
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
