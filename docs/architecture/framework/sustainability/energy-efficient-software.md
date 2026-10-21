---
url: https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software/
title: Develop energy-efficient software \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:22.354209+00:00
---

# Develop energy-efficient software  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Develop energy-efficient software Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations to write software that minimizes energy consumption and server load.

## Principle overview

When you follow best practices to build your cloud applications, you optimize the energy that's utilized by the cloud infrastructure resources: AI, compute, storage, and network. You also help to reduce the water requirements of the data centers and the energy that end-user devices consume when they access your applications.

To build energy-efficient software, you need to integrate sustainability considerations throughout the software lifecycle, from design and development to deployment, maintenance, and archival. For detailed guidance about using AI to build software that minimizes the environmental impact of cloud workloads, see the Google Cloud ebook, [Build Software Sustainably](https://cloud.google.com/resources/content/build-software-sustainably).

## Recommendations

The recommendations in this section are grouped into the following focus areas:

  * Minimize computational work: Favor lean, focused code that eliminates redundant logic and avoids unnecessary computations or feature bloat.
  * Use efficient algorithms and data structures: Choose time-efficient and memory-efficient algorithms that reduce CPU load and minimize memory usage.
  * Optimize compute and data operations: Develop with the goal of efficiently using all of the available resources, including CPU, memory, disk I/O, and network. For example, when you replace busy loops with event-driven logic, you avoid unnecessary polling.
  * Implement frontend optimization: To reduce the power that's consumed by end-user devices, use strategies like minimization, compression, and [lazy-loading](https://en.wikipedia.org/wiki/Lazy_loading) for images and assets.



### Minimize computational work

To write energy-efficient software, you need to minimize the total amount of computational work that your application performs. Every unnecessary instruction, redundant loop, and extra feature consumes energy, time, and resources. Use the following recommendations to build software that performs minimal computations.

#### Write lean, focused code

To write minimal code that's essential to achieve the required outcomes, use the following approaches:

  * **Eliminate redundant logic and feature bloat** : Write code that performs only the essential functions. Avoid features that increase the computational overhead and complexity but don't provide measurable value to your users.
  * **Refactor** : To improve energy efficiency over time, regularly audit your applications to identify unused features. Take action to remove or refactor such features as appropriate.
  * **Avoid unnecessary operations** : Don't compute a value or run an action until the result is needed. Use techniques like [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation), which delay computations until a dependent component in the application needs the output.
  * **Prioritize code readability and reusability** : Write code that's readable and reusable. This approach minimizes duplication and follows the [don't repeat yourself (DRY) principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), which can help to reduce carbon emissions from software development and maintenance.



#### Use backend caching

Backend caching ensures that an application does not perform the same work repeatedly. A high cache-hit ratio leads to an almost linear reduction in energy consumption per request. To implement backend caching, use the following techniques:

  * **Cache frequent data** : Store frequently accessed data in a temporary, high-performance storage location. For example, use an in-memory caching service like [Memorystore](https://docs.cloud.google.com/memorystore/docs). When an application retrieves data from a cache, the volume of database queries and disk I/O operations is reduced. Consequently, the load on the databases and servers in the backend decreases.
  * **Cache API responses** : To avoid redundant and costly network calls, cache the results of frequent API requests.
  * **Prioritize in-memory caching** : To eliminate slow disk I/O operations and complex database queries, store data in high-speed memory (RAM).
  * **Select appropriate[cache-write strategies](https://en.wikipedia.org/wiki/Cache_\(computing\)#Write_policies)**: 
    * The write-through strategy ensures that data is written synchronously to the cache _and_ the persistent store. This strategy increases the likelihood of cache hits, so the persistent store gets fewer energy-intensive read requests.
    * The write-back (write-behind) strategy enhances the performance of write-heavy applications. Data is written to the cache first, and the database is updated asynchronously later. This strategy reduces the immediate write load on slower databases.
  * **Use smart eviction policies** : Keep the cache lean and efficient. To remove stale or low-utility data and to maximize the space that's available for frequently requested data, use policies like time to live (TTL), least recently used (LRU), and least frequently used (LFU).



### Use efficient algorithms and data structures

The algorithms and data structures that you choose determine the raw computational complexity of your software. When you select appropriate algorithms and data structures, you minimize the number of CPU cycles and memory operations that are required to complete a task. Fewer CPU cycles and memory operations lead to lower energy consumption.

#### Choose algorithms for optimal time complexity

Prioritize algorithms that achieve the required result in the least amount of time. This approach helps to reduce the duration of resource usage. To select algorithms that optimize resource usage, use the following approaches:

  * **Focus on reducing complexity** : To evaluate complexity, look beyond runtime metrics and consider the theoretical complexity of the algorithm. For example, when compared to [bubble sorting](https://en.wikipedia.org/wiki/Bubble_sort), [merge sorting](https://en.wikipedia.org/wiki/Merge_sort) significantly reduces the computational load and energy consumption for large datasets.
  * **Avoid redundant work** : Use built-in, optimized functions in your chosen programming language or framework. These functions are often implemented in a lower-level and more energy-efficient language like C or C++, so they are better optimized for the underlying hardware compared to custom-coded functions.



#### Select data structures for efficiency

The data structures that you choose determine the speed at which data can be retrieved, inserted, or processed. This speed affects CPU and memory usage. To select efficient data structures, use the following approaches:

  * **Optimize for search and retrieval** : For common operations like checking whether an item exists or retrieving a specific value, prefer data structures that are optimized for speed. For example, hash maps or hash sets enable near-constant time lookups, which is a more energy-efficient approach than linearly searching through an array.
  * **Minimize memory footprint** : Efficient data structures help to reduce the overall memory footprint of an application. Reduced memory access and management leads to lower power consumption. In addition, a leaner memory profile enables processes to run more efficiently, which lets you postpone resource upgrades.
  * **Use specialized structures** : Use data structures that are purpose-built for a given problem. For example, use a [trie](https://en.wikipedia.org/wiki/Trie) data structure for rapid string-prefix searching, and use a priority queue when you need to access only the highest or lowest value efficiently.



### Optimize compute and data operations

When you develop software, focus on efficient and proportional resource usage across the entire technology stack. Treat CPU, memory, disk, and network as limited and shared resources. Recognize that efficient usage of resources leads to tangible reductions in costs and energy consumption.

#### Optimize CPU utilization and idle time

To minimize the time that the CPU spends in an active, energy-consuming state without performing meaningful work, use the following approaches:

  * **Prefer event-driven logic over polling** : Replace resource-intensive busy loops or constant checking (polling) with event-driven logic. An event-driven architecture ensures that the components of an application operate only when they're triggered by relevant events. This approach enables on-demand processing, which eliminates the need for resource-intensive polling.
  * **Prevent constant high frequency** : Write code that doesn't force the CPU to constantly operate at its highest frequency. To minimize energy consumption, systems that are idle should be able to enter low-power states or sleep modes.
  * **Use asynchronous processing** : To prevent threads from being locked during idle wait times, use asynchronous processing. This approach frees resources and leads to higher overall resource utilization.



#### Manage memory and disk I/O efficiently

Inefficient memory and disk usage leads to unnecessary processing and increased power consumption. To manage memory and I/O efficiently, use the following techniques:

  * **Strict memory management** : Take action to proactively release unused memory resources. Avoid holding large objects in memory for longer periods than necessary. This approach prevents performance bottlenecks and reduces the power that's consumed for memory access.
  * **Optimize disk I/O** : Reduce the frequency of your application's read and write interactions with persistent storage resources. For example, use an intermediary memory buffer to store data. Write the data to persistent storage at fixed intervals or when the buffer reaches a certain size.
  * **Batch operations** : Consolidate frequent, small disk operations into fewer, larger batch operations. A batch operation consumes less energy than many individual, small transactions.
  * **Use compression** : Reduce the amount of data that's written to or read from disks by applying suitable data-compression techniques. For example, to compress data that you store in Cloud Storage, you can use [decompressive transcoding](https://docs.cloud.google.com/storage/docs/transcoding).



#### Minimize network traffic

Network resources consume significant energy during data transfer operations. To optimize network communication, use the following techniques:

  * **Minimize payload size** : Design your APIs and applications to transfer only the data that's needed for a request. Avoid fetching or returning large JSON or XML structures in cases where only a few fields are required. Ensure that the data structures that are returned are concise.
  * **Reduce round-trips** : To reduce the number of network round-trips that are required to complete a user action, use smarter protocols. For example, prefer HTTP/3 over HTTP/1.1, choose GraphQL over REST, use binary protocols, and consolidate API calls. When you reduce the volume of network calls, you reduce the energy consumption for both your servers and for end-user devices.



### Implement frontend optimization

Frontend optimization minimizes the data that your end users must download and process, which helps to reduce the load on the resources of end-user devices.

#### Minimize code and assets

When end users need to download and process smaller and more efficiently structured resources, their devices consume less power. To minimize the download volume and processing load on end-user devices, use the following techniques:

  * **Minimization and compression** : For JavaScript, CSS, and HTML files, remove unnecessary characters like whitespaces and comments by using appropriate minimization tools. Ensure that files like images are compressed and optimized. You can automate the minimization and compression of web assets by using a CI/CD pipeline.
  * **Lazy loading** : Load images, videos, and non-critical assets only when they are actually needed, such as when these elements scroll into the viewport of a web page. This approach reduces the volume of initial data transfer and the processing load on end-user devices.
  * **Smaller JavaScript bundles** : Eliminate unused code from your JavaScript bundles by using modern module bundlers and techniques like [tree shaking](https://webpack.js.org/guides/tree-shaking/). This approach results in smaller files that load faster and use fewer server resources.
  * **Browser caching** : Use HTTP caching headers to instruct the user's browser to store static assets locally. Browser caching helps to prevent repeated downloads and unnecessary network traffic on subsequent visits.



#### Prioritize lightweight user experience (UX)

The design of your user interface can have a significant impact on the computational complexity for rendering frontend content. To build frontend interfaces that provide a lightweight UX, use the following techniques:

  * **Efficient rendering** : Avoid resource-intensive, frequent [Document Object Model (DOM)](https://en.wikipedia.org/wiki/Document_Object_Model) manipulation. Write code that minimizes the rendering complexity and eliminates unnecessary re-rendering.
  * **Lightweight design patterns** : Where appropriate, prefer static sites or [progressive web apps (PWAs)](https://en.wikipedia.org/wiki/Progressive_web_app). Such sites and apps load faster and require fewer server resources.
  * **Accessibility and performance** : Responsive, fast-loading sites are often more sustainable and accessible. An optimized, clutter-free design reduces the resources that are consumed when content is rendered. Websites that are optimized for performance and speed can help to drive higher revenue. According to a research study by Deloitte and Google, [Milliseconds Make Millions](https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_report_hQYAbZJ.pdf#page=5), a 0.1-second (100ms) improvement in site speed leads to an 8.4% increase in conversions for retail sites and a 9.2% increase in the average order value.



[ Previous arrow_back  Optimize resource usage  ](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage)

[ Next Optimize data and storage  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
