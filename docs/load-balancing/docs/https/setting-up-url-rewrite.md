---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-rewrite/
title: Set up URL rewrite for a classic Application Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:21.552854+00:00
---

# Set up URL rewrite for a classic Application Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-rewrite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up URL rewrite for a classic Application Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This example demonstrates rewriting the path specified in a request for a classic Application Load Balancer.

To configure traffic management for global external Application Load Balancers and regional external Application Load Balancers, see the following pages:

  * [Setting up traffic management for global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#rewrite-url)
  * [Setting up traffic management for regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#rewrite-url)



### Before you begin

  * Read about [URL rewrites](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management#rewrites).

  * Read about [URL maps in general](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) and [path matchers](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#pm-constraints) in particular.

  * The URL rewrite example assumes that you've already created your external Application Load Balancer following the steps outlined in [Setting up a load balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets).

That example leads you through the creation of two resources:

    * `http://IP_ADDRESS/never-fetch/three-cats.jpg`
    * `http://IP_ADDRESS/love-to-fetch/two-dogs.jpg`

Where `/never-fetch/three-cats.jpg` is stored in `/cats`, which is the default service, and `/love-to-fetch/two-dogs.jpg` is stored in `/dogs`.

At this point, the URL map looks like this:
    
    gcloud compute url-maps describe http-lb
    
    
    creationTimestamp: '2020-10-13T11:18:10.561-07:00'
    defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/cats
    fingerprint: MKfYsObzqgw=
    hostRules:
    - hosts:
      - '*'
      pathMatcher: path-matcher-1
    id: '1420501688756228493'
    kind: compute#urlMap
    name: test-bucket
    pathMatchers:
    - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/cats
      name: path-matcher-1
      pathRules:
      - paths:
        - /love-to-fetch/*
        service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/dogs
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/http-lb
    




### Modifying the URL map

**Important:** The rewrite is prepended to the path as is. Full path rewrites are not supported. External Application Load Balancers only implement path prefix rewrites. For example, you _can_ rewrite: `host.name/path1/resource1` to `host.name/path2/resource1`. You _cannot_ rewrite `host.name/path1/resource1` to `host.name/path1/resource2`.

In this example, you rewrite the `/love-to-fetch/` URL so that users can reach the `two-dogs.jpg` image with this simplified URL:

  * `http://IP_ADDRESS/two-dogs.jpg`



To do this, modify the load balancer's URL map as follows:

###  Console 

### Edit your load balancer

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/add)
  2. Click `http-lb`.
  3. Click **Edit** edit.
  4. Keep the window open to continue.



### Change the host and path rules

  1. In the left column of the screen, click **Host and path rules**.
  2. Select **Advanced host and path rule (URL redirect, URL rewrite)**.
  3. Click the row that contains the non-default path rule, in this case, the row that has an asterisk (`*`) for all hosts.
  4. Click the pencil icon edit for the `/love-to-fetch/* Route traffic to a single backend: dogs` row.
  5. Under **Paths** , delete `/love-to-fetch/*` and add `/*`.
  6. Under **Action** , select **Route traffic to a single backend**.
  7. Click **Add-on action (URL rewrite)**.
  8. Leave **Host rewrite** blank.
  9. Under **Path prefix rewrite** , enter `/love-to-fetch/`.
  10. Under **Backend** , select `dogs`.
  11. Click **Save**.
  12. Click **Done**. The new host and path rule looks as follows: 

Paths  | Action | Backend  
---|---|---  
Any unmatched (default) | Route traffic to a single backend | cats  
/* | Route traffic to a single backend | dogs  
  13. If everything looks correct, click **Update** to update your HTTP load balancer.




###  gcloud 

  1. Create a YAML file `/tmp/http-lb.yaml`, making sure to substitute PROJECT_ID with your project ID.

When a user requests path `/*`, the path gets rewritten in the backend to the actual location of the content, which is `/love-to-fetch/*`.
         
         defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/cats
         hostRules:
         - hosts:
           - '*'
           pathMatcher: path-matcher-1
         name: http-lb
         pathMatchers:
         - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/cats
           name: path-matcher-1
           pathRules:
           - paths:
             - /*
             routeAction:
               urlRewrite:
                 pathPrefixRewrite: /love-to-fetch/
             service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/dogs
         tests:
         - description: Test routing to backend bucket, dogs
           host: example.com
           path: /love-to-fetch/test
           service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/dogs
         

  2. Validate the URL map.
         
         gcloud compute url-maps validate --source /tmp/http-lb.yaml
         

If the tests pass and the command outputs a success message, save the changes to the URL map.

  3. Update the URL map.
         
         gcloud compute url-maps import http-lb \
            --source /tmp/http-lb.yaml \
            --global
         




### Testing

Note the IPv4 address that was reserved:
    
    
    gcloud compute addresses describe example-ip \
        --format="get(address)" \
        --global
    

After waiting several minutes for the changes to propagate, you can test this setup.

On the command line, run the following curl command:
    
    
    curl http://IP_ADDRESS/two-dogs.jpg
    

In a browser, open `http://IP_ADDRESS/two-dogs.jpg`.

## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
