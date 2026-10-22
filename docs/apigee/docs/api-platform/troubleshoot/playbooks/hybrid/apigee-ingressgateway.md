---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-ingressgateway/
title: Apigee ingress gateway pods show 1 of 2 containers running \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:23.068127+00:00
---

# Apigee ingress gateway pods show 1 of 2 containers running  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-ingressgateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Apigee ingress gateway pods show 1 of 2 containers running Stay organized with collections  Save and categorize content based on your preferences. 

## Symptom

Your `apigee-ingressgateway` pods show only 1 of 2 containers running when you get the pod listing.

For example, when you run the following command:
    
    
    kubectl -n apigee get pods -l app=apigee-ingressgateway
    

Output:
    
    
    NAME                                                             READY   STATUS    RESTARTS   AGE
    apigee-ingressgateway-ext-ingress-myorg-hyb-8f2c412-shl9r         1/2     Running      0      6m48s
    apigee-ingressgateway-ext-ingress-myorg-hyb-8f2c412-vvzsf         1/2     Running      0      123m
    

Additionally, performing a `describe` command on one of the above pods will show the readiness probe failing with a 503 status code.

For example, in the `Events` section of the pod description, you might see the following message:
    
    
    Events:
      Type     Reason     Age                    From     Message
      ----     ------     ----                   ----     -------
      Warning  Unhealthy  76s (x32903 over 18h)  kubelet  Readiness probe failed: HTTP probe failed with statuscode: 503

## Possible cause

Cause | Description  
---|---  
Apigee ingress is configured to listen on port 80 | Apigee ingress configuration on port 80 is no longer supported starting with Apigee Hybrid 1.9.  
  
### Cause: Apigee ingress is configured to listen on port 80

This issue is caused by the Apigee ingress gateway being configured to listen on port 80, which is no longer supported starting with Apigee Hybrid 1.9.

This can happen if you upgraded from an earlier version of Apigee Hybrid that allowed port 80, or if there's another misconfiguration that enabled it.

#### Diagnosis

  1. Get a listing of your `apigee-ingressgateway` pods.

Run the following command:
         
         kubectl -n apigee get pods -l app=apigee-ingressgateway

Sample output
         
         NAME                                                              READY   STATUS    RESTARTS   AGE
         apigee-ingressgateway-ext-ingress-myorg-hyb-8f2c412-shl9r         1/2     Running   0          6m48s
         apigee-ingressgateway-ext-ingress-myorg-hyb-8f2c412-vvzsf         1/2     Running   0          123m
         

  2. Describe one of the listed pods to check the events: 
         
         kubectl -n apigee describe pod APIGEE_INGRESSGATEWAY_POD

Where APIGEE_INGRESSGATEWAY_POD is an `apigee-ingressgateway` pod listed in the previous command output.

Sample output:
         
         Events:
           Type     Reason     Age                    From     Message
           ----     ------     ----                   ----     -------
           Warning  Unhealthy  76s (x32903 over 18h)  kubelet  Readiness probe failed: HTTP probe failed with statuscode: 503
         

  3. Get the logs for the APIGEE_INGRESSGATEWAY_POD pod. 
         
         kubectl -n apigee logs APIGEE_INGRESSGATEWAY_POD

You may see a log entry showing that port 80 failed to bind due to a permission denied error followed by a message that envoy is not ready.
         
         2025-09-11T06:16:45.457621Z     error   envoy config external/envoy/source/common/listener_manager/listener_manager_impl.cc:1186        listener '0.0.0.0_80' failed to bind or apply socket options: cannot bind '0.0.0.0:80': Permission denied
         ...
         2025-09-11T06:16:46.365818Z     warn    Envoy proxy is NOT ready: config received from XDS server, but was rejected: cds updates: 1 successful, 0 rejected; lds updates: 0 successful, 1 rejected
         

  4. Review the current `apigeeroute` configuration to find the one that has port 80 (HTTP) enabled. 
     * Get a list of the defined apigee routes. 
           
           kubectl -n apigee get apigeeroute

Sample output:
           
           NAME                                  STATE     AGE
           myorg-hyb-dev-grp-000-33620d0         running   2d1h
           non-sni                               running   17s
           

     * Check each `apigeeroute` for where port 80 is defined. 

Run the following command for each `apigeeroute` listed in the previous command output:
           
           kubectl -n apigee get apigeeroute APIGEE_ROUTE_NAME -o yaml

Where APIGEE_ROUTE_NAME is the name of an individual `apigeeroute`.

Sample Command:
           
           kubectl -n apigee get apigeeroute non-sni -o yaml
                 

Sample output:
           
           apiVersion: apigee.cloud.google.com/v1alpha2
                 kind: ApigeeRoute
                 metadata:
                   name: non-sni
                   namespace: apigee
                   resourceVersion: "240441468"
                 spec:
                   enableNonSniClient: true
                   hostnames:
                   - '*'
                 ports:
                   - number: 443
                     protocol: HTTPS
                     tls:
                       credentialName: myorg-hyb-dev-grp
                       minProtocolVersion: TLS_AUTO
                       mode: SIMPLE
                   - number: 80
                     protocol: HTTP
                 selector:
                   app: apigee-ingressgateway
                 status:
                   lastAppliedGeneration: 1
                   state: running
                 

The non-sni `apigeeroute` shows that port 80 is enabled as part of this route. 



### Resolution

To resolve this issue, disable port 80 in the original `apigeeroute` yaml file by removing the following lines.
    
    
      - number: 80
        protocol: HTTP
          

If you do not have the original `apigeeroute` yaml file, you can follow the following steps:

  1. Export the current configuration with the following command: 
         
         kubectl -n apigee get apigeeroute APIGEE_ROUTE_NAME -o yaml > APIGEE_ROUTE_FILENAME.yaml

Where APIGEE_ROUTE_NAME is the `apigeeroute` being updated to remove the port 80 configuration.

Where APIGEE_ROUTE_FILENAME is the output file name containing the `apigeeroute` yaml content.

  2. Edit the `apigeeroute` yaml file to remove the port 80 configuration. 

Open the APIGEE_ROUTE_FILENAME file in a text editor and remove the following lines:
         
         - number: 80
                   protocol: HTTP
                     

  3. Replace the existing `apigeeroute` with the modified YAML file: 
         
         kubectl -n apigee replace -f APIGEE_ROUTE_FILENAME.yaml
         

Where APIGEE_ROUTE_FILENAME is the output file containing the updated `apigeeroute` configuration.

  4. The `apigee-ingressgateway` pods should now run with 2/2 containers. If they do not, delete the pods to allow new ones to be created automatically. 
         
         NAME                                                              READY   STATUS    RESTARTS   AGE
                 apigee-ingressgateway-ext-ingress-myorg-hyb-8f2c412-shl9r         2/2     Running   0          25h
                 apigee-ingressgateway-ext-ingress-myorg-hyb-8f2c412-vvzsf         2/2     Running   0          26h
                 




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support): 

  * Overrides.yaml
  * Output of the following commands: 
    * kubectl -n apigee get pods -l app=apigee-ingressgateway

    * kubectl -n apigee logs APIGEE_INGRESSGATEWAY_POD

    * kubectl -n apigee get apigeeroutes

    * For each of the stated routes, run: 
          
          kubectl -n apigee get apigeeroute APIGEE_ROUTE_NAME -o yaml

  * As an alternative, you may run and provide the [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather) information. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
