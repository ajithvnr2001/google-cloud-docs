---
url: https://docs.cloud.google.com/profiler/docs/focusing-profiles/
title: Focus the flame graph \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:50.191053+00:00
---

# Focus the flame graph  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/focusing-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Focus the flame graph

When you use the **Focus** filter, you select a single _function_ , and the flame graph displays the code paths that flow into, and out of, that specific function. A focused graph lets you perform two common tasks:

  1. Analyzing the aggregate resource consumption of a given function that is called from multiple places.
  2. Analyzing the proportion of time spent in a function for different callers of the function.



For example, how do you analyze the resource consumption around the `Sort` function by using the standard flame graph?

![Sort function in flame graph.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-focus-sort-unfiltered.png)

In the next section, we focus the graph on `Sort` and answer this question. The flame graphs on this page were constructed with the **Color mode** and **Compare to** set to the default values of **Name** and **None** respectively.

## Focused graph explained

The graph built by the **Focus** filter effectively creates two flame graphs for the specified function and joins them together:

![Flame graph for focused on the sort function.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-focus-sort-focus.png)

In the preceding graph, the frame corresponding to the `Sort` function is full width and highlighted. The frame text includes the function name, a percentage, and the number of profiles used for the analysis. In this case, the metrics indicate that the `Sort` function, in aggregate, consumed 8.85% of the CPU time.

The bottom half of the preceding graph treats the function `Sort` as the starting point of a standard flame graph and shows all of its callees. You can create this part with the standard flame graph using the **Show from frame** filter:

![Bottom of flame graphs showing sort callees.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-focus-sort-callees.png)

The top half of the graph shows the callers of `Sort` with the callees hidden. You can make an approximation of the top half using a series of filters. Start by adding a **Show stacks** filter for `Sort`. Next, for each function called by `Sort`, add either a **Hide stacks** or **Hide frames**. In this situation, you would add a **Hide stacks** for `quickSort` to eliminate this function and its children, and then add **Hide frames** for `Len` and `maxDepth`:

![Top of flame graphs showing sort callers.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-focus-sort-callers.png)

Using these filters, the approximation of the top half of the focused graph shows that the `Sort` function is reached through different call stacks. However, the metrics aren't aggregated so the graph doesn't illustrate overall metric consumption by `Sort`.

The focused graph is a little different than a graph that just combines the two approximations:

  * There is a single frame for the focus function `Sort`.
  * The focus function frame is highlighted, is full-width frame, and displays metrics that are the aggregation of all call stacks.
  * There are multiple call stacks, each beginning with a `root` frame, so you can view the entire call stack.



### Selecting a frame

If you select a frame in a focused graph, then the flame graph is redrawn with that frame's call stack displayed in more detail. If the frame is reached through multiple call stacks, each of those call stacks is displayed. Call stacks that don't include the frame are hidden from view. To restore the graph to its original state, select the frame that corresponds to the focus function.

In the previous example, `Sort` is called by `(*byFreq).sort` and by `(*byLiteral).sort`. To view the call stack for `(*byLiteral).sort` in more detail, select that frame. You can select another frame and further refine the call stacks being displayed:

![Flame graph expanded about sort.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-focus-sort-expanded.png)

To restore a focused flame graph to its original state, select the frame that displays the value of the **Focus** filter. In this case, select the gray frame with the label `Sort`. Note that to restore a standard flame graph to its original state you select the root frame.

### Analyzing the graph

To analyze a focused flame graph, you use the same controls and filters that you use to analyze a standard flame graph. However, there are differences in how the graphs interact with the pointer:

  * If your pointer hovers on a frame, the tooltip displays metric data. For a standard flame graph, total metric data for the frame is shown. For a focused flame graph, aggregate metric data for the function is shown.

  * If you select a frame, the flame graph is redrawn with that frame displayed full width. To restore a standard flame graph to its original form, you must select the top frame. To restore a focused flame graph to its original form, you must select the frame that displays the value of the focus filter.




For information on the focused graph when you are comparing profiles, see [Focusing a comparison](https://docs.cloud.google.com/profiler/docs/comparing-profiles#with-focus).

## Setting the focus filter

There are different methods you can use to set a focus filter but they result in the same graph.

### By using the graph

Place your pointer on the frame of interest, and then click **Focus** in the frame tooltip. The focus function is extracted from the frame. In this example the flame graph, which is expanded around the function `(*huffmanBitWriter).write`, displays three different call stacks:

![Flame graph focused on a tiny frame.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-graph-tiny-block-focused.png)

### By using the focus list

To focus the flame graph on a specific function, do the following:

  1. Click **List** _list_ to open the **Select focus function** table.
  2. Select a function name from the table or, for a specific function, click **Actions** _more_vert_ and then select **Focus** :



![Select focus function table.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-focus-select-focus-function.png)

If the function you selected can be called through different call stacks, each call stack is shown in the flame graph.

You can sort the table rows in ascending _arrow_upward_ or descending _arrow_downward_ order by selecting a table header element. Each row in the table displays a function name and statistics related to the function's execution. This table shows that the `(*compressor).deflate` function requires 2.78 s to execute, with 1.8 s spent in the function itself and the remainder of the time spent in its call stack. One percentage column reports that 57% of the total execution time is spent in the function `(*compressor).deflate`. Another column reports that 89% of the time, `(*compressor).deflate` or a function in its call stack, is executing. Lastly, the count column reports that there are three sequences that invoke the function `(*compressor).deflate`.

When you are comparing profiles, the content of the focus list is different. For more information, see [Focusing a comparison](https://docs.cloud.google.com/profiler/docs/comparing-profiles#with-focus).

### By using the filter bar

Click the gray text **Add profile data filter** in the filter bar, and then enter `Focus:` and a string that identifies the function to focus on. You can use a substring, including package prefixes, or the full name. When you supply an ambiguous string, the function that is the best match to the string is selected.

If you prefer, you can click **Filters** , select **Focus** , and then enter the identifying string.

If the function you selected can be called through different call stacks, each call stack is shown in the flame graph.

## Removing the focus filter

To remove the focus filter, click **Close** _close_ on the filter.

## What's next

  * [View historical trends](https://docs.cloud.google.com/profiler/docs/history-view). 
  * [Download profile data](https://docs.cloud.google.com/profiler/docs/downloading-profiles). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
