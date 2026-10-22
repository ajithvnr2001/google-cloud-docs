---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail/
title: Collect Proofpoint TAP alerts logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:36.030915+00:00
---

# Collect Proofpoint TAP alerts logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint TAP alerts logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Proofpoint Targeted Attack Protection (TAP) alerts logs by setting up a Google Security Operations feed.

For more information, see [Google SecOps data ingestion](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `PROOFPOINT_MAIL` ingestion label.

## Configure Proofpoint TAP alerts

  1. Sign in to the Proofpoint threat [insight portal](https://threatinsight.proofpoint.com) using your credentials.
  2. On the **Settings** tab, select **Connected applications**. The **Service credentials** section appears.
  3. In the **Name** section, click **Create new credential**.
  4. Type the name of your organization, such as `altostrat.com`. 
  5. Click **Generate**. In the **Generated service credential** dialog, the **Service principal** and **Secret** values appear.
  6. Copy the **Service principal** and **Secret** values. The values are displayed only at the time of creation and are required when you configure the Google Security Operations feed.
  7. Click **Done**.

**Note:** We recommended that you enter **Service credential name** as the customer email domain name. It is used for log source creation.

## Set up feeds

To configure the feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. Click the **Proofpoint** feed pack. 
  4. Locate the **Proofpoint Tap Alerts** log type. 
  5. Specify the values for the following fields:

     * **Source type** : Third party API
     * **Username** : specify the service principal that you obtained previously.
     * **Secret** : specify the secret that you obtained previously.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  6. Click **Create Feed**.




For more information about Google Security Operations feeds, see [Google Security Operations feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type). If you encounter issues when you create feeds, contact [Google Security Operations support](https://docs.cloud.google.com/chronicle/docs/support).

## Field mapping reference

This parser handles Proofpoint Mail logs in JSON or key-value format, extracting email and network activity details. It maps log fields to the UDM, categorizing events like email transactions and network HTTP requests, and enriching them with security details like actions, categories, and threat information.

## Limitations

When analyzing `PROOFPOINT_MAIL` logs, you might observe events with historical timestamps despite real-time ingestion. This behavior is inherent to the Proofpoint API, not the Google SecOps ingestion pipeline. Even when Google SecOps queries for the most recent activity, the Proofpoint API can return events that occurred several days prior. Discrepancies between the `event_timestamp` and the `ingestion_time` are expected for the `PROOFPOINT_MAIL` log type due to how Proofpoint buffers and releases event data. For further details, see the [Proofpoint event timestamp documentation](https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation/SIEM_API#.2Fv2.2Fsiem.2Fall:%7E:text=In%20other%20words,%20a%20request%20using%20the%20sinceSeconds=3600%C2%A0parameter%20will%20retrieve%20all%20events%20which%20have%20been%20created%20in%20the%20last%20hour.%20It%20is%20possible%20that%20the%20events%20returned%20from%20that%20interval%20reference%20messages%20or%20clicks%20which%20were%20first%20observed%20more%20than%20one%20hour%20ago%E2%80%94perhaps%20even%20several%20days%20ago).

## UDM mapping tables

The following tables list the mappings of Proofpoint TAP alerts raw log fields to UDM fields, categorized according to the format. 

### Clicks-related JSON-format log fields

Log field | UDM field | Description  
---|---|---  
`clicksBlocked[].classification` | `security_result.category`,  
`security_result.category_details` | The classification of the threat (for example, `malware`, `phish`).  
`clicksBlocked[].clickIP` | `principal.ip`,  
`security_result.about.ip` | The IP address of the user who clicked the URL.  
`clicksBlocked[].clickTime` | `metadata.event_timestamp`,  
`additional.fields["clickTime"]` | The timestamp of the click.  
`clicksBlocked[].GUID` | `metadata.product_log_id` | The unique identifier for the click event.  
`clicksBlocked[].guid` | `metadata.product_log_id` | The unique identifier for the click event.  
`clicksBlocked[].id` | `additional.fields["id"]` | The unique Click Identifier.  
`clicksBlocked[].messageID` | `network.email.mail_id` | The original Email Message ID.  
`clicksBlocked[].recipient` | `network.email.to`,  
`target.user.email_addresses` | The email address of the recipient.  
`clicksBlocked[].sender` | `network.email.from`,  
`principal.user.email_addresses` | The email address of the sender. The user-part is hashed. The domain-part is cleartext.  
`clicksBlocked[].senderIP` | `principal.ip` | The IP address of the original sender.  
`clicksBlocked[].threatID` | `security_result.threat_id` | The identifier for the detected threat.  
`clicksBlocked[].threatStatus` | `security_result.threat_status` | The status of the threat (`Active`, `Cleared`, and so on).  
`clicksBlocked[].threatTime` | `metadata.event_timestamp` if `clicksBlocked[].clickTime` is null,  
`additional.fields["clicks_clickTime"]` | The time when Proofpoint assigned the threatStatus.  
`clicksBlocked[].threatUrl` | `security_result.url_back_to_product` | A link to the entry on the TAP Dashboard for the particular threat.  
`clicksBlocked[].url` | `target.url`,  
`security_result.about.url` | The malicious URL that was clicked.  
`clicksBlocked[].userAgent` | `network.http.user_agent`,  
`network.http.parsed_user_agent` | The user agent of the client making the click.  
`clicksPermitted[].classification` | `security_result.category`,  
`security_result.category_details` | The classification of the threat (for example, `malware`, `phish`).  
`clicksPermitted[].clickIP` | `principal.ip`,  
`security_result.about.ip` | The IP address of the user who clicked the URL.  
`clicksPermitted[].clickTime` | `metadata.event_timestamp`,  
`additional.fields["clickTime"]` | The timestamp of the click.  
`clicksPermitted[].GUID` | `metadata.product_log_id` | The unique identifier for the click event.  
`clicksPermitted[].guid` | `metadata.product_log_id` | The unique identifier for the click event.  
`clicksPermitted[].id` | `additional.fields["id"]` | The unique Click Identifier.  
`clicksPermitted[].messageID` | `network.email.mail_id` | The original Email Message ID.  
`clicksPermitted[].recipient` | `network.email.to`,  
`target.user.email_addresses` | The email address of the recipient.  
`clicksPermitted[].sender` | `network.email.from`,  
`principal.user.email_addresses` | The email address of the sender. The user-part is hashed. The domain-part is cleartext.  
`clicksPermitted[].senderIP` | `principal.ip` | The IP address of the original sender.  
`clicksPermitted[].threatID` | `security_result.threat_id` | The identifier for the detected threat.  
`clicksPermitted[].threatStatus` | `security_result.threat_status` | The status of the threat (Active, Cleared, and so on).  
`clicksPermitted[].threatTime` | `metadata.event_timestamp` if `clicksPermitted[].clickTime` is null,  
`additional.fields["clicks_clickTime"]` | The time when Proofpoint assigned the `threatStatus`.  
`clicksPermitted[].threatUrl` | `security_result.url_back_to_product` | A link to the entry on the TAP Dashboard for the particular threat.  
`clicksPermitted[].url` | `target.url`,  
`security_result.about.url` | The malicious URL that was clicked.  
`clicksPermitted[].userAgent` | `network.http.user_agent`,  
`network.http.parsed_user_agent` | The user agent of the client making the click.  
  
### Messages-related JSON-format log fields

Log field | UDM field | Description  
---|---|---  
`messagesBlocked[].ccAddresses` | `intermediary.user.email_addresses` | A list of email addresses contained within the `CC:` header.  
`messagesBlocked[].cluster` | `additional.fields["cluster"]` | The specific Proofpoint mail processing cluster (or tenant deployment) that handled the email event.  
`messagesBlocked[].clusterId` | `additional.fields` | The name of the PPS cluster that processed the message.  
`messagesBlocked[].fromAddress` | `principal.user.email_addresses`,  
`network.email.from` if `messagesBlocked[].sender` isn't present | The email address contained in the `From:` header, excluding friendly name.  
`messagesBlocked[].guid` | `metadata.product_log_id` | The ID of the message within PPS. It can be used to identify the message in PPS and is always unique.  
`messagesBlocked[].GUID` | `metadata.product_log_id` | The ID of the message within PPS. It can be used to identify the message in PPS and is always unique.  
`messagesBlocked[].headerCC` | `additional.fields["headerCC "]` | Contains headerCC details.  
`messagesBlocked[].headerReplyTo` | `additional.fields["headerReplyTo "]` | If present, the full content of the `Reply-To:` header, including any friendly names.  
`messagesBlocked[].id` | `additional.fields["id"]` | Contains message ID details.  
`messagesBlocked[].impostorScore` | `security_result.detection_fields["impostorScore"]` | The impostor score of the message.  
`messagesBlocked[].malwareScore` | `security_result.detection_fields["malwareScore"]` | The malware score of the message.  
`messagesBlocked[].messageID` | `network.email.mail_id` | The Message-ID extracted from the headers of the email message. It can be used to look up the associated message in PPS and is unique.  
`messagesBlocked[].messageParts[].contentType` | `about.file.mime_type` | The MIME type of the file.  
`messagesBlocked[].messageParts[].disposition` | `additional.fields["disposition "]` | How the message part is handled (for example, attached, inline). Indexed dynamically.  
`messagesBlocked[].messageParts[].md5` | `about.file.md5` | The MD5 hash of the message part/file.  
`messagesBlocked[].messageParts[].oContentType` | `additional.fields["oContentType "]` | The declared Content-Type of the `messagePart`.  
`messagesBlocked[].messageParts[].sandboxStatus` | `security_detection.fields["sandboxStatus "]` | The status of the file analysis in the sandbox.  
`messagesBlocked[].messageParts[].sha256` | `about.file.sha256` | The SHA256 hash of the message part/file.  
`messagesBlocked[].messagesBlocked[].messageParts[].filename` | `about.file.full_path` | The name of the file or attachment.  
`messagesBlocked[].messageSize` | `additional.fields["messageSize"]` | The size in bytes of the message, including headers and attachments.  
`messagesBlocked[].messageTime` | `metadata.event_timestamp` | When the message was delivered to the user or quarantined by PPS.  
`messagesBlocked[].modulesRun` | `additional.fields["modulesRun"]` | The list of PPS modules which processed the message.  
`messagesBlocked[].phishScore` | `security_result.detection_fields["phishScore"]` | The phish score of the message.  
`messagesBlocked[].policyRoutes` | `additional.fields["PolicyRoutes"]` | The policy routes that the message matched during processing by PPS.  
`messagesBlocked[].QID` | `additional.fields["QID"]` | The queue ID of the message within PPS. It can be used to identify the message in PPS and isn't unique.  
`messagesBlocked[].quarantineFolder` | `security_result.priority` if `messagesBlocked[].quarantineFolder` is "Low Priority" or "High Priority",  
`security_result.detection_fields ["quarantineFolder"]` otherwise | The name of the folder that contains the quarantined message.  
`messagesBlocked[].recipient` | `network.email.to` | An array containing the email addresses of the recipients.  
`messagesBlocked[].replyToAddress` | `network.email.reply_to` if it's a valid email,  
`additional.fields["replyTo"]` otherwise | The email address contained in the `Reply-To:` header.  
`messagesBlocked[].sender` | `network.email.from` | The email address of the sender.  
`messagesBlocked[].senderIP` | `principal.ip`,  
`principal.asset.ip` | The email address of the sender.  
`messagesBlocked[].spamScore` | `security_result.detection_fields["spamScore"]` | The spam score of the message.  
`messagesBlocked[].subject` | `network.email.subject` | The email subject.  
`messagesBlocked[].suborgs.rcpts` | `additional.fields["suborgsRcpts"]` | An array of internal sub-organization IDs assigned to the recipient(s).  
`messagesBlocked[].suborgs.sender` | `additional.fields["suborgsSender"]` | The internal sub-organization ID assigned to the sender.  
`messagesBlocked[].threatsInfoMap[].campaignId` | `security_result.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`messagesBlocked[].threatsInfoMap[].campaignID` | `security_result.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`messagesBlocked[].threatsInfoMap[].classification` | `security_result.category`,  
`security_result.category_details` | The category of threat found in the message.  
`messagesBlocked[].threatsInfoMap[].completelyRewritten` | `security_result.detection_fields`,  
`security_result.action` | The rewrite status of the message. If the value is `true`, all instances of URL threats within the message were successfully rewritten. If the value is `false`, at least one instance of a threat URL was not rewritten. If the value is `na`, the message didn't contain any URL-based threats.  
`messagesBlocked[].threatsInfoMap[].detectionType` | `security_result.detection_fields` | The new field `detectionType` and `ThreatInfo` added to the response.  
`messagesBlocked[].threatsInfoMap[].threat` | `security_result.about.url` if `threatType` is`url`,  
`security_result.about.file.sha256` if `attachment`,  
`security_result.about.resource.name` if `messageText`,  
`result.about.resource.attribute.labels` with value `Email` and key `threatType`,  
`security_result.about.resource.name`,  
`security_result.about.resource.attribute.labels` | Whether the threat was an attachment, URL, or message type.  
`messagesBlocked[].threatsInfoMap[].threatID` | `security_result.threat_id` | The unique identifier associated with this threat. It can be used to query the forensics and campaign endpoints.  
`messagesBlocked[].threatsInfoMap[].threats.actors[].id` | `security_result.detection_fields` | An array of structures, which contain details about the actor's ID.  
`messagesBlocked[].threatsInfoMap[].threats.actors[].name` | `security_result.detection_fields` | An array of structures, which contain details about the actor's ID.  
`messagesBlocked[].threatsInfoMap[].threats.actors[].type` | `security_result.detection_fields` | An array of structures, which contain details about the actor's ID.  
`messagesBlocked[].threatsInfoMap[].threatStatus` | `security_result.threat_status` | The current state of the threat.  
`messagesBlocked[].threatsInfoMap[].threatTime` | `metadata.event_timestamp` if `messagesBlocked[].messageTime` isn't present,  
`security_result.detection_fields` | The time when Proofpoint assigned the `threatStatus`.  
`messagesBlocked[].threatsInfoMap[].threatType` | `security_result.threat_name` | A string specifying which threat type will be returned in the data.  
`messagesBlocked[].threatsInfoMap[].threatUrl` | `security_result.url_back_to_product` | A link to the entry about the threat on the TAP Dashboard.  
`messagesBlocked[].toAddresses` | `target.user.email_addresses` | A list of email addresses contained within the `To:` header.  
`messagesBlocked[].xmailer` | `security_result.detection_fields["xmailer"]` | The content of the `X-Mailer:` header.  
`messagesDelivered[].ccAddresses` | `intermediary.user.email_addresses` | A list of email addresses contained within the `CC:` header.  
`messagesDelivered[].cluster` | `additional.fields["cluster"]` | The specific Proofpoint mail processing cluster (or tenant deployment) that handled the email event.  
`messagesDelivered[].clusterId` | `additional.fields` | The name of the PPS cluster that processed the message.  
`messagesDelivered[].fromAddress` | `principal.user.email_addresses`,  
`network.email.from` if `messagesDelivered[].sender` isn't present | The email address contained in the `From:` header, excluding friendly name.  
`messagesDelivered[].GUID` | `metadata.product_log_id` | The ID of the message within PPS. It can be used to identify the message in PPS and is always unique.  
`messagesDelivered[].guid` | `metadata.product_log_id` | The ID of the message within PPS. It can be used to identify the message in PPS and is always unique.  
`messagesDelivered[].headerCC` | `additional.fields["headerCC "]` | Contains headerCC details.  
`messagesDelivered[].headerReplyTo` | `additional.fields["headerReplyTo "]` | If present, the full content of the `Reply-To:` header, including any friendly names.  
`messagesDelivered[].id` | `additional.fields["id "]` | Contains message ID details.  
`messagesDelivered[].impostorScore` | `security_result.detection_fields["impostorScore"]` | The impostor score of the message.  
`messagesDelivered[].malwareScore` | `security_result.detection_fields["malwareScore"]` | The malware score of the message.  
`messagesDelivered[].messageID` | `network.email.mail_id` | The Message-ID extracted from the headers of the email message. It can be used to look up the associated message in PPS and isn't unique.  
`messagesDelivered[].messageParts[].contentType` | `about.file.mime_type` | The MIME type of the file.  
`messagesDelivered[].messageParts[].disposition` | `additional.fields["disposition "]` | How the message part is handled (for example, attached, inline). Indexed dynamically.  
`messagesDelivered[].messageParts[].md5` | `about.file.md5` | The MD5 hash of the message part/file.  
`messagesDelivered[].messageParts[].oContentType` | `additional.fields["oContentType "]` | The declared Content-Type of the `messagePart`.  
`messagesDelivered[].messageParts[].sandboxStatus` | `security_detection.fields["sandboxStatus "]` | The status of the file analysis in the sandbox.  
`messagesDelivered[].messageParts[].sha256` | `about.file.sha256` | The SHA256 hash of the message part/file.  
`messagesDelivered[].messagesDelivered[].messageParts[].filename` | `about.file.full_path` | The name of the file or attachment.  
`messagesDelivered[].messageSize` | `additional.fields["messageSize"]` | The size in bytes of the message, including headers and attachments.  
`messagesDelivered[].messageTime` | `metadata.event_timestamp` | When the message was delivered to the user or quarantined by PPS.  
`messagesDelivered[].modulesRun` | `additional.fields["modulesRun"]` | The list of PPS modules that processed the message.  
`messagesDelivered[].phishScore` | `security_result.detection_fields["phishScore"]` | The phish score of the message.  
`messagesDelivered[].policyRoutes` | `additional.fields["PolicyRoutes"]` | The policy routes that the message matched during processing by PPS.  
`messagesDelivered[].QID` | `additional.fields["QID"]` | The queue ID of the message within PPS. It can be used to identify the message in PPS and isn't unique.  
`messagesDelivered[].quarantineFolder` | `security_result.priority` if `messagesDelivered[].quarantineFolder` is "Low Priority" or "High Priority",  
`security_result.detection_fields ["quarantineFolder"]` otherwise | The name of the folder that contains the quarantined message.  
`messagesDelivered[].recipient` | `network.email.to` | An array containing the email addresses of the recipients.  
`messagesDelivered[].replyToAddress` | `network.email.reply_to` if it's a valid email,  
`additional.fields ["replyTo"]` otherwise | The email address contained in the `Reply-To:` header.  
`messagesDelivered[].senderIP` | `principal.ip`,  
`principal.asset.ip` | The email address of the sender.  
`messagesDelivered[].spamScore` | `security_result.detection_fields["spamScore"]` | The spam score of the message.  
`messagesDelivered[].subject` | `network.email.subject` | The email subject.  
`messagesDelivered[].suborgs.rcpts` | `additional.fields["suborgsRcpts"]` | An array of internal sub-organization IDs assigned to the recipients.  
`messagesDelivered[].suborgs.sender` | `additional.fields["suborgsSender"]` | The internal sub-organization ID assigned to the sender  
`messagesDelivered[].threatsInfoMap[].campaignId` | `security_result.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`messagesDelivered[].threatsInfoMap[].campaignID` | `security_result.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`messagesDelivered[].threatsInfoMap[].classification` | `security_result.category`,  
`security_result.category_details` | The category of threat found in the message.  
`messagesDelivered[].threatsInfoMap[].completelyRewritten` | `security_result.detection_fields`,  
`security_result.action` | The rewrite status of the message. If the value is `true`, all instances of URL threats within the message were successfully rewritten. If the value is `false`, at least one instance of a threat URL was not rewritten. If the value is `na`, the message didn't contain any URL-based threats.  
`messagesDelivered[].threatsInfoMap[].detectionType` | `security_result.detection_fields` | The new field `detectionType` and `ThreatInfo` added to the response.  
`messagesDelivered[].threatsInfoMap[].threat` | `security_result.about.url` if `threatType` is`url`,  
`security_result.about.file.sha256` if `threatType` is `attachment`  
`security_result.about.resource.name` if `threatType` is `messageText`,  
`security_result.about.resource.name` otherwise,  
`result.about.resource.attribute.labels` with value `Email` and key `threatType`,  
`security_result.about.resource.name`,  
`security_result.about.resource.attribute.labels` | Whether the threat was an attachment, URL, or message type.  
`messagesDelivered[].threatsInfoMap[].threatID` | `security_result.threat_id` | The unique identifier associated with this threat. It can be used to query the forensics and campaign endpoints.  
`messagesDelivered[].threatsInfoMap[].threats.actors[].id` | `security_result.detection_fields` | An array of structures, which contain details about the actor's ID.  
`messagesDelivered[].threatsInfoMap[].threats.actors[].name` | `security_result.detection_fields` | An array of structures, which contain details about the actor's ID.  
`messagesDelivered[].threatsInfoMap[].threats.actors[].type` | `security_result.detection_fields` | An array of structures, which contain details about the actor's ID.  
`messagesDelivered[].threatsInfoMap[].threatStatus` | `security_result.threat_status` | The current state of the threat.  
`messagesDelivered[].threatsInfoMap[].threatTime` | `metadata.event_timestamp` if `messagesDelivered[].messageTime` isn't present,  
`security_result.detection_fields` | The time when Proofpoint assigned the `threatStatus`.  
`messagesDelivered[].threatsInfoMap[].threatType` | `security_result.threat_name` | A string specifying which threat type will be returned in the data.  
`messagesDelivered[].threatsInfoMap[].threatUrl` | `security_result.url_back_to_product` | A link to the entry about the threat on the TAP Dashboard.  
`messagesDelivered[].toAddresses` | `target.user.email_addresses` | A list of email addresses contained within the `To:`header.  
`messagesDelivered[].xmailer` | `security_result.detection_fields["xmailer"]` | The content of the X-Mailer: header.  
`msg.accountType` |  | Vendor-specific additional fields.  
`msg.address` | `principal.user.email_addresses` | The specific email address associated with the account being monitored or evaluated for threat activity.  
`msg.dashboardLink` | `security_result.url_back_to_product` | A link to the Threat Insight dashboard.  
`msg.deliveredMessages` |  | Vendor-specific additional fields.  
`msg.eventTime` | `metadata.event_timestamp` if `messageTime` and `threatTime` is empty | The exact UTC timestamp when this threat observation or log event was generated.  
`msg.highRisk` | `security_result.action` | A boolean flag (true/false) indicating whether Proofpoint classifies this account as posing an elevated security risk or compromise level.  
`msg.identity` |  | Vendor-specific additional fields.  
`msg.maliciousMessages` |  | Vendor-specific additional fields.  
`msg.observations[]` | additional.fields["observations"] | A list of specific threat intelligence behavioral tags or anomaly indicators flagged by Proofpoint algorithms.  
`msg.timeRanges[].end` | `additional.fields` | An array of time windows showing when suspicious behaviors or threat indicators were actively observed for this account.  
`msg.timeRanges[].falsePositive` | `additional.fields` | An array of time windows showing when suspicious behaviors or threat indicators were actively observed for this account.  
`msg.timeRanges[].start,msg` | `additional.fields` | An array of time windows showing when suspicious behaviors or threat indicators were actively observed for this account.  
`msg.trafficType` |  | Vendor-specific additional fields.  
`queryEndTime` | `metadata.collected_timestamp` | The time when the period queried for data ended.  
`sender_domain` | `principal.domain.name` | Extracted from `messagesBlocked[].fromAddress` or `messagesDelivered[].fromAddress` consisting of the domain name of the sender.  
  
### Syslog-format log fields

Log field | UDM field | Description  
---|---|---  
`a` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`action` | `security_result.action`,  
`security_result.action_details` | Contains action details.  
`active` | `security_result.threat_status` | The threat status.  
`adjust` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`adultscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`application` | `principal.application` | Contains principal application details.  
`attachments` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`bits` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`bulkscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`campaignID` | `security_result.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`ccAddresses` | `intermediary.user.email_addresses` | A list of email addresses contained within the `CC:` header.  
`cid` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`cipher` | `network.tls.cipher` | Contains `tls.cipher` details.  
`cipher_bits` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`class` | `security_result.category`,  
`security_result.category_details` | The threat category of the malicious URL.  
`classifier` | `security_result.category` | The category of threat found in the message.  
`clickIP` | `security_result.about.ip`, `principal.ip`,  
`principal.asset.ip` | The external IP address of the user who clicked on the link. If the user is behind a firewall performing network address translation, the IP address of the firewall will be shown.  
`clickTime` | `metadata.event_timestamp` if `messageTime` isn't present | The time the user clicked on the URL.  
`cluster` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`clusterId` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`clx_result_group` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`clx_score` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`clx_shade` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`clxscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`cmd` | `network.http.method` if STS isn't empty,  
`principal.process.command_line` otherwise | When STS isn't empty, it contains the HTTP method, otherwise, it contains command line details.  
`completelyRewritten` | `security_result.action`,  
`security_result.detection_fields["completelyRewritten"]` | The rewrite status of the message. If the value is `true`, all instances of URL threats within the message were successfully rewritten. If the value is `false`, at least one instance of a threat URL was not rewritten. If the value is `na`, the message didn't contain any URL-based threats.  
`corrupted` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`country` | `principal.location.country_or_region` | Contains country details.  
`daemon` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`date_log` | `metadata.event_timestamp` if `messageTime`, `clickTime` and `threatTime` are not present | The timestamp present in the syslog.  
`date_log_rebase` | `metadata.event_timestamp` if `messageTime`, `clickTime` and `threatTime` are not present | The timestamp present in the syslog.  
`default` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`definitions` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`delay` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`dict` | `security_result.category_details` | Contains `category_details`.  
`dnsid` | `network.dns.id` | Contains DNS ID details.  
`domain` | `principal.administrative_domain` | Contains `administrative_domain` details.  
`dsn` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`duration` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`eid` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`elapsed` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`engine` | `metadata.product_version` | Contains `product_version` details.  
`envid` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`err` | `security_result.description` | A description.  
`evt` | `extensions.auth.auth_details` | Authentication details.  
`expires` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`file` | `about.process.file.full_path` | Contains file full path details.  
`from` | `network.email.from` | Contains email of the sender.  
`fromAddress` | `network.email.from` | The email address contained in the `From:` header.  
`guid` | `metadata.product_log_id` | The ID of the message within PPS. It can be used to identify the message in PPS and is always unique.  
`hdr_mid` | `network.email.mail_id` | Contains `mail_id` details.  
`headerFrom` | `additional.fields["headerFrom"]` | The full content of the `From:` header, including any friendly name.  
`headerReplyTo` | `additional.fields["headerReplyTo"]` | If present, the full content of the `Reply-To:` header.  
`headerTo` | `additional.fields` | Vendor-specific additional fields.  
`helo` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`hfrom` | `network.email.from` | Contains the email address of the sender.  
`hfrom_domain` | `principal.administrative_domain` | Contains the `administrative_domain` details.  
`hops-ip` | `intermediary.ip` | Contains the intermediary IP address.  
`host` | `principal.hostname` | Contains hostname details.  
`id` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`id` | `additional.fields` | Vendor-specific additional fields.  
`impostor_score` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`impostorScore` | `security_result.detection_fields` | The impostor score of the message.  
`inter_host` | `intermediary.hostname` | Contains intermediary hostname details.  
`intermediary_hostname` | `intermediary.hostname` | Contains the intermediary hostname.  
`intermediary_ip` | `intermediary.ip` | Contains the intermediary IP address.  
`ip` | `principal.ip`,  
`principal.asset.ip` | Contains the IP address of the sender  
`len` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`lint` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`lip` | `intermediary.ip` | Contains the intermediary IP address.  
`log_level` | `security_result.severity` | Contains severity details.  
`lowpriorityscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`m` | `network.email.mail_id` | Contains `mail_id` details.  
`mailer` | `network.application_protocol` | Contains `application_protocol` details.  
`malwareScore` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`messageID` | `network.email.mail_id` | The Message-ID extracted from the headers of the email message.  
`messageParts[].contentType` | `about.file.mime_type` | The MIME type of the file.  
`messageParts[].disposition` | `additional.fields["disposition "]` | How the message part is handled (for example, attached, inline). Indexed dynamically.  
`messageParts[].filename` | `about.file.full_path` | The name of the file or attachment.  
`messageParts[].md5` | `about.file.md5` | The MD5 hash of the message part/file.  
`messageParts[].oContentType` | `additional.fields["oContentType "]` | The declared Content-Type of the `messagePart`.  
`messageParts[].sandboxStatus` | `security_detection.fields["sandboxStatus "]` | The status of the file analysis in the sandbox.  
`messageParts[].sha256` | `about.file.sha256` | The SHA256 hash of the message part/file.  
`messageTime` | `metadata.event_timestamp` | When the message was delivered to the user or quarantined by PPS.  
`mime` | `principal.process.file.mime_type` | Contains file `mime_type` details.  
`mlxscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`mod` | `network.application_protocol` | Contains `application_protocol` details.  
`module` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`modulesRun` | `security_result.detection_fields` | The list of PPS modules that processed the message.  
`modulesRun` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`msg` | `security_result.description` | A description.  
`msghold_response` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`msgid` | `network.email.mail_id` | Contains `mail_id` details.  
`msgs` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`name` | `about.process.file.full_path` | Contains the full path of the file.  
`notroutes` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`nrcpts` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`path` | `principal.url` | Contains URL details.  
`phishscore` | `security_result.detection_fields` | The phish score of the message.  
`pid` | `principal.process.pid` | Contains PID details.  
`policy` | `network.direction` | Describes the network flow. Contains inbound/outbound value.  
`pri` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`principal_hostname` | `principal.hostname`,  
`principal.asset.hostname` | Contains principal hostname details.  
`principal_ip_1` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_2` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_3` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_4` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_5` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_6` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_7` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_8` | `principal.ip`,  
`principal.assest.ip` | Contains principal IP details.  
`principal_ip_port_1` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_2` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_3` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_4` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_5` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_6` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_7` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_ip_port_8` | `principal.resource.attribute.labels` | Contains principal port details.  
`principal_pid` | `principal.process.pid` | Captures the process PID.  
`priority_score` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`priorityscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`profile` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`prot` | `network.application_protocol` | Contains `application_protocol` details.  
`protected` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`proto` | `network.application_protocol` | Contains `application_protocol` details.  
`pss` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`qid` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`quarantineFolder` | `security_result.priority` | The name of the folder that contains the quarantined message.  
`quarantineRule` | `security_result.rule_name` | The name of the rule that quarantined the message.  
`query` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`querydepth` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`rcode` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`rcpt` | network.email.to | Contains the email address of the recipient.  
`rcpts` | network.email.to | Contains the email address of the recipient  
`reason` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`recipient` | `target.user.email_addresses` | Contains recipient email details.  
`reject` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`reply` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`replyToAddress` | network.email.reply_to | The email address contained in the `Reply-To:` header.  
`resolve` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`restquery_stage` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`result` | `security_result.action` | Contains action details.  
`result` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`result_detail` | `security_result.description` | Provides a description.  
`reverse` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`routes` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`rss` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`rule` | `security_result.rule_name` | Contains the `rule_name`.  
`s` | `network.session_id` | Contains `session_id` details.  
`scancount` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`scope` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`score` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`selector` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`sender` | `principal.user.email_addresses` | Contains sender email details.  
`senderIP` | `principal.ip`,  
`principal.assest.ip` | Contains sender IP details.  
`sendmail_queue_id` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`sha256` | `security_result.about.file.sha256` | The SHA256 file details.  
`size` | principal.process.file.size` | Contains file size details.  
`smtputf8` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`spamscore` | `security_result.detection_fields` | The spam score of the message.  
`src_host` | `principal.hostname`,  
`principal.asset.hostname` | Contains principal hostname details.  
`STARTTLS` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`stat` | `additional.fields` | Contains status details.  
`status` | `additional.fields` | Contains status details.  
`sts` | `network.http.response_code` | Contains the `response_code` data.  
`subject` | `network.email.subject` | Contains the `email.subject`.  
`subject` | `network.email.subject` | Contains email subject details.  
`suspectscore` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`sys` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`sz` | `principal.process.file.size` | Contains file size details.  
`tests` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`threat` | `security_result.about.url` if `threatType` is `url`,  
`security_result.about.file.sha256` if `threatType` is `attachment`  
`security_result.about.resource.name` if `threatType` is `messageText`,  
`result.about.resource.attribute.labels` with value `Email` and key `threatType`  
`security_result.about.resource.name`,  
`security_result.about.resource.attribute.labels` with key `["threatType"]` |   
`threatID` | `security_result.threat_id` | Contains threat ID details.  
`threatsInfoMap[].campaignID` | `security_result1.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`threatsInfoMap[].classification` | `security_result.category`  
`security_result.category_details` | The category of threat found in the message.  
`threatsInfoMap[].threat` | `security_result.about.url` if `threatType` is `url`,  
`security_result.about.file.sha256` if `threatType` is `attachment`  
`security_result.about.resource.name` if `threatType` is `messageText`,  
`result.about.resource.attribute.labels` with value `Email` and key `threatsInfoMap[].threatType`  
`security_result.about.resource.name` otherwise,  
`security_result.about.resource.attribute.labels` with key `["threatType"]` | An array of structures, which contain details about detected threats within the message. There may be more than one threat per message.  
`threatsInfoMap[].threatID` | `security_result.threat_id` | Contains threat ID details.  
`threatsInfoMap[].threatStatus` | `security_result.threat_status` | The current state of the threat.  
`threatsInfoMap[].threatTime` | `metadata.event_timestamp` if `messageTime` and `clickTime` isn't present,  
`security_result.detection_fields` |   
`threatsInfoMap[].threatType` | `security_result.about.url` if `threatType` is `url`  
`security_result.about.file.sha256` if `threatType` is `attachment`  
`security_result.about.resource.name` if `threatType` is `messageText`  
`result.about.resource.attribute.labels` with value `Email` and key `threatsInfoMap[].threatType`  
`security_result.about.resource.name`,  
`security_result.about.resource.attribute.labels` with key `["threatType"]` | An array of structures that contain details about detected threats within the message. There may be more than one threat per message.  
`threatsInfoMap[].threatUrl` | `security_result.url_back_to_product` | A link to the entry on the TAP Dashboard for the particular threat.  
`threatStatus` | `security_result.threat_status` | The current state of the threat.  
`threatTime` | `metadata.event_timestamp` if `messageTime` and `clickTime` isn't present | The time when Proofpoint identified the URL as a threat.  
`threatType` | `security_result.about.url` if `threatType` is `url`,  
`security_result.about.file.sha256` if `threatType` is `attachment`  
`security_result.about.resource.name` if `threatType` is `messageText`,  
`result.about.resource.attribute.labels` with value `Email` and key `threatType`  
`security_result.about.resource.name`,  
`security_result.about.resource.attribute.labels` with key `["threatType"]` |   
`threatURL` | `security_result.url_back_to_product` | A link to the entry on the TAP Dashboard for the particular threat.  
`threshold` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`tls` | `network.tls.cipher` | Contains `tls.cipher` details.  
`tls-alert` | `security_result.description` | Provides a description  
`tls_verify` | `security_result.action` | Contains verify details.  
`tls_version` | `network.tls.version` | Contains TLS version details.  
`to` | `network.email.to` | Contains the email address of the recipient.  
`toAddresses` | `network.email.to` | A list of email addresses contained within the `To:` header.  
`token` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`ts` | `metadata.event_timestamp` if `messageTime`, `clickTime` and `threatTime` are not present | The timestamp present in the syslog.  
`type` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`uri` | `principal.url` | Contains URL details.  
`url_count` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`userAgent` | `network.http.user_agent`,  
`network.http.parsed_user_agent` | The HTTP User Agent.  
`value` | `network.email.from` | Contains the email address of the sender.  
`vendor` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`verify` | `security_result.action` | Contains verify details.  
`version` | `network.tls.version` | Contains TLS version details.  
`virtual` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`virusthreat` | `security_result.threat_name` | Contains threat name details.  
`virusthreatid` | `security_result.threat_id` | Contains threat ID details.  
`warn` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`x` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`X-Proofpoint-Spam-Details` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`xdelay` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`xmailer` | `security_result.detection_fields` | The content of the `X-Mailer:` header, if present, or vendor-specific security detection fields.  
  
### CEF log fields

Log field | UDM field | Description  
---|---|---  
`cluster` | `additional.fields` | Vendor-specific additional fields.  
`file_hash` | `principal.file.md5` | Contains file MD5 details.  
`file_name` | `principal.file.full_path` | Contains the path.  
`GUID` | `metadata.product_log_id` | Contains the `product_log_id`.  
`guid` | `metadata.product_log_id` | Contains the `product_log_id`.  
`headerFrom` | `additional.fields` | The full content of the `From:` header.  
`headerReplyTo` | `additional.fields["headerReplyTo"]` | The full content of the `Reply-To:` header.  
`host` | `principal.hostname`,  
`principal.assest.hostname` | Contains the principal hostname.  
`id` | `additional.fields` | Additional fields with vendor-specific event data that can't be adequately represented within the formal sections of the UDM model.  
`id` | `additional.fields` | Vendor-specific additional fields.  
`impostorScore` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`malwareScore` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`message_id` | `network.email.mail_id` | Contains `mail_id` details.  
`messageParts_contentType` | `principal.file.mime_type` | Represents the MIME type of a specific part/component of the email message.  
`messageParts_disposition` | `additional.fields` | Vendor-specific additional fields.  
`messageParts_oContentType` | `additional.fields` | Vendor-specific additional fields.  
`messageParts_sandboxStatus` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`messageParts_sha256` | `principal.file.sha256` | Contains file 256 details.  
`messageTime` | `metadata.event_timestamp` | The time when the message was delivered to the user or quarantined by PPS.  
`modulesRun` | `security_result.detection_fields` | The list of PPS modules that processed the message.  
`modulesRun` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`orig_dest` | `network.email.to` | The email address in the initial SMTP envelope/header when the email hit the gateway.  
`orig_recipient` | `target.user.email_addresses` | The email address of the recipient.  
`orig_src` | `network.email.from` | The email address of the source.  
`policyRoutes` | `additional.fields` | Vendor-specific additional fields.  
`process_id` | `principal.process.pid` | Contains process PID details.  
`QID` | `additional.fields` | The queue ID of the message within PPS. It can be used to identify the message in PPS and isn't unique.  
`quarantineFolder` | `security_result.priority` | The name of the folder that contains the quarantined message.  
`quarantineRule` | `security_result.rule_name` | The name of the rule that quarantined the message.  
`return_addr` | `principal.user.email_addresses` | The envelope address specified during SMTP transport (MAIL FROM).  
`rt` | `additional.fields` | Vendor-specific additional fields.  
`sender` | `principal.user.email_addresses` | Contains the email address of the sender.  
`src` | `principal.ip`,  
`principal.asset.ip` | Contains the principal IP address.  
`stag` | `additional.fields` | Vendor-specific additional fields.  
`start` | `additional.fields` | Vendor-specific additional fields.  
`status_code` | `additional.fields` | Vendor-specific additional fields.  
`subject` | `network.email.subject` | Contains the `email.subject`.  
`threatsInfoMap_campaignID` | `security_result.rule_id` | An identifier for the campaign of which the threat is a member, if available at the time of the query. Threats can be linked to campaigns even after these events are retrieved.  
`threatsInfoMap_classification` | `security_result.category`,  
`security_result.category_details` | The threat category of the malicious URL.  
`threatsInfoMap_detectionType` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`threatsInfoMap_threatID` | `security_result.threat_id` | Contains threat ID details.  
`threatsInfoMap_threatTime` | `metadata.event_timestamp` if `messageTime` is empty | The time when Proofpoint assigned the `threatStatus`.  
`threatsInfoMap_threatTime` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`threatsInfoMap_threatType` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`threatsInfoMap_threatUrl` | `security_result.url_back_to_product` | Contains the URL that redirects to view Proofpoint's threat intelligence, sandbox analysis, and forensic details.  
`threatStatistics_families_name0` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`threatStatistics_families_score0` | `security_result.detection_fields` | Vendor-specific security detection fields.  
`url` | `security_result.about.url` | The actual Suspicious/Malicious URL.  
`version` | `additional.fields` | Vendor-specific additional fields.  
`vip` | `additional.fields` | Vendor-specific additional fields.  
`xmailer` | `security_result.detection_fields` | The content of the `X-Mailer:` header, if present, or vendor-specific security detection fields.  
  
## UDM mapping delta reference

On September 9, 2025, Google SecOps released a new version of the Proofpoint TAP alerts parser, which includes significant changes to the mapping of Proofpoint TAP alerts log fields to UDM fields and updates to event type classifications (mappings).

### Log-field mapping delta

The following table shows the changes to how Proofpoint TAP alerts log fields are mapped to UDM fields. The **Old mapping** column lists the fields exposed prior to September 9, 2025, and the **Current mapping** column lists the new fields.

Log field | Old mapping | Current mapping  
---|---|---  
`clicks.impostorScore` | `additional.fields` | `security_result.detection_fields`  
`clicks.malwareScore` | `additional.fields` | `security_result.detection_fields`  
`clicks.phishScore` | `additional.fields` | `security_result.detection_fields`  
`clicks.quarantineFolder` | `additional.fields` | If `quarantineFolder`is equal to `low priority` or `high priority`, then map to `security_result.priority`. Otherwise, map to `security_result.detection_fields`.  
`clicks.quarantineRule` | `additional.fields` | `security_result.rule_name`  
`clicks.sender` | `about.email` | `Not Mapped`  
`clicks.senderIP` | `about.ip` | `principal.ip`  
`clicks.spamScore` | `additional.fields` | `security_result.detection_fields`  
`impostorScore` | `additional.fields` | `security_result.detection_fields`  
`malwareScore` | `additional.fields` | `security_result.detection_fields`  
`msg.impostorScore` | `additional.fields` | `security_result.detection_fields`  
`msg.malwareScore` | `additional.fields` | `security_result.detection_fields`  
`msg.phishScore` | `additional.fields` | `security_result.detection_fields`  
`msg.quarantineFolder` | `additional.fields` | If `quarantineFolder`is equal to `low priority` or `high priority`, then map to `security_result.priority`. Otherwise, map to `security_result.detection_fields`.  
`msg.quarantineRule` | `additional.fields` | `security_result.rule_name`  
`msg.spamScore` | `additional.fields` | `security_result.detection_fields`  
`msgPart.contentType` | `additional.fields` | `Not Mapped`  
`partData.contentType` | `principal.process.file.mime_type` | `about.file.mime_type`  
`partData.disposition` | `security_result.detection_fields` | `additional.fields`  
`partData.filename` | `principal.process.file.full_path` | `about.file.full_path`  
`partData.md5` | `principal.process.file.md5` | `about.file.md5`  
`partData.sha256` | `about.file.sha1` | `about.file.sha256`  
`phishScore` | `additional.fields` | `security_result.detection_fields`  
`quarantineFolder` | `additional.fields` | If `quarantineFolder` is equal to `low priority` or `high priority`, then map to UDM field `security_result.priority`. Otherwise, map to `security_result.detection_fields`.  
`spamScore` | `additional.fields` | `security_result.detection_fields`  
  
### Event-type mapping delta

Multiple events that were previously classified as _generic events_ are now properly classified with more meaningful event types.

The following table lists the delta for the handling of Proofpoint TAP alerts event types prior to September 9, 2025 and subsequently (listed in the **Old event_type** and **Current event_type** columns respectively).

Format | eventType from log | Old event_type | Current event_type  
---|---|---|---  
`SYSLOG+KV` | If the log has `fromAddress`, `toAddresses`, `hfrom`, `from`, `value`,`to`,`rcpt`,`rcpts` or `mailer`,`proto`,`mod` fields are present |  | `EMAIL_TRANSACTION`  
| If the log contains only `mail_id` details | `EMAIL_TRANSACTION` | `EMAIL_UNCATEGORIZED`  
`CEF` logs | eventname= `messagesDelivered`, `messagesBlocked` |  | `EMAIL_TRANSACTION`  
| if the log has `emails`, `sender`, `headerReplyTo`, `orig_recipient` |  | `USER_UNCATEGORIED`  
| if the log has `src`, `host` |  | `STATUS_UPDATE`  
`SYSLOG+JSON` | eventname= `messagesDelivered`, `messagesBlocked`, `clicksPermitted`, `clicksBlocked` |  | `EMAIL_TRANSACTION`  
`JSON` | `record.address` |  | `USER_UNCATEGORIZED`  
| `lookalikeDomain.name` |  | `STATUS_UPDATE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
