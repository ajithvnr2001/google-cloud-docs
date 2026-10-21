---
url: https://docs.cloud.google.com/data-studio/embed-external-content-in-reports/
title: Embed external content in reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:12:45.418423+00:00
---

# Embed external content in reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/embed-external-content-in-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Embed external content in reports Stay organized with collections  Save and categorize content based on your preferences. 

Use the URL embed component to display content hosted on other sites in your reports. For example, you can include YouTube videos, web pages, and Google Docs to create robust multi-media experiences for your viewers.

## To embed external content

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. In the toolbar, click ![Embed.](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--embed.png)**URL embed.**

  3. A blank content frame appears on the canvas. Move and resize this as needed.

  4. Drag the rotation handle at the top of the frame to rotate it.

  5. In the **Properties** panel, select the **SETUP** tab.

  6. Enter the URL to the chosen content in the **External Content URL** field.

  7. Use the _Style_ tab to configure the content frame's border and background properties.




## Check out the sample report

This [sample report](https://datastudio.google.com/reporting/1fY1E8eDjn9qvYyyKJDW5nNN___4XzYSW/page/chHU) demonstrates embedding a Google Doc, a YouTube video, and website content.

## How URL embed works

The URL embed component allows content hosted on other websites to appear within a box in your report. Report viewers can interact with that content as if viewing it in the content's built-in environment: viewers can play videos, use web applications, apply Data Studio filters, and view or edit Google Docs and Sheets, depending on the kind of content you embed. You configure the size and style of the content box in the same way as other report components.

You can embed virtually any content that is accessible using a URL. However, the provider of that content must allow it to be embedded, and the content must be visible to your report viewers. If you try to embed content from a blocked site, the embedded content box will remain blank, and you'll see an error in the External Content URL field.

## Kinds of content you can embed

### Embed a YouTube video

To embed a YouTube video in your report, copy and paste the video's shareable link into the External Content URL field. Here's how to get the shareable link:

  1. View the video on YouTube.
  2. On the lower right, click **Share**. ![](https://docs.cloud.google.com/static/data-studio/images/share-video-2018-09-05.png)
  3. On the lower right, click **COPY**. ![](https://docs.cloud.google.com/static/data-studio/images/click-embed-video-2018-09-05.png)
  4. In Data Studio, paste this link into the **External Content URL** field.



### Embed a Google Drive document

You can add Google Docs, Sheets, and Presentations to your reports to provide additional commentary and storytelling. To do this, you must first [share the document publicly](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports). Then, just copy and paste the URL to the document into the **External Content URL**.

**Important:** If you share a document with edit privileges, report viewers will be able to edit the contents.

### Embed a public Google Calendar

Follow the directions in the [Add a Google calendar to your website](https://support.google.com/calendar/answer/41207) help article to get an embeddable URL to your calendar. Then copy / paste that URL into the **External Content URL**.

### Embed a Data Studio report

You can frame a Data Studio report into another Data Studio report. The report you frame must have [embedding enabled](https://docs.cloud.google.com/data-studio/embed-a-report), as if you were embedding in the new Google Sites. You can then use the embeddable link as the **External Content URL**.

### Embed non-Google content

You can frame content from non-Google sites that permit you to do so. As a security precaution, the frame displays a notification to viewers when they mouseover it that the content does not come from Data Studio. Viewers must grant permission to view the content each time they view the report.

## Limits of URL embed

  * Some websites may block the ability to embed their content.
  * Recursive embedding is not allowed: while you can embed a Data Studio report into itself, you won't see the URL embed component in the embedded report.



## Related resources

[Embed a report](https://docs.cloud.google.com/data-studio/embed-a-report)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
