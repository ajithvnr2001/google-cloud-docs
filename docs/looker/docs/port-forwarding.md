---
url: https://docs.cloud.google.com/looker/docs/port-forwarding/
title: Port forwarding for a cleaner URL \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:36:51.854782+00:00
---

# Port forwarding for a cleaner URL  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/port-forwarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Port forwarding for a cleaner URL Stay organized with collections  Save and categorize content based on your preferences. 

By default, HTTPS assumes that the port will be 443. This means that `https://looker.yourdomain.com` would automatically be handled as though the user had typed `https://looker.yourdomain.com:443`. However, using the standard HTTPS port (443) would require running Looker as root, which is unsupported and not recommended.

One option is to have users specify a port number as part of the URL when they access Looker. For example, if you are using port 9999, then they would type: `https://looker.yourdomain.com:9999`.

On customer-hosted instances, for your users' convenience, we recommend setting up a different default port so they can type `https://looker.yourdomain.com` and still get to the correct port. You can set up a default port for Looker or redirect traffic to a different port using several methods:

  * Use the `--port=<i>` Looker startup option to specify the desired port, such as `--port=9999`. This option is discussed on the [Looker startup options](https://docs.cloud.google.com/looker/docs/startup-options) documentation page.
  * Create a script that uses `iptables`.
  * Use `xinetd`.
  * Use a Nginx reverse proxy server.
  * Use a load balancer.



> Note that it is better to forward packets directly to Looker, rather than indirectly (through a web proxy), because Looker has functionality to stop a database query when it detects that the browser has canceled a request.

## iptables on the Looker host

Looker can be accessed from a different port by using iptables. The following script will forward traffic from port 443 to 9999. It was written for Ubuntu Linux and might need to be modified if you are running a different Linux distribution.

  1. Create the script file:
         
         /etc/network/if-up.d/looker-https-forward
         

  2. Add these contents to the file:
         
         #!/bin/sh
         # Forward HTTPS traffic to the Looker app
         iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 9999
         

  3. Make it executable:
         
         sudo chmod 755 /etc/network/if-up.d/looker-https-forward
         

  4. Run the script, which will automatically run on the next system or network restart:
         
         sudo /etc/network/if-up.d/looker-https-forward
         




## xinetd on the Looker host

Another technique involves using xinetd.

  1. Make sure xinetd allows incoming traffic from all desired addresses. In the default section of **/etc/xinetd.conf** add:
         
         {
         only_from = 0.0.0.0
         # or replace 0.0.0.0 with an IP range
         # (i.e., 128.0.0.0/16) if desired
         }
         

  2. Create a file named: `/etc/xinetd.d/lookerhttps`

  3. Add these contents to the file:
         
         # default: on
         # description: Redirect HTTPS/443 requests to
         # Looker default port 9999
         service https
         {
         disable = no
         id = lookerhttps
         socket_type = stream
         protocol = tcp
         user = root
         wait = no
         redirect = 127.0.0.1 9999
         }
         




## Reverse proxy servers

It is possible to use reverse proxies with Looker. Our suggested reverse proxy server is Nginx. It is the only reverse proxy we test and fully support, although we don't necessarily prohibit other options. You can find a sample Nginx configuration on the [Sample Nginx configuration](https://docs.cloud.google.com/looker/docs/sample-nginx-configuration) documentation page.

> Note that the Apache reverse proxy has [a bug](https://bz.apache.org/bugzilla/show_bug.cgi?id=50807) in it that prevents Looker from being able to properly close connections. This means that every database query will run to completion, even if a user cancels it. For this reason, you should avoid using the Apache reverse proxy with Looker.

## Load balancer

There are many load balancers solutions available. From a high level, the load balancer would be configured to listen on port 443 and forward all requests to Looker on port 9999. In this case, your SSL server certificates would be installed on the load balancer.

## Next steps

After you have configured port forwarding, you're ready to [allow Looker Support to access your deployment](https://docs.cloud.google.com/looker/docs/support-access-customer-hosted-deployment).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
