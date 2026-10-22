---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/apache/apache-customizing-a-migration-plan/
title: Customize migration plan for Apache servers \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:25.470549+00:00
---

# Customize migration plan for Apache servers  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/apache/apache-customizing-a-migration-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customize migration plan for Apache servers

You should review the migration plan file that resulted from creating a migration. Customize the file before executing the migration. The details of your migration plan are used to extract the workload container artifacts from the source.

This document describes the contents of the migration and the kinds of customizations that you might consider before you execute the migration and generate deployment artifacts.

## Before you begin

This document assumes that you've already [created a migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and have the migration plan file.

## Edit the migration plan

After you have copied the file system and analyzed it, you can find the migration plan in the new directory that is created in the specified output path: ANALYSIS_OUTPUT_PATH/`config.yaml`.

Edit the migration plan as necessary and save the changes.

## Migration plan structure

The migration plan for Apache2 workloads has the following structure which you can customize, as described in the following sections.
    
    
    apacheServer:
      # Apache configuration for directories on the system
      # Content is the configuration as understood by apache
      directories:
      - Content: |-
          Options FollowSymLinks
          AllowOverride None
          Require all denied
        Path: /
      - Content: |-
          AllowOverride None
          Require all granted
        Path: /usr/share
      - Content: |-
          Options Indexes FollowSymLinks
          AllowOverride None
          Require all granted
        Path: /var/www/
      - Content: "#\tOptions Indexes FollowSymLinks\n#\tAllowOverride None\n#\tRequire
          all granted"
        Path: /srv/
      - Content: |-
          #   AllowOverride None
          #   Require all denied
        Path: /
      # Environment variables used by apache
      envVars:
      - Value: www-data
        Var: APACHE_RUN_USER
      - Value: www-data
        Var: APACHE_RUN_GROUP
      - Value: /var/run/apache2$SUFFIX/apache2.pid
        Var: APACHE_PID_FILE
      - Value: /var/run/apache2$SUFFIX
        Var: APACHE_RUN_DIR
      - Value: /var/lock/apache2$SUFFIX
        Var: APACHE_LOCK_DIR
      - Value: /var/log/apache2$SUFFIX
        Var: APACHE_LOG_DIR
      - Value: C
        Var: LANG
      # The port the service will listen on
      listen:
      - "80"
      - "443"
      # Apache modules to be loaded and installed
      loadModules:
      - Module: access_compat_module
      - Module: alias_module
      - Module: auth_basic_module
      - Module: authn_core_module
      - Module: authn_file_module
      - Module: authz_core_module
      - Module: authz_host_module
      - Module: authz_user_module
      - Module: autoindex_module
      - Module: deflate_module
      - Module: dir_module
      - Module: env_module
      - Module: filter_module
      - Module: mime_module
      - Module: mpm_prefork_module
      - Module: negotiation_module
      - Module: php7_module
      - Module: proxy_module
      - Module: proxy_fcgi_module
      - Module: reqtimeout_module
      - Module: rewrite_module
      - Module: setenvif_module
      - Module: socache_shmcb_module
      - Module: ssl_module
      - Module: status_module
      # The sites to be extracted
      virtualHosts:
      - address: '*:80'
        documentRoot: /var/www/html
        # should the site be enabled in extracted VM
        includeInContainerImage: true
        originalConfig: |-
          # The ServerName directive sets the request scheme, hostname and port that
          # the server uses to identify itself. This is used when creating
          # redirection URLs. In the context of virtual hosts, the ServerName
          # specifies what hostname must appear in the request's Host: header to
          # match this virtual host. For the default virtual host (this file) this
          # value is not decisive as it is used as a last resort host regardless.
          # However, you must set it for any further virtual host explicitly.
          #ServerName www.example.com
    
          ServerAdmin webmaster@localhost
          DocumentRoot /var/www/html
    
          # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
          # error, crit, alert, emerg.
          # It is also possible to configure the loglevel for particular
          # modules, e.g.
          #LogLevel info ssl:warn
    
          ErrorLog ${APACHE_LOG_DIR}/error.log
          CustomLog ${APACHE_LOG_DIR}/access.log combined
    
          # For most configuration files from conf-available/, which are
          # enabled or disabled at a global level, it is possible to
          # include a line for only one particular virtual host. For example the
          # following line enables the CGI configuration for this host only
          # after it has been globally disabled with "a2disconf".
          #Include conf-available/serve-cgi-bin.conf
        serverName: server-0
      - address: '*:443'
        # The location of the site content (will be copied to the same location the extracted container)
        documentRoot: /var/www/html
        includeInContainerImage: false
        originalConfig: |-
          ServerAdmin admin@example.com
          DocumentRoot /var/www/html
          SSLEngine on
          SSLCertificateFile /etc/ssl/certs/c2d-temporary-self-signed-cert.pem
          SSLCertificateKeyFile /etc/ssl/private/c2d-temporary-self-signed-cert.key
    
          <Directory /var/www/html>
          Options -Indexes
          AllowOverride FileInfo
          </Directory>
        serverName: server-1
    php:
      # list of php modules to be installed in the extracted container (add/remove entries to change what will be installed)
      modules:
      - calendar
      - ctype
      - curl
      - exif
      - ffi
      - fileinfo
      - filter
      - gd
      - gettext
      - iconv
      - json
      - mysqli
      - pcntl
      - pdo
      - pdo_mysql
      - posix
      - shmop
      - sockets
      - sysvmsg
      - sysvsem
      - sysvshm
      - tokenizer
      - xsl
    

### Configure security policies on directories

In the `directories` section, you can apply specific configurations to enforce security policies on certain directories. To fill in and edit this section of the plan, use the syntax for the [`Directory` directive](https://httpd.apache.org/docs/2.4/mod/core.html#directory).

### Load and install modules

In the `loadModules` section, you can specify the modules that you want to load and install. Migrate to Containers automatically detects the required modules by scanning the original configuration for the [`LoadModule` directive](https://httpd.apache.org/docs/2.4/mod/mod_so.html#loadmodule).

#### Supported Modules
    
    
    access_compat_module
    alias_module
    auth_basic_module
    authn_core_module
    authn_file_module
    authz_core_module
    authz_host_module
    authz_user_module
    autoindex_module
    deflate_module
    dir_module
    env_module
    expires_module
    filter_module
    mime_module
    mpm_prefork_module
    negotiation_module
    php7_module
    proxy_fcgi_module
    proxy_module
    remoteip_module
    reqtimeout_module
    rewrite_module
    setenvif_module
    socache_shmcb_module
    ssl_module
    status_module
    

**Note:** Including unknown modules in your migration plan causes the migration to fail with an error message that specifies the unknown modules.

### Specify and configure virtual hosts

In the `virtualHosts` section, Migrate to Containers copies all the directives enclosed in a [`<VirtualHost>` and `</VirtualHost>` block](https://httpd.apache.org/docs/2.4/mod/core.html#virtualhost).

In the `address` field, the IP address of the site is replaced with `*`.

Under `originalConfig`, the `DocumentRoot` field specifies the path from which Apache serves the requested files. For each path specified in `DocumentRoot`, Migrate to Containers does the following:

  * It compresses each path a separate tar file.
  * It copies the tar file in the artifacts for extraction.
  * It changes the permissions for the user in the Docker image with the `ADD --chown` option in the Dockerfile.



### Review the PHP extensions

Migrate to Containers automatically detects the PHP modules installed in your VM and includes them under the `php` section of the migration plan. Review this section and add or remove modules as needed.

## What's next

  * Learn how to [execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
