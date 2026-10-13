---
url: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.BigtableConfig.State
title: Class State (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:06.091136+00:00
---

# Class State (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.BigtableConfig.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class State (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.2  2.38.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.3  2.26.1  2.25.2  2.23.1  2.22.0  2.21.5  2.20.3  2.19.8  2.18.4  2.17.1  2.16.1  2.15.2  2.14.1  2.13.12  2.12.1  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.1  2.5.0  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.7.2  1.6.1  1.5.0  1.4.3  1.3.1  1.2.0  1.1.0  1.0.2  0.45.0  0.44.0  0.43.0 
    
    
    State(value)

Possible states for a Bigtable subscription. Note: more states could be added in the future. Please code accordingly.
    
    
        - The Bigtable instance, table, or app profile does not
          exist.
        - The Pub/Sub service agent has not been granted the
          `appropriate Bigtable IAM permission
          bigtable.tables.mutateRows <{$universe.dns_names.final_documentation_domain}/bigtable/docs/access-control#permissions>`__
        - The bigtable.googleapis.com API is not enabled for the
          project
          (`instructions <{$universe.dns_names.final_documentation_domain}/service-usage/docs/enable-disable>`__)
    SCHEMA_MISMATCH (5):
        Cannot write to Bigtable because of a missing column family
        (`data`), or if there is no structured row key for the
        subscription name + message ID, if because the app profile
        is not configured for single-cluster routing.
    IN_TRANSIT_LOCATION_RESTRICTION (6):
        Cannot write to the destination because enforce_in_transit
        is set to true and the destination locations are not in the
        allowed regions.
    VERTEX_AI_LOCATION_RESTRICTION (7):
        Cannot write to Bigtable because the table is not in the
        same location as where Vertex AI models used in
        `message_transform`\ s are deployed.
    

## Enums  
  
---  
**Name** | **Description**  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`ACTIVE` | The subscription can actively send messages to Bigtable.  
`NOT_FOUND` | Unused in the current implementation. Placeholder for future use.  
`APP_PROFILE_MISCONFIGURED` | Unused in the current implementation. Placeholder for future use.  
`PERMISSION_DENIED` | Cannot write to Bigtable because of permission denied errors. This can happen if:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
