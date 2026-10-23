---
url: https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o/
title: Google Cloud metrics: I through O \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:21.721740+00:00
---

# Google Cloud metrics: I through O  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Google Cloud metrics: I through O Stay organized with collections  Save and categorize content based on your preferences. 

These tables list the Google Cloud metric types whose service domain name begins with the letters `i` through `o`, such as `iam.googleapis.com`. For information about other metric types, see [Google Cloud metrics overview](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

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

### iam

Metrics from [Identity and Access Management](https://docs.cloud.google.com/iam/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `iam.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/accesspolicies/bindings_per_access_policy/exceeded` GA ** _(project)_**   
Bindings Per Access Policy quota exceeded error   
`DELTA`, `INT64`, `1`   
**[iam.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_iam.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric iam.googleapis.com/accesspolicies/bindings_per_access_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`access_policy`: uid of the access policy.   
`quota/accesspolicies/bindings_per_access_policy/limit` GA ** _(project)_**   
Bindings Per Access Policy quota limit   
`GAUGE`, `INT64`, `1`   
**[iam.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_iam.googleapis.com/Location)** |  _Current limit on quota metric iam.googleapis.com/accesspolicies/bindings_per_access_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`access_policy`: uid of the access policy.   
`quota/accesspolicies/bindings_per_access_policy/usage` GA ** _(project)_**   
Bindings Per Access Policy quota usage   
`GAUGE`, `INT64`, `1`   
**[iam.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_iam.googleapis.com/Location)** |  _Current usage on quota metric iam.googleapis.com/accesspolicies/bindings_per_access_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`access_policy`: uid of the access policy.   
`service_account/authn_events_count` GA ** _(project)_**   
Service account authentication events   
`DELTA`, `INT64`, `1`   
**[iam_service_account](https://docs.cloud.google.com/monitoring/api/resources#tag_iam_service_account)** |  _Number of authentication events for a service account. Sampled every 600 seconds. After sampling, data is not visible for up to 10800 seconds._  
`service_account/key/authn_events_count` GA ** _(project)_**   
Service account key authentication events   
`DELTA`, `INT64`, `1`   
**[iam_service_account](https://docs.cloud.google.com/monitoring/api/resources#tag_iam_service_account)** |  _Number of authentication events for a service account key. Sampled every 600 seconds. After sampling, data is not visible for up to 10800 seconds._   
`key_id`: The key ID associated with the authentication event.   
`workforce_identity_federation/count` BETA ** _(project)_**   
Workforce identity federation count   
`DELTA`, `INT64`, `1`   
**[iam.googleapis.com/WorkforcePoolProvider](https://docs.cloud.google.com/monitoring/api/resources#tag_iam.googleapis.com/WorkforcePoolProvider)** |  _Count of token exchanges using workforce identity federation._   
`result`: If the request succeeds, the value will be 'success'. Otherwise, the value will match one of the possible OAuth 2.0 error types, for instance, 'invalid_client'.   
`workload_identity_federation/count` BETA ** _(project)_**   
Workload identity federation count   
`DELTA`, `INT64`, `1`   
**[iam.googleapis.com/WorkloadIdentityPoolProvider](https://docs.cloud.google.com/monitoring/api/resources#tag_iam.googleapis.com/WorkloadIdentityPoolProvider)** |  _Count of token exchanges using workload identity federation._   
`result`: If the request succeeds, the value will be 'success'. Otherwise, the value will match one of the possible OAuth 2.0 error types, for instance, 'invalid_client'.   
`workload_identity_federation/key_usage_count` BETA ** _(project)_**   
Workload identity federation key usage count   
`DELTA`, `INT64`, `1`   
**[iam.googleapis.com/WorkloadIdentityPoolProvider](https://docs.cloud.google.com/monitoring/api/resources#tag_iam.googleapis.com/WorkloadIdentityPoolProvider)** |  _Count of times a key is used as part of workload identity federation._   
`key`: The identifier of a public key used during a workload identity federation.   
`use`: What the key was used for, one of ['verify' - verify a signature]. Additional values might be added in the future.   
  
### identitytoolkit

Metrics from [Identity Platform](https://docs.cloud.google.com/identity-platform/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `identitytoolkit.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`mfa/totp/enrollment_attempt_count` BETA ** _(project)_**   
MFA TOTP enrollment attempts   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Count of MFA TOTP enrollment attempts._   
`provider`: The identity provider for the first-factor, e.g. password, Google, Facebook, etc.   
`response_code`: (INT64) The HTTP status code.   
`mfa/totp/sign_in_challenge_attempt_count` BETA ** _(project)_**   
MFA TOTP sign in challenge attempts   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Count of MFA TOTP sign in challenge attempts._   
`provider`: The identity provider for the first-factor, e.g. password, Google, Facebook, etc.   
`response_code`: (INT64) The HTTP status code.   
`password_policy/weak_password_sign_in_count` BETA ** _(project)_**   
Weak password sign-ins   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Count of successful sign-ins with weak password._   
`client_type`: Client platform, one of [web, android, ios].   
`quota/free_daily_signin/exceeded` BETA ** _(project)_**   
Free Daily Sign-in Quota Exceeded   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_project](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_project)** |  _The number of sign-ins that have exceeded the free daily new sign-in quota._   
`pricing_tier`: The pricing tier of the identity provider used to sign in.   
`recaptcha/risk_scores` BETA ** _(project)_**   
reCAPTCHA bot detection risk score distribution   
`DELTA`, `DISTRIBUTION`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Distribution of reCAPTCHA bot scores. Scores range from 0 (high risk) to 1 (low risk)._   
`provider`: The identity provider, one of [passwordProvider, phoneProvider].   
`api_name`: The reCAPTCHA supported API name, one of [signUpPassword, signInWithPassword, getOobCode, sendVerificationCode, mfaSmsEnrollment, mfaSmsSignIn].   
`client_type`: Client platform, one of [web, android, ios].   
`recaptcha/sms_tf_risk_scores` BETA ** _(project)_**   
reCAPTCHA sms toll fraud detection risk score distribution   
`DELTA`, `DISTRIBUTION`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Distribution of reCAPTCHA sms toll fraud detection scores. Scores range from 0 (low risk) to 1 (high risk)._   
`provider`: The identity provider, one of [phoneProvider].   
`api_name`: The reCAPTCHA supported API name, one of [sendVerificationCode, mfaSmsEnrollment, mfaSmsSignIn].   
`client_type`: Client platform, one of [web, android, ios].   
`recaptcha/token_count` BETA ** _(project)_**   
reCAPTCHA token count   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Count of reCAPTCHA tokens in different states._   
`provider`: The identity provider, one of [passwordProvider, phoneProvider].   
`api_name`: The reCAPTCHA supported API name, one of [signUpPassword, signInWithPassword, getOobCode, sendVerificationCode, mfaSmsEnrollment, mfaSmsSignIn].   
`client_type`: Client platform, one of [web, android, ios].   
`token_state`: The state of a token, one of [expired, duplicate, missing, invalid, valid].   
`recaptcha/verdict_count` BETA ** _(project)_**   
reCAPTCHA verdicts count   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_tenant](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_tenant)** |  _Count of evaluation results based on the reCAPTCHA configuration._   
`provider`: The identity provider, one of [passwordProvider, phoneProvider].   
`api_name`: The reCAPTCHA supported API name, one of [signUpPassword, signInWithPassword, getOobCode, sendVerificationCode, mfaSmsEnrollment, mfaSmsSignIn].   
`client_type`: Client platform, one of [web, android, ios].   
`verdict_state`: The state of a verdict, one of [passed, failed_in_audit, failed_in_enforce].   
`usage/blocked_sms_count` BETA ** _(project)_**   
Blocked SMS   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_project](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_project)** |  _The number of SMS-based verification codes that were blocked from being sent._   
`pricing_tier`: The pricing tier of the country where the SMS is sent.   
`country_calling_code`: The country calling code of the phone number where the SMS is sent.   
`region_code`: The two-letter region code of the phone number where the SMS is sent.   
`sms_purpose`: The purpose of the SMS-based verification code (i.e. phone auth, MFA).   
`usage/daily_new_signin_count` BETA ** _(project)_**   
Daily New Sign-ins   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_project](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_project)** |  _The number of new daily active users. A sign-in or token refresh is counted as a new daily active user if the user has not previously signed in that day._   
`pricing_tier`: The pricing tier of the identity provider used to sign in.   
`is_anon`: Whether or not the sign-in is an anonymous auth sign-in.   
`usage/monthly_new_signin_count` BETA ** _(project)_**   
Monthly New Sign-ins   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_project](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_project)** |  _The number of new monthly active users. A sign-in or token refresh is counted as a new monthly active user if the user has not previously signed in that month._   
`pricing_tier`: The pricing tier of the identity provider used to sign in.   
`is_anon`: Whether or not the sign-in is an anonymous auth sign-in.   
`usage/sent_sms_count` BETA ** _(project)_**   
Sent SMS   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_project](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_project)** |  _The number of SMS-based verification codes sent._   
`pricing_tier`: The pricing tier of the country where the SMS is sent.   
`country_calling_code`: The country calling code of the phone number where the SMS is sent.   
`region_code`: The two-letter region code of the phone number where the SMS is sent.   
`sms_purpose`: The purpose of the SMS-based verification code (i.e. phone auth, MFA).   
`usage/verification_sms_count` BETA ** _(project)_**   
Verified SMS   
`DELTA`, `INT64`, `1`   
**[identitytoolkit_project](https://docs.cloud.google.com/monitoring/api/resources#tag_identitytoolkit_project)** |  _The number of successful SMS-based verifications._   
`pricing_tier`: The pricing tier of the country where the SMS is sent.   
`country_calling_code`: The country calling code of the phone number where the SMS is sent.   
`region_code`: The two-letter region code of the phone number where the SMS is sent.   
`sms_purpose`: The purpose of the SMS-based verification code (i.e. phone auth, MFA).   
  
### ids

Metrics from [Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `ids.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[ids.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_ids.googleapis.com/Endpoint)** |  _Total IDS Endpoint received bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`received_packets_count` GA ** _(project)_**   
Received packets   
`DELTA`, `INT64`, `1`   
**[ids.googleapis.com/Endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_ids.googleapis.com/Endpoint)** |  _Total IDS Endpoint received packets. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
### integrations

Metrics from [Application Integration](https://docs.cloud.google.com/application-integration). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `integrations.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`integration/execution_count` GA ** _(project)_**   
Integration execution count   
`DELTA`, `INT64`, `1`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _Count of integration executions since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Integration execution status, one of [SUCCEEDED, FAILED, CANCELLED, RETRY_ON_HOLD].   
`trigger_name`: Type of the trigger used for Integration execution, for example, "API trigger" or "Cloud Pub/Sub trigger".   
`trigger_id`: Trigger Id which triggered the execution of Integration.   
`error_enum`: Canonical code of the last error occurred during Integration execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the integration execution is a retry or a first attempt, one of [true, false].   
`integration/execution_latencies` GA ** _(project)_**   
Integration execution latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _A distribution of time taken by the integrations to complete execution. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Integration execution status, one of [SUCCEEDED, FAILED, CANCELLED, RETRY_ON_HOLD].   
`trigger_name`: Type of the trigger used for Integration execution, for example, "API trigger" or "Cloud Pub/Sub trigger".   
`trigger_id`: Trigger Id which triggered the execution of Integration.   
`error_enum`: Canonical code of the last error occurred during Integration execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the integration execution is a retry or a first attempt, one of [true, false].   
`processed_bytes_count` GA ** _(project)_**   
Processed bytes count   
`DELTA`, `INT64`, `By`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _Size of data consumed by the integration executions since the last sample. It is computed by taking the size of input and output parameters to the integration, along with the request and response payload size for Rest and Connector tasks. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`step_type`: Indicates whether the data is processed by parameters of the integration, or task request and response payload, one of [Trigger, Task].   
`step_name`: Type of the task used for processing request and response payload, or type of the trigger used for processing parameters of the integration.   
`step_id`: Task number used for processing request and response payload, or Trigger Id used for processing parameters of the integration.   
`step/execution_count` GA ** _(project)_**   
Step execution count   
`DELTA`, `INT64`, `1`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _Count of step (task or trigger) executions since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Step execution status, for example "SUCCEEDED" or "FAILED".   
`step_type`: Type of the step executed, one of [Trigger, Task].   
`step_name`: Type of the trigger or task executed, for example, "API Trigger" or "Data Mapping task".   
`step_id`: Trigger Id or task number depending upon which type of step is executed.   
`error_enum`: Canonical code of the error occurred during the step execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the step execution is a retry or a first attempt, one of [true, false].   
`is_step_external`: (BOOL) Indicates whether the task executed is internal or external, one of ["true" - external tasks such as Rest or Connector task.; "false" - internal tasks such as Data Mapper or Inline Scripting task].   
`step/execution_latencies` GA ** _(project)_**   
Step execution latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[integrations.googleapis.com/IntegrationVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_integrations.googleapis.com/IntegrationVersion)** |  _A distribution of time taken by the steps (task) to complete execution. Sampled every 60 seconds. After sampling, data is not visible for up to 86400 seconds._   
`status`: Step execution status, for example "SUCCEEDED" or "FAILED".   
`step_name`: Type of the trigger or task executed, for example, "API Trigger" or "Data Mapping task".   
`step_id`: Trigger Id or task number depending upon which type of step is executed.   
`error_enum`: Canonical code of the error occurred during the step execution, for example, "PERMISSION_DENIED" or "INVALID_ARGUMENT".   
`is_retry`: (BOOL) Indicates whether the step execution is a retry or a first attempt, one of [true, false].   
`is_step_external`: (BOOL) Indicates whether the task executed is internal or external, one of ["true" - external tasks such as Rest or Connector task.; "false" - internal tasks such as Data Mapper or Inline Scripting task].   
  
### interconnect

Metrics from [Cloud Interconnect](https://docs.cloud.google.com/interconnect/docs). For Dedicated Interconnect, Monitoring and Google Cloud collect measurements for the network/interconnect and network/attachment metric types. For Partner Interconnect, Monitoring and Google Cloud collect measurements for the network/attachment metric type only. Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `interconnect.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`network/attachment/capacity` GA ** _(project)_**   
Network Capacity   
`GAUGE`, `INT64`, `By/s`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Network Capacity of the Attachment. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/attachment/egress_dropped_packets_count` GA ** _(project)_**   
Egress dropped packets   
`DELTA`, `INT64`, `{packets}`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of outbound packets dropped since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`drop_reason`: Reason packet was dropped.   
`l3_protocol`: Layer 3 protocol.   
`network/attachment/ingress_dropped_packets_count` GA ** _(project)_**   
Ingress dropped packets   
`DELTA`, `INT64`, `{packets}`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of inbound packets dropped since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`drop_reason`: Reason packet was dropped.   
`l3_protocol`: Layer 3 protocol.   
`network/attachment/received_bytes_count` GA ** _(project)_**   
Ingress Bytes   
`DELTA`, `INT64`, `By`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of inbound bytes received. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`network/attachment/received_bytes_count_by_l3_protocol` GA ** _(project)_**   
Ingress bytes by L3 protocol   
`DELTA`, `INT64`, `By`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of inbound bytes received by L3 Protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`l3_protocol`: Layer 3 protocol.   
`network/attachment/received_packets_count` GA ** _(project)_**   
Ingress Packets   
`DELTA`, `INT64`, `{packets}`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of inbound packets received. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`network/attachment/received_packets_count_by_l3_protocol` GA ** _(project)_**   
Ingress packets by L3 protocol   
`DELTA`, `INT64`, `{packets}`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of inbound packets received by L3 Protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`l3_protocol`: Layer 3 protocol.   
`network/attachment/sent_bytes_count` GA ** _(project)_**   
Egress Bytes   
`DELTA`, `INT64`, `By`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of outbound bytes sent. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`network/attachment/sent_bytes_count_by_l3_protocol` GA ** _(project)_**   
Egress bytes by L3 protocol   
`DELTA`, `INT64`, `By`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of outbound bytes sent by L3 Protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`l3_protocol`: Layer 3 protocol.   
`network/attachment/sent_packets_count` GA ** _(project)_**   
Egress Packets   
`DELTA`, `INT64`, `{packets}`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of outbound packets sent. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`network/attachment/sent_packets_count_by_l3_protocol` GA ** _(project)_**   
Egress packets by L3 protocol   
`DELTA`, `INT64`, `{packets}`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _Number of outbound packets sent by L3 Protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`l3_protocol`: Layer 3 protocol.   
`network/interconnect/capacity` GA ** _(project)_**   
Network Capacity   
`GAUGE`, `INT64`, `By/s`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Active capacity of the interconnect. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/dropped_packets_count` GA ** _(project)_**   
Dropped Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of outbound packets dropped due to link congestion. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/link/aai/bytes_count` GA ** _(project)_**   
Application awareness on Interconnect: Bytes Count   
`DELTA`, `DOUBLE`, `By`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of bytes on the Interconnect that has application awareness enabled. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`direction`: Direction of the traffic, one of [ingress, egress].   
`outcome`: Outcome for the byte, one of [sent, dropped].   
`traffic_class`: Traffic class, one of [TC1, TC2, TC3, TC4, TC5, TC6].   
`network/interconnect/link/aai/packets_count` GA ** _(project)_**   
Application awareness on Interconnect: Packets Count   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of packets on the Interconnect that has application awareness enabled. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`direction`: Direction of the traffic, one of [ingress, egress].   
`outcome`: Outcome for the packet, one of [sent, dropped].   
`traffic_class`: Traffic class, one of [TC1, TC2, TC3, TC4, TC5, TC6].   
`network/interconnect/link/macsec/operational` GA ** _(project)_**   
Link MACsec Operational   
`GAUGE`, `BOOL`, ``   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Operational status of MACsec (if enabled) on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/receive_dropped_packets_count` GA ** _(project)_**   
Link MACsec Ingress Dropped Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec dropped ingress packets on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/receive_errors_count` GA ** _(project)_**   
Link MACsec Ingress Errors   
`DELTA`, `DOUBLE`, `{errors}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACSEC ingress errors on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/received_control_packets_count` GA ** _(project)_**   
Link MACsec Ingress Control Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec ingress control packets on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/received_data_packets_count` GA ** _(project)_**   
Link MACsec Ingress Data Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec ingress data packets on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/send_dropped_packets_count` GA ** _(project)_**   
Link MACsec Egress Dropped Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec dropped egress packets on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/send_errors_count` GA ** _(project)_**   
Link MACsec Egress Errors   
`DELTA`, `DOUBLE`, `{errors}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec egress errors on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/sent_control_packets_count` GA ** _(project)_**   
Link MACsec Egress Control Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec egress control packets on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/macsec/sent_data_packets_count` GA ** _(project)_**   
Link MACsec Egress Data Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _The number of MACsec egress data packets on the physical link. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/operational` GA ** _(project)_**   
Circuit Operational Status   
`GAUGE`, `BOOL`, ``   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Whether the operational status of the circuit is 'up'. This metric is specific to individual physical circuits. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`network/interconnect/link/rx_power` GA ** _(project)_**   
Circuit Receive Power   
`GAUGE`, `DOUBLE`, `{dBm}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Light level received over physical circuit. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`laser_index`: (INT64) Index of the laser channel on an individual circuit.   
`network/interconnect/link/tx_power` GA ** _(project)_**   
Circuit Transmit Power   
`GAUGE`, `DOUBLE`, `{dBm}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Light level transmitted over physical circuit. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`link_id`: Identifier for the individual physical circuit.   
`laser_index`: (INT64) Index of the laser channel on an individual circuit.   
`network/interconnect/operational` GA ** _(project)_**   
Operational Status   
`GAUGE`, `BOOL`, ``   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Whether the operational status of the interconnect is 'up'. This metric is specific to the aggregate LACP bundle. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/receive_errors_count` GA ** _(project)_**   
Ingress Errors   
`DELTA`, `DOUBLE`, `{errors}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of errors encountered while receiving packets. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/received_bytes_count` GA ** _(project)_**   
Ingress Bytes   
`DELTA`, `DOUBLE`, `By`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of inbound bytes received. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/received_unicast_packets_count` GA ** _(project)_**   
Ingress Unicast Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of inbound unicast packets received. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/send_errors_count` GA ** _(project)_**   
Egress Errors   
`DELTA`, `DOUBLE`, `{errors}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of errors encountered while sending packets. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/sent_bytes_count` GA ** _(project)_**   
Egress Bytes   
`DELTA`, `DOUBLE`, `By`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of outbound bytes sent. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/interconnect/sent_unicast_packets_count` GA ** _(project)_**   
Egress Unicast Packets   
`DELTA`, `DOUBLE`, `{packets}`   
**[interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)** |  _Number of outbound unicast packets sent. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/dst_to_src_received_bytes_count` GA ** _(project)_**   
Egress Bytes, measured at the source Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes sent to the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/dst_to_src_received_packets_count` GA ** _(project)_**   
Egress Packets, measured at the source Interconnect.   
`DELTA`, `INT64`, `{packets}`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of packets sent to the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/dst_to_src_sent_bytes_count` GA ** _(project)_**   
Ingress Bytes, measured at the destination Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes received from the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/dst_to_src_sent_packets_count` GA ** _(project)_**   
Ingress Packets, measured at the destination Interconnect.   
`DELTA`, `INT64`, `{packets}`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of packets received from the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/excess_dropped_bytes_count` GA ** _(project)_**   
Total bandwidth excess dropped bytes, measured ingress at the source Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes dropped due to exceeding the sum of unmetered and metered bandwidth limits. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/inline_probe_count` GA ** _(project)_**   
Inline Probes   
`DELTA`, `INT64`, `{packets}`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _The number of inline probes with a given status in the last minute. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: SUCCESS or FAILURE.   
`network/wire_endpoint/inline_probe_latency` GA ** _(project)_**   
Inline Probe RTT Latency   
`GAUGE`, `INT64`, `ms`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Pseudowire inline probe RTT latency in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/metered_received_bytes_count` GA ** _(project)_**   
Metered Received Bytes, measured ingress at the source Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes received from the customer that exceed the unmetered bandwidth limit and fit within the metered bandwidth limit. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/operational` GA ** _(project)_**   
Operational Status   
`GAUGE`, `BOOL`, ``   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _The operational status of the wire. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/out_of_band_probe_count` GA ** _(project)_**   
Out of Band Probes   
`DELTA`, `INT64`, `{packets}`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _The number of probes with a given status in the last minute. Probes traverse a pseudowire between the router of this Interconnect and the router of the remote_interface. Although the routers are the same, the probe pseudowire is distinct from your pseudowire, so the probes are out of band. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: SUCCESS or FAILURE.   
`network/wire_endpoint/out_of_band_probe_latency` GA ** _(project)_**   
Out of Band Probe RTT Latency   
`GAUGE`, `INT64`, `ms`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Pseudowire out of band probe RTT latency in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/src_to_dst_received_bytes_count` GA ** _(project)_**   
Egress Bytes, measured at the destination Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes sent to the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/src_to_dst_received_packets_count` GA ** _(project)_**   
Egress Packets, measured at the destination Interconnect.   
`DELTA`, `INT64`, `{packets}`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of packets sent to the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/src_to_dst_sent_bytes_count` GA ** _(project)_**   
Ingress Bytes, measured at the source Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes received from the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/src_to_dst_sent_packets_count` GA ** _(project)_**   
Ingress Packets, measured at the source Interconnect.   
`DELTA`, `INT64`, `{packets}`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of packets received from the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network/wire_endpoint/unmetered_received_bytes_count` GA ** _(project)_**   
Unmetered Received Bytes, measured ingress at the source Interconnect.   
`DELTA`, `INT64`, `By`   
**[wire_endpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)** |  _Number of bytes received from the customer that fall within the specified unmetered bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
### livestream

Metrics for [Live Stream API](https://docs.cloud.google.com/livestream/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `livestream.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`channel/distribution_dropped_packets_count` BETA ** _(project)_**   
Distribution dropped packets count   
`DELTA`, `INT64`, `1`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of dropped packets for distribution outputs since the last sample._   
`distribution_key`: Key of the distribution.   
`distribution_type`: The type of the distribution, one of [RTMP_PUSH, SRT_PUSH].   
`channel/distribution_published_bytes_count` BETA ** _(project)_**   
Distribution published bytes count   
`DELTA`, `INT64`, `By`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of published bytes for distribution outputs since the last sample._   
`distribution_key`: Key of the distribution.   
`distribution_type`: The type of the distribution, one of [RTMP_PUSH, SRT_PUSH].   
`channel/distribution_published_packets_count` BETA ** _(project)_**   
Distribution published packets count   
`DELTA`, `INT64`, `1`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of published packets for distribution outputs since the last sample._   
`distribution_key`: Key of the distribution.   
`distribution_type`: The type of the distribution, one of [RTMP_PUSH, SRT_PUSH].   
`channel/distribution_rtt` BETA ** _(project)_**   
Distribution RTT   
`DELTA`, `DISTRIBUTION`, `ms`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Distribution of RTT (round-trip time) over distribution output connections in milliseconds._   
`distribution_type`: The type of the distribution, one of [RTMP_PUSH, SRT_PUSH].   
`distribution_key`: Key of the distribution.   
`channel/distribution_state` BETA ** _(project)_**   
Distribution state   
`GAUGE`, `INT64`, `1`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _The state of the distribution at a specific time point. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`distribution_key`: Key of the distribution.   
`distribution_type`: The type of the distribution, one of [RTMP_PUSH, SRT_PUSH].   
`state`: Distribution state, one of [NOT_READY, READY, ERROR, AWAITING_INPUT, DISTRIBUTING].   
`channel/dropped_packets_count` BETA ** _(project)_**   
Dropped packets count   
`DELTA`, `INT64`, `1`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of dropped packets since the last sample._   
`input_type`: The type of the input, one of [RTMP_PUSH, SRT_PUSH].   
`input_attachment`: Key of the attached input resource.   
`channel/input_rtt` BETA ** _(project)_**   
Input RTT   
`DELTA`, `DISTRIBUTION`, `ms`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Distribution of RTT (round-trip time) over input connections in milliseconds._   
`input_type`: The type of the input, one of [RTMP_PUSH, SRT_PUSH].   
`input_attachment`: Key of the attached input resource.   
`channel/published_bytes_count` BETA ** _(project)_**   
Published bytes count   
`DELTA`, `INT64`, `By`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of published bytes for media segments since the last sample._   
`mux_stream`: Key of the output mux stream.   
`channel/received_bytes_count` BETA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of received bytes since the last sample._   
`input_type`: The type of the input, one of [RTMP_PUSH, SRT_PUSH].   
`input_attachment`: Key of the attached input resource.   
`channel/received_packets_count` BETA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `1`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _Count of received packets since the last sample._   
`input_type`: The type of the input, one of [RTMP_PUSH, SRT_PUSH].   
`input_attachment`: Key of the attached input resource.   
`channel/streaming_state` BETA ** _(project)_**   
Streaming state   
`GAUGE`, `INT64`, `1`   
**[livestream.googleapis.com/Channel](https://docs.cloud.google.com/monitoring/api/resources#tag_livestream.googleapis.com/Channel)** |  _The streaming state of the channel at a specific time point. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`streaming_state`: Channel streaming state, one of [STREAMING, AWAITING_INPUT, STREAMING_ERROR, STREAMING_NO_INPUT, STOPPED, STARTING, STOPPING].   
  
### loadbalancing

Metrics for [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `loadbalancing.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`application_lb/backend_latencies` BETA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _A distribution of the latency calculated from when the request was sent by the Application Load Balancer proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/backend_request_bytes_count` BETA ** _(project)_**   
Backend request bytes count per application load balancer   
`DELTA`, `INT64`, `By`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of bytes sent as requests from the application load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/backend_request_count` BETA ** _(project)_**   
Backend request count per application load balancer   
`DELTA`, `INT64`, `1`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of requests served by backends of the application load balancer. For Service Extensions, this value represents the number of gRPC streams between the load balancer and the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/backend_response_bytes_count` BETA ** _(project)_**   
Backend response bytes count per application load balancer   
`DELTA`, `INT64`, `By`   
**[gce_backend_service](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_backend_service)** |  _The number of bytes sent as response from backends to the application load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/request_bytes_count` BETA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _The number of request bytes received by the application load balancer. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/request_count` BETA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _The number of requests served by the application load balancer._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/response_bytes_count` BETA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _The number of bytes sent as responses from the application load balancer to clients._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' for the sink default rule.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`application_lb/total_latencies` BETA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gce_forwarding_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_forwarding_rule)** |  _A distribution of the latency calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`matcher_type`: The type of rule matched for the request: 'PATH_MATCHER' or 'DEFAULT_MATCH'. 'DEFAULT_MATCH' indicates that the default route rule or action was matched to the request.   
`matcher_name`: Matched rule for the request. Label value is based on matcher_type. PATH_MATCHER type will be the name of the path matcher. DEFAULT_MATCH types will be empty.   
`matched_path`: The prefix, exact, regex, or template URL path matcher that matched the request. 'UNMATCHED' when a default (empty) path was matched.   
`load_balancing_scheme`: Load balancing scheme used by the Application Load Balancer: 'EXTERNAL_MANAGED' or 'INTERNAL_MANAGED'.   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`proxy_continent`: Continent of the proxy where the traffic originated from, such as 'North America' or 'Europe'.   
`https/backend_latencies` GA ** _(project)_**   
Backend latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _A distribution of the latency calculated from when the request was sent by the proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/backend_request_bytes_count` GA ** _(project)_**   
Backend Request Bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as requests from external HTTP(S) load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP backend response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP backend response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the request: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving the HTTP request by backends (cache hits are abstracted as backend requests): 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/backend_request_count` GA ** _(project)_**   
Backend Request Count   
`DELTA`, `INT64`, `1`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of requests served by backends of external HTTP(S) load balancer. For Service Extensions, this value represents the total number of gRPC streams between the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP backend response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP backend response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the request: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving the HTTP request by backends (cache hits are abstracted as backend requests): 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/backend_response_bytes_count` GA ** _(project)_**   
Backend Response Bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as responses from backends (or cache) to external HTTP(S) load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP backend response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP backend response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the request: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving the HTTP request by backends (cache hits are abstracted as backend requests): 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/external/regional/backend_latencies` GA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _A distribution of the latency calculated from when the request was sent by the proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/backend_request_bytes_count` GA ** _(project)_**   
Backend request bytes count per external regional https load balancer   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as requests from Regional External HTTP(S) load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/external/regional/backend_request_count` GA ** _(project)_**   
Backend request count per external regional https load balancer   
`DELTA`, `INT64`, `1`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of requests served by backends of Regional External HTTP(S) load balancer. For Service Extensions, this value represents the total number of gRPC streams between the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/external/regional/backend_response_bytes_count` GA ** _(project)_**   
Backend response bytes count per external regional https load balancer   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as response from backends to Regional External HTTP(S) load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/external/regional/request_bytes_count` GA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as requests from clients to HTTP/S load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of requests served by HTTP/S load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/response_bytes_count` GA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _The number of bytes sent as responses from HTTP/S load balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/external/regional/total_latencies` GA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[http_external_regional_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_http_external_regional_lb_rule)** |  _A distribution of the latency calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (e.g. 'United States', 'Germany').   
`https/frontend_tcp_rtt` GA ** _(project)_**   
Frontend RTT   
`DELTA`, `DISTRIBUTION`, `ms`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _A distribution of the RTT measured for each connection between client and proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/internal/backend_latencies` GA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _A distribution of the latency calculated from when the request was sent by the internal Application Load Balancer proxy to the backend until the proxy received from the backend the last byte of response. For Service Extensions, this value represents the sum of latencies of each ProcessingRequest/ProcessingResponse pair between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/backend_request_bytes_count` GA ** _(project)_**   
Backend request bytes count per internal https load balancer   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as requests from Internal HTTP(S) load balancer to backends. For Service Extensions, this value represents the total number of bytes sent from the load balancer to the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/internal/backend_request_count` GA ** _(project)_**   
Backend request count per internal https load balancer   
`DELTA`, `INT64`, `1`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of requests served by backends of Internal HTTP(S) load balancer. For Service Extensions, this value represents the number of gRPC streams between the load balancer and the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/internal/backend_response_bytes_count` GA ** _(project)_**   
Backend response bytes count per internal https load balancer   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as response from backends to Internal HTTP(S) load balancer. For Service Extensions, this value represents the total number of bytes received by the load balancer from the extension backend. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`https/internal/request_bytes_count` GA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as requests from clients to internal Application Load Balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of requests served by internal Application Load Balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'QUIC/HTTP/2.0' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/response_bytes_count` GA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _The number of bytes sent as responses from internal Application Load Balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/internal/total_latencies` GA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[internal_http_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_http_lb_rule)** |  _A distribution of the latency calculated from when the request was received by the internal Application Load Balancer proxy until the proxy got ACK from client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`protocol`: Protocol used by the client: 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'SPDY' or 'UNKNOWN'.   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED' or 'UNKNOWN'.   
`https/request_bytes_count` GA ** _(project)_**   
Request bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as requests from clients to external HTTP(S) load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of requests served by external HTTP(S) load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, QUIC/HTTP/2.0, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/response_bytes_count` GA ** _(project)_**   
Response bytes   
`DELTA`, `INT64`, `By`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _The number of bytes sent as responses from external HTTP(S) load balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`https/total_latencies` GA ** _(project)_**   
Total latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[https_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule)** |  _A distribution of the latency calculated from when the request was received by the external HTTP(S) load balancer proxy until the proxy got ACK from client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`protocol`: Protocol used by the client, one of [HTTP/1.0, HTTP/1.1, HTTP/2.0, SPDY, UNKNOWN].   
`response_code`: (INT64) HTTP response code.   
`load_balancing_scheme`: Load balancing scheme: EXTERNAL or EXTERNAL_MANAGED.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`proxy_continent`: Continent of the HTTP proxy that handled the hit: 'America', 'Europe' or 'Asia'.   
`cache_result`: Cache result for serving HTTP request by proxy: 'HIT', 'MISS', 'DISABLED', 'PARTIAL_HIT' (for a request served partially from cache and partially from backend) or 'UNKNOWN'.   
`client_country`: Country of the client that issued the HTTP request (for example, 'United States', 'Germany').   
`l3/external/egress_bytes_count` GA ** _(project)_**   
Egress bytes count   
`DELTA`, `INT64`, `By`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of bytes sent from the backend of the external network load balancer to the client. For TCP flows, this metric counts the bytes on the application stream only. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/egress_packets_count` GA ** _(project)_**   
Egress packets count   
`DELTA`, `INT64`, `1`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of packets sent from the backend of the external network load balancer to the client. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes count   
`DELTA`, `INT64`, `By`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of bytes sent from the client to the backend of the external network load balancer. For TCP flows, this metric counts the bytes on the application stream only. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/ingress_packets_count` GA ** _(project)_**   
Ingress packets count   
`DELTA`, `INT64`, `1`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)**   
**[udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_udp_lb_rule)** |  _The number of packets sent from the client to the backend of the external network load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP]. This field remains empty for all resources other than loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule.   
`l3/external/rtt_latencies` GA ** _(project)_**   
RTT latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule](https://docs.cloud.google.com/monitoring/api/resources#tag_loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule)**   
**[tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_lb_rule)** |  _A distribution of the round trip time latency, measured over TCP connections for the external network load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_continent`: Continent of the client that initiated the flow to the external network load balancer.   
`client_country`: Country of the client that initiated the flow to the external network load balancer.   
`protocol`: Protocol of the connection, set to TCP if the resource is loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule, otherwise empty.   
`l3/internal/egress_bytes_count` GA ** _(project)_**   
Egress bytes per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `By`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of bytes sent from the internal TCP/UDP load balancer backend to the client (for TCP flows it's counting bytes on application stream only). Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/egress_packets_count` GA ** _(project)_**   
Egress packets per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `1`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of packets sent from the internal TCP/UDP load balancer to the client. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `By`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of bytes sent from the client to the internal TCP/UDP load balancer backend (for TCP flows it's counting bytes on application stream only). Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/ingress_packets_count` GA ** _(project)_**   
Ingress packets per internal TCP/UDP load balancer   
`DELTA`, `INT64`, `1`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)**   
**[internal_udp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_udp_lb_rule)** |  _The number of packets sent from the client to the internal TCP/UDP load balancer backend. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l3/internal/rtt_latencies` GA ** _(project)_**   
RTT latencies per internal TCP/UDP load balancer   
`DELTA`, `DISTRIBUTION`, `ms`   
**[internal_tcp_lb_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_tcp_lb_rule)** |  _A distribution of RTT measured over TCP connections for internal TCP/UDP load balancer flows. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`client_project_id`: Project ID of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_network`: Network of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_subnetwork`: Subnetwork of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`client_zone`: Zone of the client instance communicating with the internal TCP/UDP load balancer. If the client instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to CLIENT_IS_EXTERNAL.   
`l4_proxy/egress_bytes_count` GA ** _(project)_**   
Egress bytes   
`DELTA`, `INT64`, `By`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of bytes sent from VM to client using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`l4_proxy/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes   
`DELTA`, `INT64`, `By`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of bytes sent from client to VM using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`l4_proxy/tcp/closed_connections_count` GA ** _(project)_**   
Closed connections   
`DELTA`, `INT64`, `1`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of connections that were terminated over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`l4_proxy/tcp/new_connections_count` GA ** _(project)_**   
New connections   
`DELTA`, `INT64`, `1`   
**[l4_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_l4_proxy_rule)** |  _Number of connections that were opened over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`client_country`: Country of the client where the traffic originated from, such as 'United States' or 'Germany'.   
`subnet/proxy_only/addresses` GA ** _(project)_**   
Proxy-only addresses   
`GAUGE`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _The current number of proxy-only addresses by state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of the address, one of [used, free].   
`tcp_ssl_proxy/closed_connections` GA ** _(project)_**   
Closed connections   
`DELTA`, `INT64`, `1`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of connections that were terminated over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/egress_bytes_count` GA ** _(project)_**   
Egress bytes   
`DELTA`, `INT64`, `By`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of bytes sent from VM to client using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/frontend_tcp_rtt` GA ** _(project)_**   
Frontend RTT   
`DELTA`, `DISTRIBUTION`, `ms`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _A distribution of the smoothed RTT (in ms) measured by the proxy's TCP stack, each minute application layer bytes pass from proxy to client. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes   
`DELTA`, `INT64`, `By`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of bytes sent from client to VM using proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/new_connections` GA ** _(project)_**   
New connections opened   
`DELTA`, `INT64`, `1`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Number of connections that were created over TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
`tcp_ssl_proxy/open_connections` GA ** _(project)_**   
Open Connections   
`GAUGE`, `INT64`, `1`   
**[tcp_ssl_proxy_rule](https://docs.cloud.google.com/monitoring/api/resources#tag_tcp_ssl_proxy_rule)** |  _Current number of outstanding connections through the TCP proxy or SSL proxy load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`proxy_continent`: Continent of the SSL proxy that handles the connection: 'America', 'Europe' or 'Asia'.   
`client_country`: Country of the client that opened the TCP/SSL connection (for example, 'United States', 'Germany').   
  
### logging

Metrics from [Cloud Logging](https://docs.cloud.google.com/logging/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `logging.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`billing/bytes_ingested` GA ** _(project)_**   
Bytes streamed into log buckets   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes streamed into log buckets for indexing, querying, and analysis; includes up to 30 days of storage. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`resource_type`: Monitored resource type for the log entry.   
`billing/bytes_stored` GA ** _(project)_**   
Logging Retention   
`GAUGE`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Volume of logs that are retained past the default 30 days. No data exists when the retention period of a log bucket is never larger than 30 days. This metric might have a value of zero when the retention period of a log bucket is shortened to 30 days. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`data_type`: This field indicates that log volume reported here is charged for retention past the default 30 days. The data_type for all reported retention is set to `CHARGED`.   
`log_bucket_location`: The location where the log bucket resides.   
`log_bucket_id`: The id of the log bucket.   
`billing/log_bucket_bytes_ingested` GA ** _(project)_**   
Bytes streamed into log buckets   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes streamed into log buckets for indexing, querying, and analysis; includes up to 30 days of storage. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`log_source`: The resource container where the log comes from.   
`resource_type`: Monitored resource type for the logs streamed into log buckets.   
`log_bucket_location`: The location where the log bucket resides.   
`log_bucket_id`: The id of the log bucket.   
`billing/log_bucket_monthly_bytes_ingested` GA ** _(project)_**   
Bytes streamed into log buckets monthly   
`GAUGE`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes streamed into log buckets for indexing, querying, and analysis for this month-to-date; include up to 30 days of storage. Sampled every 1800 seconds. After sampling, data is not visible for up to 6000 seconds._   
`log_source`: The resource container where the log comes from.   
`resource_type`: Monitored resource type for the logs streamed into log buckets.   
`log_bucket_location`: The location where the log bucket resides.   
`log_bucket_id`: The id of the log bucket.   
`billing/monthly_bytes_ingested` GA ** _(project)_**   
Monthly bytes streamed into log buckets   
`GAUGE`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Month-to-date number of bytes streamed into log buckets for indexing, querying, and analysis; includes up to 30 days of storage. Sampled every 1800 seconds. After sampling, data is not visible for up to 6000 seconds._   
`resource_type`: Monitored resource type for the log entry.   
`byte_count` GA ** _(project)_**   
Log bytes   
`DELTA`, `INT64`, `By` |  _Total bytes of log entries, either written directly or routed to this project via project-sink, that are stored in at least one log bucket. Sampled every 60 seconds._   
`log`: Name of the log.   
`severity`: Severity of the log entry.   
`dropped_log_entry_count` DEPRECATED ** _(project)_**   
Logs-based metric errors (Deprecated)   
`DELTA`, `INT64`, `1` |  _Use "logging.googleapis.com/logs_based_metrics_error_count" instead. Sampled every 60 seconds._   
`log`: Name of the log.   
`exports/byte_count` GA ** _(project)_**   
Exported log bytes   
`DELTA`, `INT64`, `By`   
**[logging_sink](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_sink)** |  _Number of bytes in log entries that were exported. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`exports/error_count` GA ** _(project)_**   
Exported log entries failures   
`DELTA`, `INT64`, `1`   
**[logging_sink](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_sink)** |  _Number of log entries that failed to be exported. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`exports/log_entry_count` GA ** _(project)_**   
Exported log entries   
`DELTA`, `INT64`, `1`   
**[logging_sink](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_sink)** |  _Number of log entries that were exported. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`log_entry_count` GA ** _(project)_**   
Log entries   
`DELTA`, `INT64`, `1` |  _Number of log entries, either written directly or routed to this project via project-sink, that are stored in at least one log bucket. By default, log entries are stored for 30 days. Excluded logs are not counted. Sampled every 60 seconds._   
`log`: Name of the log.   
`severity`: Severity of the log entry.   
`logs_based_metrics_error_count` GA ** _(project)_**   
Logs-based metric errors   
`DELTA`, `INT64`, `1` |  _Number of log entries, either written directly or routed to this project via project-sink, and are stored in a log bucket but excluded from any system or user-defined logs-based metrics. This condition can occur if the timestamp of a log entry is more than 24 hours older, or 10 minutes newer, than the actual receive time. Sampled every 60 seconds._   
`log`: Name of the log.   
`metric_label_cardinality` BETA ** _(project)_**   
Logs-based metric active cardinality count by label   
`GAUGE`, `INT64`, `1`   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Cardinality estimate for each metric label of a logs-based metric. The estimate is computed over approximately 25 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._   
`label`: Name of the metric label.   
`metric_label_throttled` BETA ** _(project)_**   
Logs-based metric label throttled status   
`GAUGE`, `BOOL`, ``   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Indicates if metric labels are being dropped for logs-based metrics due to exceeding cardinality limits. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._   
`label`: Name of the metric label.   
`metric_throttled` GA ** _(project)_**   
Logs-based metric throttled status   
`GAUGE`, `BOOL`, ``   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Indicates if labels or points are being dropped for logs-based metrics due to exceeding active time series (cardinality) limits. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._  
`time_series_count` BETA ** _(project)_**   
Logs-based metric active time series (cardinality) count   
`GAUGE`, `INT64`, `1`   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Active time series (cardinality) estimates for logs-based metrics. Only metric labels are counted and the estimate is computed over approximately 25 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._  
  
### lustre

Metrics for [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs). Launch stages of these metrics: ALPHA BETA

The "metric type" strings in this table must be prefixed with `lustre.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cache/read_hits` BETA ** _(project)_**   
Cache read hits   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _Number of read hits for a specific device. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`device`: The device name. (Deprecated).   
`target`: The name of the Lustre target device.   
`cache/read_misses` BETA ** _(project)_**   
Cache read misses   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _Number of read misses for a specific device. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`device`: The device name. (Deprecated).   
`target`: The name of the Lustre target device.   
`instance/available_bytes` BETA ** _(project)_**   
Available bytes   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of bytes of storage space for a given Object Storage Target (OST) or Metadata Target (MDT) that is available to non-root users. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`instance/capacity_bytes` BETA ** _(project)_**   
Capacity bytes   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of bytes provisioned for the given Lustre target. The total cluster usable data or metadata space for an instance can be obtained by adding the capacity of all targets for a given type of Lustre target. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`instance/connected_clients` BETA ** _(project)_**   
Connected clients   
`GAUGE`, `INT64`, `{client}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of clients currently connected to the given Metadata Target (MDT). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device. This will always be 'mdt'.   
`target`: The name of the Metadata Target (MDT).   
`instance/free_bytes` BETA ** _(project)_**   
Free bytes   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of bytes of storage space for a given Object Storage Target (OST) or Metadata Target (MDT) that is available to root users. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`instance/inodes_free` BETA ** _(project)_**   
Free inodes   
`GAUGE`, `INT64`, `{inode}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of inodes (objects) available on the given target. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`instance/inodes_maximum` BETA ** _(project)_**   
Maximum inodes   
`GAUGE`, `INT64`, `{inode}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The maximum number of inodes (objects) the target can hold. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`instance/io_time_milliseconds_total` BETA ** _(project)_**   
Operation latency   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of read or write operations whose latency is within the bucketed latency ranges. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`operation`: The operation type.   
`size`: The bucketed latency range (e.g. 512 includes the count of operations that took between 512 and 1024 milliseconds).   
`target`: The name of the Lustre target device.   
`instance/metadata_operations_total` BETA ** _(project)_**   
Metadata Operations   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _Number of metadata operations the filesystem has performed on the given Metadata Target (MDT). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The component that handled the request.   
`operation`: The operation type.   
`target`: The name of the Lustre target device.   
`instance/read_bytes_total` BETA ** _(project)_**   
Data read bytes   
`DELTA`, `INT64`, `By`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of data bytes read from the given Object Storage Target (OST). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`operation`: The operation type.   
`target`: The name of the Lustre target device.   
`instance/read_samples_total` BETA ** _(project)_**   
Data read operations   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of read operations performed on the given Object Storage Target (OST). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`operation`: The operation type.   
`target`: The name of the Lustre target device.   
`instance/write_bytes_total` BETA ** _(project)_**   
Data write bytes   
`DELTA`, `INT64`, `By`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of data bytes written to the given Object Storage Target (OST). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`operation`: The operation type.   
`target`: The name of the Lustre target device.   
`instance/write_samples_total` BETA ** _(project)_**   
Data write operations   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Instance)** |  _The number of write operations performed on the given Object Storage Target (OST). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`operation`: The operation type.   
`target`: The name of the Lustre target device.   
`job/metadata_operations_total` BETA ** _(project)_**   
Metadata operations by job   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _Number of operations the filesystem has performed, recorded by jobstats. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`operation`: The operation type.   
`target`: The name of the Lustre target device.   
`job/read_bytes_total` BETA ** _(project)_**   
Data read bytes by job   
`DELTA`, `INT64`, `By`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _The total number of bytes that have been read. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/read_maximum_size_bytes` BETA ** _(project)_**   
Data read maximum size by job   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _The maximum read size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/read_minimum_size_bytes` BETA ** _(project)_**   
Data read minimum size by job   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _The minimum read size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/read_samples_total` BETA ** _(project)_**   
Data read operations by job   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _Total number of reads that have been recorded. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/write_bytes_total` BETA ** _(project)_**   
Data write bytes by job   
`DELTA`, `INT64`, `By`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _The total number of bytes that have been written. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/write_maximum_size_bytes` BETA ** _(project)_**   
Data write maximum size by job   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _The maximum write size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/write_minimum_size_bytes` BETA ** _(project)_**   
Data write minimum size by job   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _The minimum write size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`job/write_samples_total` BETA ** _(project)_**   
Data write operations by job   
`DELTA`, `INT64`, `{operation}`   
**[lustre.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Job)** |  _Total number of writes that have been recorded. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: The type of the Lustre target device.   
`target`: The name of the Lustre target device.   
`quota/capacity/exceeded` BETA ** _(project)_**   
Lustre storage capacity (GiB) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/capacity. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/capacity/limit` BETA ** _(project)_**   
Lustre storage capacity (GiB) quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/capacity/usage` BETA ** _(project)_**   
Lustre storage capacity (GiB) quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/capacity. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/dynamic_tier_capacity/exceeded` BETA ** _(project)_**   
Dynamic tier storage capacity (GiB) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/dynamic_tier_capacity. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/dynamic_tier_capacity/limit` BETA ** _(project)_**   
Dynamic tier storage capacity (GiB) quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/dynamic_tier_capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/dynamic_tier_capacity/usage` BETA ** _(project)_**   
Dynamic tier storage capacity (GiB) quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/dynamic_tier_capacity. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_1000MBps_throughput_per_TiB/exceeded` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 1000 MB/s/TiB. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/storage_for_1000MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_1000MBps_throughput_per_TiB/limit` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 1000 MB/s/TiB. quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/storage_for_1000MBps_throughput_per_TiB. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_1000MBps_throughput_per_TiB/usage` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 1000 MB/s/TiB. quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/storage_for_1000MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_125MBps_throughput_per_TiB/exceeded` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 125 MB/s/TiB. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/storage_for_125MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_125MBps_throughput_per_TiB/limit` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 125 MB/s/TiB. quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/storage_for_125MBps_throughput_per_TiB. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_125MBps_throughput_per_TiB/usage` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 125 MB/s/TiB. quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/storage_for_125MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_250MBps_throughput_per_TiB/exceeded` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 250 MB/s/TiB. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/storage_for_250MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_250MBps_throughput_per_TiB/limit` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 250 MB/s/TiB. quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/storage_for_250MBps_throughput_per_TiB. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_250MBps_throughput_per_TiB/usage` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 250 MB/s/TiB. quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/storage_for_250MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_500MBps_throughput_per_TiB/exceeded` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 500 MB/s/TiB. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/storage_for_500MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_500MBps_throughput_per_TiB/limit` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 500 MB/s/TiB. quota limit   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/storage_for_500MBps_throughput_per_TiB. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/storage_for_500MBps_throughput_per_TiB/usage` ALPHA ** _(project)_**   
Storage capacity (GiB) for a throughput of 500 MB/s/TiB. quota usage   
`GAUGE`, `INT64`, `GiBy`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/storage_for_500MBps_throughput_per_TiB. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/throughput/exceeded` BETA ** _(project)_**   
Lustre throughput (GBps) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric lustre.googleapis.com/throughput. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/throughput/limit` BETA ** _(project)_**   
Lustre throughput (GBps) quota limit   
`GAUGE`, `INT64`, `GBy/s`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current limit on quota metric lustre.googleapis.com/throughput. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota/throughput/usage` BETA ** _(project)_**   
Lustre throughput (GBps) quota usage   
`GAUGE`, `INT64`, `GBy/s`   
**[lustre.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/Location)** |  _Current usage on quota metric lustre.googleapis.com/throughput. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`network_name`: The Managed Lustre network name in format of projects/{project}/global/networks/{network}.   
`quota_entity/hard_limit_bytes` BETA ** _(project)_**   
Quota Hard Limit Bytes   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/QuotaEntity](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity)** |  _The absolute maximum byte usage allowed. New writes are blocked when this limit is reached. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`accounting_type`: The type of entity for which quota is accounted (e.g., user, group, project).   
`target`: The name of the Lustre target device.   
`quota_entity/hard_limit_inodes` BETA ** _(project)_**   
Quota Hard Limit Inodes   
`GAUGE`, `INT64`, `{inode}`   
**[lustre.googleapis.com/QuotaEntity](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity)** |  _The absolute maximum inode usage allowed. New file/directory creations are blocked when this limit is reached. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`accounting_type`: The type of entity for which quota is accounted (e.g., user, group, project).   
`target`: The name of the Lustre target device.   
`quota_entity/soft_limit_bytes` BETA ** _(project)_**   
Quota Soft Limit Bytes   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/QuotaEntity](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity)** |  _The soft limit for byte usage. Exceeding this starts a grace period. Enforced as a hard limit if usage remains above this limit after the grace period expires. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`accounting_type`: The type of entity for which quota is accounted (e.g., user, group, project).   
`target`: The name of the Lustre target device.   
`quota_entity/soft_limit_inodes` BETA ** _(project)_**   
Quota Soft Limit Inodes   
`GAUGE`, `INT64`, `{inode}`   
**[lustre.googleapis.com/QuotaEntity](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity)** |  _The soft limit for inode usage. Exceeding this starts a grace period. Enforced as a hard limit if usage remains above this limit after the grace period expires. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`accounting_type`: The type of entity for which quota is accounted (e.g., user, group, project).   
`target`: The name of the Lustre target device.   
`quota_entity/used_bytes` BETA ** _(project)_**   
Quota Used Bytes   
`GAUGE`, `INT64`, `By`   
**[lustre.googleapis.com/QuotaEntity](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity)** |  _The current byte usage for the entity. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`accounting_type`: The type of entity for which quota is accounted (e.g., user, group, project).   
`target`: The name of the Lustre target device.   
`quota_entity/used_inodes` BETA ** _(project)_**   
Quota Used Inodes   
`GAUGE`, `INT64`, `{inode}`   
**[lustre.googleapis.com/QuotaEntity](https://docs.cloud.google.com/monitoring/api/resources#tag_lustre.googleapis.com/QuotaEntity)** |  _The current number of inodes used by the entity. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`accounting_type`: The type of entity for which quota is accounted (e.g., user, group, project).   
`target`: The name of the Lustre target device.   
  
### managedflink

Metrics from [BigQuery Engine for Apache Flink](https://docs.cloud.google.com/managed-flink/docs).

The "metric type" strings in this table must be prefixed with `managedflink.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`deployment/cpu/limit` DEPRECATED ** _(project)_**   
CPU limit   
`GAUGE`, `DOUBLE`, `s{vCPU}/s`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The maximum amount of vCPU that the deployment can use. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/cpu/usage` DEPRECATED ** _(project)_**   
CPU usage   
`GAUGE`, `DOUBLE`, `s{vCPU}/s`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The amount of vCPU that the deployment is currently using. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/disk/limit` DEPRECATED ** _(project)_**   
Disk limit   
`GAUGE`, `INT64`, `By`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The maximum amount of disk usage allowed for the deployment, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/disk/ops_usage` DEPRECATED ** _(project)_**   
Disk operation usage   
`GAUGE`, `INT64`, `{Ops}/s`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The current disk usage for the deployment in number of operations per second. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/disk/usage` DEPRECATED ** _(project)_**   
Disk usage   
`GAUGE`, `INT64`, `By`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The amount of disk space that the deployment is currently using. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/jobs/count` DEPRECATED ** _(project)_**   
Jobs count   
`DELTA`, `INT64`, `1`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The cumulative count of the jobs in the deployment, categorized by state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: The state of the job.   
`deployment/memory/limit` DEPRECATED ** _(project)_**   
Memory limit   
`GAUGE`, `INT64`, `By`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The maximum amount of memory that the deployment can use, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/memory/usage` DEPRECATED ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The amount of memory that the deployment is currently using. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`deployment/state` DEPRECATED ** _(project)_**   
State   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The current state of the deployment. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: The state of the deployment.   
`deployment/uptime_secs` DEPRECATED ** _(project)_**   
Uptime seconds   
`GAUGE`, `INT64`, `s`   
**[managedflink.googleapis.com/Deployment](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Deployment)** |  _The number of seconds that this deployment has been running. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`job/autotuning/horizontal_scaling/max_parallelism` DEPRECATED ** _(project)_**   
Maximum task slots   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _The maximum number of allowed task slots for the job._  
`job/autotuning/horizontal_scaling/min_parallelism` DEPRECATED ** _(project)_**   
Minimum task slots   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _The minimum number of allowed task slots for the job._  
`job/autotuning/horizontal_scaling/parallelism` DEPRECATED ** _(project)_**   
Task slots   
`GAUGE`, `DOUBLE`, `1`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _The total number of task slots for the job._  
`job/autotuning/horizontal_scaling/recommended_parallelism` DEPRECATED ** _(project)_**   
Recommended task slots   
`GAUGE`, `DOUBLE`, `1`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _The number of task slots recommeded by the autotuning algorithm._  
`job/state` DEPRECATED ** _(project)_**   
State   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _The current state of job. This data is passed through from the Apache Flink API. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: Stringified enum state of job.   
`job/state_millis` DEPRECATED ** _(project)_**   
State milliseconds   
`GAUGE`, `INT64`, `ms`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _For a given state, returns the total amount of time in milliseconds since the job transitioned to that state. Otherwise, returns 0._   
`state`: The stringified enum state of the job.   
`job/state_total_millis` DEPRECATED ** _(project)_**   
State total milliseconds   
`GAUGE`, `INT64`, `ms`   
**[managedflink.googleapis.com/Job](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Job)** |  _The total amount of time, in milliseconds, the job has been in a given state._   
`state`: The stringified enum state of the job.   
`operator/current_input_n_watermark_millis` DEPRECATED ** _(project)_**   
Current Input N Watermark   
`GAUGE`, `INT64`, `ms`   
**[managedflink.googleapis.com/Operator](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Operator)** |  _The most recent input watermark, in milliseconds, this operator received in its N'th input, with the index starting from 1. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operator_name`: Human-readable name.   
`input_index`: The index for the n'th input.   
`operator/current_input_watermark_millis` DEPRECATED ** _(project)_**   
Current input watermark   
`GAUGE`, `INT64`, `ms`   
**[managedflink.googleapis.com/Operator](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Operator)** |  _The most recent input watermark, in milliseconds,received by this operator. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operator_name`: Human-readable name.   
`operator/current_output_watermark_millis` DEPRECATED ** _(project)_**   
Current output watermark   
`GAUGE`, `INT64`, `ms`   
**[managedflink.googleapis.com/Operator](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Operator)** |  _The most recent output watermark, in milliseconds, received by this operator. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operator_name`: Human-readable name.   
`operator/late_records_dropped_count` DEPRECATED ** _(project)_**   
Late records dropped count   
`DELTA`, `INT64`, `1`   
**[managedflink.googleapis.com/Operator](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Operator)** |  _The total number of records dropped due to arriving late. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operator_name`: Human-readable name.   
`operator/records_in_count` DEPRECATED ** _(project)_**   
Records in count   
`DELTA`, `INT64`, `1`   
**[managedflink.googleapis.com/Operator](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Operator)** |  _The total number of records ingested by this operator. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operator_name`: Human-readable name.   
`operator/records_out_count` DEPRECATED ** _(project)_**   
Records out count   
`DELTA`, `INT64`, `1`   
**[managedflink.googleapis.com/Operator](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Operator)** |  _The total number of records outputted by this operator. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operator_name`: Human-readable name.   
`vertex/autotuning/horizontal_scaling/parallelism` DEPRECATED ** _(project)_**   
Vertex parallelism   
`GAUGE`, `DOUBLE`, `1`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The number of task slots assigned to this vertex._   
`vertex_name`: Human-readable name.   
`vertex/autotuning/horizontal_scaling/recommended_parallelism` DEPRECATED ** _(project)_**   
Recommended vertex parallelism   
`GAUGE`, `DOUBLE`, `1`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The number of task slots recommended by the autotuning algorithm._   
`vertex_name`: Human-readable name.   
`vertex/backlog_elements` DEPRECATED ** _(project)_**   
Vertex backlog elements   
`GAUGE`, `DOUBLE`, `1`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The total number of pending records._   
`vertex_name`: Human-readable name.   
`vertex/current_input_watermark_millis` DEPRECATED ** _(project)_**   
Current input watermark   
`GAUGE`, `INT64`, `ms`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The most recent input watermark this vertex received. For operators or vertices with two inputs, this is calculated as the oldest of the most recently received watermarks. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`vertex_name`: Human-readable name.   
`vertex/input_bytes` DEPRECATED ** _(project)_**   
Input bytes   
`GAUGE`, `INT64`, `By`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The total number of bytes ingested by this vertex. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`vertex_name`: Human-readable name.   
`vertex/late_records_dropped` DEPRECATED ** _(project)_**   
Late records dropped count   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The total number of records dropped due to late arrival. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`vertex_name`: Human-readable name.   
`vertex/output_bytes` DEPRECATED ** _(project)_**   
Output bytes   
`GAUGE`, `INT64`, `By`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The total number of bytes emitted by this vertex. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`vertex_name`: Human-readable name.   
`vertex/records_in` DEPRECATED ** _(project)_**   
Records in count   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The total number of records that this vertex has ingested. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`vertex_name`: Human-readable name.   
`vertex/records_out` DEPRECATED ** _(project)_**   
Records out count   
`GAUGE`, `INT64`, `1`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The total number of records that this vertex has outputted. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`vertex_name`: Human-readable name.   
`vertex/state_millis_per_sec` DEPRECATED ** _(project)_**   
State milliseconds per second   
`GAUGE`, `INT64`, `ms/s`   
**[managedflink.googleapis.com/Vertex](https://docs.cloud.google.com/monitoring/api/resources#tag_managedflink.googleapis.com/Vertex)** |  _The number of milliseconds within the last second (that is, the percentage of time) that this vertex was in a specific state of idle, busy, or backpressured. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: The state of the vertex. When `idle`, it has nothing to do. When `busy`, it's neither idle or backpressured. When `backpressured`, it's waiting for downstream vertices to finish. Soft backpressure is when a vertex is still responsive and can, for example, trigger unaligned checkpoints. Hard backpressure is when a vertex is completely blocked and unresponsive.   
`vertex_name`: Human-readable name.   
  
### managedidentities

Metrics from [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `managedidentities.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`microsoft_ad/domain/health` BETA ** _(project)_**   
AD Domain Health   
`GAUGE`, `BOOL`, ``   
**[microsoft_ad_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_microsoft_ad_domain)** |  _Overall health status for Active Directory domain. True if healthy, else false. Sampled every 60 seconds. After sampling, data is not visible for up to 195 seconds._  
`microsoft_ad/domain/ldaps/cert_ttl` BETA ** _(project)_**   
LDAPS Certificate TTL   
`GAUGE`, `INT64`, `d`   
**[microsoft_ad_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_microsoft_ad_domain)** |  _Number of days until certificate with the closest expiry in the chain used for LDAPS expires. Will be 0 if certificate has expired. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`microsoft_ad/domain/trust/state` BETA ** _(project)_**   
AD Domain Trust Health   
`GAUGE`, `BOOL`, ``   
**[microsoft_ad_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_microsoft_ad_domain)** |  _Detailed state for Active Directory trust between source and target domain. True if connected, else false. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`trust_direction`: The direction decides the domain is trusted, trusting or both.   
`target_domain_name`: The target domain name which is in trust with.   
`trust_type`: The different inter forest trust type.   
  
### managedkafka

Metrics from [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-kafka/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `managedkafka.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`broker/under_min_isr_partitions` GA ** _(project)_**   
Under-MinISR Partitions   
`GAUGE`, `INT64`, `{partition}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Number of under minIsr partitions (|ISR| < min.insync.replicas). From MBean kafka.server:type=ReplicaManager,name=UnderMinIsrPartitionCount. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`broker/under_replicated_partitions` GA ** _(project)_**   
Under-replicated Partitions   
`GAUGE`, `INT64`, `{partition}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Number of under replicated partitions, or the number of partitions that have replicas not in sync. From MBean kafka.server:type=ReplicaManager,name=UnderReplicatedPartitions. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`byte_in_count` GA ** _(project)_**   
Byte In Count   
`DELTA`, `INT64`, `By`   
**[managedkafka.googleapis.com/Topic](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Topic)** |  _The total number of bytes from clients sent to the topic. This comes from the MBean kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec,topic=([-.\w]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`byte_out_count` GA ** _(project)_**   
Byte Out Count   
`DELTA`, `INT64`, `By`   
**[managedkafka.googleapis.com/Topic](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Topic)** |  _The total number of bytes sent to clients. This comes from the MBean kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec,topic=([-.\w]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`byte_size` GA ** _(project)_**   
Byte Size   
`GAUGE`, `INT64`, `By`   
**[managedkafka.googleapis.com/TopicPartition](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/TopicPartition)** |  _The size of the partition on disk in bytes. This comes from MBean kafka.log:type=Log,name=Size,topic=([-.\w]+),partition=([0-9]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`cluster_byte_in_count` GA ** _(project)_**   
Cluster Byte In Count   
`DELTA`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The total number of bytes from clients sent to all topics. This comes from the MBean kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`cluster_byte_out_count` GA ** _(project)_**   
Cluster Byte Out Count   
`DELTA`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The total number of bytes sent to clients from all topics. This comes from the MBean kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`cluster_message_in_count` GA ** _(project)_**   
Cluster Message In Count   
`DELTA`, `INT64`, `{message}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The total number of messages that have been published all topics. This comes from the MBean kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`connector_deadletterqueue_record_count` GA ** _(project)_**   
Connector Dead Letter Queue Record Count   
`DELTA`, `INT64`, `{request}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Total number of attempted or failed writes to the dead letter queue, from MBean kafka.connect <type=task-error-metrics, connector=(.+), task=(.+)><>(deadletterqueue-produce-failures|deadletterqueue-produce-requests). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`type`: The type of dead letter queue record counts (failures or requests).   
`connector_incoming_byte_rate` GA ** _(project)_**   
Connector Incoming Byte Rate   
`GAUGE`, `DOUBLE`, `By/s`   
**[managedkafka.googleapis.com/ConnectCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/ConnectCluster)** |  _Average number of outgoing bytes read per second from all sockets from client connection, from MBean kafka.connect <type=connect-metrics, client-id=(.+)><>incoming-byte-rate. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`client_id`: The id of the connect client.   
`connector_outgoing_byte_rate` GA ** _(project)_**   
Connector Outgoing Byte Rate   
`GAUGE`, `DOUBLE`, `By/s`   
**[managedkafka.googleapis.com/ConnectCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/ConnectCluster)** |  _Average number of outgoing bytes sent per second to all servers from client connection, from MBean kafka.connect <type=connect-metrics, client-id=(.+)><>outgoing-byte-rate. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`client_id`: The id of the connect client.   
`connector_request_rate` GA ** _(project)_**   
Connector Request Rate   
`GAUGE`, `DOUBLE`, `{request}/s`   
**[managedkafka.googleapis.com/ConnectCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/ConnectCluster)** |  _Average number of requests sent per second from client connection, from MBean kafka.connect <type=connect-metrics, client-id=(.+)><>request-rate. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`client_id`: The id of the connect client.   
`connector_response_rate` GA ** _(project)_**   
Connector Response Rate   
`GAUGE`, `DOUBLE`, `{response}/s`   
**[managedkafka.googleapis.com/ConnectCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/ConnectCluster)** |  _Average number of responses received and sent per second from client connection, from MBean kafka.connect <type=connect-metrics, client-id=(.+)><>response-rate. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`client_id`: The id of the connect client.   
`connector_sink_active_records` GA ** _(project)_**   
Connector Sink Record Active Counts   
`GAUGE`, `INT64`, `{record}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Most recent number of records read from Kafka but not completely committed by the sink task, from MBean kafka.connect <type=sink-task-metrics, connector=(.+), task=(.+)><>sink-record-active-count. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`connector_sink_record_rate` GA ** _(project)_**   
Connector Sink Record Rate   
`GAUGE`, `DOUBLE`, `{record}/s`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Average record read or send rate from sink connector, from MBean kafka.connect <type=source-task-metrics, connector=(.+), task=(.+)><>(sink-record-read-rate|sink-record-send-rate). Read rate is before transformation. Send rate is after transformation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`type`: The type of sink record (read-rate or send-rate).   
`connector_sink_record_read_total` GA ** _(project)_**   
Connector Sink Record Read Count   
`DELTA`, `INT64`, `{record}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Total number of records read from Kafka by the sink task before transformations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`connector_source_active_records` GA ** _(project)_**   
Connector Source Record Active Counts   
`GAUGE`, `INT64`, `{record}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Most recent number of records polled by the task but not completely written to Kafka, from MBean kafka.connect <type=source-task-metrics, connector=(.+), task=(.+)><>source-record-active-count. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`connector_source_record_poll_total` GA ** _(project)_**   
Connector Source Record Poll Count   
`DELTA`, `INT64`, `{record}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Total number of records polled by the source task before transformations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`connector_source_record_rate` GA ** _(project)_**   
Connector Source Record Rate   
`GAUGE`, `DOUBLE`, `{record}/s`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Average record write or poll rate from source connector, from MBean kafka.connect <type=source-task-metrics, connector=(.+), task=(.+)><>(source-record-write-rate|source-record-poll-rate). Poll rate is before transformation. Write rate is after transformation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`type`: The type of source record (write-rate or poll-rate).   
`connector_tasks` GA ** _(project)_**   
Connector Task Counts   
`GAUGE`, `INT64`, `{task}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Number of connector task in different states, from MBean kafka.connect <type=connect-worker-metrics, connector=(.+)><>(connector-destroyed-task-count|connector-failed-task-count|connector-paused-task-count|connector-restarting-task-count|connector-running-task-count|connector-unassigned-task-count). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`state`: The state of the task (running, paused, unassigned, restarting, failed, or destroyed).   
`connector_total_error_record_count` GA ** _(project)_**   
Connector Total Record Error Count   
`DELTA`, `INT64`, `{record}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Total number of task record errors, from MBean kafka.connect <type=task-error-metrics, connector=(.+), task=(.+)><>(total-record-errors|total-record-failures|total-records-skipped). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`type`: The type of task record error counts (record-errors, record-failures, or record-skipped).   
`connector_total_retries_count` GA ** _(project)_**   
Connector Total Retries   
`DELTA`, `INT64`, `{retry}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _Total number of connector task retries, from MBean kafka.connect <type=task-error-metrics, connector=(.+), task=(.+)><>total-retries. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`task`: The id of the task.   
`consumer_groups` GA ** _(project)_**   
Consumer Groups   
`GAUGE`, `INT64`, `{consumer_groups}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The current number of Consumer Groups consuming from the broker. This comes from MBean kafka.server:type=GroupMetadataManager,name=NumGroups. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: The state of the consumer group.   
`broker_index`: The index of the broker.   
`consumer_lag` GA ** _(project)_**   
Consumer Lag   
`GAUGE`, `INT64`, `message`   
**[managedkafka.googleapis.com/TopicPartition](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/TopicPartition)** |  _Lag in messages per follower replica. This comes from MBean kafka.server:type=FetcherLagMetrics,name=ConsumerLag,clientId=([-.\w]+),topic=([-.\w]+),partition=([0-9]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`client_id`: The ID of the client consuming from the partition.   
`cpu/core_usage_time` GA ** _(project)_**   
CPU Core Usage   
`DELTA`, `DOUBLE`, `s{vCPU}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Total CPU usage of the broker in vCPU seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`cpu/limit` GA ** _(project)_**   
CPU Limit   
`GAUGE`, `DOUBLE`, `s{vCPU}/s`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Current CPU limit of the broker in vCPUs. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`cpu/worker_core_usage_time` GA ** _(project)_**   
Connect Cluster Worker CPU Core Usage   
`DELTA`, `DOUBLE`, `s{vCPU}`   
**[managedkafka.googleapis.com/ConnectCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/ConnectCluster)** |  _Total connect worker CPU usage of the worker in vCPU seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the worker.   
`disk/limit` GA ** _(project)_**   
Disk Limit   
`GAUGE`, `DOUBLE`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The disk limit of the broker in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`disk/used_bytes` GA ** _(project)_**   
Used Disk Bytes   
`GAUGE`, `DOUBLE`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Used bytes of the broker's disk. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`first_offset` GA ** _(project)_**   
First Offset   
`GAUGE`, `INT64`, `{offset}`   
**[managedkafka.googleapis.com/TopicPartition](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/TopicPartition)** |  _The first offset in the partition. This comes from MBean kafka.log:type=Log,name=LogStartOffset,topic=([-.\w]+),partition=([0-9]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`jvm/memory_area/bytes_committed` GA ** _(project)_**   
JVM Memory Area Committed Bytes   
`GAUGE`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Committed bytes of a given JVM memory area. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_name`: The name of the job.   
`task_index`: The index of the task.   
`area`: The memory area.   
`jvm/memory_area/bytes_used` GA ** _(project)_**   
JVM Memory Area Used Bytes   
`GAUGE`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _Used bytes of a given JVM memory area. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_name`: The name of the job.   
`task_index`: The index of the task.   
`area`: The memory area.   
`last_offset` GA ** _(project)_**   
Last Offset   
`GAUGE`, `INT64`, `{offset}`   
**[managedkafka.googleapis.com/TopicPartition](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/TopicPartition)** |  _The last offset in the partition. This comes from MBean kafka.log:type=Log,name=LogEndOffset,topic=([-.\w]+),partition=([0-9]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`log_segments` GA ** _(project)_**   
Log Segments   
`GAUGE`, `INT64`, `{log_segments}`   
**[managedkafka.googleapis.com/TopicPartition](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/TopicPartition)** |  _The current number of log segments. This comes from MBean kafka.log:type=Log,name=NumLogSegments,topic=([-.\w]+),partition=([0-9]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`memory/limit` GA ** _(project)_**   
Memory Limit   
`GAUGE`, `DOUBLE`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The memory limit of the broker in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`memory/usage` GA ** _(project)_**   
Memory Usage   
`GAUGE`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The memory usage of the broker in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`memory/worker_usage` GA ** _(project)_**   
Connect Cluster Worker Memory Usage   
`GAUGE`, `INT64`, `By`   
**[managedkafka.googleapis.com/ConnectCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/ConnectCluster)** |  _The worker memory usage of the worker in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the worker.   
`message_in_count` GA ** _(project)_**   
Message In Count   
`DELTA`, `INT64`, `{message}`   
**[managedkafka.googleapis.com/Topic](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Topic)** |  _The total number of messages that have been published to the topic. This comes from the MBean kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec,topic=([-.\w]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`mirror_source_connector_byte_rate` GA ** _(project)_**   
Mirror Source Connector Byte Rate   
`GAUGE`, `DOUBLE`, `{byte}/s`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _The average number of bytes per sec in replicated records, from MBean kafka.connect.mirror <type=MirrorSourceConnector, target=(.+), topic=(.+), partition=(.+)><>byte-rate. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`target`: The alias of target cluster.   
`topic`: The replicated topic on target cluster.   
`partition`: The partition being replicated on target cluster.   
`mirror_source_connector_bytes` GA ** _(project)_**   
Mirror Source Connector Byte Count   
`GAUGE`, `INT64`, `{byte}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _The number of bytes in replicated records, from MBean kafka.connect.mirror <type=MirrorSourceConnector, target=(.+), topic=(.+), partition=(.+)><>byte-count. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`target`: The alias of target cluster.   
`topic`: The replicated topic on target cluster.   
`partition`: The partition being replicated on target cluster.   
`mirror_source_connector_record_age` GA ** _(project)_**   
Mirror Source Connector Record Age   
`GAUGE`, `INT64`, `ms`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _The age of a record when they are replicated, from MBean kafka.connect.mirror <type=MirrorSourceConnector, target=(.+), topic=(.+), partition=(.+)><>record-age-ms. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`target`: The alias of target cluster.   
`topic`: The replicated topic on target cluster.   
`partition`: The partition being replicated on target cluster.   
`mirror_source_connector_record_rate` GA ** _(project)_**   
Mirror Source Connector Record Rate   
`GAUGE`, `DOUBLE`, `{record}/s`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _The rate of records replicated from source to target cluster, from MBean kafka.connect.mirror <type=MirrorSourceConnector, target=(.+), topic=(.+), partition=(.+)><>record-rate. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`target`: The alias of target cluster.   
`topic`: The replicated topic on target cluster.   
`partition`: The partition being replicated on target cluster.   
`mirror_source_connector_records` GA ** _(project)_**   
Mirror Source Connector Record Count   
`GAUGE`, `INT64`, `{record}`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _The number of records replicated from source to target cluster, from MBean kafka.connect.mirror <type=MirrorSourceConnector, target=(.+), topic=(.+), partition=(.+)><>record-count. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`target`: The alias of target cluster.   
`topic`: The replicated topic on target cluster.   
`partition`: The partition being replicated on target cluster.   
`mirror_source_connector_replication_latency` GA ** _(project)_**   
Mirror Source Connector Replication Latency   
`GAUGE`, `INT64`, `ms`   
**[managedkafka.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Connector)** |  _The time it takes a record to propagate from source to target, from MBean kafka.connect.mirror <type=MirrorSourceConnector, target=(.+), topic=(.+), partition=(.+)><>replication-latency-ms. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`worker_id`: The id of the connect worker.   
`target`: The alias of target cluster.   
`topic`: The replicated topic on target cluster.   
`partition`: The partition being replicated on target cluster.   
`mtls_truststore_update_count` GA ** _(project)_**   
mTLS Truststore Update Count   
`DELTA`, `INT64`, `{update}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _A cumulative count of mTLS Truststore update attempts for the Kafka cluster categorized by the update status. This metric increments each time an mTLS truststore update attempt concludes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of the last truststore update attempt. Can be SUCCESS or a failure reason.   
`offline_partitions` GA ** _(project)_**   
Offline Partitions   
`GAUGE`, `INT64`, `{partition}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The number of offline topic partitions as observed by this Controller, from MBean kafka.controller:type=KafkaController,name=OfflinePartitionsCount. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`controller_index`: The index of the controller.   
`offset_lag` GA ** _(project)_**   
Offset Lag   
`GAUGE`, `INT64`, `{message}`   
**[managedkafka.googleapis.com/TopicPartitionConsumerGroup](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/TopicPartitionConsumerGroup)** |  _The number of messages that the consumer group has not yet committed on the partition._  
`partitions` GA ** _(project)_**   
Partitions   
`GAUGE`, `INT64`, `{partition}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The current number of partitions handled by this broker. This comes from the MBean kafka.server:type=ReplicaManager,name=PartitionCount. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`request_byte_count` GA ** _(project)_**   
Request Byte Count   
`DELTA`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The total size, in bytes, of requests made to the Cluster. This comes from the MBean kafka.network:type=RequestMetrics,name=RequestBytes,request=([-.\w]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`request`: The type of the request.   
`broker_index`: The index of the broker.   
`request_count` GA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `{request}`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The total number of requests made to the broker. This comes from the MBean kafka.network:type=RequestMetrics,name=RequestsPerSec,request={Produce|FetchConsumer|FetchFollower},version=([0-9]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`broker_index`: The index of the broker.   
`request`: The type of the request.   
`request_latencies` GA ** _(project)_**   
Request Latencies   
`GAUGE`, `INT64`, `ms`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The number of milliseconds taken for each request, at various percentiles. This comes from MBean kafka.network:type=RequestMetrics,name=TotalTimeMs,request={Produce|FetchConsumer|FetchFollower}. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`request`: The type of the request.   
`percentile`: The latency percentile.   
`broker_index`: The index of the broker.   
`storage/long_term_usage` GA ** _(project)_**   
Long Term Storage Usage   
`GAUGE`, `INT64`, `By`   
**[managedkafka.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Cluster)** |  _The long term storage usage for the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`topic_error_count` GA ** _(project)_**   
Topic Error Count   
`DELTA`, `INT64`, `{error}`   
**[managedkafka.googleapis.com/Topic](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Topic)** |  _The total number failed requests made to the topic. This comes from the MBeans kafka.server:type=BrokerTopicMetrics,name=FailedProduceRequestsPerSec,topic=([-.\w]+) and kafka.server:type=BrokerTopicMetrics,name=FailedFetchRequestsPerSec,topic=([-.\w]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`request`: The type of the request.   
`broker_index`: The index of the broker.   
`topic_request_count` GA ** _(project)_**   
Topic Request Count   
`DELTA`, `INT64`, `{request}`   
**[managedkafka.googleapis.com/Topic](https://docs.cloud.google.com/monitoring/api/resources#tag_managedkafka.googleapis.com/Topic)** |  _The total number of requests made to the topic. This comes from the MBeans kafka.server:type=BrokerTopicMetrics,name=TotalProduceRequestsPerSec,topic=([-.\w]+) and kafka.server:type=BrokerTopicMetrics,name=TotalFetchRequestsPerSec,topic=([-.\w]+). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`request`: The type of the request.   
`broker_index`: The index of the broker.   
  
### maps

Metrics from [Google Maps Platform](https://developers.google.com/maps/documentation). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `maps.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`service/request_count` DEPRECATED ** _(project)_**   
Request Count (Deprecated)   
`DELTA`, `INT64`, `1`   
**[maps.googleapis.com/Api](https://docs.cloud.google.com/monitoring/api/resources#tag_maps.googleapis.com/Api)** |  _Use "maps.googleapis.com/service/v2/request_count" instead. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`grpc_status_code`: The numeric gRPC response code or canonical gRPC equivalent of the reported Google Maps Platform API HTTP response code. See code mapping in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`platform_type`: Platform type where Google Maps API query comes from.   
`response_code`: The response code of the Maps API call.   
`response_code_class`: The response code class of the Maps API call.   
`protocol`: The protocol of the request, for example, "http" or "grpc".   
`service/request_count_by_domain` GA ** _(project)_**   
Request count by domains   
`DELTA`, `INT64`, `1`   
**[maps.googleapis.com/Api](https://docs.cloud.google.com/monitoring/api/resources#tag_maps.googleapis.com/Api)** |  _The count of completed requests by top100 frequency domains. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`platform_type`: Platform type where Google Maps API query comes from, one of [PLATFORM_TYPE_JS, PLATFORM_TYPE_WEBSERVICE, PLATFORM_TYPE_UNKNOWN, PLATFORM_TYPE_ANDROID, PLATFORM_TYPE_IOS].   
`response_code_class`: The response code class of the Maps API call, one of [2xx, 3xx, 4xx, 5xx]   
`protocol`: The protocol of the request, for example, "http" or "grpc".   
`domain`: The domain of the request.   
`service/request_latencies` DEPRECATED ** _(project)_**   
Service Request Latencies (Deprecated)   
`DELTA`, `DISTRIBUTION`, `ms`   
**[maps.googleapis.com/Api](https://docs.cloud.google.com/monitoring/api/resources#tag_maps.googleapis.com/Api)** |  _Use "maps.googleapis.com/service/v2/request_latencies" instead. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`platform_type`: Platform type where Google Maps API query comes from.   
`response_code`: The response code of the Maps API call.   
`response_code_class`: The response code class of the Maps API call.   
`protocol`: The protocol of the request, for example, "http" or "grpc".   
`service/request_latencies_by_domain` GA ** _(project)_**   
Request latencies by domains   
`DELTA`, `DISTRIBUTION`, `ms`   
**[maps.googleapis.com/Api](https://docs.cloud.google.com/monitoring/api/resources#tag_maps.googleapis.com/Api)** |  _The latencies of completed requests by top100 frequency domains. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`platform_type`: Platform type of the request, for example, "IOS", "Android" or "Web service".   
`response_code_class`: The response code class of the Maps API call.   
`protocol`: The protocol of the request, for example, "http" or "grpc".   
`domain`: The domain of the request.   
`service/v2/request_count` GA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[maps.googleapis.com/Api](https://docs.cloud.google.com/monitoring/api/resources#tag_maps.googleapis.com/Api)** |  _The count of completed requests. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`grpc_status_code`: The numeric gRPC response code or canonical gRPC equivalent of the reported Google Maps Platform API HTTP response code. See code mapping in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`platform_type`: Platform type where Google Maps API query comes from.   
`response_code`: The response code of the Maps API call.   
`response_code_class`: The response code class of the Maps API call.   
`protocol`: The protocol of the request, for example, "http" or "grpc".   
`service/v2/request_latencies` GA ** _(project)_**   
Service Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[maps.googleapis.com/Api](https://docs.cloud.google.com/monitoring/api/resources#tag_maps.googleapis.com/Api)** |  _Distribution of latencies in milliseconds for non-streaming requests. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`platform_type`: Platform type where Google Maps API query comes from.   
`response_code`: The response code of the Maps API call.   
`response_code_class`: The response code class of the Maps API call.   
`protocol`: The protocol of the request, for example, "http" or "grpc".   
  
### memcache

Metrics from [Memorystore for Memcached](https://docs.cloud.google.com/memorystore/docs/memcached). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `memcache.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`node/active_connections` BETA ** _(project)_**   
Active connections   
`GAUGE`, `INT64`, `1`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Connections active in this Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/cache_memory` BETA ** _(project)_**   
Cache memory usage   
`GAUGE`, `INT64`, `By`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Bytes alloted for the Memcached cache in this node, grouped by whether that memory is used or not. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`used`: 0 for unused and 1 for used cache memory.   
`node/cpu/usage_time` BETA ** _(project)_**   
CPU usage time   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _CPU usage time by Memcached process grouped by user and kernel mode. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`mode`: CPU usage mode, e.g. user or kernel.   
`node/cpu/utilization` BETA ** _(project)_**   
CPU usage percent   
`DELTA`, `DOUBLE`, `10^2.%`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _CPU usage percent by Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/eviction_count` BETA ** _(project)_**   
Eviction count   
`DELTA`, `INT64`, `1`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Count of items evicted by this Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/hit_ratio` BETA ** _(project)_**   
Hit ratio   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Hit ratio, expressed as a percentage of the total cache requests excluding set operations. Values are numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/items` BETA ** _(project)_**   
Items   
`GAUGE`, `INT64`, `1`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Items stored in this Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/memory/utilization` BETA ** _(project)_**   
System memory utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Utilization of system memory by Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`node/operation_count` BETA ** _(project)_**   
Memcached operation count   
`DELTA`, `INT64`, `1`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Count of Memcached operations grouped by command and response_type (e.g. hit, miss). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`command`: Name of the Memcached command.   
`response_type`: Status of the operation, e.g. hit, miss.   
`node/received_bytes_count` BETA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Bytes received by this Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/sent_bytes_count` BETA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Bytes sent by this Memcached node. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`node/uptime` BETA ** _(project)_**   
Uptime   
`GAUGE`, `INT64`, `s`   
**[memcache_node](https://docs.cloud.google.com/monitoring/api/resources#tag_memcache_node)** |  _Time in seconds the node has been running. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
### memorystore

Metrics from [Memorystore](https://docs.cloud.google.com/memorystore/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `memorystore.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`instance/backup/last_backup_duration` GA ** _(project)_**   
Last backup duration   
`GAUGE`, `INT64`, `ms`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The duration of the last backup operation as milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`instance/backup/last_backup_size` GA ** _(project)_**   
Last backup size   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The size of the last backup in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`instance/backup/last_backup_start_time` GA ** _(project)_**   
Last backup start time   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The start time of the last backup operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`instance/backup/last_backup_status` GA ** _(project)_**   
Last backup status   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The status of the last backup operation as 1/0 (success/failure). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`backup_type`: The type of the backup, one of [ON_DEMAND, AUTOMATED].   
`instance/clients/average_connected_clients` GA ** _(project)_**   
Client connections - average   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean current number of client connections across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/clients/maximum_connected_clients` GA ** _(project)_**   
Client connections - maximum   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum current number of client connections across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/clients/total_connected_clients` GA ** _(project)_**   
Client connections - total   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Current number of client connections to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/commandstats/total_calls_count` GA ** _(project)_**   
Commands count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of Engine commands. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`instance/commandstats/total_usec_count` GA ** _(project)_**   
Commands time   
`DELTA`, `INT64`, `us`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The total time consumed per command. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`instance/cpu/average_utilization` GA ** _(project)_**   
CPU utilization - average   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean CPU utilization across the instance from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/cpu/maximum_utilization` GA ** _(project)_**   
CPU utilization - maximum   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum CPU utilization across the instance from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/cross_instance_replication/secondary_average_replication_offset_diff` GA ** _(project)_**   
Cross instance replication average offset diff   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Average replication offset difference between primary shards and secondary shards. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`secondary_instance_project_number`: Secondary instance project number.   
`secondary_instance_location`: Secondary instance location.   
`secondary_instance_id`: Secondary instance Id.   
`secondary_instance_uid`: Secondary instance uid.   
`instance/cross_instance_replication/secondary_maximum_replication_offset_diff` GA ** _(project)_**   
Cross instance replication maximum offset diff   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum replication offset difference between primary shards and secondary shards. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`secondary_instance_project_number`: Secondary instance project number.   
`secondary_instance_location`: Secondary instance location.   
`secondary_instance_id`: Secondary instance Id.   
`secondary_instance_uid`: Secondary instance uid.   
`instance/cross_instance_replication/secondary_replication_links` GA ** _(project)_**   
Cross instance replication links   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Number of replication links between a primary instance and a secondary instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`secondary_instance_project_number`: Secondary instance project number.   
`secondary_instance_location`: Secondary instance location.   
`secondary_instance_id`: Secondary instance Id.   
`secondary_instance_uid`: Secondary instance uid.   
`instance/import/last_import_duration` GA ** _(project)_**   
Last import duration   
`GAUGE`, `INT64`, `ms`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The duration of the last import operation as milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`import_type`: The type of the import, one of [CREATE_IMPORT, LIVE_IMPORT].   
`import_source`: The source of the import, one of [MANAGED_BACKUP, GCS_SOURCE].   
`instance/import/last_import_start_time` GA ** _(project)_**   
Last import start time   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The start time of the last import operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_string`: Status code description.   
`import_type`: The type of the import, one of [CREATE_IMPORT, LIVE_IMPORT].   
`import_source`: The source of the import, one of [MANAGED_BACKUP, GCS_SOURCE].   
`instance/keyspace/total_keys` GA ** _(project)_**   
Total keys   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Number of keys stored in the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/memory/average_utilization` GA ** _(project)_**   
Memory utilization - average   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean memory utilization across the instance from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/memory/maximum_utilization` GA ** _(project)_**   
Memory utilization - maximum   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum memory utilization across the instance from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/memory/size` GA ** _(project)_**   
Memory size   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Memory size of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/memory/total_used_memory` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Total memory usage of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/migration_status` BETA ** _(project)_**   
Migration status   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Represents the migration status of the instance. It is HEALTHY if expected number of primary nodes are migrating and healthy. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status`: The migration status of the instance, one of [HEALTHY, UNHEALTHY, NOT_APPLICABLE].   
`instance/node/bloomfilter/objects_count` GA ** _(project)_**   
Bloom filter objects count   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of bloom filter object in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/bloomfilter/used_memory` GA ** _(project)_**   
Bloom filter memory usage   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Memory consumed by the bloom filter objects in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/blocked_clients` GA ** _(project)_**   
Blocked connections   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of client connections blocked by the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/connected_clients` GA ** _(project)_**   
Client connections   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of clients connected to the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/maxclients` BETA ** _(project)_**   
Max Clients Configuration   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Max clients configuration from valkey conf. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/pubsub_clients` BETA ** _(project)_**   
Pubsub clients   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of clients in pubsub mode. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/recent_max_input_buffer` BETA ** _(project)_**   
Max input buffer   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Max input buffer in bytes among current client connections. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/recent_max_output_buffer` BETA ** _(project)_**   
Max output buffer   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Max output buffer in bytes among current client connections. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/tracking_clients` BETA ** _(project)_**   
Tracking clients   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of clients that are being tracked by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/clients/watching_clients` BETA ** _(project)_**   
Watching clients   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of clients in watching mode. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/commandstats/calls_count` GA ** _(project)_**   
Commands count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of calls for this command on the instance node in one minute. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`instance/node/commandstats/failed_calls_count` BETA ** _(project)_**   
Failed command calls   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of failed calls for this command. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: Command of the call.   
`instance/node/commandstats/rejected_calls_count` BETA ** _(project)_**   
Rejected command calls   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of rejected calls for this command. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: Command of the call.   
`instance/node/commandstats/usec_count` GA ** _(project)_**   
Commands time   
`DELTA`, `INT64`, `us`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The total time consumed per command in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`command`: The command executed.   
`instance/node/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _CPU utilization for the instance node from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`state`: CPU usage state, one of [sys, sys_children, sys_main_thread, user, user_children, user_main_thread]   
`instance/node/cross_instance_replication/follower_replication_offset_diff` GA ** _(project)_**   
Cross instance replication follower offset diff   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Replication offset diff in bytes between a replicator node and its follower node, reported by the replicator node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`secondary_instance_project_number`: Secondary instance project number.   
`secondary_instance_location`: Secondary instance Id.   
`secondary_instance_id`: Secondary instance Id.   
`secondary_instance_uid`: Secondary instance uid.   
`follower_node_id`: Follower node Id.   
`instance/node/cross_instance_replication/role` GA ** _(project)_**   
Cross instance replication role   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Cross instance replication role of the node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`ccr_role`: Cross instance replication role, one of [replicator, follower].   
`instance/node/errorstats/errors_count` BETA ** _(project)_**   
Errors count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Different error counters for errors occurred within the engine. The engine field name is errorstat_XXX, XXX can be MOVED, ERR, OOM etc.. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`error_type`: The error type, e.g. NO_ERR, ERR, MOVED, ASK, OOM etc..   
`instance/node/json/documents_count` GA ** _(project)_**   
JSON documents count   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of JSON documents in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/json/used_memory` GA ** _(project)_**   
JSON memory usage   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Memory consumed by the JSON documents in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/keyspace/keys_with_expiration` BETA ** _(project)_**   
keys with an expiration   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of keys with an expiration. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/keyspace/total_keys` GA ** _(project)_**   
Total keys   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of keys stored in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/dataset_usage` BETA ** _(project)_**   
Memory used by dataset   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Actual dataset memory usage. The engine field name is used_memory_dataset. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/lua_usage` BETA ** _(project)_**   
Memory used by Lua engine   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of bytes used by the Lua engine. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/maxmemory` BETA ** _(project)_**   
Max memory   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Maximum amount of memory valkey can consume, 0 means ram capping is disabled. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/maxmemory_policy` BETA ** _(project)_**   
Maxmemory policy   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The maxmemory policy configuration on the node level. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`maxmemory_policy`: The maxmemory policy configuration on the node level.   
`instance/node/memory/mem_not_counted_for_evict` BETA ** _(project)_**   
Memory not counted for eviction   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Used memory that's not counted for key eviction. This is basically a transient replica and AOF buffers. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/normal_clients_usage` BETA ** _(project)_**   
Memory Usage by normal clients   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of bytes used by normal clients. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/number_of_cached_scripts` BETA ** _(project)_**   
Number of cached scripts   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The number of EVAL scripts cached by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/number_of_functions` BETA ** _(project)_**   
Number of functions   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The number of functions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/peak_usage` BETA ** _(project)_**   
Peak memory usage   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Peak memory consumed by Valkey ever (in bytes). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/replica_clients_usage` BETA ** _(project)_**   
Memory Usage by replica clients   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of bytes used by replica clients. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/rss_usage` BETA ** _(project)_**   
Usage RSS   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of bytes that Valkey allocated as seen by the operating system (a.k.a resident set size). This is the number reported by tools such as top(1) and ps(1). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/scripts_usage` BETA ** _(project)_**   
Memory used by scripts   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of bytes overhead by the EVAL scripts and Function scripts (part of used memory). The engine field name is used_memory_scripts. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total memory usage of the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/memory/utilization` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Memory utilization within the instance node from 0.0 to 1.0. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/migration_link_reconnect_count` BETA ** _(project)_**   
Migration link reconnections   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of migration link reconnections. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/migration_received_bytes_size` BETA ** _(project)_**   
Migration received bytes   
`DELTA`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of migration bytes received. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/migration_status` BETA ** _(project)_**   
Migration status   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Represents the migration status of the node, e.g. if a primary node is in migrating state and replication link is up, it is HEALTHY. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status`: The migration status of the node, one of [HEALTHY, UNHEALTHY, NOT_APPLICABLE].   
`instance/node/persistence/aof_enabled` BETA ** _(project)_**   
AOF enabled   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Flag indicating if AOF is enabled. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/aof_fsync_errors_count` GA ** _(project)_**   
AOF fsync errors count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of AOF fsync errors on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/aof_fsync_lag` GA ** _(project)_**   
AOF fsync lag   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _AOF lag between memory and persistent store on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/aof_last_bgrewrite_status` GA ** _(project)_**   
AOF last bgrewrite success   
`GAUGE`, `BOOL`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Indicates the success of the last AOF bgrewrite operation on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_string`: Status code description.   
`instance/node/persistence/aof_last_cow_size` BETA ** _(project)_**   
Last AOF COW size   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The size in bytes of the copy-on-write memory during the last AOF rewrite operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/aof_last_rewrite_time_sec` BETA ** _(project)_**   
Last AOF rewrite duration   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Duration of the last AOF rewrite operation in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/aof_last_write_status` GA ** _(project)_**   
AOF last write success   
`GAUGE`, `BOOL`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Indicates the success of the last AOF write operation on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_string`: Status code description.   
`instance/node/persistence/aof_rewrite_in_progress` BETA ** _(project)_**   
AOF rewrite in progress   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Flag indicating if an AOF rewrite is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/aof_rewrites_count` GA ** _(project)_**   
AOF rewrites count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _AOF rewrites count on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_code`: (INT64) gRPC error code (e.g. 0=OK, 8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`instance/node/persistence/async_loading` BETA ** _(project)_**   
Async loading   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Flag indicating if async loading is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/auto_restore_count` GA ** _(project)_**   
Auto restore count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of restores from dumpfile on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_code`: (INT64) gRPC error code (e.g. 0=OK, 13=INTERNAL)   
`status_string`: Status code description.   
`persistence_mode`: "AOF" or "RDB".   
`instance/node/persistence/current_cow_peak` BETA ** _(project)_**   
Current COW peak   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Peak size in bytes of the copy-on-write memory during the current fork operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/current_cow_size` BETA ** _(project)_**   
Current COW size   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The size in bytes of the copy-on-write memory during the current fork operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/current_fork_percentage` BETA ** _(project)_**   
Current fork percentage   
`GAUGE`, `DOUBLE`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The percentage of the current fork operation progress (0-100). Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/current_save_keys_total` GA ** _(project)_**   
Keys in current save   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of keys at the beginning of the current save operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/loading` BETA ** _(project)_**   
Loading   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Flag indicating if loading is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/rdb_bgsave_in_progress` GA ** _(project)_**   
RDB BGSAVE in progress   
`GAUGE`, `BOOL`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Indicates if a RDB BGSAVE is currently in progress on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/rdb_last_bgsave_status` GA ** _(project)_**   
RDB last BGSAVE success   
`GAUGE`, `BOOL`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Indicates the success of the last BGSAVE on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_string`: Status code description.   
`instance/node/persistence/rdb_last_bgsave_time_sec` BETA ** _(project)_**   
Last BGSAVE duration   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Duration of the last RDB save operation in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/rdb_last_cow_size` BETA ** _(project)_**   
Last RDB COW size   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The size in bytes of the copy-on-write memory during the last RDB save operation. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/rdb_last_save_age` GA ** _(project)_**   
RDB last save age   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Measures the time in seconds, since the last successful snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/rdb_next_save_time_until` GA ** _(project)_**   
Time until next RDB snapshot   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Measures the time in seconds, remaining until the next snapshot. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/persistence/rdb_saves_count` GA ** _(project)_**   
RDB saves count.   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of RDB saves in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`status_code`: (INT64) gRPC error code (e.g. 0=OK, 8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`instance/node/replication/offset` GA ** _(project)_**   
Replication offset   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Measures the replication offset bytes of the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/replication/primary_sync_in_progress` BETA ** _(project)_**   
Primary sync in progress   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Flag indicating if a primary syncing to replica is in progress. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/replication/sync_full_count` BETA ** _(project)_**   
Full Resync Count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The total number of full resyncs with replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/replication/sync_partial_err_count` BETA ** _(project)_**   
Partial sync Error count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The number of denied partial resync requests. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/replication/sync_partial_ok_count` BETA ** _(project)_**   
Partial sync OK count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The number of accepted partial resync requests. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/server/healthy` GA ** _(project)_**   
Node is healthy   
`GAUGE`, `BOOL`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Indicates if Instance Node is healthy and available. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/server/uptime` GA ** _(project)_**   
Node uptime   
`GAUGE`, `INT64`, `s`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Measures the uptime of the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/acl_access_denied_auths_count` BETA ** _(project)_**   
ACL access denied authentications   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of ACL access denied authentication failures. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/acl_access_denied_channels_count` BETA ** _(project)_**   
ACL access denied channels count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of failed attempts by users to access channels they do not have permission to access. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/acl_access_denied_commands_count` BETA ** _(project)_**   
ACL access denied commands count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of failed attempts by users to run commands they don’t have permission to call. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/acl_access_denied_keys_count` BETA ** _(project)_**   
ACL access denied keys count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of failed attempts by users to access keys they don’t have permission to access. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/client_output_buffer_limit_disconnections_count` BETA ** _(project)_**   
Client output buffer limit disconnections count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of disconnections due to client reaching output buffer limit. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/client_query_buffer_limit_disconnections_count` BETA ** _(project)_**   
Client query buffer limit disconnections count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of disconnections due to client reaching query buffer limit. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/connections_received_count` GA ** _(project)_**   
Client connections - received   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of total client connections created in the last one minute on the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/evicted_clients_count` BETA ** _(project)_**   
Evicted client connections   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of client connections evicted due to client memory over eviction limit. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/evicted_keys_count` GA ** _(project)_**   
Evicted keys   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of evicted keys by the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/evicted_scripts_count` BETA ** _(project)_**   
Evicted scripts count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of evicted EVAL scripts due to LRU policy. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/expire_cycle_cpu_millisecond_count` BETA ** _(project)_**   
Expire cycle cpu milliseconds   
`DELTA`, `INT64`, `ms`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The total cumulative amount of time spent on active expiry cycles. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/expired_keys_count` GA ** _(project)_**   
Expired keys   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of key expiration events in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/expired_keys_percentage` BETA ** _(project)_**   
Expired stale key percentage   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The percentage of keys probably expired. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/expired_time_cap_reached_count` BETA ** _(project)_**   
Expired time cap reached count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _The total count of times that active expiry cycles have stopped early. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/keyspace_hits_count` GA ** _(project)_**   
Keyspace hits   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of successful lookup of keys in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/keyspace_misses_count` GA ** _(project)_**   
Keyspace misses   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of failed lookup of keys in the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/latest_fork_usec` BETA ** _(project)_**   
Latest fork duration   
`GAUGE`, `INT64`, `us`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Duration of the latest fork operation in microseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/net_input_bytes_count` GA ** _(project)_**   
Network bytes - incoming   
`DELTA`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of incoming network bytes received by the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/net_output_bytes_count` GA ** _(project)_**   
Network bytes - outgoing   
`DELTA`, `INT64`, `By`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Count of outgoing network bytes sent from the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/pubsub_channels` BETA ** _(project)_**   
Pub/Sub channels   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Global number of pub/sub channels with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/pubsub_patterns` BETA ** _(project)_**   
Pub/Sub patterns   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Global number of pub/sub patterns with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/pubsubshard_channels` BETA ** _(project)_**   
Pub/Sub shard channels   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Global number of pub/sub shard channels with client subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/rejected_connections_count` GA ** _(project)_**   
Client connections - rejected   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of connections rejected because of maxclients limit by the instance node. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/total_fork_count` BETA ** _(project)_**   
Total fork count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Total number of forks since server start. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/tracking_total_items` BETA ** _(project)_**   
Tracking total items   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of items (Sum of clients per key) being tracked by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/tracking_total_keys` BETA ** _(project)_**   
Tracking total keys   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of keys being tracked by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/node/stats/tracking_total_prefixes` BETA ** _(project)_**   
Tracking total prefixes   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/InstanceNode](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/InstanceNode)** |  _Number of tracked prefixes in server prefix table. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/persistence/aof_fsync_lags` GA ** _(project)_**   
AOF fsync lags.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Distribution of AOF lag between memory and persistent store across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/persistence/aof_rewrite_count` GA ** _(project)_**   
AOF rewrite count.   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of AOF rewrites across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_code`: (INT64) gRPC error code (e.g. 0=OK,8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`instance/persistence/rdb_last_success_ages` GA ** _(project)_**   
RDB snapshot ages.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Age of RDB snapshots across instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/persistence/rdb_saves_count` GA ** _(project)_**   
RDB saves count.   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of RDB saves across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status_code`: (INT64) gRPC error code (e.g. 0=OK,8=RESOURCE_EXHAUSTED, 13=INTERNAL)   
`status_string`: Status code description.   
`instance/replication/average_ack_lag` GA ** _(project)_**   
Replication acknowledge lag - average   
`GAUGE`, `DOUBLE`, `s`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean replication acknowledge lag (in seconds) of replica across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/replication/average_offset_diff` GA ** _(project)_**   
Replication offset diff - average   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean replication offset diff (in bytes) across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/replication/maximum_ack_lag` GA ** _(project)_**   
Replication acknowledge lag - maximum   
`GAUGE`, `DOUBLE`, `s`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum replication acknowledge lag (in seconds) of replica across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/replication/maximum_offset_diff` GA ** _(project)_**   
Replication offset diff - maximum   
`GAUGE`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum replication offset diff (in bytes) across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/attributes` GA ** _(project)_**   
Vector search attributes   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The number of attributes across all indexes for vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/average_used_memory_bytes` GA ** _(project)_**   
Vector search average used memory   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The average per-node used memory for all search functionality, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/background_indexing_in_progress` GA ** _(project)_**   
Vector search background indexing in progress   
`GAUGE`, `BOOL`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Indicates if the background indexing is in progress across any index. When the metric value is true, background indexing is in progress in at least one index. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/indexed_keys` GA ** _(project)_**   
Vector search indexed keys   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The number of keys indexed across all indexes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/indexes` GA ** _(project)_**   
Vector search indexes   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The number of indexes created for searching for vector search. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/maximum_used_memory_bytes` GA ** _(project)_**   
Vector search maximum used memory   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The maximum per-node used memory for all search functionality, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/search/query_requests_count` GA ** _(project)_**   
Vector search query request count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The number of query requests across all indexes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`status`: Success or failure of the query request. one of [success, failure].   
`role`: The replication role, one of [primary, replica].   
`instance/search/total_used_memory_bytes` GA ** _(project)_**   
Vector search total used memory   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _The total used memory in bytes for all search functionality in all nodes, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/security/rotate_tls_cert_count` BETA ** _(project)_**   
TLS certificate rotation count   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of TLS certificate rotations on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`status`: The status of the TLS certificate rotation.   
`failure_reason`: The failure reason of the TLS certificate rotation.   
`rotation_trigger_source`: The trigger source of the TLS certificate rotation.   
`instance/stats/average_evicted_keys` GA ** _(project)_**   
Evicted keys - average   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean number of evicted keys due to memory capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/stats/average_expired_keys` GA ** _(project)_**   
Expired keys - average   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/stats/average_keyspace_hits` GA ** _(project)_**   
Keyspace hits - average   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean number of successful lookup of keys across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/average_keyspace_misses` GA ** _(project)_**   
Keyspace misses - average   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Mean number of failed lookup of keys across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/maximum_evicted_keys` GA ** _(project)_**   
Evicted keys - maximum   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum number of evicted keys due to memory capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/stats/maximum_expired_keys` GA ** _(project)_**   
Expired keys - maximum   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/stats/maximum_keyspace_hits` GA ** _(project)_**   
Keyspace hits - maximum   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum number of successful lookup of keys across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/maximum_keyspace_misses` GA ** _(project)_**   
Keyspace misses - maximum   
`GAUGE`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Maximum number of failed lookup of keys across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/total_connections_received_count` GA ** _(project)_**   
Client connections - received   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of client connections created in the last one minute. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/total_evicted_keys_count` GA ** _(project)_**   
Evicted keys - total   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Total number of evicted keys due to memory capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/stats/total_expired_keys_count` GA ** _(project)_**   
Expired keys - total   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Total number of key expiration events. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`instance/stats/total_keyspace_hits_count` GA ** _(project)_**   
Keyspace Hits - total   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Total number of successful lookup of keys across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/total_keyspace_misses_count` GA ** _(project)_**   
Keyspace misses - total   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Total number of failed lookup of keys across the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/total_net_input_bytes_count` GA ** _(project)_**   
Network bytes - incoming total   
`DELTA`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of incoming network bytes received by the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/total_net_output_bytes_count` GA ** _(project)_**   
Network bytes - outgoing total   
`DELTA`, `INT64`, `By`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of outgoing network bytes sent from the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
`instance/stats/total_rejected_connections_count` GA ** _(project)_**   
Client connections - rejected   
`DELTA`, `INT64`, `1`   
**[memorystore.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_memorystore.googleapis.com/Instance)** |  _Count of client connections rejected because of maxclients limit. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`role`: The replication role, one of [primary, replica].   
  
### metastore

Metrics from [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/monitoring). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `metastore.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`federation/health` BETA ** _(project)_**   
Federation service health   
`GAUGE`, `INT64`, `1`   
**[metastore.googleapis.com/Federation](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Federation)** |  _The health of the Federated Dataproc Metastore Service._   
`version`: The Hive Metastore version of the service.   
`federation/server/request_count` BETA ** _(project)_**   
Federation service request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Federation](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Federation)** |  _The number of requests sent to the Federated Dataproc Metastore Service._   
`method_name`: The request method name.   
`status`: End status of the request, one of [success, client_error, server_error].   
`version`: The Hive Metastore version of the service.   
`service/database_cpu_utilization` BETA ** _(project)_**   
Database CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The database CPU utilization of the Dataproc Metastore Service._   
`database_type`: The type of database, one of [SQL, Spanner].   
`service/grpc/finished_requests_count` BETA ** _(project)_**   
gRPC Requests Finished Count   
`DELTA`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests finished by the GRPC Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service, such as ENTERPRISE.   
`version`: The Hive Metastore version of the service.   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc/received_bytes_count` BETA ** _(project)_**   
gRPC Bytes Received   
`DELTA`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes received by the Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`service/grpc/request_latencies` BETA ** _(project)_**   
gRPC Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Distribution of gRPC request latencies for a Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc/sent_bytes_count` BETA ** _(project)_**   
gRPC Bytes Sent   
`DELTA`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes sent by the Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`service/grpc/started_requests_count` BETA ** _(project)_**   
gRPC Requests Started Count   
`DELTA`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests received and started by the GRPC Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service.   
`version`: The Hive Metastore version of the service.   
`method_name`: The request method name.   
`service/grpc_client/finished_requests_count` BETA ** _(project)_**   
gRPC Client Requests Finished Count   
`CUMULATIVE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Total number of RPCs completed on the client, regardless of success or failure._   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc_client/received_bytes_count` BETA ** _(project)_**   
gRPC Client Bytes Received   
`CUMULATIVE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes received by the gRPC client._  
`service/grpc_client/request_latencies` BETA ** _(project)_**   
gRPC Client Request Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Distribution of gRPC request latencies for a Dataproc Metastore Service._   
`status`: The gRPC status code of the request, such as `NOT_FOUND`.   
`method_name`: The request method name.   
`service/grpc_client/sent_bytes_count` BETA ** _(project)_**   
gRPC Client Bytes Sent   
`CUMULATIVE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Number of bytes sent by the gRPC client._  
`service/grpc_client/started_requests_count` BETA ** _(project)_**   
gRPC Client Requests Started Count   
`CUMULATIVE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests started by the gRPC client._   
`method_name`: The request method name.   
`service/health` GA ** _(project)_**   
Service health   
`GAUGE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The health of the Dataproc Metastore Service._   
`tier`: Service tier or instance size of the service, such as ENTERPRISE.   
`version`: The Hive Metastore version of the service.   
`release_tag`: Dataproc Metastore release tag, populated by the service backend and may change over service lifetime.   
`service/metadata/bytes_used` BETA ** _(project)_**   
Size of the metadata stored in the Dataproc Metastore service.   
`GAUGE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The amount of data that is stored in the backend database of the service._   
`version`: The Hive Metastore version of the service.   
`database_type`: The type of database, one of [SQL, Spanner].   
`service/migration/replication_lag` BETA ** _(project)_**   
Replication pipeline processing latency in seconds.   
`GAUGE`, `DOUBLE`, `s`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Current maximum duration in seconds taken to replicate data to Dataproc Metastore._   
`migration_id`: The migration ID.   
`service/migration/write_throughput` BETA ** _(project)_**   
Destination database write throughput.   
`GAUGE`, `DOUBLE`, `By/s`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _Current write throughput at the Dataproc Metastore database where the data is being copied to during the replication phase._   
`migration_id`: The migration ID.   
`service/multi_region/health` GA ** _(project)_**   
Multiregional service health   
`GAUGE`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The health of the multiregional Dataproc Metastore Service._   
`version`: The Hive Metastore version of the service.   
`release_tag`: Dataproc Metastore release tag, populated by the service backend and may change over service lifetime.   
`service_region`: The constituent region that Dataproc Metastore service is hosted in.   
`scaling_factor`: Scaling factor of the service, one of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0].   
`service/multi_region/request_count` GA ** _(project)_**   
Multiregional service request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests sent to the multiregional Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service_region`: The constituent region that Dataproc Metastore service is hosted in.   
`scaling_factor`: Scaling factor of the service, one of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0].   
`service/multi_region/request_latencies` GA ** _(project)_**   
Multiregional service request latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The latencies of the requests sent to the multiregional Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service_region`: The constituent region that Dataproc Metastore service is hosted in.   
`scaling_factor`: Scaling factor of the service, one of [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0].   
`service/query_metadata/request_count` BETA ** _(project)_**   
Admin Interface request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of Admin Interface requests._   
`database_type`: The type of database, one of [SQL, Spanner].   
`code`: The gRPC status code.   
`service/query_metadata/request_latencies` BETA ** _(project)_**   
Admin Interface request latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The end to end request latency for Admin Interface requests._   
`database_type`: The type of database, one of [SQL, Spanner].   
`code`: The gRPC status code.   
`service/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `{request}`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of requests sent to the Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service/request_latencies` BETA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The latencies of the requests sent to the Dataproc Metastore Service._   
`method_name`: The request method name.   
`version`: The Hive Metastore version of the service.   
`service/scheduled_backups/backup_count` BETA ** _(project)_**   
Scheduled Backups Count   
`DELTA`, `INT64`, `1`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The number of scheduled backups currently stored for the service._   
`state`: State of the backup, one of [SUCCEEDED, FAILED, IN_PROGRESS].   
`database_type`: The type of database, one of [SQL, Spanner].   
`version`: The Hive Metastore version of the service.   
`service/scheduled_backups/last_backup_duration` BETA ** _(project)_**   
Scheduled Backups - Last Backup Duration   
`GAUGE`, `INT64`, `s`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The duration of the last successful scheduled backup in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of the backup, one of [SUCCEEDED, FAILED, IN_PROGRESS].   
`database_type`: The type of database, one of [SQL, Spanner].   
`version`: The Hive Metastore version of the service.   
`service/scheduled_backups/last_backup_size` BETA ** _(project)_**   
Scheduled Backups Request - Last Backup Size   
`GAUGE`, `INT64`, `By`   
**[metastore.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_metastore.googleapis.com/Service)** |  _The size of the last successful scheduled backup in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of the backup, one of [SUCCEEDED, FAILED, IN_PROGRESS].   
`database_type`: The type of database, one of [SQL, Spanner].   
`version`: The Hive Metastore version of the service.   
  
### ml

Metrics from [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics) (formerly Cloud Machine Learning). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `ml.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`prediction/error_count` GA ** _(project)_**   
Error count   
`DELTA`, `INT64`, `1`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Cumulative count of prediction errors. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`prediction_type`: One of the CloudML prediction types: online_prediction, batch_prediction.   
`prediction/latencies` GA ** _(project)_**   
Latency   
`DELTA`, `DISTRIBUTION`, `us`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Latency of a certain type. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`latency_type`: One of the following: overhead, model, or user. Aggregating these three gives us the total latency.   
`prediction/online/accelerator/duty_cycle` ALPHA ** _(project)_**   
Accelerator duty cycle   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Average fraction of time over the past sample period during which the accelerator(s) were actively processing. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`replica_id`: Unique ID corresponding to the model replica.   
`prediction/online/accelerator/memory/bytes_used` ALPHA ** _(project)_**   
Accelerator memory usage   
`GAUGE`, `INT64`, `By`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Amount of accelerator memory allocated by the model replica. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`replica_id`: Unique ID corresponding to the model replica.   
`prediction/online/cpu/utilization` ALPHA ** _(project)_**   
CPU usage   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Fraction of CPU allocated by the model replica and currently in use. May exceed 100% if the machine type has multiple CPUs. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`replica_id`: Unique ID corresponding to the model replica.   
`prediction/online/memory/bytes_used` ALPHA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Amount of memory allocated by the model replica and currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`replica_id`: Unique ID corresponding to the model replica.   
`prediction/online/network/bytes_received` ALPHA ** _(project)_**   
Network bytes received   
`DELTA`, `INT64`, `By`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Number of bytes received over the network by the model replica. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`replica_id`: ID corresponding to the model replica.   
`prediction/online/network/bytes_sent` ALPHA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Number of bytes sent over the network by the model replica. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`replica_id`: Unique ID corresponding to the model replica.   
`prediction/online/replicas` ALPHA ** _(project)_**   
Replica count   
`GAUGE`, `INT64`, `1`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Number of active model replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`prediction/online/target_replicas` ALPHA ** _(project)_**   
Replica target   
`GAUGE`, `INT64`, `1`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Aspired number of active model replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`prediction/prediction_count` GA ** _(project)_**   
Prediction count   
`DELTA`, `INT64`, `1`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Cumulative count of predictions. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`prediction_type`: One of the CloudML prediction types: online_prediction, batch_prediction.   
`prediction/response_count` GA ** _(project)_**   
Response count   
`DELTA`, `INT64`, `1`   
**[cloudml_model_version](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_model_version)** |  _Cumulative count of different response codes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`prediction_type`: One of the CloudML prediction types: online_prediction, batch_prediction.   
`response_code`: (INT64) The http response code.   
`training/accelerator/memory/utilization` BETA ** _(project)_**   
Accelerator memory utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Fraction of allocated accelerator memory that is currently in use. Values are numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the CloudML training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
`training/accelerator/utilization` BETA ** _(project)_**   
Accelerator utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Fraction of allocated accelerator that is currently in use. Values are numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the CloudML training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
`training/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Fraction of allocated CPU that is currently in use. Values are numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the CloudML training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
`training/disk/utilization` GA ** _(project)_**   
Disk bytes used   
`GAUGE`, `INT64`, `By`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Number of bytes used by the training job. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the Vertex AI training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
`training/memory/utilization` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Fraction of allocated memory that is currently in use. Values are numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the CloudML training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
`training/network/received_bytes_count` GA ** _(project)_**   
Network bytes received   
`DELTA`, `INT64`, `By`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Number of bytes received by the training job over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the CloudML training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
`training/network/sent_bytes_count` GA ** _(project)_**   
Network bytes sent   
`DELTA`, `INT64`, `By`   
**[cloudml_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudml_job)** |  _Number of bytes sent by the training job over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`task_type`: One of the CloudML training job task types: master, worker or ps (for Parameter Server).   
`task_index`: (INT64) Zero based task index.   
`trial_id`: ID of hyperparameter trial.   
  
### modelarmor

Metrics from [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `modelarmor.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`template/malicious_uri_request_count` BETA ** _(project, folder, organization)_**   
Malicious URI Filter Count   
`DELTA`, `INT64`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _The number of requests detected with malicious uri content against a template. Sampled every 60 seconds._   
`match_found`: (BOOL) Whether a match was found in the request for the malicious uri filter.   
`operation_type`: Sanitize API Operation type. It can be SANITIZE_USER_PROMPT or SANITIZE_MODEL_RESPONSE.   
`client_name`: The name of the client making the request.   
`template/pi_jb_request_count` BETA ** _(project, folder, organization)_**   
Prompt Injection and Jailbreak Filter Count   
`DELTA`, `INT64`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _The number of requests detected with Prompt Injection and Jailbreak content against a template. Sampled every 60 seconds._   
`match_found`: (BOOL) Whether a match was found in the request for the Prompt Injection and Jailbreak filter.   
`operation_type`: Sanitize API Operation type. It can be SANITIZE_USER_PROMPT or SANITIZE_MODEL_RESPONSE.   
`confidence_level`: Confidence Level of Model Armor detections. It can be NA, LOW_AND_ABOVE, MEDIUM_AND_ABOVE or HIGH.   
`client_name`: The name of the client making the request.   
`template/rai_request_count` BETA ** _(project, folder, organization)_**   
Responsible AI Filter Count   
`DELTA`, `INT64`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _The number of requests detected with Responsible AI filters content against a template. Sampled every 60 seconds._   
`match_found`: (BOOL) Whether a match was found in the request for the Responsible AI filter.   
`operation_type`: Sanitize API Operation type. It can be SANITIZE_USER_PROMPT or SANITIZE_MODEL_RESPONSE.   
`filter_sub_type`: Responsible AI filter subtype. It can be DANGEROUS, SEXUALLY_EXPLICIT, HATE_SPEECH or HARASSMENT.   
`confidence_level`: Confidence Level of Model Armor detections. It can be NA, LOW_AND_ABOVE, MEDIUM_AND_ABOVE or HIGH.   
`client_name`: The name of the client making the request.   
`template/request_count` BETA ** _(project, folder, organization)_**   
SanitizeAPI Request Count   
`DELTA`, `INT64`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _The number of requests received by Model Armor sanitize APIs. Sampled every 60 seconds._   
`match_found`: (BOOL) Whether a match was found in the request for any filter.   
`operation_type`: Sanitize API Operation type. It can be SANITIZE_USER_PROMPT or SANITIZE_MODEL_RESPONSE.   
`client_name`: The name of the client making the request.   
`sanitization_verdict`: The verdict of the sanitization. It can be BLOCKED or ALLOWED.   
`template/sdp_request_count` BETA ** _(project, folder, organization)_**   
Sensitive Data Protection Filter Count   
`DELTA`, `INT64`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _The number of requests detected with Sensitive Data Protection content against a template. Sampled every 60 seconds._   
`match_found`: (BOOL) Whether a match was found in the request for the Sensitive Data Protection filter.   
`operation_type`: Sanitize API Operation type. It can be SANITIZE_USER_PROMPT or SANITIZE_MODEL_RESPONSE.   
`filter_sub_type`: Sensitive Data Protection filter subtype. It can be BASIC or ADVANCED.   
`sdp_data_type`: Type of data detected by Sensitive Data Protection. It can be NA, SSN, GCP_API_KEY, GCP_EUC, etc.   
`transformed`: (BOOL) If the content was transformed.   
`client_name`: The name of the client making the request.   
`template/unsanitized_payload_count` BETA ** _(project, folder, organization)_**   
Unsanitized Payload Count   
`DELTA`, `INT64`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _Total count of requests where sanitization could not be fully completed. Sampled every 60 seconds._   
`verdict`: The final decision (ALLOW, BLOCK, ERROR).   
`verdict_reason`: The primary reason for the verdict.   
`api_service_name`: The API service name being called.   
`api_provider`: The API Provider format.   
`template/used_token_count` BETA ** _(project, folder, organization)_**   
Used Token Count   
`DELTA`, `DOUBLE`, `1`   
**[modelarmor.googleapis.com/Template](https://docs.cloud.google.com/monitoring/api/resources#tag_modelarmor.googleapis.com/Template)** |  _The number of tokens processed against a template. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operation_type`: Sanitize API Operation type. It can be SANITIZE_USER_PROMPT or SANITIZE_MODEL_RESPONSE.   
`client_name`: The name of the client making the request.   
  
### monitoring

Metrics from [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `monitoring.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`billing/bytes_ingested` GA ** _(project)_**   
Metric bytes ingested   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Chargeable number of bytes of metric data ingested. Sampled every 60 seconds. After sampling, data is not visible for up to 1020 seconds._   
`metric_domain`: Domain name prefix from the metric type.   
`metric_type`: Metric type for the ingested data.   
`resource_type`: Monitored resource type for the ingested data.   
`billing/bytes_ingested_hourly` GA ** _(project)_**   
Metric bytes ingested hourly   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Chargeable number of bytes of metric data ingested, aggregated hourly. Sampled every 3600 seconds. After sampling, data is not visible for up to 8220 seconds._   
`metric_domain`: Domain name prefix from the metric type.   
`metric_type`: Metric type for the ingested data.   
`resource_type`: Monitored resource type for the ingested data.   
`billing/samples_ingested` GA ** _(project)_**   
Metric samples ingested   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Chargeable number of samples of metric data ingested. Chargeable usage reported as samples ingested is never reported as bytes ingested, and vice versa. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`metric_domain`: Domain name prefix from the metric type.   
`metric_type`: Metric type for the ingested data.   
`resource_type`: Monitored resource type for the ingested data.   
`billing/samples_ingested_hourly` GA ** _(project)_**   
Metric samples ingested hourly   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Chargeable number of samples of metric data ingested, aggregated hourly. Chargeable usage reported as samples ingested is never reported as bytes ingested, and vice versa. Sampled every 3600 seconds. After sampling, data is not visible for up to 7500 seconds._   
`metric_domain`: Domain name prefix from the metric type.   
`metric_type`: Metric type for the ingested data.   
`resource_type`: Monitored resource type for the ingested data.   
`billing/time_series_billed_for_queries_count` GA ** _(project)_**   
Count of time series billed for queries   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _The number of time series billed for queries. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`api_method`: The fully qualified name of the API method which billed the time series.   
`collection/attribution/write_sample_count` BETA ** _(project)_**   
Samples written by attribution id   
`DELTA`, `INT64`, `1`   
**[monitoring.googleapis.com/MetricIngestionAttribution](https://docs.cloud.google.com/monitoring/api/resources#tag_monitoring.googleapis.com/MetricIngestionAttribution)** |  _The number of chargeable metric samples written that are tagged with a reporting attribution dimension._   
`metric_domain`: The metric domain.   
`metric_type`: The metric type.   
`resource_type`: The monitored resource type.   
`collection/write_request_point_count` DEPRECATED ** _(project)_**   
(DEPRECATED) Metric write requests   
`DELTA`, `INT64`, `1`   
**[monitoring.googleapis.com/MetricStatistics](https://docs.cloud.google.com/monitoring/api/resources#tag_monitoring.googleapis.com/MetricStatistics)** |  _The number of metric points written. One request may contain multiple points, which are counted separately. This metric is deprecated. Please refer to https://cloud.google.com/monitoring/docs/metrics-management#diagnostics and https://cloud.google.com/monitoring/docs/metrics-management#view-summary for how monitor the ingestion of metrics._   
`resource_type`: The monitored resource type.   
`status`: The status code for the write attempt, for example, "OK" or "INVALID_ARGUMENT".   
`stats/filtered_byte_count` ALPHA ** _(project)_**   
Filtered byte count   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes of metric data filtered through Metric Exclusion rules. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`metric_domain`: Domain name prefix from the metric type.   
`metric_type`: Metric type that was filtered.   
`resource_type`: Monitored resource type for the filtered metric.   
`filter_id`: The Metric Exclusion rule ID which caused this metric to be filtered.   
`stats/filtered_sample_count` ALPHA ** _(project)_**   
Filtered sample count   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of samples of metric data filtered through Metric Exclusion rules. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`metric_domain`: Domain name prefix from the metric type.   
`metric_type`: Metric type that was filtered.   
`resource_type`: Monitored resource type for the filtered metric.   
`filter_id`: The Metric Exclusion rule ID which caused this metric to be filtered.   
`stats/metrics_queried_hourly_count` GA ** _(project)_**   
Metrics queried hourly count   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of API queries by metric type and origin. Only recorded for user metrics. Sampled every 3600 seconds. After sampling, data is not visible for up to 7380 seconds._   
`api_method`: The fully qualified name of the API method through which the metric was queried.   
`origin`: The origin of the query, one of [console, other].   
`metric_type`: Metric type for the queried data.   
`stats/num_time_series` GA ** _(project)_**   
Time series count   
`GAUGE`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of active time series for user-defined metrics under custom.googleapis.com and logging.googleapis.com/user. An active time series is one that has received data in the previous 24 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`prefix`: Metric type name prefix for the encompassed data, one of [custom.googleapis.com, logging.googleapis.com/user].   
`uptime_check/check_passed` GA ** _(project)_**   
Check passed   
`GAUGE`, `BOOL`, ``   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)**   
**[servicedirectory_service](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service)**   
**[uptime_url](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)** |  _True if the resource passed the check. After sampling, data is not visible for up to 35 seconds._   
`check_id`: The Uptime check for which the request was made.   
`checker_location`: For external checks, the Uptime Monitoring location making the request.   
`checker_project_id`: For internal checks, the checker project.   
`checker_network`: For internal checks, the checker network.   
`checker_zone`: For internal checks, the checker zone.   
`checked_resource_id`: ID of the resource being checked. Format depends on resource type.   
`uptime_check/content_mismatch` GA ** _(project)_**   
Content mismatch   
`GAUGE`, `BOOL`, ``   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)**   
**[servicedirectory_service](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service)**   
**[uptime_url](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)** |  _True if the response failed to match the check's specification of required content. After sampling, data is not visible for up to 35 seconds._   
`check_id`: The Uptime check for which the request was made.   
`checker_location`: For external checks, the Uptime Monitoring location making the request.   
`checker_project_id`: For internal checks, the checker project.   
`checker_network`: For internal checks, the checker network.   
`checker_zone`: For internal checks, the checker zone.   
`checked_resource_id`: ID of the resource being checked. Format depends on resource type.   
`uptime_check/error_code` GA ** _(project)_**   
Error code   
`GAUGE`, `STRING`, ``   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)**   
**[servicedirectory_service](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service)**   
**[uptime_url](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)** |  _Error, if any, that prevented contact with the resource. After sampling, data is not visible for up to 35 seconds._   
`check_id`: The Uptime check for which the request was made.   
`checker_location`: For external checks, the Uptime Monitoring location making the request.   
`checker_project_id`: For internal checks, the checker project.   
`checker_network`: For internal checks, the checker network.   
`checker_zone`: For internal checks, the checker zone.   
`checked_resource_id`: ID of the resource being checked. Format depends on resource type.   
`uptime_check/http_status` GA ** _(project)_**   
HTTP status   
`GAUGE`, `STRING`, ``   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)**   
**[servicedirectory_service](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service)**   
**[uptime_url](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)** |  _HTTP response code returned by the resource. After sampling, data is not visible for up to 35 seconds._   
`check_id`: The Uptime check for which the request was made.   
`checker_location`: For external checks, the Uptime Monitoring location making the request.   
`checker_project_id`: For internal checks, the checker project.   
`checker_network`: For internal checks, the checker network.   
`checker_zone`: For internal checks, the checker zone.   
`checked_resource_id`: ID of the resource being checked. Format depends on resource type.   
`uptime_check/request_latency` GA ** _(project)_**   
Request latency   
`GAUGE`, `DOUBLE`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)**   
**[servicedirectory_service](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service)**   
**[uptime_url](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)** |  _The request latency in milliseconds measured by Uptime Monitoring when executing the request. After sampling, data is not visible for up to 35 seconds._   
`check_id`: The Uptime check for which the request was made.   
`checker_location`: For external checks, the Uptime Monitoring location making the request.   
`checker_project_id`: For internal checks, the checker project.   
`checker_network`: For internal checks, the checker network.   
`checker_zone`: For internal checks, the checker zone.   
`checked_resource_id`: ID of the resource being checked. Format depends on resource type.   
`uptime_check/time_until_ssl_cert_expires` GA ** _(project)_**   
Time until SSL certificate expires   
`GAUGE`, `DOUBLE`, `d`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_service](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_service)**   
**[servicedirectory_service](https://docs.cloud.google.com/monitoring/api/resources#tag_servicedirectory_service)**   
**[uptime_url](https://docs.cloud.google.com/monitoring/api/resources#tag_uptime_url)** |  _The number of days until the SSL certificate on the resource expires. After sampling, data is not visible for up to 35 seconds._   
`check_id`: The Uptime check for which the request was made.   
`checker_location`: For external checks, the Uptime Monitoring location making the request.   
`checker_project_id`: For internal checks, the checker project.   
`checker_network`: For internal checks, the checker network.   
`checker_zone`: For internal checks, the checker zone.   
`checked_resource_id`: ID of the resource being checked. Format depends on resource type.   
  
### netapp

Metrics from [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `netapp.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`replication/current_transfer_bytes` GA ** _(project)_**   
Volume Replication Transfer Progress   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _Amount of data transferred thus far for the current job._  
`replication/healthy` GA ** _(project)_**   
Volume Replication Healthy   
`GAUGE`, `BOOL`, ``   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _FALSE if a scheduled transfer is missed or is unhealthy._  
`replication/lag_time` GA ** _(project)_**   
Volume Replication Transfer Lag Time   
`GAUGE`, `INT64`, `s`   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _Time since the snapshot for transfer was taken on source (includes transfer duration)._  
`replication/last_transfer_duration` GA ** _(project)_**   
Volume Replication Last Transfer Duration   
`GAUGE`, `INT64`, `s`   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _Duration of the last transfer job._  
`replication/last_transfer_size` GA ** _(project)_**   
Volume Replication Last Transfer Size   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _Size of the last transfer job._  
`replication/total_transfer_byte_count` GA ** _(project)_**   
Volume Replication Total Transfer Bytes   
`CUMULATIVE`, `INT64`, `By`   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _Cumulative data transferred for the relationship since it was created. May reset to 0._  
`replication/transferring` GA ** _(project)_**   
Volume Replication Status   
`GAUGE`, `BOOL`, ``   
**[netapp.googleapis.com/Replication](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Replication)** |  _Status of replication: TRUE = transferring, FALSE = idle._  
`storage_pool/allocated` GA ** _(project)_**   
Storage pool space usage   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Storage pool capacity allocated to volumes._  
`storage_pool/auto_tiering/cold_tier_read_byte_count` GA ** _(project)_**   
StoragePool cold tier read bytes   
`DELTA`, `INT64`, `By`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Capacity read from cold tier of the StoragePool._  
`storage_pool/auto_tiering/cold_tier_write_byte_count` GA ** _(project)_**   
StoragePool cold tier write bytes   
`DELTA`, `INT64`, `By`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Capacity write to cold tier of the StoragePool._  
`storage_pool/auto_tiering/tiered_bytes` GA ** _(project)_**   
Auto tiering storage pool capacity tiering type size   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Storage pool capacity tiering types: cold, or non-cold._   
`type`: Type of tiered data, cold or or non-cold.   
`storage_pool/capacity` GA ** _(project)_**   
Storage pool capacity   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Total size of the storage pool._   
`custom_performance_enabled`: Whether the storage pool has custom performance enabled.   
`storage_pool/iops_limit` GA ** _(project)_**   
Maximum IOPS   
`GAUGE`, `INT64`, `1`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Maximum IOPS set for the pool._   
`type`: Type of IOPS, allocated or used.   
`storage_pool/replication_status` GA ** _(project)_**   
Replication Status   
`GAUGE`, `INT64`, `1`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Replication status for regional Flex StoragePool._   
`state`: Replication status: Synced, CatchingUp, OutOfSync.   
`storage_pool/throughput_limit` GA ** _(project)_**   
Maximum Throughput   
`GAUGE`, `INT64`, `MiB/s`   
**[netapp.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/StoragePool)** |  _Maximum throughput set for the pool._   
`type`: Type of throughput, allocated or used.   
`volume/allocated_bytes` GA ** _(project)_**   
Volume space allocated   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Capacity allocated to volume from the storage pool._  
`volume/auto_tiering/cold_tier_read_byte_count` GA ** _(project)_**   
Volume cold tier read bytes   
`DELTA`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Capacity read from cold tier of the of the volume._  
`volume/auto_tiering/cold_tier_write_byte_count` GA ** _(project)_**   
Volume cold tier write bytes   
`DELTA`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Capacity write to cold tier of the of the volume._  
`volume/auto_tiering/tiered_bytes` GA ** _(project)_**   
Auto tiering volume used space type   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Auto tiering volume used capacity by tiered types: cold or hot._   
`type`: Type of tiered data, cold or hot.   
`volume/average_latency` GA ** _(project)_**   
Volume I/O operation latency   
`GAUGE`, `DOUBLE`, `ms`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Volume I/O operation latency within the storage system._   
`method`: Type of latency, read, write or metadata.   
`volume/backup_current_transfer_bytes` GA ** _(project)_**   
Volume Backup Transfer Progress   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Amount of data transferred thus far for the current job._  
`volume/backup_healthy` GA ** _(project)_**   
Volume Backup Transfer Healthy   
`GAUGE`, `BOOL`, ``   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _FALSE if a backup transfer is missed or failed or has experienced a manual backup failure._  
`volume/backup_last_transfer_duration` GA ** _(project)_**   
Volume Backup Last Transfer Duration   
`GAUGE`, `INT64`, `s`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Duration of the last transfer job._  
`volume/backup_last_transfer_size` GA ** _(project)_**   
Volume Backup Last Transfer Size   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Size of the last transfer job._  
`volume/backup_transferring` GA ** _(project)_**   
Volume Backup Status   
`GAUGE`, `BOOL`, ``   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Status of backup: TRUE = transferring, FALSE = idle._  
`volume/backup_used` GA ** _(project)_**   
Bytes backed up   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Bytes backed up (baseline and incremental changes)._  
`volume/bytes_used` GA ** _(project)_**   
Volume space used   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Capacity used to store data written as files and additional space used for snapshots._  
`volume/files_restored_bytes` GA ** _(project)_**   
Files restored bytes   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Total size of the files restored successfully._  
`volume/files_restored_count` GA ** _(project)_**   
Files restored count   
`GAUGE`, `INT64`, `1`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Total count of the files restored successfully._  
`volume/inode_limit` GA ** _(project)_**   
Volume inode allocation   
`GAUGE`, `INT64`, `1`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Inodes allocated for the volume (hard cap). Tied to allocated capacity (size) of volume._  
`volume/inode_used` GA ** _(project)_**   
Volume inode usage   
`GAUGE`, `INT64`, `1`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Number of inodes in use on the volume._  
`volume/operation_count` GA ** _(project)_**   
Operations count   
`DELTA`, `INT64`, `1`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Number of operations being performed on the volume by the clients._   
`type`: Type of operation, read, write, or metadata.   
`volume/snapshot_bytes` GA ** _(project)_**   
Volume snapshot space used   
`GAUGE`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Capacity used for snapshot copies._  
`volume/throughput` GA ** _(project)_**   
Throughput   
`DELTA`, `INT64`, `By`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Throughput for the operation type._   
`type`: Type of operation, read, write, or metadata.   
`volume/throughput_limit` GA ** _(project)_**   
Maximum throughput   
`GAUGE`, `INT64`, `KiBy/s`   
**[netapp.googleapis.com/Volume](https://docs.cloud.google.com/monitoring/api/resources#tag_netapp.googleapis.com/Volume)** |  _Maximum throughput allocated for the volume._  
  
### networkactions

Metrics from [Service Extensions](https://docs.cloud.google.com/service-extensions/docs). Launch stages of these metrics: BETA EARLY_ACCESS

The "metric type" strings in this table must be prefixed with `networkactions.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`extension/failed_open_count` BETA ** _(project)_**   
Service Extension failed invocations with fail-open   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The total number of times a service extension invocation failed when the system was configured to "fail open". In these instances, the original client request was allowed to proceed, ignoring the failure._   
`ignored_status`: The gRPC status of the invocation that was ignored, for example, "DEADLINE_EXCEEDED", "CANCELLED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/invocation_count` BETA ** _(project)_**   
Service Extension invocation count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The number of invocations handled by the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/invocation_latencies` BETA ** _(project)_**   
Service Extension invocation latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _Distribution calculated from the latency of each invocation._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED", or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/mutation_rejections_count` BETA ** _(project)_**   
Service Extension mutation rejections count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The number of extension invocations that requested headers/body/trailer mutations but were rejected. Rejections can occur for a variety of reasons, the mutation being invalid, exceeding size limits, or an internal failure._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/received_bytes_count` BETA ** _(project)_**   
Service Extension received bytes count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The number of bytes received by the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/received_chunks_count` BETA ** _(project)_**   
Service Extension received chunks count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The number of data chunks received by the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/sent_bytes_count` BETA ** _(project)_**   
Service Extension sent bytes count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The number of bytes sent by the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`extension/sent_chunks_count` BETA ** _(project)_**   
Service Extension sent chunks count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/Extension)** |  _The number of data chunks sent by the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". At this time, this label is not supported for Media CDN.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Extension type is always "plugin" for MediaCDN.   
`extension_service`: The name of the plugin the extension points to.   
`wasm_plugin/cpu/usage_times` EARLY_ACCESS ** _(project)_**   
Wasm plugin normalized CPU usage   
`DELTA`, `DISTRIBUTION`, `us{CPU}`   
**[networkactions.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/WasmPluginVersion)** |  _CPU usage time of Wasm plugin invocations, in microseconds normalized across machine platforms._   
`status`: The status of the invocation, for example, "SUCCESS" or "CPU_LIMIT_EXCEEDED".   
`operation`: The operation type of the invocation, for example, "CONFIGURE_PLUGIN" or "HTTP_REQUEST_HEADERS".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the plugin is attached, that triggered the plugin invocation.   
`wasm_plugin/invocation_count` EARLY_ACCESS ** _(project)_**   
Wasm plugin invocation count   
`DELTA`, `INT64`, `1`   
**[networkactions.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/WasmPluginVersion)** |  _Number of invocations handled by the Wasm plugin._   
`status`: The status of the invocation, for example, "SUCCESS" or "CPU_LIMIT_EXCEEDED".   
`operation`: The operation type of the invocation, for example, "CONFIGURE_PLUGIN" or "HTTP_REQUEST_HEADERS".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the plugin is attached, that triggered the plugin invocation.   
`wasm_plugin/invocation_latencies` EARLY_ACCESS ** _(project)_**   
Wasm plugin invocation latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[networkactions.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/WasmPluginVersion)** |  _Wall time latency of Wasm plugin invocations, in microseconds._   
`status`: The status of the invocation, for example, "SUCCESS" or "CPU_LIMIT_EXCEEDED".   
`operation`: The operation type of the invocation, for example, "CONFIGURE_PLUGIN" or "HTTP_REQUEST_HEADERS".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the plugin is attached, that triggered the plugin invocation.   
`wasm_plugin/memory/bytes_used` EARLY_ACCESS ** _(project)_**   
Wasm plugin memory usage   
`GAUGE`, `DISTRIBUTION`, `By`   
**[networkactions.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkactions.googleapis.com/WasmPluginVersion)** |  _Total memory allocated by Wasm plugin VMs, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
### networkconnectivity

Metrics from [Network Connectivity](https://docs.cloud.google.com/network-connectivity/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `networkconnectivity.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`gateway/edge_dynamic_route_prefixes_per_group_per_route_region` BETA ** _(project)_**   
Unique gateway edge dynamic route prefixes per spoke group per region   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Group](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Group)** |  _The number of unique gateway edge dynamic routes in a region per gateway spoke group. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`route_region`: The region that contains unique dynamic route prefixes.   
`quota/active_vpc_spokes_per_hub/exceeded` GA ** _(project)_**   
Active VPC Spokes per Hub quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Number of attempts to exceed the limit on quota metric networkconnectivity.googleapis.com/active_vpc_spokes_per_hub. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/active_vpc_spokes_per_hub/limit` GA ** _(project)_**   
Active VPC Spokes per Hub quota limit   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Current limit on quota metric networkconnectivity.googleapis.com/active_vpc_spokes_per_hub. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/active_vpc_spokes_per_hub/usage` GA ** _(project)_**   
Active VPC Spokes per Hub quota usage   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Current usage on quota metric networkconnectivity.googleapis.com/active_vpc_spokes_per_hub. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/dynamic_route_prefixes_per_hub_route_table_per_route_region/exceeded` GA ** _(project)_**   
Unique dynamic route prefixes per hub route table per route region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/RouteTable](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/RouteTable)** |  _Number of attempts to exceed the limit on quota metric networkconnectivity.googleapis.com/dynamic_route_prefixes_per_hub_route_table_per_route_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`route_region`: The region that contains unique dynamic route prefixes.   
`quota/dynamic_route_prefixes_per_hub_route_table_per_route_region/limit` GA ** _(project)_**   
Unique dynamic route prefixes per hub route table per route region quota limit   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/RouteTable](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/RouteTable)** |  _Current limit on quota metric networkconnectivity.googleapis.com/dynamic_route_prefixes_per_hub_route_table_per_route_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`route_region`: The region that contains unique dynamic route prefixes.   
`quota/dynamic_route_prefixes_per_hub_route_table_per_route_region/usage` GA ** _(project)_**   
Unique dynamic route prefixes per hub route table per route region quota usage   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/RouteTable](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/RouteTable)** |  _Current usage on quota metric networkconnectivity.googleapis.com/dynamic_route_prefixes_per_hub_route_table_per_route_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`route_region`: The region that contains unique dynamic route prefixes.   
`quota/routes_per_route_table/exceeded` GA ** _(project)_**   
Subnet Routes per Route Table quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/RouteTable](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/RouteTable)** |  _Number of attempts to exceed the limit on quota metric networkconnectivity.googleapis.com/routes_per_route_table. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/routes_per_route_table/limit` GA ** _(project)_**   
Subnet Routes per Route Table quota limit   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/RouteTable](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/RouteTable)** |  _Current limit on quota metric networkconnectivity.googleapis.com/routes_per_route_table. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/routes_per_route_table/usage` GA ** _(project)_**   
Subnet Routes per Route Table quota usage   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/RouteTable](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/RouteTable)** |  _Current usage on quota metric networkconnectivity.googleapis.com/routes_per_route_table. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/routing_vpcs_per_hub/exceeded` ALPHA ** _(project)_**   
Routing VPCs per Hub quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Number of attempts to exceed the limit on quota metric networkconnectivity.googleapis.com/routing_vpcs_per_hub. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/routing_vpcs_per_hub/limit` ALPHA ** _(project)_**   
Routing VPCs per Hub quota limit   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Current limit on quota metric networkconnectivity.googleapis.com/routing_vpcs_per_hub. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/routing_vpcs_per_hub/usage` ALPHA ** _(project)_**   
Routing VPCs per Hub quota usage   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Current usage on quota metric networkconnectivity.googleapis.com/routing_vpcs_per_hub. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_hub/exceeded` GA ** _(project)_**   
Static Routes per Hub quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Number of attempts to exceed the limit on quota metric networkconnectivity.googleapis.com/static_routes_per_hub. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_hub/limit` GA ** _(project)_**   
Static Routes per Hub quota limit   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Current limit on quota metric networkconnectivity.googleapis.com/static_routes_per_hub. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_hub/usage` GA ** _(project)_**   
Static Routes per Hub quota usage   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Hub](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Hub)** |  _Current usage on quota metric networkconnectivity.googleapis.com/static_routes_per_hub. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`spoke/gateway/forwarding_routes_max` BETA ** _(project)_**   
Maximum number of routes   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _The maximum number of routes present in a forwarding element of the NCC-GW currently. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`spoke_group`: The spoke group the routes are for.   
`zone`: The zone the forwarding element is in.   
`spoke/gateway/forwarding_routes_min` BETA ** _(project)_**   
Minimum number of routes   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _The minimum number of routes present in a forwarding element of the NCC-GW currently. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`spoke_group`: The spoke group the routes are for.   
`zone`: The zone the forwarding element is in.   
`spoke/gateway/gcp_status` BETA ** _(project)_**   
GCP health of the NCC Gateway.   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _Indicates whether the GCP health of the NCC Gateway is healthy or not. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`state`: State of the NCC Gateway GCP health, such as healthy or unhealthy.   
`spoke/gateway/received_bytes_count` BETA ** _(project)_**   
NCC Gateway spoke received bytes   
`DELTA`, `INT64`, `By`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _Count of bytes received by the NCC Gateway spoke._   
`previous_hop_type`: The type of hop sending the traffic to the spoke, one of [hub, edge, gateway, sac_attachment].   
`spoke_group`: The spoke group sending traffic to this spoke.   
`previous_hop_name`: The name of the previous hop, if applicable.   
`zone`: The zone in which the gateway received and processed packets.   
`spoke/gateway/received_packets_count` BETA ** _(project)_**   
NCC Gateway spoke received packets   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _Count of packets received by the NCC Gateway spoke._   
`previous_hop_type`: The type of hop sending the traffic to the spoke, one of [hub, edge, gateway, sac_attachment].   
`spoke_group`: The spoke group sending traffic to this spoke.   
`previous_hop_name`: The name of the previous hop, if applicable.   
`zone`: The zone in which the gateway received and processed packets.   
`spoke/gateway/sent_bytes_count` BETA ** _(project)_**   
NCC Gateway spoke sent bytes   
`DELTA`, `INT64`, `By`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _Count of bytes sent by the NCC Gateway spoke._   
`next_hop_type`: The type of hop which the gateway is sending the traffic to, one of [hub, edge, gateway, sac_attachment].   
`spoke_group`: The spoke group which the gateway is sending the traffic to, if known.   
`next_hop_name`: The name of the next hop, if applicable.   
`zone`: The zone in which the gateway processed and sent packets.   
`spoke/gateway/sent_packets_count` BETA ** _(project)_**   
NCC Gateway spoke sent packets   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _Count of packets sent by the NCC Gateway spoke._   
`next_hop_type`: The type of hop which the gateway is sending the traffic to, one of [hub, edge, gateway, sac_attachment].   
`spoke_group`: The spoke group which the gateway is sending the traffic to, if known.   
`next_hop_name`: The name of the next hop, if applicable.   
`zone`: The zone in which the gateway processed and sent packets.   
`spoke/gateway/status` BETA ** _(project)_**   
Health of the NCC Gateway.   
`GAUGE`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Spoke](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Spoke)** |  _Indicates whether the NCC Gateway is healthy or not. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`state`: State of the NCC Gateway, such as healthy or unhealthy.   
`transport/dropped_received_packets_count` BETA ** _(project)_**   
Transport dropped received packets   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Transport](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Transport)** |  _Count of incoming packets dropped by the transport over a period of time. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`ip_version`: The IP version of the packets dropped, one of [IPv4, IPv6].   
`reason`: The reason for the packet drop.   
`transport/dropped_sent_packets_count` BETA ** _(project)_**   
Transport dropped sent packets   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Transport](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Transport)** |  _Count of outgoing packets dropped by the transport over a period of time. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`ip_version`: The IP version of the packets dropped, one of [IPv4, IPv6].   
`reason`: The reason for the packet drop.   
`transport/received_bytes_count` BETA ** _(project)_**   
Transport received bytes   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Transport](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Transport)** |  _Count of bytes received by the transport over a period of time. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`ip_version`: The IP version of the bytes received, one of [IPv4, IPv6].   
`transport/received_packets_count` BETA ** _(project)_**   
Transport received packets   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Transport](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Transport)** |  _Count of packets received by the transport over a period of time. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`ip_version`: The IP version of the packets received, one of [IPv4, IPv6].   
`transport/sent_bytes_count` BETA ** _(project)_**   
Transport sent bytes   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Transport](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Transport)** |  _Count of bytes transmitted by the transport over a period of time. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`ip_version`: The IP version of the bytes transmitted, one of [IPv4, IPv6].   
`transport/sent_packets_count` BETA ** _(project)_**   
Transport sent packets   
`DELTA`, `INT64`, `1`   
**[networkconnectivity.googleapis.com/Transport](https://docs.cloud.google.com/monitoring/api/resources#tag_networkconnectivity.googleapis.com/Transport)** |  _Count of packets transmitted by the transport over a period of time. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`ip_version`: The IP version of the packets transmitted, one of [IPv4, IPv6].   
  
### networking

Metrics from [Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology). Launch stages of these metrics: ALPHA GA

The "metric type" strings in this table must be prefixed with `networking.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`all_gcp/vm_traffic/zone_pair_median_rtt` GA ** _(project, folder, organization)_**   
VM to VM median RTT per zone pair, for all GCP projects   
`GAUGE`, `DOUBLE`, `ns`   
**[networking.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networking.googleapis.com/Location)** |  _The median RTT (round-trip time) for VM to VM traffic, per zone pair and aggregated across all GCP projects. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`remote_region`: Region of the remote endpoints for which the RTT was measured.   
`remote_zone`: Zone of the remote endpoints for which the RTT was measured.   
`protocol`: Protocol of the connections for which the RTT was measured. The only valid value is TCP.   
`cloud_netslo/active_probing/probe_count` GA ** _(project)_**   
Number of probes   
`DELTA`, `INT64`, `1`   
**[gce_zone_network_health](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_zone_network_health)** |  _Number of probing probes. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`remote_zone`: Zone of the remote instance.   
`remote_region`: Region of the remote instance.   
`remote_location_type`: Type of destination.   
`protocol`: Protocol used for probing.   
`result`: Result of probing (success/failure).   
`fixed_standard_tier/limit` DEPRECATED ** _(project)_**   
Fixed standard network tier limit   
`GAUGE`, `INT64`, `By`   
**[networking.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networking.googleapis.com/Location)** |  _The limit for fixed standard network tier in number of egress bytes per second. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`bandwidth_policy_id`: The identifier for fixed standard tier policy or 'UNKNOWN'.   
`fixed_standard_tier/usage` DEPRECATED ** _(project)_**   
Fixed standard network tier usage   
`GAUGE`, `INT64`, `By`   
**[networking.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networking.googleapis.com/Location)** |  _The current rate of egress bytes per second sent over Fixed Standard Tier. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`bandwidth_policy_id`: The identifier for fixed standard tier policy or 'UNKNOWN'.   
`traffic_source`: Traffic source for the fixed standard network tier, one of [L7LB, VM].   
`google_service/request_bytes_count` GA ** _(project)_**   
Request bytes count   
`DELTA`, `INT64`, `By`   
**[google_service_gce_client](https://docs.cloud.google.com/monitoring/api/resources#tag_google_service_gce_client)** |  _The number of bytes sent in requests from the clients to the Google Service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`protocol`: Protocol of the connection, one of [HTTP/1.1, HTTP/2.0].   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none. For gRPC error mapping to response code class see <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`service_name`: The Google Service name, such as "storage.googleapis.com".   
`service_region`: The region of the client, such as "us-central1", "asia-south1", "europe-west6".   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`google_service/response_bytes_count` GA ** _(project)_**   
Response bytes count   
`DELTA`, `INT64`, `By`   
**[google_service_gce_client](https://docs.cloud.google.com/monitoring/api/resources#tag_google_service_gce_client)** |  _The number of bytes sent in responses to the clients from the Google Service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`protocol`: Protocol of the connection, one of [HTTP/1.1, HTTP/2.0].   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none. For gRPC error mapping to response code class see <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`service_name`: The Google Service name, such as "storage.googleapis.com".   
`service_region`: The region of the client, such as "us-central1", "asia-south1", "europe-west6".   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`interconnect_attachment/egress_bytes_count` GA ** _(project)_**   
Egress bytes from the Cloud Interconnect attachment   
`DELTA`, `INT64`, `By`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _The number of bytes sent from GCP via the Cloud Interconnect attachment. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_project_number`: The project number of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_project_id`: The project ID of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_region`: Region of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_zone`: Zone of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_location_type`: Type of destination, one of ["CLOUD" - when the local end is inside a VPC; "EXTERNAL" - otherwise]. If the GCP endpoint belongs to a different project, the field is set to "CLOUD" only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to EXTERNAL.   
`local_resource_type`: Resource type of local end, one of ["GCE_VM" - for a VM instance; "ICA" - for a Cloud Interconnect attachment; "VPN" - for a Cloud VPN tunnel; "ROUTER_APPLIANCE" - for a router appliance instance; "OTHER" - otherwise]. If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the local_location_type is CLOUD, 2) the projects are in the same organization, 3) the communication was via Shared VPC or VPC Peering, 4) cross project metrics were not disabled. Otherwise the field is set to OTHER.   
`local_network`: Network of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_subnetwork`: Subnetwork of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`interconnect_attachment/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes to the Cloud Interconnect attachment   
`DELTA`, `INT64`, `By`   
**[interconnect_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)** |  _The number of bytes sent to GCP via the Cloud Interconnect attachment. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_project_number`: The project number of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_project_id`: The project ID of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_region`: Region of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_zone`: Zone of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_location_type`: Type of destination, one of ["CLOUD" - when the local end is inside a VPC; "EXTERNAL" - otherwise]. If the GCP endpoint belongs to a different project, the field is set to "CLOUD" only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to EXTERNAL.   
`local_resource_type`: Resource type of local end, one of ["GCE_VM" - for a VM instance; "ICA" - for a Cloud Interconnect attachment; "VPN" - for a Cloud VPN tunnel; "ROUTER_APPLIANCE" - for a router appliance instance; "OTHER" - otherwise]. If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the local_location_type is CLOUD, 2) the projects are in the same organization, 3) the communication was via Shared VPC or VPC Peering, 4) cross project metrics were not disabled. Otherwise the field is set to OTHER.   
`local_network`: Network of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_subnetwork`: Subnetwork of the GCP endpoint that communicated via the attachment. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`interconnect_attachment/vm/egress_bytes_count` GA ** _(project)_**   
Egress bytes per VM to the Cloud Interconnect attachment   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent from the local VM to its remote peers via the tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`attachment_project_number`: The project number of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`attachment_project_id`: The project ID of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`attachment_name`: The name of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`attachment_region`: Region of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`interconnect_name`: The name of the Cloud Interconnect. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`interconnect_project_id`: The project identifier of the Cloud Interconnect. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`interconnect_attachment/vm/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes per VM from the Cloud Interconnect attachment   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent to the local VM from its remote peers via the Cloud Interconnect attachment. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`attachment_project_number`: The project number of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`attachment_project_id`: The project ID of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`attachment_name`: The name of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`attachment_region`: Region of the Cloud Interconnect attachment. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`interconnect_name`: The name of the Cloud Interconnect. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`interconnect_project_id`: The project identifier of the Cloud Interconnect. If the attachment belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to ATTACHMENT_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`node_flow/egress_bytes_count` GA ** _(project)_**   
Egress bytes count per GKE node   
`DELTA`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Number of bytes sent from the GKE node to its remote peers, including from Pods inside the node. The bytes count doesn't include packet header size. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE node.   
`local_subnetwork`: Subnetwork of the local GKE node.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`node_flow/egress_packets_count` GA ** _(project)_**   
Egress packets count per GKE node   
`DELTA`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Number of packets sent from the GKE node to its remote peers, including from Pods inside the node. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE node.   
`local_subnetwork`: Subnetwork of the local GKE node.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`node_flow/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes count per GKE node   
`DELTA`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Number of bytes sent to the GKE node from its remote peers, including to Pods inside the Node. The bytes count doesn't include packet header size. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE node.   
`local_subnetwork`: Subnetwork of the local GKE node.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`node_flow/ingress_packets_count` GA ** _(project)_**   
Ingress packets count per GKE node   
`DELTA`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Number of packets sent to the GKE node from its remote peers, including to Pods inside the node. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE node.   
`local_subnetwork`: Subnetwork of the local GKE node.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL".   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`node_flow/rtt` GA ** _(project)_**   
RTT latencies per GKE node   
`DELTA`, `DISTRIBUTION`, `ms`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _A distribution of RTT measured over TCP connections from the GKE node to Cloud endpoints, including from Pods inside the node. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE node.   
`local_subnetwork`: Subnetwork of the local GKE node.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Always TCP.   
`pod_flow/egress_bytes_count` GA ** _(project)_**   
Egress bytes count per GKE Pod   
`DELTA`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Number of bytes sent from the GKE Pod to its remote peers. The bytes count doesn't include packet header size. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE Pod.   
`local_subnetwork`: Subnetwork of the local GKE Pod.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster_location`: GKE cluster location of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_namespace`: GKE namespace of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_workload`: GKE workload name of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD", or if the remote endpoint belongs to a different project and one of the following does not hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. If the value is not known or the remote endpoint is not a GKE workload, the field is set to "NOT_APPLICABLE".   
`remote_workload_type`: GKE workload type of the remote endpoint, one of: [REPLICA_SET, DEPLOYMENT, STATEFUL_SET, DAEMON_SET, JOB, CRON_JOB, REPLICATION_CONTROLLER, UNKNOWN]. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`pod_flow/egress_packets_count` GA ** _(project)_**   
Egress packets count per GKE Pod   
`DELTA`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Number of packets sent from the GKE Pod to its remote peers. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE Pod.   
`local_subnetwork`: Subnetwork of the local GKE Pod.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster_location`: GKE cluster location of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_namespace`: GKE namespace of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_workload`: GKE workload name of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD", or if the remote endpoint belongs to a different project and one of the following does not hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. If the value is not known, the field is set to "NOT_APPLICABLE".   
`remote_workload_type`: GKE workload type of the remote endpoint, one of: [REPLICA_SET, DEPLOYMENT, STATEFUL_SET, DAEMON_SET, JOB, CRON_JOB, REPLICATION_CONTROLLER, UNKNOWN]. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`pod_flow/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes count per GKE Pod   
`DELTA`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Number of bytes sent to the GKE Pod from its remote peers. The bytes count doesn't include packet header size. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE Pod.   
`local_subnetwork`: Subnetwork of the local GKE Pod.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster_location`: GKE cluster location of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_namespace`: GKE namespace of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_workload`: GKE workload name of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD", or if the remote endpoint belongs to a different project and one of the following does not hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. If the value is not known or the remote endpoint is not a GKE workload, the field is set to "NOT_APPLICABLE".   
`remote_workload_type`: GKE workload type of the remote endpoint, one of: [REPLICA_SET, DEPLOYMENT, STATEFUL_SET, DAEMON_SET, JOB, CRON_JOB, REPLICATION_CONTROLLER, UNKNOWN]. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`pod_flow/ingress_packets_count` GA ** _(project)_**   
Ingress packets count per GKE Pod   
`DELTA`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Number of packets sent to the GKE Pod from its remote peers. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE Pod.   
`local_subnetwork`: Subnetwork of the local GKE Pod.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster_location`: GKE cluster location of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_namespace`: GKE namespace of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_workload`: GKE workload name of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD", or if the remote endpoint belongs to a different project and one of the following does not hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. If the value is not known or the remote endpoint is not a GKE workload, the field is set to "NOT_APPLICABLE".   
`remote_workload_type`: GKE workload type of the remote endpoint, one of: [REPLICA_SET, DEPLOYMENT, STATEFUL_SET, DAEMON_SET, JOB, CRON_JOB, REPLICATION_CONTROLLER, UNKNOWN]. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the remote_location_type is not "EXTERNAL". By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]. Set to "UNKNOWN" if the remote_location_type is not "EXTERNAL" or the network tier was not identified. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`pod_flow/rtt` GA ** _(project)_**   
RTT latencies per GKE Pod   
`DELTA`, `DISTRIBUTION`, `ms`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _A distribution of RTT measured over TCP connections from the GKE Pod to Cloud endpoints. By default, traffic between the Pod and an endpoint outside the VPC is attributed to the Node and not the Pod, due to IP masquerading before our sampling point. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local GKE Pod.   
`local_subnetwork`: Subnetwork of the local GKE Pod.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster`: GKE cluster of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_cluster_location`: GKE cluster location of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_namespace`: GKE namespace of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_workload`: GKE workload name of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD", or if the remote endpoint belongs to a different project and one of the following does not hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. If the value is not known or the remote endpoint is not a GKE workload, the field is set to "NOT_APPLICABLE".   
`remote_workload_type`: GKE workload type of the remote endpoint, one of: [REPLICA_SET, DEPLOYMENT, STATEFUL_SET, DAEMON_SET, JOB, CRON_JOB, REPLICATION_CONTROLLER, UNKNOWN]. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if the communication was via Shared VPC or VPC Peering. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Always TCP.   
`region/external_rtt` GA ** _(project)_**   
External RTT latencies per GCP region   
`DELTA`, `DISTRIBUTION`, `ms`   
**[networking.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networking.googleapis.com/Location)** |  _A distribution of RTT measured over TCP connections from a GCP region to Internet destinations. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the remote continent is unknown.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown.   
`remote_region`: The region of the remote endpoint. Set to "NOT_APPLICABLE" if the region is unknown.   
`remote_city`: The city of the remote endpoint. Set to "NOT_APPLICABLE" if the city is unknown.   
`remote_location_type`: Always EXTERNAL.   
`protocol`: Always TCP.   
`router_appliance/gateway/egress_bytes_count` GA ** _(project)_**   
Egress bytes from router appliance instance   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of bytes sent to GCP via the router appliance instance from on-premises hosts. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`router_appliance_network`: Network name of the router appliance instance NIC.   
`router_appliance_subnetwork`: Subnetwork name of the router appliance instance NIC.   
`local_project_id`: The project identifier of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_project_number`: The project number of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_region`: Region of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_zone`: Zone of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_location_type`: Type of destination, one of ["CLOUD" - when the local end is inside a VPC; "EXTERNAL" - otherwise]. If the GCP endpoint belongs to a different project, the field is set to "CLOUD" only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to EXTERNAL.   
`local_resource_type`: Resource type of local end, one of ["GCE_VM" - for a VM instance; "ICA" - for a Cloud Interconnect attachment; "VPN" - for a Cloud VPN tunnel; "ROUTER_APPLIANCE" - for a router appliance instance; "OTHER" - otherwise]. If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the local_location_type is CLOUD, 2) the projects are in the same organization, 3) the communication was via Shared VPC or VPC Peering, 4) cross project metrics were not disabled. Otherwise the field is set to OTHER.   
`local_network`: Network of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_subnetwork`: Subnetwork of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`router_appliance/gateway/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes to the router appliance instance   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of bytes sent from GCP via the router appliance instance to on-premises hosts. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`router_appliance_network`: Network name of the router appliance instance NIC.   
`router_appliance_subnetwork`: Subnetwork name of the router appliance instance NIC.   
`local_project_id`: The project identifier of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_project_number`: The project number of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_region`: Region of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_zone`: Zone of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_location_type`: Type of destination, one of ["CLOUD" - when the local end is inside a VPC; "EXTERNAL" - otherwise]. If the GCP endpoint belongs to a different project, the field is set to "CLOUD" only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to EXTERNAL.   
`local_resource_type`: Resource type of local end, one of ["GCE_VM" - for a VM instance; "ICA" - for a Cloud Interconnect attachment; "VPN" - for a Cloud VPN tunnel; "ROUTER_APPLIANCE" - for a router appliance instance; "OTHER" - otherwise]. If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the local_location_type is CLOUD, 2) the projects are in the same organization, 3) the communication was via Shared VPC or VPC Peering, 4) cross project metrics were not disabled. Otherwise the field is set to OTHER.   
`local_network`: Network of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_subnetwork`: Subnetwork of the GCP endpoint that communicated via the router appliance instance. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`router_appliance/vm/egress_bytes_count` GA ** _(project)_**   
Egress bytes per VM to router appliance instance   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent from the local VM to its remote peers via the router appliance instance. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`router_appliance_instance_name`: The instance name of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_instance_id`: The instance id of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_project_number`: The project number of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_project_id`: The project ID of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_zone`: Zone of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_region`: Region of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`router_appliance/vm/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes per VM from the router appliance instance   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent to the local VM from its remote peers via the router appliance instance. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`router_appliance_instance_name`: The instance name of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_instance_id`: The instance id of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_project_number`: The project number of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_project_id`: The project ID of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_zone`: Zone of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`router_appliance_region`: Region of the router appliance instance. If the router appliance instance belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to RA_PROJECT_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`vm_flow/connection_count` ALPHA ** _(project)_**   
Connection Count   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of connections measured between the local VM and its remote peers. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown or the remote_location_type is not "EXTERNAL".   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the business region is unknown or the remote_location_type is not "EXTERNAL".   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`network_topology_remote_label`: Always UNSUPPORTED.   
`remote_vpn_tunnel`: Always UNSUPPORTED.   
`vm_flow/egress_bytes_count` GA ** _(project)_**   
Egress bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent from the local VM to its remote peers. This metric does not include the header size. So this value is lower than the compute.googleapis.com/instance/network/sent_bytes_count value. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown or the remote_location_type is not "EXTERNAL".   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the business region is unknown or the remote_location_type is not "EXTERNAL".   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`network_topology_remote_label`: Always UNSUPPORTED.   
`remote_vpn_tunnel`: Always UNSUPPORTED.   
`vm_flow/egress_packets_count` ALPHA ** _(project)_**   
Egress Packets Per VM   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of packets sent from the local VM to its remote peers. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown or the remote_location_type is not "EXTERNAL".   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the business region is unknown or the remote_location_type is not "EXTERNAL".   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote instance. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`network_topology_remote_label`: Always UNSUPPORTED.   
`remote_vpn_tunnel`: Always UNSUPPORTED.   
`vm_flow/external_rtt` GA ** _(project)_**   
External RTT latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _A distribution of RTT measured over TCP connections from the local VM to Internet destinations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`network_tier`: Network tier of the connection, one of [PREMIUM, STANDARD, FIXED_STANDARD, UNKNOWN]   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the remote continent is unknown.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown.   
`remote_region`: The region of the remote endpoint. Set to "NOT_APPLICABLE" if the region is unknown.   
`remote_city`: The city of the remote endpoint. Set to "NOT_APPLICABLE" if the city is unknown.   
`remote_location_type`: Always EXTERNAL.   
`protocol`: Always TCP.   
`vm_flow/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent to the local VM from its remote peers. This metric does not include the header size. So this value is lower than the compute.googleapis.com/instance/network/received_bytes_count value. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown or the remote_location_type is not "EXTERNAL".   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the business region is unknown or the remote_location_type is not "EXTERNAL".   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`network_topology_remote_label`: Always UNSUPPORTED.   
`remote_vpn_tunnel`: Always UNSUPPORTED.   
`vm_flow/ingress_packets_count` ALPHA ** _(project)_**   
Ingress Packets Per VM   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of packets sent to the local VM from its remote peers. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`remote_country`: The country of the remote endpoint. Set to "NOT_APPLICABLE" if the country is unknown or the remote_location_type is not "EXTERNAL".   
`remote_continent`: The business region of the remote endpoint, one of [America, Asia, Europe, NOT_APPLICABLE]. Set to "NOT_APPLICABLE" if the business region is unknown or the remote_location_type is not "EXTERNAL".   
`remote_project_id`: Project ID of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote instance. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote region is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". Set to "global" if the remote zone is unknown. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_location_type`: Type of the remote endpoint, one of: ["CLOUD" - when the endpoint is inside a VPC; "EXTERNAL" - when the endpoint is an Internet endpoint including public IP of a VM or network load balancer; "GOOGLE_INTERNAL" - when the endpoint is Google infrastructure such as a health check or GFE; "ON_PREM" - when the communication is through a Cloud VPN tunnel, Cloud Interconnect Attachment or router appliance instance].   
`remote_network`: Network of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. Set to "REMOTE_IS_EXTERNAL" if the remote_location_type is not "CLOUD". If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`network_topology_remote_label`: Always UNSUPPORTED.   
`remote_vpn_tunnel`: Always UNSUPPORTED.   
`vm_flow/rtt` GA ** _(project)_**   
RTT latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _A distribution of RTT measured over TCP connections from the local VM. Measured for intra Cloud traffic only. Based on sampled traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`remote_country`: Always NOT_APPLICABLE.   
`remote_continent`: Always NOT_APPLICABLE.   
`remote_project_id`: Project ID of the remote endpoint. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_region`: Region of the remote instance. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_zone`: Zone of the remote endpoint. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_location_type`: Always CLOUD.   
`remote_network`: Network of the remote endpoint. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`remote_subnetwork`: Subnetwork of the remote endpoint. If the remote endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to REMOTE_IS_EXTERNAL.   
`protocol`: Always TCP.   
`network_topology_remote_label`: Always UNSUPPORTED.   
`remote_vpn_tunnel`: Always UNSUPPORTED.   
`vpc_flow/predicted_max_vpc_flow_logs_count` GA ** _(project)_**   
Predicted Max VPC Flow Logs Count   
`DELTA`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _A predicted upper bound for the amount of VPC Flow Logs that would be exported for a specific subnet. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._  
`vpn_tunnel/egress_bytes_count` GA ** _(project)_**   
Egress bytes from the Cloud VPN tunnel   
`DELTA`, `INT64`, `By`   
**[vpn_tunnel](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_tunnel)** |  _The number of bytes sent from GCP via the Cloud VPN tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_project_number`: The project number of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_project_id`: The project ID of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_region`: Region of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_zone`: Zone of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_location_type`: Type of destination, one of ["CLOUD" - when the local end is inside a VPC; "EXTERNAL" - otherwise]. If the GCP endpoint belongs to a different project, the field is set to "CLOUD" only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to EXTERNAL.   
`local_resource_type`: Resource type of local end, one of ["GCE_VM" - for a VM instance; "ICA" - for a Cloud Interconnect attachment; "VPN" - for a Cloud VPN tunnel; "ROUTER_APPLIANCE" - for a router appliance instance; "OTHER" - otherwise]. If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the local_location_type is CLOUD, 2) the projects are in the same organization, 3) the communication was via Shared VPC or VPC Peering, 4) cross project metrics were not disabled. Otherwise the field is set to OTHER.   
`local_network`: Network of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_subnetwork`: Subnetwork of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`vpn_tunnel/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes to the Cloud VPN tunnel   
`DELTA`, `INT64`, `By`   
**[vpn_tunnel](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_tunnel)** |  _The number of bytes sent to GCP via the Cloud VPN tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_project_number`: The project number of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_project_id`: The project ID of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_AN_EXTERNAL_PROJECT" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_AN_EXTERNAL_PROJECT.   
`local_region`: Region of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_zone`: Zone of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_location_type`: Type of destination, one of ["CLOUD" - when the local end is inside a VPC; "EXTERNAL" - otherwise]. If the GCP endpoint belongs to a different project, the field is set to "CLOUD" only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to EXTERNAL.   
`local_resource_type`: Resource type of local end, one of ["GCE_VM" - for a VM instance; "ICA" - for a Cloud Interconnect attachment; "VPN" - for a Cloud VPN tunnel; "ROUTER_APPLIANCE" - for a router appliance instance; "OTHER" - otherwise]. If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the local_location_type is CLOUD, 2) the projects are in the same organization, 3) the communication was via Shared VPC or VPC Peering, 4) cross project metrics were not disabled. Otherwise the field is set to OTHER.   
`local_network`: Network of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`local_subnetwork`: Subnetwork of the GCP endpoint that communicated via the Cloud VPN tunnel. Set to "LOCAL_IS_EXTERNAL" if the local_location_type is not "CLOUD". If the GCP endpoint belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to LOCAL_IS_EXTERNAL.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`vpn_tunnel/vm/egress_bytes_count` GA ** _(project)_**   
Egress bytes per VM to the Cloud VPN tunnel   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent from the local VM to its remote peers via the Cloud VPN tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`vpn_project_number`: The project number of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_project_id`: The project ID of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_region`: Region of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_tunnel_id`: The tunnel identifier of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_tunnel_name`: The tunnel name of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
`vpn_tunnel/vm/ingress_bytes_count` GA ** _(project)_**   
Ingress bytes per VM from the Cloud VPN tunnel   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes sent to the local VM from its remote peers via the Cloud VPN tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`local_network`: Network of the local instance.   
`local_subnetwork`: Subnetwork of the local instance.   
`local_network_interface`: NIC of the local instance.   
`vpn_project_number`: The project number of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_project_id`: The project ID of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_region`: Region of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_tunnel_id`: The tunnel identifier of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`vpn_tunnel_name`: The tunnel name of the Cloud VPN tunnel. If the tunnel belongs to a different project, the field is set with the correct value only if all of the following hold: 1) the projects are in the same organization, 2) the communication was via Shared VPC or VPC Peering, 3) cross project metrics were not disabled. Otherwise the field is set to TUNNEL_BELONGS_TO_AN_EXTERNAL_PROJECT.   
`protocol`: Protocol of the connection, one of [TCP, UDP, GRE, ICMP, ICMPV6, ESP].   
  
### networkmanagement

Metrics from [Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `networkmanagement.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`insights/active_monitored_paths` BETA ** _(project)_**   
Active Monitored Paths   
`GAUGE`, `INT64`, `1/h`   
**[networkmanagement.googleapis.com/NetworkMonitoringProvider](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkMonitoringProvider)** |  _Number of active monitored paths._  
`insights/network/data/in/packets_received_count` BETA ** _(project)_**   
Inbound data packets received for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked data probes received inbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/data/in/packets_sent_count` BETA ** _(project)_**   
Inbound data packets sent for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked data probes sent inbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/data/out/packets_received_count` BETA ** _(project)_**   
Outbound data packets received for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked data probes received outbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/data/out/packets_sent_count` BETA ** _(project)_**   
Outbound data packets sent for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked data probes sent outbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/data/total/packets_received_count` BETA ** _(project)_**   
Total data packets received for Network Path (Single-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked data probes received in this measurement interval (Single-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/data/total/packets_sent_count` BETA ** _(project)_**   
Total data packets sent for Network Path (Single-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked data probes sent in this measurement interval (Single-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/in/jitter` BETA ** _(project)_**   
Inbound jitter for Network Path (Dual-Ended)   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Packet delay variation for inbound probes in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/in/loss_percent` BETA ** _(project)_**   
Inbound loss percent for Network Path (Dual-Ended)   
`GAUGE`, `DOUBLE`, `%`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Indicator of success or failure for inbound network probes. (Packets sent - packets received)/ packets sent * 100._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/out/jitter` BETA ** _(project)_**   
Outbound jitter for Network Path (Dual-Ended)   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Packet delay variation for outbound probes in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/out/loss_percent` BETA ** _(project)_**   
Outbound loss percent for Network Path (Dual-Ended)   
`GAUGE`, `DOUBLE`, `%`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Indicator of success or failure for outbound network probes. (Packets sent - packets received)/ packets sent * 100._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/rtt_avg` BETA ** _(project)_**   
Average RTT for Network Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Average round-trip time for all tracked data and voice probes in this measurement interval._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/rtt_max` BETA ** _(project)_**   
Maximum RTT for Network Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Maximum round-trip time for all tracked data and voice probes in this measurement interval._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/rtt_min` BETA ** _(project)_**   
Minimum RTT for Network Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Minimum round-trip time for all tracked data and voice probes in this measurement interval._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/test_error` BETA ** _(project)_**   
Test error for Network Path   
`GAUGE`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _0- Indicates that the network test succeeded (i.e there wasn’t 100% loss) and performance metrics are available. 1 - Indicates that the network test failed in which case not all performance metrics might be available._   
`error_type`: Type of the error.   
`error_detail`: Detail of the error.   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP". Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/total/jitter` BETA ** _(project)_**   
Total jitter for Network Path (Single-Ended)   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Packet delay variation for probes in this measurement interval (Single-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/total/loss_percent` BETA ** _(project)_**   
Loss percent for Network Path (Single-Ended)   
`GAUGE`, `DOUBLE`, `%`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Indicator of success or failure for network probes independent of which probes are enabled. (Packets sent - packets received)/ packets sent * 100._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP". Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/in/mos` BETA ** _(project)_**   
Inbound voice MOS for Network Path (Dual-Ended)   
`GAUGE`, `DOUBLE`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Mean Opinion Score (MOS) is an estimate of sound quality of a call. Measured on inbound voice probes sent in this measurement interval only (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/in/packets_received_count` BETA ** _(project)_**   
Inbound voice packets received for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked voice probes received inbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/in/packets_sent_count` BETA ** _(project)_**   
Inbound voice packets sent for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked voice probes sent inbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/out/mos` BETA ** _(project)_**   
Outbound voice MOS for Network Path (Dual-Ended)   
`GAUGE`, `DOUBLE`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Mean Opinion Score (MOS) is an estimate of sound quality of a call. Measured on outbound voice probes sent in this measurement interval only (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/out/packets_received_count` BETA ** _(project)_**   
Outbound voice packets received for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked voice probes received outbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/out/packets_sent_count` BETA ** _(project)_**   
Outbound voice packets sent for Network Path (Dual-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked voice probes sent outbound in this measurement interval (Dual-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/total/mos` BETA ** _(project)_**   
Total voice MOS for Network Path (Single-Ended)   
`GAUGE`, `DOUBLE`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Mean Opinion Score (MOS) is an estimate of sound quality of a call. Measured on voice probes sent in this measurement interval only (Single-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/total/packets_received_count` BETA ** _(project)_**   
Total voice packets received for Network Path (Single-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked voice probes received in this measurement interval (Single-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/network/voice/total/packets_sent_count` BETA ** _(project)_**   
Total voice packets sent for Network Path (Single-Ended)   
`DELTA`, `INT64`, `1`   
**[networkmanagement.googleapis.com/NetworkPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/NetworkPath)** |  _Count of tracked voice probes sent in this measurement interval (Single-Ended Path)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: The IP address or hostname of the network path destination.   
`network_protocol`: Network protocol. Can be either "ICMP", "UDP" or "TCP".   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`destination_monitoring_point_id`: Unique identifier of the destination Monitoring Point. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_monitoring_point_display_name`: Destination Monitoring Point display name.   
`destination_cloud_provider`: Destination Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_instance_id`: Destination instance ID. Relevant only for Monitoring Point->Monitoring Point path.   
`destination_cloud_zone`: Destination cloud zone.   
`destination_cloud_region`: Destination cloud region.   
`destination_cloud_project_id`: The cloud project ID of the destination Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id. Relevant only for Monitoring Point->Monitoring Point path.   
`insights/web/browser/test_error` BETA ** _(project)_**   
Browser test status for Web Path   
`GAUGE`, `INT64`, `1`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _This metric is only available for browser web path. A browser path error can occur when a Selenium script fails to complete dueto errors in the script itself or a timeout while waiting for a response. 0 : Test completed without errors. 1 : Errors prevented test completion (see error attributes)._   
`error_type`: Type of the error.   
`error_detail`: Detail of the error.   
`response_code`: HTTP response code.   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/download/size` BETA ** _(project)_**   
HTTP download size for Web Path   
`GAUGE`, `INT64`, `By`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The number of bytes downloaded during a response to the first non-redirected HTTP request._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/download/speed` BETA ** _(project)_**   
HTTP download speed for Web Path   
`GAUGE`, `DOUBLE`, `By/s`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _Total size of the downloaded content divided by the time taken to download for the first non-redirected request._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/dns_lookup` BETA ** _(project)_**   
DNS lookup HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The time to resolve the IP address of the destination domain for the first non-redirected request._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/redirect` BETA ** _(project)_**   
Redirect HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The time for a redirected request to arrive at the final server and for a response. Includes all aspects of a redirected request, including the time taken for DNS lookup, for a TCP/SSL connection to be established, the request itself, and the response time. 0: The initial request is not redirected._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/request_receive` BETA ** _(project)_**   
Request receive HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _Time taken to download the entire content of the first HTTP response._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/request_wait` BETA ** _(project)_**   
Request wait HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The time from when the first non-redirected HTTP request is sent until the first byte of the response is received._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/ssl_connect` BETA ** _(project)_**   
SSL connect HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The time to complete the SSL handshake for the first non-redirected request._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/tcp_connect` BETA ** _(project)_**   
TCP connect HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The time to establish the TCP connection for the first non-redirected request (SYN- >SYNACK)._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/response_time/total` BETA ** _(project)_**   
Total HTTP response time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _Total response time for the first request._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/retransmission/out` BETA ** _(project)_**   
Outbound HTTP retransmission rate for Web Path   
`GAUGE`, `DOUBLE`, `%`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The percentage of packets that the client had to resend to the server. It is captured directly from the TCP/IP stack during the web transaction._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/http/test_error` BETA ** _(project)_**   
HTTP test status for Web Path   
`GAUGE`, `INT64`, `1`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _0- Indicates that the HTTP web test succeeded (i.e the web path successfully completed all stages of the request and the actual result equals to the expected result) and performance metrics are available.1 - Indicates that the HTTP web test failed in which case not all performance metrics might be available._   
`error_type`: Type of the error.   
`error_detail`: Detail of the error.   
`response_code`: HTTP response code.   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
`insights/web/total_transaction_time` BETA ** _(project)_**   
Total transaction time for Web Path   
`GAUGE`, `DOUBLE`, `ms`   
**[networkmanagement.googleapis.com/WebPath](https://docs.cloud.google.com/monitoring/api/resources#tag_networkmanagement.googleapis.com/WebPath)** |  _The total time to execute the workflow._   
`source_cloud_provider`: Source Cloud Provider. Can be either "GCP", "AWS", or "AZURE" for example. Otherwise "UNDEFINED".   
`source_monitoring_point_id`: Unique identifier of the source Monitoring Point.   
`source_monitoring_point_display_name`: Source Monitoring Point display name.   
`source_cloud_instance_id`: Source instance ID.   
`source_cloud_zone`: Source cloud zone.   
`source_cloud_region`: Source cloud region.   
`source_cloud_project_id`: The cloud project ID of the source Monitoring Point. In AWS it is equivalent to account_id, in Azure to subscription_id.   
`destination`: Web monitoring destination URL.   
`monitoring_policy_id`: The ID of the monitoring policy that created this path.   
`monitoring_policy_display_name`: The name of the monitoring policy that created this path.   
  
### networksecurity

Metrics from [Google Cloud Armor](https://docs.cloud.google.com/armor/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `networksecurity.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`dnsthreatdetector/received_dns_threat_count` BETA ** _(project)_**   
DNS threat log count   
`CUMULATIVE`, `INT64`, `bytes`   
**[networksecurity.googleapis.com/DnsThreatDetector](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/DnsThreatDetector)** |  _Total number of threat logs generated by DNS threat detection service._   
`inspected_project_id`: The ID of GCP project associated with Protective DNS.   
`severity`: The severity of threat logs (info, low, medium, high, critical).   
`type`: The type of threat logs as a string.   
`dnsthreatdetector/sent_dns_log_count` BETA ** _(project)_**   
Inspected log count   
`CUMULATIVE`, `INT64`, `bytes`   
**[networksecurity.googleapis.com/DnsThreatDetector](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/DnsThreatDetector)** |  _Total number of DNS query logs inspected by the Protective DNS service._   
`inspected_project_id`: The ID of GCP project associated with Protective DNS.   
`dos/ingress_bytes_count` BETA ** _(project)_**   
Ingress bytes   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/ProtectedEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/ProtectedEndpoint)** |  _The total number of bytes received, broken down by drop status (allowed or dropped). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`drop_status`: Indicates whether the bytes were dropped or allowed by the network infrastructure.   
`dos/ingress_packets_count` BETA ** _(project)_**   
Ingress packets   
`DELTA`, `INT64`, `{packets}`   
**[networksecurity.googleapis.com/ProtectedEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/ProtectedEndpoint)** |  _The total number of packets received, broken down by drop status (allowed or dropped). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`drop_status`: Indicates whether the packets were dropped or allowed by the network infrastructure.   
`firewall_endpoint/antivirus_signature_version` BETA ** _(project)_**   
Antivirus signature version   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _The minimum Antivirus signature version in the firewall endpoint. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`version`: The minimum Antivirus signature version in the firewall endpoint.   
`firewall_endpoint/apps_and_threats_signature_version` BETA ** _(project)_**   
Apps and threats signature version   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _The minimum Apps and Threats signature version in the firewall endpoint. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`version`: The minimum Apps and Threats signature version in the firewall endpoint.   
`firewall_endpoint/health` BETA ** _(project)_**   
Firewall Endpoint Health   
`GAUGE`, `BOOL`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Indicates whether the Firewall Endpoint is healthy or not. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`firewall_endpoint/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Total Firewall Endpoint received bytes._   
`security_profile_group_name`: The name of the security profile group.   
`inspected_network_name`: The name of the Network that was inspected.   
`inspected_project_id`: The ID of the GCP project associated with the network.   
`firewall_endpoint/received_packets_count` GA ** _(project)_**   
Received packets   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Total Firewall Endpoint received packets._   
`security_profile_group_name`: The name of the security profile group.   
`inspected_network_name`: The name of the Network that was inspected.   
`inspected_project_id`: The ID of the GCP project associated with the network.   
`firewall_endpoint/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Total Firewall Endpoint sent bytes._   
`security_profile_group_name`: The name of the security profile group.   
`inspected_network_name`: The name of the Network that was inspected.   
`inspected_project_id`: The ID of the GCP project associated with the network.   
`firewall_endpoint/sent_packets_count` GA ** _(project)_**   
Sent packets   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Total Firewall Endpoint sent packets._   
`security_profile_group_name`: The name of the security profile group.   
`inspected_network_name`: The name of the Network that was inspected.   
`inspected_project_id`: The ID of the GCP project associated with the network.   
`firewall_endpoint/threats_count` GA ** _(project)_**   
Threats count   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Total Firewall Endpoint detected threats. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`security_profile_group_name`: The name of the security profile group.   
`inspected_network_name`: The name of the Network that was inspected.   
`inspected_project_id`: The ID of the GCP project associated with the network.   
`action`: The action that was taken, either the default action or the override action specified in the security profile.   
`firewall_endpoint/wildfire_health` BETA ** _(project)_**   
WildFire Health   
`GAUGE`, `BOOL`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _Indicates whether the WildFire integration is healthy or not. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`firewall_endpoint/wildfire_signature_version` BETA ** _(project)_**   
WildFire signature version   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/FirewallEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/FirewallEndpoint)** |  _The minimum WildFire signature version in the firewall endpoint. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`version`: The minimum WildFire signature version in the firewall endpoint.   
`https/previewed_request_count` GA ** _(project)_**   
Previewed request count   
`DELTA`, `INT64`, `1`   
**[network_security_policy](https://docs.cloud.google.com/monitoring/api/resources#tag_network_security_policy)** |  _Queries that would be affected by rules currently in the 'preview' mode, if those rules were to be made non-preview. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`blocked`: (BOOL) Policy application result.   
`backend_target_name`: HTTP(S) Backend Service Name.   
`https/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[network_security_policy](https://docs.cloud.google.com/monitoring/api/resources#tag_network_security_policy)** |  _Actual result of policy enforcement on queries. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`blocked`: (BOOL) Policy application result.   
`backend_target_name`: HTTP(S) Backend Service Name.   
`l3/external/packet_count` BETA ** _(project)_**   
Packet count   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/RegionalNetworkSecurityPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/RegionalNetworkSecurityPolicy)** |  _Estimated number of packets by matching rule and enforcement action (sampled)._   
`rule_number`: (INT64) Rule number in RegionalSecurityPolicy.   
`blocked`: (BOOL) Rule application result.   
`l3/external/preview_packet_count` BETA ** _(project)_**   
Preview packet count   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/RegionalNetworkSecurityPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/RegionalNetworkSecurityPolicy)** |  _Estimated number of packets that would be affected by rule currently in preview mode, if that rule were to be made non-preview (sampled)._   
`rule_number`: (INT64) Rule number in RegionalSecurityPolicy.   
`blocked`: (BOOL) Rule application result.   
`mirroring_endpoint_network/dropped_mirrored_packets_count` GA ** _(project)_**   
Dropped mirrored packets   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/MirroringEndpointNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/MirroringEndpointNetwork)** |  _The number of mirrored packets received by the endpoint but dropped on egress._   
`spg_container`: The identifier of the GCP container associated with the security profile group.   
`spg_location`: The location of the GCP container associated with the security profile group.   
`spg_id`: Security profile group resource ID.   
`deployment_group_container`: The identifier of the GCP container associated with the deployment group.   
`deployment_group_location`: The location of the GCP container associated with the deployment group.   
`deployment_group_id`: Deployment group resource ID.   
`reason`: The reason for the drop.   
`mirroring_endpoint_network/received_mirrored_bytes_count` GA ** _(project)_**   
Received mirrored bytes   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/MirroringEndpointNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/MirroringEndpointNetwork)** |  _The number of mirrored bytes received by the endpoint from the source network._   
`spg_container`: The identifier of the GCP container associated with the security profile group.   
`spg_location`: The location of the GCP container associated with the security profile group.   
`spg_id`: Security profile group resource ID.   
`mirroring_endpoint_network/received_mirrored_packets_count` GA ** _(project)_**   
Received mirrored packets   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/MirroringEndpointNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/MirroringEndpointNetwork)** |  _The number of mirrored packets received by the endpoint from the source network._   
`spg_container`: The identifier of the GCP container associated with the security profile group.   
`spg_location`: The location of the GCP container associated with the security profile group.   
`spg_id`: Security profile group resource ID.   
`mirroring_endpoint_network/sent_mirrored_bytes_count` GA ** _(project)_**   
Sent mirrored bytes   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/MirroringEndpointNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/MirroringEndpointNetwork)** |  _The number of mirrored bytes sent by the endpoint to deployment groups._   
`spg_container`: The identifier of the GCP container associated with the security profile group.   
`spg_location`: The location of the GCP container associated with the security profile group.   
`spg_id`: Security profile group resource ID.   
`deployment_group_container`: The identifier of the GCP container associated with the deployment group.   
`deployment_group_location`: The location of the GCP container associated with the deployment group.   
`deployment_group_id`: Deployment group resource ID.   
`mirroring_endpoint_network/sent_mirrored_packets_count` GA ** _(project)_**   
Sent mirrored packets   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/MirroringEndpointNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/MirroringEndpointNetwork)** |  _The number of mirrored packets sent by the endpoint to deployment groups._   
`spg_container`: The identifier of the GCP container associated with the security profile group.   
`spg_location`: The location of the GCP container associated with the security profile group.   
`spg_id`: Security profile group resource ID.   
`deployment_group_container`: The identifier of the GCP container associated with the deployment group.   
`deployment_group_location`: The location of the GCP container associated with the deployment group.   
`deployment_group_id`: Deployment group resource ID.   
`partner_sse_gateway/established_bgp_sessions` GA ** _(project)_**   
Established BGP sessions   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/PartnerSSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/PartnerSSEGateway)** |  _Number of external BGP sessions established by the Partner SSE Gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`partner_sse_gateway/sse_received_bytes_count` GA ** _(project)_**   
Bytes received from partner   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/PartnerSSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/PartnerSSEGateway)** |  _Count of bytes received by the Partner SSE Gateway from the partner._   
`zone`: The zone in which the gateway received and processed packets.   
`partner_sse_gateway/sse_received_packets_count` GA ** _(project)_**   
Packets received from partner   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/PartnerSSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/PartnerSSEGateway)** |  _Count of packets received by the Partner SSE Gateway from the partner._   
`zone`: The zone in which the gateway received and processed packets.   
`partner_sse_gateway/sse_sent_bytes_count` GA ** _(project)_**   
Bytes sent to partner   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/PartnerSSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/PartnerSSEGateway)** |  _Count of bytes sent by the Partner SSE Gateway to the partner._   
`zone`: The zone from which the gateway sent packets.   
`partner_sse_gateway/sse_sent_packets_count` GA ** _(project)_**   
Packets sent to partner   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/PartnerSSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/PartnerSSEGateway)** |  _Count of packets sent by the Partner SSE Gateway to the partner._   
`zone`: The zone from which the gateway sent packets.   
`quota/firewall_associations_per_endpoint/exceeded` BETA ** _(project)_**   
Firewall Associations per Endpoint. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networksecurity.googleapis.com/firewall_associations_per_endpoint. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint`: The endpoint associated with the Firewall Association.   
`quota/firewall_associations_per_endpoint/limit` BETA ** _(project)_**   
Firewall Associations per Endpoint. quota limit   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current limit on quota metric networksecurity.googleapis.com/firewall_associations_per_endpoint. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint`: The endpoint associated with the Firewall Association.   
`quota/firewall_associations_per_endpoint/usage` BETA ** _(project)_**   
Firewall Associations per Endpoint. quota usage   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current usage on quota metric networksecurity.googleapis.com/firewall_associations_per_endpoint. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint`: The endpoint associated with the Firewall Association.   
`quota/intercept_deployments_associations_per_deployment_group/exceeded` GA ** _(project)_**   
Product of Intercept Deployments and Intercept Endpoint Group Associations per Intercept Deployment Group. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networksecurity.googleapis.com/intercept_deployments_associations_per_deployment_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`deployment_group`: Intercept Deployment Group.   
`quota/intercept_deployments_associations_per_deployment_group/limit` GA ** _(project)_**   
Product of Intercept Deployments and Intercept Endpoint Group Associations per Intercept Deployment Group. quota limit   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current limit on quota metric networksecurity.googleapis.com/intercept_deployments_associations_per_deployment_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`deployment_group`: Intercept Deployment Group.   
`quota/intercept_deployments_associations_per_deployment_group/usage` GA ** _(project)_**   
Product of Intercept Deployments and Intercept Endpoint Group Associations per Intercept Deployment Group. quota usage   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current usage on quota metric networksecurity.googleapis.com/intercept_deployments_associations_per_deployment_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`deployment_group`: Intercept Deployment Group.   
`quota/intercept_endpoint_group_associations_per_endpoint_group/exceeded` GA ** _(project)_**   
Intercept Endpoint Group Associations per Intercept Endpoint Group. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networksecurity.googleapis.com/intercept_endpoint_group_associations_per_endpoint_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint_group`: Intercept Endpoint Group.   
`quota/intercept_endpoint_group_associations_per_endpoint_group/limit` GA ** _(project)_**   
Intercept Endpoint Group Associations per Intercept Endpoint Group. quota limit   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current limit on quota metric networksecurity.googleapis.com/intercept_endpoint_group_associations_per_endpoint_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint_group`: Intercept Endpoint Group.   
`quota/intercept_endpoint_group_associations_per_endpoint_group/usage` GA ** _(project)_**   
Intercept Endpoint Group Associations per Intercept Endpoint Group. quota usage   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current usage on quota metric networksecurity.googleapis.com/intercept_endpoint_group_associations_per_endpoint_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint_group`: Intercept Endpoint Group.   
`quota/intercept_endpoint_groups_per_deployment_group/exceeded` GA ** _(project)_**   
Intercept Endpoint Groups per Intercept Deployment Group. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networksecurity.googleapis.com/intercept_endpoint_groups_per_deployment_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`deployment_group`: Intercept Deployment Group.   
`quota/intercept_endpoint_groups_per_deployment_group/limit` GA ** _(project)_**   
Intercept Endpoint Groups per Intercept Deployment Group. quota limit   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current limit on quota metric networksecurity.googleapis.com/intercept_endpoint_groups_per_deployment_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`deployment_group`: Intercept Deployment Group.   
`quota/intercept_endpoint_groups_per_deployment_group/usage` GA ** _(project)_**   
Intercept Endpoint Groups per Intercept Deployment Group. quota usage   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current usage on quota metric networksecurity.googleapis.com/intercept_endpoint_groups_per_deployment_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`deployment_group`: Intercept Deployment Group.   
`quota/security_profile_groups_per_intercept_endpoint_group/exceeded` GA ** _(project)_**   
Security Profile Groups per Intercept Endpoint Group. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networksecurity.googleapis.com/security_profile_groups_per_intercept_endpoint_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint_group`: Intercept Endpoint Group.   
`quota/security_profile_groups_per_intercept_endpoint_group/limit` GA ** _(project)_**   
Security Profile Groups per Intercept Endpoint Group. quota limit   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current limit on quota metric networksecurity.googleapis.com/security_profile_groups_per_intercept_endpoint_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint_group`: Intercept Endpoint Group.   
`quota/security_profile_groups_per_intercept_endpoint_group/usage` GA ** _(project)_**   
Security Profile Groups per Intercept Endpoint Group. quota usage   
`GAUGE`, `INT64`, `1`   
**[networksecurity.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/Location)** |  _Current usage on quota metric networksecurity.googleapis.com/security_profile_groups_per_intercept_endpoint_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint_group`: Intercept Endpoint Group.   
`sse_gateway/sse_received_bytes_count` DEPRECATED ** _(project)_**   
Bytes received from partner   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of bytes received by the SSE Gateway from the partner endpoint. Use networkconnectivity.googleapis.com/spoke/gateway/received_bytes_count instead._  
`sse_gateway/sse_received_packets_count` DEPRECATED ** _(project)_**   
Packets received from partner   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of packets received by the SSE Gateway from the partner endpoint. Use networkconnectivity.googleapis.com/spoke/gateway/received_packets_count instead._  
`sse_gateway/sse_sent_bytes_count` DEPRECATED ** _(project)_**   
Bytes sent to partner   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of bytes sent by the SSE Gateway to the partner endpoint. Use networkconnectivity.googleapis.com/spoke/gateway/sent_bytes_count instead._  
`sse_gateway/sse_sent_packets_count` DEPRECATED ** _(project)_**   
Packets sent to partner   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of packets sent by the SSE Gateway to the partner endpoint. Use networkconnectivity.googleapis.com/spoke/gateway/sent_packets_count instead._  
`sse_gateway/trusted_network_received_bytes_count` DEPRECATED ** _(project)_**   
Bytes received from trusted network   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of bytes received by the SSE Gateway from a trusted application network. Use networkconnectivity.googleapis.com/spoke/gateway/received_bytes_count instead._  
`sse_gateway/trusted_network_received_packets_count` DEPRECATED ** _(project)_**   
Packets received from trusted network   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of packets received by the SSE Gateway from a trusted application network. Use networkconnectivity.googleapis.com/spoke/gateway/received_packets_count instead._  
`sse_gateway/trusted_network_sent_bytes_count` DEPRECATED ** _(project)_**   
Bytes sent to trusted network   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of bytes sent by the SSE Gateway to a trusted application network. Use networkconnectivity.googleapis.com/spoke/gateway/sent_bytes_count instead._  
`sse_gateway/trusted_network_sent_packets_count` DEPRECATED ** _(project)_**   
Packets sent to trusted network   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of packets sent by the SSE Gateway to a trusted application network. Use networkconnectivity.googleapis.com/spoke/gateway/sent_packets_count instead._  
`sse_gateway/untrusted_network_received_bytes_count` DEPRECATED ** _(project)_**   
Bytes received from untrusted network   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of bytes received by the SSE Gateway from an untrusted user network. Use networkconnectivity.googleapis.com/spoke/gateway/received_bytes_count instead._  
`sse_gateway/untrusted_network_received_packets_count` DEPRECATED ** _(project)_**   
Packets received from untrusted network   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of packets received by the SSE Gateway from an untrusted user network. Use networkconnectivity.googleapis.com/spoke/gateway/received_packets_count instead._  
`sse_gateway/untrusted_network_sent_bytes_count` DEPRECATED ** _(project)_**   
Bytes sent to untrusted network   
`DELTA`, `INT64`, `By`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of bytes sent by the SSE Gateway to an untrusted user network. Use networkconnectivity.googleapis.com/spoke/gateway/sent_bytes_count instead._  
`sse_gateway/untrusted_network_sent_packets_count` DEPRECATED ** _(project)_**   
Packets sent to untrusted network   
`DELTA`, `INT64`, `1`   
**[networksecurity.googleapis.com/SSEGateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networksecurity.googleapis.com/SSEGateway)** |  _DEPRECATED: Count of packets sent by the SSE Gateway to an untrusted user network. Use networkconnectivity.googleapis.com/spoke/gateway/sent_packets_count instead._  
`tcp_ssl_proxy/new_connection_count` GA ** _(project)_**   
New connection count   
`DELTA`, `INT64`, `1`   
**[network_security_policy](https://docs.cloud.google.com/monitoring/api/resources#tag_network_security_policy)** |  _Actual result of policy enforcement on new connections. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`blocked`: (BOOL) Policy application result.   
`backend_target_name`: TCP/SSL Backend Service Name.   
`tcp_ssl_proxy/previewed_new_connection_count` GA ** _(project)_**   
Previewed new connection count   
`DELTA`, `INT64`, `1`   
**[network_security_policy](https://docs.cloud.google.com/monitoring/api/resources#tag_network_security_policy)** |  _New connections that would be affected by rules currently in the 'preview' mode, if those rules were to be made non-preview. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`blocked`: (BOOL) Policy application result.   
`backend_target_name`: TCP/SSL Backend Service Name.   
  
### networkservices

Metrics from [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `networkservices.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`extension/failed_open_count` BETA ** _(project)_**   
Extension failed invocations with fail-open   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The total number of times an Extension invocation failed when the system was configured to "fail open". In these instances, the original client request was allowed to proceed, ignoring the failure._   
`ignored_status`: The gRPC status of the invocation that was ignored, for example, "DEADLINE_EXCEEDED", "CANCELLED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/invocation_count` BETA ** _(project)_**   
Extension invocation count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The number of invocations handled by the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/invocation_latencies` BETA ** _(project)_**   
Extension invocation latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _Distribution calculated from the latency of each invocation._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/mutation_rejections_count` BETA ** _(project)_**   
Extension mutation rejections count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The number of extension invocations that requested headers/body/trailer mutations but were rejected. Rejections can occur for a variety of reasons, the mutation being invalid, exceeding size limits, or an internal failure._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/received_bytes_count` BETA ** _(project)_**   
Extension received bytes count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The number of bytes received from the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/received_chunks_count` BETA ** _(project)_**   
Extension received chunks count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The number of data chunks received from the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/sent_bytes_count` BETA ** _(project)_**   
Extension sent bytes count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The number of bytes sent to the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`extension/sent_chunks_count` BETA ** _(project)_**   
Extension sent chunks count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Extension](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Extension)** |  _The number of data chunks sent to the extension._   
`status`: The gRPC status of the invocation, for example, "OK", "FAILED_OPEN_OK", "DEADLINE_EXCEEDED".   
`event`: The event associated with the invocation, for example, "REQUEST_HEADERS", "RESPONSE_BODY".   
`attached_resource`: The name of a resource to which the extension is attached, that triggered the invocation.   
`protocol`: The format of communication supported by the extension, for example, "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC". This is populated for Callouts only.   
`extension_match`: If applicable, the name of the individual extension and its chain that was matched. The names will be separated by a period, for example, "chain1.extension1".   
`extension_type`: Distinguishes if the extension is a plugin or a callout.   
`extension_service`: The name of the callout backend service or plugin the extension points to.   
`https/backend_latencies` GA ** _(project)_**   
Backend latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[networkservices.googleapis.com/Gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Gateway)** |  _The latency from when the request is sent by the proxy to the backend, and the proxy receives the last byte of response. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`security_policy_action`: Action taken by security policy. Can be ALLOW or DENY.   
`https/request_bytes_count` GA ** _(project)_**   
Request bytes count   
`DELTA`, `INT64`, `By`   
**[networkservices.googleapis.com/Gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Gateway)** |  _The number of bytes sent as requests from an HTTP/S load balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`security_policy_action`: Action taken by security policy. Can be ALLOW or DENY.   
`https/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Gateway)** |  _The number of requests served by an HTTP/S load balancer. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`security_policy_action`: Action taken by security policy. Can be ALLOW or DENY.   
`https/response_bytes_count` GA ** _(project)_**   
Response bytes count   
`DELTA`, `INT64`, `By`   
**[networkservices.googleapis.com/Gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Gateway)** |  _The number of bytes sent as responses from an HTTP/S load balancer to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 90 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`security_policy_action`: Action taken by security policy. Can be ALLOW or DENY.   
`https/total_latencies` GA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[networkservices.googleapis.com/Gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Gateway)** |  _A distribution of the latency from when the request is received by the proxy, until the proxy receives an ACK from the client on last response byte. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`response_code`: (INT64) HTTP response code.   
`response_code_class`: (INT64) HTTP response code class: 200, 300, 400, 500 or 0 for none.   
`security_policy_action`: Action taken by security policy. Can be ALLOW or DENY.   
`multicast/admin/group_control_messages` GA ** _(project)_**   
The number of control messages received for the specific multicast group   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/MulticastGroup](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/MulticastGroup)** |  _The number of multicast group control messages. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`consumer_project_number`: Consumer project ID (numeric string).   
`consumer_location`: The consumer's zone.   
`message_type`: The type of the control message. (e.g. "IGMP_CONSUMER_JOINED")   
`result`: "UNKNOWN" for all but "IGMP_JOIN_REJECTED" messages. For "IGMP_JOIN_REJECTED", contains the rejection reason.   
`multicast/admin/number_of_active_consumers` GA ** _(project)_**   
The number of consumers currently subscribed to the specific multicast group   
`GAUGE`, `INT64`, `1`   
**[networkservices.googleapis.com/MulticastGroup](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/MulticastGroup)** |  _The number of active consumers per multicast group. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`consumer_project_number`: Consumer project ID (numeric string).   
`consumer_location`: The consumer's zone.   
`proxy.network.connection.count` ALPHA ** _(project)_**   
Proxy network connection count   
`GAUGE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _The number of network connections managed by the proxy._   
`network.transport`: Network transport.   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`proxy.network.connection.creations` ALPHA ** _(project)_**   
Proxy network connection creations   
`DELTA`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative count of new connections established by the proxy._   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`proxy.network.connection.duration` ALPHA ** _(project)_**   
Proxy network connection duration   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of the time elapsed from when a connection is established until it is closed._   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`proxy.network.connection.timeouts` ALPHA ** _(project)_**   
Proxy network connection timeouts   
`DELTA`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative count of network connections terminated by the proxy due to a timeout (e.g., connect, idle)._   
`timeout.type`: Timeout type.   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`proxy.network.errors` ALPHA ** _(project)_**   
Proxy network errors   
`DELTA`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative count of internal errors detected._   
`error.type`: Error type.   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`proxy.network.io` ALPHA ** _(project)_**   
Proxy network IO   
`DELTA`, `INT64`, `bytes`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _The cumulative number of bytes received or transmitted by the proxy._   
`network.io.direction`: Network IO direction.   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`gcp.principal.source`: Source principal.   
`gcp.principal.destination`: Destination principal.   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`proxy.network.tls.handshake.errors` ALPHA ** _(project)_**   
Proxy network TLS handshake errors   
`DELTA`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative count of failed TLS handshakes._   
`network.tls.error.type`: Network TLS error type.   
`network.connection.role`: Network connection role.   
`gcp.proxy.connection.direction`: Proxy connection direction.   
`gcp.resource.source.id`: Source resource ID.   
`gcp.resource.destination.id`: Destination resource ID.   
`apphub_source_application_container`: AppHub source application container.   
`apphub_source_application_id`: AppHub source application ID.   
`apphub_source_application_location`: AppHub source application location.   
`apphub_source_service_criticality_type`: AppHub source service criticality type.   
`apphub_source_service_environment_type`: AppHub source service environment type.   
`apphub_source_service_id`: AppHub source service ID.   
`apphub_source_workload_criticality_type`: AppHub source workload criticality type.   
`apphub_source_workload_environment_type`: AppHub source workload environment type.   
`apphub_source_workload_id`: AppHub source workload ID.   
`apphub_destination_application_container`: AppHub destination application container.   
`apphub_destination_application_id`: AppHub destination application ID.   
`apphub_destination_application_location`: AppHub destination application location.   
`apphub_destination_service_criticality_type`: AppHub destination service criticality type.   
`apphub_destination_service_environment_type`: AppHub destination service environment type.   
`apphub_destination_service_id`: AppHub destination service ID.   
`apphub_destination_workload_criticality_type`: AppHub destination workload criticality type.   
`apphub_destination_workload_environment_type`: AppHub destination workload environment type.   
`apphub_destination_workload_id`: AppHub destination workload ID.   
`gen_ai.agent.id`: Gen AI agent ID.   
`quota/multicast_groups_per_domain/exceeded` BETA ** _(project)_**   
Multicast Groups quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networkservices.googleapis.com/multicast_groups_per_domain. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`domain`: The name of the Multicast Domain.   
`quota/multicast_groups_per_domain/limit` BETA ** _(project)_**   
Multicast Groups quota limit   
`GAUGE`, `INT64`, `1`   
**[networkservices.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Location)** |  _Current limit on quota metric networkservices.googleapis.com/multicast_groups_per_domain. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`domain`: The name of the Multicast Domain.   
`quota/multicast_groups_per_domain/usage` BETA ** _(project)_**   
Multicast Groups quota usage   
`GAUGE`, `INT64`, `1`   
**[networkservices.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Location)** |  _Current usage on quota metric networkservices.googleapis.com/multicast_groups_per_domain. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`domain`: The name of the Multicast Domain.   
`quota/multicast_routes_per_vpc/exceeded` BETA ** _(project)_**   
Multicast Routes quota exceeded error   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric networkservices.googleapis.com/multicast_routes_per_vpc. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vpc_network_name`: The full resource name of the VPC network, e.g., projects/my-project/global/networks/my-network.   
`zone`: The zone of the Multicast routes.   
`quota/multicast_routes_per_vpc/limit` BETA ** _(project)_**   
Multicast Routes quota limit   
`GAUGE`, `INT64`, `1`   
**[networkservices.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Location)** |  _Current limit on quota metric networkservices.googleapis.com/multicast_routes_per_vpc. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vpc_network_name`: The full resource name of the VPC network, e.g., projects/my-project/global/networks/my-network.   
`zone`: The zone of the Multicast routes.   
`quota/multicast_routes_per_vpc/usage` BETA ** _(project)_**   
Multicast Routes quota usage   
`GAUGE`, `INT64`, `1`   
**[networkservices.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/Location)** |  _Current usage on quota metric networkservices.googleapis.com/multicast_routes_per_vpc. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vpc_network_name`: The full resource name of the VPC network, e.g., projects/my-project/global/networks/my-network.   
`zone`: The zone of the Multicast routes.   
`ull/admin/reorder_ratios` BETA ** _(project)_**   
ULL Unicast Reorder Ratios   
`DELTA`, `DISTRIBUTION`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Distribution of ULL Unicast reorder ratios. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`wasm_plugin/cpu/usage_times` BETA ** _(project)_**   
Wasm plugin normalized CPU usage   
`DELTA`, `DISTRIBUTION`, `us{CPU}`   
**[networkservices.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/WasmPluginVersion)** |  _CPU usage time of Wasm plugin invocations, in microseconds normalized across machine platforms._   
`status`: The status of the invocation, for example, "SUCCESS" or "CPU_LIMIT_EXCEEDED".   
`operation`: The operation type of the invocation, for example, "CONFIGURE_PLUGIN" or "HTTP_REQUEST_HEADERS".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the plugin is attached, that triggered the plugin invocation.   
`wasm_plugin/invocation_count` BETA ** _(project)_**   
Wasm plugin invocation count   
`DELTA`, `INT64`, `1`   
**[networkservices.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/WasmPluginVersion)** |  _Number of invocations handled by the Wasm plugin._   
`status`: The status of the invocation, for example, "SUCCESS" or "CPU_LIMIT_EXCEEDED".   
`operation`: The operation type of the invocation, for example, "CONFIGURE_PLUGIN" or "HTTP_REQUEST_HEADERS".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the plugin is attached, that triggered the plugin invocation.   
`wasm_plugin/invocation_latencies` BETA ** _(project)_**   
Wasm plugin invocation latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[networkservices.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/WasmPluginVersion)** |  _Wall time latency of Wasm plugin invocations, in microseconds._   
`status`: The status of the invocation, for example, "SUCCESS" or "CPU_LIMIT_EXCEEDED".   
`operation`: The operation type of the invocation, for example, "CONFIGURE_PLUGIN" or "HTTP_REQUEST_HEADERS".   
`effect`: The effect of the invocation, for example, "NONE", "CONTENT_MODIFIED" or "IMMEDIATE_RESPONSE".   
`attached_resource`: The name of a resource to which the plugin is attached, that triggered the plugin invocation.   
`wasm_plugin/memory/bytes_used` BETA ** _(project)_**   
Wasm plugin memory usage   
`GAUGE`, `DISTRIBUTION`, `By`   
**[networkservices.googleapis.com/WasmPluginVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/WasmPluginVersion)** |  _Total memory allocated by Wasm plugin VMs, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
### oracledatabase

Metrics from [Oracle Database@Google Cloud](https://cloud.google.com/solutions/oracle). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `oracledatabase.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`asm_diskgroup_utilization` GA ** _(project)_**   
ASM Diskgroup Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _Percentage of usable space used in a Disk Group. Usable space is the space available for growth. DATA disk group stores our Oracle database files. RECO disk group contains database files for recovery such as archives and flashback logs._   
`deployment_type`: Deployment type of CloudVmCluster node.   
`diskgroup_name`: Disk group name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/apex_apps` GA ** _(project)_**   
Active APEX Applications   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Displays the number of active APEX applications over the time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/apex_page_events` GA ** _(project)_**   
APEX Page Events   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Displays the number of page events over time._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/apex_page_load_time` GA ** _(project)_**   
APEX Page Load Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Average APEX page execution time over the time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/apex_workspaces` GA ** _(project)_**   
APEX Workspace Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Displays the number of APEX workspaces over the time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/average_active_sessions` GA ** _(project)_**   
Average Active Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The average number of sessions that are actively executing or waiting for resources._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of changes that were part of an update or delete operation that were made to all blocks in the SGA. Such changes generate redo log entries and thus become permanent changes to the database if the transaction is committed. This approximates total database work. This statistic indicates the rate at which buffers are being dirtied, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/blocking_sessions` GA ** _(project)_**   
Blocking Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of current blocking sessions._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/connection_latency` GA ** _(project)_**   
Connection Latency   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The time taken to connect to an Oracle Autonomous Database Serverless instance in each region from a Compute service virtual machine in the same region._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/connections_dropped_by_client` GA ** _(project)_**   
Connections Dropped By Client   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of connections dropped by the client._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/connections_dropped_by_server` GA ** _(project)_**   
Connections Dropped By Server   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of connections dropped by the server._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/cpu_time` GA ** _(project)_**   
CPU Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Average rate of accumulation of CPU time by foreground sessions in the database over the time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The CPU usage expressed as a percentage, aggregated across all consumer groups. The utilization percentage is reported with respect to the number of CPUs the database is allowed to use._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of successful logons during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/database_availability` GA ** _(project)_**   
Database Availability   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The database is available for connections in the given minute, with possible values. 1 = DB Available, 0 = DB Unavailable._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/db_time` GA ** _(project)_**   
DB Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The amount of time database user sessions spend executing database code (CPU Time + WaitTime). DB Time is used to infer database call latency, because DB Time increases in direct proportion to both database call latency (response time) and call volume. It is calculated as the average rate of accumulation of database time by foreground sessions in the database over the time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/failed_connections` GA ** _(project)_**   
Failed Connections   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of failed database connections._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/failed_logons` GA ** _(project)_**   
Failed Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of log ons that failed because of an invalid user name and/or password, during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/hard_parses` GA ** _(project)_**   
Parse Count (Hard)   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of parse calls (real parses) during the selected time interval. A hard parse is an expensive operation in terms of memory use, because it requires Oracle to allocate a workheap and other memory structures and then build a parse tree._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/logical_reads` GA ** _(project)_**   
Session Logical Reads   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The sum of "db block gets" plus "consistent gets", during the selected time interval. This includes logical reads of database blocks from either the buffer cache or process private memory._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/parse_failures` GA ** _(project)_**   
Parse Count (Failures)   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of parse failures during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/parses` GA ** _(project)_**   
Parse Count (Total)   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of hard and soft parses during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/peer_lag` GA ** _(project)_**   
Peer Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The total time in seconds by which the Disaster Recovery peer lags behind its Primary database._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/physical_read_total_bytes` GA ** _(project)_**   
Physical Read Total Bytes   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The size in bytes of disk reads by all database instance activity including application reads, backup and recovery, and other utilities, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/physical_reads` GA ** _(project)_**   
Physical Reads   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of data blocks read from disk, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/physical_write_total_bytes` GA ** _(project)_**   
Physical Write Total Bytes   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The size in bytes of all disk writes for the database instance including application activity, backup and recovery, and other utilities, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/physical_writes` GA ** _(project)_**   
Physical Writes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of data blocks written to disk, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/query_latency` GA ** _(project)_**   
Query Latency   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The time taken to display the results of a simple query on the user's screen._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/queued_statements` GA ** _(project)_**   
Queued Statements   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of queued SQL statements, aggregated across all consumer groups, during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/redo_generated` GA ** _(project)_**   
Redo Generated   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Amount of redo generated in bytes, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/running_statements` GA ** _(project)_**   
Running Statements   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of running SQL statements, aggregated across all consumer groups, during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/session_utilization` GA ** _(project)_**   
Session Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The maximum session utilization expressed as a percentage, aggregated across all consumer groups._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/sessions` GA ** _(project)_**   
Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of sessions in the database._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/sqlnet_bytes_from_client` GA ** _(project)_**   
Bytes Received via SQL*Net from Client   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of bytes received from the client over Oracle Net Services, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/sqlnet_bytes_from_dblink` GA ** _(project)_**   
Bytes Received via SQL*Net from DBLink   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of bytes received from a database link over Oracle Net Services, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/sqlnet_bytes_to_client` GA ** _(project)_**   
Bytes Sent via SQL*Net to Client   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of bytes sent to the client from the foreground processes, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/sqlnet_bytes_to_dblink` GA ** _(project)_**   
Bytes Sent via SQL*Net to DBLink   
`GAUGE`, `DOUBLE`, `By`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of bytes sent over a database link, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/storage_allocated` GA ** _(project)_**   
Storage Space Allocated   
`GAUGE`, `DOUBLE`, `GB`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Amount of space allocated to the database for all tablespaces, during the interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/storage_max` GA ** _(project)_**   
Maximum Storage Space   
`GAUGE`, `DOUBLE`, `GB`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Maximum amount of storage reserved for the database during the interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/storage_used` GA ** _(project)_**   
Storage Space Used   
`GAUGE`, `DOUBLE`, `GB`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Maximum amount of space used during the interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The percentage of the reserved maximum storage currently allocated for all database tablespaces. Represents the total reserved space for all tablespaces._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/user_commits` GA ** _(project)_**   
User Commits   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _The number of user commits during the selected time interval. When a user commits a transaction, the generated redo that reflects the changes made to database blocks must be written to disk. Commits often represent the closest thing to a user transaction rate._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/user_rollbacks` GA ** _(project)_**   
User Rollbacks   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Number of times users manually issue the ROLLBACK statement or an error occurs during a user's transactions, during the selected time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`autonomousdatabase/wait_time` GA ** _(project)_**   
Wait Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/AutonomousDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/AutonomousDatabase)** |  _Average rate of accumulation of non-idle wait time by foreground sessions in the database over the time interval._   
`autonomous_db_type`: Type of Autonomous database.   
`deployment_type`: Deployment type of Autonomous database.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`containerdatabase/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _Changes per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _Percent CPU utilization of container database._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`containerdatabase/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _The number of successful logons during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/parses` GA ** _(project)_**   
Parse Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _The number of hard and soft parses during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/storage_allocated` GA ** _(project)_**   
Storage Space Allocated   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _Total amount of storage space allocated to the database at the collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/storage_allocated_by_tablespace` GA ** _(project)_**   
Allocated Storage Space By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _Total amount of storage space allocated to the tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Tablespace name.   
`tablespace_type`: Tablespace type.   
`containerdatabase/storage_used` GA ** _(project)_**   
Storage Space Used   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _Total amount of storage space used by the database at the collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/storage_used_by_tablespace` GA ** _(project)_**   
Storage Space Used By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _Total amount of storage space used by tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Tablespace name.   
`tablespace_type`: Tablespace type.   
`containerdatabase/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _The percentage of provisioned storage capacity currently in use. Represents the total allocated space for all tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/storage_utilization_by_tablespace` GA ** _(project)_**   
Storage Space Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _This indicates the percentage of storage space utilized by the tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Tablespace name.   
`tablespace_type`: Tablespace type.   
`containerdatabase/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`containerdatabase/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ContainerDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _Percent CPU utilization of CloudVmCluster._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/asm_diskgroup_utilization` GA ** _(project)_**   
ASM Diskgroup Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _Percentage of usable space used in a Disk Group. Usable space is the space available for growth. DATA disk group stores our Oracle database files. RECO disk group contains database files for recovery such as archives and flashback logs._   
`deployment_type`: Deployment type of the node.   
`diskgroup_name`: Disk group name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _Percent CPU utilization._   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/filesystem_utilization` GA ** _(project)_**   
Filesystem Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _Percent utilization of provisioned filesystem._   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`filesystem_name`: Filesystem name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/load_average` GA ** _(project)_**   
Load Average   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _System load average over 5 minutes._   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/memory_utilization` GA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _Percentage of memory available for starting new applications, without swapping._   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/node_status` GA ** _(project)_**   
Node Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _Indicates whether the host is reachable._   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/ocpus_allocated` GA ** _(project)_**   
OCPUs Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _The number of OCPUs allocated._   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system/swap_utilization` GA ** _(project)_**   
Swap Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystem](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystem)** |  _Percent utilization of total swap space._   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`db_system_container_database/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The Average number of blocks changed per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`db_system_container_database/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The CPU utilization expressed as a percentage, aggregated across all consumer groups. The utilization percentage is reported with respect to the number of CPUs the database is allowed to use, which is two times the number of OCPUs._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the Db System.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`db_system_container_database/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The number of successful logons during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`db_system_container_database/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`db_system_container_database/parses` GA ** _(project)_**   
Parse Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The number of hard and soft parses during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the db.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`db_system_container_database/storage_allocated` GA ** _(project)_**   
Storage Space Allocated   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _Total amount of storage space allocated to the database at the collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`db_system_container_database/storage_allocated_by_tablespace` GA ** _(project)_**   
Allocated Storage Space By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _Total amount of storage space allocated to the tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Name of the tablespace.   
`tablespace_type`: Type of the tablespace.   
`db_system_container_database/storage_used` GA ** _(project)_**   
Storage Space Used   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _Total amount of storage space used by the database at the collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`db_system_container_database/storage_used_by_tablespace` GA ** _(project)_**   
Storage Used By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _Total amount of storage space used by tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Name of the tablespace.   
`tablespace_type`: Type of the tablespace.   
`db_system_container_database/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The percentage of provisioned storage capacity currently in use. Represents the total allocated space for all tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`db_system_container_database/storage_utilization_by_tablespace` GA ** _(project)_**   
Storage Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _This indicates the percentage of storage space utilized by the tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Name of the tablespace.   
`tablespace_type`: Type of the tablespace.   
`db_system_container_database/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`db_system_container_database/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemContainerDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of the node.   
`deployment_type`: Deployment type of the Db System.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`db_system_pluggable_database/allocated_storage_utilization_by_tablespace` GA ** _(project)_**   
Allocated Storage Utilization by Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The percentage of space used by a tablespace, out of allocated space. For CDBs, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`tablespace_name`: Name of the tablespace.   
`resource_type`: Type of the database resource.   
`tablespace_contents`: Tablespace contents.   
`db_system_pluggable_database/apply_lag` GA ** _(project)_**   
Apply Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of seconds the standby database is behind the primary database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_role`: Role of the database.   
`primary_db_id`: Primary database identifier.   
`primary_db_unique_name`: Primary database unique name.   
`db_system_pluggable_database/apply_lag_data_refresh_elapsed_time` GA ** _(project)_**   
Apply Lag Data Refresh Elapsed Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The elapsed time since the ApplyLag metric sample was last collected._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_role`: Role of the database.   
`primary_db_id`: Primary database identifier.   
`primary_db_unique_name`: Primary database unique name.   
`db_system_pluggable_database/avg_gc_current_block_receive_time` GA ** _(project)_**   
Average GC Current Block Receive Time   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average global cache current blocks receive time. Statistic reports the mean value. For Real Application Cluster (RAC) databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/avg_gccr_block_receive_time` GA ** _(project)_**   
Average GC CR Block Receive Time   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average global cache consistent-read (CR) block receive time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/backup_duration` GA ** _(project)_**   
Backup Duration   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The duration of the last database backup._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`status`: Status of the backup.   
`backup_type`: Type of the backup.   
`device_type`: Type of the device.   
`db_system_pluggable_database/backup_size` GA ** _(project)_**   
Backup Size   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The size of the last database backup._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`status`: Status of the backup.   
`backup_type`: Type of the backup.   
`device_type`: Type of the device.   
`db_system_pluggable_database/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average number of blocks changed per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/blocking_sessions` GA ** _(project)_**   
Blocking Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The current blocking sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/cpu_time` GA ** _(project)_**   
CPU Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average rate of accumulation of CPU time by foreground sessions in the database instance over the time interval. The CPU time component of Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The CPU utilization expressed as a percentage, aggregated across all consumer groups. The utilization percentage is reported with respect to the number of CPUs the database is allowed to use, which is two times the number of OCPUs._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/cpus` GA ** _(project)_**   
CPUs   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of CPUs during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/cpus_enabled` GA ** _(project)_**   
CPUs Enabled   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of CPUs or processors available on the database instance._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of successful logons during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/db_mgmt_job_executions` GA ** _(project)_**   
DB Management Job Executions Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of SQL job executions on a single Managed Database or a Database Group, and their status. Status dimensions can be the following values Succeeded, Failed, InProgress._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`managed_database_id`: Managed database identifier.   
`managed_database_group_id`: Managed database group identifier.   
`job_id`: The identifier of the job.   
`status`: Status of the job run.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/db_time` GA ** _(project)_**   
DB Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average rate of accumulation of database time (CPU + Wait) by foreground sessions in the database instance over the time interval. Also known as Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/ecpus_allocated` GA ** _(project)_**   
ECPUs Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The actual number of ECPUs allocated by the service during the selected interval. This metric is available if the VM cluster uses the ECPU compute model._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`db_system_pluggable_database/estimated_failover_time` GA ** _(project)_**   
Estimated Failover Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of seconds required to fail over to the standby database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_role`: Role of the database.   
`primary_db_id`: Primary database identifier.   
`primary_db_unique_name`: Primary database unique name.   
`db_system_pluggable_database/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/fra_space_limit` GA ** _(project)_**   
Flash Recovery Area Space Limit   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The flash recovery area space limit._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/fra_utilization` GA ** _(project)_**   
Flash Recovery Area Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The flash recovery area utilization._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/gcc_current_blocks_received` GA ** _(project)_**   
GC Current Blocks Received   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The global cache current blocks received per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/gccr_blocks_received` GA ** _(project)_**   
GC CR Blocks Received   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The global cache CR blocks received per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/interconnect_traffic` GA ** _(project)_**   
Interconnect Traffic   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average internode data transfer rate._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/invalid_objects` GA ** _(project)_**   
Invalid Objects   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of invalid database objects._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/io_throughput` GA ** _(project)_**   
IO Throughput   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average throughput in MB per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`io_type`: Type of IO.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/iops` GA ** _(project)_**   
IOPS   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average number of IO operations per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`io_type`: Type of IO.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/logical_blocks_read` GA ** _(project)_**   
Logical Blocks Read   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average number of blocks read from SGA/Memory (buffer cache) per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/max_tablespace_size` GA ** _(project)_**   
Max Tablespace Size   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The maximum possible tablespace size. For CDBs, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/memory_usage` GA ** _(project)_**   
Memory Usage   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The total size of the memory pool._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`memory_type`: Type of memory.   
`memory_pool`: Memory pool.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/monitoring_status` GA ** _(project)_**   
Monitoring Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The monitoring status of the resource. If metric collection fails, error information is captured in this metric._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`collection_name`: Collection name.   
`resource_type`: Type of the database resource.   
`error_severity`: Severity of the error.   
`error_code`: Error code.   
`db_system_pluggable_database/monitoring_user_password_expiration` GA ** _(project)_**   
Monitoring User Password Expiration   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of days left before the monitoring user password expires._   
`is_perpetual`: Whether the password is perpetual.   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/non_reclaimable_fra` GA ** _(project)_**   
Non Reclaimable FRA   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The non-reclaimable fast recovery area._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/ocpus_allocated` GA ** _(project)_**   
OCPUs Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The actual number of OCPUs allocated by the service during the selected interval of time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`db_system_pluggable_database/parses` GA ** _(project)_**   
Parse Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of hard and soft parses during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/parses_by_type` GA ** _(project)_**   
Parses By Type   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of hard or soft parses per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`parse_type`: Parse type.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/problematic_scheduled_dbms_jobs` GA ** _(project)_**   
Problematic Scheduled DBMS Jobs   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of problematic scheduled database jobs._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`type`: Type of the problematic job.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/process_limit_utilization` GA ** _(project)_**   
Process Limit Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The process limit utilization._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/processes` GA ** _(project)_**   
Processes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of database processes._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/reclaimable_fra_space` GA ** _(project)_**   
Reclaimable FRA Space   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The flash recovery area reclaimable space._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/recoverable_fra` GA ** _(project)_**   
Recoverable FRA   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The reclaimable fast recovery area._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/recovery_window` GA ** _(project)_**   
Recovery Window   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The current recovery window of a database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`device_type`: Type of the device.   
`db_system_pluggable_database/redo_apply_rate` GA ** _(project)_**   
Redo Apply Rate   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The redo apply rate on the standby database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_role`: Role of the database.   
`primary_db_id`: Primary database identifier.   
`primary_db_unique_name`: Primary database unique name.   
`db_system_pluggable_database/redo_generation_rate` GA ** _(project)_**   
Redo Generation Rate   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The redo generation rate on the primary database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/redo_size` GA ** _(project)_**   
Redo Size   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average amount of redo generated._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/retention_period` GA ** _(project)_**   
Retention Period   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of days for which database backups are retained._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/session_limit_utilization` GA ** _(project)_**   
Session Limit Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The session limit utilization._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/sessions` GA ** _(project)_**   
Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of sessions in the database._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/storage_allocated` GA ** _(project)_**   
Storage Allocated   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The total amount of storage space allocated to the database at collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/storage_allocated_by_tablespace` GA ** _(project)_**   
Storage Allocated by Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The total amount of storage space allocated to the tablespace at collection time. In the case of CDBs, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/storage_used` GA ** _(project)_**   
Storage Used   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The total storage used by the database at collection time, including the space used by tablespaces, flash recovery area, control files, and log files._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/storage_used_by_tablespace` GA ** _(project)_**   
Storage Used by Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The total amount of storage space used by tablespace at collection time. In the case of CDBs, this metric provides root container tablespace._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The percentage of provisioned storage capacity currently in use. Represents the total allocated space for all tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/storage_utilization_by_tablespace` GA ** _(project)_**   
Storage Utilization by Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The percentage of storage space utilized by the tablespace at the collection time. In the case of CDBs, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/transactions_by_status` GA ** _(project)_**   
Transactions By Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of committed or rolled back transactions per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`transaction_status`: Transaction status.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/transport_lag` GA ** _(project)_**   
Transport Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of seconds of redo not yet available on the standby database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_role`: Role of the database.   
`primary_db_id`: Primary database identifier.   
`primary_db_unique_name`: Primary database unique name.   
`db_system_pluggable_database/transport_lag_data_refresh_elapsed_time` GA ** _(project)_**   
Transport Lag Data Refresh Elapsed Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The elapsed time since the TransportLagDataRefreshElapsedTime metric sample was last collected._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`db_role`: Role of the database.   
`primary_db_id`: Primary database identifier.   
`primary_db_unique_name`: Primary database unique name.   
`db_system_pluggable_database/unprotected_data_window` GA ** _(project)_**   
Unprotected Data Window   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The current unprotected data window of a database._   
`deployment_type`: Deployment type of the node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`device_type`: Type of the device.   
`db_system_pluggable_database/unusable_indexes` GA ** _(project)_**   
Unusable Indexes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The number of unusable indexes in the database schema._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`schema_name`: Schema name.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/usable_fra` GA ** _(project)_**   
Usable FRA   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The usable fast recovery area._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/used_fra_space` GA ** _(project)_**   
Used FRA Space   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The flash recovery area space usage._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`resource_type`: Type of the database resource.   
`db_system_pluggable_database/wait_time` GA ** _(project)_**   
Wait Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/DbSystemPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/DbSystemPluggableDatabase)** |  _The average rate of accumulation of non-idle wait time by foreground sessions in the database instance over the time interval. The wait time component of Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of the node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of the node.   
`wait_class`: Wait class.   
`resource_type`: Type of the database resource.   
`exadb_containerdatabase/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _Changes per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _Percent CPU utilization of container database._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`exadb_containerdatabase/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The number of successful logons during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/parses` GA ** _(project)_**   
Parse Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The number of hard and soft parses during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/redo_generation_rate` GA ** _(project)_**   
Redo Generation Rate   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The redo generation rate on the primary database._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`resource_type`: Type of the database resource.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`exadb_containerdatabase/storage_allocated` GA ** _(project)_**   
Storage Space Allocated   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _Total amount of storage space allocated to the database at the collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/storage_allocated_by_tablespace` GA ** _(project)_**   
Allocated Storage Space By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _Total amount of storage space allocated to the tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Tablespace name.   
`tablespace_type`: Tablespace type.   
`exadb_containerdatabase/storage_used` GA ** _(project)_**   
Storage Space Used   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _Total amount of storage space used by the database at the collection time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/storage_used_by_tablespace` GA ** _(project)_**   
Storage Space Used By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _Total amount of storage space used by tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Tablespace name.   
`tablespace_type`: Tablespace type.   
`exadb_containerdatabase/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The percentage of provisioned storage capacity currently in use. Represents the total allocated space for all tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/storage_utilization_by_tablespace` GA ** _(project)_**   
Storage Space Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _This indicates the percentage of storage space utilized by the tablespace at the collection time. In case of container database, this metric provides root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`tablespace_name`: Tablespace name.   
`tablespace_type`: Tablespace type.   
`exadb_containerdatabase/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_containerdatabase/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbContainerDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbContainerDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`database_resource_id`: Oracle cloud Resource identifier of the database.   
`exadb_pluggabledatabase/allocated_storage_utilization_by_tablespace` GA ** _(project)_**   
Allocated Space Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The percentage of space used by tablespace, out of all allocated. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/avg_gc_current_block_receive_time` GA ** _(project)_**   
Average GC Current Block Receive Time   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average global cache current blocks receive time. Statistic reports the mean value. For Real Application Cluster (RAC) databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/avg_gccr_block_receive_time` GA ** _(project)_**   
Average GC CR Block Receive Time   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average global cache CR (consistent-read) block receive time. For RAC / cluster databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average number of blocks changed per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/blocking_sessions` GA ** _(project)_**   
Blocking Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _Current blocking sessions. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/cpu_time` GA ** _(project)_**   
CPU Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average rate of accumulation of CPU time by foreground sessions in the database instance over the time interval. The CPU time component of Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The CPU utilization expressed as a percentage, aggregated across all consumer groups. The utilization percentage is reported with respect to the number of CPUs the database is allowed to use, which is two times the number of OCPUs._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/cpus` GA ** _(project)_**   
CPU Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of CPUs during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of successful logons during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/db_mgmt_job_executions` GA ** _(project)_**   
Job Executions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of SQL job executions on a single managed database or a database group, and their status._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`managed_database_id`: Managed database identifier.   
`managed_database_group_id`: Managed database group identifier.   
`job_id`: The identifier of the job.   
`status`: Status of the job run.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/db_time` GA ** _(project)_**   
DB Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average rate of accumulation of database time (CPU + Wait) by foreground sessions in the database instance over the time interval. Also known as Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/ecpus_allocated` GA ** _(project)_**   
ECPU Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The actual number of ECPUs allocated by the service during the selected interval. This metric is available if the VM cluster uses the ECPU compute model._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`exadb_pluggabledatabase/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/fra_space_limit` GA ** _(project)_**   
Flash Recovery Area Limit   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The flash recovery area space limit._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/fra_utilization` GA ** _(project)_**   
Flash Recovery Area Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The flash recovery area utilization._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/gc_current_blocks_received` GA ** _(project)_**   
GC Current Blocks Received   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _Represents global cache current blocks received per second. Statistic reports the mean value. For Real Application Cluster (RAC) databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/gccr_blocks_received` GA ** _(project)_**   
GC CR Blocks Received   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The global cache CR (consistent-read) blocks received per second. For RAC / cluster databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/interconnect_traffic` GA ** _(project)_**   
Average Interconnect Traffic   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average internode data transfer rate. For RAC / cluster databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/invalid_objects` GA ** _(project)_**   
Invalid Objects   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _Invalid database objects count. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/io_throughput` GA ** _(project)_**   
IO Throughput   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average throughput in MB per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`io_type`: Type of IO.   
`exadb_pluggabledatabase/iops` GA ** _(project)_**   
IOPS   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average number of input-output operations per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`io_type`: Type of IO.   
`exadb_pluggabledatabase/logical_blocks_read` GA ** _(project)_**   
Logical Reads   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average number of blocks read from SGA/Memory (buffer cache) per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/max_tablespace_size` GA ** _(project)_**   
Max Tablespace Size   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The maximum possible tablespace size. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/memory_usage` GA ** _(project)_**   
Memory Usage   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _Memory pool total size in MB._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`memory_type`: Type of memory.   
`memory_pool`: Memory pool.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/monitoring_status` GA ** _(project)_**   
Monitoring Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The monitoring status of the resource. If a metric collection fails, error information is captured in this metric._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`collection_name`: Collection name.   
`resource_type`: Type of the database resource.   
`error_severity`: Severity of the error.   
`error_code`: Error code.   
`exadb_pluggabledatabase/monitoring_user_password_expiration` GA ** _(project)_**   
Monitoring User Password Expiration   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of days left before the monitoring user password expires._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/non_reclaimable_fra` GA ** _(project)_**   
Non Reclaimable Fast Recovery Area   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The Non-reclaimable fast recovery area._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/ocpus_allocated` GA ** _(project)_**   
OCPU Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The actual number of OCPUs allocated by the service during the selected interval of time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`exadb_pluggabledatabase/parses` GA ** _(project)_**   
Parse Count (Total)   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of hard and soft parses during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/parses_by_type` GA ** _(project)_**   
Parses By Type   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of hard or soft parses per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`parse_type`: Parse type.   
`exadb_pluggabledatabase/problematic_scheduled_dbms_jobs` GA ** _(project)_**   
Problematic Scheduled DBMS Jobs   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The problematic scheduled database jobs count. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`type`: Type of the problematic scheduled dbms jobs.   
`exadb_pluggabledatabase/process_limit_utilization` GA ** _(project)_**   
Process Limit Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The process limit utilization._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/processes` GA ** _(project)_**   
Process Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The database processes count._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/reclaimable_fra_space` GA ** _(project)_**   
Flash Recovery Area Reclaimable Space   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The flash recovery area reclaimable space._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/recoverable_fra` GA ** _(project)_**   
Reclaimable Fast Recovery Area   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The reclaimable fast recovery area._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/redo_size` GA ** _(project)_**   
Redo Generated   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average amount of redo generated, in MB per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/session_limit_utilization` GA ** _(project)_**   
Session Limit Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The session limit utilization._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/sessions` GA ** _(project)_**   
Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of sessions in the database._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/storage_allocated` GA ** _(project)_**   
Allocated Storage Space   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The maximum amount of space allocated by tablespace during the interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/storage_allocated_by_tablespace` GA ** _(project)_**   
Allocated Storage Space By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The maximum amount of space allocated by tablespace during the interval. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/storage_used` GA ** _(project)_**   
Storage Space Used   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The maximum amount of space used during the interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/storage_used_by_tablespace` GA ** _(project)_**   
Storage Space Used By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The maximum amount of space used by tablespace during the interval. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The percentage of provisioned storage capacity currently in use. Represents the total allocated space for all tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/storage_utilization_by_tablespace` GA ** _(project)_**   
Storage Space Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The percentage of the space utilized, by tablespace. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/transactions_by_status` GA ** _(project)_**   
Transactions By Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The number of committed or rolled back transactions per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`transaction_status`: Transaction status.   
`exadb_pluggabledatabase/unusable_indexes` GA ** _(project)_**   
Unusable Indexes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _Unusable indexes count in database schema. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`schema_name`: Schema name.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/usable_fra` GA ** _(project)_**   
Usable Fast Recovery Area   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The useable fast recovery area._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/used_fra_space` GA ** _(project)_**   
Flash Recovery Area Usage   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The flash recovery area space usage._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`exadb_pluggabledatabase/wait_time` GA ** _(project)_**   
Wait Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/ExadbPluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbPluggableDatabase)** |  _The average rate of accumulation of non-idle wait time by foreground sessions in the database instance over the time interval. The wait time component of Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`wait_class`: Wait class.   
`exadb_vm_cluster/asm_diskgroup_utilization` GA ** _(project)_**   
ASM Diskgroup Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Percentage of usable space used in a Disk Group. Usable space is the space available for growth. DATA disk group stores our Oracle database files. RECO disk group contains database files for recovery such as archives and flashback logs._   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`diskgroup_name`: Disk group name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Percent CPU utilization of ExadbVmCluster._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/ecpus_enabled` GA ** _(project)_**   
Ecpus Enabled   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _The actual number of ECPUs enabled by the service during the selected interval. This metric is available if the VM cluster uses the ECPU compute model._   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/exascale_vault_utilization` GA ** _(project)_**   
Exascale Vault Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Percent Exascale Vault Utilization._   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`vault_name`: Vault name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/filesystem_utilization` GA ** _(project)_**   
Filesystem Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Percent utilization of provisioned filesystem._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`filesystem_name`: File system name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/load_average` GA ** _(project)_**   
Load Average   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _System load average over 5 minutes._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/memory_utilization` GA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Percentage of memory available for starting new applications, without swapping._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/node_status` GA ** _(project)_**   
Node Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Indicates whether the host is reachable._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/ocpus_allocated` GA ** _(project)_**   
OCPU Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _The number of OCPUs allocated._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`exadb_vm_cluster/swap_utilization` GA ** _(project)_**   
Swap Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/ExadbVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/ExadbVmCluster)** |  _Percent utilization of total swap space._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of ExadbVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`filesystem_utilization` GA ** _(project)_**   
Filesystem Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _Percent utilization of provisioned filesystem._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`filesystem_name`: File system name.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`goldengate_deployment/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Total CPU usage percentage by all consumer groups._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/deployment_health` GA ** _(project)_**   
Overall Deployment Health   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Overall percentage health of deployment services._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/deployment_inbound_lag` GA ** _(project)_**   
Deployment Inbound Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Average lag, in seconds, for all inbound streams critical to deployment health._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/deployment_outbound_lag` GA ** _(project)_**   
Deployment Outbound Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Average lag, in seconds, for all outbound streams critical to deployment health._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/distribution_path_lag` GA ** _(project)_**   
Distribution Path Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Average lag, in seconds, of a Distribution Path process in the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`distribution_path_name`: Distribution Path name.   
`goldengate_deployment/distribution_path_status` GA ** _(project)_**   
Distribution Path Status   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Health percentage of a Distribution Path process in the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`distribution_path_name`: Distribution Path name.   
`goldengate_deployment/extract_lag` GA ** _(project)_**   
Extract Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _The difference, in seconds, between the time the Extract processed a record and the timestamp of that record in the data source._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`extract_name`: Extract name.   
`goldengate_deployment/extract_status` GA ** _(project)_**   
Extract Status   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Health percentage of an Extract process in the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`extract_name`: Extract name.   
`goldengate_deployment/file_system_usage` GA ** _(project)_**   
File System Usage   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Percentage of file system used._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/heartbeat_lag` GA ** _(project)_**   
Heartbeat Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Average Heartbeat Lag in seconds._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`replicat_name`: Replicat name.   
`age_seconds`: Age in seconds.   
`goldengate_deployment/memory_utilization` GA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Percentage of available memory used._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/ocpu_consumption` GA ** _(project)_**   
OCPU Consumption   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Total OCPU number consumed by the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/receiver_path_lag` GA ** _(project)_**   
Receiver Path Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Average lag, in seconds, of Receiver Path process in the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`receiver_path_name`: Receiver Path name.   
`goldengate_deployment/receiver_path_status` GA ** _(project)_**   
Receiver Path Status   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Health percentage of a Receiver Path process in the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`receiver_path_name`: Receiver Path name.   
`goldengate_deployment/replicat_lag` GA ** _(project)_**   
Replicat Lag   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _The difference, in seconds, between the time the Replicat processed the last record and the timestamp of the record in the trail._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`replicat_name`: Replicat name.   
`goldengate_deployment/replicat_status` GA ** _(project)_**   
Replicat Status   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Health percentage of a Replicat process in the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`replicat_name`: Replicat name.   
`goldengate_deployment/swap_space_usage` GA ** _(project)_**   
Swap Space Usage   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Percentage of swap space used by the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`goldengate_deployment/temp_space_usage` GA ** _(project)_**   
Temporary Space Usage   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/GoldengateDeployment](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/GoldengateDeployment)** |  _Percentage of temp space used by the deployment._   
`resource_id`: Deployment OCID.   
`deployment_name`: Deployment name.   
`load_average` GA ** _(project)_**   
Load Average   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _System load average over 5 minutes._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`memory_utilization` GA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _Percentage of memory available for starting new applications, without swapping._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`node_status` GA ** _(project)_**   
Node Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _Indicates whether the host is reachable._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`ocpus_allocated` GA ** _(project)_**   
OCPU Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _The number of OCPUs allocated._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`pluggabledatabase/allocated_storage_utilization_by_tablespace` GA ** _(project)_**   
Allocated Space Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The percentage of space used by tablespace, out of all allocated. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/avg_gc_current_block_receive_time` GA ** _(project)_**   
Average GC Current Block Receive Time   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average global cache current blocks receive time. Statistic reports the mean value. For Real Application Cluster (RAC) databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/avg_gccr_block_receive_time` GA ** _(project)_**   
Average GC CR Block Receive Time   
`GAUGE`, `DOUBLE`, `ms`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average global cache CR (consistent-read) block receive time. For RAC / cluster databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/block_changes` GA ** _(project)_**   
DB Block Changes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average number of blocks changed per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/blocking_sessions` GA ** _(project)_**   
Blocking Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _Current blocking sessions. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/cpu_time` GA ** _(project)_**   
CPU Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average rate of accumulation of CPU time by foreground sessions in the database instance over the time interval. The CPU time component of Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/cpu_utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The CPU utilization expressed as a percentage, aggregated across all consumer groups. The utilization percentage is reported with respect to the number of CPUs the database is allowed to use, which is two times the number of OCPUs._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/cpus` GA ** _(project)_**   
CPU Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of CPUs during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/current_logons` GA ** _(project)_**   
Current Logons   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of successful logons during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/db_mgmt_job_executions` GA ** _(project)_**   
Job Executions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of SQL job executions on a single managed database or a database group, and their status._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`managed_database_id`: Managed database identifier.   
`managed_database_group_id`: Managed database group identifier.   
`job_id`: The identifier of the job.   
`status`: Status of the job run.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/db_time` GA ** _(project)_**   
DB Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average rate of accumulation of database time (CPU + Wait) by foreground sessions in the database instance over the time interval. Also known as Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/executions` GA ** _(project)_**   
Execute Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of user and recursive calls that executed SQL statements during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/fra_space_limit` GA ** _(project)_**   
Flash Recovery Area Limit   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The flash recovery area space limit. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/fra_utilization` GA ** _(project)_**   
Flash Recovery Area Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The flash recovery area utilization. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/gc_current_blocks_received` GA ** _(project)_**   
GC Current Blocks Received   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _Represents global cache current blocks received per second. Statistic reports the mean value. For Real Application Cluster (RAC) databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/gccr_blocks_received` GA ** _(project)_**   
GC CR Blocks Received   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The global cache CR (consistent-read) blocks received per second. For RAC / cluster databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/interconnect_traffic` GA ** _(project)_**   
Average Interconnect Traffic   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average internode data transfer rate. For RAC / cluster databases only._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/invalid_objects` GA ** _(project)_**   
Invalid Objects   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _Invalid database objects count. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/io_throughput` GA ** _(project)_**   
IO Throughput   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average throughput in MB per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`io_type`: Type of IO.   
`pluggabledatabase/iops` GA ** _(project)_**   
IOPS   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average number of input-output operations per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`io_type`: Type of IO.   
`pluggabledatabase/logical_blocks_read` GA ** _(project)_**   
Logical Reads   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average number of blocks read from SGA/Memory (buffer cache) per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/max_tablespace_size` GA ** _(project)_**   
Max Tablespace Size   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The maximum possible tablespace size. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/memory_usage` GA ** _(project)_**   
Memory Usage   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _Memory pool total size in MB._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`memory_type`: Type of memory.   
`memory_pool`: Memory pool.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/monitoring_status` GA ** _(project)_**   
Monitoring Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The monitoring status of the resource. If a metric collection fails, error information is captured in this metric._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`collection_name`: Collection name.   
`resource_type`: Type of the database resource.   
`error_severity`: Severity of the error.   
`error_code`: Error code.   
`pluggabledatabase/non_reclaimable_fra` GA ** _(project)_**   
Non Reclaimable Fast Recovery Area   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The Non-reclaimable fast recovery area. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/ocpus_allocated` GA ** _(project)_**   
OCPU Allocated   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The actual number of OCPUs allocated by the service during the selected interval of time._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`pluggabledatabase/parses` GA ** _(project)_**   
Parse Count (Total)   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of hard and soft parses during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/parses_by_type` GA ** _(project)_**   
Parses By Type   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of hard or soft parses per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`parse_type`: Parse type.   
`pluggabledatabase/problematic_scheduled_dbms_jobs` GA ** _(project)_**   
Problematic Scheduled DBMS Jobs   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The problematic scheduled database jobs count. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`type`: Type of the problematic scheduled dbms jobs.   
`pluggabledatabase/process_limit_utilization` GA ** _(project)_**   
Process Limit Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The process limit utilization. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/processes` GA ** _(project)_**   
Process Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The database processes count. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/reclaimable_fra_space` GA ** _(project)_**   
Flash Recovery Area Reclaimable Space   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The flash recovery area reclaimable space. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/recoverable_fra` GA ** _(project)_**   
Reclaimable Fast Recovery Area   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The reclaimable fast recovery area. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/redo_size` GA ** _(project)_**   
Redo Generated   
`GAUGE`, `DOUBLE`, `MBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average amount of redo generated, in MB per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/session_limit_utilization` GA ** _(project)_**   
Session Limit Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The session limit utilization. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/sessions` GA ** _(project)_**   
Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of sessions in the database._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/storage_allocated` GA ** _(project)_**   
Allocated Storage Space   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The maximum amount of space allocated by tablespace during the interval. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/storage_allocated_by_tablespace` GA ** _(project)_**   
Allocated Storage Space By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The maximum amount of space allocated by tablespace during the interval. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/storage_used` GA ** _(project)_**   
Storage Space Used   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The maximum amount of space used during the interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/storage_used_by_tablespace` GA ** _(project)_**   
Storage Space Used By Tablespace   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The maximum amount of space used by tablespace during the interval. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/storage_utilization` GA ** _(project)_**   
Storage Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The percentage of provisioned storage capacity currently in use. Represents the total allocated space for all tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/storage_utilization_by_tablespace` GA ** _(project)_**   
Storage Space Utilization By Tablespace   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The percentage of the space utilized, by tablespace. For container databases, this metric provides data for root container tablespaces._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`tablespace_name`: Name of the tablespace.   
`tablespace_contents`: Tablespace contents.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/transactions` GA ** _(project)_**   
Transaction Count   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The combined number of user commits and user rollbacks during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/transactions_by_status` GA ** _(project)_**   
Transactions By Status   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The number of committed or rolled back transactions per second._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`transaction_status`: Transaction status.   
`pluggabledatabase/unusable_indexes` GA ** _(project)_**   
Unusable Indexes   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _Unusable indexes count in database schema. Not applicable for container databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`schema_name`: Schema name.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/usable_fra` GA ** _(project)_**   
Usable Fast Recovery Area   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The useable fast recovery area. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/used_fra_space` GA ** _(project)_**   
Flash Recovery Area Usage   
`GAUGE`, `DOUBLE`, `GBy`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The flash recovery area space usage. Not applicable for pluggable databases._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/user_calls` GA ** _(project)_**   
User Calls   
`GAUGE`, `DOUBLE`, `1`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The combined number of logons, parses, and execute calls during the selected interval._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`pluggabledatabase/wait_time` GA ** _(project)_**   
Wait Time   
`GAUGE`, `DOUBLE`, `s`   
**[oracledatabase.googleapis.com/PluggableDatabase](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/PluggableDatabase)** |  _The average rate of accumulation of non-idle wait time by foreground sessions in the database instance over the time interval. The wait time component of Average Active Sessions._   
`resource_id`: OCID, Oracle cloud Resource identifier.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`instance_number`: Instance number.   
`instance_name`: Name of the instance.   
`hostname`: Hostname of VM cluster node.   
`resource_type`: Type of the database resource.   
`wait_class`: Wait class.   
`swap_utilization` GA ** _(project)_**   
Swap Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[oracledatabase.googleapis.com/CloudVmCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_oracledatabase.googleapis.com/CloudVmCluster)** |  _Percent utilization of total swap space._   
`hostname`: Hostname of VM cluster node.   
`deployment_type`: Deployment type of CloudVmCluster node.   
`dbnode_resource_id`: Resource identifier of the dbnode.   
`resource_id`: OCID, Oracle cloud Resource identifier.   
  
### osconfig

Metrics from [VM Manager](https://docs.cloud.google.com/compute/docs/manage-os). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `osconfig.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`patch/job/instance_state` GA ** _(project)_**   
VM instance patch state   
`GAUGE`, `INT64`, `1`   
**[osconfig.googleapis.com/PatchJob](https://docs.cloud.google.com/monitoring/api/resources#tag_osconfig.googleapis.com/PatchJob)** |  _The number of VM instances that have patch jobs in a specific state._   
`state`: The state of a patch job that is running on a VM instance. The following states are available: "PENDING", "STARTED", "APPLYING_PATCHES", "SUCCEEDED", "FAILED".   
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
