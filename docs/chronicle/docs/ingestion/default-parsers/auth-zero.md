---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auth-zero/
title: Collect Auth0 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:48.010485+00:00
---

# Collect Auth0 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auth-zero/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Auth0 logs

**Parser Version:** 16.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts Auth0 log events from JSON formatted messages. It initializes UDM fields, parses the JSON payload, maps relevant fields to the UDM schema, and categorizes events based on the **type** field, setting appropriate security actions and event types.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Auth0 account with necessary permissions.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, **Auth0 Logs**).
  5. Select **Webhook** as the **Source type**.
  6. Select **AUTH_ZERO** as the **Log type**.
  7. Click **Next**.
  8. Optional: specify values for the following input parameters: 
     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label applied to the events from this feed.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
  13. On the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.
  14. Click **Done**.



## Create an API key for the webhook feed

  1. Go to **Google Cloud console** > **Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then select **API key**.

  3. Restrict the API key access to the **Chronicle API**.




## Specify the endpoint URL

  1. In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
  2. Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
         
         X-goog-api-key = API_KEY
         X-Webhook-Access-Key = SECRET
         

**Recommendation** : Specify the API key as a header instead of specifying it in the URL. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
         
         ENDPOINT_URL?key=API_KEY&secret=SECRET
         




Replace the following:

  * `ENDPOINT_URL`: the feed endpoint URL.
  * `API_KEY`: the API key to authenticate to Google Security Operations.
  * `SECRET`: the secret key that you generated to authenticate the feed.



## Configure Auth0 webhook for Google SecOps

  1. Access the Auth0 Dashboard.
  2. Go to **Monitoring** > **Streams**.
  3. Click **Create Log Stream**.
  4. Click the **Custom Webhook** button and give it a name of your choice. For example: **Google SecOps Webhook**.
  5. Configure the following: 
     * **Payload URL** : Enter the Google SecOps API endpoint URL.
     * **Content-Type** : Set the **Content-Type** header to **application/json**. This tells Google SecOps the format of the data being sent.
     * Optional: **Authorization Token** : Configure a secret for added security. This will be used to verify the authenticity of the webhook requests.

**Note:** In the Auth0 console, you can specify the JSON output format. We recommend selecting **JSON Object** for optimal compatibility.

**Customize the Payload** : You can customize the payload sent to Google SecOps by modifying the Event Category. This lets you select specific data points from the Auth0 event and format them as needed for Google SecOps. Refer to the Auth0 documentation for details on available context variables and scripting options. Ensure the final payload conforms to the expected Google SecOps UDM format.

  1. Click **Save** to create the webhook.
  2. Trigger the event associated with the hook (for example, register a new user, log in). 
  3. Verify that the logs are being sent to Google SecOps by checking the feed in the Google SecOps console.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`client_id` | `principal.asset.product_object_id` | Directly mapped from the `client_id` field.  
`client_name` | `principal.hostname` | Directly mapped from the `client_name` field.  
`connection` | `security_result.description` | Directly mapped from the `connection` field.  
`connection_id` | `security_result.rule_id` | Directly mapped from the `connection_id` field.  
`date` | `metadata.event_timestamp` | Parsed from the `date` field using the ISO8601 format.  
`description` | `metadata.description` | Directly mapped from the `description` field.  
`details.error` | `security_result.detection_fields` | Mapped from `details.error` field. Key is "Error".  
`details.error.oauthError` | `security_result.detection_fields` | Mapped from `details.error.oauthError` field. Key is "oauthError".  
`details.error.type` | `security_result.detection_fields` | Mapped from `details.error.type` field. Key is "oauth_error_type".  
`details.ipOnAllowlist` | `security_result.detection_fields` | Mapped from `details.ipOnAllowlist` field. Key is "ipOnAllowlist".  
`details.link` | `target.url` | Directly mapped from the `details.link` field if present, otherwise derived from other fields (see below).  
`details.request.auth.strategy` | `security_result.detection_fields` | Mapped from `details.request.auth.strategy` field. Key is "strategy".  
`details.request.body.app_metadata.blockedReason` | `security_result.detection_fields` | Mapped from `details.request.body.app_metadata.blockedReason` field. Key is "blockedReason".  
`details.request.body.app_metadata.customer_id` | `target.user.product_object_id` | Directly mapped from the `details.request.body.app_metadata.customer_id` field.  
`details.request.body.app_metadata.migrated` | `security_result.detection_fields` | Mapped from `details.request.body.app_metadata.migrated` field. Key is "migrated".  
`details.request.channel` | `security_result.detection_fields` | Mapped from `details.request.channel` field. Key is "channel".  
`details.request.method` | `network.http.method` | Directly mapped from the `details.request.method` field after converting to uppercase.  
`details.request.path` | `target.url` | Directly mapped from the `details.request.path` field if `details.link` is not present, otherwise derived from other fields (see below).  
`details.response.body.email` | `target.user.email_addresses` | Directly mapped from the `details.response.body.email` field.  
`details.response.body.email_verified` | `security_result.detection_fields` | Mapped from `details.response.body.email_verified` field. Key is "email_verified".  
`details.response.body.nickname` | `target.user.user_display_name` | Directly mapped from the `details.response.body.nickname` field.  
`details.response.body.user_id` | `target.user.userid` | Directly mapped from the `details.response.body.user_id` field.  
`details.response.statusCode` | `network.http.response_code` | Directly mapped from the `details.response.statusCode` field after converting to integer.  
`details.return_to` | `target.url` | Directly mapped from the `details.return_to` field if `details.link` and `details.request.path` are not present, otherwise derived from other fields (see below).  
`details.session_id` | `network.session_id` | Directly mapped from the `details.session_id` field.  
`details.stats.loginsCount` | `additional.fields` | Mapped from `details.stats.loginsCount` field. Key is "loginsCount".  
`details.requiresVerification` | `security_result.detection_fields` | Mapped from `details.requiresVerification` field. Key is "requiresVerification".  
`details.to` | `target.user.email_addresses` | Directly mapped from the `details.to` field.  
`hostname` | `target.hostname` | Directly mapped from the `hostname` field.  
`ip` | `principal.ip` | Directly mapped from the `ip` field.  
`js_data.audience` | `target.url` | Directly mapped from the `js_data.audience` field if `details.link`, `details.request.path`, and `details.return_to` are not present.  
`js_data.details.body.email_verified` | `security_result.detection_fields` | Mapped from `js_data.details.body.email_verified` field. Key is "email_verified".  
`js_data.details.body.is_signup` | `security_result.detection_fields` | Mapped from `js_data.details.body.is_signup` field. Key is "is_signup".  
`js_data.details.body.transaction.redirect_uri` | `target.url` | Directly mapped from the `js_data.details.body.transaction.redirect_uri` field if `details.link`, `details.request.path`, `details.return_to`, and `js_data.audience` are not present.  
`js_data.scope` | `security_result.detection_fields` | Mapped from `js_data.scope` field. Key is "scope".  
`js_data.tracking_id` | `security_result.detection_fields` | Mapped from `js_data.tracking_id` field. Key is "tracking_id".  
`log_id` | `metadata.product_log_id` | Directly mapped from the `log_id` field.  
`metadata.log_type` | `metadata.log_type` | Directly mapped from the `log_type` field.  
`metadata.product_name` | `metadata.product_name` | Set to "AUTH_ZERO".  
`metadata.vendor_name` | `metadata.vendor_name` | Set to "AUTH_ZERO".  
`metadata.product_event_type` | `metadata.product_event_type` | Directly mapped from the `type` field.  
`network.http.parsed_user_agent` | `network.http.parsed_user_agent` | Parsed from the `user_agent` field.  
`network.http.user_agent` | `network.http.user_agent` | Directly mapped from the `user_agent` field.  
`security_result.action` | `security_result.action` | Determined by the `type` field (ALLOW or BLOCK). See parser code for specific mappings.  
`strategy` | `security_result.detection_fields` | Mapped from the `strategy` field. Key is "strategy".  
`strategy_type` | `security_result.detection_fields` | Mapped from the `strategy_type` field. Key is "strategy_type".  
`target.user.email_addresses` | `target.user.email_addresses` | Directly mapped from the `user_name` field if it is an email address, otherwise derived from other fields (see above).  
`target.user.userid` | `target.user.userid` | Directly mapped from the `user_id` field, or `details.response.body.user_id` or `user_name` if `user_id` is not present.  
`user_agent` | `network.http.user_agent` | Directly mapped from the `user_agent` field.  
`user_id` | `target.user.userid` | Directly mapped from the `user_id` field.  
`user_name` | `target.user.email_addresses` | Directly mapped from the `user_name` field. Set to "MACHINE" if `security_result.action` is "ALLOW" and `type` is "slo", "sapi", "s", "ss", or "ssa". Set to "OTP" if `extensions.auth.type` is "MACHINE" and `type` is "slo". Determined by a combination of fields including `type`, `client_name`, `ip`, `hostname`, and `has_user`. See parser code for specific mappings.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auth-zero-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
