---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/troubleshooting-ingestion2/
title: Troubleshoot ingestion issues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:40.790864+00:00
---

# Troubleshoot ingestion issues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/troubleshooting-ingestion2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot ingestion issues

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. Use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This document explains errors that you might encounter during data ingestion and normalization in Google Security Operations and describes how to remediate them. Use the following tables to diagnose ingestion failures, identify dropped logs, and evaluate downstream impact.

The document describes the errors for the following ingestion methods: Google SecOps forwarder, Google SecOps Ingestion API, Google SecOps API feed, and Third-party technology partners.

## Source and Ingestion Errors

You might encounter the following errors when:

  * Retrieving data from source systems.
  * The Google SecOps forwarder or a third-party feed attempts to communicate with an external API or resource.

HTTP status code | Error reason | Canonical error code | Error message | Error description | Troubleshooting  
---|---|---|---|---|---  
206 | Partial content | REMOTE_SERVER_ERROR | Remote server error due to partial content. | The upstream server returns partial content instead of the full dataset for `MICROSOFT_GRAPH_ALERT` feeds. | This is an upstream API issue. Google SecOps automatically retries the transfer. No data is lost. You don't need to take any action.  
400 | Bad request | INVALID_ARGUMENT | Invalid request parameters. | The system established a connection to the source, but the feed failed because of invalid arguments. | Verify source authorizations, required roles, and that all mandatory fields are correctly filled. Check for illegal characters in IDs, regions, or names, and ensure parameters like polling intervals are within limits. Review the feed configuration and refer to the feeds documentation. If the problem continues, contact Google SecOps support.  
401 | Unauthorized | LOGIN_FAILED | Authentication failed. Verify your credentials and try again. | The system established a connection, but authorization failed due to incorrect or missing credentials. | Verify and re-enter the credentials for the source to confirm they are correct and not expired.  
403 | Forbidden | ACCESS_DENIED / PERMISSION_DENIED | Access denied. The credentials lack permissions to access this resource. | The system established a connection to the source, but the credentials lack the necessary permissions for the resource. | Ensure the service or authentication account or API key has the necessary Identity and Access Management (IAM) roles or permissions for the resource. Refer to the [feed configuration](https://docs.cloud.google.com/chronicle/docs/reference/chronicle-api-feeds) for details. For example, double-check the Azure Event Hub connection string in the Azure portal. Or, refer to the feeds documentation for the necessary permissions. For information about permissions, see [Configuration by source type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#source-types).  
404 | URL not found | FILE_NOT_FOUND / NOT_FOUND | Endpoint not found. Verify the URL and resource details. | The system couldn't locate the specific file or endpoint. | Check the following:

  * The file exists on the source.
  * Check for typos in the API URL or hostname.
  * Ensure resource IDs (like bucket names or site IDs) and the region are correct.
  * The appropriate users have access to that specific path.

If the problem continues, contact Google SecOps support.  
429 |  | ACCESS_TOO_FREQUENT | Feed timed out. | The source is rate-limiting requests. The feed failed because there were too many attempts to reach the source. | This is typically a transient issue. If it persists, contact Google SecOps support.  
500 |  |  |  | A connection to the source was established, but the source didn't respond with data. | Ensure the source is available and responding. Contact Google SecOps support if the issue persists.  
502 |  |  |  | Feed encountered a gateway error. | This error is transient and the application will retry the request. If the issue persists, contact Google SecOps support.  
503 |  |  | Transient connection issue. | The source or gateway failed to respond or timed out. | Ensure the source is available and responding. Use jittered exponential backoff if calling the API programmatically.   
504 |  |  |  | Google SecOps can't connect to the source IP address and port. | This error is transient and the application will retry the request.Check the following:

  * The source is available. 
  * A firewall isn't blocking the connection. 
  * The IP address associated with the server is correct. 

If the problem continues, contact Google SecOps support.  
| Generic credential |  | Unable to validate credentials. Check your configuration details. |  | Check the general configuration details for the credential set in the Google SecOps console.   
|  | CONNECTION_DROPPED |  | The system established a connection to the source, but the connection closed before the feed completed. | This error is transient and application will retry the request. If the issue persists, contact Google SecOps support.  
|  | CONNECTION_FAILED | Can't connect to source. | The system is unable to establish a network connection. The application can't connect to the source IP address and port. | Verify the source is available, no firewall is blocking the connection, and the IP address is correct. Check the following:

  * The source is available.
  * A firewall isn't blocking the connection.
  * The IP address associated with the server is correct.
If the problem continues, contact Google SecOps support.
  
|  | DNS_ERROR | DNS error. | The system can't resolve the source hostname. | Verify the URLs in feed parameters and source name server settings. Check for spelling errors in the server hostname.  
|  | FILE_FAILED |  | The system established a connection to the source, but a problem occurred with the file or resource. | Check the following:

  * The file isn't corrupt.
  * The file-level permissions are correct.

If the problem continues, contact Google SecOps support.  
|  | GATEWAY_ERROR |  | API returned a gateway error to the call made by Google SecOps. | Verify the source details of the feed. The application will retry the request.  
|  | INTERNAL_ERROR |  | Unable to ingest data due to an internal error. | If the problem continues, contact Google SecOps support.  
|  | INVALID_FEED_CONFIG |  | The feed configuration contains invalid values. | Review the feed configuration for incorrect settings. Refer to the feeds documentation for correct syntax.  
|  | INVALID_REMOTE_RESPONSE |  | A connection to the source was established, but the response was incorrect. | Check the feed configuration. Learn more about setting up feeds. If the problem continues, contact Google SecOps support.  
|  | INVALID_SECRET | Secret key mismatch. |  | Check for a mismatch between the secret key configured in the feed and the key that Google SecOps received in the HTTP header. For example when using HTTPS Push Ingestion.  
|  | INVALID_SSL_CERTIFICATE | Invalid SSL certificate. | The system couldn't validate the source's SSL certificate. | Check source authorizations and ensure the server's certificate is valid and trusted.   
|  | NO_RESPONSE |  | A connection to the source was established, but the source didn't respond. | Make sure the source can support requests from Google SecOps. If the problem continues, contact Google SecOps support.  
|  | REMOTE_SERVER_ERROR |  | A connection to the source was established, but the source didn't respond with data. | Make sure the source is available and is responding with data. If the problem continues, contact Google SecOps support.  
|  | REMOTE_SERVER_REPORTED_BAD_REQUEST |  | A connection to the source was established, but the source rejected the request. | Check the feed configuration. Refer to the feeds documentation for more details. If the problem continues, contact Google SecOps support.  
|  | RESOURCE_EXHAUSTED | Quota or rate limit exceeded. |  | Check if quota rejections are happening due to high request volume or data limits. The source is sending requests too frequently. Monitor quota usage and contact support if needed. For example when using the Ingestion API or Google Workspace.  
|  | SOCKET_READ_TIMEOUT |  | A connection to the source was established, but the connection timed out before the data transfer was complete. | This error is transient and application will retry the request. If the issue persists, contact Google SecOps support.  
|  | TOO_MANY_ERRORS |  | The feed timed out because it encountered multiple errors from the source. | Contact Google SecOps support.  
|  | TRANSIENT_INTERNAL_ERROR |  | Feed encountered temporary internal error. | This error is transient and the application will retry the request. If the issue persists, contact Google SecOps support.  
|  | UNSAFE_CONNECTION |  | The application failed to make a connection because the IP address was restricted. | This error is transient and Google SecOps will retry the request. If the issue persists, contact Google SecOps support.  
  
## Parser and Normalization Errors

These errors occur after ingestion, during the process of mapping raw logs to the Unified Data Model (UDM). If errors occur here, Google SecOps might drop logs, or you might not be able to search logs using UDM fields.

Parser error type | Error description | Troubleshooting  
---|---|---  
Regex | The parser has an issue with a regular expression. | Check the parser logic. For prebuilt parsers, contact Google SecOps support.   
Invalid_config | The parser's configuration file has a problem. | Validate and correct the parser configuration file.   
Indexing event batch validation error | Normalized data fails schema checks. | Review the parser's mapping to UDM fields to ensure they meet requirements.   
Backlog | The system delayed normalization. | Raw logs are in the queue waiting for processing. Contact support if the delay continues.   
LOG_PARSING_DROPPED_NO_EVENTS | The parser produced no events, causing the log to be dropped. | Check raw logs to ensure they contain data that should actually produce events.   
LOG_PARSING_DROPPED_BY_FILTER | An explicit drop filter in the parser caused the system to drop the log. | Review filter conditions in the parser code. This is often intentional for logs with no security value.   
LOG_PARSING_DROPPED_BY_FILTER: TAG_MALFORMED_ENCODING | Bad JSON or XML encoding caused parsing to fail. | Ensure the log source is using a supported and well-formed encoding.   
LOG_PARSING_NO_PARSER_FOUND | The system has no parser for this log type. | Verify that you set the correct LogType and that a parser is active for that type.   
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
