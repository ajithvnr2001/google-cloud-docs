---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/introduction/
title: Introduction to Apigee and Apigee hybrid playbooks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:47.482845+00:00
---

# Introduction to Apigee and Apigee hybrid playbooks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Introduction to Apigee and Apigee hybrid playbooks Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/troubleshooting-introduction) documentation._

The act of troubleshooting is both an art and a science. The constant effort of Apigee technical support teams has been to demystify the art and expose the science behind problem identification and resolution. 

## What are playbooks?

Developed in collaboration with ApigeeTechnical Support teams, Apigee troubleshooting **playbooks** are designed to provide quick and effective solutions to errors or other issues that you may encounter when working with Apigee products. 

## Audience

Troubleshooting playbooks are intended for readers with a high-level understanding of Apigee and its architecture, as well as some understanding of basic concepts such as policies and analytics. 

Some problems can be diagnosed and solved only by Apigee hybrid users and may require knowledge of internal components such as Cassandra datastores, Message Processors, and Synchronizers. 

If you are on Apigee, then we clearly specify when you can perform the indicated troubleshooting steps and when you need to contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) for assistance.

## Playbooks

This section describes the current playbooks.

To filter this table, do one or more of the following: select a category, select a product, type a search term, or click a column heading to sort. 

Select categoryApigee hybrid installation and upgradeAutomated issue surfacingCassandraDeploymentIngressgatewayLoggingManagement/UINetwork configurationRuntimeOtherSelect productApigee and Apigee hybridApigee hybrid only

Category | Playbook/Problem description | Error message | Playbook applicable for | Cassandra | [ Cassandra TLS certificate verification failure](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-tls-certificate-verification-failure) |  If the Apigee CA certificate does not match across clusters, then TLS certificate verification in Cassandra could fail.  | Apigee hybrid only  
---|---|---|---  
Cassandra | [ Troubleshooting Cassandra restore](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra-restore) |  During the Cassandra restoration in Apigee hybrid, you may encounter errors in the restore logs.  | Apigee hybrid only  
Automated issue surfacing | [ No network connectivity between runtime plane and control plane](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/no-network-connectivity) | Apigee API management requests fail:

  * API products, Developers, Apps do not get populated on the Apigee UI.
  * API proxy deployments do not complete.
  * Apigee API management requests fail.

| Apigee hybrid only  
Automated issue surfacing | [ Virtual host missing environment group](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-env-group) | After running `kubectl -n apigee get apigeeissues`, the AIS_VIRTUALHOST_MISSING_ENVGROUP error is displayed.  | Apigee hybrid only  
Automated issue surfacing | [ Virtual host missing selector](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector) | After running `kubectl -n apigee get apigeeissues`, the AIS_VIRTUALHOST_MISSING_SELECTOR error is displayed.  | Apigee hybrid only  
Automated issue surfacing | [ Ingress cert mismatch](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-mismatch) | After running `kubectl -n apigee get apigeeissues`, the AIS_INGRESS_CERT_MISMATCH error is displayed.  | Apigee hybrid only  
Automated issue surfacing | [ Ingress cert expiry](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingress-cert-expiry) | After running `kubectl -n apigee get apigeeissues`, the AIS_INGRESS_CERT_EXPIREY error is displayed.  | Apigee hybrid only  
Automated issue surfacing | [ Ingress mTLS CA cert expiry](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-expiry) | After running `kubectl -n apigee get apigeeissues`, the AIS_INGRESS_MTLS_CA_CERT_EXPIREY error is displayed.  | Apigee hybrid only  
Automated issue surfacing | [ Ingress mTLS CA cert invalid](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid) | After running `kubectl -n apigee get apigeeissues`, the AIS_INGRESS_MTLS_CA_CERT_INVALID error is displayed.  | Apigee hybrid only  
Cassandra |  [ Cassandra data replication failure](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-data-replication-failure) |  When replicating data during a multi-region expansion, the `CassandraDataReplication` status may show an error state and data replication may fail.  | Apigee hybrid only  
Cassandra |  [ Cassandra Java heap space issues](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-java-heap-space-issues) |  Cassandra heap issues may cause slowness in the Apigee hybrid proxy execution or even `Datastore` errors. Sometimes logs are an early indicator, even before the onset of symptoms.  | Apigee hybrid only  
Cassandra |  [ Cassandra pods not starting in the secondary region](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-pods-not-starting-secondary-region) |  Cassandra pods fail to start in one of the regions in a multi-region Hybrid setup. You may see a `node already exists` error message in the Cassandra pod logs, or a `FailedPreStopHook` warning in the Cassandra pod status.  | Apigee hybrid only  
Cassandra |  [ Cassandra troubleshooting guide](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra) |  When you use `kubectl` to view the pod states, you see that one or more Cassandra pods are stuck. This guide describes the diagnosis and resolution for problems with the Cassandra datastore.  | Apigee hybrid only  
Deployment |  [ API proxy deployments fail with no active runtime pods warning](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/no-active-runtime-pods-warning) |  The **No active runtime pods** warning is displayed in the **Details** dialog next to the error message **Deployment issues on ENVIRONMENT: REVISION_NUMBER** on the API proxy page.  | Apigee hybrid only  
Ingressgateway |  [ API calls fail with timeout errors](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/api-calls-fail-timeout-errors) | 
    
    
    curl: (7) Failed to connect to example.apis.com port 443: Operation timed out

**Note:** Sample error message as observed with `curl` command.  | Apigee hybrid only  
Ingressgateway |  [ API Calls failing with TLS errors](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ingressgateway/api-calls-failing-tls-errors) | 
    
    
    curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to example.apis.com:443

**Note:** Sample error message as observed with `curl` command.  | Apigee hybrid only  
Logging |  [ Troubleshooting Apigee logs missing from Cloud Logging](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cloud-logging-issues) |  No error messages are known to be shown in this scenario.  | Apigee and Apigee hybrid  
Management/UI |  [ Inconsistent/no data observed for entities in hybrid UI or through Management APIs](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/management-ui/inconsistent-data-hybrid-ui-mgmt-api) |  No error messages are known to be shown in this scenario.  | Apigee hybrid only  
Network configuration |  [ Access routing issues with Apigee ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/access-routing-issues) |  External clients are not able to access/connect to Apigee in a desired manner. These include either network connectivity failures (TLS handshake fails) or `4xx/5xx` responses from Apigee.  | Apigee and Apigee hybrid  
Network configuration | [ Apigee connectivity issue with northbound Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/psc) |  The northbound Private Service Connect setup is not working as expected, and the network endpoint group status remains in `Pending`.  | Apigee only  
Network configuration |  [ Apigee connectivity issues with southbound Private Service Connect targets ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/connectivity-with-sb-psc-targets) |  A network connection issue or a TCP timeout between Apigee and the target service would show up as a `503` error response and would show an error similar to below if you create a debug session. 
    
    
    {"fault":{"faultstring":"The Service is temporarily unavailable","detail":{"errorcode":"messaging.adaptors.http.flow.ServiceUnavailable","reason":"TARGET_CONNECT_TIMEOUT"}}}

| Apigee and Apigee hybrid  
Other | [ Expanding Istio property replica counts when draining nodes](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio) |  When draining Istio pods some nodes may not drain because they have a replica count of 1, while 3 or more replicas are required. In order to avoid this, you should set the minimum replica count for each property to at least 3.  | Apigee hybrid only  
Other | [ Message processor troubleshooting guide](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ts-message-processor) |  One or more apigee-runtime pods are not in the `Ready` state. When you use `kubectl` to describe a failed `apigee-runtime` pod, you see the error: 
    
    
    Readiness probe failed: HTTP probe failed with statuscode: 500

| Apigee hybrid only  
Other | [ Print build info](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ts-buildinfo) |  The `buildinfo` API returns information about the current build for a runtime component. This information may be useful if you need to contact support.  | Apigee hybrid only  
Other |  [ StreamingPull errors 100%](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/streaming-pull-error) |  If you see in your metrics dashboard that the method `google.pubsub.vl.Subscriber.StreamingPull` is failing with 100% errors, you can safely ignore the issue. This is expected behavior.  | Apigee hybrid only  
Deployment |  [ Instance is not reporting status for environment group](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-instance-not-reporting-status) |  Deployments of API proxies fail with Instance INSTANCE_NAME is not reporting status for environment group ENV_GROUP_NAME error in the Apigee hybrid UI.  | Apigee hybrid only  
Deployment |  [ API proxy deployments fail with apigee-serving-cert is not found or expired](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-serving-cert-not-found-or-expired) |  API proxy deployments fail with error messages in the `apigee-watcher` logs.  | Apigee hybrid only  
Ingressgateway |  [ Expand Istio property replica counts to avoid problems when draining Istio nodes](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio) |  When draining Istio pods some nodes may not drain because they have a replica count of `1`, while `3` or more replicas are required. In order to avoid this, you should set the minimum replica count for each property to at least `3`.  | Apigee hybrid only  
Network configuration |  [ No free IP address space troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/no-free-ip-address-space) |  During Apigee provisioning, if you select a network CIDR range that is not completely free, you may see an error message.  | Apigee and Apigee hybrid  
Network configuration |  [ 503 Service Unavailable error with TARGET_CONNECT_TIMEOUT (Internet and VPC peering targets)](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/vpc-503-target-connect-timeout) | This document describes how to diagnose and correct "503 Service Unavailable" errors with TARGET_CONNECT_TIMEOUT when using internet or VPC peering targets.  | Apigee  
Network configuration |  [ 504 Gateway timeout - Target read timeout](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout) | This document describes how to diagnose and correct "504 Gateway Timeout" errors with a TARGET_READ_TIMEOUT reason.  | Apigee and Apigee hybrid  
Runtime |  [ API requests fail with TARGET CONNECT HOST NOT REACHABLE error](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/target-connect-host-not-reachable) | This document describes how to diagnose and resolve HTTP 503 response status code errors with a "TARGET_CONNECT_HOST_NOT_REACHABLE" reason.  | Apigee and Apigee hybrid  
Runtime |  [ API requests fail with 502 Bad Gateway "Unexpected EOF at target" error](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/unexpected-eof-at-target) | This playbook describes how to diagnose and resolve 502 Bad Gateway Unexpected EOF errors.  | Apigee and Apigee hybrid  
Other |  [ Troubleshooting Apigee hybrid stuck in creating or releasing state](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/troubleshooting-apigee-hybrid) |  This document describes how to reset Apigee hybrid components when they are stuck in a `creating` or `releasing` state.  | Apigee hybrid only  
Other |  [ Immediately delete an Apigee or Apigee hybrid organization](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/delete-org) |  This document outlines how to immediately delete an Apigee or Apigee hybrid organization without retention using the `NO_RETENTION` option.  | Apigee and Apigee hybrid  
Apigee hybrid installation and upgrade | [ Cassandra Pods in CrashLoopBackOff Status](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/cassandra-pod-in-crashloopbackoff-status) |  Cassandra pods are stuck in a CrashLoopBackOff state after installation or upgrade.  | Apigee hybrid only  
Apigee hybrid installation and upgrade | [ Apigee Metrics pods in CrashLoopBackOff status](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-metrics-pods-in-crashloopbackoff) |  Apigee Metrics pods remain in a CrashLoopBackOff state after installation or upgrade.  | Apigee hybrid only  
Apigee hybrid installation and upgrade | [ Apigee ingress gateway pods show 1 of 2 containers running](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-ingressgateway) |  Your `apigee-ingressgateway` pods show only 1 of 2 containers running when you get the pod listing.  | Apigee hybrid only  
Apigee hybrid installation and upgrade | [ UDCA pod error](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/universal-data-collection-agent-pod-error) |  UDCA and Connect Agent pods throw a permission issue error.  | Apigee hybrid only  
Apigee hybrid installation and upgrade | [ Connection resets during TLS handshake for non-SNI clients](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/connection-resets-during-tls-handshake) |  Connection resets are observed during TLS handshake for non-SNI clients.  | Apigee hybrid only  
Apigee hybrid installation and upgrade | [ Insufficient Disk Space in Cassandra](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/insufficient-disk-space-cassandra) |  The Apigee hybrid installation process fails due to insufficient disk space for the Cassandra database.  | Apigee hybrid only  
Apigee hybrid installation and upgrade | [ Insufficient CPU](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/insufficient-cpu) |  When you use `kubectl` to view the pod states, you will see one or more pods in the **CrashLoopBackoff** or **FailedScheduling** state.  | Apigee hybrid only  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


