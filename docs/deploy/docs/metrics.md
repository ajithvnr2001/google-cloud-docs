---
url: https://docs.cloud.google.com/deploy/docs/metrics/
title: Viewing metrics in Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:55.646344+00:00
---

# Viewing metrics in Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Viewing metrics in Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Deploy shows metrics for how many deployments occur for a given delivery pipeline, over time, and how many of those deployments succeed.

## About Cloud Deploy metrics

All deployment metrics in Cloud Deploy have the following characteristics:

  * All metrics are measured per delivery pipeline.

  * All metrics are for deployments to your _production_ target.

The final target in your delivery pipeline [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression) is considered to be the production target.

  * All metrics are measured for a rolling 30-day period.

For example, the Deployments metric counts the number of successful and failed deployments over the last 30 days.

  * Metrics consider _successful_ deployments, and some also report failed deployments.

A successful deployment is one for which the pod or pods report a ready state. The Deployment failure rate metric counts failures as a percentage of all deployment attempts.




Cloud Deploy makes the following deployment metrics available in Google Cloud console:

  * Deployments
  * Deployment frequency
  * Deployment failure rate



## The Deployments metric

The _Deployments_ metric shows the number of successful and failed deployments from the selected delivery pipeline to your production cluster.

![The Deployments metric,
seen on the delivery pipeline details page](https://docs.cloud.google.com/static/deploy/images/deployments-metric.png)

## The Deployment frequency metric

The _Deployment frequency_ metric shows how often the delivery pipeline successfully deploys to the production target per day. This is one of the four key metrics defined by the [DevOps Research and Assessment](https://dora.dev/) (DORA) research program.

![The Deployment
frequency metric, seen on the delivery pipeline details page](https://docs.cloud.google.com/static/deploy/images/deployment-frequency-metric.png)

### How Deployment frequency is calculated

Deployment frequency is calculated based on the number of deployment _days_ , not the number of deployments. That is, if the delivery pipeline generates four deployments to production on a given day, that's counted as one deployment day.

This metric is expressed per day, per week, or per month, depending on how many deployments there are:

  * If the median number of deployment days per week is greater than or equal to 3, then the frequency is expressed as daily:

".8 times per day."

  * Otherwise, if more than 2 weeks have more than 0 deployment days then it's expressed as weekly:

"2 days per week."

  * Otherwise, if there's at least one deployment day per month, then it's expressed as monthly:

"2 days per month."




## The Deployment failure rate metric

The _Deployment failure rate_ metric shows the percentage of deployments that have failed.

![The Deployment
failure rate metric, seen on the delivery pipeline details page](https://docs.cloud.google.com/static/deploy/images/failure-rate-metric.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
