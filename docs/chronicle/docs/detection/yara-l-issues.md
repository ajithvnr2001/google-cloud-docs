---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-issues/
title: YARA-L 2.0 known issues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:01.976571+00:00
---

# YARA-L 2.0 known issues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# YARA-L 2.0 known issues

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for detection engineers who want to debug rule logic and optimize YARA-L 2.0 execution. It explains how to handle non-standard engine behaviors, such as field unnesting, Cartesian product expansion in aggregations, and enrichment eventual consistency. By following these methods, you can prevent logic errors that lead to inflated outcome values or missed detections.

YARA-L 2.0 uses a specific execution model where repeated fields are expanded into individual event rows during evaluation. Because this transformation happens at the engine level, referencing multiple repeated fields or performing arithmetic on unsigned UDM types requires specific syntax workarounds to avoid compiler errors or incorrect result sets. This document outlines those technical constraints and the required logic patterns to resolve them.

## Before you begin

Make sure your account has the following technical entitlements before testing or modifying YARA-L 2.0 rules:

### Required IAM roles

  * `roles/chronicle.viewer` (Security Operations Viewer): To view existing rules and detection metadata.
  * `roles/chronicle.editor` (Security Operations Editor): To modify rule logic and save changes.



### Required permissions

  * `chronicle.rules.runTest`: Required to execute the **Run Test** feature on historical data.

  * `chronicle.detections.get`: To inspect the output of unnested events in the detection dashboard.




## Key terminology

  * **UDM (Unified Data Model):** The normalized schema used to structure all ingested security telemetry across the platform.
  * **Unnesting:** The engine-level expansion of a single UDM event containing a repeated field (array) into multiple rows. Each row represents a unique element from the array, which can lead to row multiplication during rule evaluation.
  * **T₀ (initial run):** The first execution of a rule on incoming telemetry. This occurs during the "streaming" phase, often before background enrichment processes (like GeoIP or ASN true-ups) are finalized.



## Outcome aggregations with repeated field unnesting

When a rule references a repeated field in an event variable with multiple elements, each element splits into a separate event row.

For example, the two IP addresses in the repeated field `target.ip` on event `$e` are split into two instances of `$e`, each with a different `target.ip` value.
    
    
    rule outbound_ip_per_app {
      meta:
    
      events:
        $e.principal.application = $app
    
      match:
        $app over 10m
    
      outcome:
        $outbound_ip_count = count($e.target.ip) // yields 2.
    
      condition:
        $e
    }
    

### Event records: Before and after unnesting

The tables in this section demonstrate how a single event containing an array of IP addresses is transformed into two distinct records.

#### Before unnesting

The following table shows the event record before unnesting the repeated field:

metadata.id | principal.application | target.ip  
---|---|---  
`aaaaaaaaa` | `Google SecOps` | `[192.0.2.20`, `192.0.2.28]`  
  
#### After unnesting

The following table shows the event record after unnesting the repeated field:

metadata.id | principal.application | target.ip  
---|---|---  
`aaaaaaaaa` | `Google SecOps` | `192.0.2.20`  
`aaaaaaaaa` | `Google SecOps` | `192.0.2.28`  
  
### Nested repeated fields (Cartesian product)

When a rule references a repeated field nested within another, like `security_results.action`, the unnesting occurs at both levels (parent and child) simultaneously. This results in a Cartesian product of all elements.

In the following example, an event `$e` with two repeated values on `security_results` and two repeated values on `security_results.actions` are unnested into four instances.
    
    
    rule security_action_per_app {
      meta:
    
      events:
        $e.principal.application = $app
    
      match:
        $app over 10m
    
      outcome:
        $security_action_count = count($e.security_results.actions) // yields 4.
    
      condition:
        $e
    }
    

#### Event record before nested unnesting

The original record stores the actions within a nested array structure.

metadata.id | principal.application | security_results  
---|---|---  
`aaaaaaaaa` | `Google SecOps` | `[ { actions: [ ALLOW, FAIL ] }`, `{ actions: [ CHALLENGE, BLOCK ] } ]`  
  
#### Event records after nested unnesting

After expansion, each unique action becomes its own row, which can lead to unexpected counts in non-distinct aggregations.

metadata.id | principal.application | security_results.actions  
---|---|---  
`aaaaaaaaa` | `Google SecOps` | ALLOW  
`aaaaaaaaa` | `Google SecOps` | FAIL  
`aaaaaaaaa` | `Google SecOps` | CHALLENGE  
`aaaaaaaaa` | `Google SecOps` | BLOCK  
  
### Impact on unrelated fields

This unnesting behavior in rule evaluation can produce unexpected outcome aggregations when the rule references one or more repeated fields with a parent field that is also a repeated field. Non-distinct aggregations like `sum()`, `array()`, and `count()` can't account for duplicate values on other fields on the same event produced by the unnesting behavior.

In the following example, event `$e` has a single hostname (`google.com`), but the outcome (`hostnames`) aggregates over unnested four instances of the same event `$e`, each with a duplicate `principal.hostname` value. This outcome yields four hostnames (instead of one) due to the unnesting of repeated values on `security_results.actions`.
    
    
    rule security_action_per_app {
      meta:
    
      events:
        $e.principal.application = $app
    
      match:
        $app over 10m
    
      outcome:
        $hostnames = array($e.principal.hostname) // yields 4.
        $security_action_count = count($e.security_results.action) // yields 4.
    
      condition:
        $e
    }
    

#### Event record before unnesting with unrelated fields

The hostname is a single value, but it sits alongside the repeated security results.

metadata.id | principal.application | principal.hostname | security_results  
---|---|---|---  
`aaaaaaaaa` | `Google SecOps` | `google.com` | `[ { action: [ ALLOW, FAIL ] }`, `{ action: [ CHALLENGE, BLOCK ] } ]`  
  
#### Event record after unnesting with unrelated fields

The hostname is now duplicated across four rows, causing the `array()` function to pick it up four times.

metadata.id | principal.application | principal.hostname | security_results.action  
---|---|---|---  
`aaaaaaaaa` | `Google SecOps` | `google.com` | ALLOW  
`aaaaaaaaa` | `Google SecOps` | `google.com` | FAIL  
`aaaaaaaaa` | `Google SecOps` | `google.com` | CHALLENGE  
`aaaaaaaaa` | `Google SecOps` | `google.com` | BLOCK  
  
### Workaround for unnesting behavior

To make sure your outcome values are accurate when unnesting occurs, use the distinct version of your selected aggregation. The following functions ignore the duplicate rows created by unnesting:

  * `max()`
  * `min()`
  * `array_distinct()`
  * `count_distinct()`



## Outcome aggregations with multiple event variables

If a rule contains multiple event variables, there is a separate item in the aggregation for each combination of events that is included in the detection. For example, if the following example rule is run against the listed events:
    
    
    events:
      $e1.field = $e2.field
      $e2.somefield = $ph
    
    match:
      $ph over 1h
    
    outcome:
       $some_outcome = sum(if($e1.otherfield = "value", 1, 0))
    
    condition:
      $e1 and $e2
    
    
    
    event1:
      // UDM event 1
      field="a"
      somefield="d"
    
    event2:
      // UDM event 2
      field="b"
      somefield="d"
    
    event3:
      // UDM event 3
      field="c"
      somefield="d"
    

The sum is calculated over every combination of events, letting. you use both event variables in the outcome value calculations. The following elements are used in the calculation:
    
    
    1: $e1 = event1, $e2 = event2
    2: $e1 = event1, $e2 = event3
    3: $e1 = event2, $e2 = event1
    4: $e1 = event2, $e2 = event3
    5: $e1 = event3, $e2 = event1
    5: $e1 = event3, $e2 = event2
    

This results in a potential maximum sum of 6, even though $e2 can only correspond to 3 distinct events.

This affects sum, count, and array. For count and array, using `count_distinct` or `array_distinct` can solve the issue, but there is no workaround for sum.

## Parentheses at the start of an expression

Beginning an expression with parentheses is unsupported and triggers a parsing error in the rule editor.

#### Invalid syntax
    
    
    parsing: error with token: ")"
    invalid operator in events predicate
    

The following example generates this type of error:
    
    
    ($event.metadata.ingested_timestamp.seconds -
    $event.metadata.event_timestamp.seconds) / 3600 > 1
    

#### Valid syntax variations

The following syntax variations return the same result, but with valid syntax:
    
    
    $event.metadata.ingested_timestamp.seconds / 3600 -
    $event.metadata.event_timestamp.seconds / 3600 > 1
        1 / 3600 * ($event.metadata.ingested_timestamp.seconds -
    $event.metadata.event_timestamp.seconds) > 1
        1 < ($event.metadata.ingested_timestamp.seconds -
    $event.metadata.event_timestamp.seconds) / 3600
    

## Index array in outcome requires aggregation

Directly indexing an array within the `outcome` section for repeated fields isn't permitted. It requires a temporary placeholder variable.
    
    
    outcome:
      $principal_user_dept = $suspicious.principal.user.department[0]
    

#### Workaround

Capture the specific array index into a placeholder variable within the `events` section, then reference that placeholder in your outcome.
    
    
    events:
      $principal_user_dept = $suspicious.principal.user.department[0]
    
    outcome:
      $principal_user_department = $principal_user_dept
    

## `OR` condition with non-existence

If you apply an `OR` condition between two separate event variables and if the rule matches on non-existence, the rule successfully compiles, but can produce false positive detections.

For example, the following rule syntax can match events having `$event_a.field = "something"` even though it shouldn't:
    
    
    events:
         not ($event_a.field = "something" **or** $event_b.field = "something")
    condition:
         $event_a and #event_b >= 0
    

#### Workaround

Separate the non-existence checks into individual blocks for each variable to maintain logic integrity.
    
    
    events:
      not ($event_a.field = "something")
      not ($event_b.field = "something")
    
    condition:
      $event_a and #event_b >= 0
    

## Arithmetic with unsigned event fields

If you try to use an integer constant in an arithmetic operation with a UDM field whose type is an unsigned integer, you will get an error. For example:
    
    
    events:
      $total_bytes = $e.network.received_bytes * 2
    

Standard integer constants default to signed integers, which are incompatible with UDM fields defined as unsigned integers, like `network.received_bytes`.

#### Workaround

You can bypass this error by forcing the integer constant to behave as a float through a division operation.
    
    
    events:
      $total_bytes = $e.network.received_bytes * (2/1)
    

## GeoIP enrichment and eventual consistency

The system prioritizes speed over immediate accuracy in the initial enrichment stages (Streaming and Latency-Sensitive), which can lead to missing data and potential false positives. The system continues to enrich the data in the background, but the data may not be available when the rule is run. This is part of the normal [eventual consistency](https://docs.cloud.google.com/chronicle/docs/detection/use-enriched-data-in-rules#eventual-consistency) process.

To prevent false positives caused by enrichment lag, explicitly check that the field is not empty before evaluating its value.

For example, consider this rule event:
    
    
    $e.principal.ip_geo_artifact.network.asn = "16509" AND
    $e.principal.ip_geo_artifact.location.country_or_region = "United Kingdom"
    

The rule relies on the fact that the event must have `$e.principal.ip_geo_artifact.network.asn = "16509"` AND `$e.principal.ip_geo_artifact.location.country_or_region = "United Kingdom"` which are both enriched fields. If the enrichment is not completed in time, the rule will produce a false positive.

To avoid this, a better check for this rule would be:
    
    
    $e.principal.ip_geo_artifact.network.asn != "" AND
    $e.principal.ip_geo_artifact.network.asn = "16509" AND
    $e.principal.ip_geo_artifact.location.country_or_region != "" AND
    $e.principal.ip_geo_artifact.location.country_or_region = "United Kingdom"
    

This rule eliminates the possibility of the event being triggered by IPs with the [ASN 16509](https://www.ipqualityscore.com/asn-details/AS16509/amazon-com-inc#:%7E:text=AS16509%20is%20an%20autonomous%20system,addresses%20active%20in%20the%20network) but located outside the UK. This improves the overall precision of the rule.

Learn how to troubleshoot the enrichment lag.

## Troubleshooting

This section outlines performance expectations and provides self-service fixes for common issues where live detection behavior differs from test results.

### Future-dated events

Multi-event rules are designed to process events in chronological order relative to ingestion. If you specify and activate a multi-event rule, it doesn't create detections for events with future timestamps, for example when the `event.timestamp` has a date and time set after the `ingest.timestamp`.

### Enrichment lag

Google SecOps prioritizes ingestion speed to expose initial alerts as quickly as possible. However, background enrichment processes, such as resolving `GeoIP`, `ASN`, or `UDM` metadata, follow an eventual consistency model.

#### Initial run (T₀)

The live engine may evaluate a rule before background enrichment is complete. Depending on whether your logic relies on enriched fields for detections or exclusions, this can lead to the following temporary discrepancies:

  * **False negatives (detection lag)** : This is a common result. If a rule depends on an enriched field to trigger (for example, `target.user.department == "Finance"`), and that field is `null`, the rule doesn't match during the initial run.

  * **False positives (exclusion miss)** : If your rule uses enriched fields to filter out known-good activity (for example, `NOT target.ip_geo_country == "US"`), the rule may trigger a false positive because the "exclusion" data hasn't been applied yet.




#### True-up runs

These background runs re-evaluate the data after a delay (for example, 4 hours or 30 hours). This "trues up" the detection states as follows:

  * **Late detections** : Events that were "false negatives" at T₀ now produce a detection once the enrichment is finalized.

  * **Correction** : Any T₀ false positives remain in the system, but the fully enriched data is visible in the UDM viewer for manual triaging.




#### Run test discrepancy

The **Run Test** tool operates on historical data that has already reconciled. Because the data is fully enriched by the time you run a manual test, you can see the "true-up" results immediately. This means you won't see the T₀ false negatives or exclusion-based false positives that occurred during the live initial run.

### Error remediation

Use the following table to resolve discrepancies between live alerts and test results.

Issue | Description | Actionable fix  
---|---|---  
**Exclusion failure** | A rule fires despite an exclusion (for example, `!= "ASN_123"`) because the field was null during the initial run. |  Add a not null check to the events section to make sure data is enriched before evaluation, for example:  
  
`$e.principal.ip_geo_artifact.network.asn != ""`  
**Live compared to test match** | Live rules trigger alerts, but Run Test on the same data shows `"No Results`". | Add `$e.field != ""` which checks for all enriched fields (`GeoIP`, `ASN`, `File Path`) to synchronize live and historical behavior.  
**Missing metadata** | Detections appear in the dashboard with empty `GeoIP` or `File Path` fields. |  This is expected for **T 0** runs. To fix, include a `field != ""` check or configure a settlement delay in your rule schedule to allow more time for ingestion.   
  
### Validation and testing

To verify that a rule is correctly handling delayed enrichment, do the following:

  1. **Identify the lag:** Locate a detection you believe is a false positive. In the **Detection Type** column, check for the `<span class="material-icons">lightbulb</span>` icon. Alerts without this icon are from the primary run where enrichment lag is most common.

  2. **Update the rule logic:** Add a `field != ""` check for all enriched data points used in your logic.  
**Example (file path):**   
`$e.target.process.parent_process.file.full_path != ""`

  3. **Test and verify:**

     * Use the **Run Test** feature to make sure your logic still matches the intended historical data.
     * Verify that the rule now only triggers (or correctly excludes) during the true-up runs once the enrichment fields are populated.



For more information, see [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency) and [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
