---
url: https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps/
title: Explore heatmaps \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:22.937520+00:00
---

# Explore heatmaps  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explore heatmaps

This page describes how to analyze the heatmap in a Key Visualizer scan so you can identify the source of a Bigtable performance issue.

Before you read this page, you should be familiar with the [overview of Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview). You may also want to:

  * Learn how to [open a Key Visualizer scan](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started#viewing-scan).
  * See examples of common [patterns in Key Visualizer heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-patterns).



## Review diagnostic messages

If Key Visualizer identifies an issue with your Bigtable usage patterns, the Key Visualizer scan will include diagnostic messages above the heatmap. Click on one of the diagnostic messages for detailed information about the issue.

For descriptions of each diagnostic message, see [Key Visualizer diagnostic messages](https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics).

## Adjust brightness

Key Visualizer heatmaps use dark colors to indicate normal or low values, and bright colors to indicate high values. If the colors in a heatmap are too bright or too dark, it might be difficult to see important patterns for a metric.

Keep in mind that for most metrics, Key Visualizer identifies which values are "high" and "low" based entirely on your usage of that table. For example, if you perform 20 reads per second in a specific row range and 1 read per second in other row ranges, Key Visualizer will use a bright color for that specific row range, even though 20 reads per second is a low number for Bigtable. The [**Warnings** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#warnings) and [**Performance** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#performance) are exceptions to this rule—if these metrics appear in bright colors, then Key Visualizer has identified a potential problem.

To adjust the colors that are used for different values, use the **\+ / -** buttons on either side of the **Adjust Brightness** _brightness_6_ icon. When you increase the brightness, you lower the range of values that each color represents; when you lower the brightness, you increase the range of values.

## Zoom in on time periods and row key ranges

When you open a heatmap, it displays values for the entire time period included in the scan, as well as the entire range of row keys in your table. If you notice an issue during a specific time period, or in a specific range of row keys, you can zoom in to examine the issue more closely.

There are several ways to zoom in or out:

  * Scroll up or down within the heatmap.
  * Click the **Rectangular Zoom** _crop_ button, then click and drag to select an area to enlarge.
  * Press and hold the `Shift` key, then click and drag to select an area to enlarge.
  * Return to the previous area of the heatmap by pressing the `Backspace` or `Delete` key.
  * Zoom out to view the entire table by clicking the **Reset Zoom** _zoom_out_map_ button or pressing the `R` key.



## Drill down by row key prefix

Row keys are often composed of a hierarchy of values, with each value separated by a delimiter. For example, the row key `memusage#1423523569918` contains an identifier for all rows that capture memory usage, followed by a timestamp that identifies a specific set of data within that group. Key Visualizer automatically recognizes this type of row key and breaks it down into a hierarchy, which helps you drill down into the data for specific ranges of row keys more quickly.

To drill down into the heatmap's data for a group of row keys that share a common prefix:

  1. Move the cursor over one of the levels in the row-key hierarchy that appears to the left of the heatmap.

Key Visualizer highlights the area of the heatmap that shows this level of the hierarchy. It also shows the key prefix for all of the row keys at this level.

![Example of a highlighted area in a heatmap for a group of row keys](https://docs.cloud.google.com/bigtable/img/keyvis-key-prefix-hover.png)

  2. Click the level of the row-key hierarchy that you want to examine.

Key Visualizer zooms in on this level of the hierarchy.

![Example of zooming in on a level of the row-key hierarchy](https://docs.cloud.google.com/bigtable/img/keyvis-row-prefix-zoomed.png)

  3. Click another level of the row-key hierarchy to zoom in further, or press the `Backspace` or `Delete` key to return to the previous area.




## Pin details about a metric

As you move your cursor over a heatmap, Key Visualizer displays a tooltip that contains details about the metric that is under the cursor. You can pin this tooltip in place by clicking on the heatmap. Pinned tooltips show more detail about the metric. Pinning a tooltip also makes it easier to take a screenshot of the tooltip or copy information from the tooltip.

## Switch metrics

By default, when you open a Key Visualizer scan, it displays the **Ops** metric, which gives you an overview of your usage pattern for the table. You can switch to a different metric at any time by clicking the **Metric** drop-down list above the heatmap, then clicking the metric you want to view. If an item in the list is disabled, the value of that metric was always zero.

For descriptions of each metric, see [Key Visualizer Metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics).

## Switch key format

By default, keys are displayed as serialized bytes. This means that printable characters display as ASCII characters, or text. Non-printable characters are displayed as a series of backslashes followed by three-digit numbers. Each number represents the octal representation of a byte.

For example, a key that contains both printable and non-printable bytes might look like this:

\360q\364\031\253\735\223xdf\272\022\362\251bn\101

You can choose to view keys in hexadecimal format instead of text format:

  1. Click the **Settings** button.
  2. Under **Preferences** , choose **Hexadecimal**.
  3. Click **OK**.



## Find connections between different metrics

You can view multiple metrics at the same time in Key Visualizer when you want to compare metrics or find correlations between metrics. For example, you might want to see if hotspots on your **Ops** heatmap correlate with any hotspots on your **Latency** heatmap, which might indicate that the number of operations within a [key bucket](https://docs.cloud.google.com/bigtable/docs/keyvis-overview#key-buckets) was causing increased latency.

To view multiple metrics and their values at the same time, click `Multimetric` near the top right corner. A list of metrics appears in a pane to the right of the scan.

![Example showing the multimetric pane for_a_scan](https://docs.cloud.google.com/bigtable/img/keyvis-multimetric-pane.png)

To examine several metrics at once, use the following tools in the multimetric pane:

  * To show or hide miniature heatmaps for all metrics, click `Expand All` or `Collapse All` at the top right.

  * To show an individual metric's heatmap, click the metric name.

  * To hide an individual metric's heatmap, click the metric name again.

  * To display a metric's heatmap in the main window, click the solid arrow at the left edge of the metric's title bar.

![Left arrow shows a metric in the main window](https://docs.cloud.google.com/bigtable/img/keyvis-mini-metric.png)

  * Hover over a miniature heatmap to see corresponding activity in the main view.




To compare different metrics for a key bucket at the same point in time, you can pin a value in a scan, then switch to a different metric at the same point in time:

  1. Point to a position of interest on the large heatmap in the main window.
  2. Click to pin the tooltip. The values in the side pane stay fixed to the key bucket and point in time you've pinned.
  3. To display a metric in the large heatmap, click the solid arrow on the left for that metric. The tooltip in the main window shows you the full details for that metric.



## What's next

  * Learn to recognize [common patterns in heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-patterns).
  * Read about the [metrics you can view in a heatmap](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics).
  * Understand the [diagnostic messages that Key Visualizer can display](https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics).
  * Learn more about [row keys that contain multiple values](https://docs.cloud.google.com/bigtable/docs/schema-design#multi-value-row-key).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
