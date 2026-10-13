---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ScanConfigError-Code/
title: Web Security Scanner V1beta API - Module Google::Cloud::WebSecurityScanner::V1beta::ScanConfigError::Code (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:56.665679+00:00
---

# Web Security Scanner V1beta API - Module Google::Cloud::WebSecurityScanner::V1beta::ScanConfigError::Code (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ScanConfigError-Code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Web Security Scanner V1beta API - Module Google::Cloud::WebSecurityScanner::V1beta::ScanConfigError::Code (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Web Security Scanner V1beta API module Google::Cloud::WebSecurityScanner::V1beta::ScanConfigError::Code.

Output only. Defines an error reason code. Next id: 44

## Constants 

### CODE_UNSPECIFIED

**value:** 0  
There is no error.

### OK

**value:** 0  
There is no error.

### INTERNAL_ERROR

**value:** 1  
Indicates an internal server error. Please DO NOT USE THIS ERROR CODE unless the root cause is truly unknown.

### APPENGINE_API_BACKEND_ERROR

**value:** 2  
One of the seed URLs is an App Engine URL but we cannot validate the scan settings due to an App Engine API backend error.

### APPENGINE_API_NOT_ACCESSIBLE

**value:** 3  
One of the seed URLs is an App Engine URL but we cannot access the App Engine API to validate scan settings.

### APPENGINE_DEFAULT_HOST_MISSING

**value:** 4  
One of the seed URLs is an App Engine URL but the Default Host of the App Engine is not set.

### CANNOT_USE_GOOGLE_COM_ACCOUNT

**value:** 6  
Google corporate accounts can not be used for scanning.

### CANNOT_USE_OWNER_ACCOUNT

**value:** 7  
The account of the scan creator can not be used for scanning.

### COMPUTE_API_BACKEND_ERROR

**value:** 8  
This scan targets Compute Engine, but we cannot validate scan settings due to a Compute Engine API backend error.

### COMPUTE_API_NOT_ACCESSIBLE

**value:** 9  
This scan targets Compute Engine, but we cannot access the Compute Engine API to validate the scan settings.

### CUSTOM_LOGIN_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT

**value:** 10  
The Custom Login URL does not belong to the current project.

### CUSTOM_LOGIN_URL_MALFORMED

**value:** 11  
The Custom Login URL is malformed (can not be parsed).

### CUSTOM_LOGIN_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS

**value:** 12  
The Custom Login URL is mapped to a non-routable IP address in DNS.

### CUSTOM_LOGIN_URL_MAPPED_TO_UNRESERVED_ADDRESS

**value:** 13  
The Custom Login URL is mapped to an IP address which is not reserved for the current project.

### CUSTOM_LOGIN_URL_HAS_NON_ROUTABLE_IP_ADDRESS

**value:** 14  
The Custom Login URL has a non-routable IP address.

### CUSTOM_LOGIN_URL_HAS_UNRESERVED_IP_ADDRESS

**value:** 15  
The Custom Login URL has an IP address which is not reserved for the current project.

### DUPLICATE_SCAN_NAME

**value:** 16  
Another scan with the same name (case-sensitive) already exists.

### INVALID_FIELD_VALUE

**value:** 18  
A field is set to an invalid value.

### FAILED_TO_AUTHENTICATE_TO_TARGET

**value:** 19  
There was an error trying to authenticate to the scan target.

### FINDING_TYPE_UNSPECIFIED

**value:** 20  
Finding type value is not specified in the list findings request.

### FORBIDDEN_TO_SCAN_COMPUTE

**value:** 21  
Scan targets Compute Engine, yet current project was not whitelisted for Google Compute Engine Scanning Alpha access.

### FORBIDDEN_UPDATE_TO_MANAGED_SCAN

**value:** 43  
User tries to update managed scan

### MALFORMED_FILTER

**value:** 22  
The supplied filter is malformed. For example, it can not be parsed, does not have a filter type in expression, or the same filter type appears more than once.

### MALFORMED_RESOURCE_NAME

**value:** 23  
The supplied resource name is malformed (can not be parsed).

### PROJECT_INACTIVE

**value:** 24  
The current project is not in an active state.

### REQUIRED_FIELD

**value:** 25  
A required field is not set.

### RESOURCE_NAME_INCONSISTENT

**value:** 26  
Project id, scanconfig id, scanrun id, or finding id are not consistent with each other in resource name.

### SCAN_ALREADY_RUNNING

**value:** 27  
The scan being requested to start is already running.

### SCAN_NOT_RUNNING

**value:** 28  
The scan that was requested to be stopped is not running.

### SEED_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT

**value:** 29  
One of the seed URLs does not belong to the current project.

### SEED_URL_MALFORMED

**value:** 30  
One of the seed URLs is malformed (can not be parsed).

### SEED_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS

**value:** 31  
One of the seed URLs is mapped to a non-routable IP address in DNS.

### SEED_URL_MAPPED_TO_UNRESERVED_ADDRESS

**value:** 32  
One of the seed URLs is mapped to an IP address which is not reserved for the current project.

### SEED_URL_HAS_NON_ROUTABLE_IP_ADDRESS

**value:** 33  
One of the seed URLs has on-routable IP address.

### SEED_URL_HAS_UNRESERVED_IP_ADDRESS

**value:** 35  
One of the seed URLs has an IP address that is not reserved for the current project.

### SERVICE_ACCOUNT_NOT_CONFIGURED

**value:** 36  
The Cloud Security Scanner service account is not configured under the project.

### TOO_MANY_SCANS

**value:** 37  
A project has reached the maximum number of scans.

### UNABLE_TO_RESOLVE_PROJECT_INFO

**value:** 38  
Resolving the details of the current project fails.

### UNSUPPORTED_BLACKLIST_PATTERN_FORMAT

**value:** 39  
One or more blacklist patterns were in the wrong format.

### UNSUPPORTED_FILTER

**value:** 40  
The supplied filter is not supported.

### UNSUPPORTED_FINDING_TYPE

**value:** 41  
The supplied finding type is not supported. For example, we do not provide findings of the given finding type.

### UNSUPPORTED_URL_SCHEME

**value:** 42  
The URL scheme of one or more of the supplied URLs is not supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
