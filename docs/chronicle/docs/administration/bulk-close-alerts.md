---
url: https://docs.cloud.google.com/chronicle/docs/administration/bulk-close-alerts/
title: Close alerts in bulk \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:52:03.389372+00:00
---

# Close alerts in bulk  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/bulk-close-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Close alerts in bulk

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to programmatically close a large number of alerts using the Google Security Operations REST API. Google recommends using this method for situations where closing alerts in the platform would be too time-consuming.

#### Prerequisites

Before you start, make sure you have the following:

  * **Python Environment:** You will need Python installed to run the sample scripts.
  * **API Samples:** Access to the `api-samples-python` [GitHub repository](https://github.com/chronicle/api-samples-python).
  * **Credentials:** A valid credentials file (for example `.chronicle_credentials.json`).
  * **jq:** A command-line JSON processor used to parse the API output.



#### Search for Detections

First, you must identify the alerts (alerting detections) you want to close. You use the `list_detections.py` script to find detections associated with a specific Rule ID.

  1. Locate your Rule ID and Project details.
  2. Run the script to output the detections to a JSON file. The JSON filename can either be `detections.json` or `temp.json`.



**Command:**
    
    
    python -m detect.v1alpha.list_detections \
      --project_id=$PROJECT_ID \
      --project_instance=$PROJECT_INSTANCE \
      --credentials_file=$CREDENTIALS_FILE \
      --rule_id=$RULE_ID \
      > ip_in_abuseipdb_out.json
    

**Note:** This script supports pagination if you have more than 1,000 results.

#### Extract Detection IDs

The bulk update script requires a plain text file containing one detection ID per line. The previous step created a JSON file, which you must now convert to a text file.

  1. Use `jq` to extract the detection IDs (which start with `de_`) from the JSON array.
  2. Save the output to a text file.



**Command:**
    
    
    cat ip_in_abuseipdb_out.json | jq -r '.detections[].id' \
      > ip_in_abuseipdb_out.txt
    

This creates a file listing IDs, for example `de_ad9d2771-a567...`..

#### Configure Feedback ("close" Action)

When you close an alert, the "feedback" status is set to `CLOSED`.

  * **Default Behavior:** The `bulk_update_alerts.py` script uses a hard-coded default feedback payload: 
    * **Status:** `CLOSED`
    * **Reason:** `REASON_MAINTENANCE`
    * **Comment:** `automated cleanup`.
  * **Customization:** If you need to change the verdict (for example to `FALSE_POSITIVE`) or the comment, you can: 
    * Directly edit the `DEFAULT_FEEDBACK` dictionary in the Python file.
    * Pass CLI parameters (e.g., `--verdict="FALSE_POSITIVE"`) to override specific values.



#### Execute Bulk Close

Run the bulk update script using the text file you created before (See [Extract Detection IDs](https://docs.cloud.google.com/chronicle/docs/administration/bulk-close-alerts?tab=t.0#heading=h.rybvp6jqttdz)). This script calls the `UpdateAlert`method for each ID in your list.

**Command:**
    
    
    python -m detect.v1alpha.bulk_update_alerts \
      --project_id=$PROJECT_ID \
      --project_instance=$PROJECT_INSTANCE \
      --credentials_file=$CREDENTIALS_FILE \
      --alert_ids_file="$(pwd)/ip_in_abuseipdb_out.txt"
    

#### Verify Closure (Optional)

To verify the alerts were closed successfully, you can check the details of a single alert using the `get_alert.py` module.

**Command:**
    
    
    python -m detect.v1alpha.get_alert \
      --project_id=$PROJECT_ID \
      --project_instance=$PROJECT_INSTANCE \
      --credentials_file=$CREDENTIALS_FILE \
      --alert_id=$ALERT_ID
    

**Expected Result:** The JSON output contains a `feedbackSummary` object showing `"status": "CLOSED"` and your specified comment (for example "automated cleanup").

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
