---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-waf/
title: Collect AWS WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:10.543309+00:00
---

# Collect AWS WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS WAF logs

**Parser Version:** 11.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect the AWS Web Application Firewall (WAF) logs by setting up a Google Security Operations feed. The parser transforms raw JSON formatted logs into a structured format conforming to the Google SecOps UDM. It extracts fields like IP addresses, URLs, user agents, and security rule details, mapping them to corresponding UDM fields for consistent representation and analysis.

## Before you begin

*Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## Configure Amazon S3 bucket

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for later use.
  3. Create a user following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**. 
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
  7. Select **Third-party service** as the **Use case**.
  8. Click **Next**.
  9. Optional: add description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for later use. 
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in the **Permissions policies** section.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for and select the **AmazonS3FullAccess** policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Create a WAF web ACL (Access Control List)

If you haven't set up AWS WAF yet, you'll need to create a WAF web ACL (Access Control List). For existing setups, you can skip to the next procedure.

  1. In the AWS Console, search for and select **AWS WAF & Shield**.
  2. Click **Create web ACL**.
  3. Provide the following settings: 
     * **Name** : Give the ACL a name (for example, `my-waf-web-acl`).
     * **Region** : Choose the region where you want to apply the WAF.
     * **CloudWatch Metrics** : Enable metric collection to track the activity and rules triggered.
  4. Once created, select the **web ACL** for which you want to enable logging.



## How to configure AWS WAF Logging

  1. In the **AWS WAF Console** , go to the **Logging** tab of your web ACL.
  2. Click **Enable Logging**.
  3. Select **Amazon S3** as the destination for your logs.
  4. Choose the **S3 bucket** created earlier to store the logs.
  5. Optional: configure a log prefix for organizing the logs (for example, `waf-logs/`).
  6. Click **Save**.



## Verify Permissions for the S3 Bucket

Ensure that the S3 bucket has the proper permissions for AWS WAF to write logs.

  1. Go to the **S3 Console**.
  2. Select the bucket where the logs will be stored.
  3. In the **Permissions** tab, add the following Bucket Policy to allow AWS WAF to write logs:
         
         {
           "Version": "2012-10-17",
           "Statement": [
               {
                 "Effect": "Allow",
                 "Principal": {
                     "Service": "wafv2.amazonaws.com"
                 },
                 "Action": "s3:PutObject",
                 "Resource": "arn:aws:s3:::your-log-bucket-name/*"
               }
           ]
         }
         


**Note:** Replace `your-log-bucket-name` with the actual name of your S3 bucket.

  1. Click **Save**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS WAF feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS WAF** log type.
  3. Specify the values in the following fields.

     * **Source Type** : Amazon SQS V2
     * **Queue Name** : The SQS queue name to read from
     * **S3 URI** : The bucket URI. 
       * `s3://your-log-bucket-name/`
         * Replace `your-log-bucket-name` with the actual name of your S3 bucket.
     * **Source deletion options** : Select the deletion option according to your ingestion preferences.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **SQS Queue Access Key ID** : An account access key that is a 20-character alphanumeric string.

     * **SQS Queue Secret Access Key** : An account access key that is a 40-character alphanumeric string.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
action | security_result.action | If action is ALLOW, set security_result.action to ALLOW and security_result.severity to INFORMATIONAL. If action is BLOCK, set security_result.action to BLOCK. If action is CAPTCHA and captchaResponse.responseCode is 405, set security_result.action to BLOCK and security_result.action_details to "CAPTCHA {captchaResponse.failureReason}".  
captchaResponse.failureReason | security_result.action_details | Used in conjunction with action and captchaResponse.responseCode to determine security_result.action_details.  
captchaResponse.responseCode | security_result.action_details | Used in conjunction with action and captchaResponse.failureReason to determine security_result.action_details.  
httpRequest.clientIp | principal.ip, principal.asset.ip | Directly mapped to principal.ip and principal.asset.ip.  
httpRequest.headers | target.hostname, target.asset.hostname, network.http.user_agent, network.http.parsed_user_agent, network.http.referral_url, target.location.country_or_region, target.resource.attribute.labels, target.user.userid | Iterates through each header in httpRequest.headers. If the header name is "host" or "Host", the value is mapped to target.hostname and target.asset.hostname. If the header name is "User-Agent" or "user-agent", the value is mapped to network.http.user_agent and parsed into network.http.parsed_user_agent. If the header name is "Referer" or "referer", the value is mapped to network.http.referral_url. If the header name is "(?i)time-zone", the value is mapped to target.location.country_or_region. If the header name is "authorization", the value is decoded and the username is extracted and mapped to target.user.userid. All other headers are added as key-value pairs to target.resource.attribute.labels.  
httpRequest.httpMethod | network.http.method | Directly mapped to network.http.method.  
httpRequest.requestId | network.session_id | Directly mapped to network.session_id.  
httpRequest.uri | target.url | Directly mapped to target.url.  
httpSourceId | target.resource.name | Directly mapped to target.resource.name.  
httpSourceName | metadata.product_event_type | Directly mapped to metadata.product_event_type.  
labels | security_result.rule_labels | Iterates through each label in labels. If the label name is not empty, it is added as a key-value pair to security_result.rule_labels.  
nonTerminatingMatchingRules | security_result.action_details, security_result.rule_labels | Iterates through each rule in nonTerminatingMatchingRules. If action is ALLOW and the rule action is CAPTCHA, set security_result.action_details to "CAPTCHA SUCCESSFUL" and add the rule ID to security_result.rule_labels with the key "nonTerminatingCaptchaRuleName". If action is BLOCK or ALLOW and the rule action is COUNT, set security_result.action_details to "COUNT RULE" and add the rule ID to security_result.rule_labels with the key "nonTerminatingCountRuleName". If action is BLOCK or ALLOW and the rule action is CHALLENGE, set security_result.action_details to "COUNT RULE" and add the rule ID to security_result.rule_labels with the key "nonTerminatingChallengeRuleName".  
rateBasedRuleList | security_result.rule_id, security_result.rule_name, security_result.description | If terminatingRuleType is "RATE_BASED", iterates through each rule in rateBasedRuleList. If terminatingRuleId matches the rule name, the rule ID, rule name, and description are mapped to security_result.rule_id, security_result.rule_name, and security_result.description respectively.  
responseCodeSent | network.http.response_code | Directly mapped to network.http.response_code and converted to an integer.  
ruleGroupList | intermediary.labels, security_result.rule_id, security_result.rule_name, security_result.description, security_result.detection_fields | Iterates through each rule group in ruleGroupList. The rule group ID is added as a key-value pair to intermediary.labels. If terminatingRuleType is "MANAGED_RULE_GROUP" and terminatingRuleId matches the rule group ID, the rule ID, rule name, and description are mapped to security_result.rule_id, security_result.rule_name, and security_result.description respectively. If terminatingRuleType is "GROUP", the terminating rule ID is extracted and mapped to security_result.rule_name and security_result.description. The terminating rule group ID is added to security_result.rule_labels with the key "terminatingRuleGroupName". If terminatingRuleType is "REGULAR", the terminating rule action is extracted and added to security_result.detection _fields with the key "terminatingRuleAction_{index}".  
terminatingRuleId | security_result.rule_id, security_result.rule_name, security_result.description | If terminatingRuleType is "RATE_BASED", "MANAGED_RULE_GROUP", or "REGULAR", terminatingRuleId is mapped to security_result.rule_id, security_result.rule_name, and used to construct security_result.description.  
terminatingRuleMatchDetails | security_result.description, security_result.category_details, security_result.detection_fields | Iterates through each match in terminatingRuleMatchDetails. Sets security_result.description to "Terminating Rule". If the condition type is not empty, it is added to security_result.category_details. If the location is not empty, it is added to security_result.detection_fields with the key "location". For each matched data element, it is added to security_result.detection_fields with the key "matchedData".  
terminatingRuleType | security_result.rule_type | Directly mapped to security_result.rule_type.  
timestamp | metadata.event_timestamp | Converted to a timestamp and mapped to metadata.event_timestamp.  
webaclId | intermediary.resource.name | Directly mapped to intermediary.resource.name.  
| metadata.vendor_name | Set to "AMAZON".  
| metadata.product_name | Set to "AWS Web Application Firewall".  
| metadata.log_type | Set to "AWS_WAF".  
| network.application_protocol | Set to "HTTP".  
| metadata.event_type | Set to "NETWORK_HTTP" if httpRequest.headers contains a "host" or "Host" header. Otherwise, set to "STATUS_UPDATE".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
