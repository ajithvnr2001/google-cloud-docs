---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-chromium-renderer/
title: Troubleshooting the Chromium renderer \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:43.750384+00:00
---

# Troubleshooting the Chromium renderer  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-chromium-renderer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting the Chromium renderer Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot the `RendererNoRenderFinishedEventReceivedError` error in Looker. This error message usually indicates an issue with the Chromium renderer that generates PNG and PDF visualizations for downloads and schedules.

## Troubleshooting Chromium renderer compatibility

Use the following decision tree to troubleshoot renderer compatibility issues. [Open the decision tree in a new tab to zoom in.](https://docs.cloud.google.com/looker/docs/diagrams/chromium-renderer-troubleshooting-tree)

## Troubleshooting steps

The following sections describe the scenarios in the tree in further detail.

### Step 1: Verify Chromium version

The root cause of `RendererNoRenderFinishedEventReceivedError` could be a mismatch between the Looker instance and the version of Chromium or Google Chrome that's installed on the customer's host server.

To pinpoint the exact Chromium version and its installation path, use the following commands:
    
    
    chromium --version
    which chromium
    

Compare the output version against the list of Looker-compatible versions. Refer to the [Customer-hosted installation of rendering software](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software) page to see the list of supported versions.

If the version is not compatible, move to Step 2B: Perform Strategic Rollback. Otherwise, move on to Step 2A: Review installation and configuration

### Step 2A: Review installation and configuration

If you're using a customer-hosted Looker instance, review the [rendering software installation documentation](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software) to ensure correct configuration.

If everything looks correct, move on to Step 3A: Analyze logs.

### Step 3A: Analyze logs

Scrutinize Looker logs for any errors related to Chromium's state, its connection to the devtools, or any failed communication attempts. Look for recurring patterns or specific error messages that can provide clues to the underlying issue.

If you can't find any issues in the logs, move on to Final review and support.

### Step 2B: Perform strategic rollback

If the Chromium version is incompatible, a strategic rollback to a known compatible version (for example, Chromium 97, 109, or 114) is often the most effective solution. Contact Looker Support if you need help rolling back your Chromium version.

During the rollback process, you might encounter the following issues.

#### Step 3B: 404 errors and missing packages

Encountering 404 errors or missing packages can disrupt the rollback procedure. Ensure that the necessary package repositories are correctly configured and accessible. If needed, manually download and install missing packages.

#### Step 3C: Permission issues

Insufficient permissions can hinder the creation or modification of directories required for the rollback. Grant the appropriate user permissions to execute the rollback process. Use `sudo` or equivalent commands to elevate privileges temporarily if necessary.

#### Step 3D: dpkg frontend lock errors

In Debian-based systems, the `dpkg` frontend lock can prevent concurrent package operations. Wait for any ongoing package operations to finish. If there appears to be a frontend lock that doesn't go away with time, take a backup of your instance and use the command to force unlock the frontend:

`sudo rm /var/lib/dpkg/lock`

### Step 3E: Disable Chromium auto-updates

In customer-hosted environments, automatic Chromium updates can inadvertently introduce compatibility issues. Implement measures to prevent Chromium from auto-updating. Establish a routine to proactively monitor the Chromium version, and perform manual updates only when compatibility with Looker is ensured.

## Blank custom visualizations in PDF or PNG exports

Custom visualizations in PDF or PNG downloads render as blank on Looker (Google Cloud core) private connections instances that lack outbound internet access. This issue occurs because the Chromium renderer cannot fetch external JavaScript dependencies (such as D3 or jQuery) that are hosted on public content delivery networks (CDNs) when outbound access is restricted.

To resolve this issue, use one of the following workarounds:

  * **Bundle dependencies in your LookML project:**
    1. Download the required external dependency `.js` file.
    2. Copy and paste the raw dependency code at the top of your custom visualization `.js` file.
    3. Save the bundled `.js` file in your LookML project.
    4. Update the `manifest.lkml` file to point to the local file by using the [`file`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#file) parameter instead of external URLs in `dependencies` or `url`.
    5. Deploy the changes to production so that Looker serves the dependencies locally.
  * **Configure outbound connections for Private Service Connect:** For instances that use Private Service Connect, [configure outbound (southbound) connections](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) to let the instance reach external services and public CDNs.



For more information about custom visualizations, see [Admin settings - Visualizations](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations).

## Best practices for bulk visual downloads

When using the Looker API or automated scripts to download visual formats (such as PDF or PNG reports) in bulk, you may encounter queueing, connection timeouts, or `Render Cluster Congestion` errors. Generating visual formats is resource-intensive because it relies on the internal Chromium rendering engine.

Follow these best practices to optimize bulk rendering and prevent instance overload:

  * **Understand concurrency limits:** By default, Looker limits the volume of simultaneous image and PDF rendering processes to two concurrent render jobs (configured by using the `--concurrent-render-jobs` startup option). Sending too many concurrent requests can exhaust these slots and cause rendering jobs to queue or time out.
  * **Throttle API requests:** Artificially throttle automated scripts or API calls to a maximum of one rendering request or two simultaneous rendering requests.
  * **Introduce delays and retries:** Add sleep timers between batches of requests, and implement exponential backoff retry logic to gracefully handle potential connection drops, timeouts, or transient errors.
  * **Utilize the query cache:** Avoid using parameters that bypass the query cache, such as `force_new_run: true` (or the `run=1` URL parameter) during bulk generation unless absolutely necessary. Bypassing the cache forces Looker to run raw database queries for every single request, significantly increasing the pre-render data gathering time and causing renders to queue heavily.
  * **Prioritize raw data formats when appropriate:** If the primary goal of your automated process is raw data extraction rather than visual presentation, request data in CSV or JSON formats instead. These formats completely bypass the Chromium renderer, using far fewer resources and executing much faster.



## Final review and support

If these troubleshooting steps fail to resolve the error, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) to troubleshoot further.

## Additional resources

  * [Customer-hosted installation of rendering software](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software)
  * [Community forums](https://discuss.google.dev/c/looker/19)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
