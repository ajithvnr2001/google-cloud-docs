---
url: https://docs.cloud.google.com/chronicle/docs/investigation/generate-udm-search-queries-gemini/
title: Generate search queries with Gemini \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:56:39.550853+00:00
---

# Generate search queries with Gemini  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/generate-udm-search-queries-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Generate search queries with Gemini 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can use Gemini to generate search queries from the Gemini pane or when using Google Security Operations search.

For best results, we recommend using the Gemini pane to generate search queries.

  * Generate a search query using the Gemini pane

  * Generate a search query using natural language




## Generate a search query using the Gemini pane

  1. Sign in to Google SecOps.
  2. Click the Gemini logo to open the Gemini pane.
  3. Enter a natural language prompt and press **Enter**. The natural language prompt must be in English.

![Open Gemini pane and enter prompt](https://docs.cloud.google.com/chronicle/images/gemini-open.png)

**Figure 1.** Open Gemini pane and enter prompt.

  4. Review the generated search query. The search query uses YARA-L 2.0 syntax. If the generated search query meets your requirements, click **Run search**. Gemini produces a results summary along with suggested actions.




### Example search prompts and follow-up questions

  * `Show me all failed logins for the last 3 days`
    * `Generate a rule to help detect that behavior in the future`
  * `Show me events associated with the principle user izumi.n`
    * `Who is this user?`
  * `Search for all of the events associated with the IP 198.51.100.121 in the last 3 hours`
    * `List all of the domains in the results set`
    * `What types of events were returned?`
  * `Show me events from my firewall in the last 24 hours`
    * `What were the 16 unique hostnames in the results set?`
    * `What were the 9 unique IPs associated with the results set?`



## Generate a search query using natural language

Using the Google SecOps search feature, you can enter a natural language query about your data, and Gemini can translate this into a search query to run against UDM events.

For better results, we recommend using the Gemini pane to generate search queries.

To use a natural language search to create a search query, complete the following steps:

  1. Sign in to Google SecOps.
  2. Go to **Investigation > SIEM Search**.
  3. Enter a search statement in the natural language query bar and click **Generate Query**. You must use English for the search.

![Enter a natural language search and click Generate
Query](https://docs.cloud.google.com/static/chronicle/images/udm-search-nl.png)

**Figure 2.** Enter a natural language search and click **Generate Query**.

The following statements are examples that might generate a useful search: 

     * _network connections from 10.5.4.3 to google.com_
     * _failed user logins over the last 3 days_
     * _emails with file attachments sent to john@example.com or jane@example.com_
     * _all Cloud service accounts created yesterday_
     * _outbound network traffic from 10.16.16.16 or 10.17.17.17_
     * _all network connections to facebook.com or tiktok.com_
     * _service accounts created in Google Cloud yesterday_
     * _Windows executables modified between 8 AM and 1 PM on May 1, 2023_
     * _all activity from winword.exe on lab-pc_
     * _scheduled tasks created or modified on exchange01 during the last week_
     * _email messages that contain PDF attachments_
     * _emails sent by or sent from admin@acme.com on September 1_
     * _any files with the hash 44d88612fea8a8f36de82e1278abb02f_
     * _all activity associated with user "sam@acme.com"_

If the search statement includes a time-based term, the time picker is automatically adjusted to match. For example, this would apply to the following searches: 

     * _yesterday_
     * _within the last 5 days_
     * _on Jan 1, 2023_

If the search statement can't be interpreted, you see the following message:  
"Sorry, no valid query could be generated. Try asking a different way."

  4. Review the generated search query. The syntax is [Overview of YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-overview).

  5. Optional: Adjust the search time range.

  6. Click **Run Search**.

  7. Review the search results to determine if the event is present. If needed, use search filters to narrow the list of results.

  8. Provide feedback about the query using the **Generated Query** feedback icons. Select one of the following:

     * If the query returns the expected results, click thumb_up **Thumbs Up**.
     * If the query does not return the expected results, click thumb_down **Thumbs Down**.
     * Optional: Include additional detail in the **Feedback** field.
  9. To submit a revised search query that helps improve results:

     1. Edit the search query that was generated.
     2. Click **Submit**. 
        * If you didn't rewrite the query, you're prompted to edit the query.
        * If you did rewrite the query, the revised search query is sanitized for sensitive data and used to improve results.



### Delete a chat session

You can delete your chat conversation session or delete all chat sessions. Gemini maintains all user conversation histories privately and adheres to Google Cloud's [responsible AI practices](https://docs.cloud.google.com/duet-ai/docs/discover/responsible-ai). User history is never used to train models.

  1. In the Gemini pane, select **Delete chat** from the menu at the top right.
  2. Click **Delete chat** at the bottom right to delete the current chat session.
  3. Optional: To delete all chat sessions, select **Delete all chat sessions** and then click **Delete all chats**.



### Provide feedback

You can provide feedback to responses generated by the Gemini AI investigation assistance. Your feedback helps Google improve the feature and the output generated by Gemini.

  1. In the Gemini pane, click thumb_up **Thumb Up** or thumb_down **Thumb Down**.
  2. Optional: Click thumb_down **Thumb Down** and provide feedback.
  3. Click **Send feedback**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
