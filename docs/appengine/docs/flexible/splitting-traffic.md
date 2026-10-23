---
url: https://docs.cloud.google.com/appengine/docs/flexible/splitting-traffic/
title: Splitting traffic \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:44.171237+00:00
---

# Splitting traffic  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/splitting-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Splitting traffic Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

You can use traffic splitting to specify a percentage distribution of traffic across two or more of the versions within a service. Splitting traffic allows you to conduct [A/B testing](https://wikipedia.org/wiki/A/B_testing) between your versions and provides control over the pace when rolling out features.

Traffic splitting is applied to URLs that do not explicitly target a [version](https://docs.cloud.google.com/appengine/docs/flexible/an-overview-of-app-engine#versions). For example, the following URLs split traffic because they target all the available versions within the specified service:

  * `https://PROJECT_ID.REGION_ID.r.appspot.com` \- Distributes traffic to versions of the `default` service.
  * `https://SERVICE_ID-dot-PROJECT_ID.REGION_ID.r.appspot.com` \- Distributes traffic to versions of the `[SERVICE_ID]` service.



For information about how requests reach a version, see [How requests are routed](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed).

## Before you begin

Before you can configure traffic to a version, ensure that your user account includes the [required privileges](https://docs.cloud.google.com/appengine/docs/flexible/access-control#basic_roles).

## Avoiding caching issues

Before you turn on traffic splitting, you might want to account for potential caching problems. Caching issues can exist for any App Engine app, especially when deploying a new version. Traffic splitting often makes subtle caching problems more apparent.

For example, assume you are splitting traffic between two versions, A and B, and some external cacheable resource changed between versions, for example, a CSS file. Now assume that a client makes a request and the response contains an external reference to the cached file. The local HTTP cache will retrieve the file if it's in the cache, regardless of which version of the file is cached and which version of the application sent the response. The cached resource could be incompatible with the data that was sent in the response.

To avoid caching problems:

  * For dynamic resources, set both the [Cache-Control](https://www.rfc-editor.org/rfc/rfc9111#name-extension-directives) and [Expires](https://www.rfc-editor.org/rfc/rfc9111#name-expires) headers. These headers tell proxies that the resource is dynamic. It is best to set both headers, since not all proxy servers support the HTTP/1.1 `Cache-Control` header properly.

If you want more information on caching in general, see [Header Fields in the HTTP/1.1 RFC](https://www.rfc-editor.org/rfc/rfc9110.html#name-header-fields) and the [HTTP caching overview in Web Fundamentals](https://developers.google.com/web/fundamentals/performance/get-started/httpcaching-6).

  * For cacheable static resources that vary between versions, change the resource's URL between versions. If the static resources are served from different URLs, then both versions can happily co-exist in proxy servers and browser caches.




You can also have your app set the [Vary: Cookie](https://wikipedia.org/wiki/HTTP_Cookie) header so that the uniqueness of a resource is computed by combining the cookies and the URL for the request. However, this approach increases the burden on cache servers. There are 1000 possible values of `GOOGAPPUID`, and hence 1000 possible entries for each URL for your app. Depending on the load on the proxies between your users and your app, this can decrease how often your app serves a cached result. In addition, for the 24 hours after adding a new batch of users to a version, those users might still see cached resources. However, using `Vary: Cookie` can make it easier to rename static resources that are changing between versions.

The `Vary: Cookie` technique doesn't work in all circumstances. In general, if your app is using cookies for other purposes, you must consider how this affects the burden on proxy servers. If `codeninja` had its own cookie that had 100 possible values, then the space of all possible cache entries becomes a very big number (100 * 1000 = 100,000). In the worst case, there is a unique cookie for every user. Two common examples of this are Google Analytics (`__utma`) and SiteCatalyst (`s_vi`). In these cases, every user gets a unique copy, which severely degrades cache performance and can also increase the billable instance hours consumed by your app.

## Splitting traffic across multiple versions

When you have specified two or more versions for splitting, you must choose whether to split traffic by using either a sender IP address or HTTP cookie. It's easier to set up an IP address split, but a cookie split is more precise. For more information, see IP address splitting and Cookie splitting.

### Console

To split traffic in the Google Cloud console, go to the Versions page:

[Go to Versions](https://console.cloud.google.com/appengine/versions)

  1. Select one or more versions to which you want to split traffic.
  2. Click **Split traffic** and then specify: 
     * The method that you want to use for splitting traffic.
     * The percentage of traffic each version should receive.



### gcloud

After installing the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), you run the following command to split traffic across multiple versions, for example:
    
    
    gcloud app services set-traffic [MY_SERVICE] --splits [MY_VERSION1]=[VERSION1_WEIGHT],[MY_VERSION2]=[VERSION2_WEIGHT] --split-by [IP_OR_COOKIE]
    

For details and additional options, see the [`gcloud app services set-traffic`](https://docs.cloud.google.com/sdk/gcloud/reference/app/services/set-traffic) reference.

### API

To programmatically migrate traffic, you can use the Admin API, see [Migrating and Splitting Traffic](https://docs.cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic) for details.

### IP address splitting

If you choose to split traffic to your application by sender IP address, when the application receives a request, it hashes the IP address to a value between 0–999, and uses that number to route the request.

IP address splitting has some significant limitations:

  * Sender IP addresses are reasonably sticky, but are not permanent. Users connecting from cell phones might have a shifting IP address throughout a single session. Similarly, a user on a laptop might be moving from home to a cafe to work, and will also shifting through IP addresses. As a result, the user might have an inconsistent experience with your app as their IP address changes.
  * Because IP addresses are independently assigned to versions, the resulting traffic split will differ somewhat from what you specify. Although, as your application receives more traffic, the closer the actual split gets to your target. For example, if you ask for 5% of traffic to be delivered to an alternate version, the initial percent of traffic to the version might actually be between 3–7% but eventually averages closer to your target 5%.
  * If you need to send internal requests between apps, you should use cookie splitting instead. Requests that are sent between apps running on Google's cloud infrastructure, originate from a small number of IP addresses which are likely all assigned to the same version. Therefore, all internal requests might behave similar to requests sent from a single IP address, meaning that those requests are all routed to the same version. As a result, internal requests do not closely respect the percentages that you set for your IP-based traffic splits. For example, if you set a version to receive 1% of all the traffic to your app and the Google cloud infrastructure addresses were coincidently assigned to that version, then the actual result might far exceed 1% because all the internal requests are always routed to the assigned version. Requests sent to your app from outside of Google's cloud infrastructure will work as expected since they originate from a varied distribution of IP addresses.



### Cookie splitting

If you choose to split traffic to your application by cookies, the application looks in the [HTTP request header](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-handled) for a cookie named `GOOGAPPUID`, which contains a value between 0–999:

  * If the cookie exists, the value is used to route the request.
  * If there is no such cookie, App Engine generates a cookie with a masked random value to route the request.



If the response does not contain the `GOOGAPPUID` cookie, the app first adds the `GOOGAPPUID` cookie with a masked random value between 0–999 before it is sent.

Using cookies to split traffic makes it easier to accurately assign users to versions.

For example, if you have 3 versions:

  * Version A with 10% of Traffic
  * Version B with 60% of Traffic
  * Version C with 30% of Traffic



App Engine creates 1000 shards, and each version is assigned a number of shards corresponding to its traffic split percentage. From this example, Version A has 100 shards, Version B has 600 shards, and Version C has 300 shards.

App Engine uses the value of the `GOOGAPPUID` cookie to determine which shard a request is assigned to, and routes the request to the corresponding version. Precision for traffic routing might reach close to 0.1% to the target split. Cookie splitting has the following limitations: 

  * If you are writing a mobile app or running a desktop client, it needs to manage the `GOOGAPPUID` cookies. For example, when a `Set-Cookie` response header is used, you must store the cookie and include it with each subsequent request. Browser-based apps already manage cookies in this way automatically.

  * Splitting internal requests requires extra work. All user requests that are sent from within Google's cloud infrastructure, require that you forward the user's cookie with each request. For example, you must forward the user's cookie in requests sent from your app to another app, or to itself. Note that it is not recommended to send internal requests if those requests don't originate from a user.

  * There isn't a way to determine which version handles a particular value on `GOOGAPPUID` cookie. However, the same version handles requests with the same value on `GOOGAPPUID` cookie.




## Disabling traffic splitting

To disable traffic splitting, you [migrate all traffic to a single version](https://docs.cloud.google.com/appengine/docs/flexible/migrating-traffic).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
