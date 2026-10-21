---
url: https://docs.cloud.google.com/functions/1stgendocs/monitoring/metrics/
title: View metrics and quotas \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:42.804060+00:00
---

# View metrics and quotas  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/monitoring/metrics/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View metrics and quotas

## Viewing metrics in the console

You can [view your Cloud Run functions](https://console.cloud.google.com/functions/list) with their execution times, execution counts, and memory usage in the Google Cloud console. These metrics are also available in [Cloud Monitoring](https://console.cloud.google.com/monitoring), where you can set up custom alerting on these metrics. See the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs) for more information.

You can view the metrics for API calls in the [API overview page](https://console.cloud.google.com/apis/api/cloudfunctions.googleapis.com/overview) of the Google Cloud console.

Finally, you can view the quota metrics for both API calls and function execution in the [API quotas page](https://console.cloud.google.com/apis/api/cloudfunctions.googleapis.com/quotas) of the Google Cloud console. You can set up alerting on quota errors in [Cloud Monitoring](https://console.cloud.google.com/monitoring) by filtering executions that have an `out of quota` value for the `STATUS` metric label. See [Introduction to Alerting](https://docs.cloud.google.com/monitoring/alerts) for more information.

## Reading metrics programmatically

The following snippet illustrates how you can also read metrics from your code.

###  Node.js 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function readTimeSeriesData() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const filter = 'metric.type="compute.googleapis.com/instance/cpu/utilization"';
    
      const request = {
        name: client.projectPath(projectId),
        filter: filter,
        interval: {
          startTime: {
            // Limit results to the last 20 minutes
            seconds: Date.now() / 1000 - 60 * 20,
          },
          endTime: {
            seconds: Date.now() / 1000,
          },
        },
      };
    
      // Writes time series data
      const [timeSeries] = await client.listTimeSeries(request);
      timeSeries.forEach(data => {
        console.log(`${data.metric.labels.instance_name}:`);
        data.points.forEach(point => {
          console.log(JSON.stringify(point.value));
        });
      });
    }
    readTimeSeriesData();

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
