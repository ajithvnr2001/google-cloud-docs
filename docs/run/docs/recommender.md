---
url: https://docs.cloud.google.com/run/docs/recommender/
title: Optimize with Recommender \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:25.603873+00:00
---

# Optimize with Recommender  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Optimize with Recommender Stay organized with collections  Save and categorize content based on your preferences. 

Recommender is a service that automatically provides recommendations and insights for using resources on Google Cloud, based on heuristic methods, machine learning, and current resource usage. Each recommendation includes a link you can click to put the recommendation into effect for your service.

This guide shows how to use [Recommender](https://docs.cloud.google.com/recommender) to optimize Cloud Run services for security and costs.

## Optimize cost

Recommender optimizes costs for billing.

### Optimize billing

Recommender automatically looks at traffic received by your Cloud Run service over the past month, and will recommend switching from _request-based billing_ to _instance-based billing_ , if this is cheaper. For more details, see [billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings).

## Optimize security

Recommender increases security by optimizing:

  * Service accounts for a Cloud Run service so the service account has the minimal set of required permissions.
  * Security of the following items in environment variables:

    * Passwords
    * API keys
    * Google Application Credentials



Google _does not_ examine the values contained in those environment variables. Rather, we do a _case insensitive_ check on the variable **key names** , as shown in the following patterns:

  * The environment variable key is a case insensitive variant of `API KEY`, such as `API_KEY`, `api_key`, `APIKEY`, or `apikey`
  * The environment variable ends in a case insensitive variant of `PASSWORD`, such as `PASSWORD` or `password`
  * The environment variable is `GOOGLE_APPLICATION_CREDENTIALS`



### Security issues addressed by Recommender

The following table shows what Recommender detects and helps you address:

Recommendation | Actions  
---|---  
Service account might have more permissions than are required. | Recommender leads you to configure a new service account that has the minimal set of required permissions.  
Environment variable might contain a password. | Recommender leads you to move the password to [Secret Manager](https://docs.cloud.google.com/run/docs/configuring/services/secrets).  
Environment variable might contain an API key. | Recommender leads you to move the API key to [Secret Manager](https://docs.cloud.google.com/run/docs/configuring/services/secrets).  
Environment variable might contain Google Application Credentials. | Recommender leads you to replace this with [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity#per-service-identity) instead.  
  
## Recommendation availability after deployment

Recommender automatically provides recommendations for a service after it has been deployed, after a period of time has elapsed, typically one day. After this period of time, recommendations for the service are displayed with the service in the [Cloud Run service list](https://docs.cloud.google.com/run/docs/managing/services) in the Google Cloud console and in the [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

## Alternate ways of using recommendations

In addition to the use of recommendations covered on this page inside the Cloud Run UI, recommendations are also available through the following:

  * [Recommender API](https://docs.cloud.google.com/recommender/docs/using-api)
  * [BigQuery export](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq)
  * [Recommender Logs](https://docs.cloud.google.com/recommender/docs/viewing-logs)



## View and accept recommendations for Cloud Run

To view and accept a recommendation in the Cloud Run user interface:

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate services in the list that have something in the _Recommendations_ column.

  3. Click the **Security** icon for your service under the column heading _Recommendations_ , to display the recommendation pane for your service.

  4. In the pane, read the insight about your service and the recommendation.

  5. If you accept the recommendation, click the button at the bottom of the pane to make the changes suggested by the recommendation.

  6. Follow the instructions and documentation to change your Cloud Run service as needed.




## View recommendations in Active Assist

To view recommendations in Active Assist:

[Go to Active Assist](https://console.cloud.google.com/home/recommendations)

For more information, see the Active Assist [Getting started](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems) page.

## Dismissing a recommendation

Click **Dismiss** if you want to dismiss the recommendation without applying it. This prevents the recommendation for that function from appearing again for 30 days.

## Optimize Cloud Run apps with Gemini assistance

You can get AI-powered help from [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) chat to enhance performance and security. With Gemini Cloud Assist, you can proactively address potential issues and vulnerabilities in your cloud infrastructure, ensuring a robust and stable environment for your applications and services.

To use Gemini Cloud Assist from the Google Cloud console, do the following:

  1. [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

  2. [Set up your Cloud Run development environment](https://docs.cloud.google.com/run/docs/setup) in your Google Cloud project and ensure you have the appropriate [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration).

  3. Go to the Cloud Run page in the Google Cloud console.

[Go to Cloud Run](https://console.cloud.google.com/run)

  4. In the console toolbar, select a Google Cloud project. Use a project associated with a project ID you submitted after you were granted access to Gemini Cloud Assist.

  5. Click spark **Open or close Gemini AI chat**.

The Gemini panel opens.

  6. If necessary, click **Accept** if you agree to the terms.

  7. If you have a question about a specific application, provide context by going to the page that shows your resource before asking your question. When generating a response, Gemini includes information about the current console page and project.

  8. Enter a prompt in the **Gemini** panel.

The following table provide some example prompts for using Gemini Cloud Assist with Cloud Run.

**Prompt** | **Type of response**  
---|---  
"How to save cost on my Cloud Run service without sacrificing performance for service `example-service`?" | Best practices for saving costs on your service without sacrificing performance.  
"How can I make my Cloud Run service more reliable and prevent downtime?" | Suggestions for enhancing reliability and minimizing downtime for your service.  
"How can I better secure my Cloud Run services?" | List of recommendations for increasing the security of your Cloud Run service.  
"For Black Friday/Cyber Monday, I need my workloads to handle high traffic. How should I prepare?" | Suggested comprehensive strategy encompassing capacity planning, reliability testing, and robust operational practices.   
"How can I improve my service's performance for my Cloud Run service `example-service`?" | Considerations for improving the performance of your app.  
"My Cloud Run service "svc1" has been performing slow this week. Can you see if there's a reason?" | Instructions on how to investigate the issue using the tools available in the Google Cloud console, specifically within the Logs Explorer page of Logging.  
"How can I make my Cloud Run service bill cheaper?" | Provides several cost-optimization strategies.  



For more details, see the following resources:

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Read [Use Gemini for AI assistance and development](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
