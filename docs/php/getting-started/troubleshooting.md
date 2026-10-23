---
url: https://docs.cloud.google.com/php/getting-started/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 PHP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:20.230049+00:00
---

# Troubleshooting  |  PHP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/getting-started/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Guides ](https://docs.cloud.google.com/php/getting-started)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

## Tracing GRPC issues

### Before you begin

Be sure to initialize and enable write permissions before writing to your log file. In the following example, the log file is named `/var/log/grpc.log`:
    
    
    touch /var/log/grpc.log
    chmod 666 /var/log/grpc.log

If you encounter file permissions issues, you might need to preface the previous commands with `sudo`.

### Logging to a file

To save gRPC logs to a file, add the following lines to your `php.ini` file:
    
    
    grpc.grpc_verbosity=debug
    grpc.grpc_trace=all,-timer_check
    grpc.log_filename=/var/log/grpc.log
    

To write logs to `stderr` instead, exclude the last line from the previous example. For more information about other options, see [gRPC environment variables](https://grpc.github.io/grpc/php/md_doc_environment_variables.html).

**Note:** Enabling gRPC logs can also create many logs that grow large quickly. If you enable logging, be sure to clear the log file regularly with a `cron` job, set up a log file rotation, or turn logging off when finished debugging.

## Error Details

Google Cloud services follow [AIP-193](https://google.aip.dev/193) guidelines when returning errors. Google Cloud services use a defined set of standard error payloads, which you can find in [google.rpc.error_details.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto). These cover the most common API errors, such as quota failure and invalid parameters.

API errors emitted by PHP client libraries contain `message`, `code`, `status`, and `details` fields. Within the `details` field, additional `google.rpc.ErrorInfo` data appears in `reason`, `domain`, and `metadata` fields. The following sample shows an error that might appear if you called the Translation library with a cloud project before enabling the Translate API:
    
    
    Google\ApiCore\ApiException: {
        "reason": "SERVICE_DISABLED",
        "domain": "googleapis.com",
        "errorInfoMetadata": {
            "consumer": "projects\PROJECT_ID",
            "service": "translate.googleapis.com"
        },
        "message": "Cloud Translation API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting https:\/\/console.developers.google.com\/apis\/api\/translate.googleapis.com\/overview?project=PROJECT_ID then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
        "code": 7,
        "status": "PERMISSION_DENIED",
        "details": [
            {
                "@type": "google.rpc.errorinfo-bin",
                "reason": "SERVICE_DISABLED",
                "domain": "googleapis.com",
                "metadata": {
                    "consumer": "projects\PROJECT_ID",
                    "service": "translate.googleapis.com"
                }
            },
            {
                "@type": "google.rpc.help-bin",
                "links": [
                    {
                        "description": "Google developers console API activation",
                        "url": "https:\/\/console.developers.google.com\/apis\/api\/translate.googleapis.com\/overview?project=PROJECT_ID"
                    }
                ]
            }
        ]
    }

For more information about the general error model for Google APIs, see [Cloud API Errors](https://cloud.google.com/apis/design/errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
