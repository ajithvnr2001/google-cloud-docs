---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/setup-siem-webhook/
title: Set up a SIEM webhook \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:19.735877+00:00
---

# Set up a SIEM webhook  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/setup-siem-webhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a SIEM webhook

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

## Before you begin

  * Ensure that a [Google Cloud project for Google SecOps is configured](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) and the Chronicle API is enabled for the project.
  * [Link a Google SecOps instance to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).

**Note:** Batches of data sent through Webhook feeds may experience ingestion delays if the request size or QPS limits are set too low. The HTTPS push endpoint supports a maximum request size of 4 MB per request and a maximum throughput of 15 K QPS per Google SecOps instance.



### Using the command-line examples

This document includes `curl` command examples to help you set up and test your webhook feed. These examples use editable placeholder variables. To use them effectively:

  1. **Edit the variables:** As you follow the setup steps, you will obtain values for the webhook endpoint, an API key, and a secret. Click the placeholder variables in the sample code and replace them with your actual values:

     * `ENDPOINT_URL`: The feed endpoint URL obtained when you Create an HTTPS webhook feed.
     * `API_KEY`: The API key you Create for the webhook feed to authenticate to Google SecOps.
     * `SECRET`: The secret key generated when you Create an HTTPS webhook feed.

Editing a variable in one code sample will update it across all examples on this page.

  2. **Copy the command:** Click the **Copy the code sample** icon on the code block.

  3. **Run the command:** Paste the copied command into your terminal environment and execute it.

Make sure that the `curl` command includes the `--fail` (or `-f`) flag. This ensures that `curl` returns a non-zero exit code if the HTTP request fails, and an exit code of `0` to indicate success. This is needed for the next step.

  4. **Verify success:** A successful `curl` command returns no output. To confirm success do the following:

If the `curl` command included the `--fail` (or `-f`) flag, then check the exit code by running the following command immediately after:
         
         echo $?
         

An exit code of `0` indicates success.




## Set up an HTTPS webhook feed

To set up an HTTPS webhook feed, do the following:

  1. Create an HTTPS webhook feed and copy the endpoint URL and secret key.
  2. Create an API key to use with the endpoint URL. You can also reuse your existing API key to authenticate to Google SecOps.
  3. Specify the endpoint URL in your application.



### Send multiple events in a single webhook request

The following code sample shows how to format a single request body with multiple newline-separated JSON objects:
    
    
    curl --location 'ENDPOINT_URL' \
      --header 'Content-Type: application/json' \
      --header 'X-goog-api-key: API_KEY' \
      --header 'X-Webhook-Access-Key: SECRET' \
      --data $'{"principal": {"asset_id": "asset 123"}, "metadata": {"event_type": "GENERIC_EVENT", "product_name": "Product Acme"}}\n{"principal": {"asset_id": "asset 123"}, "metadata": {"event_type": "GENERIC_EVENT", "product_name": "Product Acme"}}' \
      --fail
    

### Create an HTTPS webhook feed

  1. In the Google SecOps menu, select **Settings** , and then click **Feeds**.
  2. Click **Add new**.
  3. In the **Feed name** field, enter a name for the feed.
  4. In the **Source type** list, select **Webhook**.
  5. Select the **Log type**. For example, to create a feed for Open Cybersecurity Schema Framework, select **Open Cybersecurity Schema Framework (OCSF)** as the **Log type**.
  6. Click **Next**.
  7. Optional: Specify values for the following input parameters: 
     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label to be applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.
  10. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  11. Copy and store the secret key as you cannot view this secret again. You can generate a new secret key, but doing so makes the previous secret key obsolete.
  12. From the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.
  13. Optional: Click the **Feed Enabled** toggle to disable the feed. The feed is enabled by default.
  14. Click **Done**.



### Create an API key for the webhook feed

  1. Go to the Google Cloud console [**Credentials**](https://console.cloud.google.com/apis/credentials) page.
  2. Click **Create credentials** , and then select **API key**.
  3. Restrict the API key access to the Chronicle API.



### Specify the endpoint URL

  1. In your client application, specify the HTTPS endpoint available in the webhook feed.
  2. Enable authentication by specifying the API key and secret key as custom headers in the following format:
         
         X-goog-api-key: API_KEY
         X-Webhook-Access-Key: SECRET
         

     * We recommend that you specify the API key as a header instead of specifying it in the URL.
           
           curl --location 'ENDPOINT_URL' \
               --header 'Content-Type: application/json' \
               --header 'X-goog-api-key: API_KEY' \
               --header 'X-Webhook-Access-Key: SECRET' \
               --data '{"principal": {"asset_id": "asset 123"}, "metadata": {"event_type": "GENERIC_EVENT", "product_name": "Product Acme"}}' \
               --fail
           

     * If your webhook client doesn't support custom headers, you can specify the API key and secret key by using query parameters in the following format:
           
           ENDPOINT_URL?key=API_KEY&secret=>SECRET
           




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
