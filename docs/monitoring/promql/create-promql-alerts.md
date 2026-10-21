---
url: https://docs.cloud.google.com/monitoring/promql/create-promql-alerts/
title: Create PromQL-based alerting policies (API) \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:26.872551+00:00
---

# Create PromQL-based alerting policies (API)  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/promql/create-promql-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create PromQL-based alerting policies (API) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a PromQL-based alerting policy by using the Cloud Monitoring API. You can use PromQL queries in your alerting policies to create complex conditions with features such as ratios, dynamic thresholds, and metric evaluation.

For general information, see [PromQL-based alerting overview](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

If you work in a Prometheus environment outside Cloud Monitoring and have Prometheus alerting rules, then you can use the Google Cloud CLI to migrate them to PromQL-based alerting policies in Monitoring. For more information, see [Migrate alerting rules and receivers from Prometheus](https://docs.cloud.google.com/monitoring/promql/promql-migrate).

## Create alerting policies with PromQL queries

You use the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) method to programmatically create alerting policies.

The only difference between creating PromQL-based alerting policies and other alerting policies is that your [`Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition) type must be [`PrometheusQueryLanguageCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition). This condition type allows alerting policies to be defined with PromQL.

The following shows a PromQL query for an alerting policy condition that uses a metric from the `kube-state` exporter to find the number of times that a container has been restarted in the last 30 minutes:
    
    
    rate(kube_pod_container_status_restarts[30m]) * 1800 > 1
    

### Constructing the alerting policy

To build a PromQL-based alerting policy, use the `AlertPolicy` condition type [`PrometheusQueryLanguageCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition). The `PrometheusQueryLanguageCondition` has the following structure:
    
    
    {
      "query": string,
      "duration": string,
      "evaluationInterval": string,
      "labels": {string: string},
      "ruleGroup": string,
      "alertRule": string
    }
    

**Note:** An alerting policy that uses PromQL must have only one condition. Policies with multiple conditions are not supported if a condition uses PromQL. However, you can reference multiple metrics in one PromQL condition and evaluate them together by using the `+` operator.

The `PrometheusQueryLanguageCondition` fields have the following definitions:

  * `query`: The PromQL expression to evaluate. Equivalent to the `expr` field from a standard Prometheus alerting rule.
  * `duration`: Specifies the length of time during which each evaluation of the query must generate a `true` value before the condition of the alerting policy is met. The value must be a number of minutes, expressed in seconds; for example, `600s` for a 10-minute duration. For more information, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).
  * `evaluationInterval`: The interval of time, in seconds, between PromQL evaluations of the query. The default value is 30 seconds. If the `PrometheusQueryLanguageCondition` was created by migrating a Prometheus alerting rule, then this value comes from the Prometheus rule group that contained the Prometheus alerting rule.

**Note:** Alerts created by a PromQL-based alerting policy don't follow the alerting policy autoclose duration. Instead, the alert is automatically closed when it reaches a set time after the last time the condition was met. This time is the larger of 270 seconds and twice the condition's evaluation interval. 
  * `labels`: An optional way to add or overwrite labels in the PromQL expression result.

  * `ruleGroup`: If the alerting policy was migrated from a Prometheus configuration file, then this field contains the value of the `name` field from the [rule group](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule_group) in the Prometheus configuration file. This field isn't required when you make a PromQL alerting policy in Cloud Monitoring API.

  * `alertRule`: If the alerting policy was migrated from a Prometheus configuration file, then this field contains the value of the `alert` field from the [alerting rule](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule) in the Prometheus configuration file. This field isn't required when you make a PromQL alerting policy in Cloud Monitoring API.




For example, the following condition uses a PromQL query to find the number of times that a container has been restarted in the last 30 minutes:
    
    
    "conditionPrometheusQueryLanguage": {
      "query": "rate(kube_pod_container_status_restarts[30m]) * 1800 > 1",
      "duration": "600s",
      "evaluationInterval": "60s",
      "alertRule": "ContainerRestartCount",
      "labels": {
        "action_required":"true",
        "severity":"critical/warning/info"}
    }
    

Use this structure as the value of a `conditionPrometheusQueryLanguage` field in a condition, which is in turn embedded in an alerting-policy structure. For more information about these structures, see [`AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy).

The following shows a complete policy with a `PrometheusQueryLanguageCondition` condition in JSON:

**Note:** The `documentation` field in the following example uses [document variables](https://docs.cloud.google.com/monitoring/alerts/doc-variables).
    
    
    {
      "displayName": "Container Restarts",
      "documentation": {
        "content": "Pod ${resource.label.namespace_name}/${resource.label.pod_name} has restarted more than once during the last 30 minutes.",
        "mimeType": "text/markdown",
        "subject": "Container ${resource.label.container_name} in Pod ${resource.label.namespace_name}/${resource.label.pod_name} has restarted more than once during the last 30 minutes."
      },
      "userLabels": {},
      "conditions": [
        {
          "displayName": "Container has restarted",
          "conditionPrometheusQueryLanguage": {
            "query": "rate(kubernetes_io:container_restart_count[30m]) * 1800",
            "duration": "600s",
            "evaluationInterval": "60s",
            "alertRule": "ContainerRestart",
            "labels": {
              "action_required":"true",
              "severity":"critical/warning/info"}
          }
        }
      ],
      "combiner": "OR",
      "enabled": true
    }
    

### Create an alerting policy

To create the alerting policy, put the alerting policy JSON into a file called POLICY_NAME.json, and then run the following command:
    
    
    curl -d @POLICY_NAME.json -H "Authorization: Bearer $TOKEN"
    -H 'Content-Type: application/json'
    -X POST https://monitoring.googleapis.com/v3/projects/${PROJECT}/alertPolicies
    

For more information about the Monitoring API for alerting policies, see [Managing alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).

For more information about using `curl`, see Invoking `curl`.

### Disable check for metric existence

When you create a PromQL-based alerting policy, Google Cloud runs a validation to ensure that the metrics referenced in the condition already exist in Monitoring. However, you can override this validation if you need to create an alerting policy before the metrics exist. For example, you might want to do so when using automation to create new projects that come with a standard set of predefined alerting policies. If you don't disable the validation, then your alerting policy creation fails until the underlying metrics are created.

To disable the check for metric existence, add the field `"disableMetricValidation": true` to your `PrometheusQueryLanguageCondition`:
    
    
    {
      "query": string,
      "duration": string,
      "evaluationInterval": string,
      "labels": {string: string},
      "ruleGroup": string,
      **"disableMetricValidation": true,**
      "alertRule": string
    }
    

If the condition of an alerting policy references a metric that doesn't exist, then the condition still runs according to its evaluation interval. However, the query result is always empty. After the underlying metric exists, the query returns data.

**Note:** Users who can view alerting policies are able to see the name of the non-existent metric in the alerting policy condition.

## Use Terraform

For instructions on configuring PromQL-based alerting policies using Terraform, see the `condition_prometheus_query_language` section of the [`google_monitoring_alert_policy` Terraform registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy).

For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Invoking `curl`

Each `curl` invocation includes a set of arguments, followed by the URL of an API resource. The common arguments include a Google Cloud project ID and an authentication token. These values are represented here by the `PROJECT_ID` and `TOKEN` environment variables.

You might also have to specify other arguments, for example, to specify the type of the HTTP request (for example, `-X DELETE`). The default request is `GET`, so the examples don't specify it.

Each `curl` invocation has this general structure:

`curl --http1.1 --header "Authorization: Bearer ${TOKEN}" <other_args> https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/<request>`

To use `curl`, you must specify your project ID and an access token. To reduce typing and errors, you can put these into environment variables as pass them to `curl` that way.

To set these variables, do the following:

  1. Create an environment variable to hold the ID of your scoping project of a metrics scope. These steps call the variable `PROJECT_ID`:
         
         PROJECT_ID=a-sample-project
         

  2. Authenticate to the Google Cloud CLI:
         
         gcloud auth login
         

  3. Optional. To avoid having to specify your project ID with each `gcloud` command, set your project ID as the default by using gcloud CLI:
         
         gcloud config set project ${PROJECT_ID}
         

  4. Create an authorization token and capture it in an environment variable. These steps call the variable `TOKEN`:
         
         TOKEN=`gcloud auth print-access-token`
         

You have to periodically refresh the access token. If commands that worked suddenly report that you are unauthenticated, reissue this command.

  5. To verify that you got an access token, echo the `TOKEN` variable:
         
         echo ${TOKEN}
         ya29.GluiBj8o....
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
