---
url: https://docs.cloud.google.com/support/docs/capture-browser-trace/
title: Capture browser trace information \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:49.451962+00:00
---

# Capture browser trace information  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/capture-browser-trace/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Capture browser trace information Stay organized with collections  Save and categorize content based on your preferences. 

Capturing browser trace files lets you share HTTP session logs and console output when you report a Google Cloud console issue to Cloud Customer Care. Providing these diagnostic artifacts helps support engineers reproduce and troubleshoot the problem faster. For more guidance about what to include in your support case, see [Reporting a Google Cloud console issue](https://docs.cloud.google.com/support/docs/best-practices#console-issue).

## Capture a HAR file

[HAR](https://en.wikipedia.org/wiki/HAR_\(file_format\)) (HTTP Archive) is a file format used to record HTTP session data, which helps with troubleshooting HTTP issues.

**Warning:** HAR files can contain sensitive data such as browser cookies and information that you submit in forms. If needed, you can edit a HAR file in a text editor or use [a HAR sanitizer tool](https://toolbox.googleapps.com/apps/har_analyzer/) to redact any sensitive information.

To capture and save a HAR file using your browser, follow these steps:

### Chrome

Use the [Chrome DevTools Network panel](https://developer.chrome.com/docs/devtools/network/overview):

  1. In the Google Cloud console, navigate to the page where you are encountering the issue.

  2. Open Chrome DevTools: right-click anywhere on the page and choose **Inspect**.

  3. In the DevTools panel, select the **Network** tab. The tool automatically begins recording network activity.

  4. Select **Preserve log**.

  5. Click block **Clear network log**.

  6. Reproduce the issue by interacting with the Google Cloud console.

  7. When you're done reproducing the issue, click  download **Export HAR (sanitized)** and save the generated HAR file.




### Edge

Use the [Microsoft Edge DevTools Network tool](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/network/):

  1. In the Google Cloud console, navigate to the page where you are encountering the issue.

  2. Open Microsoft Edge DevTools: right-click anywhere on the page and choose **Inspect**.

  3. In the DevTools panel, select the **Network** tab. The tool automatically begins recording network activity.

  4. Select **Preserve log**.

  5. Click block **Clear network log**.

  6. Reproduce the issue by interacting with the Google Cloud console.

  7. When you're done reproducing the issue, click  vertical_align_bottom **Export HAR** and save the generated HAR file.




### Firefox

Use the [Firefox DevTools Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/):

  1. In the Google Cloud console, navigate to the page where you are encountering the issue.

  2. Open Firefox DevTools: right-click anywhere on the page and choose **Inspect**.

  3. In the DevTools panel, select the **Network** tab. The tool automatically begins recording network activity.

  4. Click settings **Settings** and then select **Persist Logs**.

  5. Click  delete **Clear**.

  6. Reproduce the issue by interacting with the Google Cloud console.

  7. When you're done reproducing the issue, click settings **Settings > Save All As HAR** and save the generated HAR file.




### Safari

Use the [Safari Web Inspector Network Tab](https://webkit.org/web-inspector/network-tab/):

  1. [Enable Safari developer tools](https://developer.apple.com/documentation/safari-developer-tools/enabling-developer-features).

  2. In the Google Cloud console, navigate to the page where you are encountering the issue.

  3. Open Safari Web Inspector: in the Safari menu bar, click **Develop > Show Web Inspector**.

  4. In the Web Inspector, select the **Network** tab. The tool automatically begins recording network activity.

  5. Select **Preserve Log** and reload the web page.

  6. Click  delete_forever **Clear Network Items**.

  7. Reproduce the issue by interacting with the Google Cloud console.

  8. When you're done reproducing the issue, click **Export** and save the generated HAR file.




You can then upload your saved HAR file as an attachment in your support case.

## Capture a performance profile

If you are experiencing performance issues, such as slow page interactions or rendering, you can record a browser performance profile. To capture and save a performance profile using your browser, follow these steps:

### Chrome

Use the [Chrome DevTools Performance panel](https://developer.chrome.com/docs/devtools/performance/overview):

  1. In the Google Cloud console, navigate to the page where you are encountering the issue.

  2. Open Chrome DevTools: right-click anywhere on the page and choose **Inspect**.

  3. In the DevTools panel, select the **Performance** tab.

  4. Click  refresh **Record and reload** , and reproduce the issue by interacting with the Google Cloud console.

The profiler records for up to 10 seconds or until its buffer is full. If you need to record a longer profile to capture the issue, you can manually control recording by clicking  radio_button_checked **Record** and  stop_circle **Stop**.

  5. When you're done recording the profile, click  download **Save profile > Save trace** and save the generated file.




### Edge

Use the [Microsoft Edge DevTools Performance tool](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/evaluate-performance/):

  1. In the Google Cloud console, navigate to the page where you are encountering the issue.

  2. Open Microsoft Edge DevTools: right-click anywhere on the page and choose **Inspect**.

  3. In the DevTools panel, select the **Performance** tab.

  4. Click  refresh **Start profiling and reload page** , and reproduce the issue by interacting with the Google Cloud console.

The profiler records for up to 10 seconds or until its buffer is full. If you need to record a longer profile to capture the issue, you can manually control recording by clicking  radio_button_checked **Record** and  stop_circle **Stop**.

  5. When you're done recording the profile, click  vertical_align_bottom **Save profile** and save the generated file.




### Firefox

Use the [Firefox Profiler](https://profiler.firefox.com/docs/):

  1. [Enable the Firefox Profiler popup](https://profiler.firefox.com/docs/#/./guide-getting-started?id=enable-the-popup). This adds a profiler icon to the Firefox toolbar.

  2. In the Google Cloud console, navigate to the page where you are encountering the issue.

  3. Open the Firefox Profiler menu: in the Firefox toolbar, click the arrow next to the profiler icon.

  4. In the profiler menu, in the **Settings** field, select **Web Developer**.

  5. Click **Start Recording** , reload the web page, and reproduce the issue by interacting with the Google Cloud console.

To stop recording, click the profiler icon in the Firefox toolbar. This opens a new tab containing the recorded data in the Firefox Profiler web app.

  6. Click **Upload Local Profile** , click **Download** , and save the generated file.




### Safari

Use the [Safari Web Inspector Timelines Tab](https://webkit.org/web-inspector/timelines-tab/):

  1. [Enable Safari developer tools](https://developer.apple.com/documentation/safari-developer-tools/enabling-developer-features).

  2. In the Google Cloud console, navigate to the page where you are encountering the issue.

  3. Open Safari Web Inspector: in the Safari menu bar, click **Develop > Show Web Inspector**.

  4. In the Web Inspector, select the **Timelines** tab.

  5. Select **Stop recording once page loads**.

  6. Reload the web page and reproduce the issue by interacting with the Google Cloud console.

The profiler records for up to 10 seconds or until its buffer is full. If you need to record a longer profile to capture the issue, you can manually control recording by clicking circle **Start recording** and square **Stop recording**.

  7. When you're done recording the profile, click **Export** and save the generated file.




You can then upload your saved performance profile as an attachment in your support case.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
