---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare/
title: Collect Cloudflare logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:01:32.258947+00:00
---

# Collect Cloudflare logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloudflare logs

**Parser Version:** 24.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cloudflare logs to Google Security Operations using either Webhook (HTTP destination) or Google Cloud Storage. Cloudflare produces operational data in the form of logs for DNS, HTTP requests, Firewall events, Audit, Zero Trust, and CASB. This integration allows you to send these logs to Google SecOps for analysis and monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Cloudflare Enterprise account with Logpush enabled.
  * For Webhook method: Privileged access to Google Cloud console.
  * For GCS method: Privileged access to Google Cloud Storage.



## Method 1: Configure Cloudflare logs export using Webhook (HTTP destination)

This method lets you stream Cloudflare logs directly to Google Security Operations without intermediate storage, reducing costs and simplifying configuration.

### Configure a Webhook feed in Google SecOps

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cloudflare Webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Cloudflare** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : `\n`.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. **Copy** and **save** the secret key as you cannot view this secret again.
  13. Go to the **Details** tab.
  14. **Copy** the feed endpoint URL from the **Endpoint Information** field.
  15. Click **Done**.



### Create an API key for the Webhook feed

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials** > **API key**.
  4. Click **Edit API key**.
  5. Under **API restrictions** , select **Restrict key**.
  6. In the **Select APIs** dropdown, search for and select **Chronicle API**.
  7. Click **Save**.
  8. **Copy** the API key value.



### Configure Cloudflare Logpush HTTP destination

  1. Log in to the **Cloudflare dashboard**.
  2. Select the **Enterprise account** or **domain** you want to use with Logpush.
  3. Go to **Analytics & Logs** > **Logs**.
  4. Click **Create a Logpush job**.
  5. In **Select a destination** , choose **HTTP destination**.
  6. Enter the HTTP endpoint URL with authentication parameters:
         
         <ENDPOINT_URL>?header_X-goog-api-key=<API_KEY>&header_X-Webhook-Access-Key=<SECRET_KEY>
         

Replace the following:

     * `<ENDPOINT_URL>`: the feed endpoint URL from Google SecOps.
     * `<API_KEY>`: the API key from Google Cloud console (URL-encoded if it contains special characters).
     * `<SECRET_KEY>`: the secret key from the Webhook feed (URL-encoded if it contains special characters).
**Note:** The `header_` prefix tells Cloudflare to send these as HTTP headers rather than URL parameters.
  7. Click **Continue**.

  8. Select the dataset to push (for example, **HTTP requests** , **DNS logs** , **Firewall events** , **Audit logs** , **Zero Trust logs** , **CASB findings**).

  9. Configure your Logpush job:

     * Enter the **Job name**.
     * Under **If logs match** , optionally configure filters.
     * In **Send the following fields** , select the fields to include.
     * Choose the timestamp format: 
       * **RFC 3339** (recommended for Google SecOps)
       * **Unix** (seconds since epoch)
       * **UnixNano** (nanoseconds since epoch)
     * Configure sampling rate if needed.
  10. Click **Submit** to create the Logpush job.




### Verify the Webhook integration

After configuration, logs should appear in Google SecOps within minutes. To verify:

  1. Go to **Investigation** > **SIEM Search**.
  2. Search for logs with your configured ingestion label.
  3. Confirm Cloudflare logs are being parsed correctly.



## Method 2: Configure Cloudflare logs export using Google Cloud Storage

### Create a Google Cloud Storage bucket

  1. Sign in to the **Google Cloud console**.
  2. Go to the **Cloud Storage** > **Buckets** page.
  3. Click **Create**.
  4. On the **Create a bucket** page, enter your bucket information: 
     * **Name** : Enter a unique name that meets the bucket name requirements (for example, `cloudflare-data`).
     * **Location type** : Select a location type and region.
     * To enable hierarchical namespace, click the expander arrow to expand **Optimize for file oriented and data-intensive workloads** , and then select **Enable Hierarchical namespace on this bucket**.
  5. Click **Create**.



### Grant Cloudflare permissions to the bucket

  1. In the **Cloud Storage console** , select the GCS bucket (for example, `cloudflare-data`).
  2. Click the **Permissions** tab.
  3. Click **Grant access**.
  4. In the **Add principals** field, enter `logpush@cloudflare-data.iam.gserviceaccount.com`.
  5. In the **Assign roles** dropdown, select **Storage Object Admin**.
  6. Click **Save**.



### Configure Cloudflare Logpush to Cloud Storage

  1. Log in to the **Cloudflare dashboard**.
  2. Select the **Enterprise account** or **domain** you want to use with Logpush.
  3. Go to **Analytics & Logs** > **Logs**.
  4. Click **Create a Logpush job**.
  5. In **Select a destination** , choose **Google Cloud Storage**.
  6. Enter your GCS bucket path (for example, `cloudflare-data/logs/`).
  7. Click **Continue**.

**Note:** To prove ownership, Cloudflare sends a file to your designated destination. Find the token in the ownership challenge file and paste it into the Cloudflare dashboard to verify access.
  8. Enter the **Ownership Token** and click **Continue**.

  9. Select the dataset to push to storage.

  10. Configure your Logpush job:

     * Enter the **Job name**.
     * Under **If logs match** , you can select the events to include and/or remove from your logs.
     * In **Send the following fields** , choose which fields to push.
     * Choose the timestamp format: 
       * **RFC 3339** (recommended for Google SecOps)
       * **Unix** (seconds since epoch)
       * **UnixNano** (nanoseconds since epoch)
     * Configure sampling rate if needed.
  11. Click **Submit**.




### Configure a feed in Google SecOps to ingest Cloudflare logs from GCS

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cloudflare GCS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cloudflare** as the **Log type**.
  7. Click **Get Service Account**.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : Google Cloud Storage bucket URL in `gs://my-bucket/<value>/` format.

**Note:** The URL must end with a trailing forward slash (/).
     * **Source deletion option** : Select deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select **Delete transferred files** or **Delete transferred files and empty directories** , ensure the Google SecOps service account has **Storage Object Admin** role on the bucket.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : the label to be applied to the events from this feed.

  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage** > **Buckets**.
  2. Click on the bucket name (for example, `cloudflare-data`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. In the **Add principals** field, paste the Google SecOps service account email.
  6. In the **Assign roles** dropdown, select **Storage Object Viewer**.
  7. Click **Save**.

**Note:** If you plan to use the deletion option **Delete transferred files** or **Delete transferred files and empty directories** , grant **Storage Object Admin** role instead of Storage Object Viewer.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`ClientIP` | `read_only_udm.principal.asset.ip`, `read_only_udm.principal.ip` | The value is taken from the ClientIP field.  
`ClientRequestHost` | `read_only_udm.target.asset.hostname`, `read_only_udm.target.hostname` | The value is taken from the ClientRequestHost field.  
`ClientRequestMethod` | `read_only_udm.network.http.method` | The value is taken from the ClientRequestMethod field.  
`ClientRequestURI` | `read_only_udm.target.url` | The value is taken from the ClientRequestURI field. If the ClientRequestHost field is not empty, the value is concatenated with the ClientRequestHost field.  
`ClientSrcPort` | `read_only_udm.principal.port` | The value is taken from the ClientSrcPort field.  
`ClientRequestUserAgent` | `read_only_udm.network.http.user_agent` | The value is taken from the ClientRequestUserAgent field.  
`ClientSSLCipher` | `read_only_udm.network.tls.cipher` | The value is taken from the ClientSSLCipher field.  
`ClientSSLProtocol` | `read_only_udm.network.tls.version` | The value is taken from the ClientSSLProtocol field.  
`Country` | `read_only_udm.target.location.country_or_region` | The value is taken from the Country field.  
`CreatedAt` | `read_only_udm.metadata.event_timestamp` | The value is taken from the CreatedAt field.  
`Datetime` | `read_only_udm.metadata.event_timestamp` | The value is taken from the Datetime field.  
`DestinationIP` | `read_only_udm.target.asset.ip`, `read_only_udm.target.ip` | The value is taken from the DestinationIP field.  
`DestinationPort` | `read_only_udm.target.port` | The value is taken from the DestinationPort field.  
`DeviceID` | `read_only_udm.principal.asset_id` | The value is taken from the DeviceID field and is prefixed with "Cloudflare:".  
`DeviceName` | `read_only_udm.principal.asset.hostname`, `read_only_udm.principal.hostname` | The value is taken from the DeviceName field.  
`DstIP` | `read_only_udm.target.asset.ip`, `read_only_udm.target.ip` | The value is taken from the DstIP field.  
`DstPort` | `read_only_udm.target.port` | The value is taken from the DstPort field.  
`EdgeResponseBytes` | `read_only_udm.network.received_bytes` | The value is taken from the EdgeResponseBytes field.  
`EdgeResponseStatus` | `read_only_udm.network.http.response_code` | The value is taken from the EdgeResponseStatus field.  
`EdgeServerIP` | `read_only_udm.target.asset.ip`, `read_only_udm.target.ip` | The value is taken from the EdgeServerIP field.  
`Email` | `read_only_udm.principal.user.email_addresses`, `read_only_udm.target.user.email_addresses` | The value is taken from the Email field.  
`FirewallMatchesActions` | `read_only_udm.security_result.action` | The value is set to "ALLOW" if the FirewallMatchesAction field is "allow", "Allow", "ALLOW", "skip", "SKIP", or "Skip", "ALLOW_WITH_MODIFICATION" if the FirewallMatchesAction field is "challengeSolved" or "jschallengeSolved", "BLOCK" if the FirewallMatchesAction field is "drop" or "block", "UNKNOWN_ACTION" if the FirewallMatchesAction field is not empty.  
`FirewallMatchesRuleIDs` | `read_only_udm.security_result.rule_id` | The value is taken from the FirewallMatchesRuleIDs field.  
`FirewallMatchesSources` | `read_only_udm.security_result.rule_name` | The value is taken from the FirewallMatchesSources field.  
`HTTPMethod` | `read_only_udm.network.http.method` | The value is taken from the HTTPMethod field.  
`HTTPHost` | `read_only_udm.target.hostname` | The value is taken from the HTTPHost field.  
`HTTPVersion` | `read_only_udm.network.application_protocol` | The value is taken from the HTTPVersion field. If the value contains "HTTP", it is replaced with "HTTP".  
`IPAddress` | `read_only_udm.target.asset.ip`, `read_only_udm.target.ip` | The value is taken from the IPAddress field.  
`IsIsolated` | `read_only_udm.about.labels`, `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the IsIsolated field and is converted to a string.  
`Location` | `read_only_udm.principal.location.name` | The value is taken from the Location field.  
`OriginIP` | `read_only_udm.intermediary.ip`, `read_only_udm.target.asset.ip`, `read_only_udm.target.ip` | The value is taken from the OriginIP field.  
`OriginPort` | `read_only_udm.target.port` | The value is taken from the OriginPort field.  
`OwnerID` | `read_only_udm.target.user.product_object_id` | The value is taken from the OwnerID field.  
`Policy` | `read_only_udm.security_result.rule_name` | The value is taken from the Policy field.  
`PolicyID` | `read_only_udm.security_result.rule_id` | The value is taken from the PolicyID field.  
`PolicyName` | `read_only_udm.security_result.rule_name` | The value is taken from the PolicyName field.  
`Protocol` | `read_only_udm.network.ip_protocol` | The value is taken from the Protocol field and is converted to uppercase.  
`QueryCategoryIDs` | `read_only_udm.security_result.about.labels`, `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the QueryCategoryIDs field.  
`QueryName` | `read_only_udm.network.dns.questions.name` | The value is taken from the QueryName field.  
`QueryNameReversed` | `read_only_udm.network.dns.questions.name` | The value is taken from the QueryNameReversed field.  
`QuerySize` | `read_only_udm.network.sent_bytes` | The value is taken from the QuerySize field.  
`QueryType` | `read_only_udm.network.dns.questions.type` | The value is taken from the QueryType field. If the value is one of the known DNS record types, it is mapped to its corresponding numeric value. Otherwise, the value is converted to a string.  
`RData` | `read_only_udm.network.dns.answers` | The value is taken from the RData field. The type field is converted to an unsigned integer.  
`RayID` | `read_only_udm.metadata.product_log_id` | The value is taken from the RayID field.  
`Referer` | `read_only_udm.network.http.referral_url` | The value is taken from the Referer field.  
`RequestID` | `read_only_udm.metadata.product_log_id` | The value is taken from the RequestID field.  
`ResolverDecision` | `read_only_udm.security_result.summary` | The value is taken from the ResolverDecision field.  
`ResourceID` | `read_only_udm.target.resource.id`, `read_only_udm.target.resource.product_object_id` | The value is taken from the ResourceID field.  
`ResourceType` | `read_only_udm.target.resource.resource_subtype` | The value is taken from the ResourceType field.  
`SNI` | `read_only_udm.network.tls.client.server_name` | The value is taken from the SNI field.  
`SecurityAction` | `read_only_udm.security_result.action` | The value is set to "ALLOW" if the SecurityAction field is empty or the sec_action field is empty, "ALLOW_WITH_MODIFICATION" if the SecurityAction field is "challengeSolved" or "jschallengeSolved", "BLOCK" if the SecurityAction field is "drop" or "block".  
`SecurityLevel` | `read_only_udm.security_result.severity` | The value is taken from the SecurityLevel field and is mapped to its corresponding UDM severity value.  
`SessionID` | `read_only_udm.network.session_id` | The value is taken from the SessionID field.  
`SessionStartTime` | `read_only_udm.metadata.event_timestamp` | The value is taken from the SessionStartTime field.  
`SourceIP` | `read_only_udm.principal.asset.ip`, `read_only_udm.principal.ip`, `read_only_udm.src.asset.ip`, `read_only_udm.src.ip` | The value is taken from the SourceIP field.  
`SourcePort` | `read_only_udm.principal.port`, `read_only_udm.src.port` | The value is taken from the SourcePort field.  
`SrcIP` | `read_only_udm.principal.asset.ip`, `read_only_udm.principal.ip` | The value is taken from the SrcIP field.  
`SrcPort` | `read_only_udm.principal.port` | The value is taken from the SrcPort field.  
`TemporaryAccessDuration` | `read_only_udm.network.session_duration.seconds` | The value is taken from the TemporaryAccessDuration field.  
`Timestamp` | `read_only_udm.metadata.event_timestamp` | The value is taken from the Timestamp field.  
`Transport` | `read_only_udm.network.ip_protocol` | The value is taken from the Transport field and is converted to uppercase.  
`URL` | `read_only_udm.target.url` | The value is taken from the URL field.  
`UserAgent` | `read_only_udm.network.http.user_agent` | The value is taken from the UserAgent field.  
`UserID` | `read_only_udm.principal.user.product_object_id` | The value is taken from the UserID field.  
`UserUID` | `read_only_udm.target.user.product_object_id` | The value is taken from the UserUID field.  
`VirtualNetworkID` | `read_only_udm.principal.resource.product_object_id` | The value is taken from the VirtualNetworkID field.  
`WAFAction` | `read_only_udm.security_result.about.labels`, `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFAction field.  
`WAFAttackScore` | `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFAttackScore field.  
`WAFFlags` | `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFFlags field.  
`WAFProfile` | `read_only_udm.security_result.about.labels`, `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFProfile field.  
`WAFRCEAttackScore` | `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFRCEAttackScore field.  
`WAFRuleID` | `read_only_udm.security_result.about.labels`, `read_only_udm.security_result.about.resource.attribute.labels`, `read_only_udm.security_result.threat_id` | The value is taken from the WAFRuleID field.  
`WAFRuleMessage` | `read_only_udm.security_result.rule_name`, `read_only_udm.security_result.threat_name` | The value is taken from the WAFRuleMessage field.  
`WAFSQLiAttackScore` | `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFSQLiAttackScore field.  
`WAFXSSAttackScore` | `read_only_udm.security_result.about.resource.attribute.labels` | The value is taken from the WAFXSSAttackScore field.  
`ZoneID` | `read_only_udm.additional.fields` | The value is taken from the ZoneID field.  
| `read_only_udm.metadata.log_type` | The value is set to "CLOUDFLARE".  
| `read_only_udm.metadata.product_name` | The value is set to "Cloudflare Gateway DNS" if the log is a DNS log, "Cloudflare Gateway HTTP" if the log is a Gateway HTTP log, "Cloudflare Audit" if the log is an Audit log, or "Web Application Firewall" otherwise.  
| `read_only_udm.metadata.vendor_name` | The value is set to "Cloudflare".  
| `read_only_udm.network.application_protocol` | The value is set to "DNS" if the log is a DNS log, "HTTP" if the HTTPVersion field contains "HTTP", or the value of the Protocol field converted to uppercase if the Protocol field is not empty and is not "tls" or "TLS".  
| `read_only_udm.network.direction` | The value is set to "OUTBOUND" if the EgressIP field is not empty.  
| `read_only_udm.network.http.parsed_user_agent` | The value is taken from the UserAgent or ClientRequestUserAgent field and is parsed using the parseduseragent filter.  
| `read_only_udm.extensions.auth.type` | The value is set to "MACHINE" if the Action field is "login" or "logout".  
| `read_only_udm.metadata.event_type` | The value is set to "NETWORK_DNS" if the log is a DNS log, "NETWORK_CONNECTION" if the log is a Gateway HTTP log, "USER_RESOURCE_ACCESS" if the log is an Audit log and the ActorIP and ActorEmail fields are empty, "USER_RESOURCE_UPDATE_CONTENT" if the log is an Audit log and the ResourceType and newvalue fields are not empty, "USER_LOGIN" if the Action field is "login", "USER_LOGOUT" if the Action field is "logout", "USER_RESOURCE_ACCESS" if the Email field is not empty and matches the email address format, or "NETWORK_CONNECTION" if the EgressIP and SourceIP fields are not empty or the OriginIP and SourceIP fields are not empty.  
| `read_only_udm.target.file.mime_type` | The value is taken from the EdgeResponseContentType field.  
| `read_only_udm.target.location.country_or_region` | The value is taken from the Country field.  
| `read_only_udm.target.resource.id` | The value is taken from the AccountID field or the ResourceID field.  
| `read_only_udm.target.resource.product_object_id` | The value is taken from the AccountID field, the AppUUID field, or the ResourceID field.  
| `read_only_udm.target.user.product_object_id` | The value is taken from the OwnerID field or the UserUID field.  
`ConnectionCloseReason` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`BytesReceived` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`VirtualNetworkID` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`VirtualNetworkName` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`ApplicationIDs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationStatuses` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationNames` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationName_index` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CategoryIDs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ForensicCopyStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Quarantined` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UntrustedCertificateAction` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RegistrationID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HTTPVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationNames` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`BlockedFileReason` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`CategoryNames` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`DestinationIPCountryCode` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`SourceIPCountryCode` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`HTTPStatusCode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`SourceIPContinentCode` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`DestinationIPContinentCode` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`SourceInternalIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`ActionInfo` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`ActorType` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`ActorEmail` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`CacheReserveUsed` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CacheTieredFill` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgeCFConnectingO2O` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgePathingOp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgePathingSrc` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgePathingStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgeResponseBodyBytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgeResponseCompressionRatio` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OriginResponseDurationMs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OriginResponseHeaderReceiveDurationMs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientRequestScheme` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientASN` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Ref` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EdgeColoCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientASNDescription` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientIPClass` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientRequestHost` | `event.idm.read_only_udm.src.hostname` | Mapped from changelog  
`ClientRequestPath` | `event.idm.read_only_udm.src.file.full_path` | Mapped from changelog  
`ClientUserAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`Description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`Kind` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`RayID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`client_request_proto` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`version` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`log.Application", "log.ClientAsn", "log.ColoCode", "log.OriginProto", "log.Status" and "log.ProxyProtocol` | `additional.fields` | Mapped from changelog  
`log.ClientBytes` | `network.sent_bytes` | Mapped from changelog  
`log.ClientCountry` | `principal.location.country_or_region` | Mapped from changelog  
`log.ClientIP` | `principal.ip and principal.asset.ip` | Mapped from changelog  
`log.ClientMatchedIpFirewall` | `security_result.detection_fields` | Mapped from changelog  
`log.ClientPort` | `principal.port` | Mapped from changelog  
`log.ClientProto` | `network.ip_protocol` | Mapped from changelog  
`log.Event` | `security_result.detection_fields` | Mapped from changelog  
`log.OriginBytes` | `security_result.detection_fields` | Mapped from changelog  
`log.OriginIP` | `intermediary.ip` | Mapped from changelog  
`log.OriginPort` | `intermediary.port` | Mapped from changelog  
`log.IpFirewall` | `security_result.detection_fields` | Mapped from changelog  
`log.Timestamp` | `metadata.event_timestamp` | Mapped from changelog  
`log.ConnectTimestamp` | `security_result.detection_fields` | Mapped from changelog  
`log.DisconnectTimestamp` | `security_result.detection_fields` | Mapped from changelog  
`AppDomain` | `target.administrative_domain` | Mapped from changelog  
`Connection` | `target.resource.attribute.labels` | Mapped from changelog  
`metadata.event_type` | `USER_UNCATEGORIZED` | Mapped from changelog  
`IPSourceAddress` | `principal.ip` | Mapped from changelog  
`IPDestinationAddress` | `target.ip` | Mapped from changelog  
`IPProtocol` | `network.ip_protocol` | Mapped from changelog  
`IPDestinationSubnet", "DestinationASNNAME", "DestinationASN", and "DestinationGeoHash` | `target.resource.attribute.labels` | Mapped from changelog  
`IPSourceSubnet", "SourceASNNAME", "SourceASN", and "SourceGeoHash` | `principal.resource.attribute.labels` | Mapped from changelog  
`SourceCountry` | `principal.location.country_or_region` | Mapped from changelog  
`DestinationCountry` | `target.location.country_or_region` | Mapped from changelog  
`ColoCity", "ColoCode", "ColoCountry", "ColoGeoHash", "ColoName", "GREChecksum", "GREEtherType", "GREHeaderLength", "GREKey", "GRESequenceNumber", and "GREVersion` | `additional.fields` | Mapped from changelog  
`ICMPChecksum", "ICMPType", "ICMPCode", "IPProtocol", "ProtocolState", "IPTTL", "IPTTLBuckets", "IPTotalLength", "IPTotalLengthBuckets", "IPv4Checksum", "IPv4DSCP", "IPv4DontFragment", "IPv4ECN", "IPv4Identification", "IPv6DSCP", "IPv6ECN", "IPv6FlowLabel", and "IPv6Identification` | `additional.fields` | Mapped from changelog  
`MitigationScope", "MitigationSystem", "SampleInterval", "TCPAcknowledgementNumber", "TCPChecksum", "TCPDataOffset", "TCPFlags", "TCPFlagsString", "TCPMSS", "TCPSACKPermitted", "TCPSequenceNumber", "TCPTimestampECR", "TCPTimestampValue", "TCPUrgentPointer", "TCPWindowScale", "TCPWindowSize", "UDPChecksum", "UDPPayloadLength", and "Verdict` | `additional.fields` | Mapped from changelog  
`AttackCampaignID", "AttackID", and "AttackVector` | `additional.fields` | Mapped from changelog  
`RuleName` | `security_result.rule_name` | Mapped from changelog  
`RulesetID" and "RulesetOverrideID` | `security_result_detection_fields` | Mapped from changelog  
`ClientVersion` | `metadata.product_version` | Mapped from changelog  
`DeviceManufacturer` | `principal.asset.hardware` | Mapped from changelog  
`DeviceModel` | `principal.asset.hardware` | Mapped from changelog  
`DeviceName` | `principal.asset.attribute.labels` | Mapped from changelog  
`DeviceSerialNumber` | `principal.resource.attribute.labels` | Mapped from changelog  
`DeviceType` | `principal.resource.name` | Mapped from changelog  
`OSVersion` | `principal.platform_version` | Mapped from changelog  
`PostureCheckName` | `additional.fields` | Mapped from changelog  
`PostureCheckType` | `additional.fields` | Mapped from changelog  
`PostureEvaluatedResult` | `additional.fields` | Mapped from changelog  
`PostureExpectedJSON.os` | `security_result.detection_fields` | Mapped from changelog  
`PostureExpectedJSON.operator` | `security_result.detection_fields` | Mapped from changelog  
`PostureExpectedJSON.connection_id` | `security_result.detection_fields` | Mapped from changelog  
`PostureReceivedJSON.os` | `security_result.detection_fields` | Mapped from changelog  
`PostureReceivedJSON.overall` | `security_result.detection_fields` | Mapped from changelog  
`PostureReceivedJSON.version` | `security_result.detection_fields` | Mapped from changelog  
`PostureReceivedJSON.state` | `security_result.detection_fields` | Mapped from changelog  
`PostureReceivedJSON.last_seen` | `date` | Mapped from changelog  
`ClientRequestSource` | `additional.fields` | Mapped from changelog  
`SecurityActions", "SecurityRuleIDs", and "SecuritySources` | `additional.fields` | Mapped from changelog  
`SecurityAction", "SecurityRuleID` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`SecurityRuleID` | `security_result.threat_id` | Mapped from changelog  
`SecurityRuleDescription` | `security_result.threat_name` | Mapped from changelog  
`metadata.event_type` | `GENERIC_EVENT` | Mapped from changelog  
`ClientRequestURI` | `target.uri` | Mapped from changelog  
`BotScore` | `security_result.detection_fields` | Mapped from changelog  
`WAFRCEAttackScore", "WAFSQLiAttackScore", "WAFXSSAttackScore", "WAFAttackScore", "WAFFlags` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`AssetExternalID` | `principal.asset_id` | Mapped from changelog  
`AssetDisplayName` | `principal.asset.attribute.labels` | Mapped from changelog  
`AssetLink` | `principal.url` | Mapped from changelog  
`AssetMetadata.userKey` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.clientId` | `principal.user.userid` | Mapped from changelog  
`AssetMetadata.anonymous` | `security_result.detection_fields` | Mapped from changelog  
`AssetMetadata.nativeApp` | `security_result.detection_fields` | Mapped from changelog  
`DetectedTimestamp` | `metadata.event_timestamp` | Mapped from changelog  
`FindingTypeDisplayName` | `security_result.description` | Mapped from changelog  
`FindingTypeID` | `security_result.rule_id` | Mapped from changelog  
`FindingTypeSeverity` | `security_result.severity` | Mapped from changelog  
`InstanceID` | `principal.resource.product_object_id` | Mapped from changelog  
`IntegrationDisplayName` | `additional.fields` | Mapped from changelog  
`IntegrationID` | `metadata.product_deployment_id` | Mapped from changelog  
`IntegrationPolicyVendor` | `additional.fields` | Mapped from changelog  
`AssetMetadata.customerId` | `principal.user.userid` | Mapped from changelog  
`AssetMetadata.primaryEmail` | `principal.user.email_addresses` | Mapped from changelog  
`AssetMetadata.agreedToTerms` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.ipWhitelisted` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.lastLoginTime` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.isEnforcedIn2Sv` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.isEnrolledIn2Sv` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.isDelegatedAdmin` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.changePasswordAtNextLogin` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.includeInGlobalAddressList` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.isAdmin` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.suspended` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.url` | `principal.url` | Mapped from changelog  
`AssetMetadata.site_admin` | `principal.user.attribute.labels` | Mapped from changelog  
`AssetMetadata.login` | `principal.user.userid` | Mapped from changelog  
`AssetMetadata.owner.id` | `principal.user.userid` | Mapped from changelog  
`AssetMetadata.name.fullName` | `principal.user.user_display_name` | Mapped from changelog  
`AssetMetadata.name.givenName` | `principal.user.first_name` | Mapped from changelog  
`AssetMetadata.name.familyName` | `principal.user.last_name` | Mapped from changelog  
`Allowed` | `security_result.action` | Mapped from changelog  
`BytesReceived` | `network.received_bytes` | Mapped from changelog  
`BytesSent` | `network.sent_bytes` | Mapped from changelog  
`ClientTCPHandshakeDurationMs` | `additional.fields` | Mapped from changelog  
`ClientTLSCipher` | `network.tls.cipher` | Mapped from changelog  
`ClientTLSHandshakeDurationMs` | `additional.fields` | Mapped from changelog  
`ClientTLSVersion` | `network.tls.version` | Mapped from changelog  
`ConnectionCloseReason` | `additional.fields` | Mapped from changelog  
`ConnectionReuse` | `additional.fields` | Mapped from changelog  
`DestinationTunnelID` | `additional.fields` | Mapped from changelog  
`EgressPort` | `principal.port` | Mapped from changelog  
`EgressRuleID` | `additional.fields` | Mapped from changelog  
`EgressRuleName` | `additional.fields` | Mapped from changelog  
`IngressColoName` | `additional.fields` | Mapped from changelog  
`Offramp` | `additional.fields` | Mapped from changelog  
`OriginTLSCertificateIssuer` | `additional.fields` | Mapped from changelog  
`OriginTLSCertificateValidationResult` | `additional.fields` | Mapped from changelog  
`OriginTLSCipher` | `additional.fields` | Mapped from changelog  
`OriginTLSHandshakeDurationMs` | `additional.fields` | Mapped from changelog  
`OriginTLSVersion` | `additional.fields` | Mapped from changelog  
`RuleEvaluationDurationMs` | `additional.fields` | Mapped from changelog  
`SessionEndTime` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
