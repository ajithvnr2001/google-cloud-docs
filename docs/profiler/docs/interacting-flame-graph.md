---
url: https://docs.cloud.google.com/profiler/docs/interacting-flame-graph/
title: Interact with the flame graph \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:51.440047+00:00
---

# Interact with the flame graph  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/interacting-flame-graph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Interact with the flame graph

Cloud Profiler displays profiling data by using flame graphs. For a conceptual introduction, see [Flame graphs](https://docs.cloud.google.com/profiler/docs/concepts-flame).

The flame graph is composed of _frames_. Each frame represents a function in the service:

  * The width of a frame corresponds to its consumption of the metric being analyzed. The top frame, for example, represents the entire service and consumes 100% of the metric being analyzed. Therefore, this frame is shown as full width.

  * By default, the frame color corresponds, where possible, to the function's package. If package information is unavailable, as with Node.js, the names of the source files are used to color the function blocks. In a call stack, a change in block color means a transition from one package to another. You can change the way the frames are colored. For more information, see [Color mode](https://docs.cloud.google.com/profiler/docs/filtering-profiles#color-filter).




The flame graph shows one or more call stacks with the values averaged over a set of profiles:

  * Each individual profile represents data collected one time per minute from a single instance of the configured service in a single Compute Engine zone. The collection period for a profile varies with the profile type. See [Profile collection](https://docs.cloud.google.com/profiler/docs/concepts-profiling#collection) for more information.
  * A maximum of 250 profiles are averaged. If there are more than 250 profiles available, 250 of them are selected randomly as a sample set.
  * The top frame, or "root", in a flame graph represents the entire service. Under the "root" frame, is another frame or set of frames making up the second row in the graph. Each of these color-coded frames is a top-level call made by the service. Under each of those colored function frames is another set of function frames, each of which is responsible for some part of the resource of the frame above it. The hierarchy of function frames in the graph represents the call sequence, and the width of a frame represents that function or method's contribution to the resource consumption.



For example, the profiler graph of the consumed heap for the docdemo-service shows that the service calls different top-level frames, one of them is the Go runtime's `main` function. The width of these top-level frames show the majority of the heap is consumed by the call stack involving Go runtime's `main`, application-specific `main`, `allocOnce`, and `allocImpl`:

![Profiler graph for consumed heap.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-heap.png)

The root frame displays metric consumption information.

## Hovering over a frame

When you hold the pointer over a frame in the flame graph, a frame tooltip opens and displays additional information about the frame:

  * Function name
  * Function filename
  * Absolute usage and percentage usage



In the metric consumption information, the prefix **total** indicates that the metric-value and percentage are for a function and its children. In contrast, the prefix **self** indicates the metric-value and percentage are for the function with the consumption of its children excluded.

The dialog also includes buttons:

  * [**Focus**](https://docs.cloud.google.com/profiler/docs/focusing-profiles): Focuses the graph on the current frame's function.
  * [**Show stacks**](https://docs.cloud.google.com/profiler/docs/filtering-profiles#stack-filters): Adds a filter to only show the stacks that include this frame's function.
  * [**Show history**](https://docs.cloud.google.com/profiler/docs/history-view): Opens the history view for the frame's function.



In this example, the tooltip shows that the `runtime.main` function is located in the `/usr/local/go/src/runtime/proc.go` file. The metric consumption information shows that `runtime.main` and its children consume 54.73 MiB of memory, or about 98% of the total memory consumed by the program:

![Metric consumption for runtime.main.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-heap-main.png)

## Selecting a frame

When you select a frame, the flame graph is redrawn with that frame shown full width and the colors higher in the call stack are muted. Selecting on a frame doesn't change any settings, it only changes how the graph is displayed. To revert to the original view, select the root (top) frame.

In the following example, the pointer is on a tiny frame and it is difficult to view the call stack. The tooltip identifies `(*huffmanBitWriter).write` as the frame function:

![A tiny frame in the flame graph.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-graph-tiny-block.png)

After you select the frame, the graph is redrawn, making the call stack more visible:

![The tiny frame expanded.](https://docs.cloud.google.com/static/profiler/docs/images/profiler-graph-tiny-block-expanded.png)

**Note:** To restore a standard flame graph to the original state, select the root (top) frame. To restore a focused flame graph to its original state, select the frame that displays the value of the **Focus** filter. For example, if your filter bar contains `Focus: Sort`, select the frame with the label `Sort`.

## What's next

  * [Filter the flame graph](https://docs.cloud.google.com/profiler/docs/filtering-profiles). 
  * [Focus the flame graph on a function](https://docs.cloud.google.com/profiler/docs/focusing-profiles). 
  * [View historical trends](https://docs.cloud.google.com/profiler/docs/history-view). 
  * [Compare profiles](https://docs.cloud.google.com/profiler/docs/comparing-profiles). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
