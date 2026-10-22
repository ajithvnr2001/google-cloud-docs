---
url: https://docs.cloud.google.com/chronicle/docs/detection/migrate-cbn-alerts/
title: Migrate CBN alerts to YARA-L alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:33.215712+00:00
---

# Migrate CBN alerts to YARA-L alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/migrate-cbn-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate CBN alerts to YARA-L alerts

**Caution:** The **Enterprise Insights** page and CBN alerts are deprecated. Use the **Alerts and IOCs** page to view alerts. We recommend that you migrate the existing CBN alerts to the YARA-L detection engine as described in this guide. Google Security Operations's YARA-L detection engine is the preferred option for detection alerts because it offers enhanced transparency in detection logic and robust tuning capabilities. For more information see [Overview of the YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-overview).

This document provides details on how you can migrate Configuration Based Normalization (CBN) alerts to YARA-L detection alerts. As a security analyst, with the help of this document, you can continue getting notifications for alerts from third-party systems using the **Alerts and IOCs** page.

## Migrate CBN alerts to the YARA-L detection engine

To migrate CBN alerts, you can ensure that your prior CBN alerts are available as detection rule alerts using the following options.

### Use UDM search

Using the UDM search option, you can view events with the `alert_state` set in the parsers:
    
    
    security_result.alert_state = "ALERTING"
    

From the UDM search results, you can explore the following fields to understand which sources are generating CBN alerts in your environment:

  * `Metadata` > `Vendor Name`

  * `Metadata` > `Product Name`




### Download default CBN alerts using the Tools API and manually review

The previous approach helps you to find alerts that have fired, but does not cover the scenario of alerts that you have not seen before. You can use the `backstory.googleapis.com/v1/tools/cbn` parsers method to download default, select, or all CBNs, and manually review the parser logic applied to find `is_alert` or `alert_state` based alerts.

You can port CBN alerts to YARA-L detection engine rule alerts which you actively use.

#### Migrate Windows Defender antivirus alerts that were previously displayed in Enterprise Insights as CBN alerts

The following example shows how you can migrate Windows Defender antivirus alerts that were previously displayed in Enterprise Insights as CBN alerts.

  1. Find an example alert using any one of the approaches explained previously. 

  2. Using the Raw Log / UDM Event viewer, copy select UDM fields that will provide reliable detection. See the following example.
         
         metadata.vendor_name = "Microsoft"
         metadata.product_name = "Windows Defender AV"
         metadata.product_event_type = "MALWAREPROTECTION_STATE_MALWARE_DETECTED"
         principal.asset.hostname = "client02.example.local"
         security_result.action = "BLOCK"
         security_result.severity = "MEDIUM"
         

  3. Create a new YARA-L detection engine rule.
         
         rule windows_defender_av_monitored_events {
             meta:
             author = "Chronicle"
             description = "Migration of CBN alerts to Google SecOps YARA-L detection engine rule alert."
             // Severity is set at the Outcome level via security_result.severity
             severity = "INFORMATIONAL"
             priority = "INFORMATIONAL"
         events:
                 $windows_defender_av.metadata.vendor_name = "Microsoft"
                 $windows_defender_av.metadata.product_name = "Windows Defender AV"
                 $windows_defender_av.metadata.product_event_type = "MALWAREPROTECTION_STATE_MALWARE_DETECTED"
                 $windows_defender_av.principal.asset.hostname = $host
                 // optionally tune to only detection on ALLOW, i.e., failure to BLOCK
                 //$windows_defender_av.security_result.action = "ALLOW"
                 // optionally tune on severity of detection
                 //$windows_defender_av.security_result.severity != "LOW"
         outcome:
                 $risk_score = max(
                 if ($windows_defender_av.security_result.severity = "UNKNOWN_SEVERITY", 0) +
                 if ($windows_defender_av.security_result.severity = "LOW", 25) +
                 if ($windows_defender_av.security_result.severity = "MEDIUM", 50) +
                 if ($windows_defender_av.security_result.severity = "HIGH", 75) +
                 if ($windows_defender_av.security_result.severity = "CRITICAL", 100)
                 )
         $severity = array_distinct($windows_defender_av.security_result.severity)
             condition:
             $windows_defender_av
         }
         




#### CBN alert appears to use a field that was not parsed into UDM

Using the parser extensions option you can quickly address this scenario.

For example, Corelight CBN alert uses the `notice` field and conditionally alerts only if true:
    
    
    if [notice] == "true" {
      mutate {
        replace => {
          "is_significant" => "true"
          "is_alert"       => "true"
        }
      }
    }
    

Because this value isn't normalized into UDM by default you can use a parser extension Grok as follows to add that value as a UDM field of type `Additional`:
    
    
    filter {
        mutate {
            replace => {
                "notice" => ""
            }
        }
        grok {
            match     => { "message" => [ "(?P<message>\{.*\})$" ] }
            on_error  => "_grok_not_syslog"
            overwrite => [ "message" ]
        }
        json {
            on_error       => "not_json" 
            source         => "message"
            array_function => "split_columns"
        }
        if ![not_json] {
            if [notice] != "" {
                mutate {
                    convert => {
                        "notice" => "string"
                    }
                }
                mutate {
                    replace => {
                        "additional_notice.key" => "notice"
                        "additional_notice.value.string_value" => "%{notice}"
                    }
                }
                mutate {
                    merge => {
                        "event1.idm.read_only_udm.additional.fields" => "additional_notice"
                    }
                }
                mutate {
                    merge => {
                        "@output" => "event1"
                    }
                }
            }
        }
    }
    

You can then utilize this in a YARA-L detection engine rule as follows, and using the [Maps function](https://docs.cloud.google.com/chronicle/docs/yara-l/expressions#maps):
    
    
    events:
        // Corelight : Weird Log
        (
            $corelight.metadata.vendor_name = "Corelight" and
            $corelight.metadata.product_name = "Zeek" and
            // this requires a custom parser extension to extract notice
            $corelight.metadata.product_event_type = "weird" and
            $corelight.additional.fields["notice"] = "true"
        )
    

You must enable and turn on the authored rules for alerting. For more information, see [Run rule live data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
