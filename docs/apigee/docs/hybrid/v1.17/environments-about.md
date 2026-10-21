---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environments-about/
title: About environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:49.043810+00:00
---

# About environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environments-about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  About environments Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environments-about.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/environments-about.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/environments-about.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/environments-about.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environments-about.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/environments-about.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/environments-about.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/environments-about.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/environments-about.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/environments-about.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/environments-about.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/environments-about.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/environments-about.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/environments-about.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/environments-about.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/environments-about.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/environments-about.html)



An _environment_ provides an isolated context or "sandbox" for running API proxies. In a single organization, you can create multiple environments.

The following code shows an example override configuration where multiple environments are defined. 
    
    
    namespace: my-namespace
    org: my-organization
    ...
    envs:
      - name: test
        serviceAccountPaths:
          synchronizer: "your_keypath/synchronizer-manager-service-account.json
          udca: "your_keypath/analytic-agent-service-account.json
    
    
      - name: prod
        serviceAccountPaths:
          synchronizer: "your_keypath/synchronizer-manager-service-account.json
          udca: "your_keypath/analytic-agent-service-account.json
    ...

**Note:** See: 

  * [` namespace `](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#namespace)
  * [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#org)
  * [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-name)
  * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-serviceaccountpaths-synchronizer)
  * [`envs[].serviceAccountPaths.udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-saactpaths-udca)



Suppose a proxy with the base path `/foo1` is deployed to environment **test**. You could call the proxy like this: 
    
    
    curl -k https://api.example.com/foo1

When this call hits the ingress, the ingress knows to send it to the message processor associated with the `test` environment, which handles the request. 

Similarly, if `foo1` is also deployed to the `prod` environment, you could make a proxy request like this, to the host alias `apiprod.mydomain.net`: 
    
    
    curl -k https://apiprod.example.com/foo1

And the call is routed by the ingress to the MP associated with that host. 

**NOTE** On a request to an API proxy, the ingress compares the `Host` header of the incoming request to the list of host aliases to determine which virtual host handles the request. `curl` commands, browsers, and many other utilities automatically set the `Host` header with the domain of the request. If for any reason your app is not setting the `Host` header automatically, you must set it manually. 

**Antipattern** : Deploy all of your proxies to one hybrid environment. 

**Best practice** : Create multiple environments and deploy a limited number of proxies to each one. 

##  Limit the number of proxy deployments 

For hybrid, the fact that many environments can share the same virtual hosts as defined in environment groups means that you must think carefully about how you manage your proxy deployments to any given environment. In hybrid, the best practice is to create multiple environments and deploy a limited number of proxies to each one. 

**How many proxies should you deploy to an environment?** There is not a set answer to this question; however, the following table provides general guidance on why it's a good idea to limit the number of proxies deployed to each environment and what you need to think about when managing proxy deployments: 

**NOTE:** When deciding how many proxies to deploy to an environment, be sure to consider the product configuration limits described in [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#hybrid).Issue to consider | Description  
---|---  
Message processor boot-up time  |  There is a direct correlation between the amount of time a message processor (MP) takes to boot up and the number of proxies deployed to that MP. In an auto-scaling Kubernetes environment, an increase in boot time might be a problem. The more proxies that are deployed to the MP, the longer it will take for that MP to come up if it needs to be scaled or recreated.   
Scaling performance  |  If you have several proxies deployed to an environment, and one of the proxies gets a lot of traffic so that it frequently auto-scales, all of the proxies in that environment will scale with it. The performance effect of scaling multiple proxies with a single high-traffic proxy might be a problem.   
Noisy neighbor  |  If you have several proxies deployed to the same environment, and one proxy crashes, then all of the proxies in the environment will be taken down while the MPs restart. By limiting the number of proxies deployed to an environment, you minimize the impact of a single proxy crashing.   
  
##  Environment groups and virtualhosts 

[Environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) allow you to group environments together. Environments within each group share the same hostnames. You can group environments by function, by hostname address, by region if you are implementing a multi-region hybrid installation, or by any other metric you choose.

Because routing is managed by the combination of environment group hostnames, API proxy base paths, and environments, each virtual host only needs to list the name of the environment group and any appropriate certs. 

The following code shows an example override configuration where multiple virtualhosts are defined. Note that name of the virtualhosts must be the names of the environment groups. 
    
    
    gcp:
      region: us-central1
      projectID: hybrid-example
    
    
    k8sCluster:
      name: apigee-hybrid
      region: us-central1
    
    
    org: hybrid-example
    
    contractProvider: https://us-apigee.googleapis.com # if using [data residency](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/using-data-residency-with-apigee-hybrid)
    
    instanceID: "my_hybrid_example"
    
    
    virtualhosts:
      - name: group-1  # the name of an environment group
        sslCertPath: ./certs/keystore.pem
        sslKeyPath: ./certs/keystore.key
    
    virtualhosts:
      - name: group-2
        sslCertPath: ./certs/keystore.pem
        sslKeyPath: ./certs/keystore.key
    ...

**Note:** See 

  * [gcp-projectID](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-projectid).
  * [k8scluster-name](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#k8scluster-name).
  * [k8scluster-region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#k8scluster-region).
  * [instanceid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#instanceid).



##  Additional resources 

  * [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview)
  * [Managing environments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with)
  * [Managing environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with)
  * [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs)
  * [Configure virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/base-path-routing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
