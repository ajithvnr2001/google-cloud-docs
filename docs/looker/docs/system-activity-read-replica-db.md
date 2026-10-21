---
url: https://docs.cloud.google.com/looker/docs/system-activity-read-replica-db/
title: Creating a System Activity read replica database \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:57:39.969780+00:00
---

# Creating a System Activity read replica database  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/system-activity-read-replica-db/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a System Activity read replica database Stay organized with collections  Save and categorize content based on your preferences. 

The [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) feature is available only for Looker-hosted instances. For customer-hosted instances, you can create a read replica of the Looker backend database to gain some of the benefits of Elite System Activity.

> To use this option, your instance must be configured to [use a MySQL backend database](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql).
> 
> This option is available for customer-hosted instances only. For Looker-hosted instances, please [contact a Google Cloud sales specialist](https://cloud.google.com/contact).

To set up a read replica of your MySQL backend database and configure Looker to use the read replica for System Activity queries:

  1. Create a read replica of your MySQL backend database. For example, to create a MySQL read replica in AWS, follow the instructions in [Amazon's Working with Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) documentation. Save the DB instance identifier and port number, you'll need those to configure Looker in the next step.

  2. On your Looker instance, create a `yaml` file named `sa-db`, containing the following:
         
         dialect: mysql
         host: <DB instance identifier>
         username: root
         password: <password>
         database: looker
         port: <DB instance port>
         

  3. Stop Looker.

  4. Start Looker with the [startup option](https://docs.cloud.google.com/looker/docs/startup-options) `--internal-analytics-connection-file sa-db.yml`. This configures Looker to use the read replica database configured in `sa-db.yml` for System Activity queries.

  5. Optionally, you can also use the following startup options to modify your Elite System Activity configuration:

     * `--internal-analytics-retention-days=<number>`: By default, System Activity stores 90 days of historical data. Use this startup option to specify how many days of historical data System Activty will store. We do not recommend increasing data retention beyond 90 days, but you can reduce the length of data retention to improve performance. If you want to increase historical data retention beyond the default 90 days, ask your account executive about Looker hosting with the [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) option.

If you want more days than the default, ask your account executive about Looker hosting with the Elite System Activity option \- `--internal-analytics-connection-pool-size=<number>`: By default, System Activity queries are limited to a database connection pool size of 1, meaning that multiple System Analytics queries will queue and run serially in the backend database. This protects the internal database from being overloaded with System Analytics queries. Use this startup option to specify the number of concurrent System Analytics queries that can be run simultaneously. For example, 8.




Once configured to use the read replica database for System Activity queries, Looker will continue to use main MySQL database as the internal application database. System Activity dashboards and Explores will use the read replica database.

To verify that Looker is using the read replica database for System Activity queries:

  * If you change the password in the `sa-db.yml` file, System Activity queries will return an error.
  * On the MySQL database, you can run `show processlist;` to see the current running processes. The main Looker database should show many open connections that are in a sleep state, while the `looker__internal__analytics` database will show analytical queries.



> System Activity dashboards and Explores will use the read replica database, but the legacy `i__looker` Explores will still query the primary backend database. Update any saved Looks or dashboards that query `i__looker` to cause them to query System Activity. Use the methods described on this documentation page to ensure that any saved Looks and dashboards are querying the correct connection to the read replica database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-22 UTC."],[],[]] 
