---
url: https://docs.cloud.google.com/migrate/kf/docs/2.2/how-to/routes-and-domains/
title: Routes and Domains \u00a0|\u00a0 Kf 2.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:21.885241+00:00
---

# Routes and Domains  |  Kf 2.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.2/how-to/routes-and-domains/

Version 2.2

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.2 ](https://docs.cloud.google.com/migrate/kf/docs/2.2)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.2/getting-started)



Send feedback 

#  Routes and Domains Stay organized with collections  Save and categorize content based on your preferences. 

Some Apps are useful without being accessible outside the cluster, but most need to be available outside of the cluster on one or more HTTP endpoints. In Kf, this is the job of Routes.

By default, each App is accessible to other processes in the cluster using the cluster internal App address: `app-name.space-name`. You can use this address when you deploy one or more Apps in a cluster that need to communicate with one another; they allow traffic to go directly from one App to another rather than out of the cluster and back. This makes communications more secure, faster, and guaranteed to use the service in the local cluster.

If your App needs to be accessible from outside of the cluster, you'll need to create Routes for it.

## The cluster-internal domain

The cluster-internal domain for each App has some special characteristics.

  * Using it in your Apps allows [East-West](https://en.wikipedia.org/wiki/East-west_traffic) (point to point) routing.
  * Traffic sent to it is load-balanced between running App Pods.
  * You can connect to non-HTTP endpoints using the internal domain.



Routes allow you to create vanity URLs on top of the cluster-internal domain.

### App load balancing

Traffic is routed by Istio to healthy instances of an App using a [round-robin](https://en.wikipedia.org/wiki/Round-robin_DNS) policy. Currently, this policy can't be changed.

## Route capabilities

Routes tell the cluster's ingress gateway where to deliver traffic and what to do if no Apps are available on the given address. By default, if no App is available on a Route and the Route receives a request it returns an [HTTP 503 status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503).

Routes are comprised of three parts: host, domain, and path. For example, in the URI `payroll.mydatacenter.example.com/login`:

  * The host is `payroll`
  * The domain is `mydatacenter.example.com`
  * The path is `/login`



Routes _must_ contain a host and domain, but the path is optional. Multiple Routes can share the same host and domain if they specify different paths. Multiple Apps can share the same Route and traffic will be split between them. This is useful if you need to support legacy blue/green deployments. If multiple Apps are bound to different paths, the priority is longest to shortest path.

**Warning:** Kf doesn't currently support TCP port-based routing. You must use a [Kubernetes LoadBalancer](https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/) if you want to expose a TCP port to the Internet. Ports are available on the cluster internal App address `<app-name>.<space>`.

## Using Routes

The following sections describe how to use the `kf` CLI to manage Routes.

### List Routes

Developers can list Routes for the current Space using the `kf routes` command.
    
    
    $ kf routes
    Getting Routes in Space: my-space
    Found 2 Routes in Space my-space
    
    HOST    DOMAIN       PATH    APPS
    echo    example.com  /       echo
    *       example.com  /login  uaa
    

### Create Route

Developers can create Routes using the `kf create-route` command.
    
    
    # Create a Route in the targeted Space to match traffic for myapp.example.com/*
    $ kf create-route example.com --hostname myapp
    
    # Create a Route in the Space myspace to match traffic for myapp.example.com/*
    $ kf create-route -n myspace example.com --hostname myapp
    
    # Create a Route in the targeted Space to match traffic for myapp.example.com/mypath*
    $ kf create-route example.com --hostname myapp --path /mypath
    
    # You can also supply the Space name as the first parameter if you have
    # scripts that rely on the old cf style API.
    $ kf create-route myspace example.com --hostname myapp # myapp.example.com
    

After a Route is created, if no Apps are bound to it then an [HTTP 503 status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) is returned for any matching requests.

**Note:** Routes that share the same host and domain must be in the same Space.

### Map a Route to your App

Developers can make their App accessible on a Route using the `kf map-route` command.
    
    
    $ kf map-route MYAPP mycluster.example.com --host myapp --path mypath
    

**Note:** `map-route` creates the Route if it doesn't exist yet.

### Unmap a Route

Developers can remove their App from being accessible on a Route using the `kf unmap-route` command.
    
    
    $ kf unmap-route MYAPP mycluster.example.com --host myapp --path mypath
    

### Delete a Route

Developers can delete a Route using the `kf delete-route` command.
    
    
    $ kf delete-route mycluster.example.com --host myapp --path mypath
    

Deleting a Route will stop traffic from being routed to all Apps listening on the Route.

### Declarative Routes in your App manifest

Routes can be managed declaratively in your App manifest file. They will be created if they do not yet exist.
    
    
    ---
    applications:
    - name: my-app
      # ...
      routes:
      - route: example.com
      - route: www.example.com/path
    

You can read more about the supported route properties in the [manifest documentation](https://docs.cloud.google.com/migrate/kf/docs/2.2/how-to/manifest).

**Note:** Declaring Routes in your manifest file only creates new Routes, it does not delete Routes you created manually or as part of a previous push.

## Advanced topics

### Routing CRDs

There are four types that are relevant to routing:

  * VirtualService
  * Route
  * Service
  * App



Each App has a Service, which is an abstract name given to all running instances of your App. The name of the Service is the same as the App. A Route represents a single external URL. Routes constantly watch for changes to Apps, when an App requests to be added to a Route, the Route updates its list of Apps and then the VirtualService. A VirtualService represents a single domain and merges a list of all Routes in a Space that belong to that domain.

Istio reads the configuration on VirtualServices to determine how to route traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
