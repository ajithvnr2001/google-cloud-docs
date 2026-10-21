---
url: https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/setting-up-https-ingress/
title: Set up HTTPS ingress \u00a0|\u00a0 Kf 2.10 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:43:37.726437+00:00
---

# Set up HTTPS ingress  |  Kf 2.10  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/setting-up-https-ingress/

Version 2.10

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
  * [ 2.10 ](https://docs.cloud.google.com/migrate/kf/docs/2.10)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.10/getting-started)



Send feedback 

#  Set up HTTPS ingress Stay organized with collections  Save and categorize content based on your preferences. 

You can secure the ingress gateway with HTTPS by using simple TLS, and enable HTTPS connections to specific webpages. In addition, you can redirect HTTP connections to HTTPS.

HTTPS creates a secure channel over an insecure network, protecting against man-in-the-middle attacks and encrypting traffic between the client and server. To prepare a web server to accept HTTPS connections, an administrator must create a public key certificate for the server. This certificate must be signed by a trusted certificate authority for a web browser to accept it without warning.

**Note:** These instructions supplement the Istio instructions to [configure a TLS ingress gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress), and assume that a valid certificate and private key for the server have already been created.

Edit the gateway named external-gateway in the `kf` namespace using the built-in Kubernetes editor:
    
    
    kubectl edit gateway -n kf external-gateway

  1. Assuming you have a certificate and key for your service, create a Kubernetes secret for the ingress gateway. Make sure the secret name does not begin with `istio` or `prometheus`. For this example, the secret is named `myapp-https-credential`.
  2. Under `servers:`
     1. Add a section for port 443.
     2. Under `tls:`, set the `credentialName` to the name of the secret you just created.
     3. Under `hosts:`, add the host name of the service you want to secure with HTTPS. This can be set to an entire domain using a wildcard (e.g. `*.example.com`) or scoped to just one hostname (e.g. `myapp.example.com`).
  3. There should already be a section under `servers:` for port 80 HTTP. Keep this section in the Gateway definition if you would like all traffic to come in as HTTP.
  4. To redirect HTTP to HTTPS, add the value `httpsRedirect: true` under `tls` in the HTTP server section. See the [Istio Gateway documentation](https://istio.io/latest/docs/reference/config/networking/gateway/) for reference. Note that adding this in the section where `hosts` is set to `*` means that **all** traffic is redirected to HTTPS. If you only want to redirect HTTP to HTTPS for a single app/domain, add a separate HTTP section specifying the redirect.



Shown below is an example of a Gateway `spec` that sets up HTTPS for `myapp.example.com` and redirects HTTP to HTTPS for that host:
    
    
    spec:
      selector:
        istio: ingressgateway
      servers:
      - hosts:
        - myapp.example.com
        port:
          name: https
          number: 443
          protocol: HTTPS
        tls:
          credentialName: myapp-https-credential
          mode: SIMPLE
      - hosts:
        - myapp.example.com
        port:
          name: http-my-app
          number: 80
          protocol: HTTP
        tls:
          httpsRedirect: true
      - hosts:
        - '*'
        port:
          name: http
          number: 80
          protocol: HTTP
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
