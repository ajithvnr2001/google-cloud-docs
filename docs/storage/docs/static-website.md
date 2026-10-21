---
url: https://docs.cloud.google.com/storage/docs/static-website/
title: Static website examples and tips \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:20.435086+00:00
---

# Static website examples and tips  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/static-website/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Static website examples and tips Stay organized with collections  Save and categorize content based on your preferences. 

You can host a static website on a Cloud Storage bucket. Use buckets to serve assets like HTML, CSS, JavaScript, and images. You can also configure custom index and error pages, and manage subdomains for your site. This page provides configuration examples and tips for hosting a static website on Cloud Storage.

To get started, see [Host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website).

## Specialty pages

When you configure a bucket to host a static website, you can specify specialty pages, such as index pages and error pages. The following sections describe these pages.

### Index pages

An index page (also called a [webserver directory index](https://wikipedia.org/wiki/Webserver_directory_index)) is a file served to visitors when they request a URL that doesn't have an associated file. When you assign a `MainPageSuffix` property, Cloud Storage looks for a file with that name whose prefix matches the URL the visitor requested.

For example, say you set the `MainPageSuffix` of your static website to `index.html`. Additionally, say you have no file named `directory` in your bucket `www.example.com`. In this situation, if a user requests the URL `http://www.example.com/directory`, Cloud Storage attempts to serve the file `www.example.com/directory/index.html`. If that file also doesn't exist, Cloud Storage returns an error page.

The `MainPageSuffix` also controls the file served when users request the top level site. Continuing the preceding example, if a user requests `http://www.example.com`, Cloud Storage attempts to serve the file `www.example.com/index.html`.

When attempting to access a URL with a trailing slash, such as `http://www.example.com/dir/`, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#empty-obj).

### Error page

The error page is the file returned to visitors of your static site who request a URL that does not correspond to an existing file. If you have assigned a `MainPageSuffix`, Cloud Storage only returns the error page if there is neither a file with the requested name nor an applicable index page.

When returning an error page, the http response code is `404`. The property that controls which file acts as the error page is `NotFoundPage`. If you don't set `NotFoundPage`, users receive a generic error page.

## Website configuration examples

### Three-object bucket

Suppose a bucket named `www.example.com` has been configured as a website with the following settings and files:

  * `MainPageSuffix` = "index.html"
  * `NotFoundPage` = "404.html"
  * The bucket contains three publicly shared objects: "index.html", "404.html", and "dir/index.html".

**Note:** An empty object might exist at `http://www.example.com/dir/`. If an empty object exists, it is returned instead of the directory's `index.html` file. [See the troubleshooting topic](https://docs.cloud.google.com/storage/docs/troubleshooting#empty-obj) if you get a 301 HTTP response when attempting to access `http://www.example.com/dir/`.

The following table shows the content served for selected URLs:

URL Requested | Content Served | HTTP response code | http://www.example.com   
http://www.example.com/  
http://www.example.com/index.html | The object "index.html". | 200  
---|---|---  
http://www.example.com/hello | The object "404.html". | 404  
http://www.example.com/dir/index.html | The object "dir/index.html". | 200  
http://www.example.com/dir | A response with an empty body and a `Location` header that points to "dir/index.html". | 301  
http://www.example.com/dir/ | The object "dir/index.html", assuming no zero-byte object exists for /dir/ | 200  
A zero byte empty object, if it exists for /dir/. [See the Troubleshooting topic](https://docs.cloud.google.com/storage/docs/troubleshooting#empty-obj) for removing this zero byte object. | 301  
  
### Two-object bucket

Suppose a bucket named `www.example.com` has been configured as a website with the following settings and files:

  * `MainPageSuffix` = "main.html"
  * `NotFoundPage` = "404.html"
  * The bucket contains two publicly shared objects: "main.html" and "404.html".



The following table shows the content served for selected URLs:

URL Requested | Content Served | HTTP response code | http://www.example.com   
http://www.example.com/ | The object "main.html". | 200  
---|---|---  
http://www.example.com/index.html | The object "404.html". | 404  
  
If an object is shared publicly, you can also view that object with the URL: 
    
    
    http://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME

For example, the URL for an `index.html` object would be: 
    
    
    http://storage.googleapis.com/www.example.com/index.html

For more information about working with publicly accessible data, see [Accessing Public Data](https://docs.cloud.google.com/storage/docs/access-public-data).

## Tips for working with a bucket configured as a website

The following are some tips to keep in mind when using a bucket to host a static website.

### Add subdomains

Suppose you also want to serve content at `test.example.com`, from a different bucket than the one that serves content at `www.example.com`. To do so:

  1. [Create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to serve your additional content.

  2. If you followed the tutorial at [Hosting a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website) to serve your content over HTTPS, edit your load balancer in the [Google Cloud console](https://console.cloud.google.com/networking/loadbalancing) as follows:

     1. For **Backend configuration** , create a new backend bucket `test-bucket` by selecting the new bucket you created.
     2. For **Host and path rules** , add a new rule as follows: 
            
            Hosts                  Paths     Backends
            test.example.com       /*        test-bucket
            

     3. For **Frontend configuration** , add a new Frontend IP and port with the same values as your first configuration, with the following exceptions:

        * For **IP address** , create and reserve a new IP address.
        * For **Certificate** , create a new SSL certificate for `test.example.com`.
  3. After you update the load balancer, add a new `A` record to your domain registration service using the IP address of the new frontend configuration: 
         
         NAME                  TYPE     DATA
         test                  A        IP_ADDRESS
         


**Note:** If you are serving without a load balancer by using a `CNAME` redirect, your bucket name must match the subdomain `test.example.com`. In this scenario, because you already verified the domain `example.com`, you can create buckets to support subdomains without additional verification. Once you've created your new bucket, [add a new `CNAME` record](https://docs.cloud.google.com/storage/docs/hosting-static-website-http) for the subdomain: 
    
    
    NAME                  TYPE     DATA
    test                  CNAME    c.storage.googleapis.com.
    

### API behavior

The `MainPageSuffix` and `NotFoundPage` website configurations are only used for requests that come to Cloud Storage through a [`CNAME` or `A` redirect](https://docs.cloud.google.com/storage/docs/request-endpoints#custom-domains). For example, a request to `www.example.com` shows the index page, but an equivalent request to `storage.googleapis.com/www.example.com` does not.

Thus, API behavior for requests to Cloud Storage domains, such as `storage.googleapis.com/www.example.com`, is preserved. For example, you can continue to list objects in the `www.example.com` bucket as you would for any other bucket. In the case of the `www.example.com` bucket, the object listing you receive includes `404.html` and `index.html`.

### Host static assets for a dynamic website

You can use Cloud Storage to host static assets for a dynamic website that is hosted, for example, in [Google App Engine](https://docs.cloud.google.com/appengine) or in [Google Compute Engine](https://docs.cloud.google.com/compute). Some benefits of hosting your static assets, like images or JavaScript files, in a bucket include:

  * Cloud Storage behaves like a [Content Delivery Network (CDN)](https://wikipedia.org/wiki/Content_delivery_network) because publicly readable objects are cached in the Cloud Storage network by default.

  * Bandwidth charges for accessing content typically cost less with Cloud Storage.

  * The load on your web servers is lessened when serving the static content from Cloud Storage.




When hosting static assets for a dynamic website, you do not need to create DNS records and point to a bucket or load balancer as you do for a static website. For example, you could have a bucket named `www_example_com_assets` with appropriate assets configured as shared publicly and then access those assets using the Cloud Storage domain. For example, suppose you have the JavaScript file `library.js` in the bucket `www_example_com_assets` that is shared publicly, then you can access it as `http://storage.googleapis.com/www_example_com_assets/library.js`.

### Set cache parameters

You can control how or if your website assets are cached by configuring the [`Cache-Control` metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control). Generally, only set cache control metadata for objects that are accessible to all anonymous users, which is a requirement for any object served from a Cloud Storage bucket as part of a static website.

Cloud Storage applies a cache control setting of 3600 seconds to objects that are accessible to all anonymous users, unless you specify explicit cache control settings. See [Viewing and Editing Metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata) for instructions for setting object metadata, such as `Cache-Control`.

You can also use Cloud CDN to cache external HTTP(S) load balanced content close to your users, which often reduces serving costs. For more information, see [Caching](https://docs.cloud.google.com/storage/docs/caching).

### Monitor your charges

If you are serving assets from a bucket configured as a static website or serving static assets from a bucket for a dynamic website hosted outside of Cloud Storage, you should monitor the charges to your project containing the bucket. Serving content incurs Cloud Storage costs for storing the content, using the network, and performing retrieval operations. For details, see the [Cloud Storage Pricing page](https://docs.cloud.google.com/storage/pricing).

You may also incur networking charges if you use an external Application Load Balancer to set up HTTPS. See [Network Pricing](https://docs.cloud.google.com/vpc/network-pricing#lb) for more details.

The [simple pricing example](https://docs.cloud.google.com/storage/pricing-examples#simple) on the pricing examples page can be used as an approximation for the use case of a low-traffic, static website. Note, however, that the example does not account for charges associated with the external Application Load Balancer, which can often be the largest charge for static website hosting. You can use the [Pricing Calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

New Google Cloud users might be eligible for a [free trial](https://cloud.google.com/free/). 

If you are a current Google Cloud user, you can get a detailed breakdown of your project costs on the [billing page](https://console.cloud.google.com/billing).

### Troubleshooting

See [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#static-website) for common issues associated with using a bucket configured to serve static website content.

## What's next

  * [Try Google Cloud jump start solutions that use Cloud Storage](https://docs.cloud.google.com/architecture/storage).
  * [Learn about other web serving options](https://docs.cloud.google.com/solutions/web-serving-overview) on Google Cloud.



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
