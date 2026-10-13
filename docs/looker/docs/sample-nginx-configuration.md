---
url: https://docs.cloud.google.com/looker/docs/sample-nginx-configuration/
title: Sample Nginx configuration \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:00.064918+00:00
---

# Sample Nginx configuration  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/sample-nginx-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Sample Nginx configuration Stay organized with collections  Save and categorize content based on your preferences. 

[Nginx](http://nginx.com/) is a popular web and reverse proxy server.

It can be used as a layer between Looker and end users in order to change the port that web browsers use to access Looker. By default users must use a URL similar to **https://hostname.domain.com:9999**. Using an Nginx configuration similar to the one on this page, users can access Looker without the port number, like **https://hostname.domain.com**. This is easier for users to type and remember, and is generally more convenient.

A sample `nginx.conf` is included here. It will need to be customized for your environment.
    
    
    user www-data;
    worker_processes 4;
    pid /var/run/nginx.pid;
    
    events {
      worker_connections 768;
      # multi_accept on;
    }
    
    http {
    
      ##
      # Basic Settings
      ##
    
      sendfile on;
      tcp_nopush on;
      tcp_nodelay on;
      keepalive_timeout 65;
      types_hash_max_size 2048;
      large_client_header_buffers 6 32k;
      client_max_body_size 100m;
    
      # server_names_hash_bucket_size 64;
      # server_name_in_redirect off;
      include /etc/nginx/mime.types;
      default_type application/octet-stream;
    
      ##
      # Logging Settings
      ##
      access_log /var/log/nginx/access.log;
      error_log /var/log/nginx/error.log debug; # change from debug to warn or error for production
    
      ##
      # Gzip Settings
      ##
      gzip on;
      gzip_disable "msie6";
    
      ##
      # Virtual Host Configs
      ##
    
      include /etc/nginx/conf.d/*.conf;
      include /etc/nginx/sites-enabled/*;
    
      server {
        listen                     443;
        ssl                        on;
        ssl_certificate            /etc/looker/ssl/certs/self-ssl.crt;
                                     # replace with your cert file
        ssl_certificate_key        /etc/looker/ssl/private/self-ssl.key;
                                     # replace with your key file
        ssl_protocols              TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers                RC4:HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;
        ssl_session_cache          shared:SSL:10m;
        ssl_session_timeout        10m;
    
        location / {
          proxy_pass https://looker.domain.com:9999; # Replace looker.domain.com with the name
                                                     # that clients will use to access Looker
    
          ### Force timeouts if one of backend hosts is dead ###
          proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    
          ### Set headers ###
          proxy_set_header          X-Real-IP $remote_addr;
          proxy_set_header          Accept-Encoding "";
          proxy_set_header          Host $http_host;
          proxy_set_header          X-Forwarded-For $proxy_add_x_forwarded_for;
    
          ### Don't timeout waiting for long queries - timeout is 1 hr ###
          proxy_read_timeout        3600;
          proxy_set_header          X-Forwarded-Proto $scheme;
    
          ### By default we don't want to redirect ###
          proxy_redirect            off;
    
          proxy_buffer_size         128k;
          proxy_buffers             4 256k;
          proxy_busy_buffers_size   256k;
        }
      }
    
      server {
        listen                     19999;
        ssl                        on;
        ssl_certificate            /etc/looker/ssl/certs/self-ssl.crt;
                                     # replace with your cert file
        ssl_certificate_key        /etc/looker/ssl/private/self-ssl.key;
                                     # replace with your key file
        ssl_protocols              TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers                RC4:HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;
        ssl_session_cache          shared:SSL:10m;
        ssl_session_timeout        10m;
    
        location / {
          proxy_pass https://looker.domain.com:19999; # Replace looker.domain.com with the name
                                                      # that clients will use to access Looker
    
          ### Force timeouts if one of backend hosts is dead ###
          proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    
          ### Set headers ###
          proxy_set_header          X-Real-IP $remote_addr;
          proxy_set_header          Accept-Encoding "";
          proxy_set_header          Host $http_host;
          proxy_set_header          X-Forwarded-For $proxy_add_x_forwarded_for;
    
          ### Don't timeout waiting for long queries - timeout is 1 hr ###
          proxy_read_timeout        3600;
          proxy_set_header          X-Forwarded-Proto $scheme;
    
          ### By default we don't want to redirect ###
          proxy_redirect            off;
    
          proxy_buffer_size         128k;
          proxy_buffers             4 256k;
          proxy_busy_buffers_size   256k;
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
