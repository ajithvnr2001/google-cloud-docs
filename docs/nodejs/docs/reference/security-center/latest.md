---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/
title: Security Command Center API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:13.683799+00:00
---

# Security Command Center API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Security Command Center API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.0.1  9.5.0  9.4.0  9.3.0  8.12.0  8.11.0  8.10.0  8.9.0  8.7.0  8.5.0  8.4.0  8.3.0  8.1.0  8.0.0  7.4.0  7.2.1  7.0.0  6.3.1  6.2.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.1  5.4.1  5.3.5 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/security-center.svg)](https://www.npmjs.org/package/@google-cloud/security-center)

Security Command Center API client for Node.js

> Node.js idiomatic client for [Cloud Security Command Center][product-docs].

[Cloud Security Command Center](https://cloud.google.com/security-command-center/docs/) helps security teams gather data, identify threats, and act on them before they result in business damage or loss. It offers deep insight into application and data risk so that you can quickly mitigate threats to your cloud resources and evaluate overall health. With Cloud Security Command Center, you can view and monitor an inventory of your cloud assets, scan storage systems for sensitive data, detect common web vulnerabilities, and review access rights to your critical resources, all from a single, centralized dashboard.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/CHANGELOG.md).

  * [Security Command Center API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/securitycenter/latest)
  * [Security Command Center API Documentation](https://cloud.google.com/security-command-center/docs/reference/rest)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Versioning

  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Security Command Center API API](https://console.cloud.google.com/flows/enableapi?apiid=securitycenter.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/security-center
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
batch create resource value configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.batch_create_resource_value_configs.js)  
bulk mute findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.bulk_mute_findings.js)  
create big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_big_query_export.js)  
create event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_event_threat_detection_custom_module.js)  
create finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_finding.js)  
create mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_mute_config.js)  
create notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_notification_config.js)  
create security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_security_health_analytics_custom_module.js)  
create source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.create_source.js)  
delete big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.delete_big_query_export.js)  
delete event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.delete_event_threat_detection_custom_module.js)  
delete mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.delete_mute_config.js)  
delete notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.delete_notification_config.js)  
delete resource value config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.delete_resource_value_config.js)  
delete security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.delete_security_health_analytics_custom_module.js)  
get big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_big_query_export.js)  
get effective event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_effective_event_threat_detection_custom_module.js)  
get effective security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_effective_security_health_analytics_custom_module.js)  
get event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_event_threat_detection_custom_module.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_iam_policy.js)  
get mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_mute_config.js)  
get notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_notification_config.js)  
get organization settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_organization_settings.js)  
get resource value config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_resource_value_config.js)  
get security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_security_health_analytics_custom_module.js)  
get simulation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_simulation.js)  
get source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_source.js)  
get valued resource | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.get_valued_resource.js)  
group assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.group_assets.js)  
group findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.group_findings.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_assets.js)  
list attack paths | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_attack_paths.js)  
list big query exports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_big_query_exports.js)  
list descendant event threat detection custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_descendant_event_threat_detection_custom_modules.js)  
list descendant security health analytics custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_descendant_security_health_analytics_custom_modules.js)  
list effective event threat detection custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_effective_event_threat_detection_custom_modules.js)  
list effective security health analytics custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_effective_security_health_analytics_custom_modules.js)  
list event threat detection custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_event_threat_detection_custom_modules.js)  
list findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_findings.js)  
list mute configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_mute_configs.js)  
list notification configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_notification_configs.js)  
list resource value configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_resource_value_configs.js)  
list security health analytics custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_security_health_analytics_custom_modules.js)  
list sources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_sources.js)  
list valued resources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.list_valued_resources.js)  
run asset discovery | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.run_asset_discovery.js)  
set finding state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.set_finding_state.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.set_iam_policy.js)  
set mute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.set_mute.js)  
simulate security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.simulate_security_health_analytics_custom_module.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.test_iam_permissions.js)  
update big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_big_query_export.js)  
update event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_event_threat_detection_custom_module.js)  
update external system | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_external_system.js)  
update finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_finding.js)  
update mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_mute_config.js)  
update notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_notification_config.js)  
update organization settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_organization_settings.js)  
update resource value config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_resource_value_config.js)  
update security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_security_health_analytics_custom_module.js)  
update security marks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_security_marks.js)  
update source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.update_source.js)  
validate event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1/security_center.validate_event_threat_detection_custom_module.js)  
create finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.create_finding.js)  
create source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.create_source.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.get_iam_policy.js)  
get organization settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.get_organization_settings.js)  
get source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.get_source.js)  
group assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.group_assets.js)  
group findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.group_findings.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.list_assets.js)  
list findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.list_findings.js)  
list sources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.list_sources.js)  
run asset discovery | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.run_asset_discovery.js)  
set finding state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.set_finding_state.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.test_iam_permissions.js)  
update finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.update_finding.js)  
update organization settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.update_organization_settings.js)  
update security marks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.update_security_marks.js)  
update source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1beta1/security_center.update_source.js)  
create finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.create_finding.js)  
create notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.create_notification_config.js)  
create source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.create_source.js)  
delete notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.delete_notification_config.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.get_iam_policy.js)  
get notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.get_notification_config.js)  
get organization settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.get_organization_settings.js)  
get source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.get_source.js)  
group assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.group_assets.js)  
group findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.group_findings.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.list_assets.js)  
list findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.list_findings.js)  
list notification configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.list_notification_configs.js)  
list sources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.list_sources.js)  
run asset discovery | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.run_asset_discovery.js)  
set finding state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.set_finding_state.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.test_iam_permissions.js)  
update finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.update_finding.js)  
update notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.update_notification_config.js)  
update organization settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.update_organization_settings.js)  
update security marks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.update_security_marks.js)  
update source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v1p1beta1/security_center.update_source.js)  
batch create resource value configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.batch_create_resource_value_configs.js)  
bulk mute findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.bulk_mute_findings.js)  
create big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.create_big_query_export.js)  
create finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.create_finding.js)  
create mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.create_mute_config.js)  
create notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.create_notification_config.js)  
create source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.create_source.js)  
delete big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.delete_big_query_export.js)  
delete mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.delete_mute_config.js)  
delete notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.delete_notification_config.js)  
delete resource value config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.delete_resource_value_config.js)  
get big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_big_query_export.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_iam_policy.js)  
get mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_mute_config.js)  
get notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_notification_config.js)  
get resource value config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_resource_value_config.js)  
get simulation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_simulation.js)  
get source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_source.js)  
get valued resource | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.get_valued_resource.js)  
group findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.group_findings.js)  
list attack paths | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_attack_paths.js)  
list big query exports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_big_query_exports.js)  
list findings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_findings.js)  
list mute configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_mute_configs.js)  
list notification configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_notification_configs.js)  
list resource value configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_resource_value_configs.js)  
list sources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_sources.js)  
list valued resources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.list_valued_resources.js)  
set finding state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.set_finding_state.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.set_iam_policy.js)  
set mute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.set_mute.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.test_iam_permissions.js)  
update big query export | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_big_query_export.js)  
update external system | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_external_system.js)  
update finding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_finding.js)  
update mute config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_mute_config.js)  
update notification config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_notification_config.js)  
update resource value config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_resource_value_config.js)  
update security marks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_security_marks.js)  
update source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycenter/samples/generated/v2/security_center.update_source.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/security-center@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
