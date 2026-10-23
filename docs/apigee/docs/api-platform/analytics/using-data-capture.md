---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/
title: Collecting custom data with the DataCapture policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:29.711325+00:00
---

# Collecting custom data with the DataCapture policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Collecting custom data with the DataCapture policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

In addition to the [usual API data collected by Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview#what-kind-of-data-is-collected-and-analyzed), you can also collect custom data using the [DataCapture](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) policy. There are two main steps required, as described in the following sections:

  1. Create a Data Collector REST resource.
  2. Specify the data you want to collect  using the DataCapture policy's `<Collect>` element.

**Note** :If you have an Apigee organization with Pay-as-you-go billing, you must enable the Apigee API Analytics add-on to use this policy. For more information, see [Manage the Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on). 

If you are unsure whether you are using a Subscription or Pay-as-you-go Apigee organization, contact your Apigee organization administrator.

## Create a Data Collector REST resource

To use the `DataCapture` policy, you must first create a [ Data Collector](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.datacollectors) REST resource. To do so, send an API request like the following:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -X POST -H "content-type:application/json" \
      -d '
    {
      "name": "dc_my_custom_data",
      "description": "Collects data for analysis.",
      "type": "STRING",
    }' \
      "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/datacollectors"

This creates a resource named `dc_my_custom_data`, which you can use with the `DataCapture` policy.

**Notes:**

  * The name of the Data Collector resource must begin with the prefix `dc_`.
  * If you use a Data Collector in multiple policies, the captured data will be overwritten by the last policy that executes.

**Warning:** Do _not_ create two data collectors whose names differ only by case, such as `dc_my_data` and `dc_My_Data`, as then exporting data will result in a "duplicate column names" error.

## Specify the data to collect

You can specify the data to collect using the DataCapture policy's [ `<Collect>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#collect) element. There are various ways to do this, as shown in the [Examples](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#examples) section in the DataCapure reference page. One way is to specify a [flow variable](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference), which stores data passed in API requests and responses. For example, you could collect data that customers enter in a web page form using the flow variable `message.formparam.param_name.values`, where `param_name` is the name of a parameter in the form. Suppose the form has a parameter named `payment_amount`. The corresponding flow variable would be `message.formparam.payment_amount.values`.

The following code specifies this variable by the `ref` attribute of the `<Collect>` element.
    
    
    <DataCapture name="capturepayment">
        <Capture>
            <DataCollector>dc_my_custom_data</DataCollector>
            <Collect ref="message.form_param.payment_amount.values" >
        </Capture>
    </DataCapture>

With this setting, the data entered in the form's `payment_amount` field will be collected by DataCapture and stored in a variable named `dc_my_custom_data`.

## Creating a custom report from data collected with DataCapture

Once you have set up data collection with the DataCapture policy, you can use the data to create a custom report by the procedure described in [Adding a custom report](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports#add). To do so, when you select a metric for the report, as shown in [ step 4 of the procedure](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports#step4), choose the variable that has the same name as the Data Collector REST resource you created for DataCapture—for example, `dc_my_custom_data`.

You can also use the same variable as a dimension in a custom report. Since dimensions group data by the values of the variable, it is usually preferable for the variable to be a string that only takes on a limited number of values.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
