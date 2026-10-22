---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/mapping--modeling/
title: Map and model alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:03.757533+00:00
---

# Map and model alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/mapping--modeling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map and model alerts 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to map and model alerts for your events. By default, alerts aren't mapped and modeled, which is a necessary step to properly analyze security data. This process happens in the **Mapping and modeling** section of the Google Security Operations platform.

## Map your events

The following use case outlines how to map your events:

  1. From the **Cases** screen **Events** tab, select an event and click  settings  **Event Configuration**.
  2. Select modeling **Mapping & Modeling**. For this use case, map your data using the predefined family **MailRelayOrTAP** for email monitoring events. 



## Understand the mapping hierarchy

You can configure mapping and modeling at one of three levels. Mappings are inherited from the top down, so any mappings you apply at a higher level are automatically applied to all levels below it.

  * **Source** : The name of the source you provided earlier that ingested the data and created the alert. For example, your source might be called `Email Connector`. At this level, you only need to map the **Time** field—it's common across all stages. If you perform the mapping now, the subsequent stages—**Product - "Mail"** and **Event - "Suspicious email"** —automatically inherit the same mapping.
  * **Product** : The product is the application that ingests data from a specific source, for example, **Mail**. For example, a single connector can ingest data from multiple sources. If you map at this level, all subsequent events inherit the same mapping.
  * **Event** : This is the `event_name` you defined earlier, for example, **Suspicious email**. The event in this case is the email message itself.
  * For this use case, map all relevant fields at the **Product** level, assigning each field to the appropriate field in the code.

Target field | The field value | Extracted field | Transformation function  
---|---|---|---  
`DestinationUserName` | `event["destinationUserName"]` | `TO_STRING`| The email address of the person who received the email.  
`SourceUserName` | `event["sourceUserName"]` | `EXTRACT_BY_REGEX` format:  
  

    
    
    [\w\.-]+@[\w\.-]+

| The email address of the person who sent the email  
`EmailSubject` | `event["subject"]` | `TO_STRING` | The email subject  
`DestinationURL` | `event["found_url"]` | `TO_STRING` | URLs found in the email body  
`StartTime` | `event["startTime"]` | `FROM_UNIXTIME_STRING_OR_LONG` | Start time the email was received.  
`EndTime` | `event["endTime"]` | `FROM_UNIXTIME_STRING_OR_LONG` | End time the email was received.  
  
## Simulate and review your mapped alerts

After mapping your case, simulate the alert to see the mapping results, as follows:

  1. On the **Overview** tab of the alert, click more_vert**More** and select **Ingest alert as test case**. A new, simulated alert appears as a case in the case queue. All simulated cases tag with a **Test** marked next to the case name.
  2. Click more_vert  **More > Show Result** to see each mapped email message argument.
  3. Optional: Click **Explore** to visualize the entities and their relationships.
  4. After completing the connector mapping and modeling, enable the connector to begin automatic alert ingestion:
     1. Go to the **Connectors** page.
     2. Click the toggle to the on position
     3. Click **Save**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
