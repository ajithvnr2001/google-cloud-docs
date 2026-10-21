---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sysdig/
title: Collect Sysdig logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:54:51.930177+00:00
---

# Collect Sysdig logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sysdig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sysdig logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts security event data from Sysdig JSON logs, transforming and mapping the raw log fields into the Google Security Operations UDM format. It handles various fields, including metadata, principal or target information, security result details, and Kubernetes-related context, enriching the data for analysis within Google SecOps. The parser also performs data type conversions, error handling, and conditional logic based on field values to ensure accurate and comprehensive UDM representation.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Sysdig Secure.



## Create an API key for the webhook feed

  1. Go to **Google Cloud console > Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then select **API key**.

  3. Restrict the API key access to the **Google Security Operations API**.




## Option 1

## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Sysdig Logs**.
  5. Select **Webhook** as the **Source type**.
  6. Select **Sysdig** as the **Log type**.
  7. Click **Next**.
  8. Optional: Specify values for the following input parameters:

     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
  9. Click **Next**.

  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.

  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.

  12. Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.

  13. From the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.

  14. Click **Done**.




## Specify the endpoint URL

  1. In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
  2. Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
         
         X-goog-api-key = API_KEY
         X-Webhook-Access-Key = SECRET
         

**Recommendation** : Specify the API key as a header instead of specifying it in the URL.

  3. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
         
         ENDPOINT_URL?key=API_KEY&secret=SECRET
         

Replace the following:

     * `ENDPOINT_URL`: the feed endpoint URL.
     * `API_KEY`: the API key to authenticate to Google SecOps.
     * `SECRET`: the secret key that you generated to authenticate the feed.



## Configure Webhook in Sysdig

  1. Sign in to Sysdig Secure with Admin privileges.
  2. Go to **Profile** > **Settings** > **Event Forwarding**.
  3. Click **+Add Integration** and select **Webhook** from the drop-down.
  4. Specify values for the following input parameters:

     * **Integration Name** : Provide a descriptive name for the webhook (for example, **Google SecOps Webhook**).
     * **Endpoint** : Enter the Webhook `<ENDPOINT_URL>`, followed by `<API_KEY` and `<SECRET>`.
     * **Data to Send** : Select from the drop-down the types of Sysdig data that should be forwarded.

**Note:** Don't select allow insecure connections.
     * Test the integration, then toggle **Enabled** to activate it.

     * Click **Save**.




## Option 2

### Forward data directly to Google SecOps

  1. Sign in to Sysdig Secure using your administrator credentials.
  2. Go to **Settings** > **Event Forwarding**.
  3. Click **+Add Integration** and select **Google Chronicle** from the drop-down.
  4. Specify values for the following input parameters: 
     * **Integration Name** : Provide a descriptive name for the integration (for example, **Google SecOps Integration**).
     * **Customer ID** : The Google Customer ID associated with your Google Cloud account. (In **Google SecOps** , find this in **Settings** > **Profile**).
     * **Namespace** : Optional: Use as a tag to identify the appropriate data domain for indexing and enrichment.
     * **JSON Credentials** : Upload your Google SecOps JSON credentials.
     * **Region** : Select your region, such as US, Europe, or Asia.
     * **Data to Send** : Select the types of Sysdig data that should be forwarded from the drop-down.
     * Test the integration, then toggle **Enabled** to activate it.
     * Click **Save**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`agentId` | `read_only_udm.metadata.product_deployment_id` | The value of `agentId` from the raw log is directly mapped to this UDM field.  
`category` | `read_only_udm.security_result.category_details` | The value of `category` from the raw log is directly mapped to this UDM field.  
`content.fields.container.id` | `read_only_udm.target.asset.asset_id` | The value of `content.fields.container.id` from the raw log is prepended with "container_id:" and mapped to this UDM field. Used if `containerId` is empty.  
`content.fields.container.image.repository` | `read_only_udm.target.file.full_path` | The value of `content.fields.container.image.repository` from the raw log is directly mapped to this UDM field.  
`content.fields.container.image.tag` | `read_only_udm.metadata.ingestion_labels.value` where key is `tag` | The value of `content.fields.container.image.tag` from the raw log is directly mapped to this UDM field.  
`content.fields.evt.res` | `read_only_udm.metadata.ingestion_labels.value` where key is `evt_res` | The value of `content.fields.evt.res` from the raw log is directly mapped to this UDM field.  
`content.fields.evt.type` | `read_only_udm.metadata.event_type` | The value of `content.fields.evt.type` from the raw log is directly mapped to this UDM field.  
`content.fields.falco.rule` | `read_only_udm.security_result.rule_name` | The value of `content.fields.falco.rule` from the raw log is directly mapped to this UDM field. Used if `content.ruleName` is empty.  
`content.fields.group.gid` | `read_only_udm.target.group.product_object_id` | The value of `content.fields.group.gid` from the raw log is directly mapped to this UDM field.  
`content.fields.group.name` | `read_only_udm.target.group.group_display_name` | The value of `content.fields.group.name` from the raw log is directly mapped to this UDM field.  
`content.fields.proc.cmdline` | `read_only_udm.target.process.command_line` | The value of `content.fields.proc.cmdline` from the raw log is directly mapped to this UDM field.  
`content.fields.proc.pcmdline` | `read_only_udm.target.process.parent_process.command_line` | The value of `content.fields.proc.pcmdline` from the raw log is directly mapped to this UDM field.  
`content.fields.proc.pid` | `read_only_udm.target.process.pid` | The value of `content.fields.proc.pid` from the raw log is directly mapped to this UDM field.  
`content.fields.proc.ppid` | `read_only_udm.target.process.parent_process.pid` | The value of `content.fields.proc.ppid` from the raw log is directly mapped to this UDM field.  
`content.fields.proc.sid` | `read_only_udm.metadata.ingestion_labels.value` where key is `sid` | The value of `content.fields.proc.sid` from the raw log is directly mapped to this UDM field.  
`content.fields.user.loginname` | `read_only_udm.principal.user.user_display_name` | The value of `content.fields.user.loginname` from the raw log is directly mapped to this UDM field.  
`content.fields.user.uid` | `read_only_udm.principal.user.userid` | The value of `content.fields.user.uid` from the raw log is directly mapped to this UDM field.  
`content.output` | `read_only_udm.additional.fields.value.string_value` where key is `content_output` | The value of `content.output` from the raw log is directly mapped to this UDM field.  
`content.policyId` | `read_only_udm.security_result.rule_id` | The value of `content.policyId` from the raw log is directly mapped to this UDM field.  
`content.policyOrigin` | `read_only_udm.additional.fields.value.string_value` where key is `content_policyOrigin` | The value of `content.policyOrigin` from the raw log is directly mapped to this UDM field.  
`content.policyVersion` | `read_only_udm.additional.fields.value.string_value` where key is `content_policyVersion` | The value of `content.policyVersion` from the raw log is directly mapped to this UDM field.  
`content.ruleName` | `read_only_udm.security_result.rule_name` | The value of `content.ruleName` from the raw log is directly mapped to this UDM field.  
`content.ruleTags` | `read_only_udm.security_result.rule_labels` | The values in the `content.ruleTags` array from the raw log are mapped to this UDM field, with keys generated dynamically as "ruletag_index".  
`content.ruleType` | `read_only_udm.additional.fields.value.string_value` where key is `content_ruleType` | The value of `content.ruleType` from the raw log is directly mapped to this UDM field.  
`containerId` | `read_only_udm.target.asset.asset_id` | The value of `containerId` from the raw log is prepended with "container_id:" and mapped to this UDM field.  
`description` | `read_only_udm.metadata.description` | The value of `description` from the raw log is directly mapped to this UDM field.  
`id` | `read_only_udm.metadata.product_log_id` | The value of `id` from the raw log is directly mapped to this UDM field.  
`labels.container.label.io.kubernetes.container.name` | `read_only_udm.additional.fields.value.string_value` where key is `container_name` | The value of `labels.container.label.io.kubernetes.container.name` from the raw log is directly mapped to this UDM field.  
`labels.container.label.io.kubernetes.pod.name` | `read_only_udm.additional.fields.value.string_value` where key is `pod_name` | The value of `labels.container.label.io.kubernetes.pod.name` from the raw log is directly mapped to this UDM field. Used if `labels.kubernetes.pod.name` is empty.  
`labels.container.label.io.kubernetes.pod.namespace` | `read_only_udm.principal.namespace` | The value of `labels.container.label.io.kubernetes.pod.namespace` from the raw log is directly mapped to this UDM field. Used if `labels.kubernetes.namespace.name` is empty.  
`labels.aws.instanceId` | `read_only_udm.target.resource.product_object_id` | The value of `labels.aws.instanceId` from the raw log is directly mapped to this UDM field.  
`labels.aws.region` | `read_only_udm.target.resource.attribute.cloud.availability_zone` | The value of `labels.aws.region` from the raw log is directly mapped to this UDM field.  
`labels.host.hostName` | `read_only_udm.principal.ip` OR `read_only_udm.principal.hostname` | If the value contains "ip", it's parsed as an IP address and mapped to `principal.ip`. Otherwise, it's mapped to `principal.hostname`.  
`labels.host.mac` | `read_only_udm.principal.mac` | The value of `labels.host.mac` from the raw log is directly mapped to this UDM field. Used if `machineId` is empty.  
`labels.kubernetes.cluster.name` | `read_only_udm.additional.fields.value.string_value` where key is `kubernetes_cluster_name` | The value of `labels.kubernetes.cluster.name` from the raw log is directly mapped to this UDM field.  
`labels.kubernetes.deployment.name` | `read_only_udm.additional.fields.value.string_value` where key is `kubernetes_deployment_name` | The value of `labels.kubernetes.deployment.name` from the raw log is directly mapped to this UDM field.  
`labels.kubernetes.namespace.name` | `read_only_udm.principal.namespace` | The value of `labels.kubernetes.namespace.name` from the raw log is directly mapped to this UDM field.  
`labels.kubernetes.node.name` | `read_only_udm.additional.fields.value.string_value` where key is `kubernetes_node_name` | The value of `labels.kubernetes.node.name` from the raw log is directly mapped to this UDM field.  
`labels.kubernetes.pod.name` | `read_only_udm.additional.fields.value.string_value` where key is `pod_name` | The value of `labels.kubernetes.pod.name` from the raw log is directly mapped to this UDM field.  
`labels.kubernetes.service.name` | `read_only_udm.additional.fields.value.string_value` where key is `kubernetes_service_name` | The value of `labels.kubernetes.service.name` from the raw log is directly mapped to this UDM field.  
`machineId` | `read_only_udm.principal.mac` | The value of `machineId` from the raw log is directly mapped to this UDM field.  
`name` | `read_only_udm.security_result.summary` | The value of `name` from the raw log is directly mapped to this UDM field.  
`severity` | `read_only_udm.security_result.severity` | The value of `severity` from the raw log is mapped to a string value based on these ranges: <4 = HIGH, >3 and <6 = MEDIUM, 6 = LOW, 7 = INFORMATIONAL.  
`source` | `read_only_udm.security_result.description` | The value of `source` from the raw log is directly mapped to this UDM field.  
`timestampRFC3339Nano` | `read_only_udm.metadata.event_timestamp` | The value of `timestampRFC3339Nano` from the raw log is parsed as a timestamp and mapped to this UDM field.  
`type` | `read_only_udm.metadata.product_event_type` | The value of `type` from the raw log is directly mapped to this UDM field.  
(Parser Logic) | `read_only_udm.metadata.product_name` | Hardcoded to "SYSDIG".  
(Parser Logic) | `read_only_udm.metadata.vendor_name` | Hardcoded to "SYSDIG".  
(Parser Logic) | `read_only_udm.metadata.event_type` | Set to "PROCESS_UNCATEGORIZED" by default, or "GENERIC_EVENT" if `labels.host.hostName` is empty.  
(Parser Logic) | `read_only_udm.metadata.log_type` | Hardcoded to "SYSDIG".  
(Parser Logic) | `read_only_udm.target.resource.resource_type` | Set to "CLOUD_PROJECT" if `labels.aws.instanceId` exists.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sysdig-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
