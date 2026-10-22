---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-alerts/
title: Manage billing alerts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:42.047141+00:00
---

# Manage billing alerts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage billing alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page covers creating and silencing Billing alerts and alert rules.

## Before you begin

Before continuing, ensure you have the following required role:

  * **MonitoringRule PA Creator** : create and manage `MonitoringRule` custom resources. Ask your IAM Org Admin to grant you the `monitoringrule-pa-creator` role.



## Create alert rules

You can create alert rules based on invoice metrics and your spend thresholds using the [`MonitoringRule`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/monitoring/v1/monitoring-v1#monitoringrule) resource in the [Observability API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/observability-api-overview).

See [Create alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-alert-rules#create-rules) for instructions on creating alerts using the GDC console.

To create an alert rule, work through the following steps:

  1. Create a YAML file, and add in the `MonitoringRule` resource and the following contents:
         
         apiVersion: monitoring.gdc.goog/v1
         kind: MonitoringRule
         metadata:
           name: MONITORING_RULE_NAME
           namespace: PROJECT
         spec:
           interval: INTERVAL
           limit: LIMIT
           alertRules:
           - alert: ALERT
             expr: EXPRESSION
             labels:
               severity: SEVERITY
               code: BILLING_CODE
               resource: BILLING
             annotations:
               message: MESSAGE
         

Replace the following variables:

Variable | Description  
---|---  
MONITORING_RULE_NAME | The name of the monitoring rule.   
  
For example: `invoice-total-cost`.  
PROJECT | The project namespace of where the invoice resides.   
  
For example: `platform-obs`.  
INTERVAL | The length of time the alert re-runs in a given period.   
  
For example: `60s` defines that the alert runs every sixty seconds.  
LIMIT | The amount of times an alert can run.   
  
For example: `0` for no limit.  
ALERT | The alert name.   
  
For example: `invoice_total_cost_approaching_limit`.  
EXPRESSION | The PromQL expression to describe the alert rule. To retrieve a PromQL expression, see [Query alerts from the HTTP API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-alerts#query-alerts-from-http-api).   
  
For example, to set an alert rule with a spend threshold at 80% of your $500,000 budgeted amount, use the following expression:   
  
`sum(metering_invoice_line_item_total_cost{task_order_number="TASK_ORDER", clin_number="CLIN"}) / 500000 > 0.8`   
  
Replace TASK_ORDER with your task order and CLIN with your contract line item number.  
SEVERITY | The severity of the alert rule. Severity values include `error`, `critical`, `warning`, and `info`.  
BILLING_CODE | The billing code you define for the alert rule.   
  
For example: `"BILLING-100"`.  
MESSAGE | A description of the alert that appears when the alert rule runs.   
  
For example: `"Spending exceeded limit"`.  
  2. Apply the contents of the YAML file and set the alert rule:
         
         kubectl apply -f FILENAME.yaml
         




## Create spend threshold alerts

Your Infrastructure Operator (IO) creates spend threshold alert policies in the GDC console. Spend threshold alerts are custom billing alerts that indicate when the billing costs exceed the threshold you set. For example, your IO creates billing total cost alerts and configures the alerts based on a fixed dollar amount, or as a percentage of the initial budgeted amount.

To create spend threshold alerts and other organization-level billing alerts, submit a request to your IO. Include the following parameters in your request:

  * Task order (TO) number.
  * CLIN
  * The total budget amount for the specified TO and CLIN.
  * The budget threshold.



## Silence alerts

You can silence and unsilence alert rules through the GDC console. Follow the instructions in [Silence an alert](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-alerts-and-policies#silence-an-alert).

## Configure billing notifications

To configure billing notifications, follow the instructions in [Configure notification channels](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/configure-notification-channels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
