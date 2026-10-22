---
url: https://docs.cloud.google.com/database-migration/docs/manage-profiles/
title: Manage connection profiles \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:07.299316+00:00
---

# Manage connection profiles  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/manage-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)



Send feedback 

#  Manage connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

**Alpha**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Review all connection profiles

All connection profiles can be reviewed from the connection profiles page. The connection profiles list presents all connection profiles created by any user, which haven't been deleted.

The connection profiles list displays a default set of high-level information for each connection profile, including:

  * The connection profile **display name**.

  * **Usage** indicates if the connection profile is in use by one or more active migration jobs, where an active migration job is any migration job that's not in "Completed" status. The number of jobs next to status indicates the total number of jobs (both active and inactive) referencing the connection profile.

  * The database **engine** which the connection profile is configured for (MySQL or PostgreSQL).

  * The **hostname** or **IP** , and **port** of the source database that the connection profile is representing.

  * When the connection profile was created.




In addition, the user may choose additional columns to display more information. To do this, click on the column selection button at the top-right corner of the connection profiles list. Additional columns available for display include:

  * The **username** with which Database Migration Service is connecting to the source database.

  * The method of **SSL/TLS configuration** used (none, server-only, or client-server).

  * When this connection profile was most recently **modified**.




## Perform actions on connection profiles

From the connection profiles list, users can drill into a specific connection profile to view detailed information and manage the connection profile.

Information available in the connection profiles details page includes:

  * List of migration jobs using the connection profile.

  * When the connection profile was created.

  * When the connection profile was last modified.

  * All the details provided during connection profile configuration, such as the hostname/IP and port, username, and SSL/TLS configuration.




Actions can be performed on a single connection profile from the connection profile view, or on multiple connection profiles from the connection profiles list view.

### Modify connection profile

Other than the engine type, any part of the connection profile definition can be modified at any time.

### Delete connection profile

To delete a connection profile, first delete the migration job(s) that are using the connection profile, and then delete the connection profile.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
