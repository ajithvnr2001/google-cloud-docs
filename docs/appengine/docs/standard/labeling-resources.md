---
url: https://docs.cloud.google.com/appengine/docs/standard/labeling-resources/
title: Labeling App Engine resources \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:43.712447+00:00
---

# Labeling App Engine resources  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/labeling-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Labeling App Engine resources Stay organized with collections  Save and categorize content based on your preferences. 

Labels are a lightweight way to group together resources that are related or associated with each other. You can use labels to get a more fine-grained view of how resources are billed for your App Engine services. You can also take advantage of features like nested filtering to perform more precise searches for your resources.

Here are some ways you can use labels:

  * Label the types of services you create. For example, if you add labels such as `service:default`, `service:backend` and `service:frontend` to your App Engine services, you can compare how these different services use outgoing bandwidth, instance hours, and other [resources](https://docs.cloud.google.com/appengine/docs/standard/quotas#Resources).

  * Label by team or cost center to distinguish projects owned by different teams. This can be used in cost accounting or budgeting. For example, `team:marketing` and `team:research`.

  * Label the environment a service is running in. For example, `environment:prod` and `environment:test`.

  * Label by owner or primary contact if there's an individual who is responsible for a resource.

  * Label the status of a service. For example, `state:inuse` and `state:readyfordeletion`.




Labels can be used only for billing data and not for any other tools, such as the Metrics Explorer.

## Restrictions

  * You can assign up to 64 labels to each resource.
  * You can only explicitly label services. Versions and instances inherit labels from their parent service.
  * The App Engine flexible environment does not support billing labels for Firestore in Datastore mode (Datastore) usage. 



## Adding or modifying labels

To add labels to App Engine services:

### Console

  1. Go to the App Engine Services page.

[Go to Services](https://console.cloud.google.com/appengine/services)

  2. Select the checkboxes next to the services you want to label.

  3. Click **Show info panel** and select the **Labels** tab to expand the labels column.

  4. Click **Add label** to add a key-value pair to the services you selected. For example, to add the label `env:prod`, enter `env` for the **Key** and `prod` for the **Value**.

  5. Save your changes.




### Admin API

You can add and set labels through the `Service` resource. Refer to the Admin API reference documentation:

  * [REST API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#resource:-service)
  * [RPC API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#service)



## Viewing billing data associated with your labeled services

You can add granularity to billing data for your application using labels. For example, you can view the costs for a specific resource, such as the outgoing bandwidth, broken down by day and by service. This can give you insight into daily application costs and allow you to optimize your application's resource use.

To view labels for billing, export your data to BigQuery and then query the data:

  1. [Export your billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

After you enable the BigQuery export, it might take a few hours to see your data.

  2. From the [BigQuery page in the Google Cloud console](https://console.cloud.google.com/bigquery), select your project and billing dataset.

  3. Run a query against the table created from your BigQuery export.




Labels are added to your dataset as repeated fields, which that means multiple labels can be attached to a single row in your cost dataset. To easily query by label, you might want to [FLATTEN](https://docs.cloud.google.com/bigquery/docs/legacy-nested-repeated#flatten) the table on the labels field.

For example, the following query pulls cost data, the label key, and the label value for outgoing bandwidth where a label exists:
    
    
    SELECT
      product,
      resource_type,
      start_time,
      end_time,
      labels.key,
      labels.value,
      cost
    FROM (FLATTEN([YOUR_DATASET.TABLEID], labels))
    WHERE
      cost > 0.0
      and labels.key is not null
      and resource_type = 'Out Bandwidth'
    LIMIT 100
    

BigQuery returns your data with a flattened output:

product | resource_type | start_time | end_time | labels_key | labels_value | cost  
---|---|---|---|---|---|---  
App Engine | Out Bandwidth | 2017-10-07 22:00:00 | 2017-10-07 23:00:00 | service | default | 0.020033  
App Engine | Out Bandwidth | 2017-10-07 13:00:00 | 2017-10-07 14:00:00 | service | frontend | 0.016042  
App Engine | Out Bandwidth | 2017-10-07 06:00:00 | 2017-10-07 07:00:00 | service | backend_task | 0.013125  
App Engine | Out Bandwidth | 2017-10-07 21:00:00 | 2017-10-07 22:00:00 | service | default | 0.020722  
App Engine | Out Bandwidth | 2017-10-07 19:00:00 | 2017-10-07 20:00:00 | service | frontend | 0.020725  
App Engine | Out Bandwidth | 2017-10-08 04:00:00 | 2017-10-08 05:00:00 | service | backend_task | 0.02072  
App Engine | Out Bandwidth | 2017-10-08 02:00:00 | 2017-10-08 03:00:00 | service | default | 0.020723  
App Engine | Out Bandwidth | 2017-10-07 14:00:00 | 2017-10-07 15:00:00 | service | frontend | 0.020724  
App Engine | Out Bandwidth | 2017-10-07 23:00:00 | 2017-10-08 00:00:00 | service | backend_task | 0.021417  
  
### Time periods in billing reports

To ensure that each day in the report covers a full 24 hour period, the billing data that you export only contains data up to the most recent midnight, Pacific Time. For example, if you export billing data at noon on December 3rd, the export includes data up to December 2nd, 11:59 PM.

For each day in the report, billing data is attributed to labels that exist at the beginning of the day. For example, if you create a label at noon Pacific Time on December 3rd, the report for December 3rd will not attribute data to the label since the label did not exist at the beginning of the day. Data will be attributed to the label starting December 4th.

Labels created at noon and removed in the same 24 hour period will not have data attributed to it.

## Viewing labels in the Google Cloud console

After you label resources, you can view the labels in the Google Cloud console.

  1. Go to the App Engine Services page.

[Go to Services](https://console.cloud.google.com/appengine/services)

  2. For each service, you can see all the labels in the **Labels** column.




## Removing labels

To remove labels from services:

  1. Go to the App Engine Services page.

[Go to App Engine Services](https://console.cloud.google.com/appengine/services)

  2. Select the checkboxes next to the services for which you want to remove labels.

  3. Click **Show info panel** and select the **Labels** tab to expand the labels column.

  4. Click the **X** next to all the labels you want to remove.

  5. Save your changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
