---
url: https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection/
title: Best practices for Compute Engine regions selection \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:00.118964+00:00
---

# Best practices for Compute Engine regions selection  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Best practices for Compute Engine regions selection Stay organized with collections  Save and categorize content based on your preferences. 

This article describes criteria to consider when choosing which Google Cloud regions to use for your Compute Engine resources, a decision that is typically made by cloud architects or engineering management. This document primarily focuses on the latency aspect of the selection process and is intended for apps accessed by consumers, such as mobile or web apps or games, but many of the concepts can apply to other use cases.

Google offers [multiple regions worldwide](https://docs.cloud.google.com/compute/docs/regions-zones) to deploy your Compute Engine resources. Several factors play a role in choosing your regions:

  * Region-specific restrictions
  * User latency by region
  * Latency requirements of your app
  * Amount of control over latency
  * Balance between low latency and simplicity



## Terminology

region
    An independent geographic area where you run your resources. Each region consists of zones, typically at least three zones.
zone
    A deployment area for Google Cloud resources within a region. Putting resources in different zones in a region reduces the risk of an infrastructure outage affecting all resources simultaneously.
Compute Engine resources
    Resources in Compute Engine, such as [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances), are deployed in a zone within a region. Other products, such as [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) and [Dataflow](https://docs.cloud.google.com/dataflow), use Compute Engine resources and therefore, can be deployed in the same regions or zone.
round-trip time (RTT)
    The time it takes to send an IP packet and to receive the acknowledgment.

## When to choose your Compute Engine regions

Early in the architecture phase of an app, decide how many and which Compute Engine regions to use. Your choice might affect your app, for example:

  * Architecture of your app might change if you sync some data between copies because the same users could connect through different regions at different times.
  * Price differs by region.
  * Process to move an app and its data between regions is cumbersome, and sometimes costly, so should be avoided once the app is live.

**Note:** The availability of regions and the user profile of apps might change after launch, and this document can still provide guidance.

## Factors to consider when selecting regions

It's common for people to deploy in a region where they're located, but they fail to consider if this is the best user experience. Suppose that you're located in Europe with a global user base and want to deploy in a single region. Most people would consider deploying in a region in Europe, but it is usually the best choice to have this app hosted in one of the US regions–because the US is the most connected to other regions.

Multiple factors affect where you decide to deploy your app.

### Latency

The main factor to consider is the latency your user experiences. However, this is a complex problem because user latency is affected by multiple aspects, such as caching and load-balancing mechanisms.

In enterprise use cases, latency to on-premises systems or latency for a certain subset of users or partners is more critical. For example, choosing the closest region to your developers or on-premises database services interconnected with Google Cloud might be the deciding factor.

### Pricing

Google Cloud resource costs differ by region. The following resources are available to estimate the price:

  * [Compute Engine pricing](https://cloud.google.com/skus/?currency=USD)

  * [Pricing calculator](https://cloud.google.com/products/calculator/)

  * [Google Cloud SKUs](https://cloud.google.com/skus/)

  * [Billing API](https://docs.cloud.google.com/billing/reference/rest/v1/services.skus/list)




If you decide to deploy in multiple regions, be aware that there are [data transfer charges](https://docs.cloud.google.com/vpc/network-pricing#general) for data synced between regions.

### Colocation with other Google Cloud services

Colocate your Compute Engine resources with other Google Cloud services, wherever possible. While most latency-sensitive services are available in every region, some services are available only in [specific locations](https://cloud.google.com/about/locations/).

### Machine-type availability

Not all CPU platforms and machine types are available in every region. The availability of specific CPU platforms or specific instance types differs by region and even zone. If you want to deploy resources using certain machine types, find out about [zonal availability of these resources](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### Resource quotas

Your ability to deploy Compute Engine resources is limited by regional [resource quotas](https://docs.cloud.google.com/compute/quotas), so make sure that you request sufficient quota for the regions you plan to deploy in. If you are planning an especially large deployment, work with the sales team early to discuss your region selection choices to ensure that you have sufficient quota capacity.

### Carbon-free energy percentage

To power each Google Cloud region, Google uses electricity from the grid where the region is located. This electricity generates more or less carbon emissions, depending on the type of power plants generating electricity for that grid and when Google consumes it. Google recently set the goal that by 2030, we'll have carbon-free electricity powering your applications in the time and the place that you need them—24 hours a day, in every Google Cloud region.

Until that goal is achieved, each Google Cloud region will be supplied by a mix of carbon-based and carbon-free energy sources every hour. We call this metric our carbon-free energy percentage (CFE%) and [we publish CFE% for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon). For new applications on Google Cloud, you can use this table to begin incorporating carbon impact into your architecture decisions. Choosing a region with a higher CFE % means that, on average, your application will be powered with carbon-free energy a higher percentage of the hours that it runs, reducing the gross carbon emissions of that application.

## Evaluate latency requirements

Latency is often the key consideration for your region selection because high user latency can lead to an inferior user experience. You can affect some aspects of latency, but some are outside of your control.

When optimizing for latency, many system architects consider only network latency or distance between the user's ISP and the virtual machine instance. However, this is only one of many factors affecting user latency, as you can see in the following diagram.

![Evaluate latency in compute engine region selection](https://docs.cloud.google.com/static/solutions/images/best-practices-compute-engine-region-selection-1evaluate.svg)

As an app architect, you can optimize the region selection and app latency, but have no control over the users' last mile and latency to the closest Google edge [Points of Presence (POP)](https://wikipedia.org/wiki/Point_of_presence).

Region selection can only affect the latency to the Compute Engine region and not the entirety of the latency. Depending on the use case, this might be only a small part of overall latency. For example, if your users are primarily using cellular networks, it might not be valuable to try to optimize your regions, as this hardly affects total user latency.

### Last mile latency

The latency of this segment differs depending on the technology used to access the internet. For example, the typical latency to reach an ISP is 1-10 ms on modern networks. Conversely, typical latencies on a 3G cellular network are 100-500 ms. The latency range for DSL and cable providers is roughly 10-60 ms.

### Google frontend and edge POP latency

Depending on your deployment model, the latency to Google's network edge is also important. This is where global load-balancing products terminate TCP and SSL sessions and from which Cloud CDN delivers cached results. Based on the content served, many round-trips might already end here because only part of the data needs to be retrieved the whole way. This latency might be significantly higher if you use the [standard network service tier](https://docs.cloud.google.com/network-tiers).

### Compute Engine region latency

The user request enters Google's network at the edge POP. The Compute Engine region is where Google Cloud resources handling requests are located. This segment is the latency between the edge POP and Compute Engine region, and sits wholly within Google's global network.

### App latency

This is the latency from the app responding to requests, including the time the app needs in order to process the request.

Different apps have different latency requirements. Depending on the app, users are more forgiving of latency issues. Apps that interact asynchronously or mobile apps with a high latency threshold—100 milliseconds or more—can be deployed in a single region without degrading the user experience. However, for apps such as real-time games, a few milliseconds of latency can have a greater effect on user experience. Deploy these types of apps in multiple regions close to the users.

## Global deployment patterns

This section explains how various deployment models affect latency factors.

### Single region deployment

The following image illustrates a single region deployment.

![Latency of single frontend deployment](https://docs.cloud.google.com/static/solutions/images/best-practices-compute-engine-region-selection-2single.svg)

Even if your app serves a global user base, in many cases, a single region is still the best choice. The lower latency benefits might not outweigh the added complexity of multi-region deployment. Even with a single region deployment, you can still use optimizations, such as Cloud CDN and global load balancing, to reduce user latency. You can choose to use a second region for backup and disaster recovery reasons, but this does not affect the app's serving path and therefore, won't affect user latency.

### Distributed frontend in multiple regions and backend in a single region

The following diagram shows a deployment model where you distribute the frontend across multiple regions but limit the backend to a single region. This model gives you the benefit of lower latency to the frontend servers while not not having to sync data across multiple regions.

![Latency of distributed frontend deployment](https://docs.cloud.google.com/static/solutions/images/best-practices-compute-engine-region-selection-3distributed.svg)

This deployment model provides low user latency in scenarios where the average user request involves no data requests or involves just a few data requests to the central backend before the app can produce a result. An example is an app that deploys an intelligent caching layer on the frontend or that handles data writes asynchronously. An app that makes many requests that require a full roundtrip to the backend may not benefit from this model.

### Distributed frontend and backend in multiple regions

A deployment model where you distribute the frontend and backend in multiple regions lets you minimize user latency because the app can fully answer any request locally. However, this model comes with added complexity because all data needs to be stored and accessible locally. To answer all user requests, data needs to be fully replicated across all regions.

![Latency of distributed multi deployment](https://docs.cloud.google.com/static/solutions/images/best-practices-compute-engine-region-selection-4distrubutedmulti.svg)

Spanner—the globally consistent managed database offering—has a [three-continent multi-regional](https://docs.cloud.google.com/spanner/docs/instances#multi-region_configurations) option, where, in addition to read-write replicas in the US, two read replicas are situated in Europe and Asia. This option provides low-latency read access to the data to compute instances situated in US, Europe, or Asia. If your service is targeting the US, a multi-regional option with replication within the US also exists.

If you decide to run your own database service on Compute Engine, you replicate the data yourself. This replication is a significant undertaking because keeping data consistently synced globally is difficult to do. It is easier to manage if the database gets written to only one region by asynchronous writes and the other regions host read-only replicas of the database.

Replicating databases across regions is difficult, and we recommend engaging a strong partner with experience in this area, such as [Datastax](https://www.datastax.com/) for Cassandra replication.

### Multiple parallel apps

Depending on the nature of your app, with a variation of the previous approach, you can preserve the low user latency while reducing the need for constant data replication. As illustrated in the following image, there are multiple parallel apps, all consisting of a frontend and backend, and users are directed to the correct app. Only a small fraction of data is shared between the sites.

![Latency of parallel apps](https://docs.cloud.google.com/static/solutions/images/best-practices-compute-engine-region-selection-5multiparallel.svg)

For example, when running a retail business you might serve users in different regions through different country domains and run parallel sites in all those regions, only syncing product and user data when necessary. Local sites maintain their local stock availability and users connect to a locally hosted site by selecting a country domain. When a user visits a different country domain, they are redirected to the correct domain.

Another example is in real-time games. You might only have a global lobby service where users choose a game room or world close to their location and those rooms or worlds do not share data with each other.

A third example is offering Software-as-a-Service (SaaS) in different regions, where data location is selected upon account creation, either based on user location or their choice. After they log in, the user is redirected to a location specific subdomain and uses the service regionally.

## Optimize latency between users and regions

Regardless of your deployment model, you can combine optimization methods to reduce the visible latency to the end user. Some of these methods are Google Cloud features, while others require you to change your app.

### Use Premium Tier networking

Google offers premium (default) and standard [Network Service Tiers](https://docs.cloud.google.com/network-tiers). Standard Tier traffic is delivered over transit ISPs from Google Cloud regions, while Premium Tier offers lower latency by delivering the traffic through Google's global private network. Premium Tier networking reduces user latency and should be used for all parts of the app in the serving path. Premium Tier networking is also necessary to use Google's global load-balancing products.

### Use Cloud Load Balancing and Cloud CDN

Cloud Load Balancing, such as HTTP(S) load balancing, TCP, and SSL proxy load balancing, let you automatically redirect users to the closest region where there are backends with available capacity.

Even if your app is only in a single region, [using Cloud Load Balancing still provides lower user latency](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency) because TCP and SSL sessions are terminated at the network edge. Easily terminate user traffic with HTTP/2 and Quick UDP Internet Connections (QUIC). You can also integrate Cloud CDN with HTTP(S) load balancing to deliver static assets directly from the network edge, further reducing user latency.

### Cache locally

When your frontend locations are different from your backend locations, make sure to cache answers from backend services whenever possible. When the frontend and backend are in the same region, app latency is reduced because time-consuming queries are also reduced. Memorystore for Redis is a fully managed in-memory data store you can use.

### Optimize your app client or web frontend

You can use techniques on the client side, either a mobile app or the web frontend, to optimize user latency. For example, preload some assets or cache data within the app.

You can also optimize the way your app fetches information by reducing the number of requests and retrieving information in parallel, whenever possible.

## Measure user latency

Once you establish a baseline of your latency requirements, look at your user base to decide the best placement of your Google Cloud resources. Depending on whether this is a new or existing app, there are different strategies to employ.

Use the following strategies to measure latency to partners that you access during app serving or to measure latency to your on-premises network that might be interconnected to your Google Cloud project using Cloud VPN or Dedicated Interconnect.

### Estimate latency for new workloads

If you don't have an existing app with a similar user base to your new app, estimate latency from various Google Cloud regions based on rough location distribution of your expected user base.

Estimate 1 ms of round-trip latency for every 100 km traveled. Because networks do not follow an ideal path from source to destination, you can usually guess that actual distance is around 1.5 to 2 times the distance measured on a map. Of course, in some less densely populated regions, networks might follow an even less ideal path. The latency added through active equipment within ISP networks is usually negligible when looking at cross-regional distances.

These numbers can help you estimate latency to edge POP and Cloud CDN nodes, as well as Compute Engine regions around the globe as listed on the [network map](https://cloud.google.com/about/locations/#meet-our-network).

### Measure latency to existing users

If you already have an existing app with a similar user base, there are several tools that you can use to better estimate latencies.

  * **Representative users** : If you have users or partners, that represent a cross-section of your geographical distributions and that are willing to work with you, or employees in those countries, ask them to measure the latency to various Google Cloud regions. Tools such as [Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview) can help you get some measurements.
  * **Access logs** : If you have an active app hosted outside of Google Cloud, use data from the access logs to get a rough cross-section of users. Your logs might provide country or city information, which also lets you estimate latencies.
  * **IP address** : If you have access to your users' IP addresses, create scripts to test reachability and latencies from various Google Cloud regions. If their firewall blocks your probes, try to randomize the last IP octet to get a response from another device with similar latency to your app.
  * **Latency information from Google Cloud** : If you have an existing app in Google Cloud, there are several ways to collect latency information.

    * [User-defined request headers](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service#user-defined-request-headers): Activate headers for customers' country, subregion, and city information, as well as estimated RTT between the load balancer and the client.
    * [Cloud Monitoring metrics for HTTP(S) load balancing](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics_for): Include frontend RTT and backend latencies.
    * [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs): You get the TCP RTT between both ends of a connection as part of the metrics provided.



### Global connectivity

When estimating latency, keep the [topology of Google's global network](https://cloud.google.com/about/locations/#meet-our-network) in mind.

  * POPs: Where user traffic enters the network.
  * Cloud CDN nodes: Where traffic is cached.
  * Regions: Where your resources can be located.
  * Connectivity: Between the POPs and regions.



Find a list of locations where Google interconnects with other ISPs in [PeeringDB](http://as15169.peeringdb.com/).

Make sure to take interregional topology into consideration when deciding which regions to deploy in. For example, if you want to deploy an app with a global user base in a single region, it is usually best to have this app hosted in one of the US regions–because the US is connected to most other regions. Although there is direct connectivity between many continents, there are cases where it is missing, for instance, between Europe and Asia, so traffic between Europe and Asia flows through the US.

If your app is hosted across multiple regions and you need to synchronize data, be aware of latency between those regions. While this latency can change over time, it is usually stable. Either measure latency yourself by bringing up test instances in all potential regions or use third-party websites to get an idea of current latencies between regions.

## Put it all together

Now that you have considered latency requirements, potential deployment models, and the geographic distribution of your user base, you understand how these factors affect latency to certain regions. It is time to decide which regions to launch your app in.

Although there isn't a right way to weigh the different factors, the following step-by-step methodology might help you decide:

  1. See if there are non-latency related factors that block you from deploying in specific regions, such as price or colocation. Remove them from your list of regions.
  2. Choose a deployment model based on the latency requirements and the general architecture of the app. For most mobile and other non-latency critical apps, a single region deployment with Cloud CDN delivery of cacheable content and SSL termination at the edge might be the optimal choice.
  3. Based on your deployment model, choose regions based on the geographic distribution of your user base and your latency measurements:

     * For a single region deployment:

       * If you need low-latency access to your corporate premises, deploy in the region closest to this location.
       * If your users are primarily from one country or region, deploy in a region closest to your representative users.
       * For a global user base, deploy in a region in the US.
     * For a multi-region deployment:

       * Choose regions close to your users based on their geographic distribution and the app's latency requirement. Depending on your app, optimize for a specific median latency or make sure that 95-99% of users are served with a specific target latency. Users in certain geographical locations often have a higher tolerance for latency because of their infrastructure limitations.
  4. If user latency is similar in multiple regions, pricing might be the deciding factor.




When selecting Compute Engine regions, latency is one of the biggest factors to consider. Evaluate and measure latency requirements to deliver a quality user experience, and repeat the process if the geographic distribution of your user base changes.

## What's next

  * Review Compute Engine [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * Learn about [Optimizing application latency with load balancing](https://docs.cloud.google.com/compute/docs/load-balancing/optimize-app-latency).
  * Read the [Google Cloud for data center professionals](https://docs.cloud.google.com/docs/compare/data-centers) guide.
  * Watch the [Cloud performance atlas](https://www.youtube.com/playlist?list=PLIivdWyY5sqK5zce0-fd1Vam7oPY-s_8X) video series.
  * For a more complete view on how to optimize user latency, see the [High-performance browser networking](https://hpbn.co/) site.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
