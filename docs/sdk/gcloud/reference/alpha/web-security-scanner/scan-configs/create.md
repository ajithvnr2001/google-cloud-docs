---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/web-security-scanner/scan-configs/create/
title: gcloud alpha web-security-scanner scan-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:42:20.835012+00:00
---

# gcloud alpha web-security-scanner scan-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/web-security-scanner/scan-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha web-security-scanner scan-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha web-security-scanner scan-configs create - create a Web Security Scanner ScanConfig 
SYNOPSIS
    

`gcloud alpha web-security-scanner scan-configs create` `--display-name`=`DISPLAY_NAME` `--starting-urls`=[`STARTING_URLS`,…] [`--blacklist-patterns`=[`BLACKLIST_PATTERNS`,…]] [`--no-export-to-security-center`] [`--max-qps`=`MAX_QPS`] [`--risk-level`=`RISK_LEVEL`; default="normal"] [`--target-platforms`=[`TARGET_PLATFORMS`,…]; default=`"app_engine,`compute"] [`--user-agent`=`USER_AGENT`] [`--auth-password`=`AUTH_PASSWORD` `--auth-type`=`AUTH_TYPE` `--auth-url`=`AUTH_URL` `--auth-user`=`AUTH_USER`] [`--schedule-interval-days`=`SCHEDULE_INTERVAL_DAYS` `--schedule-next-start`=`SCHEDULE_NEXT_START`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a Web Security Scanner ScanConfig. 
EXAMPLES
     The following command creates a scan config named "my-scan-config": 
    
    
    gcloud alpha web-security-scanner scan-configs create --display-name=my-scan-config

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     A human-readable name for the scan config. 
`--starting-urls`=[`STARTING_URLS`,…]
     URLs the scan starts scanning from. These URLs must be 'owned' by the project in some way (resolve to a reserved IP address, or be the default `https://<PROJECT-ID>.<REGION-ID>.r.appspot.com`). 
OPTIONAL FLAGS
    

`--blacklist-patterns`=[`BLACKLIST_PATTERNS`,…]
     List of blacklist URL patterns as described online: <https://cloud.google.com/security-scanner/docs/excluded-urls>
`--export-to-security-center`
     If True, the scanner will export scan results to Cloud Security Command Center. Defaults to true. Enabled by default, use `--no-export-to-security-center` to disable. 
`--max-qps`=`MAX_QPS`
     Maximum queries per second (QPS) of the scanners. Defaults to 15, with a maximum of 20. 
`--risk-level`=`RISK_LEVEL`; default="normal"
     The risk level selected for the scan. Defaults to normal scanning. `RISK_LEVEL` must be one of: `low`, `normal`. 
`--target-platforms`=[`TARGET_PLATFORMS`,…]; default=`"app_engine,compute"`
     List of platforms the site is running on. Defaults to 'app_engine,compute'. `TARGET_PLATFORMS` must be one of: `app-engine`, `cloud-functions`, `cloud-run`, `compute`, `target-platform-unspecified`. 
`--user-agent`=`USER_AGENT`
     List of user agents to use when crawling. Defaults to 'chrome_linux'. `USER_AGENT` must be one of: `chrome-android`, `chrome-linux`, `safari-iphone`, `user-agent-unspecified`. 
`--auth-password`=`AUTH_PASSWORD`
     Password for the test user. Required if `--auth-type` is not 'none'. 
`--auth-type`=`AUTH_TYPE`
     Type of authentication to use. `AUTH_TYPE` must be one of: 

`custom`
     Authentication with a custom account. 
`google`
     Authentication with a Google account. 
`none`
     Disables Authentication. 
`--auth-url`=`AUTH_URL`
     URL of the login page for your site. Required if `--auth-type` is 'custom'. Otherwise, it should not be set. 
`--auth-user`=`AUTH_USER`
     The test user to log in as. Required if `--auth-type` is not 'none'. 'google' login requires a full email address. Cannot be your own account. 
`--schedule-interval-days`=`SCHEDULE_INTERVAL_DAYS`
     How frequently the scan should be run automatically (in days). If not set, there is no automatic scheduling of this scan. 
`--schedule-next-start`=`SCHEDULE_NEXT_START`
     When the next automatic scheduled scan should start. Requires `--schedule-interval-days` to be set. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `websecurityscanner/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
