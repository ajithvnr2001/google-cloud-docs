---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-plan-maintenance-windows/
title: Plan maintenance windows \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:52.369054+00:00
---

# Plan maintenance windows  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-plan-maintenance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Plan maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped offers you the ability to configure maintenance windows to schedule times for automatic updates. Maintenance windows are designed to target times where a brief downtime causes the lowest impact to your database clusters. You can schedule maintenance windows based on day of the week and hour, and length in which the maintenance window is open. For example, you could set a maintenance window to start at 3:00 AM on Tuesdays that spans eight hours.

You can also plan maintenance exclusions, which prevents disruptions to your workloads during date ranges where, due to unique circumstances, you don't want to allow the set maintenance window.

## Create a maintenance window

To create a maintenance window for your database cluster, complete the following steps:

###  Console 

  1. From the navigation menu of the GDC console, choose **Database Service**.

  2. Select the database cluster that you want to plan maintenance settings for.

  3. In the **Maintenance** section, click edit **Edit**.

  4. Select the **Start time** and **Length** for the maintenance window. Also select the days of the week to apply the maintenance window for.

**Important:** Due to other possible processes running when the maintenance window opens for your database cluster, automatic updates for your database cluster could have a delayed start. The maintenance window length defines when the maintenance processes can start. After maintenance on the database cluster starts, the process runs until completion, possibly running past the defined maintenance window.

![Create a maintenance window](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/maintenance-window-dbs.png)

  5. To apply a maintenance exclusion, click **Add Maintenance Exclusion**.

  6. Give the exclusion a name and define the time window to exclude for your maintenance window.

  7. Click **Save**.




###  gdcloud 

  1. To create a maintenance window for your database cluster, run:
         
         gdcloud maintenance policies create POLICY_NAME \
             --project PROJECT_ID \
             --weekly-cycle-days DAYS_OF_WEEK \
             --weekly-cycle-start-time START_TIME \
             --weekly-cycle-duration DURATION
         

Replace the following:

     * `POLICY_NAME`: The name of the maintenance policy.
     * `PROJECT_ID`: The ID of the project in which to create the maintenance policy.
     * `DAYS_OF_WEEK`: Comma-separated list of days of the week when maintenance can begin. Accepted values are RFC-822 formatted days of the week, such as `Mon`.
     * `START_TIME`: The time of the day, in UTC timezone, when maintenance can begin. The value must follow the `hh:mm` format, such as `20:36`.
     * `DURATION`: The maximum duration that the maintenance can last for, such as `2h3m`.
  2. To apply a maintenance exclusion to your maintenance window, run:
         
         gdcloud maintenance policies update POLICY_NAME \
             --project PROJECT_ID \
             --add-exclusion-name EXCLUSION_NAME \
             --add-exclusion-start START_TIME \
             --add-exclusion-end END_TIME
         

Replace the following:

     * `POLICY_NAME`: The name of the maintenance policy.
     * `PROJECT_ID`: The ID of the project in which to create the maintenance policy.
     * `EXCLUSION_NAME`: The name of the new maintenance exclusion to add.
     * `START_TIME`: The start date and time for the new maintenance exclusion. Accepted values must follow the RFC-3339 formatted timestamp, such as `2006-01-02T15:04:05Z`.
     * `END_TIME`: The end date and time for the new maintenance exclusion. Accepted values must follow the RFC-3339 formatted timestamp, such as `2006-01-02T15:04:05Z`.
  3. To attach the maintenance policy to your database cluster, run:
         
         gdcloud maintenance policy-bindings create POLICY_BINDING_NAME \
             --project PROJECT_ID \
             --policy-name POLICY_NAME \
             --resource-name RESOURCE_NAME
         

Replace the following:

     * `POLICY_BINDING_NAME`: The name of the policy binding resource.
     * `PROJECT_ID`: The ID of the project in which to create the maintenance policy.
     * `POLICY_NAME`: The name of the maintenance policy created in the previous step.
     * `RESOURCE_NAME`: The resource name to bind to. For example, for a database cluster named `my-cluster`, the resource name would be the following:

       * PostGreSQL: `DBClusters.postgresql.dbadmin.gdc.goog/my-cluster`
  4. Verify the maintenance policy exists and reflects your intended configuration:
         
         gdcloud maintenance policies list --project PROJECT_ID
         

  5. Verify the policy binding exists, and its `Valid` condition is `True`:
         
         gdcloud maintenance policy-bindings list --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project in which to create the maintenance policy.




## Remove a maintenance window

To remove a maintenance window for your database cluster, complete the following steps:

###  Console 

  1. From the navigation menu of the GDC console, choose **Database Service**.

  2. Select the database cluster that you want to plan maintenance settings for.

  3. In the **Maintenance** section, click edit **Edit**.

  4. In the **Length** field, select **24h**.

  5. Select all the days of the week.

  6. Click **Save**.




This removes the defined maintenance window and allows maintenance updates to start at any time.

###  gdcloud 

  1. To remove a maintenance window from your database cluster, run:
         
         gdcloud maintenance policies delete POLICY_NAME \
             --project PROJECT_ID
         

Replace the following:

     * `POLICY_NAME`: The name of the maintenance policy.
     * `PROJECT_ID`: The ID of the project in which the maintenance policy exists.
  2. Remove the maintenance policy binding from the database cluster:
         
         gdcloud maintenance policy-bindings delete POLICY_BINDING_NAME \
             --project PROJECT_ID
         

Replace the following:

     * `POLICY_BINDING_NAME`: The name of the maintenance policy binding.
     * `PROJECT_ID`: The ID of the project in which the maintenance policy exists.



## Manage maintenance exclusions

If you created a maintenance exclusion for your maintenance window, you can edit or remove the exclusion without affecting the maintenance window. To edit or remove a maintenance exclusion, complete the following steps:

###  Console 

  1. From the navigation menu of the GDC console, choose **Database Service**.

  2. Select the database cluster that you want to manage a maintenance exclusion for.

  3. In the **Maintenance** section, click edit **Edit**.

  4. Edit the date ranges and start times of the exclusion. If you want to delete the exclusion, click delete **Delete**.

![Manage a maintenance exclusion](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/maintenance-exclusion-dbs.png)

  5. Click **Save** to save your maintenance exclusion modifications to the maintenance window.




###  gdcloud 

The gdcloud CLI only supports adding and deleting maintenance exclusions. Therefore, you must delete the existing exclusion and add a new one if you want to modify your exclusion date range or times.

  1. To delete a maintenance exclusion, run:
         
         gdcloud maintenance policies update POLICY_NAME \
             --project PROJECT_ID \
             --remove-exclusion-name EXCLUSION_NAME
         

Replace the following:

     * `POLICY_NAME`: The name of the maintenance policy.
     * `PROJECT_ID`: The ID of the project in which to delete the maintenance policy's exclusion.
     * `EXCLUSION_NAME`: The name of the maintenance exclusion to delete.
  2. To add a new maintenance exclusion to apply any previous exclusion edits, run:
         
         gdcloud maintenance policies update POLICY_NAME \
             --project PROJECT_ID \
             --add-exclusion-name EXCLUSION_NAME \
             --add-exclusion-start START_TIME \
             --add-exclusion-end END_TIME
         

Replace the following:

     * `POLICY_NAME`: The name of the maintenance policy.
     * `PROJECT_ID`: The ID of the project in which the maintenance policy exists.
     * `EXCLUSION_NAME`: The name of the new maintenance exclusion to add.
     * `START_TIME`: The start date and time for the new maintenance exclusion. Accepted values must follow the RFC-3339 formatted timestamp, such as `2006-01-02T15:04:05Z`.
     * `END_TIME`: The end date and time for the new maintenance exclusion. Accepted values must follow the RFC-3339 formatted timestamp, such as `2006-01-02T15:04:05Z`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
