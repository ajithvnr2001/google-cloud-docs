---
url: https://docs.cloud.google.com/certificate-manager/docs/logs-metrics/
title: Logs and metrics \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:42.716580+00:00
---

# Logs and metrics  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/logs-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Certificate Manager logs various types of information about its operation and how to view that information.

## Logs

To view Certificate Manager logs, use the [Logs Explorer](https://console.cloud.google.com/logs) in the Google Cloud console.

Certificate Manager provides Google Cloud logs described in [Google Cloud logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#certificate_manager).

Certificate Manager uses Cloud Logging to capture and store logs. Certificate Manager logging is always enabled and only captures a minimal amount of information specifically related to certificate expiration. The Certificate Manager monitored resource type is `certificatemanager.googleapis.com/Project`.

You can also capture and retrieve Certificate Manager logs using Cloud Logging. See the documentation for [Cloud Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) for information on how to configure this logging mechanism.

### Configure log alerts

You can configure alerts for events that Certificate Manager writes to Cloud Logging, such as certificate expiration. For instructions, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

For example, to configure an alert for certificates that have expired, use the following as the alert query:
    
    
    logName = "projects/PROJECT_ID/logs/certificatemanager.googleapis.com%2Fcertificates_expiry" AND jsonPayload.state = "EXPIRED"
    

If you want to configure an alert for certificates that are close to expiration, use the following as the alert query:
    
    
    logName = "projects/PROJECT_ID/logs/certificatemanager.googleapis.com%2Fcertificates_expiry" AND jsonPayload.state = "CLOSE_TO_EXPIRY"
    

Replace `PROJECT_ID` with the ID of the target Google Cloud project.

For Google-managed certificates `CLOSE_TO_EXPIRY` logs are generated daily, starting 5-10 days before expiration, depending on the certificate's lifetime and renewal process. For self-managed certificates too, `CLOSE_TO_EXPIRY` logs are generated daily, starting 10 days before expiration.

## Metrics

This section lists the metrics supported by Certificate Manager. To view Certificate Manager metrics, use the [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in the Google Cloud console.

### Standard metrics

Certificate Manager writes the following standard Cloud Monitoring API metrics:

Metric | Description  
---|---  
`serviceruntime.googleapis.com/api/request_count`

  * Kind: `Delta`
  * Type: `INT64`
  * Unit: `1`

| Cumulative count of completed requests. The following labels apply:  


  * `protocol` indicates the request's protocol, such as `http` or `grpc`.
  * `response_code` is the HTTP (or equivalent for gRPC) response code for HTTP/gRPC requests. See [code list](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto).
  * `response_code_class` is the class (or equivalent for gRPC) of the response code, such as `200` or `400`.
  * `grpc_status_code` is the gRPC response code or its HTTP equivalent. See [code list](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto).

  
`serviceruntime.googleapis.com/api/request_latencies`

  * Kind: `Delta`
  * Type: `DISTRIBUTION`
  * Unit: `Seconds`

| Distribution of latencies for non-streaming requests.  
`serviceruntime.googleapis.com/api/request_sizes`

  * Kind: `Delta`
  * Type: `DISTRIBUTION`
  * Unit: `Byte`

| Distribution of request sizes. Request size is recorded when a request completes.  
`serviceruntime.googleapis.com/api/response_sizes`

  * Kind: `Delta`
  * Type: `DISTRIBUTION`
  * Unit: `Byte`

| Distribution of response sizes. Response size is recorded when a request completes.  
  
### Custom metrics

Additionally, Certificate Manager writes the following custom metrics using the Cloud Monitoring API:

Metric | Description  
---|---  
`certificatemanager.googleapis.com/project/certificates`

  * Kind: `GAUGE`
  * Type: `INT64`
  * Unit: `1`

| Number of certificates provisioned within the target Google Cloud project. The following labels apply:  


  * `type` indicates whether the certificate is Google-managed (`MANAGED`) or self-managed (`SELF_MANAGED`).
  * `scope` indicates whether the certificate scope is Cloud Load Balancing (`DEFAULT`) or Media CDN (`EDGE_CACHE`).
  * `is_active` indicates whether the certificate is active. Valid values are `true` and `false`.

  
`certificatemanager.googleapis.com/map/entries`

  * Kind: `GAUGE`
  * Type: `INT64`
  * Unit: `1`

| Number of certificate map entries provisioned within the target Google Cloud project. The following labels apply:  


  * `is_primary` indicates whether the certificate map entry is the primary entry in the certificate map. Valid values are `true` and `false`.

  
  
## What's next

  * [Deploy a Google-managed certificate with DNS authorization (tutorial)](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth)
  * [Deploy a Google-managed certificate with load balancer authorization (tutorial)](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth)
  * [Deploy a Google-managed certificate with CA Service (tutorial)](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas)
  * [Deploy a self-managed certificate (tutorial)](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed)
  * [Migrate a certificate to Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/migrate)
  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
